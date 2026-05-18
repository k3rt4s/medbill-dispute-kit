# Changelog

All notable changes to medbill-dispute-kit, in plain English, from the patient's perspective.

This project follows [Keep a Changelog](https://keepachangelog.com) conventions. Versions follow [Semantic Versioning](https://semver.org). The kit is instruction-only, so "version" here means a coherent snapshot of rules, references, schemas, and templates.

## [v0.3.0] — 2026-05-18

### Added

- **Ground-ambulance rule and dispute template** (`rules/10_ground_ambulance.md`, `templates/letter_ground_ambulance.md`). The federal No Surprises Act explicitly excludes ground ambulance — the single largest balance-billing gap in federal law. The kit now recognizes ground ambulance as a separate bill type, checks the patient's state against a list of 11 currently-named states with ground-ambulance protections (California, Colorado, Delaware, Georgia, Illinois, Maine, Maryland, New York, Ohio, Vermont, Washington), and routes to one of two letter variants: Variant A cites the state's balance-billing statute and demands reprocessing at in-network cost-sharing; Variant B argues UCC § 2-305 with the Medicare ambulance fee schedule as the floor. ERISA preemption guardrail is built into the variant selection.
- **IRS § 501(r) Financial Assistance Policy application template** (`templates/letter_financial_assistance_application.md`). For non-profit hospital bills, formally requests the hospital's FAP, Plain Language Summary, application form, Billing and Collections Policy, and the calculation of Amounts Generally Billed (AGB). Triggers the hospital's federal obligation under 26 CFR § 1.501(r)-6 to suspend extraordinary collection action during eligibility review. Includes presumptive-eligibility block (Medicaid/SNAP/WIC enrollment) and escalation pointer to IRS Form 13909 if the hospital is non-responsive.
- **CMS Hospital Price Transparency complaint template** (`templates/complaint_cms_hpt.md`). For when a hospital has not posted a compliant machine-readable file under 45 CFR Part 180. Files at the federal CMS portal with timestamped screenshots; produces real regulatory pressure because CMS can impose civil monetary penalties up to ~$2 million per year. Most useful as a parallel action to an underlying billing dispute, because forcing a compliant MRF unlocks the hospital's actual negotiated rates as evidence.
- **Patient-Provider Dispute Resolution walkthrough rule** (`rules/11_ppdr_walkthrough.md`). PPDR is portal-driven, not letter-driven, so it ships as a rule with a checklist rather than a template. Covers the four eligibility conditions (uninsured/self-pay, GFE entitlement, $400-over-GFE threshold, 120-day filing window), the $25 filing fee, the SDR process, and the unique protections that attach during pendency (no collections, no late fees, no credit reporting). Surfaces the parallel CMS complaint for missing-GFE scenarios.
- **Epic 7 in USER_STORIES.md** — "Cover federally-unprotected bill types." Stories 7.1 (ground ambulance), 7.2 (PPDR), 7.3 (FAP application), 7.4 (HPT complaint) all shipped.

### Changed

- **`schemas/bill.toml`** — `findings` controlled vocabulary extended with `ground_ambulance_state_protected`, `ground_ambulance_unprotected`, `ppdr_eligible`, `501r_eligible_candidate`, `hpt_mrf_noncompliance_evidence`. `next_action` enum extended with `dispute_state_balance_billing`, `dispute_ground_ambulance`, `apply_for_financial_assistance`, `file_cms_hpt_complaint`, `file_irs_501r_complaint`.
- **`schemas/action.toml`** — `action_type` enum extended with `state_balance_billing_letter_sent`, `ground_ambulance_letter_sent`, `irs_501r_complaint_filed`, `ebsa_intervention_request`.
- **`BUILD_PLAN.md`** updated: v0.3.0 marked shipped; v0.4.0 backlog reshuffled (state packs CA/TX/NY/FL moved into v0.4.0 to keep v0.3.0 focused on bill-type coverage).

### Known issues

- The 11-state ground-ambulance list in `rules/10_ground_ambulance.md` is current as of this release; legislatures move quickly in this area. Re-verify before relying. The LLM should warn the patient when using the list.

## [v0.2.0] — 2026-05-18

### Added

- **Georgia state pack** (`references/laws_state_ga.md`). Georgia has unusually strong patient-side protections — the hospital itemization duty is automatic (six business days from inpatient discharge, no written request required) and lives in the Fair Business Practices Act with a private right of action and attorney's fees. The Surprise Billing Consumer Protection Act covers ground ambulance as of January 1, 2024, closing the biggest gap in the federal No Surprises Act. Worked example covering all twelve required state-pack sections plus four Georgia-specific items (FBPA private action, hospital lien statute, charity care, wage garnishment).
- **Dedicated Tennessee state pack** (`references/laws_state_tn.md`) extracted from what had been a TN-flavored state-law template. Same content; cleaner separation. The template file (`references/laws_state_template.md`) is now a pure template covering all twelve required sections plus a contribution checklist for new state packs.
- **Hardship-negotiation letter template** (`templates/letter_hardship_negotiation.md`). For bills that are correctly coded but unaffordable. Anchors to the Medicare allowable rate, references the hospital's IRS § 501(r) Financial Assistance Policy where applicable, makes a specific dollar offer, and refuses auto-debit and interest charges.
- **FDCPA § 1692g debt-validation request template** (`templates/letter_fdcpa_validation.md`). Use within thirty days of a third-party medical-debt collector's first written contact to force production of the original-creditor name, signed contract, itemized statement, EOB, accounting, and chain of assignment. Triggers an automatic pause on collection activity until validation is provided. Includes guardrails to route the patient to a different template if the entity contacting them is the original creditor, not a third-party collector.
- **Worked-example session** (`examples/walkthrough.md`) showing the kit handling three bills in one session — an unitemized hospital stay, an upcoded ER physician fee, and a third-party collection notice — and producing three drafted letters plus a complete tracker CSV. Demonstrates every phase of `llm/workflow.md` end to end.
- **Build plan** (`BUILD_PLAN.md`) tracking versioned engineering work parallel to USER_STORIES.md. Lists everything shipped in v0.1.0, the v0.2.0 backlog completed in this release, and the planned v0.3.0/v0.4.0/v1.0.0 milestones.
- **Stories 4.6 (negotiate a hardship reduction) and 4.7 (respond to a third-party medical-debt collector)** added to `USER_STORIES.md` and marked shipped in v0.2.0.

### Changed

- **`schemas/action.toml`** action_type enum extended with `state_ag_complaint_filed`, `cms_hpt_complaint_filed`, `fdcpa_validation_request`, and `fap_application_submitted`. Existing enum values unchanged.
- **`references/laws_state_template.md`** rewritten as a pure template — all twelve required state-pack items checklist with no Tennessee content. Tennessee content is now in `laws_state_tn.md`.

### Fixed

- README correctly states Marshall Allen died May 19, 2024 (not 2022). Same fix landed in v0.1.0 but called out here for changelog completeness.

### Known issues

- The kit's state-specific routing logic in `llm/workflow.md` still names Tennessee as the default; the LLM is supposed to ask the patient's state before doing state-specific work. If the patient forgets to answer, the LLM may render Tennessee citations to a patient in another state. Hardening this is in v0.3.0.

## [v0.1.0] — 2026-05-18

### Added

- Initial public release at [github.com/k3rt4s/medbill-dispute-kit](https://github.com/k3rt4s/medbill-dispute-kit).
- **LLM operating layer** (`llm/system_prompt.md`, `llm/workflow.md`, `llm/output_contracts.md`) — the role, the five-phase end-to-end process, and the output shapes the LLM must produce.
- **Methodology rules** (`rules/00_principles.md` through `rules/09_pricing_resources.md`) — ten files extracted from Marshall Allen's *Never Pay the First Bill* covering price variation, never-pay-first, itemization, CPT coding, the No Surprises Act, negotiation, small claims, insurance appeals, avoiding unneeded care, and shopping for fair prices.
- **Federal-law reference** (`references/laws_federal.md`) — No Surprises Act, Hospital Price Transparency Rule, ERISA § 502(a), UCC § 2-305 verbatim, FDCPA, IRS § 501(r), credit-bureau voluntary changes, Patient-Provider Dispute Resolution. Each with statutory citation and source URL.
- **CPT E/M reference** (`references/cpt_codes_em.md`) — documentation requirements for ER visits 99281-99285 and office visits 99202-99215 under the 2021 and 2023 AMA revisions. Includes copyright caveat (AMA-owned; the file paraphrases under fair use).
- **External resources** (`references/resources.md`) — Turquoise Health, FAIR Health Consumer, Healthcare Bluebook, GoodRx, Cost Plus Drugs, Dollar For, Undue Medical Debt, Laurie Todd, DOL EBSA, the Marshall Allen Project.
- **Tennessee state-law layer** (originally in `references/laws_state_template.md` as a TN-flavored worked example; moved to `references/laws_state_tn.md` in v0.2.0).
- **TOML schemas** (`schemas/bill.toml`, `schemas/tracker.toml`, `schemas/action.toml`, `schemas/deduplication_rules.toml`) — structured shapes the LLM emits at each phase of the workflow.
- **Letter templates** — itemization request (`letter_itemization_request.md`), initial dispute (`letter_initial_dispute.md`), 30-day warning before small claims (`letter_30day_warning.md`), No Surprises Act violation (`letter_no_surprises_violation.md`), ERISA insurance appeal (`letter_insurance_appeal_erisa.md`), state DOI complaint (`complaint_state_doi.md`).
- **Tracker** (`tracker/tracker_template.csv` and `tracker/tracker_columns.md`) — the persistent CSV state document the patient carries between sessions.
- **User stories** (`USER_STORIES.md`) — six epics covering onboarding, deduplication, diagnosis, action, multi-session persistence, and multi-state support. INVEST-aligned, with Given/When/Then acceptance criteria per workspace convention.
- **License** — MIT.
- **`.gitignore`** to keep local bill data, scanned PDFs, and personal trackers out of the repository.

[v0.3.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.3.0
[v0.2.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.2.0
[v0.1.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.1.0
