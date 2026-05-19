# South Carolina state pack

The fully-worked state-law layer for South Carolina patients. The LLM uses this when the patient's state is South Carolina. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md); neighboring North Carolina at [`laws_state_nc.md`](laws_state_nc.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Three things shape South Carolina's patient-side leverage, and one of them is a gap, not a strength:

1. The **South Carolina Unfair Trade Practices Act (SCUTPA), § 39-5-140**, gives consumers a private right of action with **mandatory attorney's fees on any violation** and **treble damages for willful violations**. SCUTPA reaches the hospital itself (not just third-party collectors). This is the headline SC lever in any provider-side billing dispute.
2. **South Carolina has no state surprise-billing statute and no state ground-ambulance protection.** Two successive "Stop Surprise Bills Act" bills (H185 in 2023-2024, H3302 in 2025-2026) have stalled. SC patients rely entirely on the federal No Surprises Act, which **does not cover ground ambulance**. This is the single biggest gap in SC patient protection.
3. **SC prohibits wage garnishment for medical debt** under § 37-5-104 of the Consumer Protection Code. Like North Carolina (and unlike Georgia), a creditor with a money judgment for a medical bill cannot reach the patient's wages — bank-account levy is available, but wage garnishment generally is not.

## Hospital itemization right

- **Statute (existing):** **No SC statute creates a stand-alone hospital itemized-billing duty as of 2026-05-18.** The user's prompt referenced § 44-7-3120 — that section number does not contain a Patient's Bill of Rights or itemization duty. The closest existing provisions are the **Lewis Blackman Hospital Patient Safety Act, § 44-7-3410 et seq.** (clinical-trainee identification, attending-physician disclosure — patient-safety, not billing), and the general regulatory standard at **DHEC Regulation 61-16** (hospital licensure minimum standards).
- **Statute (pending, do not cite as enacted):**
  - **H4622 (2023-2024 session)** proposed adding **S.C. Code § 44-7-327** ("Itemized billing"), with a January 1, 2025 compliance date. Passed the House 107-0 on April 9, 2024; died in Senate Committee on Medical Affairs at session end.
  - **H4069 (2025-2026 session, "Patient-Friendly Billing Act")** carries the same concept forward with a January 1, 2027 compliance date. As of 2026-05-18 the bill is in conference committee. Bill source: [scstatehouse.gov H4069](https://www.scstatehouse.gov/sess126_2025-2026/bills/4069.htm).
- **Source for the historical search:** [Justia Title 44, Chapter 7 index](https://law.justia.com/codes/south-carolina/title-44/chapter-7/); [scstatehouse.gov Title 44 Chapter 7](https://www.scstatehouse.gov/code/t44c007.php); [scstatehouse.gov H4622](https://www.scstatehouse.gov/sess125_2023-2024/bills/4622.htm); [DHEC R.61-16](https://www.dph.sc.gov/sites/scdph/files/media/document/R.61-16.pdf)
- **What an SC patient should do anyway:**
  - Send a written itemization request citing **federal Hospital Price Transparency Rule (45 CFR Part 180)** and **the IRS § 501(r) billing-and-collections requirement for non-profit hospitals** as the substantive floor. Both are documented in [`laws_federal.md`](laws_federal.md).
  - For non-profit hospitals, IRS § 501(r)(6) requires "reasonable efforts" to determine charity-care eligibility before "extraordinary collection actions," which includes confirming the bill is correct. A refusal to itemize undercuts the "reasonable efforts" defense.
  - **Crystallize a paper trail** by sending the request certified mail. If the provider later sues or refers to collections without itemizing, that paper trail supports a § 39-5-140 SCUTPA claim for unfair-or-deceptive billing practices (see below).
- **Private right of action:** No direct itemization statute means no direct private cause of action. SCUTPA at § 39-5-140 is the workhorse — see below.
- **ERISA:** Federal price-transparency rules are not preempted; they regulate the provider, not the plan.

## SCUTPA — South Carolina Unfair Trade Practices Act

- **Statutes:** **S.C. Code § 39-5-10 et seq.**; declaration of unlawfulness at **§ 39-5-20**; private cause of action at **§ 39-5-140**; surprise-billing UDAP designation at **§ 39-5-45** (pending — not enacted).
- **Sources:** [scstatehouse.gov Title 39 Chapter 5](https://www.scstatehouse.gov/code/t39c005.php); [§ 39-5-140 Justia](https://law.justia.com/codes/south-carolina/title-39/chapter-5/section-39-5-140/); [§ 39-5-10 Justia](https://law.justia.com/codes/south-carolina/title-39/chapter-5/section-39-5-10/)
- **Elements (consumer plaintiff):**
  1. An unfair or deceptive method, act, or practice;
  2. In the conduct of any trade or commerce;
  3. Resulting in an ascertainable loss of money or property;
  4. Public interest impact — the practice has the potential for repetition (controlling SC Supreme Court gloss from Daisy Outdoor Advert. Co. v. Abbott).
- **Why SC patients lead with this statute:**
  - **Mandatory attorney's fees** under § 39-5-140 — "upon the finding by the court of a violation of this article, the court shall award . . . reasonable attorney's fees and costs." Not discretionary.
  - **Treble damages** under § 39-5-140 for willful or knowing violations — "the court shall award three times the actual damages sustained."
  - **Reaches original creditors**, including hospital in-house billing departments — broader than federal FDCPA, which stops at third-party collectors.
  - Three-year statute of limitations (§ 39-5-150), aligning with the contract clock.
- **Common SCUTPA predicates in medical billing:**
  - Billing for services never rendered or upcoding (billing a higher CPT level than the documentation supports);
  - Misrepresenting in-network status;
  - Pursuing collection or credit reporting on a bill the provider cannot or will not itemize;
  - Threatening litigation or wage garnishment the creditor has no intent or legal basis to pursue (recall: SC bars wage garnishment for medical debt — see below);
  - Furnishing inaccurate medical-debt information to consumer reporting agencies.
- **"Public interest" requirement (SC-specific gotcha):** SC courts require the plaintiff to show the practice has impact beyond the individual transaction — "potential for repetition." Standard hospital billing practices applied across thousands of patients meet this easily; one-off clerical errors may not. Cite the provider's volume (revenue, admissions, system-wide billing department) in the demand letter.
- **No-class-action limit:** § 39-5-140 expressly bars representative-capacity actions. Individual SCUTPA suits only. Patients with similar grievances must file individually (no Rule 23 class).
- **ERISA preemption:** As applied to a self-funded ERISA plan's claim-handling, SCUTPA is preempted. For provider-side disputes, fully-insured plans, Medicaid managed care, individual/marketplace plans, the statute is in play.

## Unfair Claims Practices — § 38-59-20

- **Statute:** **S.C. Code § 38-59-20** ("Improper claim practices")
- **Source:** [Justia § 38-59-20](https://law.justia.com/codes/south-carolina/title-38/chapter-59/section-38-59-20/); [scstatehouse.gov Title 38 Chapter 59](https://www.scstatehouse.gov/code/t38c059.php)
- **Substance:** Prohibits insurers and accident-and-health, property, casualty, surety, marine, and title carriers from engaging in a defined list of improper claim practices "if committed without just cause and performed with such frequency as to indicate a general business practice." Includes misrepresenting policy provisions, failing to acknowledge claims promptly, failing to adopt and implement reasonable investigation/settlement standards, denying without reasonable investigation, and failing to attempt good-faith settlement once liability is reasonably clear.
- **Critical caveat — no private right of action:** **Masterclean, Inc. v. Star Ins. Co., 347 S.C. 405, 556 S.E.2d 371 (2001)** holds that § 38-59-20 does not create a private cause of action. Enforcement is by the Department of Insurance only.
- **Workaround that makes this statute matter anyway:** Cite § 38-59-20 violations as the substantive standard in a **SCUTPA § 39-5-140 complaint** (insurer's claim-handling can be SCUTPA-actionable if the public-interest element is met), and as evidence supporting a **common-law bad-faith claim under Nichols v. State Farm** (see below).
- **Practical use:** Reference § 38-59-20 in any complaint to the SC Department of Insurance Consumer Services Division. Do not plead it as a stand-alone count in litigation — SC courts dismiss those.

## Statutory remedy for bad-faith claim refusal — § 38-59-40

- **Statute:** **S.C. Code § 38-59-40** ("Liability for attorneys' fees where insurer has refused to pay claim")
- **Source:** [Justia § 38-59-40](https://law.justia.com/codes/south-carolina/title-38/chapter-59/section-38-59-40/)
- **Substance:** Where (1) a claim is covered by a policy of insurance or a non-profit hospital service plan / medical service corporation contract, (2) the insurer refuses to pay within **90 days after written demand**, and (3) a trial judge finds the refusal was **without reasonable cause or in bad faith**, the insurer is liable for the policyholder's reasonable attorney's fees in addition to the loss.
- **Fee cap:** Statutory fees capped at **one-third of the judgment**, set by the trial judge. Appeal carries an additional fee award if the judgment is affirmed.
- **"Reasonable cause" is a lower bar than common-law bad faith:** SC courts read § 38-59-40 to permit fee awards for **negligent** denials that lack reasonable cause, not just patent bad faith. This makes the statute easier to win than the Nichols common-law tort.
- **Coverage:** Any policy of insurance and non-profit hospital service plans (Blue Cross-style plans). First-party only.
- **ERISA preemption:** Preempted as applied to self-funded ERISA employer plans. Fully-insured plans, Medicaid managed care, individual/marketplace plans remain reachable.
- **Procedural requirements:**
  - Send the demand in writing by certified mail, identifying (i) the policy, (ii) the claim/loss, and (iii) the demand for payment.
  - Wait 90 days. Payment within 90 days defeats the fee claim. Payment after day 90 does not abate the claim.

## Common-law bad faith — Nichols v. State Farm

- **Authority:** **Nichols v. State Farm Mut. Auto. Ins. Co., 279 S.C. 336, 306 S.E.2d 616 (1983).** (Caveat: the user's prompt referenced "1996" — the case is 1983; subsequent cases refine but Nichols is the source.)
- **Source:** [Justia, Nichols v. State Farm (1983)](https://law.justia.com/cases/south-carolina/supreme-court/1983/21979-1.html); [Lawpipe summary](https://www.lawpipe.com/South-Carolina/Nichols_v_State_Farm_Mut_Auto_Ins_Co.html); [Property Insurance Coverage Law Blog overview](https://www.propertyinsurancecoveragelaw.com/blog/no-breach-of-contract-claim-does-not-preclude-bad-faith-cause-of-action-in-south-carolina/)
- **Elements:**
  1. The existence of a mutually binding insurance contract;
  2. The insurer's refusal to pay benefits due under the contract;
  3. The refusal was the result of bad faith or unreasonable action.
- **Damages:**
  - **Consequential (actual) damages** in tort, not limited by the contract cap (the patient can recover damages flowing from the wrongful denial, e.g., emotional distress, financial harm).
  - **Punitive damages** if the insurer's actions were **willful or in reckless disregard** of the insured's rights. Punitives are capped under **S.C. Code § 15-32-530** at the greater of three times compensatory damages or $500,000, with statutory exceptions for egregious conduct.
- **No requirement to win the breach of contract:** SC courts have held a bad-faith claim can survive even when the breach-of-contract claim fails, where the insurer's handling of the claim was independently unreasonable.
- **Bad-faith standard:** Higher than mere negligence. Plaintiff must show the denial was "unreasonable" — typically a denial without a reasonable basis for disputing coverage.
- **Statute of limitations:** Three years from the date the insured knew or should have known of the bad faith (§ 15-3-530), running from the denial itself in most cases. Watch this closely — Property Insurance Coverage Law Blog has documented multiple SC plaintiffs who lost on SoL grounds.
- **ERISA preemption:** Preempted as applied to self-funded ERISA plans; the federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) attorney's fees.

## Surprise billing — state law gap

- **There is no enacted SC state surprise-billing statute as of 2026-05-18.**
- **Pending bills (do not cite as enacted):**
  - **H185 (2023-2024 session, "Stop Surprise Bills Act")** would have added **S.C. Code § 38-71-292** prohibiting surprise billing and **§ 39-5-45** designating surprise billing as a per-se SCUTPA violation. Stalled in Senate Banking and Insurance Committee.
  - **H3302 (2025-2026 session, "Stop Surprise Bills")** carries the same concept forward. Status pending as of 2026-05-18.
- **Sources:** [scstatehouse.gov H185](https://www.scstatehouse.gov/sess125_2023-2024/bills/185.htm); [scstatehouse.gov H3302](https://www.scstatehouse.gov/sess126_2025-2026/bills/3302.htm); [SCDOI No Surprises Act page](https://doi.sc.gov/1001/No-Surprises-Act-Information)
- **Note on the user's prompt:** the prompt referenced § 38-71-880 — that section number does not contain a surprise-billing provision. The intended SC surprise-billing cite, when (if) enacted, would be **§ 38-71-292**.
- **What SC patients have instead:** the **federal No Surprises Act (Public Law 116-260, 45 CFR Parts 149)**, which covers emergency services, out-of-network ancillary services at in-network facilities, and **air ambulance** — but **not ground ambulance**, and not non-emergency OON services at OON facilities. See [`laws_federal.md`](laws_federal.md).
- **For SC patients on PPOs or out-of-area plans:** the federal NSA generally covers the same scenarios SC would have covered. The SC gap matters most for **ground ambulance** (no federal coverage, no SC coverage — see below).
- **ERISA:** federal NSA does reach self-funded ERISA plans for the categories it covers.

## Ground ambulance balance billing — unprotected gap

**SC has no enacted state-law protection for ground-ambulance balance billing as of 2026-05-18.** This is the single largest gap in SC patient protection compared to states like California, Maryland, New York, Ohio, and (since 2024) Georgia.

- The federal No Surprises Act **explicitly excludes ground ambulance**.
- Source: [Commonwealth Fund state ground-ambulance tracker](https://www.commonwealthfund.org/blog/2026/consumers-still-face-surprise-bills-ground-ambulances-states-are-trying-protect-them) shows SC as **not yet on the list** of states that closed the gap (22 states as of early 2026).
- **Bill 4113 (2023-2024)** created an EMS provider assessment fee program but **did not address patient-side balance-billing protection**. Source: [scstatehouse.gov H4113](https://www.scstatehouse.gov/sess125_2023-2024/bills/4113.htm).

Until the SC General Assembly closes this gap, an SC patient's leverage on a ground-ambulance bill is:

- **Negotiate directly with the EMS agency.** Most SC EMS is county-operated; political pressure via a county council member is sometimes effective.
- **File a SCUTPA § 39-5-140 complaint** if the EMS agency or its billing contractor uses unfair or deceptive collection practices (e.g., threats of wage garnishment that SC law prohibits — see below).
- **Apply for hospital charity care** if the ambulance bill is bundled with a hospital admission and the hospital has a § 501(r) FAP.

## Regulatory agencies

### South Carolina Department of Insurance (SCDOI), Consumer Services Division

- **Online complaint:** [doi.sc.gov/8/Consumers](https://doi.sc.gov/8/Consumers); NAIC portal at [online.doi.sc.gov/Eng/Public/Consumer/Consumer.aspx](https://online.doi.sc.gov/Eng/Public/Consumer/Consumer.aspx); PDF form at [doi.sc.gov DocumentCenter](https://doi.sc.gov/DocumentCenter/View/14594/Consumer-Complaint-Form-PDF-)
- **Phone:** main **(803) 737-6160**; Consumer Services **(803) 737-6180**; toll-free **1-800-768-3467**; Mon–Fri 8:30 a.m.–5:00 p.m.
- **Email:** [info@doi.sc.gov](mailto:info@doi.sc.gov)
- **Mail:**
  > South Carolina Department of Insurance
  > Consumer Services Division
  > P.O. Box 100105
  > Columbia, SC 29202-3105
  > (Physical: Capitol Center, 1201 Main Street, Suite 1000, Columbia, SC 29201)
- **Authority:** All insurance companies licensed in SC, including fully-insured health insurers, HMOs, PPOs, and Medicare supplement. Administers § 38-59-20 unfair claims practices and the federal No Surprises Act in SC. **No authority over self-funded ERISA plans** (route to DOL EBSA at **1-866-444-3272**). Does not regulate providers, hospitals, or original-creditor debt collectors — route those to SCDCA / SC AG.

### South Carolina Department of Consumer Affairs (SCDCA)

- **Online complaint:** [consumer.sc.gov/consumer-resources/consumer-complaints](https://consumer.sc.gov/consumer-resources/consumer-complaints); online filing at [applications.sc.gov/DCAComplaintSystem](https://applications.sc.gov/DCAComplaintSystem/Login/ConsumerLogin.aspx)
- **Phone:** toll-free in SC **1-800-922-1594**; local **(803) 734-4200**; Mon–Fri 8:30 a.m.–5:00 p.m.
- **Email:** [scdca@scconsumer.gov](mailto:scdca@scconsumer.gov)
- **Mail:**
  > South Carolina Department of Consumer Affairs
  > P.O. Box 5757
  > Columbia, SC 29250-5757
  > (Physical: 293 Greystone Blvd., Suite 400, Columbia, SC)
- **Authority:** **The primary individual-complaint agency in SC.** Administers the SC Consumer Protection Code (Title 37) and provides mediation services. Reaches providers, hospitals, debt collectors, and original creditors. SCDCA also enforces SC's licensing of consumer-finance lenders and debt collectors. Source: [SCDCA Divisions](https://consumer.sc.gov/about-us/scdca-divisions).

### South Carolina Attorney General, Consumer Protection and Antitrust Division

- **Website:** [scag.gov/inside-the-office/legal-services-division/consumer-protection-antitrust](https://www.scag.gov/inside-the-office/legal-services-division/consumer-protection-antitrust/)
- **Phone:** main **(803) 734-3970**
- **Mail:**
  > South Carolina Attorney General's Office
  > Consumer Protection and Antitrust Division
  > P.O. Box 11549
  > Columbia, SC 29211
- **Authority:** Enforces SCUTPA (§ 39-5-10 et seq.) and SC antitrust law on behalf of the state. **Does not handle individual consumer complaints** — those route to SCDCA. The AG's office investigates pattern-and-practice violations and brings parens patriae actions. Useful as a CC line in serious dispute letters to demonstrate the patient is aware of escalation paths.

## Small-claims court — Magistrate Court

- **Court name:** **Magistrates Court** (one or more per county; sometimes called "Summary Court" in local usage)
- **Jurisdictional limit:** **$7,500**, codified at **S.C. Code § 22-3-10**
- **Source:** [scstatehouse.gov Title 22 Chapter 3](https://www.scstatehouse.gov/code/t22c003.php); [SC Judicial Branch court fees](https://www.sccourts.org/courts/trial-courts/circuit-court/court-fees/); [Nolo SC small claims overview](https://www.nolo.com/legal-encyclopedia/south-carolina-small-claims-court-31724.html)
- **Filing fee:** **typically $80** for the initial summons-and-complaint, plus approximately **$10 per additional defendant**. County-by-county variation. Verify current fees with the local Clerk of Magistrates Court (county-specific surcharges apply). H4813 (2025-2026 session) proposes raising civil-filing assessments from $25 to $40 — not yet enacted; verify before filing.
- **Attorney rules:** **Permitted, not required.** Designed for pro se litigants — simplified pleadings, limited formal discovery, relaxed evidence rules. SC Magistrate Court generally **requires corporations to appear through a licensed attorney** for trial conduct (the unauthorized-practice-of-law rule under Renaissance Enters., Inc. v. Summit Teleservices, Inc., 334 S.C. 649, 515 S.E.2d 257 (1999)) — a procedural advantage SC patients share with NC, but not with GA.
- **Appeal:** Either party may appeal to the Court of Common Pleas for a trial de novo within **30 days of judgment** (S.C. Code § 18-7-10 et seq.).
- **Jury trial:** Available in Magistrate Court on demand at filing for civil cases up to $7,500. Demand within 5 days of service is the procedural requirement under S.C. Code § 22-3-1010 et seq.

## Statute of limitations

- **Most contracts (written or oral) and tort actions:** **3 years from breach or accrual** — **S.C. Code § 15-3-530(1)** ("an action upon a contract, obligation, or liability, express or implied")
- **Sealed instruments and mortgage-secured contracts:** **20 years** — **S.C. Code § 15-3-520** (rare; specific formal-seal requirements)
- **UCC § 2-725 sale-of-goods contracts:** 6 years — S.C. Code § 36-2-725 (rarely the right cite for hospital services; services contracts use § 15-3-530)
- **SCUTPA (§ 39-5-140) claims:** **3 years** — § 39-5-150
- **Sources:** [Justia § 15-3-530](https://law.justia.com/codes/south-carolina/title-15/chapter-3/section-15-3-530/); [scstatehouse.gov Title 15 Chapter 3](https://www.scstatehouse.gov/code/t15c003.php); [Parker Poe SoL summary](https://www.parkerpoe.com/webfiles/PLC%20-%20Statutes%20of%20Limitations_%20South%20Carolina.pdf)

SC's 3-year contract clock — reduced from 6 years in 1988 — is **shorter than most states** (GA is 6 written, FL is 5, TX is 4). This is a meaningful patient-side advantage when a hospital sits on a bill or sells it to a debt buyer. **Discovery rule applies:** the clock runs from when the injured party "discovered or should have discovered" the breach by reasonable diligence — not from the date payment was originally due. In medical-billing context, this typically means the date a disputed charge first appeared on a statement.

Most hospital admissions involve a signed financial-responsibility form. Even when signed, the form is a written contract under § 15-3-530, **not "under seal" under § 15-3-520** (20 years) unless it specifically recites and uses the formal seal language and indicia required by SC case law. **Hospital forms are virtually never "under seal" in the § 15-3-520 sense** — push back hard if a collector cites the 20-year limit.

Partial payment or a written acknowledgment of the debt can restart the clock under SC contract law. **Do not make a partial payment on a time-barred debt without legal advice.**

## Credit reporting

SC has **no enacted state-specific medical-debt credit-reporting restriction as of 2026-05-18.** Patients in SC rely on:

- The 2022-2023 voluntary changes by Equifax/Experian/TransUnion (paid medical debt removed; debt under $500 not reported; 1-year delay before reporting).
- Federal FCRA dispute rights (15 U.S.C. §§ 1681i, 1681s-2).
- The (vacated) CFPB 2025 medical-debt-on-credit-reports rule — a July 2025 federal court ruling held the CFPB exceeded its authority; medical debt remains reportable. Source: [SC Public Radio coverage](https://www.southcarolinapublicradio.org/2025-07-15/americans-medical-debt-can-stay-in-credit-reports-judge-rules-what-does-that-mean).

**Pending bills:** H4149 (2025-2026 session) would prohibit creditors, debt collectors, and consumer reporting agencies from reporting medical debt from SC medical facilities. As of 2026-05-18 the bill is in House Judiciary Committee. Source: [scstatehouse.gov H4149](https://www.scstatehouse.gov/sess126_2025-2026/bills/4149.htm). Do not cite as enacted.

**Federal preemption posture is in flux.** The CFPB issued an October 2025 interpretive rule taking the position that FCRA preempts state laws restricting medical-debt credit reporting. If that survives challenge, it limits the effect of any state-level law SC might eventually pass.

For deceptive furnishing of medical-debt information to credit bureaus, **SCUTPA § 39-5-140** can support a private claim against the furnisher, and the patient may have an independent federal FCRA claim under 15 U.S.C. § 1681s-2(b).

## Charity care

SC has **no state statute** requiring a hospital financial-assistance policy beyond federal law. Source: [Dollar For SC sheet](https://dollarfor.org/state_sheet/south-carolina/).

- **Non-profit hospitals** are bound by **IRS § 501(r)** (federal) — see [`laws_federal.md`](laws_federal.md). § 501(r)(4) requires a written FAP; § 501(r)(5) caps charges to FAP-eligible patients at the "amount generally billed" rate; § 501(r)(6) requires reasonable efforts to determine FAP eligibility before extraordinary collection actions.
- **For-profit hospitals** in SC have **no FAP mandate** at all.
- **SC Medically Indigent Assistance Program (MIAP), S.C. Code § 44-6-150 et seq.**, pays for services Medicaid would cover for SC citizens / lawful permanent residents at or below **200% of the federal poverty level**. Funded via county appropriations and the state. Source: [SCDHHS MIAP overview](https://msp.scdhhs.gov/managedcare/site-page/who-is-eligible-medicaid).
- Use [Dollar For](https://dollarfor.org/state_sheet/south-carolina/) for screening.

## Hospital lien statute

- **Statutes:** **S.C. Code §§ 44-127-10 through 44-127-60** ("South Carolina Health Care Lien Act"), enacted by Act 207 of 2002.
- **Note on the user's prompt:** the prompt referenced § 29-13-10 — that section number does not contain SC's hospital lien provision. The correct citation is **Title 44, Chapter 127**, not Title 29. Title 29 covers general mortgages and non-medical liens.
- **Sources:** [scstatehouse.gov Title 44](https://www.scstatehouse.gov/code/title44.php) (Chapter 127); [MWL Hospital Lien Laws (50-state chart)](https://www.mwl-law.com/wp-content/uploads/2019/09/HOSPITAL-LIEN-LAWS-IN-ALL-50-STATES-CHART-00215685x9EBBF.pdf); [Joye Law Firm SC lien overview](https://www.joyelawfirm.com/blog/how-long-do-i-have-to-pay-a-medical-lien-in-south-carolina/); [David W. Martin overview](https://www.davidwmartininjurylaw.com/how-to-handle-medical-liens-in-south-carolina-personal-injury-settlements/)
- **Substance:** Hospitals, chiropractors, physicians, dentists, nurses, and other licensed health care providers may file a lien **only against the patient's recovery from a third-party tortfeasor** (e.g., the at-fault driver in a car wreck). **Not a lien on the patient's home, wages, or bank accounts.**
- **Perfection requirements (§ 44-127-30):**
  - Provider must give **written notice within 90 days of commencement of services**, to:
    1. The patient — that any sum received from a third party is subject to the lien;
    2. The third party (if known) — that any settlement/judgment payment is subject to the lien;
    3. The third party's insurer or surety.
  - Notice must be served by certified mail with return receipt or by personal service.
- **MWL 50-state chart caveat:** The MWL chart historically labeled SC as "no statewide lien law," which **was correct before 2002**. Chapter 127 was enacted in 2002, so SC now has a statewide statute. If a collector or attorney cites the older "no SC hospital lien law" position, point them to Title 44 Chapter 127.
- **Enforcement:** A perfected lien may be enforced by action against the third party / insurer / patient. **Defective perfection is the single most common attack** — confirm the timely 90-day notice was served on all required parties.

## Wage garnishment — prohibited for medical debt

- **Statute:** **S.C. Code § 37-5-104** (Consumer Protection Code, Title 37)
- **Source:** [scstatehouse.gov Title 37 Chapter 5](https://www.scstatehouse.gov/code/t37c005.php); [Nolo SC garnishment overview](https://www.nolo.com/legal-encyclopedia/south-carolina-wage-garnishment-laws.html); [SC Legal Services wage-garnishment brochure](https://sclegal.org/brochures/wage-garnishment/)
- **Substance:** SC generally **prohibits wage garnishment for consumer debts**, including medical debt. § 37-5-104 bars garnishment of unpaid earnings for debts arising from consumer credit sales, consumer leases, consumer loans, and consumer rental-purchase agreements. SC case law and SCDCA guidance treat medical-bill debt as falling within this protection.
- **Limited exceptions (the only debts where wages can be garnished):**
  1. Money owed to the federal or state government (taxes, federally guaranteed student loans);
  2. Child support;
  3. Alimony;
  4. A garnishment order entered in another state while the consumer was a resident there, where the consumer later moved to SC.
- **Anti-retaliation:** **§ 37-5-106** prohibits an employer from firing an employee for an attempted consumer-debt garnishment.
- **What this means in practice:** A medical creditor with a money judgment cannot reach the patient's wages. **Bank-account levy is available**, but wage garnishment generally is not. A debt collector or hospital threatening wage garnishment on a medical bill is making a per-se misrepresentation, which is itself an actionable **SCUTPA § 39-5-140** violation.
- **Use:** In response letters to collectors threatening wage garnishment for a medical bill, cite § 37-5-104 and demand the collector identify the statutory exception authorizing garnishment. None usually exists, and the threat itself is a SCUTPA candidate.

## Quick reference for letter rendering

When the LLM renders a South Carolina-bound letter, substitute these defaults:

- **State headline statute (provider-side):** **S.C. Code § 39-5-140** (SCUTPA private right of action) with **mandatory attorney's fees** and **treble damages for willful violations**. This is the headline cite in every SC dispute letter to a provider, hospital, or original creditor. Add a one-line note about the public-interest / potential-for-repetition gloss.
- **State statute (itemization right):** **No SC statute requires hospital itemization on patient request as of 2026-05-18.** Use **federal Hospital Price Transparency (45 CFR Part 180)** and **IRS § 501(r)** as the substantive floor. Note that **H4069 (Patient-Friendly Billing Act)** is pending — verify enactment status before mailing if accuracy matters.
- **State insurance department (CC line):** South Carolina Department of Insurance, Consumer Services Division, P.O. Box 100105, Columbia, SC 29202-3105; toll-free **1-800-768-3467**
- **State consumer-affairs (CC line):** South Carolina Department of Consumer Affairs, P.O. Box 5757, Columbia, SC 29250-5757; toll-free **1-800-922-1594**
- **State AG consumer protection (CC line):** South Carolina Attorney General's Office, Consumer Protection and Antitrust Division, P.O. Box 11549, Columbia, SC 29211; main **(803) 734-3970**
- **Small-claims court name:** **Magistrates Court of [county]**
- **Filing fee (in 30-day warning):** "approximately $80 (S.C. Code § 8-21-1010; verify current schedule with the Clerk of Magistrates Court)"
- **Statute of limitations (in 30-day warning):** "S.C. Code § 15-3-530(1) (three years for breach of contract)" — and for SCUTPA claims, "§ 39-5-150 (three years)"
- **For insurer-side disputes:** lead with **§ 38-59-40** (statutory attorney's fees for 90-day refusal without reasonable cause) and add **common-law bad faith (Nichols v. State Farm, 1983)** for consequential and punitive damages. Cite **§ 38-59-20** as the substantive standard for the unfair-claim-practices argument, but do not plead § 38-59-20 as a stand-alone count.
- **For provider-side disputes:** lead with **§ 39-5-140 (SCUTPA)**. Add federal § 501(r) for non-profit hospitals and federal Hospital Price Transparency Rule (45 CFR Part 180) for any hospital.
- **For ground-ambulance bills:** acknowledge the gap — no SC state-law protection as of 2026-05-18; no federal NSA protection for ground ambulance. Use **§ 39-5-140 SCUTPA** against any unfair collection practices, and pursue charity care or county-level political pressure (most SC EMS is county-operated).
- **For threats of wage garnishment on medical debt:** cite **§ 37-5-104** and treat the threat itself as a **§ 39-5-140 SCUTPA** violation.
- **For hospital-lien situations (personal-injury settlements):** cite **S.C. Code §§ 44-127-10 through 44-127-60 (Health Care Lien Act)**; confirm the 90-day notice was served on all required parties — defective perfection invalidates the lien.

## Key South Carolina-specific advantages and gaps

Worth keeping in mind when triaging an SC patient's bills:

1. **SCUTPA § 39-5-140 with mandatory attorney's fees and treble damages for willful violations** — the headline SC lever. Fees are mandatory upon any finding of violation; trebling is mandatory upon willfulness. This is closer to NC § 75-1.1 (automatic trebling) than to GA FBPA (treble only for intentional violations).
2. **SCUTPA reaches original creditors** — the hospital's own billing department, not just outsourced collection vendors. Federal FDCPA reach stops at third-party collectors; SC closes that gap.
3. **No wage garnishment for medical debt** — § 37-5-104 prohibits it. A collector threatening wage garnishment on a medical bill is making a per-se SCUTPA-actionable misrepresentation.
4. **Three-year contract SoL** — short enough that aged debts and debt-buyer purchases frequently lose litigation leverage. Verify the discovery / breach date before responding to any "balance owed" demand more than three years old.
5. **§ 38-59-40 statutory attorney's fees** — easier to win than common-law bad faith. The "without reasonable cause" standard covers negligent denials, not just patent bad faith. Send the 90-day demand letter early.
6. **Magistrate Court corporate-appearance rule** — corporate defendants generally cannot self-represent at trial in SC Magistrate Court. This raises the economic friction on the corporate side and improves the pro se patient's leverage.
7. **Gap: No state itemization statute (yet).** Use federal price-transparency and § 501(r) as the floor; watch H4069 for enactment.
8. **Gap: No state surprise-billing protection.** Federal No Surprises Act is the only protection. Watch H3302.
9. **Gap: No state ground-ambulance protection.** This is the largest single hole. Use SCUTPA, county-level political pressure, and charity care.
10. **Gap: No state medical-debt credit-reporting law.** Watch H4149; until then rely on federal FCRA dispute rights and the (now-vacated) CFPB rule's general direction of travel.
11. **Hospital lien at Title 44 Chapter 127, not 29-13-10.** The pre-2002 "SC has no hospital lien statute" position is outdated — the Health Care Lien Act was enacted in 2002.
