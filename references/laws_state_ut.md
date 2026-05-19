# Utah state pack

The fully-worked state-law layer for Utah patients. The LLM uses this when the patient's state is Utah. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-19. Re-verify annually.

Three things make Utah's patient-side leverage distinctive:

1. **Hospital itemization is statutory** under Utah Code § 26B-2-219 — every Utah hospital must deliver an itemized statement, and a pre-EOB itemization must be conspicuously marked "DUPLICATE: DO NOT PAY." That marking requirement is a Utah-specific leverage point when collectors push pre-EOB invoices.
2. **A 45-day pre-collection notice is mandatory** under Utah's Healthcare Debt Collection Amendments (HB 128 / HB 204 line of bills, codified in Title 26B). No collection referral or credit-bureau report is lawful without it. Few patients know to demand proof.
3. **Ground-ambulance balance billing is prohibited by state law** as of May 7, 2025, via HB 301 — Utah closed the federal No Surprises Act's biggest gap with a fixed-fee schedule and a direct-pay mandate.

## Hospital itemization right

- **Statute:** **Utah Code § 26B-2-219** — "Requirement for hospitals to provide statements of itemized charges to patients" (recodified 2023; the previous citation was § 26-21-20 under the old Health Code).
- **Source:** [le.utah.gov/xcode/Title26B/Chapter2/26B-2-S219.html](https://le.utah.gov/xcode/Title26B/Chapter2/26B-2-S219.html); historical text at [law.justia.com/codes/utah/2022/title-26/chapter-21/part-1/section-20](https://law.justia.com/codes/utah/2022/title-26/chapter-21/part-1/section-20/); FindLaw mirror at [codes.findlaw.com/ut/title-26b-utah-health-and-human-services-codes/ut-code-sect-26b-2-219](https://codes.findlaw.com/ut/title-26b-utah-health-and-human-services-codes/ut-code-sect-26b-2-219/)
- **What it requires:**
  - A hospital **shall** provide a statement of itemized charges to any patient receiving medical care or other services.
  - Delivery is at the hospital's expense — in person, by mail, or by verifiable electronic delivery — **after** the hospital receives the EOB from the third-party payor reflecting the patient's remaining responsibility.
  - The statement must itemize each charge actually provided by the hospital and **may not** include charges of physicians who bill separately (physician services, anesthesia, radiology reads, etc., must be billed and itemized by those providers).
  - **Pre-EOB itemizations must be marked in bold**: "DUPLICATE: DO NOT PAY" (or equivalent). A pre-EOB statement without this marking is itself a Utah statutory violation.
- **Trigger:** Statutory duty runs by default once the EOB is received. The kit's standard written request is still useful — it crystallizes the dated paper trail and forecloses any claim the hospital was not on notice.
- **Scope:** All Utah-licensed hospitals (nonprofit, for-profit, government). Outpatient, ER-only, and ambulatory surgery centers are within "hospital" services for facilities licensed as hospitals; freestanding ASCs and physician offices are not covered by this section (general consumer-protection law still applies).
- **Enforcement:** Administrative, via the Utah Department of Health and Human Services licensing authority. No express private right of action under § 26B-2-219. Violations should be cited as evidentiary support in a Division of Consumer Protection complaint (UCSPA, § 13-11) and in a Utah Insurance Department complaint where the dispute touches the carrier.
- **ERISA:** Not preempted — regulates the provider, not the plan.

## Unfair Claim Settlement Practices Act

- **Statute:** **Utah Code § 31A-26-303** (and the broader Title 31A, Chapter 26, Part 3, Claim Practices)
- **Source:** [le.utah.gov/xcode/Title31A/Chapter26/31A-26-s303.html](https://le.utah.gov/xcode/Title31A/Chapter26/31A-26-s303.html); [law.justia.com/codes/utah/title-31a/chapter-26/part-3/section-303](https://law.justia.com/codes/utah/title-31a/chapter-26/part-3/section-303/); Utah Insurance Department summary at [insurance.utah.gov/consumers/legal-resources/unfair-claims](https://insurance.utah.gov/consumers/legal-resources/unfair-claims/)
- **Substance:** Prohibits insurers and their representatives from a defined list of unfair claim-settlement practices, including:
  - Knowingly misrepresenting material facts or policy provisions in connection with a claim.
  - Failing to acknowledge and act promptly on claim communications.
  - Failing to adopt reasonable standards for prompt investigation and processing of claims.
  - Compelling the insured to litigate by offering substantially less than the amount ultimately recovered.
  - Failing to provide a reasonable explanation for a denial or compromise offer.
  - Not attempting in good faith to effectuate prompt, fair, and equitable settlement when liability is reasonably clear.
- **Critical caveat:** **No private right of action.** Subsection (5) of § 31A-26-303 expressly disclaims any private cause of action; the Utah Supreme Court confirmed this in *Machan v. Unum Life Ins. Co. of Am.*, 2005 UT 37, 116 P.3d 342. Enforcement is by the Commissioner of Insurance only.
- **Use:** Cite UCSPA violations in your Utah Insurance Department complaint, and use them as **evidentiary support** for a common-law *Beck* breach-of-implied-covenant claim (below). Do not plead § 31A-26-303 as a standalone count in litigation.

## First-party bad-faith (common law)

- **Authority:** **Beck v. Farmers Insurance Exchange**, 701 P.2d 795 (Utah 1985)
- **Source:** [law.justia.com/cases/utah/supreme-court/1985/18926-0.html](https://law.justia.com/cases/utah/supreme-court/1985/18926-0.html); case brief at [quimbee.com/cases/beck-v-farmers-insurance-exchange](https://www.quimbee.com/cases/beck-v-farmers-insurance-exchange); secondary analysis [BYU JPL](https://digitalcommons.law.byu.edu/cgi/viewcontent.cgi?article=1271&context=jpl)
- **Substance:** In a first-party insurance relationship the insurer owes an implied covenant of good faith and fair dealing. Breach gives rise to a **cause of action in contract** (not tort) — meaning damages are limited to those reasonably foreseeable from the breach (the policy benefits, consequential damages flowing naturally from the breach, attorney's fees where contract or statute supplies them). The covenant requires the insurer to:
  - Diligently investigate the facts to determine claim validity.
  - Fairly evaluate the claim.
  - Promptly and reasonably reject or settle.
  - Deal with laymen as laymen, not as experts in underwriting subtleties.
  - Refrain from actions that injure the insured's ability to obtain policy benefits.
- **Damages posture:**
  - First-party: contract measure only. Utah does not recognize first-party insurance bad faith as a tort. No punitive damages for the bad-faith breach itself (though punitives may attach to a separate intentional-tort theory if the facts support it).
  - Third-party (e.g., liability carrier's failure to settle a claim against its insured within limits): tort measure, with full consequential and possibly punitive damages, under *Beck* and *Black v. Allstate Ins. Co.*, 2004 UT 66.
- **Use:** Plead breach of contract plus breach of the implied covenant of good faith and fair dealing against a Utah-regulated health insurer that has unreasonably delayed, denied, or low-balled a claim. Pair the complaint with documented UCSPA violations as evidence of unreasonableness.
- **ERISA preemption:** *Beck* claims are **preempted** as applied to self-funded ERISA employer plans (the standard *Pilot Life v. Dedeaux* analysis). Available against fully-insured plans, individual/marketplace plans, Medicaid managed care, and non-ERISA insurance.

## Surprise Billing — Health Care Cost Disclosure (HB 60, 2019)

- **Statute:** **Utah Code § 31A-22-650**, enacted by HB 60 (2019 General Session); related provisions at §§ 31A-22-651 through 31A-22-653 (emergency-service balance-billing report and rate framework).
- **Sources:** [le.utah.gov/xcode/Title31A/Chapter22/31A-22-S650.html](https://le.utah.gov/xcode/Title31A/Chapter22/31A-22-S650.html); Utah Insurance Department No Surprises Act page at [insurance.utah.gov/consumers/health-insurance/no-surprises-act](https://insurance.utah.gov/consumers/health-insurance/no-surprises-act/); University of Utah notice [doc.uhealthplan.utah.edu/notices/balance-billing.pdf](https://doc.uhealthplan.utah.edu/notices/balance-billing.pdf)
- **What it prohibits:**
  - Balance billing for **emergency services** rendered by an out-of-network provider or facility (patient cost-share capped at the in-network amount and counted toward in-network deductible and out-of-pocket maximum).
  - Balance billing for **non-emergency covered services performed by an out-of-network provider at an in-network facility** (ancillary services such as anesthesia, pathology, radiology, lab).
- **How patient cost-share is set:** at the in-network coinsurance/copay/deductible level. Rate disputes are between provider and payer.
- **Caveats:**
  - **ERISA preemption:** Does not reach self-funded ERISA employer plans. For those, federal NSA is the only protection.
  - Excludes workers' compensation, Medicare, Medicaid (each has its own scheme).
  - Does **not** cover ground ambulance — that gap was closed separately by HB 301 in 2025 (next section).
  - Federal No Surprises Act (Public Law 116-260) provides a parallel federal floor effective Jan 1, 2022; protections layer rather than displace.

## Ground-ambulance balance billing (HB 301, 2025)

- **Statute:** HB 301 (2025 General Session), Ambulance Provider Payment Amendments. Codified within Utah Code Title 31A (insurer obligations) and Title 26B (provider rate cap and EMS framework).
- **Effective:** **May 7, 2025**. **Sunset:** the ambulance reimbursement sections are set to repeal on July 1, 2027 (Legislature must reauthorize).
- **Sources:** Bill text [le.utah.gov/Session/2025/bills/introduced/HB0301.pdf](https://le.utah.gov/Session/2025/bills/introduced/HB0301.pdf); NFP regulatory summary [nfp.com/insights/utah-issues-various-healthcare-coverage-updates](https://www.nfp.com/insights/utah-issues-various-healthcare-coverage-updates/); BillTrack50 [billtrack50.com/billdetail/1799284](https://www.billtrack50.com/billdetail/1799284); EMS regulatory hub [ems.utah.gov/regulations/laws-rules-fees](https://ems.utah.gov/regulations/laws-rules-fees/)
- **What it requires:**
  - **Prohibits balance billing** for covered ground-ambulance transports — the patient owes only in-network cost-share.
  - Sets statutory base rates: **$1,234.92 (BLS/EMT), $1,630.31 (Advanced EMT), $2,383.73 (Paramedic/ALS)**, plus **$42.24 per loaded mile**, with annual adjustment.
  - Requires health plans (including out-of-network) and workers' compensation carriers to **directly accept claims from and pay ground-ambulance providers** at the statutory rates.
- **Significance:** The federal No Surprises Act **explicitly excludes ground ambulance**. Utah is now one of the (approximately fifteen) states that has closed that gap by statute. Until 2025 this was the single biggest balance-billing exposure for Utah patients.
- **Caveats:**
  - **ERISA preemption:** Self-funded ERISA employer plans are not bound by the rate cap or direct-pay mandate. For self-funded plans, the patient still has only federal-floor protections (which, for ground ambulance, are effectively none).
  - The sunset on July 1, 2027 is real — confirm enactment status before relying on HB 301 for any 2027+ date of service.
  - Air ambulance is federally preempted by the Airline Deregulation Act; the federal NSA covers air ambulance balance billing.

## Healthcare debt-collection notice requirement

- **Statute:** Utah's Healthcare Debt Collection Amendments (HB 128 / 2018; expanded by HB 204 / 2018), codified within Title 26B (recodified from Title 26 in 2023). The original 2017 HB 128 framework is at [le.utah.gov/~2017/bills/static/hb0128.html](https://le.utah.gov/~2017/bills/static/hb0128.html); HB 204 enrolled text at [le.utah.gov/~2018/bills/hbillenr/HB0204.htm](https://le.utah.gov/~2018/bills/hbillenr/HB0204.htm).
- **Substance:** A health-care provider **may not** refer a patient's unpaid bill to a collection agency or report it to a credit bureau without first delivering a statutory pre-collection notice. The notice must contain:
  - The nature and amount of the debt.
  - A warning that nonpayment may result in a collection-agency referral or a credit-bureau report and may negatively affect the patient's credit.
  - A due date that is **at least 45 days after the notice is sent** (60 days for Medicare beneficiaries) and **only after the insurer's time to determine its obligation has expired** without penalty.
- **Practical use:** When a Utah patient receives a collection letter or credit-report dispute, demand proof of the statutory pre-collection notice and the underlying EOB-adjudication date. Absence of either invalidates the referral and is grounds for an FCRA dispute against the furnisher and a Division of Consumer Protection complaint.
- **Secondary summary:** [healthipass.com/blog/utah-has-changed-the-law-with-patient-debt-collections-is-your-practice-ready](https://healthipass.com/blog/utah-has-changed-the-law-with-patient-debt-collections-is-your-practice-ready/); [askmuellerconsulting.com/utah-has-changed-the-law-for-patient-debt-collections](https://www.askmuellerconsulting.com/utah-has-changed-the-law-for-patient-debt-collections/)

## Regulatory agencies

### Utah Insurance Department (UID)

- **Online complaint portal:** [insurance.utah.gov/complaints](https://insurance.utah.gov/complaints/) (PDF cover sheet at [insurance.utah.gov/wp-content/uploads/UIDComplaintForm.pdf](https://insurance.utah.gov/wp-content/uploads/UIDComplaintForm.pdf))
- **Phone:** Salt Lake area **(801) 957-9200**; in-state toll-free **1-800-439-3805**. Health consumer line: **(801) 957-9280**.
- **Fax:** (385) 465-6047
- **Physical address:**
  > Utah Insurance Department
  > 4315 South 2700 West, Suite 2300
  > Taylorsville, UT 84129
- **Mailing address:**
  > Utah Insurance Department
  > ATTN: Consumer Services
  > P.O. Box 146901
  > Salt Lake City, UT 84114-6901
- **Authority:** All insurance companies licensed in Utah — fully-insured health insurers, HMOs, Medicare supplement, accident/health. Administers the UCSPA (§ 31A-26-303), the surprise-billing protections (§ 31A-22-650), and HB 301's ground-ambulance direct-pay mandate as applied to carriers. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and **does not regulate providers, hospitals, or debt collectors directly** (route to Division of Consumer Protection or AG).

### Utah Attorney General — Division of Consumer Protection (DCP)

- **Online complaint:** [services.dcp.utah.gov/s](https://services.dcp.utah.gov/s/); main site [consumerprotection.utah.gov](https://consumerprotection.utah.gov/)
- **Phone:** **(801) 530-6601**
- **Authority:** Enforces the **Utah Consumer Sales Practices Act, Utah Code Title 13, Chapter 11** (§ 13-11 et seq.), which is Utah's general UDAP statute. Reach over providers, hospitals, third-party debt collectors, and (importantly) **original creditors**.
- **Note on agency structure:** The Division of Consumer Protection sits within the Utah Department of Commerce administratively, but the Attorney General's Office holds parallel enforcement authority for UCSPA violations and is the litigating arm. Address consumer complaints to DCP; complex or pattern-and-practice matters can be cc'd to the AG's office.

### Utah Consumer Sales Practices Act (UCSPA) — private right of action

- **Statute:** **Utah Code § 13-11-19** (private actions by consumer); general prohibitions at § 13-11-4 (deceptive acts/practices) and § 13-11-5 (unconscionable acts/practices)
- **Source:** [law.justia.com/codes/utah/title-13/chapter-11/section-19](https://law.justia.com/codes/utah/title-13/chapter-11/section-19/); statute chapter at [le.utah.gov/xcode/Title13/Chapter11/13-11.html](https://le.utah.gov/xcode/Title13/Chapter11/13-11.html); practitioner summary [snjlegal.com](https://snjlegal.com/2023/05/23/the-utah-consumer-sales-practices-act-a-valuable-protection-for-consumers-against-unscrupulous-businesses/)
- **Substance:** A consumer who suffers loss from a violation may recover **actual damages or $2,000, whichever is greater**, plus court costs. Injunctive relief is available. **Reasonable attorney's fees** are recoverable by the prevailing party in many UCSPA actions (with a fee-shifting carve-out against consumers only where the claim was "groundless" — a high bar).
- **Statute of limitations:** Two years after the violation, or one year after termination of any enforcement-authority proceeding with respect to the violation, whichever is later (§ 13-11-19(8)).
- **Why it matters:** UCSPA reaches the hospital's in-house billing department as an "original creditor" and reaches the provider directly for misrepresentations on bills (phantom charges, upcoding, false claims of in-network status, deceptive collection tactics). This is the closest Utah analog to Georgia's FBPA § 10-1-399 — a true patient-side leverage statute with statutory damages and fee-shifting. The minimum $2,000 statutory damages floor is meaningful in small-claims posture.

## Small claims court — Utah Justice Court

- **Court name:** Small Claims Court (a docket within Utah's Justice Courts and, for matters exceeding the justice-court limit, within District Court)
- **Statute:** **Utah Code § 78A-8-102**
- **Jurisdictional limit:** **$20,000 inclusive of attorney's fees, exclusive of court costs and interest**, effective **January 1, 2025 through December 31, 2029** (raised from $15,000). After the sunset reverts to $15,000 absent reauthorization.
- **Source:** [le.utah.gov/xcode/Title78A/Chapter8/78A-8-S102.html](https://le.utah.gov/xcode/Title78A/Chapter8/78A-8-S102.html); rules at [legacy.utcourts.gov/rules/viewall.php?type=SRPE](https://legacy.utcourts.gov/rules/viewall.php?type=SRPE); self-help portal [utcourts.gov/en/self-help/case-categories/consumer/small-claims.html](https://www.utcourts.gov/en/self-help/case-categories/consumer/small-claims.html)
- **Filing fees:** Tiered by amount in controversy — approximately $60 ($0–$2,000), $80 ($2,001–$7,500), $185 ($7,501–$20,000), per the Utah Courts fee schedule. Confirm at the court before filing; fees adjust periodically.
- **Attorney rules:** A party may be self-represented, represented by an attorney admitted in Utah, represented by an employee, or — with the court's express approval — represented by any other person who is not compensated for the representation. **Attorneys are permitted but not required.** Procedures are informal; the Rules of Evidence are relaxed; no formal discovery as of right.
- **Jury:** No jury at the small-claims docket. Either party may **appeal de novo to the District Court within 30 days** under § 78A-8-106 and Utah R. Small Cl. P. 12; a jury is available there on the de novo trial.

**Update tracking:** The 2025 $20,000 limit (HB 326 / 2024) sunsets December 31, 2029. Use $20,000 in dispute letters for claims accruing 2025-2029; check enactment status before drafting if the matter falls near or after the sunset.

## Statute of limitations

- **Written contracts:** **6 years from breach** — **Utah Code § 78B-2-309(2)** ("an action may be brought within six years upon any contract, obligation, or liability founded upon an instrument in writing")
- **Oral contracts / open accounts:** **4 years from breach** — **Utah Code § 78B-2-307** (general four-year residual including obligations not founded upon a writing)
- **Sources:** [le.utah.gov/xcode/Title78B/Chapter2/78B-2-S309.html](https://le.utah.gov/xcode/Title78B/Chapter2/78B-2-S309.html); [law.justia.com/codes/utah/2010/title78b/78b-2-309.html](https://law.justia.com/codes/utah/2010/title78b/78b-2-309.html); debt-SOL summary [tryascend.com/statute-of-limitations/utah/debt](https://tryascend.com/statute-of-limitations/utah/debt)

Most Utah hospital admissions involve a signed financial-responsibility form — that's a written contract, so 6 years applies. Implied-in-fact arrangements without a signed agreement may be treated as oral or open-account (4 years). The clock runs from breach (typically the day payment was due and not made).

**Acknowledgment / partial payment:** Under § 78B-2-309 itself, the six-year period begins (or restarts) on the later of: (a) the day the debt arose, (b) the day the debtor makes a **written** acknowledgment of the debt or a written promise to pay, or (c) the day the debtor (or a third party) **makes a payment** on the debt. **Do not make a partial payment on a time-barred Utah medical debt without legal advice** — a single payment can restart the entire six-year clock.

## Hospital lien statute

- **Citations:** **Utah Code §§ 38-7-1 through 38-7-8**, the Hospital Lien Law
- **Sources:** Chapter index [le.utah.gov/xcode/Title38/Chapter7/38-7.html](https://le.utah.gov/xcode/Title38/Chapter7/38-7.html); § 38-7-1 [le.utah.gov/xcode/Title38/Chapter7/38-7-S1.html](https://le.utah.gov/xcode/Title38/Chapter7/38-7-S1.html); chapter PDF [le.utah.gov/xcode/Title38/Chapter7/C38-7_1800010118000101.pdf](https://le.utah.gov/xcode/Title38/Chapter7/C38-7_1800010118000101.pdf); annotated index [law.justia.com/codes/utah/title-38/chapter-7](https://law.justia.com/codes/utah/title-38/chapter-7/)
- **Substance:** A licensed hospital may file a lien for the reasonable value of services rendered to an injured person **against any cause of action the injured person has against a third party** whose negligence or wrongful act caused the injury. The lien attaches to the third-party recovery (judgment or settlement), **not to the patient's home, wages, or bank accounts**.
- **Perfection requirements (§ 38-7-2):**
  - File a verified written notice in the district court of the county where the hospital is located, containing an itemized statement of services and dates, the hospital's name and address, and the name of the alleged third-party tortfeasor.
  - Mail a copy by **certified mail, return receipt requested**, to the home office of any insurance carrier known to insure that tortfeasor against liability.
- **Penalties for noncompliance (§ 38-7-2.5):**
  - A hospital that fails to comply with the notice/filing requirements **forfeits any right to costs and attorney's fees** in lien enforcement.
  - **Willful refusal to release** a notice of lien or to record proper notice within **20 days** of receiving notice of noncompliance exposes the lien claimant to **$1,000 or treble damages, whichever is greater**, plus attorney's fees to the prevailing patient.
- **Use:** Always test perfection. Demand the file-stamped court copy and the certified-mail return receipt. A defective lien is unenforceable against the third-party recovery, and the $1,000/treble penalty is a real lever when the hospital sits on a defective lien after written notice.

## Hospital charity care

- **Statute:** **Utah Code § 26B-2-224** (formerly § 26-21-23 before the 2023 recodification) — every licensed hospital in Utah, **nonprofit or for-profit**, must maintain a charity-care program. Utah is stronger than federal law on this point because § 501(r) only binds nonprofits.
- **Sources:** Dollar For Utah state sheet [dollarfor.org/state_sheet/utah](https://dollarfor.org/state_sheet/utah/); commentary on nonprofit-hospital "gifts to the community" [d36oiwf74r1rap.cloudfront.net/wp-content/uploads/2024/02/Nonprofit-Hosp-PB-Jan2024.pdf](https://d36oiwf74r1rap.cloudfront.net/wp-content/uploads/2024/02/Nonprofit-Hosp-PB-Jan2024.pdf)
- **Nonprofit additional obligation:** Utah nonprofit hospitals must spend a minimum amount on community benefits ("gifts to the community"), defined to include indigent care, community education/services/research, medical discounts, donated time, and donated money. Failure threatens property-tax exemption.
- **Federal § 501(r) floor:** All nonprofit hospitals must publish an FAP, an emergency-care policy, and a plain-language summary; charge FAP-eligible patients no more than amounts generally billed (AGB); and abide by extraordinary-collection-action restrictions during a 240-day application window (typically 120 days for billing + 120 days for FAP application).
- **Practical use:** Apply within 240 days of the first post-discharge billing statement. Cite § 26B-2-224 alongside § 501(r) when contesting collection actions taken before the FAP eligibility determination is final.

## Wage garnishment

- **Statute:** **Utah Code §§ 70C-7-103** (wage-claim limitations in consumer-credit context) and the procedural rules at **URCP 64D** (writs of garnishment) and **§ 78B-5-505** (exemptions).
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a court judgment. Post-judgment, garnishment of disposable earnings is capped at the lesser of (a) 25% of disposable earnings for that pay period, or (b) the amount by which disposable earnings exceed 30× the federal minimum hourly wage — tracking the federal Consumer Credit Protection Act, 15 U.S.C. § 1673.
- **Use:** Cite in responses to collectors threatening garnishment without a judgment in hand. Demand the writ docket number and confirm via Utah XChange or the issuing court's clerk before paying.

## Credit reporting

Utah has not enacted a state-specific medical-debt credit-reporting **prohibition** of the type recently passed in Colorado, New York, or Illinois. Utah's lever is procedural rather than substantive: the HB 128 / HB 204 framework above bars credit-bureau reporting **without the statutory 45-day pre-collection notice**. Once that notice is properly given, ordinary FCRA rules apply.

Layered protections for a Utah patient:

- **HB 128 / HB 204 framework** (Utah, Title 26B): no credit-bureau report or collection referral without statutory notice and minimum 45-day window. Useful in FCRA § 1681i / § 1681s-2(b) disputes against furnishers.
- **2022-2023 voluntary CRA changes** (Equifax/Experian/TransUnion): paid medical debt removed; medical debt under $500 not reported; one-year delay before any medical debt is reported.
- **Federal FCRA** dispute rights (15 U.S.C. §§ 1681i, 1681s-2) — applicable in Utah courts.
- **UCSPA § 13-11** — deceptive furnishing or misrepresentation about a medical debt to a CRA is actionable as a deceptive practice with the statutory damages floor and fee shifting noted above.

**Federal preemption posture is in flux.** The CFPB issued an October 2025 interpretive rule asserting that the FCRA preempts state laws restricting medical-debt credit reporting; a federal court has vacated the CFPB's underlying 2024 medical-debt rule on FCRA-preemption grounds (see [bhfs.com/insight/federal-court-vacates-cfpbs-medical-debt-rule-finds-fcra-preempts-state-laws](https://www.bhfs.com/insight/federal-court-vacates-cfpbs-medical-debt-rule-finds-fcra-preempts-state-laws/)). Utah's procedural notice rule sits on cleaner ground than a substantive reporting ban because it regulates **provider conduct** (when and how to refer) rather than CRA reporting behavior directly, but the area is contested.

## Quick reference for letter rendering

When the LLM renders a Utah-bound letter, substitute these defaults:

- **State statute (itemization right):** **Utah Code § 26B-2-219**. Pre-EOB statements must be marked "DUPLICATE: DO NOT PAY." Cite the absence of that marking, or the failure to deliver a post-EOB itemization, as a Utah-specific statutory violation.
- **State UDAP (provider-side leverage):** **Utah Code § 13-11-19** — actual damages or $2,000 statutory minimum, plus attorney's fees and injunctive relief. Mention in any 30-day demand against a Utah provider for upcoding, phantom charges, or misrepresented in-network status.
- **Pre-collection notice posture:** Demand proof of the **45-day statutory pre-collection notice** (60 days for Medicare beneficiaries) under Utah's Healthcare Debt Collection Amendments (HB 128 / HB 204) and the underlying EOB-adjudication date. Absence of either is grounds for a DCP complaint and an FCRA dispute.
- **State insurance department (CC line):** Utah Insurance Department, Consumer Services, P.O. Box 146901, Salt Lake City, UT 84114-6901 — phone (801) 957-9200 / 1-800-439-3805.
- **State consumer-protection (CC line):** Utah Division of Consumer Protection, 160 East 300 South, 2nd Floor, Salt Lake City, UT 84111 — phone (801) 530-6601 (verify mailing address at [consumerprotection.utah.gov](https://consumerprotection.utah.gov/) before sending).
- **Small-claims court name:** **Justice Court of [city or precinct], Small Claims Division** (or **District Court Small Claims** above the justice-court limit).
- **Jurisdictional limit (in 30-day warning):** "$20,000 inclusive of attorney's fees (Utah Code § 78A-8-102, effective Jan. 1, 2025)".
- **Statute of limitations (in 30-day warning):** "Utah Code § 78B-2-309 (six years for breach of written contract)".
- **For ground-ambulance balance bills (DOS on or after May 7, 2025):** Cite HB 301 (2025), Ambulance Provider Payment Amendments — statutory fee schedule, direct-pay mandate, balance-billing prohibition. Highest-leverage Utah-specific cite when applicable.
- **For first-party insurer disputes:** Plead breach of contract + breach of the implied covenant of good faith and fair dealing under **Beck v. Farmers**, 701 P.2d 795 (Utah 1985), with documented § 31A-26-303 UCSPA violations as evidentiary support. Do **not** plead UCSPA as a standalone count.

## Key Utah-specific patient advantages

Worth keeping in mind when triaging a Utah patient's bills:

1. **45-day pre-collection notice rule** (HB 128 / HB 204) — Utah is one of only a handful of states (Delaware, Florida, Idaho, Nevada, Utah) with a statutory cooling-off period before any medical-debt collection referral or credit-bureau report. Demand proof of the notice and the underlying EOB-adjudication date. Most patients and many providers do not realize this is enforceable as written.
2. **Duplicate-billing marking requirement** (§ 26B-2-219) — pre-EOB itemizations must be marked "DUPLICATE: DO NOT PAY." Unmarked pre-EOB invoices are themselves a statutory violation, useful framing in a DCP complaint.
3. **UCSPA statutory damages and fee-shifting** (§ 13-11-19) — $2,000 minimum statutory damages and prevailing-party attorney's fees make UCSPA a credible litigation lever even on small dollar amounts. Closest Utah analog to Georgia's FBPA.
4. **Charity care applies to for-profit hospitals too** (§ 26B-2-224) — Utah requires every licensed hospital to maintain a charity-care program, broader than federal § 501(r) which binds only nonprofits.
5. **Ground-ambulance closure** (HB 301, eff. May 7, 2025) — closes the single biggest federal No Surprises Act gap. Sunset July 1, 2027; confirm before relying on for late-2027+ dates of service.
6. **Hospital lien penalty teeth** (§ 38-7-2.5) — willful refusal to release a defective lien exposes the hospital to **$1,000 or treble damages, whichever is greater**, plus attorney's fees. Patients rarely invoke this; it shifts negotiating posture sharply.
7. **Small-claims limit raised to $20,000** (effective Jan. 1, 2025 through Dec. 31, 2029) — covers the great majority of disputed medical bills without escalation to District Court. Informal procedures and no jury at the small-claims docket lower the cost and complexity of bringing a patient-side action.
