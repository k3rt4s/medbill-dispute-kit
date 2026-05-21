# Template — Good Faith Estimate request (uninsured / self-pay)

Use when the patient is uninsured or self-pay and a scheduled service is at least three business days away, or when a bill has arrived for a self-pay service for which no GFE was offered. The federal No Surprises Act, at 45 CFR § 149.610, requires providers and facilities to furnish a written Good Faith Estimate of expected charges to any uninsured or self-pay individual who schedules a service at least three business days in advance, and to make a GFE available on request for any service the individual is shopping for.

If a final bill exceeds the GFE by $400 or more, the patient can initiate the federal Patient-Provider Dispute Resolution process under 45 CFR § 149.620 (see `templates/letter_ppdr_initiate.md`).

Use this template in two modes:

- Pre-service: request the GFE before the scheduled service.
- Post-bill: demand the GFE that should have been issued, as a precondition to validating the bill that arrived.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

[SCHEDULING / BILLING DEPARTMENT]
[PROVIDER OR FACILITY NAME]
[PROVIDER MAILING ADDRESS]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: Request for Good Faith Estimate under 45 CFR § 149.610 —
    Patient: [PATIENT FULL NAME]
    DOB: [DOB]
    Insurance status: [Uninsured / Self-pay — not submitting this claim to my health plan]
    Scheduled service (pre-service mode): [SERVICE DESCRIPTION], scheduled [SCHEDULED DATE]
    Billed service (post-bill mode): account # [ACCOUNT NUMBER], date of service [DATE OF SERVICE]

To Scheduling / Billing:

I am [scheduled to receive / received] the service identified above as an uninsured / self-pay patient. Pursuant to the federal No Surprises Act at 45 CFR § 149.610 and the related CMS guidance issued December 21, 2021 and updated thereafter, I am writing to request a written Good Faith Estimate (GFE) of expected charges.

I. Authority

The No Surprises Act requires every health care provider and health care facility to provide a written Good Faith Estimate of expected charges to any uninsured or self-pay individual who:

(a) schedules a service at least three (3) business days in advance, or
(b) requests a GFE while shopping for or considering a service, or
(c) is in any post-service dispute over a bill that should have included a co-provider GFE under § 149.610(c)(2).

The GFE must be issued no later than:

- one (1) business day after scheduling, for services scheduled three (3) to nine (9) business days in advance;
- three (3) business days after scheduling, for services scheduled ten (10) or more business days in advance;
- three (3) business days after a request, for services not yet scheduled.

II. Required content of the GFE (per 45 CFR § 149.610(c)(1))

The Good Faith Estimate must, at a minimum, include each of the following:

1. Patient name and date of birth.
2. Description in plain language of the primary item or service expected to be furnished.
3. Itemized list of items or services reasonably expected to be furnished as part of the primary item or service, including any items or services to be furnished by co-providers or co-facilities that are reasonably expected to be furnished in conjunction with the primary item or service.
4. Applicable diagnosis codes, expected service codes (CPT/HCPCS), and expected charges associated with each item or service.
5. Name, National Provider Identifier (NPI), and Tax Identification Number (TIN) of each provider or facility represented in the estimate, and the state(s) and office or facility location(s) where the items or services are expected to be furnished.
6. List of items or services that the convening provider or convening facility anticipates will require separate scheduling and that are expected to occur before or following the expected period of care for the primary item or service.
7. Disclaimer that the GFE is only an estimate and that actual items, services, or charges may differ.
8. Disclaimer that the patient has the right to initiate a Patient-Provider Dispute Resolution if the actual billed charges are substantially in excess of the expected charges in the GFE.
9. Disclaimer that the GFE is not a contract and does not require the patient to obtain the items or services from any of the providers or facilities identified in the GFE.

III. Specific request

Please provide the Good Faith Estimate in writing to the mailing address above, by [DEADLINE — set to the applicable statutory deadline above; if uncertain, set to 7 calendar days from this letter's postmark].

For clarity, "self-pay" in this context means I am not requesting that the claim be submitted to my health plan. If I have insurance, I am exercising the No Surprises Act's self-pay election to bypass insurance for this service.

[Render IV if this is post-bill mode.]

IV. Post-bill consequence

If you cannot produce a GFE for the date of service above because no GFE was issued at the time scheduling required one, that fact is itself a violation of 45 CFR § 149.610 and is properly reported to the federal No Surprises Help Desk and to [STATE]'s Department of Insurance. In that event, my position is that the bill referenced above is not enforceable as billed and must be re-issued at no more than the amount that would have been disclosed in a compliant GFE. I will pay only the GFE amount, computed from your facility's published cash-pay prices under 45 CFR Part 180 (the Hospital Price Transparency Rule) for the codes billed.

V. Disclaimer awareness

I am aware that the GFE is an estimate and that actual charges may differ. I also know my right under 45 CFR § 149.620 to initiate the Patient-Provider Dispute Resolution process if the final billed amount exceeds the GFE by $400 or more for any single provider or facility on the GFE. I expect the disclaimers required by § 149.610(c)(1) to be included in the written GFE.

Please direct your response to the address above.

Sincerely,



[PATIENT FULL NAME]

DOB: [DOB]
Account number (post-bill mode): [ACCOUNT NUMBER]
Scheduled date (pre-service mode): [SCHEDULED DATE]

Enclosures:
- (Pre-service mode) Copy of the scheduling confirmation
- (Post-bill mode) Copy of the bill referenced above
```

---

## Placeholders and rendering notes

- The drafter selects pre-service vs post-bill mode based on whether `dispute_letter_sent_date` or a billed `dos_start` is present in `tracker.csv`. Pre-service is rare in this kit's workflow (most bills arrive after the fact); post-bill is the common case.
- "Self-pay" includes patients who are insured but elect not to submit a particular claim to their plan. The right to do this is preserved by § 149.610(c)(3); the patient does not have to be uninsured to use the GFE/PPDR process.
- This template is patient-only-facing. There is no parallel CC to the insurer because, by definition, the patient has elected self-pay for this service.

## Parallel actions

1. Mail this letter certified to the provider's scheduling or billing department.
2. If the provider has an online patient portal, send a duplicate message there. Some providers' GFE workflow is portal-only.
3. Log the action with `action_type = "received_bill"` superseded by a new action `gfe_requested` (custom — kit users can add to schemas/action.toml if not present).

## Follow-up

- If the provider issues a compliant GFE: keep it. If the final bill exceeds the GFE by $400+, draft `templates/letter_ppdr_initiate.md`.
- If the provider refuses or fails to issue a GFE within the statutory window: file a complaint with the No Surprises Help Desk at 1-800-985-3059 or cms.gov/nosurprises and update `tracker.csv` with `next_action = file_cms_complaint`.
- If the bill arrived without a GFE and the provider claims no GFE was required: ask in writing for the basis (was the patient not classified as self-pay? was the service not "scheduled" within the rule? was there a co-provider gap?). Document the answer; it may itself be a NSA finding for the dispute letter.
