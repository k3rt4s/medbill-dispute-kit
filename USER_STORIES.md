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

**Status:** in progress (Tennessee shipped v0.1.0, Georgia shipped v0.2.0; v0.3.0+ adds CA, TX, NY, FL via contributor PRs)
**How to apply:** Track contributor PRs that fill in additional states.

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

## Cross-references

- Roadmap: this project does not yet have a `roadmap.json`. Roadmap is captured by story status above.
- Changelog: see commit history; once releases start, a `CHANGELOG.md` will mirror version blocks.
- Engineering plan: each rule/template is referenced from its story above by relative path.
