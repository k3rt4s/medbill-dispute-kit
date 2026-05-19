# Build plan — medbill-dispute-kit

The "how" doc, sitting under [USER_STORIES.md](USER_STORIES.md). Story-level "what and why" lives there; this file tracks engineering work, dependencies, and shipping order. Per workspace convention (AGENTS.md §6), this document is the engineering counterpart to user stories.

## Version status

| Version | Status  | Date       | Highlights                                                                                                                                                                                                                                         |
| ------- | ------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| v0.1.0  | shipped | 2026-05-18 | Initial scaffold: 33 files, full Tennessee worked example, 6 letter templates, 10 rules, federal-law references, schemas, tracker template                                                                                                         |
| v0.2.0  | shipped | 2026-05-18 | Georgia state pack (incl. ground-ambulance protection), dedicated TN state file, hardship + FDCPA templates, worked example, CHANGELOG, BUILD_PLAN                                                                                                 |
| v0.3.0  | shipped | 2026-05-18 | Ground-ambulance rule + dispute template (closes the federal NSA gap), IRS § 501(r) FAP application template, CMS Hospital Price Transparency complaint template, PPDR walkthrough rule, schema extensions                                         |
| v0.4.0  | shipped | 2026-05-18 | CA + TX + NY + FL state packs, Medicare appeal track, Medicaid appeal template (TennCare worked example), dental dispute template, glossary, FAQ, LLM compatibility doc, short-context QUICKSTART, CONTRIBUTING, optional tracker validator script |
| v0.5.0  | shipped | 2026-05-18 | PA + IL + OH state packs (9 total), multi-encounter + insurance-denial worked examples, GitHub issue templates, PR template, SECURITY, CODE_OF_CONDUCT, basic CI (markdown link check + pytest), validator pytest coverage                         |
| v0.6.0  | shipped | 2026-05-18 | NC + MI + WA state packs (12 total, ~50% of US population), EMTALA rule + CMS complaint template, HIPAA right-of-access rule + OCR complaint template, auto med-pay rule + 3-variant template, workers' comp rule, roadmap.json                    |
| v0.7.0  | shipped | 2026-05-18 | NJ + VA + AZ + MA state packs (16 total, ~60% of US population), bankruptcy-and-medical-debt rule, small claims walkthrough, deadline-watcher script, START_HERE copy-paste quickstart                                                             |
| v0.8.0  | shipped | 2026-05-18 | CO + MD + MO + MN state packs (20 total, ~67% of US population), TRICARE rule, VA Community Care/MISSION Act rule, telehealth rule, DECISION_TREE.md quick-reference                                                                               |
| v0.9.0  | shipped | 2026-05-18 | IN + WI + SC + AL state packs (24 total, ~74% of US population), Section 1557 rule, air ambulance rule, COMMON_OUTCOMES + ANTI_PATTERNS docs                                                                                                       |
| v0.10.0 | shipped | 2026-05-19 | KY + OR + OK + CT state packs (28 total, ~78% of US population), ACA marketplace appeal rule, Medicare observation-status rule, RECORDS_RETENTION guide                                                                                            |
| v0.11.0 | shipped | 2026-05-19 | UT + IA + NV + AR state packs (32 total, ~82% of US population), CPT/HCPCS quick-reference, HPT MRF format reference                                                                                                                               |
| v0.12.0 | shipped | 2026-05-19 | KS + MS + NM + NE state packs (36 total, ~84% of US population), INDEX cross-reference map, FAQ refresh covering v0.6-v0.11 features                                                                                                               |
| v1.0.0  | partial | —          | Thirty-six state packs shipped (adds KS, MS, NM, NE to prior 32); long-tail 14-state coverage open for community PRs                                                                                                                               |

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

## v0.4.0 backlog (shipped)

State-pack expansion plus plan-type coverage plus documentation, all shipped 2026-05-18.

