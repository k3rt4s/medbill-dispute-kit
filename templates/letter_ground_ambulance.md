# Template — Ground ambulance balance bill

Two distinct letters depending on whether the patient's state has a ground-ambulance balance-billing protection. The LLM picks based on `rules/10_ground_ambulance.md`.

If the state has a protection: use Variant A (state-law violation). Pattern matches the No Surprises Act letter — cite the specific state statute, demand reprocessing at in-network cost-sharing, CC the state insurance department.

If the state does not have a protection: use Variant B (fair-price negotiation). Pattern is general dispute under UCC § 2-305 and the Medicare ambulance fee schedule as the floor anchor.

---

## Variant A — State has a ground-ambulance protection

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

[BILLING DEPARTMENT MANAGER]
[AMBULANCE PROVIDER NAME]
[PROVIDER MAILING ADDRESS]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: Improper balance billing in violation of [STATE] law —
    Account #[ACCOUNT NUMBER]
    Patient: [PATIENT FULL NAME]
    Date of transport: [DATE OF SERVICE]
    Disputed balance billed: $[BALANCE]

Dear Billing Department:

The above-referenced charges balance-bill me for ground ambulance services in violation of [STATE STATUTE — e.g. O.C.G.A. § 33-20E-1 et seq. as amended by HB 286 effective January 1, 2024; or California Health & Safety Code § 1797.225; or other applicable state citation].

Facts:

On [DATE OF SERVICE], I received ground ambulance transport from [PROVIDER NAME] from [PICKUP LOCATION] to [DESTINATION]. My health plan, [PLAN NAME], is regulated by [STATE]. [STATE STATUTE] prohibits balance billing for ground ambulance services by an out-of-network provider where my plan covers the service. My cost-sharing must be calculated as if the service were provided in-network and applied toward my in-network deductible and out-of-pocket maximum.

[OPTIONAL — IF PLAN IS SELF-FUNDED ERISA, OMIT THIS LETTER ENTIRELY AND USE VARIANT B. The LLM should ask up-front whether the plan is self-funded.]

Required actions:

1. Adjust the balance on my account to reflect only in-network cost-sharing as required by [STATE STATUTE].
2. Confirm in writing within fifteen (15) business days that the balance has been corrected.
3. Cease any collection activity on the disputed balance during this dispute.

If my health plan has not yet paid you per the state's statutory formula (the greater of the negotiated rate, the usual and customary rate, or, for plans subject to the Georgia Surprise Billing Act, 180% of the Medicare rate, or your state's equivalent), please initiate the state's arbitration process directly with the plan. The patient is held harmless by the statute and is not a party to that arbitration.

I have filed a parallel complaint with [STATE INSURANCE DEPARTMENT NAME].

I am preserving all rights and remedies under federal and state law.

Sincerely,



[PATIENT FULL NAME]

Account number: [ACCOUNT NUMBER]
Date of service: [DATE OF SERVICE]

cc:
    [STATE INSURANCE DEPARTMENT NAME] — Consumer Services
    [INSURANCE PLAN NAME] — Member Services

