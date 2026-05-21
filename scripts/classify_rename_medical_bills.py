"""classify_rename_medical_bills.py — vision-classify every file in
Health_Bills/inbox/, rename it using the file_management v1.1 naming
convention, split multi-bill PDFs, and route into per-provider folders
under providers/ (medical) or a flat other/ folder (financial / personal
/ unknown).

Naming convention (locked, from ai-toolkit/src/file_management/BUILD_PLAN.md
§4.1):

    <contents_summary>_<category>_<YYYY>_<MM>_v<N>.<ext>

- contents_summary: snake_case, ≤40 chars, content-derived
- category: one of {medical, financial, personal, unknown} for this kit
- YYYY / MM: from statement date or content date; 0000/00 if undetermined
- vN: collision counter starting at v1

Routing:
- category == medical → providers/<provider-slug>/
- category in {financial, personal, unknown} → other/

Reads Azure OpenAI creds from a workstation .env file (default
~/.medbill-dispute-kit/.env; override via $MEDBILL_KIT_ENV_FILE).

Usage:
    python classify_rename_medical_bills.py
    python classify_rename_medical_bills.py --inbox <path>
    python classify_rename_medical_bills.py --dry-run
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import traceback
from pathlib import Path

import os

import fitz  # PyMuPDF

# Defaults. Override at runtime via CLI args or these env vars:
#   $HEALTHBILLS_ROOT       — parent of inbox/, providers/ (or Billers/+EOB/), other/
#   $MEDBILL_KIT_ENV_FILE   — path to the workstation .env that holds
#                             AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT,
#                             AZURE_OPENAI_DEPLOYMENT
ENV_FILE = Path(
    os.environ.get("MEDBILL_KIT_ENV_FILE")
    or (Path.home() / ".medbill-dispute-kit" / ".env")
)
HEALTH_ROOT = Path(
    os.environ.get("HEALTHBILLS_ROOT")
    or (Path.home() / "Health_Bills")
)
DEFAULT_INBOX = HEALTH_ROOT / "inbox"
DEFAULT_PROVIDERS = HEALTH_ROOT / "providers"
DEFAULT_OTHER = HEALTH_ROOT / "other"

MAX_PAGES = 20
RENDER_DPI = 120
JPEG_QUALITY = 80

ALLOWED_CATEGORIES = {"medical", "financial", "personal", "unknown"}

SYSTEM_PROMPT = """\
You are inspecting one or more scanned pages of a US medical, dental,
insurance, or benefits document. The pages may contain ONE document,
MULTIPLE distinct documents stapled together, or non-medical material
mixed with medical material.

Return a single JSON object with this exact shape:

{
  "documents": [
    {
      "contents_summary": "snake_case_descriptor",
      "category": "medical | financial | personal | unknown",
      "provider_name": "billing entity or insurer name as shown",
      "document_type": "bill | eob | payment_receipt | collection_notice | predetermination | cobra_notice | benefits_summary | marketplace_letter | dispute_letter | insurance_card | rollover_statement | other",
      "year": 2025,
      "month": 11,
      "statement_date": "YYYY-MM-DD or null",
      "account_number": "as shown, or null",
      "balance": 600.00,
      "pages": [1, 2, 3]
    }
  ]
}

Rules for contents_summary:
- Lowercase snake_case, 5 to 40 characters.
- Lead with the provider or insurer slug, then a short doc-kind suffix.
- Examples: "tristar_southern_hills_bill", "hospital_medicine_bill",
  "labcorp_collection_notice", "optum_eob", "humana_dental_denial",
  "sage_dental_predetermination", "hca_cobra_premium",
  "voya_401k_rollover", "tenncare_enrollment_letter",
  "wellstar_bill", "centennial_heart_bill", "premier_radiology_bill".
- Underscores between words, no spaces, no special characters.

Rules for category:
- "medical": any healthcare or dental bill, EOB from a health insurer,
  collection notice for medical debt, predetermination, dental denial,
  marketplace health-coverage letter, hospital/provider statements,
  TennCare/Medicaid/Medicare correspondence.
- "financial": COBRA premium notices, 401k rollover statements,
  insurance premium-only bills, anything that is a financial product
  rather than a clinical bill.
- "personal": identity documents, generic personal letters.
- "unknown": cannot determine.

Rules for year/month:
- Use the statement date if present, else the content date.
- If neither is determinable, use 0 for both.

