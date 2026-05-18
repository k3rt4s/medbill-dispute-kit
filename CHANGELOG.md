# Changelog

All notable changes to medbill-dispute-kit, in plain English, from the patient's perspective.

This project follows [Keep a Changelog](https://keepachangelog.com) conventions. Versions follow [Semantic Versioning](https://semver.org). The kit is instruction-only, so "version" here means a coherent snapshot of rules, references, schemas, and templates.

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

[v0.2.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.2.0
[v0.1.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.1.0
