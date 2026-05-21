# Template — HIPAA medical records request

Use to obtain the patient's medical record under the federal right of access at 45 CFR § 164.524 (HIPAA Privacy Rule) before, during, or in support of a billing dispute. The record is the only way to verify that every service line on the bill corresponds to a service actually delivered in the documented chart. Marshall Allen recommends running this in parallel with the itemization request on any bill where the line-item count or quantity looks inflated, where a "service not received" finding has surfaced, or where the patient's recollection of the encounter does not match what was billed.

Legal anchors: 45 CFR § 164.524 (right of access; 30-day response window, one 30-day extension permitted), 45 CFR § 164.502(a)(1)(i) (covered-entity disclosure obligations), and the HHS Office for Civil Rights' 2016 guidance on permitted fees (labor for copying only; no per-page surcharge in most states; no flat "retrieval fee").

If the provider fails to respond within 30 days, refuses, or charges an excessive fee, escalate to `templates/complaint_hipaa_access.md` (OCR HIPAA complaint).

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]
Date of birth: [DOB]

[DATE]

[MEDICAL RECORDS DEPARTMENT / HEALTH INFORMATION MANAGEMENT]
[PROVIDER NAME]
[PROVIDER MAILING ADDRESS]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: Request for individual access to protected health information
    pursuant to 45 CFR § 164.524 —
    Patient: [PATIENT FULL NAME]
    DOB: [DOB]
    Medical record number (if known): [MRN]
    Date(s) of service requested: [DATE OF SERVICE OR RANGE]
    Billing account number for cross-reference: [ACCOUNT NUMBER]

To Medical Records:

I am the patient identified above. Pursuant to the federal right of individual access at 45 CFR § 164.524 of the HIPAA Privacy Rule, I request a complete copy of my designated record set for the date(s) of service listed above.

I. Scope of records requested

Please provide the following, to the extent each exists for the date(s) of service above:

1. Complete patient chart, including admission and discharge notes, history and physical, progress notes, consultation notes, and any addenda.

2. Physician and nursing notes for every clinician who saw me during the encounter, including any resident, fellow, midlevel, or contracted provider.

3. All diagnostic results, including but not limited to laboratory results, imaging reports, EKG tracings, pathology reports, and the corresponding interpretations.

4. Complete medication administration record (MAR), including each drug name, dose, route, time, and the credentials of the administering clinician.

5. Procedure and operative reports for every billed procedure or interventional service.

6. Anesthesia record if applicable, including pre-anesthesia evaluation, intra-operative anesthesia notes, and post-anesthesia recovery notes.

7. Emergency department record in full, including triage notes, vital signs, nursing reassessments, and the disposition note, if the encounter was in the ED.

8. Discharge summary or after-visit summary.

9. Copies of any consent forms I signed, including the consent to treat, financial responsibility forms, and any HIPAA acknowledgments.

10. The encounter-level billing audit trail or charge-capture document, if your system maintains one as part of the designated record set, showing which clinician or system entered each charge.

II. Format and delivery

Please provide the records in [paper / electronic (PDF on encrypted USB or via your patient portal)] format, delivered to the mailing address above (paper) or to the patient portal account on file (electronic).

The HIPAA Privacy Rule requires that you provide the records in the form and format requested, if readily producible. If electronic copies of the records are maintained, electronic delivery is required upon request (45 CFR § 164.524(c)(2)(ii)).

III. Fees

Under 45 CFR § 164.524(c)(4) and the HHS Office for Civil Rights' January 2016 guidance, a covered entity may charge only a reasonable, cost-based fee that includes:

- Labor for copying;
- Supplies for paper or electronic media; and
- Postage if the patient requests mailing.

The following are not permitted: search and retrieval fees, per-page fees in excess of labor cost in states whose law caps such fees, and flat "minimum" fees that exceed actual cost.

Please provide a written itemized statement of any fee in advance, broken down by category, so I can confirm it is consistent with § 164.524(c)(4) before authorizing the work. If the fee exceeds [the state cap, where applicable / $30], I request the flat-rate option permitted under the HHS 2016 guidance (where a covered entity offers patients a single flat fee that does not exceed actual costs).

IV. Statutory response window

Under 45 CFR § 164.524(b)(2), you must act on this request no later than thirty (30) days after receipt. One thirty (30)-day extension is permitted under § 164.524(b)(2)(ii) on written notice to me stating the reason and the date by which records will be provided. No further extensions are permitted by rule.

V. Purpose of the request (not legally required, provided as context)

I am reviewing the billing account referenced above against the underlying medical record to verify that every service line on the bill corresponds to a service actually documented in the chart. This is a routine billing-review purpose; the request is not for litigation discovery and a release-of-information form for third parties is not needed because I am requesting my own records as the individual subject of the protected health information.

VI. Contact

Please send the records to the address above. If anything in this request is unclear, please call me at [PATIENT PHONE] or email [PATIENT EMAIL]; please do not delay the records pending clarification of a single line item.

Sincerely,



[PATIENT FULL NAME]

Patient DOB: [DOB]
Account number for cross-reference: [ACCOUNT NUMBER]
Date of service: [DATE OF SERVICE]

Enclosures:
- Copy of a government-issued photo identification (if your records department requires identity verification by mail; many do)
- (Optional) Copy of the bill being reviewed, to help your records team locate the encounter

cc:
- file
- (If escalating later) [STATE] Office for Civil Rights regional office / federal HHS OCR
```

---

## Placeholders and rendering notes

- `[STATE]` controls one piece of substance: many states cap per-page copy fees below the federal rule. If `references/laws_state_<code>.md` lists a state cap, the drafter renders the cap in the "Fees" section. Common caps: TN $0.50/page after first 5 pages free, NY $0.75/page, CA $0.25/page or $10 minimum, TX $25 for first 20 pages.
- `[MRN]` — if the patient knows their medical record number from a portal or prior letter, fill it in. Otherwise leave blank; date of service + DOB is sufficient.
- Many large hospital systems route records requests through a third-party vendor (Sharecare, MRO, ScanSTAT, Verisma). The patient may receive a fee quote from the vendor rather than the provider. The federal rule still binds the covered entity; vendor pricing is constrained by the same § 164.524(c)(4) limits.

## Parallel actions to take the same day

1. Mail this letter certified to the records department.
2. If the provider has a patient-portal records request feature, submit the same request there in parallel. Keep a screenshot of the submission confirmation.
3. Log the action in `tracker.csv` with `action_type = records_request_sent` (via `scripts/log_interaction.py`).
4. If the bill is in active dispute, send a one-line update to the biller stating that you have requested the medical record under HIPAA § 164.524 and will not pay any disputed portion until the record is reviewed.

## Follow-up

- 30 days from postmark: if no records and no extension notice → draft `templates/complaint_hipaa_access.md` for OCR.
- If extension notice received: 60-day total deadline.
- When records arrive: review against the itemized bill line by line. Document every service line that is not supported by a chart entry. Add those line items to the dispute letter (`templates/letter_initial_dispute.md`) under a new section "Services billed without documentation".
- If a service was billed but not documented, the dispute strengthens significantly. The provider's options narrow: amend the chart (which raises its own concerns under state medical-records statutes), refund the charge, or face a state DOI / AG complaint citing both the billing dispute and the records gap.

## What this is not

This is not a litigation discovery request. It is not a subpoena. It is the patient's federal HIPAA right of access to their own records, and it carries a 30-day statutory clock. A records department that responds with "send us a subpoena" or "have your attorney request these" is in apparent violation of § 164.524 and should be reported to HHS OCR.
