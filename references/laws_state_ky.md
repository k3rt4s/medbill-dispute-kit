# Kentucky state pack

The fully-worked state-law layer for Kentucky patients. The LLM uses this when the patient's state is Kentucky. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md); Indiana at [`laws_state_in.md`](laws_state_in.md); Tennessee at [`laws_state_tn.md`](laws_state_tn.md). All citations verified against public sources as of 2026-05-19. Re-verify annually.

Three things make Kentucky's patient-side leverage distinctive:

1. **15-year statute of limitations on written contracts** under KRS 413.090(2) — one of the longest in the United States. A signed hospital financial-responsibility form keeps a claim alive for fifteen years from breach. This cuts both ways: the patient has a very long runway to sue on a billing dispute, and the hospital has a very long runway to collect, so the timing analysis in 30-day warning letters and in counsel to "wait it out" looks very different than in 4-to-6-year states.
2. **Third-party private right of action under the UCSPA** — State Farm Mutual Auto. Ins. Co. v. Reeder, 763 S.W.2d 116 (Ky. 1988), held that KRS 304.12-230 creates a private cause of action for **both first- and third-party** claimants. Kentucky is one of a small minority of states allowing third-party claimants (not just policyholders) to sue an insurer directly for unfair claims-settlement practices.
3. **Wittmer v. Jones unified bad-faith framework** — 864 S.W.2d 885 (Ky. 1993), gathered all bad-faith theories (common-law, statutory, first-party, third-party) under one three-element test, with punitive damages and consequential damages (including emotional distress) on the table.

Several other Kentucky features cut against the patient and are flagged below: **no hospital lien statute**, **no state surprise-billing statute** comparable to GA HB 888 or NY Article 49 (federal NSA is the operative protection), **no enacted ground-ambulance balance-billing protection** as of this writing, and a **$2,500 small-claims ceiling** — among the lowest in the country.

A note on user-provided cites:

- **KRS 216.2925 is not the itemization statute.** The Kentucky hospital-itemization right is at **KRS 216B.250** ("Health facility to furnish itemized statement of charges on request of paying patient"), in the Chapter 216B health-facility licensure subtitle.
- **KRS 134.300 is not the hospital lien statute** — that section was repealed in 2010 and pertained to tax bills, not medical liens. **Kentucky has no hospital lien statute at all.** Liens against personal-injury recoveries are obtained by contract/assignment, not by statutory lien filing. Section 12 below covers this.

## Hospital itemization right

