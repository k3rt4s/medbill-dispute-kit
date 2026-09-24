# Expected: 02_collection_notice

Synthetic single-page collection referral notice, all fields invented (DEF-03). Source text, exactly as drawn into `input.pdf`:

```text
LABCORP
Laboratory Corporation of America

NOTICE OF COLLECTION REFERRAL

Patient: Devon R. Achebe (synthetic test patient)
Account Number: LC-SYN-550219
Original Service Date: 2026-02-11
Referral Date: 2026-06-01

Your account balance of $340.00 for laboratory services has been
referred to Meridian Recovery Associates for collection.

BALANCE REFERRED: $340.00
```

## Load-bearing (a wrong value here is a fail)

- `category`: `medical` (a medical-debt collection notice, per the system prompt's own category rule for "collection notice for medical debt")
- `document_type`: `collection_notice`, not `bill`. This document has no line-item billing (no charges/adjustments/payments table like case 1), just a referred balance; calling it `bill` would be a miscategorization even though a dollar figure is present.
- `provider_name`: names LabCorp; `slugify_provider()`'s alias match (`labcorp|laboratory\s+corporation`, `scripts/classify_rename_medical_bills.py:220`) maps this to the aliased slug `labcorp`, not a generic slug built from "Meridian Recovery Associates" (the collection agency, not the medical provider on the account).
- `balance`: `340.00`
- `account_number`: `LC-SYN-550219`

## Genuinely ambiguous (do not fail on these alone)

- `year`/`month`: the fixture deliberately carries two dates and no field literally labeled "Statement Date." `2026`/`06` (Referral Date, the notice's own issuance date) is the best analog to "statement date"; `2026`/`02` (Original Service Date) is a defensible alternate read. Either passes.
- `contents_summary`: any reasonable descriptor leading with `labcorp` (e.g. `labcorp_collection_notice`, the system prompt's own worked example for this exact provider/type pairing).
