"""generate_cases_05_06.py, write synthetic EOB-mismatch and emergency-cost-share fixtures."""

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
    date_of_service: str,
    total_billed: str,
    current_balance: str,
    in_network_status: str,
    was_emergency: bool,
    findings: str,
    next_action: str,
    next_action_due: str,
    claim_number: str,
    has_itemization: bool,
) -> dict[str, object]:
    """Return the strictly named tracker fields populated by these synthetic cases."""
    return {
        "bill_id": bill_id, "encounter_id": encounter_id, "provider_name": provider_name,
        "provider_type": provider_type, "account_number": account_number,
        "statement_date": statement_date, "date_of_service_start": date_of_service,
        "date_of_service_end": date_of_service, "total_billed": total_billed,
        "current_balance": current_balance, "insurance_carrier": "Example Health Plan",
        "in_network_status": in_network_status, "was_emergency": was_emergency,
        "findings": findings, "next_action": next_action, "next_action_due": next_action_due,
        "last_action_taken": "received_bill", "last_action_date": statement_date,
        "certified_mail_last": "", "status": "open", "last_statement_date": statement_date,
        "has_eob": True, "matched_claim_numbers": claim_number,
        "has_itemization": has_itemization,
        "itemization_signals": "one_structured_charge_line" if has_itemization else "",
        "eob_request_sent_date": "", "eob_request_tracking": "",
        "itemization_request_sent_date": "", "itemization_request_tracking": "",
        "dispute_letter_sent_date": "", "dispute_letter_tracking": "",
        "thirty_day_warning_sent_date": "", "thirty_day_warning_tracking": "",
        "response_due_date": "", "drafted_eob_request": "", "drafted_itemization_request": "",
        "drafted_dispute_letter": "", "dispute_template_used": "",
        "benchmarks_available": "", "counter_offer_amount": "", "drafted_counter_offer": "",
        "counter_offer_sent_date": "", "counter_offer_tracking": "",
        "drafted_doi_complaint": "", "doi_complaint_sent_date": "", "doi_complaint_tracking": "",
        "doi_complaint_number": "", "drafted_small_claims_civil_warrant": "",
        "small_claims_filed_date": "", "small_claims_case_number": "", "small_claims_court": "",
        "drafted_hipaa_records_request": "",
        "notes": "Synthetic regression fixture; all names and identifiers are fictional.",
    }


