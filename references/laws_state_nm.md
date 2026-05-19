# New Mexico state pack

The fully-worked state-law layer for New Mexico patients. The LLM uses this when the patient's state is New Mexico. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md); Tennessee at [`laws_state_tn.md`](laws_state_tn.md). All citations verified against public sources as of 2026-05-19. Re-verify annually.

Three things make New Mexico's patient-side leverage unusually strong:

1. **The Patients' Debt Collection Protection Act** (N.M. Stat. § 57-32-1 et seq., effective July 1, 2021) requires hospitals to screen every patient for indigency, public coverage, and financial assistance before billing or collecting, and **shields indigent patients (household income at or below 200% FPL) from collection actions, lawsuits, garnishment, and credit reporting entirely**. This is one of the strongest pre-collection screening regimes in the country.
2. **The New Mexico Unfair Practices Act** (N.M. Stat. § 57-12-1 et seq.) is a UDAP statute with **treble damages, mandatory attorney's fees to a prevailing patient, and reach over original creditors** — including the hospital's in-house billing department.
3. **First-party insurance bad faith is a common-law tort** in New Mexico (Sloan v. State Farm, 2004), separate from the statutory § 59A-16-30 private right, and supports **punitive damages** on an unreasonable denial or delay even without a culpable mental-state finding for compensatory damages.

## Hospital itemization right

