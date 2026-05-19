# Arizona state pack

The fully-worked state-law layer for Arizona patients. The LLM uses this when the patient's state is Arizona. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Three things make Arizona's patient-side leverage unusually strong:

1. **Proposition 209 (the Predatory Debt Collection Protection Act, 2022)** caps interest on medical debt at **3% per year**, dramatically raises the wage-garnishment exemption (to **90% of disposable earnings or 60× the highest applicable minimum wage**, whichever is greater), raises the homestead exemption to **$400,000**, and increases personal-property exemptions across the board. This is the most patient-favorable medical-debt reform package in any US state.
2. **Common-law first-party bad faith** has been recognized in Arizona since **Noble v. National American Life Insurance Co., 128 Ariz. 188, 624 P.2d 866 (1981)** — the patient/insured can sue the insurer directly for tort damages (including emotional distress and, in egregious cases, punitives) when the insurer denies a covered claim without a reasonable basis. Arizona is one of a small minority of states where a private cause of action also exists under the **Unfair Claim Settlement Practices Act** at common law per **Sparks v. Republic Nat'l Life Ins. Co., 132 Ariz. 529, 647 P.2d 1127 (1982)**.
3. **Attorneys are prohibited in Justice Court Small Claims Division** without the consent of both parties (A.R.S. § 22-517). The corporate creditor cannot bring a lawyer, which strongly favors a self-represented patient.

## Hospital itemization right

