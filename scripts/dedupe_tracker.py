"""dedupe_tracker.py — post-process tracker.csv after an LLM extraction.

Normalizes provider names with the same alias map used in
classify_rename_medical_bills.py, dedupes more aggressively when the
extractor failed to read account numbers off collection notices and
follow-up statements, and drops informational documents that aren't
bills (NOT-A-BILL itemizations, language-assistance notices,
TennCare-Connect letters, payment-plan reminders, etc.).

Reads:  C:/Code_data/medbill-dispute-kit/tracker/tracker.csv
Writes: C:/Code_data/medbill-dispute-kit/tracker/tracker.csv (in place)
Backs up the input to tracker.csv.bak before overwriting.

Usage:
    python dedupe_tracker.py
    python dedupe_tracker.py --tracker <path>
    python dedupe_tracker.py --dry-run
"""

from __future__ import annotations

import argparse
import csv
import datetime
import re
import shutil
import sys
from pathlib import Path

DEFAULT_TRACKER = Path(r"C:\Code_data\medbill-dispute-kit\tracker\tracker.csv")

TRACKER_COLUMNS = [
    "bill_id", "encounter_id", "provider_name", "provider_type",
    "account_number", "statement_date", "date_of_service_start",
    "date_of_service_end", "total_billed", "current_balance",
    "insurance_carrier", "in_network_status", "was_emergency",
    "findings", "next_action", "next_action_due", "last_action_taken",
    "last_action_date", "certified_mail_last", "status",
    "last_statement_date", "notes",
]

# (regex, canonical_display_name)
PROVIDER_ALIASES: list[tuple[re.Pattern, str]] = [
    (re.compile(r"tristar|southern\s*hills\s*(med|medical)"),
     "TriStar Southern Hills Medical Center"),
    (re.compile(r"labcorp|laboratory\s+corporation"), "Labcorp"),
    (re.compile(r"premier\s+radiology"), "Premier Radiology"),
    (re.compile(r"centennial\s+heart"), "Centennial Heart at Southern Hills"),
    (re.compile(r"hospital\s+medicine\s+services"),
     "Hospital Medicine Services of TN"),
    (re.compile(r"emergency\s+medicine\s+services"),
     "Emergency Medicine Services of TN"),
    (re.compile(r"radiology\s+alliance"), "Radiology Alliance"),
    (re.compile(r"quantum\s+radiology"), "Quantum Radiology"),
    (re.compile(r"anova\s+medical"), "Anova Medical Associates"),
    (re.compile(r"wellstar"), "Wellstar Health System"),
    (re.compile(r"ascension\b"), "Ascension"),
    (re.compile(r"^humana"), "Humana"),
    (re.compile(r"^optum"), "Optum"),
    (re.compile(r"sage\s+dental"), "Sage Dental of Franklin"),
    (re.compile(r"tenncare"), "State of Tennessee Division of TennCare"),
]

# Drop a row outright when notes match any of these patterns.
DROP_PATTERNS: list[re.Pattern] = [
    re.compile(r"this\s+is\s+not\s+a\s+bill", re.I),
    re.compile(r"language\s+assistance", re.I),
    re.compile(r"nondiscrimination", re.I),
    re.compile(r"informational\s+notice", re.I),
    re.compile(r"payment\s+plan\s+reminder", re.I),
    re.compile(r"tenncare\s+connect", re.I),
]


def normalize_provider(name: str | None) -> str:
    if not name:
        return ""
    low = name.lower()
    for pattern, canonical in PROVIDER_ALIASES:
        if pattern.search(low):
            return canonical
    return name.strip()


def is_non_bill(row: dict) -> tuple[bool, str]:
    notes = row.get("notes") or ""
    for pat in DROP_PATTERNS:
        if pat.search(notes):
            return True, pat.pattern
    # Also drop rows that have no balance AND no total billed AND no DOS —
    # nothing to act on.
    if (not (row.get("current_balance") or "").strip()
            and not (row.get("total_billed") or "").strip()
            and not (row.get("date_of_service_start") or "").strip()):
        return True, "empty_balance_billed_dos"
    return False, ""


def coerce_float(v) -> float | None:
    if v is None or v == "":
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def dedup_key(row: dict) -> tuple:
    provider = normalize_provider(row.get("provider_name")).lower()
    acct = (row.get("account_number") or "").strip()
    dos = (row.get("date_of_service_start") or "").strip()
    bal = coerce_float(row.get("current_balance"))
    if acct:
        return ("acct", provider, acct)
    if dos and bal is not None:
        return ("dos_bal", provider, dos, round(bal, 2))
    if dos:
        return ("dos", provider, dos)
    if bal is not None:
        return ("bal", provider, round(bal, 2))
    return ("name_only", provider)


def merge_rows(a: dict, b: dict) -> dict:
    """Combine two duplicate rows. Prefer the row with later statement_date
    for live fields, but preserve any non-empty value from the other."""
    a_stmt = a.get("statement_date") or ""
    b_stmt = b.get("statement_date") or ""
    if b_stmt > a_stmt:
        primary, secondary = b, a
    else:
        primary, secondary = a, b
    merged = dict(primary)
    for col in TRACKER_COLUMNS:
        if not (merged.get(col) or "").strip():
            merged[col] = secondary.get(col, "")
    # last_statement_date: the maximum across both rows
    merged["last_statement_date"] = max(a_stmt, b_stmt,
                                        a.get("last_statement_date") or "",
                                        b.get("last_statement_date") or "")
    return merged


