# User Stories — medbill-dispute-kit

Per AGENTS.md §6 convention. Stories use Connextra form with Given/When/Then acceptance criteria. Status legend: `proposed` · `accepted` · `next` · `priority` · `shipped (vX.Y.Z)` · `withdrawn`.

## Personas

- **Patient under bills**: A US adult who has received one or more medical bills they suspect are wrong or unfair. May have insurance, may not. Not a lawyer.
- **Patient advocate**: A friend, adult child, or financial counselor helping someone else dispute bills.
- **Out-of-state contributor**: A developer who wants to add their state's law pack to the kit.

---

## Epic 1 — Onboard a new patient

### Story 1.1 — Drop the kit into any LLM and start

**As a** patient under bills, **I want to** load this kit into any major LLM and have it know what to do, **so that** I don't need to be an LLM expert to get help.

**AC:**

- Given the contents of `llm/`, `rules/`, `references/`, `schemas/`, `templates/`, and `tracker/` are uploaded to a fresh LLM session, When the patient types "I want to dispute medical bills", Then the LLM follows `llm/workflow.md` and asks for the first bill.
- Given the LLM has < 200k token context, When the patient follows the staged-load instructions in `llm/system_prompt.md`, Then the LLM can still complete the full workflow by loading rules and templates on demand.

**Status:** shipped (v0.1.0)

### Story 1.2 — Ingest a single bill image or PDF

**As a** patient under bills, **I want to** upload a photo or PDF of a bill and have the LLM extract the structured fields, **so that** I don't have to transcribe anything.

**AC:**

- Given a clear photo of a US medical bill, When uploaded with the kit loaded, Then the LLM produces a row matching `schemas/bill.toml` and asks the patient to confirm before saving.
- Given an unclear or partial image, When the LLM cannot read a required field, Then it asks the patient for that field specifically rather than guessing.

**Status:** shipped (v0.1.0)

---

## Epic 2 — Deduplicate noisy bill streams

### Story 2.1 — Recognize follow-up statements for an existing bill

**As a** patient under bills, **I want** the kit to recognize when a newly uploaded statement is just a reminder for a bill I already have, **so that** my tracker doesn't fill up with duplicates.

**AC:**

- Given a bill already exists in the tracker with account number X and balance Y, When a new statement is uploaded with the same account number and a balance within $5 of Y, Then the LLM treats it as a follow-up statement and updates the existing row's `last_statement_date` field rather than creating a new row.
- Given the deduplication rules in `schemas/deduplication_rules.toml`, When two records match on at least two of {account_number, provider_tax_id, date_of_service, patient_account_id} and balances overlap, Then they are treated as the same bill.

**Status:** shipped (v0.1.0)

### Story 2.2 — Recognize separately-billed providers for one hospital visit

**As a** patient who had one hospital stay but receives bills from the hospital plus the radiologist plus the ER physician group plus the anesthesiologist, **I want** the kit to group these as the same encounter, **so that** I can see the total cost of the stay and apply No Surprises Act analysis across all of them.

**AC:**

- Given multiple bills share a service date and a facility name, When they are extracted, Then they are linked under an `encounter_id` in the tracker and the LLM flags the encounter for No Surprises Act review if any of the providers might be out-of-network.

**Status:** shipped (v0.1.0)

---

## Epic 3 — Diagnose what's wrong with a bill

### Story 3.1 — Flag CPT severity coding mismatch

**As a** patient under bills, **I want** the LLM to compare the CPT level coded on my bill against the actual visit I had, **so that** an upcoded ER visit gets challenged.

**AC:**

- Given an itemized bill containing E/M code 99284 or 99285, When the patient's described visit is short (under 30 minutes) with simple decision-making, Then the LLM flags the line as "possible upcoding" and references `references/cpt_codes_em.md` for the documentation requirements.

**Status:** shipped (v0.1.0)

### Story 3.2 — Flag No Surprises Act violations

**As a** patient under bills, **I want** the LLM to flag when I'm being balance-billed in a scenario where federal law prohibits it, **so that** I can use the strongest possible challenge first.

**AC:**

- Given an emergency-services bill from an out-of-network provider, When extracted, Then the LLM cites the No Surprises Act, references `rules/04_no_surprises_act.md`, and offers `templates/letter_no_surprises_violation.md`.
- Given a non-emergency bill at an in-network facility from an out-of-network ancillary provider (anesthesia, radiology, pathology, lab, assistant surgeon, hospitalist, intensivist, neonatologist), When extracted, Then the same flag and template are offered.

**Status:** shipped (v0.1.0)

### Story 3.3 — Flag price gouging using transparency data

**As a** patient under bills, **I want** the LLM to call out line items priced far above fair-market for my area, **so that** I have a concrete number to argue down to.

**AC:**

