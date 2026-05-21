# Kit index — cross-reference map

The kit has grown to 100+ files. This document is the index: by scenario, by file type, by federal law, by state. Use it to navigate when the kit feels too large to skim.

## Find by scenario

For the patient's most common questions, jump straight to:

| Scenario                                 | First read                                            | Then                                              |
| ---------------------------------------- | ----------------------------------------------------- | ------------------------------------------------- |
| I just got a stack of bills              | [`docs/START_HERE.md`](START_HERE.md)                 | [`docs/DECISION_TREE.md`](DECISION_TREE.md)       |
| Where do I start with one specific bill? | [`docs/DECISION_TREE.md`](DECISION_TREE.md)           | The template the tree points to                   |
| What mistakes should I avoid?            | [`docs/ANTI_PATTERNS.md`](ANTI_PATTERNS.md)           | —                                                 |
| What outcomes are realistic?             | [`docs/COMMON_OUTCOMES.md`](COMMON_OUTCOMES.md)       | —                                                 |
| What paperwork should I keep?            | [`docs/RECORDS_RETENTION.md`](RECORDS_RETENTION.md)   | —                                                 |
| Which LLM should I use?                  | [`llm/compatibility.md`](../llm/compatibility.md)     | [`llm/system_prompt.md`](../llm/system_prompt.md) |
| What does this acronym mean?             | [`references/glossary.md`](../references/glossary.md) | —                                                 |
| What's the FAQ?                          | [`FAQ.md`](../FAQ.md)                                 | —                                                 |
| How do I contribute?                     | [`CONTRIBUTING.md`](../CONTRIBUTING.md)               | `.github/ISSUE_TEMPLATE/`                         |

## Find by file type

### Rules (the methodology — 24 files)

| Rule                                                                                    | What it covers                                                   |
| --------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [`rules/00_principles.md`](../rules/00_principles.md)                                   | Three principles: price variation, negotiability, no-rationality |
| [`rules/01_never_pay_first.md`](../rules/01_never_pay_first.md)                         | The first move on every bill                                     |
| [`rules/02_request_itemization.md`](../rules/02_request_itemization.md)                 | Itemization request                                              |
| [`rules/03_check_cpt_codes.md`](../rules/03_check_cpt_codes.md)                         | CPT coding verification                                          |
| [`rules/04_no_surprises_act.md`](../rules/04_no_surprises_act.md)                       | Federal NSA balance-billing prohibitions                         |
| [`rules/05_negotiate_fair_price.md`](../rules/05_negotiate_fair_price.md)               | Fair-price negotiation framework                                 |
| [`rules/06_small_claims.md`](../rules/06_small_claims.md)                               | Small-claims court mechanics                                     |
| [`rules/07_appeal_insurance_denial.md`](../rules/07_appeal_insurance_denial.md)         | General insurance-denial appeals                                 |
| [`rules/08_avoid_unneeded_care.md`](../rules/08_avoid_unneeded_care.md)                 | Cheapest dispute is the bill you don't have                      |
| [`rules/09_pricing_resources.md`](../rules/09_pricing_resources.md)                     | Pricing-transparency tools                                       |
| [`rules/10_ground_ambulance.md`](../rules/10_ground_ambulance.md)                       | NSA gap; state-by-state                                          |
| [`rules/11_ppdr_walkthrough.md`](../rules/11_ppdr_walkthrough.md)                       | Federal PPDR for self-pay GFE disputes                           |
| [`rules/12_medicare_appeals.md`](../rules/12_medicare_appeals.md)                       | Medicare 5-level appeal structure                                |
| [`rules/13_emtala.md`](../rules/13_emtala.md)                                           | Emergency-care anti-dumping                                      |
| [`rules/14_hipaa_right_of_access.md`](../rules/14_hipaa_right_of_access.md)             | Records access under 45 CFR § 164.524                            |
| [`rules/15_auto_med_pay.md`](../rules/15_auto_med_pay.md)                               | Accident-related billing, hospital liens                         |
| [`rules/16_workers_comp.md`](../rules/16_workers_comp.md)                               | Workers' comp balance-billing prohibition                        |
| [`rules/17_bankruptcy_and_medical_debt.md`](../rules/17_bankruptcy_and_medical_debt.md) | Bankruptcy as a tool of last resort                              |
| [`rules/18_tricare.md`](../rules/18_tricare.md)                                         | TRICARE for military beneficiaries                               |
| [`rules/19_va_community_care.md`](../rules/19_va_community_care.md)                     | VA MISSION Act                                                   |
| [`rules/20_telehealth.md`](../rules/20_telehealth.md)                                   | Telehealth billing patterns                                      |
| [`rules/21_section_1557.md`](../rules/21_section_1557.md)                               | ACA civil rights and language access                             |
| [`rules/22_air_ambulance.md`](../rules/22_air_ambulance.md)                             | Air ambulance under NSA                                          |
| [`rules/23_aca_marketplace.md`](../rules/23_aca_marketplace.md)                         | Marketplace-plan appeal framework                                |
| [`rules/24_observation_status.md`](../rules/24_observation_status.md)                   | Medicare observation-status billing                              |

