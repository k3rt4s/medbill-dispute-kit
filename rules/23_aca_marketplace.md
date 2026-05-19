# Rule 23 — ACA marketplace plan appeals

ACA marketplace plans (purchased on healthcare.gov or a state-based exchange) are subject to a distinct federal appeals framework that differs from both ERISA self-funded plans and Medicare. Patients who try to apply ERISA tactics to a marketplace plan, or who fail to invoke the external-review right, often miss leverage points unique to the marketplace track.

This rule fires whenever the patient's denied claim is from an individual-market ACA-compliant plan (whether purchased on the federal exchange, a state exchange, or off-exchange but ACA-compliant).

## What's protected

Under the ACA's "internal and external review process" requirements (45 CFR § 147.136, paralleled at 29 CFR § 2590.715-2719 and 26 CFR § 54.9815-2719):

- **Standard internal appeal** within 180 days of denial; plan must decide within 30 days for pre-service claims, 60 days for post-service claims, 72 hours for urgent care.
- **External review** by an Independent Review Organization (IRO) after exhaustion of internal appeals. Decision is binding on the plan.
- **Expedited external review** for urgent situations, with parallel filing alongside the internal appeal.
- **Right to continue receiving services** during the appeal in certain circumstances.

## The four-step structure

1. **Internal appeal level 1** — first formal request to the insurer.
2. **Internal appeal level 2** — second-level review by a different reviewer (where the plan offers a second level; not all do).
3. **External review by IRO** — independent, binding. Typically free or low-cost ($25 filing fee in some states).
4. **Civil action** in state or federal court if all administrative remedies are exhausted and the dispute is not resolved.

Some state-based exchanges and state insurance laws layer additional protections; check the state pack.

## When this rule fires (vs other rules)

- **Marketplace plan denial** → this rule.
- **Employer-sponsored self-funded plan denial** → use `rules/07_appeal_insurance_denial.md` (ERISA track).
- **Employer-sponsored fully-insured plan denial** → use both rules; the marketplace-style external review applies but state insurance department complaints are also strong.
- **Medicare denial** → use `rules/12_medicare_appeals.md`.
- **Medicaid denial** → use the Medicaid two-step process; see template `letter_medicaid_appeal.md`.

## How to recognize a marketplace plan

The patient's insurance card and EOB usually identify the plan as "Marketplace," "Exchange," or "Individual." On healthcare.gov enrollments, the card may say "Marketplace Plan" or include the metal tier (Bronze/Silver/Gold/Platinum). State-based exchange plans (CoveredCA, NY State of Health, Pennie, etc.) have state-specific branding.

A plan with the same insurer name but obtained through an employer is **not** a marketplace plan — it's group coverage, often (but not always) ERISA-governed.

## The patient's playbook

### 1. Identify the denial reason precisely

The denial letter must include:

- The specific reason for the denial
- The specific plan provision relied on
- A description of the appeals process and timeframes
- A statement of the right to receive, free of charge, all documents and records relevant to the claim
- The diagnosis code, treatment code, and the standard used to deny (where applicable)

If any of these are missing, the denial itself may be procedurally invalid. 45 CFR § 147.136(b)(2)(ii) requires specific notice elements.

### 2. Request the case file

Within the appeal letter, demand under 45 CFR § 147.136(c)(2):

- The complete claim file
- The clinical guidelines or coverage policies relied on
- The credentials of the reviewer who denied
- Any independent medical opinions consulted

### 3. Internal appeal

File within 180 days. Use the standard appeal structure: state the relief requested, quote the plan provisions, attach the treating physician's medical-necessity letter, cite clinical practice guidelines, preserve all rights.

The template `templates/letter_insurance_appeal_erisa.md` adapts for marketplace plans by:

- Removing ERISA § 502(a) citations
- Adding 45 CFR § 147.136 citations
- Adding the right to expedited external review where applicable

### 4. External review by IRO

The single most valuable feature of the marketplace appeals framework. After the internal appeal is denied (or in parallel for urgent cases):

- Submit a request for external review to the plan (the plan forwards to an IRO).
- The IRO is independent of the insurer and reviews the case de novo.
- The decision is **binding on the plan**.
- Filing fee: free in most states or $25.
- Decision timeframe: 45 days standard, 72 hours expedited.

Success rate at external review is significantly higher than internal appeal alone — typically 40-60% of well-grounded cases prevail at the IRO level.

### 5. State insurance department complaint (parallel)

Marketplace plans are regulated by the state insurance department. A parallel state complaint creates pressure independent of the appeal process. Use `templates/complaint_state_doi.md`.

### 6. State-based exchange consumer assistance

States with state-based marketplaces (CA, NY, MA, CO, CT, RI, MD, WA, etc.) have consumer-assistance personnel who help with appeals. These are free and meaningfully effective. Find via the state exchange's website.

### 7. Civil action

After exhausting administrative remedies (internal appeal + external review), a patient can sue in state or federal court. Unlike ERISA self-funded plans where federal court is the forum and standard of review is deferential, marketplace plan litigation can be in state court with more patient-favorable procedures depending on state law.

## Special situations

### Pre-existing conditions

ACA marketplace plans cannot deny based on pre-existing conditions (42 U.S.C. § 300gg-3). A denial citing pre-existing conditions is facially invalid; the appeal is the kit's straightforward dispute.

### Essential Health Benefits

The ACA requires marketplace plans to cover ten categories of Essential Health Benefits (45 CFR § 156.110). A denial of a service that falls within an EHB category is suspect; the appeal can argue the denial conflicts with federal benefit requirements.

### Network adequacy

Marketplace plans must maintain adequate provider networks (45 CFR § 156.230). A denial citing out-of-network status when the patient could not access an in-network provider in reasonable time/distance is a network-adequacy complaint, parallel to the appeal.

### Continuation of care

Where the patient is mid-treatment and the insurer changes networks or terminates a provider, ACA continuation-of-care rules at 45 CFR § 156.230(d) may apply.

## Tracker tagging

- `findings`: `marketplace_plan_denial`, `marketplace_network_adequacy`, `marketplace_ehb_denial`
- `next_action`: `marketplace_internal_appeal`, `marketplace_external_review`, `state_doi_complaint`, `marketplace_civil_action`

## Free help

- **Healthcare.gov marketplace help line:** 1-800-318-2596
- **State-based exchange consumer assistance** for the patient's state
- **State health insurance assistance** — search the state's name plus "consumer assistance health insurance"
- **Federal CCIIO consumer assistance** — for system-wide patterns

## Related

- [[07_appeal_insurance_denial]] — ERISA self-funded plans (contrast)
- [[12_medicare_appeals]] — Medicare (contrast)
- `templates/letter_insurance_appeal_erisa.md` — adapt with 45 CFR § 147.136 citations for marketplace plans
- `templates/complaint_state_doi.md` — parallel state complaint
