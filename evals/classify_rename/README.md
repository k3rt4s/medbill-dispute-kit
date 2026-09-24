# classify_rename AG3 eval fixture

AG3 regression fixture for `scripts/classify_rename_medical_bills.py`, the vision intake classifier that reads a scanned bill or letter and decides its category, document type, provider, and rename.

Built under `ai_development/docs/ai-grounding.md` AG3, following the `evals/<name>/<fixture-slug>/` shape `docs/agent-eval.md` sets and the ai-grounding demo at `C:\Code\ai_development\evals\ai-grounding\` reuses for a product feature. `check_rules.py` rule AI-01 flagged this project on 2026-09-24 because `scripts/classify_rename_medical_bills.py` calls a model API (`from openai import OpenAI`, against Azure OpenAI's `/openai/v1/` endpoint) with no `evals\` directory at all. Lane H6 judged the finding real, and Jon delegated the build-or-suppress call to the ai_development main orchestrator, which decided: every flagged project builds a harness. `RUN_2026-09-24_ai01_medbill-dispute-kit.md` scoped this run to that one file.

## Why this feature and not the other six

`git grep -n -E "anthropic|openai|ollama|/v1/messages|/v1/chat/completions|/api/generate" -- '*.py'` on 2026-09-24 found seven scripts that call the Azure OpenAI endpoint: `classify_rename_medical_bills.py` (this fixture), `draft_letters_by_state.py`, `index_bills_and_claims.py`, `match_claims_to_bills.py`, `parse_990.py`, `parse_sbc.py`, and `parse_spd.py`. AI-01 only ever reports the first one it hits, so it named this project without naming the whole feature surface; the project run prompt scoped this pass to the flagged file only, which is what satisfies the AI-01 presence check (the rule looks for `evals\` existing at all, not for full coverage). The other six calls are real AI-01 exposure of their own and are not evaluated here; see the work board's Pending section for the backlog item, which is Jon's call, not this run's, per CORE-11 (scope is what was assigned).

## Why a vision fixture looks different from the ai-grounding demo

The ai-grounding demo fixture is text-in, text-out: one context passage, four questions, four known-good answers. This feature is image-in, structured-JSON-out: the script renders each inbox file to JPEG pages (`render_pdf_pages`) and sends them to the model with `SYSTEM_PROMPT` (`scripts/classify_rename_medical_bills.py:68-129`), which must return `category`, `document_type`, `provider_name`, `contents_summary`, `year`/`month`, `account_number`, and `balance`. Each case here is a self-contained input file rather than a shared passage, so each gets its own subfolder instead of one shared `context.md`.

## Cases

Six cases in `cases/`, following the project run prompt's split: one bill-like fixture per distinct `document_type` (up to four), then a non-bill document, then an unreadable scan. For the last two, the correct behavior is to classify honestly rather than force a confident bill-shaped answer with invented figures; a confident wrong rename (inventing a balance or account number, or mislabeling a non-bill as `bill`) is the costly failure this fixture exists to catch, not a missed rename.

| #   | Case                         | `category` | `document_type`   | Tests                                                                                                                                                                                       |
| --- | ---------------------------- | ---------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | `01_hospital_bill`           | medical    | bill              | Baseline bill classification, `PROVIDER_ALIASES` slug match ("tristar/southern hills")                                                                                                      |
| 2   | `02_collection_notice`       | medical    | collection_notice | Non-"bill" medical document type, `PROVIDER_ALIASES` slug match ("labcorp")                                                                                                                 |
| 3   | `03_cobra_notice`            | financial  | cobra_notice      | `category` = financial, not medical, for a premium-only notice                                                                                                                              |
| 4   | `04_dental_predetermination` | medical    | predetermination  | An estimate that says "THIS IS NOT A BILL" on its face; must not become `document_type: bill` despite carrying a dollar figure                                                              |
| 5   | `05_eob_non_bill`            | medical    | eob               | Non-bill document (explicit EOB, per the project run prompt's example): must not invent the $1,800 billed amount as patient balance when the document states `$0.00` patient responsibility |
| 6   | `06_unreadable_scan`         | unknown    | other (or null)   | Abstain case: a legible-free noise image must not produce a confident rename with invented fields                                                                                           |

Each `cases/<n>/` holds only `expected.md`: the exact source text drawn into the fixture (as a code block, for the five document cases), the known-good fields, which ones are load-bearing for pass/fail versus which are genuinely ambiguous in the fixture (and so are graded either way), and why.

This repo's `.gitignore` blocks every `*.pdf`/`*.jpg`/`*.jpeg`/`*.png`/`*.heic` unconditionally ("Local data — never commit a real bill or tracker"), the same rule `examples/sample_bills/fixture_tools.py` already works under, so the case directories never hold the binary itself, synthetic or not. `generate_fixtures.py` in this folder regenerates the binaries on demand from the text embedded in each `expected.md` (kept in sync by hand) and refuses to write anywhere inside the repo, writing instead to `C:\Code_data\medbill-dispute-kit\evals\classify_rename\cases\<n>\input.{pdf,jpg}` by default. Re-running it is idempotent and safe.

## Synthetic data only (DEF-03)

Every fixture is invented: patient names, account numbers, dates, dollar amounts, and provider names are fabricated for this run (seeded 2026-09-24). No real bill, EOB, or patient record enters this repo, the data root, or this run. `gh repo view --json visibility` was checked before any fixture text was committed: **public**.

## Running it by hand

Per `docs/agent-eval.md`'s "no script until two runs by hand" rule, reused here: no grading/runner script exists yet, and none should be added until this fixture has been graded by hand at least twice. To run a case: first `python evals\classify_rename\generate_fixtures.py` to materialize the binaries into the data root (see above), then feed the worker `cases/<n>/input.pdf` (or `.jpg`) from there plus the `SYSTEM_PROMPT` from `scripts/classify_rename_medical_bills.py:68-129`, or run the script itself in `--dry-run` mode against a one-file inbox built from that fixture. Grade the JSON it returns against `cases/<n>/expected.md`: a load-bearing field that comes back wrong is a fail for that case; a genuinely-ambiguous field noted in `expected.md` is not graded either way.

## Run log

**Not yet run.** This machine has no `~/.medbill-dispute-kit/.env` (or `$MEDBILL_KIT_ENV_FILE`) and the project's own standing rule is "never call Azure OpenAI; every test runs offline against fixtures; no lane creates a credential file here." That is exactly AG3's "model cannot be reached" case: fixtures are committed with results marked not yet run, per `RUN_2026-09-24_ai01_common.md` step 6, rather than skipped or faked. A scored board item, "run the AI-01 classify_rename cases twice by hand," carries this forward. When it runs, record each pass here: date, model/deployment, per-case pass/fail against `expected.md`, and (per AG3) a copy of the dated result in `C:\Code_data\medbill-dispute-kit\ai_grounding_eval\<date>.md`.
