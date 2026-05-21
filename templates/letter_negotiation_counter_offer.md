# Template — Negotiated counter-offer with benchmarked pricing

Use when the bill is for services the patient actually received, the EOB and itemization are both in hand, and the line-item charges are materially above fair market value. This is Marshall Allen's "I'll pay what's fair, not what you wrote down" play, anchored in UCC § 2-305(2) (open price term must be fixed in good faith), the federal Hospital Price Transparency Rule (45 CFR Part 180), and the Medicare Physician Fee Schedule as the most defensible public-data benchmark.

The letter offers a concrete dollar amount, references the line-level analysis from `_benchmarks.csv`, and gives the provider a 30-day window to accept or counter. If they don't respond, the next escalation is `letter_30day_warning.md` then `small_claims_civil_warrant.md`.

This is not a hardship letter; it does not depend on the patient's ability to pay. Use `letter_hardship_negotiation.md` instead when the argument is "I can't pay" rather than "this number is fictional."

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

RE: Counter-offer on disputed charges —
    Account #[ACCOUNT NUMBER]
    Patient: [PATIENT FULL NAME]
    Date(s) of service: [DATE OF SERVICE]
    Current balance asserted by provider: $[CURRENT BALANCE]
    Counter-offer: $[COUNTER OFFER AMOUNT]

Dear Billing:

This letter is a written counter-offer to the above-referenced account. I have completed a line-item review of the itemized bill against the Explanation of Benefits issued by my health plan and against publicly available pricing benchmarks. The amount you are asking me to pay materially exceeds what your facility itself charges in cash, what the federal Hospital Price Transparency Rule requires you to disclose, and what UCC § 2-305(2) permits a seller to set in good faith for an unstated price term. This letter sets out my counter-offer with supporting evidence.

I. The legal framework

The contract under which I received care does not state a price. Under UCC § 2-305(2) (adopted in [STATE]), where the price has not been fixed in the contract, the seller is required to set it in good faith. Good faith in the medical-services context means a price reasonably aligned with the seller's own published cash rates, contracted commercial rates, and the rate the largest single-payer (Medicare) determines is reasonable. A charge multiple times the Medicare allowable is not a good-faith open price term; it is a sticker price the seller never actually expects to collect.

The federal Hospital Price Transparency Rule (45 CFR Part 180), in force since January 1, 2021, requires hospitals to publish a complete machine-readable file of their standard charges for every item and service, including the gross charge, discounted cash price, payer-specific negotiated charges, and de-identified minimum and maximum negotiated charges. CMS may impose civil monetary penalties up to $5,500 per hospital per day for non-compliance.

For physician services, the Medicare Physician Fee Schedule (42 CFR § 414) establishes the rate Medicare pays for each CPT/HCPCS code nationally. Commercial insurers typically pay between 100 % and 250 % of the Medicare rate. Patient-side amounts above 200 % of Medicare without contractual justification are facially excessive.

II. Line-item analysis

The following table compares your charges against (a) the Medicare allowable rate for the same code and (b) my plan's adjudicated allowed amount per the EOB.

[The LLM renders this table from `_benchmarks.csv` for the matching bill. Include only line items where the ratio is >= 1.50 or the absolute spread is >= $200; one row per CPT code.]

| CPT/HCPCS | Description   | Your charge | Medicare allowed | Ratio    | EOB allowed    |
| --------- | ------------- | ----------: | ---------------: | -------: | -------------: |
| [CODE]    | [DESCRIPTION] | $[BILLED]   | $[MEDICARE]      | [RATIO]x | $[EOB ALLOWED] |
| [CODE]    | [DESCRIPTION] | $[BILLED]   | $[MEDICARE]      | [RATIO]x | $[EOB ALLOWED] |
| [CODE]    | [DESCRIPTION] | $[BILLED]   | $[MEDICARE]      | [RATIO]x | $[EOB ALLOWED] |

Source for Medicare allowables: CMS Physician Fee Schedule Lookup, national rate, retrieved [DATE]. Source for EOB allowed amounts: my health plan's Explanation of Benefits dated [EOB DATE], claim number(s) [CLAIM NUMBERS].

