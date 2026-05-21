#!/usr/bin/env python3
"""
deadline_watch.py

Optional helper for medbill-dispute-kit. Reads a tracker CSV and reports
which bills have actions that are overdue, due in the next N days, or
imminently approaching. Standard library only; no external dependencies.

Usage:
    python deadline_watch.py path/to/tracker.csv
    python deadline_watch.py path/to/tracker.csv --window 14
    python deadline_watch.py path/to/tracker.csv --as-of 2026-06-01
    python deadline_watch.py path/to/tracker.csv --sol --state TN
    python deadline_watch.py path/to/tracker.csv --sol --state TN --sol-warn 365

By default the script considers `next_action_due` for every row. Output
is grouped: overdue first, then due-soon, then upcoming.

With --sol, the script additionally reports accounts whose written-contract
statute of limitations has expired (defendant can raise SOL as an
affirmative defense in any collection suit) or expires soon. SOL is
computed from the bill's earliest known statement_date plus the state's
written-contract SOL years per `references/sol_by_state.md`.

Exit codes:
    0 — no overdue items
    1 — one or more overdue items
    2 — usage error or file not found
"""

import argparse
import csv
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

# Written-contract SOL years per state, mirroring references/sol_by_state.md.
# Update both files together. The kit does not give legal advice; verify
# current statute before relying.
SOL_YEARS_WRITTEN_CONTRACT: dict[str, int] = {
    "AL": 6, "AK": 3, "AZ": 6, "AR": 5, "CA": 4, "CO": 6, "CT": 6,
    "DE": 3, "DC": 3, "FL": 5, "GA": 6, "HI": 6, "ID": 5, "IL": 10,
    "IN": 6, "IA": 10, "KS": 5, "KY": 10, "LA": 10, "ME": 6, "MD": 3,
    "MA": 6, "MI": 6, "MN": 6, "MS": 3, "MO": 10, "MT": 8, "NE": 5,
    "NV": 6, "NH": 3, "NJ": 6, "NM": 6, "NY": 6, "NC": 3, "ND": 6,
    "OH": 8, "OK": 5, "OR": 6, "PA": 4, "RI": 10, "SC": 3, "SD": 6,
    "TN": 6, "TX": 4, "UT": 6, "VT": 6, "VA": 5, "WA": 6, "WV": 10,
    "WI": 6, "WY": 10,
}
# State-specific shorter SOL overrides for facility / hospital medical debt
# when the state has carved out a separate rule (per sol_by_state.md notes).
SOL_OVERRIDES_FACILITY: dict[str, int] = {
    "FL": 3,  # HB 7089: 3 years on facility medical debt
}

# Expected response windows (in calendar days) for each mailed action.
# When the tracker has the corresponding *_sent_date populated and no
# resolution, the script computes the response deadline from the sent
# date plus the window. If the deadline is past, the bill is flagged.
RESPONSE_WINDOWS_DAYS: dict[str, tuple[str, int]] = {
    # column name -> (action description, days)
    "eob_request_sent_date":
        ("EOB request to insurer (ERISA § 1024(b)(4) 30-day rule)", 30),
    "itemization_request_sent_date":
        ("Itemization request to provider (state statutes; 30 days typical)", 30),
    "dispute_letter_sent_date":
        ("Initial dispute letter (kit standard: 15 business days)", 21),
    "counter_offer_sent_date":
        ("Counter-offer negotiation letter (kit standard: 30 days)", 30),
    "thirty_day_warning_sent_date":
        ("30-day warning before small claims", 30),
    "doi_complaint_sent_date":
        ("State DOI / AG complaint (most agencies acknowledge within 30 days, "
         "substantive response 30-90 days)", 45),
    "small_claims_filed_date":
        ("Small-claims filing (most counties set first court date 30-60 days out)", 45),
}


