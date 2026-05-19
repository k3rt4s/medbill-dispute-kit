# Pennsylvania state pack

The fully-worked state-law layer for Pennsylvania patients. The LLM uses this when the patient's state is Pennsylvania. Tennessee equivalent at [`laws_state_tn.md`](laws_state_tn.md); Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md); New York equivalent at [`laws_state_ny.md`](laws_state_ny.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Three things make Pennsylvania's patient-side leverage unusually strong:

1. **42 Pa.C.S. § 8371** is the gold-standard first-party insurance bad-faith statute in the United States. Enacted 1990, it gives policyholders a private right of action and authorizes **interest at prime + 3%, punitive damages, court costs, AND attorney's fees** on a clear-and-convincing showing of bad-faith claims handling. No other state combines all four remedies in one short, plaintiff-favorable section. Treat this as the headline lever in any PA insurer dispute.
2. **42 Pa.C.S. § 8127** is one of the strongest wage-garnishment exemptions in the country: **wages are categorically exempt from garnishment for consumer debts (including medical debt)** with only narrow exceptions (taxes, child/spousal support, board for four weeks, residential-lease rent, restitution, certain student loans). A PA hospital that wins a judgment for medical debt still cannot garnish the patient's paycheck.
3. **PA UTPCPL (73 P.S. § 201-1 et seq.) + FCEUA (73 P.S. § 2270.1 et seq.)** reach **original creditors** as well as third-party debt collectors. A hospital's own in-house billing department can be sued under the UTPCPL with **treble damages, $100 statutory minimum, and attorney's fees** — a remedy the federal FDCPA does not provide because it does not reach original creditors.

Treat these three as the structural headlines in any PA dispute strategy. Note up front: **Pennsylvania does NOT have a state surprise-billing statute, a state ground-ambulance balance-billing law, or a state medical-debt credit-reporting restriction.** Patients in those situations rely on the federal No Surprises Act (which excludes ground ambulance) and federal FCRA dispute rights. Multiple PA bills addressing these gaps were pending in the 2025-2026 session as of this writing but had not been enacted.

## Hospital itemization right