### Letter and complaint templates (30+ files)

| Template                                                                                                | When to use                                      |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| [`letter_itemization_request.md`](../templates/letter_itemization_request.md)                           | First action against any unitemized bill         |
| [`letter_request_eob.md`](../templates/letter_request_eob.md)                                           | EOB not received from insurer                    |
| [`email_biller_eob_requested.md`](../templates/email_biller_eob_requested.md)                           | Courtesy email to biller alongside EOB request   |
| [`letter_records_request_hipaa.md`](../templates/letter_records_request_hipaa.md)                       | HIPAA § 164.524 medical-records request          |
| [`letter_initial_dispute.md`](../templates/letter_initial_dispute.md)                                   | After itemization, specific finding              |
| [`letter_dispute_reply.md`](../templates/letter_dispute_reply.md)                                       | Provider replied without addressing substance    |
| [`letter_30day_warning.md`](../templates/letter_30day_warning.md)                                       | Escalation before small claims                   |
| [`letter_no_surprises_violation.md`](../templates/letter_no_surprises_violation.md)                     | NSA balance-billing violation                    |
| [`letter_request_insurer_initiate_idr.md`](../templates/letter_request_insurer_initiate_idr.md)         | Demand plan initiate federal IDR                 |
| [`letter_good_faith_estimate_request.md`](../templates/letter_good_faith_estimate_request.md)           | Uninsured / self-pay GFE demand                  |
| [`letter_ppdr_initiate.md`](../templates/letter_ppdr_initiate.md)                                       | Self-pay PPDR submission when bill > GFE+$400    |
| [`letter_insurance_appeal_erisa.md`](../templates/letter_insurance_appeal_erisa.md)                     | ERISA self-funded plan denial                    |
| [`letter_erisa_502c_penalty.md`](../templates/letter_erisa_502c_penalty.md)                             | $110/day demand for plan-document non-production |
| [`letter_medicare_appeal.md`](../templates/letter_medicare_appeal.md)                                   | Medicare Levels 1-2                              |
| [`letter_medicaid_appeal.md`](../templates/letter_medicaid_appeal.md)                                   | Medicaid MCO + state fair hearing                |
| [`letter_dental_dispute.md`](../templates/letter_dental_dispute.md)                                     | Dental downcoding/bundling                       |
| [`letter_hardship_negotiation.md`](../templates/letter_hardship_negotiation.md)                         | Correctly-billed but unaffordable                |
| [`letter_negotiation_counter_offer.md`](../templates/letter_negotiation_counter_offer.md)               | UCC § 2-305 counter-offer with benchmark table   |
| [`letter_fdcpa_validation.md`](../templates/letter_fdcpa_validation.md)                                 | Third-party collector validation                 |
| [`letter_credit_report_dispute_fcra.md`](../templates/letter_credit_report_dispute_fcra.md)             | Medical debt reported to a credit bureau         |
| [`letter_ground_ambulance.md`](../templates/letter_ground_ambulance.md)                                 | Two variants by state law                        |
| [`letter_financial_assistance_application.md`](../templates/letter_financial_assistance_application.md) | IRS § 501(r) FAP for non-profit hospitals        |
| [`letter_auto_med_pay.md`](../templates/letter_auto_med_pay.md)                                         | 3 variants for accident-related billing          |
| [`letter_wc_carrier_redirect.md`](../templates/letter_wc_carrier_redirect.md)                           | Work-related injury payer redirect               |
| [`letter_challenge_hospital_lien.md`](../templates/letter_challenge_hospital_lien.md)                   | Statutory hospital lien on tort recovery         |
| [`letter_subrogation_response.md`](../templates/letter_subrogation_response.md)                         | Plan subrogation / reimbursement claim           |
| [`small_claims_civil_warrant.md`](../templates/small_claims_civil_warrant.md)                           | County-agnostic civil-warrant skeleton           |
| [`encounter_combined_dispute.md`](../templates/encounter_combined_dispute.md)                           | Multi-provider encounter under NSA ancillary     |
| [`attorney_intake_packet.md`](../templates/attorney_intake_packet.md)                                   | Two-page case summary for attorney consult       |
| [`complaint_state_doi.md`](../templates/complaint_state_doi.md)                                         | State insurance department complaint             |
| [`complaint_cms_hpt.md`](../templates/complaint_cms_hpt.md)                                             | Federal Hospital Price Transparency complaint    |
| [`complaint_emtala.md`](../templates/complaint_emtala.md)                                               | CMS EMTALA complaint                             |
| [`complaint_hipaa_access.md`](../templates/complaint_hipaa_access.md)                                   | HHS OCR HIPAA right-of-access complaint          |
| [`complaint_irs_form_13909.md`](../templates/complaint_irs_form_13909.md)                               | IRS Form 13909 tax-exempt org complaint          |

