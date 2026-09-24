# Expected: 03_cobra_notice

Synthetic single-page COBRA premium notice, all fields invented (DEF-03). Source text, exactly as drawn into `input.pdf`:

```text
HUMANA COBRA ADMINISTRATION

COBRA CONTINUATION COVERAGE PREMIUM NOTICE

Former Employee: Priya S. Nakamura (synthetic test patient)
Election ID: COBRA-SYN-77042
Coverage Period: 2026-07-01 to 2026-07-31

Monthly COBRA Premium Due: $687.50
Due Date: 2026-06-20

Nonpayment by the due date will result in loss of continuation
coverage.
```

## Load-bearing (a wrong value here is a fail)

- `category`: `financial`, not `medical`. The system prompt draws this line explicitly ("COBRA premium notices... anything that is a financial product rather than a clinical bill" — `scripts/classify_rename_medical_bills.py:108-110`); this fixture exists specifically to check the classifier keeps the two categories apart when it never fails to keep an ordinary hospital bill in `medical` (case 1).
- `document_type`: `cobra_notice`
- `balance`: `687.50` (the premium due, which is a real payment obligation here, unlike cases 4 and 5)
- `provider_name`: names Humana COBRA Administration; no `PROVIDER_ALIASES` entry matches this one, so `slugify_provider()` falls through to the generic cleanup path (`scripts/classify_rename_medical_bills.py:233`), giving a slug built straight from the string (e.g. `humana_cobra_administration`) rather than an aliased canonical form.

## Genuinely ambiguous (do not fail on these alone)

- `year`/`month`: the fixture carries both a due date (`2026-06-20`) and a coverage period (`2026-07-01` to `2026-07-31`), and nothing labeled "Statement Date." `2026`/`06` (due date, this notice's own issuance-adjacent date) and `2026`/`07` (coverage period) are both defensible; do not fail on this alone.
- `contents_summary`: any reasonable descriptor for a COBRA premium notice (e.g. `humana_cobra_premium`, close to the system prompt's own `hca_cobra_premium` example).
- `account_number`: the fixture uses "Election ID" rather than "Account Number." A transcription of `COBRA-SYN-77042` into `account_number`, or `null` on the reasoning that no field is literally labeled "account number," are both acceptable.
