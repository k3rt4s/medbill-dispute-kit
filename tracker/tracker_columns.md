# Tracker — column dictionary

The tracker is the persistent state of your dispute process. It travels with you across LLM sessions. Each row is one bill; actions taken against a bill go in a parallel action log (see `schemas/action.toml`) or summarized in the `notes` field.

The canonical schema is in [`schemas/tracker.toml`](../schemas/tracker.toml). This file is a plain-English guide for the patient.

## How to use the tracker

1. Download `tracker_template.csv` once.
2. The LLM populates it as you upload bills. At the end of each session, the LLM emits an updated version; save it to your computer with the date in the filename (e.g. `tracker_2026-05-18.csv`).
3. Next session, upload your most recent tracker first. The LLM reads it and tells you what's overdue or coming up.

The example row in the template demonstrates the shape; delete it before using.

## Columns

| Column                  | What it is                                                                                                                                                                      | Required |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `bill_id`               | Stable identifier the LLM mints when it first sees this bill. Format `B-YYYY-NNN`. Do not edit.                                                                                 | yes      |
| `encounter_id`          | Identifier for the healthcare encounter (e.g. a hospital stay). Multiple bills from one stay share this. Format `E-YYYY-NNN`.                                                   | no       |
| `provider_name`         | The billing entity exactly as it appears on the statement.                                                                                                                      | yes      |
| `provider_type`         | One of: `hospital`, `physician_group`, `anesthesiology`, `radiology`, `pathology`, `lab`, `emergency_physician`, `ambulance`, `dental`, `pharmacy`, `device_supplier`, `other`. | yes      |
| `account_number`        | The provider's account number for this bill. The single strongest deduplication key.                                                                                            | yes      |
| `statement_date`        | Date the original statement was issued. ISO 8601 (YYYY-MM-DD).                                                                                                                  | yes      |
| `date_of_service_start` | First date of the service or admission.                                                                                                                                         | yes      |
| `date_of_service_end`   | Last date of service for multi-day encounters.                                                                                                                                  | no       |
| `total_billed`          | Total amount the provider charged before insurance adjustment, USD, decimal.                                                                                                    | yes      |
| `current_balance`       | What the bill currently shows as owed, USD, decimal.                                                                                                                            | yes      |
| `insurance_carrier`     | Name of the insurance plan shown on the bill.                                                                                                                                   | no       |
| `in_network_status`     | One of: `in_network`, `out_of_network`, `unknown`, `uninsured`, `self_pay`.                                                                                                     | no       |
| `was_emergency`         | `true` or `false` or empty. Drives No Surprises Act analysis.                                                                                                                   | no       |
| `findings`              | Semicolon-separated list from the controlled vocabulary in `schemas/bill.toml`. Examples: `no_itemization;possible_upcoding_99285`.                                             | no       |
| `next_action`           | One of the action enums in `schemas/bill.toml`. What you'll do next on this bill.                                                                                               | yes      |
| `next_action_due`       | Date by which the next action must be taken. ISO 8601.                                                                                                                          | yes      |
| `last_action_taken`     | Slug of the most recent completed action (from `action.toml`).                                                                                                                  | no       |
| `last_action_date`      | When `last_action_taken` happened.                                                                                                                                              | no       |
| `certified_mail_last`   | Most recent certified-mail tracking number used on this bill. Useful for proving the paper trail.                                                                               | no       |
| `status`                | One of: `open`, `awaiting_response`, `in_dispute`, `settled`, `closed`.                                                                                                         | yes      |
| `last_statement_date`   | Updated each time a follow-up statement arrives for the same bill.                                                                                                              | no       |
| `notes`                 | Free text. Quote in CSV if it contains commas or newlines.                                                                                                                      | no       |

## CSV formatting rules

- UTF-8 encoded, LF line endings (Unix).
- Header row is required and must match the column order above exactly.
- Quote a field only if it contains a comma, a newline, or a double quote (RFC 4180). Escape embedded double quotes by doubling them.
- Empty cells are empty (no `null`, no `N/A`).
- Dates are ISO 8601 (`YYYY-MM-DD`).
- Decimals use a period, no thousand separators, two decimal places (`12500.00`, not `12,500` or `12500`).
- Booleans are lowercase `true` or `false`, or empty if unknown.

## Why not Excel / Google Sheets?

CSV is the lowest common denominator. Every spreadsheet program opens it, and every LLM can read it. If you'd rather work in Excel or Sheets day-to-day, that's fine — export to CSV before uploading to the LLM, and let the LLM emit CSV back. Don't ask the LLM to read an `.xlsx` directly; CSV round-trips are more reliable.

## Action log (separate file)

The tracker holds current state. For the chronological history of every action you've taken on each bill — every letter sent, every phone call, every complaint filed — the LLM can also maintain an action log conforming to `schemas/action.toml`. This is optional; many users keep this history in the `notes` field of the tracker for simplicity. For multi-bill cases with many actions, a separate action log is easier to read.

The action log is append-only: never edit a prior action, only add a new one. If a prior action's outcome changes (e.g. settlement amount was renegotiated), append a new action superseding it.
