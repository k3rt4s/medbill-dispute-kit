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

By default the script considers `next_action_due` for every row. Output
is grouped: overdue first, then due-soon, then upcoming.

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

    print(f"Tracker: {csv_path.name}")
    print(f"As of:   {as_of.isoformat()}  (window: {args.window} days)\n")
    print(format_group("Overdue", overdue))
    print(format_group(f"Due in next {args.window} days", due_soon))
    print(format_group("Upcoming", upcoming))

    if overdue:
        print(f"{len(overdue)} bill(s) overdue. Take action.")
        return 1
    elif due_soon:
        print(f"{len(due_soon)} bill(s) due soon.")
        return 0
    else:
        print("All clear.")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
