# Template — Hardship negotiation

Use when a bill is correctly coded for services you actually received, but the amount exceeds what you can pay. This is **not** a dispute letter — it's a negotiation. The goal is a reduction, a payment plan, or both, ideally with the Medicare rate as the anchor and the hospital's published cash price as the ceiling.

For non-profit hospitals (most US hospitals), pair this with an IRS § 501(r) Financial Assistance Policy (FAP) application. The hospital is **required** to consider you for charity care before any extraordinary collection action. Screen for eligibility through [Dollar For](https://dollarfor.org) first if you're not sure whether you qualify.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

[BILLING DEPARTMENT MANAGER / FINANCIAL COUNSELOR]
[PROVIDER NAME]
[PROVIDER MAILING ADDRESS]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: Request for hardship reduction and payment plan —
    Account #[ACCOUNT NUMBER]
    Patient: [PATIENT FULL NAME]
    Date(s) of service: [DATE OF SERVICE]
    Current balance: $[CURRENT BALANCE]

Dear Billing / Financial Counseling:

I am writing to request a hardship reduction and a manageable payment plan for the above-referenced account. I am committed to paying a fair amount for the services I received; however, the current balance exceeds what I am able to pay given my financial circumstances.

I. Request

I respectfully request:

1. A reduction of the current balance to a fair amount based on [the Medicare allowable rate / your published cash price / your charity-care policy / a combination thereof];
2. If applicable, a determination of my eligibility for your Financial Assistance Policy pursuant to 26 U.S.C. § 501(r) and 26 CFR § 1.501(r); and
3. A payment plan that I can sustain, with no interest, no fees, and no auto-debit requirement.

II. Financial circumstances

[The LLM renders one or more of the blocks below based on the patient's situation. Do not embellish; understate if anything.]

[BLOCK A — Income relative to federal poverty level]

My household consists of [N] persons. My household's gross annual income is approximately $[INCOME]. The federal poverty level for a household of [N] in 2026 is approximately $[FPL]. My income is approximately [N]% of the federal poverty level.

[BLOCK B — Existing medical-debt burden]

In addition to this account, I currently have $[TOTAL OTHER MEDICAL DEBT] in other medical debt across [N] other providers from the same time period. The cumulative balance exceeds my ability to pay without significant hardship.

[BLOCK C — Insurance gap]

[I was uninsured at the time of service / My insurance applied a deductible of $[AMOUNT] that I have not yet met / My insurance denied coverage and the appeal is pending / Other relevant insurance facts]. I am not seeking to avoid payment; I am asking for a fair price given that I am the one paying it.

[BLOCK D — Other circumstances]

[Briefly state any additional facts: job loss, divorce, disability, primary caregiver responsibilities, etc. One or two sentences; the goal is candor, not pity.]

[END BLOCKS]

III. Reference points for a fair amount

[The LLM renders these where data is available.]

- **Medicare allowable rate for the services in question:** approximately $[MEDICARE RATE]. (Source: CMS Physician Fee Schedule Lookup for the relevant CPT codes.)
- **Your hospital's published cash price under the federal Hospital Price Transparency Rule (45 CFR Part 180):** approximately $[CASH PRICE]. (Source: your machine-readable file, retrieved [DATE].)
- **Fair-market range for these services in this geographic area:** $[FAIR LOW] to $[FAIR HIGH]. (Source: [Turquoise Health / FAIR Health Consumer / etc.], retrieved [DATE].)

A fair patient-side amount falls between the Medicare rate and the cash price. I am prepared to pay $[PROPOSED AMOUNT] in full satisfaction of this account, payable [as a lump sum / on a payment plan of $[MONTHLY AMOUNT] per month for [N] months].

IV. Financial assistance policy

[Render this block only if the provider is a non-profit hospital. If unsure, render it; non-profit status is verifiable from the hospital's tax filings and patient-facing materials.]

As a non-profit hospital subject to 26 U.S.C. § 501(r), your facility maintains a Financial Assistance Policy and is required to:

1. Provide me a plain-language summary of the policy and an application before any payment is required;
2. Make reasonable efforts to determine my eligibility before any extraordinary collection action (lawsuits, wage garnishment, credit reporting, denying future care);
3. Charge me no more than amounts generally billed (AGB) to insured patients if I am FAP-eligible.

Please provide me with your Financial Assistance Policy summary and application. I will complete and return the application within 30 days of receipt.

V. Hold on collections during this discussion

I respectfully request that collection activity on this account be held during good-faith negotiation of this request. I will respond promptly to any reasonable counter-proposal.

VI. What I cannot do

For complete transparency: I cannot agree to a payment plan that includes auto-debit from a checking account or credit card on file. I am willing to send monthly payments by check or one-time-confirmed electronic transfer. I cannot agree to interest charges or late fees on a hardship plan. I cannot agree to a "settle in full or face collections" deadline that does not allow time for review of your FAP application.

I am genuinely committed to paying a fair amount and would prefer to resolve this directly rather than escalate. Please contact me at [PATIENT PHONE] or [PATIENT EMAIL] to discuss.

Sincerely,



[PATIENT FULL NAME]

Account number: [ACCOUNT NUMBER]
Date of service: [DATE OF SERVICE]

Enclosures: copy of bill; [if attaching: proof of income, household size, other supporting documentation]
```

---

## Placeholders and rendering notes

- The LLM renders only the financial-circumstances blocks that apply. Do not pad. If the patient does not want to disclose income, omit Block A and lead with Blocks C and D.
- `[PROPOSED AMOUNT]` should be set deliberately. A common starting offer is the Medicare allowable rate. A common closing position is the hospital's published cash price. Anywhere in between is defensible; below Medicare is aggressive and may need additional justification.
- The "what I cannot do" section is important. Many providers will respond with auto-debit-required payment plans; this letter pre-empts that.

## Before sending

The LLM should confirm with the patient:

1. The bill is actually correct (CPT codes verified, no No Surprises Act issue, no duplicate or services-not-received findings). If any of those apply, use `letter_initial_dispute.md` first or in parallel. Hardship is the wrong frame when the underlying bill is wrong.
2. The patient has run the Dollar For screener (or has decided independently they don't want to) — Dollar For will often file the FAP application on the patient's behalf and is faster than mailing this letter.
3. The patient has gathered the supporting documentation they will need if the hospital asks for income verification: pay stubs, prior tax return, household-size proof.

## Parallel actions

- Submit the Dollar For screener at [dollarfor.org](https://dollarfor.org).
- If the hospital is non-profit, find and download its FAP from the hospital's website; you'll need to mention it in the letter.
- Look up the Medicare allowable rate for the procedure codes on your bill via the CMS Physician Fee Schedule Lookup at [cms.gov/medicare/physician-fee-schedule/search](https://www.cms.gov/medicare/physician-fee-schedule/search).

## Follow-up

The LLM logs this with `action_type = "settlement_offered"` (because it's an offer to settle, even though framed as a negotiation request). `response_due_by` is 30 days from today by default. Track the offer amount in the action's `amount_disputed` field for negotiation history.
