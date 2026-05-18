# Template — No Surprises Act violation

Use when a bill appears to violate the federal No Surprises Act. This template is **not** a general dispute letter; the legal basis is narrow and specific, and the audience includes both the provider and the federal regulator. Always pair with a parallel complaint at 1-800-985-3059 or [cms.gov/medical-bill-rights/help/submit-a-complaint](https://www.cms.gov/medical-bill-rights/help/submit-a-complaint).

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

RE: Improper balance billing in violation of the No Surprises Act —
    Account #[ACCOUNT NUMBER]
    Patient: [PATIENT FULL NAME]
    Date(s) of service: [DATE OF SERVICE]
    Disputed amount: $[BALANCE BILLED AMOUNT]

Dear Billing Department:

I am writing to notify you that the above-referenced charges appear to violate the federal No Surprises Act (Public Law 116-260, Division BB, Title I), implemented at 45 CFR Part 149 and effective January 1, 2022.

Facts:

[Pick the applicable scenario below; the LLM renders only the one that applies.]

[SCENARIO 1 — Emergency services]

The services on [DATE OF SERVICE] were emergency services rendered at [FACILITY NAME]. Section 2799A-1 of the Public Health Service Act prohibits balance billing for emergency services provided by an out-of-network provider or at an out-of-network facility. Cost-sharing must be calculated as if the services were provided in-network, and the provider may not charge the patient more than the in-network cost-sharing amount.

[SCENARIO 2 — Out-of-network ancillary at in-network facility]

The services on [DATE OF SERVICE] were rendered by an out-of-network [anesthesiology / radiology / pathology / laboratory / assistant surgeon / hospitalist / intensivist / neonatology] provider at [IN-NETWORK FACILITY NAME], which is in-network under my health plan, [PLAN NAME]. Section 2799A-1 of the Public Health Service Act prohibits balance billing in these circumstances; I am liable only for in-network cost-sharing.

[SCENARIO 3 — Air ambulance]

The services on [DATE OF SERVICE] were out-of-network air ambulance services. Section 2799B-5 of the Public Health Service Act prohibits balance billing for out-of-network air ambulance services; cost-sharing must be calculated as in-network.

[SCENARIO 4 — Self-pay/uninsured, no Good Faith Estimate]

I was uninsured/self-pay at the time of the scheduled services on [DATE OF SERVICE]. The No Surprises Act, 45 CFR § 149.610, required that I be provided a Good Faith Estimate at least one business day before the scheduled service. No such Good Faith Estimate was provided. The bill received exceeds any estimate by $400 or more.

I am initiating the Patient-Provider Dispute Resolution process under 45 CFR § 149.620 at the federal IDR portal at https://nsa-idr.cms.gov. Pursuant to that process, this bill may not be sent to collections, may not accrue late fees, and may not be reported to consumer reporting agencies while the dispute is pending.

[END SCENARIOS]

Required actions:

1. Reprocess this account so that any patient cost-sharing reflects in-network amounts only (or, for the self-pay scenario, abide by the outcome of the federal PPDR process).
2. Confirm in writing within fifteen (15) business days that the balance has been adjusted to comply with the No Surprises Act, or provide written explanation of why you contend the Act does not apply.
3. Cease any collection activity on the disputed balance during this dispute, consistent with federal protections.

I have filed a parallel complaint with the federal No Surprises Help Desk (1-800-985-3059) and the federal complaint portal at https://www.cms.gov/medical-bill-rights/help/submit-a-complaint. I have also filed a complaint with the [STATE INSURANCE DEPARTMENT].

The No Surprises Act authorizes civil monetary penalties of up to $10,000 per violation. I am preserving all rights and remedies, federal and state.

Sincerely,



[PATIENT FULL NAME]

Account number: [ACCOUNT NUMBER]
Date of service: [DATE OF SERVICE]

cc:
    Centers for Medicare and Medicaid Services — No Surprises Help Desk
    [STATE INSURANCE DEPARTMENT NAME] — Consumer Insurance Services
    [INSURANCE PLAN NAME] — Member Services (where applicable)

Enclosures: copy of bill; copy of Explanation of Benefits (if any); copy of Good Faith Estimate (if any was provided)
```

---

## Placeholders and rendering notes

- The LLM renders only the scenario block that applies.
- If the bill spans services that fall into multiple categories (e.g. emergency services and an out-of-network ancillary on a subsequent admission), the LLM may render multiple scenarios but should clearly label each.
- For ground-ambulance balance bills, **do not use this template**. Ground ambulance is excluded from the federal No Surprises Act. Check state law via `references/laws_state_template.md`; if no state protection applies, fall back to `letter_initial_dispute.md` arguing UCC § 2-305 and state law.

## Parallel actions to take same day

1. **Federal CMS complaint:** call 1-800-985-3059 or submit at the federal portal. Save the confirmation number.
2. **State insurance department complaint:** submit at the patient's state portal.
3. **Insurance company notice:** call your insurance company and tell them you believe this is a balance-billing violation under the NSA; ask them to reprocess at in-network cost-sharing.

## Follow-up

The LLM logs this with `action_type = "no_surprises_letter_sent"` and creates parallel `cms_complaint_filed` and `state_doi_complaint_filed` action entries the same day. `response_due_by` is 15 business days from today.
