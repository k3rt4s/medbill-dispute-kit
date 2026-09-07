"""Generate synthetic regression fixtures for sample-bill cases 03 and 04."""

from __future__ import annotations

import argparse
from pathlib import Path

from fixture_tools import DEFAULT_OUTPUT, write_case


SYNTHETIC_NOTE = "Synthetic regression fixture; all names and identifiers are fictional."
CASE_01_FACILITY_LINES = [
    {
        "description": "Revenue 0450 emergency department; CPT 99284",
        "cpt_code": "99284",
        "charge": 1850,
        "units": 1,
        "date": "2026-08-01",
    },
    {
        "description": "Revenue 0320 radiology; CPT 71046",
        "cpt_code": "71046",
        "charge": 412,
        "units": 1,
        "date": "2026-08-01",
    },
    {
        "description": "Revenue 0301 laboratory; CPT 80053",
        "cpt_code": "80053",
        "charge": 228,
        "units": 1,
        "date": "2026-08-01",
    },
]


def _tracker_row(
    *,
    bill_id: str,
    encounter_id: str,
    provider_name: str,
    provider_type: str,
    account_number: str,
    statement_date: str,
    date_of_service_start: str,
    date_of_service_end: str,
    total_billed: int,
    current_balance: int,
    insurance_carrier: str,
    in_network_status: str,
    was_emergency: bool,
    findings: str,
    next_action: str,
    next_action_due: str,
    has_eob: bool,
    matched_claim_numbers: str,
    has_itemization: bool,
    itemization_signals: str,
    last_statement_date: str,
) -> dict:
    """Return only fields defined by tracker/tracker_template.csv."""
    return {
        "bill_id": bill_id,
        "encounter_id": encounter_id,
        "provider_name": provider_name,
        "provider_type": provider_type,
        "account_number": account_number,
        "statement_date": statement_date,
        "date_of_service_start": date_of_service_start,
        "date_of_service_end": date_of_service_end,
        "total_billed": total_billed,
        "current_balance": current_balance,
        "insurance_carrier": insurance_carrier,
        "in_network_status": in_network_status,
        "was_emergency": was_emergency,
        "findings": findings,
        "next_action": next_action,
        "next_action_due": next_action_due,
        "status": "open",
        "last_statement_date": last_statement_date,
        "has_eob": has_eob,
        "matched_claim_numbers": matched_claim_numbers,
        "has_itemization": has_itemization,
        "itemization_signals": itemization_signals,
        "notes": SYNTHETIC_NOTE,
    }