def parse_date(value: str) -> date | None:
    value = value.strip()
    if not value:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def load_tracker(csv_path: Path) -> list[dict]:
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def categorize(
    rows: list[dict],
    as_of: date,
    window_days: int,
) -> tuple[list[dict], list[dict], list[dict]]:
    """Return (overdue, due_soon, upcoming) lists."""
    overdue: list[dict] = []
    due_soon: list[dict] = []
    upcoming: list[dict] = []

    window_end = as_of + timedelta(days=window_days)

    for row in rows:
        due = parse_date(row.get("next_action_due", ""))
        if due is None:
            continue

        status = row.get("status", "").strip()
        if status in ("settled", "closed", "closed_resolved", "closed_paid", "closed_written_off"):
            continue

        days_remaining = (due - as_of).days
        item = {
            "bill_id": row.get("bill_id", ""),
            "provider": row.get("provider_name", ""),
            "next_action": row.get("next_action", ""),
            "due": due.isoformat(),
            "days": days_remaining,
            "balance": row.get("current_balance", ""),
        }

        if days_remaining < 0:
            overdue.append(item)
        elif days_remaining <= window_days:
            due_soon.append(item)
        else:
            upcoming.append(item)

    overdue.sort(key=lambda x: x["days"])
    due_soon.sort(key=lambda x: x["days"])
    upcoming.sort(key=lambda x: x["days"])
    return overdue, due_soon, upcoming


def format_group(title: str, items: list[dict]) -> str:
    if not items:
        return f"{title}: none\n"
    lines = [f"{title}:"]
    for item in items:
        days = item["days"]
        if days < 0:
            days_text = f"{-days} days ago"
        elif days == 0:
            days_text = "today"
        elif days == 1:
            days_text = "tomorrow"
        else:
            days_text = f"in {days} days"
        balance = f"${item['balance']}" if item['balance'] else "(no balance)"
        lines.append(
            f"  {item['bill_id']:>12}  {item['due']}  {days_text:<14}  "
            f"{item['next_action']:<32}  {balance:>10}  {item['provider']}"
        )
    return "\n".join(lines) + "\n"


def compute_response_status(
    rows: list[dict],
    as_of: date,
    warn_days: int,
) -> tuple[list[dict], list[dict]]:
    """Return (overdue_response, due_soon_response) lists keyed off the
    operational *_sent_date columns. The deadlines come from
    RESPONSE_WINDOWS_DAYS and are independent of the next_action_due
    column."""
    overdue: list[dict] = []
    due_soon: list[dict] = []
    for row in rows:
        status = (row.get("status") or "").strip()
        if status in ("settled", "closed", "closed_resolved",
                       "closed_paid", "closed_written_off",
                       "superseded"):
            continue
        for col, (desc, days) in RESPONSE_WINDOWS_DAYS.items():
            sent_value = (row.get(col) or "").strip()
            sent = parse_date(sent_value)
            if sent is None:
                continue
            # The user signals resolution by setting status to
            # resolved/settled etc. (handled above) or by clearing
            # the sent date. If a downstream sent date is also
            # populated (e.g., the user moved to the next step),
            # the earlier window is treated as superseded.
            deadline = sent + timedelta(days=days)
            days_remaining = (deadline - as_of).days
            item = {
                "bill_id": row.get("bill_id", ""),
                "provider": (row.get("provider_name", "")
                              or row.get("biller_name", "")),
                "action_column": col,
                "action_description": desc,
                "sent": sent.isoformat(),
                "deadline": deadline.isoformat(),
                "days": days_remaining,
                "balance": row.get("current_balance", ""),
            }
            if days_remaining < 0:
                overdue.append(item)
            elif days_remaining <= warn_days:
                due_soon.append(item)
    overdue.sort(key=lambda x: x["days"])
    due_soon.sort(key=lambda x: x["days"])
    return overdue, due_soon


