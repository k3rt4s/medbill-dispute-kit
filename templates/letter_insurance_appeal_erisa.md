# Template — Insurance appeal (ERISA self-funded plan)

Use when an ERISA-covered employer health plan has denied a claim and you are filing the internal appeal (or the final-level appeal). For non-ERISA plans (individual market, government, church), the structure is similar but the closing legal citations differ; the LLM should adapt accordingly.

This template follows the structure Marshall Allen credited to Laurie Todd ("the Insurance Warrior"): contract analysis first, clinical evidence as numbered exhibits, specific relief at the close.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

Appeals Department
[PLAN NAME]
[PLAN MAILING ADDRESS]
[CITY, STATE ZIP]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: Formal appeal of denied claim
    Member: [PATIENT FULL NAME]
    Member ID: [INSURANCE MEMBER ID]
    Plan: [PLAN NAME]
    Group #: [GROUP NUMBER]
    Claim #: [CLAIM NUMBER]
    Date(s) of service: [DATE OF SERVICE]
    Service denied: [SERVICE / PROCEDURE]
    Denial date: [DENIAL DATE]
    Denial reason cited: [DENIAL REASON, quoted from the denial letter]

Dear Appeals Department:

I am filing this internal appeal of [PLAN NAME]'s denial dated [DENIAL DATE] of coverage for [SERVICE / PROCEDURE] rendered on [DATE OF SERVICE]. The denial is in error and should be reversed.

I. Relief requested

I respectfully request that the plan:

1. Reverse the denial and approve coverage for [SERVICE / PROCEDURE] at the in-network benefit level.
2. Process the claim and remit payment to the provider, or reimburse me directly if I have paid out of pocket, in the amount of $[AMOUNT].
3. Provide a written decision on this appeal within the timeframes required by 29 CFR § 2560.503-1 (or the plan's stated deadlines, whichever is shorter).

II. Plan terms

I have reviewed [PLAN NAME]'s Summary Plan Description (SPD). The SPD obligates the plan to cover [SERVICE / PROCEDURE] in my circumstances. Specifically:

- [Quote the SPD provision that defines covered services to include this category, with section number.]
- [Quote any SPD provision about respecting the treating physician's medical decision-making.]
- [Quote any SPD provision about medical necessity standards.]

The denial reason cited — [DENIAL REASON] — does not match the SPD's actual language. [Explain the mismatch concretely.]

III. Medical necessity (if denied as not medically necessary)

The service is medically necessary for my specific case. Attached as Exhibit A is a written statement from my treating physician, [PHYSICIAN NAME, CREDENTIALS], who has determined that [SERVICE / PROCEDURE] is medically necessary because [clinical rationale].

The service is also supported by published clinical practice guidelines:

- Exhibit B: [Guideline source — e.g. specialty society name, year, citation]
- Exhibit C: [Peer-reviewed study or evidence-based guideline if applicable]

[Quote the specific recommendation language from the guideline that supports the service for the patient's condition.]

IV. Not experimental or investigational (if denied as experimental)

The service is not experimental or investigational. It is [FDA-approved / cleared / standard of care]. Specifically:

- Exhibit D: [FDA approval or clearance documentation]
- Exhibit E: [Standard-of-care guideline inclusion]
- The service is covered by [list other major insurers covering this service, if known], which is inconsistent with characterizing it as experimental.

V. Documentation supporting the appeal

I am attaching the following:

- Exhibit A: Treating physician's medical-necessity letter, dated [DATE]
- Exhibit B: [Clinical guideline]
- Exhibit C: [Peer-reviewed evidence]
- Exhibit D: [FDA documentation, if applicable]
- Exhibit E: [Other supporting evidence]
- Exhibit F: Copy of the denial letter dated [DENIAL DATE]
- Exhibit G: Copy of the Explanation of Benefits

VI. Procedural requests

Pursuant to 29 CFR § 2560.503-1, please provide, free of charge, all documents, records, and other information relevant to my claim, including:

1. The complete Summary Plan Description and plan document for the plan year in which the service was rendered.
2. Any internal rule, guideline, protocol, or other similar criterion the plan relied on in denying the claim.
3. The qualifications of the reviewer(s) who decided the initial denial.
4. Any clinical or scientific evidence the plan relied on in denying the claim as not medically necessary or experimental.

VII. Preservation of rights

This plan is, to my knowledge, governed by the Employee Retirement Income Security Act of 1974 (ERISA), 29 U.S.C. §§ 1001 et seq. I am preserving all rights under ERISA, specifically:

- ERISA § 502(a)(1)(B), 29 U.S.C. § 1132(a)(1)(B), to bring a civil action to recover benefits due under the plan;
- ERISA § 503, requiring a full and fair review of denied claims;
- The right to request external review by an Independent Review Organization following exhaustion of internal appeals;
- Any right to attorney's fees under ERISA § 502(g).

I expect a written decision on this appeal within the timeframes required by the plan and by 29 CFR § 2560.503-1. If the denial is upheld, please simultaneously provide:

1. The specific reasons for upholding the denial, including reference to specific plan provisions;
2. A statement of my right to receive, upon request, all documents relevant to the claim;
3. A statement of my right to bring a civil action under ERISA § 502(a);
4. A description of the external review process available to me.

I can be reached at [PATIENT PHONE] or [PATIENT EMAIL].

Sincerely,



[PATIENT FULL NAME]

Member ID: [INSURANCE MEMBER ID]
Group #: [GROUP NUMBER]
Claim #: [CLAIM NUMBER]

cc:
    [STATE INSURANCE DEPARTMENT NAME] — Consumer Insurance Services
    US Department of Labor — Employee Benefits Security Administration (1-866-444-3272)

Enclosures: Exhibits A-G as listed above
```

---

## Placeholders and rendering notes

- The LLM renders only the sections (Medical necessity, Not experimental) that match the actual denial reason. Skip irrelevant sections rather than padding.
- If the plan is not ERISA-covered (individual market, government employer, church plan), remove the ERISA citations in Section VII and substitute the applicable state law or ACA appeal-rights language. The LLM should ask the patient "is this insurance through an employer (and if so, is it self-funded), through the ACA marketplace, through Medicare, or other?" before rendering.
- Exhibit-letter ordering matters less than the fact that each cited exhibit is actually attached. The LLM should list only exhibits the patient will actually attach.

## Parallel actions

- **State insurance department complaint:** file the same day. State pressure is often what gets ERISA disputes moving.
- **DOL EBSA**: free informal intervention at 1-866-444-3272. This is underused; EBSA benefits advisors will call the plan administrator on the patient's behalf.

## Follow-up

The LLM logs this with `action_type = "insurance_appeal_internal_sent"`. ERISA plans typically have 30 days to respond to non-urgent claims and 60-72 hours for urgent. Set `response_due_by` accordingly based on the plan's actual stated timeframe (which the SPD will specify).

## Final-level appeal and external review

After internal appeal denial, the patient may request external review by an Independent Review Organization, which is required by the ACA for most plans. The structure of the external review submission is similar to this template; the audience is the IRO, not the plan. External review decisions are binding on the insurer.

## When to call a lawyer

If the amount in dispute exceeds ~$10,000, the denial involves multiple denials of related services (e.g. ongoing chemotherapy), or the medical issue is complex, consult an ERISA attorney before the final internal appeal. ERISA attorneys often work on contingency; the entire administrative record gets locked in at the end of internal appeals, so the strongest submission needs to happen before the final denial.
