# Minnesota state pack

The fully-worked state-law layer for Minnesota patients. The LLM uses this when the patient's state is Minnesota. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Three things make Minnesota's patient-side leverage unusually strong:

1. The **Debt Fairness Act of 2024** (effective October 1, 2024) is the most patient-favorable medical-debt law in the United States. It caps medical-debt interest at zero percent, prohibits credit-bureau reporting of medical debt, bans denial of medically necessary care for unpaid bills, and stops automatic transfer of medical debt to a surviving spouse.
2. **Conciliation Court's $20,000 jurisdictional limit** is among the highest in the country, and **attorneys are not authorized representatives** under Minn. Stat. § 491A.02 — the patient is statistically certain to face a billing-department employee, not defense counsel.
3. The **hospital itemization right under Minn. Stat. § 144.591** is automatic on discharge, free of charge, and **§ 144.588** makes affidavit compliance a precondition to debt-collection referral or wage garnishment, with mandatory dismissal with prejudice as the penalty for noncompliance.

## Hospital itemization right

- **Statute:** **Minn. Stat. § 144.591** (Patient Bill Itemization)
- **Source:** [revisor.mn.gov/statutes/cite/144.591](https://www.revisor.mn.gov/statutes/cite/144.591)
- **What it requires:**
  - Within **30 calendar days** following discharge, a hospital (including critical access hospitals) must deliver an itemized description of billed charges by **secure email, secure online portal, or, upon request, by mail**.
  - The hospital **may not bill or charge the patient** for the itemized description.
  - Each line must describe the actual service or supply. The statute expressly forbids descriptions that use only a medical billing code, "miscellaneous charges," or "supply charges," and requires plain-language definitions of technical or medical terms.
- **Scope exclusions:** Patients with Medicare, Medicaid, MinnesotaCare, or employer self-insured (ERISA) coverage are excluded from § 144.591. For self-funded ERISA patients, fall back to § 62J.81 (good-faith estimate) and Minn. Stat. § 62J.535 (uniform billing).
- **Enforcement:** Section 144.591 itself does not name a private right of action, but the related collection statute § 144.588 makes hospital noncompliance with billing duties grounds for **mandatory dismissal with prejudice** of any collection action — see below.

## Pre-collection affidavit requirement (the lever that gives § 144.591 teeth)

- **Statute:** **Minn. Stat. § 144.588**
- **Source:** [revisor.mn.gov/statutes/cite/144.588](https://www.revisor.mn.gov/statutes/cite/144.588)
- **Substance:** Before a hospital may sue a patient, garnish wages, or refer a medical debt to a third-party collector, it must execute an "affidavit of expert review" certifying:
  - Compliance with the pre-collection requirements of Minn. Stat. § 144.587 (charity-care screening).
  - A reasonable belief the debt is owed.
  - All known third-party payors have been properly billed.
  - The patient was given an opportunity to apply for charity care.
  - A reasonable payment plan was offered if the patient indicated inability to pay in full.
  - (For garnishment) no reasonable basis exists for the wages or funds to be exempt.
- **Penalty:** Failure to comply with the affidavit requirement triggers **mandatory dismissal with prejudice** of the collection action. Failure on referrals to collection agencies subjects the hospital to fines by the Commissioner of Health and enforcement by the Attorney General.
- **Use:** Any MN hospital collection lawsuit or garnishment action without a § 144.588 affidavit on file is per se defective. Demand the affidavit in your first response.

## Good-faith estimate and uniform billing

- **Statutes:**
  - **Minn. Stat. § 62J.81** — Disclosure of payment arrangements; good-faith estimates
  - **Minn. Stat. § 62J.535** — Uniform billing requirements
- **Sources:** [revisor.mn.gov/statutes/cite/62J.81](https://www.revisor.mn.gov/statutes/cite/62J.81); [revisor.mn.gov/statutes/cite/62J.535](https://www.revisor.mn.gov/statutes/cite/62J.535)
- **§ 62J.81 substance:**
  - On consumer request, a provider must give a **good-faith estimate** of the allowable payment within **10 business days**, at no cost. Health plan companies have a mirror duty to provide the contracted-allowable amount and estimated enrollee out-of-pocket cost on enrollee request, also within 10 business days.
  - Providers must also disclose other fees the consumer may be required to pay (including facility fees).
  - The estimate is **not legally binding**, but it crystallizes the discrepancy between estimate and final bill — useful evidence under the consumer-fraud and deceptive-trade-practices laws (§ 325F.69, § 325D.44).
- **§ 62J.535 substance:** Requires that paper claim transactions use the federal electronic claim transaction code sets and the uniform billing forms specified in § 62J.52. Useful for identifying upcoding, invalid CPT/ICD combinations, or non-standard billing codes during audit.
- **Scope exclusions:** Medical Assistance and MinnesotaCare enrollees are exempt from § 62J.81 for covered services.

## Unfair Claims Settlement Practices Act

- **Statute:** **Minn. Stat. § 72A.20** (with related practices at §§ 72A.17-72A.32)
- **Source:** [revisor.mn.gov/statutes/cite/72A.20](https://www.revisor.mn.gov/statutes/cite/72A.20)
- **Substance:** Prohibits insurers from engaging in defined unfair claims-settlement practices — misrepresenting policy provisions, failing to investigate, denying without a reasonable basis, forcing litigation by lowballing, requiring duplicative documentation, delaying communications, etc. — when those practices occur with sufficient frequency to indicate a general business practice.
- **Critical caveat:** **No private right of action.** The Minnesota Supreme Court held in **Morris v. American Family Mut. Ins. Co.**, 386 N.W.2d 233 (Minn. 1986), that § 72A.20 does not create a private cause of action, alone or in conjunction with § 8.31 (Attorney General's private-enforcement statute). Minnesota also does not recognize common-law first-party bad faith. Source: [law.justia.com/cases/minnesota/supreme-court/1986/c5-85-224-2.html](https://law.justia.com/cases/minnesota/supreme-court/1986/c5-85-224-2.html).
- **Use:** Cite UCSPA violations in complaints to the Minnesota Department of Commerce (see below) and as **evidentiary support** for a § 604.18 statutory bad-faith claim. Do not plead UCSPA as a standalone count in litigation.

## Statutory first-party bad faith

- **Statute:** **Minn. Stat. § 604.18** (enacted 2008)
- **Source:** [revisor.mn.gov/statutes/cite/604.18](https://www.revisor.mn.gov/statutes/cite/604.18)
- **Substance:** Replaces the common-law first-party bad-faith claim Minnesota declined to recognize in Morris. Two elements:
  1. The insurer denied policy benefits without a reasonable basis, AND
  2. The insurer **knew of the lack of a reasonable basis** or acted in **reckless disregard** of the lack of a reasonable basis.
- **Damages and costs:**
  - **Taxable cost award**: one-half of the judgment proceeds in excess of the insurer's pre-trial offer (made at least 10 days before trial), capped at the lesser of that excess or **$250,000**.
  - **Attorney fees**: reasonable fees up to **$100,000**, if separately accounted for and not duplicative of fees recoverable elsewhere.
  - **Exclusions**: punitive/exemplary damages and attorney fees recoverable under other statutes cannot be double-counted.
- **Procedural requirements:**
  - The bad-faith claim is **not pleaded in the initial complaint**. It is added by motion after the underlying coverage action is well underway, supported by affidavits.
  - The bad-faith award is determined by the **court in a separate post-verdict proceeding**, after the fact-finder decides the underlying benefits owed.
  - **Not available** when the underlying claim is resolved by arbitration or appraisal.
- **Critical exemption — health-carrier agreements:** § 604.18, subd. 1(c) expressly **excludes "health carrier agreements"** from its scope. Most provider-payer disputes about health-insurance benefits are therefore **outside** § 604.18. The statute is in play for auto no-fault medical benefits (PIP), disability, and other non-"health carrier" first-party coverages. **Do not promise § 604.18 leverage on a routine health-insurance claim denial without confirming the policy is not a "health carrier agreement" as defined in Minn. Stat. § 62A.011, subd. 2.**
- **ERISA preemption:** As with all state bad-faith statutes, § 604.18 is preempted as applied to self-funded ERISA employer plans. For ERISA self-funded plans, the federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) attorney fees.

## Surprise billing / out-of-network protections

- **Statutes:**
  - **Minn. Stat. § 62Q.55** — Emergency services
  - **Minn. Stat. § 62A.65** — Individual market protections
- **Sources:** [revisor.mn.gov/statutes/cite/62Q.55](https://www.revisor.mn.gov/statutes/cite/62Q.55); [revisor.mn.gov/statutes/cite/62A.65](https://www.revisor.mn.gov/statutes/cite/62A.65)
- **§ 62Q.55 substance:**
  - Plans must cover emergency services 24/7 regardless of in-network status.
  - Decisions on emergency coverage denials must consider "a reasonable layperson's belief that the circumstances required immediate medical care" (the **prudent layperson standard**) and the time of day.
  - **Out-of-network emergency cost-sharing must equal in-network cost-sharing** and count toward the in-network deductible.
  - All emergency-services coverage must comply with the federal No Surprises Act.
- **§ 62A.65 substance:** Individual-market protections — guaranteed renewability, no pre-existing condition exclusions (post-2014), gender-rating prohibition. Limited direct use in billing disputes; useful when an individual-market carrier is non-renewing during an active claim.
- **No state-law ground ambulance protection.** As of 2026-05-18, Minnesota has **not** enacted ground-ambulance balance-billing protection. The federal No Surprises Act expressly excludes ground ambulance. Minnesota Ambulance Association advocacy for state protection is ongoing but no statute has been enacted. This is Minnesota's biggest patient-side gap in the surprise-billing layer. Sources: [Commonwealth Fund map](https://www.commonwealthfund.org/publications/maps-and-interactives/expanding-no-surprises-act-protect-consumers-surprise-ambulance); [MDH No Surprises FAQ](https://www.health.state.mn.us/facilities/insurance/managedcare/faq/nosurprisesact.html).
- **ERISA preemption:** § 62Q.55 does not reach self-funded ERISA employer plans. Those are covered by the federal NSA only.

## Minnesota Debt Fairness Act of 2024 (headline lever)

- **Bill:** HF 4077 (2024) — Commerce Policy Omnibus, signed by Governor Walz on June 17, 2024
- **Effective date:** Most medical-debt provisions took effect **October 1, 2024**; income-based wage-garnishment caps **April 1, 2025**
- **Sources:** [AG Ellison Oct 2024 release](https://www.ag.state.mn.us/Office/Communications/2024/10/02_DebtFairnessAct.asp); [Mid-Minnesota Legal Aid summary](https://mylegalaid.org/news-stories/debt-fairness-act-outlines-changes-you-should-know-about/); [AG effective-dates handout](https://www.ag.state.mn.us/Office/Communications/2024/docs/DFA_EffectiveDates.pdf)
- **What it does for medical debt:**
  - **Interest cap: 0%.** Reduces interest on medical debt from 8% to **zero**.
  - **Credit-bureau reporting prohibited.** Medical debt may not be reported to consumer credit reporting agencies (codified at Minn. Stat. ch. 332C; verify exact citation before pleading).
  - **No denial of medically necessary care** because of an outstanding bill (Minn. Stat. § 62J.807).
  - **No automatic spousal transfer.** A patient's medical debt does not pass to a surviving spouse by operation of law.
  - **Collection practice limits:** debt collectors may not use robo-dialers for medical debt, may not state that medical services will be withheld for nonpayment, may not contact third parties about the debt, and must give patients notice of the right to consult an attorney or the AG.
- **Wage-garnishment scaling** (effective April 1, 2025): garnishment caps scale by income, starting at **5%** of disposable earnings for low-income debtors and rising to **25%** for high-income debtors. The first **$4,000** in a bank account is exempt from garnishment.
- **Federal preemption posture:** A CFPB October 2025 interpretive rule asserts that the federal FCRA preempts state laws restricting medical-debt credit reporting. If sustained, it limits the credit-bureau-reporting portion of the DFA. Other DFA provisions (interest cap, spousal-transfer ban, denial-of-care ban, collection-practice limits) are not affected by FCRA preemption because they regulate debt itself, not consumer-reporting agencies.

## Consumer protection statutes — provider-side leverage

- **Statutes:**
  - **Minn. Stat. § 325F.69** — Prevention of Consumer Fraud Act (PCFA): prohibits "fraud, unfair or unconscionable practice, false pretense, false promise, misrepresentation, misleading statement or deceptive practice" in connection with the sale of merchandise (services included).
  - **Minn. Stat. § 325D.44** — Uniform Deceptive Trade Practices Act (UDTPA): prohibits passing-off, false product/source representations, false price-reduction statements, threats to withhold health-care services during collection, advertising prices that exclude mandatory fees (2024 amendment), and other listed practices.
  - **Minn. Stat. § 325D.45** — UDTPA remedies: injunctive relief without proof of damages, attorney fees if the defendant **willfully** engaged in deceptive practice knowing it was deceptive, costs to prevailing party.
  - **Minn. Stat. § 8.31, subd. 3a** — Private Attorney General statute: allows any person injured by a violation of § 325F.69 (and other Chapter 8 reference laws) to bring a civil action and recover **damages, costs and disbursements, costs of investigation, and reasonable attorney fees**.
- **Sources:** [revisor.mn.gov/statutes/cite/325F.69](https://www.revisor.mn.gov/statutes/cite/325F.69); [revisor.mn.gov/statutes/cite/325D.44](https://www.revisor.mn.gov/statutes/cite/325D.44); [revisor.mn.gov/statutes/cite/325D.45](https://www.revisor.mn.gov/statutes/cite/325D.45); [revisor.mn.gov/statutes/cite/8.31](https://www.revisor.mn.gov/statutes/cite/8.31)
- **Use:**
  - PCFA + § 8.31 subd. 3a is the patient's principal **private right of action** against the **hospital itself** for billing for services never rendered, upcoding, misrepresenting in-network status, or misrepresenting estimates. Damages plus attorney fees.
  - UDTPA gets injunctive relief and (for willful conduct) attorney fees. Note § 325D.44 expressly forbids "implying health care services will be withheld during collection" — a direct hit against threats made by collectors.
- **Ly v. Nystrom caveat:** Under **Ly v. Nystrom**, 615 N.W.2d 302 (Minn. 2000), private § 8.31 actions must show the conduct produces a **public benefit**, not a purely private dispute. Billing-practice claims involving a hospital's standard procedures generally meet this test (they affect many patients); a one-off billing-clerk error may not.

## Regulatory agencies

### Minnesota Department of Commerce — Consumer Services / Insurance

- **Online complaint:** [mn.gov/commerce/consumers/file-a-complaint](https://mn.gov/commerce/consumers/file-a-complaint/)
- **Phone:** main complaints line **(651) 539-1600**; Greater Minnesota **(800) 657-3602**
- **Mail:**
  > Minnesota Department of Commerce
  > 85 7th Place East, Suite 280
  > Saint Paul, MN 55101
- **Authority:** all insurance companies licensed in Minnesota, including fully insured health insurers, HMOs, PPOs, Medicare supplement. Administers § 72A.20 UCSPA and Minnesota's emergency-services and surprise-billing provisions for state-regulated plans. **No authority over self-funded ERISA plans** (route to U.S. DOL EBSA at 1-866-444-3272). Limited authority over providers and hospitals — route those to the AG and to the Minnesota Department of Health.

### Minnesota Attorney General — Consumer Protection

- **Online complaint:** [ag.state.mn.us/office/complaint.asp](https://www.ag.state.mn.us/Office/Complaint.asp)
- **Phone:** Twin Cities **(651) 296-3353**; outside Twin Cities **(800) 657-3787**; Minnesota Relay **(800) 627-3529**
- **Mail:**
  > Office of Minnesota Attorney General
  > Consumer Protection Division
  > 445 Minnesota Street, Suite 600
  > St. Paul, MN 55101
- **Authority:** enforces the Prevention of Consumer Fraud Act (§ 325F.69), the Uniform Deceptive Trade Practices Act (§ 325D.44), the Debt Fairness Act, and § 144.588 hospital pre-collection compliance. Reach over **providers, hospitals, third-party debt collectors, and original creditors**. The AG's office has actively used these powers against hospital billing practices in Minnesota (see, e.g., the 2008 settlements over hospital collection practices and the AG's role in driving the DFA).

### Minnesota Department of Health

- **Authority over hospital licensing and the Patient Bill of Rights** (Minn. Stat. § 144.651). Useful when the dispute is about hospital conduct rather than insurance. Complaints: [health.state.mn.us/facilities/regulation/ohfc](https://www.health.state.mn.us/facilities/regulation/ohfc/).

## Conciliation Court (small claims)

- **Court name:** **Conciliation Court** (one division in each county district court)
- **Jurisdictional limit:** **$20,000** (general civil claims); **$4,000** if the claim involves a consumer credit transaction — Minn. Stat. § 491A.01, subd. 3a (as amended by 2024 Minn. Laws ch. 123, art. 15, § 6)
- **Source:** [revisor.mn.gov/statutes/cite/491A.01](https://www.revisor.mn.gov/statutes/cite/491A.01); FAQs at [mncourts.gov/help-topics/conciliation-court/faqs](https://mncourts.gov/help-topics/conciliation-court/faqs)
- **Filing fee:** statutory base **$65** per filing party under Minn. Stat. § 357.022; counties may add law-library fees (typical total **$70-$80**).
- **Attorney rules:**
  - Minn. Stat. § 491A.02 lists who may represent corporations, partnerships, LLCs, sole proprietorships, and associations in conciliation court: "an officer, manager, or partner or an agent." **Attorneys are not listed as authorized representatives.**
  - In practice, Minnesota courts have held that attorneys may appear in conciliation court for natural-person parties unless the local rule restricts it, but the statute is plainly **designed to keep lawyers out** of the entity-side appearance. The corporate defendant (hospital, billing service, collector) is virtually certain to send a non-lawyer employee.
  - **Removal:** either party may remove the case to district court within 20 days of judgment by demanding a trial de novo. Removal forfeits the no-attorney advantage; the case proceeds under standard district court rules.
- **Note:** medical-debt claims by a hospital against a patient are subject to § 144.588 (above) and § 491A.01, subd. 3a's $4,000 consumer-credit-transaction cap. Hospitals filing suit on uninsured medical debt above $4,000 must use district court, not conciliation court — another reason the hospital's collection lawyer must comply with the affidavit requirement.

## Statute of limitations

- **Contracts and obligations (express or implied):** **6 years from breach** — Minn. Stat. § 541.05, subd. 1(1)
- **Source:** [revisor.mn.gov/statutes/cite/541.05](https://www.revisor.mn.gov/statutes/cite/541.05)
- **Open accounts:** Minnesota does not have a separate shorter limitation for open accounts; the six-year contract limitation applies generally to "obligation, express or implied, as to which no other limitation is expressly prescribed."

Most hospital admissions involve a signed financial-responsibility form (a written contract) or an implied contract for services. Six years from the date payment was due and not made.

**Partial payment or a written acknowledgment of the debt can restart the clock** under Minnesota common-law principles (e.g., *Sevcik v. State Farm Mut. Auto. Ins.*, on the toll-by-acknowledgment rule). Do not make a partial payment on a time-barred medical debt without legal advice — even a token payment can revive a stale debt for another six-year period.

## Ground ambulance balance billing

**Not protected under Minnesota state law as of 2026-05-18.** Minnesota has not enacted ground-ambulance balance-billing protection; the federal No Surprises Act expressly excludes ground ambulance. Minnesota patients facing a ground-ambulance balance bill have only:

- The federal NSA's protection for **air ambulance** (does not apply to ground)
- The general consumer-fraud and deceptive-trade-practices laws if the bill is itself deceptive or upcoded
- The Debt Fairness Act's 0% interest cap and credit-bureau-reporting prohibition (the bill cannot be reported or accrue interest, but the underlying charge stands)
- Negotiation, charity-care screening under § 144.587, and § 144.588 pre-collection compliance

Sources: [Commonwealth Fund state map](https://www.commonwealthfund.org/publications/maps-and-interactives/expanding-no-surprises-act-protect-consumers-surprise-ambulance); [American Ambulance Association overview](https://ambulance.org/sp_product/state-balance-billing-overview-v1/).

## No-fault auto insurance and medical bills

- **Statute:** **Minn. Stat. §§ 65B.41 to 65B.71** (Minnesota No-Fault Automobile Insurance Act); medical-benefits provision at **§ 65B.44, subd. 2**
- **Source:** [revisor.mn.gov/statutes/cite/65B.44](https://www.revisor.mn.gov/statutes/cite/65B.44)
- **Substance:** Every Minnesota auto policy must include at least **$20,000 in medical-expense benefits per person** for injuries arising from the use of an auto, payable without regard to fault. Covers medical, surgical, x-ray, dental, chiropractic, rehabilitation, prescription drugs, ambulance, hospital, and (limited) extended care. Reparation obligors may not impose preestablished benefit limitations or managed-care arrangements.
- **Use:**
  - Auto-accident medical bills generally route to the patient's auto insurer first under no-fault, not to health insurance. A hospital billing a Minnesota auto-injury patient must first attempt to collect from the PIP carrier; § 144.588 requires "all known third-party payors have been properly billed" as a condition of collection.
  - § 604.18 statutory bad faith **is** available against the PIP carrier (auto coverage is not a "health carrier agreement").
  - PIP exhaustion ($20,000 cap) is common in serious accidents; the patient's health insurance then becomes the secondary payor. Track the order: PIP → health insurer → patient. A hospital that bills the patient first while PIP coverage remains has a § 144.588 problem.

## Hospital charity care

- **Statute:** **Minn. Stat. § 144.587** (charity-care screening and pre-collection)
- **Source:** [revisor.mn.gov/statutes/cite/144.587](https://www.revisor.mn.gov/statutes/cite/144.587)
- **Substance:**
  - Hospitals must screen uninsured patients for charity-care eligibility **within 30 days** of service, in person or by telephone.
  - Hospitals must assist patients in applying and may not impose application procedures that place an unreasonable burden on the patient (taking into account disability or language).
  - Hospitals must post charity-care availability notices in multiple languages and make policies and applications available online.
  - **Until the hospital has determined the patient is ineligible for charity care, it may not initiate** payment plans, debt-collection referrals, loans, or accept credit card payments over $500.
  - Patients may decline screening or apply for charity care without consequence.
- **Use:** This is one of the strongest pre-collection statutes in the country. Any Minnesota hospital that has not screened the uninsured patient for charity care has failed a § 144.588 affidavit precondition; any collection action that proceeded without the screening is dismissable.
- **Screening tool:** Dollar For at [dollarfor.org/state_sheet/minnesota](https://dollarfor.org/state_sheet/minnesota/).

## Hospital lien statute

- **Citations:** **Minn. Stat. §§ 514.68 through 514.69**
- **Sources:** [revisor.mn.gov/statutes/cite/514.68](https://www.revisor.mn.gov/statutes/cite/514.68)
- **Substance:** A hospital operating in Minnesota has a lien for the reasonable charges for hospital care of an injured person, attaching to **any and all causes of action accruing to the injured person** against a third party who caused the injury. **Not a lien on the patient's home, wages, or bank accounts.** The lien is expressly **subordinate to attorney liens** (attorney fees come first out of any recovery).
- **Perfection requirements:** Verified statement filed with the court administrator of the district court of the county where the hospital is located, identifying the patient, the injury date, the amount claimed, and known liable third parties; with notice to the patient and known liable parties.
- **Use:** A Minnesota hospital lien on a third-party tort recovery is enforceable only if perfected by statutory filing. Any lien asserted against a patient's wages, bank account, or home title is per se invalid — those require a judgment under standard collection procedures, which in turn require § 144.588 compliance.

## Credit reporting

**Minnesota prohibits medical-debt reporting to consumer credit reporting agencies under the Debt Fairness Act of 2024**, effective October 1, 2024. This is the broadest state-level restriction on medical-debt reporting in the United States. Verify the exact statutory citation (DFA provisions appear in Minn. Stat. ch. 332C and related sections) before pleading.

**Federal preemption posture:** A CFPB October 2025 interpretive rule asserts FCRA preemption of state medical-debt-reporting restrictions. If sustained on judicial review, it limits Minnesota's reporting ban. As of 2026-05-18, the DFA's reporting prohibition is still in force and the federal posture is contested. Patients can:

- Send the furnisher a written dispute citing the DFA's reporting prohibition (Minnesota law) and the federal FCRA dispute right (15 U.S.C. §§ 1681i, 1681s-2).
- File with the AG (DFA enforcement) and the CFPB (FCRA furnisher accuracy).
- Layer the credit-bureau voluntary changes (paid medical debt removed; <$500 not reported; 1-year delay) as backup.

## Wage garnishment

- **Statute:** Minn. Stat. ch. 571 (garnishment); income-based scaling under the Debt Fairness Act (2024) effective April 1, 2025
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a court judgment. Pre-judgment garnishment is not available for ordinary consumer debt. **Post-judgment garnishment is capped on an income-graduated scale** under the DFA: **5%** of disposable earnings for low-income debtors up to **25%** for high-income debtors. The first **$4,000** in a bank account is exempt.
- **§ 144.588 layer:** Even a hospital with a judgment must serve the § 144.588 affidavit before garnishment; absence of the affidavit triggers mandatory dismissal of the garnishment proceeding.

## Quick reference for letter rendering

When the LLM renders a Minnesota-bound letter, substitute these defaults:

| Field                                      | Value                                                                                                                                                                  |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| State statute (itemization right)          | **Minn. Stat. § 144.591** — automatic 30 days after discharge, no charge to patient, line-item descriptions required (no codes or "miscellaneous")                     |
| Pre-collection compliance lever            | **Minn. Stat. § 144.588** affidavit requirement — mandatory dismissal with prejudice for noncompliance                                                                 |
| Charity-care screening                     | **Minn. Stat. § 144.587** — must screen within 30 days, no collection action until screening complete                                                                  |
| State insurance/commerce dept. CC line     | Minnesota Department of Commerce, Consumer Services, 85 7th Place East, Suite 280, Saint Paul, MN 55101; (651) 539-1600                                                |
| State AG CC line                           | Office of Minnesota Attorney General, Consumer Protection Division, 445 Minnesota Street, Suite 600, St. Paul, MN 55101; (651) 296-3353 / (800) 657-3787               |
| Small-claims court name                    | **Conciliation Court** (within the district court of [county])                                                                                                         |
| Small-claims limit                         | **$20,000** (general); **$4,000** (consumer credit transactions)                                                                                                       |
| Filing fee                                 | "$65 statutory plus county law-library fee, typically $70-$80 total"                                                                                                   |
| Statute of limitations (in 30-day warning) | "Minn. Stat. § 541.05, subd. 1(1) (six years for contract or other obligation)"                                                                                        |
| Provider-side private right of action      | **Minn. Stat. § 325F.69 (PCFA) + § 8.31, subd. 3a** — damages, costs, investigation costs, **reasonable attorney fees**                                                |
| Deceptive trade practices                  | **Minn. Stat. § 325D.44** — including the prohibition on implying services will be withheld during collection — with attorney fees for willful conduct under § 325D.45 |
| Debt Fairness Act (medical debt)           | **0% interest cap, credit-bureau reporting prohibited, no denial of care for unpaid bills, no spousal transfer** — effective Oct 1, 2024 (HF 4077)                     |
| Bad-faith (insurance)                      | **Minn. Stat. § 604.18** — taxable cost up to $250k, attorney fees up to $100k. **Does not apply to "health carrier agreements"** — verify policy type before citing   |
| UCSPA (administrative only)                | **Minn. Stat. § 72A.20** — cite in Commerce complaints; no private right of action under *Morris v. American Family Mut. Ins. Co.*, 386 N.W.2d 233 (Minn. 1986)        |
| Ground ambulance                           | **No state-law protection** — patient must negotiate or use general consumer-fraud levers                                                                              |

## Key Minnesota-specific advantages

Worth keeping in mind when triaging a MN patient's bills:

1. **Debt Fairness Act stack.** Zero-percent interest, no credit-bureau reporting, no spousal transfer, no denial of care. No other state has assembled all four in one package. Cite the DFA prominently in any first-response letter — most billing departments and collectors are still catching up to its scope.
2. **§ 144.588 affidavit precondition.** A hospital that sues or garnishes without the seven-point affidavit gets **mandatory dismissal with prejudice**. This is one of the cleanest procedural defenses in the country. Demand the affidavit in your first response.
3. **§ 144.587 charity-care screening.** Until the hospital has screened the uninsured patient and either approved or denied charity care, all collection actions are blocked. The screening obligation runs whether the patient asked for it or not.
4. **§ 325F.69 PCFA + § 8.31 subd. 3a private right of action.** Patient can sue the hospital itself for fraud, unfair practice, or misrepresentation in billing, and recover **attorney fees**. Far broader than the federal FDCPA, which reaches only third-party collectors.
5. **Conciliation Court at $20,000, attorneys functionally excluded for corporate parties.** Minnesota's small-claims limit is among the highest, and § 491A.02 forces hospitals and billing services to appear through a non-lawyer officer or employee. The economic asymmetry favors the patient.
6. **No common-law first-party bad faith, but § 604.18 fills part of the gap.** Be careful: § 604.18 expressly excludes "health carrier agreements," so it does not apply to most health-insurance claim denials. It does apply to auto PIP, disability, and similar coverages.
7. **No-fault auto interaction.** Auto-injury medical bills route to the PIP carrier first ($20k minimum). A hospital that bills the patient before exhausting PIP coverage has a § 144.588 problem.
