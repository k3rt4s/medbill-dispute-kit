# Contributing

The kit is open under MIT. Pull requests welcome, especially:

- New state-law packs (analogous to `references/laws_state_tn.md`)
- Additional letter or complaint templates for gaps the kit doesn't cover
- Real-world feedback on rules or templates that didn't work as expected (in PR form or as a GitHub issue)
- Examples showing the kit in action with synthetic patients
- Improvements to the schemas, deduplication rules, or workflow
- Translations and accessibility work

## What does not belong in PRs

- Personally identifying information about real patients, providers, or bills. Use synthetic or clearly fictionalized data.
- Legal advice for specific patients or situations. The kit is a methodology; specific advice is for licensed attorneys.
- Promotional content for paid services. Free, open resources for patients are welcome; paid offerings should be disclosed and only included where directly relevant (e.g., we link Dollar For because they handle FAP applications for free).
- Code with telemetry. The kit is intentionally instruction-only and locally-loaded; it should not call home.

## Adding a state pack

The single most valuable contribution. Use this checklist:

1. Read `references/laws_state_template.md` and `references/laws_state_tn.md` / `laws_state_ga.md` to understand the structure.
2. Cover all 12 required sections:
   - Hospital itemization right
   - Unfair claims settlement practices
   - Bad-faith remedy (statute or common law)
   - State surprise-billing statute (if broader than federal NSA)
   - Ground-ambulance protection (most states don't have one; say so)
   - State insurance department contact
   - State attorney general consumer protection contact
   - Small claims court (name, limit, fees, attorney rules)
   - Statute of limitations
   - Medical-debt credit-reporting protections (most states defer to federal)
   - Charity care / state-level FAP requirements
   - Hospital lien statute
3. Source every citation with a URL — Justia, Cornell LII, or the state's official code website.
4. Date the file in the opening paragraph ("All citations verified against public sources as of YYYY-MM-DD").
5. Conclude with a "Quick reference for letter rendering" table.
6. Conclude with a "Key [State]-specific advantages" section listing 3-5 structural patient-side levers worth knowing about.
7. Add the new state to:
   - `BUILD_PLAN.md` version status
   - `CHANGELOG.md` under the next version
   - `README.md` state-pack list
   - `llm/QUICKSTART_short_context.md` Stage 2 list
8. Open the PR. Include in the description the date you verified the citations.

## Adding a template

Templates live in `templates/`. Each must:

- Open with a paragraph explaining when to use it (and when not to).
- Render the letter inside a fenced markdown block tagged `letter`.
- Use clear placeholders in square brackets, e.g., `[PATIENT FULL NAME]`, `[DATE OF SERVICE]`.
- List all placeholders the LLM must fill in, with notes on rendering ambiguities.
- Document parallel actions the patient should take.
- Document follow-up (action_type to log, response_due_by to set).
- Add a story for the template to `USER_STORIES.md` if it represents new functional coverage.
- Add the template to `llm/QUICKSTART_short_context.md` Stage 5 list.

## Adding a rule

Rules live in `rules/`. Numbering is roughly sequential by topic, not strict. Each rule should:

- Start with a one-paragraph summary of when the rule fires.
- State "the rule" in 2-4 sentences.
- Provide the reasoning ("why this is the rule").
- Provide the playbook (what to do).
- Cross-reference related rules using `[[double-bracket]]` links.

## Adding a schema field

Schemas live in `schemas/`. When extending:

- Add the field to the relevant `.toml` file with type, required flag, description, and example.
- If extending an enum, place the new value in the existing list; do not delete prior values (we keep backward compatibility for tracker CSVs in the wild).
- If the field is part of a controlled vocabulary used by rules, update both the schema and the consuming rule.
- Bump the schema_version in the meta section.

## Coding style — when scripts are involved

The kit ships with optional helper scripts in `scripts/`. Style:

- Python 3.11+ (the kit is Windows/Mac/Linux portable; avoid OS-specific calls).
- Standard library only by default; if a dependency is needed, justify it in the script's docstring.
- Each script gets a docstring header with: what it does, how to invoke, example output.
- No telemetry, no network calls except where the script is explicitly performing a network task documented at the top.

## Commit messages

- Subject line: imperative mood, under 70 characters, describes the change.
- Body: explain "why" rather than "what" for non-trivial changes.
- Reference any related issue numbers.

## PR review checklist

For maintainers reviewing a PR:

- [ ] Cites public, verifiable sources for any factual claim
- [ ] No PII, no real-patient data
- [ ] Tests no claims that have already been disproved (e.g., "TN UCSPA gives a private right of action" — it does not; § 56-7-105 does)
- [ ] Cross-references match (template → story → BUILD_PLAN entry → CHANGELOG entry)
- [ ] Markdown renders cleanly on github.com
- [ ] Tone is helpful and patient-focused, not adversarial or paranoid

## Disagreement and conflict

Reasonable people will disagree about:

- How aggressive a template letter should be
- Whether a particular state-law citation is the strongest authority for a given proposition
- Whether a workflow step should be mandatory or optional

Default position: be conservative on legal-citation accuracy (favor verified over clever); be patient-favorable on tone (firm but not aggressive); err toward more documentation rather than less. The downside of an overly cautious letter is a slower dispute; the downside of an overly aggressive letter is a fight you didn't need to have.

## Maintainer cadence

This is a side project. Reviews are best-effort. If a PR has been open more than two weeks without response, ping the maintainer at the email listed on the GitHub profile.
