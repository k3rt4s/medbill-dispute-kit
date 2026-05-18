# Template — Dental insurance dispute

Dental insurance billing has its own pathologies separate from medical insurance. The two most common patient-side issues are **downcoding** (the insurer reimburses at the rate for a less-expensive procedure than what was performed) and **bundling** (the insurer treats two billable procedures as one for reimbursement purposes). Tennessee's HB 949 / SB 677, codified at Tenn. Code Ann. § 56-2-305 (effective July 1, 2024), explicitly targets these practices and adds enforcement penalties. Many states have similar non-covered-services laws.

This template handles both insurer-side disputes (claim denied or down-paid) and provider-side disputes (the dentist's office bill is wrong) — pick the variant in Section II.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

[For insurer-side dispute:
 Appeals Department
 [DENTAL PLAN NAME]
 [PLAN MAILING ADDRESS]]

[For provider-side dispute:
 Billing Department
 [DENTAL OFFICE NAME]
 [OFFICE MAILING ADDRESS]]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: Dental claim dispute —
    Patient: [PATIENT FULL NAME]
    [If insurer-side: Member ID: [MEMBER ID]; Group #: [GROUP]; Claim #: [CLAIM]]
    [If provider-side: Account #: [ACCOUNT]]
    Date(s) of service: [DATE OF SERVICE]
    Total at issue: $[AMOUNT]

Dear [Appeals Department / Billing Department]:

I am writing to dispute the [denial of / underpayment of / charges on] the above-referenced [claim / account]. The [denial / charge] is in error and should be corrected for the reasons set forth below.

I. Services rendered

The following services were performed on [DATE OF SERVICE] by [DENTIST NAME, DDS, License #]:

- **[ADA / CDT code]** — [Plain-English description of the procedure performed]. Tooth/quadrant: [LOCATION]. Charge: $[CHARGE].
- [Additional services as applicable]

II. Nature of the dispute

[The LLM renders the applicable block(s). Render only those that fit.]

[BLOCK A — Insurer downcoded the claim]

Your Explanation of Benefits dated [DATE] reimbursed the procedure as if [LOWER-COST CDT CODE WITH DESCRIPTION] had been performed, rather than the actual procedure [HIGHER-COST CDT CODE WITH DESCRIPTION] that was rendered and documented in my dental record. The procedures are not clinically interchangeable; my dentist performed [CORRECT PROCEDURE] for the following clinical reasons: [reasons].

Downcoding a properly-documented procedure violates the terms of my plan and, in Tennessee, **Tenn. Code Ann. § 56-2-305** (effective July 1, 2024), which prohibits a dental plan from downcoding to a procedure not performed or supported by the clinical documentation. [For other states, substitute the state's non-covered-services or anti-downcoding statute; if none exists, rely on the plan terms and the implied covenant of good faith.]

I request that you reprocess this claim using the actual CDT code [CORRECT CODE] and adjust payment accordingly.

[BLOCK B — Insurer bundled procedures]

Your Explanation of Benefits combined two separately billable procedures — [CDT CODE A — DESCRIPTION] and [CDT CODE B — DESCRIPTION] — and paid only for one. The ADA Current Dental Terminology specifies that these procedures are independently billable when performed on the same date; they are not part of a single bundled service.

Bundling separately-billable procedures violates the terms of my plan and, in Tennessee, **Tenn. Code Ann. § 56-2-305**. [For other states, substitute.]

I request that you reprocess this claim recognizing each procedure separately and adjust payment accordingly.

[BLOCK C — Coverage policy misapplied]

Your denial states the procedure is "not covered" or "not medically necessary." Pursuant to my plan, [QUOTE THE COVERAGE PROVISION THAT APPLIES]. My specific clinical situation falls within the covered category for the reasons stated by my dentist (see Exhibit A — dentist's narrative report). The denial reason cited does not match the plan's actual terms or the clinical facts.

[BLOCK D — Frequency limitation misapplied]

Your denial cites a frequency limitation (e.g., "two cleanings per benefit year"). [Either: I have not exceeded the stated limitation; the prior service occurred on [DATE] and the current service is more than [interval] later. OR: I qualify for the medically-necessary exception to the frequency limitation because [clinical reason — periodontal disease, pregnancy, post-procedure follow-up, etc.].]

[BLOCK E — Virtual credit card or unusual payment method]

You issued reimbursement to my dentist via a virtual credit card or other payment method that imposes processing fees on the dentist. In Tennessee, **Tenn. Code Ann. § 56-2-305** (effective July 1, 2024) prohibits dental plans from requiring providers to accept virtual credit cards as the only reimbursement method. While this is a provider-protection provision, it has downstream effects on me as the patient because the provider's net reimbursement is reduced and may be passed through. Please remit payment by ACH or check.

[BLOCK F — Provider-side: charges exceed agreed treatment plan]

The treatment plan dated [TREATMENT PLAN DATE], signed before treatment, stated my total responsibility as $[ESTIMATED AMOUNT]. The bill received is $[BILLED AMOUNT], a difference of $[DELTA] that was not disclosed in advance. Please provide a written reconciliation showing each line item and why the actual cost exceeded the estimate, or correct the bill to the estimated amount per the signed treatment plan.

[BLOCK G — Provider-side: insurance not properly billed]

The bill received treats my insurance as if it were never billed, but the insurance plan has confirmed the claim was either not submitted or not adjudicated. Please submit the claim through my insurance per my member ID [MEMBER ID] and reissue the bill reflecting any contractual write-off and patient responsibility.

[END BLOCKS]

III. Documentation

I am attaching the following:

- Exhibit A: [Dentist's narrative report or clinical documentation supporting the procedure as billed]
- Exhibit B: [Copy of the Explanation of Benefits or bill at issue]
- Exhibit C: [Treatment plan, if applicable]
- Exhibit D: [Photographs or radiographs supporting clinical documentation, if applicable]

IV. Requested action

I request that you, within fifteen (15) business days of the date of this letter:

1. Reprocess the claim correctly OR provide a corrected bill;
2. Issue payment to the dentist (or remove the disputed amount from my account) consistent with the correct adjudication;
3. Provide a written response addressing each disputed line and the basis for any portion you maintain.

If we cannot resolve this matter directly, I will escalate by:

- Filing a complaint with the [STATE INSURANCE DEPARTMENT] under [STATE STATUTE — e.g., Tenn. Code Ann. § 56-2-305 / § 56-8-105 for Tennessee; analogous statutes for other states];
- Filing a complaint with the [STATE ATTORNEY GENERAL] Consumer Protection Division under the state's UDAP statute;
- Pursuing any private rights of action available under state law.

Sincerely,



[PATIENT FULL NAME]

[For insurer-side: Member ID: [MEMBER ID]; Claim #: [CLAIM]]
[For provider-side: Account #: [ACCOUNT]]
Date of service: [DATE OF SERVICE]

cc:
    [STATE INSURANCE DEPARTMENT NAME — Consumer Insurance Services]
    [STATE ATTORNEY GENERAL — Consumer Protection]
    [STATE DENTAL ASSOCIATION, if relevant — many state dental societies advocate for patients against downcoding]
    [Treating dentist]

Enclosures: as listed in Section III
```

---

## Placeholders and rendering notes

- Dental procedures use **CDT codes** (Current Dental Terminology), not CPT. CDT is owned by the ADA. The LLM should not redistribute full CDT descriptors but may cite codes and use short paraphrased descriptions.
- The most common downcoded procedures in 2024-2026 practice are:
  - D2740 (porcelain/ceramic crown) downcoded to D2750 (porcelain fused to high noble metal) or D2391 (resin-based composite — one surface, posterior)
  - D4341 / D4342 (scaling and root planing) downcoded to D1110 (adult prophylaxis)
  - D2950 (core buildup) bundled into D2740 (crown)
  - D9230 / D9248 (nitrous oxide / sedation) treated as part of the underlying procedure
- The LLM must ask the patient: did your dentist provide a treatment plan in advance? Did you sign it? Was the actual procedure consistent with what was on the treatment plan?

## State-specific citations

**Tennessee:** Tenn. Code Ann. § 56-2-305 (effective July 1, 2024 via HB 949 / SB 677). Adds penalties to the Non-Covered Services Law; addresses downcoding, bundling, and virtual-credit-card restrictions.

**Other states:** Most states have a non-covered-services law. The ADA tracks these at [success.ada.org/en/practice-management/dental-insurance-and-third-party-payers/state-laws-on-dental-insurance](https://success.ada.org). Substitute the citation in the letter or use a generic "applicable state non-covered-services statute" placeholder with a warning to verify.

**No state statute:** Rely on the plan's own terms and the implied covenant of good faith and fair dealing. The argument is weaker but still actionable.

## Parallel actions

- **State insurance department complaint** if the insurer is downcoding or bundling without basis. State regulators take dental complaints seriously, particularly in states with anti-downcoding statutes.
- **State dental association** advocacy. Many state dental societies have insurance-issues committees that aggregate downcoding patterns and can pressure plans. Search "[State] dental association insurance committee."
- **National-Association-of-Dental-Plans complaint** — for chronic offenders, NADP runs voluntary best-practices certification; complaints there create reputational pressure.

## When this is not the right template

- The procedure was actually upcoded by the **dentist** (the dentist billed a more expensive code than they performed): that's a billing-error dispute against the dentist, not the insurer. Use `templates/letter_initial_dispute.md` and direct it to the dental office.
- The bill is correct but the patient cannot afford the patient-responsibility portion: use `templates/letter_hardship_negotiation.md`.

## Follow-up

The LLM logs this with `action_type = "dental_appeal_filed"` (insurer-side) or `initial_dispute_letter_sent` (provider-side). Set `response_due_by` to 15 business days from today. For insurer denials, after the internal appeal denial, request external review via the state's IRO process (analogous to the medical insurance external review described in `rules/07_appeal_insurance_denial.md`).
