# Worked example — ERISA insurance denial

A patient whose ERISA-covered employer health plan denied a claim for a recommended procedure. Walks through the kit's insurance-appeal track: plan-type identification, evidence gathering, internal appeal letter, external review, and parallel state-DOI complaint.

Names and details are fictional.

---

## Background

Patient's employer is a large national company. Patient's health plan is administered by a third-party administrator (TPA) — the patient's ID card says "ExampleCorp Health Plan, administered by [Major National Insurer]." The plan is self-funded; the employer pays claims out of its own funds and contracts the insurer as a TPA. Patient's doctor recommended an advanced imaging study; the plan denied as "not medically necessary."

Patient is in Tennessee. The bill itself is $4,800.

---

## Session 1 — Identify plan type, gather evidence, draft appeal

### Turn 1 — Patient

> My insurance denied a procedure my doctor said I needed. I want to appeal. I'm in Tennessee.

### Turn 1 — LLM

> Insurance denials route through `rules/07_appeal_insurance_denial.md`, which is a different track from a billing dispute. Before we go further, I need to figure out what kind of plan you have, because that determines which appeal framework applies. Three questions:
>
> 1. Is this insurance through your employer, the ACA exchange, Medicare, Medicaid (TennCare), or something else?
> 2. If employer-based, do you know if it's self-funded or fully insured? Check your Summary Plan Description (SPD) or call HR. The SPD usually says.
> 3. Can you upload the denial letter?

### Turn 2 — Patient

> Employer, big national company. The ID card says ExampleCorp Health Plan administered by [Major National Insurer]. I'll ask HR about self-funded. Denial letter attached.

Uploads denial letter.

### Turn 2 — LLM

> The ID-card pattern you described — employer name as the plan, insurer name as the administrator — strongly suggests self-funded ERISA. Big national employers are almost always self-funded. Confirm with HR, but I'm going to draft the appeal assuming ERISA § 502(a) applies. If HR confirms fully-insured instead, we'll add Tennessee bad-faith statute § 56-7-105 to the citations.
>
> Reading the denial letter:
>
> - Service denied: [advanced imaging study, with specific CPT code]
> - Date of service requested: [date]
> - Denial reason: "not medically necessary based on the plan's clinical guidelines"
> - Internal appeal deadline: 180 days from the denial date (standard for ERISA)
> - The letter cites your right to appeal under "the plan's procedures" but doesn't mention ERISA § 502(a) explicitly — flag for the appeal letter since DOL claims regs require this disclosure.
>
> What I need from you next:
>
> 1. The plan's Summary Plan Description (SPD). HR can provide; you're entitled to it.
> 2. A written statement of medical necessity from your treating doctor. This is the single most valuable piece of evidence at every level of appeal.
> 3. Clinical practice guidelines from a specialty society supporting the procedure for your condition.
> 4. Any prior tests, history, or treatments you've tried that bear on medical necessity.

### Turn 3 — Patient

> HR confirmed self-funded ERISA. SPD attached. I'll get the medical-necessity letter from my doctor this week.

Uploads SPD.

### Turn 3 — LLM

> Confirmed ERISA. Reviewing SPD for the relevant coverage language. Key findings:
>
> - SPD Section [X] covers "medically necessary diagnostic imaging" with no carve-out for the type of study your doctor ordered.
> - SPD Section [Y] states that "medical necessity determinations are made by the plan in consultation with treating physicians" — useful, because the plan should respect your doctor's judgment.
> - SPD Section [Z] describes the appeal process: written internal appeal within 180 days, plan must decide within 30 days, then external review by an IRO available.
> - The denial reason in the letter cites "clinical guidelines" but doesn't identify which guidelines or how your case fails to meet them. Under DOL claims regs (29 CFR § 2560.503-1), you're entitled to request the specific criteria the plan applied. The appeal letter will demand this.
>
> Drafting the internal appeal using `templates/letter_insurance_appeal_erisa.md`. I'll flag [NEEDS USER INPUT] for the parts that depend on your doctor's letter once you get it.

### Turn 4 — LLM (renders draft)

Renders the appeal letter following the Laurie Todd / Marshall Allen structure:

