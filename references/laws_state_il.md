# Illinois state pack

The fully-worked state-law layer for Illinois patients. The LLM uses this when the patient's state is Illinois. Peer packs at [`laws_state_ca.md`](laws_state_ca.md), [`laws_state_fl.md`](laws_state_fl.md), [`laws_state_ga.md`](laws_state_ga.md), [`laws_state_ny.md`](laws_state_ny.md), [`laws_state_tn.md`](laws_state_tn.md), [`laws_state_tx.md`](laws_state_tx.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Three things make Illinois's patient-side leverage unusually strong:

1. The **Hospital Uninsured Patient Discount Act** (210 ILCS 89/) caps charges at **135% of the hospital's documented cost** for medically-necessary services to qualifying uninsured patients (income ≤ 600% FPL for urban hospitals, ≤ 300% FPL for rural/Critical Access), and caps annual collections from any one qualifying patient at **25% of family income**. This is one of the most prescriptive uninsured-discount statutes in the country.
2. The **Consumer Fraud and Deceptive Business Practices Act** (815 ILCS 505/) is one of the broadest consumer-protection statutes in the United States — it reaches **original creditors** (the hospital itself), carries a **private right of action with attorney's fees and punitive damages**, and was further amended in 2024 to make adverse medical-debt credit reporting itself a CFA violation.
3. The **statute of limitations on a written hospital admissions contract is ten (10) years** under 735 ILCS 5/13-206 — the longest in the country tied with a handful of other states. Combined with Illinois's partial-payment-restart rule, this dramatically expands the dispute window compared to the 3-6 year SOL in most peer states.

Treat these three as the structural headlines in any Illinois dispute strategy. The 135%-of-cost cap is the single highest-leverage Illinois-specific cite when the patient was uninsured at the time of service.

## Hospital itemization right

Illinois has **two overlapping itemization statutes** plus a generally-applicable patient-rights provision. None of them follow Georgia's "automatic delivery within X days" model — all require a written patient request — but the right is firm and enforceable.