### Reference files

| Reference                                                                                             | Use                                                                  |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| [`references/laws_federal.md`](../references/laws_federal.md)                                         | Federal-law cite source of truth                                     |
| [`references/laws_state_*.md`](../references/)                                                        | Per-state cite source of truth (36 states)                           |
| [`references/laws_state_template.md`](../references/laws_state_template.md)                           | Template for new state packs                                         |
| [`references/cpt_codes_em.md`](../references/cpt_codes_em.md)                                         | E/M coding documentation requirements                                |
| [`references/cpt_quick_reference.md`](../references/cpt_quick_reference.md)                           | High-frequency CPT/HCPCS codes                                       |
| [`references/medicare_pfs_common.csv`](../references/medicare_pfs_common.csv)                         | ~150 CPT/HCPCS rows at CY2025 national Medicare rates                |
| [`references/ncci_pairs_common.csv`](../references/ncci_pairs_common.csv)                             | NCCI unbundling pairs for the audit detector                         |
| [`references/hpt_mrf_format.md`](../references/hpt_mrf_format.md)                                     | Reading a hospital's price-transparency MRF                          |
| [`references/mrf_vendor_adapters.md`](../references/mrf_vendor_adapters.md)                           | Four supported MRF formats and the kit's fetch adapter               |
| [`references/doi_portals.md`](../references/doi_portals.md)                                           | State DOI / AG portal directory (35 states) + federal                |
| [`references/medical_debt_protection_by_state.md`](../references/medical_debt_protection_by_state.md) | 15 states: credit reporting, interest cap, charity care, itemization |
| [`references/sol_by_state.md`](../references/sol_by_state.md)                                         | 50-state written-contract SOL table for medical-debt cases           |
| [`references/irs_990_review.md`](../references/irs_990_review.md)                                     | Walkthrough of Schedule H Part I/V/VI for non-profit hospitals       |
| [`references/spd_parsing_guide.md`](../references/spd_parsing_guide.md)                               | SPD extraction field set and use cases                               |
| [`references/phone_call_scripts.md`](../references/phone_call_scripts.md)                             | Six scripts plus protocols and state recording laws                  |
| [`references/glossary.md`](../references/glossary.md)                                                 | All kit acronyms defined                                             |
| [`references/resources.md`](../references/resources.md)                                               | External patient-advocacy resources                                  |

### LLM operating files

| File                                                                    | What it does                       |
| ----------------------------------------------------------------------- | ---------------------------------- |
| [`llm/system_prompt.md`](../llm/system_prompt.md)                       | LLM persona and contract           |
| [`llm/workflow.md`](../llm/workflow.md)                                 | 5-phase end-to-end process         |
| [`llm/output_contracts.md`](../llm/output_contracts.md)                 | Format requirements for LLM output |
| [`llm/compatibility.md`](../llm/compatibility.md)                       | LLM-by-LLM guidance                |
| [`llm/QUICKSTART_short_context.md`](../llm/QUICKSTART_short_context.md) | 7-stage load for under-32k models  |

### Schemas

| Schema                                                                    | What it describes                 |
| ------------------------------------------------------------------------- | --------------------------------- |
| [`schemas/bill.toml`](../schemas/bill.toml)                               | One bill record                   |
| [`schemas/tracker.toml`](../schemas/tracker.toml)                         | Master tracker CSV                |
| [`schemas/action.toml`](../schemas/action.toml)                           | Single action history entry       |
| [`schemas/deduplication_rules.toml`](../schemas/deduplication_rules.toml) | Follow-up-statement deduplication |

### Worked examples