Enclosure: copy of the bill; copy of the Explanation of Benefits from [INSURANCE PLAN NAME]
```

---

## Variant B — State has no ground-ambulance protection (or plan is ERISA self-funded)

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

[BILLING DEPARTMENT MANAGER]
[AMBULANCE PROVIDER NAME]
[PROVIDER MAILING ADDRESS]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: Dispute of ground ambulance charges —
    Account #[ACCOUNT NUMBER]
    Patient: [PATIENT FULL NAME]
    Date of transport: [DATE OF SERVICE]
    Currently billed: $[CURRENT BALANCE]
    Disputed amount: $[DISPUTED AMOUNT]

Dear Billing Department:

I am disputing the charges on the above-referenced account. The amount billed substantially exceeds the reasonable value of the services rendered. I am committed to paying a fair amount, but I cannot pay charges that are several multiples of the established Medicare reimbursement rate for the same transport.

I. Charges and reference points

Charge as billed: $[CHARGE]
Medicare allowable rate for the corresponding HCPCS code(s) [e.g. A0429, A0427, A0428] in this geographic locality: approximately $[MEDICARE RATE]
Source: CMS Ambulance Fee Schedule, [cms.gov/medicare/medicare-fee-for-service-payment/ambulancefeeschedule](https://www.cms.gov/medicare/medicare-fee-for-service-payment/ambulancefeeschedule), retrieved [DATE].

II. Insurance payment to date

My health plan, [PLAN NAME], has [paid $[AMOUNT] / denied / processed as out-of-network with $[AMOUNT] paid] toward this bill, leaving a patient balance of $[CURRENT BALANCE].

[OPTIONAL — IF DENIED, ADD: I am pursuing an internal appeal with my health plan; this letter concerns the provider-side balance independent of that appeal.]

III. Legal basis

Under Uniform Commercial Code § 2-305(2), an open-price term must be fixed by the seller in good faith. I did not receive an itemized price quote prior to transport — I could not have, given the emergency nature of the call — and your bill therefore reflects an open-price contract. The charged amount is approximately [N] times the Medicare allowable rate and is not, on its face, a reasonable price set in good faith. [STATE] further provides remedies under the [STATE UDAP STATUTE — e.g. Tennessee Consumer Protection Act, Tenn. Code Ann. § 47-18-104; Georgia Fair Business Practices Act, O.C.G.A. § 10-1-393].

IV. Proposed corrected amount

I propose a corrected balance of $[PROPOSED — typically 150% to 250% of Medicare] in full satisfaction of this account, payable [as a lump sum / on a payment plan of $[MONTHLY] per month for [N] months, with no interest or fees].

V. Request

1. Issue a corrected itemized statement reflecting the proposed amount within fifteen (15) business days.
2. If you disagree, provide a written explanation that addresses the gap between your charged amount and the Medicare allowable rate, with reference to actual costs incurred (fuel, labor, equipment depreciation, response-time targets) rather than chargemaster rates.
3. Cease collection activity during this dispute.

If you are a municipal or county-operated ambulance service, please also provide your financial-assistance policy and application; I would like to be considered for any applicable hardship reduction.

Sincerely,



[PATIENT FULL NAME]

Account number: [ACCOUNT NUMBER]
Date of service: [DATE OF SERVICE]

cc:
    [STATE INSURANCE DEPARTMENT NAME] — Consumer Services (where applicable)
    [STATE ATTORNEY GENERAL] — Consumer Protection Division

Enclosure: copy of the bill; copy of the Explanation of Benefits; CMS Ambulance Fee Schedule lookup printout
```

---

## Placeholders and rendering notes

- The LLM picks Variant A or B based on the answers to two questions: (1) is the patient's state on the list in `rules/10_ground_ambulance.md`? (2) is the patient's plan self-funded ERISA? If yes to (1) and no to (2), Variant A. Otherwise Variant B.
- HCPCS ambulance codes the LLM should know: A0425 (ground mileage), A0426 (ALS routine), A0427 (ALS emergency), A0428 (BLS routine), A0429 (BLS emergency), A0433 (ALS Level 2), A0434 (specialty care transport). Look up the Medicare rate for the specific code(s) on the bill.
- The 150-250% of Medicare range is a defensible negotiation anchor for unprotected states. Below 150% is aggressive; above 250% concedes too much.

## Parallel actions

- **If state-protected (Variant A):** File a state insurance department complaint the same day. State pressure produces the fastest results.
- **If unprotected (Variant B):** Search for the patient's ambulance subscription / hardship program before sending the letter. Many municipal services will simply waive the balance for low-income residents if asked.
- **For both:** If the patient's health plan denied or under-paid, file an appeal using `templates/letter_insurance_appeal_erisa.md` (ERISA) or the non-ERISA equivalent. The provider-side dispute and the insurer-side appeal run in parallel.

## Follow-up

The LLM logs Variant A with `action_type = "no_surprises_letter_sent"` (closest match; a future schema revision should add `state_balance_billing_letter_sent`). Variant B is logged as `initial_dispute_letter_sent`. Either variant gets `response_due_by` set to 15 business days from today.
