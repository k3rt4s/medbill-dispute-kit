# Template — CMS Hospital Price Transparency complaint

For when a hospital has failed to publish a compliant machine-readable file (MRF) of standard charges under 45 CFR Part 180. Filed at the federal CMS complaint portal; produces real regulatory pressure because CMS can impose civil monetary penalties up to approximately $2 million per year for non-compliant large hospitals. PatientRightsAdvocate.org audits suggest only 34-36% of hospitals are fully compliant, so this complaint has very high probability of success.

This complaint is most useful as a **parallel action** to a billing dispute, not as a standalone remedy. The patient's individual bill is not corrected by this complaint, but the complaint pressures the hospital to (a) publish the MRF, which gives the patient hard evidence of negotiated rates and cash prices to use in their dispute, and (b) makes a corporate-side compliance officer aware of the patient's case, which often accelerates the underlying dispute.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

Centers for Medicare and Medicaid Services
Hospital Price Transparency Compliance
[Filed online at https://www.cms.gov/hospital-price-transparency/contact-us]

RE: Complaint — Hospital Price Transparency Rule non-compliance
    Hospital: [HOSPITAL LEGAL NAME]
    CMS Certification Number (CCN): [CCN IF KNOWN, OTHERWISE NOTE "unknown"]
    Hospital address: [HOSPITAL ADDRESS]
    Date(s) of observation: [DATES THE PATIENT CHECKED THE WEBSITE]

To the Hospital Price Transparency compliance team:

I am submitting this complaint regarding [HOSPITAL LEGAL NAME]'s non-compliance with the Hospital Price Transparency Rule, 45 CFR Part 180, specifically with respect to the machine-readable file (MRF) requirement at 45 CFR § 180.50 and the consumer-friendly shoppable-services display required by 45 CFR § 180.60.

I. Summary of non-compliance observed

[The LLM renders the applicable subset of these blocks based on what the patient actually observed. Be specific; CMS triages complaints on specificity.]

[BLOCK A — No MRF posted at all]

I have searched the hospital's website at [HOSPITAL WEBSITE URL] on [DATES] and was unable to locate any machine-readable file of standard charges. The hospital's website does not include a link labeled "price transparency," "machine-readable file," "standard charges," or similar, in any location reasonable consumers would discover (homepage footer, billing page, patient information page). I also searched for the file at the standard discoverable location [hospitalwebsite.example.com/standardcharges] without success.

[BLOCK B — MRF posted but materially incomplete]

The hospital's machine-readable file at [URL OF MRF] is materially incomplete. Specifically:

- [The file omits payer-specific negotiated charges for one or more named payers / The file omits the discounted cash price for items and services / The file omits de-identified minimum and maximum negotiated charges / The file omits coded items (CPT, HCPCS, DRG, NDC) that the rule requires / The file uses placeholder text such as "N/A," "Call for price," or "[redacted]" in place of actual charges / Other specific deficiency].
- [If applicable per CY 2026 OPPS final rule:] The file does not appear to include the median allowed amount or 10th/90th percentile allowed amounts required as of [APPLICABLE EFFECTIVE DATE].
- The hospital's attestation of accuracy, required by 45 CFR § 180.50, is [not present / dated more than one year ago / signed by someone who does not appear to be the CEO or other delegated executive].

[BLOCK C — No consumer-friendly display]

The hospital does not maintain a consumer-friendly display of at least 300 shoppable services as required by 45 CFR § 180.60, or its display includes fewer than 300 services without providing the standard charges file in a sortable format as an alternative. Specifically: [describe what is or is not on the hospital's website].

[BLOCK D — MRF posted but locked behind login or other access barrier]

The MRF appears to exist at [URL] but is [behind a login wall / requires the user to agree to terms / only accessible after providing personal information]. 45 CFR § 180.50(d)(1) requires the file to be "easily accessible," "without barriers" including without requiring users to establish a user account.

[END BLOCKS]

II. Patient context

I have a current billing dispute with [HOSPITAL NAME] regarding account #[ACCOUNT NUMBER], date of service [DATE]. The hospital's failure to publish a compliant machine-readable file directly impairs my ability to:

1. Verify the negotiated rate that should have been applied to my insurance claim;
2. Compare the hospital's cash price with the amount I am being charged;
3. Evaluate whether the charged amount is reasonable in good faith under generally applicable contract law.

The Hospital Price Transparency Rule exists precisely to enable this kind of patient-side verification, and the hospital's non-compliance has the practical effect of suppressing the information patients are entitled to use.

III. Requested action

I respectfully request that the Centers for Medicare and Medicaid Services:

1. Open an investigation into [HOSPITAL NAME]'s compliance with 45 CFR Part 180.
2. Take appropriate enforcement action under 45 CFR § 180.90, up to and including civil monetary penalties.
3. Require the hospital to come into compliance with all elements of the rule within a defined timeframe and to certify compliance to CMS.
4. Provide me notification of the outcome of the investigation to the address above.

IV. Evidence

I have attached screenshots of the hospital's website pages I reviewed, with timestamps, demonstrating the non-compliance described above.

Thank you for your attention to this matter.

Sincerely,



[PATIENT FULL NAME]

Date(s) of website observation: [DATES]
Patient's affected account number: [ACCOUNT NUMBER] (provided for context; you may share this complaint with the hospital in connection with your investigation)

Enclosures: screenshots of the hospital website pages on the dates of observation
```

---

## How to file

The CMS complaint portal lives at [cms.gov/hospital-price-transparency/contact-us](https://www.cms.gov/hospital-price-transparency/contact-us). The portal accepts the complaint as a web form or by email; check the page for the current submission method. Attach the letter and the screenshots. Note the date of submission and any confirmation number for your tracker.

PatientRightsAdvocate.org also accepts complaints at [hospitalpricingfiles.patientrightsadvocate.org](https://hospitalpricingfiles.patientrightsadvocate.org); a parallel submission there contributes to their public audit data and adds advocacy pressure on the hospital independent of the CMS regulatory process.

## Placeholders and rendering notes

- **Specificity matters.** CMS receives many low-quality complaints. A complaint with timestamped screenshots, specific URLs, and specific identified deficiencies (e.g. "the file is missing the de-identified minimum negotiated charge for CPT 99214") will be triaged ahead of a generic complaint.
- **The patient does not need to identify which deficiency applies to their specific CPT codes.** If the file is missing any required element, the rule is violated. The LLM should err on the side of comprehensiveness.
- **If the patient's hospital has been audited by PatientRightsAdvocate.org**, reference the audit findings explicitly. Their semi-annual reports are at [patientrightsadvocate.org/pra-reports](https://www.patientrightsadvocate.org/pra-reports).

## What to use the MRF for once it appears

If the complaint produces compliance (the hospital posts a compliant MRF), use the MRF immediately:

1. **Find the patient's CPT codes** in the MRF.
2. **Note the negotiated rate** for the patient's insurance carrier and the cash price.
3. **Use these numbers** as the anchors in any pending dispute letter under `letter_initial_dispute.md` or `letter_hardship_negotiation.md`. "Your own published file shows a cash price of $X for this CPT" is a much stronger argument than third-party fair-price data.

## Follow-up

The LLM logs this with `action_type = "cms_hpt_complaint_filed"`. CMS does not typically respond directly to the complainant about specific enforcement actions, so `response_due_by` is less meaningful here. Set it to 90 days from today as a check-in milestone; if the hospital's compliance posture has not changed by then, consider re-filing with new evidence or escalating to a member of Congress (which the office's case-work team will route).
