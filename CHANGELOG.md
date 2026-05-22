# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to medbill-dispute-kit, in plain English, from the patient's perspective.

This project follows [Keep a Changelog](https://keepachangelog.com) conventions. Versions follow [Semantic Versioning](https://semver.org). The kit is instruction-only, so "version" here means a coherent snapshot of rules, references, schemas, and templates.

## [v0.13.2] — 2026-05-22

### Added

- **Workstation-local configuration via `kit_config.toml`.** Previously, three pipeline overrides (`ALWAYS_SKIP_SLUGS`, `FOLDER_TEMPLATE_OVERRIDES`, `BILLER_STATE_OVERRIDES`) had to be edited inline in the kit's Python sources, which created a recurring "do not commit this hunk" risk and made it impossible to push a workstation-tuned kit without scrubbing first. The three overrides now load from a single TOML file at `<HEALTHBILLS_ROOT>/kit_config.toml` (overridable via the `MEDBILL_KIT_CONFIG_FILE` env var). The public kit ships with safe empty defaults; the workstation's config lives outside the kit's source tree entirely and is never tracked in any repo.
- TOML config sections: `[always_skip_slugs] slugs = [...]`, `[folder_template_overrides] <slug> = "<template_key>"`, `[biller_state_overrides] <slug> = "<two-letter-code>"`.
- Both `scripts/check_completeness.py` and `scripts/draft_letters_by_state.py` ship a private `_load_kit_config()` helper using `tomllib` (stdlib, Python 3.11+). Missing or unreadable config file returns an empty dict so the pipeline still works on a fresh checkout.

### Changed

- `scripts/check_completeness.py` and `scripts/draft_letters_by_state.py` — three formerly-inline workstation dicts are now loaded from config; the inline-comment "WORKSTATION-LOCAL — do not commit" markers are gone because the data simply doesn't live in source any more.

## [v0.13.1] — 2026-05-21

### Fixed

- **WC / auto-medpay false positive on form-label checkbox blocks.** `scripts/draft_letters_by_state.py` was mis-routing every bill whose template printed the "Please indicate if applicable: AUTO ACCIDENT / WORKER'S COMPENSATION / Date of Injury" form-field labels to the WC carrier redirect or auto-medpay letter, even though those labels are checkbox-style Y/N fields, not positive answers. The detector now strips the form-label block (header line plus ~6 immediately following lines) before counting injury keywords, so the labels themselves no longer trigger. Narrative mentions of WC / MVA elsewhere in the bill still trigger as designed. Surfaced when a Premier Radiology bill with a UB-04-style billing form generated an unwanted auto-medpay draft for a routine internal-medicine visit.

## [v0.13.0] — 2026-05-21

The Marshall Allen methodology release. Brings the "Never Pay the First Bill" workflow into the local-ops pipeline end-to-end.

### Added

- **Price benchmarking against Medicare PFS** (`scripts/fetch_price_benchmarks.py`, `references/medicare_pfs_common.csv`). Per-folder `_benchmarks.csv` with billed vs Medicare ratio and FAIR Health / Bluebook URLs. CY2025 national rates for ~150 codes across ED, observation, inpatient, radiology, lab, cardiology, OB/GYN, mental health, PT, immunizations, drugs.
- **Negotiated counter-offer template and drafter integration** (`templates/letter_negotiation_counter_offer.md`). UCC § 2-305 framing with embedded benchmark table; auto-computed offer at 200 % of Medicare allowables (or 20 % of balance fallback).
- **State DOI / AG portal directory** (`references/doi_portals.md`). 35-state portal directory plus federal parallel filings. Drafter emits `COMPLAINT_DOI.md` alongside the main letter.
- **Small-claims civil-warrant skeleton** (`templates/small_claims_civil_warrant.md`). County-agnostic with five claim theories preserved.
- **Billing-error audit detector** (`scripts/audit_billing_errors.py`, `references/ncci_pairs_common.csv`). Per-folder `_audit.csv` from duplicate-CPT, NCCI unbundling, modifier-25 stacking, late-fee, service-not-received, and quantity-inflation detectors.
- **HIPAA records request template** (`templates/letter_records_request_hipaa.md`). Invokes 45 CFR § 164.524 with state per-page fee caps.
- **GFE and PPDR templates for the NSA self-pay path** (`templates/letter_good_faith_estimate_request.md`, `templates/letter_ppdr_initiate.md`).
- **Hospital lien and subrogation response templates** (`templates/letter_challenge_hospital_lien.md`, `templates/letter_subrogation_response.md`). Six-ground lien challenge; made-whole, common-fund, allocation, NSA-carve-out defenses.
- **FCRA credit-report dispute template** (`templates/letter_credit_report_dispute_fcra.md`). Eight grounds covering federal CFPB rule, bureau policies, state bans, active dispute, paid-by-insurance, identity theft, outdated reporting.
- **Insurer-IDR request template** (`templates/letter_request_insurer_initiate_idr.md`). Demands the plan initiate federal IDR and confirms patient cost-sharing is fixed at the in-network amount.
- **Workers' compensation carrier redirect template** (`templates/letter_wc_carrier_redirect.md`). Drafter sidecar-keyword detection routes work-related-injury bills to WC redirect and motor-vehicle bills to auto med-pay in parallel with the regular dispute flow.
- **Encounter clustering and combined dispute letter** (`scripts/check_completeness.py`, `templates/encounter_combined_dispute.md`). Bills with overlapping DOS (±1 day) share an `E-YYYY-NNN` encounter id; encounters with 4+ billers and an EOB on file get a single combined letter anchored to the alphabetically-first bill id.
- **Aging-letter ladder** (`templates/letter_dispute_reply.md`). Second written dispute with blocks A–E for non-substantive responses.
- **ERISA § 502(c)(1) statutory-penalty template** (`templates/letter_erisa_502c_penalty.md`). Computes $110/day from the 30-day window with a 15-day cure period.
- **Interaction log producer** (`scripts/log_interaction.py`). Append-only `actions.csv` rows validated against `schemas/action.toml`, with bill-id existence check against `tracker.csv`.
- **Evidence bundler and cloud push** (`scripts/bundle_evidence.py`, `scripts/bundle_to_cloud.py`). Per-dispute zip with `MANIFEST.md`; rclone-based offsite push with `--immutable`.
- **Medical-debt SOL tracking** (`references/sol_by_state.md`, `scripts/deadline_watch.py --sol --state`). Surfaces accounts past or near the state's written-contract SOL with a re-aging reminder.
- **State medical-debt protection summary** (`references/medical_debt_protection_by_state.md`). 15-state index across credit reporting, interest cap, charity-care screening, itemized-bill statute.
- **IRS Form 990 community-benefit review reference** (`references/irs_990_review.md`). Schedule H Part I/V/VI walkthrough.
- **Hospital MRF lookup** (`scripts/fetch_mrf.py`, `references/mrf_vendor_adapters.md`). Four-format adapter (CMS template JSON / CSV, Turquoise CSV, TransparentRx JSON, Epic-native CSV) emitting per-CPT rate bands.
- **SPD parser** (`scripts/parse_spd.py`, `references/spd_parsing_guide.md`). Azure OpenAI-driven structured plan-profile extraction.
- **Phone-call scripts and protocols** (`references/phone_call_scripts.md`). Six scripts plus universal protocols and a state-by-state recording-law list. Kit remains mail-first; scripts are provided for community use.
- **Stories 19.1–19.23** added to `USER_STORIES.md`.

### Changed

- **`schemas/tracker.toml`** — added `encounter_id`, `benchmarks_available`, `counter_offer_amount`, the operational date+tracking triples for counter-offer / DOI / small-claims, and the corresponding `drafted_*` paths. `next_action` enum expanded.
- **`schemas/action.toml`** — added 12 new action types covering records, GFE, IDR, subrogation, counter-offer outcomes, advocate/CFO calls, bundle archive, audit findings.
- **`scripts/check_completeness.py`** — encounter clustering, benchmarks gate, expanded `derive_status` covering counter-offer / DOI / small-claims branches.
- **`scripts/draft_letters_by_state.py`** — registers all new templates; passes benchmark table, encounter-sibling summary, and state portal data to the LLM via the new `extras` channel; auto-computes counter-offer; detects accident vs work-injury routing.
- **`references/resources.md`** — FMMA, DPC Frontier, Sesame, PatientRightsAdvocate cash-pay comparables.
- **`scripts/README.md`** — documents all new scripts, encounter clustering, available FOLDER_TEMPLATE_OVERRIDES keys.
- **`roadmap.json`** — v0.13.0 features added.

## [v0.12.0] — 2026-05-19

### Added

- **Kansas state pack** (`references/laws_state_ks.md`). Kansas Consumer Protection Act (K.S.A. § 50-623 et seq.) with mandatory attorney's fees; small claims K.S.A. § 61-2702 with attorneys typically prohibited. Note: Kansas does not recognize common-law first-party bad-faith tort (Spencer v. Aetna 1979); limited remedy under K.S.A. § 40-256 attorney-fees statute.
- **Mississippi state pack** (`references/laws_state_ms.md`). Tighe v. Crosthwait common-law first-party bad-faith with punitive-damages exposure; Mississippi Consumer Protection Act (Miss. Code § 75-24); Justice Court small claims at $3,500. Mississippi has no general hospital lien statute (a defensive advantage).
- **New Mexico state pack** (`references/laws_state_nm.md`). Hovet v. Allstate UCSPA private right of action under § 59A-16-30 (unusually patient-favorable); Sloan v. State Farm common-law bad-faith tort; Surprise Billing Protection Act § 59A-57 includes ground ambulance protection at § 59A-57-7. NM Unfair Practices Act with treble damages and attorney's fees.
- **Nebraska state pack** (`references/laws_state_ne.md`). Braesch v. Union Ins. common-law first-party bad-faith; Nebraska Consumer Protection Act; County Court small claims at $3,900 with attorneys typically prohibited.
- **INDEX.md cross-reference map** (`docs/INDEX.md`). The single-page navigation index covering all 100+ files in the kit: by scenario, by file type, by federal law, by state. Intended for users navigating the now-large kit.
- **FAQ refresh** (`FAQ.md`). 18 new questions covering v0.6-v0.11 content: EMTALA, HIPAA right of access, auto med-pay, workers' comp, bankruptcy, TRICARE, VA Community Care, telehealth, ground ambulance, air ambulance, observation status, ACA marketplace, Section 1557. Plus process-and-tooling questions covering the deadline watcher, decision tree, common outcomes, anti-patterns, records retention, START_HERE, CPT quick-reference, HPT MRF format.
- **Stories 18.1-18.3** added to `USER_STORIES.md`.

### Changed

- **`BUILD_PLAN.md`** — v0.12.0 marked shipped; v1.0.0 status updated to 36 state packs.
- **`README.md`** — state-pack list expanded to 36; INDEX referenced.
- **`llm/QUICKSTART_short_context.md`** — Stage 2 state list expanded.
- **`roadmap.json`** — v0.12.0 features added.

### Known issues

- 36 state packs cover roughly 84% of US population. Remaining 14 states (AK, DE, HI, ID, LA, ME, MT, ND, NH, RI, SD, VT, WV, WY) open for community PRs.

## [v0.11.0] — 2026-05-19

### Added

- **Utah state pack** (`references/laws_state_ut.md`). Beck v. Farmers common-law first-party bad-faith doctrine; Utah Consumer Sales Practices Act; small-claims $15,000 limit (high).
- **Iowa state pack** (`references/laws_state_ia.md`). 10-year SOL on written contracts (Iowa Code § 614.1(5)) tied for longest in US; Dolan v. Aid Ins. Co. common-law bad-faith; Iowa Consumer Fraud Act and Private Right of Action for Consumer Frauds Act.
- **Nevada state pack** (`references/laws_state_nv.md`). NRS § 686A.310 with private right of action (per Allstate v. Miller 2009); Bartgis common-law bad-faith; AB 469 (2019) strong pre-NSA balance-billing protection at NRS § 439B.700 et seq.
- **Arkansas state pack** (`references/laws_state_ar.md`). Aetna v. Broadway Arms common-law bad-faith; Arkansas Deceptive Trade Practices Act with private right of action; small-claims $5,000 limit with attorneys typically prohibited.
- **CPT/HCPCS quick reference** (`references/cpt_quick_reference.md`). Highest-frequency codes for E/M, imaging, lab, common procedures, surgical, ambulance, DME, J-codes. Common modifiers and place-of-service codes. Honors AMA copyright via paraphrase.
- **Hospital Price Transparency MRF format reference** (`references/hpt_mrf_format.md`). CMS template format, discoverable-URL pattern (`/cms-hpt.txt`), how to read the CSV, common compliance failures, citation patterns for dispute letters.
- **Stories 17.1-17.3** added to `USER_STORIES.md`.

### Changed

- **`BUILD_PLAN.md`** — v0.11.0 marked shipped; v1.0.0 status updated to 32 state packs.
- **`README.md`** — state-pack list expanded to 32; new reference docs noted.
- **`llm/QUICKSTART_short_context.md`** — Stage 2 state list expanded.
- **`roadmap.json`** — v0.11.0 features added.

### Known issues

- 32 state packs cover roughly 82% of US population. Remaining 18 states open for community PRs.
- The CPT quick-reference is paraphrased per AMA copyright; full descriptors require AMA or CMS lookup.

## [v0.10.0] — 2026-05-19

### Added

- **Kentucky state pack** (`references/laws_state_ky.md`). 15-year SOL on written contracts (among longest in US); State Farm v. Reeder third-party UCSPA private RoA (unusual); Wittmer v. Jones common-law bad faith.
- **Oregon state pack** (`references/laws_state_or.md`). UTPA with civil penalties and attorney's fees; ORS § 442.563 et seq. Hospital Financial Assistance; Balance Billing Protection Act.
- **Oklahoma state pack** (`references/laws_state_ok.md`). Christian v. American Home Assur. robust common-law bad-faith doctrine with punitive damages; Oklahoma Consumer Protection Act original-creditor reach.
- **Connecticut state pack** (`references/laws_state_ct.md`). CUTPA punitive damages plus attorney's fees plus class actions; state-mandated comprehensive hospital FA under § 19a-509b; CT Medical Debt Reform Act 2024.
- **ACA marketplace appeal rule** (`rules/23_aca_marketplace.md`). 45 CFR § 147.136 internal/external appeal framework, IRO binding decision, parallel state DOI complaint, civil action after exhaustion. Distinct from ERISA self-funded and Medicare tracks.
- **Medicare observation-status rule** (`rules/24_observation_status.md`). Two-midnight rule (42 CFR § 412.3), MOON notice requirement (NOTICE Act), Condition Code 44 reclassification, SNF three-day inpatient rule, self-administered-drug refunds, Alexander v. Becerra observation appeal right.
- **Records retention guide** (`docs/RECORDS_RETENTION.md`). What to keep, where, for how long, naming conventions, special cases (bankruptcy, settlement, deceased patients). Conservative rule: 10 years from last activity.
- **Stories 16.1-16.3** added to `USER_STORIES.md`.

### Changed

- **`BUILD_PLAN.md`** — v0.10.0 marked shipped; v1.0.0 status updated to 28 state packs.
- **`README.md`** — state-pack list expanded to 28; new rules and RECORDS_RETENTION referenced.
- **`llm/QUICKSTART_short_context.md`** — Stage 2 and Stage 4 lists expanded for new states and rules.
- **`roadmap.json`** — v0.10.0 features added.

### Known issues

- 28 state packs cover roughly 78% of US population. Remaining 22 states open for community PRs.
- Observation-status appeal rights are still evolving post-*Alexander v. Becerra*; CMS rulemaking continues.
- The records-retention guide errs on the side of keeping documents longer than legally required; this is intentional for patient-protection but consumes more storage than minimum.

## [v0.9.0] — 2026-05-18

### Added

- **Indiana state pack** (`references/laws_state_in.md`). Erie Ins. v. Hickman common-law bad-faith doctrine with punitive damages; 2023 HB 1004 price-transparency rules; Indiana Deceptive Consumer Sales Act original-creditor reach.
- **Wisconsin state pack** (`references/laws_state_wi.md`). Anderson v. Continental Ins. common-law bad-faith with punitive damages; 6-year written-contract SOL; OCI complaint channel.
- **South Carolina state pack** (`references/laws_state_sc.md`). Nichols v. State Farm + common-law bad-faith doctrine; 3-year SOL (short relative to most states); Magistrate Court $7,500 small-claims limit.
- **Alabama state pack** (`references/laws_state_al.md`). Aetna v. Lavoie common-law bad-faith with robust punitive-damages doctrine; 6-year written-contract SOL; District Court $6,000 small-claims limit.
- **ACA Section 1557 rule** (`rules/21_section_1557.md`). Federal anti-discrimination statute (42 U.S.C. § 18116) covering race, color, national origin (language access for LEP patients), sex, age, and disability at any healthcare entity receiving federal funds. 2024 final rule under 45 CFR Part 92. HHS OCR complaint within 180 days. Three patient-billing-relevant contexts: language access, disability accommodation, disparate-impact patterns.
- **Air ambulance rule** (`rules/22_air_ambulance.md`). Federal NSA does cover air ambulance (unlike ground ambulance) at 42 U.S.C. § 300gg-112. ADA preemption of state remedies under 49 U.S.C. § 41713(b)(1) is critical context. Membership programs (Air Methods, AirMedCare Network) as a prevention pattern.
- **Common outcomes reference** (`docs/COMMON_OUTCOMES.md`). Public-source typical-outcome figures for each dispute track: settlement rates, reduction percentages, time-to-resolution. Sources include Dollar For, KFF, PatientRightsAdvocate, CFPB, ProPublica, *An Arm and a Leg* podcast.
- **Anti-patterns reference** (`docs/ANTI_PATTERNS.md`). 20+ common patient-side mistakes (paying the first bill, auto-debit on file, vague disputes, conceding non-disputed amounts, confusing EOB with bill, etc.) with the right move for each. Intended as a one-time read before starting a dispute.
- **Stories 15.1-15.4** added to `USER_STORIES.md`.

### Changed

- **`BUILD_PLAN.md`** — v0.9.0 marked shipped; v1.0.0 status updated to 24 state packs.
- **`README.md`** — state-pack list expanded to 24; new docs referenced.
- **`llm/QUICKSTART_short_context.md`** — Stage 2 expanded; Stage 4 rules list updated.
- **`roadmap.json`** — v0.9.0 features added.

### Known issues

- 24 state packs cover roughly 74% of US population. Remaining 26 states open for community PRs.
- Section 1557's regulatory interpretation (especially gender-identity and sexual-orientation protections) has been subject to litigation; verify current 45 CFR Part 92 state before relying.
- Air-ambulance regulatory landscape continues to evolve; ADA preemption may be re-examined by future legislation or Department of Transportation rulemaking.

## [v0.8.0] — 2026-05-18

### Added

- **Colorado state pack** (`references/laws_state_co.md`). Headlines: Hospital Discounted Care Act (C.R.S. § 6-20-101 et seq., HB22-1285) caps charges for qualifying uninsured patients at the average of Medicare/Medicaid rates with 4%-of-income payment plans and collections bars; C.R.S. § 10-3-1116 provides a private bad-faith remedy with 2× covered benefit, attorney's fees, and court costs; ground-ambulance protection under C.R.S. § 25.5-4-414 effective January 1, 2025 with 325%-of-Medicare floor.
- **Maryland state pack** (`references/laws_state_md.md`). Headline distinctive feature: HSCRC all-payer rate-setting system. Maryland hospitals charge the same rate to every payer; no insurer-negotiated discount differential.
- **Missouri state pack** (`references/laws_state_mo.md`). Notable: RSMo § 375.296 vexatious refusal-to-pay statute (20% of first $1,500 + 10% of excess + attorney's fees); 10-year SOL on written contracts under RSMo § 516.110 — tied for longest in the country.
- **Minnesota state pack** (`references/laws_state_mn.md`). Notable: Minnesota Debt Fairness Act (HF 4077, 2024) caps medical-debt interest; $20,000 no-attorney Conciliation Court is one of the highest pro-se-friendly small-claims limits in the country; Minn. Stat. § 604.18 first-party bad-faith remedy with taxable costs and attorney fees up to $250k.
- **TRICARE rule** (`rules/18_tricare.md`). 10 U.S.C. § 1071-1110b, 32 CFR Part 199. 15% balance-billing cap, active-duty zero-cost-share, BCAC referral, regional-contractor routing (East: Humana Military; West: TriWest as of 2024). Active-duty service members receiving any bill is routed to immediate contractor intervention.
- **VA Community Care / MISSION Act rule** (`rules/19_va_community_care.md`). Pub. L. 115-182, 38 CFR Part 17 Subpart W. Direct-billing prohibition for authorized care; Optum / TriWest TPA routing; 72-hour notification requirement for emergency-care coverage under 38 U.S.C. § 1725; VA Patient Advocate and Veterans Service Organization referral pattern.
- **Telehealth rule** (`rules/20_telehealth.md`). Place-of-service codes (02 home-other, 10 in-home, 11 office, 22 outpatient hospital), modifier coding (95 video, 93 audio-only), facility-fee appropriateness, audio-only vs video coding (99441-99443 vs 99213/14 + modifier), state telehealth-parity statutes (CA, NY, TN, TX, MA examples), licensure-across-state-lines considerations, Center for Connected Health Policy as the state-by-state tracker.
- **Decision-tree quick reference** (`docs/DECISION_TREE.md`). 14+ patient scenarios with explicit template recommendations and cross-references to the relevant rules. Intended as a printable single-page index.
- **Stories 14.1-14.4** added to `USER_STORIES.md`.

### Changed

- **`BUILD_PLAN.md`** — v0.8.0 marked shipped; v1.0.0 status updated to 20 state packs.
- **`README.md`** — state-pack list expanded to 20; rules list updated; DECISION_TREE referenced.
- **`llm/QUICKSTART_short_context.md`** — Stage 2 (state pack list) and Stage 4 (rules-by-finding list) expanded.
- **`roadmap.json`** — v0.8.0 features added; long-tail state list updated.

### Known issues

- 20 state packs cover roughly 67% of the US population by state of residence. Remaining 30 states open for community PRs.
- Telehealth rules under Medicare have been in flux post-COVID public-health-emergency rules and continue to evolve. The kit's telehealth rule reflects 2026 state of play; verify current CMS guidance.
- TRICARE regional-contractor assignments may shift; the kit's named contractors are accurate as of 2024-2026 but should be re-verified before relying on for letter drafting.

## [v0.7.0] — 2026-05-18

### Added

- **New Jersey state pack** (`references/laws_state_nj.md`). Headlines: NJ Consumer Fraud Act (N.J.S.A. 56:8-1 et seq.) with mandatory treble damages and attorney's fees for any "ascertainable loss" — one of the most patient-favorable UDAP statutes in the country; comprehensive state-funded Charity Care Program (N.J.S.A. 26:2H-18.51 et seq.) with sliding-scale eligibility up to 300% FPL; Out-of-Network Consumer Protection Act (N.J.S.A. 26:2SS-1 et seq., 2018) predating the federal NSA; Louisa Carman Medical Debt Relief Act (2024) restrictions on medical-debt credit reporting.
- **Virginia state pack** (`references/laws_state_va.md`). Headlines: Virginia Consumer Protection Act (Va. Code § 59.1-196 et seq.) with treble damages for willful violations and mandatory attorney's fees; Virginia's small-claims court bars attorneys entirely (Va. Code § 16.1-122.4) — a structural advantage for pro se patients; Balance Billing Protection Act (Va. Code § 38.2-3445 et seq., 2020) including HB 730 (2024) ground-ambulance coverage; Va. Code § 8.01-413.01 medical-debt protections.
- **Arizona state pack** (`references/laws_state_az.md`). Headlines: Proposition 209 (2022) is unusually patient-favorable — 3% interest cap on medical debt under A.R.S. § 44-1201(F), 10%/60×-minimum-wage wage-garnishment exemption, $400k homestead, and increased personal-property exemptions; Noble/Rawlings/Linthicum trilogy of common-law first-party bad-faith doctrine; small-claims court bars attorneys under A.R.S. § 22-512; Abbott v. Banner Health Network (2016) limits hospital liens to "customary charges" (insurance-contracted rates), not chargemaster.
- **Massachusetts state pack** (`references/laws_state_ma.md`). Headlines: Chapter 93A (M.G.L. c. 93A § 9) with mandatory 30-day demand-letter mechanic — failure to respond appropriately exposes the defendant to double or treble damages plus attorney's fees; AG's Office actively enforces Chapter 93A against healthcare entities; Health Safety Net Program (M.G.L. c. 118E § 9) covers uninsured patients for medically-necessary care at acute hospitals; near-universal coverage via Chapter 58 (2006) means the kit's typical workflows skew toward insurance-dispute rather than uninsured-patient cases.
- **Bankruptcy and medical debt rule** (`rules/17_bankruptcy_and_medical_debt.md`). Covers Chapter 7 vs. Chapter 13 distinctions, when bankruptcy is the right tool vs. when to dispute first or apply for charity care first, medical-debt-specific bankruptcy mechanics (no non-dischargeability, automatic stay under 11 U.S.C. § 362, the coordination problem with other dispute tracks), free and low-cost help including Upsolve for straightforward Chapter 7s.
- **Small claims walkthrough** (`examples/small_claims_walkthrough.md`). Full worked example of a Tennessee General Sessions filing for a $310 walking-boot price-gouging dispute. Covers filing decision, statement of claim drafting, exhibits checklist, hearing-day script with common defendant arguments and rebuttals, post-judgment collection mechanics.
- **Deadline-watcher script** (`scripts/deadline_watch.py`). Reads a tracker CSV and groups bills into overdue, due-soon (configurable window, default 7 days), and upcoming. Returns exit code 1 if any bill is overdue. Skips settled and closed rows. Python 3.10+ standard library only.
- **Copy-paste quickstart** (`docs/START_HERE.md`). Three-minute setup guide, opening-prompt template, and copy-paste prompts for seven common patient scenarios (stack of bills, overpriced bill, denied claim, debt collector calling, hospital charity care, old overdue bill, financial hardship).
- **Stories 13.1-13.4** added to `USER_STORIES.md` covering bankruptcy decision-making, deadline watching, small-claims walkthrough, and copy-paste quickstart.

### Changed

- **`scripts/README.md`** — documents `deadline_watch.py` usage and behavior.
- **`BUILD_PLAN.md`** — v0.7.0 marked shipped; v1.0.0 status updated to reflect 16 state packs.
- **`README.md`** — state-pack list expanded to 16; START_HERE referenced; deadline watcher mentioned.
- **`llm/QUICKSTART_short_context.md`** — Stage 2 state-pack list expanded.
- **`roadmap.json`** — v0.7.0 features added.

### Known issues

- The kit now ships 16 state packs covering roughly 60% of the US population by state of residence. Remaining 34 states open for community PRs.
- `deadline_watch.py` does not yet send notifications (email, calendar invite, etc.); it produces console output only. A future revision could add notification adapters.
- The bankruptcy rule does not include a template; non-trivial bankruptcies require an attorney and the rule's role is to identify the decision point and surface free counsel resources.

## [v0.6.0] — 2026-05-18

### Added

- **North Carolina state pack** (`references/laws_state_nc.md`). Headline: N.C. Gen. Stat. § 75-1.1 UDPA with automatic treble damages and original-creditor reach, unlocked for § 58-63-15 UCPA-predicate violations under *Gray v. N.C. Ins. Underwriting Ass'n* (2000). NC Constitution Art. X § 1 categorically prohibits wage garnishment for medical debt. Small-claims corporate-defendant rule (unauthorized-practice-of-law) requires defense counsel for corporate appearances — opposite of GA. Administrative Medical Debt Relief Initiative (HASP) has erased ~$6.5B for 2.5M North Carolinians as of late 2025. Ground-ambulance gap unclosed (HB 456 passed House 2025 but not yet enacted as of this release).
- **Michigan state pack** (`references/laws_state_mi.md`). Headline: Michigan's no-fault auto-insurance interaction with medical billing is the distinctive issue — pre-2019 unlimited-PIP regime, 2019 reforms with capped options, MCL § 500.3157 fee schedule capped at 200-230% of Medicare, *Andary v. USAA* retroactivity ruling. MCL § 500.2006 automatic 12% penalty interest is uniquely strong, accruing even when claim is reasonably in dispute per *Nickola v. MIC General Ins.* (2017). Small claims at $7,000 with attorneys prohibited entirely (MCL § 600.8408). Michigan does not recognize stand-alone common-law bad-faith tort per *Roberts v. Auto-Owners*; MCPA private right of action neutered post-*Smith v. Globe Life* (1999).
- **Washington state pack** (`references/laws_state_wa.md`). Headlines: Charity Care Act (RCW 70.170.060) is the most generous in the country — 100% free care up to 300% FPL for Tier 1 hospitals, up to 200% FPL for Tier 2, with sliding-scale up to 400%/300% respectively. Medical-debt credit-reporting ban (RCW 70.41.400(3) and RCW 70.54.475) makes any reported debt void and unenforceable. Insurance Fair Conduct Act (RCW 48.30.015) provides treble damages and attorney's fees for unreasonable denial of coverage. Balance Billing Protection Act (RCW 48.49) extended to ground ambulance via SSB 5986 effective January 1, 2025, at 325% of Medicare payment floor. Small claims attorneys prohibited (RCW 12.40.080).
- **EMTALA rule and CMS complaint template** (`rules/13_emtala.md`, `templates/complaint_emtala.md`). Covers the federal anti-dumping statute at 42 U.S.C. § 1395dd: medical screening examination, stabilizing treatment, appropriate transfer, and the prohibition on care refusal over insurance verification. CMS regulatory complaint plus the 2-year SOL on the civil action under § 1395dd(d)(2)(A). Five scenario blocks (screening failure, stabilization failure, inappropriate transfer, refusal over prior bill, active labor).
- **HIPAA right-of-access rule and OCR complaint template** (`rules/14_hipaa_right_of_access.md`, `templates/complaint_hipaa_access.md`). Covers 45 CFR § 164.524: 30-day deadline, reasonable cost-based fee cap, format and transmission rights. OCR complaint within 180 days. Six violation blocks (no response, excessive fee, refused format, procedural barriers, partial response, outright denial). Recent OCR settlements typically $40k-$240k+ per right-of-access violation.
- **Auto med-pay rule and 3-variant template** (`rules/15_auto_med_pay.md`, `templates/letter_auto_med_pay.md`). Rule covers the payer-order question (med-pay/PIP/UM-UIM/health insurance/at-fault driver's BI), state no-fault vs. tort distinction, hospital-lien dynamics. Variant A demands the auto insurer apply med-pay/PIP. Variant B demands the hospital bill health insurance instead of reserving for a settlement lien. Variant C challenges a perfected hospital lien using state-statute perfection defects, the made-whole doctrine, and chargemaster-unconscionability.
- **Workers' compensation rule** (`rules/16_workers_comp.md`). Covers the headline rule (accepted WC claims cannot generate balance bills to the patient), how WC differs from ordinary medical billing in every key dimension, state-by-state statutory citations for TN/CA/TX/NY/FL/PA/IL/OH, the contested-claim and denied-claim paths. Rule-only release; no dedicated template yet (general dispute templates with WC-specific citations are the primary tool for improper WC balance bills).
- **Roadmap** (`roadmap.json`) per AGENTS.md §7. Structured feature roster covering everything shipped in v0.1.0 through v0.6.0 plus planned and proposed items (long-tail state coverage, Spanish localization, outcomes bank, advocate variant, Turquoise/Dollar For integrations). Each feature has id, title, description, status, and (where applicable) release version + date.
- **Stories 10.1-10.2, 11.1-11.2, 12.1** added to `USER_STORIES.md` covering EMTALA, HIPAA, auto med-pay, workers' comp, and the long-tail-state framing.

### Changed

- **`schemas/bill.toml`** — `findings` controlled vocabulary extended with `emtala_violation_screening`, `emtala_violation_stabilizing`, `emtala_violation_transfer`, `emtala_threat_future_care`, `records_request_delayed`, `records_request_excessive_fee`, `records_request_denied`, `accident_related`, `hospital_lien_threatened`, `subrogation_overreach_suspected`, `work_related_injury`, `wc_claim_accepted`, `wc_claim_denied`, `wc_balance_billing_improper`. `next_action` enum extended with `request_records_hipaa`, `file_emtala_complaint`, `file_ocr_complaint`, `invoke_med_pay`, `force_health_insurance_bill`, `challenge_hospital_lien`, `redirect_to_wc_carrier`, `file_wc_appeal`, `engage_wc_attorney`, `consult_emtala_counsel`.
- **`schemas/action.toml`** — `action_type` enum extended with `emtala_complaint_filed`, `ocr_hipaa_complaint_filed`, `auto_med_pay_demand_sent`, `force_health_insurance_billing`, `hospital_lien_challenge`, `wc_carrier_redirect_sent`, `wc_appeal_filed`, `wc_attorney_engaged`.
- **`BUILD_PLAN.md`** — v0.6.0 marked shipped; v1.0.0 status updated to reflect 12 state packs.
- **`README.md`** — state-pack list expanded to 12; new rules/templates added to the templates description.
- **`llm/QUICKSTART_short_context.md`** — Stage 2 (state pack list) and Stage 5 (template list) updated for the new files.

### Known issues

- The kit now ships 12 state packs covering ~50% of US population by state of residence. The remaining 38 states will require community PRs via the `.github/ISSUE_TEMPLATE/state_pack_request.yml` form.
- Workers' compensation ships as a rule without a dedicated letter template. General-purpose dispute templates with WC-specific citations cover the common balance-billing-against-accepted-WC-claim scenario. A WC-specific template can ship in a future release if a contributor adds one.
- The auto-med-pay Variant C (challenge to a perfected hospital lien) is functionally a starting demand only; non-trivial lien disputes need an attorney, and the template flags this.

## [v0.5.0] — 2026-05-18

### Added

- **Pennsylvania state pack** (`references/laws_state_pa.md`). Headline: 42 Pa. C.S. § 8371 first-party bad-faith statute, generally regarded as the most patient-favorable in the country — punitive damages, attorney's fees, court costs, interest. Also covers Act 146 of 2020 (HB 1862) surprise billing; Magisterial District Court at $12,000; 4-year SOL on written contracts under 42 Pa. C.S. § 5525; the UTPCPL's reach over original creditors.
- **Illinois state pack** (`references/laws_state_il.md`). Headlines: Hospital Uninsured Patient Discount Act (210 ILCS 89/) caps charges for uninsured patients at 135% of cost; Fair Patient Billing Act (210 ILCS 88/); Illinois Consumer Fraud Act (815 ILCS 505/) is one of the broadest UDAP statutes in the country with original-creditor reach; 10-year SOL on written contracts under 735 ILCS 5/13-206; ground-ambulance protection at 215 ILCS 5/356z.3a effective 2023.
- **Ohio state pack** (`references/laws_state_oh.md`). Headlines: OCSPA reach over hospital corporate entities post-*Brakle v. Cleveland Clinic Foundation* (2021); Hospital Care Assurance Program (Ohio Rev. Code § 5168.14) requires hospitals to provide free care to patients ≤100% FPL; ground-ambulance coverage via Ohio Rev. Code §§ 3902.50-3902.54 effective Jan 12, 2022; corrected citations including a 6-yr written / 4-yr oral SOL post-SB 13 (2021) and Ohio's *lack* of a general hospital-lien statute (defensible advantage).
- **Multi-encounter worked example** (`examples/multi_encounter_walkthrough.md`). Two hospital encounters, seven bills, three sessions over six weeks. Demonstrates encounter linking, deduplication of follow-up statements, save/resume across sessions, response-driven re-routing when itemized bills arrive, and quantified settlement accounting.
- **Insurance-denial worked example** (`examples/insurance_denial_walkthrough.md`). ERISA self-funded plan denial of an advanced imaging study, internal appeal with treating-physician evidence, external review by an Independent Review Organization, parallel DOL EBSA intervention and state DOI complaint. Demonstrates plan-type identification as the first move in any denial dispute.
- **GitHub issue templates** (`.github/ISSUE_TEMPLATE/`). Three YAML form templates: bug report, state-pack request (with role selector for requester vs. contributor), and content correction (with source-URL requirement and severity dropdown). Plus a `config.yml` directing common questions to FAQ.md and CONTRIBUTING.md.
- **GitHub pull-request template** (`.github/PULL_REQUEST_TEMPLATE.md`). Type-of-change checkboxes covering all kit areas; quality checklist; state-pack-specific 12-section checklist; factual-correction-specific source-and-date verification.
- **Security policy** (`SECURITY.md`). Defines scope (the optional Python scripts and CI workflow), out-of-scope items (third-party services we link to, user's own data hygiene), reporting channel via maintainer email or private GitHub security advisory, and disclosure timeline.
- **Code of conduct** (`CODE_OF_CONDUCT.md`). Adapted from Contributor Covenant 2.1 with two project-specific norms: patient stories are not entertainment, and disagreements should be on the citation rather than the person.
- **Continuous integration** (`.github/workflows/ci.yml`). Runs on push and PR to main. Two jobs: validate-tracker (runs `scripts/validate_tracker.py` against the example tracker and runs pytest if `tests/` exists) and markdown-links (uses `gaurav-nelson/github-action-markdown-link-check` with retry-and-fallback configuration in `.github/markdown-link-check.json`).
- **Validator unit tests** (`tests/test_validate_tracker.py`). Eight pytest cases covering happy path, missing required column, bad date format, bad decimal format, bad enum value, bad findings token, header-order mismatch, and schema-loading sanity check. All pass.
- **Stories 9.6, 9.7, 9.8** added to `USER_STORIES.md` and marked shipped.

### Changed

- **`BUILD_PLAN.md`** — v0.5.0 marked shipped; v1.0.0 status updated to reflect nine state packs.
- **`README.md`** — state-pack list expanded to nine; new sections covering the GitHub-workflow polish.

### Known issues

- The kit's state-pack list now covers nine states comprising roughly 40% of the US population. Long-tail coverage of the remaining 41 states is open for community PRs; `.github/ISSUE_TEMPLATE/state_pack_request.yml` is the coordination channel.
- The markdown-link-check CI job is configured with `continue-on-error: true` because GitHub-hosted runners occasionally hit rate limits on external sites; failures should be triaged manually rather than treated as build breakers.

## [v0.4.0] — 2026-05-18

### Added

- **California state pack** (`references/laws_state_ca.md`). The most patient-favorable state in the kit. AB 72 surprise billing (codified at Cal. Health & Safety Code § 1371.9 and Cal. Ins. Code § 10112.8 et seq.); IMR external review under the Knox-Keene Act with ~73% favorable-to-enrollee outcomes; Hospital Fair Pricing Act (Health & Safety Code § 127400 et seq.) applies to all California hospitals not just non-profits, with 400% FPL eligibility post-AB 2297; AB 716 (2024) ground ambulance protection (HSC §§ 1371.56, 1797.124, 1797.233, Ins. Code § 10126.66); SB 1061 (2024) medical-debt credit-reporting voidance.
- **Texas state pack** (`references/laws_state_tx.md`). Headline: Texas is one of the few states with a private right of action under Chapter 541 of the Insurance Code, with treble damages for knowing violations and attorney's fees. Other notables: SB 1264 balance billing (Tex. Ins. Code Chapter 1467); SB 916 (2025) extended ground ambulance protection through Sept 2027; the Texas Constitution Art. XVI § 28 bars wage garnishment for consumer debt; Tex. Civ. Prac. & Rem. Code § 146.002 requires providers to bill within 10 months or forfeit collection.
- **New York state pack** (`references/laws_state_ny.md`). Three structural patient-side advantages: the Fair Medical Debt Reporting Act (Gen. Bus. Law § 380-j(f)) prohibits medical debt on credit reports; the Consumer Credit Fairness Act sets a 3-year statute of limitations for medical-debt actions under CPLR § 214-i; Hospital Financial Assistance Law (Pub. Health Law § 2807-k(9-a) as amended in 2024) extends FA at 400% FPL across all general hospitals with a 180-day pre-suit moratorium. Bad-faith is common-law-only under Pavia/Bi-Economy; GBL § 349 is the practical substitute with treble damages.
- **Florida state pack** (`references/laws_state_fl.md`). Headline: Fla. Stat. § 624.155 Civil Remedy Notice as the first-party bad-faith vehicle, filed electronically with the Florida DFS, with a 60-day cure period, damages that can exceed policy limits, and recovery of attorney's fees. Other notables: § 395.301 7-day itemization with "miscellaneous" line items expressly prohibited; HB 7089 (2024) added a 3-year SOL on facility medical debt and a collection-action freeze under § 395.3011; ground ambulance not yet protected (HB 425 died in 2025; successor expected); hospital liens are county-by-county post-Shands.
- **Medicare appeal track** (`rules/12_medicare_appeals.md` + `templates/letter_medicare_appeal.md`). The five-level Medicare appeal structure (Redetermination by MAC for A/B, Reconsideration by plan for C/D, QIC reconsideration, ALJ hearing at OMHA, DAB review, federal court) with the AIC thresholds ($190 for ALJ, $1,900 for federal court, both 2026), the form numbers, and the parallel routing through SHIP, Medicare Rights Center, and Center for Medicare Advocacy for free help.
- **Medicaid appeal template** (`templates/letter_medicaid_appeal.md`). Two-step process (MCO internal appeal then state fair hearing) under 42 CFR § 438.402 et seq., with Aid Paid Pending option under § 438.420 and an EPSDT-specific block for under-21 enrollees. Tennessee TennCare worked example including TennCare Solutions contact info (1-800-878-3192) and Tennessee Justice Center as a free-help option.
- **Dental dispute template** (`templates/letter_dental_dispute.md`). Covers insurer downcoding, bundling, frequency-limit denials, and virtual-credit-card payment objections, plus provider-side disputes when actual charges exceed a signed treatment plan. Hooks into Tennessee § 56-2-305 (HB 949 / SB 677, effective July 1, 2024) as the worked example.
- **Glossary** (`references/glossary.md`). Plain-English definitions for every acronym and term the kit uses across rules, templates, and references.
- **FAQ** (`FAQ.md`). 20+ questions covering kit usage, deadlines, escalation, edge cases, and contribution. Each answer cross-references the relevant rule or template.
- **LLM compatibility notes** (`llm/compatibility.md`). Coverage of Claude (Opus and Sonnet variants), ChatGPT (5 and 5 Pro), Gemini (2.5 Pro and 3), Llama 3.1/3.3 with Ollama and LM Studio, Qwen 2.5/3 with vLLM. Notes on context windows, vision capability, behaviors to watch for, and privacy considerations.
- **Short-context QUICKSTART** (`llm/QUICKSTART_short_context.md`). Seven-stage staged-load pattern for LLMs with under 32k tokens.
- **Contribution guidelines** (`CONTRIBUTING.md`). PR guidelines including the 12-section state-pack checklist, template-creation rules, schema-extension rules, coding style for optional helper scripts.
- **Optional tracker validator** (`scripts/validate_tracker.py` + `scripts/README.md`). Python 3.11+ standard-library-only script that validates a tracker CSV against the TOML schemas. Checks header order, ISO date format, decimal format, boolean format, and all enum / controlled-vocabulary fields. Returns clean exit codes.
- **Epics 8 and 9 in USER_STORIES.md** — "Plan-type coverage" (stories 8.1 Medicare, 8.2 Medicaid, 8.3 dental) and "Discoverability and contribution" (stories 9.1 glossary, 9.2 FAQ, 9.3 short-context, 9.4 contribution, 9.5 validator). All shipped v0.4.0.

### Changed

- **`schemas/bill.toml`** — `next_action` enum extended with `appeal_medicare`, `appeal_medicaid`, `appeal_dental`, `fdcpa_validation_request`.
- **`schemas/action.toml`** — `action_type` enum extended with `medicare_redetermination_filed`, `medicare_reconsideration_filed`, `medicare_alj_hearing_filed`, `medicaid_mco_appeal_filed`, `medicaid_fair_hearing_filed`, `dental_appeal_filed`.
- **`BUILD_PLAN.md`** — v0.4.0 marked shipped; v1.0.0 marked partial (six state packs done, long-tail 44 states open for community PRs).
- **`README.md`** — state-pack list expanded to six (TN, GA, CA, TX, NY, FL); template list expanded; glossary/FAQ/CONTRIBUTING/scripts/ folder references added.

### Known issues

- Long-tail state coverage (44 states) remains community-contribution territory. Use `references/laws_state_template.md` as the checklist.
- A future schema revision should add a `state_balance_billing_letter_sent` (already in `action.toml`) variant; the kit currently logs ground-ambulance Variant A as `ground_ambulance_letter_sent` regardless of whether it cited state surprise-billing or ground-ambulance-specific authority. Functionally fine; semantically loose.
- CPT and CDT descriptors remain paraphrased / cited by code only per AMA / ADA copyright. Patients needing the official full descriptors should use the CMS Physician Fee Schedule Lookup or the ADA's CDT lookup.

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

[v0.12.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.12.0
[v0.11.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.11.0
[v0.10.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.10.0
[v0.9.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.9.0
[v0.8.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.8.0
[v0.7.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.7.0
[v0.6.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.6.0
[v0.5.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.5.0
[v0.4.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.4.0
[v0.3.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.3.0
[v0.2.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.2.0
[v0.1.0]: https://github.com/k3rt4s/medbill-dispute-kit/releases/tag/v0.1.0
