# Template — Request for itemized bill

Use this letter as the first action against any non-itemized bill. Send via certified mail with return receipt. The state-statute citation defaults to Tennessee; swap for the patient's state using `references/laws_state_template.md`.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE — today, full month/day/year]

[BILLING DEPARTMENT MANAGER]
[PROVIDER NAME]
[PROVIDER MAILING ADDRESS]
[CITY, STATE ZIP]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: Request for itemized statement — Account #[ACCOUNT NUMBER]
    Patient: [PATIENT FULL NAME]
    Date(s) of service: [DATE OF SERVICE]

Dear Billing Department:

Pursuant to [APPLICABLE STATE STATUTE — e.g. Tennessee Code Annotated § 68-11-220], I am formally requesting a complete itemized statement of services and charges for the above-referenced account.

Please provide all of the following:

1. A complete itemized statement showing each service, supply, and medication, the date and time it was provided, the units billed, and the unit charge.
2. The CPT or HCPCS code and revenue code for each line item.
3. A plain-English description of each CPT/HCPCS code.
4. The name and National Provider Identifier (NPI) of the provider rendering each service.
5. The Explanation of Benefits (EOB) from my insurance company corresponding to this account, if insurance was billed.
6. The hospital chargemaster price, the cash price, and the negotiated rate that was applied for each line item, as required to be publicly available under the federal Hospital Price Transparency Rule (45 CFR Part 180).

[APPLICABLE STATE STATUTE] requires that this information be provided within thirty (30) days of receipt of a written request made within one year of discharge. Please send the itemized statement to the address above by [DATE 30 DAYS FROM TODAY].

I am preserving all legal rights, including the right to dispute charges, the right to request external review, and any rights I may have under the No Surprises Act and the Employee Retirement Income Security Act of 1974 (ERISA), as applicable to my plan.

If you have any questions about this request, please contact me at the phone number or email above.

Sincerely,



[PATIENT FULL NAME]

Account number: [ACCOUNT NUMBER]
Date of service: [DATE OF SERVICE]
```

---

## Placeholders the LLM must fill

- `[PATIENT FULL NAME]`, `[STREET ADDRESS]`, `[CITY, STATE ZIP]`, `[PATIENT PHONE]`, `[PATIENT EMAIL]` — from the patient's contact information
- `[DATE]` — today's date, formatted "Month D, YYYY"
- `[BILLING DEPARTMENT MANAGER]` — if unknown, use "Billing Department Manager"
- `[PROVIDER NAME]`, `[PROVIDER MAILING ADDRESS]`, `[CITY, STATE ZIP]` — from the bill
- `[CERTIFIED MAIL TRACKING NUMBER]` — the patient obtains this at the post office when they mail it; the LLM should leave it as `[NEEDS USER INPUT: certified mail tracking #]` until the patient provides it after mailing
- `[ACCOUNT NUMBER]` — from the bill
- `[PATIENT FULL NAME]` (subject line and signature) — same as header
- `[DATE OF SERVICE]` — from the bill
- `[APPLICABLE STATE STATUTE]` — Tennessee Code Annotated § 68-11-220 by default; for other states the LLM looks this up using `references/laws_state_template.md` and warns the patient to verify before mailing
- `[DATE 30 DAYS FROM TODAY]` — calendar arithmetic from today's date

## Variations

- If the patient is uninsured/self-pay, add to item 5: "I am uninsured/self-pay and was not provided a Good Faith Estimate pursuant to the No Surprises Act, 45 CFR § 149.610. Please provide the Good Faith Estimate that should have been provided, if any was prepared."
- If the patient suspects this is a hospital encounter with multiple separate billers, add a note at the bottom: "I understand that other professional fees (physicians, anesthesiologists, radiologists, pathologists, laboratories) for this encounter may be billed separately. Please confirm which services are within the scope of this account and which were billed under separate accounts."

## Follow-up

The LLM should log this action against the bill (`action.toml` with `action_type = "requested_itemization"`) and set the bill's `next_action_due` to 30 days from today.