- **Statute:** **A.R.S. § 36-436.01** — itemized statement of charges for hospital services.
- **Source:** [law.justia.com/codes/arizona/title-36/section-36-436-01](https://law.justia.com/codes/arizona/2023/title-36/section-36-436-01/); azleg.gov at [azleg.gov/ars/36/00436-01.htm](https://www.azleg.gov/ars/36/00436-01.htm)
- **What it requires:**
  - On **written request** by the patient (or the patient's representative or third-party payor), a hospital must furnish an itemized statement of all charges within a reasonable time.
  - The statement must identify each service, supply, drug, and procedure and the amount charged for each.
- **Scope:** Hospitals licensed under A.R.S. Title 36, Chapter 4. The duty is **request-triggered**, unlike Georgia's automatic six-business-day rule. Always send the request in writing (email or certified mail) to crystallize the timeline.
- **Private right of action:** Not expressly created by § 36-436.01 itself. Enforcement is via the Arizona Department of Health Services (licensing complaint) and, in practice, via the **Arizona Consumer Fraud Act (A.R.S. § 44-1521 et seq.)** when the hospital's billing conduct is misleading or includes services not rendered. The Consumer Fraud Act has a private right of action recognized by **Sellinger v. Freeway Mobile Home Sales, 110 Ariz. 573, 521 P.2d 1119 (1974)**.
- **ERISA:** Not preempted — regulates the provider, not the plan.

## Unfair Claim Settlement Practices Act

- **Statute:** **A.R.S. § 20-461** (listed practices); enforcement at **A.R.S. § 20-456** (Director cease-and-desist); penalties at **§ 20-457**.
- **Source:** [law.justia.com/codes/arizona/title-20/section-20-461](https://law.justia.com/codes/arizona/2023/title-20/section-20-461/); azleg.gov at [azleg.gov/ars/20/00461.htm](https://www.azleg.gov/ars/20/00461.htm)
- **Substance:** Prohibits insurers from engaging in a defined list of unfair claims-settlement practices — misrepresenting policy provisions, failing to acknowledge or act reasonably promptly on claims, refusing to pay claims without conducting a reasonable investigation, failing to provide a prompt and reasonable explanation of the basis for denial, etc.
- **Private right of action — Arizona-specific posture:** Arizona is one of only a handful of states where the Supreme Court has recognized **a private cause of action under the UCSPA at common law**. **Sparks v. Republic National Life Insurance Co., 132 Ariz. 529, 647 P.2d 1127 (1982)** held that violations of A.R.S. § 20-461 are evidence of (and can ground) a common-law bad-faith action. Most states' UCSPAs expressly bar a private remedy (see e.g. Georgia's O.C.G.A. § 33-6-37). Arizona's does not.
- **Practical use:** Plead UCSPA violations as evidence supporting the common-law bad-faith count (Noble, below). Also file a complaint with DIFI — even where the private suit is the main lever, an open regulator file changes the insurer's posture quickly.
- **Caveat:** ERISA self-funded plans escape state-law bad-faith and UCSPA claims; remedy is 29 U.S.C. § 1132(a)(1)(B).

## Common-law first-party bad faith

- **Leading case:** **Noble v. National American Life Insurance Co., 128 Ariz. 188, 624 P.2d 866 (Ariz. 1981)** — recognized the tort of first-party bad faith. The insurer owes the insured a duty to act in good faith and deal fairly. Breach is a tort, not just a contract claim.
- **Standard:** Insurer must have a **reasonable basis** for denying or delaying payment. **Rawlings v. Apodaca, 151 Ariz. 149, 726 P.2d 565 (1986)** clarified the two-part test: (1) the insurer acted unreasonably, and (2) the insurer knew or recklessly disregarded that its conduct was unreasonable. Negligence is not enough; knowing/reckless disregard is required.
- **Damages:** Compensatory damages for the underlying loss, **emotional-distress damages**, consequential damages (e.g. credit harm from unpaid medical bills the insurer should have covered), and **punitive damages** where the insurer's conduct is shown by clear and convincing evidence to be aggravated, outrageous, or malicious (**Linthicum v. Nationwide Life Ins. Co., 150 Ariz. 326, 723 P.2d 675 (1986)**).
- **Why Arizona stands out:** Most states recognize first-party bad faith only by statute (with caps) or not at all. Arizona's recognition is common-law, broad, and patient-favorable. Combined with UCSPA evidence (per Sparks), the bad-faith count is one of the strongest leverage tools in the kit when the patient has a fully-insured health plan and a wrongly-denied claim.
- **ERISA preemption:** Preempted as to self-funded employer plans; available against fully-insured plans, Medicaid managed care (AHCCCS plans), individual marketplace plans, Medicare supplements, and Arizona-regulated short-term/limited-duration plans.

## Surprise Billing — Arizona Out-of-Network Claim Dispute Resolution

- **Statute:** **A.R.S. § 20-3111 et seq.** — Out-of-Network Claim Dispute Resolution.
- **Source:** [law.justia.com/codes/arizona/title-20/chapter-20/article-2](https://law.justia.com/codes/arizona/2023/title-20/chapter-20/article-2/); azleg.gov at [azleg.gov/arsDetail/?title=20](https://www.azleg.gov/arsDetail/?title=20); DIFI consumer page at [difi.az.gov/consumers/surprise-out-network-bills](https://difi.az.gov/consumers/surprise-out-network-bills)
- **What it does:** Establishes a state arbitration/mediation process for surprise out-of-network bills. A patient who receives a "surprise out-of-network bill" of **$1,000 or more** (after deductible, coinsurance, and copays) for services at an in-network facility or in an emergency may request a dispute-resolution conference with DIFI. The patient pays in-network cost-share; the provider and insurer fight over the balance through the state process.
- **Triggering events:**
  - Emergency services from an out-of-network provider or facility.
  - Non-emergency services at an in-network facility where the patient was not given timely written notice that ancillary providers (anesthesiology, pathology, radiology, etc.) were out-of-network and a chance to elect an in-network alternative.
- **Process:**
  - Patient files the dispute with DIFI. Informal teleconference within 30 days. If unresolved, arbitration follows.
  - The provider may not pursue collection during the dispute process; doing so is itself a violation.
- **Federal interaction:** The federal **No Surprises Act (45 C.F.R. Part 149)** layers on top. Arizona's process applies to fully-insured plans and self-pay arrangements where the parties consent; federal NSA covers ERISA self-funded plans and fills gaps Arizona's statute does not.
- **Caveats:** ERISA self-funded plans use the federal NSA federal IDR, not the Arizona process. **Ground ambulance is not covered** by either Arizona's statute or the federal NSA (see "Ground ambulance" below).

## Regulatory agencies

### Arizona Department of Insurance and Financial Institutions (DIFI)

- **Online complaint portal:** [difi.az.gov/consumers/file-complaint](https://difi.az.gov/consumers/file-complaint)
- **Phone:** main **(602) 364-3100**; toll-free in Arizona **(800) 325-2548**; consumer assistance **(602) 364-2499**
- **Mail:**
  > Arizona Department of Insurance and Financial Institutions
  > Consumer Affairs Division
  > 100 N. 15th Avenue, Suite 261
  > Phoenix, AZ 85007-2630
- **Authority:** Created in 2020 by merging the Department of Insurance with the Department of Financial Institutions. Regulates fully-insured health insurers, HMOs, PPOs, Medicare supplements, and the state surprise-billing dispute process. Administers A.R.S. § 20-461 UCSPA enforcement. **No authority over self-funded ERISA plans** (route to DOL EBSA at **1-866-444-3272**) and does not regulate providers, hospitals, or debt collectors (route to AG).

### Arizona Attorney General — Consumer Protection & Advocacy Section

- **Online complaint:** [azag.gov/complaints/consumer](https://www.azag.gov/complaints/consumer)
- **Phone:** Phoenix **(602) 542-5763**; Tucson **(520) 628-6504**; toll-free statewide **(800) 352-8431**
- **Mail:**
  > Office of the Arizona Attorney General
  > Consumer Protection & Advocacy Section
  > 2005 N. Central Avenue
  > Phoenix, AZ 85004
- **Authority — Arizona Consumer Fraud Act (A.R.S. § 44-1521 et seq.):** The Act prohibits any deceptive or unfair act or practice in connection with the sale or advertisement of merchandise (which includes services, per the statutory definition). Reaches **original creditors**, including hospitals and physician practices, not just third-party debt collectors. **Private right of action recognized at common law** (Sellinger v. Freeway Mobile Home Sales, 110 Ariz. 573 (1974)) with actual damages and, in willful cases, **punitive damages** and **attorney's fees** under A.R.S. § 12-341.01 (any contested contract action).
- **Why this matters:** This is the Arizona analog to Georgia's FBPA. A hospital that bills for services not rendered, upcodes, misrepresents in-network status, or threatens lawsuits without intent to sue is squarely within the Consumer Fraud Act. Use it as the primary count when the dispute is with the hospital's billing department, not the insurer.

## Small claims court — Justice Court Small Claims Division

- **Court name:** **Small Claims Division of the Justice Court** (each Justice Court precinct in Arizona has one)
- **Jurisdictional limit:** **$3,500**, codified at **A.R.S. § 22-503**
- **Sources:** [law.justia.com/codes/arizona/title-22/section-22-503](https://law.justia.com/codes/arizona/2023/title-22/section-22-503/); [azcourts.gov/selfservicecenter/Small-Claims](https://www.azcourts.gov/selfservicecenter/Small-Claims)
- **Filing fees:** typical 2024-2025 filing fee in Maricopa County is **$36-$38** for the small-claims complaint plus **$18-$20** per service; total around **$54-$58**. Other counties similar. Fee waiver/deferral available on demonstrated need (A.R.S. § 12-302).
- **Attorney rules — Arizona-specific advantage:** Under **A.R.S. § 22-512**, "no attorney at law nor any person other than the plaintiff and defendant shall take part in the conduct or defense of an action in the small claims division" without the consent of all parties. A corporate defendant may appear through a non-attorney officer or full-time employee. The hospital/collector cannot bring counsel unless the patient agrees — and a self-represented patient should never agree.
- **Jury trial:** Not available in Small Claims. Either party may instead file in the regular Justice Court civil division ($10,000 limit), where attorneys are permitted and a six-person jury is available on demand.
- **Appeal:** Small Claims judgments are **final and non-appealable** (A.R.S. § 22-519). Patients should weigh this carefully — but in a dispute that is likely to settle with a credible filing, the no-appeal rule strongly favors the side willing to file.

## Statute of limitations

- **Written contracts:** **6 years from breach** — A.R.S. § 12-548
- **Oral contracts:** **3 years from breach** — A.R.S. § 12-543(1)
- **Open accounts / stated and mutual accounts:** **3 years** — A.R.S. § 12-543(2)
- **Sources:** [law.justia.com/codes/arizona/title-12/section-12-548](https://law.justia.com/codes/arizona/2023/title-12/section-12-548/); [law.justia.com/codes/arizona/title-12/section-12-543](https://law.justia.com/codes/arizona/2023/title-12/section-12-543/)

Most hospital admissions involve a signed financial-responsibility form — a written contract, so the 6-year clock under § 12-548 applies. Implied-in-fact medical-billing arrangements without a signed agreement may be treated as open accounts or oral contracts (3 years). The clock runs from breach (typically the date payment was due and not paid), not from when damages are discovered.

**Acknowledgment / partial-payment rule:** A new promise in writing or a partial payment can restart the limitations period under common-law principles (Arizona follows the Restatement approach). **Do not make a partial payment on a time-barred debt without legal advice** — it can revive the obligation. Note also that Proposition 209's 3% interest cap (below) limits accrued interest going forward, but does **not** itself toll or extend the limitations clock.

## Ground ambulance balance-billing

**Not covered by Arizona state law.** Arizona's surprise-billing statute (A.R.S. § 20-3111 et seq.) does **not** include ground ambulance, and the federal **No Surprises Act explicitly excludes** ground ambulance.

This means an Arizona patient hit with a balance bill from an out-of-network ground ambulance has **no state or federal balance-billing protection**. Practical levers:

- Negotiate directly with the ambulance provider citing UCC § 2-305 (price-not-fixed → reasonable price).
- If the patient was unconscious or otherwise unable to consent, argue lack of agreement to the rate.
- Apply the patient's insurer's allowed amount and pay only the in-network cost-share, then dispute the balance under the Consumer Fraud Act if the provider refuses negotiation.
- For Medicare/Medicaid patients, the federal Balance Billing Protection rule applies — providers accepting assignment cannot balance-bill.

A federal advisory committee (Ground Ambulance and Patient Billing) recommended in 2023 that ground ambulance be brought under NSA-style protections. **No Arizona bill had passed as of this writing.** Track legislation each session.

## Medical-debt credit reporting and collection — Proposition 209 (2022)

Arizona voters passed **Proposition 209, the Predatory Debt Collection Protection Act**, in November 2022. The measure took effect December 5, 2022 and is the strongest patient-side debt-collection reform of any US state.

- **Codification:** Amendments to A.R.S. Title 12 (Chapter 11, Article 4 — exemptions) and A.R.S. § 44-1201 (interest).
- **Source:** ballot text at [apps.azsos.gov/election/2022/general/ballotmeasuretext/proposition-209.pdf](https://apps.azsos.gov/election/2022/general/ballotmeasuretext/I-04-2022.pdf); summary at [azag.gov/consumer/Proposition-209](https://www.azag.gov/consumer/Proposition-209)

### Interest rate cap on medical debt

- **Cap:** Interest on **medical debt** is capped at **3% per year** (down from 10% default for unwritten obligations under A.R.S. § 44-1201). Codified at A.R.S. § 44-1201(F).
- **Definition of medical debt:** Debt arising from the receipt of medical services, products, or devices, broadly defined. Includes hospital, physician, dental, pharmacy, ambulance, and lab debt.
- **Effect:** Hospitals and collectors charging post-judgment interest at 10% on medical debt are violating § 44-1201(F). Patients can challenge the interest portion of any judgment or balance.

### Wage garnishment

- **Pre-Prop 209:** 25% of disposable earnings.
- **Post-Prop 209:** **10% of disposable earnings**, or the amount by which weekly disposable earnings exceed **60× the highest applicable minimum wage** (whichever is **less**). Codified at A.R.S. § 33-1131.
- Practical effect: At Arizona's 2025 minimum wage of $14.35, the threshold floor is $861/week — earnings below that are entirely exempt from garnishment. This is the most generous wage-garnishment exemption in the US.

### Homestead exemption

- **Pre-Prop 209:** $150,000.
- **Post-Prop 209:** **$400,000**, adjusted annually for inflation. Codified at A.R.S. § 33-1101.

### Other exemption increases

- Motor vehicle exemption raised to **$15,000** (one vehicle) — A.R.S. § 33-1125(8)
- Household furniture/appliances exemption raised to **$15,000** — A.R.S. § 33-1123
- Bank-account exemption raised to **$5,000** — A.R.S. § 33-1126(A)(9)

### Litigation status

Proposition 209 survived a constitutional challenge in 2022-2023 (Arizona Creditors Bar Association v. State); the Arizona Supreme Court declined review. The Act is in full effect.

### Credit reporting

Arizona has no state-specific statute restricting medical-debt furnishing to credit bureaus beyond the federal FCRA (15 U.S.C. §§ 1681i, 1681s-2). Patients in Arizona rely on:

- The 2022-2023 voluntary changes by Equifax/Experian/TransUnion (paid medical debt removed; debt under $500 not reported; 1-year delay before reporting).
- The CFPB's 2025 final rule (status under federal preemption challenge as of this writing) prohibiting most medical debt on consumer credit reports.
- Federal FCRA dispute rights against the furnisher.

Where furnishing is **inaccurate** (wrong amount, wrong patient, dispute not noted), an Arizona patient can also assert an Arizona Consumer Fraud Act claim against the furnisher under § 44-1522.

## Hospital charity care

Arizona has **no state statute** requiring a hospital financial-assistance policy beyond federal law. Non-profit hospitals are bound by **IRS § 501(r)** (federal); for-profit and county/municipal hospitals have no state FAP mandate.

Two Arizona-specific add-ons:

- **AHCCCS (Arizona Medicaid)** uses presumptive eligibility at hospitals; many medical debts can be retroactively covered if the patient was AHCCCS-eligible at the time of service. Always screen for AHCCCS eligibility before treating any debt as final.
- Hospitals operating in Arizona's **Disproportionate Share Hospital (DSH)** pool receive supplemental funding tied to indigent-care obligations under A.R.S. § 36-2912; cite DSH participation in a dispute letter where applicable.

Use Dollar For at [dollarfor.org/state_sheet/arizona](https://dollarfor.org/state_sheet/arizona/) for screening and FAP-application generation.

## Hospital lien statute

- **Citations:** **A.R.S. §§ 33-931 through 33-938** — health care provider liens.
- **Sources:** [law.justia.com/codes/arizona/title-33/chapter-7/article-2](https://law.justia.com/codes/arizona/2023/title-33/chapter-7/article-2/); azleg.gov at [azleg.gov/arsDetail/?title=33](https://www.azleg.gov/arsDetail/?title=33)
- **Substance:** Hospitals, physicians, nurses, ambulance providers, and other licensed health care providers may file a lien for the **customary charges** for care provided to an injured patient, **only against the patient's cause of action against a third party** who caused the injury. **Not a lien on the patient's home, wages, or bank accounts.**
- **Perfection requirements:**
  - Record a verified statement of the lien in the office of the county recorder of the county where the services were rendered, within **30 days after the patient receives services** (A.R.S. § 33-932).
  - Send a copy by registered mail to the patient and each known person/insurer alleged to be liable (§ 33-932(B)).
- **"Customary charges" limit (Arizona-specific patient advantage):** A line of cases including **Abbott v. Banner Health Network, 239 Ariz. 409, 372 P.3d 933 (2016)** holds that for a patient covered by health insurance (including AHCCCS), the hospital must first bill the insurer at the contracted rate; the lien is limited to the contracted/customary charges, not the full chargemaster amount. Always confirm the insurer-first step was attempted and that the lien amount reflects allowed charges, not list prices.
- **Anti-balance-billing for AHCCCS patients:** Under federal Medicaid law and A.R.S. § 36-2903.01, AHCCCS patients cannot be balance-billed; a lien for the chargemaster amount against an AHCCCS patient's third-party recovery is improper.

## Quick reference for letter rendering

When the LLM renders an Arizona-bound letter, substitute these defaults:

- **State statute (itemization right):** **A.R.S. § 36-436.01** — written request triggers the hospital's duty to provide an itemized statement.
- **State insurance department (CC line):** Arizona Department of Insurance and Financial Institutions, Consumer Affairs Division, 100 N. 15th Avenue, Suite 261, Phoenix, AZ 85007-2630 ([difi.az.gov](https://difi.az.gov))
- **State AG consumer protection (CC line):** Office of the Arizona Attorney General, Consumer Protection & Advocacy Section, 2005 N. Central Avenue, Phoenix, AZ 85004 ([azag.gov/complaints/consumer](https://www.azag.gov/complaints/consumer))
- **Small-claims court name:** **Small Claims Division of the [precinct name] Justice Court, [county] County**
- **Small-claims jurisdictional limit:** **$3,500** (A.R.S. § 22-503)
- **Filing fee (in 30-day warning):** "approximately $54-$58 including service"
- **No-attorney advantage:** Reference A.R.S. § 22-512 — corporate creditor cannot bring counsel without patient's consent.
- **Statute of limitations (in 30-day warning):** "A.R.S. § 12-548 (six years for breach of written contract)" or "A.R.S. § 12-543 (three years for oral contract or open account)" as applicable.
- **Interest cap (in any letter discussing accrued interest):** "Interest on medical debt is capped at 3% per year under A.R.S. § 44-1201(F) (Proposition 209, eff. Dec. 5, 2022)."
- **Garnishment threat response:** "Under A.R.S. § 33-1131 (Proposition 209), wage garnishment is capped at 10% of disposable earnings, and earnings below 60× the highest applicable minimum wage are entirely exempt."
- **For insurer-side disputes (denials, slow-pay):** Cite **A.R.S. § 20-461** UCSPA violations and the **common-law bad-faith** count under **Noble v. National American Life Ins. Co., 128 Ariz. 188 (1981)** and **Rawlings v. Apodaca, 151 Ariz. 149 (1986)**, with **Sparks v. Republic Nat'l Life, 132 Ariz. 529 (1982)** confirming UCSPA violations as evidence of bad faith.
- **For provider-side disputes (vs. insurer-side):** Cite **A.R.S. § 44-1521 et seq.** Arizona Consumer Fraud Act with private right of action per **Sellinger v. Freeway Mobile Home Sales, 110 Ariz. 573 (1974)**, plus attorney's fees under A.R.S. § 12-341.01.

## Key Arizona-specific advantages

Worth keeping in mind when triaging an AZ patient's bills:

1. **Proposition 209 stack (2022)** — the single biggest patient-side debt-collection reform of any US state. The **3% interest cap on medical debt** alone can shave thousands off accrued balances on older debts. The **garnishment floor (60× minimum wage exempt)** makes most working-class patients judgment-proof in practice. The **$400,000 homestead** protects nearly any Arizona home from forced sale to satisfy a medical-debt judgment. Mention Prop 209 in every Arizona letter where interest or collection threats are at issue.
2. **Common-law bad-faith doctrine (Noble / Rawlings)** — Arizona's recognition of first-party bad faith as a tort, with emotional-distress and punitive exposure, is broader than most states' statutory regimes. The **Sparks v. Republic National Life** holding that UCSPA violations evidence bad faith gives the patient both a regulatory complaint route (DIFI) and a tort claim from the same insurer conduct.
3. **No attorneys in small claims (A.R.S. § 22-512)** — the corporate creditor cannot bring counsel without the patient's consent. The economic leverage in Justice Court small claims is therefore higher in Arizona than in most states, because the corporate side faces non-attorney representation in a tribunal designed for pro se litigants.
4. **Hospital-lien "customary charges" rule (Abbott v. Banner Health)** — the lien is limited to insurance-contracted/customary rates, not chargemaster amounts. Combined with AHCCCS anti-balance-billing protections, this neutralizes the most common hospital-lien overreach pattern (lien at full chargemaster against a third-party tort recovery).
5. **Arizona Consumer Fraud Act reach over original creditors** — the hospital's in-house billing department is squarely within § 44-1521 et seq., with private right of action, punitive damages on willful violations, and attorney's fees under § 12-341.01. This is the Arizona analog to Georgia's FBPA and is the right lead-count against deceptive billing by providers.
