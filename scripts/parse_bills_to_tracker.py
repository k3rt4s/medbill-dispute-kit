"""parse_bills_to_tracker.py — walk Health_Bills/providers/, extract
structured bill data per the kit's schemas/bill.toml shape via Azure
OpenAI vision, dedupe per schemas/deduplication_rules.toml, and write
tracker.csv to C:/Code_data/medbill-dispute-kit/tracker/.

Output paths follow AGENTS.md §3 (generated data lives under Code_data,
never under Code):
    C:/Code_data/medbill-dispute-kit/tracker/tracker.csv
    C:/Code_data/medbill-dispute-kit/tracker/parse_log.md

Usage:
    python parse_bills_to_tracker.py
    python parse_bills_to_tracker.py --providers-root <path>
    python parse_bills_to_tracker.py --out-dir <path>
    python parse_bills_to_tracker.py --dry-run
"""

from __future__ import annotations

import argparse
import base64
import csv
import datetime
import json
import os
import re
import sys
import traceback
from pathlib import Path

import fitz  # PyMuPDF

ENV_FILE = Path(r"C:\Code\projects\ai-toolkit\.env")
HEALTH_ROOT = Path(r"D:\Proton Drive\My files\Financial\Health_Bills")
DEFAULT_PROVIDERS = HEALTH_ROOT / "providers"
DEFAULT_OUT_DIR = Path(r"C:\Code_data\medbill-dispute-kit\tracker")

MAX_PAGES = 10
RENDER_DPI = 120
JPEG_QUALITY = 80

TRACKER_COLUMNS = [
    "bill_id",
    "encounter_id",
    "provider_name",
    "provider_type",
    "account_number",
    "statement_date",
    "date_of_service_start",
    "date_of_service_end",
    "total_billed",
    "current_balance",
    "insurance_carrier",
    "in_network_status",
    "was_emergency",
    "findings",
    "next_action",
    "next_action_due",
    "last_action_taken",
    "last_action_date",
    "certified_mail_last",
    "status",
    "last_statement_date",
    "notes",
]

PROVIDER_TYPES = {
    "hospital", "physician_group", "anesthesiology", "radiology",
    "pathology", "lab", "emergency_physician", "ambulance", "dental",
    "pharmacy", "device_supplier", "other",
}

IN_NETWORK_VALUES = {
    "in_network", "out_of_network", "unknown", "uninsured", "self_pay",
}

# Subset of bill.toml findings vocabulary that this prompt asks the model
# to consider. Keep it tight so the model picks deliberately.
FINDINGS_VOCAB = [
    "no_itemization",
    "possible_upcoding_99285",
    "possible_upcoding_99284",
    "no_surprises_emergency",
    "no_surprises_ancillary_oon",
    "no_good_faith_estimate",
    "ppdr_eligible",
    "duplicate_line",
    "price_above_fair_market",
    "denied_by_insurance",
    "balance_due_before_insurance_paid",
    "follow_up_statement_only",
    "no_findings",
]

NEXT_ACTION_DUE_DAYS = {
    "request_itemization": 14,
    "request_records_hipaa": 30,
    "initial_dispute": 14,
    "appeal_insurance_denial": 30,
    "dispute_no_surprises_violation": 30,
    "negotiate": 21,
    "apply_for_financial_assistance": 14,
    "fdcpa_validation_request": 30,
    "30day_warning": 30,
    "file_state_complaint": 30,
    "file_cms_complaint": 30,
    "file_cms_hpt_complaint": 30,
    "file_ppdr": 30,
    "monitor": 30,
    "closed_resolved": 0,
    "closed_paid": 0,
}