- **Section I — Relief requested:** specifies the SPD provisions obligating coverage, requests reversal and direct provider payment.
- **Section II — Plan terms:** quotes specific SPD provisions.
- **Section III — Medical necessity:** placeholder for the doctor's letter; LLM lists what the doctor should address.
- **Section IV — Procedural requests:** demands the SPD, the clinical criteria, the qualifications of the denial reviewer.
- **Section VII — Preservation of rights:** explicit ERISA § 502(a)(1)(B) citation, external-review right, attorney's-fees right under § 502(g).

LLM lists the `[NEEDS USER INPUT]` items:

- Doctor's name, credentials, and written statement
- Specific exhibits (guideline citations, peer-reviewed studies)
- Date of denial letter and claim number
- Member ID and group number

### Turn 5 — Patient

> Got the doctor's letter. He says the study is medically necessary because [clinical reasons]. He cited two specialty-society guidelines and one peer-reviewed paper.

### Turn 5 — LLM

> Folding the doctor's statement into Section III and listing the exhibits in Section VII. The appeal letter is ready to mail.
>
> Two parallel actions to take the same day:
>
> 1. **DOL EBSA informal intervention.** ERISA self-funded plans are subject to DOL oversight. Call 1-866-444-3272, ask for a benefits advisor, give them the plan name, claim number, and denial details. They'll often contact the plan administrator directly on your behalf. Free, fast, and gets results that internal appeals sometimes don't.
> 2. **Tennessee Department of Commerce and Insurance complaint.** Even though your plan is ERISA-preempted from state insurance regulation, the TDCI complaint creates a paper trail and sometimes the plan administrator responds to state pressure even when not legally required to.
>
> Logging the appeal in the tracker.

### Turn 6 — LLM (Phase 5)

> Tracker saved. **Save as:** `tracker_denial_2026-05-18.csv`.
>
> **Session summary:** identified plan type (self-funded ERISA), assembled evidence, drafted internal appeal letter with ERISA § 502(a) preservation language. Parallel actions: DOL EBSA call, TDCI complaint.
>
> **Overdue:** none.
>
> **Due in next 7 days:** mail the appeal letter certified; the plan's internal-appeal deadline is 180 days from the denial, so you have time, but earlier is better.
>
> **Highest-priority next action:** mail the appeal letter, call EBSA, submit the TDCI complaint. Bring me responses next session.

---

## Session 2 (3 weeks later) — Internal appeal denied, prepare external review

### Turn 1 — Patient

> Back. They denied the internal appeal too.

Uploads the internal-appeal denial letter.

### Turn 1 — LLM

> Standard pattern; about half of internal appeals are denied. The good news: the denial letter is a roadmap. Let me read it.
>
> Reading. The internal-appeal denial says:
>
> - "Upon further review, the plan maintains that the procedure does not meet the plan's medical-necessity criteria."
> - Cites specific medical-necessity criteria this time (the prior denial was vague; this one names a clinical guideline).
> - Includes the notice of your right to external review by an Independent Review Organization, with a 4-month deadline.
> - Mentions your right to bring civil action under ERISA § 502(a) after exhausting administrative remedies.
>
> Three steps next:
>
> 1. **External review.** This is your strongest remaining tool short of federal court. An IRO is independent of your plan — they review the entire administrative record de novo. Decisions are binding on the plan. Filing the external review is the next move.
> 2. **The new clinical guideline citation.** The internal denial pointed to a specific guideline this time. We need to compare that guideline to your situation in detail. Read the guideline, identify where your facts match the covered indication. The IRO will decide on this.
> 3. **EBSA follow-up.** Call EBSA again with the internal-denial letter. They may escalate.

### Turn 2 — Patient

> EBSA already called once; they're "monitoring" but said the appeal had to play out. Let's do external review.

### Turn 2 — LLM

> Filing external review. The process:
>
> - Request is filed with your plan (not directly with the IRO); the plan forwards to the IRO within 5 business days.
> - The plan must include the entire administrative record.
> - You may submit additional evidence within 10 business days of the IRO's notice that it has received your request.
> - IRO decides within 45 days standard, 72 hours expedited.
> - The IRO's decision is binding on the plan.
> - Filing fee is usually $25 or free; check the plan's denial letter.
>
> Drafting the external review request. It's structurally similar to the internal appeal — same exhibits, same SPD analysis — but tightened up to address the specific criterion the plan now cites and to add any new clinical evidence.

