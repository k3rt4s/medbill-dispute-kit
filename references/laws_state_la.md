# Louisiana state pack

The fully-worked state-law layer for Louisiana patients. The LLM uses this when the patient's state is Louisiana. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md), Tennessee at [`laws_state_tn.md`](laws_state_tn.md), Mississippi at [`laws_state_ms.md`](laws_state_ms.md). All citations verified against public sources as of 2026-08-19. Re-verify annually.

Louisiana is not a common-law state. It runs on a civil-law tradition descended from French and Spanish law, not English common law, and that changes more than terminology. Four things a Louisiana pack has to get right that no common-law state pack has to think about:

1. **No UCC Article 2.** Louisiana is the only US state that never adopted the Uniform Commercial Code's sales article. The UCC § 2-305 "reasonable price" argument this kit cites in every other state pack (see [`laws_federal.md`](laws_federal.md)) has no direct home in Louisiana. Louisiana's own Civil Code fills the same gap through contract-interpretation articles (La. C.C. arts. 1983, 2054, 2055) and, if no contract claim is available, the quasi-contractual remedy of enrichment without cause (La. C.C. art. 2298), the closest Louisiana equivalent to common-law quantum meruit. See "No UCC 2-305, the Louisiana substitute" below.
2. **Prescription, not "statute of limitations."** Louisiana calls a time-bar "prescription." A hospital bill does not get the 10-year period just because the patient signed a financial-responsibility form at admission. Most medical bills prescribe in **3 years** as a claim for compensation for services rendered or an action on an open account (La. C.C. art. 3494), not the 10-year default for personal actions generally (La. C.C. art. 3499). Getting this wrong in a demand letter overstates the patient's runway by 7 years.
3. **Health-insurance bad faith lives in its own statute.** Louisiana's general property-and-casualty claims-handling and bad-faith statute, La. R.S. 22:1892, expressly excludes life, health, and accident policies. The statute that actually governs a medical claim, La. R.S. 22:1821, is a different section with its own 30-day deadline and its own penalty. Citing 1892 or the now-repealed 1973 against a health insurer is citing the wrong statute.
4. **A brand-new 2026 state medical-debt law.** The Louisiana Medical Debt Protection Act (La. R.S. 51:1501-1507), effective June 9, 2026, caps interest on medical debt for medically necessary care at 3% a year and voids any higher contractual rate. It is new enough that its practical application hasn't been tested; verify it has not been amended before relying on it in a filing.

## Hospital itemization right

