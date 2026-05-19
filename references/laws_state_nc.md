# North Carolina state pack

The fully-worked state-law layer for North Carolina patients. The LLM uses this when the patient's state is North Carolina. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Three things make North Carolina's patient-side leverage unusually strong:

1. The **Unfair and Deceptive Trade Practices Act (UDPA) at N.C. Gen. Stat. § 75-1.1 reaches original creditors** (the hospital itself, not just third-party collectors) and **automatically trebles damages** under § 75-16, plus discretionary attorney's fees under § 75-16.1. This is the single highest-leverage NC-specific lever against a provider's in-house billing department.
2. The **Medical Debt De-Weaponization Act / Medical Debt Relief Program** (effective July 1, 2025, implemented via the NCDHHS HASP Medicaid hospital-payment program) requires all participating hospitals to forgive Medicaid-enrollee debt back to 2014 and most low-income debt over two years old, plus stops reporting medical debt to credit bureaus. Every eligible hospital in the state has signed on.
3. The **NC Debt Collection Act (§§ 75-50 through 75-56) applies to original creditors**, not just third-party debt collectors, with statutory penalties of $500-$4,000 **per violation** plus the underlying actual damages. Federal FDCPA reaches only third-party collectors; the NC version closes that gap.

## Hospital itemization right

