# Oregon state pack

The fully-worked state-law layer for Oregon patients. The LLM uses this when the patient's state is Oregon. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md), Tennessee at [`laws_state_tn.md`](laws_state_tn.md). All citations verified against public sources as of 2026-05-19. Re-verify annually.

Two things make Oregon's patient-side leverage unusually strong:

1. **Moody v. Oregon Community Credit Union** (2023) opened a negligence-per-se path against insurers for violations of the Unfair Claim Settlement Practices Act (ORS 746.230), reversing four decades of read-only enforcement. Combined with the Oregon Unlawful Trade Practices Act's robust private right of action, this gives Oregon patients two of the strongest extra-contractual levers on the West Coast.
2. **Oregon's hospital financial assistance regime (ORS 442.601 et seq., HB 3076 and HB 3320)** is one of the few in the country to require **presumptive eligibility screening before any bill over $500 is sent**, with a statutory four-tier income sliding scale (100% / 75% / 50% / 25% off) up to 400% of the federal poverty level. It also caps interest on patient medical debt at the one-year Treasury yield and (effective Jan 1, 2026) bans medical debt from credit reports entirely.

## Hospital itemization right

- **Statute:** **No Oregon-specific statute mandates itemized hospital bills on a fixed timeline.** Oregon's nearest analog is **ORS 676.310** (itemized billing as a professional-conduct rule for licensed practitioners) plus the federal HIPAA right of access to billing records (45 C.F.R. § 164.524) and the federal No Surprises Act's good-faith-estimate rule for the uninsured (45 C.F.R. § 149.610).
- **Source:** [oregon.public.law/statutes/ors_676.310](https://oregon.public.law/statutes/ors_676.310); HIPAA Right of Access at [hhs.gov/hipaa/for-professionals/privacy/guidance/access](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/access/index.html)
- **What it requires:**
  - Under ORS 676.310, a licensed practitioner must prepare an itemized billing indicating the charges for each service, with services performed by persons other than direct employees indicated separately. Failure to comply is unprofessional conduct subject to licensing-board discipline (not directly an individual remedy).
  - Under HIPAA, a patient written request triggers a 30-day production deadline (one 30-day extension permitted). Reasonable, cost-based fees may apply.
- **Scope:** ORS 676.310 reaches individually licensed practitioners (physicians, PAs, NPs, dentists, etc.). Hospital institutional billing is not directly covered by a hard deadline. A patient should request the itemized statement in writing and cite both HIPAA and ORS 676.310 (as to the treating practitioner).
- **Private right of action:** Not under ORS 676.310 directly (licensing-board remedy only). HIPAA itself has no private right of action, but the **Oregon UTPA (ORS 646.605 et seq.) does** — billing for services never rendered, upcoding, or refusing to produce a requested itemization in a deceptive manner is reachable as an unlawful trade practice (see UTPA section below).
- **ERISA:** Not preempted — regulates the provider, not the plan.

**Tactical note for letters:** Because Oregon lacks a Georgia-style six-business-day automatic itemization duty, the kit's standard demand letter to Oregon providers should rely on HIPAA's 30-day rule plus the UTPA's deceptive-practices reach. The 30-day window also dovetails with the kit's standard 30-day warning before escalation.

## Unfair Claim Settlement Practices Act

- **Statute:** **ORS 746.230** — Unfair claim settlement practices (insurance trade practices article, ORS 746.005 et seq.)
- **Source:** [oregon.public.law/statutes/ors_746.230](https://oregon.public.law/statutes/ors_746.230); [law.justia.com/codes/oregon/volume-18/chapter-746/section-746-230](https://law.justia.com/codes/oregon/volume-18/chapter-746/section-746-230/)
- **Substance:** Prohibits insurers from engaging in a defined list of unfair claims-settlement practices — misrepresenting policy provisions, failing to acknowledge claims promptly, failing to adopt reasonable standards for prompt investigation, refusing to pay without conducting a reasonable investigation, compelling litigation by offering substantially less than amounts ultimately recovered, etc.
- **Private right of action posture:**
  - **Brewer v. Erwin**, 287 Or. 435, 600 P.2d 398 (1979) was, for many years, read by Oregon courts to foreclose a freestanding private cause of action under ORS 746.230. (Note: Brewer itself was a landlord-tenant case; its sweeping language about implied causes of action under regulatory statutes was extended by later courts to insurance trade-practice claims.) Standalone § 746.230 counts were routinely dismissed.
  - **Moody v. Oregon Community Credit Union**, 371 Or. 772, 542 P.3d 24 (2023), changed the landscape. The Oregon Supreme Court held 4-3 that an insured may pursue a **common-law negligence per se** claim using ORS 746.230 as the standard of care, and may recover **emotional distress damages** without a physical-impact predicate. The court did not create a direct statutory cause of action under § 746.230 itself, so Brewer is technically not overruled — but its practical effect is largely gone.
- **Use:** After Moody, plead a common-law negligence claim with ORS 746.230 supplying the duty (negligence per se), then layer the UTPA (see below) where the conduct also reaches consumers in the marketplace sense. Continue to cite UTPA violations in complaints to the Division of Financial Regulation and as evidentiary support in any contract action.

## Bad-faith failure to pay (common-law tort posture)

- **Leading case:** **Farris v. U.S. Fidelity & Guaranty Co.**, 284 Or. 453, 587 P.2d 1015 (1978). Note: Farris is a 1978 decision, not 1991 — the 1991 date in the input appears to be a transcription error. Verify before citing.
- **Substance pre-Moody:** Farris was read for decades to mean that, outside the duty-to-defend context, Oregon does **not** recognize a freestanding common-law bad-faith tort against a first-party insurer. Insured remedies were limited to contract damages plus, in narrow circumstances, prejudgment interest and statutory attorney's fees under ORS 742.061 (insurance-action fee statute).
- **Substance post-Moody (2023):** The Oregon Supreme Court did not adopt a generic "bad faith" tort, but it did recognize that ORS 746.230 supplies a tort-law duty enforceable through negligence per se, with emotional-distress damages available. Several commentators describe this as a functional bad-faith remedy in everything but name.
- **Sources:** [law.justia.com/cases/oregon/supreme-court/1978/284-or-453-0.html](https://law.justia.com/cases/oregon/supreme-court/1978/284-or-453-0.html) (Farris); [law.justia.com/cases/oregon/supreme-court/2023/s069409.html](https://law.justia.com/cases/oregon/supreme-court/2023/s069409.html) (Moody); analysis at [millernash.com/industry-news/oregon-bad-faith-insurance-claims-gain-traction-thanks-to-new-ruling-from-court-of-appeals](https://www.millernash.com/industry-news/oregon-bad-faith-insurance-claims-gain-traction-thanks-to-new-ruling-from-court-of-appeals) and [stoel.com/insights/publications/the-evolving-landscape-of-bad-faith-law-in-oregon-a-year-after-moody-v-oregon-community-credit-union](https://www.stoel.com/insights/publications/the-evolving-landscape-of-bad-faith-law-in-oregon-a-year-after-moody-v-oregon-community-credit-union)
- **ORS 742.061 attorney's-fee hook:** When recovery in an insurance action exceeds the amount the insurer offered, plaintiff recovers reasonable attorney's fees. This is the primary fee-shift in fully-insured-plan disputes and is the easiest lever to cite in a 30-day warning letter to an Oregon insurer.
- **ERISA preemption:** Both the negligence-per-se claim and § 742.061 are **preempted** as to self-funded ERISA plans. Use 29 U.S.C. § 1132(a)(1)(B) and § 1132(g) (federal fee shift) instead.

## Balance Billing Protection Act

- **Statute:** **ORS 743B.287** (out-of-network at in-network facility, in-network cost-share cap) and related provisions in **ORS chapter 743B** (no-balance-billing for emergency services). Note: the input referenced ORS 743A.058 — that section addresses telemedicine coverage, not balance billing. The correct citation is **ORS 743B.287** for the core balance-billing prohibition.
- **Effective:** Original Oregon balance-billing law, March 1, 2018. Updated to interlock with the federal No Surprises Act effective Jan 1, 2022.
- **Sources:** [oregonlegislature.gov/bills_laws/ors/ors743B.html](https://www.oregonlegislature.gov/bills_laws/ors/ors743b.html); consumer overview at [dfr.oregon.gov/news/2021/pages/20211230-new-law-protects-consumers.aspx](https://dfr.oregon.gov/news/2021/pages/20211230-new-law-protects-consumers.aspx); patient handout at [dfr.oregon.gov/Documents/Surprise-billing-consumers.pdf](https://dfr.oregon.gov/Documents/Surprise-billing-consumers.pdf)

### What it prohibits

- Balance billing for **emergency services** from an out-of-network (OON) provider or facility.
- Balance billing for **non-emergency services** rendered by an OON provider at an **in-network** facility (ancillary services — anesthesia, radiology, pathology, lab, hospitalists, etc.).
- Patient cost-sharing is capped at the in-network amount and counts toward the in-network deductible and out-of-pocket maximum.
- Provider-payer rate disputes are resolved between them; the patient is held harmless.

### Caveats

- **ERISA preemption:** The Oregon Act does not reach self-funded ERISA employer plans on its own. The federal No Surprises Act fills that gap for emergency and OON-at-INN-facility scenarios.
- **Ground ambulance is governed by a separate statute, ORS 743B.292** (HB 3243, 2025), effective January 1, 2026 — see "Ground ambulance" section below.
- Excludes workers' compensation, Medicare, and Medicaid (those have their own rate regimes).
- Patients receive both state-law and federal NSA disclosures from providers; protections layer rather than displace.

## Regulatory agencies

### Oregon Department of Consumer and Business Services — Division of Financial Regulation (DFR)

- **Online complaint:** [dfr.oregon.gov/help/complaints-licenses/Pages/file-complaint.aspx](https://dfr.oregon.gov/help/complaints-licenses/Pages/file-complaint.aspx); direct insurance form at [www4.cbs.state.or.us/exs/dfcs/complaint/index.cfm?fuseaction=home.english](https://www4.cbs.state.or.us/exs/dfcs/complaint/index.cfm?fuseaction=home.english)
- **Phone:** Consumer Advocacy Hotline **1-888-877-4894** (toll-free); main Salem **(503) 378-4140**; fax (503) 947-7862
- **Email by topic:**
  - Insurance: DFR.InsuranceHelp@dcbs.oregon.gov
  - Medical providers (provider-complaint intake): HCProvider.Complaints@DCBS.oregon.gov
  - Financial services: DFR.FinancialServicesHelp@dcbs.oregon.gov
- **Mail:**
  > Oregon Division of Financial Regulation
  > PO Box 14480
  > Salem, OR 97309-0405
- **Authority:** all insurance companies licensed in Oregon, including fully-insured health insurers, HMOs, PPOs, and Medicare supplement. Administers the Balance Billing Protection Act, the new HB 3243 ground-ambulance regime, and the UCSPA (ORS 746.230). **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and does not regulate hospital itemization disputes (route to AG / DOJ).

### Oregon Department of Justice — Consumer Protection Section

- **Online complaint:** [justice.oregon.gov/consumercomplaints](https://justice.oregon.gov/consumercomplaints/) (file 24/7)
- **Phone:** Consumer Hotline **1-877-877-9392**
- **Mail:**
  > Oregon Department of Justice
  > Consumer Protection Section
  > 1162 Court Street NE
  > Salem, OR 97301-4096
- **Authority:** enforces the Oregon Unlawful Trade Practices Act (UTPA), ORS 646.605 et seq. Reaches providers, hospitals, third-party debt collectors, **and original creditors** — the exact gap left by DFR. Use for disputes with hospital in-house billing, deceptive collections, and medical-debt credit-reporting violations (now an explicit UTPA hook under SB 605, see Credit Reporting below).

## Oregon Unlawful Trade Practices Act (UTPA)

- **Citations:** **ORS 646.605 et seq.**; substantive list at **ORS 646.608**; private right of action at **ORS 646.638**.
- **Sources:** [law.justia.com/codes/oregon/volume-16/chapter-646](https://law.justia.com/codes/oregon/volume-16/chapter-646/); statute summary at [oregonlegislature.gov/lpro/Publications/BB2016TheUnlawfulTradePracticesAct.pdf](https://www.oregonlegislature.gov/lpro/Publications/BB2016TheUnlawfulTradePracticesAct.pdf)
- **Substance:** prohibits a broad list of deceptive and unfair practices in the sale of real estate, goods, **or services** (the "services" prong reaches medical billing). The list is non-exhaustive and includes misrepresenting characteristics, quantities, or charges, advertising with intent not to perform as advertised, and any other unconscionable tactic.
- **Private right of action — ORS 646.638:**
  - **Actual damages or statutory damages of $200, whichever is greater.**
  - **Punitive damages** available for reckless or knowing violations.
  - **Reasonable attorney's fees and costs** to the prevailing plaintiff (or to a prevailing defendant only if the action was frivolous).
  - Equitable relief, including injunction.
  - **No pre-suit notice requirement comparable to Georgia's 30-day FBPA demand**, but practical norms encourage a written demand to set up the willfulness predicate for punitive damages.
- **Why it matters:** the UTPA reaches **original creditors** (the hospital itself), not just third-party collectors. This is Oregon's analog to Georgia's FBPA but with a lower statutory-damages floor ($200) and no pre-suit ante-litem requirement. Combined with SB 605's express UTPA hook (see below), it is the single highest-value Oregon-specific lever against providers and collectors.

## Small claims court — Circuit Court Small Claims Department

- **Court name:** Small claims department of the **Oregon Circuit Court** (every county has one; large counties have justice-court small-claims departments as well).
- **Jurisdictional limit:** **$10,000**, codified at **ORS 46.405(2)**.
- **Source:** [oregon.public.law/statutes/ors_46.405](https://oregon.public.law/statutes/ors_46.405); [law.justia.com/codes/oregon/title-5/chapter-46/section-46-405](https://codes.findlaw.com/or/title-5-small-claims-department-of-circuit-court/or-rev-st-sect-46-405.html); Multnomah County procedural overview at [courts.oregon.gov/courts/multnomah/go/pages/smallclaims.aspx](https://www.courts.oregon.gov/courts/multnomah/go/pages/smallclaims.aspx)
- **Mandatory vs optional filing:** Claims **up to $750** must be filed in small claims (the regular circuit court has no concurrent jurisdiction at that level). Claims **$751 to $10,000** may be filed in small claims or in regular circuit court at plaintiff's election.
- **Filing fees:** typical 2025-2026 ranges $53 (claims up to $2,500) and $98 (claims $2,500 to $10,000), plus service costs. Verify on the Oregon Judicial Department fee schedule for the specific county.
- **Attorney rules:** **attorneys are not permitted to represent parties in small claims without the judge's prior consent** under ORS 46.415(2). Either party may petition the court for permission; consent is typically granted only when the opposing party is also represented or for genuine complexity. This is a stronger pro-se norm than most states.
- **Jury trial:** **Defendant may demand a jury trial** by removing the case to the regular department of the circuit court within the statutory window. Plaintiff cannot demand a jury in small claims. If the defendant removes, attorneys are permitted and full civil procedure applies. This is the single most important tactical quirk of Oregon small claims.
- **Corporate appearance:** a corporation or LLC may appear through a non-attorney officer or employee under the small-claims rules — useful when a hospital sends a billing-department staffer rather than counsel.

## Statute of limitations

- **Written and oral contracts:** **6 years from breach** — **ORS 12.080(1)**. Oregon does not distinguish between written and oral contracts for the general limitations period — both share the six-year clock. This is unusual and patient-favorable compared to most states.
- **Open accounts:** also 6 years under ORS 12.080(1) (a contract or liability, express or implied).
- **Source:** [oregon.public.law/statutes/ors_12.080](https://oregon.public.law/statutes/ors_12.080); [law.justia.com/codes/oregon/volume-01/chapter-012/section-12-080](https://law.justia.com/codes/oregon/volume-01/chapter-012/section-12-080/)
- **Accrual:** the clock runs from **the breach** (typically the day payment was due and not made), not from discovery. The Oregon Court of Appeals has repeatedly declined to extend the discovery rule to general breach-of-contract claims.
- **Partial payment / acknowledgment:** under ORS 12.240, a written acknowledgment or part-payment of the debt restarts the clock. **Do not make a partial payment on a time-barred debt without legal advice.**

## Ground ambulance balance billing

- **Statute:** **ORS 743B.292** — Balance billing prohibited for ground ambulance services; rate requirements; reporting; rules; penalties.
- **Enacted by:** **HB 3243 (2025)**, effective **January 1, 2026**.
- **Sources:** [law.justia.com/codes/oregon/volume-18/chapter-743b/section-743b-292](https://law.justia.com/codes/oregon/volume-18/chapter-743b/section-743b-292/); [dfr.oregon.gov/business/reg/health/Pages/ground-ambulance-rate-reporting.aspx](https://dfr.oregon.gov/business/reg/health/Pages/ground-ambulance-rate-reporting.aspx); bill history at [legiscan.com/OR/bill/HB3243/2025](https://legiscan.com/OR/bill/HB3243/2025)
- **What it prohibits:** A Ground Ambulance Service Organization (GASO) may not bill an enrollee for covered ground-ambulance services beyond the in-network cost-share specified in the enrollee's health benefit plan. Any overpayment must be refunded within **45 business days**.
- **Rate floor:** Health plans must reimburse GASOs at the locally established rate filed with DCBS, or — if no local rate is filed — **no less than 325% of the Medicare rate**. (This is materially higher than Georgia's 180%-of-Medicare floor.)
- **Scope:** All state-regulated health benefit plans. **Self-funded ERISA plans, PEBB plans, and OEBB plans may opt in** but are not covered by default. Includes interfacility transports and treatment-without-transport scenarios.
- **Database:** DCBS maintains a public database of established local rates ([dfr.oregon.gov/business/reg/health/Pages/ground-ambulance-rate-reporting.aspx](https://dfr.oregon.gov/business/reg/health/Pages/ground-ambulance-rate-reporting.aspx)). Cite the published local rate (or the 325%-of-Medicare floor) when challenging a balance bill.
- **Why it matters:** the **federal No Surprises Act explicitly excludes ground ambulance** — Oregon is one of the (growing) states that closes the gap. For any post-Jan-1-2026 Oregon ground-ambulance bill, this is the single highest-leverage cite.

## Credit reporting — Oregon Medical Debt Protection Act

- **Statute:** **ORS 646A.677** as amended by **SB 605 (2025)**.
- **Effective:** **January 1, 2026** (the medical-debt credit-reporting ban specifically; the financial-assistance-screening and interest-cap provisions of 646A.677 are already in force).
- **Sources:** [law.justia.com/codes/oregon/volume-16/chapter-646a/section-646a-677](https://law.justia.com/codes/oregon/volume-16/chapter-646a/section-646a-677/); enrolled SB 605 text at [olis.oregonlegislature.gov/liz/2025R1/Downloads/MeasureDocument/SB605/Enrolled](https://olis.oregonlegislature.gov/liz/2025R1/Downloads/MeasureDocument/SB605/Enrolled); summary at [ocj.org/news/oregon-legislature-passes-law-remove-medical-debt-credit-reports](https://ocj.org/news/oregon-legislature-passes-law-remove-medical-debt-credit-reports); industry analysis at [natlawreview.com/article/oregon-prohibits-medical-debt-credit-reports](https://natlawreview.com/article/oregon-prohibits-medical-debt-credit-reports)
- **What it prohibits:**
  - **Hospitals, debt collectors, creditors, and any other party** may not report the amount or existence of any medical debt an Oregon resident owes or is alleged to owe to a consumer reporting agency.
  - **Consumer reporting agencies** must block any item they know or reasonably should know to be medical debt from appearing in a credit report.
  - The definition of "medical debt" is broad — virtually any obligation for treatment, supplies, or balances on dedicated medical-expense credit cards, **excluding purely cosmetic procedures**.
- **Pre-existing protections under ORS 646A.677 (already in force):**
  - Hospital must screen for financial-assistance eligibility before transferring medical debt for collection.
  - Interest on medical debt for patients who do not qualify for financial assistance is capped at the one-year constant-maturity Treasury yield (subject to a floor of 2% and a ceiling of 5% per annum). Patients who **do** qualify for financial assistance owe **0% interest**.
- **Remedies:** Violation is expressly an unlawful trade practice under the UTPA — so the full UTPA remedy stack applies: actual or $200 statutory damages, attorney's fees, punitive damages for knowing/reckless conduct, and **courts may void improperly reported debt**. This is the single most important addition: a court can wipe out the debt itself, not just enjoin the credit report.
- **Federal-preemption posture:** Under flux. The CFPB issued (October 2025) an interpretive rule asserting that FCRA preempts state medical-debt credit-reporting laws. The CFPB then vacated that rule in 2026. Oregon, Maine, and Vermont have already enacted laws, so Oregon's statute is likely to survive any renewed preemption challenge in practice, but the litigation posture should be watched.

## Hospital financial assistance

- **Citations:** **ORS 442.601** (definitions), **ORS 442.610** (notice and applications), **ORS 442.614** (FA policy requirements), **ORS 442.615** (screening, processing, appeals, collections). Enacted via **HB 3076 (2019)** and strengthened by **HB 3320 (2023)**.
- **Sources:** [oregon.public.law/statutes/ors_442.614](https://oregon.public.law/statutes/ors_442.614); [oregon.public.law/statutes/ors_442.615](https://oregon.public.law/statutes/ors_442.615); HB 3320 enrolled text at [olis.oregonlegislature.gov/liz/2023R1/Downloads/MeasureDocument/HB3320](https://olis.oregonlegislature.gov/liz/2023R1/Downloads/MeasureDocument/HB3320); Dollar For state sheet at [dollarfor.org/state_sheet/oregon](https://dollarfor.org/state_sheet/oregon/)
- **Mandatory sliding scale** (nonprofit hospitals and their affiliated clinics):
  - Up to **200% FPL**: 100% off (free care)
  - 201-300% FPL: at least 75% off
  - 301-350% FPL: at least 50% off
  - 351-400% FPL: at least 25% off
- **Presumptive eligibility (HB 3320, 2023):** Nonprofit hospitals **must** prescreen patients for financial-assistance eligibility before sending any bill greater than **$500** for a single stay or visit, where the patient is uninsured, on the Oregon Health Plan / state medical assistance, or owes more than $500 after insurance. **This is the single most aggressive state FA mandate in the country** — patients should never receive a > $500 bill from an Oregon nonprofit hospital without an FA screening attempt.
- **Application window:** at least **240 days** from the first post-discharge bill — among the longest in the country.
- **Immigration status:** Oregon law explicitly **requires** hospitals to provide assistance regardless of immigration status.
- **No minimum-bill threshold:** hospitals may **not** impose a floor below which FA is unavailable.
- **Interest cap:** as above under ORS 646A.677 — 0% for FA-qualified patients, otherwise capped at the one-year Treasury yield (2-5% range).
- **For-profit hospitals:** Oregon's HB 3320 FA mandate applies primarily to **nonprofit** hospitals. For-profit hospitals are subject to a narrower set of requirements and federal § 501(r) does not reach them. Always check the hospital's tax status before relying on the full state FA stack.
- **2026 watch:** in April 2026, news coverage reported Democratic-led legislative moves to weaken parts of the HB 3320 framework (specifically around the income tiers and presumptive-eligibility process). Verify the live statute before filing a complaint. Source: [opb.org/article/2026/04/11/oregon-democrats-hospital-bills-medicaid-charity-care](https://www.opb.org/article/2026/04/11/oregon-democrats-hospital-bills-medicaid-charity-care/).
- **Use Dollar For** at [dollarfor.org/state_sheet/oregon](https://dollarfor.org/state_sheet/oregon/) for patient-side screening.

## Hospital lien statute

- **Citations:** **ORS 87.555** through **ORS 87.585**.
- **Sources:** [oregon.public.law/statutes/ors_87.555](https://oregon.public.law/statutes/ors_87.555); [oregon.public.law/statutes/ors_87.565](https://oregon.public.law/statutes/ors_87.565) (notice); [oregon.public.law/statutes/ors_87.560](https://oregon.public.law/statutes/ors_87.560) (limitations); practitioner overview at [johnsonlaw.com/medical-liens-101-hospitals-chiropractors-and-what-they-can-claim-from-your-settlement](https://johnsonlaw.com/medical-liens-101-hospitals-chiropractors-and-what-they-can-claim-from-your-settlement)
- **Substance:** Hospitals, physicians, physician assistants, and nurse practitioners may file a lien for the reasonable value of treatment **only against the injured patient's cause of action or settlement against a third party** who caused the injury, **and against PIP / no-fault medical insurance proceeds**. **Not a lien on the patient's home, wages, bank accounts, or standard health insurance proceeds.**
- **Perfection requirements (ORS 87.565):**
  - File notice of lien with the recording officer (county clerk) of the county where the hospital/provider is located **within 30 days after the patient's discharge**.
  - Serve a certified copy on the injured person, the at-fault party, and the at-fault party's insurer **before the date of judgment, award, or settlement**.
  - Failure to perfect timely defeats the lien.
- **Limitations (ORS 87.560):**
  - No lien against Workers' Compensation Act recoveries.
  - No lien against the portion of the recovery representing the patient's reasonable attorney's fees, costs, and litigation expenses (a meaningful patient-side carve-out — Oregon is among the more generous states on this point).
  - When liens exceed available funds, the insurer must prorate without regard to filing sequence.
- **2024 amendment (HB 4010, effective June 6, 2024):** expanded "lien claimants" to include licensed physician assistants and nurse practitioners. Verify recency of cited statute if a PA/NP is the lien claimant.
- **Tactical note:** always confirm that the hospital first attempted to submit the bill to the patient's health insurer. ORS 742.524 and general subrogation principles disfavor liens stacked on top of unbilled insurance claims.

## Wage garnishment

- **Statute:** **ORS chapter 18** (garnishment), specifically **ORS 18.385** (exempt wages) and **ORS 18.840** (challenge process).
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a court judgment. Post-judgment, Oregon's exemption is **the greater of 75% of disposable earnings or $254 per workweek** (adjusted from time to time; verify the current threshold via the Oregon Judicial Department). Oregon's exemption is more generous than the federal CCPA 25%-of-disposable cap because it adds a dollar floor.
- **Source:** [oregon.public.law/statutes/ors_18.385](https://oregon.public.law/statutes/ors_18.385)
- **Use:** in response letters to collectors threatening garnishment without a judgment in hand, and to point out that even a judgment is followed by Oregon's enhanced exemption floor.

## Quick reference for letter rendering

When the LLM renders an Oregon-bound letter, substitute these defaults:

- **State statute (itemization right):** HIPAA Right of Access (45 C.F.R. § 164.524, 30-day rule) plus ORS 676.310 (itemized-billing professional-conduct rule). Oregon does not have a fixed-day automatic itemization mandate — frame requests in writing and use the 30-day HIPAA deadline.
- **State insurance regulator (CC line):** Oregon Division of Financial Regulation, Consumer Advocacy Unit, PO Box 14480, Salem, OR 97309 (Consumer Hotline 1-888-877-4894)
- **State AG consumer protection (CC line):** Oregon Department of Justice, Consumer Protection Section, 1162 Court Street NE, Salem, OR 97301-4096 (Consumer Hotline 1-877-877-9392; online complaint at [justice.oregon.gov/consumercomplaints](https://justice.oregon.gov/consumercomplaints/))
- **Small-claims court name:** **Circuit Court of [county], Small Claims Department**
- **Filing fee (in 30-day warning):** "$53 to $98 depending on amount claimed"
- **Statute of limitations (in 30-day warning):** "ORS 12.080(1) (six years for contract claims, written or oral)"
- **For ground-ambulance balance bills (post Jan 1, 2026):** Cite **ORS 743B.292** as enacted by HB 3243 (2025). Reference the DCBS local-rate database or the 325%-of-Medicare floor.
- **For provider-side disputes (vs. insurer-side):** Cite the **Oregon UTPA, ORS 646.605 et seq.** with the private right of action at **ORS 646.638** (statutory $200 minimum, actual damages, attorney's fees, punitive damages). No pre-suit notice required, but the kit's standard 30-day warning letter is good practice for setting up the willfulness/punitive predicate.
- **For insurer-side disputes (fully-insured plans):** Cite **ORS 746.230** as the standard of care, plead negligence per se per **Moody v. Oregon Community Credit Union**, and invoke **ORS 742.061** for attorney's fees on any insurance-policy recovery exceeding the insurer's tender.
- **For medical-debt credit-reporting violations (effective Jan 1, 2026):** Cite **ORS 646A.677** as amended by SB 605 (2025); plead the UTPA hook for $200 statutory damages plus attorney's fees and request the court void the debt.

## Key Oregon-specific advantages

Worth keeping in mind when triaging an Oregon patient's bills:

1. **Original-creditor reach via UTPA** — ORS 646.605 et seq. reaches the hospital itself with statutory damages, attorney's fees, and punitive damages on a knowing/reckless violation. No 30-day ante-litem requirement (unlike Georgia FBPA).
2. **Post-Moody negligence-per-se path** — for fully-insured-plan denials, ORS 746.230 can supply the duty of care for a tort claim with emotional-distress damages. Combined with ORS 742.061's insurance-action attorney's fee shift, this is a credible litigation lever against Oregon health insurers (subject to ERISA preemption for self-funded plans).
3. **Presumptive financial-assistance screening** — Oregon's HB 3320 mandate that nonprofit hospitals **proactively** screen for FA before sending any > $500 bill is the most aggressive in the country. If an Oregon nonprofit hospital sends a > $500 bill to an uninsured or OHP-enrolled patient without an FA screening, that is itself a statutory violation and a UTPA hook.
4. **Interest cap + zero-interest for FA-qualified patients** — ORS 646A.677 caps interest at the one-year Treasury yield (2-5% floor/ceiling), and patients who qualify for FA owe **0% interest** regardless of payment plan length. Reference this when collectors propose high-interest payment plans.
5. **Medical-debt credit-reporting ban (effective Jan 1, 2026)** — Oregon goes further than most states by allowing courts to **void improperly reported debt**, not merely block the report. This is qualitatively stronger relief than what FCRA or any other state law currently affords.
6. **Pro-se norms in small claims** — ORS 46.415 prohibits attorney representation without judicial consent in small claims. The defendant's only escape is to remove the case to the regular department of circuit court for a jury trial, which is expensive enough that most low-value hospital claims will not be removed. Patients can run small claims as a near-pure pro-se forum.
7. **Hospital lien carve-out for attorney's fees** — ORS 87.560 protects the portion of a third-party recovery representing attorney's fees from any provider lien. Patients with personal-injury settlements keep more of the net than they would in most states.
