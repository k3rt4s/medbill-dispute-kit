# Rule 11, Patient-Provider Dispute Resolution (PPDR) walkthrough

For uninsured and self-pay patients whose final bill exceeds the Good Faith Estimate (GFE) they were entitled to receive. PPDR is the federal dispute resolution process created by the No Surprises Act. It is **portal-driven**, not letter-driven, so this is a rule with a checklist, not a template.

The kit treats PPDR as a separate track from other disputes because the protections that attach during PPDR (no collections, no late fees, no credit reporting) are uniquely valuable, and because the filing is on a strict 120-day clock.

> **NSA figures re-verified against CMS as of 2026-09-07:** [CMS’s PPDR intake page](https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/dispute-medical-bill) is the source for current patient-facing PPDR eligibility and fee information.

## The rule

If the patient meets all four of these conditions, file PPDR:

1. The patient was **uninsured or self-pay** for the service in question.
2. The patient **received a Good Faith Estimate** from the provider or facility.
3. One provider or facility charged at least **$400 more** than its Good Faith Estimate.
4. The patient has an **initial bill dated within the last 120 calendar days**.

If the patient is uninsured or self-pay and never received a GFE, that is itself a No Surprises Act issue. File a complaint at the No Surprises Help Desk (1-800-985-3059); do not treat a missing GFE as satisfying CMS’s PPDR intake requirement.

## Why this is high-leverage

While a PPDR is pending:

- **The bill cannot be sent to collections.**
- **The bill cannot accrue late fees.**
- **The bill cannot be reported to consumer reporting agencies.**

These protections are written into 45 CFR § 149.620 and apply for the duration of the dispute. Filing PPDR stops the collections clock on a self-pay bill more effectively than any other federal action.

The filing fee is **$25** and nonrefundable. If the dispute is decided in the patient's favor, CMS says the $25 is deducted from the amount owed to the provider.

## Where the process lives

