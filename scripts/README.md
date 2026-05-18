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

## Requirements

Python 3.11 or newer (for `tomllib` in the standard library). On 3.10 or earlier, `pip install tomli` and change the import at the top of `validate_tracker.py`.

No third-party dependencies.

## Not yet built

The kit could grow more scripts over time; if you have an idea (e.g., a deadline-watcher that emails you when a `next_action_due` date is approaching, a bill-to-tracker importer that accepts a CSV from a billing portal), open an issue or PR.