- **Statute:** **KRS 216B.250** — "Health facility to furnish itemized statement of charges on request of paying patient"
- **Source:** [apps.legislature.ky.gov/law/statutes/statute.aspx?id=9240](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=9240); chapter index at [apps.legislature.ky.gov/law/statutes/chapter.aspx?id=38238](https://apps.legislature.ky.gov/law/statutes/chapter.aspx?id=38238); 2020 PDF copy at [statecodesfiles.justia.com/kentucky/2020/chapter-216b/section-216b-250/section-216b-250.pdf](https://statecodesfiles.justia.com/kentucky/2020/chapter-216b/section-216b-250/section-216b-250.pdf)
- **What it requires:**
  - On the **written request** of a paying patient (or the patient's representative), a licensed health facility must furnish an itemized statement of all charges for services rendered.
  - The duty is **request-triggered**, not automatic — contrast Georgia's automatic 6-business-day duty under O.C.G.A. § 10-1-393(b)(14). Send the request in writing by certified mail to crystallize the paper trail.
  - Statute was originally enacted in 1986 and last amended April 10, 1998. No specific response deadline is codified; a 30-day window per the federal price-transparency and Medicare CoP framework is the reasonable default, and the kit's standard 30-day warning aligns with this.
- **Scope:** All licensed health facilities under Chapter 216B (hospitals, nursing facilities, ambulatory surgical centers, etc.). Reaches inpatient, outpatient, and ER services.
- **Penalty:** Chapter 216B is enforced by the Cabinet for Health and Family Services through licensure proceedings. No express patient-side private cause of action under KRS 216B.250 itself; the leverage comes from layered (a) KCPA § 367.170/367.220 deceptive-practices theory if the refusal is part of a deceptive pattern, (b) federal § 501(r)(6) "amounts generally billed" verification, (c) 45 C.F.R. § 180 federal hospital price transparency, and (d) 42 C.F.R. § 482.13 Medicare Conditions of Participation.
- **ERISA:** Not preempted — regulates the provider, not the plan.

## Kentucky Consumer Protection Act (KCPA)

- **Statute:** **KRS 367.110 to 367.300** — prohibited acts enumerated at **§ 367.170**, private right of action at **§ 367.220**
- **Sources:** [apps.legislature.ky.gov/law/statutes/chapter.aspx?id=39092](https://apps.legislature.ky.gov/law/statutes/chapter.aspx?id=39092); private RoA at [apps.legislature.ky.gov/law/statutes/statute.aspx?id=34922](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=34922); definitions at [apps.legislature.ky.gov/law/statutes/statute.aspx?id=34907](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=34907); Attorney General resource page at [ag.ky.gov/Resources/Consumer-Resources/Consumers/resources/Pages/statutes.aspx](https://www.ag.ky.gov/Resources/Consumer-Resources/Consumers/resources/Pages/statutes.aspx)
- **Substance:** KRS 367.170 declares "unfair, false, misleading, or deceptive acts or practices in the conduct of any trade or commerce" unlawful. The Kentucky Supreme Court has applied this broadly to consumer transactions, including services and medical billing where the patient or guarantor is the purchaser.
- **Private right of action — § 367.220:** A person who purchases goods or services primarily for personal, family, or household purposes and suffers any **ascertainable loss of money or property** as a result of a § 367.170 violation may sue in Circuit Court for **actual damages**, equitable relief, and (at the court's discretion) **reasonable attorney's fees and costs**. Punitive damages are not foreclosed where the conduct supports them. See *Alexander v. S&M Motors, Inc.*, 28 S.W.3d 303 (Ky. 2000) (attorney-fee award is discretionary).
- **Reach over original creditors:** KCPA applies to suppliers directly, not just third-party debt collectors. The hospital's in-house billing department is reachable. Analogous to Georgia FBPA § 10-1-399 and Indiana DCSA § 24-5-0.5-4, though Kentucky's KCPA does **not** include a treble-damages multiplier — actual damages plus discretionary fees is the standard remedy.
- **No ante-litem demand requirement** as a precondition to suit. The kit's standard 30-day warning letter is recommended as best practice and as a cure opportunity, but it is not statutorily required.
- **AG enforcement:** The Kentucky Attorney General's Office of Consumer Protection may bring parallel action for injunctive relief, civil penalties, and restitution under §§ 367.190–367.200.

## Unfair Claims Settlement Practices Act (UCSPA)

- **Statute:** **KRS 304.12-230** — Kentucky's adoption of the NAIC model unfair-claims-settlement-practices act
- **Sources:** [apps.legislature.ky.gov/law/statutes/statute.aspx?id=17037](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=17037); commentary at [propertyinsurancecoveragelaw.com/blog/kentucky-unfair-claims-settlement-practices-act](https://www.propertyinsurancecoveragelaw.com/blog/kentucky-unfair-claims-settlement-practices-act/)
- **Substance:** Prohibits insurers from engaging in a defined list of unfair claims-settlement practices, including misrepresenting policy provisions, failing to acknowledge claims promptly, failing to adopt reasonable claim-investigation standards, refusing to pay without conducting a reasonable investigation, not attempting in good faith to effectuate prompt and fair settlement where liability is reasonably clear, compelling insureds to litigate by offering substantially less than amounts ultimately recovered.
- **Private right of action — *State Farm Mut. Auto. Ins. Co. v. Reeder*, 763 S.W.2d 116 (Ky. 1988):** The Kentucky Supreme Court held that KRS 304.12-230 creates a **private cause of action for both first-party and third-party claimants** against insurers. Although the statute does not expressly grant a private remedy and does prescribe Commissioner of Insurance enforcement, the court read the act to protect the class of injured claimants and refused to construe it as the Commissioner's exclusive province. Source: [law.justia.com/cases/kentucky/supreme-court/1988/88-sc-146-dg-1.html](https://law.justia.com/cases/kentucky/supreme-court/1988/88-sc-146-dg-1.html).
- **Why this is unusual:** Most NAIC-model states (including Georgia, Tennessee, Indiana) hold their UCSPA non-actionable as a private cause and route the patient to the regulator. Kentucky is in the **minority that allows direct private suit**, and is one of the very few that allows it for third-party claimants. This is a meaningful patient-side advantage when the dispute is with an insurer rather than the hospital.
- **Pair with bad-faith framework:** The UCSPA cause of action is governed in practice by the three-element *Wittmer v. Jones* test (see next section). The UCSPA enumeration provides the conduct catalog; *Wittmer* provides the standard for actionable bad faith.
- **ERISA preemption:** UCSPA-based claims against self-funded ERISA employer plans are generally preempted. For ERISA self-funded plans, the federal remedy is 29 U.S.C. § 1132(a)(1)(B) with possible § 1132(g) attorney's fees — no state UCSPA cause. The statute remains in play for fully-insured plans, Medicaid managed care, Medicare supplement, and individual/marketplace plans.

## Bad-faith failure to pay

- **Source case:** ***Wittmer v. Jones***, **864 S.W.2d 885 (Ky. 1993)** — Kentucky Supreme Court unified the bad-faith analysis across first-party, third-party, common-law, and statutory theories under a single three-element test
- **Source:** [law.justia.com/cases/kentucky/supreme-court/1993/92-sc-707-dg-1.html](https://law.justia.com/cases/kentucky/supreme-court/1993/92-sc-707-dg-1.html); modern application at [insurancecoveragenotesanddevelopments.com/supreme-court-of-kentucky-permits-third-party-bad-faith-claim-to-proceed-against-insurer-before-final-adjudication-of-coverage](https://www.insurancecoveragenotesanddevelopments.com/supreme-court-of-kentucky-permits-third-party-bad-faith-claim-to-proceed-against-insurer-before-final-adjudication-of-coverage/); see also *Belt v. Cincinnati Ins. Co.*, 642 S.W.3d 690 (Ky. 2022).
- **The three-element test:**
  1. The insurer must be **obligated to pay the claim** under the terms of the policy;
  2. The insurer must **lack a reasonable basis in law or fact** for denying the claim; and
  3. The insurer either **knew there was no reasonable basis** for denying the claim or **acted with reckless disregard** for whether such a basis existed.
- **Damages:**
  - **Contract damages** (the underlying loss the insurer should have paid).
  - **Consequential damages** flowing from the bad-faith conduct, including **emotional distress and mental anguish** — *Wittmer* expressly recognized these as recoverable.
  - **Punitive damages** are available in both first-party and third-party bad-faith cases under *Wittmer*. Standard: clear-and-convincing evidence of oppression, fraud, or malice (KRS 411.184/411.186). Kentucky does not statutorily cap punitive damages, though excessive-punitives constitutional scrutiny applies.
  - **Attorney's fees** are not automatically recoverable under *Wittmer* itself; recovery requires a separate fee-shifting basis (KCPA § 367.220(3) if pled in parallel, federal-question route via § 1132(g) for ERISA-eligible matters).
- **Coverage scope:** Reaches first-party claims (insured suing own insurer) and third-party claims (claimant suing an insurer for unfair settlement of a liability claim against the insured). Applies to fully-insured accident-and-sickness and health policies, individual/marketplace plans. **ERISA-preempted** for self-funded employer plans.
- **Practical posture:** Plead *Wittmer* bad faith as a count, **cite specific KRS 304.12-230 subsections as the conduct catalog** under the *Wittmer* framework, and file a parallel KY DOI complaint. This three-track posture (UCSPA private right + *Wittmer* tort + DOI complaint) is materially stronger than Georgia's (no common-law bad faith, no UCSPA private right) or Tennessee's (statutory bad faith only, no UCSPA private right).
- **The "tall burden":** Kentucky Court of Appeals decisions remind plaintiffs that *Wittmer* sets a high standard — a good-faith coverage dispute or honest mistake is not bad faith. The insurer's having a "fairly debatable" basis to deny defeats the claim.

## Surprise billing — federal NSA primary, Kentucky has no enacted analogue

Kentucky has **not** enacted a comprehensive state surprise-billing statute analogous to Georgia's O.C.G.A. § 33-20E-1 et seq. (Surprise Billing Consumer Protection Act), New York Article 49, Texas SB 1264, California AB 72, or Washington's Balance Billing Protection Act. The operative protection for Kentucky patients is the **federal No Surprises Act** (effective January 1, 2022). See [`laws_federal.md`](laws_federal.md).

- **Sources:** Kentucky Department of Insurance consumer bulletin at [insurance.ky.gov/ppc/Documents/nsa%20-%20consumer%20bulletin%2012-2021.pdf](https://insurance.ky.gov/ppc/Documents/nsa%20-%20consumer%20bulletin%2012-2021.pdf); Kentucky Voices for Health summary at [kyvoicesforhealth.org/the-no-surprises-act-what-kentuckians-should-know](https://kyvoicesforhealth.org/the-no-surprises-act-what-kentuckians-should-know/); UofL Health patient notice at [uoflhealth.org/patients-visitors/pay-my-bill/no-surprises-act-notice](https://uoflhealth.org/patients-visitors/pay-my-bill/no-surprises-act-notice/)
- **What this means in practice:**
  - Emergency services and ancillary out-of-network services at in-network facilities are covered by the federal NSA's hold-harmless rule for plans regulated under it (group health plans, individual market, marketplace, self-funded ERISA).
  - **Ground ambulance is not covered** by the federal NSA — and Kentucky has no enacted state-level closure (see next section).
  - State-regulated fully-insured plans remain subject to general KRS Chapter 304 prompt-pay and unfair-claims-practices rules, but no Kentucky balance-billing-prohibition statute applies on top of the NSA the way GA § 33-20E does.
- **Legislative history — incremental bills, none enacted as a comprehensive statute:**
  - SB 24 (2019) — "AN ACT relating to out-of-network balance billing." Defined balance-billing terms in KRS 304.17A-005, would have required insurer reimbursement at the lower of billed amount or U&C rate and prohibited downstream balance billing. Did not become law.
  - HB 179 (2020-2024 sessions, reintroduced multiple times) — surprise-billing framework with insurer claims-data reporting. Did not become law as enacted Kentucky statute.
- **DOI bulletins are the operative state-side guidance.** Kentucky DOI has issued bulletins and a consumer notice tracking the federal NSA. Where a fully-insured Kentucky plan declines to apply NSA protections, file a DOI complaint citing federal NSA preemption-of-floor authority plus KRS 304.12-230 (UCSPA) and *Wittmer*.

**Watch list:** HB 447 (2026 session) was introduced January 21, 2026 to provide a ground-ambulance balance-billing prohibition (effective January 1, 2027 if enacted) and was in House Banking & Insurance Committee as of late January 2026. Track its progress before relying on a state-law ground-ambulance cite.

## Ground-ambulance balance billing — no state protection as of this writing

- **Status:** Kentucky has **no enacted statute** prohibiting balance billing for ground ambulance. The federal NSA explicitly excludes ground ambulance (Public Health Service Act § 2799B-1 carve-out). For ground-ambulance bills in Kentucky, the patient has **no state-law hold-harmless protection** at the time of writing.
- **2025 attempt — HB 245 (2025 session):** Would have required health plans to cover emergency ground ambulance, set minimum allowable reimbursement at the lesser of the local rate or 400% of Medicare, and prohibited OON ground-ambulance providers from balance billing. **Died in committee on March 28, 2025.** Bill tracking at [billtrack50.com/billdetail/1818393](https://www.billtrack50.com/billdetail/1818393); session record at [apps.legislature.ky.gov/record/25rs/hb245.html](https://apps.legislature.ky.gov/record/25rs/hb245.html).
- **2026 attempt — HB 447 (2026 session):** Reintroduced with similar structure (400% Medicare reimbursement ceiling, balance-billing prohibition for OON ground ambulance, payment-in-full rule). Status as of late January 2026: **in House Banking & Insurance Committee**. If enacted, applies to plans issued or renewed on or after **January 1, 2027**. Bill PDF: [apps.legislature.ky.gov/recorddocuments/bill/26RS/hb447/orig_bill.pdf](https://apps.legislature.ky.gov/recorddocuments/bill/26RS/hb447/orig_bill.pdf); session record: [apps.legislature.ky.gov/record/26rs/hb447.html](https://apps.legislature.ky.gov/record/26rs/hb447.html); legiscan: [legiscan.com/KY/bill/HB447/2026](https://legiscan.com/KY/bill/HB447/2026).
- **Practical posture for current ground-ambulance disputes:**
  - Cite UCC § 2-305 (open-price reasonable-price defense — see [`laws_federal.md`](laws_federal.md)) and the Kentucky Consumer Protection Act § 367.170 for any deceptive/excessive billing pattern.
  - File a KY DOI complaint where the insurer's contribution toward an OON ambulance is the dispute (state-regulated fully-insured plans).
  - For self-funded ERISA plans, file with U.S. DOL EBSA (1-866-444-3272) since the state DOI has no jurisdiction.
  - Negotiate aggressively — Kentucky ambulance providers are not subject to a state-law cap, and the patient's leverage is documentary (Medicare rate comparison, hospital chargemaster, municipal ambulance rate if applicable).
- **Why this is the biggest Kentucky-specific gap:** Ground ambulance is the single largest source of unprotected surprise medical bills nationally. Kentucky is in the majority of states without a closure as of 2026-05; the planned 2027 effective date for HB 447 (if enacted) is the soonest realistic relief.

## Regulatory agencies

### Kentucky Department of Insurance (DOI) — Consumer Protection Division

- **Online complaint:** [insurance.ky.gov/ppc/new_default.aspx?divid=4](https://insurance.ky.gov/ppc/new_default.aspx?divid=4); form instructions at [insurance.ky.gov/ppc/Documents/KDOI_InstructionsConsumerComplaintForm071824.pdf](https://insurance.ky.gov/ppc/Documents/KDOI_InstructionsConsumerComplaintForm071824.pdf)
- **Phone:** toll-free in Kentucky **1-800-595-6053** (Option 1); direct **(502) 564-6034**
- **Email:** DOI.ConsumerComplaints@ky.gov
- **Mail:**
  > Kentucky Department of Insurance
  > Consumer Protection Division
  > 500 Mero Street, 2 SE 11
  > Frankfort, KY 40601
- **Authority:** Licensed insurers, HMOs, fully-insured accident-and-sickness plans, Medicare supplement, dental plans. Administers KRS 304.12-230 (UCSPA), prompt-pay rules, and the state's role in federal NSA enforcement. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and does not regulate providers, hospitals, or debt collectors (route to AG).

### Kentucky Attorney General — Office of Consumer Protection

- **Online complaint:** [ag.ky.gov/Resources/Consumer-Resources/Consumers/Pages/Consumer-Complaints.aspx](https://www.ag.ky.gov/Resources/Consumer-Resources/Consumers/Pages/Consumer-Complaints.aspx); direct form at [secure.kentucky.gov/formservices/AttorneyGeneral/ConsumerMediationForm](https://secure.kentucky.gov/formservices/AttorneyGeneral/ConsumerMediationForm)
- **Phone:** Consumer Protection Division **(502) 696-5389**; Louisville office **(502) 429-7134**
- **Mail:**
  > Office of the Attorney General
  > Office of Consumer Protection
  > 1024 Capital Center Drive, Suite 200
  > Frankfort, KY 40601
- **Authority:** Enforces the **Kentucky Consumer Protection Act (KRS 367.110 et seq.)** against suppliers, including hospitals' in-house billing departments, providers, and third-party debt collectors. Reach over **original creditors** — the gap not covered by DOI. Use when the dispute is with the hospital's billing office, not with an insurer's claim decision.

### Cabinet for Health and Family Services — Office of Inspector General (OIG), Health Care Access Branch

- **Charitable health-care registration:** [chfs.ky.gov/agencies/dph/dpqi/hcab/Pages/charitablehc.aspx](https://www.chfs.ky.gov/agencies/dph/dpqi/hcab/Pages/charitablehc.aspx)
- **Authority over:** facility-level licensure complaints against hospitals under Chapter 216B (including the itemization duty in KRS 216B.250). Route facility-licensure and patient-rights complaints here; bill-amount disputes go to AG/DOI.

## Small claims court — District Court small claims division

- **Court name:** **Small Claims Division of the District Court** (KRS 24A.230)
- **Jurisdictional limit:** **$2,500** exclusive of interest and costs, codified at **KRS 24A.230(1)**
- **Sources:** [apps.legislature.ky.gov/law/statutes/statute.aspx?id=39856](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=39856); handbook at [kycourts.gov/Legal-Help/Documents/P-6_Small_Claims_Handbook.pdf](https://www.kycourts.gov/Legal-Help/Documents/P-6_Small_Claims_Handbook.pdf); summary at [kyjustice.org/topics/court-basics/small-claims](https://www.kyjustice.org/topics/court-basics/small-claims); KRS 24A.270 filing-fee provision at [apps.legislature.ky.gov/law/statutes/statute.aspx?id=20715](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=20715)
- **Filing fees:** The small-claims filing fee equals the District Court fee for claims of $500 or less and varies modestly by county; expect roughly **$35-$60** as of 2025-2026 (verify with the local Circuit Court Clerk before filing). Indigent litigants may file an Affidavit of Substantial Hardship to defer or waive the fee.
- **Attorney rules:** Permitted, not required. Designed for pro se litigants — simplified pleadings, limited formal discovery, relaxed evidence rules.
- **Corporate appearance:** Kentucky's small-claims division does **not** have a Georgia-style express rule allowing non-attorney corporate appearance at any amount. Corporate defendants commonly appear through counsel, though pro se appearances by an officer or employee are permitted in practice and not categorically barred by statute or rule for the small-claims division. The hospital is more likely than not to send counsel, especially given the **$2,500 cap**, which by itself constrains the economic value of any single small-claims action.
- **Claims-per-year cap:** KRS 24A.250 limits any individual or entity to **25 small-claims filings per calendar year**. Not an issue for a single-patient dispute but worth knowing if multiple billing entities are involved.
- **Removal to plenary docket:** Either party may move to transfer to the regular District Court civil docket under KRS 24A.310. Corporate defendants seeking to deploy counsel and avoid the relaxed procedures sometimes do this.
- **Appeals:** De novo appeal to Circuit Court within **30 days**.

**Practical limitation:** The $2,500 cap is one of the lowest small-claims ceilings in the United States (Tennessee is at $25,000; Georgia at $15,000; Indiana at $10,000). For any medical bill above $2,500, the patient must file in the regular District Court civil docket (jurisdiction up to $5,000 per KRS 24A.120) or Circuit Court (above $5,000) — and the procedural simplifications of small-claims practice do not apply. Many medical billing disputes will exceed $2,500, so flag this early when triaging a Kentucky patient.

## Statute of limitations

- **Written contracts:** **15 years** from breach — **KRS 413.090(2)**
  - Source: [apps.legislature.ky.gov/law/statutes/statute.aspx?id=43545](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=43545)
  - **Important caveat — July 15, 2014 split:** The 15-year period applies to written contracts **executed before July 15, 2014**. For written contracts executed on or after July 15, 2014, the limitations period was reduced by KRS 413.160 (as amended by 2014 Ky. Acts ch. 99) to **10 years**. Confirm the date the financial-responsibility form was signed before relying on a 15-year vs. 10-year cite. Source: [findlaw.com/state/kentucky-law/kentucky-civil-statute-of-limitations-laws.html](https://www.findlaw.com/state/kentucky-law/kentucky-civil-statute-of-limitations-laws.html); practical-law overview at [grsm.com/Templates/media/files/pdf/Statutes%20of%20Limitations%20KY%203_25_2024.pdf](https://www.grsm.com/Templates/media/files/pdf/Statutes%20of%20Limitations%20KY%203_25_2024.pdf).
- **Oral contracts / open accounts:** **5 years** from breach — **KRS 413.120(1)**
- **Tort (general):** 1 year — KRS 413.140(1)(a)
- **KCPA actions:** subject to general contract or tort limitations depending on theory; KCPA itself does not specify a distinct period.

Most Kentucky hospital admissions involve a signed financial-responsibility form — a written contract — so **10 years (KRS 413.160) applies to post-2014 admissions** and **15 years (KRS 413.090(2)) applies to pre-2014 admissions**. Either way, Kentucky's window is materially longer than Georgia (6 written / 4 oral), Tennessee (6 contract), or Indiana (6 written/oral). The clock runs from breach (typically the day payment was due and not made), not from when damages are discovered.

**Tolling and revival:** Partial payment or written acknowledgment of the debt can restart the clock under common-law principles applied in Kentucky. **Do not make a partial payment on a time-barred medical debt without legal advice** — it can revive the limitations period entirely.

**Two-edged nature:** The long limitations period is patient-favorable in the sense that the patient retains more time to sue on a billing dispute, but it is provider-favorable in the sense that the hospital and its assignees retain a very long window to collect or sue. A patient sitting on a disputed bill in Kentucky cannot assume the clock will run out before they act.

## Credit reporting

Kentucky has **not** enacted a state-specific medical-debt credit-reporting restriction. Patients in Kentucky rely on:

- The **2022-2023 voluntary changes** by Equifax/Experian/TransUnion (paid medical debt removed; debt under $500 not reported; 1-year delay before reporting unpaid medical debt).
- **Federal FCRA dispute rights** (15 U.S.C. §§ 1681i, 1681s-2).
- **KCPA (KRS 367.170 / 367.220)** as a state UDAP overlay where furnishing inaccurate medical-debt information to bureaus is part of a deceptive pattern.

**Federal preemption posture is in flux.** A federal court in the Eastern District of Texas vacated the CFPB's 2025 medical-debt credit-reporting rule in July 2025, and the CFPB has since indicated it will not pursue a replacement. The October 2025 CFPB interpretive position on FCRA preemption of state restrictions adds further uncertainty. Re-verify the federal landscape annually. Source: [medicaldebtpolicyscorecard.org/state/KY](https://www.medicaldebtpolicyscorecard.org/state/KY); [library.nclc.org/article/latest-keeping-medical-debt-out-credit-reports](https://library.nclc.org/article/latest-keeping-medical-debt-out-credit-reports).

**Watch list:** HB 288 (2025 session) on interest-on-medical-debt is in the working-bill pile; not enacted as of this writing.

## Hospital charity care

- **Statutes:** **KRS 216.940 to 216.945** ("Kentucky Charitable Health Care Services Act") with companion provision at **KRS 304.40-075** (insurance code immunity for volunteer providers)
- **Sources:** Kentucky Charitable Health Care Services Program at [chfs.ky.gov/agencies/dph/dpqi/hcab/Pages/charitablehc.aspx](https://www.chfs.ky.gov/agencies/dph/dpqi/hcab/Pages/charitablehc.aspx); Dollar For state sheet at [dollarfor.org/state_sheet/kentucky](https://dollarfor.org/state_sheet/kentucky/); CHFS Charitable Health Care Services overview at [stateregstoday.com/health/healthcare/hospital-financial-assistance-and-charity-care-eligibility-in-kentucky](https://www.stateregstoday.com/health/healthcare/hospital-financial-assistance-and-charity-care-eligibility-in-kentucky)
- **Substance:** The KCHCSA principally provides for **registration of charitable health-care organizations and immunity for volunteer providers** rather than imposing an FAP-by-statute mandate on each hospital. Kentucky **is among the minority of states** (GA, KS, KY, MO, NM, OH, OK, PA, TN per the Kentucky Hospital Association) that extend charity-care expectations to hospitals receiving certain public-funding offsets.
- **State-specific patient-side protections beyond federal § 501(r):**
  - **240-day minimum application window** from the first post-discharge bill — Kentucky law sets this floor for non-profit hospital FAP applications, longer than the federal § 501(r) 240-day "extraordinary collection actions" notification period and providing a clear documentary anchor.
  - **120-day collection moratorium** — non-profit hospitals must wait at least 120 days after the initial post-discharge bill before selling the debt, reporting it to credit agencies, or pursuing legal action. This overlays the federal § 501(r) framework with a hard floor.
  - **No copayment for emergency services** — Kentucky prohibits hospitals from requiring a copay as a condition of providing emergency services. This is a meaningful patient-facing protection at the point of presentation.
- **What Kentucky law does *not* impose:**
  - No income-tier statutory schedule (federal § 501(r) defaults apply).
  - No state mandate of a specific FAP discount table (the hospital's own FAP, screened against AGB, is operative).
  - No statutory residency or citizenship eligibility floor — federal § 501(r) prohibits these as disqualifiers for emergency/medically necessary care.
- **Federal floor — IRS § 501(r)** (26 U.S.C. § 501(r), 26 C.F.R. § 1.501(r)-1 through -7): all non-profit Kentucky hospitals must have a published Financial Assistance Policy, may not charge FAP-eligible patients more than the "amounts generally billed" (AGB), and must make reasonable efforts to determine FAP eligibility before initiating extraordinary collection actions.
- **For-profit and county/municipal hospitals:** No federal § 501(r) coverage. State KCHCSA emergency-copayment prohibition still applies; other leverage is KCPA-deception theory and the hospital's own posted FAP if one exists.
- **Use Dollar For** at [dollarfor.org/state_sheet/kentucky](https://dollarfor.org/state_sheet/kentucky/) for screening.

## Hospital lien — **Kentucky has no hospital lien statute**

- **Status:** Kentucky is one of the small minority of US states **without a statutory hospital lien**. Florida, Kentucky, Michigan, Mississippi (statute repealed 1989), Ohio, Pennsylvania, South Carolina, West Virginia, and Wyoming share this characteristic per the MWL 50-state survey ([mwl-law.com/wp-content/uploads/2019/09/HOSPITAL-LIEN-LAWS-IN-ALL-50-STATES-CHART-00215685x9EBBF.pdf](https://www.mwl-law.com/wp-content/uploads/2019/09/HOSPITAL-LIEN-LAWS-IN-ALL-50-STATES-CHART-00215685x9EBBF.pdf)).
- **The user-provided cite KRS 134.300 is wrong** — KRS 134.300 (now repealed by 2009 Ky. Acts ch. 10, § 100, effective January 1, 2010) addressed tax-collection compensation, not hospital liens. The repeal is well-documented and the section has no successor.
- **How hospital "liens" work in Kentucky in practice:**
  - **Contractual assignment / letter of protection:** Most Kentucky personal-injury patients enter a written assignment of personal-injury settlement proceeds to the treating hospital as part of admission or treatment paperwork. This is contractual, not statutory; the hospital's enforcement remedy is breach-of-contract, not lien foreclosure.
  - **Subrogation under the patient's health-insurance policy:** Where a health insurer paid the bill, the insurer holds subrogation rights against any third-party tortfeasor recovery per the patient's policy.
  - **Judgment creditor status:** A hospital that obtains a judgment can pursue post-judgment collection (garnishment, judgment lien on real property under KRS 426.720) like any other judgment creditor. This is **not a "hospital lien"** in the statutory sense; it requires the hospital to first sue and win on the underlying bill.
- **What this means for the patient:**
  - A purported "hospital lien" filed without a contractual assignment, a judgment, or a recorded subrogation interest **lacks statutory authority in Kentucky** and is not enforceable as a lien on personal-injury proceeds, real property, wages, or bank accounts.
  - Demand the hospital identify the legal basis for any asserted lien (specific contract clause, specific judgment, specific KRS section). The hospital cannot point to a Kentucky hospital-lien statute, so the basis must be contractual or judgment-based.
  - This is **patient-favorable**: the absence of a hospital-lien statute means the hospital cannot file a one-sided notice and burden the patient's personal-injury recovery the way it could in Georgia, Indiana, Tennessee, or most other states.
- **Comparison:** Georgia (O.C.G.A. § 44-14-470 et seq.) and Indiana (IC 32-33-4) both have hospital-lien statutes that allow a hospital to file a verified statement after providing notice and capture a lien on the patient's personal-injury cause of action. Kentucky has no analogue; the hospital must sue on contract.

## Wage garnishment

- **Statute:** **KRS 427.010** (exemptions) read with **KRS 425.501–425.506** (garnishment procedure)
- **Sources:** [apps.legislature.ky.gov/law/statutes/statute.aspx?id=46624](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=46624); [apps.legislature.ky.gov/law/statutes/statute.aspx?id=18417](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=18417); summary at [nolo.com/legal-encyclopedia/kentucky-wage-garnishment-laws.html](https://www.nolo.com/legal-encyclopedia/kentucky-wage-garnishment-laws.html)
- **Substance:** Medical-bill creditors cannot garnish wages without **first obtaining a court judgment**. Post-judgment, garnishment is capped at the federal CCPA limit — the lesser of (i) 25% of disposable earnings or (ii) the amount by which weekly disposable earnings exceed 30× the federal minimum wage (15 U.S.C. § 1673). Kentucky has not enacted a more protective state-level cap.
- **Doctrine of necessaries:** Kentucky recognizes the common-law doctrine that one spouse may be liable for the other spouse's "necessary" medical care. Pre-judgment exposure remains contractual unless both spouses signed the financial-responsibility form.
- **Use:** In response letters to collectors threatening garnishment **without a judgment in hand** — the threat itself is a deceptive-collection-practices issue under federal FDCPA (third-party collectors) and the KCPA (original creditors).

## Quick reference for letter rendering

When the LLM renders a Kentucky-bound letter, substitute these defaults:

- **State statute (itemization request):** **KRS 216B.250** — written request required, no codified response deadline (use kit-standard 30 days). Cite federal § 501(r), 45 C.F.R. § 180, and 42 C.F.R. § 482.13 as overlay authority.
- **State statute (provider-side primary lever):** **KRS 367.170 (KCPA prohibited acts) + KRS 367.220 (private right of action with discretionary attorney's fees)**. Kentucky's analogue to GA FBPA / IN DCSA. Reaches the hospital's in-house billing department, not just third-party collectors. No treble-damages multiplier — actual damages plus discretionary fees.
- **State statute (insurer-side primary lever):** **KRS 304.12-230 (UCSPA, private right of action per *State Farm v. Reeder*)** paired with **a common-law bad-faith count under *Wittmer v. Jones*** (three-element test, punitive damages and emotional-distress damages on the table).
- **State insurance department (CC line):** Kentucky Department of Insurance, Consumer Protection Division, 500 Mero Street, 2 SE 11, Frankfort, KY 40601 (DOI.ConsumerComplaints@ky.gov; 1-800-595-6053)
- **State AG consumer protection (CC line):** Office of the Attorney General, Office of Consumer Protection, 1024 Capital Center Drive, Suite 200, Frankfort, KY 40601 ([secure.kentucky.gov/formservices/AttorneyGeneral/ConsumerMediationForm](https://secure.kentucky.gov/formservices/AttorneyGeneral/ConsumerMediationForm); 502-696-5389)
- **Small-claims court name:** **Small Claims Division of the [County] District Court**
- **Small-claims jurisdictional ceiling (in 30-day warning):** "$2,500 under KRS 24A.230" — bills above this go to regular District Court (up to $5,000) or Circuit Court (above $5,000)
- **Filing fee (in 30-day warning):** "approximately $35-$60 depending on county"
- **Statute of limitations (in 30-day warning, post-2014 admissions):** "KRS 413.160 (ten years for written contracts executed on or after July 15, 2014)"
- **Statute of limitations (pre-2014 admissions):** "KRS 413.090(2) (fifteen years for written contracts executed before July 15, 2014)"
- **For surprise-billing scenarios:** Cite the **federal No Surprises Act** — Kentucky has no enacted state-level statute on top of it. For state-regulated fully-insured plans, layer KRS 304.12-230 (UCSPA) + DOI complaint.
- **For ground-ambulance bills:** No state-law balance-billing protection. Negotiate under UCC § 2-305 (reasonable price) and KCPA § 367.170 (deception). Track HB 447 (2026 session, effective Jan 1, 2027 if enacted) for future cases.
- **For asserted "hospital liens":** Demand the legal basis. Kentucky has **no hospital lien statute** (KRS 134.300 was repealed in 2010 and was never a hospital-lien provision). Any purported lien must rest on a written assignment, a recorded judgment, or a recorded subrogation right.

## Key Kentucky-specific advantages

Worth keeping in mind when triaging a Kentucky patient's bills:

1. **15-year (pre-2014) / 10-year (post-2014) SOL on written contracts** — among the longest in the United States. Provides a very long runway to sue on a billing dispute. **Two-edged** — also gives the hospital a long collection runway, so do not assume the clock will run out.
2. **UCSPA private right of action per *State Farm v. Reeder*** — Kentucky is one of the very few states that recognizes a private cause of action under its UCSPA, and one of the even fewer that extends it to **third-party claimants**. This is materially stronger than the regulator-only posture in Georgia (§ 33-6-37), Tennessee, Indiana, and most NAIC-model states.
3. ***Wittmer v. Jones* unified bad-faith framework with punitive damages and emotional-distress damages** — first-party and third-party, common-law and statutory, all under one three-element test. Punitive damages and consequential damages (emotional distress, mental anguish) are recoverable on appropriate facts.
4. **KCPA reach over original creditors with discretionary attorney's-fee shifting** — KRS 367.220(3) puts fee recovery in the patient's reach against the hospital directly, not just against third-party debt collectors.
5. **No hospital lien statute** — patient-favorable structurally. A purported "hospital lien" in Kentucky must rest on contract, judgment, or subrogation; there is no one-sided statutory filing mechanism.
6. **Kentucky-specific charity-care minimums** — 240-day application window, 120-day collection moratorium, and emergency-copay prohibition layered on top of federal § 501(r). The 240-day window is the longest application floor in any state we track.

## Kentucky-specific weaknesses to flag

1. **$2,500 small-claims ceiling** — one of the lowest in the US (TN $25,000, GA $15,000, IN $10,000). Most medical billing disputes will exceed this and have to proceed in the regular District Court civil docket or Circuit Court, losing the procedural simplifications of small-claims practice.
2. **No state surprise-billing statute** — federal NSA is the sole protection for emergency and OON-at-INN ancillary scenarios. No GA-style § 33-20E or NY-style Article 49 overlay.
3. **No state ground-ambulance protection** — federal NSA's biggest gap is not closed in Kentucky. HB 245 died March 28, 2025; HB 447 (2026 session) is in committee with a January 1, 2027 effective date if enacted. Until then, ground-ambulance balance bills have no state-law floor.
4. **No state medical-debt credit-reporting restriction** — Kentucky relies entirely on the federal FCRA framework and voluntary bureau changes.
5. **KCPA lacks a treble-damages multiplier** — actual damages plus discretionary attorney's fees only. Less leverage on the supplier side than Georgia FBPA's treble-damages provision for intentional violations or Indiana DCSA's treble-damages or $1,000 minimum.
6. **No automatic hospital itemization duty** — KRS 216B.250 is request-triggered, not automatic like Georgia's 6-business-day rule. Patient must affirmatively request in writing.