[If the patient has retrieved the hospital's machine-readable file, the LLM adds the relevant cash-price column. Otherwise this paragraph is omitted.]

Your facility's own published cash price under 45 CFR § 180.50 for [PROCEDURE] is $[CASH PRICE], retrieved from your machine-readable file at [MRF URL] on [DATE]. The amount you are billing me is [N]x your own published cash rate.

III. Counter-offer

In full and final satisfaction of this account, I offer to pay $[COUNTER OFFER AMOUNT]. This figure represents [200 % of the Medicare allowable / the EOB allowed amount / the published cash price — whichever frame the LLM chose; pick the one most defensible from the evidence].

Payment terms:

1. Lump-sum payment by check or single confirmed electronic transfer within fifteen (15) business days of your written acceptance.
2. No auto-debit. No financing fees. No "balance forward" carrying over to a future statement.
3. Upon payment, you will mark this account paid-in-full, withdraw any prior credit reporting on this account, and provide written confirmation suitable for tax and insurance records.

I will not pay the asserted balance of $[CURRENT BALANCE]. That amount does not represent a good-faith price under UCC § 2-305(2), is materially above your own published cash rate, and is materially above the rate every other payer for the same service pays.

IV. Response deadline and consequences of non-response

I require your written response within thirty (30) calendar days of the date stamped on the USPS certified-mail receipt above. Your response should be one of:

(a) Acceptance of the counter-offer at $[COUNTER OFFER AMOUNT], with the payment instructions and a copy of the written paid-in-full confirmation you will provide upon payment.

(b) A written counter-counter-offer with an itemized basis. If you assert any charge above the Medicare rate, I expect the basis stated in writing, with reference to your published cash rate, contracted commercial rates, or specific cost factors particular to my care.

(c) A written refusal. If you refuse, I will treat this account as in formal dispute, file a complaint with the [STATE] Department of Insurance / Department of Commerce and Insurance and (if applicable) the [STATE] Attorney General's Division of Consumer Affairs, file a parallel complaint with CMS for any apparent Hospital Price Transparency Rule non-compliance, and exercise my right to bring a civil action in [COUNTY] [STATE] small-claims / general-sessions court seeking a declaratory judgment that the asserted balance is not a good-faith price under UCC § 2-305(2).

Failure to respond within 30 days will be treated as a refusal and the same escalation will follow.

V. No admission

This letter is an offer of compromise under [STATE] Rule of Evidence 408 (or its state equivalent) and is inadmissible to prove the validity or invalidity of the asserted balance. No statement in this letter is an admission of liability for any amount, and the counter-offer expires at the deadline above whether or not it has been formally rejected.

Please direct your response to the address above. Telephone responses are not accepted; this dispute is in writing only.

Sincerely,



[PATIENT FULL NAME]

Account number: [ACCOUNT NUMBER]
Date of service: [DATE OF SERVICE]

Enclosures:
- Copy of your itemized bill dated [STATEMENT DATE]
- Copy of the Explanation of Benefits dated [EOB DATE], claim(s) [CLAIM NUMBERS]
- Line-item benchmark analysis (Medicare PFS rates, retrieval date [DATE])
- [If applicable: screenshot of your published cash price from the MRF]

cc:
- [STATE] Department of Insurance — Consumer Services
- [STATE AG Division of Consumer Affairs — for the same complaint]
- file
```

---

## Placeholders and rendering notes

- `[COUNTER OFFER AMOUNT]` is the single most important value in the letter. The drafter pulls it from `tracker.csv`'s `counter_offer_amount` column. If that column is empty, the drafter computes a default: 200 % of the sum of Medicare allowables for the billed CPT codes for which a Medicare rate is available, plus the EOB-allowed amount for line items where no Medicare rate is on file.
- The line-item table is the heart of the letter. Render only line items where the ratio is >= 1.50 or the absolute spread is >= $200. Suppressing the in-range rows keeps the letter focused on what's actually disputed.
- The "Counter-offer" paragraph must name the anchor (Medicare rate / EOB / cash price) so the recipient can see the math, not just the number.
- If the patient is in a state that has not adopted UCC Article 2 in its medical-services context (rare), the drafter substitutes the state's common-law equivalent (reasonable price under quantum meruit / implied-in-fact contract). Most states will apply UCC § 2-305 or its analogue.

## Before sending

The drafter checks:

1. `has_eob == "Y"` (the EOB is the second leg of the comparison; without it the letter cannot reference plan-allowed amounts).
2. `has_itemization == "Y"` (a line-item analysis requires line items).
3. `_benchmarks.csv` exists for this biller folder with at least one row where `ratio_billed_to_medicare >= 1.50`. If every line is in fair-market range, this letter is the wrong tool — there is no price-gouging argument to make.

If any of these are missing, the drafter falls back to `letter_initial_dispute.md` or `letter_hardship_negotiation.md` as appropriate.

## Parallel actions (same day as mailing)

- Mail the certified letter to the provider.
- File the matching DOI complaint via `complaint_state_doi.md`, category E (price gouging) and category F (HPT non-compliance) if applicable. The DOI complaint creates parallel pressure and external documentation; never let a counter-offer sit alone.
- If the provider is a non-profit hospital, mail the financial-assistance application alongside (`letter_financial_assistance_application.md`) so a § 501(r) determination is also pending while negotiation runs.

## Follow-up

- Log this in `tracker.csv` with `counter_offer_sent_date` and `counter_offer_tracking`, and `response_due_date` = today + 30 calendar days.
- If 30 days pass with no response: draft `letter_30day_warning.md` next.
- If 45 days pass total with no acceptance and no counter-counter-offer: draft `small_claims_civil_warrant.md` and proceed to filing.
- If the provider accepts the counter-offer: pay only on receipt of their written acceptance + paid-in-full assurance. Verbal acceptances do not bind. Record the acceptance in `tracker.csv` `notes` field and update `status` to `settled`.