def format_response_group(title: str, items: list[dict]) -> str:
    if not items:
        return f"{title}: none\n"
    lines = [f"{title}:"]
    for item in items:
        days = item["days"]
        if days < 0:
            days_text = f"{-days} days past"
        elif days == 0:
            days_text = "today"
        elif days == 1:
            days_text = "tomorrow"
        else:
            days_text = f"in {days} days"
        balance = f"${item['balance']}" if item['balance'] else "(no balance)"
        col = item["action_column"].replace("_sent_date", "")
        lines.append(
            f"  {item['bill_id']:>12}  sent {item['sent']}  "
            f"{col:<28} due {item['deadline']} ({days_text:<14})  "
            f"{balance:>10}  {item['provider']}"
        )
    return "\n".join(lines) + "\n"


def compute_sol_status(
    rows: list[dict],
    as_of: date,
    state_code: str,
    sol_warn_days: int,
    use_facility_rule: bool = False,
) -> tuple[list[dict], list[dict]]:
    """Return (expired, near_expiry) lists of SOL-aware items.

    SOL is computed from the earliest statement_date the kit can find for
    the row, plus the state's written-contract SOL years. Rows without a
    parseable statement_date are skipped. Settled / closed rows are skipped."""
    expired: list[dict] = []
    near: list[dict] = []
    state = (state_code or "").strip().upper()
    if not state:
        return expired, near
    years = SOL_YEARS_WRITTEN_CONTRACT.get(state)
    if not years:
        return expired, near
    if use_facility_rule and state in SOL_OVERRIDES_FACILITY:
        years = SOL_OVERRIDES_FACILITY[state]

    for row in rows:
        status = (row.get("status") or "").strip()
        if status in ("settled", "closed", "closed_resolved",
                       "closed_paid", "closed_written_off",
                       "superseded"):
            continue
        stmt = parse_date(row.get("statement_date", ""))
        if stmt is None:
            stmt = parse_date(row.get("dos_start", ""))
        if stmt is None:
            continue
        # Approximate SOL expiry: statement_date + N years.
        try:
            expiry = stmt.replace(year=stmt.year + years)
        except ValueError:
            # Handle Feb 29 + leap-year edge case.
            expiry = stmt.replace(year=stmt.year + years, day=28)
        days_remaining = (expiry - as_of).days
        item = {
            "bill_id": row.get("bill_id", ""),
            "provider": row.get("provider_name", "")
                        or row.get("biller_name", ""),
            "statement_date": stmt.isoformat(),
            "sol_expiry": expiry.isoformat(),
            "days": days_remaining,
            "balance": row.get("current_balance", ""),
            "state": state,
            "sol_years": years,
        }
        if days_remaining < 0:
            expired.append(item)
        elif days_remaining <= sol_warn_days:
            near.append(item)
    expired.sort(key=lambda x: x["days"])
    near.sort(key=lambda x: x["days"])
    return expired, near


