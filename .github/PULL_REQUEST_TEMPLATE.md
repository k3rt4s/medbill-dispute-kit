# Pull request

<!--
Thanks for contributing. Please fill in this template so reviewers can move quickly.
For state-pack PRs, see CONTRIBUTING.md for the 12-section checklist.
-->

## What this PR does

<!-- One-paragraph summary. -->

## Type of change

<!-- Check all that apply. -->

- [ ] New state pack
- [ ] New letter or complaint template
- [ ] New rule or rule expansion
- [ ] Reference file update (laws_federal.md, cpt_codes_em.md, resources.md, glossary.md)
- [ ] Schema change (bill.toml, tracker.toml, action.toml, deduplication_rules.toml)
- [ ] Workflow / system-prompt change
- [ ] Documentation (README, FAQ, CONTRIBUTING, etc.)
- [ ] Tooling (scripts/, .github/, tests/)
- [ ] Bug or correction
- [ ] Other

## Quality checklist

- [ ] No personally identifying information about real patients, providers, or bills
- [ ] No paid-service promotion or telemetry
- [ ] Markdown renders cleanly on github.com
- [ ] Cross-references in `USER_STORIES.md`, `BUILD_PLAN.md`, `CHANGELOG.md`, `README.md` updated where applicable
- [ ] Tone is helpful and patient-focused, not adversarial or paranoid

## For state-pack PRs

- [ ] All 12 required sections per `references/laws_state_template.md` are present (or explicitly noted as "no such statute in this state")
- [ ] Every statute citation has a source URL
- [ ] Citations verified against the state's official code website (date noted in the file)
- [ ] ERISA-preemption caveats included where applicable
- [ ] "Quick reference for letter rendering" table included
- [ ] "Key [State]-specific advantages" closer included
- [ ] State added to `BUILD_PLAN.md`, `CHANGELOG.md`, `README.md`, `llm/QUICKSTART_short_context.md`

## For factual-correction PRs

- [ ] Source URL for every changed citation
- [ ] Date of verification noted

## How was this tested?

<!-- For new templates or rules: did you walk an LLM through them with synthetic data? For state packs: did you cross-check the citations against the state's official code? -->

## Anything reviewers should pay extra attention to

<!-- Especially anything you're uncertain about. Better to flag than hide. -->