- **Statute:** **N.C. Gen. Stat. § 131E-91** — Fair billing and collections practices for hospitals and ambulatory surgical facilities (Hospital Licensure Act, Article 5)
- **Source:** [ncleg.gov/EnactedLegislation/Statutes/PDF/BySection/Chapter_131E/GS_131E-91.pdf](https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/BySection/Chapter_131E/GS_131E-91.pdf); [Justia](https://law.justia.com/codes/north-carolina/chapter-131e/article-5/) (Article 5 index); [FindLaw](https://codes.findlaw.com/nc/chapter-131e-health-care-facilities-and-services/nc-gen-st-sect-131e-91/)
- **What it requires:**
  - Upon request of the patient, the hospital or ambulatory surgical facility (ASF) must present an itemized list of charges in language a layperson can understand.
  - Non-itemized bills must include written notice of the patient's right to request an itemized bill **free of charge**.
  - A patient may request the itemized bill **any time within 3 years after discharge**, or for as long as the facility, a collection agency, or another assignee asserts the patient owes the bill — whichever is longer.
  - The facility must establish a documented method for patients to inquire about or dispute a bill.
- **Collections-side duties (same statute):**
  - At least **30 days' written notice** to the patient before referring a bill to collections.
  - **No referral to collections during the pendency of a charity-care / financial-assistance application.**
  - Any collection agency under contract to the facility must inform patients of the facility's charity-care policies during collection activity.
- **Scope:** Hospitals and ambulatory surgical facilities licensed in North Carolina. Sister provision for ASFs at § 131E-147.1 mirrors the same duties.
- **Private right of action:** § 131E-91 does not itself create a private cause of action, but a violation is routinely pled as the predicate "unfair or deceptive act" under § 75-1.1 (see below), which carries treble damages and attorney's fees.
- **ERISA:** Not preempted — regulates the provider, not the plan.

## UDPA — Unfair and Deceptive Trade Practices Act

- **Statutes:** **N.C. Gen. Stat. § 75-1.1** (general prohibition), **§ 75-16** (automatic treble damages), **§ 75-16.1** (discretionary attorney's fees)
- **Sources:** [ncleg.gov Chapter 75 Article 1 PDF](https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/ByArticle/Chapter_75/Article_1.pdf); [Justia Chapter 75 Article 1](https://law.justia.com/codes/north-carolina/chapter-75/article-1/); [§ 75-16.1 PDF](https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/BySection/Chapter_75/GS_75-16.1.pdf)
- **Elements (consumer plaintiff):**
  1. An unfair or deceptive act or practice;
  2. In or affecting commerce;
  3. That proximately caused injury to the plaintiff.
- **Why NC patients love this statute:**
  - **Treble damages are automatic**, not discretionary — § 75-16 directs the court to enter judgment "for treble the amount fixed by the verdict" once liability is found.
  - **Attorney's fees** are recoverable under § 75-16.1 if the court finds the defendant willfully engaged in the act and made an unwarranted refusal to fully resolve the dispute.
  - **Reaches original creditors**, including hospital in-house billing departments — far broader than federal FDCPA.
  - Four-year statute of limitations (§ 75-16.2), longer than the standard three-year contract clock.
- **Common UDPA predicates in medical billing:**
  - Billing for services never rendered
  - Upcoding (billing a higher CPT level than the documentation supports)
  - Misrepresenting in-network status
  - Pursuing collections after a charity-care application is pending (per § 131E-91)
  - Threatening litigation or wage garnishment the creditor has no intent or legal basis to pursue
  - Furnishing inaccurate medical-debt information to credit bureaus
- **Critical limit — "learned profession" exemption:** § 75-1.1(b) excludes "professional services rendered by a member of a learned profession." Courts apply a two-part test: (a) the actor is a member of a learned profession, and (b) the conduct at issue **is the rendering of professional services**. Billing, collection, and business-side conduct by a hospital or practice are **commerce**, not learned-profession services, and remain reachable under § 75-1.1. Gray v. N.C. Ins. Underwriting Ass'n, 352 N.C. 61, 529 S.E.2d 676 (2000) is the leading case holding that insurance-claim handling falls inside § 75-1.1.
- **ERISA preemption:** As applied to a self-funded ERISA employer plan's claim-handling, § 75-1.1 is preempted. For fully-insured plans, Medicaid managed care, and direct provider-billing disputes, the statute is in play.

## NC Debt Collection Act — applies to original creditors

- **Statutes:** **N.C. Gen. Stat. §§ 75-50 through 75-56** (Article 2 of Chapter 75)
- **Sources:** [ncleg.gov Chapter 75 Article 2 PDF](https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/ByArticle/Chapter_75/Article_2.pdf); [Justia Article 2](https://law.justia.com/codes/north-carolina/chapter-75/article-2/)
- **Substance:** Prohibits a defined list of debt-collection abuses — false or misleading representations, unfair threats and coercion, harassment, contacting at unreasonable hours, communicating with third parties about the debt, etc.
- **Scope advantage over federal FDCPA:** **Applies to original creditors**, not only third-party debt collectors. A hospital's in-house billing department is reachable; under federal FDCPA it is not.
- **Remedies:** Actual damages **plus a civil penalty of $500 to $4,000 per violation** (§ 75-56). Violations also independently support a § 75-1.1 UDPA claim with the treble-damages and fee provisions above.
- **Practical use:** Cite the specific subsection violated (e.g., § 75-54 for unfair representations, § 75-55 for unconscionable means) in dispute letters before the dispute escalates to litigation.

## Unfair Insurance Trade Practices Act

- **Statutes:** **N.C. Gen. Stat. § 58-63-1 et seq.** (declaration of purpose at § 58-63-1; listed practices at § 58-63-15)
- **Sources:** [ncleg.gov Chapter 58 Article 63 PDF](https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/ByArticle/Chapter_58/Article_63.pdf); [Justia § 58-63-1](https://law.justia.com/codes/north-carolina/chapter-58/article-63/section-58-63-1/); [FindLaw § 58-63-15](https://codes.findlaw.com/nc/chapter-58-insurance/nc-gen-st-sect-58-63-15/)
- **Substance:** Prohibits insurers from engaging in defined unfair or deceptive practices, including the unfair-claim-settlement-practices list (misrepresenting policy provisions, failing to promptly acknowledge claims, denying without reasonable investigation, failing to attempt good-faith settlement once liability is reasonably clear).
- **Critical caveat — no private right of action under this Article:** The unfair-claim-settlement subsection expressly does not create a private cause of action; enforcement is by the Commissioner of Insurance only. Courts repeatedly dismiss standalone § 58-63-15 claims brought by insureds.
- **Workaround that makes this statute matter anyway:** Under **Gray v. N.C. Ins. Underwriting Ass'n**, 352 N.C. 61, 529 S.E.2d 676 (2000), an insurer's violation of § 58-63-15 unfair-claim-settlement standards **constitutes a per-se violation of § 75-1.1** — which does carry a private cause of action, treble damages, and attorney's fees. The patient pleads § 75-1.1 as the cause of action and uses § 58-63-15 as the substantive standard.
- **Use:** Cite both statutes together in complaints to the NCDOI Consumer Services Division and in any pre-suit demand letter.

## Bad-faith refusal to pay (common law)

- **Authority:** Common-law tort recognized in **Dailey v. Integon General Ins. Corp.**, 75 N.C. App. 387, 331 S.E.2d 148 (1985), with subsequent appellate development
- **Sources:** [Justia, Dailey v. Integon (1985)](https://law.justia.com/cases/north-carolina/court-of-appeals/1985/843sc283-1.html); [NC pattern jury instruction PJI 810.92](https://sog.unc.edu/sites/default/files/pji-master-2024/civil/810.92%20Punitive%20Damages%20-%20Insurance%20Company%27s%20Bad%20Faith%20Refusal%20to%20Settle%20a%20Claim.pdf)
- **Elements:**
  1. A refusal to pay a valid claim;
  2. The refusal was not based on an honest disagreement or innocent mistake;
  3. **Aggravating or outrageous conduct** — fraud, malice, gross negligence, willful and wanton conduct, or other conduct showing reckless disregard of the policyholder's rights.
- **Damages:** Compensatory damages plus **punitive damages** if the aggravating-conduct element is met. Capped under N.C. Gen. Stat. § 1D-25 (the greater of three times compensatory damages or $250,000), with statutory exceptions.
- **NC bad-faith doctrine is narrow:** Honest disagreement, even if the insurer turns out to be wrong, is not bad faith. The plaintiff must show conduct closer to fraud than negligence. This is a meaningfully higher bar than Georgia § 33-4-6, Texas Chapter 541, or California Comunale-line cases.
- **ERISA preemption:** State-law bad-faith claims against self-funded ERISA plans are preempted; the federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) attorney's fees. Fully-insured, Medicaid managed care, and individual/marketplace plans remain reachable.
- **Practical use:** Reserve as a fallback after § 75-1.1 / § 58-63-15 demand letters fail. The high evidentiary bar makes this a litigation cause of action, not a leverage cite in a first-round letter.

## Surprise billing — state law

- **Statute:** **N.C. Gen. Stat. § 58-3-200** (general insurance and managed-care network provisions), plus HMO-specific protections at **§ 58-67-88** (HMOs cannot balance-bill members for emergency services)
- **Sources:** [ncleg.gov § 58-3-200](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_58/GS_58-3-200.html); [Source on Healthcare Price summary](https://sourceonhealthcare.org/legislation/n-c-gen-stat-%C2%A7-58-3-200-miscellaneous-insurance-and-managed-care-coverage-and-network-provisions-general-regulations-for-insurance/); [Duke Health patient notice](https://www.dukehealth.org/paying-for-care/your-rights-and-protections-against-surprise-medical-bills); [Charlotte Center for Legal Advocacy summary](https://charlottelegaladvocacy.org/no-surprises-act-protecting-patients-from-surprise-medical-bills/)

### What NC state law protects

- For **HMO members**, balance billing is broadly prohibited for covered services. The HMO must hold the patient harmless from any rate dispute with an out-of-network provider.
- For all NC-regulated plans, a patient may not be charged more for emergency services from an out-of-network provider than from an in-network provider (cost-sharing capped at in-network amount for the screening and stabilization phase).
- At an **in-network hospital or ambulatory surgical center**, certain ancillary providers (emergency medicine, anesthesia, pathology, radiology, laboratory, neonatology, assistant surgeon, hospitalist, intensivist) may bill no more than the plan's in-network cost-share. Balance billing by these providers is prohibited.

### Critical gap

- **PPO members may still be balance-billed** for out-of-network services outside the in-network-facility ancillary category — NC state law's PPO protection is meaningfully weaker than its HMO protection.
- **Ground ambulance is not covered** by NC state law (see Ground ambulance section below).
- The federal **No Surprises Act (Public Law 116-260, eff. Jan 1, 2022)** fills most of the PPO gap for emergency services and in-network-facility ancillary services. Where federal and state both apply, they layer rather than displace; the more-protective rule governs.

### HB 312 legislative history

HB 312 (2021-2022 session) was a proposed comprehensive NC surprise-billing statute that would have aligned NC state law with the broader scope of the federal No Surprises Act. **It did not pass.** NC patients therefore rely on the existing patchwork at § 58-3-200 plus the federal NSA. Verify session status before citing HB 312 in any dispute letter — at the time of writing it remains unenacted.

### ERISA

State-level NC surprise-billing protections do not reach self-funded ERISA employer plans. Federal NSA does reach those plans for emergency services and in-network-facility ancillary services.

## Ground ambulance balance billing

**NC has no enacted state-law protection for ground-ambulance balance billing as of 2026-05-18.** This is the single largest gap in NC patient protection compared to states like California, Maryland, New York, Ohio, and Georgia.

- The federal No Surprises Act **explicitly excludes ground ambulance**.
- House Bill 456 (2025) — "No Surprises for Ambulance Services Act" — was introduced and passed the House unanimously in 2025 to close this gap, but had not been enacted into law as of 2026-05-18. **Verify enactment status before citing.**
- Source: [HB 456 bill text](https://www.ncleg.gov/Sessions/2025/Bills/House/PDF/H456v1.pdf); [Carolina Journal coverage](https://www.carolinajournal.com/nc-house-unanimously-caps-costs-for-emergency-ambulance-rides/); [NC Health News, "Short ambulance ride, big bill"](https://www.northcarolinahealthnews.org/2025/06/09/short-ambulance-ride-big-bill/); [Commonwealth Fund state tracker](https://www.commonwealthfund.org/blog/2026/consumers-still-face-surprise-bills-ground-ambulances-states-are-trying-protect-them)

Until HB 456 (or a successor) is enacted, an NC patient's leverage on a ground-ambulance bill is:

- Negotiate directly with the EMS agency (most NC EMS is county-operated; political pressure via a county commissioner is sometimes effective).
- File a § 75-1.1 UDPA complaint if the EMS agency or its billing contractor uses unfair or deceptive collection practices.
- Apply for hospital charity care if the ambulance bill rolled into a hospital admission.

## Regulatory agencies

### North Carolina Department of Insurance (NCDOI), Consumer Services Division

- **Online complaint:** [ncdoi.gov/assistance-or-file-complaint](https://www.ncdoi.gov/assistance-or-file-complaint)
- **Phone:** Consumer Services toll-free **1-855-408-1212**; main switchboard **(919) 807-6000**
- **Mail:**
  > North Carolina Department of Insurance
  > Consumer Services Division
  > 1201 Mail Service Center
  > Raleigh, NC 27699-1201
- **Authority:** All insurance companies licensed in NC, including fully-insured health insurers, HMOs, PPOs, and Medicare supplement. Administers § 58-63-15 unfair claims practices and § 58-3-200 surprise-billing provisions. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272). Does not regulate providers, hospitals, or original-creditor debt collectors — route those to the NC AG.

### North Carolina Department of Justice (Attorney General), Consumer Protection Division

- **Online complaint:** [ncdoj.gov/file-a-complaint/consumer-complaint](https://ncdoj.gov/file-a-complaint/consumer-complaint/)
- **Phone:** Consumer hotline **1-877-5-NO-SCAM** (1-877-566-7226); main **(919) 716-6000**
- **Email:** [consumer@ncdoj.gov](mailto:consumer@ncdoj.gov)
- **Mail:**
  > N.C. Department of Justice
  > Consumer Protection Division
  > 9001 Mail Service Center
  > Raleigh, NC 27699-9001
- **Authority:** Enforces § 75-1.1 UDPA and the § 75-50 et seq. Debt Collection Act. Reach over providers, hospitals, third-party debt collectors, **and original creditors** — exactly the gap not covered by NCDOI. Useful when the dispute is with the hospital's in-house billing department or a hospital-owned collection arm.

## Small-claims court — Magistrate Court (District Court)

- **Court name:** **Small Claims Court**, a docket of the **District Court** heard by a **Magistrate**. NC does not use the term "Magistrate Court" as a stand-alone court name.
- **Jurisdictional limit:** **$10,000**, codified at **N.C. Gen. Stat. § 7A-210** (and § 7A-211)
- **Source:** [ncleg.gov Chapter 7A Article 19 PDF](https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/ByArticle/Chapter_7A/Article_19.pdf); [NC Judicial Branch small-claims page](https://www.nccourts.gov/help-topics/lawsuits-and-small-claims/small-claims)
- **Filing fee:** **$96 statewide** (set in 2024, unchanged into 2026). Petition to Proceed as an Indigent is available for fee waiver.
- **Attorney rules:** Permitted, not required. Designed for pro se litigants. Corporate defendants in NC small claims generally must appear through a licensed attorney for trial conduct under the unauthorized-practice-of-law rule — a procedural advantage NC patients enjoy that GA patients do not (Magistrate Court in GA expressly allows non-attorney corporate appearance).
- **Appeal:** Either party may appeal to District Court for a trial de novo within 10 days of judgment (N.C. Gen. Stat. § 7A-228).
- **Jury trial:** Not available in small-claims division. Available on de novo appeal in District Court.

## Statute of limitations

- **Most contracts (written or oral) and open accounts:** **3 years from breach** — **N.C. Gen. Stat. § 1-52(1)**
- **Contracts under seal:** **10 years** — **N.C. Gen. Stat. § 1-47(2)**
- **UCC § 2-725 sale-of-goods contracts:** 4 years — N.C. Gen. Stat. § 25-2-725 (rarely the right cite for hospital services; services contracts use § 1-52)
- **UDPA (§ 75-1.1) claims:** 4 years — N.C. Gen. Stat. § 75-16.2
- **Sources:** [§ 1-52 PDF](https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/BySection/Chapter_1/GS_1-52.pdf); [Smith Debnam practitioner summary](https://www.smithdebnamlaw.com/article/statute-of-limitations-in-north-carolina/); [§ 25-2-725 Justia](https://law.justia.com/codes/north-carolina/chapter-25/article-2/section-25-2-725/)

NC's 3-year contract clock is **shorter than most states** — Georgia is 6 years for written, Florida 5, Texas 4. This is a meaningful patient-side advantage when a hospital sits on a bill or sells it to a debt buyer. The clock runs from breach (typically the day payment was due and not made), not from when the patient knew of the damages.

Most hospital admissions involve a signed financial-responsibility form. Even when signed, the form is a written contract under § 1-52 (3 years), not "under seal" under § 1-47(2) (10 years) unless it specifically recites and uses the formal seal language and indicia required by NC case law. **Hospital forms are virtually never "under seal" in the § 1-47(2) sense** — push back hard if a collector cites the 10-year limit.

Partial payment or a written acknowledgment of the debt can restart the clock under standard NC contract law. **Do not make a partial payment on a time-barred debt without legal advice.**

## Credit reporting — Medical Debt De-Weaponization Act / Medical Debt Relief Program

**This is one of NC's strongest patient-side levers.** The legislative bill (HB 367 / SB 321 / HB 1039, "Medical Debt De-Weaponization Act") did not pass as a stand-alone statute in 2023-2024. Instead, the Cooper / Stein administrations implemented the same protections **administratively** through the NCDHHS Healthcare Access and Stabilization Program (HASP), making enhanced Medicaid hospital payments conditional on hospitals signing on to a Medical Debt Relief Initiative.

- **Source materials:** [NCDHHS Medical Debt portal](https://www.ncdhhs.gov/medicaldebt); [NC Governor press release, $6.5B erased (Oct 2025)](https://governor.nc.gov/news/press-releases/2025/10/13/governor-stein-ncdhhs-announce-more-65-billion-medical-debt-erased-north-carolina-0); [NC Health News, 11 must-dos for hospitals](https://www.northcarolinahealthnews.org/2024/08/13/nc-medical-debt-relief-plan-11-hospitalmust-dos-for-hospitals/); [bill text H1039](https://www.ncleg.gov/Sessions/2025/Bills/Senate/PDF/S672v0.pdf); [Office Ally compliance brief](https://cms.officeally.com/blog/north-carolinas-new-medical-bill-de-weaponization-act)

### What participating NC hospitals (every eligible hospital) must do

- **Forgive all medical debt** owed by patients who were enrolled in Medicaid on July 1, 2025, dating back to **January 1, 2014**.
- **Forgive medical debt more than two years old** for patients at or below **350% of the federal poverty level** ($52,710 individual / $109,200 family of four at 2024 thresholds), or for patients whose total medical debt to that hospital **exceeds 5% of their annual income**.
- **Stop reporting medical debt to credit bureaus** for any debt covered by the program.
- Adopt charity-care eligibility automatically for patients at or below 200% FPL (free care) and 300% FPL (discounted care).
- Provide a written debt-mitigation policy, automatic screening for charity care, and a 30-day notice before any collections referral.

### Use in a dispute letter

If the patient is on Medicaid, below 350% FPL, or has a bill more than two years old, **ask the hospital in writing whether the patient qualifies under the hospital's Medical Debt Relief Program participation**. Every eligible hospital in NC has signed on; refusal to apply the program correctly is itself a § 75-1.1 UDPA candidate.

### Federal preemption posture

The CFPB issued an October 2025 interpretive rule taking the position that the FCRA preempts state laws restricting medical-debt credit reporting. The NC program is structured as a **hospital contractual obligation under HASP**, not a state law restricting credit-bureau furnishers, so it is largely insulated from that preemption argument. Monitor for changes.

## Hospital charity care

- **Statutes:** **N.C. Gen. Stat. § 131E-214.13** (price disclosure for top DRGs and CPTs) and **§ 131E-214.14** (disclosure of charity-care policy and annual financial-assistance costs)
- **Sources:** [ncleg.gov Chapter 131E Article 11B PDF](https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/ByArticle/Chapter_131E/Article_11B.pdf); [§ 131E-214.14 (2013) Justia](https://law.justia.com/codes/north-carolina/2013/chapter-131e/article-11b/section-131e-214.14/); [Hilltop Institute NC Community Benefit summary](https://hilltopinstitute.org/wp-content/uploads/hcbp/hcbp_docs/HCBP_CBL_NC.pdf)
- **Substance:**
  - Hospitals and ASFs required to file IRS Form 990 Schedule H must publish their financial-assistance policy and annual charity-care cost figures on a publicly searchable NC Department portal, plus display in a conspicuous place at the facility.
  - § 131E-91 collections-side duties (no collections during pending charity-care application; mandatory 30-day pre-collection notice) layer on top.
- **HEAL Act caveat:** The user's prompt referenced "the HEAL Act" — note that the NC HEAL Initiative is the **administrative Medical Debt Relief Program** described above, not a stand-alone statute. The codified charity-care obligations live in §§ 131E-214.13, 131E-214.14, and 131E-91. The HASP / HEAL contractual obligations supplement (and in practice supersede) the statutory floor.
- **Federal floor for non-profit hospitals:** IRS § 501(r) (federal); applies to all NC non-profit hospitals.
- Use [Dollar For](https://dollarfor.org/state_sheet/north-carolina/) for screening.

## Hospital lien statute

- **Statutes:** **N.C. Gen. Stat. §§ 44-49 and 44-50** (Article 9 of Chapter 44, "Hospital Liens")
- **Sources:** [ncleg.gov Chapter 44 Article 9 PDF](https://www.ncleg.gov/EnactedLegislation/Statutes/PDF/ByArticle/Chapter_44/Article_9.pdf); [§ 44-50 FindLaw](https://codes.findlaw.com/nc/chapter-44-liens/nc-gen-st-sect-44-50/); [§ 44-49 FindLaw](https://codes.findlaw.com/nc/chapter-44-liens/nc-gen-st-sect-44-49.html); [Wallace Pierce practitioner overview](https://www.wallacepierce.com/durham-car-accident-lawyer/compensation-for-injuries/liens-and-subrogation/physicians-liens-under-44-49/)
- **Substance:** A lien attaches in favor of physicians, dentists, nurses, hospitals, ambulance providers, and similar drug/supply providers **only against the patient's recovery from a third-party tortfeasor** (e.g., the at-fault driver in a car wreck). **Not a lien on the patient's home, wages, or bank accounts.**
- **Perfection requirements (§ 44-49(b)):**
  - As a **condition precedent**, the provider must furnish the patient's attorney — upon request and free of charge — with an itemized statement, hospital record, or medical report, plus written notice of the lien claim.
  - Recent case law / practice update: medical providers must produce itemized bills and records within **60 days of a HIPAA request** by the patient or attorney; failure can invalidate the lien.
- **Cap (§ 44-50):** The combined amount payable on all liens cannot exceed **50% of the damages recovered** after attorney's fees. The patient is guaranteed 50% of the net recovery free of liens.
- **Practical use:** If the bill stems from an accident with a third-party tortfeasor, demand the lien itemization and notice under § 44-49(b). Defective perfection is the single most common attack on hospital liens in NC.

## Wage garnishment

- **Statute:** N.C. Const. art. X, § 1 prohibits garnishment of personal earnings for most consumer debts, including medical debt, **with limited statutory exceptions** (taxes, child support, federal student loans, court-ordered restitution, ambulance bills under § 131E-49 in some counties).
- **Source:** Compare federal CCPA at 15 U.S.C. § 1673.
- **Substance:** Unlike Georgia (which permits 25% disposable-earnings garnishment post-judgment), **NC does not permit a medical creditor to garnish wages even after obtaining a judgment**. Bank account levy is available; wage garnishment generally is not.
- **Use:** In response letters to collectors threatening wage garnishment for a medical bill, cite N.C. Const. art. X, § 1 and demand the collector identify the statutory exception authorizing garnishment. None usually exists, and the threat itself can be a § 75-50 et seq. and § 75-1.1 violation.

## Quick reference for letter rendering

When the LLM renders a North Carolina-bound letter, substitute these defaults:

- **State statute (itemization right):** **N.C. Gen. Stat. § 131E-91** — patient may request itemized bill at any time within 3 years after discharge, or for as long as the debt is asserted; collections referral requires 30 days' written notice; no collections during pending charity-care application.
- **State headline statute (provider-side):** **N.C. Gen. Stat. § 75-1.1** with **automatic treble damages under § 75-16** and discretionary **attorney's fees under § 75-16.1**. This is the headline cite in every NC dispute letter to a provider, hospital, or original creditor.
- **State insurance department (CC line):** North Carolina Department of Insurance, Consumer Services Division, 1201 Mail Service Center, Raleigh, NC 27699-1201; toll-free **1-855-408-1212**
- **State AG consumer protection (CC line):** N.C. Department of Justice, Consumer Protection Division, 9001 Mail Service Center, Raleigh, NC 27699-9001; **1-877-5-NO-SCAM** ([ncdoj.gov/file-a-complaint/consumer-complaint](https://ncdoj.gov/file-a-complaint/consumer-complaint/))
- **Small-claims court name:** **Small Claims Court of [county] (District Court, before a Magistrate)**
- **Filing fee (in 30-day warning):** "$96 statewide (N.C. Gen. Stat. § 7A-305; verify current schedule with the Clerk of Court)"
- **Statute of limitations (in 30-day warning):** "N.C. Gen. Stat. § 1-52(1) (three years for breach of most contracts)" — and for UDPA claims, "§ 75-16.2 (four years)"
- **For credit-reporting / financial-hardship cases:** cite the **NC Medical Debt Relief Program** (HASP-conditioned, effective July 1, 2025) and demand the hospital apply its Medical Debt Mitigation Policy.
- **For provider-side disputes:** lead with § 75-1.1 + § 75-16 (treble damages) + § 75-16.1 (fees). Add § 131E-91 as the substantive predicate for itemization or charity-care violations, § 75-50 et seq. for debt-collection abuses.
- **For insurer-side disputes:** plead § 75-1.1 with § 58-63-15 (unfair-claim-settlement standards) as the per-se predicate per Gray v. N.C. Ins. Underwriting Ass'n. Add common-law bad-faith (Dailey v. Integon) only when aggravating-conduct evidence is present.
- **For ground-ambulance bills:** acknowledge the gap — no NC state-law protection as of 2026-05-18; HB 456 pending. Use § 75-1.1 / § 75-50 et seq. against any unfair collection practices, and pursue charity care.

## Key North Carolina-specific advantages

Worth keeping in mind when triaging an NC patient's bills:

1. **§ 75-1.1 with automatic treble damages and attorney's fees** — far and away the headline NC lever. Treble damages are not discretionary; once liability is found, the court must enter judgment for three times the verdict. § 75-16.1 fees push the economics in the patient's favor before a single deposition.
2. **§ 75-1.1 reaches original creditors** — the hospital's own billing department, not just outsourced collection vendors. Federal FDCPA reach stops at third-party collectors; NC closes that gap.
3. **NC Debt Collection Act § 75-50 et seq. also reaches original creditors** with $500-$4,000 statutory penalties per violation. Cite alongside § 75-1.1 in every dispute letter to an original-creditor hospital.
4. **Medical Debt Relief Program (HASP)** — every eligible NC hospital has contractually agreed to forgive most low-income and Medicaid-enrollee debt and stop reporting medical debt to credit bureaus. Always screen the patient against the 350% FPL / 5%-of-income / 2-year thresholds before drafting a letter.
5. **No wage garnishment for medical debt** — NC Constitution prohibits it. A collector threatening wage garnishment on a medical bill is making a per-se UDPA-actionable misrepresentation.
6. **Three-year contract SoL** — short enough that aged debts and debt-buyer purchases frequently lose their litigation leverage. Verify the breach date before responding to any "balance owed" demand more than three years old.
7. **HMO members protected from balance billing**, PPO members partially protected via the federal NSA. Identify plan type early.
8. **NSA gap for ground ambulance is real and unclosed in NC** — manage patient expectations on ambulance bills, but use § 75-1.1 and § 75-50 et seq. aggressively against abusive ambulance billing practices.
