# Output contracts

What your responses must look like at each phase of the workflow. Deviating from these contracts makes the tracker round-trip break.

## Bill extraction (Phase 1)

When you extract a new bill, output it as a fenced TOML block conforming to `schemas/bill.toml`. Example:

```toml
[bill]
bill_id = "B-2026-001"
encounter_id = "E-2026-001"
provider_name = "Example General Hospital"
provider_type = "hospital"
provider_tax_id = ""
account_number = "ACCT123456"
patient_account_id = ""
statement_number = "STMT-9988"
statement_date = "2026-04-30"
date_of_service_start = "2026-03-15"
date_of_service_end = "2026-03-17"
total_billed = 12500.00
total_insurance_paid = 11000.00
total_patient_paid = 0.00
current_balance = 1500.00
payment_due_date = "2026-05-30"
insurance_carrier = "Example Health Plan"
contact_phone = "1-800-555-0100"
contact_address = "PO Box 1234, City, ST 00000"
payment_url = ""
findings = []
next_action = "request_itemization"
next_action_due = "2026-05-18"
status = "open"
notes = ""
```

After the TOML, in plain prose, say: "Confirm this matches what's on the bill, or tell me what to fix."

## Tracker emit (Phase 5 and on request)

When emitting the full tracker, output a fenced CSV block with the header row exactly matching `tracker/tracker_columns.md`. Every cell quoted only if it contains a comma, a newline, or a double quote (RFC 4180). Example:

```csv
bill_id,encounter_id,provider_name,provider_type,account_number,statement_date,date_of_service_start,date_of_service_end,total_billed,current_balance,insurance_carrier,findings,next_action,next_action_due,status,last_statement_date,notes
B-2026-001,E-2026-001,Example General Hospital,hospital,ACCT123456,2026-04-30,2026-03-15,2026-03-17,12500.00,1500.00,Example Health Plan,"no_itemization;possible_upcoding_99285",request_itemization,2026-05-18,open,2026-04-30,""
```

After the CSV, tell the user the filename to save it as.

## Letter drafts (Phase 4)

Letters render as Markdown inside a fenced block tagged `letter`:

````markdown
```letter

[Patient name]
[Patient address]
[Phone] · [Email]

[Date]

[Recipient]
[Recipient address]

RE: ...

Dear [Recipient]:

[Body, in plain prose, matching the template]

Sincerely,

[Patient name]

Account number: [...]
Date of service: [...]
Enclosures: [...]

```text
````

Any unfilled placeholder appears as `[NEEDS USER INPUT: short description]`. After the letter block, in plain prose, list each `[NEEDS USER INPUT]` item and ask the user to supply it.

## Action log entries (Phase 4)

When you log an action against a bill, append a TOML block conforming to `schemas/action.toml`:

```toml
[[action]]
bill_id = "B-2026-001"
action_type = "initial_dispute"
date_sent = "2026-05-18"
recipient = "Billing Department, Example General Hospital"
template_used = "templates/letter_initial_dispute.md"
certified_mail_tracking = "9407 1234 5678 9012 3456 78"
response_due_by = "2026-06-08"
status = "awaiting_response"
notes = ""
```

## Briefings (Phase 5)

End-of-session briefing format, plain prose, no markdown headings:

> **Session summary:** [one sentence, what changed].
> **Overdue:** [list bills past their `next_action_due`, or "none"].
> **Due in the next 7 days:** [list with dates].
> **Highest-priority next action for next session:** [one bill, one action].
> **Save your tracker as:** `tracker_YYYY-MM-DD.csv`.

## What never to do

- Do not output personally identifying information (PII) of anyone other than the patient you're talking to.
- Do not fabricate certified-mail tracking numbers, account numbers, or statute citations. If you don't have it, mark it `[NEEDS USER INPUT]`.
- Do not output a tracker fragment. Tracker emits are always the complete tracker.
- Do not put the rendered letter inside the tracker CSV. Letters live outside the tracker.