### Turn 3 — Patient

> My doctor sent me a peer-reviewed paper showing the procedure has stronger evidence than the plan's guideline acknowledges.

### Turn 3 — LLM

> Excellent. Adding the peer-reviewed paper as Exhibit [X], with a paragraph in Section III pointing out that the plan's cited guideline is outdated relative to current evidence. This is a common pattern; the IRO is independent enough to weigh this kind of evidence honestly.
>
> External review letter rendered. Mail certified with the new exhibit attached.

### Turn 4 — Patient

> Done. Now what?

### Turn 4 — LLM (Phase 5)

> Save state. **Save as:** `tracker_denial_2026-06-08.csv`.
>
> **Session summary:** internal appeal denied; external review filed with the IRO; new peer-reviewed evidence added.
>
> **Overdue:** none.
>
> **Due in next 7 days:** wait for IRO decision (45 days standard). Make sure you receive a notice that the IRO has the case within 5 business days from when the plan forwarded it.
>
> **Highest-priority next action:** wait, then re-engage when the IRO decision arrives.

---

## Session 3 (6 weeks later) — IRO decision

### Turn 1 — Patient

> IRO ruled in my favor. The plan has to cover the procedure.

### Turn 1 — LLM

> Great outcome. Logging the win. Three things to confirm before closing the file:
>
> 1. The plan must reprocess the claim and pay the provider. Verify with the provider that the claim was paid; ask for a corrected statement.
> 2. The plan must also reimburse you for any out-of-pocket you paid pending the appeal (if any). Check the IRO decision for the precise terms.
> 3. If the procedure had already happened and the provider had been chasing you for the balance, contact the provider to confirm the balance is now zero.

### Turn 2 — Patient

> Confirmed paid, no balance.

### Turn 2 — LLM

> Closing the bill. `status = settled`, savings = $4,800 (full coverage of the originally denied procedure). Logging the IRO decision date and outcome in `notes`.
>
> Final session summary across the three sessions: 1 bill, 1 denial, 1 internal appeal, 1 external review, $4,800 covered.
>
> **Save as:** `tracker_denial_2026-07-20.csv`.
>
> If anything similar happens with this insurer in the future, the playbook is now known. Keep this tracker as a reference.

---

## What this example shows

- **Plan-type identification matters.** The very first step in any denial dispute is figuring out which appeal framework applies. ERISA self-funded, ERISA fully-insured, Medicare, Medicaid, TRICARE, individual-market ACA — each has its own rules. Going down the wrong track loses time.
- **The SPD is the contract.** ERISA appeals are won by reading the plan document carefully and arguing from its specific terms.
- **The doctor's letter is the single most valuable evidence.** A one-page treating-physician statement of medical necessity carries more weight than the patient's own narrative or general clinical literature.
- **Parallel actions matter.** EBSA, state DOI, and the formal appeal can all run in parallel. State DOI sometimes can't enforce against an ERISA plan but the complaint creates pressure.
- **External review is the leverage point.** Half of internal appeals lose; a much larger fraction of external reviews flip the denial because the IRO is independent.
- **Track the parallel-process timeline.** ERISA appeals have multiple clocks running at once (internal-appeal window, external-review window, statute of limitations for § 502(a) suit). The tracker captures them so they don't lapse.

## What this example does not show

- **A non-ERISA insurance denial.** Individual-market plans, Medicare, Medicaid all have different processes. See [`letter_medicare_appeal.md`](../templates/letter_medicare_appeal.md) and [`letter_medicaid_appeal.md`](../templates/letter_medicaid_appeal.md).
- **A § 502(a) federal-court filing.** External review is binding; usually no further appeal is needed. If the IRO had denied, the next step would be ERISA § 502(a)(1)(B) suit in federal court — that's an attorney-mediated process, not a self-help one.
- **A pre-service denial.** This example handled a denial after the service was rendered. Pre-service denials (where you're trying to get authorization before the procedure) have shorter timelines (15-30 days for non-urgent, 72 hours for urgent) and may follow expedited tracks.

See [`walkthrough.md`](walkthrough.md) for a basic three-bill walkthrough and [`multi_encounter_walkthrough.md`](multi_encounter_walkthrough.md) for a multi-session multi-bill scenario.