- **General statute:** **La. R.S. 40:2010**
- **Source:** [codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-40-sect-2010](https://codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-40-sect-2010/)
- **What it requires:** Every hospital licensed by the Louisiana Department of Health must have an itemized statement of billed services available **within 10 business days of discharge**. The hospital must tell the patient the statement is available before the patient is discharged, and a copy must be presented to the patient within that 10-day window. An **interim statement** must be furnished on request by the patient or an authorized agent, even before the 10 days run.
- **Duty is automatic**, similar to Georgia's automatic 6-business-day duty and unlike Tennessee's request-triggered one. A written request is not required, but sending one anyway creates a paper trail.
- **Facility-based physician billing disclosure:** **La. R.S. 22:1880(D)** separately requires that when a facility-based physician bills a patient for out-of-network services, the bill itself must include an itemized list of services and dates, a conspicuous notice ("NOTICE: THIS IS A BILL. BASED UPON INFORMATION FROM YOUR HEALTH PLAN, YOU OWE THE AMOUNT SHOWN"), and a phone number for billing questions. Source: [codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-22-sect-1880](https://codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-22-sect-1880/).
- **Injury-related itemization (tied to the hospital privilege, see "Hospital lien" below):** **La. R.S. 9:4755** requires a health care provider, hospital, or ambulance service to furnish an itemized statement within **30 days** of a certified-mail written request when the bill arises from a third-party injury claim. Failure to comply **dissolves the provider's privilege** on the settlement proceeds, a real enforcement tooth this general itemization duty doesn't otherwise have.

## Unfair claims settlement practices

- **Statute:** **La. R.S. 22:1964(14)**, part of Title 22's general trade-practices chapter
- **Source:** [codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-22-sect-1964](https://codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-22-sect-1964/)
- **Substance:** Lists unfair claims-settlement practices when committed "with such frequency as to indicate a general business practice": misrepresenting policy provisions, failing to acknowledge communications promptly, refusing to pay claims without a reasonable investigation, and similar conduct.
- **Critical caveat:** § 1964 itself does not create a private right of action. The Louisiana Supreme Court in *Langsford v. Flattman*, 2003-1586 (La. 2004), held that a third-party claimant has no direct cause of action against an insurer absent a statute creating one, and that statutes creating such a right (including R.S. 22:1892 and the § 1964(14) list) must be strictly construed. Enforcement of § 1964 standing alone is by the Commissioner of Insurance under **R.S. 22:1967-1970**. Cite § 1964(14) in an LDI complaint as evidence of a pattern; do not plead it alone in court.

## Bad-faith failure to pay

Louisiana splits this by policy type. Get the right one; they are not interchangeable.

### Health and accident claims, the one that applies to most medical bills

- **Statute:** **La. R.S. 22:1821**
- **Source:** [codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-22-sect-1821](https://codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-22-sect-1821/)
- **Substance:** Health and accident insurance claims must be paid **within 30 days** of written notice and proof of claim, unless the insurer has "just and reasonable grounds" for the delay. Failure to comply subjects the insurer to a penalty of **double the health and accident benefits due during the period of delay**, plus **attorney fees determined by the court**. Accidental-death claims get a separate 60-day window with 6% annual interest on late payment.
- **Applies to self-insured employer plans too**, the statute text extends the penalty and attorney-fee provisions to any person or organization providing health and accident coverage "as a self-insurer for his or its employees." In practice, ERISA preemption still knocks this out for genuinely ERISA-covered self-funded plans (see below); the self-insurer language matters more for non-ERISA self-funded arrangements (church plans, some governmental plans).
- **This is a private right of action**, brought by the insured directly.

### Property and casualty claims, not the medical-bill statute

- **Statute:** **La. R.S. 22:1892**, restructured by **2024 Regular Session Act No. 3 (SB 323)**, effective **July 1, 2024**, which folded the former good-faith-duty statute, **La. R.S. 22:1973** (now repealed), into 1892(I).
- **Source:** [legis.la.gov/legis/Law.aspx?d=509041](https://www.legis.la.gov/legis/Law.aspx?d=509041)
- **Why it does not apply to a medical bill:** Subsection K states plainly: "The provisions of this Section do not apply to claims made under life and health and accident insurance policies." That exclusion covers the whole section, including the good-faith duty in subsection I. Citing R.S. 22:1892 (or the old 22:1973) against a health insurer in a Louisiana dispute letter is citing a statute that carves out the exact claim type being disputed.
- **When it does matter:** auto med-pay and other property/casualty first-party claims connected to an accident (as opposed to the health plan's own coverage of the resulting medical bills).
- **ERISA preemption:** as elsewhere, state-law bad-faith remedies are generally preempted for ERISA-covered self-funded employer plans. R.S. 22:1821's own self-insurer language does not override federal preemption.

## Louisiana Unfair Trade Practices Act (LUTPA), private right of action

- **Statute:** **La. R.S. 51:1401 et seq.**; private right of action at **La. R.S. 51:1409**
- **Source:** [codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-51-sect-1409](https://codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-51-sect-1409/)
- **Substance:** Any person who suffers an ascertainable loss from an unfair or deceptive trade practice may sue individually for actual damages. If the court finds the practice was **knowingly used after the Attorney General had put the defendant on notice**, damages are trebled. The court awards **reasonable attorney fees and costs** to a prevailing plaintiff.
- **Prescription:** **one year**, running from the transaction or act giving rise to the claim, per the statute's own text. This is shorter than the general 3-year open-account period and much shorter than the 10-year default, so do not sit on a LUTPA claim.
- **Exemptions:** **La. R.S. 51:1406** exempts, among others, conduct subject to the jurisdiction of the insurance commissioner, financial-institution regulators, and public-utility regulators. Source: [codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-51-sect-1406](https://codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-51-sect-1406/). In practice this routes insurer-side disputes to Title 22 remedies (R.S. 22:1821, 22:1892, 22:1964) and away from LUTPA. LUTPA remains available against hospitals, providers, and debt collectors for deceptive billing or collection conduct that is not itself an insurance-regulated act.
- **Open question for hospitals specifically:** see the gaps section at the end. The Attorney General's own consumer-dispute intake explicitly excludes "licensed professionals (doctors, dentist, attorneys, etc.)"; whether that exclusion extends to a hospital as a corporate billing entity (as opposed to an individual physician) was not confirmed against a primary source. Do not assume LUTPA reaches a hospital's billing office without independent confirmation for the specific dispute.

## Balance billing

- **Statute:** **La. R.S. 22:1874**, "Billing by contracted health care providers"
- **Source:** [codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-22-sect-1874](https://codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-22-sect-1874/)
- **What it does:** A health care provider **contracted (in-network)** with the patient's health insurance issuer is prohibited from billing, attempting to collect, or collecting any amount from the enrollee in excess of the contracted reimbursement rate for covered services, other than copayment, coinsurance, deductible, noncovered services, or amounts identified on the explanation of benefits. A contracted provider **may not sue** an enrollee to collect an amount above the contracted rate; if it does anyway, **the prevailing party recovers costs and reasonable attorney fees**.
- **Why this is broader than the federal No Surprises Act:** the federal NSA only reaches specific out-of-network scenarios (emergency care, ancillary providers at an in-network facility). R.S. 22:1874 bars excess billing by **any** contracted, in-network provider for **any** covered service, a wider net than the federal floor.
- **Limits:** applies to providers contracted with a "health insurance issuer" regulated by Louisiana. As with the rest of Title 22, this does not clearly reach self-funded ERISA employer plans; those patients fall back on the federal NSA for what it covers.
- **Federal floor still applies:** for true out-of-network emergency and ancillary-provider scenarios, the federal No Surprises Act is the primary protection; see [`laws_federal.md`](laws_federal.md). R.S. 22:1874 is a Louisiana-specific supplement for in-network overbilling, not a replacement for the NSA.

## Regulatory agencies

### Louisiana Department of Insurance (LDI)

- **Main site:** [ldi.la.gov](https://ldi.la.gov)
- **Online complaint form:** [ldi.la.gov/onlineservices/ConsumerComplaintForm](https://www.ldi.la.gov/onlineservices/ConsumerComplaintForm)
- **Phone:** **225-342-5900**, toll-free **1-800-259-5300**
- **Office of Health (health-plan-specific line):** 225-219-4770
- **Mail:** P.O. Box 94214, Baton Rouge, LA 70804-9214
- **Authority over:** fully-insured health plans, HMOs, and insurers licensed in Louisiana, including R.S. 22:1821, 22:1874, 22:1880.2, and 22:1964 complaints. **No authority over self-funded ERISA plans**; route those to DOL EBSA at 1-866-444-3272.
- Note: LDI's own complaint-form page returned an access error to this session's automated fetch; the URL and phone numbers above were confirmed through independent search results carrying the LDI domain and matching official page titles, not a direct page load. Confirm the portal is live before sending a patient to it.

### Louisiana Attorney General, Consumer Protection Section

- **Phone (hotline):** **1-800-351-4889**; office **225-326-6400**; fax 225-326-6499
- **Online complaint:** [ag.state.la.us/Page/ConsumerDispute](https://www.ag.state.la.us/Page/ConsumerDispute)
- **Mail:** P.O. Box 94005, Baton Rouge, LA 70804-9005
- **Authority over:** LUTPA enforcement, general unfair-and-deceptive-practices complaints against businesses, including debt collectors.
- **Does not handle:** insurance claims (route to LDI), airlines, utilities, elected officials, child support, employer-employee disputes, or, in the office's own words, "licensed professionals (doctors, dentist, attorneys, etc.)." As noted above, whether a hospital as an institution falls inside or outside that last carve-out is not confirmed; if the AG's intake declines a hospital-billing complaint, LDI (if an insurer is involved) or small claims court are the fallback paths.

## Small claims court, justice of the peace and city-court divisions

Louisiana has no single court called "small claims court." Two parallel tracks exist, both capped at the same dollar figure:

- **Justice of the Peace Courts:** civil jurisdiction concurrent with district court up to **$5,000**, per **La. Code Civ. Proc. art. 4911**. Not confirmed against a primary-source fetch in this session (Justia and FindLaw pages for this specific article did not load); the figure is corroborated by multiple independent secondary sources and is consistent with the small-claims-division figure below, but verify against the article text directly before citing it in a filing.
- **Small Claims Divisions of city courts:** established under **La. R.S. 13:5200-5211**; jurisdiction up to **$5,000, exclusive of interest, court costs, attorney fees, or penalties** (R.S. 13:5202). Source: [codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-13-sect-5202](https://codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-13-sect-5202/). No more than 10 plaintiffs may join an action; class actions, summary proceedings, and executory proceedings are prohibited; the division is "not a court of record."
- **Procedure:** informal, technical evidence rules relaxed; hearsay is admissible if the judge finds it generally reliable (R.S. 13:5203). Attorneys are permitted but not required for individuals.
- **Filing fee:** the statutory base is **$35 per defendant** (R.S. 13:5205), but individual city courts charge more in practice, for example roughly $75-$115 depending on the parish and number of defendants. Confirm the local court's actual fee schedule.
- **Above $5,000:** the claim moves to regular city court (**$15,000** default civil jurisdiction under **La. Code Civ. Proc. art. 4843**, though several parishes' city courts have a higher local limit, up to $50,000 in some) or parish court (**$20,000** under **La. Code Civ. Proc. art. 4842**) or district court.
- **No jury risk at this level:** Louisiana limits jury trials to cases where an individual petitioner's claim exceeds **$10,000** (**La. Code Civ. Proc. art. 1732**, lowered from $50,000 effective January 1, 2021). A small-claims-division case, capped at $5,000, never reaches that threshold.
- Sources: [codes.findlaw.com/la/code-of-civil-procedure/la-code-civ-proc-tit-i-art-4842](https://codes.findlaw.com/la/code-of-civil-procedure/la-code-civ-proc-tit-i-art-4842/); [codes.findlaw.com/la/code-of-civil-procedure/la-code-civ-proc-tit-i-art-4843](https://codes.findlaw.com/la/code-of-civil-procedure/la-code-civ-proc-tit-i-art-4843/); [codes.findlaw.com/la/code-of-civil-procedure/la-code-civ-proc-tit-v-art-1732](https://codes.findlaw.com/la/code-of-civil-procedure/la-code-civ-proc-tit-v-art-1732/).

## Statute of limitations, called prescription in Louisiana

This is the section where a common-law pack's usual pattern breaks. Do not reuse the "6 years, written contract" framing from other state packs.

- **General personal action (residual default):** **10 years**, **La. C.C. art. 3499**. Source: [codes.findlaw.com/la/civil-code/la-civ-code-tit-xxiv-art-3499](https://codes.findlaw.com/la/civil-code/la-civ-code-tit-xxiv-art-3499/). This is the article most likely to be mis-cited for a medical bill because it sounds like the general contract rule.
- **The one that actually governs most medical bills:** **3 years**, **La. C.C. art. 3494**, which subjects to a three-year prescription both "an action for the recovery of compensation for services rendered, including... professional fees" (art. 3494(1)) and "an action on an open account" (art. 3494(4)). Louisiana courts treat hospital and provider bills as falling into one or both of these categories. Source: [codes.findlaw.com/la/civil-code/la-civ-code-tit-xxiv-art-3494](https://codes.findlaw.com/la/civil-code/la-civ-code-tit-xxiv-art-3494/).
- **Practical rule of thumb:** treat a Louisiana medical bill as prescribing in **3 years from the date it became due**, not 10, unless there is a specific written promissory note or settlement agreement that would independently qualify as its own contract with its own term. When in doubt, use the shorter period; it is the safer assumption for a patient deciding whether to raise prescription as a defense.
- **Prescription must be affirmatively raised.** **La. C.C. art. 3452** provides that "courts may not supply a plea of prescription" on their own. A patient (or their attorney) must actually plead it, typically through the peremptory exception of prescription, or a stale debt can still result in a judgment.
- **Payment or acknowledgment restarts the clock.** **La. C.C. art. 3464** interrupts prescription when the debtor acknowledges the creditor's right, including by partial payment or a written or verbal promise to pay. Under **art. 3466**, an interruption wipes out the time that already ran and starts the full period over. **Do not make a partial payment on an old Louisiana medical bill without understanding this**; it can revive a claim that was about to prescribe.
- **LUTPA:** 1 year (see above), separate from and much shorter than either prescription period for the underlying debt.

## Ground ambulance balance-billing

- **Statute:** **La. R.S. 22:1880.2**, enacted by 2023 Regular Session Act 453 (SB 109), effective **August 1, 2023**
- **Source:** [codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-22-sect-1880-2](https://codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-22-sect-1880-2/)
- **What it does:** for out-of-network **emergency ground ambulance** services, the minimum reimbursement an insurer must pay is (1) the rate set or approved by the local governmental entity where the service originated, or, if none, (2) **325% of the current Medicare rate for the same service in the same geographic area, or the provider's billed charges, whichever is less**. Patient cost-sharing is capped at the in-network level, and payment under the statute is "payment in full" for the covered service, the ambulance provider cannot balance-bill for the difference.
- **Why this matters:** the federal No Surprises Act explicitly excludes ground ambulance. Louisiana is one of a small group of states (with Georgia, California, Texas, and Arkansas among 2023-2024 additions) that closed that specific gap for its own regulated plans.
- **Limits:** covers **emergency** ground ambulance under Louisiana-regulated health plans; likely does not reach self-funded ERISA plans, consistent with the rest of Title 22. Non-emergency ground ambulance and air ambulance are not addressed by this section (air ambulance is covered by the federal NSA).

## Credit reporting

Louisiana has **not** enacted a state-specific law restricting medical debt from appearing on credit reports, unlike New York, California, Colorado, and a growing list of other states that acted after the CFPB's 2024 credit-reporting rule was vacated in 2025. Louisiana patients rely on:

- The 2022-2023 voluntary changes by Equifax, Experian, and TransUnion (paid medical collections removed; medical collections under $500 excluded; one-year delay before reporting).
- Federal FCRA dispute rights, 15 U.S.C. §§ 1681i, 1681s-2.

**The 2026 Louisiana Medical Debt Protection Act does not appear to address credit reporting.** Based on the sources available to this session, its provisions are limited to interest-rate limits and debt-collection restrictions (see "Wage garnishment and the 2026 Act" below), not furnishing to credit bureaus. Confirm this against the enacted text if a patient's dispute turns specifically on a credit-report entry.

## Hospital lien statute, Louisiana calls it a privilege

Louisiana's civil-law vocabulary shows up here too: this is not called a "lien," it is a "privilege" (a preferred claim on specific property, a civil-law concept with a different pedigree than the common-law lien).

- **Citations:** **La. R.S. 9:4751 through 9:4755**
- **Source:** [codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-9-sect-4752](https://codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-9-sect-4752/); [codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-9-sect-4755](https://codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-9-sect-4755/)
- **Substance:** a health care provider, hospital, or ambulance service that furnishes services to an injured person has a privilege for its reasonable charges, attaching **only to the net proceeds of any recovery, settlement, judgment, or insurance indemnity payment** arising from the same injury, on account of a third party's liability. **Not a lien on the patient's home, wages, or general bank accounts.** An attorney's privilege on the same proceeds outranks the provider's privilege.
- **Perfection:** the privilege becomes effective only when **written notice** (certified mail, or fax with proof of transmission) is delivered, before any proceeds are paid out, to the injured person, their attorney, the person alleged liable, that person's insurer, and any insurer obligated to pay indemnity to the injured person (**R.S. 9:4753**).
- **Payor liability for ignoring notice:** a payor who disburses proceeds to the injured person after receiving proper notice remains liable to the provider for the privileged amount, up to the net amount paid (**R.S. 9:4754**).
- **Itemization tied to the privilege:** on a certified-mail written request, the provider must furnish an itemized statement within **30 days**, or the privilege is **dissolved and ineffective** (**R.S. 9:4755**). This gives the general itemization right in this specific context real teeth.

## Louisiana charity care

- **No general state statute** requires a private nonprofit or for-profit hospital to offer charity care beyond the federal IRS § 501(r) floor (see [`laws_federal.md`](laws_federal.md)). Program generosity is up to each hospital's own financial-assistance policy.
- **State-supported "charity hospitals" are different.** **La. R.S. 46:6** governs admission to hospitals operated by the LSU Board of Supervisors (the modern successor to Louisiana's historic public charity-hospital system, for example University Medical Center New Orleans and University Health Shreveport). Any bona fide Louisiana resident needing medical services, including the uninsured, is eligible for treatment; non-emergency care may be denied only to patients above **200% of the federal poverty guidelines** who refuse to pay reasonable charges, and emergency care and medically necessary treatment for incarcerated persons are separately protected. Source: [codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-46-sect-6](https://codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-46-sect-6/).
- This LSU-system rule is narrow: it applies to that specific set of state-operated hospitals, not to private nonprofit hospitals generally. For a private nonprofit hospital, screen through [Dollar For](https://dollarfor.org) and demand the hospital's federal § 501(r) Financial Assistance Policy as with any other state.

## Wage garnishment and the 2026 Act

- **General wage exemption:** **La. R.S. 13:3881** exempts **75% of a debtor's disposable weekly earnings** from seizure, with a floor equal to 30 times the federal minimum hourly wage, tracking the federal Consumer Credit Protection Act's 25%-of-disposable-earnings cap from the other direction. A judgment is required before any garnishment. Source: [codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-13-sect-3881](https://codes.findlaw.com/la/revised-statutes/la-rev-stat-tit-13-sect-3881/).
- **The Louisiana Medical Debt Protection Act**, **La. R.S. 51:1501-1507**, created by **2026 Regular Session Act No. 897 (SB 414)**, effective **June 9, 2026**: caps the annual interest rate chargeable on medical debt for "medically necessary care" at **3%**, and voids any contractual provision setting a higher rate. Multiple independent news and advocacy sources describe additional provisions in the same Act restricting wage and bank-account garnishment for this category of debt (reportedly tied to a percentage of the federal poverty level) and prohibiting a lien or foreclosure on a patient's primary residence or vehicle for medical debt. **This session could not independently confirm the specific garnishment threshold or the exact lien-prohibition language against the enrolled bill's primary text** (the official PDF did not render as extractable text to the tools available). Treat the 3% interest cap as confirmed and the garnishment/lien details as reported-but-unverified until checked against the enrolled bill or a Louisiana Department of Justice summary.

## Quick reference for letter rendering

When the LLM renders a Louisiana-bound letter, substitute these defaults:

- **State statute (itemization right):** **La. R.S. 40:2010**, automatic, available within 10 business days of discharge, no request required (send one anyway for the paper trail).
- **State insurance department (CC line):** Louisiana Department of Insurance, P.O. Box 94214, Baton Rouge, LA 70804-9214 ([ldi.la.gov](https://ldi.la.gov))
- **State AG consumer protection (CC line):** Louisiana Department of Justice, Consumer Protection Section, P.O. Box 94005, Baton Rouge, LA 70804-9005
- **Small-claims track:** Small Claims Division of the [Parish] City Court, or Justice of the Peace Court, for claims up to $5,000
- **Filing fee (in the 30-day warning):** "approximately $35-$115 depending on the parish and number of defendants"
- **Statute of limitations / prescription (in the 30-day warning):** "La. C.C. art. 3494 (three years, action for services rendered or on open account)", not the 10-year article 3499 default
- **For health-insurer bad faith:** cite **La. R.S. 22:1821** (30-day payment deadline, double-benefit penalty plus attorney fees), not R.S. 22:1892
- **For in-network overbilling:** cite **La. R.S. 22:1874**
- **For ground ambulance:** cite **La. R.S. 22:1880.2** (325% of Medicare floor, or local government rate)
- **For provider-side price disputes (no UCC 2-305 available):** cite **La. C.C. arts. 1983 and 2054-2055** (good-faith performance and equitable gap-filling) as the primary theory, with **La. C.C. art. 2298** (enrichment without cause) as the subsidiary fallback if no contract claim applies. See "No UCC 2-305, the Louisiana substitute" below.

## No UCC 2-305, the Louisiana substitute

Every other state pack in this kit reaches for UCC § 2-305's "reasonable price" gap-filler when a patient signed an admission form agreeing to pay "all charges" with no price stated. Louisiana never adopted UCC Article 2, so that citation does not work here; a Louisiana hospital admission is governed entirely by the Civil Code's law of obligations and, separately, its law of sale (La. C.C. art. 2439 et seq., which covers the sale of a "thing" for a price and is a poor fit for a services-heavy hospital bill in any case).

The Louisiana substitute is built from three articles working together, not one:

1. **La. C.C. art. 1983**: "Contracts have the effect of law for the parties... [and] must be performed in good faith." A hospital that fixes an unreasonably inflated chargemaster price for an "all charges" agreement is arguably not fixing that price in good faith, the same substantive idea UCC 2-305(2) expresses for a sale of goods.
2. **La. C.C. arts. 2054 and 2055**: when a contract leaves a particular situation unaddressed (here, the actual price), the law fills the gap with "whatever the law, equity, or usage regards as implied." Article 2055 defines equity in this context as the principle that "no one is allowed to enrich himself unjustly at the expense of another," and usage as the practice regularly observed in similar contracts, comparable cash-pay or negotiated rates for the same service are the natural evidence here.
3. **La. C.C. art. 2298, enrichment without cause**: if no contract theory reaches the dispute, Louisiana's quasi-contractual remedy (its version of the actio de in rem verso, the closest Louisiana equivalent to common-law quantum meruit) allows recovery measured by the lesser of the enrichment or the impoverishment. This remedy is **explicitly subsidiary**, the article itself says it "shall not be available if the law provides another remedy." Plead it as a fallback, not a first theory, when a contract-based argument (arts. 1983, 2054-2055) is available.

Practical effect for a dispute letter: instead of "the hospital's charge violates UCC § 2-305's reasonable-price requirement," a Louisiana letter should read something like "the hospital's charge, fixed unilaterally and far above the reasonable value of the service, is inconsistent with its duty of good faith performance under La. C.C. art. 1983 and the equitable gap-filling required by La. C.C. arts. 2054-2055." Comparable cash-pay prices (see [`resources.md`](resources.md)) remain just as useful as evidence; only the citation changes.

## Key Louisiana-specific advantages

1. **The health-insurer bad-faith statute has real teeth and is easy to trigger.** R.S. 22:1821's 30-day deadline and double-benefit-plus-attorney-fees penalty apply to ordinary health and accident claims, not just a narrow subset, and the statute explicitly reaches self-insured coverage arrangements too (subject to ERISA preemption where it genuinely applies).
2. **In-network overbilling has its own statute with fee-shifting built in.** R.S. 22:1874 bars contracted providers from suing patients for more than the contracted rate, and awards costs and attorney fees to whichever side prevails if they do sue, a real deterrent against a hospital's in-house billing department pursuing a balance-billed patient in court.
3. **Ground ambulance is covered.** R.S. 22:1880.2 closes the federal NSA's biggest gap for Louisiana-regulated plans, with a 325%-of-Medicare floor.
4. **The 3-year prescriptive period cuts both ways in the patient's favor.** Because most Louisiana medical debt prescribes in 3 years rather than a common-law state's typical 4-6, a patient facing an old, half-forgotten bill reaches the point where prescription is a viable defense meaningfully sooner, provided they do not restart the clock with a careless partial payment.
5. **A fresh, patient-favorable 2026 interest-rate cap.** The Louisiana Medical Debt Protection Act's 3% annual interest cap on medically-necessary-care debt is a real, specific number a patient can hold a collector to once the Act's garnishment and lien provisions are confirmed against primary text.

## Gaps: claims this pack could not fully verify

Listed here rather than silently included, per this kit's standard: omit or flag what cannot be confirmed rather than guess.

1. **Justice of the Peace Court's $5,000 jurisdictional limit (La. Code Civ. Proc. art. 4911).** Corroborated by multiple independent secondary sources and consistent with the parallel small-claims-division figure, but this session could not load the article's primary text directly (both Justia and FindLaw pages for this specific article failed to load). Verify before citing in a filing.
2. **Whether LUTPA reaches a hospital as a corporate billing entity.** The Attorney General's consumer-dispute intake explicitly excludes "licensed professionals (doctors, dentist, attorneys, etc.)" and insurance claims. It is unclear whether a hospital's billing office, as opposed to an individual physician, falls inside or outside that carve-out. Confirm with the AG's office for the specific dispute before relying on LUTPA against a hospital.
3. **The Louisiana Medical Debt Protection Act's garnishment and lien provisions (La. R.S. 51:1501-1507, 2026 Act 897).** The 3% interest cap is confirmed from two independent sources. Reported details on a wage/bank-account garnishment threshold (tied to a percentage of the federal poverty level) and a prohibition on liens or foreclosure against a primary residence or vehicle appeared consistently across secondary sources but could not be confirmed against the enrolled bill's primary text in this session (the PDF did not render as extractable text). Do not cite a specific garnishment percentage until this is confirmed.
4. **The 2022 amendment to LUTPA's insurance exemption (R.S. 51:1406).** Some secondary sources describe a 2022 amendment narrowing the insurance-commissioner exemption. This pack does not rely on that claim anywhere above, but a future update should resolve it before asserting LUTPA reaches insurer conduct.
5. **Whether R.S. 22:1874's fee-shifting provision extends to disputes beyond a provider's lawsuit against the patient** (for example, a patient-initiated suit against the provider). The statute's fee-shifting language is framed around the provider bringing an action; this pack does not assume it helps a patient who sues first.