- **Primary statute:** **Medical Patient Rights Act, 410 ILCS 50/3(d)** — "The right of each patient, regardless of source of payment, to examine and receive a reasonable explanation of his total bill for services rendered by his physician or health care provider, including the itemized charges for specific services received."
- **Hospital-specific statute:** **Fair Patient Billing Act, 210 ILCS 88/15 and 88/20** — every hospital bill must include a phone number the patient may use to inquire about or dispute the bill, and every hospital must make an itemized statement available on patient request.
- **Sources:** [Medical Patient Rights Act on ilga.gov](https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=1525); [Fair Patient Billing Act on ilga.gov](https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=2798&ChapterID=21); [healthcarereportcard.illinois.gov/fair-patient-billing-act](https://healthcarereportcard.illinois.gov/fair-patient-billing-act)
- **What it requires:**
  - Patient (or authorized representative) makes a written request to the hospital's billing department.
  - Hospital must furnish an itemized statement listing each charge separately, identified by date of service and provider.
  - Reasonable timeframe is not statutorily fixed but Illinois Department of Public Health guidance treats 30 days as the outer limit; most hospitals deliver within 7-14 days.
- **Scope:** All Illinois-licensed hospitals (Article 28 facilities) under the Fair Patient Billing Act; all physicians and health care providers (regardless of setting) under the Medical Patient Rights Act.
- **Private right of action:** The Medical Patient Rights Act does not itself create a damages action, but a violation supports a parallel claim under the Consumer Fraud Act (815 ILCS 505/) — which does have a private right of action with attorney's fees. See "Illinois Consumer Fraud and Deceptive Business Practices Act" section below.
- **ERISA:** Not preempted — regulates the provider, not the plan.

Use 410 ILCS 50/3(d) and 210 ILCS 88/15 jointly as the citation in `templates/letter_itemization_request.md` for any Illinois patient. The user's framing referenced the Hospital Report Card Act (210 ILCS 86/); that Act governs hospital quality reporting, not itemized billing, and is the wrong cite for an itemization-request letter.

## Unfair Claims Settlement Practices Act

- **Statute:** **215 ILCS 5/154.5, 5/154.6, 5/154.7** — Article XXVI.1 of the Illinois Insurance Code, the Improper Claims Practices provisions (Illinois's UCSPA equivalent)
- **Sources:** [215 ILCS 5/154.6 on ilga.gov](https://www.ilga.gov/legislation/ilcs/documents/021500050K154.6.htm); [215 ILCS 5/154.6 on FindLaw](https://codes.findlaw.com/il/chapter-215-insurance/il-st-sect-215-5-154-6/); [215 ILCS 5/154.6 on LawServer](https://www.lawserver.com/law/state/illinois/il-statutes/215_ilcs_5_154-6)
- **Substance:** § 154.6 enumerates eleven specific acts that constitute "improper claims practices" when committed knowingly or with such frequency to indicate a persistent tendency — misrepresenting policy provisions, failing to acknowledge claims promptly, failing to adopt reasonable investigation standards, failing to attempt good-faith prompt and fair settlement when liability has become reasonably clear, compelling insureds to sue by offering substantially less than the amount ultimately recovered, etc.
- **Critical caveat:** **No private right of action.** Illinois courts have consistently held that §§ 154.5-154.7 are **regulatory in nature only** — enforced by the Director of the Illinois Department of Insurance, not by private suit. See *Roppo v. Travelers Commercial Ins. Co.*, 869 F.3d 568 (7th Cir. 2017), confirming the long-standing rule from *Purlee v. Liberty Mutual Fire Ins. Co.* and progeny.
- **Use:** Cite UCSPA violations in your **Illinois Department of Insurance complaint** (see Regulatory agencies section). They are also useful evidentiary support for a § 155 vexatious-and-unreasonable claim (next section). Do not plead §§ 154.5-154.7 as a standalone count in court — it will be dismissed.

## Bad-faith failure to pay — § 155 vexatious-and-unreasonable remedy

- **Statute:** **215 ILCS 5/155**
- **Sources:** [215 ILCS 5/155 on ilga.gov](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=021500050K155); [215 ILCS 5/155 on FindLaw](https://codes.findlaw.com/il/chapter-215-insurance/il-st-sect-215-5-155/); [215 ILCS 5/155 on Onecle](https://law.onecle.com/illinois/215ilcs5/155.html); practitioner overview at [illinoislegalaid.org/legal-information/litigating-policyholder-claims-against-insurance-companies](https://www.illinoislegalaid.org/legal-information/litigating-policyholder-claims-against-insurance-companies)
- **Substance:** In any action where the liability of an insurer on a policy is in issue, or for unreasonable delay in settling a claim, if the court finds the insurer's action or delay was "**vexatious and unreasonable**," the court may award the insured:
  - reasonable attorney's fees,
  - other costs,
  - plus an additional amount **not to exceed any one of the following, whichever is greatest**:
    - (a) **60% of the amount the insured is found to be entitled to recover** in excess of what the insurer offered to pay, **or**
    - (b) **$60,000**, **or**
    - (c) the excess of the amount the court or jury finds the insured is entitled to recover over the amount the insurer offered to pay.
- **Standard:** "Vexatious and unreasonable" — more than negligence or honest mistake, but a lower bar than the punitive-damages "willful and wanton" standard. Bona-fide coverage disputes do not qualify; refusal to investigate, lowball offers contradicted by the insurer's own file, and pattern delay do.
- **§ 155 is the only bad-faith remedy.** Illinois does not recognize a separate common-law first-party bad-faith tort. § 155 preempts the common-law tort claim per *Cramer v. Insurance Exch. Agency*, 174 Ill. 2d 513 (1996). For ERISA self-funded plans, § 155 is preempted; the federal remedy is 29 U.S.C. § 1132(a)(1)(B).
- **ERISA preemption:** § 155 is preempted as to self-funded employer plans. In play for fully-insured plans, HMOs, Medicaid managed care, and individual/marketplace policies.
- **Note on the citation framing in the original drafting request:** the request referenced "**215 ILCS 5/155.36** (Department investigation)." That citation is incorrect for this purpose. § 155.36 actually requires Class 1(b) and Class 2(a) insurers to comply with specified sections of the Managed Care Reform and Patient Rights Act (215 ILCS 134/) — it is a managed-care-incorporation provision, not a bad-faith investigation mechanism. The Department-investigation route is the consumer complaint process administered under §§ 154.5-154.7 and § 401 (general investigative authority). Use § 155 for the litigation remedy, the §§ 154.6 list for the IDOI complaint.

## Surprise billing — Network Adequacy and Transparency Act + § 356z.3a

Illinois layers state surprise-billing protection on top of the federal No Surprises Act through three statutes:

- **215 ILCS 124/** — **Network Adequacy and Transparency Act** (effective Jan 1, 2019; amended multiple times since)
- **215 ILCS 5/356z.3** — Balance-billing prohibition (amended 2022 by Public Act 102-0901 to align with the federal NSA, effective July 1, 2022, with certain provisions effective Jan 1, 2023)
- **215 ILCS 5/356z.3a** — Notice and Consent waiver mechanism for OON consent at in-network facilities (added by Public Act 102-0901)

- **Sources:** [Network Adequacy and Transparency Act on ilga.gov](https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=3824&ChapterID=22); [215 ILCS 5/356z.3 on ilga.gov](https://ilga.gov/legislation/ilcs/documents/021500050K356z.3.htm); [215 ILCS 5/356z.3a on FindLaw](https://codes.findlaw.com/il/chapter-215-insurance/il-st-sect-215-5-356z-3a/); [IDOI Company Bulletin 2022-03 on PA 102-0901](https://idoi.illinois.gov/content/dam/soi/en/web/insurance/companies/companybulletins/cb2022-03.pdf); [The Source on HealthCare Price and Competition – Network Adequacy Act](https://sourceonhealthcare.org/legislation/215-ill-comp-stat-%C2%A7%C2%A7-124-1-through-124-25-network-adequacy-and-transparency-act/)

### What it prohibits

- Balance billing for **emergency services** from an out-of-network (OON) provider at any facility.
- Balance billing for **non-emergency services** rendered by an OON provider at an **in-network** facility, including ancillary services (anesthesia, radiology, pathology, lab, neonatology, assistant surgeon, hospitalist).
- Balance billing when the facility or provider fails to satisfy the **notice-and-consent waiver requirements** in § 356z.3a (one business day advance disclosure, plain-English consent form, good-faith estimate, no waiver for emergency or ancillary services).
- Patient cost-sharing is capped at the **in-network amount** and counts toward the in-network deductible and out-of-pocket maximum.

### Where Illinois state law adds value beyond the federal NSA

- Network Adequacy Act's directory-accuracy provisions provide an **affirmative provider-side duty** to maintain accurate participating-provider lists, with IDOI enforcement and per-violation fines. A misclassification by the carrier becomes a state-law violation separate from any NSA balance-billing dispute.
- 60-day advance notice to beneficiaries before a participating provider's nonrenewal or termination (215 ILCS 124/15) — gives the patient a window to switch providers without surprise OON exposure.

### Caveats

- **ERISA preemption:** state surprise-billing rules in §§ 356z.3 and 356z.3a do not reach self-funded ERISA employer plans. Those plans are covered only by the federal NSA.
- The federal NSA and Illinois law layer rather than displace where both apply.
- Excludes workers' compensation, Medicare, Medicaid (Medicaid has separate balance-billing protections at 305 ILCS 5/).

### Ground ambulance — important correction to common drafting framing

**§ 356z.3a as currently codified does *not* apply to ground ambulance.** The statute's "health care provider" definition expressly excludes "a provider of air ambulance or ground ambulance services," and § 356z.3a(b)(7) states the section "does not apply with respect to air ambulance or ground ambulance services."

Ground-ambulance balance-billing protection in Illinois comes from a **separate, later-enacted statute** (the Consumer Protection from Surprise Health Care Billing Act, enacted via SB 2405 in the 103rd General Assembly), with operative protections effective **on or after July 1, 2025**. See "Ground-ambulance protection" section below for the correct cite. Drafts that cite § 356z.3a for ground ambulance need to be corrected; this is a real risk in dispute letters because providers' counsel will catch the misquote and use it to discredit the rest of the letter.

## Illinois Consumer Fraud and Deceptive Business Practices Act (CFA / ICFA)

The **most important Illinois-specific lever after the Uninsured Discount Act.** One of the broadest consumer-protection statutes in the country.

- **Statute:** **815 ILCS 505/** — full Act; key sections **§ 505/2** (substantive prohibition), **§ 505/10a** (private right of action and remedies), **§ 505/2EEEE** (medical-debt-credit-reporting prohibition, added 2024)
- **Sources:** [815 ILCS 505 on ilga.gov](https://www.ilga.gov/Legislation/ILCS/Articles?ActID=2356&ChapterID=67); [§ 505 articles on ilga.gov](https://www.ilga.gov/legislation/ilcs/ilcs4.asp?ActID=2356&ChapterID=67&SeqStart=8200000&SeqEnd=10000000); [Illinois Legal Aid: Remedies Available Under the CFA](https://www.illinoislegalaid.org/node/147976); practitioner discussion at [thebusinesslitigators.com Illinois Consumer Fraud Act](https://www.thebusinesslitigators.com/business-commercial-litigation/consumer-fraud-defense/illinois-consumer-fraud-and-deceptive-businesses-practices-act-e/)

### What it prohibits

§ 505/2 sweeps broadly — unfair methods of competition and unfair or deceptive acts or practices, including but not limited to: misrepresentation, concealment, or omission of material facts in the conduct of trade or commerce, "with intent that others rely upon" the misrepresentation. Federal FTC Act case law is incorporated by reference. The "unfair" prong is independent of "deceptive" — conduct that offends public policy or causes substantial consumer injury without offsetting benefit qualifies even without misrepresentation.

### Why it is the strongest Illinois lever

1. **Reach over original creditors.** Unlike the federal FDCPA, ICFA reaches **the hospital itself**, not just third-party debt collectors. Hospital in-house billing practices — upcoding, billing for services never rendered, misrepresenting in-network status, threatening lawsuits without intent to sue — are directly actionable under § 505/2 against the hospital.
2. **Private right of action with strong remedies.** § 505/10a authorizes a private suit by any "person who suffers actual damage" with recovery of:
   - actual damages,
   - **punitive damages** when the conduct was willful (Illinois Pattern Jury Instructions apply standard punitive standards),
   - **reasonable attorney's fees and costs** in the court's discretion to prevailing plaintiffs (and to prevailing defendants only on a "bad faith" showing by the plaintiff — an asymmetric provision designed to encourage consumer plaintiffs),
   - injunctive relief.
3. **No notice-of-defect or ante-litem demand requirement.** Unlike Georgia's FBPA, ICFA can be filed without a pre-suit demand. The 30-day warning letter from this kit is still smart practice but not statutorily required.
4. **Medical-debt-credit-reporting violation is an ICFA violation per se.** Public Act 103-0648 (effective Jan 1, 2025) added § 505/2EEEE, making it unlawful for a consumer reporting agency to create a consumer report containing adverse information related to medical debt incurred by an Illinois consumer or a collection action against the consumer for medical debt. Violations are enforceable through the full ICFA remedy stack (private suit, AG action, attorney's fees, punitives). See "Credit reporting" section below.

### Statute of limitations on the ICFA claim itself

**3 years** from the date of the unfair or deceptive act, under 815 ILCS 505/10a(e). This is separate from and shorter than the 10-year contract SOL — patients with stale-bill disputes need to use the contract SOL, not ICFA, for limitations purposes.

### Practical use

For provider-side disputes (vs. insurer-side), **always pair the standard hospital-billing dispute with an explicit ICFA citation in the 30-day warning letter.** The combination of attorney's fees, punitives, and original-creditor reach makes ICFA the single most effective deterrent against further hospital collection action.

## Regulatory agencies

### Illinois Department of Insurance (IDOI)

- **Online complaint:** [idoi.illinois.gov/consumers/file-a-complaint.html](https://idoi.illinois.gov/consumers/file-a-complaint.html); complaint forms at [idoi.illinois.gov/consumers/understanding-complaint-process.html](https://idoi.illinois.gov/consumers/understanding-complaint-process.html)
- **Phone:** Office of Consumer Health Insurance toll-free **1-877-527-9431**; general consumer hotline **1-866-445-5364**; TDD **217-524-4872**
- **Email:** doi.complaints@illinois.gov
- **Mail (Springfield, headquarters for complaints):**
  > Illinois Department of Insurance
  > Consumer Services Section
  > 320 W. Washington Street, 4th Floor
  > Springfield, IL 62767
- **Chicago office:**
  > Illinois Department of Insurance
  > 555 W. Monroe Street, 5th Floor
  > Chicago, IL 60661
- **Authority:** all insurance companies and HMOs licensed in Illinois — fully-insured health insurers, dental, vision, Medicare supplement. Administers the Improper Claims Practices Article, Network Adequacy and Transparency Act, surprise-billing provisions, and § 155 bad-faith complaints (in parallel with court litigation). **No authority over self-funded ERISA plans** (route to U.S. DOL EBSA at 1-866-444-3272), does not regulate providers, hospitals, or debt collectors (route to AG).

### Illinois Attorney General — Consumer Fraud Bureau and Health Care Bureau

- **Online complaint:** [illinoisattorneygeneral.gov/file-a-complaint/consumer/](https://illinoisattorneygeneral.gov/file-a-complaint/consumer/); central portal [illinoisattorneygeneral.gov/File-A-Complaint](https://illinoisattorneygeneral.gov/File-A-Complaint/index)
- **Hotlines:**
  - Chicago **1-800-386-5438** (TTY 1-800-964-3013)
  - Springfield **1-800-243-0618** (TTY 1-877-844-5461)
  - Carbondale **1-800-243-0607**
  - Health Care Bureau Helpline **1-877-305-5145**
- **Mail (Chicago, primary intake for consumer complaints):**
  > Office of the Illinois Attorney General
  > Consumer Fraud Bureau
  > 100 W. Randolph Street, 12th Floor
  > Chicago, IL 60601
- **Mail (Springfield):**
  > Office of the Illinois Attorney General
  > Consumer Fraud Bureau
  > 500 S. Second Street
  > Springfield, IL 62701
- **Authority:** enforces ICFA (815 ILCS 505/), the Fair Patient Billing Act (210 ILCS 88/), the Hospital Uninsured Patient Discount Act (210 ILCS 89/), and Illinois debt-collection statutes. Reach over providers, hospitals, third-party debt collectors, **and original creditors** — exactly the gap not covered by IDOI. The **Health Care Bureau** is a dedicated unit within the AG's office that handles insurance-coverage, medical-billing, and patient-rights complaints and has a documented track record of recovering disputed bills directly on behalf of consumers. Use the Health Care Bureau Helpline for direct intervention on billing disputes.

## Small claims court — Circuit Court small-claims division

- **Court name:** **Circuit Court of [county], Small Claims Division** (Illinois has unified circuit courts; small-claims is a docket, not a separate court)
- **Jurisdictional limit:** **$10,000**, set by **Illinois Supreme Court Rule 281**
- **Source:** [Illinois Supreme Court Rules, Article II Part F (Small Claims)](https://www.illinoiscourts.gov/courts/supreme-court/supreme-court-rules/); county small-claims guides linked through [illinoiscourts.gov](https://www.illinoiscourts.gov/)
- **Filing fees:** vary by county; representative 2024-2026 ranges:
  - Cook County: $90-$268 depending on claim size
  - DuPage / Lake / Will counties: ~$284 for claims $5,000.01-$10,000
  - McHenry / Madison counties: $89 for claims up to $2,500, $264 for $2,500.01-$10,000
- **Fee waiver:** available for low-income filers under **Illinois Supreme Court Rule 298** (sworn application for waiver of court fees).
- **Attorney rules:** permitted, not required. Designed for pro se litigants. **Corporations and LLCs cannot appear pro se** in Illinois small-claims court — they must be represented by a licensed attorney (per Supreme Court Rule 282(b) and *Downtown Disposal Servs., Inc. v. City of Chicago*, 2012 IL 112040 line of cases). This is Illinois-specific and asymmetric: the patient (a natural person) may appear pro se, but the hospital corporation must hire counsel — a meaningful economic deterrent against the hospital pressing a defended claim.
- **Jury trial:** available on demand (Illinois Supreme Court Rule 285); however, in small-claims defendants must demand a jury within the time to file the appearance and pay a separate jury fee.

## Statute of limitations

- **Written contracts:** **10 years from breach** — **735 ILCS 5/13-206**
- **Oral contracts / unwritten:** **5 years from breach** — **735 ILCS 5/13-205**
- **ICFA claims:** 3 years from the unfair or deceptive act — 815 ILCS 505/10a(e)
- **Source:** [735 ILCS 5/13-206 on ilga.gov](https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=073500050K13-206); [Illinois Legal Aid: Selected statutes of limitations](https://www.illinoislegalaid.org/legal-information/selected-statutes-limitations); [735 ILCS 5 Article XIII on Justia](https://law.justia.com/codes/illinois/chapter-735/act-735-ilcs-5/article-xiii/)

Most hospital admissions involve a signed financial-responsibility form — a written contract — so **10 years applies**. Implied-in-fact medical-billing arrangements without a signed agreement default to the 5-year oral/unwritten SOL. The clock runs from the date of breach (typically the day payment was due and not made), not from when damages are discovered.

**Partial payment or written acknowledgment of the debt restarts the clock** under 735 ILCS 5/13-206 and Illinois common law (*Lampe v. Pawlarczyk*, 314 Ill. App. 3d 455 (2000)). The new 10-year period runs from the date of the new payment or promise. **Do not make a partial payment on a time-barred debt without legal advice** — it can revive a debt that was otherwise unenforceable.

The 10-year written-contract SOL is **tied for the longest in the country** (with Rhode Island, Iowa, and a few others) and is one of the structural Illinois advantages — it gives the patient a long window to identify and dispute billing errors. The flip side: it also gives hospitals a long window to sue, so disputes should be initiated, not deferred.

## Ground-ambulance protection

- **Statute:** **Consumer Protection from Surprise Health Care Billing Act** (added to the Insurance Code via SB 2405, 103rd General Assembly), with protections effective **on or after July 1, 2025**.
- **Important correction:** the original drafting framing cited **215 ILCS 5/356z.3a** as the ground-ambulance protection effective 2023. **That is incorrect.** § 356z.3a expressly excludes ground ambulance — its definition of "health care provider" carves out air and ground ambulance services, and the section itself "does not apply with respect to air ambulance or ground ambulance services." Ground-ambulance protection in Illinois comes from the later, separate enactment described here.
- **Sources:** [SB 2405 bill text on LegiScan](https://legiscan.com/IL/text/SB2405/id/3109427); [SB 2405 Bill Status on ilga.gov](https://www.ilga.gov/Legislation/BillStatus?GAID=18&DocNum=2405&DocTypeID=SB&LegId=0&SessionID=114); [IDOI Company Bulletin 2022-13 on ground ambulance (predecessor framework)](https://idoi.illinois.gov/content/dam/soi/en/web/insurance/companies/companybulletins/cb2022-13.pdf); related earlier provision under [HB 2391, 103rd GA](https://www.ilga.gov/legislation/103/HB/10300HB2391.htm)
- **Substance:** for services on or after July 1, 2025, when a covered patient receives services from a **nonparticipating ground ambulance service provider**, the health-insurance issuer must ensure the patient incurs no greater out-of-pocket cost than they would have with a participating provider. Cost-sharing is applied as if the services had been provided by a participating ambulance provider. The statute also establishes maximum allowable payment amounts and a dispute mechanism for provider-insurer rate disputes that does not involve the patient. Failure to comply is an unlawful practice under ICFA, enforceable by the AG.
- **ERISA:** preempted as to self-funded employer plans. In play for fully-insured plans and HMOs regulated by Illinois.
- **Pre-July 2025 ground ambulance bills:** Illinois state law provides no protection. Patient is limited to federal-NSA-equivalent leverage (which excludes ground ambulance entirely), general state UCC and contract law, and Medicaid/Medicare program rules where applicable. This is the most important date-of-service check in Illinois ambulance disputes.

## Credit reporting

Illinois enacted **one of the strongest state-level medical-debt-credit-reporting bans in the country** in 2024, via SB 2933 / Public Act 103-0648, codified at **815 ILCS 505/2EEEE**.

- **Statute:** **815 ILCS 505/2EEEE** (added by Public Act 103-0648, effective **January 1, 2025**)
- **Sources:** [Public Act 103-0648 full text on ilga.gov](https://www.ilga.gov/legislation/publicacts/fulltext.asp?Name=103-0648); [SB 2933 Bill Status on ilga.gov](https://www.ilga.gov/legislation/billstatus.asp?DocNum=2933&DocTypeID=SB&GA=103&GAID=17&LegID=151908&SessionID=112); [Consumer Financial Services Law Monitor analysis](https://www.consumerfinancialserviceslawmonitor.com/2024/05/illinois-passes-legislation-to-ban-reporting-of-medical-debt/); [NCLC Digital Library: The Latest on Keeping Medical Debt Out of Credit Reports](https://library.nclc.org/article/latest-keeping-medical-debt-out-credit-reports)
- **Substance:** makes it unlawful for a consumer reporting agency to create a consumer report containing any adverse information that the CRA knows or should know relates to medical debt incurred by the consumer, or to a collection action against the consumer to collect medical debt. Definition of "medical debt" excludes debt charged to a credit card or to an open-end or closed-end financial-institution credit line that is not exclusively for medical purposes.
- **Enforcement:** as an amendment to the Consumer Fraud and Deceptive Business Practices Act, violations carry the full ICFA remedy stack — AG enforcement, private right of action with attorney's fees, punitive damages, injunctive relief.
- **Note on the drafting-request framing:** the original framing referenced "**Illinois Consumer Credit Card Liability Act**" as the medical-debt credit-reporting statute. That is incorrect. The Illinois Consumer Credit Card Liability Act (815 ILCS 145/) is a 1970s statute limiting cardholder liability for unauthorized credit-card use — unrelated to medical debt. The correct cite is **815 ILCS 505/2EEEE** as added by Public Act 103-0648.
- **Federal preemption posture is in flux.** The CFPB issued an October 2025 interpretive rule taking the position that the federal Fair Credit Reporting Act preempts state laws restricting medical-debt credit reporting. If that survives challenge, it limits the effect of § 505/2EEEE. The Illinois AG has signaled it will defend the state law. **Check current preemption status before relying on the state-law remedy in litigation;** the AG complaint route remains available regardless of the preemption fight.
- **Separately enacted:** Public Act 103-0647 (HB 5290, effective July 2, 2024) appropriated state funds to purchase and forgive outstanding Illinois medical debt — separate program, not a credit-reporting statute; relevant to relief but not to dispute letters.

## Hospital Uninsured Patient Discount Act — 135% of cost cap

The single highest-leverage Illinois-specific protection. **Every dispute letter on behalf of an uninsured Illinois patient should lead with this cite.**

- **Statute:** **Hospital Uninsured Patient Discount Act, 210 ILCS 89/** (eff. April 1, 2009; expanded by Public Act 102-0581 (eff. 2022) raising the urban income threshold to 600% FPL and the rural threshold to 300% FPL)
- **Sources:** [210 ILCS 89 article listing on ilga.gov](https://www.ilga.gov/Legislation/ILCS/Articles?ActID=3001&ChapterID=21&Print=True); [§ 89/10 on Onecle](https://law.onecle.com/illinois/210ilcs89/10.html); [Hospital Uninsured Patient Discount Act on Illinois Hospital Report Card](https://healthcarereportcard.illinois.gov/contents/view/hospital_uninsured_patient_discount_act); [team-iha.org Discount and Cap FAQs](https://www.team-iha.org/finance/charity-care-financial-assistance/discount-and-cap-faqs/)

### Who qualifies

- Patient must be **uninsured** for the services in question (no third-party payor — no commercial insurance, Medicare, Medicaid, workers' comp, or other coverage that would cover the bill).
- Patient income at or below:
  - **600% of the federal poverty level** for hospitals in a metropolitan statistical area (urban hospitals).
  - **300% of the federal poverty level** for Critical Access Hospitals and hospitals outside an MSA (rural hospitals).
- **Asset limit (hospital may, but is not required to, apply):** assets ≤ 600% FPL for urban hospitals; ≤ 300% FPL for rural / Critical Access. The hospital must elect whether to apply asset testing; many do not.

### What the discount looks like

For charges in excess of **$300** in any one inpatient admission or outpatient encounter:

- **Sliding-scale discount based on family income** (210 ILCS 89/10):
  - ≤ 200% FPL: **90% discount**
  - 200.01-300% FPL: **80% discount**
  - 300.01-400% FPL: **75% discount**
  - 400.01-500% FPL: **75% discount** (per 2022 amendment)
  - 500.01-600% FPL: **70% discount**
- **The hard cap: 135% of the hospital's cost.** The "uninsured discount" mechanism mathematically caps the amount the hospital can collect at **1.35 × the hospital's documented cost** for the services. Cost is derived from the hospital's most recently filed Medicare cost report, CMS-2552-96/10 Worksheet C Part I (the hospital's audited cost-to-charge ratio). The result is that even before the sliding-scale percentage discount, no qualifying uninsured patient can be charged more than 135% of the hospital's documented cost for the service.
- **Annual collection cap:** the maximum amount that may be collected from an eligible patient in any **12-month period** for hospital services is **25% of the patient's family income** (210 ILCS 89/15). This is a hard cap regardless of the underlying bill amount.

### What the hospital must do

- Apply the discount on request from any patient who provides documentation of income (within hospital's stated application window — typically 60-90 days after first bill, but the hospital may not deny solely for late application without good cause).
- Annually file the hospital's Worksheet C cost-to-charge ratio with the Illinois Attorney General's office.
- Disclose the availability of the discount in plain English on every bill, in admission materials, and in the hospital's online financial-assistance page.

### Enforcement

The AG enforces 210 ILCS 89/ directly. The Hospital Uninsured Patient Discount Act does not contain an express private right of action, but **a violation supports a private ICFA claim** under 815 ILCS 505/2 — combining the Discount Act's substantive cap with ICFA's remedy stack (attorney's fees, punitives) is the standard Illinois patient-side litigation theory.

### Caveats

- Does **not** apply to patients with any insurance coverage for the service in question. If insurance denied the claim for medical-necessity reasons but the patient was insured at the time of service, the Discount Act does not apply — pursue the denial through internal/external appeals and § 155.
- Does not apply to Medicare/Medicaid patients (separate program rules).
- Does not apply to physician practice charges that are not hospital-billed. Independent physician practices, ambulatory surgery centers not owned by a hospital, and freestanding imaging are outside the Act's scope. If the physician's services were billed through the hospital, they are covered.

## Fair Patient Billing Act — 210 ILCS 88/

Companion statute to the Uninsured Patient Discount Act. Imposes uniform pre-collection procedural requirements on all Illinois hospitals.

- **Statute:** **Fair Patient Billing Act, 210 ILCS 88/** (eff. 2007)
- **Sources:** [210 ILCS 88 on ilga.gov](https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=2798&ChapterID=21); [Fair Patient Billing Act consumer page](https://healthcarereportcard.illinois.gov/fair-patient-billing-act); [Hinshaw Law Alert on 210 ILCS 88](https://www.hinshawlaw.com/a/web/2TDFApYtDnkCFApyTEXawA/healthlawalert_illinoisadministrativecode210ilcs_080813.pdf); [The Source on HealthCare Price and Competition – Fair Patient Billing Act](https://sourceonhealthcare.org/legislation/210-ill-comp-stat-%C2%A7%C2%A7-88-1-through-88-55-fair-patient-billing-act/); [Lexology: The Illinois Fair Patient Billing Act](https://www.lexology.com/library/detail.aspx?g=5ffe9a0c-d41b-4d10-8c66-94034929677a)

### What it requires

- **Bill contents (§ 88/15):** every hospital bill must (i) be itemized on request, (ii) list a telephone number the patient may call to inquire about or dispute the bill, (iii) disclose the availability of financial assistance and the Uninsured Patient Discount, (iv) disclose interpreter services for non-English speakers.
- **Pre-collection procedures (§ 88/30):**
  - For **insured patients**: hospital may not refer a bill to collections without first offering the patient the opportunity to request a **reasonable payment plan**, with at least **30 days following the initial bill** for the patient to request the plan. If the patient requests a plan but fails to agree to one within 30 days of the request, the hospital may proceed with collection.
  - For **uninsured patients**: hospital may not pursue collection action unless it has (i) complied with screening for Uninsured Patient Discount eligibility under 210 ILCS 89/, (ii) applied any available discount, and (iii) offered a reasonable payment plan.
  - **No collection agency, law firm, or individual may initiate legal action for non-payment of a hospital bill without the written approval of an authorized hospital employee.** This is enforceable against the collector — a collection suit filed without hospital authorization is improper and can be challenged on the face of the complaint.
- **Reasonable payment plan defined:** the statute leaves "reasonable" undefined, but Illinois Department of Public Health guidance and IL AG enforcement positions treat plans extending the balance over at least the term needed to keep monthly payments under 10% of gross monthly income as presumptively reasonable; harsher terms invite an unfairness claim under ICFA.

### Enforcement

The AG enforces 210 ILCS 88/. The Act does not contain an express private right of action, but **a violation supports a private ICFA claim** under 815 ILCS 505/2 — the standard Illinois patient-side theory. Practical use: cite § 88/30 in every collection-response letter to (a) document compliance failures by the hospital and (b) trigger ICFA exposure.

### Why this matters more in Illinois than in peer states

Illinois's combination of the Fair Patient Billing Act, the Uninsured Patient Discount Act, and ICFA creates a **three-statute trap** for hospitals that cut procedural corners on collections:

1. Skip the pre-collection screening → § 88/30 violation.
2. Bill above 135% of cost to a qualifying uninsured patient → § 89/10 violation.
3. Either violation, asserted via ICFA → fee-shifting, punitives, and AG referral exposure.

The trap is well-known to hospital systems' general counsel; even a letter that names the three statutes together typically moves the bill substantially.

## Hospital lien — Health Care Services Lien Act (770 ILCS 23/)

- **Citations:** **Health Care Services Lien Act, 770 ILCS 23/1 through 23/45**
- **Important framing note:** the original drafting-request framing referenced "**770 ILCS 35/**" as the Illinois hospital-lien act. That was the **old Hospital Lien Act**, which was **repealed by Public Act 93-51 effective July 1, 2003**. The current statute is **770 ILCS 23/**. Liens validly created under the old § 35/ before July 1, 2003 remain enforceable on their original terms, but no new liens have been filed under § 35/ since 2003.
- **Sources:** [770 ILCS 23 article on ilga.gov](https://ilga.gov/legislation/ilcs/ilcs3.asp?ActID=2498&ChapterID=63); [770 ILCS 23/10 on ilga.gov](https://www.ilga.gov/legislation/ilcs/documents/077000230K10.htm); [770 ILCS 23/10 on FindLaw](https://codes.findlaw.com/il/chapter-770-liens/il-st-sect-770-23-10/); practitioner discussion at [sherwoodlawgroup.com Health Care Services Lien Act](https://sherwoodlawgroup.com/blog/2924/health-care-services-lien-act-allows-maximum-recovery/) and [Cassiday Schade overview](https://www.cassiday.com/the-amendment-to-the-illinois-health-care-services-lien-act-to-lien-or-not-to-lien)

### Substance

- Hospitals, health care professionals, and health care providers may file a lien for reasonable charges for treatment of an injured person — **only against the patient's cause of action or recovery from a third party** who caused the injury (e.g., the at-fault driver in an auto wreck). **Not a lien against the patient's home, wages, or bank accounts.**
- **Aggregate 40% cap (§ 23/10(a)):** the total of all liens under the Act may not exceed **40%** of the verdict, judgment, award, settlement, or compromise on the injured person's claim.
- **Per-category one-third sub-cap:** no individual licensed category of health care professional (e.g., physicians) and no individual licensed category of health care provider (e.g., hospitals) may receive more than **one-third** of the total recovery.
- **Equal-half allocation when liens collectively exceed 40%:** when the combined liens hit or exceed 40%, that 40% is split — 20% allocated among health care **professionals**, 20% among health care **providers**, with proportional sharing within each half.

### Notice and perfection

- Lien notice must include: name and address of injured person, date of injury, name and address of the health care professional/provider, name of the party alleged to be liable.
- Lien must be served on the patient (or representative) and all known third-party liable parties and their insurers, **by certified mail with return receipt, or by personal service**, before the third party pays the injured person.
- A judgment, award, or settlement may not be satisfied without the injured person first giving written notice to the lien holder.
- **Document-request enforcement (§ 23/30):** if the lien-asserting provider fails or refuses to comply within **20 days** with a written authorization signed by the patient or representative requesting medical records, treatment notes, and itemization, **the lien is null and void**. This is a routinely overlooked enforcement lever — a patient who methodically requests and documents the 20-day window can defeat a lien on procedural grounds.

### Use

In personal-injury / third-party-liability cases, demand the cost-to-charge documentation and the itemization within the 20-day window. A defective lien is a stronger lever than a substantive challenge to the bill amount because the procedural defect renders the entire lien unenforceable.

## Other Illinois-specific patient-side advantages

### Medical Patient Rights Act — 410 ILCS 50/

- **Statute:** **Medical Patient Rights Act, 410 ILCS 50/3**
- **Source:** [410 ILCS 50 on ilga.gov](https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=1525)
- **Substance:** declaratory bill of rights for medical patients. Subsection (d) is the itemization right discussed above. Other subsections include the right to refuse treatment, the right to privacy and confidentiality of records, and (for maternity care) the right to itemized maternity-care billing.
- **Use:** general "umbrella" cite alongside the Fair Patient Billing Act in itemization-request letters. Establishes that the right to an itemized bill exists in Illinois law independent of the hospital-specific Fair Patient Billing Act.

### ICFA reach over original creditors and third-party collectors

Already discussed under "Illinois Consumer Fraud and Deceptive Business Practices Act." Worth restating: ICFA's reach **over original creditors** (the hospital itself, not just the collection agency or attorney) is the central feature distinguishing Illinois from states whose consumer-protection statutes exempt creditors collecting their own debts. This is the strongest single Illinois lever against a hospital's in-house billing department.

### Wage garnishment limits

- **Statute:** **735 ILCS 5/12-803 through 5/12-819** (Wage Deduction Article)
- **Sources:** [Illinois Legal Aid: defending wage and non-wage garnishments](https://www.illinoislegalaid.org/legal-information/defending-wage-and-non-wage-garnishments); [Nolo: A Guide to Illinois Wage Garnishment Laws](https://www.nolo.com/legal-encyclopedia/illinois-wage-garnishment-law.html)
- **Substance:**
  - Medical-bill creditors (consumer-debt collectors) cannot garnish wages without first obtaining a court judgment.
  - Post-judgment garnishment is capped at the lesser of:
    - **15% of gross wages** (Illinois's cap, lower than the federal 25%), or
    - the amount by which weekly disposable earnings exceed **45 times the federal or state minimum wage, whichever is greater**.
  - If the debtor earns less than the protected weekly amount (currently around $371.25/week using federal minimum wage, higher with Illinois minimum wage), **no wage garnishment is permitted at all**.
  - Social Security, unemployment compensation, workers' compensation, and certain other benefits are **fully exempt** from garnishment.
- **Use:** in response letters to collectors who threaten garnishment without a judgment in hand. The 15% Illinois cap is more protective than the federal 25% baseline.

### Hospital charity care — Community Benefits Act and § 501(r)

- **Statute:** **Community Benefits Act, 210 ILCS 76/**
- **Source:** [210 ILCS 76 on ilga.gov](https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=2465&ChapterID=21)
- **Substance:** every Illinois non-profit hospital must annually file a Community Benefits Plan with the Illinois Attorney General, including documented charity care reported at **actual cost** (using the Medicare cost-to-charge ratio), separate from other community-benefit categories. Combined with federal IRS § 501(r) requirements, this creates a robust public-record framework for documenting that a hospital does in fact offer charity care.
- **Exemptions:** Act does not apply to (i) hospitals operated by a unit of government, (ii) hospitals outside a Metropolitan Statistical Area, or (iii) hospitals with 100 or fewer beds.
- **Use:** before sending a financial-assistance request, pull the hospital's most recent Community Benefits Plan filing from the AG's website to identify the hospital's stated charity-care policy. Quoting back the hospital's own published policy is a stronger lever than citing § 501(r) generically. Use Dollar For at [dollarfor.org](https://dollarfor.org/) for additional screening.

### Property tax exemption pressure for nonprofit hospitals

Illinois hospitals' property tax exemption is conditioned on documented charity care under **35 ILCS 200/15-86** (added 2012, refined by *Carle Foundation v. Cunningham Twp.*, 2017 IL 120427). A hospital that fails to provide adequate charity care risks losing its exemption — a meaningful ancillary lever in negotiations with non-profit hospitals over individual bills, because the institution's tax counsel is acutely aware of how a documented failure to follow charity-care policy can be aggregated to threaten exemption status.

## Quick reference for letter rendering

When the LLM renders an Illinois-bound letter, substitute these defaults:

- **State statute (itemization right):** **410 ILCS 50/3(d)** (Medical Patient Rights Act) **and 210 ILCS 88/15** (Fair Patient Billing Act). Itemization is on written request — no automatic-delivery duty under Illinois law (unlike Georgia's 6-day automatic rule).
- **State insurance department (CC line):** Illinois Department of Insurance, Consumer Services Section, 320 W. Washington Street, 4th Floor, Springfield, IL 62767 (toll-free Office of Consumer Health Insurance 1-877-527-9431; complaints email doi.complaints@illinois.gov).
- **State AG consumer protection (CC line):** Illinois Attorney General, Consumer Fraud Bureau / Health Care Bureau, 100 W. Randolph Street, 12th Floor, Chicago, IL 60601 (Health Care Bureau Helpline 1-877-305-5145; consumer hotline 1-800-386-5438).
- **Small-claims court name:** **Circuit Court of [county], Small Claims Division** (Supreme Court Rule 281, $10,000 limit).
- **Filing fee (in 30-day warning):** "$89-$284 depending on county and claim size; fee waiver available under Illinois Supreme Court Rule 298."
- **Statute of limitations (in 30-day warning):** "**735 ILCS 5/13-206 (ten years for breach of written contract).**" If the admission was without a signed financial-responsibility form, substitute "735 ILCS 5/13-205 (five years for oral contract or unwritten obligation)."
- **For uninsured patients:** Lead with **210 ILCS 89/ (Hospital Uninsured Patient Discount Act)** — the 135%-of-cost cap. State the income basis, request the hospital's filed Worksheet C cost-to-charge ratio, and demand recalculation. Pair with 210 ILCS 88/30 (pre-collection procedure) and 815 ILCS 505/2 (ICFA fee-shifting).
- **For provider-side disputes (vs. insurer-side):** Cite **815 ILCS 505/2 and 505/10a** (ICFA private right of action with attorney's fees and punitive damages) in every letter to an Illinois hospital or third-party collector. This is Illinois's strongest deterrent against further collection action.
- **For insurer-side bad-faith disputes:** Cite **215 ILCS 5/155** for the vexatious-and-unreasonable remedy (attorney's fees + costs + 60% of recovery / $60,000 / excess over offer, whichever greatest). Cite **§§ 5/154.5-154.7** (improper claims practices) in the parallel IDOI complaint, not as a litigation count.
- **For ground ambulance balance bills:** Check date of service. **On or after July 1, 2025:** cite the Consumer Protection from Surprise Health Care Billing Act (added by SB 2405, 103rd GA). **Before July 1, 2025:** Illinois state law provides no protection; rely on federal NSA only for what it covers (which excludes ground ambulance), plus general contract/UCC § 2-305 challenges. **Do not cite 215 ILCS 5/356z.3a for ground ambulance — that section expressly excludes ground ambulance.**
- **For credit-report violations:** cite **815 ILCS 505/2EEEE** (Public Act 103-0648, effective Jan 1, 2025) as an ICFA-anchored ban on adverse medical-debt credit reporting in Illinois. Note that federal preemption posture under the October 2025 CFPB interpretive rule is being litigated; the AG complaint route remains available.
- **For hospital liens (third-party recovery cases):** cite **770 ILCS 23/10** (40% aggregate cap, one-third per-category cap, equal-half allocation when liens exceed 40%) and **770 ILCS 23/30** (20-day medical-records-request rule — failure to comply renders the lien null and void).

## Key Illinois-specific advantages

Worth keeping in mind when triaging an Illinois patient's bills:

1. **Hospital Uninsured Patient Discount Act (210 ILCS 89/) — 135% of cost cap.** The single strongest Illinois lever for uninsured patients. Hard-coded limit on what the hospital can collect, anchored to the hospital's own audited Medicare cost report, plus a 25%-of-family-income annual collection cap. No peer state has a more prescriptive uninsured-discount mechanism.
2. **Fair Patient Billing Act (210 ILCS 88/) — pre-collection procedural trap.** Mandatory 30-day payment-plan offer for insured patients, mandatory screening + payment plan for uninsured patients, hospital-employee written-authorization requirement before any collection lawsuit. A hospital that skips any step exposes itself to ICFA liability.
3. **Illinois Consumer Fraud and Deceptive Business Practices Act (815 ILCS 505/) — broadest in the country with original-creditor reach.** Private right of action, attorney's fees and costs to prevailing plaintiffs, punitive damages for willful conduct, and (critically) reach over the hospital itself, not just third-party debt collectors. Pair with § 89/ or § 88/ violations for fee-shifting.
4. **10-year written-contract SOL (735 ILCS 5/13-206).** Tied for the longest in the country. Patients have a long window to investigate, dispute, and challenge bills — though partial payment restarts the clock, so caution is needed.
5. **Medical-debt credit-reporting ban (815 ILCS 505/2EEEE, effective Jan 1, 2025).** Adverse medical-debt credit reporting is itself an ICFA violation. Strongest state-level credit-report protection available, subject to ongoing federal-preemption litigation under the October 2025 CFPB interpretive rule.
6. **§ 155 bad-faith remedy.** Up to **$60,000 statutory penalty** (or 60% of recovery or excess over offer, whichever greatest), **plus attorney's fees and costs**, against fully-insured carriers that handle claims in a vexatious-and-unreasonable manner. Stronger fee-shifting than common-law bad-faith states.
7. **Corporate-defendant disadvantage in small-claims court.** Illinois requires corporations and LLCs (including hospitals) to be represented by a licensed attorney in small-claims actions, while individual plaintiffs may appear pro se. The asymmetric cost makes small-claims a particularly effective lever for sub-$10,000 disputes in Illinois.
8. **Health Care Services Lien Act 20-day records-request rule (770 ILCS 23/30).** Procedural defeat of a lien for failure to produce records on written request — routinely overlooked, easy to invoke, and dispositive when triggered.
9. **Health Care Bureau within the AG's office.** Dedicated unit (helpline 1-877-305-5145) with a documented track record of directly intervening to resolve consumer medical-billing disputes — distinct from a general consumer-complaint process and unusually responsive among state AG offices.

The headline framing for any Illinois patient: **135%-of-cost cap (if uninsured), three-statute trap (88/89/505) for hospital procedural violations, broadest-in-country ICFA reach, longest-in-country 10-year written-contract SOL.** If the patient was uninsured at the time of service, the Uninsured Patient Discount Act is almost always the strongest opening cite; if the patient was insured, ICFA + § 155 is the strongest combination.
