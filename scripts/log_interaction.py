"""log_interaction.py — append one row to the master action log.

Marshall Allen's discipline: every phone call, every email, every
in-person encounter with a biller or insurer gets logged. Date, who,
what they said, what they promised. The action log is the paper trail
that turns a dispute into evidence.

Writes to `<log-dir>/actions.csv` (default `~/.medbill-dispute-kit/
tracker/`, override via $HEALTHBILLS_LOG_DIR). The schema matches
`schemas/action.toml`. Action IDs auto-increment as A-YYYY-NNN. The
file is append-only; there's no edit mode. To correct a prior action,
add a new action with action_type = other and reference the prior
action_id in notes.

Usage:
    python log_interaction.py \\
        --bill-id B-abc1234567 \\
        --action phone_call_to_billing \\
        --recipient "Acme Hospital billing dept" \\
        --note "Spoke with Jane (rep ID 4421); she promised
                callback by Friday with itemization status"

    python log_interaction.py \\
        --bill-id B-abc1234567 \\
        --action records_request_sent \\
        --recipient "Acme Hospital HIM dept" \\
        --tracking 9405511899223345678901 \\
        --template templates/letter_records_request_hipaa.md \\
        --response-due 2026-06-20

The bill-id must already exist in tracker.csv; the script will refuse
to log against an unknown bill so you don't silently miss an entry by
typoing the ID.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import os
import re
import sys
from pathlib import Path

LOG_DIR = Path(
    os.environ.get("HEALTHBILLS_LOG_DIR")
    or (Path.home() / ".medbill-dispute-kit" / "tracker")
)
TRACKER_CSV = LOG_DIR / "tracker.csv"
ACTIONS_CSV = LOG_DIR / "actions.csv"

ACTION_COLUMNS = [
    "action_id", "bill_id", "action_type", "date",
    "recipient", "template_used", "certified_mail_tracking",
    "response_due_by", "amount_disputed", "amount_paid",
    "status", "outcome", "notes",
]

ACTION_TYPES = {
    "received_bill", "requested_itemization", "received_itemization",
    "phone_call_to_billing", "phone_call_to_insurance",
    "phone_call_to_billing_advocate", "phone_call_to_cfo",
    "initial_dispute_letter_sent", "no_surprises_letter_sent",
    "insurance_appeal_internal_sent", "insurance_appeal_external_sent",
    "30day_warning_sent", "state_doi_complaint_filed",
    "state_ag_complaint_filed", "cms_complaint_filed",
    "cms_hpt_complaint_filed", "ppdr_filed",
    "fdcpa_validation_request", "fap_application_submitted",
    "state_balance_billing_letter_sent", "ground_ambulance_letter_sent",
    "irs_501r_complaint_filed", "ebsa_intervention_request",
    "medicare_redetermination_filed", "medicare_reconsideration_filed",
    "medicare_alj_hearing_filed", "medicaid_mco_appeal_filed",
    "medicaid_fair_hearing_filed", "dental_appeal_filed",
    "emtala_complaint_filed", "ocr_hipaa_complaint_filed",
    "auto_med_pay_demand_sent", "force_health_insurance_billing",
    "hospital_lien_challenge", "wc_carrier_redirect_sent",
    "wc_appeal_filed", "wc_attorney_engaged",
    "small_claims_filed", "small_claims_hearing",
    "settlement_offered", "settlement_accepted",
    "payment_made", "writeoff_received",
    "sent_to_collections", "credit_report_dispute_filed",
    "records_request_sent", "records_received",
    "gfe_requested", "gfe_received",
    "idr_request_to_insurer", "subrogation_response_sent",
    "counter_offer_sent", "counter_offer_accepted",
    "counter_offer_rejected", "evidence_bundle_archived",
    "audit_finding_logged", "other",
}
STATUS_VALUES = {
    "completed", "awaiting_response", "response_received", "superseded",
}

ACTION_ID_RE = re.compile(r"^A-(\d{4})-(\d+)$")


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def next_action_id(year: int, existing: list[dict]) -> str:
    max_n = 0
    for row in existing:
        aid = (row.get("action_id") or "").strip()
        m = ACTION_ID_RE.match(aid)
        if m and int(m.group(1)) == year:
            n = int(m.group(2))
            if n > max_n:
                max_n = n
    return f"A-{year}-{max_n + 1:04d}"


def known_bill_ids() -> set[str]:
    return {r["bill_id"] for r in read_csv(TRACKER_CSV)
            if r.get("bill_id")}


def append_action(row: dict) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    write_header = not ACTIONS_CSV.exists()
    with ACTIONS_CSV.open("a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=ACTION_COLUMNS,
                           extrasaction="ignore")
        if write_header:
            w.writeheader()
        w.writerow({c: row.get(c, "") for c in ACTION_COLUMNS})


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--bill-id", required=True,
                    help="Bill identifier from tracker.csv (e.g., B-abc1234567).")
    ap.add_argument("--action", required=True,
                    help="action_type slug per schemas/action.toml")
    ap.add_argument("--recipient", default="",
                    help="Who the action was directed at.")
    ap.add_argument("--date", default="",
                    help="Action date (ISO 8601). Defaults to today.")
    ap.add_argument("--note", default="",
                    help="Free-text note describing the interaction.")
    ap.add_argument("--template", default="",
                    help="Template path if a letter was sent.")
    ap.add_argument("--tracking", default="",
                    help="USPS certified-mail tracking number.")
    ap.add_argument("--response-due", default="",
                    help="ISO date by which a response is expected.")
    ap.add_argument("--amount-disputed", default="",
                    help="USD amount contested by this action, if any.")
    ap.add_argument("--amount-paid", default="",
                    help="USD amount paid by this action, if any.")
    ap.add_argument("--status", default="completed",
                    help="completed | awaiting_response | "
                         "response_received | superseded "
                         "(default: completed)")
    ap.add_argument("--outcome", default="",
                    help="Brief outcome once response received.")
    ap.add_argument("--skip-bill-check", action="store_true",
                    help="Allow logging without validating bill_id "
                         "against tracker.csv (e.g., for actions on "
                         "encounter-wide events).")
    args = ap.parse_args()

    if args.action not in ACTION_TYPES:
        print(f"[fatal] unknown action_type '{args.action}'. "
              f"See schemas/action.toml for the full list.",
              flush=True)
        return 1

    if args.status not in STATUS_VALUES:
        print(f"[fatal] status must be one of {sorted(STATUS_VALUES)}",
              flush=True)
        return 1

    date_iso = args.date or datetime.date.today().isoformat()
    try:
        year = int(date_iso[:4])
    except ValueError:
        print(f"[fatal] could not parse year from --date {date_iso}",
              flush=True)
        return 1

    if not args.skip_bill_check:
        known = known_bill_ids()
        if not known:
            print(f"[fatal] no tracker.csv yet at {TRACKER_CSV}; "
                  f"run check_completeness.py first or pass "
                  f"--skip-bill-check", flush=True)
            return 1
        if args.bill_id not in known:
            print(f"[fatal] bill_id '{args.bill_id}' not in "
                  f"tracker.csv. Known IDs start with: "
                  f"{sorted(list(known))[:3]}...", flush=True)
            return 1

    existing = read_csv(ACTIONS_CSV)
    action_id = next_action_id(year, existing)

    row = {
        "action_id": action_id,
        "bill_id": args.bill_id,
        "action_type": args.action,
        "date": date_iso,
        "recipient": args.recipient,
        "template_used": args.template,
        "certified_mail_tracking": args.tracking,
        "response_due_by": args.response_due,
        "amount_disputed": args.amount_disputed,
        "amount_paid": args.amount_paid,
        "status": args.status,
        "outcome": args.outcome,
        "notes": args.note,
    }
    append_action(row)
    print(f"[logged] {action_id} {args.action} "
          f"bill={args.bill_id} -> {ACTIONS_CSV}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
