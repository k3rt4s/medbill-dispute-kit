# Template — Initiate Patient-Provider Dispute Resolution (PPDR)

Use when the patient is uninsured or self-pay, received a Good Faith Estimate before the service (or should have under 45 CFR § 149.610), and the final bill for any single provider or facility exceeds that provider's or facility's GFE by $400 or more. The federal No Surprises Act at 45 CFR § 149.620 establishes the Patient-Provider Dispute Resolution process, administered by certified Selected Dispute Resolution Entities (SDREs) under CMS oversight.

The patient files PPDR directly with CMS, not with the provider. The provider then has 10 business days to submit its own information; the SDRE issues a binding determination within 30 business days of selection. The patient's filing fee is $25 (waived for hardship).

This template generates the **content** of the PPDR submission. The patient files via the CMS portal at https://nsa-idr.cms.gov/consumer/. The portal accepts uploaded attachments; this letter goes in as the "narrative" attachment and supports the structured form fields.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]
Date of birth: [DOB]

[DATE]

CENTERS FOR MEDICARE AND MEDICAID SERVICES
Patient-Provider Dispute Resolution Program
[Filed via the federal IDR portal at https://nsa-idr.cms.gov/consumer/]

RE: Patient-Provider Dispute Resolution initiation under 45 CFR § 149.620 —
    Patient: [PATIENT FULL NAME]
    DOB: [DOB]
    Provider or facility in dispute: [PROVIDER OR FACILITY NAME]
    Provider NPI: [NPI]
    Provider TIN: [TIN]
    Date(s) of service: [DATE OF SERVICE RANGE]
    GFE amount for this provider/facility: $[GFE AMOUNT]
    Final billed amount for this provider/facility: $[BILLED AMOUNT]
    Spread: $[SPREAD = BILLED − GFE]

To the Patient-Provider Dispute Resolution Program:

I am the uninsured / self-pay individual identified above. I am initiating Patient-Provider Dispute Resolution under 45 CFR § 149.620 because the final billed amount for the provider or facility identified above is at least $400 greater than the Good Faith Estimate that provider or facility issued (or was required to issue) under 45 CFR § 149.610.

I. Eligibility (each element is met)

1. I was an uninsured / self-pay individual at the time of the scheduled service. [The drafter selects: I had no health coverage / I had coverage but elected self-pay under § 149.610(c)(3) for this service.]

2. The service was furnished by [PROVIDER OR FACILITY NAME] on [DATE OF SERVICE]. The bill identifying this service is account number [ACCOUNT NUMBER]. A copy of the bill is attached as Exhibit A.

3. I received a written Good Faith Estimate from [PROVIDER OR FACILITY NAME] dated [GFE DATE] showing an expected charge of $[GFE AMOUNT] for the items and services identified on the GFE. A copy of the GFE is attached as Exhibit B. [Or, the drafter renders: I did not receive a Good Faith Estimate. The provider was obligated to issue one under 45 CFR § 149.610 because [the service was scheduled at least three business days in advance / I requested a GFE on [DATE] for a service I was considering]. My position is that the GFE amount for purposes of this PPDR is $0, because no GFE was issued; in the alternative, the GFE amount should be deemed equal to the provider's published cash price under 45 CFR Part 180 for the codes billed, which is $[CASH PRICE]. The dispute spread under either framing exceeds $400.]

4. The final bill from this provider or facility is $[BILLED AMOUNT], which exceeds the GFE amount by $[SPREAD]. The spread of $[SPREAD] is $400 or more, satisfying the threshold in § 149.620(b)(1)(ii).

5. This PPDR is being initiated within 120 calendar days of receipt of the bill (§ 149.620(b)(2)). I received the bill on [BILL RECEIPT DATE]; today is calendar day [N] from receipt.

II. Items / services and code-level comparison

The following table compares the codes on the Good Faith Estimate against the codes on the final bill. Items present on the GFE are matched to billed items; items billed but not on the GFE are flagged separately as ineligible for charge under the rule (§ 149.620(a)(2)(ii) — items not on the GFE cannot exceed the GFE amount, period).

[The drafter renders this table from the GFE itself and from `Billers/<slug>/_benchmarks.csv` for the billed side.]

| CPT/HCPCS | Description   | On GFE?        | GFE amount  | Billed amount  | Delta          |
| --------- | ------------- | -------------: | ----------: | -------------: | -------------: |
| [CODE]    | [DESCRIPTION] | Y              | $[GFE LINE] | $[BILLED LINE] | $[DELTA]       |
| [CODE]    | [DESCRIPTION] | Y              | $[GFE LINE] | $[BILLED LINE] | $[DELTA]       |
| [CODE]    | [DESCRIPTION] | N (not on GFE) | $0.00       | $[BILLED LINE] | $[BILLED LINE] |

III. Relief requested

Pursuant to 45 CFR § 149.620(f), I respectfully request that the Selected Dispute Resolution Entity:

1. Review the GFE, the final bill, and the supporting evidence attached.

2. Issue a determination under the rule that:

(a) For items on the GFE, the amount I owe is no more than the GFE amount as adjusted by any allowable factor under § 149.620(f)(3) (a higher amount may be allowed only if the provider demonstrates that the difference reflects medically necessary items or services not reflected in the GFE, that the higher amount reflects an item or service to which the patient consented in writing in advance, or that the higher amount is consistent with the median payment amount of the SDRE's qualifying payment amounts);

(b) For items billed but not on the GFE, the amount I owe is zero, because the rule prohibits the provider from charging more than the GFE amount for items not on the GFE; and

(c) The patient cost is reduced from $[BILLED AMOUNT] to $[GFE AMOUNT or applicable lower amount].

3. Order the provider or facility to issue a corrected bill consistent with the determination within fifteen (15) business days, to withdraw any prior collection activity, and to provide written confirmation of paid-in-full status upon my payment of the adjusted amount.

IV. Status of any payments made

[Render whichever applies.]

I have not made any payment toward this bill.

[OR]

I have made the following payment(s) toward this bill, which I expect to be credited against the adjusted amount: $[AMOUNT PAID] on [DATE]; receipt attached as Exhibit C.

V. Pendency of collection

[Render whichever applies.]

The provider has not yet referred this account to collections.

[OR]

The provider has referred this account to [COLLECTION AGENCY] on [DATE]. Under the rule, the provider is required to cease collection activity (and to instruct any third-party collector to cease) while this PPDR is pending. The provider was notified on [DATE] of this PPDR; a copy of that notice is attached.

VI. Authorization and certification

I authorize the SDRE and CMS to obtain and review any information from the provider or facility necessary to resolve this dispute.

I declare under penalty of perjury under the laws of the United States that the foregoing is true and correct.

Executed on [DATE] at [CITY], [STATE].



[PATIENT FULL NAME]

DOB: [DOB]
Address: [STREET ADDRESS, CITY, STATE ZIP]

Exhibits attached / uploaded:
A — Final bill from [PROVIDER OR FACILITY NAME], account [ACCOUNT NUMBER], dated [STATEMENT DATE]
B — Good Faith Estimate dated [GFE DATE] (or evidence that no GFE was issued)
C — Receipt(s) for any payment(s) already made, if applicable
D — Copy of notice to provider of PPDR initiation (recommended courtesy)
E — Provider's machine-readable file excerpt under 45 CFR Part 180 for the codes billed, if applicable
F — Line-item benchmark analysis (Medicare PFS rates for context)
G — Filing-fee receipt or hardship-fee-waiver request
```

---

## Placeholders and rendering notes

- `[PROVIDER OR FACILITY NAME]` — PPDR is per-provider. If a patient received bills from a hospital, an ER physician, a radiologist, and an anesthesiologist for the same encounter, each one that exceeds its own GFE by $400+ requires its own PPDR submission. The drafter generates one letter per qualifying biller and queues them.
- `[GFE AMOUNT]` and `[BILLED AMOUNT]` — both must be on a per-provider, per-facility basis. Multi-provider GFEs (where one "convening provider" assembles a combined GFE including co-providers) still measure the $400 threshold per individual provider line within the GFE, not against the combined total.
- The structured form fields in the CMS portal will ask for the same data; this letter fills the narrative-attachment slot.
- The $25 filing fee can be waived. The drafter should suggest the hardship waiver if `tracker.csv` already shows an active financial-assistance application or if the patient flags hardship in `notes`.

## Parallel actions (same day as filing)

1. Submit the PPDR via the CMS portal at https://nsa-idr.cms.gov/consumer/.
2. Notify the provider in writing (certified mail) that PPDR has been initiated, so the provider's obligation to cease collection takes effect immediately. The CMS portal does not, on its own, notify the provider for several business days.
3. Log the action in `tracker.csv` with `action_type = ppdr_filed`.

## Follow-up

- The SDRE acknowledges receipt within 3 business days.
- The provider has 10 business days from selection to submit its position.
- The SDRE issues a binding determination within 30 business days of selection.
- If the patient prevails, the provider must issue a corrected bill within 15 business days.
- The determination is binding; neither party may relitigate in court except on narrow APA-style grounds.

## When PPDR is not the right tool

- Insured-and-claim-submitted services use the standard EOB / appeal path, not PPDR.
- Services covered by the federal No Surprises Act's balance-billing protections (emergency, OON ancillary at IN facility, OON air ambulance) use the NSA dispute path against the insurer, not PPDR.
- Services where the spread is under $400 use ordinary dispute / negotiation, not PPDR.