def format_sol_group(title: str, items: list[dict]) -> str:
    if not items:
        return f"{title}: none\n"
    lines = [f"{title}:"]
    for item in items:
        days = item["days"]
        if days < 0:
            days_text = f"expired {-days} days ago"
        elif days == 0:
            days_text = "expires today"
        elif days == 1:
            days_text = "expires tomorrow"
        else:
            days_text = f"expires in {days} days"
        balance = f"${item['balance']}" if item['balance'] else "(no balance)"
        lines.append(
            f"  {item['bill_id']:>12}  stmt {item['statement_date']}  "
            f"SOL {item['sol_expiry']} ({item['state']}, "
            f"{item['sol_years']}y)  {days_text:<22}  "
            f"{balance:>10}  {item['provider']}"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("csv_path", help="Path to tracker CSV")
    parser.add_argument(
        "--window",
        type=int,
        default=7,
        help="Days ahead to consider as 'due soon' (default: 7)",
    )
    parser.add_argument(
        "--as-of",
        type=str,
        default=None,
        help="Date to evaluate against in YYYY-MM-DD (default: today)",
    )
    parser.add_argument(
        "--sol", action="store_true",
        help="Also report accounts whose written-contract SOL has "
             "expired or expires soon. Requires --state.",
    )
    parser.add_argument(
        "--state", default="",
        help="Two-letter state code (e.g. TN) for SOL calculation. "
             "Use the state where the patient resided AT THE TIME OF "
             "SERVICE, not where they reside now.",
    )
    parser.add_argument(
        "--sol-warn", type=int, default=180,
        help="Days ahead to surface accounts approaching SOL "
             "expiration (default: 180).",
    )
    parser.add_argument(
        "--sol-facility-rule", action="store_true",
        help="Use the state's facility-medical-debt SOL override if "
             "one exists (e.g., FL HB 7089's 3-year rule on hospital "
             "debt).",
    )
    args = parser.parse_args()

    csv_path = Path(args.csv_path).resolve()
    if not csv_path.exists():
        sys.stderr.write(f"file not found: {csv_path}\n")
        return 2

    if args.as_of:
        as_of = parse_date(args.as_of)
        if as_of is None:
            sys.stderr.write(f"invalid --as-of date: {args.as_of}\n")
            return 2
    else:
        as_of = date.today()

    try:
        rows = load_tracker(csv_path)
    except (OSError, csv.Error) as e:
        sys.stderr.write(f"error reading {csv_path}: {e}\n")
        return 2

    overdue, due_soon, upcoming = categorize(rows, as_of, args.window)
    resp_overdue, resp_due_soon = compute_response_status(
        rows, as_of, args.window,
    )

    print(f"Tracker: {csv_path.name}")
    print(f"As of:   {as_of.isoformat()}  (window: {args.window} days)\n")
    print(format_group("Overdue", overdue))
    print(format_group(f"Due in next {args.window} days", due_soon))
    print(format_group("Upcoming", upcoming))

    print("Response windows on mailed actions:\n")
    print(format_response_group("Response overdue", resp_overdue))
    print(format_response_group(
        f"Response due in next {args.window} days", resp_due_soon,
    ))

    sol_expired: list[dict] = []
    sol_near: list[dict] = []
    if args.sol:
        if not args.state:
            sys.stderr.write("--sol requires --state\n")
            return 2
        state_norm = args.state.strip().upper()
        if state_norm not in SOL_YEARS_WRITTEN_CONTRACT:
            sys.stderr.write(
                f"unknown state code: {args.state}. See "
                f"references/sol_by_state.md\n"
            )
            return 2
        sol_expired, sol_near = compute_sol_status(
            rows, as_of, state_norm, args.sol_warn,
            use_facility_rule=args.sol_facility_rule,
        )
        years = SOL_YEARS_WRITTEN_CONTRACT[state_norm]
        if args.sol_facility_rule and state_norm in SOL_OVERRIDES_FACILITY:
            years = SOL_OVERRIDES_FACILITY[state_norm]
        print(f"\nSOL (written contract, {state_norm}: {years} years; "
              f"facility-rule={args.sol_facility_rule}):\n")
        print(format_sol_group("SOL expired", sol_expired))
        print(format_sol_group(
            f"SOL within next {args.sol_warn} days", sol_near,
        ))
        if sol_expired:
            print(
                "Reminder: do not confirm the debt is yours and do not "
                "make a partial payment on an SOL-expired account "
                "without first researching your state's re-aging rule. "
                "Acknowledging or paying can restart the clock."
            )

    if overdue or resp_overdue:
        if overdue:
            print(f"\n{len(overdue)} bill(s) with overdue next_action.")
        if resp_overdue:
            print(f"{len(resp_overdue)} mailed action(s) past their "
                  f"expected response window.")
        return 1
    elif due_soon or resp_due_soon or sol_expired:
        if sol_expired:
            print(f"\n{len(sol_expired)} bill(s) past SOL.")
        if due_soon:
            print(f"{len(due_soon)} bill(s) due soon.")
        if resp_due_soon:
            print(f"{len(resp_due_soon)} mailed action(s) approaching "
                  f"response deadline.")
        return 0
    else:
        print("All clear.")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
