"""classify_eobs.py — match each EOB in Health_Bills/EOB/ to a provider
folder under Health_Bills/providers/, route off-patient EOBs to a
separate not_for_me/ folder, and leave unmatched ones in EOB/unmatched/.

Workflow:
1. Hash dedup pass. Files with identical SHA-256 are moved to
   EOB/_duplicates/, keeping the lexicographically-first filename in
   place. No API calls happen for duplicates.
2. For each unique EOB, vision-classify via Azure OpenAI gpt-5.2 and
   extract: patient first/last name, provider name, insurer name, date
   of service, claim number, total charges, patient responsibility, and
   a snake_case contents_summary.
3. Route the file:
   - patient is NOT Jonathan Bowker → EOB/not_for_me/<renamed>
   - provider matches an existing providers/<slug>/ folder (via alias
     map or fuzzy match) → providers/<slug>/<renamed>
   - else → EOB/unmatched/<renamed>
4. Rename per file_management v1.1: `<contents_summary>_eob_medical_<YYYY>_<MM>_v<N>.pdf`
   (or `_other_<…>` for non-medical EOBs, though most should be medical).

Usage:
    python classify_eobs.py
    python classify_eobs.py --dry-run
"""

from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import json
import os
import re
import shutil
import sys
import traceback
from pathlib import Path

import fitz  # PyMuPDF

ENV_FILE = Path(r"C:\Code\projects\ai-toolkit\.env")
HEALTH_ROOT = Path(r"D:\Proton Drive\My files\Financial\Health_Bills")
DEFAULT_EOB_DIR = HEALTH_ROOT / "EOB"
DEFAULT_PROVIDERS = HEALTH_ROOT / "providers"
DEFAULT_LOG_DIR = Path(r"C:\Code_data\medbill-dispute-kit\tracker")

MAX_PAGES = 10
RENDER_DPI = 120
JPEG_QUALITY = 80

# Patient identity — anything that looks like Jonathan Bowker counts as the
# subscriber's own EOB. Anything else (other Bowker first name, or no
# Bowker at all) routes to not_for_me/.
JON_FIRST_NAMES = {"jonathan", "jon", "johnathan", "john", "j"}
LAST_NAME = "bowker"

# Provider aliases — same intent as classify_rename_medical_bills.py, but
# expanded to cover the existing folder names under providers/.
PROVIDER_ALIASES: list[tuple[re.Pattern, str]] = [
    (re.compile(r"tristar|southern\s*hills\s*(med|medical)"),
     "tristar_southern_hills_medical_center"),
    (re.compile(r"labcorp|laboratory\s+corporation"), "labcorp"),
    (re.compile(r"premier\s+radiology"), "premier_radiology"),
    (re.compile(r"centennial\s+heart"), "tristar_southern_hills_medical_center"),
    (re.compile(r"hospital\s+medicine\s+services"),
     "hospital_medicine_services_of_tn"),
    (re.compile(r"emergency\s+medicine\s+services"),
     "emergency_medicine_services_of_tn"),
    (re.compile(r"radiology\s+alliance"), "radiology_alliance"),
    (re.compile(r"quantum\s+radiology"), "quantum_radiology"),
    (re.compile(r"anova\s+medical"), "anova_medical_associates"),
    (re.compile(r"wellstar"), "wellstar_health_system"),
    (re.compile(r"ascension\s+saint\s+thomas|^ascension"), "ascension"),
    (re.compile(r"^humana"), "humana"),
    (re.compile(r"^optum"), "optum"),
    (re.compile(r"sage\s+dental"), "sage_dental_of_franklin"),
    (re.compile(r"tenncare"), "state_of_tennessee_division_of_tenncare"),
]

SYSTEM_PROMPT = """\
You are reading a US health-insurance Explanation of Benefits (EOB).
Extract these fields and return JSON only:

{
  "patient_first_name": "first name of the patient (the person who got the service), or null",
  "patient_last_name": "last name of the patient, or null",
  "subscriber_name": "name of the plan subscriber if shown and different from patient, else null",
  "insurance_carrier": "issuing insurance plan name (e.g. United Healthcare, BCBS, Humana, Optum, Aetna)",
  "provider_name": "name of the provider (doctor, facility, lab) whose service this EOB covers",
  "facility_name": "facility where the service occurred if shown, else null",
  "date_of_service": "YYYY-MM-DD or null",
  "claim_number": "the EOB's claim number / reference number, or null",
  "total_charges": 250.00,
  "allowed_amount": 100.00,
  "insurance_paid": 75.00,
  "patient_responsibility": 25.00,
  "contents_summary": "snake_case, ≤40 chars, lead with provider slug then 'eob', e.g. quantum_radiology_eob",
  "document_type": "eob",
  "notes": "one short sentence describing the service and outcome"
}

Rules:
- Use null for any field that is not visible. Do not guess.
- `contents_summary`: lowercase, underscores between words, 5–40 chars,
  lead with the provider's name in snake_case then "_eob".
  Examples: "quantum_radiology_eob", "labcorp_eob", "tristar_southern_hills_eob".
- `total_charges`, `allowed_amount`, `insurance_paid`, `patient_responsibility`
  are plain USD numbers (no $).
- Respond with JSON only. No markdown fences, no commentary.
"""


