# New Jersey state pack

The fully-worked state-law layer for New Jersey patients. The LLM uses this when the patient's state is New Jersey. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Three things make New Jersey's patient-side leverage unusually strong:

1. **State-funded charity care is mandatory at every acute-care hospital** under N.J.S.A. 26:2H-18.51 et seq. Patients at or below 200% of FPL pay nothing for medically necessary inpatient and outpatient services; sliding-scale assistance reaches 300% of FPL. Funded by the Health Care Subsidy Fund — hospitals are reimbursed, so they have no economic disincentive to grant it.
2. **The Louisa Carman Medical Debt Relief Act** (P.L. 2024, c.48, N.J.S.A. 56:11-56 et seq.) is the most aggressive state-level medical-debt statute in the country: total ban on credit-bureau reporting of medical debt, 3% interest cap, 120-day pre-collection waiting period, mandatory charity-care screening, and a wage-garnishment ban for households below 600% of FPL.
3. **The Out-of-Network Consumer Protection Act** (N.J.S.A. 26:2SS-1 et seq., effective 2018, pre-dating the federal NSA) holds patients harmless from balance bills for emergency care and inadvertent OON services at in-network facilities, with an arbitration backstop for the provider-payer dispute.

Two things to know that **temper** New Jersey's reputation:

- **The Consumer Fraud Act's "learned professional" exception** insulates hospitals, physicians, and nursing homes from CFA claims when operating within their professional capacity. The CFA's treble damages and fee-shifting are a powerful lever in other industries, but a much weaker lever against the hospital itself. It still reaches third-party debt collectors and ancillary commercial conduct.
- **The Insurance Fair Conduct Act (IFCA)** created a private right of action for UCSPA violations in 2022 — but the legislature narrowed it to **UM/UIM auto claims only**. It does not reach health-insurance bad faith.

## Hospital itemization right

