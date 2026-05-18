# Template — Medicare appeal (Levels 1 and 2)

Use for a written Medicare appeal request at Level 1 (Redetermination for Parts A/B, Reconsideration for Part C, or Redetermination for Part D) or Level 2 (QIC for A/B, IRE for Part D). Levels 3-5 use specific OMHA / DAB / federal-court forms; for those, see `rules/12_medicare_appeals.md`.

The LLM picks the variant by asking the patient: which part of Medicare is this (A/B, Part C, Part D)? what level are you at? what was the date of the prior decision?

The form **CMS-20027** is the optional Medicare-published form for Level 1 Original Medicare appeals; a written letter containing the required elements is equally acceptable. For Part C and Part D, the plan's denial notice will state how to file.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

[APPEALS DEPARTMENT — name depends on level/part. Examples:
 - Original Medicare Level 1: The MAC named on the MSN
 - MA Level 1: The Medicare Advantage plan's appeals department
 - Part D Level 1: The Part D plan's appeals department
 - Level 2 A/B: The Qualified Independent Contractor named in the redetermination decision
 - Level 2 D: Maximus Federal Services Part D Appeals]
[APPEALS DEPARTMENT MAILING ADDRESS]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: [Pick one:
    Request for Medicare Redetermination (Part A/B Level 1) /
    Request for Reconsideration (Part C Level 1) /
    Request for Coverage Determination Redetermination (Part D Level 1) /
    Request for QIC Reconsideration (Part A/B Level 2) /
    Request for IRE Review (Part D Level 2)]
    Beneficiary: [PATIENT FULL NAME]
    Medicare Beneficiary Identifier (MBI): [MBI]
    [If Part C / Part D, also include: Plan name: [PLAN NAME]; Member ID: [MEMBER ID]; Group #: [GROUP]]
    Claim / Coverage Determination #: [CLAIM OR DETERMINATION NUMBER]
    Service date(s): [DATE(S) OF SERVICE]
    Prior decision date: [DATE OF MSN, EOB, OR PRIOR-LEVEL DECISION]
    Amount in controversy: $[AMOUNT]

Dear Appeals Department:

I respectfully request [redetermination / reconsideration / IRE review] of the denial dated [PRIOR DECISION DATE] regarding the services or items described above. The denial is in error and should be reversed for the reasons set forth below.

I. Service(s) and items at issue

[Describe each denied service or item, the date(s), and the provider. Example:
- CPT 70551 (MRI brain without contrast), date of service [DATE], performed by [PROVIDER NAME, NPI].
- Drug name (NDC, dose, days supply), prescribed [DATE], by [PRESCRIBING PROVIDER, NPI].]

II. Denial reason cited

The prior decision states the denial reason as: "[QUOTE THE DENIAL REASON VERBATIM FROM THE MSN / EOB / PRIOR DECISION]."

III. Why this denial is in error

[The LLM renders one or more of the following blocks based on the actual denial reason.]

[BLOCK A — Medical necessity]

The service is medically necessary for my specific clinical condition. My treating physician, [PHYSICIAN NAME, NPI, CREDENTIALS], has determined that this service is appropriate and necessary; their written statement is attached as Exhibit A. The relevant Local Coverage Determination [LCD ID: L#####] / National Coverage Determination [NCD ID: ###.#] includes my clinical situation as a covered indication. Specifically, [briefly map the patient's diagnosis and clinical history to the covered-indication language in the LCD/NCD].

[BLOCK B — Coding correction]

The denial appears to rest on a coding issue. The service should have been billed using [CORRECT CPT/HCPCS code] rather than [CODE AS BILLED]. The patient does not control the provider's coding; if the provider submitted an incorrect code, the appropriate remedy is to require the provider to resubmit. I am simultaneously asking the provider to correct the submission.

[BLOCK C — Documentation supplemented]

The denial appears to rest on insufficient documentation. I am submitting additional documentation as Exhibit [X]: [list — clinical notes, imaging reports, lab results, treating-physician letter, prior conservative-treatment records]. This additional documentation establishes [the medical necessity / the diagnosis required by the LCD / the prior-conservative-treatment requirement / the specific clinical fact at issue].

[BLOCK D — Formulary or step-therapy exception (Part D)]

The denied drug is medically necessary for my condition because the preferred formulary alternatives are [inappropriate / contraindicated / have been tried and failed / pose unacceptable risk]. Specifically: [explain]. My prescribing physician's statement supporting this exception is attached as Exhibit A.

[BLOCK E — Wrong patient or duplicate]

The denied claim was filed for a service I did not receive, or duplicates another already-paid claim. [Provide specifics.] Please reverse the denial and correct the claim history.

[END BLOCKS]

IV. Procedural requests

1. Please make all documents, evidence, and clinical-criteria materials used in the prior decision available to me, free of charge, per 42 CFR § 405.946 (Original Medicare) or 42 CFR § 422.566 (Medicare Advantage) or 42 CFR § 423.580 (Part D).
2. Please notify me in writing of your decision within the timeframes required by law: 60 days for Original Medicare Level 1; 30 days (services) or 60 days (payment) for Part C Level 1; 7 days for Part D Level 1 standard, 24 hours for expedited.
3. If you uphold the prior decision in whole or in part, please simultaneously provide the specific reasons referenced to the LCD, NCD, plan policy, or evidence relied on, and a statement of my right to advance to the next level of appeal with the applicable deadline.

V. Expedited review (render only if applicable)

I request **expedited** review of this appeal pursuant to [42 CFR § 422.584 (Part C) / 42 CFR § 423.584 (Part D)] because waiting for a standard decision could seriously jeopardize my life, health, or ability to regain maximum function. Specifically: [state the clinical urgency]. My treating physician's supporting statement is attached as Exhibit B.

VI. Representative

[Render only if applicable.]

I have appointed [REPRESENTATIVE NAME] as my representative for this appeal. Form CMS-1696 ("Appointment of Representative") is attached as Exhibit Z. Please copy [REPRESENTATIVE NAME] on all correspondence at [REPRESENTATIVE ADDRESS / PHONE / EMAIL].

VII. Documentation enclosed

- Exhibit A: Treating physician's written statement dated [DATE]
- Exhibit B: [As applicable: clinical guidelines, peer-reviewed studies, prior-treatment records]
- Exhibit C: Copy of the Medicare Summary Notice / EOB / prior decision being appealed
- Exhibit D: [As applicable: corrected billing documents]
- [Other exhibits as needed]

Thank you for your prompt attention to this appeal.

Sincerely,



[PATIENT FULL NAME]

Medicare Beneficiary Identifier: [MBI]
[For Part C / D: Plan name and Member ID]
Date of service: [DATE OF SERVICE]
Date of prior decision: [DATE OF MSN / EOB / PRIOR-LEVEL DECISION]

cc:
    [State Health Insurance Assistance Program (SHIP) for the patient's state — free Medicare appeals help]
    [Treating physician for this service]
    [Patient's representative if any]

Enclosures: as listed in Section VII
```

---

## Placeholders and rendering notes

- The LLM must ask up-front: which part of Medicare (A/B, C, D)? Which level? Date of the prior decision (to confirm the filing deadline hasn't run)?
- For **Part C and Part D**, copy the plan's appeals department address from the denial notice. Never guess; plans use multiple addresses for different types of correspondence.
- For **Original Medicare Level 1**, the MAC and its address are on the MSN.
- For **Level 2 A/B**, the QIC is named in the Level 1 redetermination decision letter — typically C2C Innovative Solutions or Maximus, depending on the region.
- For **Level 2 D**, the IRE is Maximus Federal Services. Their address is at [medicareappeals.com](https://medicareappeals.com).

## Required elements (per CMS-20027 and 42 CFR equivalents)

Every Medicare appeal at Levels 1 and 2 must include:

1. Beneficiary's name
2. Medicare Beneficiary Identifier (MBI)
3. Specific service(s) or item(s) for which redetermination is being requested
4. Specific date(s) of service
5. Patient's name and signature (if not signed by the beneficiary, a Form CMS-1696 Appointment of Representative is required)

The letter format above includes all five plus richer evidentiary support.

## Free appeal help — the LLM must surface

- **State Health Insurance Assistance Program (SHIP)** — every state has one; lookup at [shiphelp.org](https://www.shiphelp.org). Free, unbiased, trained counselors.
- **Medicare Rights Center** — [medicarerights.org](https://www.medicarerights.org). National counseling helpline.
- **Center for Medicare Advocacy** — [medicareadvocacy.org](https://www.medicareadvocacy.org). Free templates and legal-services referrals.

For Levels 3-5 with significant amounts at stake, a Medicare-specialty attorney is appropriate. Many work on contingency or hourly with caps; the Medicare Rights Center can refer.

## Follow-up

The LLM logs at the appropriate `action_type`: `medicare_redetermination_filed` (Level 1), `medicare_reconsideration_filed` (Level 2 A/B or D), or `medicare_alj_hearing_filed` (Level 3, separate template). Set `response_due_by` based on the level: 60 days for Level 1 A/B, 30-60 days for Part C Level 1, 7 days for Part D Level 1, 60 days for Level 2 A/B, 30 days for Level 2 D.

If the appeal is upheld in the patient's favor, log the closure and update the underlying bill's `current_balance` if the upstream provider should now refund or reduce.

## Related

- [[../rules/12_medicare_appeals]] — full five-level walkthrough
- [[letter_insurance_appeal_erisa.md]] — for ERISA-covered employer plans (different process)