def load_env(env_path: Path) -> None:
    if not env_path.exists():
        sys.exit(f"[fatal] env file not found at {env_path}")
    for ln in env_path.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#") or "=" not in ln:
            continue
        k, _, v = ln.partition("=")
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


def make_client():
    from openai import OpenAI
    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"].rstrip("/")
    return (
        OpenAI(
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
            base_url=endpoint + "/openai/v1/",
        ),
        os.environ["AZURE_OPENAI_DEPLOYMENT"],
    )


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def render_pdf_pages(pdf_path: Path) -> list[bytes]:
    doc = fitz.open(str(pdf_path))
    pages: list[bytes] = []
    zoom = RENDER_DPI / 72.0
    mat = fitz.Matrix(zoom, zoom)
    for page in doc:
        pix = page.get_pixmap(matrix=mat)
        pages.append(pix.tobytes("jpeg", jpg_quality=JPEG_QUALITY))
    doc.close()
    return pages


def call_vision(client, deployment: str, images: list[bytes]) -> dict:
    content: list[dict] = [
        {"type": "text",
         "text": "Extract the EOB fields per the schema. JSON only."}
    ]
    for img in images:
        b64 = base64.b64encode(img).decode()
        content.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{b64}"},
        })
    resp = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": content},
        ],
        max_completion_tokens=1536,
    )
    raw = (resp.choices[0].message.content or "").strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
    return json.loads(raw)


