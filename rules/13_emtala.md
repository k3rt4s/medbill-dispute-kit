# Rule 13 — EMTALA (Emergency Medical Treatment and Active Labor Act)

EMTALA is the federal statute that prevents hospitals participating in Medicare from "dumping" patients with emergency conditions or active labor. It is not primarily a billing statute, but it bears on billing in three ways: (a) hospitals cannot delay or refuse stabilizing emergency care over inability to pay or insurance verification; (b) patients harmed by EMTALA violations have a private civil action against the hospital; (c) the existence of EMTALA strengthens the patient's negotiation posture when a hospital threatens to deny future emergency care over an unpaid bill.

## The statute

- **Citation:** 42 U.S.C. § 1395dd
- **Implementing regulations:** 42 CFR § 489.20, § 489.24
- **Patient-facing CMS resource:** [cms.gov/medicare/regulations-guidance/legislation/emergency-medical-treatment-labor-act](https://www.cms.gov/medicare/regulations-guidance/legislation/emergency-medical-treatment-labor-act)
- **Effective:** 1986; amendments since

## What EMTALA requires of a Medicare-participating hospital with a dedicated emergency department

1. **Medical screening examination (MSE)** for any individual who "comes to the emergency department" requesting examination or treatment, regardless of ability to pay, insurance status, or immigration status.
2. **Stabilizing treatment** if an emergency medical condition is identified, before any transfer or discharge.
3. **Appropriate transfer** if the hospital cannot stabilize and the benefits of transfer outweigh risks. The receiving hospital must accept if it has specialized capabilities.
4. **No delay** in MSE or stabilizing treatment to inquire about payment method or insurance status.

## EMTALA violations relevant to billing disputes

The kit fires this rule when:

- **A patient was denied emergency screening or stabilizing treatment, ostensibly for inability to pay or insurance reasons.** This is a direct EMTALA violation regardless of any subsequent bill.
- **A patient was discharged from the ED in an unstable condition** with apparent connection to insurance or payment concerns.
- **A hospital has threatened to deny future emergency care over an unpaid prior bill.** Hospitals cannot deny emergency care; making this threat is itself problematic and the threat is empty as a matter of law.
- **A patient was inappropriately transferred** (or asked to transfer) while unstable, with apparent connection to payment.

## Patient remedies

### Civil action under § 1395dd(d)(2)(A)

A patient who suffers "personal harm as a direct result" of a hospital's EMTALA violation may sue the hospital in federal or state court for damages. The statute imports state-law damages and limitations rules for the medical malpractice claim's substantive components, but the federal cause of action provides the basis.

- **Statute of limitations:** **2 years from the date of the violation** — 42 U.S.C. § 1395dd(d)(2)(C)
- **Damages:** state-law damages standard
- **Forum:** federal or state court
- **Counsel strongly recommended** — EMTALA litigation is technical and the damages analysis depends on state malpractice doctrine

### CMS regulatory complaint

Patients may also complain to CMS directly:

- **CMS Regional Office:** find your state's regional office at [cms.gov/medicare/regulations-guidance/legislation/emergency-medical-treatment-labor-act/contacts](https://www.cms.gov/medicare/regulations-guidance/legislation/emergency-medical-treatment-labor-act/contacts)
- **State survey agency** investigates on CMS's behalf
- **Penalties:** hospitals face CMP up to ~$133,000 per violation (for hospitals with 100+ beds; ~$66,000 for smaller). Physicians face CMP up to ~$133,000 per violation plus possible Medicare exclusion. Penalty amounts are inflation-adjusted; check current schedule.

### State licensure complaint

Most states have an analog through the state health department. Often parallel to CMS.

## When EMTALA is not the right route

- **A bill that overcharges for emergency care that was actually provided.** EMTALA doesn't cap pricing; the price-gouging dispute follows `letter_initial_dispute.md` and No Surprises Act analysis under `rules/04_no_surprises_act.md`.
- **A denial of non-emergency care.** EMTALA is emergency-care-specific. Non-emergency denial-of-care patterns route through state law (medical-records access laws, anti-discrimination statutes).
- **Insurance denial of an emergency claim.** That's an insurance appeal, not an EMTALA matter. Use `rules/07_appeal_insurance_denial.md`.

## How the existence of EMTALA strengthens billing-dispute negotiation

EMTALA's existence and the CMP exposure on the hospital change the dynamic when a billing department threatens consequences for unpaid bills:

- "We won't see you again" — for emergency care, this is empty. The patient is entitled to MSE and stabilization regardless.
- "We'll send you to collections" — that's a collection matter, not an emergency-access matter; EMTALA is not the lever here.
- "We'll deny prior authorization for future scheduled care" — possible but separate from EMTALA.

The kit's posture: do not let an EMTALA-protected emergency-care threat distort the billing dispute. If a billing department invokes future emergency-care access as leverage, log it and treat the bill on its merits.

## Tracker tagging

The LLM logs EMTALA cases with new schema findings:

- `findings`: `emtala_violation_screening`, `emtala_violation_stabilizing`, `emtala_violation_transfer`, `emtala_threat_future_care`
- `next_action`: `file_emtala_complaint` (CMS) and/or `consult_emtala_counsel` (for the civil action)

## Important limits

- **Counsel recommended** for the civil action under § 1395dd(d)(2)(A). The damages analysis depends on state malpractice doctrine and the 2-year statute of limitations is unforgiving.
- **EMTALA does not require the hospital to admit the patient or to provide non-emergency care.** Once stabilized, the hospital's EMTALA obligation generally ends.
- **EMTALA applies only to hospitals participating in Medicare.** Nearly all US hospitals participate, but verify.

## Related

- `templates/complaint_emtala.md` — for the CMS regulatory complaint
- [[04_no_surprises_act]] — the related federal protection for emergency-services billing
- [[07_appeal_insurance_denial]] — for insurance denials of emergency-service claims
