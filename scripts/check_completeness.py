"""check_completeness.py — derive per-bill state by joining
Billers/<slug>/_bills.csv with the master matches.csv (in the log
directory, default ~/.medbill-dispute-kit/tracker/). Writes/updates
the master tracker.csv with one row per bill, including:

  - has_eob (Y/N) — derived from matches.csv
  - has_itemization (Y/N) — read from _bills.csv (set by indexer's
    peer-reviewed dated-charge-line heuristic)
  - status — gathering_evidence | ready_to_dispute |
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
import datetime
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
BENCHMARKS_FILENAME = "_benchmarks.csv"
AUDIT_FILENAME = "_audit.csv"

# Audit finding_code -> controlled-vocabulary slug in bill.toml.
# Keep in sync with schemas/bill.toml findings.controlled_vocabulary.
AUDIT_FINDING_TO_SLUG: dict[str, str] = {
    "duplicate_cpt_same_bill": "duplicate_cpt_same_bill",
    "unbundling_ncci": "unbundling_ncci",
    "modifier_25_stacking": "modifier_25_stacking",
    "late_fee_or_finance_charge": "late_fee_or_finance_charge",
    "service_not_received_suspected": "service_not_received_suspected",
    "quantity_high": "quantity_inflation_suspected",
}

# Ratio above which a billed CPT is considered materially over Medicare and
# therefore eligible for the negotiated-counter-offer track. 1.50 = 150% of
# Medicare allowable. Most commercial insurers pay 100-250% of Medicare;
# patient-side amounts above 150% without contractual basis are facially
# negotiable per Marshall Allen's UCC § 2-305 framing.
COUNTER_OFFER_RATIO_THRESHOLD = 1.50

# Slugs whose folders should always derive `status = closed`
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
    "bill_id", "encounter_id",
    "biller_slug", "biller_name", "doc_type", "account_number",
    "file", "statement_date", "dos_start", "dos_end",
    "total_billed", "current_balance",
    # Evidence gates
    "has_eob", "matched_claim_numbers", "has_itemization",
    "itemization_signals", "benchmarks_available",
    "findings",
    # Derived state
    "status", "next_action", "next_action_due",
    # Operational (preserved across runs)
    "eob_request_sent_date", "eob_request_tracking",
    "itemization_request_sent_date", "itemization_request_tracking",
    "dispute_letter_sent_date", "dispute_letter_tracking",
    "thirty_day_warning_sent_date", "thirty_day_warning_tracking",
    "counter_offer_amount",
    "counter_offer_sent_date", "counter_offer_tracking",
    "doi_complaint_sent_date", "doi_complaint_tracking",
    "doi_complaint_number",
    "small_claims_filed_date", "small_claims_case_number",
    "small_claims_court",
    "drafted_hipaa_records_request",
    # Free text
    "response_due_date", "notes",
]


def make_bill_id(biller_slug: str, file_name: str) -> str:
    """Build a stable bill_id from biller_slug + filename only.

    No derived date is included in the id so that re-OCR runs that
    change statement_date / dos_start don't shift the id and break
    the merge of user-supplied operational fields (sent dates,
    tracking numbers, notes) across runs."""
    h = hashlib.sha1(f"{biller_slug}/{file_name}".encode()).hexdigest()
    return f"B-{h[:10]}"


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


_ISO_DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")


def parse_iso_date(s: str) -> datetime.date | None:
    if not s:
        return None
    m = _ISO_DATE_RE.match(s.strip())
    if not m:
        return None
    try:
        return datetime.date(int(m.group(1)), int(m.group(2)),
                             int(m.group(3)))
    except ValueError:
        return None


def assign_encounter_ids(rows: list[dict],
                          window_days: int = 1,
                          preserved: dict[str, str] | None = None
                          ) -> None:
    """Cluster rows by overlapping date-of-service windows and assign
    each cluster a stable encounter_id of the form E-YYYY-NNN, where
    YYYY is the cluster's earliest DOS year.

    Two rows belong to the same encounter when their effective DOS
    (dos_start, falling back to statement_date) are within +/-
    window_days of each other. Same-day visits to a hospital plus its
    contracted radiology + emergency-physician group will cluster;
    distinct unrelated services will not.

    Rows without any parseable date are not clustered and get no
    encounter_id (left empty).

    The `preserved` map preserves prior encounter_id assignments from
    tracker.csv across runs, so user-supplied encounter overrides
    survive."""
    if preserved is None:
        preserved = {}

    indexed: list[tuple[int, datetime.date]] = []
    for i, r in enumerate(rows):
        d = (parse_iso_date(r.get("dos_start", ""))
             or parse_iso_date(r.get("statement_date", "")))
        if d is None:
            continue
        indexed.append((i, d))

    indexed.sort(key=lambda t: t[1])
    cluster_for: dict[int, int] = {}
    next_cluster = 0
    last_date: datetime.date | None = None
    for i, d in indexed:
        if last_date is None or (d - last_date).days > window_days:
            next_cluster += 1
        cluster_for[i] = next_cluster
        last_date = d

    # Build cluster -> [row indices]
    members: dict[int, list[int]] = defaultdict(list)
    for i, c in cluster_for.items():
        members[c].append(i)

    counters: dict[int, int] = defaultdict(int)
    cluster_id_for: dict[int, str] = {}
    for c, idxs in members.items():
        # Honor any preserved id for this cluster — pick the first
        # bill_id with a prior encounter_id.
        prior_eid = ""
        for i in idxs:
            pid = preserved.get(rows[i].get("bill_id", ""), "")
            if pid:
                prior_eid = pid
                break
        if prior_eid:
            cluster_id_for[c] = prior_eid
            continue
        # Otherwise mint a new one from the cluster's earliest DOS year.
        earliest_year = min(parse_iso_date(rows[i].get("dos_start", ""))
                            or parse_iso_date(rows[i].get("statement_date", ""))
                            for i in idxs).year
        counters[earliest_year] += 1
        cluster_id_for[c] = (
            f"E-{earliest_year}-{counters[earliest_year]:03d}"
        )

    for i, c in cluster_for.items():
        rows[i]["encounter_id"] = cluster_id_for[c]


def load_audit_findings_by_bill() -> dict[tuple[str, str], set[str]]:
    """Return {(slug, file): {finding_slug, ...}} from _audit.csv per
    slug. Maps audit finding_codes to bill.toml controlled-vocabulary
    slugs via AUDIT_FINDING_TO_SLUG."""
    out: dict[tuple[str, str], set[str]] = defaultdict(set)
    if not BILLERS_DIR.is_dir():
        return out
    for slug_dir in BILLERS_DIR.iterdir():
        if not slug_dir.is_dir():
            continue
        audit = slug_dir / AUDIT_FILENAME
        if not audit.exists():
            continue
        for row in read_csv(audit):
            slug = slug_dir.name
            bill_file = (row.get("bill_file") or "").strip()
            code = (row.get("finding_code") or "").strip()
            slug_for = AUDIT_FINDING_TO_SLUG.get(code)
            if bill_file and slug_for:
                out[(slug, bill_file)].add(slug_for)
    return out


def load_benchmarks_by_slug() -> dict[str, bool]:
    """Return {biller_slug: has_overpriced_lines} where True means at
    least one CPT on a bill in this folder is billed at >= the counter
    offer ratio threshold over the Medicare allowable. Drives the
    benchmarks_available column on tracker.csv."""
    out: dict[str, bool] = {}
    if not BILLERS_DIR.is_dir():
        return out
    for slug_dir in sorted(d for d in BILLERS_DIR.iterdir() if d.is_dir()):
        bench = slug_dir / BENCHMARKS_FILENAME
        if not bench.exists():
            continue
        overpriced = False
        for row in read_csv(bench):
            try:
                ratio = float(row.get("ratio_billed_to_medicare") or 0)
            except ValueError:
                continue
            if ratio >= COUNTER_OFFER_RATIO_THRESHOLD:
                overpriced = True
                break
        out[slug_dir.name] = overpriced
    return out


def load_matches_by_bill() -> dict[tuple[str, str], list[dict]]:
    """Return {(biller_slug, bill_file): [claim_match_rows]} for matches
    where a bill was linked to one or more claims.

    Keyed by (slug, file) — not file alone — so basename collisions
    across slugs (e.g. two billers each having a "statement_v1.pdf")
    do not silently cross-link."""
    matches = read_csv(MATCHES_CSV)
    by_bill: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for m in matches:
        slug = (m.get("bill_slug") or "").strip()
        bill_file = (m.get("bill_file") or "").strip()
        if slug and bill_file and m.get("match_type") in (
            "deterministic", "azure",
        ):
            by_bill[(slug, bill_file)].append(m)
    return by_bill


def derive_status(has_eob: str, has_itemization: str,
                  benchmarks_available: str,
                  sent_eob: str, sent_itemization: str,
                  sent_dispute: str, sent_counter_offer: str,
                  sent_warning: str, sent_doi: str,
                  small_claims_filed: str,
                  doc_type: str, current_balance: str,
                  slug: str) -> tuple[str, str]:
    """Return (status, next_action)."""
    if slug in ALWAYS_SKIP_SLUGS:
        return "closed", "monitor"

    # Zero-balance doc → already settled or informational
    try:
        bal = float(current_balance) if current_balance else 0.0
    except (TypeError, ValueError):
        bal = 0.0
    if doc_type == "informational" or (bal == 0.0 and not sent_eob
                                       and not sent_itemization
                                       and not sent_dispute
                                       and not sent_counter_offer):
        return "closed", "monitor"

    have_eob = has_eob == "Y"
    have_item = has_itemization == "Y"
    have_benchmarks = benchmarks_available == "Y"

    # Already in court escalation
    if small_claims_filed:
        return "escalated", "await_court_date"
    # Already in pre-court escalation
    if sent_warning:
        # If a DOI complaint hasn't gone out yet, that's the parallel
        # next step before small claims; the warning gives a 15-day
        # window in which DOI pressure often moves things.
        if not sent_doi:
            return "escalated", "file_doi_complaint"
        return "escalated", "file_small_claims"
    # Counter-offer / dispute in flight
    if sent_counter_offer or sent_dispute:
        if not sent_doi:
            return "disputed", "file_doi_complaint"
        return "disputed", "await_response"

    if have_eob and have_item:
        # Prefer the price-benchmarked counter-offer track when the
        # bill is materially over Medicare. Falls back to the
        # template-picker dispute track when prices look reasonable.
        if have_benchmarks:
            return "ready_to_dispute", "negotiate_counter_offer"
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
    benchmarks_by_slug = load_benchmarks_by_slug()
    audit_findings_by_bill = load_audit_findings_by_bill()
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
        bill_id = make_bill_id(biller_slug, file_name)

        claim_matches = matches_by_bill.get((biller_slug, file_name), [])
        has_eob = "Y" if claim_matches else "N"
        matched_claim_numbers = ";".join(
            sorted({m.get("claim_number", "") for m in claim_matches
                    if m.get("claim_number")})
        )

        prior = existing.get(bill_id, {})
        sent_eob = prior.get("eob_request_sent_date", "")
        sent_item = prior.get("itemization_request_sent_date", "")
        sent_dispute = prior.get("dispute_letter_sent_date", "")
        sent_warning = prior.get("thirty_day_warning_sent_date", "")
        sent_counter_offer = prior.get("counter_offer_sent_date", "")
        sent_doi = prior.get("doi_complaint_sent_date", "")
        small_claims_filed = prior.get("small_claims_filed_date", "")

        raw_item = (bill.get("has_itemization") or "").strip().upper()
        has_itemization = "Y" if raw_item == "Y" else "N"
        benchmarks_available = (
            "Y" if benchmarks_by_slug.get(biller_slug) else "N"
        )
        doc_type = bill.get("doc_type", "")

        # Merge audit findings into the findings column. Preserve any
        # user-added findings present on the prior tracker row.
        audit_slugs = audit_findings_by_bill.get(
            (biller_slug, file_name), set(),
        )
        prior_findings = {
            f.strip()
            for f in (prior.get("findings") or "").split(";")
            if f.strip()
        }
        merged_findings = sorted(audit_slugs | prior_findings)

        status, next_action = derive_status(
            has_eob=has_eob,
            has_itemization=has_itemization,
            benchmarks_available=benchmarks_available,
            sent_eob=sent_eob, sent_itemization=sent_item,
            sent_dispute=sent_dispute,
            sent_counter_offer=sent_counter_offer,
            sent_warning=sent_warning, sent_doi=sent_doi,
            small_claims_filed=small_claims_filed,
            doc_type=doc_type, current_balance=bill.get("current_balance", ""),
            slug=biller_slug,
        )

        row = {
            "bill_id": bill_id,
            "encounter_id": prior.get("encounter_id", ""),
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
            "benchmarks_available": benchmarks_available,
            "findings": ";".join(merged_findings),
            "status": status,
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
            "counter_offer_amount": prior.get("counter_offer_amount", ""),
            "counter_offer_sent_date": sent_counter_offer,
            "counter_offer_tracking": prior.get("counter_offer_tracking", ""),
            "doi_complaint_sent_date": sent_doi,
            "doi_complaint_tracking": prior.get("doi_complaint_tracking", ""),
            "doi_complaint_number": prior.get("doi_complaint_number", ""),
            "small_claims_filed_date": small_claims_filed,
            "small_claims_case_number": prior.get("small_claims_case_number", ""),
            "small_claims_court": prior.get("small_claims_court", ""),
            "drafted_hipaa_records_request":
                prior.get("drafted_hipaa_records_request", ""),
            "response_due_date": prior.get("response_due_date", ""),
            "notes": prior.get("notes", ""),
        }
        rows.append(row)
        counters["preserved" if bill_id in existing else "new"] += 1

    # Assign encounter_ids by clustering bills with adjacent DOS.
    preserved_encounters = {
        bid: row.get("encounter_id", "")
        for bid, row in existing.items()
        if row.get("encounter_id")
    }
    assign_encounter_ids(rows, window_days=1,
                          preserved=preserved_encounters)

    # Sort by biller_slug, then statement_date, then bill_id for stable output
    rows.sort(key=lambda r: (r["biller_slug"], r.get("statement_date") or "",
                              r["bill_id"]))

    write_csv(TRACKER_CSV, TRACKER_COLUMNS, rows)
    print(f"[done] {TRACKER_CSV}: {len(rows)} bills, {counters}",
          flush=True)
    # Print quick state breakdown
    from collections import Counter
    status_counts = Counter(r["status"] for r in rows)
    action_counts = Counter(r["next_action"] for r in rows)
    print("[status]", dict(status_counts), flush=True)
    print("[next_action]", dict(action_counts), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