- **Statute (general patient right):** **N.M. Stat. § 24-7B-1 et seq.** — the Katie Faith Martinez Patients' Bill of Rights Act, which guarantees every patient the right to "receive an itemized, detailed and understandable explanation of health care charges regardless of the source of payment."
- **Statute (debt-collection screening + billing detail):** **N.M. Stat. § 57-32-6** — Patients' Debt Collection Protection Act, requires every bill from a health care facility, third-party provider, or medical creditor to disclose the charges, whether health insurance was verified, the results of indigency/public-coverage screening, and whether insurance or a public program has been or will be billed.
- **Statute (facility-fee transparency, effective Jan 1, 2027):** **Fair Pricing for Routine Medical Care Act** (HB 306, 2026), requires standardized itemized bills that separately identify any facility fee and provide a contact point to contest charges.
- **Sources:** [nmlegis.gov, HB 493 (2011, Patients' Bill of Rights enactment)](https://www.nmlegis.gov/sessions/11%20Regular/bills/house/HB0493.html); [law.justia.com/codes/new-mexico/chapter-57/article-32/section-57-32-6](https://law.justia.com/codes/new-mexico/chapter-57/article-32/section-57-32-6/); [osi.state.nm.us, Patients' Debt Collection Protection Act consumer page](https://www.osi.state.nm.us/en/consumer-assistance/patients-debt-collection-protection-act/); [nmlegis.gov, HB 306 (2026, Fair Pricing for Routine Medical Care Act)](https://www.nmlegis.gov/Sessions/26%20Regular/bills/house/HB0306.HTML)
- **What it requires:**
  - Under the Patients' Bill of Rights, an itemized, detailed, understandable explanation of charges to every patient regardless of payer.
  - Under § 57-32-6, every bill must include itemized charges, insurance-verification status, indigency-screening results, and assistance-program information.
- **Scope:** All "health care facilities" (broader than just hospitals — clinics, surgery centers, ER departments).
- **Private right of action:** Patients' Bill of Rights complaints route to the **New Mexico Medical Board** (provider discipline) rather than a direct civil remedy. § 57-32 violations are enforceable by the Attorney General (§ 57-32-10) and may support a Unfair Practices Act count under § 57-12-1 et seq. with treble damages and attorney's fees.
- **ERISA:** Not preempted — regulates the provider, not the plan.

## Insurance Trade Practices Act — private right of action

- **Statute:** **N.M. Stat. § 59A-16-1 et seq.** (Trade Practices and Frauds Article of the Insurance Code), private cause of action at **§ 59A-16-30**.
- **Source:** [law.justia.com/codes/new-mexico/chapter-59a/article-16/section-59a-16-30](https://law.justia.com/codes/new-mexico/chapter-59a/article-16/section-59a-16-30/); unfair claims practices defined at [§ 59A-16-20](https://law.justia.com/codes/new-mexico/chapter-59a/article-16/section-59a-16-20/)
- **Substance:** Any person who has suffered damages from an insurer's or agent's violation of Article 16 (including the unfair-claims-practices list at § 59A-16-20 — misrepresenting policy provisions, failing to acknowledge claims promptly, failing to conduct reasonable investigation, denying without basis, etc.) may sue in district court for **actual damages, plus costs, plus attorney's fees** where the insurer's violation was willful.
- **Private right confirmed:** *Hovet v. Allstate Insurance Co.*, 2004-NMSC-010, 135 N.M. 397 — the New Mexico Supreme Court confirmed that § 59A-16-30 creates a direct private right of action, and extended it to third-party claimants in liability-insurance contexts where the insurer fails to make good-faith settlement efforts. Source: [law.justia.com/cases/new-mexico/supreme-court/2004/9244.html](https://law.justia.com/cases/new-mexico/supreme-court/2004/9244.html).
- **Standing limit:** the private right reaches insurance companies and their agents; it does **not** reach attorneys representing insurers.
- **Use for medical-billing disputes:** plead § 59A-16-30 alongside common-law bad faith when the insurer denied a covered claim, misrepresented benefits, failed to investigate, or delayed payment. The willfulness finding unlocks attorney's fees.
- **ERISA preemption:** § 59A-16-30 is preempted as applied to self-funded ERISA employer plans. In play for fully-insured plans, Medicaid managed care, individual/marketplace policies.

## Bad-faith failure to pay (first-party common-law tort)

- **Authority:** **Sloan v. State Farm Mut. Auto. Ins. Co.**, 2004-NMSC-004, 135 N.M. 106, 85 P.3d 230 — controlling New Mexico Supreme Court authority on first-party insurance bad faith.
- **Source:** [law.justia.com/cases/new-mexico/supreme-court/2004/953c.html](https://law.justia.com/cases/new-mexico/supreme-court/2004/953c.html)
- **Substance:**
  - First-party bad faith is a common-law tort separate from breach of contract and from the statutory § 59A-16-30 claim. Sloan's central holding: in a first-party context, an **unreasonable** denial or delay of payment is enough to recover compensatory damages, and if the denial or delay was **"frivolous or unfounded"** that finding alone supports submitting punitive damages to the jury — no additional culpable-mental-state finding required.
  - "Failure to timely investigate, evaluate or pay a claim is a bad faith breach of the duty to act honestly and in good faith in the performance of the insurance contract."
- **Demand-and-wait requirement:** none — Sloan is common-law, not statutory. Best practice is still a written demand by certified mail giving the insurer a reasonable period (often 30-60 days) to cure before suit; it tightens the record and forecloses excuses.
- **Damages available:**
  - Contract damages (the unpaid claim)
  - Tort damages including emotional distress where proven
  - Punitive damages on a "frivolous or unfounded" denial (Sloan)
  - Attorney's fees recoverable via the companion § 59A-16-30 statutory claim where willfulness is shown
- **ERISA preemption:** Sloan-pattern bad-faith claims are preempted for self-funded ERISA plans. Fully-insured plans, Medicaid managed care, and individual/marketplace policies remain in play.

## Surprise Billing Protection Act

- **Statute:** **N.M. Stat. § 59A-57A-1 et seq.** — Surprise Billing Protection Act, plus the provider-side prohibition at **N.M. Stat. § 59A-16-21.3**.
- **Original enactment:** HB 207 (2019), effective January 1, 2020. (Often referred to in shorthand as "HB 35" elsewhere; the enacted vehicle was HB 207 in the 2019 Regular Session.)
- **Sources:** [law.justia.com/codes/new-mexico/chapter-59a/article-57a](https://law.justia.com/codes/new-mexico/chapter-59a/article-57a/); [nmlegis.gov, HB 207 (2019)](https://www.nmlegis.gov/Sessions/19%20Regular/bills/house/HB0207.HTML); provider-side prohibition at [§ 59A-16-21.3](https://law.justia.com/codes/new-mexico/chapter-59a/article-16/section-59a-16-21-3/); OSI consumer guidance at [osi.state.nm.us, surprise medical bills](https://www.osi.state.nm.us/en/consumer-assistance/insurance-types/managed-health-care-review/help-with-a-surprise-medical-bill/)

### What it prohibits

- Balance billing for **emergency services** rendered by an out-of-network (OON) provider or facility.
- Balance billing for **non-emergency services** rendered by an OON provider at an **in-network** facility (ancillary services — anesthesia, radiology, pathology, lab, hospitalist, etc.).
- Patient cost-sharing is capped at the in-network amount and counts toward the in-network deductible and out-of-pocket maximum.
- Insurers must use the rate-setting and dispute mechanisms in § 59A-57A-8 (and apply the cost-management permissions in § 59A-57A-9) rather than passing balances through to the patient.

### Where New Mexico goes beyond the federal No Surprises Act

- Predates the federal NSA (effective Jan 1, 2020 vs federal Jan 1, 2022) and continues to govern state-regulated plans in parallel.
- Provider-side prohibition at § 59A-16-21.3 directly bars the provider (not just the carrier) from "knowingly submitting a surprise bill" to the patient.
- Patient-protection appeal mechanism integrated with the Patient Protection Act for carrier-determination disputes.

### Caveats

- **ERISA preemption:** the Act does not reach self-funded ERISA employer plans, which rely on the federal NSA alone.
- **Excludes Medicare, Medicaid, workers' comp.**
- See ground-ambulance section below — New Mexico's Act **does not** cover ground ambulance, unlike Georgia, California, Maryland, New York, Ohio, and several other states.

## Regulatory agencies

### Office of Superintendent of Insurance (OSI)

- **Online complaint:** [osi.state.nm.us/en/complaints](https://www.osi.state.nm.us/en/complaints/)
- **Phone:** main consumer line **1-855-4-ASK-OSI** (1-855-427-5674); switchboard (505) 827-4601
- **Mail:**
  > Office of Superintendent of Insurance
  > Consumer Assistance Bureau
  > 1120 Paseo de Peralta
  > Santa Fe, NM 87501
  > (P.O. Box 1689, Santa Fe, NM 87504-1689)
- **Authority:** all insurance companies licensed in New Mexico — fully-insured health plans, HMOs, PPOs, Medicare supplement. Administers the Surprise Billing Protection Act and the Article 16 unfair claims practices regime. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and does not regulate providers, hospitals, or debt collectors (route to AG).

### New Mexico Attorney General (NM DOJ) — Consumer Protection Division

- **Online complaint:** [nmdoj.gov/get-help/submit-a-complaint](https://nmdoj.gov/get-help/submit-a-complaint/) and complaint-type selector at [secure.nmdoj.gov/ECS/ECSIntakeTypeGroups](https://secure.nmdoj.gov/ECS/ECSIntakeTypeGroups)
- **Phone:** Albuquerque main **(505) 717-3500**; toll-free Consumer Hotline **1-844-255-9210**; statewide intake line (800) 678-1508
- **Mail:**
  > New Mexico Department of Justice
  > Office of the Attorney General
  > Consumer Protection Division
  > 201 3rd St NW, Suite 300
  > Albuquerque, NM 87102
- **Authority:** enforces the Unfair Practices Act (N.M. Stat. § 57-12-1 et seq.) and the Patients' Debt Collection Protection Act (§ 57-32-10), reaching providers, hospitals, original creditors, debt buyers, and third-party collectors — exactly the gap not covered by OSI. Use for hospital in-house billing disputes, deceptive billing, balance-billing complaints, and PDCPA enforcement.

## Unfair Practices Act — UDAP private right

- **Statute:** **N.M. Stat. § 57-12-1 et seq.** — New Mexico Unfair Practices Act (UPA); private remedies at **§ 57-12-10**.
- **Source:** [law.justia.com/codes/new-mexico/chapter-57/article-12/section-57-12-10](https://law.justia.com/codes/new-mexico/chapter-57/article-12/section-57-12-10/); short title at [§ 57-12-1](https://law.justia.com/codes/new-mexico/chapter-57/article-12/section-57-12-1/)
- **Substance:** Any person who suffers loss of money or property from an unfair, deceptive, or unconscionable trade practice may sue for **actual damages or $100, whichever is greater**. On a finding that the defendant **willfully** engaged in the practice, the court **may** treble actual damages (or award **$300**, whichever is greater). The court **shall** award **attorney's fees and costs to a prevailing patient**.
- **Reach:** original creditors included — the hospital itself, not just third-party collectors, can be liable for deceptive billing practices (misrepresenting amounts owed, threatening lawsuits without intent or right to sue, contacting at prohibited hours, misrepresenting insurance-network status, double-billing).
- **Why it matters for medical bills:** combines with § 57-32 (Patients' Debt Collection Protection Act) as the enforcement engine for the patient-screening, billing-disclosure, and indigent-protection rules. A § 57-32 violation typically also supports a § 57-12 count, unlocking treble damages and mandatory fees.
- **Statute of limitations:** four years (N.M. Stat. § 37-1-4, "actions not otherwise provided").

## Small claims court — Magistrate Court / Metropolitan Court

- **Court names:**
  - **Magistrate Court** — all counties except Bernalillo
  - **Metropolitan Court** — Bernalillo County (Albuquerque metro)
- **Jurisdictional limit:** **$10,000**, exclusive of interest and costs
  - Magistrate Court: **N.M. Stat. § 35-3-3**
  - Metropolitan Court: **N.M. Stat. § 34-8A-3**
- **Sources:** [law.justia.com/codes/new-mexico/chapter-35/article-3/section-35-3-3](https://law.justia.com/codes/new-mexico/chapter-35/article-3/section-35-3-3/); [law.justia.com/codes/new-mexico/chapter-34/article-8a/section-34-8a-3](https://law.justia.com/codes/new-mexico/chapter-34/article-8a/section-34-8a-3/)
- **Filing fees (2024-2025):**
  - Claims up to $2,500: **$77**
  - Claims $2,501-$5,000: **$132**
  - Claims $5,001-$10,000: **$187**
  - Fee waiver available on a showing of indigency
- **Attorney rules:** permitted, not required. Designed for pro se use — simplified pleadings, relaxed evidence rules. Corporations may appear through a non-attorney officer.
- **Jury trial:** available on demand in magistrate and metro court (six-person jury); jury fees additional.

## Statute of limitations

- **Written contracts (six years):** **N.M. Stat. § 37-1-3** — actions on notes and other written instruments must be commenced within six years after the cause of action accrues.
- **Open accounts / oral contracts / "actions not otherwise provided" (four years):** **N.M. Stat. § 37-1-4** — accounts, unwritten contracts, injuries to property, conversion, fraud, and any action not otherwise provided.
- **Sources:** [law.justia.com/codes/new-mexico/chapter-37/article-1/section-37-1-3](https://law.justia.com/codes/new-mexico/chapter-37/article-1/section-37-1-3/); [law.justia.com/codes/new-mexico/chapter-37/article-1/section-37-1-4](https://law.justia.com/codes/new-mexico/chapter-37/article-1/section-37-1-4/)

Most hospital admissions involve a signed financial-responsibility form — facially a written contract, so § 37-1-3's six years would apply. **However**, New Mexico courts have treated hospital billing relationships as "accounts" subject to § 37-1-4's four-year period even where the patient signed a generic responsibility form, because the underlying obligation is an open account for services rendered at variable prices rather than a sum-certain promissory note. The safer cite in a dispute letter is **four years**; the hospital bears the burden to show the agreement is a true written contract sufficient to invoke six years.

Partial payment or written acknowledgment can restart or extend the clock. **Do not make a partial payment on a time-barred debt without legal advice.**

## Ground ambulance balance-billing

**Not covered by New Mexico state surprise-billing law.** The Surprise Billing Protection Act (§ 59A-57A-1 et seq.) and the provider-side prohibition at § 59A-16-21.3 **exclude ambulance transportation** from the definition of covered "emergency care" and "health care service." This means:

- Patients with state-regulated plans (fully insured) **can still be balance-billed** by an out-of-network ground ambulance provider in New Mexico.
- The federal No Surprises Act also explicitly excludes ground ambulance.
- Air ambulance is covered by the federal NSA.

This is the single biggest gap in New Mexico's surprise-billing regime relative to states like Georgia (HB 286, 2024), California, Maryland, and New York. If a New Mexico patient receives a ground-ambulance bill, the available levers are:

1. **The Patients' Debt Collection Protection Act** (§ 57-32) still applies — the ambulance creditor must screen for indigency, public coverage, and assistance before collecting.
2. **UDAP / Unfair Practices Act** (§ 57-12-10) for deceptive or unconscionable billing.
3. **Negotiation against the Medicare rate** (typically the ambulance industry's lowest accepted reimbursement) as the floor for a settlement offer.

Sources: [law.justia.com/codes/new-mexico/chapter-59a/article-57a](https://law.justia.com/codes/new-mexico/chapter-59a/article-57a/); [osi.state.nm.us, bulletin 2024-020 — Surprise Billing data call](https://www.osi.state.nm.us/en/news/bulletin-2024-020/); CMS action plan for ground ambulance bills at [cms.gov/medical-bill-rights/help/plan/insurance-ground-ambulance-bill](https://www.cms.gov/medical-bill-rights/help/plan/insurance-ground-ambulance-bill).

## Credit reporting — Patients' Debt Collection Protection Act

- **Statute:** **N.M. Stat. § 57-32-1 et seq.** — Patients' Debt Collection Protection Act (PDCPA), effective July 1, 2021. Implementing rules at **13.10.39 NMAC**.
- **Sources:** [law.justia.com/codes/new-mexico/chapter-57/article-32](https://law.justia.com/codes/new-mexico/chapter-57/article-32/); [nmlegis.gov, SB 71 (2021)](https://www.nmlegis.gov/Sessions/21%20Regular/bills/senate/SB0071.html); [srca.nm.gov, 13.10.39 NMAC implementing rule](https://srca.nm.gov/parts/title13/13.010.0039.html); [osi.state.nm.us, PDCPA consumer page](https://www.osi.state.nm.us/en/consumer-assistance/patients-debt-collection-protection-act/)
- **Indigency definition:** household income at or below **200% of the federal poverty level**, calculated using MAGI rules used for Medicaid eligibility.
- **Pre-collection screening (§ 57-32-3, § 57-32-6):** Before billing or any collection action, a health care facility must verify health-insurance coverage, screen for public coverage (Medicaid, Medicare, marketplace), and screen for indigency and any other available financial assistance. The patient must be notified in writing within 30 days if determined indigent.
- **Indigent-patient protections (§ 57-32-4):** For patients determined indigent, the facility, third-party provider, or medical creditor:
  - **Shall not pursue** collection actions, lawsuits, garnishment, wage deduction, bank-account levy, or property liens
  - **Shall terminate** any pending collection action upon indigency determination
  - **Shall not hire** third parties to collect
  - **Shall not** report the debt to a consumer reporting agency
  - **Shall not** sell or assign the debt to a debt buyer
- **Adverse-action waiting period:** under the broader Act and 13.10.39 NMAC, no adverse credit reporting during the screening and notification window following the bill becoming due.
- **Voluntary-payment protection (§ 57-32-7):** Voluntary payments by an indigent patient do **not** extend the statute of limitations, admit liability, or waive defenses.
- **Enforcement:** New Mexico Attorney General, complaint process at § 57-32-10; private cause of action available via the Unfair Practices Act overlay (§ 57-12-1 et seq.) for treble damages and attorney's fees.

**Federal preemption posture is in flux.** The CFPB issued an October 2025 interpretive rule taking the position that the FCRA preempts state laws restricting medical-debt credit reporting. If that survives challenge, it limits the credit-reporting prong of § 57-32-4, but does not affect the collection-action, lawsuit, garnishment, and assignment prohibitions, which rest on different statutory bases.

## Hospital charity care

- **Statute:** **N.M. Stat. § 27-5-1 et seq.** — Indigent Hospital and County Health Care Act.
- **Source:** [law.justia.com/codes/new-mexico/2019/chapter-27/article-5/section-27-5-2](https://law.justia.com/codes/new-mexico/2019/chapter-27/article-5/section-27-5-2/); county health-care fund mechanics at [§ 27-5-4](https://codes.findlaw.com/nm/chapter-27-public-assistance/nm-st-sect-27-5-4.html)
- **Substance:** Counties are responsible for the care and health-care services of indigent patients, supported by local revenues that match federal Medicaid funds and supply countywide health planning. Hospitals owned by a county, and hospitals contracted with a county, must provide charity care to indigent patients and may draw on the county health-care assistance fund.
- **Indigent patient defined:** a person who can normally support themselves but, given income, assets, and other necessities, cannot pay the cost of ambulance transport or medical care.
- **Per-patient leverage:** cite ICHCA participation and county contract in dispute letters to county hospitals; the Act is a recognized state-law basis for charity care above the federal § 501(r) floor.
- **Federal floor:** non-profit hospitals are separately bound by IRS § 501(r) (see `laws_federal.md`). Combining the two creates layered obligations.
- **PDCPA overlay:** § 57-32 requires indigency screening at every facility, not just county-owned ones, so charity-care assessment is now universal.
- **Screening tool:** Dollar For at [dollarfor.org/state_sheet/new-mexico](https://dollarfor.org/state_sheet/new-mexico/).

## Hospital lien statute

- **Citations:** **N.M. Stat. §§ 48-8-1 through 48-8-7**
- **Sources:** [law.justia.com/codes/new-mexico/chapter-48/article-8](https://law.justia.com/codes/new-mexico/chapter-48/article-8/); creation/exception at [§ 48-8-1](https://law.justia.com/codes/new-mexico/chapter-48/article-8/section-48-8-1/); persons liable / limitation at [§ 48-8-3](https://law.justia.com/codes/new-mexico/chapter-48/article-8/section-48-8-3/); settlement-rights limit at [§ 48-8-7](https://www.lawserver.com/law/state/new-mexico/nm-statutes/new_mexico_statutes_48-8-7)
- **Substance:** Hospitals may file a lien for reasonable charges, **only against the patient's cause of action or settlement proceeds from a third party** who caused the injury (e.g., the at-fault driver in a car wreck). **Not a lien on the patient's home, wages, or bank accounts.**
- **Perfection requirements:**
  - File a written notice with the county clerk in the county where the hospital is located.
  - Mail the filed notice by certified mail to the patient (or counsel of record) and to the insurance carrier of the alleged tortfeasor.
  - Liability of the payor to satisfy the lien continues for **one year after payment** of damages/settlement to the patient.
- **Enforcement (§ 48-8-3):** the hospital may sue to enforce the lien against the person, firm, or corporation that paid the patient; on a successful enforcement suit the hospital may recover reasonable attorney's fees and filing costs (these fee-shifting provisions cut against the patient/settlement payor, not the patient on the underlying bill).
- **Patient leverage:** scrutinize notice and perfection carefully; defective filings or missed certified-mail steps invalidate the lien. The reasonableness of charges is also a recognized defense, particularly when the hospital's chargemaster rate exceeds what it would have accepted from the patient's own insurer.

## Wage garnishment

- **Statute:** **N.M. Stat. § 35-12-1 et seq.** (magistrate court) and federal Consumer Credit Protection Act caps (15 U.S.C. § 1673).
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a court judgment. Post-judgment garnishment is capped at the lesser of (i) 25% of disposable earnings, or (ii) the amount by which weekly disposable earnings exceed 40 times the federal minimum wage (New Mexico applies the higher 40× floor in some contexts vs the federal 30× minimum — verify against current statute for the specific dispute).
- **PDCPA overlay:** under § 57-32-4, garnishment is **categorically prohibited** against an indigent patient (income at or below 200% FPL), regardless of judgment status. The Act took effect July 1, 2021 and is the strongest pre-emptive defense against medical-debt garnishment in New Mexico.

## Quick reference for letter rendering

When the LLM renders a New Mexico-bound letter, substitute these defaults:

- **State statute (itemization right):** N.M. Stat. § 24-7B-1 et seq. (Katie Faith Martinez Patients' Bill of Rights) for the itemized-explanation right; **N.M. Stat. § 57-32-6** for the billing-detail disclosure rule (insurance-verification status, indigency-screening outcome, assistance-program information must be on the bill).
- **State insurance department (CC line):** Office of Superintendent of Insurance, Consumer Assistance Bureau, 1120 Paseo de Peralta (P.O. Box 1689), Santa Fe, NM 87501-1689, **1-855-427-5674**, [osi.state.nm.us/en/complaints](https://www.osi.state.nm.us/en/complaints/)
- **State AG consumer protection (CC line):** New Mexico Department of Justice, Consumer Protection Division, 201 3rd St NW, Suite 300, Albuquerque, NM 87102, **1-844-255-9210**, [nmdoj.gov/get-help/submit-a-complaint](https://nmdoj.gov/get-help/submit-a-complaint/)
- **Small-claims court name:** **Magistrate Court of [county]** (or **Metropolitan Court of Bernalillo County** in Albuquerque)
- **Filing fee (in 30-day warning):** "$77 for claims up to $2,500, $132 up to $5,000, $187 up to $10,000"
- **Statute of limitations (in 30-day warning):** "N.M. Stat. § 37-1-4 (four years for accounts and unwritten contracts; six years under § 37-1-3 if the obligation qualifies as a written contract — generally treated as four years for hospital open accounts)"
- **For insurer-side disputes:** Cite **N.M. Stat. § 59A-16-30** (private right of action with attorney's fees on willful violations) plus a common-law bad-faith count under **Sloan v. State Farm, 2004-NMSC-004** (punitive damages on frivolous-or-unfounded denial).
- **For provider-side disputes (vs. insurer-side):** Cite **N.M. Stat. § 57-12-10** (Unfair Practices Act private remedy — actual or $100 minimum, treble damages on willful violation, **mandatory attorney's fees to prevailing patient**) plus § 57-32 PDCPA pre-collection screening duties.
- **For indigent patients (≤200% FPL):** Cite **N.M. Stat. § 57-32-4** as a categorical bar to collection action, lawsuit, garnishment, lien, sale to a debt buyer, and credit reporting. This is the single highest-leverage New Mexico-specific cite when applicable.

## Key New Mexico-specific patient advantages

Worth keeping in mind when triaging a New Mexico patient's bills:

1. **Universal indigency screening and protection (PDCPA, § 57-32)** — every health-care facility must screen every patient for indigency and public coverage **before** billing or collecting, and indigent patients get an absolute shield against collection actions, lawsuits, garnishment, liens, debt-buyer sales, and credit reporting. No other state in the kit's tracked set has a comparably strong pre-collection screening regime.
2. **Attorney's-fee recovery is mandatory for a prevailing patient under UPA § 57-12-10**, and treble damages are available on willful violations. Always include UPA framing in 30-day warning letters to New Mexico providers — fee recovery makes pro bono or contingency counsel realistically interested in even modest disputes.
3. **First-party bad faith is common-law and supports punitive damages on an unreasonable denial alone** (Sloan, 2004). The statutory § 59A-16-30 layer adds attorney's fees on willfulness. Plead both.
4. **Original-creditor reach** — UPA covers the hospital's in-house billing department, not just third-party collectors. Combined with PDCPA, this means the hospital itself bears direct UDAP liability for deceptive billing.
5. **Ground-ambulance gap** — note as a caveat, not an advantage: New Mexico's Surprise Billing Protection Act excludes ground ambulance, so balance bills from ambulance providers remain a live risk. The PDCPA and UPA still apply as fallback levers.