- **Federal IDR portal:** [nsa-idr.cms.gov](https://nsa-idr.cms.gov), this is the same portal used for provider-payer IDR; PPDR is a separate workflow within it.
- **CMS PPDR page:** [cms.gov/nosurprises/providers-payment-resolution-with-patients](https://www.cms.gov/nosurprises/providers-payment-resolution-with-patients), explains the process from the provider's perspective; relevant context for what the SDR entity is looking at.
- **CMS PPDR overview for patients:** [cms.gov/medical-bill-rights](https://www.cms.gov/medical-bill-rights), patient-facing summary.

## Checklist, what the patient needs before filing

The LLM walks the patient through this checklist. Each item should be collected, scanned, and named for upload.

### 1. The Good Faith Estimate (if one was provided)

If the patient received a GFE, usually delivered before scheduled service or, for self-pay scheduled services, automatically, locate it. Common forms:

- A document titled "Good Faith Estimate," "GFE," or "estimate of charges"
- A printed estimate from the provider's patient portal
- An email or PDF attachment

The GFE shows the estimated total and lists each item or service with its associated estimated charge.

If the patient cannot find a GFE: did they get one, did the provider not send one, or was it discarded? CMS’s current intake page requires a GFE. Where no GFE was received, use the federal No Surprises Help Desk complaint path rather than claiming PPDR eligibility.

### 2. The final bill

The bill that exceeds the GFE. PPDR is filed against a **single provider's bill** at a time. If the patient has bills from multiple providers (the hospital, the radiologist, the pathologist), each requires its own PPDR filing.

### 3. Evidence of self-pay or uninsured status

PPDR is for uninsured or self-pay patients. Self-pay means the patient chose not to submit the claim through insurance for this service, even if they have insurance. If the patient submitted to insurance and the claim was processed, PPDR is not available, the dispute path is internal appeal to the plan instead.

### 4. The $400 threshold per provider

Verify the math: final bill minus GFE estimate for that same provider equals at least $400. Hospital bills often have separate line items from separately-billed providers (anesthesia, radiology, pathology); each provider's $400 threshold is calculated separately against that provider's GFE line.

### 5. Date the bill was received

CMS’s current intake page requires an **initial bill dated within the last 120 calendar days**. Preserve the initial bill and its date for the submission.

### 6. $25 filing fee

Pay at the portal. The fee is nonrefundable; if the dispute is decided in the patient's favor, CMS says it is deducted from the amount owed to the provider.

## How PPDR works after filing

The compressed sequence:

1. **Patient files at the federal IDR portal**, attaching the GFE (if any), the final bill, and basic identifying information.
2. **CMS selects an SDR entity** (a third-party arbitrator certified by HHS). Patient and provider receive notice.
3. **Provider has 10 business days** to submit their evidence: original GFE, justification for the billed amount, supporting documentation.
4. **Patient may submit additional evidence** in response.
5. **SDR entity reviews and issues a decision**, typically within 30 days of receiving both parties' submissions. The SDR's determination of the appropriate amount is **binding** on the provider.
6. **Provider must adjust the bill** to the SDR-determined amount within 30 days of the decision.
7. **If SDR rules below the billed amount:** CMS says the $25 fee is deducted from the amount owed to the provider. Patient owes the resulting amount under the determination.
8. **If SDR rules at the billed amount:** patient owes the billed amount, but the collections-pause and credit-report protections that applied during the dispute are now lifted.

## What evidence the patient should submit

Beyond the basic filing, the SDR entity will weigh:

1. **The provider's own published cash price** (from the hospital's Hospital Price Transparency machine-readable file, if applicable, see [`templates/complaint_cms_hpt.md`](../templates/complaint_cms_hpt.md) for how to compel one).
2. **Reasonable fair-market data** for the CPT codes in question (Turquoise Health, FAIR Health Consumer; see [`references/resources.md`](../references/resources.md)).
3. **Medicare allowable rates** for the same CPT codes (CMS Physician Fee Schedule Lookup).
4. **The GFE itself** as the patient's reasonable expectation.
5. **Any clinical-necessity context**, if the bill includes services beyond what was on the GFE because of an intra-procedure decision, the patient should not be liable for those add-ons absent the patient's informed consent to a new GFE.

## When PPDR is the wrong tool

- **The patient has insurance and used it.** PPDR is for self-pay. Use internal-appeal templates instead.
- **The disputed amount is below $400 above the GFE.** PPDR doesn't apply; use general dispute templates.
- **The 120-day clock has run.** Same; use general dispute templates and consider whether the underlying issue is also a GFE-failure-to-provide complaint to CMS.
- **The dispute is about a service not on the GFE at all.** If the bill includes a service the patient didn't consent to and that wasn't on the GFE, that's a services-not-received finding and a separate dispute under `letter_initial_dispute.md`.

## Parallel actions

- **CMS complaint** if the GFE was deficient or missing: 1-800-985-3059, or [cms.gov/medical-bill-rights/help/submit-a-complaint](https://www.cms.gov/medical-bill-rights/help/submit-a-complaint). Failure to provide a GFE is its own NSA violation independent of the PPDR process.
- **State insurance department**: for fully-insured plans where the patient is also pursuing an internal appeal, the state complaint creates parallel pressure.
- **Hospital Price Transparency complaint**: if the hospital's MRF is non-compliant, file the parallel CMS HPT complaint. Use the MRF to anchor the patient's PPDR submission.

## Follow-up

The LLM logs the filing with `action_type = "ppdr_filed"`. Set `response_due_by` to 60 days from filing (typical end-to-end PPDR resolution timeline). Note in `notes` field that collections-pause and credit-protection apply during the pendency. If the patient receives any collections contact during pendency, that contact itself violates federal law, log a separate finding and file an immediate complaint with the No Surprises Help Desk.

## Related rules

- [[01_never_pay_first]], the general principle PPDR enforces for self-pay patients
- [[04_no_surprises_act]], PPDR's parent framework
- [[09_pricing_resources]], the price data that anchors the patient's PPDR submission
