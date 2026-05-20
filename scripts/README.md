# scripts/

Optional helpers. The kit is instruction-only; nothing in `scripts/` is required to use it. These tools exist for people who want to sanity-check their tracker outside of an LLM session.

## validate_tracker.py

Validates a tracker CSV against the TOML schemas in `../schemas/`.

```bash
python scripts/validate_tracker.py my_tracker_2026-05-18.csv
```

Returns exit code 0 if the file conforms, 1 if it has structural problems, 2 on usage errors.

Checks:

- Header row matches `schemas/tracker.toml` column order
- Date cells parse as ISO 8601 (`YYYY-MM-DD`)
- Decimal cells parse as numbers with optional decimal points
- Boolean cells are `true`, `false`, or empty
- Enum fields (`provider_type`, `next_action`, `status`, `in_network_status`) contain only values from the corresponding `schemas/bill.toml` enum
- Semicolon-separated `findings` entries each match the controlled vocabulary

Does not check:

- Logical correctness (e.g., that a bill with `dispute_ground_ambulance` is in a state that has a ground-ambulance statute)
- Cross-row consistency (e.g., that two bills with the same `encounter_id` share a date of service)
- Provider-name typos

For those, eyeball the tracker or ask the LLM to review it.

## deadline_watch.py

Reports overdue and upcoming bill actions from a tracker CSV.

```bash
python scripts/deadline_watch.py my_tracker_2026-05-18.csv
python scripts/deadline_watch.py my_tracker_2026-05-18.csv --window 14
python scripts/deadline_watch.py my_tracker_2026-05-18.csv --as-of 2026-06-01
```

Groups bills into three categories based on `next_action_due`:

- **Overdue** — already past due
- **Due soon** — within the configurable window (default 7 days)
- **Upcoming** — beyond the window

Skips rows whose `status` is settled or closed. Returns exit code 1 if any bill is overdue, 0 otherwise. Useful in cron, Task Scheduler, or a weekly check-in to make sure no deadlines have lapsed.

## Local-ops scripts (workstation pipeline, not part of the kit's instruction layer)

The scripts below are for a single-workstation pipeline that takes a folder full of scanned medical-bill PDFs and turns it into a clean per-provider folder layout plus a tracker CSV the LLM workflow can consume. They are deliberately not part of the kit's instruction-only contract: they call Azure OpenAI for vision OCR, expect a specific local folder layout, and read API credentials from a workstation `.env`. Use them, ignore them, or rewrite them to fit your own setup.

All four accept `--help` and CLI overrides for every input/output path. The Azure OpenAI `.env` location is the one exception, intentionally hardcoded to `C:/Code/projects/ai-toolkit/.env` per the workspace-wide AGENTS.md §4 pre-push peer review pattern — edit the constant at the top of each script if your workstation keeps the credentials somewhere else.

### classify_rename_medical_bills.py

Vision-classifies each file in an `inbox/` folder, renames per the file_management v1.1 convention `<contents_summary>_<category>_<YYYY>_<MM>_v<N>.<ext>`, splits multi-bill PDFs by page range, and routes into `providers/<slug>/` for medical files or `other/` for financial/personal/unknown.

### parse_bills_to_tracker.py

Walks the renamed `providers/<slug>/` tree, extracts structured fields per `schemas/bill.toml` via vision, dedupes by exact account match plus a provider+DOS+balance fallback, and writes `tracker.csv` outside the repo at `C:/Code_data/medbill-dispute-kit/tracker/`.

### dedupe_tracker.py

Post-processes `tracker.csv`. Normalizes provider names via an alias map, re-dedupes when the extractor missed an account number, and drops non-bill rows (NOT-A-BILL itemizations, language-assistance notices, payment-plan reminders). Preserves existing `bill_id`/`encounter_id` values so downstream references stay stable across runs.

### classify_eobs.py

Hash-dedupes a folder full of insurer EOBs (Windows download-conflict copies are common), then vision-classifies each unique EOB and routes to the matching `providers/<slug>/` folder. EOBs for someone other than the account holder land in a `not_for_me/` subfolder; EOBs for the account holder with no matching provider land in `unmatched/`.

### Requirements for the local-ops scripts

- Python 3.11+
- `PyMuPDF` (fitz) for PDF rendering
- `openai` for the Azure-OpenAI-compatible client
- Azure OpenAI deployment with vision support (the workstation default uses `gpt-5.2`)
- Workstation `.env` with `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`

### Privacy note

All four scripts upload bill / EOB images to Azure OpenAI for OCR. They write a decision log to `C:/Code_data/medbill-dispute-kit/tracker/` that contains patient name, provider name, dates, and amounts — treat `Code_data/` as sensitive. Do not run these scripts on shared workstations or paths that sync to multi-user storage.

## Not yet built

The kit could grow more scripts over time; if you have an idea (e.g., a bill-to-tracker importer that accepts a CSV from a billing portal, a CalDAV exporter that pushes deadlines to your calendar), open an issue or PR.
