# Rule 20 — Telehealth billing

Telehealth went from niche to mainstream during COVID-19 and has remained mainstream. The billing practices have not entirely caught up. Telehealth visits routinely produce three patient-side billing problems: site-of-service confusion (the provider bills as in-person), modifier-and-place-of-service errors (denials over technical coding), and parity-rule violations (some states require insurers to pay the same rate for telehealth as in-person, but enforcement is uneven).

This rule fires whenever a patient receives a bill for a telehealth visit.

## What's at stake

A telehealth visit can be one of several billing patterns:

1. **Telehealth as primary modality** — patient is at home, provider is at a clinic or remote. Place-of-service code 02 (telehealth provided other than in home) or 10 (in home).
2. **Facility-based telehealth** — patient is at one healthcare facility, provider is at another (telestroke, teleICU). Different billing pattern.
3. **Telephone-only (audio-only)** — different CPT codes (99441-99443 for new patients, generally lower-paying than video).
4. **Asynchronous / store-and-forward** — provider reviews data submitted by patient (e-visit codes 99421-99423).

Each has different coverage and reimbursement rules under Medicare, Medicaid, and commercial plans.

## The patient's playbook

### 1. Verify place-of-service coding

Pull the itemized bill or EOB. Confirm the place-of-service code matches the actual encounter:

- **02** — telehealth provided other than in home
- **10** — telehealth provided in home (post-2022 distinction)
- **11** — office (should NOT appear on a telehealth bill)
- **22** — outpatient hospital (should NOT appear on a telehealth bill)

If the bill shows POS 11 or 22 for what was a home telehealth visit, the bill is mis-coded. The hospital's "facility fee" attached to POS 22 is particularly inflated.

### 2. Verify modifier coding

Telehealth services typically require modifier 95 (synchronous interactive audio-visual telecommunications) or modifier 93 (audio-only). Missing modifiers can cause denials at the insurance side, leaving the patient holding an unadjudicated bill.

### 3. Check telehealth parity

Many states have telehealth parity statutes requiring commercial insurers to cover telehealth at the same rate as in-person care for the same service. State law varies widely:

- **California**: Cal. Health & Safety Code § 1374.13 — strong parity for HMOs and PPOs.
- **New York**: NY Ins. Law § 3217-h — parity required.
- **Tennessee**: Tenn. Code § 56-7-1002 — parity for medically necessary telehealth.
- **Texas**: Tex. Ins. Code § 1455.004 — parity required.
- **Massachusetts**: M.G.L. c. 175 § 47BB — parity for behavioral health telehealth, broader for some services.

For other states, the kit looks up via the state pack or via the [Center for Connected Health Policy](https://www.cchpca.org/) state law tracker.

### 4. Check Medicare telehealth coverage post-COVID

Medicare's telehealth coverage rules have been in flux post-COVID public health emergency:

- Most telehealth flexibilities adopted during the PHE were extended through legislation through 2024 and 2025.
- The end of the PHE flexibilities and the move to permanent rules is ongoing; check current CMS guidance.
- Specifically: post-PHE rules tighten the originating-site requirement for some services (the patient must be at a defined medical facility for some Medicare telehealth services to be covered).

### 5. Common billing errors

- **In-person CPT code billed for a telehealth visit.** Provider billed CPT 99214 (in-person established office visit) when the encounter was telehealth and should have been 99214 + modifier 95 or appropriate POS code.
- **Facility fee on a non-facility telehealth.** Hospital systems sometimes attach an outpatient facility fee to a telehealth visit that did not involve hospital facilities. Dispute as a service-not-rendered.
- **Audio-only billed as video.** Provider documented an audio-only visit (99441-99443) but billed a higher-paying video code (99213/99214 with modifier 95). Patient's clinical record will document the modality.
- **Telehealth visit denied for "out-of-network telehealth" where the patient was at home in the state of the provider's license.** Many state telehealth-parity statutes require coverage regardless of network status for in-state telehealth. Verify.

### 6. State-licensed-provider issue

Telehealth across state lines has licensure implications. A provider must be licensed in the state where the patient is physically located at the time of the visit, with limited exceptions for compact states and emergency situations. If the patient was treated by a provider not licensed in the patient's state and the insurer denies on this basis, that may be a legitimate denial (the patient should have asked about licensure beforehand). For ongoing care, this is generally the provider's problem.

## When this rule fires together with others

- **Insurance denial of a telehealth claim** → also fire `rules/07_appeal_insurance_denial.md`.
- **No Surprises Act violation involving an out-of-network telehealth provider at an in-network facility** → fire `rules/04_no_surprises_act.md`. NSA does cover telehealth ancillary services.
- **CPT upcoding (audio-only billed as video)** → fire `rules/03_check_cpt_codes.md`.

## Tracker tagging

- `findings`: `telehealth_wrong_pos`, `telehealth_missing_modifier`, `telehealth_facility_fee_improper`, `telehealth_parity_violation`
- `next_action`: `dispute_telehealth_coding` (route through `initial_dispute` action), `appeal_telehealth_denial` (route through insurance appeal)

## Resources

- **Center for Connected Health Policy** — [cchpca.org](https://www.cchpca.org/). The single best resource for state-by-state telehealth law tracking.
- **CMS telehealth page** — [cms.gov/medicare/coverage/telehealth](https://www.cms.gov/medicare/coverage/telehealth).
- **CTeL (Center for Telehealth and e-Health Law)** — telehealth law tracking.

## Related

- [[03_check_cpt_codes]] — for telehealth coding disputes
- [[07_appeal_insurance_denial]] — for denied telehealth claims
- `references/laws_state_*.md` — state-specific telehealth-parity statutes
