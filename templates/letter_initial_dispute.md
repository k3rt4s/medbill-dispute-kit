# Template — Initial dispute letter

Use this after you have an itemized bill and have identified specific findings (price gouging, CPT mismatch, duplicate charges, services not received). Send via certified mail.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

[BILLING DEPARTMENT MANAGER]
[PROVIDER NAME]
[PROVIDER MAILING ADDRESS]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: Formal dispute of charges — Account #[ACCOUNT NUMBER]
    Patient: [PATIENT FULL NAME]
    Date(s) of service: [DATE OF SERVICE]
    Statement date: [STATEMENT DATE]
    Total currently billed: $[CURRENT BALANCE]
    Total disputed: $[TOTAL DISPUTED AMOUNT]

Dear Billing Department:

I am writing to formally dispute specific charges on the above-referenced account. I have reviewed the itemized statement and identified the following issues:

[For each finding, the LLM renders one of the blocks below. Number them sequentially.]

[BLOCK A — Price exceeds fair-market rate]

1. Line item: [CPT or service description]
   Charged: $[AMOUNT CHARGED]
   Fair-market rate for this CPT/HCPCS code in this geographic area: $[FAIR PRICE RANGE]
   Source: [Turquoise Health / FAIR Health Consumer / Healthcare Bluebook / hospital MRF — include URL or attached printout reference]
   Overcharge: $[CHARGED − FAIR HIGH]
   Position: The charged amount is approximately [N]× the fair-market range. Pursuant to Uniform Commercial Code § 2-305(2), a price to be fixed by the seller "means a price for him to fix in good faith." The current price does not appear to meet that standard. I propose a corrected charge of $[PROPOSED CORRECTED AMOUNT, typically the upper end of fair-market].

[BLOCK B — CPT severity coded too high]

2. Line item: CPT [CODE] — [description]
   Charged: $[AMOUNT CHARGED]
   Issue: CPT [CODE] requires [MDM complexity / time threshold] per the AMA's E/M documentation guidelines. The actual encounter on [date] involved [duration in minutes / problems addressed / decision-making complexity]. The appropriate code is [LOWER CODE]. The price difference attributable to incorrect coding is approximately $[OVERCHARGE].
   Position: Please recode to [LOWER CODE] and issue a corrected bill, or provide the clinical documentation that supports the higher-level code as currently billed.

[BLOCK C — Duplicate charge]

3. Line item: [description], appears [N] times on [date]
   Charged: $[AMOUNT × N]
   Issue: This appears to be a duplicate of [reference line]. The same service does not appear in the clinical record [N] times.
   Position: Please remove [N−1] of the [N] duplicate entries, reducing the charge by $[AMOUNT × (N−1)].

[BLOCK D — Service not received]

4. Line item: [description]
   Charged: $[AMOUNT]
   Issue: I have no record of receiving this service on [date]. My recollection of services received that day is: [summary].
   Position: Please remove this line item or provide contemporaneous clinical documentation that the service was rendered.

[BLOCK E — Improper bundling]

5. Line items: [description A, CPT X] and [description B, CPT Y]
   Charged: $[A] + $[B] = $[total]
   Issue: CMS National Correct Coding Initiative (NCCI) edits indicate that CPT [X] and CPT [Y] should not be billed together for the same date of service; one is included in the other. Source: CMS NCCI edits, current quarter.
   Position: Please remove the bundled component (CPT [Y or X]), reducing the charge by $[AMOUNT].

[END OF BLOCKS]

Summary of dispute:

Currently billed:           $[CURRENT BALANCE]
Total disputed (above):     $[TOTAL DISPUTED]
Proposed corrected total:   $[CURRENT BALANCE − TOTAL DISPUTED]

I am prepared to pay $[PROPOSED CORRECTED TOTAL] upon receipt of a corrected itemized statement reflecting these adjustments. I am not refusing to pay; I am declining to pay charges that are erroneous, mis-coded, or unjustifiably above market rates.

Legal references:

- Hospital Price Transparency Rule, 45 CFR Part 180 (chargemaster, cash price, and negotiated-rate disclosure)
- Uniform Commercial Code § 2-305(2) (open price term — price to be set in good faith)
- [As applicable: No Surprises Act, Public Law 116-260, Division BB, Title I]
- [As applicable: state itemization statute — e.g. Tennessee Code § 68-11-220]

Please send a corrected, itemized statement and a written response to the points above within fifteen (15) business days of the date of this letter. If I do not receive a substantive response by [DATE 15 BUSINESS DAYS FROM TODAY], I will escalate this matter through additional channels, which may include a formal complaint to the [STATE INSURANCE / HEALTH DEPARTMENT], a complaint to the Centers for Medicare and Medicaid Services if applicable, and other available remedies.

If you have any questions, please contact me at the phone number or email above.

Sincerely,



[PATIENT FULL NAME]

Account number: [ACCOUNT NUMBER]
Date of service: [DATE OF SERVICE]

Enclosures: copy of itemized statement; fair-market price evidence (printed/screenshotted with dates)
```

---

## Placeholders and rendering notes

- The LLM renders only the blocks that apply to this bill's findings. A bill with one price-gouging line and no other findings renders only Block A.
- `[TOTAL DISPUTED AMOUNT]` is the sum of overcharge amounts across all rendered blocks.
- `[PROPOSED CORRECTED TOTAL]` is `current_balance − total_disputed`.
- `[DATE 15 BUSINESS DAYS FROM TODAY]` is calendar arithmetic skipping Saturday/Sunday and federal holidays.
- State-specific citations are pulled from `references/laws_state_template.md`.

## When to use a different template

- If the bill is a balance bill that the No Surprises Act prohibits, use `letter_no_surprises_violation.md` instead. The NSA argument is stronger and stands on federal law.
- If this is an insurance denial, use `letter_insurance_appeal_erisa.md` instead. The audience is the plan administrator, not the provider's billing department.

## Follow-up

The LLM logs this action with `action_type = "initial_dispute_letter_sent"` and sets `response_due_by` to 15 business days from today.