def generate(output: Path) -> list[Path]:
    """Write cases 05 and 06 beneath the caller-provided data-root output directory."""
    mismatch_bill = {
        "bill_id": "B-2026-005", "encounter_id": "E-2026-005",
        "provider_name": "Example Regional Medical Center", "provider_type": "hospital",
        "provider_tax_id": "00-0000000", "account_number": "EX-000125",
        "patient_account_id": "PAT-000005", "statement_number": "STM0000005",
        "statement_date": "2026-08-15", "date_of_service_start": "2026-08-05",
        "date_of_service_end": "2026-08-05", "total_billed": "2000.00",
        "total_insurance_paid": "1500.00", "total_insurance_adjustment": "0.00",
        "total_patient_paid": "0.00", "current_balance": "500.00",
        "payment_due_date": "2026-08-29", "insurance_carrier": "Example Health Plan",
        "in_network_status": "in_network", "was_emergency": False,
        "contact_phone": "615-555-0100", "contact_address": "123 Example Street, Anytown, TN 37000",
        "payment_url": "https://example.invalid/pay", "cpt_codes": ["99214"],
        "line_items": [{"description": "Established office visit", "cpt_code": "99214", "charge": "2000.00", "units": 1, "date": "2026-08-05"}],
        "findings": ["no_findings"], "next_action": "initial_dispute", "next_action_due": "2026-08-29",
        "status": "open", "last_statement_date": "2026-08-15",
        "notes": "Synthetic bill shows $500.00 current balance; synthetic EOB shows $200.00 patient responsibility. No dedicated findings token exists for this EOB mismatch.",
    }
    mismatch_tracker = _tracker_row(
        bill_id="B-2026-005", encounter_id="E-2026-005", provider_name="Example Regional Medical Center",
        provider_type="hospital", account_number="EX-000125", statement_date="2026-08-15",
        date_of_service="2026-08-05", total_billed="2000.00", current_balance="500.00",
        in_network_status="in_network", was_emergency=False, findings="no_findings", next_action="initial_dispute",
        next_action_due="2026-08-29", claim_number="CLM0000005", has_itemization=True,
    )
    case_05 = write_case(
        output, "case_05_eob_mismatch", "Case 05: Synthetic bill and EOB patient-responsibility mismatch",
        [mismatch_bill], [mismatch_tracker], {
            "bill": """EXAMPLE REGIONAL MEDICAL CENTER
123 Example Street, Anytown, TN 37000 | BILLING PHONE: 615-555-0100
NPI: 0000000000 | EIN: 00-0000000
PATIENT: Alex Example | PATIENT ACCOUNT: PAT-000005
ACCOUNT: EX-000125 | STATEMENT: STM0000005
DATE OF SERVICE: 2026-08-05 | STATEMENT DATE: 2026-08-15
INSURER: Example Health Plan | NETWORK: In network | EMERGENCY: No
ITEMIZED SERVICE | CPT | UNITS | CHARGE
Established office visit | 99214 | 1 | $2,000.00
TOTAL BILLED: $2,000.00
INSURANCE PAID: $1,500.00
INSURANCE ADJUSTMENT: $0.00
PATIENT PAID: $0.00
CURRENT BALANCE: $500.00
PAY BY: 2026-08-29
PAYMENT PORTAL: https://example.invalid/pay""",
            "eob": """EXAMPLE HEALTH PLAN
123 Example Street, Anytown, TN 37000 | MEMBER ID: MEM0000005
EOB FOR: Alex Example | CLAIM: CLM0000005
PROVIDER: Example Regional Medical Center | DATE OF SERVICE: 2026-08-05
TOTAL BILLED: $2,000.00
PLAN PAID: $1,500.00
PLAN ADJUSTMENT: $300.00
PATIENT RESPONSIBILITY: $200.00
This synthetic EOB states a $200.00 patient responsibility, which differs from the synthetic bill's $500.00 current balance.""",
        },
        "Factual synthetic mismatch case: the bill shows $500.00 owed and the EOB shows $200.00 patient responsibility. The workflow uses initial_dispute because the bill schema has no dedicated EOB-mismatch finding token.",
    )

    emergency_bill = {
        "bill_id": "B-2026-006", "encounter_id": "E-2026-006",
        "provider_name": "Sample Emergency Physicians PLLC", "provider_type": "emergency_physician",
        "provider_tax_id": "00-0000000", "account_number": "EX-000126",
        "patient_account_id": "PAT-000006", "statement_number": "STM0000006",
        "statement_date": "2026-08-16", "date_of_service_start": "2026-08-06",
        "date_of_service_end": "2026-08-06", "total_billed": "3500.00",
        "total_insurance_paid": "0.00", "total_insurance_adjustment": "0.00",
        "total_patient_paid": "0.00", "current_balance": "3500.00",
        "payment_due_date": "2026-08-30", "insurance_carrier": "Example Health Plan",
        "in_network_status": "out_of_network", "was_emergency": True,
        "contact_phone": "615-555-0100", "contact_address": "123 Example Street, Anytown, TN 37000",
        "payment_url": "https://example.invalid/pay", "cpt_codes": ["99285"],
        "line_items": [{"description": "Emergency physician service", "cpt_code": "99285", "charge": "3500.00", "units": 1, "date": "2026-08-06"}],
        "findings": ["no_surprises_emergency"], "next_action": "dispute_no_surprises_violation",
        "next_action_due": "2026-08-30", "status": "open", "last_statement_date": "2026-08-16",
        "notes": "Synthetic coverage assumption: the EOB applies $200.00 in-network cost sharing to an out-of-network emergency physician claim; the bill separately shows a $3,500.00 balance.",
    }
    emergency_tracker = _tracker_row(
        bill_id="B-2026-006", encounter_id="E-2026-006", provider_name="Sample Emergency Physicians PLLC",
        provider_type="emergency_physician", account_number="EX-000126", statement_date="2026-08-16",
        date_of_service="2026-08-06", total_billed="3500.00", current_balance="3500.00",
        in_network_status="out_of_network", was_emergency=True, findings="no_surprises_emergency",
        next_action="dispute_no_surprises_violation", next_action_due="2026-08-30", claim_number="CLM0000006", has_itemization=True,
    )
    case_06 = write_case(
        output, "case_06_balance_bill_nsa", "Case 06: Synthetic out-of-network emergency bill and in-network EOB cost share",
        [emergency_bill], [emergency_tracker], {
            "bill": """SAMPLE EMERGENCY PHYSICIANS PLLC
123 Example Street, Anytown, TN 37000 | BILLING PHONE: 615-555-0100
NPI: 0000000000 | EIN: 00-0000000
PATIENT: Casey Testcase | PATIENT ACCOUNT: PAT-000006
ACCOUNT: EX-000126 | STATEMENT: STM0000006
DATE OF SERVICE: 2026-08-06 | STATEMENT DATE: 2026-08-16
INSURER: Example Health Plan | NETWORK: Out of network | EMERGENCY: Yes
ITEMIZED SERVICE | CPT | UNITS | CHARGE
Emergency physician service | 99285 | 1 | $3,500.00
TOTAL BILLED: $3,500.00
INSURANCE PAID: $0.00
INSURANCE ADJUSTMENT: $0.00
PATIENT PAID: $0.00
CURRENT BALANCE: $3,500.00
PAY BY: 2026-08-30
PAYMENT PORTAL: https://example.invalid/pay""",
            "eob": """EXAMPLE HEALTH PLAN
123 Example Street, Anytown, TN 37000 | MEMBER ID: MEM0000006
EOB FOR: Casey Testcase | CLAIM: CLM0000006
PROVIDER: Sample Emergency Physicians PLLC | DATE OF SERVICE: 2026-08-06
NETWORK STATUS: Out of network emergency physician
TOTAL BILLED: $3,500.00
PLAN ALLOWED AMOUNT: $1,000.00
PLAN PAID: $800.00
IN-NETWORK COST SHARING APPLIED: $200.00
PATIENT RESPONSIBILITY: $200.00
This synthetic EOB records an in-network cost-sharing assumption for this synthetic emergency claim.""",
        },
        "Factual synthetic emergency case: the bill identifies an out-of-network emergency physician, while the EOB records $200.00 in-network cost sharing. It supplies the existing no_surprises_emergency workflow token without making a legal conclusion in the source documents.",
    )
    return [case_05, case_06]


def main() -> None:
    """Write the two fixtures to the selected output directory."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    for path in generate(args.output):
        print(path)


if __name__ == "__main__":
    main()
