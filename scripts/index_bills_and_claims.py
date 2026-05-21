"""index_bills_and_claims.py — walk Billers/<slug>/ and EOB/<slug>/ and
write per-folder index CSVs derived from the sidecar text.

Per-folder outputs:
    Billers/<slug>/_bills.csv      -- one row per bill PDF
    EOB/<slug>/_claims.csv         -- one row per CLAIM (not per file);
                                       a multi-claim EOB produces N rows

Bills get structured-field extraction (account_number, statement_date,
dos_start, dos_end, total_billed, current_balance, biller_name_raw) plus
an is_itemized heuristic per the kit's peer-reviewed detector. EOBs
get one row per claim entry (claim_number, provider_rendering_raw,
biller_entity_raw, status, patient_account, dos_start, dos_end,
billed, allowed, paid, patient_responsibility, patient_name).

Idempotent: each sidecar's content hash is stored in its row. On
re-run, sidecars whose hash hasn't changed are skipped (no Azure
call). New / changed sidecars are sent to gpt-5.2 once.

Usage:
    python index_bills_and_claims.py
    python index_bills_and_claims.py --force  # re-extract every file
"""

from __future__ import annotations

import argparse
import csv
import datetime
import hashlib
import json
import os
import re
import sys
from pathlib import Path

# Default root for the Health_Bills tree. Override via $HEALTHBILLS_ROOT
# env var or --root flag. The default is a placeholder; the public
# scripts don't ship with a workstation-specific path.
HEALTH_ROOT = Path(
    os.environ.get("HEALTHBILLS_ROOT")
    or (Path.home() / "Health_Bills")
)
BILLERS_DIR = HEALTH_ROOT / "Billers"
EOB_DIR = HEALTH_ROOT / "EOB"
# Azure OpenAI credentials live in a workstation .env. Override via
# $MEDBILL_KIT_ENV_FILE or --env-file.
ENV_FILE = Path(
    os.environ.get("MEDBILL_KIT_ENV_FILE")
    or (Path.home() / ".medbill-dispute-kit" / ".env")
)
SIDECAR_SUFFIX = ".extracted.txt"

BILLS_CSV = "_bills.csv"
CLAIMS_CSV = "_claims.csv"

BILL_COLUMNS = [
    "row_hash", "file", "biller_slug", "biller_name_raw",
    "account_number", "statement_date",
    "dos_start", "dos_end",
    "total_billed", "current_balance",
    "has_itemization", "itemization_signals",
    "doc_type", "notes",
]

CLAIM_COLUMNS = [
    "row_hash", "file", "biller_slug",
    "patient_name", "member_id",
    "claim_number", "patient_account_number",
    "provider_rendering_raw", "biller_entity_raw",
    "network_status",
    "dos_start", "dos_end",
    "total_billed", "total_allowed", "total_plan_paid",
    "patient_responsibility",
    "notes",
]

# Itemization detector (peer-reviewed heuristic, see scripts/README.md).
DATED_LINE_RE = re.compile(
    r"(?P<date>\b(?:\d{1,2}/\d{1,2}/\d{2,4}|\d{4}-\d{2}-\d{2})\b)"
    r"[^\n]{0,200}?\$\s*(?P<amount>\d{1,3}(?:,\d{3})*\.\d{2})"
    r"|"
    r"\$\s*(?P<amount2>\d{1,3}(?:,\d{3})*\.\d{2})"
    r"[^\n]{0,200}?(?P<date2>\b(?:\d{1,2}/\d{1,2}/\d{2,4}|\d{4}-\d{2}-\d{2})\b)",
    re.I,
)
PAYMENT_LEDGER_KEYWORDS = re.compile(
    r"\b(payment\s+received|thank\s+you|adjustment|write[-\s]?off|"
    r"refund|insurance\s+paid|contractual\s+adjustment|"
    r"patient\s+payment|balance\s+forward|previous\s+balance|"
    r"finance\s+charge)\b",
    re.I,
)
AGING_KEYWORDS = re.compile(
    r"\b(statement\s+date|due\s+date|billing\s+date|aging|cycle)\b",
    re.I,
)
EOB_KEYWORDS = re.compile(
    r"\b(explanation\s+of\s+benefits|"
    r"(allowed|plan\s+paid)\s+amount|"
    r"deductible|coinsurance|patient\s+responsibility|"
    r"claim\s+number|remark\s+code)\b",
    re.I,
)
UB04_HEADERS_RE = re.compile(
    r"\b(revenue\s+code|HCPCS\s*/?\s*rates?|service\s+units|"
    r"total\s+charges|type\s+of\s+bill|occurrence\s+code|"
    r"value\s+code)\b",
    re.I,
)
CMS1500_HEADERS_RE = re.compile(
    r"\b(place\s+of\s+service|CPT\s*/?\s*HCPCS|modifiers?|"
    r"diagnosis\s+pointer|days\s*/\s*units)\b",
    re.I,
)
ITEMIZED_HEADER_RE = re.compile(
    r"\b(itemized\s+statement|itemization|detail\s+of\s+charges|"
    r"itemized\s+bill)\b",
    re.I,
)
CPT_HCPCS_RE = re.compile(
    r"\b(?:CPT|HCPCS)\s*\(?(\d{4,5}[A-Z]?)\)?|"
    r"\b(\d{5})\b(?=[^\n]{0,80}\$)",
    re.I,
)