BILL_ID_RE = re.compile(r"^B-(\d{4})-(\d{3,})$")
ENCOUNTER_ID_RE = re.compile(r"^E-(\d{4})-(\d{3,})$")


def fill_missing_bill_ids(rows: list[dict]) -> None:
    """Preserve any existing B-YYYY-NNN id (so downstream references stay
    stable across runs). Only fill rows that have no id, using the year
    derived from the row's own statement_date or today's year as a
    fallback, and a number that does not collide with the existing
    highest id in that year."""
    by_year_max: dict[int, int] = {}
    for r in rows:
        m = BILL_ID_RE.match((r.get("bill_id") or "").strip())
        if m:
            y, n = int(m.group(1)), int(m.group(2))
            by_year_max[y] = max(by_year_max.get(y, 0), n)

    today_year = datetime.date.today().year
    for r in rows:
        if BILL_ID_RE.match((r.get("bill_id") or "").strip()):
            continue
        # Year preference: statement_date, then last_statement_date,
        # then DOS start, then today.
        year = today_year
        for col in ("statement_date", "last_statement_date",
                    "date_of_service_start"):
            v = (r.get(col) or "").strip()
            if len(v) >= 4 and v[:4].isdigit():
                year = int(v[:4])
                break
        by_year_max[year] = by_year_max.get(year, 0) + 1
        r["bill_id"] = f"B-{year}-{by_year_max[year]:03d}"


def fill_missing_encounter_ids(rows: list[dict]) -> None:
    """Preserve existing E-YYYY-NNN values. For rows missing one but with
    a date_of_service_start that already has an encounter assigned on a
    sibling row, reuse that sibling's encounter id. For genuinely new
    encounter dates, mint E-<year-of-dos>-<next> where <year-of-dos> is
    the year of the DOS itself, not today."""
    by_year_max: dict[int, int] = {}
    dos_to_encounter: dict[str, str] = {}
    for r in rows:
        eid = (r.get("encounter_id") or "").strip()
        m = ENCOUNTER_ID_RE.match(eid)
        if m:
            y, n = int(m.group(1)), int(m.group(2))
            by_year_max[y] = max(by_year_max.get(y, 0), n)
            dos = (r.get("date_of_service_start") or "").strip()
            if dos:
                dos_to_encounter.setdefault(dos, eid)

    for r in rows:
        if ENCOUNTER_ID_RE.match((r.get("encounter_id") or "").strip()):
            continue
        dos = (r.get("date_of_service_start") or "").strip()
        if not dos:
            r["encounter_id"] = ""
            continue
        if dos in dos_to_encounter:
            r["encounter_id"] = dos_to_encounter[dos]
            continue
        year = int(dos[:4]) if len(dos) >= 4 and dos[:4].isdigit() \
            else datetime.date.today().year
        by_year_max[year] = by_year_max.get(year, 0) + 1
        eid = f"E-{year}-{by_year_max[year]:03d}"
        r["encounter_id"] = eid
        dos_to_encounter[dos] = eid


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tracker", default=str(DEFAULT_TRACKER))
    ap.add_argument("--dry-run", action="store_true",
                    help="Print what would change without writing.")
    args = ap.parse_args()

    tracker = Path(args.tracker)
    if not tracker.exists():
        sys.exit(f"[fatal] tracker not found: {tracker}")

    with tracker.open(encoding="utf-8") as f:
        rows_in = list(csv.DictReader(f))
    print(f"[load] {len(rows_in)} rows from {tracker}", flush=True)

    dropped: list[tuple[dict, str]] = []
    kept: list[dict] = []
    for r in rows_in:
        is_drop, reason = is_non_bill(r)
        if is_drop:
            dropped.append((r, reason))
            continue
        kept.append(r)
    print(f"[filter] dropped {len(dropped)} non-bill row(s), "
          f"kept {len(kept)}", flush=True)
    for r, reason in dropped:
        print(f"  - {r.get('bill_id')} {r.get('provider_name')!r}  reason={reason}",
              flush=True)

    # Normalize provider names
    for r in kept:
        r["provider_name"] = normalize_provider(r.get("provider_name"))

    # Dedupe by key
    groups: dict[tuple, dict] = {}
    merges: list[tuple[str, str]] = []
    for r in kept:
        key = dedup_key(r)
        existing = groups.get(key)
        if not existing:
            groups[key] = r
            continue
        merged = merge_rows(existing, r)
        merges.append((existing.get("bill_id", "?"), r.get("bill_id", "?")))
        groups[key] = merged

    rows_out = sorted(
        groups.values(),
        key=lambda r: (r.get("provider_name") or "",
                       r.get("statement_date") or ""),
    )
    print(f"[dedup] merged {len(merges)} row(s); "
          f"{len(rows_out)} unique bill(s) remain", flush=True)
    for old_id, new_id in merges:
        print(f"  - merged {new_id} into {old_id}", flush=True)

    fill_missing_bill_ids(rows_out)
    fill_missing_encounter_ids(rows_out)

    if args.dry_run:
        print("[dry-run] no files written", flush=True)
        return 0

    backup = tracker.with_suffix(tracker.suffix + ".bak")
    shutil.copy2(tracker, backup)
    print(f"[backup] {backup}", flush=True)

    with tracker.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=TRACKER_COLUMNS, extrasaction="ignore")
        w.writeheader()
        for r in rows_out:
            w.writerow({col: r.get(col, "") for col in TRACKER_COLUMNS})

    print(f"[write] {tracker} ({len(rows_out)} rows)", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