def generate(output: Path) -> list[Path]:
    """Write cases 03 and 04 beneath an explicit data-root output directory."""
    encounter_id = "E-2026-003"
    case_03_bills = [
        {
            "bill_id": "B-2026-003",
            "encounter_id": encounter_id,
            "provider_name": "Example Regional Medical Center",
            "provider_type": "hospital",
            "provider_tax_id": "00-0000000",
            "account_number": "EX-000125",
            "patient_account_id": "PAT-000003",
            "statement_number": "STM0000003",
            "statement_date": "2026-08-12",
            "date_of_service_start": "2026-08-03",
            "date_of_service_end": "2026-08-03",
            "total_billed": 1800,
            "current_balance": 1800,
            "payment_due_date": "2026-08-26",
            "insurance_carrier": "Example Health Plan",
            "in_network_status": "in_network",
            "was_emergency": True,
            "contact_phone": "615-555-0100",
            "contact_address": "123 Example Street, Anytown, TN 37000",
            "payment_url": "https://example.invalid/pay",
            "cpt_codes": ["99284"],
            "line_items": [
                {
                    "description": "Revenue 0450 emergency department; CPT 99284",
                    "cpt_code": "99284",
                    "charge": 1800,
                    "units": 1,
                    "date": "2026-08-03",
                },
            ],
            "findings": ["no_findings"],
            "next_action": "monitor",
            "next_action_due": "2026-08-26",
            "status": "open",
            "last_statement_date": "2026-08-12",
            "notes": SYNTHETIC_NOTE,
        },
        {
            "bill_id": "B-2026-004",
            "encounter_id": encounter_id,
            "provider_name": "Sample Emergency Physicians PLLC",
            "provider_type": "emergency_physician",
            "provider_tax_id": "00-0000000",
            "account_number": "EX-000126",
            "patient_account_id": "PAT-000003",
            "statement_number": "STM0000004",
            "statement_date": "2026-08-12",
            "date_of_service_start": "2026-08-03",
            "date_of_service_end": "2026-08-03",
            "total_billed": 640,
            "current_balance": 640,
            "payment_due_date": "2026-08-26",
            "insurance_carrier": "Example Health Plan",
            "in_network_status": "in_network",
            "was_emergency": True,
            "contact_phone": "615-555-0100",
            "contact_address": "123 Example Street, Anytown, TN 37000",
            "payment_url": "https://example.invalid/pay",
            "cpt_codes": ["99284"],
            "line_items": [
                {
                    "description": "Emergency physician professional service; CPT 99284",
                    "cpt_code": "99284",
                    "charge": 640,
                    "units": 1,
                    "date": "2026-08-03",
                },
            ],
            "findings": ["no_findings"],
            "next_action": "monitor",
            "next_action_due": "2026-08-26",
            "status": "open",
            "last_statement_date": "2026-08-12",
            "notes": SYNTHETIC_NOTE,
        },
        {
            "bill_id": "B-2026-005",
            "encounter_id": encounter_id,
            "provider_name": "Testcase Radiology Associates",
            "provider_type": "radiology",
            "provider_tax_id": "00-0000000",
            "account_number": "EX-000127",
            "patient_account_id": "PAT-000003",
            "statement_number": "STM0000005",
            "statement_date": "2026-08-12",
            "date_of_service_start": "2026-08-03",
            "date_of_service_end": "2026-08-03",
            "total_billed": 412,
            "current_balance": 412,
            "payment_due_date": "2026-08-26",
            "insurance_carrier": "Example Health Plan",
            "in_network_status": "in_network",
            "was_emergency": True,
            "contact_phone": "615-555-0100",
            "contact_address": "123 Example Street, Anytown, TN 37000",
            "payment_url": "https://example.invalid/pay",
            "cpt_codes": ["71046"],
            "line_items": [
                {
                    "description": "Radiology interpretation; CPT 71046",
                    "cpt_code": "71046",
                    "charge": 412,
                    "units": 1,
                    "date": "2026-08-03",
                },
            ],
            "findings": ["no_findings"],
            "next_action": "monitor",
            "next_action_due": "2026-08-26",
            "status": "open",
            "last_statement_date": "2026-08-12",
            "notes": SYNTHETIC_NOTE,
        },
    ]
    case_03_trackers = [
        _tracker_row(
            bill_id=bill["bill_id"],
            encounter_id=encounter_id,
            provider_name=bill["provider_name"],
            provider_type=bill["provider_type"],
            account_number=bill["account_number"],
            statement_date=bill["statement_date"],
            date_of_service_start=bill["date_of_service_start"],
            date_of_service_end=bill["date_of_service_end"],
            total_billed=bill["total_billed"],
            current_balance=bill["current_balance"],
            insurance_carrier=bill["insurance_carrier"],
            in_network_status=bill["in_network_status"],
            was_emergency=bill["was_emergency"],
            findings="no_findings",
            next_action="monitor",
            next_action_due="2026-08-26",
            has_eob=False,
            matched_claim_numbers="",
            has_itemization=True,
            itemization_signals="one_structured_charge_line",
            last_statement_date=bill["statement_date"],
        )
        for bill in case_03_bills
    ]
    case_03 = write_case(
        output,
        "case_03_multi_provider_encounter",
        "Case 03: Three separate bills for one synthetic emergency encounter",
        case_03_bills,
        case_03_trackers,
        {
            "01_facility_bill": """EXAMPLE REGIONAL MEDICAL CENTER
123 Example Street, Anytown, TN 37000 | BILLING PHONE: 615-555-0100
NPI: 0000000000 | EIN: 00-0000000

PATIENT: Casey Testcase | PATIENT ACCOUNT: PAT-000003
ACCOUNT: EX-000125 | STATEMENT: STM0000003
ENCOUNTER: E-2026-003 | DATE OF SERVICE: 2026-08-03 | STATEMENT DATE: 2026-08-12
INSURER: Example Health Plan | NETWORK: In network | EMERGENCY: Yes

REVENUE CODE | CPT | DESCRIPTION | UNITS | CHARGE
0450 | 99284 | Emergency department facility service | 1 | $1,800

TOTAL BILLED: $1,800
CURRENT BALANCE: $1,800
PAY BY: 2026-08-26
PAYMENT PORTAL: https://example.invalid/pay""",
            "02_emergency_bill": """SAMPLE EMERGENCY PHYSICIANS PLLC
123 Example Street, Anytown, TN 37000 | BILLING PHONE: 615-555-0100
NPI: 0000000000 | EIN: 00-0000000

PATIENT: Casey Testcase | PATIENT ACCOUNT: PAT-000003
ACCOUNT: EX-000126 | STATEMENT: STM0000004
ENCOUNTER: E-2026-003 | DATE OF SERVICE: 2026-08-03 | STATEMENT DATE: 2026-08-12
INSURER: Example Health Plan | NETWORK: In network | EMERGENCY: Yes

CPT | DESCRIPTION | UNITS | CHARGE
99284 | Emergency physician professional service | 1 | $640

TOTAL BILLED: $640
CURRENT BALANCE: $640
PAY BY: 2026-08-26
PAYMENT PORTAL: https://example.invalid/pay""",
            "03_radiology_bill": """TESTCASE RADIOLOGY ASSOCIATES
123 Example Street, Anytown, TN 37000 | BILLING PHONE: 615-555-0100
NPI: 0000000000 | EIN: 00-0000000

PATIENT: Casey Testcase | PATIENT ACCOUNT: PAT-000003
ACCOUNT: EX-000127 | STATEMENT: STM0000005
ENCOUNTER: E-2026-003 | DATE OF SERVICE: 2026-08-03 | STATEMENT DATE: 2026-08-12
INSURER: Example Health Plan | NETWORK: In network | EMERGENCY: Yes

CPT | DESCRIPTION | UNITS | CHARGE
71046 | Radiology interpretation | 1 | $412

TOTAL BILLED: $412
CURRENT BALANCE: $412
PAY BY: 2026-08-26
PAYMENT PORTAL: https://example.invalid/pay""",
        },
        "Three separately billed providers share one synthetic emergency date and encounter identifier. The unique bill IDs and account numbers mean the records link by encounter without merging.",
    )

    followup_bill = {
        "bill_id": "B-2026-001",
        "encounter_id": "E-2026-001",
        "provider_name": "Example Regional Medical Center",
        "provider_type": "hospital",
        "provider_tax_id": "00-0000000",
        "account_number": "EX-000123",
        "patient_account_id": "PAT-000001",
        "statement_number": "STM0000006",
        "statement_date": "2026-09-01",
        "date_of_service_start": "2026-08-01",
        "date_of_service_end": "2026-08-01",
        "total_billed": 2490,
        "total_insurance_paid": 1000,
        "total_insurance_adjustment": 490,
        "total_patient_paid": 250,
        "current_balance": 750,
        "payment_due_date": "2026-09-15",
        "insurance_carrier": "Example Health Plan",
        "in_network_status": "in_network",
        "was_emergency": True,
        "contact_phone": "615-555-0100",
        "contact_address": "123 Example Street, Anytown, TN 37000",
        "payment_url": "https://example.invalid/pay",
        "cpt_codes": ["99284", "71046", "80053"],
        "line_items": CASE_01_FACILITY_LINES,
        "findings": ["follow_up_statement_only"],
        "next_action": "monitor",
        "next_action_due": "2026-09-15",
        "status": "open",
        "last_statement_date": "2026-09-01",
        "notes": "Synthetic follow-up statement for the same account as case 01; matching synthetic EOB is in case 01.",
    }
    followup_tracker = _tracker_row(
        bill_id="B-2026-001",
        encounter_id="E-2026-001",
        provider_name="Example Regional Medical Center",
        provider_type="hospital",
        account_number="EX-000123",
        statement_date="2026-09-01",
        date_of_service_start="2026-08-01",
        date_of_service_end="2026-08-01",
        total_billed=2490,
        current_balance=750,
        insurance_carrier="Example Health Plan",
        in_network_status="in_network",
        was_emergency=True,
        findings="follow_up_statement_only",
        next_action="monitor",
        next_action_due="2026-09-15",
        has_eob=True,
        matched_claim_numbers="CLM0000001",
        has_itemization=True,
        itemization_signals="three_structured_charge_lines",
        last_statement_date="2026-09-01",
    )
    case_04 = write_case(
        output,
        "case_04_followup_statement",
        "Case 04: Follow-up statement for case 01 account",
        [followup_bill],
        [followup_tracker],
        {
            "04_followup_statement": """EXAMPLE REGIONAL MEDICAL CENTER
123 Example Street, Anytown, TN 37000 | BILLING PHONE: 615-555-0100
NPI: 0000000000 | EIN: 00-0000000

PATIENT: Alex Example | PATIENT ACCOUNT: PAT-000001
ACCOUNT: EX-000123 | STATEMENT: STM0000006
ENCOUNTER: E-2026-001 | DATE OF SERVICE: 2026-08-01 | STATEMENT DATE: 2026-09-01
INSURER: Example Health Plan | NETWORK: In network | EMERGENCY: Yes

ITEMIZED SERVICES FROM PRIOR STATEMENT
REVENUE CODE | CPT | DESCRIPTION | UNITS | CHARGE
0450 | 99284 | Emergency department service | 1 | $1,850
0320 | 71046 | Chest radiology service | 1 | $412
0301 | 80053 | Comprehensive laboratory panel | 1 | $228

ACCOUNT LEDGER
TOTAL BILLED: $2,490
INSURANCE PAID: $1,000
INSURANCE ADJUSTMENT: $490
PATIENT PAYMENT APPLIED: $250
CURRENT BALANCE: $750
PAY BY: 2026-09-15
PAYMENT PORTAL: https://example.invalid/pay

This synthetic follow-up statement has no EOB document in this case. The matching synthetic EOB is case 01 claim CLM0000001.""",
        },
        "A later synthetic statement for the exact same account and encounter as case 01. It retains the exact case-01 line-item set and records a partial patient payment. No EOB document is included here; tracker evidence points to case 01 claim CLM0000001. The fixture expects has_itemization=true even if a current detector misses it; that detector behavior is a known bug and this fixture does not change its rendering to work around it.",
    )
    return [case_03, case_04]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    for path in generate(args.output):
        print(path)


if __name__ == "__main__":
    main()