def detect_is_itemized(body: str) -> tuple[bool, str]:
    """Return (is_itemized, signals_summary)."""
    signals: list[str] = []

    # Pass A: dated charge lines
    distinct_dates: set[str] = set()
    for m in DATED_LINE_RE.finditer(body):
        d = m.group("date") or m.group("date2")
        if d:
            distinct_dates.add(d.strip())
    dcl_count = len(distinct_dates)
    signals.append(f"dcl={dcl_count}")

    # Override-to-false signals
    if PAYMENT_LEDGER_KEYWORDS.search(body) and \
       len(PAYMENT_LEDGER_KEYWORDS.findall(body)) >= 2:
        signals.append("ledger_override")
        return False, ";".join(signals)
    if EOB_KEYWORDS.search(body) and len(EOB_KEYWORDS.findall(body)) >= 4:
        signals.append("eob_override")
        return False, ";".join(signals)
    # Aging-only override: dated charge lines are present but each
    # dated line sits within 50 chars of an aging keyword (statement
    # date, due date, billing cycle). Indicates an aging report rather
    # than itemized services.
    if dcl_count > 0 and AGING_KEYWORDS.search(body):
        aging_dominant = True
        for m in DATED_LINE_RE.finditer(body):
            window_start = max(0, m.start() - 50)
            window_end = min(len(body), m.end() + 50)
            if not AGING_KEYWORDS.search(body[window_start:window_end]):
                aging_dominant = False
                break
        if aging_dominant:
            signals.append("aging_only_override")
            return False, ";".join(signals)

    # Override-to-true signals
    if UB04_HEADERS_RE.search(body):
        signals.append("ub04_headers")
        return True, ";".join(signals)
    if CMS1500_HEADERS_RE.search(body):
        signals.append("cms1500_headers")
        return True, ";".join(signals)
    if ITEMIZED_HEADER_RE.search(body):
        cpt_hits = sum(1 for _ in CPT_HCPCS_RE.finditer(body))
        signals.append(f"itemized_header+cpt={cpt_hits}")
        if cpt_hits >= 1:
            return True, ";".join(signals)

    # Primary rule: 3+ distinct dated charge lines
    if dcl_count >= 3:
        return True, ";".join(signals)
    return False, ";".join(signals)


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


def read_sidecar_body(sidecar: Path) -> str:
    try:
        text = sidecar.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        if ln.strip() == "# ---":
            return "\n".join(lines[i+1:])
    return text


def hash_body(body: str) -> str:
    return hashlib.sha1(body.encode("utf-8", errors="replace")).hexdigest()[:16]


def read_existing(csv_path: Path, columns: list[str]) -> list[dict]:
    if not csv_path.exists():
        return []
    with csv_path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(csv_path: Path, columns: list[str], rows: list[dict]) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in columns})


BILL_SYSTEM = """\
You are extracting structured fields from a US medical-bill statement
(or itemization). Output JSON only:
{
  "biller_name_raw": "billing entity name as printed",
  "account_number": "as printed, or null",
  "statement_date": "YYYY-MM-DD or null",
  "dos_start": "YYYY-MM-DD or null",
  "dos_end": "YYYY-MM-DD or null",
  "total_billed": 1234.56,
  "current_balance": 234.56,
  "doc_type": "bill | itemization | collection_notice | predetermination | cobra_notice | informational",
  "notes": "one short sentence summarizing the document"
}
Use null for any field that is not visible. Do not guess. Output JSON
only — no markdown fences, no commentary.
"""


