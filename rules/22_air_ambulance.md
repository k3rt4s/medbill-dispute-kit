# Rule 22 — Air ambulance billing

Air ambulance (helicopter EMS, fixed-wing critical-care transport) is covered by the federal No Surprises Act — unlike ground ambulance, which is the federal NSA's biggest gap. Despite federal protection, air ambulance bills routinely produce patient-side problems because the underlying charges are enormous, network status is often unclear, and the federal Airline Deregulation Act preempts most state air-ambulance billing regulation.

This rule fires whenever a patient receives a bill for an air-ambulance transport.

## What's protected by the federal NSA

The No Surprises Act prohibits balance billing for out-of-network air ambulance. Specifically:

- **42 U.S.C. § 300gg-112** (added by NSA) — bans balance billing for out-of-network air ambulance services.
- Patient cost-sharing is calculated as if the service were in-network and counts toward in-network deductible and out-of-pocket maximum.
- Provider-payer disputes over the actual payment amount go through the federal Independent Dispute Resolution (IDR) process; the patient is held harmless.

## What's not protected

- **Insurance plans not subject to the NSA**: a small number of insurance arrangements (some short-term limited-duration plans, certain self-funded plans before the NSA's effective date) may not be covered. The vast majority of plans are subject.
- **The actual price the patient might have to pay**: even with NSA balance-billing protection, the patient still owes their in-network cost-share, which for air ambulance can be substantial (deductible plus coinsurance on a $50,000-$100,000 transport).
- **The underlying charge itself**: NSA does not cap what air-ambulance providers can charge; it only limits what patients are responsible for.

## The Airline Deregulation Act preemption problem

Air-ambulance carriers are regulated as "air carriers" under federal aviation law, including the Airline Deregulation Act of 1978 (ADA, 49 U.S.C. § 41713(b)(1)). The ADA preempts state laws that "relate to a price, route, or service of an air carrier" — which courts have applied broadly to state attempts to regulate air-ambulance billing.

The practical consequence: state surprise-billing laws, state rate-setting, and state consumer-protection laws generally **cannot** be applied against air-ambulance charges in the same way they can against ordinary medical providers. The federal NSA is the principal floor.

A 2021 Eleventh Circuit decision (*Air Evac EMS, Inc. v. Cheatham*) and similar cases have reinforced this preemption. The Department of Transportation has begun examining air-ambulance pricing under its consumer-protection authority, but no comprehensive federal rate-setting has emerged.

## When this rule fires

- A patient receives an air-ambulance bill (helicopter EMS, fixed-wing inter-facility transport).
- The bill includes balance-billed amounts beyond in-network cost-sharing.
- A patient's insurance has paid an amount the air-ambulance carrier considers insufficient and the carrier is billing the patient for the difference.

## The patient's playbook

### 1. Verify the carrier billed insurance and the NSA applies

Pull the EOB. If the patient has health insurance subject to the NSA (most do), the carrier should have processed the air-ambulance claim at in-network cost-sharing levels. Any balance billed to the patient beyond that is illegal under the NSA.

### 2. For NSA violations

Send the air-ambulance carrier a letter citing 42 U.S.C. § 300gg-112 and 45 CFR § 149.130 (balance-billing prohibitions for air ambulance). Demand reprocessing at in-network cost-sharing.

CC parallel:

- **CMS No Surprises Help Desk**: 1-800-985-3059 or [cms.gov/medical-bill-rights/help/submit-a-complaint](https://www.cms.gov/medical-bill-rights/help/submit-a-complaint)
- The patient's health insurer (for in-network reprocessing)

### 3. For the underlying patient cost-share

Even after NSA reprocessing, the patient's in-network cost-share on a $50,000-$100,000 transport can be thousands of dollars. Hardship-negotiation and charity-care pathways apply:

- For a non-profit hospital-affiliated air carrier: IRS § 501(r) FAP may apply. Use `templates/letter_financial_assistance_application.md`.
- For for-profit air-ambulance companies: hardship negotiation via `templates/letter_hardship_negotiation.md`. Most carriers maintain unofficial financial-hardship programs.

### 4. Membership programs

Many air-ambulance carriers (Air Methods, AirMedCare Network, REACH Membership Plus, others) sell annual memberships for $40-$150 that waive patient out-of-pocket costs for transports by that carrier's network. For patients in rural areas where air ambulance is a real risk, these may be worth considering.

### 5. State complaints

State surprise-billing complaints are typically preempted by the ADA but state regulators may still:

- Forward complaints to federal CMS for federal-law enforcement
- Investigate non-billing aspects of the encounter (clinical-care quality, paramedic-license issues)
- Document patterns for federal-policy advocacy

File state complaints anyway; the regulatory pressure can move billing departments even where direct state-law remedy is preempted.

### 6. Federal patient-side advocacy

- **Patient Advocate Foundation**: [patientadvocate.org](https://www.patientadvocate.org) — has handled air-ambulance billing cases.
- **Center for Air Ambulance Patient Rights**: search current advocacy resources; the policy landscape changes frequently.

## When this is not the right frame

- **Ground ambulance** — see `rules/10_ground_ambulance.md`. Different federal-NSA posture (ground ambulance is **not** covered by the NSA; state law is the primary protection).
- **Patient cost-share is correct and in-network** — that's a hardship-negotiation matter, not an NSA violation.
- **Self-funded ERISA plan with pre-2022 effective date** — verify NSA applicability; vast majority are covered but edge cases exist.

## Tracker tagging

- `findings`: `air_ambulance_nsa_violation`, `air_ambulance_in_network_cost_share_hardship`
- `next_action`: `dispute_air_ambulance_nsa`, `negotiate_hardship`, `file_cms_nsa_complaint`

## Note on policy reform

Air-ambulance pricing reform is an active federal policy area. The NSA is the floor; state efforts have been preempted by the ADA. The Department of Transportation has begun rulemaking under its consumer-protection authority. Updates to this rule are likely as the policy landscape evolves.

## Related

- [[04_no_surprises_act]] — the federal Act that covers air ambulance
- [[10_ground_ambulance]] — the federal Act explicitly excludes ground ambulance
- `templates/letter_no_surprises_violation.md` — for the NSA balance-billing dispute
- `templates/letter_hardship_negotiation.md` — for the underlying in-network cost-share if unaffordable
