# Expected: 04_dental_predetermination

Synthetic single-page dental predetermination estimate, all fields invented (DEF-03). Source text, exactly as drawn into `input.pdf`:

```text
SAGE DENTAL INSURANCE SERVICES

PREDETERMINATION OF BENEFITS

Patient: Owen T. Fitzgerald (synthetic test patient)
Reference Number: SAGE-SYN-19935
Requested Procedure: Crown, porcelain/ceramic (D2740)
Provider: Brightpath Family Dental

This is NOT a bill. This estimate shows anticipated coverage
if the procedure above is performed within 90 days.

Estimated Plan Payment: $410.00
Estimated Patient Responsibility: $290.00
```

## Load-bearing (a wrong value here is a fail)

- `category`: `medical` (dental predetermination is named explicitly in the system prompt's medical examples — `scripts/classify_rename_medical_bills.py:104-107`)
- `document_type`: `predetermination`, not `bill`. The document states "This is NOT a bill" on its face and carries a dollar figure anyway; this is the fixture that tests whether the classifier can hold both facts at once instead of pattern-matching "has a dollar amount" to `document_type: bill`. Returning `bill` here is the costly-failure shape this run prompt calls out.

## Genuinely ambiguous (do not fail on these alone)

- `provider_name`: the letterhead names Sage Dental Insurance Services (the insurer issuing the estimate, and the system prompt's own worked example is literally `sage_dental_predetermination`); the body names Brightpath Family Dental (the treating provider). Either is a defensible read of "provider"; do not fail on this alone.
- `balance`: `290.00` (the estimated patient responsibility) is one defensible read; `null` is another, on the reasoning that an *estimate* contingent on a procedure happening within 90 days is not a fixed, currently-owed balance the way cases 1-3 are. Either passes; what fails is `2740` (the procedure code, D2740, mistaken for a dollar figure) or any amount not printed on the page.
- `year`/`month`: no statement or service date is printed on this fixture; `0`/`0` (undetermined, per the system prompt's own rule — `scripts/classify_rename_medical_bills.py:115-116`) is correct, and `null` is an acceptable near-equivalent.
- `account_number`: the fixture uses "Reference Number" rather than "Account Number." A transcription of `SAGE-SYN-19935`, or `null`, are both acceptable.