CLAIM_SYSTEM = """\
You are extracting claim-level rows from a UHC (or similar) Explanation
of Benefits document. The EOB can contain ONE or MANY claims, each
identified by a "Claim number:" line. For each claim, return the
fields below.

Output JSON only:
{
  "patient_name": "Member/Patient name as printed",
  "member_id": "Member ID as printed, or null",
  "claims": [
    {
      "claim_number": "...",
      "patient_account_number": "...",
      "provider_rendering_raw": "rendering doctor / clinician name",
      "biller_entity_raw": "billing entity name (often PC/LLC/Inc.)",
      "network_status": "Network | Out-of-Network | unknown",
      "dos_start": "YYYY-MM-DD or null",
      "dos_end": "YYYY-MM-DD or null",
      "total_billed": 0,
      "total_allowed": 0,
      "total_plan_paid": 0,
      "patient_responsibility": 0
    }
  ]
}

For each claim, sum line-item totals if a single total isn't shown.
Use null for fields not visible. If only one claim is present, the
"claims" array has one element. Output JSON only.
"""


def call_vision_text(client, deployment: str, system: str,
                     body: str) -> dict | None:
    try:
        resp = client.chat.completions.create(
            model=deployment,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": body[:80_000]},
            ],
            max_completion_tokens=4096,
        )
    except Exception as exc:
        print(f"  [api error] {exc}", flush=True)
        return None
    raw = (resp.choices[0].message.content or "").strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"  [parse error] {exc}; raw[:120]={raw[:120]!r}",
              flush=True)
        return None


def coerce_float(v) -> str:
    if v is None or v == "":
        return ""
    try:
        return f"{float(v):.2f}"
    except (TypeError, ValueError):
        return ""


def coerce_date(v) -> str:
    if not v:
        return ""
    s = str(v).strip()
    return s if re.match(r"^\d{4}-\d{2}-\d{2}$", s) else ""


def process_bills_folder(folder: Path, client, deployment: str,
                         force: bool) -> tuple[int, int]:
    """Returns (added, skipped)."""
    slug = folder.name
    csv_path = folder / BILLS_CSV
    existing = read_existing(csv_path, BILL_COLUMNS)
    by_hash = {r.get("row_hash", ""): r for r in existing}

    rows_out: list[dict] = []
    seen_files: set[str] = set()
    added = skipped = 0

    for sc in sorted(folder.glob(f"*{SIDECAR_SUFFIX}")):
        source_name = sc.name[:-len(SIDECAR_SUFFIX)]
        seen_files.add(source_name)
        body = read_sidecar_body(sc)
        if not body.strip():
            continue
        h = hash_body(body)
        if not force and h in by_hash and by_hash[h].get("file") == source_name:
            rows_out.append(by_hash[h])
            skipped += 1
            continue

        is_itemized, signals = detect_is_itemized(body)
        print(f"[bill] {slug}/{source_name}", flush=True)
        data = call_vision_text(client, deployment, BILL_SYSTEM, body)
        if data is None:
            data = {}
        row = {
            "row_hash": h,
            "file": source_name,
            "biller_slug": slug,
            "biller_name_raw": (data.get("biller_name_raw") or "").strip(),
            "account_number": (data.get("account_number") or "").strip(),
            "statement_date": coerce_date(data.get("statement_date")),
            "dos_start": coerce_date(data.get("dos_start")),
            "dos_end": coerce_date(data.get("dos_end")),
            "total_billed": coerce_float(data.get("total_billed")),
            "current_balance": coerce_float(data.get("current_balance")),
            "has_itemization": "Y" if is_itemized else "N",
            "itemization_signals": signals,
            "doc_type": (data.get("doc_type") or "").strip(),
            "notes": (data.get("notes") or "")[:240],
        }
        rows_out.append(row)
        added += 1
        print(f"  bal=${row['current_balance']!r} stmt={row['statement_date']!r} "
              f"itemized={row['has_itemization']}", flush=True)

    # Preserve rows for files we couldn't see this run (defensive)
    for r in existing:
        if r.get("file") not in seen_files and r not in rows_out:
            rows_out.append(r)

    write_csv(csv_path, BILL_COLUMNS, rows_out)
    return added, skipped


