# Rule 24 — Medicare observation status and the two-midnight rule

A Medicare patient admitted to a hospital may be placed in either "inpatient" status or "observation" (outpatient) status. The clinical care can look identical to the patient; the billing consequences are very different. Many Medicare patients discover only after discharge that they were "outpatient under observation" the entire time, which exposes them to substantial Medicare Part B cost-sharing instead of Part A coverage and disqualifies the encounter for the three-day hospital-stay requirement for Skilled Nursing Facility coverage.

This rule fires when a Medicare beneficiary was hospitalized and the bill or post-discharge SNF coverage decision reveals "observation" status.

## What's at stake

### Part A vs Part B

- **Inpatient (Part A):** flat per-discharge payment to the hospital. Patient pays the Part A deductible (around $1,632 in 2024-2026). Drugs, services, and procedures during the stay are covered without separate cost-sharing.
- **Observation (Part B):** outpatient services. Patient pays the Part B deductible plus 20% coinsurance on each separately-billed item — physician visits, drugs, lab tests, imaging. Self-administered drugs (the patient's own home medications administered in the hospital) typically not covered at all.

### The Skilled Nursing Facility three-day rule

Medicare Part A covers SNF care only if the patient had a qualifying **three-day inpatient hospital stay** preceding the SNF admission (42 CFR § 409.30). Observation days do not count. A patient who spent five days in the hospital under observation status, then needed SNF rehab, may discover they have no SNF coverage at all.

This is the most financially consequential observation-status problem and the reason CMS and Congress have repeatedly examined the rule.

## The two-midnight rule

CMS's "two-midnight rule" (42 CFR § 412.3, effective October 2013) sets the expectation:

- If the admitting physician expects the patient to need hospital care that spans **two or more midnights**, the patient should generally be admitted as inpatient (Part A).
- If less than two midnights, observation (Part B) is generally appropriate.

The rule is not absolute; clinical judgment governs. But it sets a presumption.

## The MOON notice

The Medicare Outpatient Observation Notice (MOON) — required under the NOTICE Act (Pub. L. 114-42, 2015) — must be delivered to Medicare beneficiaries within **36 hours** of starting to receive observation services. The notice tells the patient:

- They are an outpatient receiving observation services, not an inpatient
- The Part B financial consequences
- The implication for SNF coverage

If the patient did not receive a MOON or received it late, that's a process violation worth documenting.

## When this rule fires

- A Medicare patient received a bill showing observation/outpatient status when they expected inpatient.
- A Medicare patient was denied SNF coverage because the hospital stay was observation, not inpatient.
- A Medicare patient is contesting the MOON they received.
- A Medicare patient discovers self-administered drug charges they didn't anticipate.

## The patient's playbook

### 1. Confirm the actual status

Pull the hospital bill and the Medicare Summary Notice (MSN). The MSN identifies whether each encounter was billed to Part A (inpatient) or Part B (outpatient/observation).

### 2. Request the medical records

Under HIPAA (`rules/14_hipaa_right_of_access.md`), request the admission orders, attending-physician notes, and any utilization-review documentation showing why observation was chosen instead of inpatient.

### 3. Self-administered drug refunds

Many hospitals charge for "self-administered drugs" during observation stays at retail prices (sometimes $50-$200 per dose for medications the patient could have brought from home). Some hospitals have policies allowing patients to bring their own medications; others do not. Either way, the patient can:

- Ask the hospital pharmacy for a refund or write-off of self-administered drug charges
- Submit the receipts to the patient's Medicare Advantage plan (if applicable) or to original Medicare for reimbursement consideration (Part B coverage of self-administered drugs is limited but case-by-case appeal may be appropriate)

### 4. Reclassification request

If the patient believes inpatient status was clinically appropriate:

- Request that the hospital reclassify the encounter to inpatient.
- The hospital can do this within certain time windows (typically before claim submission).
- After claim submission, the hospital must use Medicare's "Condition Code 44" process for reclassification, which requires utilization-review committee approval and physician sign-off.
- If reclassification is denied, appeal through the standard Medicare appeals process (see `rules/12_medicare_appeals.md`).

### 5. SNF coverage appeal

If the patient was denied SNF coverage due to the observation classification:

- Request the Medicare beneficiary appeal under 42 CFR § 405.940 et seq.
- The appeal can argue that the hospital encounter was clinically equivalent to an inpatient stay and should have been classified as such.
- A Beneficiary Notice of Non-coverage (BNN) provides the appeal hook.

### 6. State health insurance assistance program (SHIP)

Every state has a SHIP. Free, expert assistance for Medicare beneficiaries on observation status, appeals, and SNF coverage disputes. Lookup at [shiphelp.org](https://www.shiphelp.org).

### 7. Center for Medicare Advocacy

The Center for Medicare Advocacy ([medicareadvocacy.org](https://www.medicareadvocacy.org)) maintains a Self-Help Packet for "Observation Status" appeals. They also pursue class-action and policy advocacy on observation status. Free resources.

## The CMA observation-status lawsuit

In *Alexander v. Azar* (now *Alexander v. Becerra*), the Center for Medicare Advocacy successfully challenged the government's failure to provide a meaningful appeals process for observation-to-inpatient reclassification disputes. As a result of the 2022 settlement and subsequent CMS rulemaking, certain beneficiaries placed in observation status now have an expedited appeal right. Verify current procedures; this area is still evolving as of 2026.

## Tracker tagging

- `findings`: `medicare_observation_status_dispute`, `medicare_snf_denied_observation`, `medicare_self_admin_drug_charges`
- `next_action`: `request_observation_reclassification`, `appeal_snf_denial`, `dispute_self_admin_drug_charges`

## When this rule does not apply

- **Patient is not on Medicare.** Observation status is primarily a Medicare problem because of the Part A/Part B distinction and the SNF three-day rule.
- **Medicare Advantage observation issues** — Medicare Advantage plans have their own appeal process; see `rules/12_medicare_appeals.md` and check the plan's specific rules for observation-status disputes. Many MA plans have eliminated the SNF three-day rule, simplifying things for those enrollees.

## Related

- [[12_medicare_appeals]] — the appeals framework that observation-status disputes route into
- [[14_hipaa_right_of_access]] — for getting the medical records to support the dispute
- `templates/letter_medicare_appeal.md` — adapt with observation-status-specific arguments