Multi-document rule:
- If the pages contain multiple distinct documents (different providers
  or clearly separate statements), return one entry per document and
  list only that document's pages in `pages` (1-indexed).

Other field rules:
- `balance` is the patient responsibility in USD as a plain number, or
  null if no balance.
- Use null for any field that is not visible or that you are not sure
  about. Do not guess account numbers, dates, or amounts.
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


def render_pdf_pages(pdf_path: Path, max_pages: int = MAX_PAGES) -> list[bytes]:
    """Render up to max_pages of the PDF as JPEG bytes; stop iterating
    after the cap to avoid paying the render cost on pages we will not
    send to the model."""
    doc = fitz.open(str(pdf_path))
    pages: list[bytes] = []
    zoom = RENDER_DPI / 72.0
    mat = fitz.Matrix(zoom, zoom)
    for i, page in enumerate(doc):
        if i >= max_pages:
            break
        pix = page.get_pixmap(matrix=mat)
        pages.append(pix.tobytes("jpeg", jpg_quality=JPEG_QUALITY))
    doc.close()
    return pages


def call_vision(client, deployment: str, images: list[bytes]) -> dict:
    content: list[dict] = [
        {"type": "text",
         "text": "Identify each document in these pages and return JSON only."}
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
        max_completion_tokens=4096,
    )
    raw = (resp.choices[0].message.content or "").strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
    return json.loads(raw)


def sanitize_summary(s: str | None) -> str:
    """Per BUILD_PLAN §4.10."""
    if not s:
        return "untitled"
    s = str(s)
    s = s.lower()
    s = re.sub(r"[^a-z0-9 _\-]", "", s)
    s = re.sub(r"[\s\-]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    if len(s) > 40:
        head = s[:40]
        if "_" in head:
            s = head.rsplit("_", 1)[0]
        else:
            s = head
    return s or "untitled"


PROVIDER_ALIASES: list[tuple[re.Pattern, str]] = [
    (re.compile(r"tristar|southern\s*hills"), "tristar_southern_hills_medical_center"),
    (re.compile(r"labcorp|laboratory\s+corporation"), "labcorp"),
    (re.compile(r"premier\s+radiology"), "premier_radiology"),
]


def slugify_provider(s: str | None) -> str:
    if not s:
        return "unknown"
    low = s.lower()
    for pattern, canonical in PROVIDER_ALIASES:
        if pattern.search(low):
            return canonical
    cleaned = re.sub(r"[^a-z0-9]+", "_", low)
    return cleaned.strip("_")[:50] or "unknown"


def normalize_category(c: str | None) -> str:
    c = (c or "unknown").lower().strip()
    return c if c in ALLOWED_CATEGORIES else "unknown"


def safe_int(v, lo: int = 0, hi: int = 9999) -> int:
    try:
        n = int(v)
    except (TypeError, ValueError):
        return 0
    if n < lo or n > hi:
        return 0
    return n


def compose_name(doc: dict, ext: str, version: int) -> str:
    summary = sanitize_summary(doc.get("contents_summary"))
    category = normalize_category(doc.get("category"))
    year = safe_int(doc.get("year"))
    month = safe_int(doc.get("month"), 0, 12)
    return f"{summary}_{category}_{year:04d}_{month:02d}_v{version}{ext.lower()}"


def resolve_destination(doc: dict, ext: str, providers_root: Path,
                        other_root: Path) -> Path:
    """Return a non-colliding path; increment v1 → v2 → ..."""
    category = normalize_category(doc.get("category"))
    if category == "medical":
        folder = providers_root / slugify_provider(doc.get("provider_name"))
    else:
        folder = other_root
    folder.mkdir(parents=True, exist_ok=True)
    for version in range(1, 1000):
        candidate = folder / compose_name(doc, ext, version)
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"too many version collisions in {folder}")


def split_pdf(pdf_path: Path, pages: list[int], out_path: Path) -> None:
    src = fitz.open(str(pdf_path))
    dst = fitz.open()
    for p in pages:
        idx = int(p) - 1
        if 0 <= idx < len(src):
            dst.insert_pdf(src, from_page=idx, to_page=idx)
    dst.save(str(out_path))
    dst.close()
    src.close()