- **Regulation:** **28 Pa. Code § 103.22** (Implementation of Hospital Patient's Bill of Rights), provisions 12 and 13
- **Enabling statute:** **Health Care Facilities Act, 35 P.S. § 448.803**, in conjunction with § 2102(g) of the Administrative Code of 1929 (71 P.S. § 532(g))
- **Sources:** [pacodeandbulletin.gov/Display/pacode/file=/secure/pacode/data/028/chapter103/s103.22.html](https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/028/chapter103/s103.22.html); [law.cornell.edu/regulations/pennsylvania/28-Pa-Code-SS-103-22](https://www.law.cornell.edu/regulations/pennsylvania/28-Pa-Code-SS-103-22)
- **What it requires:**
  - The patient has the right to **examine and receive a detailed explanation of his bill** (Patient's Bill of Rights, provision 12).
  - The patient has the right to **full information and counseling on the availability of known financial resources for his health care** (provision 13).
  - The hospital governing body must establish and implement a Patient's Bill of Rights "not less in substance and coverage than" 28 Pa. Code § 103.22.
- **Critical caveat:** Pennsylvania has **no dedicated statutory itemization deadline** comparable to New York's 7-day rule (N.Y. Pub. Health Law § 2831) or Georgia's automatic 6-business-day rule (O.C.G.A. § 10-1-393(b)(14)). The PA right exists at the **regulatory** level — binding on PA-licensed hospitals via licensure conditions, but enforced administratively by the Department of Health rather than through a private cause of action under § 103.22 itself. Patients combine § 103.22 with the **federal Hospital Price Transparency Rule (45 CFR Part 180)** and the **federal Good Faith Estimate** requirement (45 CFR § 149.610) for uninsured/self-pay patients to construct a complete itemization-leverage stack.
- **Scope:** Hospitals licensed under the Pennsylvania Health Care Facilities Act. Outpatient-only physician practices are not bound by § 103.22 but are bound by federal price-transparency and GFE rules.
- **Practical use:** Cite § 103.22 (provision 12) in the itemization request; pair with the federal Price Transparency Rule for non-hospital providers. If the hospital refuses, escalate to **PA Department of Health, Division of Acute and Ambulatory Care** ([health.pa.gov](https://www.health.pa.gov/topics/facilities/Pages/Acute-and-Ambulatory-Care.aspx)), and CC the PA Attorney General Health Care Section (see below).

## Unfair Insurance Practices Act (UIPA)

- **Statute:** **40 P.S. § 1171.1 et seq.** — Pennsylvania Unfair Insurance Practices Act (UIPA), enacted July 22, 1974 (P.L. 589, No. 205)
- **Implementing regulation:** **31 Pa. Code Chapter 146** (Unfair Insurance Practices — Unfair Claims Settlement Practices)
- **Sources:** [legis.state.pa.us/WU01/LI/LI/US/PDF/1974/0/0205..PDF](https://www.legis.state.pa.us/WU01/LI/LI/US/PDF/1974/0/0205..PDF); [codes.findlaw.com/pa/title-40-ps-insurance/pa-st-sect-40-1171-5](https://codes.findlaw.com/pa/title-40-ps-insurance/pa-st-sect-40-1171-5/); [pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/031/chapter146/chap146toc.html](https://www.pacodeandbulletin.gov/Display/pacode?file=%2Fsecure%2Fpacode%2Fdata%2F031%2Fchapter146%2Fchap146toc.html)
- **Substance:** Prohibits insurers from misrepresenting policy provisions, failing to acknowledge claims promptly, denying without reasonable investigation, compelling litigation by offering substantially less than amounts ultimately recovered, and engaging in the other unfair claims-settlement practices enumerated at 40 P.S. § 1171.5.
- **Critical caveat — no private right of action:** The Pennsylvania Supreme Court held in ***D'Ambrosio v. Pennsylvania National Mutual Casualty Insurance Co.***, 494 Pa. 501, 431 A.2d 966 (1981), that **UIPA does not create a private cause of action**. The Court declined to "supplement" UIPA's regulatory enforcement scheme with a judicially created tort, but openly invited the Legislature to enact one. **The Legislature accepted that invitation in 1990 by enacting 42 Pa.C.S. § 8371** (see next section), which is now the operative private remedy for insurance bad faith in Pennsylvania.
- **Sources:** [law.justia.com/cases/pennsylvania/supreme-court/1981/494-pa-501-0.html](https://law.justia.com/cases/pennsylvania/supreme-court/1981/494-pa-501-0.html); [corporate.findlaw.com/corporate-governance/insurance-company-liability-for-bad-faith-in-pennsylvania.html](https://corporate.findlaw.com/corporate-governance/insurance-company-liability-for-bad-faith-in-pennsylvania.html)
- **Use:** Cite UIPA violations in your complaint to the PA Insurance Department (see "Regulatory agencies" below) and as evidentiary support for a § 8371 bad-faith claim. **Do not plead UIPA as a standalone count in litigation** — *D'Ambrosio* has been followed continuously since 1981 and remains controlling.

## Bad-faith failure to pay — 42 Pa.C.S. § 8371

- **Statute:** **42 Pa.C.S. § 8371** (Actions on insurance policies). Enacted 1990 (Act 6 of 1990); effective July 1, 1990.
- **Sources:** [legis.state.pa.us/WU01/LI/LI/CT/HTM/42/00.083.071.000..HTM](https://www.legis.state.pa.us/WU01/LI/LI/CT/HTM/42/00.083.071.000..HTM); [siddonslaw.com/bad-faith-insurance-lawyer/pennsylvania](https://siddonslaw.com/bad-faith-insurance-lawyer/pennsylvania/); [chartwelllaw.com/bad-faith-claims-map/pennsylvania](https://www.chartwelllaw.com/bad-faith-claims-map/pennsylvania); [marshalldennehey.com/articles/pennsylvania-supreme-court-clarifies-standard-courts-must-use-when-considering-claims-made](https://marshalldennehey.com/articles/pennsylvania-supreme-court-clarifies-standard-courts-must-use-when-considering-claims-made)
- **Full statutory text:**
  > In an action arising under an insurance policy, if the court finds that the insurer has acted in bad faith toward the insured, the court may take all of the following actions:
  > (1) Award interest on the amount of the claim from the date the claim was made by the insured in an amount equal to the prime rate of interest plus 3%.
  > (2) Award punitive damages against the insurer.
  > (3) Assess court costs and attorney fees against the insurer.
- **Why this is the strongest first-party bad-faith statute in the country:** § 8371 is the only state bad-faith statute that bundles **prime-plus-3% interest, punitive damages, AND attorney's fees** in a single section with a generally applicable private right of action. Georgia (O.C.G.A. § 33-4-6) provides a 50%-of-loss or $5,000 penalty plus fees but no punitives. Tennessee (§ 56-7-105) caps at 25% of the recovery plus fees, no punitives. California has common-law bad faith with punitives but no statutory interest premium. Texas (Ch. 541) gives treble damages but on a tighter standard. Pennsylvania bundles the strongest remedies into the simplest text.
- **Standard:** The Pennsylvania Supreme Court in ***Rancosky v. Washington National Insurance Co.***, 642 Pa. 153, 170 A.3d 364 (2017), confirmed the two-prong *Terletsky* standard:
  - (1) The insurer **did not have a reasonable basis** for denying benefits under the policy, AND
  - (2) The insurer **knew or recklessly disregarded** its lack of a reasonable basis in denying the claim.
  - The standard is **clear and convincing evidence** — a higher proof burden than preponderance, but does not require a showing of subjective malicious intent.
- **What counts as bad faith in claims handling:** delays without reasonable basis, denials inconsistent with the policy language, misrepresenting coverage, failing to investigate, failing to communicate, lowball settlement offers, and post-litigation conduct (the PA Superior Court has recognized post-litigation bad faith).
- **Coverage:** Any insurance policy, including **health insurance**, accident-and-sickness, disability, life, auto, and homeowners. First-party only (third parties cannot directly sue the tortfeasor's insurer under § 8371).
- **ERISA preemption:** § 8371 is **preempted** as applied to self-funded ERISA employer plans. ***Barber v. Unum Life Insurance Co.***, 383 F.3d 134 (3d Cir. 2004) and progeny. For self-funded plans, the federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) attorney's fees — no state bad-faith penalty. § 8371 is fully in play for fully-insured plans, Medicaid managed care, individual/marketplace plans, and PA-issued group insured plans.
- **No demand-and-wait requirement:** Unlike Georgia's § 33-4-6 (60-day demand) or Tennessee's § 56-7-105 (60-day demand), § 8371 has **no statutory pre-suit notice requirement**. A bad-faith claim may be filed at any point during or after the underlying coverage dispute.
- **Statute of limitations:** **2 years** for § 8371 claims under 42 Pa.C.S. § 5524, as established in ***Ash v. Continental Insurance Co.***, 593 Pa. 523, 932 A.2d 877 (2007). The clock runs from the date the insurer's bad-faith conduct caused harm to the insured.
- **Use:** Cite § 8371 prominently in any insurer-side dispute in PA. Pair with a parallel UIPA complaint to the PA Insurance Department (the regulatory filing is free, generates a paper trail, and frequently moves the carrier in ways litigation cannot). For health-insurance denials, also pursue the **state external review process** administered by the PA Insurance Department under Act 146 of 2022 (see "External review" below).

## Surprise billing — Pennsylvania has NO state-law protection

- **Statute:** **None.** Pennsylvania has not enacted a state surprise-billing law. HB 1862 (2019-2020 session) and SB 822 (2019-2020) would have provided protection but were not enacted; the federal No Surprises Act (effective Jan 1, 2022) overtook the legislative push.
- **What governs in PA:** the **federal No Surprises Act** (Pub. L. 116-260, Div. BB, Title I); see [`laws_federal.md`](laws_federal.md) for full treatment. The PA Insurance Department enforces the federal NSA in PA for fully-insured plans.
- **Sources:** [pa.gov/agencies/insurance/laws-regulations-notices/no-surprises-act](https://www.pa.gov/agencies/insurance/laws-regulations-notices/no-surprises-act); [pa.gov/services/insurance/request-a-review-of-an-unexpected-medical-bill-no-surprises-act](https://www.pa.gov/services/insurance/request-a-review-of-an-unexpected-medical-bill-no-surprises-act); [pahealthaccess.org/pa-smb-hb1862](https://pahealthaccess.org/pa-smb-hb1862/); [legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?bn=1862&body=H&sind=0&syear=2019&type=B](https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?sYear=2019&sInd=0&body=H&type=B&bn=1862)
- **Heads up — Act 146 of 2022 is NOT a surprise-billing law:** Pennsylvania Act 146 of 2022 (enacted from SB 225) amended the Insurance Company Law of 1921 to govern **prior authorization of medical services** and the **state external review process** for adverse benefit determinations. State-specific provisions took effect for Plan Year 2024. Some online summaries incorrectly conflate Act 146/2022 with surprise billing — verify. The pending 2025-2026 session bill SB 822 (re-introduced) would create a PA surprise-billing framework, but it had not been enacted as of this writing.
- **Practical implication for PA patients:** for surprise-bill situations, the **federal NSA is the primary lever**. Cite federal NSA provisions in dispute letters; file federal-NSA complaints via the PA Insurance Department portal at [pa.gov/services/insurance/request-a-review-of-an-unexpected-medical-bill-no-surprises-act](https://www.pa.gov/services/insurance/request-a-review-of-an-unexpected-medical-bill-no-surprises-act) or the federal CMS portal at [nsa-idr.cms.gov](https://nsa-idr.cms.gov/).

## State external review of denied claims — Act 146 of 2022

- **Statute:** **Act 146 of 2022** (SB 225), amending Article XXI ("Quality Health Care Accountability and Protection") of the Insurance Company Law of 1921. Codified at **40 P.S. §§ 991.2101 - 991.2193**, with new provisions on prior authorization and external review.
- **Sources:** [palegis.us/statutes/unconsolidated/law-information?sessYr=2022&sessInd=0&actNum=146](https://www.palegis.us/statutes/unconsolidated/law-information?sessYr=2022&sessInd=0&actNum=146); [pacodeandbulletin.gov/Display/pabull?file=/secure/pabulletin/data/vol53/53-49/1709.html](https://www.pacodeandbulletin.gov/Display/pabull?file=/secure/pabulletin/data/vol53/53-49/1709.html); [pa.gov/agencies/oa/newsroom/pennsylvania-insurance-department-and-code-pa-launch-state-external-review-process-and-new-website-for-pennsylvanians-to-appeal-denied-health-plan-services.html](https://www.pa.gov/agencies/oa/newsroom/pennsylvania-insurance-department-and-code-pa-launch-state-external-review-process-and-new-website-for-pennsylvanians-to-appeal-denied-health-plan-services.html)
- **Substance:**
  - Patients with fully-insured PA health plans who receive a **final adverse benefit determination** (medical necessity, experimental/investigational, OON access denial) may request **independent external review** by a state-certified Independent Review Organization (IRO) at no cost to the patient.
  - **Filing window: 4 months** from the patient's receipt of the final adverse determination notice.
  - **Standard decision: 45 days**; **expedited: 72 hours** where delay would significantly increase risk to health.
  - The IRO's decision is **binding on the plan**.
- **Use:** Always exhaust the plan's internal appeal first, then file the state external review. This is the cleanest, cheapest leverage for medical-necessity denials. For self-funded ERISA plans, use the federal external-review process under 29 CFR § 2590.715-2719 instead — Act 146 does not reach self-funded plans.

## Regulatory agencies

### Pennsylvania Insurance Department (PID)

- **Online complaint portal:** **Consumer Services Online (CSO) Portal** at [pa.gov/agencies/insurance/consumer-help-center/complaints-questions-help](https://www.pa.gov/agencies/insurance/consumer-help-center/complaints-questions-help)
- **Phone:** **1-877-881-6388** (toll-free Consumer Services)
- **Email:** ra-in-consumer@pa.gov
- **Mailing address:**
  > Pennsylvania Insurance Department
  > Bureau of Consumer Services
  > Room 1209, Strawberry Square
  > Harrisburg, PA 17120
- **Fax:** (717) 787-8585
- **Authority:** All insurance companies licensed in PA, including fully-insured health insurers, HMOs, PPOs, Medicare supplement, surprise-billing protections under federal NSA, prior authorization and external review under Act 146 of 2022, UIPA enforcement (40 P.S. § 1171.1 et seq.) and Chapter 146 of the PA Code. **No authority over self-funded ERISA plans** (route to U.S. DOL EBSA at 1-866-444-3272) and does not regulate hospitals, providers, or debt collectors (route to PA AG Health Care Section or PA Department of Health).
- **Source:** [pa.gov/agencies/insurance/contact-us](https://www.pa.gov/agencies/insurance/contact-us)

### Pennsylvania Office of Attorney General — Health Care Section

- **Phone:** **1-717-705-6938** (Harrisburg); in-state toll-free **1-877-888-4877**
- **Online complaint form:** [attorneygeneral.gov/submit-a-complaint/health-care-complaint](https://www.attorneygeneral.gov/submit-a-complaint/health-care-complaint/)
- **Mailing address:**
  > Pennsylvania Office of Attorney General
  > Health Care Section
  > 14th Floor, Strawberry Square
  > Harrisburg, PA 17120
- **Authority:** A dedicated Health Care Section (PA is one of a small group of states with a dedicated AG bureau for health-care matters, alongside NY and a handful of others) handles consumer disputes with health insurers, HMOs, hospitals, providers, and pharmacy benefit managers. Investigates billing disputes, access-to-care denials, parity violations, coverage disputes, and consumer-protection violations under the PA UTPCPL (73 P.S. § 201-1 et seq.) and FCEUA (73 P.S. § 2270.1 et seq.). The Section has historically recovered millions of dollars in refunds and savings for PA consumers and routinely contacts providers/insurers on individual complaints rather than functioning purely as a filing cabinet.
- **Source:** [attorneygeneral.gov/protect-yourself/healthcare-matters/how-can-the-health-care-section-help-me](https://www.attorneygeneral.gov/protect-yourself/healthcare-matters/how-can-the-health-care-section-help-me/)
- **Use:** Pair the Health Care Section complaint with a PID filing for insurer disputes (Section pressures the provider/insurer relationship; PID regulates the carrier). For hospital and provider billing disputes, the Health Care Section is the primary lever.

### Pennsylvania Office of Attorney General — Bureau of Consumer Protection (BCP)

- **Phone:** **1-800-441-2555** (toll-free)
- **Email:** consumers@attorneygeneral.gov
- **Online complaint:** [attorneygeneral.gov/submit-a-complaint/consumer-complaint](https://www.attorneygeneral.gov/submit-a-complaint/consumer-complaint/)
- **Authority:** Enforces the PA Unfair Trade Practices and Consumer Protection Law (UTPCPL, 73 P.S. § 201-1 et seq.), the Fair Credit Extension Uniformity Act (FCEUA, 73 P.S. § 2270.1 et seq.), and other consumer-protection statutes. Reach over providers, hospitals, third-party debt collectors, **and original creditors** — covering the gap left by the federal FDCPA. Useful when the dispute is with a hospital's in-house billing department or a non-insurance provider.
- **Use this Bureau, not the Health Care Section, for:** non-medical-billing consumer complaints, debt-collector misconduct unrelated to health care, deceptive-trade-practice claims under the UTPCPL. **Use the Health Care Section for anything that touches a health-care provider, insurer, or pharmacy benefit manager.**

### Pennsylvania Department of Health (DOH)

- **Hospital licensing and quality complaints:** **1-800-254-5164** ([health.pa.gov](https://www.health.pa.gov/topics/facilities/Pages/Acute-and-Ambulatory-Care.aspx))
- **Authority:** Licensing and patient-care quality at PA-licensed hospitals under the Health Care Facilities Act (35 P.S. § 448.101 et seq.). Administers 28 Pa. Code § 103.22 (Hospital Patient's Bill of Rights), including the itemization right. Does **not** handle billing disputes per se (route those to AG Health Care Section or PID). Useful when the dispute also implicates patient-care quality, sanitation, facility licensure, or systemic non-compliance with the Patient's Bill of Rights.

## Small claims court — Magisterial District Court

- **Court name:** **Magisterial District Court** (one per district; each county has multiple districts). Pennsylvania uniquely consolidates small-claims, landlord-tenant, traffic, and minor criminal matters into a single trial-court tier presided over by an elected Magisterial District Judge (MDJ).
- **Jurisdictional limit:** **$12,000**, codified at **42 Pa.C.S. § 1515(a)** (Jurisdiction and venue). The cap applies to the principal claim — actual damages sought — not including interest, court costs, or attorney's fees.
- **Sources:** [palegis.us/statutes/consolidated/view-statute?ttl=42&div=0&chpt=15&sctn=15](https://www.legis.state.pa.us/cfdocs/legis/LI/consCheck.cfm?txtType=HTM&ttl=42&div=0&chpt=15&sctn=15&subsctn=0); [legalatoms.com/pennsylvania/pennsylvania-small-claims-court-jurisdiction-magisterial-district](https://legalatoms.com/pennsylvania/pennsylvania-small-claims-court-jurisdiction-magisterial-district/); [pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/246/chapter300/chap300toc.html](https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/246/chapter300/chap300toc.html)
- **Filing fees:** Typically **$50 to $150** depending on claim amount and number of defendants; additional service fees charged separately for constable delivery. Vary slightly by district. In forma pauperis fee waivers available on poor-person application.
- **Attorney rules:** Attorneys permitted but uncommon. Designed for pro se litigants. **Corporations and LLCs may appear through a non-attorney officer or employee under Pa.R.C.P.M.D.J. 207** — a Pennsylvania-specific advantage for self-represented patients facing hospital defendants, because the hospital typically sends a billing-department staffer rather than retaining counsel.
- **Jury trial:** Not available at the Magisterial District Court level. Either party dissatisfied with the MDJ's judgment may **appeal de novo to the Court of Common Pleas within 30 days** (civil cases) for a fresh trial with full civil rules and jury available on request. Appeal triggers full Pennsylvania Rules of Civil Procedure and significantly higher litigation cost — a deterrent to hospital defendants.
- **Procedure:** File a civil complaint at the MDJ office covering the defendant's location. Constable serves the complaint. Hearing typically scheduled within 60 days. Decisions often delivered same-day or within a week.

## Statute of limitations

- **Breach of contract (written, oral, promissory note, open-end account):** **4 years** from breach — **42 Pa.C.S. § 5525(a)**
- **Default "catch-all" residual:** **6 years** — **42 Pa.C.S. § 5527** (applies to actions not subject to another specific limitations period)
- **Bad-faith claim under § 8371:** **2 years** — 42 Pa.C.S. § 5524, per *Ash v. Continental Ins. Co.*, 593 Pa. 523, 932 A.2d 877 (2007)
- **UTPCPL claim:** **6 years** — 42 Pa.C.S. § 5527 (no specific UTPCPL SOL; courts apply the residual)
- **FCEUA claim:** **2 years** — 73 P.S. § 2270.5(a); see also Prince Law Offices summary at [blog.princelaw.com/2017/09/13/pennsylvania-consumers-protections-under-the-fair-credit-extension-uniformity-act](https://blog.princelaw.com/2017/09/13/pennsylvania-consumers-protections-under-the-fair-credit-extension-uniformity-act/)
- **Sources:** [legis.state.pa.us/WU01/LI/LI/CT/HTM/42/00.055.025.000..HTM](https://www.legis.state.pa.us/WU01/LI/LI/CT/HTM/42/00.055.025.000..HTM); [tryascend.com/statute-of-limitations/medical/pennsylvania](https://tryascend.com/statute-of-limitations/medical/pennsylvania); [www.abi.org/feed-item/the-pennsylvania-statute-of-limitations-on-debt-collection](https://www.abi.org/feed-item/the-pennsylvania-statute-of-limitations-on-debt-collection)

**Which statute applies to a medical bill?**

Most hospital admissions involve a signed financial-responsibility form — a written contract, so **4 years under § 5525(a)** applies. Implied-in-fact medical-billing arrangements without a signed agreement are treated the same way; § 5525(a) lists "express contract not in writing" alongside written contracts, both at 4 years. Unlike New York, Pennsylvania does NOT have a separate consumer-credit short-clock provision.

**Clock starts at breach** — typically the day payment was due and not made, not when damages were discovered.

**Partial payment or written acknowledgment can restart or revive the clock** under PA common law (general acknowledgment doctrine). **Do not make a partial payment on a time-barred medical debt without legal advice.** This is the opposite of New York's post-CCFA rule, where partial payment does not revive the clock.

**For dispute letters: cite 42 Pa.C.S. § 5525(a) (four years)** as the applicable limitation period for any medical-debt collection action against a Pennsylvania patient.

## Ground-ambulance protection — Pennsylvania has NO state-law protection

- **Statute:** **None.** Pennsylvania has not enacted a state ground-ambulance balance-billing protection. As of April 2025, Pennsylvania is **not** among the 19 states with ground-ambulance balance-billing protections (which include CA, CO, DE, FL, IL, IN, ME, MD, MN, NH, NJ, NY, OH, OK, TX, UT, VT, VA, WA, and others added in 2024-2025).
- **Pending:** **HB 1152** (2025-2026 session) would require insurers to reimburse EMS providers directly within 45 days at 350% of the current published Medicare rate, but its primary focus is EMS-provider reimbursement, not patient hold-harmless. Status: referred to Veterans and Emergency Services Committee, not enacted as of this writing.
- **Sources:** [commonwealthfund.org/blog/2026/consumers-still-face-surprise-bills-ground-ambulances-states-are-trying-protect-them](https://www.commonwealthfund.org/blog/2026/consumers-still-face-surprise-bills-ground-ambulances-states-are-trying-protect-them); [ehdinsurance.com/pennsylvania-ems-crisis-how-house-bill-1152-could-impact-your-emergency-services](https://ehdinsurance.com/pennsylvania-ems-crisis-how-house-bill-1152-could-impact-your-emergency-services/); [ambulance.org/sp_product/state-balance-billing-overview-v1](https://ambulance.org/sp_product/state-balance-billing-overview-v1/)
- **What governs:** The **federal No Surprises Act explicitly excludes ground ambulance**. PA patients receiving balance bills from OON ground-ambulance providers have **no state-law hold-harmless protection**. The only patient-side levers are: (a) the UTPCPL if the ambulance billing is deceptive or contains errors; (b) the FCEUA if the collector's conduct is abusive; (c) the federal Hospital Price Transparency Rule does not reach standalone ambulance services; and (d) negotiation/charity-care leverage.
- **Practical use:** When a PA patient gets a ground-ambulance balance bill, the strategy is **negotiate to the in-network rate or Medicare-allowable equivalent**, with UTPCPL leverage if any billing error or deceptive practice is present. This is a meaningful gap in PA protection compared to NY, CA, GA, MD, IL, and CO patients.

## Medical-debt credit reporting — Pennsylvania has NO state-law restriction

- **Statute:** **None.** Pennsylvania has not enacted a state medical-debt credit-reporting law comparable to NY (Fair Medical Debt Reporting Act, N.Y. Gen. Bus. Law § 380-j(f)), NJ, DE, CO, IL, MN, or other states.
- **Pending:** Multiple 2025-2026 session bills (Senate Co-Sponsorship Memo 45026 and others) would create PA protections, but none had been enacted as of this writing.
- **What governs:** federal **Fair Credit Reporting Act** (15 U.S.C. §§ 1681 et seq.) dispute rights, plus the voluntary 2022-2023 changes by Equifax/Experian/TransUnion (paid medical debt removed; debt under $500 not reported; 1-year delay before reporting). The CFPB's January 2025 medical-debt rule, which would have removed most medical debt from credit reports, was **vacated by a federal court in the Eastern District of Texas on July 11, 2025** (*Cornerstone Credit Union League v. CFPB*) — the rule is not in effect.
- **Sources:** [inquirer.com/health/medical-debt-bills-credit-agencies-20250830.html](https://www.inquirer.com/health/medical-debt-bills-credit-agencies-20250830.html); [patientfairness.com/medical-debt-and-credit-reporting-cfpb-and-state-regulations](https://www.patientfairness.com/medical-debt-and-credit-reporting-cfpb-and-state-regulations); [palegis.us/senate/co-sponsorship/memo?memoID=45026](https://www.palegis.us/senate/co-sponsorship/memo?memoID=45026); [library.nclc.org/article/latest-keeping-medical-debt-out-credit-reports](https://library.nclc.org/article/latest-keeping-medical-debt-out-credit-reports)
- **Practical use:** For PA patients with medical debt on credit reports, the available levers are:
  - **Federal FCRA disputes** under 15 U.S.C. §§ 1681i (CRA dispute) and 1681s-2 (furnisher dispute) for inaccurate, incomplete, or unverifiable entries.
  - **Voluntary bureau policies** (paid medical debt removed; under $500 not reported; 1-year reporting delay).
  - **UTPCPL/FCEUA claims** if the furnishing is deceptive (e.g., furnishing a disputed debt without noting the dispute, reporting a debt the patient never owed).
  - **Federal NSA payment-protection** for surprise bills that should not have been routed to collections in the first place.

## Charity care obligations — Act 55 of 1997 (Institutions of Purely Public Charity Act)

- **Statute:** **Institutions of Purely Public Charity Act, Act 55 of 1997 (P.L. 508, No. 55), codified at 10 P.S. §§ 371-385**, signed November 26, 1997.
- **Sources:** [legis.state.pa.us/WU01/LI/LI/US/HTM/1997/0/0055..HTM](https://www.legis.state.pa.us/WU01/LI/LI/US/HTM/1997/0/0055..HTM); [pa.gov/content/dam/copapwp-pagov/en/dos/programs/charities/Institutions-of-Purely-Public-Charity-Act.pdf](https://www.pa.gov/content/dam/copapwp-pagov/en/dos/programs/charities/Institutions-of-Purely-Public-Charity-Act.pdf); [dollarfor.org/state_sheet/pennsylvania](https://dollarfor.org/state_sheet/pennsylvania/); [dickinsonlaw.psu.edu/sites/default/files/2022-07/Putting-the-Charity-Back-PA-BAR-Quarterly.pdf](https://dickinsonlaw.psu.edu/sites/default/files/2022-07/Putting-the-Charity-Back-PA-BAR-Quarterly.pdf)
- **Substance:** Act 55 codifies the five-prong **HUP test** (from *Hospital Utilization Project v. Commonwealth*, 507 Pa. 1, 487 A.2d 1306 (1985)) that a hospital or other institution must satisfy to qualify as a "purely public charity" entitled to state and local tax exemption. The five prongs at 10 P.S. § 375(b)-(f): (1) advance a charitable purpose, (2) donate or render gratuitously a substantial portion of services, (3) benefit a substantial and indefinite class, (4) relieve government of some of its burden, and (5) operate entirely free from private profit motive.
- **Charity-care prong (§ 375(c)):** The institution must "**donate or render gratuitously a substantial portion of its services**" by providing services free or at reduced rates to "those who cannot afford to pay for what they receive." The hospital satisfies this by meeting **one of seven alternative standards** in § 375(c)(1)-(7), including:
  - Goods/services donated equal at least 5% of total program costs; OR
  - At least 5% of patient bill is uncompensated (charity care); OR
  - The institution provides at least 5% of its services to government-program beneficiaries (Medicaid, etc.) at rates below cost; OR
  - One of four other quantitative standards.
- **Tax-exemption hook:** PA's Supreme Court in *In re Pottstown Hospital* (2024) reinforced that compliance with both HUP and Act 55 is required for purely-public-charity tax exemption. **A PA nonprofit hospital that loses charity-care status loses property-tax exemption** — a material lever in negotiations, because hospital systems vigorously protect their exempt status.
- **What Act 55 does NOT do:** Act 55 does **not** establish specific income-eligibility thresholds, application timelines, sliding-scale formulas, or pre-suit collection moratoriums. PA charity-care policies are largely set by the federal **IRS § 501(r)** framework (for nonprofit hospitals) and by individual hospital policies, with Act 55 functioning as the state tax-exemption gatekeeper rather than a uniform patient-rights statute. **A 2025-2026 PA House bill** (passed May 2025 in the House, pending in Senate) would require **standardized hospital financial-aid application forms statewide** — a meaningful gap-closer if enacted.
- **Practical use:**
  - Cite **IRS § 501(r)** + the hospital's posted FAP for nonprofit hospitals (federal floor).
  - Cite **Act 55 / 10 P.S. § 375(c)** for the tax-exempt nonprofit charity-care obligation; reference the seven-standard test as evidence of the hospital's underlying obligation to serve indigent patients gratuitously.
  - Use the **Pennsylvania Health Care Cost Containment Council (PHC4)** uncompensated-care reports as comparable-data leverage to challenge denials of charity-care eligibility. PHC4 statutory authority: Act 89 of 1986, as amended by Act 15 of 2020; see [phc4.org](https://www.phc4.org/) and [legis.state.pa.us/WU01/LI/LI/US/PDF/2009/0/0003..PDF](https://www.legis.state.pa.us/WU01/LI/LI/US/PDF/2009/0/0003..PDF). PHC4 (formerly codified at 40 P.S. § 1551 et seq., now operating under reauthorized Executive Order) collects hospital financial and quality data and publishes it; the data is useful both in dispute letters and in media/AG-complaint escalation.
  - **For uninsured PA patients**, screen via **Dollar For** at [dollarfor.org/state_sheet/pennsylvania](https://dollarfor.org/state_sheet/pennsylvania/) for the patient's specific hospital's FAP.

## Hospital lien statute — Pennsylvania has NO statewide hospital lien act

- **Statute:** **None.** Pennsylvania is one of approximately nine states without a comprehensive statewide hospital lien act. **40 P.S. § 991.2401 is NOT a hospital lien statute** — it is the opening section of Article XXI ("Quality Health Care Accountability and Protection") of the Insurance Company Law of 1921, governing managed-care plan obligations. Cite Article XXI sections for managed-care disputes, not for hospital liens.
- **Sources:** [mwl-law.com/wp-content/uploads/2019/09/HOSPITAL-LIEN-LAWS-IN-ALL-50-STATES-CHART-00215685x9EBBF.pdf](https://www.mwl-law.com/wp-content/uploads/2019/09/HOSPITAL-LIEN-LAWS-IN-ALL-50-STATES-CHART-00215685x9EBBF.pdf); [gibperk.com/understanding-medical-liens-in-pennsylvania-personal-injury-cases](https://www.gibperk.com/understanding-medical-liens-in-pennsylvania-personal-injury-cases/); [mayersoninjurylaw.com/blog/2025/september/how-to-prove-a-medical-lien-in-a-personal-injury](https://www.mayersoninjurylaw.com/blog/2025/september/how-to-prove-a-medical-lien-in-a-personal-injury/); [aldlawfirm.com/blog/what-is-a-medical-lien-and-can-it-be-reduced](https://aldlawfirm.com/blog/what-is-a-medical-lien-and-can-it-be-reduced/)
- **What governs in PA:** PA hospitals collecting from personal-injury settlements rely on **contract-based liens** (the financial-responsibility form the patient signs at admission, or an assignment-of-benefits/subrogation clause) and on common-law equitable principles. The PA Superior Court has held that "where there is no express agreement to pay, the law implies a promise to pay a reasonable fee for a health provider's services" — a quantum-meruit basis for recovery, not a statutory lien.
- **Medicaid liens — separate framework:** PA **Medicaid (Medical Assistance)** does have statutory subrogation/lien rights under **Act 44 of 2008**, codified at **62 P.S. § 1409** (Third-Party Liability for Medicaid recipients). This is a Medicaid-specific lien against third-party tort recoveries, not a general hospital lien.
- **Practical use:** PA patients in personal-injury contexts should:
  - Demand that the hospital identify the **specific contractual or assignment provision** authorizing the lien; absent a signed agreement, the hospital is reduced to a quantum-meruit reasonable-value claim, often negotiable downward.
  - Confirm the hospital first attempted billing to the patient's health insurer before asserting any lien; PA common law and managed-care contract terms typically require insurer-first billing.
  - Note that **42 Pa.C.S. § 8127's wage-garnishment exemption applies even with a judgment in hand** — a hospital that wins a contract-based lien judgment cannot reach the patient's wages anyway.

## Wage garnishment — 42 Pa.C.S. § 8127 (one of the strongest patient protections in the country)

- **Statute:** **42 Pa.C.S. § 8127** (Personal earnings exempt from process)
- **Sources:** [palegis.us/statutes/consolidated/view-statute?ttl=42&div=00.&chapter=081.&section=027.&subsctn=000.](https://www.palegis.us/statutes/consolidated/view-statute?txtType=HTM&ttl=42&div=00.&chapter=081.&section=027.&subsctn=000.); [law.justia.com/codes/pennsylvania/title-42/chapter-81/section-8127](https://law.justia.com/codes/pennsylvania/title-42/chapter-81/section-8127/); [codes.findlaw.com/pa/title-42-pacsa-judiciary-and-judicial-procedure/pa-csa-sect-42-8127](https://codes.findlaw.com/pa/title-42-pacsa-judiciary-and-judicial-procedure/pa-csa-sect-42-8127/); [nolo.com/legal-encyclopedia/pennsylvania-wage-garnishment-law.html](https://www.nolo.com/legal-encyclopedia/pennsylvania-wage-garnishment-law.html)
- **Substance:** "The wages, salaries and commissions of individuals shall while in the hands of the employer be exempt from any attachment, execution or other process" — subject only to the enumerated exceptions.
- **Exceptions (the only situations in which PA wages CAN be garnished):**
  - Support actions (child or spousal)
  - PHEAA (PA Higher Education Assistance Agency) student loans
  - Board for four weeks or less
  - Restitution in criminal cases
  - Residential-lease rent (Pa.R.C.P.M.D.J. Subchapter F under § 8127(a)(3.1))
  - Federal taxes and PA state/local taxes
  - Federal student loans (administrative garnishment under federal law, not § 8127)
- **Medical debt is NOT in the exception list.** A hospital, physician, ambulance company, or any other medical creditor that wins a money judgment against a PA patient **cannot garnish that patient's wages**. This holds true even if the judgment is for $50,000 in medical bills.
- **What this means structurally:** the largest collection lever in most states — wage garnishment — is unavailable to PA medical creditors. They can pursue bank-account levies (subject to PA's separate exemptions including the homestead protections, joint accounts, and an exemption for $300 of cash under 42 Pa.C.S. § 8123), property liens, and credit-reporting (subject to the FCRA voluntary changes), but they cannot reach paychecks. This dramatically reduces the collection-pressure value of a hospital lawsuit and is one of the strongest patient-side defenses in the country.
- **Practical use:** In 30-day warning letters to PA medical creditors, surface § 8127 directly. The economic calculus of suing a PA patient is materially different from suing a NY or GA patient because the wage-garnishment endgame is unavailable. Many PA hospitals will negotiate rather than litigate once the patient signals awareness of § 8127.

## Other PA-specific patient-side advantages

### PA Unfair Trade Practices and Consumer Protection Law (UTPCPL)

- **Statute:** **73 P.S. § 201-1 et seq.** (Pennsylvania Unfair Trade Practices and Consumer Protection Law)
- **Private right of action:** **73 P.S. § 201-9.2** — any person who purchases or leases goods or services "primarily for personal, family or household purposes" and suffers loss of money or property due to an unfair or deceptive practice may bring suit for **actual damages or $100, whichever is greater**, plus **up to treble damages at the court's discretion**, plus **reasonable attorney's fees and costs**.
- **Reach over original creditors:** Unlike the federal FDCPA (15 U.S.C. § 1692a(6)), which exempts the original creditor, the UTPCPL **applies to hospitals and providers acting as original creditors** as well as to debt collectors. Pennsylvania Supreme Court in *Gregg v. Ameriprise Financial, Inc.*, 245 A.3d 637 (Pa. 2021) held that the UTPCPL imposes **strict liability** for deceptive conduct under the catchall provision (§ 201-2(4)(xxi)) — no intent or knowledge requirement for deception (though fraud subsections require scienter).
- **Substantive practices reachable for medical billing:**
  - Misrepresenting in-network status
  - Billing for services never rendered (phantom charges)
  - Upcoding (charging for a more expensive service than was performed)
  - Misrepresenting the patient's obligation, the policy terms, or the available financial assistance
  - Threatening litigation without intent to sue
  - Failing to disclose material terms (facility fees, OON status)
  - Dunning for time-barred debt
- **Sources:** [attorneygeneral.gov/wp-content/uploads/2018/02/Unfair_Trade_Practices_Consumer_Protection_Law.pdf](https://www.attorneygeneral.gov/wp-content/uploads/2018/02/Unfair_Trade_Practices_Consumer_Protection_Law.pdf); [klehr.com/publications/pennsylvania-businesses-are-strictly-liable-for-violations-of-pennsylvanias-unfair-trade-practices-and-consumer-protection-law-the-pennsylvania-supreme-court-holds](https://klehr.com/publications/pennsylvania-businesses-are-strictly-liable-for-violations-of-pennsylvanias-unfair-trade-practices-and-consumer-protection-law-the-pennsylvania-supreme-court-holds/); [marshalldennehey.com/articles/expansive-scope-liability-under-pennsylvania-unfair-trade-practices-and-consumer](https://marshalldennehey.com/articles/expansive-scope-liability-under-pennsylvania-unfair-trade-practices-and-consumer)
- **Why this matters for PA medical billing:** UTPCPL is the **functional substitute** in Pennsylvania for state surprise-billing protections and dedicated medical-billing statutes other states have enacted. Almost any deceptive billing practice is reachable under § 201-2(4)(xxi) (the catchall), and the fee-shifting + treble-damages structure makes plaintiff-side litigation economic even on smaller disputes. Pair UTPCPL with FCEUA (below) for one-two punch on hospital in-house billing.

### PA Fair Credit Extension Uniformity Act (FCEUA)

- **Statute:** **73 P.S. § 2270.1 et seq.** (Fair Credit Extension Uniformity Act), enacted Act 7 of 2000, effective June 26, 2000
- **Sources:** [legis.state.pa.us/WU01/LI/LI/US/PDF/2000/0/0007..PDF](https://www.legis.state.pa.us/WU01/LI/LI/US/PDF/2000/0/0007..PDF); [ovlg.com/blog/fceua-a-protection-for-debtors-in-pennsylvania.html](https://www.ovlg.com/blog/fceua-a-protection-for-debtors-in-pennsylvania.html); [blog.princelaw.com/2017/09/13/pennsylvania-consumers-protections-under-the-fair-credit-extension-uniformity-act](https://blog.princelaw.com/2017/09/13/pennsylvania-consumers-protections-under-the-fair-credit-extension-uniformity-act/); [attorneygeneral.gov/protect-yourself/consumer-advisories/fair-debt-collection-practices](https://www.attorneygeneral.gov/protect-yourself/consumer-advisories/fair-debt-collection-practices/)
- **Substance:** PA state-law parallel to the federal FDCPA (15 U.S.C. §§ 1692 et seq.) but **broader in two material respects**:
  - **(1) Reaches original creditors.** The FCEUA applies to **both creditors AND debt collectors**, unlike the federal FDCPA which is third-party only. § 2270.4(a) makes it an unfair practice for "a creditor" (not just a "debt collector") to engage in the listed prohibited conduct.
  - **(2) Longer SOL.** **2-year statute of limitations** vs. federal FDCPA's 1-year.
- **Enforcement via UTPCPL:** A violation of the FCEUA is **automatically a violation of the UTPCPL** (73 P.S. § 2270.5(a)), so the consumer gets UTPCPL's **$100 minimum, treble damages, and attorney's fees** for FCEUA violations.
- **Prohibited conduct (selected; § 2270.4):** Harassment, false threats of suit or arrest, contact at inconvenient hours (before 8 AM or after 9 PM), contact at workplace if employer prohibits, contact of third parties about the debt, false representation of debt amount, false representation as an attorney or government representative, threats to take property/wages that the creditor cannot lawfully take.
- **Practical use:** Whenever a PA hospital's in-house billing department or a third-party collector engages in any of the listed practices, **dual-cite FCEUA + UTPCPL** in the dispute letter. This is the highest-leverage one-two combination in PA for collection misconduct because original creditors are reachable, the SOL is longer than federal, and the remedy stack includes treble damages and attorney's fees.

### PA Patient's Bill of Rights — emergency-service billing disclosure

- **Regulation:** **28 Pa. Code § 117.41** (Emergency patient care), in conjunction with § 103.22 (general Patient's Bill of Rights)
- **Source:** [pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/028/chapter117/s117.41.html](https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/028/chapter117/s117.41.html&d=reduce)
- **Substance:** Hospitals must "establish procedures to clearly inform patients of emergency-service billing policies, including prominent display of that information in the emergency service area," specifically indicating whether patients will be billed separately for physicians' services and other emergency services.
- **Use:** When a PA patient receives a surprise OON physician bill at an in-network ER, the § 117.41 disclosure rule is a defensive lever — the hospital bears the burden of showing compliant disclosure, and absent that, the separate physician fee was not properly disclosed at the point of care.

### Pennsylvania Patient Test Result Information Act (Act 112 of 2018)

- **Statute:** **35 P.S. § 449.5b** (Patient Test Result Information Act), enacted from HB 1884, Act 112 of 2018, effective December 23, 2018 (enforcement deferred to Dec 23, 2019).
- **Sources:** [palegis.us/statutes/unconsolidated/law-information?sessYr=2018&sessInd=0&actNum=112.](https://www.palegis.us/statutes/unconsolidated/law-information?sessYr=2018&sessInd=0&actNum=112.); [pa.gov/content/dam/copapwp-pagov/en/health/documents/topics/documents/facilities-and-licensing/Act%20112%20Guidance.pdf](https://www.pa.gov/content/dam/copapwp-pagov/en/health/documents/topics/documents/facilities-and-licensing/Act%20112%20Guidance.pdf)
- **Substance:** Requires diagnostic-imaging entities to notify patients directly within **20 days** when an imaging exam shows a "significant abnormality" warranting follow-up. **NOT a billing statute** despite some online summaries that conflate Act 112 with surprise billing. Cite Act 112 only in delayed-diagnosis or test-result-notification contexts, not for billing disputes.

### Nonprofit hospital pre-collection moratorium

- **Source of obligation:** Combination of federal IRS § 501(r)(6) (extraordinary-collection-actions rules), individual hospital FAP policies, and Pennsylvania-specific nonprofit-hospital practices. Per industry summaries (Commoner Law, Dollar For), **nonprofit PA hospitals generally must wait at least 120 days after the first post-discharge bill** before selling debt, referring to credit reporting, or initiating judicial collection, and must allow **240 days for the patient to apply for financial assistance**. These are 501(r)(6) timelines, not PA-specific statutory minimums, but PA enforces them via the Act 55 purely-public-charity tax-exemption hook (a hospital that violates 501(r) practices may also jeopardize Act 55 status).
- **Sources:** [commoner-law.com/rights/healthcare-rights/medical-debt-rights/pennsylvania](https://commoner-law.com/rights/healthcare-rights/medical-debt-rights/pennsylvania); [consumerfinance.gov/data-research/research-reports/understanding-required-financial-assistance-in-medical-care](https://www.consumerfinance.gov/data-research/research-reports/understanding-required-financial-assistance-in-medical-care/); [dollarfor.org/state_sheet/pennsylvania](https://dollarfor.org/state_sheet/pennsylvania/)
- **Use:** When a PA nonprofit hospital begins collection inside the 120-day or 240-day window, cite the IRS § 501(r)(6) timelines + Act 55 purely-public-charity exemption + IRS Form 990 Schedule H reporting. The collection-action threat is the loss of nonprofit-hospital state tax exemption under Act 55.

## Quick reference for letter rendering

When the LLM renders a Pennsylvania-bound letter, substitute these defaults:

| Field                                      | Value                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| State itemization right                    | **28 Pa. Code § 103.22**, provisions 12 and 13 (PA Hospital Patient's Bill of Rights — right to examine and receive a detailed explanation of bill); pair with federal Hospital Price Transparency Rule (45 CFR Part 180) and federal GFE (45 CFR § 149.610) for uninsured/self-pay                                |
| State insurance regulator (CC line)        | Pennsylvania Insurance Department, Bureau of Consumer Services, Room 1209, Strawberry Square, Harrisburg, PA 17120; 1-877-881-6388; [pa.gov/agencies/insurance/consumer-help-center/complaints-questions-help](https://www.pa.gov/agencies/insurance/consumer-help-center/complaints-questions-help)               |
| State AG (CC line, for billing disputes)   | PA Office of Attorney General, Health Care Section, 14th Floor, Strawberry Square, Harrisburg, PA 17120; 1-877-888-4877 (in-state) / 1-717-705-6938; [attorneygeneral.gov/submit-a-complaint/health-care-complaint](https://www.attorneygeneral.gov/submit-a-complaint/health-care-complaint/)                     |
| State AG (CC line, for non-medical)        | PA Office of Attorney General, Bureau of Consumer Protection, 1-800-441-2555; consumers@attorneygeneral.gov                                                                                                                                                                                                        |
| Small-claims court name                    | **Magisterial District Court of [district number]** in the defendant's county; $12,000 cap per 42 Pa.C.S. § 1515(a)                                                                                                                                                                                                |
| Filing fee (in 30-day warning)             | "Approximately $50-$150 in Magisterial District Court, plus separate constable service fees, depending on claim amount and number of defendants"                                                                                                                                                                   |
| Statute of limitations (in 30-day warning) | "**42 Pa.C.S. § 5525(a) — four years for breach of written contract**, applicable to medical-debt collection actions in Pennsylvania"                                                                                                                                                                              |
| Ground-ambulance citation                  | **No PA state law.** Federal NSA excludes ground ambulance. Negotiate to in-network or Medicare-allowable rate; UTPCPL/FCEUA leverage if billing is deceptive.                                                                                                                                                     |
| Hospital financial-assistance citation     | Federal IRS § 501(r) + PA **Institutions of Purely Public Charity Act, 10 P.S. §§ 371-385** (Act 55 of 1997) for nonprofit hospitals; for-profit/public hospitals have no PA statutory FAP mandate                                                                                                                 |
| Credit-reporting citation                  | **No PA state law.** Use federal FCRA (15 U.S.C. §§ 1681i, 1681s-2) dispute rights; voluntary bureau policies (paid debt removed, under $500 not reported, 1-year delay)                                                                                                                                           |
| Surprise-billing citation                  | **No PA state law.** Use federal No Surprises Act (Pub. L. 116-260); file PA NSA complaint at [pa.gov/services/insurance/request-a-review-of-an-unexpected-medical-bill-no-surprises-act](https://www.pa.gov/services/insurance/request-a-review-of-an-unexpected-medical-bill-no-surprises-act)                   |
| External-appeal citation                   | **Act 146 of 2022** (40 P.S. §§ 991.2101 - 991.2193) state external review for fully-insured PA plans; 4-month filing window, 45-day standard / 72-hour expedited, IRO binding on plan, no patient fee                                                                                                             |
| Bad-faith citation                         | **42 Pa.C.S. § 8371** — interest at prime + 3%, punitive damages, court costs, AND attorney's fees on clear-and-convincing showing of bad-faith insurer conduct. No demand-and-wait requirement. 2-year SOL under § 5524 per *Ash*.                                                                                |
| Insurance-practices citation               | **40 P.S. § 1171.1 et seq.** (UIPA) — regulator enforcement only, no private right of action per *D'Ambrosio*. File PID complaint; use as evidentiary support for § 8371 claim.                                                                                                                                    |
| Deceptive-practices citation               | **73 P.S. § 201-1 et seq.** (UTPCPL) — private right of action under § 201-9.2: actual damages or $100 minimum, up to treble damages, attorney's fees. **Reaches original creditors** including hospitals.                                                                                                         |
| Debt-collector misconduct citation         | **73 P.S. § 2270.1 et seq.** (FCEUA) — reaches original creditors AND third-party collectors; 2-year SOL; FCEUA violations are automatically UTPCPL violations, accessing UTPCPL's treble-damages + attorney's-fees remedies.                                                                                      |
| Hospital lien citation                     | **None — PA has no statewide hospital lien statute.** Hospitals rely on contractual liens (admission financial-responsibility forms) and common-law quantum meruit. Medicaid liens are governed separately by Act 44 of 2008 / 62 P.S. § 1409.                                                                     |
| Wage-garnishment posture                   | **42 Pa.C.S. § 8127** — PA categorically exempts wages from garnishment for medical debt and all consumer debt. Exceptions: support, PHEAA, board (≤4 wks), restitution, residential rent, federal/state taxes, federal student loans. **A PA medical creditor with a judgment cannot reach the patient's wages.** |

## Key Pennsylvania-specific advantages

Worth keeping in mind when triaging a PA patient's bills:

1. **42 Pa.C.S. § 8371 — the strongest first-party insurance bad-faith statute in the United States.** Prime + 3% interest, punitive damages, court costs, AND attorney's fees, all available on a clear-and-convincing showing of bad-faith claims handling under the two-prong *Terletsky/Rancosky* standard. No demand-and-wait requirement; no statutory penalty cap; no requirement that conduct be malicious — recklessness suffices. Enacted 1990 in direct response to the PA Supreme Court's 1981 *D'Ambrosio* invitation; has been the gold standard ever since. This is the headline lever in any PA fully-insured-plan dispute. **ERISA-preempted for self-funded plans.**
2. **42 Pa.C.S. § 8127 — wages categorically exempt from medical-debt garnishment.** PA is one of a handful of states (with NC, SC, and TX) where wages cannot be garnished for medical debt even with a judgment. The economic calculus of suing a PA patient is materially different from suing a NY or GA patient because the post-judgment endgame on wages is unavailable. Many hospitals will negotiate rather than litigate once aware.
3. **UTPCPL (73 P.S. § 201-1) + FCEUA (73 P.S. § 2270.1) reach original creditors.** Unlike the federal FDCPA, PA's debt-collection consumer-protection framework binds hospitals and providers acting as original creditors. Combined with strict-liability under *Gregg v. Ameriprise* (2021) and the § 201-9.2 remedy stack ($100 minimum, treble damages, attorney's fees), this makes hospital in-house billing departments directly liable for deceptive practices.
4. **State external review under Act 146 of 2022** — Free, IRO-binding, 45-day decision (72-hour expedited), 4-month filing window. Cleanest leverage for medical-necessity denials on fully-insured plans.
5. **Dedicated AG Health Care Section** — 1-877-888-4877, a PA-specific advantage shared by only a handful of states (NY, MA, others). Subject-matter expertise on health-care disputes, routinely intervenes on individual cases, has historically recovered millions in refunds and savings.
6. **Magisterial District Court non-attorney corporate-appearance rule** — corporate defendants can appear through a non-lawyer officer or employee under Pa.R.C.P.M.D.J. 207. Pro se patients are more likely to face a hospital billing-department staffer than a defense attorney; the economic leverage in small claims is correspondingly higher.
7. **Act 55 of 1997 (10 P.S. §§ 371-385) tax-exemption hook** — PA nonprofit hospitals must satisfy the HUP test's charity-care prong to maintain state and local tax exemption. The threat of losing that exemption is a meaningful settlement lever when negotiating with PA nonprofit systems (which include most major PA hospitals).

Worth flagging where PA is **weaker** than the strongest state packs:

- **No state surprise-billing law.** PA relies entirely on the federal No Surprises Act. (NY, CA, GA, TX, FL, and 30+ others have broader state-law surprise-billing protections.)
- **No state ground-ambulance balance-billing protection.** The federal NSA excludes ground ambulance; PA has not closed this gap. (19 states have, including CA, NY, CO, IL, OH, TX, MD, VA, WA, and others.)
- **No state medical-debt credit-reporting restriction.** PA relies entirely on federal FCRA + the voluntary 2022-2023 bureau changes. (NY's FMDRA, CO, IL, MN, NJ, DE, and others have state-level prohibitions.)
- **No statewide hospital lien act.** Hospitals must rely on contractual liens and common-law quantum meruit. (Most states have a dedicated hospital lien statute.)
- **Charity-care framework is tax-exemption-driven, not patient-rights-driven.** PA's Act 55 protects the hospital's nonprofit status but does not, like NY's PHL § 2807-k(9-a) or CA's Hospital Fair Pricing Act, set patient-side eligibility thresholds, application timelines, or pre-suit moratoriums by statute.

Net assessment: PA is **moderate-to-strong overall**, with two world-class patient-side levers (§ 8371 bad-faith and § 8127 wage exemption) and a strong consumer-protection stack (UTPCPL + FCEUA reaching original creditors), but meaningful gaps on surprise billing, ground ambulance, credit reporting, and uniform charity-care standards. Lead with the bad-faith and wage-exemption cites in PA disputes; supplement with UTPCPL/FCEUA for billing-conduct claims; and route surprise-bill and ground-ambulance situations through federal-NSA and UTPCPL-deception channels respectively, since no PA-specific state lever exists.
