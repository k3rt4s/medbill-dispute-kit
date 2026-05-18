# Build plan — medbill-dispute-kit

The "how" doc, sitting under [USER_STORIES.md](USER_STORIES.md). Story-level "what and why" lives there; this file tracks engineering work, dependencies, and shipping order. Per workspace convention (AGENTS.md §6), this document is the engineering counterpart to user stories.

## Version status

| Version | Status  | Date       | Highlights                                                                                                                                                                                                 |
| ------- | ------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| v0.1.0  | shipped | 2026-05-18 | Initial scaffold: 33 files, full Tennessee worked example, 6 letter templates, 10 rules, federal-law references, schemas, tracker template                                                                 |
| v0.2.0  | shipped | 2026-05-18 | Georgia state pack (incl. ground-ambulance protection), dedicated TN state file, hardship + FDCPA templates, worked example, CHANGELOG, BUILD_PLAN                                                         |
| v0.3.0  | shipped | 2026-05-18 | Ground-ambulance rule + dispute template (closes the federal NSA gap), IRS § 501(r) FAP application template, CMS Hospital Price Transparency complaint template, PPDR walkthrough rule, schema extensions |
| v0.4.0  | planned | —          | CA + TX + NY state packs, Medicare/Medicaid appeal tracks, dental dispute track, schema validator                                                                                                          |
| v1.0.0  | planned | —          | 10+ state packs, full appeal coverage across plan types, glossary, FAQ, validated examples                                                                                                                 |

## v0.2.0 backlog (active)

Items listed in shipping order. Each item names the file(s) it touches and the USER_STORIES.md story it advances.

- [x] **BUILD_PLAN.md** — this file. Tracks engineering work. No story; meta.
- [x] **Refactor Tennessee out of `references/laws_state_template.md`** into a dedicated `references/laws_state_tn.md`. Reduce the template file to a pure skeleton. Lets state packs grow without bloating the template. Story 6.1.
- [x] **`references/laws_state_ga.md`** — Georgia state pack, full worked example like TN. **GA ships with ground-ambulance protection (§ 33-20E-1 et seq. as amended by HB 286, effective 2024-01-01) and FBPA private right of action with attorney's fees (§ 10-1-399)** — two structural advantages over TN. Story 6.1.
- [x] **`templates/letter_hardship_negotiation.md`** — for bills that are correctly coded but unaffordable. References IRS § 501(r) for non-profit hospitals, points at Dollar For for screening. Story 4.6 (shipped).
- [x] **`templates/letter_fdcpa_validation.md`** — § 1692g validation request to a third-party medical-debt collector within 30 days of first contact. Story 4.7 (shipped).
- [x] **`examples/walkthrough.md`** — synthetic patient walking through intake → diagnosis → letter → tracker, covering hospital, ER physician, and third-party collector bills. Story 1.1 acceptance.
- [x] **`CHANGELOG.md`** — baseline v0.1.0 + v0.2.0 entry. Per AGENTS.md §8.
- [x] **README.md** updates — reference new state packs, examples, new templates.
- [x] **`schemas/action.toml`** — extended `action_type` enum to include `fdcpa_validation_request`, `state_ag_complaint_filed`, `cms_hpt_complaint_filed`, `fap_application_submitted`.
- [x] **USER_STORIES.md** — added stories 4.6 and 4.7 marked shipped (v0.2.0).

## v0.3.0 backlog (shipped)

Bill-type coverage and federal-process walkthroughs. State packs CA/TX/NY moved to v0.4.0 to keep v0.3.0 focused on coverage of bill types the kit could not previously handle (ground ambulance, charity-care, PPDR, HPT non-compliance).

- [x] `rules/10_ground_ambulance.md` + `templates/letter_ground_ambulance.md` — federal NSA explicitly excludes ground ambulance; this is the single biggest balance-billing gap. Ships with state-by-state protection table (11 states currently named) and a two-variant letter (state-protected vs. unprotected). New Epic 7. Stories 7.1 shipped.
- [x] `templates/letter_financial_assistance_application.md` — IRS § 501(r) financial-assistance policy application. Pairs with Dollar For. Story 7.3 shipped.
- [x] `templates/complaint_cms_hpt.md` — Hospital Price Transparency Rule non-compliance complaint to CMS. Story 7.4 shipped.
- [x] `rules/11_ppdr_walkthrough.md` — federal Patient-Provider Dispute Resolution is portal-driven; ships as a rule with a checklist, not a letter template. Story 7.2 shipped.
- [x] `schemas/bill.toml` — extended `findings` controlled vocabulary with `ground_ambulance_state_protected`, `ground_ambulance_unprotected`, `ppdr_eligible`, `501r_eligible_candidate`, `hpt_mrf_noncompliance_evidence`. Extended `next_action` enum with `dispute_state_balance_billing`, `dispute_ground_ambulance`, `apply_for_financial_assistance`, `file_cms_hpt_complaint`, `file_irs_501r_complaint`.
- [x] `schemas/action.toml` — extended `action_type` enum with `state_balance_billing_letter_sent`, `ground_ambulance_letter_sent`, `irs_501r_complaint_filed`, `ebsa_intervention_request`.
- [x] `USER_STORIES.md` — added Epic 7 with stories 7.1, 7.2, 7.3, 7.4 all shipped.
- [x] `CHANGELOG.md` v0.3.0 entry.
- [x] `README.md` updated to reference new files.

