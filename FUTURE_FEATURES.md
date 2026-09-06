# Future features

Engineering-language backlog of work not yet scheduled. Sits under [USER_STORIES.md](USER_STORIES.md) (the user-value master) and [BUILD_PLAN.md](BUILD_PLAN.md) (the shipped-work tracker). When an item here is ready to ship, it moves into BUILD_PLAN.md with a version target and gets a corresponding story in USER_STORIES.md.

Items here are not promises. The kit is open-source; contributors are welcome to pick any of these up. Each item lists the rough shape of the work, the kit components that would change, and a one-line note on why it has not shipped yet.

---

## Scored index

- **state-coverage-longtail**: ship the 10 missing state law packs -> [State coverage, long tail](#state-coverage-long-tail)
  `score: kind=feature gain=3/6/15 rev=two-way hours=10/15/25 conf=opinion p=0.4 flags=legal id=state-coverage-longtail`
  `return: likelihood one-time completion of the 10 missing state packs, contributor-dependent open-source pickup with no committed date, estimated at p 0.4 of landing; impact patients in those 10 states get a dedicated, cited pack instead of the generic references/laws_state_template.md skeleton, worth an estimated 3 to 15 h of value depending on adoption, to whoever picks it up plus Jon's citation-accuracy review; evidence FUTURE_FEATURES.md 'State coverage, long tail' section (10 states, 3-6h/state estimate) and ls references/laws_state_*.md showing 40 of 50 states shipped`
  - worker: sonnet 30/45/60 h
- **spanish-localization**: minimum Spanish footprint for prompts, templates and docs -> [Spanish localization](#spanish-localization)
  `score: kind=feature gain=10/25/60 rev=two-way hours=15/25/40 conf=opinion p=0.3 flags=legal id=spanish-localization`
  `return: likelihood one-time minimum-footprint translation, contributor/reviewer-dependent (the item itself says machine translation is not adequate and needs a bilingual medical-billing-fluent reviewer), estimated at p 0.3 of landing; impact opens the kit to the ~13.5% of US households that speak Spanish at home, at the cost of every patient-facing legal template being retranslated and re-reviewed on every future English wording change, worth an estimated 10 to 60 h of reach value; evidence FUTURE_FEATURES.md 'Spanish localization' section (40-80h minimum-footprint estimate) and the absence of any *.es.md file under templates/, llm/ or docs/`
  - worker: sonnet 40/60/90 h
- **outcomes-bank**: community-contributed anonymized outcomes database -> [Outcomes bank](#outcomes-bank)
  `score: kind=feature gain=5/10/25 rev=two-way hours=5/10/15 conf=opinion p=0.25 id=outcomes-bank`
  `return: likelihood one-time build, contributor-dependent, the item's own text calls the privacy design 'the hard part', estimated at p 0.25 of landing; impact lets future patients calibrate expected outcomes and lets the kit calibrate its own recommendations, worth an estimated 5 to 25 h of value once populated, but a botched PII-scrub design risks a real re-identification incident for a contributor who submits data (that risk belongs in risk=, not here); evidence FUTURE_FEATURES.md 'Outcomes bank' section (20-40h estimate) naming the schema, review process and append-only storage as the open design questions`
  - worker: sonnet 20/30/45 h
- **advocate-variant**: multi-patient variant for advocates -> [Advocate variant](#advocate-variant)
  `score: kind=feature gain=8/20/45 rev=two-way hours=10/20/30 conf=opinion p=0.2 flags=legal id=advocate-variant`
  `return: likelihood one-time fork, large scope (multi-tenant schema, caseload views, an authorization-and-HIPAA workflow), estimated at p 0.2 of landing; impact opens the kit to advocates handling multiple patients at once, worth an estimated 8 to 45 h of value if adopted, and the HIPAA-authorization workflow is user-facing legal surface that needs review before any advocate relies on it; evidence FUTURE_FEATURES.md 'Advocate variant' section (40-60h estimate) and the single-patient tracker.csv schema in schemas/tracker.toml that the fork would have to generalize`
  - worker: sonnet 40/55/70 h
- **turquoise-api**: live pricing via Turquoise Health API -> [Turquoise Health API integration](#turquoise-health-api-integration)
  `score: kind=feature gain=5/10/20 rev=two-way hours=3/6/10 conf=opinion p=0.15 id=turquoise-api`
  `return: likelihood one-time integration, contingent on Turquoise's commercial terms for non-commercial open-source use which are unconfirmed, estimated at p 0.15 of landing; impact live, cross-hospital negotiated-rate pricing in place of the static Medicare PFS table scripts/fetch_price_benchmarks.py bundles today, worth an estimated 5 to 20 h of stronger-benchmark value per adopter; evidence FUTURE_FEATURES.md 'Turquoise Health API integration' section (10-20h estimate) and scripts/fetch_price_benchmarks.py's current static-table plus manual-URL approach`
  - worker: sonnet 10/15/25 h
- **dollarfor-integration**: scripted Dollar For charity-care screener integration -> [Dollar For screener integration](#dollar-for-screener-integration)
  `score: kind=feature gain=4/8/18 rev=two-way hours=3/5/8 conf=opinion p=0.15 id=dollarfor-integration`
  `return: likelihood one-time integration, contingent on Dollar For having or offering an API which is unconfirmed, estimated at p 0.15 of landing; impact automates a step patients are already told to take manually via templates/letter_hardship_negotiation.md and references/resources.md, worth an estimated 4 to 18 h of saved patient/contributor time; evidence FUTURE_FEATURES.md 'Dollar For screener integration' section (10-20h estimate, API availability unconfirmed) and the existing manual reference in templates/letter_hardship_negotiation.md`
  - worker: sonnet 10/15/22 h
- **parse-990**: auto-extract IRS Form 990 Schedule H data -> [parse_990.py, auto-extract Schedule H data](#parse_990py-auto-extract-schedule-h-data)
  `score: kind=feature gain=6/12/25 rev=two-way hours=5/10/15 conf=opinion p=0.3 flags=legal id=parse-990`
  `return: likelihood one-time script, replacing the manual walkthrough in references/irs_990_review.md, estimated at p 0.3 of landing; impact the extracted charity-care, community-benefit and executive-compensation figures feed directly into the IRS Form 13909 and hardship-negotiation drafters, so a parsing bug produces a wrong number in a filed legal complaint (the kit's own no-invented-figures rule in llm/output_contracts.md:116 and THEORY.md), worth an estimated 6 to 25 h of saved manual-review time weighed against that exposure; evidence FUTURE_FEATURES.md 'parse_990.py' section (20-30h estimate including test coverage against real filings) and references/irs_990_review.md's current manual procedure`
  - worker: sonnet 20/28/35 h
- **chargemaster-comparison-helper**: additional fair-price comparables for counter-offer letters -> [In-letter chargemaster comparison helper](#in-letter-chargemaster-comparison-helper)
  `score: kind=feature gain=5/12/25 rev=two-way hours=6/12/20 conf=opinion p=0.2 risk=0.3x5 flags=legal id=chargemaster-comparison-helper`
  `return: likelihood one-time helper, the item's own text calls scraping the comparable sources 'legally fraught', estimated at p 0.2 of landing; impact adds independent fair-price anchors to the UCC 2-305 counter-offer argument in templates/letter_negotiation_counter_offer.md, worth an estimated 5 to 25 h of stronger-negotiation value, but building it by scraping (rather than a curated database) risks a cease-and-desist or a bad-faith-pricing claim against the project, which is the doing-it risk in risk= not the impact; evidence FUTURE_FEATURES.md 'In-letter chargemaster comparison helper' section (20-40h estimate) and scripts/fetch_price_benchmarks.py's current per-CPT benchmark table that this helper would extend`
  - worker: sonnet 20/30/45 h
- **sbc-parser**: parse the ACA Summary of Benefits and Coverage -> [Insurance plan SBC (Summary of Benefits and Coverage) parser](#insurance-plan-sbc-summary-of-benefits-and-coverage-parser)
  `score: kind=feature gain=4/8/18 rev=two-way hours=4/8/12 conf=opinion p=0.25 id=sbc-parser`
  `return: likelihood one-time parser complementing the existing scripts/parse_spd.py, estimated at p 0.25 of landing; impact gives patients a structured deductible/OOP-max/coinsurance profile from the standardized ACA SBC format, worth an estimated 4 to 18 h of value; evidence FUTURE_FEATURES.md 'Insurance plan SBC' section (15-25h estimate) and the existing scripts/parse_spd.py this would sit beside`
  - worker: sonnet 15/20/30 h
- **dispute-reply-classifier**: auto-recommend which reply-ladder blocks fire -> [Automated dispute-reply classifier](#automated-dispute-reply-classifier)
  `score: kind=feature gain=2/4/8 rev=two-way hours=1/2/4 conf=opinion p=0.4 flags=legal id=dispute-reply-classifier`
  `return: likelihood one-time small classifier (4-8h quoted, the smallest item on this list), estimated at p 0.4 of landing; impact automates which of the five reply-ladder blocks (A-E) in templates/letter_dispute_reply.md a drafted letter uses, so a misclassification sends the wrong legal-response block to a provider, worth an estimated 2 to 8 h of saved patient decision time weighed against that risk; evidence FUTURE_FEATURES.md 'Automated dispute-reply classifier' section (4-8h estimate) and the five named blocks in templates/letter_dispute_reply.md`
  - worker: sonnet 4/6/10 h
- **prebill-verification-helper**: pre-service benefits/GFE verification helper -> [Pre-bill insurance-verification helper](#pre-bill-insurance-verification-helper)
  `score: kind=feature gain=3/6/12 rev=two-way hours=3/5/8 conf=opinion p=0.25 flags=legal id=prebill-verification-helper`
  `return: likelihood one-time helper covering a stage (pre-service) the kit does not currently address, estimated at p 0.25 of landing; impact drafts a verification-of-benefits demand and a Good Faith Estimate demand before service, worth an estimated 3 to 12 h of value to a patient who avoids a bad bill entirely, and the new demand-letter language needs the same legal review as any other template; evidence FUTURE_FEATURES.md 'Pre-bill insurance-verification helper' section (10-15h estimate) noting the kit's current flow assumes the bill has already arrived`
  - worker: sonnet 10/13/18 h
- **dedup-v2**: content-hash dedup for re-OCR edge cases -> [Better deduplication across re-OCR runs](#better-deduplication-across-re-ocr-runs)
  `score: kind=debt gain=1/2/5 freq=4 rev=two-way hours=4/8/12 conf=opinion p=1 id=dedup-v2`
  `return: likelihood estimated 2 to 8 times a year one of the three named edge cases (account-number reformat, provider-name rebrand, partial-payment balance shift) causes a wrong merge, no telemetry exists to count it so this is opinion, not measured; impact a patient or contributor manually untangles one mis-merged tracker row, an estimated 1 to 5 h per occurrence; evidence schemas/deduplication_rules.toml's current match keys (account_number, provider_tax_id, patient_account_id, date_of_service_start) read directly, and FUTURE_FEATURES.md 'Better deduplication' section naming the three edge cases and a 15-25h v2 estimate`
  - worker: sonnet 15/20/28 h
- **litigation-hold-template**: litigation-hold notice template -> [Litigation-hold notice template](#litigation-hold-notice-template)
  `score: kind=feature gain=3/6/15 rev=two-way hours=1/2/4 conf=opinion p=0.3 flags=legal id=litigation-hold-template`
  `return: likelihood used only by patients who reach the small-claims escalation stage, which the kit's own text says its small-claims escalation reaches that point regularly, estimated at p 0.3 that a given patient needing it gets it before this ships; impact preserving relevant records before litigation, worth an estimated 3 to 15 h of avoided evidence-spoliation harm to a patient who would otherwise need it and not have it; evidence FUTURE_FEATURES.md 'Litigation-hold notice template' section (4-6h estimate) and the absence of any hold-notice template under templates/`
  - worker: sonnet 4/6/9 h
- **security-md-scope-fix**: reconcile SECURITY.md's low-risk claim with the local-ops pipeline -> [SECURITY.md scope statement, reconcile with the local-ops pipeline](#securitymd-scope-statement-reconcile-with-the-local-ops-pipeline)
  `score: kind=docs gain=1/2/4 rev=two-way hours=0.5/1/1.5 conf=assessed p=1 flags=security id=security-md-scope-fix`
  `return: likelihood the discrepancy already exists today, confirmed by reading both files, so p 1 that it is live right now rather than a chance event; impact a reader of SECURITY.md line 3 (the optional helper script uses the Python standard library only, low-risk by design) reasonably concludes nothing in scripts/ reaches the network, when scripts/README.md documents that the local-ops pipeline sends bill and EOB text to Azure OpenAI and writes patient PII to the local .medbill-dispute-kit folder, an estimated 1 to 4 h of wasted trust-verification time or a real misjudgment for whoever relies on the claim; evidence SECURITY.md line 3 read directly against the scripts/ directory listing (17 scripts, of which classify_rename_medical_bills.py through bundle_to_cloud.py are the Azure-backed pipeline) and THEORY.md's Known soft spots entry recording the same gap`
  - worker: sonnet 0.3/0.5/1 h

---

## State coverage, long tail

Ten states do not yet have a dedicated pack. The kit can still run for patients in these states using `references/laws_state_template.md` as a generic skeleton; what's missing is a worked-out file matching the 12-section structure of the existing packs.

| State         | Code | Notable considerations the pack should cover                                               |
| ------------- | ---- | ------------------------------------------------------------------------------------------ |
| Alaska        | AK   | Different SOL pattern; remote-care logistics; AK Insurance Code Title 21                   |
| Delaware      | DE   | DE Code Title 18 Insurance; small-claims jurisdictional limit; Justice of the Peace courts |
| Maine         | ME   | Maine Revised Statutes Title 24-A; LD 1101 medical-debt protections (2023)                 |
| Montana       | MT   | MCA Title 33; 8-year SOL on contracts                                                      |
| North Dakota  | ND   | NDCC Title 26.1; small-claims jurisdictional limit                                         |
| New Hampshire | NH   | RSA Title XXXVII; surprise-billing protections SB 591 (2024)                               |
| Rhode Island  | RI   | RIGL Title 27; medical-debt credit-reporting ban (Act 76, 2023)                            |
| South Dakota  | SD   | SDCL Title 58; community-impact patterns                                                   |
| Vermont       | VT   | 18 V.S.A. § 9456 hospital FAP requirements; Act 76 (2023) credit-reporting ban             |
| Wyoming       | WY   | WS Title 26; 10-year SOL on contracts                                                      |

Each state pack is ~150-300 lines of Markdown citing actual state statutes with URLs. Contribution checklist lives in `CONTRIBUTING.md`. Issue template at `.github/ISSUE_TEMPLATE/state_pack_request.yml`.

Expected effort per state: 3-6 hours of research and writing.

## Spanish localization

About 13.5% of US households speak Spanish at home. The kit is currently English-only.

The minimum useful Spanish footprint is:

- `llm/system_prompt.es.md`, Spanish version of the LLM persona.
- `templates/*_es.md` for the highest-frequency templates: itemization request, initial dispute, EOB request, 30-day warning, hardship negotiation, NSA violation, FAP application.
- `docs/START_HERE.es.md` and `docs/DECISION_TREE.es.md`.
- `FAQ.es.md` covering the top 30 questions.

Patient-facing templates carry legal weight; translations must be done by someone fluent in both languages and in US medical-billing terminology. Machine translation is not adequate for the templates without human review.

Expected effort: 40-80 hours for the minimum footprint, including review.

## Outcomes bank

A community-contributed, anonymized database of real dispute outcomes, input (bill type, state, finding) and output (resolution, time elapsed, money saved). Would let future patients calibrate expected outcomes and the kit calibrate its recommendations.

The hard part is privacy. Patients cannot share medical details without risk; even apparently-anonymized records often re-identify in small geographic areas. The kit would need:

- A submission schema that scrubs PII at the source.
- A review process for accepted submissions.
- A storage layer (likely an append-only JSON file in the repo, with PRs only).
- Patient-facing guidance on what is safe to share.

Expected effort: 20-40 hours for the schema and process; ongoing maintenance proportional to submission volume.

## Advocate variant

A version of the kit oriented for patient advocates handling multiple patients simultaneously. Differences from the patient kit:

- Multi-tenant tracker schema (one CSV per patient, with a top-level roster).
- Caseload-view scripts (across-patient deadline watcher, across-patient SOL summary).
- Advocate-facing prompts that frame the LLM as a colleague to the advocate, not a substitute for the patient.
- Authorization-and-HIPAA workflow for the advocate to act on a patient's behalf.

The state-machine pipeline already handles multi-encounter and multi-biller logic per patient; extending to multi-patient is mostly orchestration.

Expected effort: 40-60 hours for the initial fork plus the multi-patient orchestration.

## Turquoise Health API integration

`scripts/fetch_price_benchmarks.py` currently bundles a static Medicare PFS table and constructs FAIR Health / Healthcare Bluebook URLs for manual lookup. Turquoise Health's API would give live pricing data across hospitals, including the negotiated rates buried in MRFs but normalized for cross-comparison.

Turquoise's API is commercial. Use would require:

- A credentialing flow for kit users (the API is not free).
- A cache layer to avoid re-querying for the same code in the same ZIP.
- A fallback to the existing static Medicare table when the API is unavailable.

Expected effort: 10-20 hours, contingent on Turquoise's commercial terms for open-source non-commercial use.

## Dollar For screener integration

Dollar For (dollarfor.org) is a non-profit that screens patients for hospital charity care under § 501(r) and, when eligible, files the FAP application on the patient's behalf. They are referenced in `templates/letter_hardship_negotiation.md` and `references/resources.md` as the recommended first step before formal dispute action.

A scripted integration would:

- Detect non-profit hospitals from the bill's biller_name (cross-referencing the IRS Tax Exempt Organization Search).
- Run the patient through the Dollar For eligibility screener via API (if Dollar For offers one) or via a deep-link workflow (if not).
- Update tracker.csv with the screener result and Dollar For case number.

Expected effort: 10-20 hours, contingent on Dollar For having or offering an API.

## parse_990.py, auto-extract Schedule H data

`references/irs_990_review.md` walks through what to pull from a non-profit hospital's IRS Form 990 / Schedule H manually. A scripted parser would:

- Accept a hospital EIN or ProPublica Nonprofit Explorer URL.
- Download the most recent 990 (the IRS publishes them as XML).
- Extract Schedule H Part I (charity-care numbers, community-benefit expense, bad debt), Part V Section B (facility-level policy responses), and Part VII (top-executive compensation).
- Emit a structured JSON profile per hospital that the IRS-13909 drafter and the hardship-negotiation drafter consume.

The 990 XML format is well-documented but verbose. Mapping XML elements to Schedule H fields is the bulk of the work.

Expected effort: 20-30 hours including test coverage against a half-dozen real 990 filings.

## In-letter chargemaster comparison helper

The counter-offer letter currently embeds a per-CPT benchmark table comparing billed amounts to Medicare PFS and (when available) the hospital's published cash price from the MRF. A helper that pulls additional comparables, Surgery Center of Oklahoma's all-inclusive cash prices, Free Market Medical Association directory prices, Sesame marketplace prices, would strengthen the UCC § 2-305 argument by showing three or four independent fair-price anchors instead of one or two.

Most of these sources do not have public APIs. The helper would either scrape (legally fraught) or maintain a curated comparable database in `references/`.

Expected effort: 20-40 hours including the comparable database.

## Insurance plan SBC (Summary of Benefits and Coverage) parser

The ACA requires every plan to publish a standardized two-to-four-page Summary of Benefits and Coverage. The SBC is structurally consistent across plans (the ACA prescribes the format), making it more parseable than the Summary Plan Description. A parser would extract deductible / OOP-max / coinsurance / copay / coverage-tier data into a structured profile separate from the SPD profile.

The kit currently has `scripts/parse_spd.py`; an SBC parser would complement it. The SBC is patient-facing; the SPD is the full plan terms.

Expected effort: 15-25 hours.

## Automated dispute-reply classifier

The aging-letter ladder (`templates/letter_dispute_reply.md`) has five blocks (A-E) for the common patterns of non-substantive provider response: form letter, new statement at the original balance, conclusory "we reviewed" letter, hardship offer when the dispute was about coding, invitation-to-call when the patient requested writing. The user currently selects which blocks apply manually.

A classifier could read the provider's response sidecar (OCR'd from the provider's letter) and recommend which blocks fire. Implementation: a small Azure OpenAI prompt with the five block descriptions and the response text, returning a multi-label JSON.

Expected effort: 4-8 hours.

## Pre-bill insurance-verification helper

For a patient considering elective care, a helper that drafts a verification-of-benefits demand letter to the insurer plus a Good Faith Estimate demand to the provider, and tracks both responses, would let the patient know what they're signing up for before service. Currently the kit's flow assumes the bill has already arrived.

Expected effort: 10-15 hours; partly templated work, partly drafter integration.

## Better deduplication across re-OCR runs

`schemas/deduplication_rules.toml` defines how follow-up statements collapse onto an existing bill row. Currently the rules match on `account_number + provider_tax_id + DOS + balance`. Edge cases that occasionally still produce duplicates: account-number reformat on a system migration, provider-name rebrand mid-dispute, partial-payment-induced balance shifts.

A v2 dedup ruleset would add content-hashing of itemized line items as a secondary key, and would surface ambiguous matches to the user for confirmation rather than silently merging.

Expected effort: 15-25 hours including regression coverage.

## Litigation-hold notice template

When a patient anticipates litigation (the kit's small-claims escalation reaches that point regularly), federal and most state rules permit a "litigation hold" notice instructing the recipient not to destroy relevant records. A template would issue the hold to the provider, the collector if any, and the patient's plan.

The kit currently does not address evidence-spoliation risk explicitly; the implicit assumption is that providers keep records for their own statutory periods. A litigation-hold notice would close that gap.

Expected effort: 4-6 hours for the template plus drafter integration.

## SECURITY.md scope statement, reconcile with the local-ops pipeline

`SECURITY.md:3` opens with "The kit ships no executable code by default... The optional helper script in `scripts/` uses the Python standard library only. The repository is therefore low-risk by design." That sentence is accurate for `validate_tracker.py` and `deadline_watch.py`, and it is singular because it was written when those were the only two scripts. `scripts/` now also holds the local-ops pipeline (`classify_rename_medical_bills.py` through `bundle_to_cloud.py`), which sends bill and EOB text to Azure OpenAI and writes patient PII under `~/.medbill-dispute-kit/`. The in-scope list at `SECURITY.md:7` was already pluralized to "helper scripts"; the opening paragraph was not.

The risk is not a vulnerability, it is a reader who cites `SECURITY.md` as evidence that nothing in `scripts/` reaches the network or takes a dependency, and is wrong about the half of it that does. `scripts/README.md` documents the pipeline's network use correctly, so the two files currently disagree.

Work: split the claim so the two trust models are named separately rather than averaged, and decide whether the out-of-scope list should say anything about the Azure endpoint a patient configures themselves. Any wording change to a published security policy is a maintainer call, not a mechanical edit, which is why this is recorded here rather than patched. Recorded 2026-08-20.

Expected effort: under an hour once the wording is decided.

---

## Standing notes

Not scored: this is a closed pointer, not open work. "Multi-language patient-facing UI for the LLM" (the prompt chain, system_prompt/workflow/output_contracts/decision_tree, needing a Spanish parallel) is fully subsumed by the Spanish localization item in the Scored index above; its own text says so ("Expected effort: subsumed by the Spanish-localization item above"). Do not score it separately; scoring spanish-localization covers this scope.

---

## How to pick something up

1. Open a GitHub issue at [k3rt4s/medbill-dispute-kit/issues](https://github.com/k3rt4s/medbill-dispute-kit/issues) saying which item you're picking up.
2. Reference the relevant sub-bullets above so the scope is shared.
3. Open a PR when ready. The reviewer will check against `CONTRIBUTING.md` and the corresponding USER_STORIES.md story if one exists.
4. If shipped, the item moves to `BUILD_PLAN.md` (with version), gets a story in `USER_STORIES.md` (status `shipped`), and an entry in `CHANGELOG.md`.

## Related

- [USER_STORIES.md](USER_STORIES.md), user-value master.
- [BUILD_PLAN.md](BUILD_PLAN.md), shipped-and-shipping-soon engineering work.
- [roadmap.json](roadmap.json), machine-readable feature roster.
- [CONTRIBUTING.md](CONTRIBUTING.md), PR guidelines.
