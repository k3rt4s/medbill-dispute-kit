# Future features

Engineering-language backlog of work not yet scheduled. Sits under [USER_STORIES.md](USER_STORIES.md) (the user-value master) and [BUILD_PLAN.md](BUILD_PLAN.md) (the shipped-work tracker). When an item here is ready to ship, it moves into BUILD_PLAN.md with a version target and gets a corresponding story in USER_STORIES.md.

Items here are not promises. The kit is open-source; contributors are welcome to pick any of these up. Each item lists the rough shape of the work, the kit components that would change, and a one-line note on why it has not shipped yet.

---

## State coverage — long tail

Fourteen states do not yet have a dedicated pack. The kit can still run for patients in these states using `references/laws_state_template.md` as a generic skeleton; what's missing is a worked-out file matching the 12-section structure of the existing packs.

| State         | Code | Notable considerations the pack should cover                                                                     |
| ------------- | ---- | ---------------------------------------------------------------------------------------------------------------- |
| Alaska        | AK   | Different SOL pattern; remote-care logistics; AK Insurance Code Title 21                                         |
| Delaware      | DE   | DE Code Title 18 Insurance; small-claims jurisdictional limit; Justice of the Peace courts                       |
| Hawaii        | HI   | HRS Chapter 431; Prepaid Health Care Act parallel to ERISA for fully insured                                     |
| Idaho         | ID   | Idaho Code Title 41; pre-existing Idaho Patient Act protections                                                  |
| Louisiana     | LA   | Unique civil-law tradition (no UCC § 2-305 analogue — quantum meruit applies); 10-year prescription on contracts |
| Maine         | ME   | Maine Revised Statutes Title 24-A; LD 1101 medical-debt protections (2023)                                       |
| Montana       | MT   | MCA Title 33; 8-year SOL on contracts                                                                            |
| North Dakota  | ND   | NDCC Title 26.1; small-claims jurisdictional limit                                                               |
| New Hampshire | NH   | RSA Title XXXVII; surprise-billing protections SB 591 (2024)                                                     |
| Rhode Island  | RI   | RIGL Title 27; medical-debt credit-reporting ban (Act 76, 2023)                                                  |
| South Dakota  | SD   | SDCL Title 58; community-impact patterns                                                                         |
| Vermont       | VT   | 18 V.S.A. § 9456 hospital FAP requirements; Act 76 (2023) credit-reporting ban                                   |
| West Virginia | WV   | WV Code Chapter 33; UDAP Article 19                                                                              |
| Wyoming       | WY   | WS Title 26; 10-year SOL on contracts                                                                            |

Each state pack is ~150-300 lines of Markdown citing actual state statutes with URLs. Contribution checklist lives in `CONTRIBUTING.md`. Issue template at `.github/ISSUE_TEMPLATE/state_pack_request.yml`.

Expected effort per state: 3-6 hours of research and writing.

## Spanish localization

About 13.5% of US households speak Spanish at home. The kit is currently English-only.

The minimum useful Spanish footprint is:

- `llm/system_prompt.es.md` — Spanish version of the LLM persona.
- `templates/*_es.md` for the highest-frequency templates: itemization request, initial dispute, EOB request, 30-day warning, hardship negotiation, NSA violation, FAP application.
- `docs/START_HERE.es.md` and `docs/DECISION_TREE.es.md`.
- `FAQ.es.md` covering the top 30 questions.

Patient-facing templates carry legal weight; translations must be done by someone fluent in both languages and in US medical-billing terminology. Machine translation is not adequate for the templates without human review.

Expected effort: 40-80 hours for the minimum footprint, including review.

## Outcomes bank

A community-contributed, anonymized database of real dispute outcomes — input (bill type, state, finding) and output (resolution, time elapsed, money saved). Would let future patients calibrate expected outcomes and the kit calibrate its recommendations.

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

## parse_990.py — auto-extract Schedule H data

`references/irs_990_review.md` walks through what to pull from a non-profit hospital's IRS Form 990 / Schedule H manually. A scripted parser would:

- Accept a hospital EIN or ProPublica Nonprofit Explorer URL.
- Download the most recent 990 (the IRS publishes them as XML).
- Extract Schedule H Part I (charity-care numbers, community-benefit expense, bad debt), Part V Section B (facility-level policy responses), and Part VII (top-executive compensation).
- Emit a structured JSON profile per hospital that the IRS-13909 drafter and the hardship-negotiation drafter consume.

The 990 XML format is well-documented but verbose. Mapping XML elements to Schedule H fields is the bulk of the work.

Expected effort: 20-30 hours including test coverage against a half-dozen real 990 filings.

## In-letter chargemaster comparison helper

The counter-offer letter currently embeds a per-CPT benchmark table comparing billed amounts to Medicare PFS and (when available) the hospital's published cash price from the MRF. A helper that pulls additional comparables — Surgery Center of Oklahoma's all-inclusive cash prices, Free Market Medical Association directory prices, Sesame marketplace prices — would strengthen the UCC § 2-305 argument by showing three or four independent fair-price anchors instead of one or two.

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

## Multi-language patient-facing UI for the LLM

The kit's LLM prompts assume English. For Spanish-speaking patients (see "Spanish localization" above), the entire prompt chain — system_prompt, workflow, output_contracts, decision_tree — would need a Spanish parallel.

Expected effort: subsumed by the Spanish-localization item above.

---

## How to pick something up

1. Open a GitHub issue at [k3rt4s/medbill-dispute-kit/issues](https://github.com/k3rt4s/medbill-dispute-kit/issues) saying which item you're picking up.
2. Reference the relevant sub-bullets above so the scope is shared.
3. Open a PR when ready. The reviewer will check against `CONTRIBUTING.md` and the corresponding USER_STORIES.md story if one exists.
4. If shipped, the item moves to `BUILD_PLAN.md` (with version), gets a story in `USER_STORIES.md` (status `shipped`), and an entry in `CHANGELOG.md`.

## Related

- [USER_STORIES.md](USER_STORIES.md) — user-value master.
- [BUILD_PLAN.md](BUILD_PLAN.md) — shipped-and-shipping-soon engineering work.
- [roadmap.json](roadmap.json) — machine-readable feature roster.
- [CONTRIBUTING.md](CONTRIBUTING.md) — PR guidelines.