def process_file(client, deployment, path: Path,
                 providers_root: Path, other_root: Path,
                 dry_run: bool) -> None:
    suffix = path.suffix.lower()
    print(f"\n[process] {path.name}", flush=True)

    if suffix == ".pdf":
        try:
            images = render_pdf_pages(path, max_pages=MAX_PAGES)
        except Exception as exc:
            print(f"  [skip] render failed: {exc}", flush=True)
            return
    elif suffix in {".jpg", ".jpeg", ".png", ".webp"}:
        images = [path.read_bytes()]
    else:
        print(f"  [skip] unsupported type: {suffix}", flush=True)
        return

    try:
        result = call_vision(client, deployment, images)
    except Exception as exc:
        print(f"  [skip] vision call failed: {exc}", flush=True)
        return

    docs = result.get("documents") or result.get("bills") or []
    if not docs:
        print(f"  [skip] no documents returned from model", flush=True)
        return

    print(f"  [classify] {len(docs)} document(s) detected", flush=True)
    for i, doc in enumerate(docs, 1):
        print(f"    {i}. summary={doc.get('contents_summary')!r:40s} "
              f"cat={normalize_category(doc.get('category'))} "
              f"provider={doc.get('provider_name')!r} "
              f"type={doc.get('document_type')} "
              f"date={doc.get('statement_date')} "
              f"acct={doc.get('account_number')} "
              f"bal={doc.get('balance')} "
              f"pages={doc.get('pages')}",
              flush=True)

    if dry_run:
        return

    if len(docs) == 1:
        doc = docs[0]
        dst = resolve_destination(doc, suffix, providers_root, other_root)
        path.rename(dst)
        print(f"  [rename] -> {dst.relative_to(HEALTH_ROOT)}", flush=True)
        return

    if suffix != ".pdf":
        print(f"  [warn] {len(docs)} docs in non-PDF; keeping only the first",
              flush=True)
        doc = docs[0]
        dst = resolve_destination(doc, suffix, providers_root, other_root)
        path.rename(dst)
        print(f"  [rename] -> {dst.relative_to(HEALTH_ROOT)}", flush=True)
        return

    # Multi-doc split: resolve and write one at a time so that two docs
    # sharing the same (summary, category, year, month) get v1, v2, v3 etc.
    # instead of overwriting each other.
    written: list[Path] = []
    try:
        for doc in docs:
            pages = doc.get("pages") or []
            if not pages:
                raise ValueError(
                    f"document {doc.get('contents_summary')!r} has no pages"
                )
            dst = resolve_destination(doc, suffix, providers_root, other_root)
            split_pdf(path, pages, dst)
            written.append(dst)
            print(f"  [split]  -> {dst.relative_to(HEALTH_ROOT)} "
                  f"(pages {pages})", flush=True)
    except Exception as exc:
        print(f"  [error] split failed: {exc}; rolling back", flush=True)
        for w in written:
            try:
                w.unlink()
            except Exception:
                pass
        return

    path.unlink()
    print(f"  [done] removed multi-doc original", flush=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--inbox", default=str(DEFAULT_INBOX))
    ap.add_argument("--providers-root", default=str(DEFAULT_PROVIDERS))
    ap.add_argument("--other-root", default=str(DEFAULT_OTHER))
    ap.add_argument("--dry-run", action="store_true",
                    help="Classify and print only; no rename/split/move.")
    args = ap.parse_args()

    inbox = Path(args.inbox)
    providers_root = Path(args.providers_root)
    other_root = Path(args.other_root)
    if not inbox.is_dir():
        sys.exit(f"[fatal] inbox not found: {inbox}")
    providers_root.mkdir(parents=True, exist_ok=True)
    other_root.mkdir(parents=True, exist_ok=True)

    load_env(ENV_FILE)
    for k in ("AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT",
              "AZURE_OPENAI_DEPLOYMENT"):
        if not os.environ.get(k):
            sys.exit(f"[fatal] missing env var: {k}")
    client, deployment = make_client()

    files = sorted(f for f in inbox.iterdir() if f.is_file())
    print(f"[main] inbox: {inbox}", flush=True)
    print(f"[main] providers root: {providers_root}", flush=True)
    print(f"[main] other root: {other_root}", flush=True)
    print(f"[main] {len(files)} file(s) to process; dry_run={args.dry_run}",
          flush=True)

    for f in files:
        try:
            process_file(client, deployment, f,
                         providers_root, other_root, args.dry_run)
        except Exception:
            print(f"  [error] unhandled exception on {f.name}:", flush=True)
            traceback.print_exc()
            continue

    print("\n[main] done", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
