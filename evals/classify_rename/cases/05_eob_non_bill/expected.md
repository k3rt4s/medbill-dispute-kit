# Expected: 05_eob_non_bill

Synthetic single-page explanation of benefits, all fields invented (DEF-03). This is the project run prompt's "non-bill document... explanation of benefits" case: EOB is its own `document_type` in the classifier's schema (`scripts/classify_rename_medical_bills.py:82`), distinct from `bill`. Source text, exactly as drawn into `input.pdf`:

```text
OPTUM HEALTH INSURANCE

EXPLANATION OF BENEFITS

This is a summary of how your claim was processed.
THIS IS NOT A BILL.

Subscriber: Renata L. Voss (synthetic test patient)
Claim Number: OPT-SYN-402188
Date of Service: 2026-04-02
Provider: Centennial Heart Associates

Billed Amount:        $1,800.00
Plan Discount:          -$950.00
Plan Paid:              -$850.00
Patient Responsibility:      $0.00

If you believe this claim was processed incorrectly, you have
the right to appeal.
```

## Load-bearing (a wrong value here is a fail)

- `category`: `medical`
- `document_type`: `eob`, not `bill`. The page says "THIS IS NOT A BILL" outright.
- `balance`: `0.00` (or a clear null/none reading), taken from the explicit "Patient Responsibility: $0.00" line. **The failure this case exists to catch: the model returning `1800.00` (the billed amount) as the patient's owed balance.** An EOB's headline dollar figure is what the provider charged the insurer, not what the patient owes; confusing the two is exactly the "confident wrong rename" the project run prompt calls the costly failure, made worse here because it would tell a patient they owe $1,800 when the document says they owe nothing.

## Genuinely ambiguous (do not fail on these alone)

- `provider_name`: the letterhead names Optum (the insurer issuing the EOB, and the system prompt's own worked example is literally `optum_eob`); the body names Centennial Heart Associates (the treating provider whose claim this is). Either is a defensible read of "provider"; do not fail on this alone.
- `year`/`month`: `2026`/`04`, from "Date of Service" (there is no separate statement date on an EOB fixture built this way).
- `account_number`: the fixture uses "Claim Number" rather than "Account Number." A transcription of `OPT-SYN-402188` into `account_number`, or `null`, are both acceptable.
- `contents_summary`: any reasonable descriptor (e.g. `optum_eob`, the system prompt's own worked example for this exact provider/type pairing).
