# scripts/

Optional helpers. The kit is instruction-only at its core; nothing in `scripts/` is required to use it from an LLM. These tools exist for two purposes:

1. **Generic, instruction-only helpers** that anyone can run against any tracker CSV. (`validate_tracker.py`, `deadline_watch.py`.) No third-party dependencies, no API keys.
2. **A local-ops pipeline** for the workstation use case where the patient drops mail into an `inbox/` folder and the scripts route, OCR, match, and draft dispute letters automatically. This pipeline uses Azure OpenAI for vision OCR and field extraction. It expects a specific folder layout under a personal `Health_Bills/` directory.

## Generic helpers

### `validate_tracker.py`

Validates a tracker CSV against the TOML schemas in `../schemas/`. Returns exit code 0 if the file conforms, 1 if it has structural problems, 2 on usage errors. Checks header row, ISO 8601 dates, decimal-parseable amounts, boolean conformance, enum membership, and semicolon-separated findings vocabulary.

```bash
python scripts/validate_tracker.py my_tracker_2026-05-18.csv
```

### `deadline_watch.py`

Reports overdue and upcoming bill actions from a tracker CSV. Groups bills into Overdue / Due soon / Upcoming based on `next_action_due`. Exits 1 if anything is overdue. Useful in Task Scheduler / cron for weekly check-ins.

```bash
python scripts/deadline_watch.py my_tracker_2026-05-18.csv
python scripts/deadline_watch.py my_tracker_2026-05-18.csv --window 14
python scripts/deadline_watch.py my_tracker_2026-05-18.csv --as-of 2026-06-01
```

## Local-ops pipeline (workstation-specific)

The scripts below form a state-machine pipeline that takes scanned medical-bill mail, OCRs it, organizes it into a per-biller folder structure, links bills to EOBs, and drafts the right next letter based on the evidence we currently have.

The key design rule: **never draft a substantive dispute letter until we have BOTH the bill's EOB from the insurer AND the bill's itemized statement from the provider.** If either is missing, the script drafts a request letter to obtain it instead. This prevents premature disputes that the biller can dismiss for lack of evidence.

The full chain, in order:

```text
classify_rename_medical_bills.py    intake — split mixed inbox/ into Billers/ and EOB/
text-extraction step                 (out of scope for this kit — use ai-toolkit's file_management
                                      Stage 5 `extract_documents.py` or any equivalent that produces
                                      `<file>.extracted.txt` sidecars next to each source file)
restructure_to_billers_eob.py       one-time migration if older `providers/` layout exists
index_bills_and_claims.py           per-folder _bills.csv and _claims.csv via Azure
match_claims_to_bills.py            link each EOB claim to a bill it adjudicates
check_completeness.py               derive per-bill has_eob / has_itemization gates
draft_letters_by_state.py           draft the next letter for each dispute group
```

### `restructure_to_billers_eob.py`

One-time migration from the older `providers/<biller_slug>/` layout (which mixed bills and EOBs in one folder per biller) into the two-track layout `Billers/<biller_slug>/` + `EOB/<biller_slug>/`. Detects EOBs by the explicit "Explanation of Benefits" text marker (not by "THIS IS NOT A BILL", which appears on hospital itemizations as well). Old `DISPUTE_LETTER.md` drafts get archived to `_archive_old_letters/` so the new state-machine drafts fresh ones.

```bash
python scripts/restructure_to_billers_eob.py --dry-run
python scripts/restructure_to_billers_eob.py
```

### `index_bills_and_claims.py`

Reads every `<file>.extracted.txt` sidecar produced by the text extractor and uses Azure OpenAI gpt-5.2 (text-only, no image render) to extract structured fields. Writes `_bills.csv` per `Billers/<slug>/` (one row per bill PDF) and `_claims.csv` per `EOB/<slug>/` (one row per CLAIM line — a multi-claim EOB produces N rows). Idempotent: each sidecar's content hash is recorded in its row, so re-runs only call Azure for new or changed files.

Computes the `has_itemization` flag using the peer-reviewed heuristic:

- Count of distinct **dated charge lines** (a line with both a service date and a charge amount), threshold ≥ 3.
- Override-to-false when payment-ledger keywords dominate ("payment received", "balance forward", "contractual adjustment") or when EOB-style fields are prominent (claim_number / allowed / coinsurance / deductible).
- Override-to-true when **UB-04** form headers (revenue code, service units, total charges) or **CMS-1500** form headers (place of service, CPT/HCPCS, modifiers, days/units) are present.

