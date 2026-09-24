"""generate_fixtures.py, write the classify_rename AG3 eval's synthetic PDFs and image under a data-root output directory, never inside the repo.

Regenerates the six inputs described in `cases/*/expected.md` (each expected.md
carries the exact source text as a record, so the case is legible without the
binary). Mirrors `examples/sample_bills/fixture_tools.py`'s rule: this repo's
`.gitignore` blocks every `*.pdf`/`*.jpg` unconditionally so there is never a
question of which PDF in the tree is real, so generated fixtures are written
outside the repo instead of being force-added past that guard.

Usage:
    python generate_fixtures.py
    python generate_fixtures.py --output <path outside the repo>
"""

from __future__ import annotations

import argparse
import random
from pathlib import Path

import pymupdf

DEFAULT_OUTPUT = Path("C:/Code_data/medbill-dispute-kit/evals/classify_rename/cases")

# Keep in sync with the "Source text" block in each case's expected.md.
CASES: dict[str, list[str]] = {
    "01_hospital_bill": [
        "TRISTAR SOUTHERN HILLS MEDICAL CENTER",
        "Patient Billing Statement",
        "",
        "Patient: Marisol J. Quintero (synthetic test patient)",
        "Account Number: TSH-88214-SYN",
        "Statement Date: 2026-06-14",
        "Service Date: 2026-05-30",
        "",
        "Description                          Amount",
        "Emergency Dept Level 4 visit          $2,140.00",
        "Insurance Adjustment                 -$1,540.00",
        "Insurance Payment                      -$400.00",
        "",
        "AMOUNT DUE FROM PATIENT: $200.00",
        "",
        "Please remit payment within 30 days.",
    ],
    "02_collection_notice": [
        "LABCORP",
        "Laboratory Corporation of America",
        "",
        "NOTICE OF COLLECTION REFERRAL",
        "",
        "Patient: Devon R. Achebe (synthetic test patient)",
        "Account Number: LC-SYN-550219",
        "Original Service Date: 2026-02-11",
        "Referral Date: 2026-06-01",
        "",
        "Your account balance of $340.00 for laboratory services has been",
        "referred to Meridian Recovery Associates for collection.",
        "",
        "BALANCE REFERRED: $340.00",
    ],
    "03_cobra_notice": [
        "HUMANA COBRA ADMINISTRATION",
        "",
        "COBRA CONTINUATION COVERAGE PREMIUM NOTICE",
        "",
        "Former Employee: Priya S. Nakamura (synthetic test patient)",
        "Election ID: COBRA-SYN-77042",
        "Coverage Period: 2026-07-01 to 2026-07-31",
        "",
        "Monthly COBRA Premium Due: $687.50",
        "Due Date: 2026-06-20",
        "",
        "Nonpayment by the due date will result in loss of continuation",
        "coverage.",
    ],
    "04_dental_predetermination": [
        "SAGE DENTAL INSURANCE SERVICES",
        "",
        "PREDETERMINATION OF BENEFITS",
        "",
        "Patient: Owen T. Fitzgerald (synthetic test patient)",
        "Reference Number: SAGE-SYN-19935",
        "Requested Procedure: Crown, porcelain/ceramic (D2740)",
        "Provider: Brightpath Family Dental",
        "",
        "This is NOT a bill. This estimate shows anticipated coverage",
        "if the procedure above is performed within 90 days.",
        "",
        "Estimated Plan Payment: $410.00",
        "Estimated Patient Responsibility: $290.00",
    ],
    "05_eob_non_bill": [
        "OPTUM HEALTH INSURANCE",
        "",
        "EXPLANATION OF BENEFITS",
        "",
        "This is a summary of how your claim was processed.",
        "THIS IS NOT A BILL.",
        "",
        "Subscriber: Renata L. Voss (synthetic test patient)",
        "Claim Number: OPT-SYN-402188",
        "Date of Service: 2026-04-02",
        "Provider: Centennial Heart Associates",
        "",
        "Billed Amount:        $1,800.00",
        "Plan Discount:          -$950.00",
        "Plan Paid:              -$850.00",
        "Patient Responsibility:      $0.00",
        "",
        "If you believe this claim was processed incorrectly, you have",
        "the right to appeal.",
    ],
}


def write_pdf(path: Path, lines: list[str]) -> None:
    doc = pymupdf.open()
    page = doc.new_page(width=612, height=792)  # US letter
    y = 72.0
    for line in lines:
        page.insert_text((72, y), line, fontsize=11, fontname="helv")
        y += 18
    doc.save(str(path))
    doc.close()


def write_unreadable_scan(path: Path, seed: int = 20260924) -> None:
    """Uniform gray speckle noise, no legible content: a blank/failed scan."""
    rng = random.Random(seed)
    pix = pymupdf.Pixmap(pymupdf.csGRAY, pymupdf.IRect(0, 0, 850, 1100))
    mv = pix.samples_mv
    for i in range(len(mv)):
        mv[i] = max(0, min(255, 200 + rng.randint(-6, 6)))
    pix.save(str(path), jpg_quality=60)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", default=str(DEFAULT_OUTPUT))
    args = ap.parse_args()

    output = Path(args.output).resolve()
    repo = Path(__file__).resolve().parents[2]
    if output.is_relative_to(repo):
        raise SystemExit(
            f"[fatal] refusing to write generated fixtures inside the repo: {output}"
        )

    for name, lines in CASES.items():
        case_dir = output / name
        case_dir.mkdir(parents=True, exist_ok=True)
        write_pdf(case_dir / "input.pdf", lines)
        print(f"wrote {case_dir / 'input.pdf'}")

    scan_dir = output / "06_unreadable_scan"
    scan_dir.mkdir(parents=True, exist_ok=True)
    write_unreadable_scan(scan_dir / "input.jpg")
    print(f"wrote {scan_dir / 'input.jpg'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
