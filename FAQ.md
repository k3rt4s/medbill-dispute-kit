# FAQ

## About the kit

**What is this kit, in one sentence?**

A pack of Markdown rules, TOML schemas, and letter templates you load into any large language model along with your medical bills, and it walks you through analyzing, deduplicating, and disputing them across the months-long process.

**Who is it for?**

US patients with one or more medical bills they suspect are wrong, unfair, or unaffordable. Also useful for friends or family helping someone else navigate medical bills. Not for outside-US bills, veterinary bills, or non-medical disputes.

**Do I need to write code or run anything?**

No. The kit is instruction-only. You upload the files to an LLM (Claude.ai, ChatGPT, Gemini, a local model — any with file upload) and tell it you want to dispute medical bills. The LLM does the work using the rules in the kit. The only optional code is a small Python tracker validator in `scripts/`.

**Is this legal advice?**

No. It is a structured way to apply public laws and well-documented consumer-protection patterns. If your dispute exceeds ~$10,000, involves suspected fraud, involves an injury claim, or you are uncomfortable proceeding alone, talk to a lawyer. Free 30-minute consultations are common via state bar referral services, and legal-aid organizations exist in every state.

**Why the open license?**

The methodology is Marshall Allen's, who died in 2024 and whose successor non-profit the [Marshall Allen Project](https://www.marshallallenproject.org/) continues the work. Surprise medical bills are a national problem. Free distribution of the tools is the point.

## Using the kit

**Which LLM should I use?**

Any of the major ones work. Claude or GPT with file upload and a long context window will handle the whole kit in one shot. See [`llm/compatibility.md`](llm/compatibility.md) for specifics. For very short-context models, use the staged load described in [`llm/QUICKSTART_short_context.md`](llm/QUICKSTART_short_context.md).

**Does my data leave my computer?**

That depends on the LLM you use. Cloud LLMs (Claude.ai, ChatGPT, Gemini) process your bills on their servers; check their privacy policies. Local LLMs (Ollama, LM Studio, llama.cpp) keep everything on your machine. The kit itself ships no telemetry and connects to nothing.

**What if I'm not in Tennessee or Georgia?**

The kit ships dedicated state packs for Tennessee, Georgia, California, Texas, New York, and Florida. For any other state, the LLM uses `references/laws_state_template.md` to find your state's equivalent statutes and warns you to verify before mailing. Contributing your state's pack as a PR is welcome.

**My bill is from a non-US provider. Will this work?**

No. The kit's rules and statutes are US-only.

## Common patient questions

**The bill due date is in 5 days. What do I do?**

Do not panic and do not pay. The due date on the bill is the provider's preferred date, not a legal deadline. Your actual deadline — the point at which the bill could become collectible or affect your credit — is typically 180+ days out under federal rules. You have time to verify the bill before paying.

**I missed the 30-day deadline for [itemization / FDCPA validation / something else]. What now?**

Most deadlines in the kit are "best practice" deadlines that increase your leverage, not statutes of limitations. Missing a 30-day window for FDCPA validation, for example, doesn't bar you from disputing the debt — it just means you don't get the automatic collection-pause that § 1692g provides. The dispute itself remains available. Tell the LLM what deadline you missed and it will route to the next-best path.

**The hospital sent me to collections. Is it too late to dispute?**

No. Collections doesn't change the underlying merits of the bill. If a third-party collector is now involved, use `templates/letter_fdcpa_validation.md` to demand verification from the collector while you continue disputing with the original provider. For credit-report effects, the 2022 voluntary bureau changes mean paid medical debt and sub-$500 collections are no longer reported.

**I already paid the bill. Can I still dispute it?**

Yes, but the leverage is lower. You're now seeking a refund rather than refusing payment. The same evidence applies; the timeline drags out because the provider has your money. For small amounts a refund is sometimes uneconomic to pursue; for larger amounts (no Surprises Act violations, clear coding errors, services not received), small claims court is still the realistic venue.

**My bill is for $50,000. Is small claims really the right venue?**

If the disputed amount is above your state's small-claims jurisdictional limit (Tennessee $25,000; Georgia $15,000; California $12,500; Texas $20,000; New York $5,000-$10,000; Florida $8,000), small claims is not available. Options: split the claim into separately-actionable parts if defensible, settle for an amount within the limit, or move to regular civil court with counsel.