def sanitize_summary(s: str | None) -> str:
    if not s:
        return "untitled_eob"
    s = str(s).lower()
    s = re.sub(r"[^a-z0-9 _\-]", "", s)
    s = re.sub(r"[\s\-]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    if len(s) > 40:
        head = s[:40]
        s = head.rsplit("_", 1)[0] if "_" in head else head
    return s or "untitled_eob"


def is_jons_eob(extracted: dict) -> bool:
    first = (extracted.get("patient_first_name") or "").lower().strip()
    last = (extracted.get("patient_last_name") or "").lower().strip()
    if last != LAST_NAME:
        return False
    if first in JON_FIRST_NAMES:
        return True
    # Sometimes only an initial is visible; accept "j" with last=bowker
    if first and first[0] == "j" and len(first) <= 2:
        return True
    return False


def match_provider_folder(extracted: dict, existing_folders: set[str]) -> str | None:
    """Return slug of providers/<slug>/ folder, or None if no match."""
    candidates = []
    for key in ("provider_name", "facility_name", "insurance_carrier"):
        val = extracted.get(key)
        if val:
            candidates.append(val.lower())
    if not candidates:
        return None

    # Try alias map
    for cand in candidates:
        for pattern, canonical_slug in PROVIDER_ALIASES:
            if pattern.search(cand):
                if canonical_slug in existing_folders:
                    return canonical_slug

    # Try direct slug match against existing folders (token-overlap heuristic)
    for cand in candidates:
        words = set(re.findall(r"[a-z0-9]+", cand))
        if not words:
            continue
        best = None
        best_score = 0
        for folder in existing_folders:
            folder_words = set(folder.split("_"))
            overlap = len(words & folder_words)
            if overlap > best_score and overlap >= 2:
                best = folder
                best_score = overlap
        if best:
            return best

    return None


def parse_dos_year_month(dos: str | None) -> tuple[int, int]:
    if not dos:
        return 0, 0
    m = re.match(r"^(\d{4})-(\d{2})-\d{2}$", dos)
    if not m:
        return 0, 0
    y, mo = int(m.group(1)), int(m.group(2))
    if y < 1900 or y > 2100 or mo < 1 or mo > 12:
        return 0, 0
    return y, mo


def compose_filename(extracted: dict, ext: str, version: int) -> str:
    summary = sanitize_summary(extracted.get("contents_summary") or "")
    if not summary.endswith("_eob"):
        summary = (summary + "_eob")[:40].rstrip("_")
    year, month = parse_dos_year_month(extracted.get("date_of_service"))
    category = "medical"
    return f"{summary}_{category}_{year:04d}_{month:02d}_v{version}{ext.lower()}"


def unique_in_folder(folder: Path, extracted: dict, ext: str) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    for v in range(1, 1000):
        cand = folder / compose_filename(extracted, ext, v)
        if not cand.exists():
            return cand
    raise RuntimeError(f"too many version collisions in {folder}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--eob-dir", default=str(DEFAULT_EOB_DIR))
    ap.add_argument("--providers-root", default=str(DEFAULT_PROVIDERS))
    ap.add_argument("--log-dir", default=str(DEFAULT_LOG_DIR))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    eob_dir = Path(args.eob_dir)
    providers_root = Path(args.providers_root)
    log_dir = Path(args.log_dir)
    if not eob_dir.is_dir():
        sys.exit(f"[fatal] EOB folder not found: {eob_dir}")
    if not providers_root.is_dir():
        sys.exit(f"[fatal] providers root not found: {providers_root}")

    not_for_me = eob_dir / "not_for_me"
    unmatched = eob_dir / "unmatched"
    duplicates = eob_dir / "_duplicates"

    load_env(ENV_FILE)
    for k in ("AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT",
              "AZURE_OPENAI_DEPLOYMENT"):
        if not os.environ.get(k):
            sys.exit(f"[fatal] missing env var: {k}")
    client, deployment = make_client()

    existing_folders = {
        d.name for d in providers_root.iterdir() if d.is_dir()
    }
    print(f"[main] eob dir: {eob_dir}", flush=True)
    print(f"[main] existing provider folders: {len(existing_folders)}",
          flush=True)

    # Pass 1: hash dedup
    files = sorted(
        f for f in eob_dir.iterdir()
        if f.is_file() and f.suffix.lower() in {".pdf", ".jpg", ".jpeg", ".png"}
    )
    print(f"[hash] {len(files)} file(s) to hash", flush=True)

    seen: dict[str, Path] = {}
    dup_moves: list[tuple[Path, Path]] = []
    unique_files: list[Path] = []
    for f in files:
        h = sha256_of(f)
        if h in seen:
            dup_dst = duplicates / f.name
            dup_moves.append((f, dup_dst))
            continue
        seen[h] = f
        unique_files.append(f)
    print(f"[hash] {len(unique_files)} unique, {len(dup_moves)} duplicate(s)",
          flush=True)

    if not args.dry_run and dup_moves:
        duplicates.mkdir(parents=True, exist_ok=True)
        for src, dst in dup_moves:
            if dst.exists():
                # already there from a previous run, just remove the source
                src.unlink()
            else:
                src.rename(dst)
        print(f"[hash] moved duplicates to {duplicates}", flush=True)

    # Pass 2: classify each unique file
    rows: list[dict] = []
    decisions = {"matched": 0, "unmatched": 0, "not_for_me": 0, "error": 0}

    for f in unique_files:
        print(f"\n[parse] {f.name}", flush=True)
        try:
            if f.suffix.lower() == ".pdf":
                images = render_pdf_pages(f)
            else:
                images = [f.read_bytes()]
            if len(images) > MAX_PAGES:
                images = images[:MAX_PAGES]
            extracted = call_vision(client, deployment, images)
        except Exception as exc:
            print(f"  [error] {exc}", flush=True)
            decisions["error"] += 1
            rows.append({
                "source_file": f.name,
                "decision": "error",
                "destination": "",
                "error": str(exc)[:120],
            })
            continue

        patient = (
            (extracted.get("patient_first_name") or "") + " "
            + (extracted.get("patient_last_name") or "")
        ).strip() or "?"
        provider = (extracted.get("provider_name") or "?").strip()
        dos = extracted.get("date_of_service") or "?"
        pr = extracted.get("patient_responsibility")
        ip = extracted.get("insurance_paid")
        print(f"  patient={patient!r} provider={provider!r} dos={dos} "
              f"ins_paid={ip} pat_resp={pr}", flush=True)

        # Decide destination
        if not is_jons_eob(extracted):
            target_folder = not_for_me
            decision = "not_for_me"
            slug = ""
        else:
            slug = match_provider_folder(extracted, existing_folders) or ""
            if slug:
                target_folder = providers_root / slug
                decision = "matched"
            else:
                target_folder = unmatched
                decision = "unmatched"

        decisions[decision] += 1
        ext = f.suffix.lower()

        if args.dry_run:
            propose = compose_filename(extracted, ext, 1)
            print(f"  -> [{decision}] {target_folder.name}/{propose}",
                  flush=True)
            rows.append({
                "source_file": f.name,
                "decision": decision,
                "destination": f"{target_folder.name}/{propose}",
                "patient": patient,
                "provider": provider,
                "dos": dos,
                "ins_paid": ip,
                "pat_resp": pr,
                "slug": slug,
            })
            continue

        dst = unique_in_folder(target_folder, extracted, ext)
        f.rename(dst)
        rel_dst = dst.relative_to(HEALTH_ROOT)
        print(f"  -> [{decision}] {rel_dst}", flush=True)
        rows.append({
            "source_file": f.name,
            "decision": decision,
            "destination": str(rel_dst),
            "patient": patient,
            "provider": provider,
            "dos": dos,
            "ins_paid": ip,
            "pat_resp": pr,
            "slug": slug,
        })

    # Write decision log to Code_data
    log_dir.mkdir(parents=True, exist_ok=True)
    log_csv = log_dir / "eob_classify_log.csv"
    fieldnames = ["source_file", "decision", "destination", "patient",
                  "provider", "dos", "ins_paid", "pat_resp", "slug", "error"]
    with log_csv.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow(row)
    print(f"\n[main] decisions: {decisions}", flush=True)
    print(f"[main] log: {log_csv}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