The heuristic is conservative: false positives (claiming itemized when it isn't) are worse than false negatives, because the next step is to mail a dispute letter assuming the evidence is in hand.

```bash
python scripts/index_bills_and_claims.py
python scripts/index_bills_and_claims.py --force   # re-extract every file
```

### `match_claims_to_bills.py`

Links each EOB claim row to the bill that adjudicates it. Two-stage:

1. **Deterministic** (no API call): same biller_slug + amount within $0.50 + DOS overlap (or claim DOS within 60 days of the bill's statement date if no bill DOS).
2. **Azure OpenAI fallback** when deterministic returns multiple candidates or none: gpt-5.2 sees the claim row and the candidate bills with a strict "respond UNKNOWN if not confident" prompt. False positives are worse than false negatives.

Output: `<log-dir>/matches.csv` with one row per attempted match. Match types: `deterministic`, `azure`, `azure_unknown`, `unmatched`, `bill_only` (no claim for this slug), `claim_only` (no bill for this slug). The log directory defaults to `~/.medbill-dispute-kit/tracker/`; override via `$HEALTHBILLS_LOG_DIR`.

```bash
python scripts/match_claims_to_bills.py
```

### `check_completeness.py`

Joins the per-folder CSVs with `matches.csv` and writes the master `tracker.csv` to the log directory (default `~/.medbill-dispute-kit/tracker/`, override via `$HEALTHBILLS_LOG_DIR`). Each bill row carries:

- `has_eob` (Y/N, derived from matches.csv)
- `has_itemization` (Y/N, from `_bills.csv`)
- `current_status` (`gathering_evidence` | `ready_to_dispute` | `disputed` | `escalated` | `settled` | `closed` | `superseded`)
- `next_action` (`request_eob` | `request_itemization` | `draft_dispute` | etc.)

Manual columns the user fills in after mailing each letter (`eob_request_sent_date`, `eob_request_tracking`, etc.) are preserved across runs — the script never overwrites a value the user has entered.

```bash
python scripts/check_completeness.py
```

### `draft_letters_by_state.py`

For each dispute group (bills with the same `biller_slug` + `account_number`) selects the canonical bill (latest statement_date) and drafts whichever letter the state machine wants:

- `has_eob = N` and `eob_request_sent_date` empty → draft `LETTER_REQUEST_EOB.md`
- `has_itemization = N` and `itemization_request_sent_date` empty → draft `LETTER_REQUEST_ITEMIZATION.md`
- Both gates green and no dispute letter sent yet → draft `DISPUTE_LETTER.md` using the appropriate kit template (NSA, FDCPA, dental dispute, ERISA appeal, initial dispute)

Output files land in `Billers/<slug>/<bill_id>_LETTER_*.md`. The path is recorded back into `tracker.csv` columns `drafted_eob_request`, `drafted_itemization_request`, `drafted_dispute_letter`.

Per-folder overrides exist for cases where the template is known regardless of OCR signals (e.g., `quantum_radiology` → NSA, `humana` → dental_dispute, `labcorp` → FDCPA). The model fills placeholders from real bill/EOB content; if a field isn't visible in evidence, the model is instructed to leave the placeholder rather than invent a value.

```bash
python scripts/draft_letters_by_state.py
python scripts/draft_letters_by_state.py --dry-run
python scripts/draft_letters_by_state.py --force
```

### `classify_rename_medical_bills.py`

Intake stage. Walks `inbox/`, calls Azure OpenAI vision on each file, renames per the file_management v1.1 convention `<contents_summary>_<category>_<YYYY>_<MM>_v<N>.<ext>`, splits multi-bill PDFs by page range, and routes each output to:

- `Billers/<biller_slug>/` for bills, itemizations, collection notices
- `EOB/<biller_slug>/` for Explanation of Benefits documents
- `other/` for financial/personal non-medical documents

Provider-alias map handles the common biller-name variants (TriStar/Southern Hills/HCA, Labcorp/Laboratory Corporation, Premier Radiology variants, etc.). Re-running on the same `inbox/` is safe; files already routed are not re-processed.

```bash
python scripts/classify_rename_medical_bills.py
python scripts/classify_rename_medical_bills.py --dry-run
```

## Privacy notes

The local-ops scripts upload bill / EOB images and extracted text to Azure OpenAI. They also write index CSVs and the master tracker to your log directory (default `~/.medbill-dispute-kit/tracker/`, override via `$HEALTHBILLS_LOG_DIR`) containing patient name, provider name, claim numbers, dates of service, and dollar amounts. Treat that directory as sensitive: keep it on local disk (not synced to multi-user storage), and back up encrypted.

The Azure deployment reads credentials from a workstation `.env` file. The default location is `~/.medbill-dispute-kit/.env`; override via `$MEDBILL_KIT_ENV_FILE`. The `.env` file must contain `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, and `AZURE_OPENAI_DEPLOYMENT`. Do not commit this file to any repo.

## Requirements

- Python 3.11+
- `PyMuPDF` (fitz) for PDF rendering — used by `classify_rename_medical_bills.py`
- `openai` for the Azure-compatible client
- Azure OpenAI deployment with vision support (the workstation default uses `gpt-5.2`)
- Workstation `.env` with `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`
- Tesseract OCR (optional, on PATH) — the text extractor falls back to vision OCR for image-only PDFs, so Tesseract is not required by these scripts

`validate_tracker.py` and `deadline_watch.py` have no third-party dependencies and need no API keys.

## When to extend

If you have a new biller pattern that the alias map doesn't cover, edit `BILLER_ALIASES` near the top of `classify_rename_medical_bills.py`. If you have a new dispute scenario (e.g., a new state's medical-debt protection law), add a template under `../templates/` and a corresponding entry in the `DISPUTE_TEMPLATE_PICKER` or `FOLDER_TEMPLATE_OVERRIDES` map in `draft_letters_by_state.py`.

The kit's roadmap (`../roadmap.json`) is the source of truth for what's planned next. Open an issue or PR.