**My insurer denied the whole claim. Now what?**

Different path from a billing dispute. Use `templates/letter_insurance_appeal_erisa.md` for ERISA-covered employer plans, `templates/letter_medicare_appeal.md` for Medicare, `templates/letter_medicaid_appeal.md` for Medicaid. Internal appeal first, then external review. State complaint in parallel. See [`rules/07_appeal_insurance_denial.md`](rules/07_appeal_insurance_denial.md).

**I can't afford the bill even at a fair price.**

Two paths. (1) For non-profit hospitals: apply for charity care under IRS § 501(r) using `templates/letter_financial_assistance_application.md`, and run the [Dollar For](https://dollarfor.org) screener. (2) For any provider: negotiate a hardship reduction using `templates/letter_hardship_negotiation.md`. Both can run in parallel. Neither requires admitting the original bill is correct.

**The doctor's billing department says I have to pay or they won't see me anymore.**

If this is a non-profit hospital and you have an open § 501(r) FAP application, denying future care while the application is pending is itself a violation of 26 CFR § 1.501(r)-6. For non-emergency outpatient relationships, you cannot be denied future care for an unpaid bill if you are working through the dispute process in good faith. For emergencies, EMTALA prohibits denial of stabilizing treatment regardless of bills. Document the threat and add it to a state attorney general complaint.

**My ambulance bill is $4,000. Is that protected by the No Surprises Act?**

If it was **air ambulance**, yes. If it was **ground ambulance**, federal NSA does **not** cover it. About a dozen states (CA, CO, DE, GA, IL, ME, MD, NY, OH, VT, WA) have closed the gap with state laws. See [`rules/10_ground_ambulance.md`](rules/10_ground_ambulance.md). Tennessee and Florida are not on the list.

## Process questions

**The hospital isn't responding to my dispute letter. How long should I wait?**

Send the initial dispute letter, give 15 business days for substantive response. If silence, send a follow-up referencing the prior letter. After 30 days total, escalate with the 30-day warning before small claims. CC the state insurance department, attorney general, and BBB. That usually breaks the silence; if not, file.

**Do I need a lawyer for small claims court?**

No. Small claims is specifically designed for self-represented parties. Many states even prohibit attorneys at the initial hearing (e.g., California). Bring the documents, present them chronologically, stick to facts. The kit's `rules/06_small_claims.md` covers preparation in detail.

**The provider settled for less than I demanded. Should I take it?**

Usually yes. A settlement at 60-70% of the disputed amount in 2-3 months beats spending another 6-12 months in small claims court for the remaining 30-40%. Get the settlement in writing. Have it state expressly that the settled amount discharges the entire account; otherwise the provider may try to bill the remainder later.

**What if I make my bill worse by complaining?**

Providers cannot lawfully retaliate against patients for filing complaints. Many states have explicit anti-retaliation provisions. In practice, billing departments rarely retaliate because the complaint creates a documented paper trail that strengthens the patient's position in any subsequent dispute. The risk is overwhelmingly upside.

**Can I just settle quickly to make this go away?**

You can, and sometimes it's the right call (especially for small amounts at the bottom of your priority list). But quick settlement without first asking for an itemization usually means paying inflated charges. At minimum, ask "is this the best you can do?" Most billing departments will reduce 20-40% on the first ask.

## Edge cases

**My bill is more than a year old. Is it still disputable?**

Likely yes. The relevant statute of limitations for the provider to collect from you ranges from 3-6 years depending on state. The dispute process can be initiated any time before that. Specific state-by-state details in the state packs.

**The provider went out of business. Where do I send the dispute?**

Send to the listed billing address; if returned, send to the registered agent of the corporate entity (look up at the secretary of state for the state of incorporation). If the practice was acquired by another entity, send to that successor; medical-bill obligations don't typically vanish with a sale.

**I have bills from a deceased family member. Am I liable?**

Generally no, unless you co-signed or you have a filial-responsibility statute applicable in your state (rare and rarely enforced). The estate is liable to the extent of assets. Heirs are not personally liable for the decedent's medical debt absent a contractual undertaking. Consult a probate attorney in your state if assets are at stake.

**The provider is on a payment plan with me and now is suing me.**

This is unusual and likely a clerical breakdown rather than intentional. Respond to the lawsuit on time (do not default), file an answer asserting the payment plan as an affirmative defense, attach documentation. If the dollar amount is small, small claims court is the venue. Consider filing a counterclaim under your state's UDAP statute for the trouble.

**Can I use the kit to help my parent / friend?**

Yes. The LLM doesn't care whose bills they are; you'll need their authorization (or Power of Attorney for a parent who can't act for themselves) for most communications to be effective. Letters can be signed by the patient and mailed by you, or signed by an authorized representative with appropriate authority documentation attached.

**My bill is wrong but the provider says they cannot change it because it's already been adjudicated by my insurance.**

A "the insurance already paid, we can't change it" response is almost never accurate. The provider can always issue a corrected claim and refund any insurance overpayment. The patient-side leverage: refuse to pay the disputed portion, document the request for correction, escalate via state insurance department complaint if the provider insists on a wrong bill.

## Federal-protection questions (added since v0.6)

**My hospital refused to give me emergency care because I owed them money.**

That is an EMTALA violation. The Emergency Medical Treatment and Active Labor Act (42 U.S.C. § 1395dd) prohibits Medicare-participating hospitals from refusing emergency screening or stabilization over insurance or payment concerns. File a CMS complaint using [`templates/complaint_emtala.md`](templates/complaint_emtala.md). The 2-year statute of limitations on the civil action under § 1395dd(d)(2)(A) is unforgiving; consult plaintiff-side counsel if you suffered harm. See [`rules/13_emtala.md`](rules/13_emtala.md).

**My provider won't give me my medical records, or wants to charge an unreasonable fee.**

That is a HIPAA right-of-access violation under 45 CFR § 164.524. The provider must produce the records within 30 days at a reasonable cost-based fee. File an OCR complaint using [`templates/complaint_hipaa_access.md`](templates/complaint_hipaa_access.md) within 180 days of the violation. OCR settlements for right-of-access violations typically run $40k-$240k per case; mentioning OCR by name to the provider's privacy officer often resolves the issue without formal investigation. See [`rules/14_hipaa_right_of_access.md`](rules/14_hipaa_right_of_access.md).

**My bill is from a motor-vehicle accident.**

Different track. See [`rules/15_auto_med_pay.md`](rules/15_auto_med_pay.md). You have multiple potential payers (med-pay/PIP, UM/UIM, at-fault driver's liability, your health insurance) and the order matters. Hospitals sometimes try to preserve the bill for a personal-injury settlement lien at chargemaster rates instead of billing health insurance at the contracted rate — this is challengeable in most states. Use the three-variant template [`templates/letter_auto_med_pay.md`](templates/letter_auto_med_pay.md).

**I was injured at work.**

Workers' compensation territory. See [`rules/16_workers_comp.md`](rules/16_workers_comp.md). Accepted WC claims cannot generate balance bills to the patient. If a provider is billing you for a WC-covered injury, that bill is improper.

**I think bankruptcy might be the answer for my medical debt.**

It might be. See [`rules/17_bankruptcy_and_medical_debt.md`](rules/17_bankruptcy_and_medical_debt.md). Medical debt is fully dischargeable in Chapter 7. The kit's view: try the disputes, charity-care applications, and hardship negotiations first; bankruptcy is a last move because of the credit-report impact. For straightforward Chapter 7 below the means-test threshold, [Upsolve](https://upsolve.org) is a free non-profit. For everything else, consult a bankruptcy attorney.

**My family member is on TRICARE.**

TRICARE has its own federal program (10 U.S.C. § 1071-1110b) with a 15% balance-billing cap, active-duty zero-cost-share, and a regional-contractor complaint process. See [`rules/18_tricare.md`](rules/18_tricare.md). For active-duty service members, any bill is almost certainly a billing error; route immediately to the regional contractor.

**My family member is a veteran with a Community Care bill.**

Federal MISSION Act (Pub. L. 115-182) generally prohibits direct billing of veterans for authorized community care. See [`rules/19_va_community_care.md`](rules/19_va_community_care.md). The bill should be redirected to the TPA (Optum or TriWest depending on region), not paid by the veteran.

**The visit was telehealth but the bill looks weird.**

Common. Telehealth has its own coding rules. See [`rules/20_telehealth.md`](rules/20_telehealth.md). Watch for facility fees attached to home telehealth (POS code mismatches), audio-only visits billed as video, and missing or wrong modifiers. Many states have telehealth-parity statutes requiring insurers to cover at the same rate as in-person.

**My bill is from a ground ambulance, $4,000.**

Federal No Surprises Act does not cover ground ambulance — the biggest gap in the NSA. State law may cover. See [`rules/10_ground_ambulance.md`](rules/10_ground_ambulance.md) for the state-by-state table. Where covered, use [`templates/letter_ground_ambulance.md`](templates/letter_ground_ambulance.md) Variant A; where not, Variant B argues UCC § 2-305 with the Medicare ambulance fee schedule as the floor.

**My bill is from an air ambulance, $40,000.**

The federal NSA covers air ambulance (unlike ground). Balance billing is prohibited at 42 U.S.C. § 300gg-112. See [`rules/22_air_ambulance.md`](rules/22_air_ambulance.md). Note: the Airline Deregulation Act preempts most state remedies, so federal NSA enforcement is the principal lever.

**I'm on Medicare and was charged for self-administered drugs during a hospital stay.**

Likely an observation-status issue. See [`rules/24_observation_status.md`](rules/24_observation_status.md). If you were "outpatient under observation" rather than "inpatient," Medicare Part B applies and you bear cost-sharing on individual items, including drugs the hospital administered that you could have taken from home. You can request reclassification to inpatient (Condition Code 44) if clinically appropriate. The State Health Insurance Assistance Program (SHIP, free) helps with this.

**I'm on an ACA marketplace plan and they denied my claim.**

Distinct framework from ERISA. See [`rules/23_aca_marketplace.md`](rules/23_aca_marketplace.md). Internal appeal under 45 CFR § 147.136 (180 days), then external review by an Independent Review Organization with binding decision. Parallel state DOI complaint adds pressure. Success rate at external review is meaningful.

**I think I was discriminated against in healthcare access.**

ACA Section 1557 (42 U.S.C. § 18116) applies. See [`rules/21_section_1557.md`](rules/21_section_1557.md). Common patient-billing-relevant contexts: language access (LEP patients without qualified interpreters), disability accommodation (missing sign-language interpreters, inaccessible equipment), disparate-impact patterns. HHS OCR complaint within 180 days of the violation.

## Process and tooling questions (added since v0.7)

**How do I track deadlines without re-opening the LLM?**

Use [`scripts/deadline_watch.py`](scripts/deadline_watch.py) against your tracker CSV. It groups bills into overdue, due-soon, and upcoming. Exit code 1 if anything is overdue, so you can wire it into a weekly cron or Windows Task Scheduler.

**Can I just print one page that tells me where to start?**

Yes — [`docs/DECISION_TREE.md`](docs/DECISION_TREE.md) is intended as a printable single-page index from "what kind of bill" to "which template applies."

**What's the realistic outcome for my type of dispute?**

See [`docs/COMMON_OUTCOMES.md`](docs/COMMON_OUTCOMES.md). Public-source typical settlement rates, reduction percentages, and time-to-resolution by track.

**What mistakes do most patients make?**

See [`docs/ANTI_PATTERNS.md`](docs/ANTI_PATTERNS.md). 20+ common patient-side mistakes (paying the first bill, putting auto-debit on file, vague disputes, etc.) with the right move for each.

**How long do I need to keep all this paperwork?**

See [`docs/RECORDS_RETENTION.md`](docs/RECORDS_RETENTION.md). Conservative rule: 10 years from last activity on the account.

**How do I get started without reading everything?**

[`docs/START_HERE.md`](docs/START_HERE.md) is the three-minute setup with copy-paste opening prompts for the seven most common patient scenarios.

**What does CPT 99284 (or any other code) mean?**

See [`references/cpt_quick_reference.md`](references/cpt_quick_reference.md) for the most common codes; [`references/cpt_codes_em.md`](references/cpt_codes_em.md) for E/M documentation requirements. For codes not in those files, use the CMS Physician Fee Schedule Lookup.

**My hospital's price file looks weird. How do I read it?**

See [`references/hpt_mrf_format.md`](references/hpt_mrf_format.md) for the CMS machine-readable file format. Common compliance failures (missing cash price, opaque algorithms, login walls) are themselves CMS HPT-complaint hooks. To pull specific CPT prices from the file programmatically, [`scripts/fetch_mrf.py`](scripts/fetch_mrf.py) handles the four most common MRF schemas (CMS template JSON or CSV, Turquoise legacy CSV, TransparentRx JSON, Epic-native wide CSV).

## v0.13.0 pipeline questions

**What is the price-benchmarking step and how do I run it?**

[`scripts/fetch_price_benchmarks.py`](scripts/fetch_price_benchmarks.py) walks every `_bills.csv` in your `Billers/<slug>/` tree, extracts the CPT/HCPCS codes that appear next to dollar amounts in the OCR sidecar, joins each one against `references/medicare_pfs_common.csv` (~150 codes at CY2025 national rates), and writes `_benchmarks.csv` per folder with the billed-to-Medicare ratio plus FAIR Health and Bluebook URLs. If `_mrf_lookups/` has been populated by `fetch_mrf.py`, the hospital's published cash price and contracted-rate columns merge in automatically. The result is the evidence base the counter-offer drafter renders in `LETTER_COUNTER_OFFER.md`.

**What's the difference between the regular dispute letter and the counter-offer letter?**

The regular `letter_initial_dispute.md` argues the bill is wrong on specific findings: an NCCI unbundling violation, an EOB-vs-bill discrepancy, a service not documented in the record. The counter-offer letter `letter_negotiation_counter_offer.md` argues the price itself is not a good-faith open price term under UCC § 2-305(2). It includes a line-item table comparing your billed amounts to Medicare, the hospital's cash price, and the EOB allowed amount, and concretely offers to pay an anchor amount (default 200% of Medicare). Use the dispute letter when something is wrong about the bill; use the counter-offer when the bill is correctly itemized but priced 3-10x what the hospital actually accepts from any payer.

**How does the kit detect billing errors automatically?**

[`scripts/audit_billing_errors.py`](scripts/audit_billing_errors.py) scans each bill's OCR sidecar for the patterns Marshall Allen catalogues: duplicate CPTs on the same date of service, NCCI unbundling pairs (e.g., a comprehensive metabolic panel billed alongside a basic metabolic panel that's already included), modifier-25 stacking, late fees and finance charges (most states cap or prohibit these on medical debt), service-not-received language, and quantity inflation. The detected findings flow into `tracker.csv` `findings` column and into `_audit.csv` per folder. The dispute drafter then cites them by code rather than relying on the LLM to re-discover them.

**The audit flagged service_not_received_suspected on one of my bills. What happens?**

The drafter auto-generates `LETTER_RECORDS_REQUEST_HIPAA.md` for that bill in addition to whatever other letters apply. The HIPAA § 164.524 records request invokes the federal 30-day clock and the relevant state per-page fee cap. Once you receive the chart, compare it line-by-line against the itemized bill. Services billed without supporting documentation become the strongest possible dispute basis.

**What is encounter clustering and what does it do?**

[`scripts/check_completeness.py`](scripts/check_completeness.py) groups bills with overlapping date-of-service (±1 day) into the same encounter, assigning each cluster a stable id of the form `E-YYYY-NNN`. A typical hospital admission generates four to six separate bills (facility, ER physician, radiology, anesthesia, pathology, ambulance); the encounter id links them. When an encounter has 4+ distinct billers and at least one bill with an EOB on file, [`scripts/draft_letters_by_state.py`](scripts/draft_letters_by_state.py) drafts a single `LETTER_ENCOUNTER_COMBINED.md` that argues the NSA ancillary-provider theory across the whole encounter at once, with one CC list covering every provider.

**How do I keep an action log without spreadsheet fatigue?**

[`scripts/log_interaction.py`](scripts/log_interaction.py) is a one-line CLI that appends a row to `actions.csv` for every phone call, mailing, or received response. The script auto-increments action ids as `A-YYYY-NNN`, validates the action_type against the schema, and refuses to log against a bill id that isn't in the tracker. The dispute drafter pulls relevant actions into its prompt context when drafting later letters, so a logged call ("rep promised hold on collections through 2026-06-30") flows into the next dispute letter automatically.

**Should I make phone calls or stick to certified mail?**

The kit is mail-first because Marshall Allen's discipline is "every paper trail needs a paper trail". Verbal promises are deniable; certified mail is not. If you do make calls, [`references/phone_call_scripts.md`](references/phone_call_scripts.md) ships six scripts plus universal protocols (rep ID, call-reference number, three-step confirmation, same-day follow-up letter) and a state-by-state one-party/two-party consent list for legal recording.

**How do I back up my evidence offsite?**

[`scripts/bundle_evidence.py`](scripts/bundle_evidence.py) zips each dispute group's full artifact set (bill, EOB, all drafted letters, benchmark and audit rows, action log, manifest) into a single timestamped archive. [`scripts/bundle_to_cloud.py`](scripts/bundle_to_cloud.py) pushes them to any rclone-supported backend (Backblaze B2, Wasabi, S3, Google Drive, etc.) with `--immutable` so existing remote files are never overwritten. Pair with rclone's `crypt` backend for client-side encryption.

**How does the SOL tracker work?**

`scripts/deadline_watch.py --sol --state TN` (replace TN with your state) computes the written-contract statute of limitations for each open tracker row from the bill's statement_date plus the state's SOL years from [`references/sol_by_state.md`](references/sol_by_state.md). It surfaces accounts past SOL and accounts approaching SOL, and prints a reminder that confirming the debt or making a partial payment can restart the clock in most states.

**My bill is for a work-related injury. What does the kit do?**

The drafter detects work-related-injury keywords in the bill's OCR sidecar and auto-drafts `LETTER_WC_CARRIER_REDIRECT.md` redirecting the bill to the workers'-comp carrier under the state WC anti-balance-billing statute. The redirect runs alongside (not instead of) the regular dispute flow. The same pattern handles motor-vehicle injuries via `LETTER_AUTO_MED_PAY.md`.

**My bill is from a non-profit hospital. What additional leverage do I have?**

Three federal levers: § 501(r) FAP screening obligation (use `letter_hardship_negotiation.md` + `letter_financial_assistance_application.md`); § 501(r)(6) restrictions on extraordinary collection action; and IRS Form 13909 complaint when the hospital's conduct contradicts its Schedule H representations. The kit ships [`references/irs_990_review.md`](references/irs_990_review.md) walking through which Schedule H fields to pull from the hospital's most recent 990 and how to use them, plus [`templates/complaint_irs_form_13909.md`](templates/complaint_irs_form_13909.md) for the federal complaint.

**When should I engage an attorney?**

When the dispute hits any of: a hospital lien interfering with a tort settlement; amount in controversy approaching or exceeding the state's small-claims jurisdictional limit; an ERISA fiduciary-breach claim; an FCRA private right of action; or any case where the kit's free flow has produced diminishing returns. [`templates/attorney_intake_packet.md`](templates/attorney_intake_packet.md) generates a two-page case summary (page 1 facts and ask, page 2 artifact index) you can hand to an attorney for an intake consult.

**Self-pay election under NSA — when is it worth doing instead of letting insurance bill?**

[`scripts/analyze_self_pay_election.py`](scripts/analyze_self_pay_election.py) compares the two paths per bill: the insurance path (deductible + coinsurance up to OOP max, using your parsed SPD profile if available) vs the self-pay path (lowest of 200% Medicare, hospital's cash price from the MRF, or 60% AGB if FAP-eligible). For patients with high deductibles and access to charity care, self-pay frequently costs less. Allen's argument concretized.

## Contributing

**I'd like to add my state's pack. How?**

Use `references/laws_state_template.md` as the checklist and follow the structure of `laws_state_tn.md` through `laws_state_fl.md` as templates. Source every citation with a URL. Include the verification date in the file header. PR to [github.com/k3rt4s/medbill-dispute-kit](https://github.com/k3rt4s/medbill-dispute-kit). See [`CONTRIBUTING.md`](CONTRIBUTING.md).

**I found a bug in a rule or template.**

Open an issue at the GitHub repo with as much detail as you can — what the rule/template says, what the correct content should be, the source URL for the corrected information. PRs welcome.

**I have a real-world dispute outcome I'd like to share.**

Strip personally identifying information first. Then either open an issue describing the pattern (without names) or PR an example into `examples/`. Outcomes data helps future patients calibrate.