## v0.4.0 backlog (next)

State-pack expansion plus plan-type coverage.

- [ ] `references/laws_state_ca.md` — California (AB 72 surprise-billing predates NSA; IMR external review; $12,500 small-claims for individuals; Health & Safety Code § 1797.225 ground ambulance protection). Story 6.1.
- [ ] `references/laws_state_tx.md` — Texas (SB 1264 surprise-billing; $20,000 JP small-claims). Story 6.1.
- [ ] `references/laws_state_ny.md` — New York (Article 49; 2024 medical-debt credit-reporting ban; $5,000 small-claims; Pub. Health Law § 4906 ground ambulance). Story 6.1.
- [ ] `references/laws_state_fl.md` — Florida ($8,000 small-claims). Story 6.1.
- [ ] `templates/letter_medicare_appeal.md` + `rules/12_medicare_appeals.md` — redetermination → reconsideration → ALJ. Story 4.4 extension.
- [ ] `templates/letter_medicaid_appeal.md` — state Medicaid managed-care appeals. Story 4.4 extension.
- [ ] `templates/letter_dental_dispute.md` — hooks into TN § 56-2-305 downcoding/bundling; opens dental as a vertical. Story 3.x.
- [ ] `templates/letter_credit_bureau_dispute.md` — paid medical and sub-$500 collections under 2022 voluntary bureau changes. New Epic 7.
- [ ] `scripts/validate_tracker.py` — validates a tracker CSV against the TOML schemas. Optional helper. Story 5.2 extension.
- [ ] `examples/sample_bills/` — synthetic bill images/PDFs (clearly fictional patients) to test extraction. Story 1.2.

## v1.0.0 stretch

Things that turn this from a one-state-worked-out kit into a comprehensive resource.

- [ ] State packs for all 50 states. Long tail; community contribution territory.
- [ ] `references/glossary.md` — chargemaster, EOB, AOB, NPI, EIN, CPT, HCPCS, MDM, MRF, NCCI, AGB, IRO.
- [ ] `FAQ.md` — "I missed the 30-day window," "veterinary bills?" (no), "outside US?" (no), etc.
- [ ] `llm/compatibility.md` — Claude vs ChatGPT vs Gemini vs local; context-length and file-upload notes.
- [ ] `llm/QUICKSTART_short_context.md` — staged-load pattern demonstrated.
- [ ] `CONTRIBUTING.md` — PR submission guidance, especially for state-pack contributions.
- [ ] Spanish-language patient-facing prompts and templates.

## Stretch / ecosystem (no version target)

- [ ] Provider/advocate-side variant of the kit (one operator, many patients).
- [ ] Turquoise Health API integration for auto-lookup of fair prices given CPT + ZIP.
- [ ] Dollar For screener integration.
- [ ] Anonymized real-outcomes bank. Privacy is the hard part.
- [ ] Reverse-direction kit: tools for hospital financial counselors and patient advocates.

## Cross-cutting maintenance

Recurring work that never finishes but should be on someone's calendar:

- [ ] Verify state-statute citations annually. Laws drift; state codes get reorganized.
- [ ] Re-check the No Surprises Act regs after each CMS rulemaking. PPDR fee schedule has been revisited; ground-ambulance committee report pending.
- [ ] Re-verify external URLs in `references/resources.md` quarterly (especially marshallallenproject.org which post-dates Marshall Allen's death in May 2024).
- [ ] Re-confirm CPT documentation requirements after each AMA E/M update (last major: 2021 office codes, 2023 ED codes).

## Stories that need creation in USER_STORIES.md

The backlog above introduces work for new stories not yet captured:

- Epic 4 — Take action on a bill
  - Story 4.6 (proposed): "Negotiate a hardship reduction" — for correctly-billed but unaffordable bills.
  - Story 4.7 (proposed): "Respond to a third-party medical-debt collector" — § 1692g validation pattern.
- Epic 7 — Defend the credit report and debt-collection surface (new)
  - Story 7.1 (proposed): "Dispute a paid or sub-$500 medical collection on a credit report."
  - Story 7.2 (proposed): "Respond to a ground-ambulance balance bill where federal NSA does not apply."

These will be added to USER_STORIES.md when the corresponding templates/rules ship.

## How this doc gets updated

Per AGENTS.md §6, when a story ships, three places update in lockstep: USER_STORIES.md (status → shipped + version), `roadmap.json` if/when this repo gets one, and CHANGELOG.md. This BUILD_PLAN.md is engineering's view; checkbox items get checked off as work lands. Items in this file should be moveable up and down the priority list as we learn; deletions are fine. The persistence guarantee lives in USER_STORIES.md, not here.