- [x] `references/laws_state_ca.md` — California pack. Notable: IMR ~73% favorable-to-enrollee per DMHC; Hospital Fair Pricing Act applies to all CA hospitals, not just non-profits; AB 716 ground ambulance protection. Story 6.1 shipped for CA.
- [x] `references/laws_state_tx.md` — Texas pack. Notable: Chapter 541 private right of action with treble damages for knowing violations; SB 916 (2025) extends ground ambulance protection through 2027; Texas Constitution wage-garnishment ban for consumer debt. Story 6.1 shipped for TX.
- [x] `references/laws_state_ny.md` — New York pack. Notable: Fair Medical Debt Reporting Act (Gen. Bus. Law § 380-j(f)) prohibits medical debt on credit reports; Consumer Credit Fairness Act 3-year SOL on medical debt (CPLR § 214-i); GBL § 349 as the practical bad-faith substitute with treble damages. Story 6.1 shipped for NY.
- [x] `references/laws_state_fl.md` — Florida pack. Notable: § 624.155 Civil Remedy Notice as the first-party bad-faith vehicle with potential damages exceeding policy limits; § 395.301 7-day itemization with "miscellaneous" line items prohibited; HB 7089 3-year SOL on facility medical debt + extraordinary-collection-action freeze. Story 6.1 shipped for FL.
- [x] `rules/12_medicare_appeals.md` + `templates/letter_medicare_appeal.md` — five-level Medicare appeals walkthrough (redetermination → QIC reconsideration → ALJ → DAB → federal court) covering Parts A/B, C, D. Story 8.1 shipped.
- [x] `templates/letter_medicaid_appeal.md` — Medicaid two-step appeal (MCO internal → state fair hearing) under 42 CFR § 438.402 et seq. Tennessee TennCare worked example with TennCare Solutions contact info; state-adaptation pattern for other states. Story 8.2 shipped.
- [x] `templates/letter_dental_dispute.md` — dental insurer downcoding/bundling/coverage disputes, plus provider-side bills exceeding treatment plan. Hooks into Tennessee § 56-2-305 as the worked example. Story 8.3 shipped.
- [x] `references/glossary.md` — plain-English definitions for all kit acronyms (AGB, AOB, ALJ, CDT, CMP, CRN, DPC, EPSDT, FBPA, FCCPA, FCRA, FDCPA, FDUTPA, GFE, HCPCS, HPT, IDR, IMR, IRE, IRO, LCD, MAC, MBI, MCO, MDM, MRF, MSN, NCCI, NSA, OMHA, OOP, PPDR, QIC, RVU, SDR, SHIP, SPD, TIN, TPA, UCC, UCR, UDAP, VCC). Story 9.1 shipped.
- [x] `FAQ.md` — 20+ patient-facing questions covering kit-use, deadlines, escalation, edge cases, and contribution. Story 9.2 shipped.
- [x] `llm/compatibility.md` — coverage of Claude, ChatGPT, Gemini, Llama, Qwen with context-window and vision considerations. Story 1.1 extension.
- [x] `llm/QUICKSTART_short_context.md` — 7-stage load pattern for LLMs under 32k tokens. Story 9.3 shipped.
- [x] `CONTRIBUTING.md` — PR guidelines including the 12-section state-pack checklist. Story 9.4 shipped.
- [x] `scripts/validate_tracker.py` + `scripts/README.md` — optional Python 3.11+ tracker validator with no third-party dependencies. Story 9.5 shipped.
- [x] `schemas/bill.toml` — `next_action` enum extended with `appeal_medicare`, `appeal_medicaid`, `appeal_dental`, `fdcpa_validation_request`.
- [x] `schemas/action.toml` — `action_type` enum extended with `medicare_redetermination_filed`, `medicare_reconsideration_filed`, `medicare_alj_hearing_filed`, `medicaid_mco_appeal_filed`, `medicaid_fair_hearing_filed`, `dental_appeal_filed`.
- [x] `USER_STORIES.md` — added Epic 8 (Plan-type coverage) and Epic 9 (Discoverability and contribution).
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
