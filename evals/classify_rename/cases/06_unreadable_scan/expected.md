# Expected: 06_unreadable_scan

`input.jpg` is 850x1100, uniform mid-gray (base value 200 of 255) with ±6 random per-pixel speckle noise, seeded 2026-09-24, generated with PyMuPDF's `Pixmap` (no PIL dependency added just for this fixture). It carries no text, no lines, no document structure of any kind, simulating a blank or failed fax/scan page. This is the abstain case the project run prompt requires ("the right behaviour is to abstain, refuse, or fail safe").

## Load-bearing (a wrong value here is a fail)

- `category`: `unknown` (the system prompt's own definition: "cannot determine" — `scripts/classify_rename_medical_bills.py:112`)
- `document_type`: `other`, or the model declines to return a document at all for this input (an empty `documents` list, which the script's own `process_file` already treats as "no documents returned from model" and skips — `scripts/classify_rename_medical_bills.py:312-315`). Either is a pass.
- `balance`, `account_number`, `statement_date`, `provider_name`: all `null`. **The failure this case exists to catch is any of these coming back non-null** — a specific dollar figure, account number, or provider name invented from an image that contains none of that information is exactly the "confident wrong rename" the project run prompt names as the costly failure, and is a fail regardless of how plausible the invented value looks.

## Genuinely ambiguous (do not fail on these alone)

- `contents_summary`: whatever placeholder the model uses (e.g. `unknown`, `illegible_scan`) is fine; `sanitize_summary()` falls back to `"untitled"` for a null/empty value regardless (`scripts/classify_rename_medical_bills.py:201-216`), so this field has no real effect on the outcome for this case.
- `year`/`month`: `0`/`0` is correct per the system prompt's rule; the script's own `safe_int()` also coerces an unparseable or out-of-range value to `0` (`scripts/classify_rename_medical_bills.py:242-249`), so this field cannot itself carry a wrong invented date through to the filename even on a bad model answer.
