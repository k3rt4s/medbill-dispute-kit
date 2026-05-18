# Federal laws and regulations

Authoritative citations for every federal law referenced in the rules. The LLM should pull from this file when drafting letters, complaints, or court filings rather than paraphrasing from memory.

## No Surprises Act (NSA)

- **Statutory authority:** Public Law 116-260, Division BB, Title I (Consolidated Appropriations Act, 2021)
- **Implementing regulations:** 45 CFR Parts 149 and 150; parallel provisions at 26 CFR and 29 CFR for self-funded plans
- **Effective:** January 1, 2022
- **Official patient page:** [cms.gov/nosurprises](https://www.cms.gov/nosurprises)
- **Know Your Rights:** [cms.gov/medical-bill-rights](https://www.cms.gov/medical-bill-rights)
- **No Surprises Help Desk:** **1-800-985-3059**
- **Complaint portal:** [cms.gov/medical-bill-rights/help/submit-a-complaint](https://www.cms.gov/medical-bill-rights/help/submit-a-complaint)
- **Civil monetary penalty:** up to $10,000 per violation

### What the Act actually prohibits

1. **Balance billing for emergency services** at any facility, in- or out-of-network. Includes emergency behavioral health.
2. **Balance billing for non-emergency services delivered by out-of-network providers at in-network facilities.** This is the "ER doc is out-of-network at an in-network hospital" trap — also covers anesthesiology, radiology, pathology, laboratory services, assistant surgeons, hospitalists, intensivists, and neonatology.
3. **Balance billing for out-of-network air ambulance.**
4. Requires **Good Faith Estimates** (GFEs) for uninsured and self-pay patients; see PPDR below.

### Important exclusions and traps

- **Ground ambulance is NOT covered.** This is the single biggest gap in the Act; ground ambulance balance billing remains legal under federal law. Some states (e.g. California, Maryland, New York, Ohio) have state-level ground-ambulance protections. Patients with a ground-ambulance balance bill should check their state's law before paying.
- Patients can **waive NSA protections** in some out-of-network non-emergency situations by signing a "Surprise Billing Protection Form" / Notice and Consent form at least 72 hours in advance. **Do not sign these.** A patient who signs the form has agreed to be balance-billed at out-of-network rates.

### Source for verbatim quotes

DOL EBSA's plain-language guide is the citable patient-facing reference: [dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/avoid-surprise-healthcare-expenses](https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/avoid-surprise-healthcare-expenses).

---

## Patient-Provider Dispute Resolution (PPDR)

The federal process for uninsured and self-pay patients whose final bill exceeds the Good Faith Estimate.

- **Authority:** No Surprises Act, implementing rule at 45 CFR § 149.620
- **CMS provider page:** [cms.gov/nosurprises/providers-payment-resolution-with-patients](https://www.cms.gov/nosurprises/providers-payment-resolution-with-patients)
- **Federal IDR portal:** [nsa-idr.cms.gov](https://nsa-idr.cms.gov/)
- **Filing fee:** $25 (refunded if the SDR entity rules below the billed amount)
- **Eligibility threshold:** the final bill from a single provider must exceed that provider's GFE by **$400 or more**
- **Filing window:** **120 calendar days** from receipt of the bill
- **Collections freeze during dispute:** the bill cannot be sent to collections, accrue late fees, or be reported during PPDR

### How to use it in the kit

If a patient is uninsured or self-pay and got no GFE, the toolkit's first move is a complaint to the No Surprises Help Desk (1-800-985-3059); failure to provide a GFE is itself an NSA violation. If a GFE was issued and the final bill is $400+ over for any single provider, file PPDR via the federal IDR portal within 120 days.

---

## Hospital Price Transparency Rule

- **Citation:** 45 CFR Part 180; machine-readable file requirement at 45 CFR § 180.50
- **Official regulation text (eCFR):** [ecfr.gov/current/title-45/subtitle-A/subchapter-E/part-180](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-E/part-180)
- **CMS fact sheet:** [cms.gov/newsroom/fact-sheets/hospital-price-transparency-fact-sheet](https://www.cms.gov/newsroom/fact-sheets/hospital-price-transparency-fact-sheet)
- **Effective:** January 1, 2021 (original); CMS template format mandatory beginning July 1, 2024; further refinements in the CY 2026 OPPS final rule
- **CMS technical implementation:** [github.com/CMSgov/hospital-price-transparency](https://github.com/CMSgov/hospital-price-transparency)
- **Complaint submission:** [cms.gov/hospital-price-transparency/contact-us](https://www.cms.gov/hospital-price-transparency/contact-us)

### What hospitals must post

1. A **machine-readable file** containing all standard charges for all items and services, including gross charges, payer-specific negotiated charges, discounted cash prices, de-identified minimum and maximum negotiated charges. As of CY 2026, must include median allowed amount plus 10th/90th percentile with 12-15 month lookback, plus a hospital attestation of accuracy.
2. A **consumer-friendly display** of at least 300 shoppable services (or the standard charges file in a sortable format).

### Reality check

Hospital compliance with this rule is poor. [PatientRightsAdvocate.org](https://www.patientrightsadvocate.org/) audits have found roughly 34-36% of hospitals fully compliant in recent reports. If a hospital won't produce its MRF or shoppable-services display, file a complaint with CMS. CMP penalties can reach ~$2M/year for large non-compliant hospitals.

---

## ERISA § 502(a)

- **Statutory citation:** **29 U.S.C. § 1132(a)** (ERISA § 502(a))
- **Official text (Cornell LII):** [law.cornell.edu/uscode/text/29/1132](https://www.law.cornell.edu/uscode/text/29/1132)
- **Implementing regs (claims procedures):** 29 CFR § 2560.503-1

### What it grants

- **§ 502(a)(1)(B):** suit "to recover benefits due to him under the terms of his plan, to enforce his rights under the terms of the plan, or to clarify his rights to future benefits."
- **§ 502(a)(2):** suit for breach of fiduciary duty (per 29 U.S.C. § 1109).
- **§ 502(a)(3):** equitable relief.
- DOL claims regs require denial letters to **explicitly state** the participant's § 502(a) right to sue.

### When it applies

Only ERISA-covered plans. Most large-employer self-funded plans are ERISA. **Not ERISA:**

- Government employer plans (federal, state, local)
- Church plans (unless the plan opted in)
- Individual market plans (those purchased on or off the ACA exchange)
- Medicare, Medicaid, TRICARE
- TennCare (Tennessee Medicaid managed care)

### Practical implications

For ERISA disputes:

- Exhaust internal appeals first; failure to exhaust usually bars suit.
- Venue is federal court; no jury; deferential review applies if the plan grants discretionary authority to the administrator (the "Firestone discretion" standard).
- Attorney's fees may be awarded to a prevailing claimant (§ 502(g)).
- Free informal intervention is available from the DOL Employee Benefits Security Administration (EBSA): **1-866-444-3272**, [dol.gov/agencies/ebsa](https://www.dol.gov/agencies/ebsa). EBSA benefits advisors will contact plan administrators on a participant's behalf before formal litigation; this is fast, free, and often resolves disputes that internal appeals couldn't.

### Preemption note

ERISA preempts state insurance-law remedies for ERISA-covered self-funded plans. Bad-faith claims, unfair-claims-practices claims, and similar state-law theories typically cannot be brought against an ERISA self-funded plan. For fully-insured ERISA plans, the "savings clause" preserves state regulation of insurance, so state remedies may still apply. The toolkit's plan-type question early in intake is meant to route the patient correctly.

---

## UCC § 2-305 (Open Price Term)

- **Citation:** Uniform Commercial Code § 2-305 (adopted by every state; codifications vary, e.g. Tenn. Code § 47-2-305, Cal. Com. Code § 2305)
- **Official text (Cornell LII):** [law.cornell.edu/ucc/2/2-305](https://www.law.cornell.edu/ucc/2/2-305)

### Verbatim text

> **§ 2-305. Open Price Term.**
>
> (1) The parties if they so intend can conclude a contract for sale even though the price is not settled. In such a case the price is a reasonable price at the time for delivery if (a) nothing is said as to price; or (b) the price is left to be agreed by the parties and they fail to agree; or (c) the price is to be fixed in terms of some agreed market or other standard as set or recorded by a third person or agency and it is not so set or recorded.
>
> (2) A price to be fixed by the seller or by the buyer means a price for him to fix in good faith.
>
> (3) When a price left to be fixed otherwise than by agreement of the parties fails to be fixed through fault of one party the other may at his option treat the contract as cancelled or himself fix a reasonable price.
>
> (4) Where, however, the parties intend not to be bound unless the price is fixed or agreed and it is not fixed or agreed there is no contract. In such a case the buyer must return any goods already received or if unable so to do must pay their reasonable value at the time of delivery and the seller must return any portion of the price paid on account.

### Why it matters

A patient signing a hospital admissions form agreeing to pay "all charges" without a stated price has entered into an open-price contract. UCC § 2-305(2) requires the seller (the hospital) to fix the price **in good faith**, and § 2-305(1) supplies a **reasonable price** as the default when none was set. Inflated chargemaster prices may violate both.

### Caveats

UCC Article 2 governs sale of goods, not pure services. Courts split on whether a hospital admission is a hybrid goods-and-services contract for Article 2 purposes. Cite § 2-305 as a negotiation lever and a credible small-claims argument — not as a guaranteed legal win. The strongest pairings are with common-law unconscionability, quantum meruit, and the implied covenant of good faith and fair dealing.

---

## Fair Debt Collection Practices Act (FDCPA)

- **Citation:** 15 U.S.C. §§ 1692-1692p
- **Full text (FTC):** [ftc.gov/system/files/documents/plain-language/fair-debt-collection-practices-act.pdf](https://www.ftc.gov/system/files/documents/plain-language/fair-debt-collection-practices-act.pdf)

### Key sections for medical debt

- **§ 1692g (Validation of debts):** within 5 days of first contact, a collector must send written notice stating (a) the amount of the debt, (b) the name of the creditor, (c) that the consumer has 30 days to dispute the debt in writing, (d) that if disputed in writing within 30 days the collector must verify the debt and pause collection, (e) that the consumer may request the original creditor's name and address.
- **§ 1692e:** prohibits false or misleading representations (threatening arrest, falsely implying lawsuit, misrepresenting the debt's legal status).
- **§ 1692f:** prohibits unfair practices, including collecting amounts not expressly authorized by contract or law.
- **§ 1692c(c):** consumer may demand written cessation of contact.

### Important limit

The FDCPA applies only to **third-party debt collectors and debt buyers**, not to the original creditor (the hospital or doctor's office collecting its own debt). For original-creditor collection abuse, look to state UDAP (Unfair and Deceptive Acts and Practices) laws.

### Practical use

Send a § 1692g validation request within 30 days of first contact from any third-party collector on a medical debt. Most cannot produce a signed contract, the itemized underlying bill, and an unbroken chain of assignment, particularly for resold debt.

---

## IRS § 501(r) — Hospital Charity Care

- **Citation:** 26 U.S.C. § 501(r); regs at 26 CFR § 1.501(r)
- **IRS page:** [irs.gov/charities-non-profits/financial-assistance-policy-and-emergency-medical-care-policy-section-501r4](https://www.irs.gov/charities-non-profits/financial-assistance-policy-and-emergency-medical-care-policy-section-501r4)

### What it requires

Every 501(c)(3) non-profit hospital must:

1. Adopt and **widely publicize** a written **Financial Assistance Policy (FAP)** covering emergency and medically-necessary care.
2. Charge FAP-eligible patients **no more than amounts generally billed (AGB)** to insured patients.
3. Make **reasonable efforts to determine FAP eligibility** before any "extraordinary collection action" (lawsuits, wage garnishment, credit reporting, denying future care).
4. Provide written notice with a **30-day-minimum deadline** before extraordinary collection actions begin.

### Practical implications

Most hospitals in the US are non-profits. Every patient with a hospital bill from a non-profit hospital should screen for FAP eligibility before any negotiation. Eligibility is typically pegged to a multiple of the federal poverty level (commonly 200%-400% FPL). [Dollar For](https://dollarfor.org/) is a free non-profit that helps patients apply.

---

## Credit reporting changes affecting medical debt

The CFPB's January 2025 final rule that would have prohibited all medical debt from credit reports was **vacated July 11, 2025** by the U.S. District Court for the Eastern District of Texas. See [Berkeley Consumer Law on the vacatur](https://consumerlaw.berkeley.edu/news/court-overturns-federal-rule-keeps-medical-debt-credit-reports).

Still in effect, by voluntary action of the three credit bureaus (Equifax, Experian, TransUnion) since March 2022:

- **Paid medical collections** removed from credit reports
- **One-year grace period** before unpaid medical debt may be reported
- **Medical collections under $500** entirely excluded from credit reports (effective April 2023)

A patient with a paid or sub-$500 medical collection on their credit report can demand removal directly from the bureaus.

---

## Choosing Wisely

- **URL:** [choosingwisely.org](https://www.choosingwisely.org)
- An ABIM Foundation project listing specialty-society recommendations for tests and procedures commonly done but not evidence-supported. Useful when a patient is questioning a recommended service before it generates a bill (see [[../rules/08_avoid_unneeded_care]]).
