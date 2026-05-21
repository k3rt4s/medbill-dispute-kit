"""check_completeness.py — derive per-bill state by joining
Billers/<slug>/_bills.csv with the master matches.csv (in the log
directory, default ~/.medbill-dispute-kit/tracker/). Writes/updates
the master tracker.csv with one row per bill, including:

  - has_eob (Y/N) — derived from matches.csv
  - has_itemization (Y/N) — read from _bills.csv (set by indexer's
    peer-reviewed dated-charge-line heuristic)
  - current_status — gathering_evidence | ready_to_dispute |
    disputed | escalated | settled | closed
  - next_action — request_eob | request_itemization | draft_dispute |
    monitor | (and others depending on prior sent letters)
  - matched_claim_numbers — semicolon-joined list of EOB claim ids
    linked to this bill

The script PRESERVES user-supplied operational columns (sent dates,
certified-mail tracking numbers, manual notes) by merging on bill_id
when an existing tracker.csv is present. The script never overwrites
fields you've manually filled in.

Bill IDs are stable across runs: format `B-YYYY-NNN` where YYYY is
derived from the bill's statement_date (or DOS) and NNN is a hash of
biller_slug + filename. Same bill file -> same bill_id forever.

Usage:
   python check_completeness.py
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

HEALTH_ROOT = Path(
    os.environ.get("HEALTHBILLS_ROOT")
    or (Path.home() / "Health_Bills")
)
BILLERS_DIR = HEALTH_ROOT / "Billers"
LOG_DIR = Path(
    os.environ.get("HEALTHBILLS_LOG_DIR")
    or (Path.home() / ".medbill-dispute-kit" / "tracker")
)
TRACKER_CSV = LOG_DIR / "tracker.csv"
MATCHES_CSV = LOG_DIR / "matches.csv"

BILLS_FILENAME = "_bills.csv"

# Slugs whose folders should always derive `current_status = closed`
# rather than triggering dispute actions. Used for insurer / agency
# correspondence that is not a billable provider claim.
#
# This list is intentionally empty in the public kit. Populate it on
# your own workstation with slugs that are always-correspondence on
# YOUR plan (e.g. your plan's claims-processor slug, your Medicaid
# state agency slug, your COBRA administrator slug). The pipeline
# still works if you leave it empty — those rows just appear with a
# `gathering_evidence` status until you mark them resolved.
ALWAYS_SKIP_SLUGS: set[str] = set()

TRACKER_COLUMNS = [
    # Identity
    "bill_id", "biller_slug", "biller_name", "doc_type", "account_number",
    "file", "statement_date", "dos_start", "dos_end",
    "total_billed", "current_balance",
    # Evidence gates
    "has_eob", "matched_claim_numbers", "has_itemization",
    "itemization_signals",
    # Derived state
    "current_status", "next_action", "next_action_due",
    # Operational (preserved across runs)
    "eob_request_sent_date", "eob_request_tracking",
    "itemization_request_sent_date", "itemization_request_tracking",
    "dispute_letter_sent_date", "dispute_letter_tracking",
    "thirty_day_warning_sent_date", "thirty_day_warning_tracking",
    # Free text
    "response_due_date", "notes",
]


def make_bill_id(biller_slug: str, file_name: str,
                 statement_date: str, dos_start: str) -> str:
    """Build a stable bill_id from biller_slug + filename. The hash
    suffix is 8 hex chars (~4 billion buckets) so collisions across
    a realistic bill collection are vanishingly unlikely."""
    year = "0000"
    for cand in (statement_date, dos_start):
        if cand and len(cand) >= 4 and cand[:4].isdigit():
            year = cand[:4]
            break
    h = hashlib.sha1(f"{biller_slug}/{file_name}".encode()).hexdigest()
    return f"B-{year}-{h[:8]}"


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, columns: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in columns})


def load_bills() -> list[dict]:
    bills: list[dict] = []
    if not BILLERS_DIR.is_dir():
        return bills
    for slug_dir in sorted(d for d in BILLERS_DIR.iterdir() if d.is_dir()):
        bills_csv = slug_dir / BILLS_FILENAME
        for row in read_csv(bills_csv):
            row["biller_slug"] = slug_dir.name
            bills.append(row)
    return bills


def load_matches_by_bill() -> dict[str, list[dict]]:
    """Return {bill_file: [claim_match_rows]} for matches where a bill
    was linked to one or more claims."""
    matches = read_csv(MATCHES_CSV)
    by_bill: dict[str, list[dict]] = defaultdict(list)
    for m in matches:
        bill_file = m.get("bill_file", "").strip()
        if bill_file and m.get("match_type") in (
            "deterministic", "azure",
        ):
            by_bill[bill_file].append(m)
    return by_bill


def derive_status(has_eob: str, has_itemization: str,
                  sent_eob: str, sent_itemization: str,
                  sent_dispute: str, sent_warning: str,
                  doc_type: str, current_balance: str,
                  slug: str) -> tuple[str, str]:
    """Return (current_status, next_action)."""
    if slug in ALWAYS_SKIP_SLUGS:
        return "closed", "monitor"

    # Zero-balance doc → already settled or informational
    try:
        bal = float(current_balance) if current_balance else 0.0
    except (TypeError, ValueError):
        bal = 0.0
    if doc_type == "informational" or (bal == 0.0 and not sent_eob
                                       and not sent_itemization
                                       and not sent_dispute):
        return "closed", "monitor"

    have_eob = has_eob == "Y"
    have_item = has_itemization == "Y"

    # Already in dispute escalation
    if sent_warning:
        return "escalated", "await_response_or_file_small_claims"
    if sent_dispute:
        return "disputed", "await_response"

    if have_eob and have_item:
        return "ready_to_dispute", "draft_dispute"
    if not have_eob and not have_item:
        if sent_eob and sent_itemization:
            return "gathering_evidence", "await_eob_and_itemization"
        if sent_eob and not sent_itemization:
            return "gathering_evidence", "request_itemization"
        if not sent_eob and sent_itemization:
            return "gathering_evidence", "request_eob"
        return "gathering_evidence", "request_eob_and_itemization"
    if not have_eob:
        if sent_eob:
            return "gathering_evidence", "await_eob"
        return "gathering_evidence", "request_eob"
    if not have_item:
        if sent_itemization:
            return "gathering_evidence", "await_itemization"
        return "gathering_evidence", "request_itemization"
    return "gathering_evidence", "review"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.parse_args()

    bills = load_bills()
    matches_by_bill = load_matches_by_bill()
    existing = {r["bill_id"]: r for r in read_csv(TRACKER_CSV) if r.get("bill_id")}

    rows: list[dict] = []
    counters = {"new": 0, "preserved": 0, "skipped_no_data": 0}

    for bill in bills:
        biller_slug = bill.get("biller_slug", "")
        file_name = bill.get("file", "")
        if not biller_slug or not file_name:
            counters["skipped_no_data"] += 1
            continue
        statement_date = bill.get("statement_date", "")
        dos_start = bill.get("dos_start", "")
        bill_id = make_bill_id(biller_slug, file_name, statement_date, dos_start)

        claim_matches = matches_by_bill.get(file_name, [])
        has_eob = "Y" if claim_matches else "N"
        matched_claim_numbers = ";".join(
            sorted({m.get("claim_number", "") for m in claim_matches if m.get("claim_number")})
        )

        prior = existing.get(bill_id, {})
        sent_eob = prior.get("eob_request_sent_date", "")
        sent_item = prior.get("itemization_request_sent_date", "")
        sent_dispute = prior.get("dispute_letter_sent_date", "")
        sent_warning = prior.get("thirty_day_warning_sent_date", "")

        has_itemization = bill.get("has_itemization", "N") or "N"
        doc_type = bill.get("doc_type", "")

        status, next_action = derive_status(
            has_eob=has_eob,
            has_itemization=has_itemization,
            sent_eob=sent_eob, sent_itemization=sent_item,
            sent_dispute=sent_dispute, sent_warning=sent_warning,
            doc_type=doc_type, current_balance=bill.get("current_balance", ""),
            slug=biller_slug,
        )

        row = {
            "bill_id": bill_id,
            "biller_slug": biller_slug,
            "biller_name": bill.get("biller_name_raw", ""),
            "doc_type": doc_type,
            "account_number": bill.get("account_number", ""),
            "file": file_name,
            "statement_date": statement_date,
            "dos_start": dos_start,
            "dos_end": bill.get("dos_end", ""),
            "total_billed": bill.get("total_billed", ""),
            "current_balance": bill.get("current_balance", ""),
            "has_eob": has_eob,
            "matched_claim_numbers": matched_claim_numbers,
            "has_itemization": has_itemization,
            "itemization_signals": bill.get("itemization_signals", ""),
            "current_status": status,
            "next_action": next_action,
            "next_action_due": prior.get("next_action_due", ""),
            # Preserve user-set operational fields
            "eob_request_sent_date": sent_eob,
            "eob_request_tracking": prior.get("eob_request_tracking", ""),
            "itemization_request_sent_date": sent_item,
            "itemization_request_tracking": prior.get("itemization_request_tracking", ""),
            "dispute_letter_sent_date": sent_dispute,
            "dispute_letter_tracking": prior.get("dispute_letter_tracking", ""),
            "thirty_day_warning_sent_date": sent_warning,
            "thirty_day_warning_tracking": prior.get("thirty_day_warning_tracking", ""),
            "response_due_date": prior.get("response_due_date", ""),
            "notes": prior.get("notes", ""),
        }
        rows.append(row)
        counters["preserved" if bill_id in existing else "new"] += 1

    # Sort by biller_slug, then statement_date, then bill_id for stable output
    rows.sort(key=lambda r: (r["biller_slug"], r.get("statement_date") or "",
                              r["bill_id"]))

    write_csv(TRACKER_CSV, TRACKER_COLUMNS, rows)
    print(f"[done] {TRACKER_CSV}: {len(rows)} bills, {counters}",
          flush=True)
    # Print quick state breakdown
    from collections import Counter
    status_counts = Counter(r["current_status"] for r in rows)
    action_counts = Counter(r["next_action"] for r in rows)
    print("[status]", dict(status_counts), flush=True)
    print("[next_action]", dict(action_counts), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
