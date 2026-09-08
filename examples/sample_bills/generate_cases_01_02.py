"""Generate synthetic regression fixtures for sample-bill cases 01 and 02."""

from __future__ import annotations

import argparse
from pathlib import Path

from fixture_tools import DEFAULT_OUTPUT, write_case


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
        "last_statement_date": statement_date,
        "has_eob": has_eob,
        "matched_claim_numbers": matched_claim_numbers,
        "has_itemization": has_itemization,
        "itemization_signals": itemization_signals,
        "notes": "Synthetic regression fixture; all names and identifiers are fictional.",
    }


def generate(output: Path) -> list[Path]:
    """Write cases 01 and 02 beneath an explicit data-root output directory."""
    facility_lines = [
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
    facility_bill = {
        "bill_id": "B-2026-001",
        "encounter_id": "E-2026-001",
        "provider_name": "Example Regional Medical Center",
        "provider_type": "hospital",
        "provider_tax_id": "00-0000000",
        "account_number": "EX-000123",
        "patient_account_id": "PAT-000001",
        "statement_number": "STM0000001",
        "statement_date": "2026-08-10",
        "date_of_service_start": "2026-08-01",
        "date_of_service_end": "2026-08-01",
        "total_billed": 2490,
        "total_insurance_paid": 1000,
        "total_insurance_adjustment": 490,
        "total_patient_paid": 0,
        "current_balance": 1000,
        "payment_due_date": "2026-08-24",
        "insurance_carrier": "Example Health Plan",
        "in_network_status": "in_network",
        "was_emergency": True,
        "contact_phone": "615-555-0100",
        "contact_address": "123 Example Street, Anytown, TN 37000",
        "payment_url": "https://example.invalid/pay",
        "cpt_codes": ["99284", "71046", "80053"],
        "line_items": facility_lines,
        "findings": ["no_findings"],
        "next_action": "monitor",
        "next_action_due": "2026-08-24",
        "status": "open",
        "last_statement_date": "2026-08-10",
        "notes": "Synthetic itemized facility statement with a matching synthetic EOB.",
    }
    facility_tracker = _tracker_row(
        bill_id="B-2026-001",
        encounter_id="E-2026-001",
        provider_name="Example Regional Medical Center",
        provider_type="hospital",
        account_number="EX-000123",
        statement_date="2026-08-10",
        date_of_service_start="2026-08-01",
        date_of_service_end="2026-08-01",
        total_billed=2490,
        current_balance=1000,
        insurance_carrier="Example Health Plan",
        in_network_status="in_network",
        was_emergency=True,
        findings="no_findings",
        next_action="monitor",
        next_action_due="2026-08-24",
        has_eob=True,
        matched_claim_numbers="CLM0000001",
        has_itemization=True,
        itemization_signals="three_structured_charge_lines",
    )
    case_01 = write_case(
        output,
        "case_01_hospital_facility_itemized",
        "Case 01: Itemized hospital facility bill with matching EOB",
        [facility_bill],
        [facility_tracker],
        {
            "facility_bill": """EXAMPLE REGIONAL MEDICAL CENTER
123 Example Street, Anytown, TN 37000 | BILLING PHONE: 615-555-0100
NPI: 0000000000 | EIN: 00-0000000

PATIENT: Alex Example | PATIENT ACCOUNT: PAT-000001
ACCOUNT: EX-000123 | STATEMENT: STM0000001
DATE OF SERVICE: 2026-08-01 | STATEMENT DATE: 2026-08-10
INSURER: Example Health Plan | NETWORK: In network | EMERGENCY: Yes

UB-04 STYLE FACILITY CHARGES
REVENUE CODE | CPT | DESCRIPTION | UNITS | CHARGE
0450 | 99284 | Emergency department service | 1 | $1,850
0320 | 71046 | Chest radiology service | 1 | $412
0301 | 80053 | Comprehensive laboratory panel | 1 | $228

TOTAL BILLED: $2,490
INSURANCE PAID: $1,000
INSURANCE ADJUSTMENT: $490
PATIENT PAID: $0
CURRENT BALANCE: $1,000
PAY BY: 2026-08-24
PAYMENT PORTAL: https://example.invalid/pay""",
            "eob": """EXAMPLE HEALTH PLAN
123 Example Street, Anytown, TN 37000 | BILLING PHONE: 615-555-0100
EOB FOR: Alex Example | MEMBER ID: MEM0000001
CLAIM: CLM0000001 | PROVIDER: Example Regional Medical Center
DATE OF SERVICE: 2026-08-01

TOTAL BILLED: $2,490
PLAN PAID: $1,000
PLAN ADJUSTMENT: $490
PATIENT RESPONSIBILITY: $1,000

This synthetic EOB matches the facility statement's current balance.""",
        },
        "A fully itemized, in-network emergency facility statement. The synthetic EOB matches the $1,000 patient-responsibility amount and supports has_eob=true and has_itemization=true.",
    )

    summary_bill = {
        "bill_id": "B-2026-002",
        "encounter_id": "E-2026-002",
        "provider_name": "Example Regional Medical Center",
        "provider_type": "hospital",
        "provider_tax_id": "00-0000000",
        "account_number": "EX-000124",
        "patient_account_id": "PAT-000002",
        "statement_number": "STM0000002",
        "statement_date": "2026-08-11",
        "date_of_service_start": "2026-08-02",
        "date_of_service_end": "2026-08-02",
        "total_billed": 420,
        "current_balance": 420,
        "payment_due_date": "2026-08-25",
        "insurance_carrier": "Example Health Plan",
        "in_network_status": "unknown",
        "was_emergency": False,
        "contact_phone": "615-555-0100",
        "contact_address": "123 Example Street, Anytown, TN 37000",
        "payment_url": "https://example.invalid/pay",
        "findings": ["no_itemization"],
        "next_action": "request_itemization",
        "next_action_due": "2026-08-25",
        "status": "open",
        "last_statement_date": "2026-08-11",
        "notes": "Synthetic one-page summary statement with no itemized charge lines.",
    }
    summary_tracker = _tracker_row(
        bill_id="B-2026-002",
        encounter_id="E-2026-002",
        provider_name="Example Regional Medical Center",
        provider_type="hospital",
        account_number="EX-000124",
        statement_date="2026-08-11",
        date_of_service_start="2026-08-02",
        date_of_service_end="2026-08-02",
        total_billed=420,
        current_balance=420,
        insurance_carrier="Example Health Plan",
        in_network_status="unknown",
        was_emergency=False,
        findings="no_itemization",
        next_action="request_itemization",
        next_action_due="2026-08-25",
        has_eob=False,
        matched_claim_numbers="",
        has_itemization=False,
        itemization_signals="",
    )
    case_02 = write_case(
        output,
        "case_02_summary_no_itemization",
        "Case 02: Summary statement without itemization",
        [summary_bill],
        [summary_tracker],
        {
            "summary_statement": """EXAMPLE REGIONAL MEDICAL CENTER
123 Example Street, Anytown, TN 37000 | BILLING PHONE: 615-555-0100
NPI: 0000000000 | EIN: 00-0000000

PATIENT: Jordan Sample | PATIENT ACCOUNT: PAT-000002
ACCOUNT: EX-000124 | STATEMENT: STM0000002
DATE OF SERVICE: 2026-08-02 | STATEMENT DATE: 2026-08-11
INSURER: Example Health Plan | NETWORK: Unknown | EMERGENCY: No

SUMMARY STATEMENT
TOTAL BILLED: $420
CURRENT BALANCE: $420
PAY BY: 2026-08-25
PAYMENT PORTAL: https://example.invalid/pay

This summary statement contains no itemized services, CPT codes, revenue-code fields, units, or charge lines.""",
        },
        "A one-page synthetic summary statement with no itemized charge lines. It has no EOB document and supports has_eob=false and has_itemization=false.",
    )
    return [case_01, case_02]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    for path in generate(args.output):
        print(path)


if __name__ == "__main__":
    main()