SYSTEM_PROMPT = f"""\
You are reading a US medical bill, EOB, dental statement, collection
notice, or related healthcare document. Extract the structured fields
below and return JSON only.

Schema (return exactly this shape):

{{
  "provider_name": "billing entity / insurer name as shown",
  "provider_type": "one of: hospital, physician_group, anesthesiology, radiology, pathology, lab, emergency_physician, ambulance, dental, pharmacy, device_supplier, other",
  "account_number": "as shown on the statement, or null",
  "statement_number": "invoice or statement number if shown, or null",
  "statement_date": "YYYY-MM-DD or null",
  "date_of_service_start": "YYYY-MM-DD or null",
  "date_of_service_end": "YYYY-MM-DD or null",
  "total_billed": 100.00,
  "current_balance": 50.00,
  "total_insurance_paid": 25.00,
  "total_insurance_adjustment": 25.00,
  "total_patient_paid": 0.00,
  "insurance_carrier": "name of insurance plan or null",
  "in_network_status": "in_network | out_of_network | unknown | uninsured | self_pay",
  "was_emergency": true,
  "contact_phone": "billing dept phone, or null",
  "cpt_codes": ["12345", "67890"],
  "findings": ["slug", "slug"],
  "document_type": "bill | eob | payment_receipt | collection_notice | predetermination | other",
  "notes": "one-sentence summary of the document"
}}

Rules:
- Use null for any field that is not visible. Do not guess account
  numbers, dates, amounts, or CPT codes.
- `total_billed` is the gross charge before insurance adjustments.
- `current_balance` is what the patient currently owes (could be 0).
- `findings` should draw from this controlled vocabulary only:
  {", ".join(FINDINGS_VOCAB)}.
  Apply `no_itemization` if no CPT codes / line items are visible.
  Apply `follow_up_statement_only` if this looks like a repeat
  statement with no new charges. Apply `no_findings` if nothing
  jumps out.
- `was_emergency` is true only when the document explicitly references
  ER / emergency department services.
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
         "text": "Extract the bill fields per the schema. JSON only."}
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
        max_completion_tokens=2048,
    )
    raw = (resp.choices[0].message.content or "").strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
    return json.loads(raw)


def coerce_float(v) -> float | None:
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def coerce_date(v) -> str | None:
    if not v:
        return None
    s = str(v).strip()
    if re.match(r"^\d{4}-\d{2}-\d{2}$", s):
        return s
    return None


def normalize_provider_type(t: str | None) -> str:
    t = (t or "other").lower().strip()
    return t if t in PROVIDER_TYPES else "other"


def normalize_network(s: str | None) -> str | None:
    s = (s or "").lower().strip()
    return s if s in IN_NETWORK_VALUES else None


def infer_next_action(extracted: dict, file_hint: str) -> str:
    """Pick a sensible default next_action from extracted fields + filename hints."""
    findings = extracted.get("findings") or []
    doc_type = (extracted.get("document_type") or "").lower()
    bal = coerce_float(extracted.get("current_balance")) or 0.0
    name_low = file_hint.lower()

    if doc_type == "collection_notice" or "collection" in name_low:
        return "fdcpa_validation_request"
    if doc_type == "eob" or "_eob_" in name_low:
        return "monitor"
    if doc_type == "predetermination":
        return "appeal_insurance_denial"
    if doc_type == "payment_receipt" or bal <= 0:
        return "closed_paid" if bal == 0 else "monitor"
    if "no_itemization" in findings:
        return "request_itemization"
    if "no_surprises_emergency" in findings or "no_surprises_ancillary_oon" in findings:
        return "dispute_no_surprises_violation"
    if "denied_by_insurance" in findings:
        return "appeal_insurance_denial"
    if "price_above_fair_market" in findings:
        return "negotiate"
    if bal < 50:
        return "negotiate"
    return "request_itemization"


def compute_next_action_due(next_action: str) -> str:
    days = NEXT_ACTION_DUE_DAYS.get(next_action, 14)
    return (datetime.date.today() + datetime.timedelta(days=days)).isoformat()


def infer_status(extracted: dict, balance: float) -> str:
    doc_type = (extracted.get("document_type") or "").lower()
    if doc_type in {"payment_receipt"} or balance == 0:
        return "closed"
    return "open"


def normalize_account(acct) -> str:
    if not acct:
        return ""
    return re.sub(r"\s+", "", str(acct))


def make_bill_record(extracted: dict, source_file: Path,
                     bill_seq: dict, encounter_seq: dict,
                     known_bills: list[dict]) -> dict | None:
    """Build a tracker row from an extracted document; apply dedup."""
    provider_name = (extracted.get("provider_name") or "").strip()
    account_number = normalize_account(extracted.get("account_number"))
    statement_date = coerce_date(extracted.get("statement_date"))
    dos_start = coerce_date(extracted.get("date_of_service_start"))
    dos_end = coerce_date(extracted.get("date_of_service_end"))
    total_billed = coerce_float(extracted.get("total_billed"))
    current_balance = coerce_float(extracted.get("current_balance"))

    if not provider_name and not account_number:
        # Cannot place this document on the tracker
        return None

    # Dedup: same provider + same account → update existing
    for existing in known_bills:
        if (existing["account_number"]
                and account_number
                and existing["account_number"] == account_number
                and existing["provider_name"].lower() == provider_name.lower()):
            # Merge as follow-up: keep latest statement_date and balance
            if statement_date and (
                not existing.get("last_statement_date")
                or statement_date > existing["last_statement_date"]
            ):
                existing["last_statement_date"] = statement_date
                if current_balance is not None:
                    existing["current_balance"] = current_balance
                if statement_date > (existing.get("statement_date") or ""):
                    existing["statement_date"] = statement_date
            existing.setdefault("source_files", []).append(str(source_file))
            return None

    # New bill
    year = datetime.date.today().year
    bill_seq[year] = bill_seq.get(year, 0) + 1
    bill_id = f"B-{year}-{bill_seq[year]:03d}"

    # Encounter assignment: share encounter_id with any existing bill that
    # has the same date_of_service_start
    encounter_id = ""
    if dos_start:
        for existing in known_bills:
            if existing.get("date_of_service_start") == dos_start \
                    and existing.get("encounter_id"):
                encounter_id = existing["encounter_id"]
                break
    if not encounter_id and dos_start:
        encounter_seq[year] = encounter_seq.get(year, 0) + 1
        encounter_id = f"E-{year}-{encounter_seq[year]:03d}"

    findings = extracted.get("findings") or []
    if not isinstance(findings, list):
        findings = [str(findings)]
    findings = [str(f) for f in findings if f]

    file_hint = source_file.name
    next_action = infer_next_action(extracted, file_hint)
    next_action_due = compute_next_action_due(next_action)

    record = {
        "bill_id": bill_id,
        "encounter_id": encounter_id,
        "provider_name": provider_name,
        "provider_type": normalize_provider_type(extracted.get("provider_type")),
        "account_number": account_number,
        "statement_date": statement_date or "",
        "date_of_service_start": dos_start or "",
        "date_of_service_end": dos_end or "",
        "total_billed": "" if total_billed is None else f"{total_billed:.2f}",
        "current_balance": "" if current_balance is None else f"{current_balance:.2f}",
        "insurance_carrier": (extracted.get("insurance_carrier") or "").strip(),
        "in_network_status": normalize_network(extracted.get("in_network_status")) or "",
        "was_emergency": "true" if extracted.get("was_emergency") is True
                          else ("false" if extracted.get("was_emergency") is False else ""),
        "findings": ";".join(findings),
        "next_action": next_action,
        "next_action_due": next_action_due,
        "last_action_taken": "",
        "last_action_date": "",
        "certified_mail_last": "",
        "status": infer_status(extracted, current_balance or 0.0),
        "last_statement_date": statement_date or "",
        "notes": (extracted.get("notes") or "")[:240],
        "source_files": [str(source_file)],
    }
    return record


def write_tracker(rows: list[dict], out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "tracker.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=TRACKER_COLUMNS, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({col: row.get(col, "") for col in TRACKER_COLUMNS})
    return csv_path


def write_log(events: list[str], out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / "parse_log.md"
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"\n## Parse run {ts}\n\n")
        for ln in events:
            f.write(f"- {ln}\n")
    return log_path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--providers-root", default=str(DEFAULT_PROVIDERS))
    ap.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    ap.add_argument("--dry-run", action="store_true",
                    help="Extract and print summary; do not write tracker.csv.")
    args = ap.parse_args()

    providers_root = Path(args.providers_root)
    out_dir = Path(args.out_dir)
    if not providers_root.is_dir():
        sys.exit(f"[fatal] providers root not found: {providers_root}")

    load_env(ENV_FILE)
    for k in ("AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT",
              "AZURE_OPENAI_DEPLOYMENT"):
        if not os.environ.get(k):
            sys.exit(f"[fatal] missing env var: {k}")
    client, deployment = make_client()

    image_suffixes = {".jpg", ".jpeg", ".png", ".webp"}
    files = sorted(
        f for f in providers_root.rglob("*")
        if f.is_file() and (f.suffix.lower() == ".pdf"
                            or f.suffix.lower() in image_suffixes)
    )

    print(f"[main] providers root: {providers_root}", flush=True)
    print(f"[main] out dir: {out_dir}", flush=True)
    print(f"[main] {len(files)} file(s) to parse; dry_run={args.dry_run}",
          flush=True)

    bill_seq: dict[int, int] = {}
    encounter_seq: dict[int, int] = {}
    bills: list[dict] = []
    events: list[str] = []

    for f in files:
        rel = f.relative_to(providers_root)
        print(f"\n[parse] {rel}", flush=True)
        try:
            if f.suffix.lower() == ".pdf":
                images = render_pdf_pages(f)
            else:
                images = [f.read_bytes()]
            if len(images) > MAX_PAGES:
                images = images[:MAX_PAGES]
            extracted = call_vision(client, deployment, images)
        except Exception as exc:
            msg = f"[skip] {rel}: {exc}"
            print(f"  {msg}", flush=True)
            events.append(msg)
            continue

        record = make_bill_record(extracted, f, bill_seq, encounter_seq, bills)
        if record is None:
            msg = f"[merge] {rel}: merged into existing bill"
            print(f"  {msg}", flush=True)
            events.append(msg)
            continue

        bills.append(record)
        msg = (f"[new] {record['bill_id']} {record['provider_name']!r} "
               f"acct={record['account_number']!r} "
               f"bal=${record['current_balance']} "
               f"next={record['next_action']} due={record['next_action_due']}")
        print(f"  {msg}", flush=True)
        events.append(f"{rel}: {msg}")

    print(f"\n[main] {len(bills)} unique bill(s) after dedup", flush=True)

    if args.dry_run:
        print("[main] dry-run: tracker.csv not written", flush=True)
        return 0

    csv_path = write_tracker(bills, out_dir)
    log_path = write_log(events, out_dir)
    print(f"[main] tracker: {csv_path}", flush=True)
    print(f"[main] log:     {log_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
