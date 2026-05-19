# Colorado state pack

The fully-worked state-law layer for Colorado patients. The LLM uses this when the patient's state is Colorado. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Three things make Colorado's patient-side leverage unusually strong:

1. The **Hospital Discounted Care Act (HB22-1285)** caps charges for uninsured and underinsured patients at the **average of the Medicare and Medicaid rates** and mandates a screening-and-payment-plan process before any collections can begin. This is the most generous uninsured-patient pricing cap of any U.S. state.
2. **C.R.S. § 10-3-1116 creates a private bad-faith cause of action with statutory damages of two times the covered benefit plus reasonable attorney's fees and court costs** — among the most patient-favorable bad-faith statutes in the country, and dramatically broader than the common-law "reasonableness" standard most states use.
3. **HB23-1136 / C.R.S. § 25.5-4-414** closed the federal No Surprises Act's ground-ambulance gap effective **January 1, 2025**, capping patient cost-share at the in-network amount for ground-ambulance services.

## Hospital itemization right

- **Statute:** **C.R.S. § 25-3-112** (Hospitals — Patient Bill of Rights — Itemized Statements); reinforced by the **Hospital Discounted Care Act, C.R.S. § 6-20-101 et seq.** (HB22-1285), which adds pre-service price-estimate and post-service itemization duties for uninsured / underinsured patients.
- **Source:** [law.justia.com/codes/colorado/title-25/article-3/section-25-3-112](https://law.justia.com/codes/colorado/title-25/article-3/section-25-3-112/); HDCA at [law.justia.com/codes/colorado/title-6/article-20](https://law.justia.com/codes/colorado/title-6/article-20/); statutory text at [leg.colorado.gov/sites/default/files/2022a_1285_signed.pdf](https://leg.colorado.gov/sites/default/files/2022a_1285_signed.pdf)
- **What it requires:**
  - On written request, a licensed hospital must furnish an **itemized statement** of all goods and services provided, identifying each charge by service date, CPT/HCPCS or DRG code where applicable, and the rate billed.
  - Under the HDCA, hospitals must additionally provide uninsured / underinsured patients a **written estimate** before non-emergency services and a final itemized bill on request, in plain language.
  - Hospitals operating in Colorado must also comply with federal **45 C.F.R. § 180** hospital price-transparency rules (machine-readable file plus consumer-friendly shoppable list).
- **Scope:** Inpatient and outpatient services at any general hospital licensed in Colorado. Long-term care, freestanding ASCs, and independent physician practices fall outside § 25-3-112 but may be reached via the Colorado Consumer Protection Act if billing is deceptive.
- **Enforcement:** Colorado Department of Public Health and Environment (CDPHE) licenses hospitals and can sanction for violations; the Department of Health Care Policy and Financing (HCPF) enforces HDCA compliance. Patients also have a Colorado Consumer Protection Act remedy for deceptive billing (see § 6-1-101 et seq. below).
- **ERISA:** Not preempted — regulates the provider, not the plan.

## Unfair Claim Settlement Practices Act

- **Statute:** **C.R.S. § 10-3-1104(1)(h)** (defined list of unfair claim-settlement practices), part of the Unfair Claim Settlement Practices Act, **§ 10-3-1101 et seq.**
- **Source:** [law.justia.com/codes/colorado/title-10/article-3/part-11/section-10-3-1104](https://law.justia.com/codes/colorado/title-10/article-3/part-11/section-10-3-1104/)
- **Substance:** Prohibits insurers from a defined list of unfair settlement practices: misrepresenting pertinent facts or policy provisions, failing to acknowledge claims promptly, failing to adopt reasonable standards for prompt investigation, refusing to pay without a reasonable investigation, not attempting in good faith to effectuate prompt and equitable settlements, compelling insureds to litigate to recover amounts due, etc.
- **Critical distinction from most states:** Colorado **does** provide a private right of action — but **not under § 10-3-1104 directly**. The private action flows through **C.R.S. §§ 10-3-1115 and 10-3-1116** (see next section). Cite § 10-3-1104 as the source of the prohibited conduct, then plead the cause of action under § 10-3-1116.
- **Regulatory complaints:** Division of Insurance investigates and can fine insurers under § 10-3-1108 (administrative penalties up to $1,500 per violation, $1,500,000 aggregate annual).

## Bad-faith / unreasonable delay or denial — § 10-3-1115 / § 10-3-1116

- **Statute:** **C.R.S. § 10-3-1115** (defines "unreasonable delay or denial"); **C.R.S. § 10-3-1116** (creates the private right of action and statutory damages)
- **Source:** [law.justia.com/codes/colorado/title-10/article-3/part-11/section-10-3-1115](https://law.justia.com/codes/colorado/title-10/article-3/part-11/section-10-3-1115/); [law.justia.com/codes/colorado/title-10/article-3/part-11/section-10-3-1116](https://law.justia.com/codes/colorado/title-10/article-3/part-11/section-10-3-1116/)
- **Substance:**
  - A first-party claimant whose insurer **unreasonably delays or denies payment of a covered benefit** may bring an action and recover **two times the covered benefit, plus reasonable attorney's fees and court costs**.
  - "Unreasonably" is defined as without a reasonable basis. This is a **statutory negligence-style standard**, not the common-law "frivolous and unfounded" standard most states apply — substantially easier for a patient to plead and prove.
  - The 2x statutory damages are **on top of** the underlying covered benefit, not a percentage of it. Example: a wrongfully denied $20,000 hospital claim yields $20,000 (benefit) + $40,000 (2x statutory damages) + attorney's fees + costs = $60,000+ recovery.
  - Available **in addition to** any common-law bad-faith claim — the statutory action does not displace the tort remedy.
- **Coverage:** "Any first-party claimant" under "any policy of insurance," including health insurance. Confirmed by *Kisselman v. American Family Mutual Ins. Co.*, 292 P.3d 964 (Colo. App. 2011), and reinforced in *Rooftop Restoration, Inc. v. American Family*, 418 P.3d 1173 (Colo. 2018).
- **Procedural notes:**
  - **No pre-suit demand requirement** in the statute itself. The 30-day warning letter strengthens the "unreasonable" showing by establishing the insurer was on notice but is not a statutory prerequisite.
  - **Three-year statute of limitations** for the § 10-3-1116 claim (C.R.S. § 13-80-101(1)(a) — statutory liability).
- **ERISA preemption:** § 10-3-1116 is **preempted** as applied to self-funded ERISA employer plans. For ERISA self-funded plans, the federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) attorney's fees — no state 2x statutory damages. The statute is in play for fully-insured plans, individual marketplace plans, Medicaid managed care (where state regulation reaches), and short-term/limited-duration policies sold in Colorado.

## Surprise Billing — Out-of-Network Health Care Act

- **Statute:** **C.R.S. § 10-16-704** (Out-of-Network Health Care Services); related provisions at **§ 10-16-704.5** (binding arbitration for OON disputes) and **§ 10-16-1401 et seq.** (No-Surprise-Billing measures, HB19-1174 and follow-on legislation)
- **Source:** [law.justia.com/codes/colorado/title-10/article-16/part-7/section-10-16-704](https://law.justia.com/codes/colorado/title-10/article-16/part-7/section-10-16-704/)
- **Original enactment:** HB19-1174 (2019), effective January 1, 2020
- **Ground-ambulance expansion:** **HB23-1136 / C.R.S. § 25.5-4-414**, effective **January 1, 2025** (see "Ground ambulance" section)

### What it prohibits

- Balance billing for **emergency services** at any out-of-network facility or by any OON provider.
- Balance billing for **non-emergency services** rendered by an OON provider at an **in-network** facility (anesthesia, radiology, pathology, hospitalists, lab, etc.).
- Patient cost-share is capped at the in-network amount and counts toward the in-network deductible and out-of-pocket maximum.

### Where Colorado goes beyond the federal No Surprises Act

- Pre-dates the federal NSA by two years; Colorado-regulated plans were already compliant before January 2022.
- **Ground ambulance is now covered** under C.R.S. § 25.5-4-414 (effective Jan 1, 2025); the federal NSA explicitly excludes ground ambulance.
- **Mandatory binding arbitration** under § 10-16-704.5 resolves provider-payer rate disputes — patient is not a party and not financially exposed to the outcome.
- **Hospital Discounted Care Act** independently caps charges for uninsured/underinsured patients at Medicare/Medicaid rates regardless of network status (HDCA addresses the *uninsured* gap that NSA does not touch at all).

### Caveats

- **ERISA preemption:** Does not reach self-funded ERISA employer plans. Those are covered only by the federal NSA (which does cover most balance billing but excludes ground ambulance until/unless Congress acts).
- Excludes air ambulance (covered by federal NSA), workers' compensation, Medicare, and Medicaid (Medicaid has its own balance-billing prohibition at C.R.S. § 25.5-4-301).
- The HDCA's uninsured-patient cap requires the patient to complete the hospital's screening process; patients who do not screen may forfeit the cap (see HDCA section).

## Hospital Discounted Care Act (HB22-1285)

- **Statute:** **C.R.S. § 6-20-101 et seq.** — Colorado Hospital Discounted Care Act
- **Source:** [law.justia.com/codes/colorado/title-6/article-20](https://law.justia.com/codes/colorado/title-6/article-20/); HCPF rules at [hcpf.colorado.gov/hospital-discounted-care](https://hcpf.colorado.gov/hospital-discounted-care)
- **Effective:** **September 1, 2022** (most provisions); collections restrictions phased in through 2023.

### What it requires

- **Screening:** Before billing or collecting, a hospital must screen the patient for eligibility for public health-coverage programs (Medicaid, CHP+) and for hospital discounted care under the HDCA. The hospital must offer translation and culturally appropriate assistance.
- **Charge cap for uninsured / underinsured at or below 250% FPL:** Total amounts charged may not exceed **the average of the Medicare and Medicaid rates** for the same services for individuals at or below 250% of the federal poverty level. Hospitals may not charge above their standard discounted-care rate even to patients above 250% FPL once HDCA eligibility is established.
- **Mandatory payment plans:** Monthly payments capped at **4% of the patient's monthly household income** (2% for patients on the discounted-care schedule). No interest on HDCA payment plans.
- **Collection prohibitions:** Until the screening process is complete and the hospital has offered a discounted-care payment plan, the hospital and any affiliated debt collector may not initiate a collection action, report to credit bureaus, place a lien, garnish wages, or sell the debt. Aggressive-collection actions (lawsuits, wage garnishment, bank levy) are barred against HDCA-eligible patients on a compliant payment plan.
- **Documentation duty:** Hospitals must provide a written estimate and itemized statement in plain language and translate on request.

### Enforcement

- **HCPF (Department of Health Care Policy and Financing)** receives complaints, audits hospital compliance, and may issue corrective action plans and civil penalties up to $5,000 per violation.
- **Patient remedies:** A patient charged in violation of the HDCA may pursue the Colorado Consumer Protection Act remedies (treble damages or $500 minimum statutory damages plus attorney's fees — see § 6-1-101 et seq. below), because HDCA violations are deemed deceptive trade practices under the Act.

### Caveats

- The screening process is patient-driven — the patient must complete the application and provide income documentation. The kit's intake step should always ask whether HDCA screening was offered and completed.
- HDCA applies only to **licensed hospitals**. Freestanding clinics, urgent care, independent physician practices, ambulatory surgery centers, and most ER docs (billing separately) are not covered. Anesthesia, radiology, and pathology balances billed separately from the hospital fall outside HDCA but are reachable via the OON surprise-billing statute if applicable.
- HDCA caps apply to the charge, not the negotiated insurer payment — once a patient has insurance that paid, HDCA's uninsured cap is not the primary lever; the OON / network-rules path is.

## Colorado Consumer Protection Act

- **Statute:** **C.R.S. § 6-1-101 et seq.** — Colorado Consumer Protection Act (CCPA); deceptive trade practice definitions at **§ 6-1-105**; private right of action at **§ 6-1-113**
- **Source:** [law.justia.com/codes/colorado/title-6/article-1](https://law.justia.com/codes/colorado/title-6/article-1/)
- **Substance:** A consumer injured by a deceptive trade practice may recover **the greater of actual damages or $500, trebled to up to three times actual damages for bad-faith violations, plus reasonable attorney's fees and court costs**.
- **Reach over hospitals and providers:** The CCPA covers any person engaged in "any sales, service, or business activity," explicitly including health-care providers and hospitals. Billing for services not rendered, upcoding, misrepresenting in-network status, misrepresenting the existence of a financial-assistance policy, or failing to disclose HDCA eligibility are all reachable.
- **HDCA cross-reference:** HDCA violations are expressly enforceable through the CCPA — gives the patient a private path with attorney's fees that HDCA's administrative regime alone does not.
- **Procedural:** No pre-suit demand requirement in the statute. **Three-year statute of limitations** under C.R.S. § 13-80-101(1)(g).

## Regulatory agencies

### Colorado Division of Insurance (DOI)

- **Online complaint:** [doi.colorado.gov/for-consumers/file-a-complaint](https://doi.colorado.gov/for-consumers/file-a-complaint)
- **Phone:** main **(303) 894-7490**; toll-free in Colorado **1-800-930-3745**
- **Mail:**
  > Colorado Division of Insurance
  > Consumer Affairs Section
  > 1560 Broadway, Suite 850
  > Denver, CO 80202
- **Authority:** all insurance companies licensed in Colorado, including fully-insured health insurers, HMOs, PPOs, Medicare supplement. Administers the Out-of-Network Health Care Act, the UCSPA, and the § 10-3-1115/1116 unreasonable-delay framework. Runs the OON binding-arbitration process. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and does not regulate hospitals (route to CDPHE/HCPF) or debt collectors (route to AG).

### Colorado Attorney General — Consumer Protection Section

- **Online complaint:** [coag.gov/file-complaint](https://coag.gov/file-complaint/)
- **Phone:** Consumer Protection main **(720) 508-6000**; consumer hotline **1-800-222-4444**
- **Mail:**
  > Colorado Attorney General
  > Consumer Protection Section
  > Ralph L. Carr Colorado Judicial Center
  > 1300 Broadway, 10th Floor
  > Denver, CO 80203
- **Authority:** enforces the Colorado Consumer Protection Act (§ 6-1-101 et seq.) and the Colorado Fair Debt Collection Practices Act (C.R.S. § 5-16-101 et seq.). Reach over hospitals, physician practices, third-party debt collectors, **and original creditors** — exactly the gap not covered by DOI. Useful when the dispute is with the hospital's in-house billing department.

### Department of Health Care Policy and Financing (HCPF)

- **HDCA complaint portal:** [hcpf.colorado.gov/hospital-discounted-care](https://hcpf.colorado.gov/hospital-discounted-care)
- **Phone:** **(303) 866-2993**
- **Authority:** administers and enforces the Hospital Discounted Care Act; receives screening and billing complaints, audits hospitals, imposes corrective action plans and penalties.

## Small claims court

- **Court name:** **County Court — Small Claims Division**
- **Jurisdictional limit:** **$7,500**, codified at **C.R.S. § 13-6-403**
- **Source:** [law.justia.com/codes/colorado/title-13/article-6/part-4/section-13-6-403](https://law.justia.com/codes/colorado/title-13/article-6/part-4/section-13-6-403/); procedural rules at [courts.state.co.us](https://www.courts.state.co.us/) (Colo. R. C.P. 501-521 — Small Claims)
- **Filing fees:** typically $31-$85 depending on claim amount; service of process additional ($10-$50 per defendant). Varies by county clerk.
- **Attorney rules:** Attorneys are **permitted but the proceeding is informal** — relaxed evidence rules, no formal discovery, simplified pleadings. If the defendant brings an attorney, the plaintiff may also bring one or have the case transferred to County Court's regular docket.
- **Jury trial:** Not available in Small Claims. Either party may demand a jury by requesting transfer to County Court regular docket under Colo. R. C.P. 511.

## Statute of limitations

- **Written contracts:** **6 years from breach** — **C.R.S. § 13-80-103.5(1)(a)** (recovery of a liquidated debt or unliquidated determinable amount)
- **Oral / implied contracts:** **3 years from breach** — C.R.S. § 13-80-101(1)(a)
- **Statutory bad-faith (§ 10-3-1116):** 3 years — C.R.S. § 13-80-101(1)(a)
- **Colorado Consumer Protection Act:** 3 years from discovery of the deceptive practice — C.R.S. § 13-80-101(1)(g)
- **Source:** [law.justia.com/codes/colorado/title-13/article-80/section-13-80-103-5](https://law.justia.com/codes/colorado/title-13/article-80/section-13-80-103-5/); [law.justia.com/codes/colorado/title-13/article-80/section-13-80-101](https://law.justia.com/codes/colorado/title-13/article-80/section-13-80-101/)

Most hospital admissions involve a signed financial-responsibility form — a written contract, so 6 years applies. Implied-in-fact medical-billing arrangements without a signed agreement may be treated as oral contracts (3 years). The clock runs from breach (typically the day payment was due and not made).

Partial payment or written acknowledgment of the debt can restart the clock under Colorado common-law accrual rules. **Do not make a partial payment on a time-barred debt without legal advice.**

## Ground ambulance balance-billing

**Covered by Colorado state law as of January 1, 2025**, via **C.R.S. § 25.5-4-414** (HB23-1136). For ambulance services provided on or after that date, an insured patient receiving ground ambulance from an out-of-network provider may be billed no more than the in-network cost-share. The insurer must pay the provider the greater of (i) **325% of the published Medicare rate** for the service in the relevant geographic area, or (ii) the provider's billed amount if lower. The patient is held harmless from any rate dispute between provider and insurer.

This closes the single biggest balance-billing gap in federal law — the federal No Surprises Act **explicitly excludes ground ambulance**. Colorado's 325%-of-Medicare floor is high enough that providers have material incentive to participate (compared to Georgia's 180% floor, for context), which reduces the likelihood of disputes ending up in arbitration at all.

ERISA-preempted for self-funded employer plans; excludes air ambulance (federal NSA covers it), workers' comp, Medicare, and Medicaid (the last two have their own balance-billing prohibitions).

## Credit reporting — Colorado Medical Debt Reform Act

- **Statute:** **C.R.S. § 5-18-101 et seq.** (Colorado Medical Debt Collection Practices), enacted by **HB23-1126** ("Protect Consumers from Excessive Medical Debt"), effective **August 7, 2023**.
- **Source:** [leg.colorado.gov/bills/hb23-1126](https://leg.colorado.gov/bills/hb23-1126)
- **Substance:**
  - **Prohibits reporting medical debt to consumer credit reporting agencies.** A debt collector or medical creditor in Colorado may not furnish information about a medical debt to a CRA. This is broader than the 2022-2023 voluntary CRA changes; it is a state-law furnishing prohibition.
  - **Caps interest on medical debt at 3%** APR (well below the typical 8% statutory rate).
  - **Requires payment-plan offers** before collection escalation.
  - Creates a private right of action with **actual damages, statutory damages up to $1,000 per violation, and attorney's fees** under C.R.S. § 5-16-113.
- **Federal preemption posture:** The CFPB issued an October 2025 interpretive rule taking the position that the FCRA preempts state laws restricting medical-debt credit reporting. **Colorado's furnishing prohibition may be challenged on preemption grounds.** As of this writing the statute remains on the books and enforceable; monitor litigation. The interest cap and payment-plan duties are not preempted.

## Hospital lien statute

- **Citations:** **C.R.S. § 38-27-101 through § 38-27-106**
- **Sources:** [law.justia.com/codes/colorado/title-38/article-27/section-38-27-101](https://law.justia.com/codes/colorado/title-38/article-27/section-38-27-101/)
- **Substance:** Hospitals may file a lien for **reasonable charges** for treatment of an injured person, **only against any recovery the patient obtains from a third party** who caused the injury (e.g., the at-fault driver). **Not a lien on the patient's home, wages, or bank accounts.**
- **Perfection requirements:**
  - File a verified statement of the lien with the clerk and recorder in the county where the hospital is located **within 90 days after the patient's discharge**.
  - Mail a copy of the lien notice by certified mail to the patient and any third party / insurer believed liable.
- **Critical Colorado restriction (§ 38-27-101(2.5)):** A hospital **may not assert a lien if the patient has health insurance that would cover the treatment**. The hospital must first bill the patient's health insurer; if the insurer pays at the contracted rate, the lien is extinguished. **Always confirm this insurer-first step was attempted** — failure to do so invalidates the lien and creates a CCPA deceptive-trade-practice claim.
- **2021 reform:** SB21-009 codified the prohibition on filing liens against insured patients and added attorney's-fee recovery for patients who successfully challenge an invalid lien.

## Hospital charity care

The **Hospital Discounted Care Act (C.R.S. § 6-20-101 et seq.)** functions as Colorado's mandatory financial-assistance regime — substantially broader than IRS § 501(r), and reaches **for-profit and county/municipal hospitals as well as non-profit**. See HDCA section above.

Non-profit hospitals additionally remain bound by IRS § 501(r) (federal). Hospitals participating in the Colorado **Healthcare Affordability and Sustainability Enterprise** (CHASE) provider fee program have heightened HDCA compliance obligations.

Use Dollar For at [dollarfor.org/state_sheet/colorado](https://dollarfor.org/state_sheet/colorado/) for screening, and HCPF's HDCA portal for direct hospital-specific eligibility lookup.

## Wage garnishment

- **Statute:** **C.R.S. § 13-54-104** (Colorado wage-garnishment exemptions)
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a court judgment. Post-judgment, Colorado is **more protective than federal law**: garnishment is capped at the lesser of (i) **20% of disposable earnings** (federal is 25%), or (ii) the amount by which weekly disposable earnings exceed **40× the state minimum wage** (federal is 30× federal minimum wage).
- **HDCA overlay:** Wage garnishment is **expressly prohibited** against HDCA-eligible patients who are on a compliant discounted-care payment plan, regardless of whether a judgment has been entered (C.R.S. § 6-20-110).
- **Use:** In response letters to collectors threatening garnishment without a judgment, or against any HDCA-eligible patient.

## Quick reference for letter rendering

When the LLM renders a Colorado-bound letter, substitute these defaults:

| Element                              | Colorado value                                                                                                                              |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Itemization statute**              | C.R.S. § 25-3-112; HDCA at C.R.S. § 6-20-101 et seq. for uninsured                                                                          |
| **Insurance bad-faith**              | C.R.S. § 10-3-1116 (2x covered benefit + attorney's fees + costs)                                                                           |
| **Surprise-billing statute**         | C.R.S. § 10-16-704 et seq.                                                                                                                  |
| **Ground ambulance**                 | C.R.S. § 25.5-4-414 (effective Jan 1, 2025)                                                                                                 |
| **Consumer Protection Act**          | C.R.S. § 6-1-101 et seq. (treble damages, $500 minimum, attorney's fees)                                                                    |
| **Small-claims court**               | County Court, Small Claims Division                                                                                                         |
| **Small-claims limit**               | $7,500 (C.R.S. § 13-6-403)                                                                                                                  |
| **Filing fee (in 30-day warning)**   | "$31-$85 depending on claim amount"                                                                                                         |
| **Statute of limitations**           | "C.R.S. § 13-80-103.5 (six years for breach of written contract)"                                                                           |
| **Insurance dept (CC line)**         | Colorado Division of Insurance, Consumer Affairs Section, 1560 Broadway, Suite 850, Denver, CO 80202                                        |
| **AG consumer protection (CC line)** | Colorado Attorney General, Consumer Protection Section, 1300 Broadway, 10th Floor, Denver, CO 80203                                         |
| **HDCA enforcement (CC line)**       | HCPF, Hospital Discounted Care Program, 1570 Grant Street, Denver, CO 80203                                                                 |
| **Ground ambulance cite**            | C.R.S. § 25.5-4-414 (HB23-1136, effective Jan 1, 2025)                                                                                      |
| **Provider-side disputes**           | Cite C.R.S. § 6-1-105 (CCPA deceptive trade practice) + § 6-1-113 (private right of action with attorney's fees) in addition to UCC § 2-305 |
| **Insurer-side disputes**            | Cite C.R.S. § 10-3-1116 (unreasonable delay/denial, 2x statutory damages + attorney's fees)                                                 |
| **Uninsured / underinsured patient** | Always cite HDCA, C.R.S. § 6-20-101 et seq., and ask whether screening was offered                                                          |

## Key Colorado-specific advantages

Worth keeping in mind when triaging a CO patient's bills:

1. **Hospital Discounted Care Act** — the most generous uninsured-patient pricing cap in the country. Charges capped at the **average of Medicare and Medicaid rates** for patients at or below 250% FPL, payment plans capped at **4% of monthly income** with no interest, and collections barred until screening is complete. Always ask whether HDCA screening was offered before doing anything else for an uninsured patient.
2. **§ 10-3-1116 statutory bad-faith** — **two times the covered benefit plus attorney's fees and court costs**, on a negligence-style "unreasonable" standard. Among the strongest private bad-faith remedies in the United States. Always cite in any insurer-directed dispute letter; the prospect of statutory doubling alone often moves insurers to settle.
3. **Colorado Consumer Protection Act treble damages** — § 6-1-113 provides actual damages (or $500 minimum) trebled for bad-faith violations, plus attorney's fees, reaching hospitals and original creditors that DOI cannot. Pair with § 10-3-1116 (insurer) or HDCA (hospital) for maximum leverage.
4. **Ground ambulance protection** — Colorado closed the federal NSA's biggest gap effective January 1, 2025 at a generous 325%-of-Medicare floor. Always check whether a ground-ambulance bill post-dates that effective date.
5. **Hospital-lien insurer-first rule** — C.R.S. § 38-27-101(2.5) bars hospital liens against insured patients whose insurer would cover the treatment. Catch this whenever a third-party-liability scenario surfaces (auto accident, slip-and-fall); invalid liens convert into a CCPA claim with attorney's fees.
6. **Medical-debt credit-reporting prohibition** — C.R.S. § 5-18-101 et seq. bars Colorado debt collectors from furnishing medical-debt info to CRAs at all. Federal preemption challenges are pending; the statute remains enforceable as of this writing and the interest cap (3%) and payment-plan duties are not preempted.
7. **Stronger wage-garnishment cap** — 20% of disposable earnings (vs. federal 25%), and outright prohibited for HDCA-eligible patients on a compliant plan.
