# medbill-dispute-kit theory

What a session needs to believe before it changes this kit. Format: `ai_development/docs/readme-standards.md` R10.

## Invariants

- The kit has two trust models under one repo, not one. The LLM-droppable core (`rules/`, `references/`, `schemas/`, `templates/`, `llm/`) runs inside whatever LLM the patient chose and touches no network. `scripts/` is split again: `validate_tracker.py` and `deadline_watch.py` are stdlib-only and safe to run anywhere; the local-ops pipeline (`classify_rename_medical_bills.py` through `bundle_to_cloud.py`) uploads bill and EOB text to Azure OpenAI and writes patient PII to `~/.medbill-dispute-kit/`. Treating "the kit doesn't call home" (README, SECURITY.md's opening line) as true of `scripts/` as a whole is wrong; it is true only of the two generic helpers.
- No dollar figure, statute citation, tracking number, or account number may be invented. `llm/output_contracts.md:116` states it for the LLM; `draft_letters_by_state.py` enforces the same rule mechanically, leaving a placeholder rather than filling a field the OCR evidence doesn't support.
- `kit_config.toml` and the workstation `.env` (Azure credentials) are per-workstation and must never be committed; `.gitignore` blocks tracker CSVs, bills, and images but does not list `kit_config.toml` or `.env` by name, so a contributor relies on the scripts/README instruction, not a repo-enforced guard.

## Load-bearing constraints

- Every one of the 40 shipped state packs under `references/laws_state_*.md` (all but `laws_state_template.md`) opens with "All citations verified against public sources as of `<date>`. Re-verify annually." That date is the actual freshness signal, not the file's presence in the repo; a pack existing does not mean its citations are current. `docs/ANTI_PATTERNS.md:107` is the reason: patients are told to re-verify high-stakes citations against the state's own code site before mailing.
- Exactly two packs, `laws_state_hi.md` and `laws_state_id.md`, carry a "Verification gaps" section listing claims found in secondary sources but not confirmed in statute text, excluded rather than guessed. Four packs share their 2026-08-19 date (`hi`, `id`, `la`, `wv`), so the section is not consistent even across the newest batch, let alone the 36 older packs at 2026-05-18/19. Its absence from a pack is not evidence that pack has no gaps, only that nobody wrote them down.
- The dispute-letter drafter (`draft_letters_by_state.py`) gates on evidence, not on time elapsed: it will not draft a substantive dispute letter until both `has_eob` and `has_itemization` are true for that bill (`check_completeness.py` computes both). Missing either produces a request letter instead. This ordering is the kit's core anti-pattern defense (`docs/ANTI_PATTERNS.md`), not a style preference.

## Decisions that look wrong

- `check_completeness.py` never overwrites a tracker column the user has hand-filled (send dates, tracking numbers); only its own derived columns (`has_eob`, `status`, etc.) are recomputed each run. A session "fixing" a stale-looking manual field on re-run would silently discard real user history.
- `validate_tracker.py` checks structural conformance only (columns, dates, enums); it deliberately does not check that a bill's flags are logically consistent with its state (e.g., a balance-billing flag on a state with no such statute). Extending it to do so is out of its documented scope.

## Known soft spots

- SECURITY.md's in-scope description ("optional helper script... uses the Python standard library only") describes `validate_tracker.py`/`deadline_watch.py` accurately but reads as a claim about all of `scripts/`. It predates or ignores the Azure-backed local-ops pipeline documented in `scripts/README.md`. Don't cite SECURITY.md as proof the pipeline is dependency-free or network-silent; it isn't, and the discrepancy hasn't been reconciled.
- Whether the pre-2026-08-19 state packs (38 of 40) would pass the same "Verification gaps" bar the newest two packs set is untested; nobody has gone back and re-run that check against them.