| Example                                                                                   | Scenario                                         |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------ |
| [`examples/walkthrough.md`](../examples/walkthrough.md)                                   | One session, three bills                         |
| [`examples/multi_encounter_walkthrough.md`](../examples/multi_encounter_walkthrough.md)   | Two encounters, 7 bills, 3 sessions over 6 weeks |
| [`examples/insurance_denial_walkthrough.md`](../examples/insurance_denial_walkthrough.md) | ERISA denial through external IRO review         |
| [`examples/small_claims_walkthrough.md`](../examples/small_claims_walkthrough.md)         | Full small-claims filing                         |

### Scripts

| Script                                                                                    | Purpose                                                            |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| [`scripts/validate_tracker.py`](../scripts/validate_tracker.py)                           | Validate tracker CSV against schemas                               |
| [`scripts/deadline_watch.py`](../scripts/deadline_watch.py)                               | Overdue actions, response windows, SOL tracking by state           |
| [`scripts/classify_rename_medical_bills.py`](../scripts/classify_rename_medical_bills.py) | Inbox intake: classify, rename, route to Billers/ or EOB/          |
| [`scripts/restructure_to_billers_eob.py`](../scripts/restructure_to_billers_eob.py)       | One-time migration from older providers/ layout                    |
| [`scripts/index_bills_and_claims.py`](../scripts/index_bills_and_claims.py)               | Per-folder `_bills.csv` and `_claims.csv` via Azure OpenAI         |
| [`scripts/match_claims_to_bills.py`](../scripts/match_claims_to_bills.py)                 | Link each EOB claim to a bill it adjudicates                       |
| [`scripts/fetch_price_benchmarks.py`](../scripts/fetch_price_benchmarks.py)               | Per-folder `_benchmarks.csv` vs Medicare + MRF data                |
| [`scripts/fetch_mrf.py`](../scripts/fetch_mrf.py)                                         | Pull hospital MRF, extract per-CPT rate bands                      |
| [`scripts/audit_billing_errors.py`](../scripts/audit_billing_errors.py)                   | Per-folder `_audit.csv` with NCCI / duplicate / modifier-25 / etc. |
| [`scripts/check_completeness.py`](../scripts/check_completeness.py)                       | Master tracker.csv: gates, encounters, state machine               |
| [`scripts/draft_letters_by_state.py`](../scripts/draft_letters_by_state.py)               | State-machine letter generator with all kit templates              |
| [`scripts/parse_spd.py`](../scripts/parse_spd.py)                                         | SPD PDF -> structured plan-profile JSON via Azure OpenAI           |
| [`scripts/log_interaction.py`](../scripts/log_interaction.py)                             | Append-only action log producer (calls, mailings, responses)       |
| [`scripts/bundle_evidence.py`](../scripts/bundle_evidence.py)                             | Per-dispute-group zip with MANIFEST.md for offsite backup          |
| [`scripts/bundle_to_cloud.py`](../scripts/bundle_to_cloud.py)                             | Push bundles to encrypted offsite via rclone                       |
| [`scripts/analyze_self_pay_election.py`](../scripts/analyze_self_pay_election.py)         | Compare insurance vs NSA self-pay path per bill                    |

### Governance and meta

| File                                          | Purpose                            |
| --------------------------------------------- | ---------------------------------- |
| [`README.md`](../README.md)                   | Project overview                   |
| [`BUILD_PLAN.md`](../BUILD_PLAN.md)           | Engineering roadmap                |
| [`USER_STORIES.md`](../USER_STORIES.md)       | User-value master                  |
| [`CHANGELOG.md`](../CHANGELOG.md)             | Release notes per Keep a Changelog |
| [`FAQ.md`](../FAQ.md)                         | Patient-facing questions           |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md)       | PR guidelines                      |
| [`CODE_OF_CONDUCT.md`](../CODE_OF_CONDUCT.md) | Contributor Covenant 2.1           |
| [`SECURITY.md`](../SECURITY.md)               | Vulnerability reporting            |
| [`LICENSE`](../LICENSE)                       | MIT                                |
| [`roadmap.json`](../roadmap.json)             | Structured feature roster          |

## Find by federal law