def process_eob_folder(folder: Path, client, deployment: str,
                       force: bool) -> tuple[int, int]:
    """Returns (claim_rows_added, files_skipped)."""
    slug = folder.name
    csv_path = folder / CLAIMS_CSV
    existing = read_existing(csv_path, CLAIM_COLUMNS)
    existing_hashes = {r.get("row_hash", ""): r for r in existing}

    rows_out: list[dict] = []
    seen_files: set[str] = set()
    added_rows = 0
    skipped_files = 0

    for sc in sorted(folder.glob(f"*{SIDECAR_SUFFIX}")):
        source_name = sc.name[:-len(SIDECAR_SUFFIX)]
        seen_files.add(source_name)
        body = read_sidecar_body(sc)
        if not body.strip():
            continue
        h = hash_body(body)
        existing_for_file = [r for r in existing if r.get("file") == source_name]
        if not force and existing_for_file and \
                all(r.get("row_hash") == h for r in existing_for_file):
            rows_out.extend(existing_for_file)
            skipped_files += 1
            continue

        print(f"[eob] {slug}/{source_name}", flush=True)
        data = call_vision_text(client, deployment, CLAIM_SYSTEM, body)
        if data is None:
            continue
        claims = data.get("claims") or []
        patient_name = (data.get("patient_name") or "").strip()
        member_id = (data.get("member_id") or "").strip()
        if not claims:
            # Synthesize a single "no-claim" row so we don't lose the file
            rows_out.append({
                "row_hash": h, "file": source_name, "biller_slug": slug,
                "patient_name": patient_name, "member_id": member_id,
                "notes": "no claims parsed",
            })
            added_rows += 1
            continue
        for c in claims:
            rows_out.append({
                "row_hash": h,
                "file": source_name,
                "biller_slug": slug,
                "patient_name": patient_name,
                "member_id": member_id,
                "claim_number": (c.get("claim_number") or "").strip(),
                "patient_account_number":
                    (c.get("patient_account_number") or "").strip(),
                "provider_rendering_raw":
                    (c.get("provider_rendering_raw") or "").strip(),
                "biller_entity_raw":
                    (c.get("biller_entity_raw") or "").strip(),
                "network_status": (c.get("network_status") or "").strip(),
                "dos_start": coerce_date(c.get("dos_start")),
                "dos_end": coerce_date(c.get("dos_end")),
                "total_billed": coerce_float(c.get("total_billed")),
                "total_allowed": coerce_float(c.get("total_allowed")),
                "total_plan_paid": coerce_float(c.get("total_plan_paid")),
                "patient_responsibility":
                    coerce_float(c.get("patient_responsibility")),
                "notes": "",
            })
            added_rows += 1
        print(f"  +{len(claims)} claim(s)", flush=True)

    for r in existing:
        if r.get("file") not in seen_files and r not in rows_out:
            rows_out.append(r)

    write_csv(csv_path, CLAIM_COLUMNS, rows_out)
    return added_rows, skipped_files


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--force", action="store_true",
                    help="Re-extract every sidecar even if its hash hasn't changed.")
    args = ap.parse_args()

    load_env(ENV_FILE)
    for k in ("AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT",
              "AZURE_OPENAI_DEPLOYMENT"):
        if not os.environ.get(k):
            sys.exit(f"[fatal] missing env var: {k}")
    client, deployment = make_client()

    totals = {"bills_added": 0, "bills_skipped": 0,
              "claim_rows_added": 0, "eob_files_skipped": 0}

    if BILLERS_DIR.is_dir():
        for folder in sorted(d for d in BILLERS_DIR.iterdir() if d.is_dir()):
            a, s = process_bills_folder(folder, client, deployment, args.force)
            totals["bills_added"] += a
            totals["bills_skipped"] += s
    if EOB_DIR.is_dir():
        for folder in sorted(d for d in EOB_DIR.iterdir() if d.is_dir()):
            a, s = process_eob_folder(folder, client, deployment, args.force)
            totals["claim_rows_added"] += a
            totals["eob_files_skipped"] += s

    print(f"\n[done] {totals}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
