# Expected: 01_hospital_bill

Synthetic single-page hospital statement, all fields invented (DEF-03). Source text, exactly as drawn into `input.pdf`:

```text
TRISTAR SOUTHERN HILLS MEDICAL CENTER
Patient Billing Statement

Patient: Marisol J. Quintero (synthetic test patient)
Account Number: TSH-88214-SYN
Statement Date: 2026-06-14
Service Date: 2026-05-30

Description                          Amount
Emergency Dept Level 4 visit          $2,140.00
Insurance Adjustment                 -$1,540.00
Insurance Payment                      -$400.00

AMOUNT DUE FROM PATIENT: $200.00

Please remit payment within 30 days.
```

## Load-bearing (a wrong value here is a fail)

- `category`: `medical`
- `document_type`: `bill`
- `provider_name`: names Tristar Southern Hills (Medical Center); `slugify_provider()` maps this to the aliased slug `tristar_southern_hills_medical_center` (`scripts/classify_rename_medical_bills.py:219-234`), so the eventual folder is `providers/tristar_southern_hills_medical_center/`, not a generic slug built from the raw string.
- `balance`: `200.00`, the patient-due line, not `2140.00` (billed) or `1940.00` (billed minus adjustment). Confusing the gross charge for the patient balance is the costly-failure shape this fixture set exists to catch.
- `account_number`: `TSH-88214-SYN` (or a clear transcription of it, not null and not a different string)

## Genuinely ambiguous (do not fail on these alone)

- `year`/`month`: `2026`/`06` (statement date) is the documented rule ("use the statement date if present" — system prompt, `scripts/classify_rename_medical_bills.py:114-116`); `2026`/`05` (service date) is a defensible misread of which date is "the" date and should not by itself fail the case.
- `contents_summary`: any reasonable snake_case descriptor leading with the provider slug (e.g. `tristar_southern_hills_bill`), per the system prompt's own worked example of this exact provider.