| Federal law                                      | Rule                                                                                                                                                                            | Template                                                                                                |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| No Surprises Act (42 U.S.C. § 300gg-111 et seq.) | [`04_no_surprises_act.md`](../rules/04_no_surprises_act.md), [`11_ppdr_walkthrough.md`](../rules/11_ppdr_walkthrough.md), [`22_air_ambulance.md`](../rules/22_air_ambulance.md) | [`letter_no_surprises_violation.md`](../templates/letter_no_surprises_violation.md)                     |
| Hospital Price Transparency (45 CFR Part 180)    | [`05_negotiate_fair_price.md`](../rules/05_negotiate_fair_price.md), [`hpt_mrf_format.md`](../references/hpt_mrf_format.md)                                                     | [`complaint_cms_hpt.md`](../templates/complaint_cms_hpt.md)                                             |
| ERISA § 502(a) (29 U.S.C. § 1132(a))             | [`07_appeal_insurance_denial.md`](../rules/07_appeal_insurance_denial.md)                                                                                                       | [`letter_insurance_appeal_erisa.md`](../templates/letter_insurance_appeal_erisa.md)                     |
| UCC § 2-305 (open price term)                    | [`05_negotiate_fair_price.md`](../rules/05_negotiate_fair_price.md)                                                                                                             | [`letter_initial_dispute.md`](../templates/letter_initial_dispute.md)                                   |
| FDCPA § 1692g (15 U.S.C. § 1692g)                | (built into the validation template)                                                                                                                                            | [`letter_fdcpa_validation.md`](../templates/letter_fdcpa_validation.md)                                 |
| IRS § 501(r) (26 U.S.C. § 501(r))                | (built into FAP application)                                                                                                                                                    | [`letter_financial_assistance_application.md`](../templates/letter_financial_assistance_application.md) |
| EMTALA (42 U.S.C. § 1395dd)                      | [`13_emtala.md`](../rules/13_emtala.md)                                                                                                                                         | [`complaint_emtala.md`](../templates/complaint_emtala.md)                                               |
| HIPAA right of access (45 CFR § 164.524)         | [`14_hipaa_right_of_access.md`](../rules/14_hipaa_right_of_access.md)                                                                                                           | [`complaint_hipaa_access.md`](../templates/complaint_hipaa_access.md)                                   |
| ACA Section 1557 (42 U.S.C. § 18116)             | [`21_section_1557.md`](../rules/21_section_1557.md)                                                                                                                             | (adapt from OCR HIPAA template)                                                                         |
| ACA appeal rights (45 CFR § 147.136)             | [`23_aca_marketplace.md`](../rules/23_aca_marketplace.md)                                                                                                                       | (adapt from ERISA appeal)                                                                               |
| Medicare appeals (42 CFR § 405.940 et seq.)      | [`12_medicare_appeals.md`](../rules/12_medicare_appeals.md), [`24_observation_status.md`](../rules/24_observation_status.md)                                                    | [`letter_medicare_appeal.md`](../templates/letter_medicare_appeal.md)                                   |
| Medicaid appeals (42 CFR § 438.402 et seq.)      | (built into template)                                                                                                                                                           | [`letter_medicaid_appeal.md`](../templates/letter_medicaid_appeal.md)                                   |
| TRICARE (10 U.S.C. § 1071-1110b)                 | [`18_tricare.md`](../rules/18_tricare.md)                                                                                                                                       | (adapt initial dispute)                                                                                 |
| VA MISSION Act (Pub. L. 115-182)                 | [`19_va_community_care.md`](../rules/19_va_community_care.md)                                                                                                                   | (adapt initial dispute)                                                                                 |

## Find by state

State packs are at `references/laws_state_<two-letter>.md`. Each follows the same structure: intro callout, 12 numbered sections, quick reference, key advantages.

Currently shipped (36 states as of v0.12.0):

AL, AR, AZ, CA, CO, CT, FL, GA, IA, IL, IN, KS, KY, MA, MD, MI, MN, MO, MS, NC, NE, NJ, NM, NV, NY, OH, OK, OR, PA, SC, TN, TX, UT, VA, WA, WI

Remaining 14 states (long tail, community PR territory):

AK, DE, HI, ID, LA, ME, MT, ND, NH, RI, SD, VT, WV, WY

## Find by privacy/scope concern

- **PII boundary:** the kit ships no patient data. Bills and trackers belong on the user's local machine; the `.gitignore` excludes them by default. [`SECURITY.md`](../SECURITY.md) defines what's in vs out of scope.
- **State law disclaimer:** verify any specific statute citation before mailing. State law changes; the kit's verification dates are noted in each state-pack header.
- **Legal advice boundary:** the kit is methodology, not advice. For disputes over $10,000, ERISA federal court, EMTALA civil action, or suspected fraud — talk to a lawyer.
- **LLM-side privacy:** see [`llm/compatibility.md`](../llm/compatibility.md) for cloud vs local privacy notes.

## Update cadence

Major versions ship as `vX.Y.0`. Patch fixes (e.g., a state-statute correction) ship as `vX.Y.Z`. State packs are dated in each file's intro paragraph; re-verify annually. Federal-law citations are dated in [`references/laws_federal.md`](../references/laws_federal.md).