- **Statute:** **N.J.S.A. 26:2H-12.8** (rights of persons admitted to a general hospital) implemented by **N.J.A.C. 8:43G-4.1** (patient rights regulation)
- **Source:** [law.justia.com/codes/new-jersey/title-26/section-26-2h-12-8](https://law.justia.com/codes/new-jersey/title-26/section-26-2h-12-8/); regulation at [law.cornell.edu/regulations/new-jersey/N-J-A-C-8-43G-4-1](https://www.law.cornell.edu/regulations/new-jersey/N-J-A-C-8-43G-4-1); official Patient's Bill of Rights at [nj.gov/health/healthcarequality/patients-families/patient-your-rights](https://www.nj.gov/health/healthcarequality/patients-families/patient-your-rights/)
- **What it requires:**
  - On request, the patient or responsible party must be provided with an itemized bill and an explanation of charges.
  - The patient has a right to appeal charges, and the hospital must provide an explanation of the appeal procedure.
  - The patient has the right to a copy of the hospital's payment rates, regardless of source of payment.
  - Information about financial-assistance sources (including Charity Care) must be disclosed.
- **Scope:** Every licensed general hospital in New Jersey. Unlike Georgia's automatic 6-business-day duty, the NJ duty is **request-triggered** — send the request in writing (certified mail) to crystallize the paper trail.
- **Medical and billing records statute:** **N.J.S.A. 26:2H-5n** separately requires the hospital to provide medical and billing records on request, with statutory fee caps; source at [law.justia.com/codes/new-jersey/title-26/section-26-2h-5n](https://law.justia.com/codes/new-jersey/title-26/section-26-2h-5n/).
- **Private right of action:** None directly under the patient-rights regulation. Enforcement runs through the Department of Health (licensure consequences) and through ancillary doctrines (breach of contract for the underlying charge, common-law fraud, FDCPA against collectors). The Louisa Carman Act adds a separate AG enforcement track for collection-side violations.
- **ERISA:** Not preempted — regulates the provider, not the plan.

## Out-of-Network Consumer Protection, Transparency, Cost Containment and Accountability Act

- **Statute:** **N.J.S.A. 26:2SS-1 et seq.** (the "OON Act")
- **Enacted:** P.L. 2018, c.32, signed June 1, 2018, effective August 30, 2018 — predates the federal No Surprises Act
- **Source:** [pub.njleg.gov/bills/2018/pl18/32_.pdf](https://pub.njleg.gov/bills/2018/pl18/32_.pdf); DOBI Bulletin 21-14 (NSA interaction) at [nj.gov/dobi/bulletins/blt21_14.pdf](https://www.nj.gov/dobi/bulletins/blt21_14.pdf); consumer summary at [pirg.org/newjersey/center/articles/how-to-protect-yourself-from-surprise-medical-bills-in-new-jersey](https://pirg.org/newjersey/center/articles/how-to-protect-yourself-from-surprise-medical-bills-in-new-jersey/)

### What it prohibits

- Balance billing for **emergency or urgent services** from an out-of-network (OON) provider or facility.
- Balance billing for **inadvertent OON services** — services rendered by an OON provider at an in-network facility (ancillary services, anesthesia, radiology, pathology, lab, hospitalists, assistant surgeons).
- The patient's cost-share is capped at the in-network amount and counts toward in-network deductible and out-of-pocket maximum.
- Providers must give written disclosure of network status before scheduled services (transparency mandate).

### Provider-payer arbitration

- N.J.S.A. 26:2SS-10 establishes baseball-style arbitration administered by DOBI for rate disputes between OON providers and carriers. **The patient is not a party** and is held harmless from the outcome.

### Where the NJ Act and the federal NSA layer

- For fully-insured NJ plans, **both** the OON Act and the federal No Surprises Act protections apply. The patient gets whichever rule produces the lower out-of-pocket cost.
- For self-funded ERISA plans, only the federal NSA applies (the NJ Act is preempted as to those plans).
- DOBI Bulletin 21-14 explains the interaction.

### Caveats

- **Ground ambulance is NOT covered** by either the NJ OON Act or the federal NSA. This is the single largest balance-billing gap remaining in New Jersey. Unlike Georgia (HB 286, 2024), New Jersey has not closed this gap legislatively as of 2026-05-18.
- Air ambulance is covered by the federal NSA (not the NJ Act directly).
- Workers' compensation, Medicare, and Medicaid are excluded.

## Unfair Claims Settlement Practices Act

- **Statute:** **N.J.S.A. 17:29B-1 et seq.** (Insurance Trade Practices Act); listed unfair claims-settlement practices at **§ 17:29B-4(9)**; parallel life/health provision at **N.J.S.A. 17B:30-13.1**
- **Source:** [law.justia.com/codes/new-jersey/title-17b/section-17b-30-13-1](https://law.justia.com/codes/new-jersey/title-17b/section-17b-30-13-1/)
- **Substance:** Prohibits insurers from misrepresenting policy provisions, failing to acknowledge claims promptly, denying without a reasonable investigation, failing to act in good faith to effectuate prompt and equitable settlement once liability is reasonably clear, and similar practices.
- **Critical caveat — no general private right of action for health insurance:** New Jersey courts have consistently held that the UCSPA itself creates no private cause of action. The 2022 **Insurance Fair Conduct Act (IFCA), N.J.S.A. 17:29BB-1 et seq.**, created a statutory private right for UCSPA violations — but it is limited to **uninsured/underinsured motorist (UM/UIM) auto claims**. IFCA does not cover health-insurance disputes.
- **Use:** Cite UCSPA violations in a complaint to DOBI (see below) and as evidentiary support for a common-law Pickett-style bad-faith claim against the health insurer. Do not plead UCSPA as a standalone count against a health insurer in litigation.

## Bad-faith failure to pay (Pickett standard)

- **Source of law:** Common-law cause of action; leading case **Pickett v. Lloyd's, 131 N.J. 457, 621 A.2d 445 (1993)**
- **Source:** [law.justia.com/cases/new-jersey/supreme-court/1993/131-n-j-457.html](https://law.justia.com/cases/new-jersey/supreme-court/1993/131-n-j-457.html); analysis at [newjerseyinsurancecoveragelitigation.com/bad-faith/bad-faith-law-in-new-jersey](https://www.newjerseyinsurancecoveragelitigation.com/bad-faith/bad-faith-law-in-new-jersey/)
- **Substance:** First-party bad faith is established when (1) the insurer denies or delays benefits, (2) for reasons that are **not even fairly debatable**, and (3) the insurer knew or recklessly disregarded the lack of a reasonable basis for the denial or delay. "Fairly debatable" is the gating standard — if a denial has any objectively reasonable basis, there is no bad faith.
- **Damages:**
  - Contract damages (the wrongfully withheld benefit).
  - **Consequential damages** that were fairly within the contemplation of the insurer (medical-debt collection costs, credit-score harm if reasonably foreseeable, business-loss damages).
  - **Emotional-distress damages and punitive damages** only in **egregious circumstances** — the Pickett bar is high.
  - Attorney's fees are not awarded as a matter of right under Pickett alone; the patient must rely on the contract itself or another fee-shifting statute.
- **Coverage:** All first-party policies of insurance issued in New Jersey, including health insurance (accident and sickness), fully-insured employer plans, and individual marketplace plans.
- **ERISA preemption:** Pickett claims are **preempted** as to self-funded ERISA employer plans. For ERISA self-funded plans, the federal remedy is 29 U.S.C. § 1132(a)(1)(B) (benefits) plus possible § 1132(g) attorney's fees — no state bad-faith consequential damages.
- **Practical posture:** Pickett is harder to win than Georgia's § 33-4-6 statutory bad-faith claim — there is no "60-day demand and then automatic penalty" mechanism, and "fairly debatable" gives insurers wide latitude. Useful primarily where the denial reasoning is patently absurd (mathematical errors, denials citing non-existent policy language, repeated denials after the insurer concedes the basis was wrong).

## Consumer Fraud Act

- **Statute:** **N.J.S.A. 56:8-1 et seq.** (NJCFA)
- **Source:** statute PDF at [njconsumeraffairs.gov/statutes/consumer-fraud-act.pdf](https://www.njconsumeraffairs.gov/statutes/consumer-fraud-act.pdf); overview at [njlegalservices.com/nj-consumer-fraud-lawyer](https://njlegalservices.com/nj-consumer-fraud-lawyer)
- **Substance:** Prohibits "unconscionable commercial practice, deception, fraud, false pretense, false promise, misrepresentation, or the knowing concealment, suppression, or omission of any material fact" in connection with the sale of any merchandise or service.
- **Remedies — exceptionally strong:**
  - **Mandatory treble damages** on any ascertainable loss caused by the unlawful practice (the court has no discretion to refuse trebling once liability and ascertainable loss are proven).
  - **Mandatory reasonable attorney's fees and costs**.
  - **Mandatory filing fees and reasonable investigative expenses**.
- **Critical caveat — "learned professional" exception:** New Jersey courts have held that hospitals, physicians, dentists, nursing homes, and other comprehensively-regulated healthcare entities are **excluded from CFA liability** when operating within their professional capacity. This rule was established by the NJ Supreme Court in 2004 and has since extended to most healthcare providers. The rationale: such entities are already subject to "comprehensive regulation by the relevant regulatory bodies" (NJ Department of Health, NJ Board of Medical Examiners), so they are not "ordinary commercial sellers" at whom the CFA was directed.
- **Where the CFA still bites in medical billing:**
  - **Third-party debt collectors** are not "learned professionals" — CFA applies to collection conduct.
  - **Billing-vendor companies** acting on behalf of the hospital (revenue-cycle management firms, third-party billers) may not enjoy the exception when their conduct is purely commercial.
  - **Ambulance services**, including ambulance billing, have been held to be learned professionals in some NJ cases — verify case law before pleading CFA against an ambulance provider.
  - **Misrepresentation of network status** by a hospital marketing arm, sale of medical credit cards (CareCredit and similar), and ancillary upselling may fall outside the professional capacity and inside the CFA.
  - **Bait-and-switch pricing** at urgent-care chains and standalone facilities not directly licensed as hospitals.
- **Practical posture:** The CFA is the most powerful consumer-protection statute in NJ — but it is the weakest in the country at reaching hospitals directly. Use it against the collector or against a separately-incorporated billing entity; do not plead it against the hospital itself without first checking whether the most recent learned-professional case law has shifted.

## Regulatory agencies

### New Jersey Department of Banking and Insurance (DOBI)

- **Online complaint (insurance):** [sbs.naic.org/solar-web/pages/public/onlineComplaintForm/onlineComplaintForm.jsf?state=NJ](https://sbs.naic.org/solar-web/pages/public/onlineComplaintForm/onlineComplaintForm.jsf?state=NJ) (NAIC State-Based Systems portal, used by DOBI)
- **Consumer information hub:** [nj.gov/dobi/consumer.htm](https://www.nj.gov/dobi/consumer.htm)
- **Phone:** main **(609) 292-7272**; Consumer Hotline **1-800-446-7467** (8:30 AM to 5:00 PM ET, Monday-Friday)
- **Mail:**
  > New Jersey Department of Banking and Insurance
  > Consumer Inquiry and Response Center
  > P.O. Box 471
  > Trenton, NJ 08625-0471
- **Authority:** all insurance companies licensed in New Jersey, including fully-insured health insurers, HMOs, PPOs, Medicare supplement, and dental. Administers the Out-of-Network Consumer Protection Act and the OON arbitration program. UCSPA enforcement. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and does not regulate providers, hospitals, or debt collectors (route to AG / Consumer Affairs / Health Dept).

### New Jersey Attorney General — Division of Consumer Affairs

- **Online complaint:** [njconsumeraffairs.nj.gov/file-a-complaint](https://njconsumeraffairs.nj.gov/file-a-complaint); landing page at [njconsumeraffairs.gov/Pages/Consumer-Complaints.aspx](https://www.njconsumeraffairs.gov/Pages/Consumer-Complaints.aspx)
- **Phone:** main **(973) 504-6200**; toll-free in NJ **1-800-242-5846**
- **Mail:**
  > New Jersey Division of Consumer Affairs
  > 124 Halsey Street
  > Newark, NJ 07102
- **Authority:** enforces the NJ Consumer Fraud Act, the **Louisa Carman Medical Debt Relief Act** (sole enforcement authority), licensed-professional discipline through the relevant board (Board of Medical Examiners, Board of Nursing, etc.), and debt-collection regulation. The right CC line for any letter that raises billing-conduct or collection-conduct issues, especially anything that triggers the Louisa Carman Act.

### NJ Department of Health (for hospital patient-rights and Charity Care)

- **Health Facility Surveys & Field Operations complaint line:** **1-800-792-9770**
- **Charity Care information:** [nj.gov/health/charitycare](https://www.nj.gov/health/charitycare/)
- **Authority:** enforces N.J.A.C. 8:43G hospital licensing regulations, including the Patient's Bill of Rights and Charity Care obligations. The right CC line for any letter that alleges a hospital denied an itemized bill request, failed to disclose Charity Care availability, or violated patient-rights regulations.

## Small claims court — Special Civil Part, Small Claims Section

- **Court name:** **Superior Court of New Jersey, Law Division, Special Civil Part — Small Claims Section** (one per county)
- **Jurisdictional limit:** **$5,000** (raised from $3,000 effective July 1, 2022). Tenancy/security-deposit claims have a separate $5,000 limit.
- **Procedural rules:** **R. 6:1-1 et seq.** (Special Civil Part rules); small-claims-specific rules at **R. 6:11**
- **Source:** [njcourts.gov/self-help/small-claims-court](https://www.njcourts.gov/self-help/small-claims-court); fee schedule at [njcourts.gov/sites/default/files/forms/11112_courtfees.pdf](https://www.njcourts.gov/sites/default/files/forms/11112_courtfees.pdf); Capehart Scatchard summary of the 2022 increase at [capehart.com/new-jersey-supreme-court-approves-increase-in-jurisdictional-limits-of-small-claims-and-special-civil-part](https://www.capehart.com/new-jersey-supreme-court-approves-increase-in-jurisdictional-limits-of-small-claims-and-special-civil-part/)
- **Filing fees (2026):** **$15 for one defendant, plus $2-$5 per additional defendant** in the Small Claims Section; Special Civil Part regular cases ($5,001-$20,000) are $50-$75. Service of process via mailer fee (typically $7 per defendant).
- **Attorney rules:** permitted, not required. Designed for pro se litigants. **Corporations and LLCs may defend a small-claims action through a non-attorney officer or employee under R. 6:11**, but may not prosecute a claim without an attorney except in the small-claims monetary range. This is the NJ analog to Georgia's broader Magistrate Court rule — narrower than Georgia (defense-only, not offense), but still a material advantage for a patient-plaintiff.
- **Jury trial:** not available in small claims; either party may demand a jury by paying the larger Special Civil Part fee and transferring out of small claims under R. 6:5-3.
- **For claims $5,001-$20,000:** file in the Special Civil Part general docket (not Small Claims Section); more formal procedure, modest discovery available.
- **For claims over $20,000:** file in the Law Division of Superior Court (general civil); full discovery and motion practice apply.

## Statute of limitations

- **Written and oral contracts:** **6 years from breach** — **N.J.S.A. 2A:14-1**
- **Source:** [law.justia.com/codes/new-jersey/title-2a/section-2a-14-1](https://law.justia.com/codes/new-jersey/title-2a/section-2a-14-1/); NJ Courts FAQ at [njcourts.gov/faq/what-statute-of-limitations-claim-my-case](https://www.njcourts.gov/faq/what-statute-of-limitations-claim-my-case)
- **Substance:** Actions on "contractual claim or liability, express or implied" — both written and oral — must be brought within six years of accrual. The clock runs from the **breach** (typically the day payment was due and not made), not from when damages are discovered.
- **UCC exception:** Contracts for the sale of goods are governed by **N.J.S.A. 12A:2-725** (four years). Hospital services are services, not goods, so § 2A:14-1 controls.
- **Tolling and revival:**
  - Partial payment or written acknowledgment of the debt can restart the clock under NJ common law. **Do not make a partial payment on a time-barred medical debt without legal advice.**
  - The Louisa Carman Act's mandatory 120-day pre-collection wait and required notice procedures do not toll the statute, but they delay when the creditor may sue.
- **Practical posture:** Six years is the right number to cite in any 30-day warning letter or hardship narrative. Most hospital financial-responsibility forms are signed (written contract); even where no signed form exists, oral and implied contracts share the same 6-year limit in NJ.

## Ground ambulance balance billing

**Not covered by New Jersey state law.** The OON Consumer Protection Act (N.J.S.A. 26:2SS) does **not** apply to ground ambulance transport, and the federal No Surprises Act also excludes ground ambulance.

The patient is left with these levers:

- Negotiate directly with the ambulance provider citing reasonable-and-customary doctrine and UCC § 2-305 (open-price-term reasonableness).
- If the bill was incurred under a no-fault auto policy, **PIP coverage** (see below) may pay the ambulance bill regardless of fault.
- If the patient is income-eligible, the Louisa Carman Act's 3% interest cap, 120-day collection wait, and credit-reporting ban still apply to the ambulance debt as "medical debt."

Tracking: any NJ bill introduced to close the ground-ambulance gap should be flagged at the next annual re-verification.

## Credit reporting — Louisa Carman Medical Debt Relief Act

- **Statute:** **N.J.S.A. 56:11-56 et seq.** — Louisa Carman Medical Debt Relief Act
- **Enacted:** **P.L. 2024, c.48**, signed July 22, 2024
- **Effective dates:** credit-reporting ban and basic protections **July 22, 2024**; remaining provisions (interest cap, payment-plan rules, wage-garnishment ban, charity-care screening, plain-language requirements) **July 22, 2025**
- **Source:** statute text at [law.justia.com/codes/new-jersey/title-56/section-56-11-56](https://law.justia.com/codes/new-jersey/title-56/section-56-11-56/); P.L. text at [pub.njleg.gov/Bills/2024/PL24/48_.HTM](https://pub.njleg.gov/Bills/2024/PL24/48_.HTM); Governor's signing statement at [nj.gov/governor/news/news/562024/20240722a.shtml](https://www.nj.gov/governor/news/news/562024/20240722a.shtml); practitioner analyses at [bracheichler.com/insights/louisa-carman-medical-debt-relief-act-requirements-take-effect-july-22-2025](https://www.bracheichler.com/insights/louisa-carman-medical-debt-relief-act-requirements-take-effect-july-22-2025/), [frierlevitt.com/articles/navigating-new-jerseys-louisa-carman-medical-debt-relief-act](https://www.frierlevitt.com/articles/navigating-new-jerseys-louisa-carman-medical-debt-relief-act/), [stevenslee.com/health-law-observer-blog/new-jerseys-medical-debt-relief-act-now-fully-in-effect](https://www.stevenslee.com/health-law-observer-blog/new-jerseys-medical-debt-relief-act-now-fully-in-effect/)

### Core provisions

- **Total credit-bureau ban:** No consumer reporting agency may include any patient's medical debt (paid or unpaid, any amount) for healthcare services rendered on or after July 22, 2024. No medical creditor or debt collector may report medical debt to a CRA. **Any reported debt is void and unenforceable.**
- **Interest cap:** **3% per year** maximum on any medical debt. Post-judgment interest follows court rules but cannot exceed 3%.
- **120-day pre-collection wait:** No collection actions (lawsuit, third-party referral, sale of debt) may begin until **at least 120 days after the initial bill** is sent, and only after the provider has offered the patient a reasonable payment plan in writing.
- **Reasonable payment plan defined:** Monthly payments capped at the **lesser of an affordable amount or 3% of monthly income**, documented in writing, with a 60-day grace period for late payments and maximum 3% annual interest.
- **Wage garnishment ban:** No wage garnishment for any patient with household income below **600% of the federal poverty level** — regardless of judgment status.
- **Asset and lien restrictions:** No liens on the patient's primary residence and no asset seizures for medical debts under $1,000.
- **Charity-care screening mandate:** Before initiating collection, providers must screen for charity-care eligibility and refer the patient to applicable state and federal programs.
- **Plain-language notices:** Collection notices must use **14-point bold font** and disclose patient rights, the credit-reporting ban, and the appeal process.
- **Insurance-appeal pause:** No collection action may proceed while an insurance appeal is pending; a successful appeal voids the debt for all purposes.

### Enforcement

- **Sole enforcement authority is the NJ Attorney General / Division of Consumer Affairs.** Civil penalties available against medical creditors and medical debt collectors.
- The statute is silent on a direct private right of action for damages, but a violation will typically also be a violation of the FDCPA (if the actor is a debt collector) and may be deceptive conduct under collateral common-law theories.

### Loopholes to watch

- **Medical credit cards** (CareCredit and similar third-party financing products) **may not be covered** — the debt converts from "medical debt" to "credit-card debt" once the patient enrolls. Counsel patients to avoid these products precisely because they strip Louisa Carman protections.
- The credit-reporting ban applies only to services on or after **July 22, 2024**. Pre-July-2024 services remain reportable subject to the federal voluntary CRA changes (paid medical debt removed; debt under $500 not reported; one-year delay before reporting).
- **Federal preemption posture is in flux.** The CFPB October 2025 interpretive rule asserted that the FCRA preempts state laws restricting medical-debt credit reporting. If that survives challenge, it limits some of the Louisa Carman credit-reporting reach.

### Why this is the headline NJ lever

In any letter to a NJ medical creditor or collector, **cite the Louisa Carman Act first**. It is post-2024 — collectors who built their workflows pre-2024 routinely violate it. The credit-reporting ban with the **"void and unenforceable"** trigger gives the patient an immediate defense if the debt has been reported.

## Hospital charity care

- **Statute:** **N.J.S.A. 26:2H-18.51 et seq.** (Hospital Care Payment Assistance / Charity Care), funded under the Health Care Subsidy Fund (N.J.S.A. 26:2H-18.58)
- **Source:** program homepage at [nj.gov/health/charitycare](https://www.nj.gov/health/charitycare/); program overview at [nj.gov/health/hcf/charity-care/overview](https://www.nj.gov/health/hcf/charity-care/overview/); fact sheet at [nj.gov/health/charitycare/documents/charitycare_factsheet_en.pdf](https://www.nj.gov/health/charitycare/documents/charitycare_factsheet_en.pdf)
- **Substance:** **Every acute-care hospital in NJ is required by state law to provide medically necessary inpatient and outpatient services regardless of ability to pay**, with a sliding-scale subsidy based on household income and assets.

### Sliding scale (2026)

| Income as % of FPL | Patient pays        |
| ------------------ | ------------------- |
| 0-200%             | 0%                  |
| 201-225%           | 20%                 |
| 226-250%           | 40%                 |
| 251-275%           | 60%                 |
| 276-300%           | 80%                 |
| >300%              | 100% (not eligible) |

For households between 200% and 300% FPL, **out-of-pocket medical expenses exceeding 30% of gross annual income** may qualify for additional assistance above the sliding-scale grant.

### Asset limits

- Individual: **$7,500** in non-essential assets
- Family: **$15,000** in non-essential assets
- Primary residence, primary vehicle, and retirement accounts are excluded from the asset test.

### Process and hospital obligations

- Apply directly at the hospital's business or admissions office, **within one year of the date of service**.
- The hospital must make a determination **within 10 business days** of receiving a complete application.
- Hospitals must screen applicants for Medicaid and other assistance before approving Charity Care.
- Hospitals must post Charity Care availability notices in **English, Spanish, and any language spoken by 10% or more of the population** in the hospital's service area.
- Hospitals are reimbursed for documented Charity Care from the **Health Care Subsidy Fund** — they have no economic disincentive to grant it.

### Why this matters

NJ Charity Care is the **strongest state-mandated hospital financial-assistance program in the United States**. For any uninsured or underinsured NJ patient at or below 300% FPL, the first move in a dispute should be a written Charity Care application, certified mail, with copies to the NJ Department of Health Charity Care Coordinator if the hospital fails to respond within 10 business days. The Louisa Carman Act (above) reinforces this by requiring providers to screen for Charity Care eligibility before pursuing any collection action.

For screening tools, Dollar For at [dollarfor.org/state_sheet/new-jersey](https://dollarfor.org/state_sheet/new-jersey/) is the standard cross-state aid.

## Hospital lien statute

- **Citations:** **N.J.S.A. 2A:44-35 through 2A:44-41**
- **Source:** [law.justia.com/codes/new-jersey/title-2a](https://law.justia.com/codes/new-jersey/title-2a/) (Chapter 44); 50-state comparison at [mwl-law.com/wp-content/uploads/2019/09/HOSPITAL-LIEN-LAWS-IN-ALL-50-STATES-CHART-00215685x9EBBF.pdf](https://www.mwl-law.com/wp-content/uploads/2019/09/HOSPITAL-LIEN-LAWS-IN-ALL-50-STATES-CHART-00215685x9EBBF.pdf)
- **Substance:** Hospitals, nursing homes, and licensed physicians and dentists who treat a person injured by another's negligence may file a lien for reasonable charges, **only against the patient's cause of action or settlement against the at-fault third party**. **Not a lien on the patient's home, wages, or bank accounts.** The Louisa Carman Act independently bars liens on primary residences for medical debts and asset seizures under $1,000.
- **Perfection requirements:**
  - File a verified written notice of lien with the county clerk in the county where the hospital is located.
  - Filing must occur **before payment of any moneys** to the injured patient or their representatives, and **no later than 90 days after the first treatment**.
  - The notice must include the patient's name and address, the date and circumstances of the accident, the name of the alleged tortfeasor, and the hospital's name and address.
- **Priority:** Hospital liens generally take priority over the patient's recovery but are subordinate to attorney's fees in the underlying personal-injury case (N.J.S.A. 2A:44-39 limits the lien to a percentage of net recovery after fees).
- **Key check:** confirm the lien notice was filed within 90 days. A late-filed lien is invalid against the patient.

## No-fault auto insurance (PIP)

- **Statute:** **N.J.S.A. 39:6A-1 et seq.** — New Jersey Automobile Reparation Reform Act
- **Key provisions:** PIP requirement at **§ 39:6A-4**; coverage options at **§ 39:6A-4.3**; PIP arbitration at **§ 39:6A-5.1** and **§ 39:6A-25**
- **Source:** [law.justia.com/codes/new-jersey/title-39](https://law.justia.com/codes/new-jersey/title-39/) (Chapter 6A); plain-English summary at [aielloharris.com/practice-areas/personal-injury-law/motor-vehicle-accidents/car-accidents/n-j-s-a-396a-nj-motor-vehicle-insurance-car-accident-laws](https://aielloharris.com/practice-areas/personal-injury-law/motor-vehicle-accidents/car-accidents/n-j-s-a-396a-nj-motor-vehicle-insurance-car-accident-laws/)

### Why this matters for medical bills

New Jersey is a **no-fault PIP state**. For any medical bill connected to a motor-vehicle accident, the auto insurer pays first — regardless of fault. This is a critical interaction point:

- **PIP medical-expense benefits** are required in every NJ auto policy. Standard limit is up to **$250,000** for permanent or significant brain/spinal/disfigurement injuries treated at a trauma center; the basic standard limit is **$15,000** with options to elect higher tiers up to $250,000.
- Deductible options: $250, $500, $1,000, $2,000, or $2,500.
- **Coverage is regardless of fault** — a patient injured as a driver, passenger, pedestrian, or cyclist is covered by the host-vehicle's PIP first.
- **Ground ambulance bills covered by PIP** are not subject to the OON Consumer Protection Act gap — the PIP carrier pays the bill (subject to PIP fee schedule) and the patient does not get balance-billed.

### PIP dispute resolution

- **N.J.S.A. 39:6A-5.1** and N.J.A.C. 11:3-5 set up **mandatory PIP arbitration** through the National Arbitration Forum (now administered by Forthright Solutions) for disputes between providers and PIP carriers. The patient is generally not a party.
- For patient-side disputes (denial of PIP benefits), the patient may either compel arbitration or sue the PIP carrier — and a Pickett-style bad-faith claim is available against a PIP carrier that denies benefits without a fairly debatable basis.

### Practical posture in a dispute letter

If the patient was injured in a motor-vehicle accident in NJ, **always check whether PIP was billed first**. A hospital that bills the patient directly without first submitting to the patient's auto PIP carrier (or the at-fault vehicle's carrier) is misallocating responsibility — and the patient has both a contract defense (the hospital agreed to bill PIP) and a statutory route (request PIP arbitration to make the carrier pay the provider directly).

## Wage garnishment

- **Statute:** **N.J.S.A. 2A:17-50 et seq.** for the general framework; **N.J.S.A. 2A:17-56** for income-execution percentage limits
- **General limits:** Up to **10% of disposable income** if the debtor earns no more than 250% of the FPL; up to **25% of disposable income** if above 250% FPL — both subject to the federal CCPA floor (30× federal minimum wage exemption).
- **Medical-debt overlay — Louisa Carman Act:** **No wage garnishment is permitted for any medical debt where the patient's household income is below 600% of the FPL**, regardless of whether a judgment has been entered. This is the highest income-protection threshold for medical-debt garnishment in any US state as of 2026-05-18.
- **Procedural:** Most creditors must sue and obtain a judgment before garnishing wages. Medical creditors who obtain a judgment and attempt to garnish must independently establish that the patient is above 600% FPL — practically, this means most NJ medical-debt judgments cannot be collected through wage garnishment.
- **Use:** In response letters to collectors threatening garnishment, cite both the general 10%/25% caps and the Louisa Carman 600% FPL ban. Include a hardship narrative establishing income below 600% FPL.

## Quick reference for letter rendering

When the LLM renders a New Jersey-bound letter, substitute these defaults:

- **State statute (itemization right):** **N.J.S.A. 26:2H-12.8** and **N.J.A.C. 8:43G-4.1** — request-triggered, must be made in writing. Cite both together in any letter requesting itemization.
- **State insurance department (CC line):** New Jersey Department of Banking and Insurance, Consumer Inquiry and Response Center, P.O. Box 471, Trenton, NJ 08625-0471; toll-free 1-800-446-7467
- **State AG consumer protection (CC line):** New Jersey Division of Consumer Affairs, 124 Halsey Street, Newark, NJ 07102; toll-free 1-800-242-5846 ([njconsumeraffairs.nj.gov/file-a-complaint](https://njconsumeraffairs.nj.gov/file-a-complaint))
- **State health department (CC line — for hospital patient-rights and Charity Care violations):** New Jersey Department of Health, Health Facility Surveys & Field Operations, 1-800-792-9770
- **Small-claims court name:** **Superior Court of New Jersey, Law Division, Special Civil Part — Small Claims Section, [county] County**
- **Filing fee (in 30-day warning):** "approximately $15 plus $2-$5 per additional defendant in Small Claims (up to $5,000); $50-$75 in regular Special Civil Part (up to $20,000)"
- **Statute of limitations (in 30-day warning):** "N.J.S.A. 2A:14-1 (six years for contract claims)"
- **For credit-reporting violations (post-July 22, 2024 services):** Cite **N.J.S.A. 56:11-56 et seq. (Louisa Carman Medical Debt Relief Act)** — note that any reported debt is **void and unenforceable**, and the AG has sole enforcement authority. This is the single highest-leverage NJ-specific cite for any debt-collection or credit-reporting dispute.
- **For balance bills (emergency or inadvertent OON at in-network facility):** Cite **N.J.S.A. 26:2SS-1 et seq. (OON Consumer Protection Act)** as primary state-law authority; layer the federal No Surprises Act for ERISA-self-funded plan members.
- **For ground-ambulance balance bills:** **Not covered by state law.** Rely on PIP (if motor-vehicle-related), Louisa Carman protections, reasonable-and-customary doctrine, and direct negotiation.
- **For health-insurer bad-faith denials:** Cite common-law **Pickett v. Lloyd's, 131 N.J. 457 (1993)** and the underlying UCSPA violations at **N.J.S.A. 17:29B-4(9)** as evidentiary support. Do **not** plead UCSPA as a standalone count — and do **not** plead IFCA in a health-insurance case (IFCA covers UM/UIM auto only).
- **For provider-side misconduct (vs. insurer-side):** The Consumer Fraud Act (N.J.S.A. 56:8-1 et seq.) generally does **not** reach the hospital itself due to the learned-professional exception. Cite it only against third-party collectors, separately-incorporated billing companies, or commercial-conduct fragments that fall outside the professional capacity.
- **For Charity Care:** Cite **N.J.S.A. 26:2H-18.51 et seq.** and the sliding-scale FPL chart above. Demand a written eligibility determination within 10 business days under the program rules.

## Key New Jersey-specific advantages

Worth keeping in mind when triaging a NJ patient's bills:

1. **State-funded mandatory Charity Care** — every acute-care hospital in NJ must provide medically necessary care to patients at or below 300% FPL, with a state-administered sliding-scale subsidy and a state-funded reimbursement so hospitals have no incentive to refuse. The strongest state-mandated hospital financial-assistance program in the country.
2. **Louisa Carman Act trifecta** — total credit-bureau ban on medical debt, 3% interest cap, and a 600%-FPL wage-garnishment ban. Combined, these strip almost all leverage from the collector's toolkit for any income-eligible NJ patient. The "void and unenforceable" trigger on improperly reported debt is a litigation-friendly hammer.
3. **Pre-NSA balance-bill protection** — NJ has had OON Consumer Protection since 2018; provider compliance is mature, and DOBI's arbitration backstop is operational. The patient is held harmless from rate disputes for emergency and inadvertent OON services at in-network facilities.
4. **PIP coverage breadth** — every NJ auto policy pays medical bills up to $250,000 (in the elected tier) regardless of fault. For any motor-vehicle-related medical bill, the first leverage move is always to redirect billing to PIP.
5. **Small-claims corporate-defense rule** — corporations and LLCs can defend a small-claims action through a non-attorney employee (R. 6:11), which means the patient-plaintiff is likely to face a billing-department staffer rather than defense counsel. Narrower than Georgia (defense-only, not offense), but still raises the economic leverage of a small-claims filing.

## Key New Jersey-specific weaknesses

Equally important to flag when comparing NJ leverage to other states:

1. **Consumer Fraud Act does not reach hospitals directly** — the learned-professional exception immunizes hospitals, physicians, and nursing homes operating within their professional capacity. The CFA's mandatory treble damages and fee-shifting hit third-party collectors and ancillary commercial entities, not the hospital. This is a major narrowing relative to states (Georgia's FBPA, California's CLRA, etc.) whose UDAP statutes reach providers directly.
2. **No IFCA private right of action for health insurance** — IFCA's punchy treble-damages-plus-fees remedy applies only to UM/UIM auto claims. Health-insurance bad-faith claims rely on Pickett (common-law, no statutory penalty, attorney's fees only if recovered through the contract).
3. **Ground ambulance not covered** — unlike Georgia and several other states, NJ has not closed the ground-ambulance balance-billing gap. Negotiation, PIP (where applicable), and Louisa Carman protections are the only levers.
4. **Itemization right is request-triggered, not automatic** — patients must affirmatively request the itemized bill in writing. Without a written request, there is no clean documentary record of the hospital's non-compliance.