- Given a line item with a CPT code, When extracted, Then the LLM points the patient to the relevant transparency tool (Turquoise Health, Healthcare Bluebook, FAIR Health Consumer, or the hospital's own price file) and explains how to look up a fair price.

**Status:** shipped (v0.1.0)

---

## Epic 4 — Take action on a bill

### Story 4.1 — Request an itemized bill

**As a** patient who received only a summary bill, **I want** the LLM to draft a certified-mail itemization request that cites the right state statute, **so that** the provider's 30-day clock starts running.

**AC:**

- Given the patient's state, When the LLM uses `templates/letter_itemization_request.md`, Then the rendered letter cites the correct state statute (TN Code § 68-11-220 for Tennessee; for other states, the LLM uses the lookup pattern in `references/laws_state_template.md`).

**Status:** shipped (v0.1.0)

### Story 4.2 — Draft an initial dispute letter

**As a** patient with a problematic bill, **I want** a polite-but-firm dispute letter that names each disputed line item with the legal basis, **so that** the provider has a clear paper trail of my objection.

**AC:**

- Given findings from Epic 3, When the LLM uses `templates/letter_initial_dispute.md`, Then the letter lists each disputed line with citation, proposes a corrected total, and requests written response within 15 business days.

**Status:** shipped (v0.1.0)

### Story 4.3 — Escalate with a 30-day warning before small claims

**As a** patient whose initial dispute was ignored, **I want** to escalate with a formal warning of small claims court action, **so that** the provider's legal cost to defend exceeds the disputed amount.

**AC:**

- Given the initial dispute has gone unanswered for 30+ days, When the LLM uses `templates/letter_30day_warning.md`, Then the letter includes the disputed amount, the patient's prior good-faith efforts, the cost-to-defend argument, and CC lines to the state insurance department, attorney general, and BBB.

**Status:** shipped (v0.1.0)

### Story 4.4 — Draft an ERISA appeal for an insurance denial

**As a** patient whose ERISA-governed plan denied a claim, **I want** an appeal letter that argues from plan terms and federal evidence standards rather than emotion, **so that** I preserve my right to sue under ERISA § 502(a) if denied again.

**AC:**

- Given a denial letter from an ERISA-covered plan, When the LLM uses `templates/letter_insurance_appeal_erisa.md`, Then the appeal cites the plan's Summary Plan Description, attaches medical-necessity evidence, references ERISA § 502(a), and preserves all rights to civil action.

**Status:** shipped (v0.1.0)

### Story 4.5 — File a state insurance department complaint

**As a** patient ignored by a provider or insurer, **I want** a ready-to-submit state complaint, **so that** I trigger a regulatory investigation and increase pressure.

**AC:**

- Given the patient's state, When the LLM uses `templates/complaint_state_doi.md`, Then the complaint includes the right agency name, contact info, and statutory hooks.

**Status:** shipped (v0.1.0)

### Story 4.6 — Negotiate a hardship reduction

**As a** patient whose bill is correctly coded but unaffordable, **I want** a negotiation letter that anchors to the Medicare rate and demands consideration under the hospital's Financial Assistance Policy, **so that** I am not pushed into a payment plan I can't sustain.

**AC:**

- Given a bill with no dispute findings but a balance the patient cannot afford in full, When the LLM uses `templates/letter_hardship_negotiation.md`, Then the letter cites IRS § 501(r) where applicable, names reference points (Medicare rate, hospital cash price, fair-market range) with sources, makes a specific dollar offer, and refuses auto-debit and interest charges.

**Status:** shipped (v0.2.0)

### Story 4.7 — Respond to a third-party medical-debt collector

**As a** patient receiving first written contact from a third-party debt collector on an alleged medical debt, **I want** to demand validation under FDCPA § 1692g within the 30-day window, **so that** collection activity is paused and the collector is forced to produce the underlying paper trail.

**AC:**

- Given a collector's first written communication received within the last 30 days, When the LLM uses `templates/letter_fdcpa_validation.md`, Then the letter demands the original-creditor name and address, the signed contract, an itemized statement, EOB, payments accounting, chain of assignment, state licensure, and date of last activity, and preserves FDCPA and FCRA rights.
- Given the bill is from the original creditor (hospital or doctor's office) rather than a third-party collector, When the patient asks for this template, Then the LLM declines and routes to `letter_initial_dispute.md` or `letter_hardship_negotiation.md` instead.

**Status:** shipped (v0.2.0)

---

## Epic 5 — Carry state across the months-long process

### Story 5.1 — Download an updated tracker after each session

**As a** patient running a multi-month dispute process, **I want** to download my updated tracker as a CSV at the end of every session, **so that** I can re-upload it next time without losing context.

**AC:**

- Given any session, When the patient says "save my progress" or the LLM detects the conversation is wrapping, Then the LLM outputs a complete CSV matching `schemas/tracker.toml` and tells the patient where to save it.

**Status:** shipped (v0.1.0)

### Story 5.2 — Resume next session by uploading the tracker

**As a** returning patient, **I want** to resume by uploading my tracker and any new statements, **so that** I don't re-tell my story.

**AC:**

- Given an uploaded `tracker.csv` matching `schemas/tracker.toml`, When the LLM ingests it at session start, Then the LLM summarizes open actions, overdue items, and any deadline within 7 days.

**Status:** shipped (v0.1.0)

---

## Epic 6 — Support states beyond Tennessee

### Story 6.1 — Use the state-law template to look up another state

**As a** patient in (e.g.) Texas, **I want** the kit to find the right Texas statutes without me knowing them, **so that** the kit isn't TN-only.

**AC:**

- Given a patient outside Tennessee, When the LLM hits a state-specific step, Then it follows `references/laws_state_template.md` to find the equivalent statute, agency, and small-claims process, and warns the patient that the citation should be verified before sending mail.

**Status:** shipped for six states (Tennessee v0.1.0, Georgia v0.2.0, California + Texas + New York + Florida v0.4.0). Long-tail state coverage remains open for contributor PRs.
**How to apply:** Track contributor PRs that fill in remaining states using `references/laws_state_template.md` as the checklist.

---

## Epic 7 — Cover federally-unprotected bill types

### Story 7.1 — Dispute a ground-ambulance balance bill

**As a** patient receiving a balance bill from an out-of-network ground ambulance provider, **I want** the kit to recognize that ground ambulance is excluded from the federal No Surprises Act, route my case based on whether my state has its own protection, and draft the correct dispute letter, **so that** I am not stuck paying a $3,000 surprise bill that the federal Act explicitly leaves unprotected.

**AC:**

- Given a ground-ambulance bill, When the patient's state is on the list in `rules/10_ground_ambulance.md` and the plan is not ERISA-self-funded, Then the LLM uses `templates/letter_ground_ambulance.md` Variant A citing the specific state statute.
- Given a ground-ambulance bill, When the patient's state has no protection or the plan is ERISA-self-funded, Then the LLM uses `templates/letter_ground_ambulance.md` Variant B arguing UCC § 2-305 with the Medicare ambulance fee schedule as the floor anchor.
- The LLM asks up-front whether the patient's plan is self-funded ERISA before choosing between variants.

**Status:** shipped (v0.3.0)

### Story 7.2 — File PPDR for a self-pay bill exceeding the Good Faith Estimate

**As a** patient who was uninsured or self-pay for a scheduled service, received (or should have received) a Good Faith Estimate, and is now staring at a final bill more than $400 above the estimate, **I want** the kit to walk me through filing federal Patient-Provider Dispute Resolution within the 120-day window, **so that** I get a binding determination from a neutral arbitrator and the collections-pause / credit-protection benefits that attach during PPDR.

**AC:**

- Given a self-pay patient with a final bill exceeding the GFE by $400+ within 120 days of receipt, When the LLM walks them through `rules/11_ppdr_walkthrough.md`, Then the patient has a complete checklist of evidence to upload to the federal IDR portal and an action logged in their tracker with the appropriate deadline.
- Given a patient who was entitled to but never received a GFE, When the LLM identifies this, Then it surfaces a parallel CMS complaint at 1-800-985-3059 and notes the failure-to-provide-GFE is itself an NSA violation independent of PPDR.

**Status:** shipped (v0.3.0)

### Story 7.3 — Apply for hospital financial assistance under IRS § 501(r)

**As a** patient with a bill from a non-profit hospital that I cannot afford in full, **I want** the kit to draft a Financial Assistance Policy application request that cites the applicable IRS regulations, triggers the hospital's procedural obligations during pendency, and refuses extraordinary collection action while the application is processed, **so that** I am screened for charity care before any collections clock runs.

**AC:**

- Given a non-profit hospital bill, When the patient uses `templates/letter_financial_assistance_application.md`, Then the letter requests the FAP, Plain Language Summary, application form, Billing & Collections Policy, and AGB calculation; states the patient's eligibility factors; and demands suspension of extraordinary collection action under 26 CFR § 1.501(r)-6.
- Given a non-responsive hospital after 30 days, When the LLM logs the timeout, Then it surfaces the escalation path (IRS Form 13909 plus state AG complaint).

**Status:** shipped (v0.3.0)

### Story 7.4 — Force a non-compliant hospital to publish a price-transparency MRF

**As a** patient whose hospital has not published a compliant machine-readable file of standard charges, **I want** a CMS complaint that produces regulatory pressure on the hospital, **so that** I gain access to the negotiated rates and cash prices the federal rule entitles me to see and which would anchor my underlying billing dispute.

**AC:**

- Given a hospital without a compliant MRF on its website, When the patient uses `templates/complaint_cms_hpt.md`, Then the complaint cites 45 CFR Part 180, identifies the specific deficiency (no MRF / incomplete MRF / no consumer display / access-barrier), and includes timestamped screenshots as evidence.

**Status:** shipped (v0.3.0)

---

## Epic 8 — Plan-type coverage (Medicare, Medicaid, dental)

### Story 8.1 — Appeal a Medicare claim denial

**As a** Medicare beneficiary whose claim was denied by the MAC, by a Medicare Advantage plan, or by a Part D plan, **I want** to file the appropriate appeal at the correct level with the correct deadlines, **so that** I exhaust the five-level Medicare appeal process correctly without losing the right to advance to ALJ or federal court.

**AC:**

- Given a denied Medicare claim, When the LLM walks the patient through `rules/12_medicare_appeals.md`, Then it identifies which Medicare part (A/B, C, D) and which level (1-5) applies, calculates the filing deadline from the date of the prior decision, and uses `templates/letter_medicare_appeal.md` to draft the Level 1 or Level 2 request with all required elements per 42 CFR § 405.946 / § 422.566 / § 423.580.
- Given an expedited-review-eligible situation, When the LLM detects clinical urgency, Then it renders the expedited-review section and shortens the response deadline accordingly.

**Status:** shipped (v0.4.0)

### Story 8.2 — Appeal a Medicaid managed-care denial

**As a** Medicaid enrollee whose service was denied by my MCO, **I want** to file the MCO internal appeal within 60 days and, if still denied, the state fair hearing within the state's deadline, **so that** I exhaust the federal-floor appeal process without losing the right to state-level review.

**AC:**

- Given a Medicaid MCO denial, When the LLM uses `templates/letter_medicaid_appeal.md`, Then it identifies the correct MCO appeal address, cites 42 CFR § 438.402 et seq., includes the Aid Paid Pending option where applicable, and routes to the state fair hearing as Step 2.
- Tennessee-specific path: Given a TennCare denial, When the patient asks for state fair hearing, Then the letter is addressed to TennCare Solutions and references Tennessee Justice Center as a free-help option.

**Status:** shipped (v0.4.0)

### Story 8.3 — Dispute a dental insurance downcoding or bundling

**As a** patient whose dental insurer downcoded a procedure or bundled separately-billable procedures, **I want** an appeal letter that cites the state's non-covered-services statute and the ADA's CDT code requirements, **so that** I (and my dentist) recover the correct payment.

**AC:**

- Given a dental EOB showing downcoding or bundling, When the LLM uses `templates/letter_dental_dispute.md`, Then the letter identifies the specific CDT code(s) at issue, cites the state non-covered-services statute (Tennessee § 56-2-305 as the worked example), and demands reprocessing with attached clinical documentation.
- Given a state that has not enacted a non-covered-services statute, When the LLM cannot cite a state-specific anti-downcoding law, Then it falls back to the plan terms and the implied covenant of good faith.

**Status:** shipped (v0.4.0)

---

## Epic 9 — Discoverability and contribution

### Story 9.1 — Find a glossary entry for any acronym the kit uses

**As a** patient unfamiliar with the alphabet soup of health-care billing, **I want** to look up any term used by the kit in one place, **so that** I don't lose context to terminology.

**AC:**

- Given any acronym used in a rule, template, or reference file, When the patient searches `references/glossary.md`, Then they find a plain-English definition.

**Status:** shipped (v0.4.0)

### Story 9.2 — Get answers to common questions without re-reading the rules

**As a** new patient picking up the kit, **I want** quick answers to recurring questions ("the bill is overdue, what now?", "do I need a lawyer?", "what if I missed a deadline?"), **so that** I don't have to read every rule file to get unstuck.

**AC:**

- `FAQ.md` covers ≥ 20 common scenarios with answers grounded in specific rules.
- Each FAQ answer cross-references the rule or template that handles the case.

**Status:** shipped (v0.4.0)

### Story 9.3 — Run the kit on a short-context LLM

**As a** patient using a small local model or a cloud LLM with limited context, **I want** a staged-load pattern that doesn't require all kit files in memory simultaneously, **so that** I can still complete the workflow.

**AC:**

- `llm/QUICKSTART_short_context.md` describes a 7-stage load pattern.
- Each stage names the specific files to load and what the LLM should do with them.

**Status:** shipped (v0.4.0)

### Story 9.4 — Contribute a new state pack as a PR

**As an** open-source contributor with knowledge of my state's medical-bill protections, **I want** clear contribution guidelines, **so that** my PR meets the kit's quality bar on the first try.

**AC:**

- `CONTRIBUTING.md` includes a checklist for new state packs covering all 12 required sections.
- Specifies the citation discipline (URL per claim, verified-on date).
- Lists the cross-references that must update in lockstep (BUILD_PLAN, CHANGELOG, README, QUICKSTART).

**Status:** shipped (v0.4.0)

### Story 9.5 — Validate a tracker CSV outside an LLM session

**As a** technical user, **I want** a script that confirms my tracker conforms to the schema, **so that** I can catch typos before re-uploading to the LLM.

**AC:**

- `scripts/validate_tracker.py` runs on Python 3.11+ standard library, no dependencies.
- Validates header order, date format, decimal format, boolean format, and all enum / controlled-vocabulary fields.
- Returns exit code 0 on valid, 1 on invalid with errors to stderr.

**Status:** shipped (v0.4.0)

### Story 9.6 — Pytest coverage for the validator

**As a** maintainer, **I want** unit tests for `scripts/validate_tracker.py`, **so that** schema changes are caught before they reach contributors.

**AC:**

- `tests/test_validate_tracker.py` covers the happy path, missing-required-column, bad-date, bad-decimal, bad-enum, bad-findings-token, and header-order-mismatch cases.
- Tests run with `python -m pytest tests/` and pass.
- GitHub Actions workflow at `.github/workflows/ci.yml` runs the validator and pytest on every push and PR to main.

**Status:** shipped (v0.5.0)

### Story 9.7 — Lower friction for first-time contributors

**As a** first-time contributor opening an issue or PR, **I want** structured templates that prompt me for the right information, **so that** my contribution doesn't bounce on missing context.

**AC:**

- `.github/ISSUE_TEMPLATE/` contains bug, state-pack-request, and content-correction templates, each requiring source URLs where applicable.
- `.github/PULL_REQUEST_TEMPLATE.md` has a checklist for state packs, templates, rules, schema changes, factual corrections, and other change types.
- `CODE_OF_CONDUCT.md` adapted from Contributor Covenant 2.1.
- `SECURITY.md` defines scope and vulnerability-reporting channel.

**Status:** shipped (v0.5.0)

### Story 9.8 — Worked examples beyond the simple case

**As a** new user with a complex multi-bill, multi-month situation, **I want** to see the kit handle a realistic scenario before I try it on my own bills, **so that** I can calibrate expectations.

**AC:**

- `examples/multi_encounter_walkthrough.md` shows two hospital encounters with 7 bills, three sessions over six weeks, deduplication of follow-up statements, and resolution with quantified savings.
- `examples/insurance_denial_walkthrough.md` shows an ERISA self-funded plan denial, internal appeal, external review by an IRO, and final coverage.

**Status:** shipped (v0.5.0)

---

## Epic 10 — Federal-protection coverage beyond billing

### Story 10.1 — Complain to CMS about an EMTALA violation

**As a** patient who was denied emergency screening, stabilization, or appropriate transfer by a Medicare-participating hospital, **I want** a complaint letter to CMS that fits the agency's investigation process and preserves my civil right of action, **so that** I both create regulatory pressure and protect my 2-year statute of limitations.

**AC:**

- Given an emergency-care denial, When the LLM walks the patient through `rules/13_emtala.md`, Then it categorizes the violation (failure to screen, failure to stabilize, inappropriate transfer, refusal over prior unpaid bill, active labor) and drafts the right CMS complaint.
- Given the complaint is filed, When the LLM logs the action, Then the 2-year SOL under 42 U.S.C. § 1395dd(d)(2)(C) is calendared and the patient is advised to consult plaintiff-side counsel for the civil action.

**Status:** shipped (v0.6.0)

### Story 10.2 — Force release of medical or billing records under HIPAA

**As a** patient whose provider has delayed access, charged excessive fees, refused electronic transmission, or denied records access entirely, **I want** an OCR complaint that cites the specific 45 CFR § 164.524 provision violated, **so that** I unblock the records I need to support my underlying billing dispute.

**AC:**

- Given a records-request situation, When the LLM walks the patient through `rules/14_hipaa_right_of_access.md`, Then it diagnoses which subsection of § 164.524 is in play (no response in 30 days, excessive fee, refused format, procedural barriers, partial response, outright denial).
- Given OCR complaint readiness, When the LLM uses `templates/complaint_hipaa_access.md`, Then the complaint identifies the specific subsection violated, attaches evidence, and is filed within the 180-day window.

**Status:** shipped (v0.6.0)

---

## Epic 11 — Accident-related and work-injury billing

### Story 11.1 — Force correct payer ordering on accident-related medical bills

**As a** patient injured in a motor-vehicle accident, **I want** the kit to identify all the potential payers (med-pay/PIP, UM/UIM, at-fault driver's BI, my health insurance) and force each provider to bill them in the correct order, **so that** I don't get hit with chargemaster-priced lien recoveries from my eventual settlement.

**AC:**

- Given an accident-related bill, When the LLM walks the patient through `rules/15_auto_med_pay.md`, Then it routes the case based on whether the state is no-fault or tort, identifies the relevant policy coverages, and (for non-trivial cases) recommends retaining a personal-injury attorney.
- Given a hospital is preserving the bill for a settlement lien, When the LLM uses `templates/letter_auto_med_pay.md` Variant B, Then the letter demands the provider bill health insurance under any state-specific insurance-first rule (e.g., O.C.G.A. § 44-14-471(c)).
- Given a hospital has perfected a lien, When the LLM uses Variant C, Then the patient receives a structured challenge citing perfection defects, the made-whole doctrine where applicable, and chargemaster-unconscionability arguments.

**Status:** shipped (v0.6.0)

### Story 11.2 — Reject improper balance bills for workers' compensation injuries

**As a** worker with an accepted workers' compensation claim, **I want** any medical bill that arrives at my address to be redirected to the workers' comp carrier or flagged as improper balance billing, **so that** I do not pay something I am statutorily exempt from owing.

**AC:**

- Given a bill stemming from a work-related injury, When the LLM walks the patient through `rules/16_workers_comp.md`, Then it confirms the WC claim status, identifies the correct carrier, and produces a redirect letter or escalation to the state workers' comp board as appropriate.
- Given the WC claim is contested or denied, When the LLM advises on parallel tracks, Then it surfaces both the state workers' comp appeal path and the health-insurance-with-subrogation interim option.

**Status:** shipped (v0.6.0)

---

## Epic 12 — Long-tail state coverage

### Story 12.1 — Twelve state packs cover ~50% of US population

**As a** US patient in one of the twelve largest states by population, **I want** the kit to ship a dedicated state pack with verified citations for my state, **so that** I do not need to ask the LLM to look up my state's statutes from a template.

**AC:**

- Dedicated state packs ship for Tennessee, Georgia, California, Texas, New York, Florida, Pennsylvania, Illinois, Ohio, North Carolina, Michigan, Washington.
- Every pack covers the 12 required sections of `references/laws_state_template.md` plus 1-5 state-specific advantages.
- Every pack is dated and verified against public sources.

**Status:** shipped (v0.6.0; long-tail 38 states remain open for community PRs)

---

## Epic 13 — Financial-distress and procedural tooling

### Story 13.1 — Decide when bankruptcy is the right tool for medical debt

**As a** patient whose medical debt exceeds any realistic repayment plan, **I want** the kit to identify when bankruptcy makes sense, when other tools should be tried first, and what to bring to a consultation, **so that** I do not file unnecessarily or fail to file when I should.

**AC:**

- Given a patient with significant medical debt, When the LLM walks them through `rules/17_bankruptcy_and_medical_debt.md`, Then it identifies (a) whether the bill is dispute-eligible (if so, dispute first), (b) whether the patient qualifies for charity care (if so, apply first), (c) the means-test eligibility for Chapter 7, (d) the credit-report impact, (e) the right next step (free legal aid, Upsolve for simple Chapter 7s, a bankruptcy attorney).

**Status:** shipped (v0.7.0)

### Story 13.2 — Watch dispute deadlines outside an LLM session

**As a** patient running a months-long dispute process, **I want** to check my tracker for overdue or upcoming deadlines without re-opening the LLM, **so that** I don't lose a 30-day response window because I forgot to check in.

**AC:**

- `scripts/deadline_watch.py` reads a tracker CSV and groups bills into overdue, due-soon (within a configurable window), and upcoming. Returns exit code 1 if any bill is overdue. Skips settled and closed rows.

**Status:** shipped (v0.7.0)

### Story 13.3 — File in small claims court

**As a** patient whose dispute has gone unanswered through the kit's escalation ladder, **I want** to see what filing in small claims actually looks like before I do it, **so that** I know whether to proceed and how to prepare.

**AC:**

- `examples/small_claims_walkthrough.md` covers the full small-claims filing process for a Tennessee General Sessions case: filing decision, statement of claim drafting, exhibits checklist, hearing preparation script, common defendant arguments and rebuttals, post-judgment collection.

**Status:** shipped (v0.7.0)

### Story 13.4 — Get started in ten minutes

**As a** new user landing on the repo, **I want** copy-paste opening prompts for common scenarios, **so that** I can start disputing tonight without reading every rule file.

**AC:**

- `docs/START_HERE.md` provides a three-minute setup guide, an opening prompt template, and copy-paste prompts for seven common patient scenarios (stack of bills, overpriced bill, denied claim, debt collector calling, hospital charity care, old overdue bill, financial hardship).

**Status:** shipped (v0.7.0)

---

## Epic 14 — Federal-program coverage and modality patterns

### Story 14.1 — Handle a TRICARE balance-billing or denial issue

**As a** TRICARE beneficiary receiving a balance bill or claim denial, **I want** the kit to recognize TRICARE's federal protections (15% balance-billing cap, active-duty zero-cost-share, regional contractor and BCAC referral) and route accordingly, **so that** I don't apply commercial-plan tactics to a federal program with different rules.

**AC:**

- Given a TRICARE bill or denial, When the LLM walks the patient through `rules/18_tricare.md`, Then it confirms the patient's eligibility status (active duty / retiree / dependent), regional contractor (East: Humana Military; West: TriWest), and identifies whether the bill violates the 15% cap under 10 U.S.C. § 1079(h). Active-duty members are routed to immediate contractor intervention.

**Status:** shipped (v0.8.0)

### Story 14.2 — Handle a VA Community Care direct-billing problem

**As a** veteran receiving care from a non-VA provider under the MISSION Act, **I want** the kit to recognize when the provider is improperly billing me directly instead of the VA TPA, **so that** I forward the bill to the right place and do not pay something that VA owes.

**AC:**

- Given a Community Care bill, When the LLM walks the patient through `rules/19_va_community_care.md`, Then it confirms the authorization is in place, identifies the right TPA (Optum or TriWest), and routes the bill to the TPA rather than treating it as the veteran's responsibility.
- Given a service-connected condition, When billed any amount, Then the LLM flags as likely error and routes to VA Patient Advocate or VSO.

**Status:** shipped (v0.8.0)

### Story 14.3 — Catch telehealth coding and parity issues

**As a** patient billed for a telehealth visit, **I want** the kit to check that the place-of-service code matches the actual modality (home vs office), that modifier 95 or 93 is applied appropriately, that an in-person facility fee was not improperly attached, and that state telehealth-parity rules are followed, **so that** I do not pay for coding errors.

**AC:**

- Given a telehealth bill, When the LLM walks the patient through `rules/20_telehealth.md`, Then it verifies POS code (02 or 10 vs 11/22), modifier coding (95/93), facility-fee appropriateness, audio-only vs video coding (99441-99443 vs 99213/14 + modifier), and state telehealth-parity applicability.

**Status:** shipped (v0.8.0)

### Story 14.4 — Use the decision tree as a quick reference

**As a** patient with a specific bill in hand, **I want** a single-page decision tree that points me directly at the right template, **so that** I do not have to read every rule file to figure out where to start.

**AC:**

- `docs/DECISION_TREE.md` covers the 14+ most common patient scenarios with explicit template recommendations and cross-references to the relevant rules.

**Status:** shipped (v0.8.0)

---

## Epic 15 — Civil-rights and modality coverage

### Story 15.1 — Use Section 1557 against discrimination-tinged billing

**As a** patient who experienced inadequate language access, disability accommodation, or other discrimination-tinged conduct that affected billing, **I want** the kit to surface ACA Section 1557 protections and route to HHS OCR, **so that** I have a federal civil-rights lever in addition to ordinary billing disputes.

**AC:**

- Given a patient describing an access failure (LEP, disability, etc.), When the LLM uses `rules/21_section_1557.md`, Then it categorizes the violation, drafts a parallel Section 1557 dispute, and routes to OCR within the 180-day complaint window.

**Status:** shipped (v0.9.0)

### Story 15.2 — Handle an air-ambulance balance bill correctly

**As a** patient billed for an air-ambulance transport, **I want** the kit to apply federal NSA protections (which cover air ambulance, unlike ground ambulance) and address the practical pricing issues, **so that** I do not pay illegal balance bills and can negotiate the legal in-network cost-share down where applicable.

**AC:**

- Given an air-ambulance bill, When the LLM walks the patient through `rules/22_air_ambulance.md`, Then it confirms NSA applicability, identifies balance-billing violations, flags ADA preemption of state remedies, and routes to NSA reprocessing or hardship negotiation depending on whether the disputed amount is balance-billed or in-network cost-share.

**Status:** shipped (v0.9.0)

### Story 15.3 — Calibrate expectations from common outcomes

**As a** patient deciding whether to pursue a dispute, **I want** rough patterns of typical settlement amounts, time-to-resolution, and success rates by track, **so that** I can decide whether a fight is worth picking.

**AC:**

- `docs/COMMON_OUTCOMES.md` provides public-source patterns for each major dispute track (itemization, initial dispute, NSA, insurance appeal, § 501(r), FDCPA, small claims, hardship, bankruptcy).
- Time-to-resolution figures are provided for the most common patient questions.

**Status:** shipped (v0.9.0)

### Story 15.4 — Avoid common patient-side mistakes

**As a** patient starting a dispute, **I want** to read once about the most common patient-side mistakes, **so that** I do not undermine my own case before I begin.

**AC:**

- `docs/ANTI_PATTERNS.md` covers 20+ common patient-side mistakes (paying the first bill, auto-debit on file, vague disputes, threatening too much/too little, confusing EOB with bill, etc.) with the right move for each.

**Status:** shipped (v0.9.0)

---

## Epic 16 — Plan-type and modality completeness

### Story 16.1 — Appeal a marketplace plan denial correctly

**As a** patient on an ACA marketplace plan whose claim was denied, **I want** the kit to recognize that the appeals framework differs from ERISA and Medicare and route to the right combination of internal appeal, external review by IRO, and state insurance department complaint, **so that** I do not miss the binding-IRO-decision lever unique to ACA-compliant plans.

**AC:**

- Given a denial from a marketplace plan, When the LLM walks the patient through `rules/23_aca_marketplace.md`, Then it routes to internal appeal under 45 CFR § 147.136, followed by IRO external review with binding decision, plus parallel state DOI complaint.

**Status:** shipped (v0.10.0)

### Story 16.2 — Dispute observation status for Medicare patients

**As a** Medicare beneficiary surprised by observation-status billing (Part B cost-sharing instead of Part A, or denied SNF coverage because no qualifying three-day inpatient stay), **I want** the kit to surface reclassification and appeal paths, **so that** I get the correct financial treatment for a hospitalization that clinically looked like an inpatient stay.

**AC:**

- Given a Medicare patient with observation-status billing concerns, When the LLM walks them through `rules/24_observation_status.md`, Then it covers the two-midnight rule, the MOON notice requirement, Condition Code 44 reclassification process, SNF three-day rule, self-administered-drug refund pathway, and the SHIP / Center for Medicare Advocacy resources.

**Status:** shipped (v0.10.0)

### Story 16.3 — Retain documents correctly across a months-long dispute

**As a** patient running a months-long dispute, **I want** clear guidance on what paperwork to keep, where, for how long, and how to organize it, **so that** I don't lose key evidence and don't drown in unnecessary paper.

**AC:**

- `docs/RECORDS_RETENTION.md` covers what to keep (provider, insurer, regulator, contemporaneous notes, pricing evidence), what to throw away, retention periods by statute-of-limitations type, naming conventions for digital storage, and special cases (bankruptcy, settlement confirmation, deceased patients).

**Status:** shipped (v0.10.0)

---

## Epic 17 — Patient-pricing reference and additional state coverage

### Story 17.1 — Look up common CPT/HCPCS codes without paying for AMA access

**As a** patient reading an itemized bill, **I want** a quick reference for the most common procedure codes that appear on medical bills, **so that** I can orient myself without needing a paid AMA subscription.

**AC:**

- `references/cpt_quick_reference.md` covers the highest-frequency CPT and HCPCS codes for imaging, lab, common procedures, surgical, ambulance, DME, and J-codes. Includes the common modifiers and place-of-service codes that affect billing. Honors AMA copyright by paraphrasing rather than redistributing full descriptors.

**Status:** shipped (v0.11.0)

### Story 17.2 — Read a hospital's machine-readable file

**As a** patient with a hospital bill, **I want** to find and read the hospital's machine-readable file of standard charges, **so that** I can argue from the hospital's own published prices rather than third-party estimates.

**AC:**

- `references/hpt_mrf_format.md` describes the CMS template format, the discoverable-URL pattern, what to look for in the file, common compliance failures, and how to cite the MRF in a dispute letter.

**Status:** shipped (v0.11.0)

### Story 17.3 — Cover the next four most-populous states

**As a** patient in Utah, Iowa, Nevada, or Arkansas, **I want** a dedicated state pack rather than the LLM looking up my state's statutes from the template, **so that** my dispute letters cite the right authorities with confidence.

**AC:**

- Dedicated state packs ship for UT, IA, NV, AR matching the 12-section format of existing packs. Total: 32 state packs covering ~82% of US population.

**Status:** shipped (v0.11.0)

---

## Epic 18 — Kit navigability and additional state coverage

### Story 18.1 — Navigate the kit when it's grown to 100+ files

**As a** patient or contributor opening the repo for the first time at 100+ files, **I want** a single-page cross-reference index that maps every file by scenario, type, federal law, and state, **so that** I can find what I need without skimming everything.

**AC:**

- `docs/INDEX.md` provides scenario-, type-, law-, and state-based navigation.
- Every rule, template, reference, schema, example, and governance file is listed at least once.

**Status:** shipped (v0.12.0)

### Story 18.2 — Get FAQ answers covering all kit features

**As a** user with questions about features added across v0.6-v0.11, **I want** the FAQ to cover them rather than reading every rule file, **so that** I can answer common scenarios quickly.

**AC:**

- FAQ.md adds 18+ entries covering EMTALA, HIPAA right of access, auto med-pay, workers' comp, bankruptcy, TRICARE, VA Community Care, telehealth, ground ambulance, air ambulance, observation status, ACA marketplace, Section 1557, plus process-and-tooling questions for the deadline watcher, decision tree, common outcomes, anti-patterns, records retention, START_HERE, CPT quick-reference, and HPT MRF format.

**Status:** shipped (v0.12.0)

### Story 18.3 — Cover the next four states by population

**As a** patient in Kansas, Mississippi, New Mexico, or Nebraska, **I want** a dedicated state pack rather than the LLM looking up my state's statutes from the template.

**AC:**

- Dedicated state packs ship for KS, MS, NM, NE matching the existing 12-section format. Total: 36 state packs covering ~84% of US population.

**Status:** shipped (v0.12.0)

---

## Cross-references

- Roadmap: this project does not yet have a `roadmap.json`. Roadmap is captured by story status above.
- Changelog: see commit history; once releases start, a `CHANGELOG.md` will mirror version blocks.
- Engineering plan: each rule/template is referenced from its story above by relative path.
