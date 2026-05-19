# Iowa state pack

The fully-worked state-law layer for Iowa patients. The LLM uses this when the patient's state is Iowa. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-19. Re-verify annually.

Three things make Iowa's patient-side leverage distinctive:

1. **Common-law first-party bad faith tort is recognized** — Iowa joined the minority of states that allow an insured to sue an insurer in tort for bad-faith refusal to pay a first-party claim. See *Dolan v. Aid Ins. Co.*, 431 N.W.2d 790 (Iowa 1988). Punitive damages are in play.
2. **Iowa Private Right of Action for Consumer Frauds Act (Iowa Code Chapter 714H)** gives Iowa consumers a private cause of action with actual damages, **treble damages for willful violations**, and **mandatory attorney's fees**. This is Iowa's analogue to Georgia's FBPA § 10-1-399 and reaches the hospital directly, not just third-party collectors.
3. **Ten-year statute of limitations on written contracts** (Iowa Code § 614.1(5)) is one of the longer SOL periods in the country — relevant when the hospital is chasing an old signed financial-responsibility agreement, but also relevant defensively when the patient wants to assert breach-of-contract counterclaims against the hospital.

A note on user-provided cites:

- **Iowa Code Chapter 514L is not the hospital-itemization chapter.** Chapter 514L is the "Pharmacy Identification Card" chapter (definitions tied to NCPDP pharmacy-card implementation guides). Iowa has **no statutory analogue** to Georgia's automatic 6-business-day itemized-billing duty under O.C.G.A. § 10-1-393(b)(14). The right to an itemized statement in Iowa comes from a layered set of federal and licensure sources rather than a single state code section. The relevant chapters are flagged in the section below.
- **Iowa Code § 614.1 numbering:** the **5-year unwritten-contract period** is at **§ 614.1(4)**, and the **10-year written-contract period** is at **§ 614.1(5)**. (Your prompt swapped the subsection numbers; the substance is correct.)

Both corrections are reflected in the relevant sections below.

## Hospital itemization right

- **Statute:** Iowa has **no statutory analogue** to Georgia's automatic 6-business-day itemized-billing duty (O.C.G.A. § 10-1-393(b)(14)). The right to an itemized statement in Iowa comes from a layered set of sources rather than a single state code section.
- **Sources of the right:**
  - **Federal — 26 U.S.C. § 501(r)(6)** and **26 C.F.R. § 1.501(r)-6** require non-profit hospitals to bill at the "amounts generally billed" (AGB) cap and to make reasonable efforts to determine FAP eligibility before extraordinary collection actions. Receipt of an itemized statement is part of the practical record patients need to verify AGB compliance.
  - **Federal — 42 C.F.R. § 482.13** (Medicare Conditions of Participation, Patient's Rights) requires hospitals to inform patients of charges. Most Iowa hospitals participate in Medicare and are bound.
  - **Hospital licensure regulations — Iowa Admin. Code 481-51** (hospital regulations under Iowa Code Chapter 135B) require hospitals to maintain financial records and provide patient-rights information; itemization-on-request is part of the practical patient-rights framework.
  - **Iowa Private Right of Action for Consumer Frauds Act — Iowa Code § 714H.3** reaches "unfair practices" and "deception" in consumer transactions and is the strongest UDAP-style lever when a hospital refuses or evades itemization (see Chapter 714H section below).
- **Practical posture for the kit:** Send a written, certified-mail request for a CPT/HCPCS-coded itemized statement under "federal price transparency and § 501(r) AGB compliance" authority, plus Iowa Code § 714H.3 deception theory. A 14- to 30-day response window is reasonable. Non-response is itself a fact the Iowa AG can act on under Chapter 714H and the Consumer Fraud Act (§ 714.16).

## Iowa Consumer Fraud Act and Private Right of Action

### Iowa Consumer Fraud Act — Iowa Code § 714.16 (AG enforcement only)

- **Statute:** **Iowa Code § 714.16** — "Consumer frauds"
- **Source:** [law.justia.com/codes/iowa/title-xvi/chapter-714/section-714-16](https://law.justia.com/codes/iowa/title-xvi/chapter-714/section-714-16/); statutory PDF at [legis.iowa.gov/docs/code/714.16.pdf](https://www.legis.iowa.gov/docs/code/714.16.pdf)
- **Substance:** Prohibits any "deception, fraud, false pretense, false promise, misrepresentation, or the concealment, suppression, or omission of a material fact, with intent that others rely upon" such conduct in connection with the sale or advertisement of merchandise or services. Hospitals and providers, as sellers of services, fall within scope.
- **Enforcement:** **Iowa Attorney General only.** § 714.16 itself does not create a private right of action. AG remedies include injunctive relief, civil penalties up to $40,000 per violation, restitution, and disgorgement.
- **Use:** File a parallel AG complaint citing § 714.16 (see Regulatory Agencies below) alongside any § 714H private suit.

### Private Right of Action for Consumer Frauds Act — Iowa Code Chapter 714H

- **Statute:** **Iowa Code Chapter 714H** — "Consumer Fraud — Private Actions" (effective **July 1, 2009**, ending Iowa's prior status as the last state without a private consumer-fraud right of action)
- **Source:** [law.justia.com/codes/iowa/title-xvi/chapter-714h](https://law.justia.com/codes/iowa/title-xvi/chapter-714h/); statutory PDF at [legis.iowa.gov/docs/code/714H.pdf](https://www.legis.iowa.gov/docs/code/714H.pdf); practitioner overview at [bpglegal.com/articles/iowas-new-consumer-fraud-law](https://www.bpglegal.com/articles/iowas-new-consumer-fraud-law/) and [youriowalawyers.com/blog/2009/february/iowa-s-consumer-rights-act](https://www.youriowalawyers.com/blog/2009/february/iowa-s-consumer-rights-act/)
- **Substance:** A consumer who suffers an ascertainable loss of money or property as the result of a "prohibited practice" (the same enumerated conduct under § 714.16 — deception, fraud, false promise, misrepresentation, concealment of material fact) may bring a civil action and recover **actual damages**, plus the court "shall" award **reasonable attorney's fees and costs** to a prevailing consumer. For **willful** violations, the court may award **liquidated or punitive damages up to three times actual damages**.
- **Procedural requirements:**
  - **Pre-suit notice to the Iowa AG** (§ 714H.7): the consumer (or counsel) must file a copy of the petition with the AG's Consumer Protection Division at the time suit is filed. Not a 30-day ante-litem demand like Georgia's FBPA, but creates the parallel AG-file paper trail. Failure to comply does not bar the action but is a procedural defect.
  - **Class actions:** explicitly permitted under § 714H.5.
- **Reach over original creditors:** Chapter 714H applies directly to suppliers and sellers of services, including hospitals and providers in their billing capacity. Mirrors the Georgia FBPA and Indiana DCSA advantage.
- **Why it matters:** Iowa Chapter 714H is the **strongest patient-side state-law cite** for provider-side disputes (itemization refusals, "phantom" charges, upcoding, misrepresenting in-network status, threatening unfounded suit). The "shall" attorney's-fees language makes fee recovery realistic in a way Iowa's general fee-shifting rules do not.
- **Exclusions:** Conduct already regulated by other professional-licensing or financial-services statutes is partially carved out; medical billing falls outside those carve-outs.

## Unfair Claim Settlement Practices Act (UCSPA)

- **Statute:** **Iowa Code Chapter 507B** — "Insurance Trade Practices"; enumerated unfair claims-settlement practices at **§ 507B.4(9)** (renumbered subsection — earlier code editions used § 507B.4(3)(j) and similar)
- **Source:** [law.justia.com/codes/iowa/title-xiii/chapter-507b](https://law.justia.com/codes/iowa/title-xiii/chapter-507b/); statutory PDF at [legis.iowa.gov/docs/code/507B.4.pdf](https://www.legis.iowa.gov/docs/code/507B.4.pdf); United Policyholders summary at [uphelp.org/claim-guidance-publications/insurance-consumer-rights-in-iowa-2022](https://uphelp.org/claim-guidance-publications/insurance-consumer-rights-in-iowa-2022/)
- **Substance:** Prohibits insurers from engaging in a defined list of unfair claims-settlement practices — misrepresenting policy provisions, failing to acknowledge claims promptly, refusing to pay without a reasonable investigation, failing to affirm or deny coverage in a reasonable time, not attempting in good faith to effectuate prompt and equitable settlements where liability has become reasonably clear, etc. Trigger requires the conduct be committed "with such frequency as to indicate a general business practice."
- **Critical caveat — no private right of action:** Iowa courts have repeatedly held that Chapter 507B is silent on a private remedy and that no private cause of action exists. Enforcement is exclusively by the **Iowa Insurance Commissioner**.
- **Why it still matters — the bridge to *Dolan*:** Although the statute itself is non-actionable, Iowa recognizes a separate **common-law tort of first-party bad faith** under *Dolan v. Aid Ins. Co.* (1988). The conduct enumerated in § 507B.4(9) is precisely the conduct that supports a *Dolan* bad-faith claim. Plead the bad-faith tort, **cite UCSPA violations as evidence**, and file a parallel Iowa Insurance Division complaint. Three-track posture mirrors Indiana's *Hickman* framework.
- **Use in dispute letters:** Cite specific § 507B.4(9) subsections when the dispute is with an insurer over a denied or underpaid claim; the IID complaint mechanism is the operative regulatory remedy, and the citation primes the *Dolan* tort claim if litigation follows.

## Bad-faith failure to pay (common-law tort)

- **Source case:** ***Dolan v. Aid Ins. Co.***, **431 N.W.2d 790 (Iowa 1988)** — Iowa Supreme Court formally recognized a tort cause of action for an insurer's breach of the duty of good faith and fair dealing toward its first-party insured.
- **Source:** [law.justia.com/cases/iowa/supreme-court/1988/87-1380-0.html](https://law.justia.com/cases/iowa/supreme-court/1988/87-1380-0.html); practitioner overview at [oflaherty-law.com/learn-about-law/bad-faith-claims-in-iowa](https://www.oflaherty-law.com/learn-about-law/bad-faith-claims-in-iowa); [propertyinsurancecoveragelaw.com/blog/iowa-bad-faith-law-can-iowa-policyholders-hold-insurers-accountable-for-wrongful-claims-conduct](https://www.propertyinsurancecoveragelaw.com/blog/iowa-bad-faith-law-can-iowa-policyholders-hold-insurers-accountable-for-wrongful-claims-conduct/)
- **Two-element test (per *Dolan*, adopting *Anderson v. Continental Ins. Co.* standard):**
  1. **No reasonable basis** for denying or delaying payment of benefits.
  2. The insurer's **knowledge or reckless disregard** of the lack of a reasonable basis.
- **The "fairly debatable" standard:** Where the claim is "fairly debatable" — meaning the insurer has a rational, principled basis (factual or legal) for its position — the insurer is entitled to debate it, and bad faith cannot lie even if the insurer's position ultimately proves wrong. This is a meaningful brake on the tort and aligns Iowa with Wisconsin/Indiana on the standard side.
- **Damages:**
  - Contract damages (the underlying loss the insurer should have paid).
  - **Consequential damages** flowing from the bad-faith conduct (emotional distress, related economic harm in appropriate cases).
  - **Punitive damages** where the bad faith is shown by clear and convincing evidence. Iowa applies a punitive-damage statute (Iowa Code § 668A.1) with a 75/25 allocation rule (75% to the state Civil Reparations Trust Fund when the conduct was not directed specifically at the claimant; 100% to the claimant when it was).
  - **Attorney's fees are not automatically recoverable** under *Dolan* (contrast Georgia's § 33-4-6 statutory penalty-and-fees structure). Fees come only via Chapter 714H (if pled in parallel) or separate fee-shifting statute or contract terms.
- **Coverage scope:** First-party only. Applies to fully insured health policies, accident and sickness, individual/marketplace plans. **ERISA-preempted** as applied to self-funded employer plans — for those, the federal remedy is 29 U.S.C. § 1132(a)(1)(B). Plead carefully and confirm plan funding type before relying on *Dolan*.
- **Procedural posture:** No ante-litem demand requirement. Statute of limitations is the general 5-year tort period under Iowa Code § 614.1(4) for the bad-faith count, with the underlying breach-of-contract count tracking § 614.1(5) (10 years) if written.

## Surprise billing

Iowa has a **narrow** state surprise-billing protection focused on emergency-room services, with the federal No Surprises Act doing most of the work.

### Emergency services — Iowa Code § 514C.16

- **Statute:** **Iowa Code § 514C.16** — "Emergency room services"
- **Source:** [legis.iowa.gov/docs/code/514C.16.pdf](https://www.legis.iowa.gov/docs/code/514C.16.pdf); chapter index at [law.justia.com/codes/iowa/title-xiii/chapter-514c](https://law.justia.com/codes/iowa/title-xiii/chapter-514c/); UIHC patient-facing summary at [healthcare.uiowa.edu/marcom/uihc/billing/Balance_Billing_Rights_and_Protections.pdf](https://www.healthcare.uiowa.edu/marcom/uihc/billing/Balance_Billing_Rights_and_Protections.pdf)
- **Substance:** A carrier subject to Iowa insurance laws must cover all provider charges for **emergency services**, including services furnished by an **out-of-network provider**. Prior authorization may not be required. Coverage continues through stabilization, with post-stabilization protections subject to written informed consent that the patient is giving up the protection (mirrors the federal NSA notice-and-consent process at 45 C.F.R. § 149.420).
- **Scope:** State-regulated insurance carriers and HMOs. **ERISA-preempted** for self-funded employer plans. Excludes Medicare and Medicaid.
- **Limit:** § 514C.16 covers the **emergency room** scenario. Iowa has **no general state-law analogue to Georgia's § 33-20E-1 et seq.** that prohibits balance billing for non-emergency services rendered by an OON provider at an in-network facility (ancillary services — anesthesia, radiology, pathology). For ancillary OON-at-INN scenarios, **the federal No Surprises Act is the primary protection**.

### Federal No Surprises Act — primary protection

For Iowa patients, the federal No Surprises Act (45 C.F.R. Parts 144-149; 26 C.F.R. Part 54; 29 C.F.R. Part 2590) does most of the work beyond the § 514C.16 ER scenario. The Iowa Insurance Division administers state enforcement of the NSA. Iowa CMS State Enforcement Letter at [cms.gov/cciio/programs-and-initiatives/other-insurance-protections/caa-enforcement-letters-iowa.pdf](https://www.cms.gov/cciio/programs-and-initiatives/other-insurance-protections/caa-enforcement-letters-iowa.pdf).

### Practical posture

Where a non-emergency bill exceeds a federal No Surprises Act good-faith estimate by **$400 or more**, use the federal Patient-Provider Dispute Resolution (PPDR) process for self-pay/uninsured patients. For balance-billing on an emergency-room visit through a state-regulated plan, file a complaint with the Iowa Insurance Division citing § 514C.16. For self-funded ERISA plans, route to DOL EBSA (1-866-444-3272).

## Regulatory agencies

### Iowa Insurance Division (IID) — Consumer Services

- **Online complaint:** [iid.iowa.gov/consumers/filing-complaints/how-do-i-consumer-complaints](https://iid.iowa.gov/consumers/filing-complaints/how-do-i-consumer-complaints); NAIC SBS portal at [sbs.naic.org/solar-web/pages/public/onlineComplaintForm](https://sbs.naic.org/solar-web/pages/public/onlineComplaintForm/onlineComplaintForm.jsf?state=ia)
- **Phone:** main **(515) 654-6600**; toll-free **1-877-955-1212**; Market Regulation Bureau / complaints **(515) 654-6640**
- **Hours:** 8:00 a.m. - 4:30 p.m., Monday through Friday
- **Mail:**
  > Iowa Insurance Division
  > Attn: Consumer Services
  > 1963 Bell Avenue, Suite 100
  > Des Moines, IA 50315
- **Authority:** Licensed insurers, HMOs, accident-and-sickness policies, Medicare supplement. Administers Iowa Code Chapter 507B (UCSPA), § 514C.16 (emergency-services coverage), and state-side enforcement of the federal No Surprises Act. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and does not regulate providers, hospitals, or debt collectors (route to AG).
- **Contact page:** [iid.iowa.gov/about/contact](https://iid.iowa.gov/about/contact)

### Iowa Attorney General — Consumer Protection Division

- **Online complaint:** [iowaattorneygeneral.gov/for-consumers/file-a-consumer-complaint](https://www.iowaattorneygeneral.gov/for-consumers/file-a-consumer-complaint); online form at [iowaattorneygeneral.gov/for-consumers/file-a-consumer-complaint/complaint-form](https://www.iowaattorneygeneral.gov/for-consumers/file-a-consumer-complaint/complaint-form); printable form at [iowaattorneygeneral.gov/for-consumers/file-a-consumer-complaint/printable-consumer-complaint-form](https://www.iowaattorneygeneral.gov/for-consumers/file-a-consumer-complaint/printable-consumer-complaint-form)
- **Phone:** main **(515) 281-5926**; toll-free **1-888-777-4590**
- **Mail:**
  > Office of the Attorney General of Iowa
  > Consumer Protection Division
  > Hoover State Office Building
  > 1305 E. Walnut Street
  > Des Moines, IA 50319-0106
- **Authority:** Enforces the **Iowa Consumer Fraud Act (§ 714.16)** against sellers including hospitals' in-house billing departments, providers, and third-party debt collectors. Receives § 714H.7 pre-suit notices in private consumer-fraud actions. Reach over **original creditors** — the exact gap not covered by IID. Use when the dispute is with the hospital's billing office, not with an insurer's claim decision.

## Small claims court

- **Court name:** **Small Claims Docket** of the Iowa District Court (in the county where the defendant resides or the obligation arose)
- **Jurisdictional limit:** **$6,500**, codified at **Iowa Code § 631.1(1)**
- **Source:** [law.justia.com/codes/iowa/title-xv/chapter-631](https://law.justia.com/codes/iowa/title-xv/chapter-631/); statute PDF at [legis.iowa.gov/docs/code/631.1.pdf](https://www.legis.iowa.gov/docs/code/631.1.pdf); judicial-branch guide at [iowacourts.gov/for-the-public/representing-yourself/small-claims](https://www.iowacourts.gov/for-the-public/representing-yourself/small-claims); People's Law Library at [peopleslawiowa.org/index.php/research-topics/consumer-law/small-claims/what-small-claims](https://www.peopleslawiowa.org/index.php/research-topics/consumer-law/small-claims/what-small-claims)
- **Filing fees:** **$95** filing and docketing fee under **Iowa Code § 631.6**, plus service-of-process costs. A claim above $6,500 may still be filed in small claims but the plaintiff **waives the excess**.
- **Attorney rules:** **Permitted, not required** under **Iowa Code § 631.14**. Designed for pro se litigants — simplified pleadings, limited discovery, relaxed evidence rules. **Important Iowa advantage:** § 631.14(1) explicitly permits a corporation, partnership, association, or other non-individual entity to be represented by **an officer or employee** — no dollar-threshold restriction. This mirrors Georgia's Magistrate Court rule and is **more favorable** to patients than Indiana's $1,500 cap on non-attorney corporate appearance. A hospital defendant in Iowa small claims will frequently send a billing-department staffer rather than retain counsel.
- **Jury trial:** Not available on the small claims docket. Either party may demand removal to the regular district court docket (with jury rights) under Iowa Rules of Civil Procedure, typically within the time set by local rule.

## Statute of limitations

- **Written contracts:** **10 years from breach** — **Iowa Code § 614.1(5)**
- **Unwritten contracts and open accounts:** **5 years from breach** — **Iowa Code § 614.1(4)**
- **Injuries to person or reputation, statutory penalties, fraud:** 2 years — § 614.1(2)
- **Source:** [law.justia.com/codes/iowa/title-xv/chapter-614/section-614-1](https://law.justia.com/codes/iowa/title-xv/chapter-614/section-614-1/); statutory PDF at [legis.iowa.gov/docs/code/614.1.pdf](https://www.legis.iowa.gov/docs/code/614.1.pdf); practitioner summary at [findlaw.com/state/iowa-law/iowa-civil-statute-of-limitations-laws.html](https://www.findlaw.com/state/iowa-law/iowa-civil-statute-of-limitations-laws.html); debt-collection summary at [nationallist.com/image/cache/White_Paper_Iowa_Debt_Collection.pdf](https://www.nationallist.com/image/cache/White_Paper_Iowa_Debt_Collection.pdf)

Most hospital admissions involve a signed financial-responsibility form — a written contract, so **10 years under § 614.1(5)** applies. Implied-in-fact medical-billing arrangements without a signed agreement fall under unwritten contract / open-account treatment at § 614.1(4) (5 years). The clock runs from breach (typically the day payment was due and not made), not from when damages are discovered.

**Practical implications of the 10-year written-contract SOL:**

- **Defensively (when the patient is sued):** Iowa's 10-year clock is among the longest in the country, so hospitals and assignees have a long window to file. The "this debt is too old to sue on" defense rarely succeeds inside 10 years from breach. Compare to Georgia (6 years), Indiana (6), Tennessee (6), Texas (4).
- **Offensively (when the patient is suing under Chapter 714H or *Dolan*):** Iowa's 10-year breach-of-contract window gives the patient a long runway to pursue overcharge, upcoding, and AGB-cap violations under contract theories before SOL bars suit. Pair with the 5-year tort/fraud limitations period on § 614.1(2)-based claims.

Partial payment or **written acknowledgment of the debt restarts the clock** under common-law principles applied in Iowa. **Do not make a partial payment on a time-barred medical debt without legal advice** — it can revive the limitations period entirely.

## Ground ambulance balance-billing

**Iowa has no state-law ground-ambulance balance-billing protection** as of 2026-05-19. § 514C.16 covers emergency services broadly but does not explicitly extend the balance-billing prohibition to OON ground-ambulance transport in the way Georgia's § 33-20E-1 et seq. (as amended by HB 286), Indiana's HEA 1385, or the laws in approximately 19 other states do.

For Iowa patients:

- The **federal No Surprises Act explicitly excludes ground ambulance** (see 86 Fed. Reg. 36872, and the federal Advisory Committee on Ground Ambulance and Patient Billing reports).
- **Pre-NSA state surprise-billing protection in Iowa is minimal beyond emergency-room services** (§ 514C.16). Ground-ambulance balance bills are largely unrestricted at the state level.
- **Practical leverage** comes from (a) the federal Patient-Provider Dispute Resolution process for self-pay/uninsured patients where applicable, (b) Iowa Chapter 714H deception theories where the ambulance bill is materially inflated or misrepresents the rate, and (c) municipal-government-operated ambulance services, which may be subject to local fee schedules.
- **Watch list:** Several Iowa General Assembly sessions have seen proposals to add ground-ambulance protection; re-verify enactment status before relying on a state-law cite. PIRG's 2025 tracking at [pirg.org/edfund/resources/emergency-the-high-cost-of-ambulance-surprise-bills](https://pirg.org/edfund/resources/emergency-the-high-cost-of-ambulance-surprise-bills/) is a useful reference.

## Credit reporting

Iowa has **not enacted** a state-specific medical-debt credit-reporting restriction. Iowa patients rely on:

- **Voluntary credit bureau policy changes** (2022-2023): paid medical debt removed; debt under $500 not reported; one-year delay before reporting unpaid medical debt.
- **Federal FCRA dispute rights** (15 U.S.C. §§ 1681i, 1681s-2) against furnishers and bureaus.
- **Iowa Code Chapter 714H** as a state UDAP overlay where furnishing inaccurate medical-debt information to bureaus is shown to be deceptive (e.g., furnishing a balance that exceeds the § 501(r) AGB cap, or furnishing while the patient's FAP application is pending).
- **Iowa Consumer Credit Code — Iowa Code § 537.7103** governs prohibited debt-collection practices generally (Iowa Fair Debt Collection Practices analogue), reachable for harassing or deceptive collection conduct.

**Federal preemption posture is in flux.** The CFPB issued an October 2025 interpretive rule taking the position that the FCRA preempts state laws restricting medical-debt credit reporting. If sustained, it limits the effect of any Iowa state-level law that subsequently passes.

## Hospital charity care

Iowa has **no state statute** requiring a hospital financial-assistance policy beyond federal law. Non-profit Iowa hospitals are bound by **federal § 501(r)** (26 U.S.C. § 501(r)(4)-(6) and 26 C.F.R. § 1.501(r)-4 through -6): widely-publicized FAP, AGB caps, prohibition on extraordinary collection actions before FAP eligibility determination.

For-profit and county/municipal hospitals have no state FAP mandate. Lean on Chapter 714H deception theories and on the hospital's own posted FAP if one exists.

Iowa Code Chapter 347 (county hospitals) and Iowa Code Chapter 347A (county hospital trusts) impose general public-purpose duties on county-operated facilities, useful as background where the dispute involves a county hospital.

Use Dollar For at [dollarfor.org/state_sheet/iowa](https://dollarfor.org/state_sheet/iowa/) for screening. Iowa Legal Aid's medical-debt resource page is at [iowalegalaid.org/resource/dealing-with-medical-debt](https://iowalegalaid.org/resource/dealing-with-medical-debt/).

## Hospital lien statute

- **Citations:** **Iowa Code Chapter 582 (§§ 582.1 through 582.4)** — "Hospital Lien"
- **Sources:** [law.justia.com/codes/iowa/title-xiv/chapter-582](https://law.justia.com/codes/iowa/title-xiv/chapter-582/); statutory PDF at [legis.iowa.gov/docs/code/582.pdf](https://www.legis.iowa.gov/docs/code/582.pdf); LawServer summary at [lawserver.com/law/state/iowa/ia-code/iowa_code_chapter_582](https://www.lawserver.com/law/state/iowa/ia-code/iowa_code_chapter_582)
- **Substance:** Hospitals (and the hospital's emergency ambulance services) may file a lien for reasonable and customary charges, **only against the patient's cause of action against a third party** who caused the injury. **Not a lien on the patient's home, wages, or bank accounts.**
- **Sections at a glance:**
  - **§ 582.1** — Definitions
  - **§ 582.1A** — Nature of lien (third-party recovery only; not against workers' comp claims under Iowa Code Chapters 85, 85A, 85B)
  - **§ 582.2** — Written notice of lien (registered/certified-mail notice to patient and to all known liable parties / their insurers prior to perfection)
  - **§ 582.3** — Duration and enforcement
  - **§ 582.4** — Lien docket and recording fees
- **Critical patient protection — health-plan-first requirement:** Under § 582.1A, a hospital eligible to file a lien must first take **reasonable steps to determine whether the patient is covered under a health plan**, and if so, **all charges shall first be submitted to the health plan** prior to filing notice of lien. The lien amount is capped at the **patient's responsibility under any provider agreement between the hospital and the health plan** — i.e., the hospital cannot file a lien for chargemaster gross charges if a contracted rate would apply. **This is a meaningful Iowa-specific check on overreach.**
- **Pro-rata share of attorney fees:** A hospital that recovers under a lien must bear its **pro rata share of the legal and administrative expenses** incurred by the patient's attorney in obtaining the third-party judgment/settlement.
- **What to check on a presented lien:** Verify (1) timely written notice under § 582.2, (2) that the hospital actually submitted the charges to the health plan first under § 582.1A, (3) that the lien amount reflects the in-network/contracted patient-responsibility cap and not chargemaster gross charges, and (4) that the lien does not attempt to reach workers' comp proceeds. A defective lien is unenforceable.

## Wage garnishment

- **Statute:** **Iowa Code § 642.21** (continuing garnishment and exemption schedule); supplemented by federal Consumer Credit Protection Act, 15 U.S.C. § 1673
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a **court judgment**. Iowa's exemption schedule is **more protective than the federal floor** at low income levels — exempt amounts depend on annual debtor income (e.g., a debtor earning under $12,000/year is exempt from any wage garnishment; tiered caps apply up through higher income brackets). Federal 25%-of-disposable-earnings cap applies as a ceiling.
- **Use:** In response letters to collectors threatening garnishment without a judgment in hand, and to flag Iowa's tiered exemption when the patient's income is modest.

## Quick reference for letter rendering

When the LLM renders an Iowa-bound letter, substitute these defaults:

- **State statute (provider-side primary lever):** **Iowa Code § 714H.3 (Private Right of Action for Consumer Frauds Act)** plus **§ 714H.5** for the private right of action with treble damages and **mandatory attorney's fees**. This is Iowa's analogue to Georgia's FBPA and the strongest patient-side cite against hospitals for itemization refusals, deceptive billing, and unfounded collection conduct. Parallel cite to **§ 714.16** for AG-enforcement leverage.
- **State statute (insurer-side primary lever):** **Iowa Code § 507B.4(9) (UCSPA, cited for IID complaint)** plus a *Dolan* common-law bad-faith count in any litigation. The UCSPA itself is non-actionable, but its enumeration drives the *Dolan* tort.
- **State statute (emergency-services balance billing):** **Iowa Code § 514C.16** for OON emergency-room scenarios on state-regulated plans.
- **State insurance department (CC line):** Iowa Insurance Division, Consumer Services, 1963 Bell Avenue, Suite 100, Des Moines, IA 50315
- **State AG consumer protection (CC line):** Office of the Attorney General of Iowa, Consumer Protection Division, Hoover State Office Building, 1305 E. Walnut Street, Des Moines, IA 50319-0106
- **§ 714H.7 pre-suit notice:** When filing a Chapter 714H private action, send a copy of the petition to the AG's Consumer Protection Division at the address above at the time of filing.
- **Small-claims court name:** **Small Claims Docket of the Iowa District Court for [County] County**
- **Filing fee (in 30-day warning):** "$95 under Iowa Code § 631.6"
- **Statute of limitations (in 30-day warning):** "Iowa Code § 614.1(5) (ten years for breach of written contract)" — the long SOL is itself a leverage point worth naming.
- **For ground-ambulance balance bills:** Iowa has **no state-law protection**; rely on federal NSA Patient-Provider Dispute Resolution for self-pay/uninsured cases and on § 714H deception theories where the bill is materially inflated.
- **For provider-side disputes (vs. insurer-side):** Cite **Iowa Code § 714H.3 and § 714H.5 (private right of action with treble damages and mandatory attorney's fees)** in addition to UCC § 2-305. Chapter 714H does not require a 30-day ante-litem demand; the kit's standard 30-day warning letter serves to create a cure-opportunity record.

## Key Iowa-specific advantages

Worth keeping in mind when triaging an Iowa patient's bills:

1. **Common-law bad-faith tort (*Dolan*)** — Iowa is one of the minority of states with a judicially-recognized first-party bad-faith tort, putting punitive damages and consequential damages on the table beyond contract recovery. Materially stronger than Georgia's purely statutory § 33-4-6 framework for the right facts.
2. **Chapter 714H private right of action with treble damages and mandatory attorney's fees** — Iowa Code § 714H.5 provides the same kind of fee-shifting and multiplier remedy as Georgia's FBPA, reaching the hospital directly (not just third-party collectors). The "shall award" language for attorney's fees is meaningfully stronger than Georgia's "may award."
3. **Ten-year written-contract SOL (§ 614.1(5))** — among the longest in the country. Useful offensively against hospitals on overcharge and AGB-violation contract theories; a defensive headwind when the hospital is suing the patient on an old signed financial-responsibility form.
4. **Small-claims corporate non-attorney rule (§ 631.14)** — no dollar threshold restricting corporate defendants from appearing through an officer or employee. Mirrors Georgia's Magistrate Court advantage and is meaningfully better than Indiana's $1,500 cap. The economic leverage in small claims is high because the corporate side knows it does not get to bring expensive counsel without losing money on the appearance.
5. **Hospital-lien insurer-first cap (§ 582.1A)** — Iowa law explicitly caps lien amounts at the contracted in-network patient-responsibility figure and requires the hospital to bill the health plan first. This is a real check that does not exist in many other states and is a frequent point of attack on overreaching liens.
6. **Iowa wage-garnishment exemption schedule (§ 642.21)** — more protective than the federal floor at low income brackets; debtors below $12,000/year are fully exempt.

## Iowa-specific weaknesses to flag

1. **No automatic itemized-statement duty** — Iowa has no analogue to Georgia's automatic 6-business-day itemization right under O.C.G.A. § 10-1-393(b)(14). The patient must request the itemization in writing, and the leverage comes from layered federal § 501(r), Medicare CoP, Iowa hospital licensure regulations, and Chapter 714H deception theories rather than a single bright-line statute.
2. **UCSPA is non-actionable** — Iowa Code Chapter 507B cannot be pled as a standalone count. The *Dolan* tort is the route, with the "fairly debatable" standard providing a meaningful brake.
3. **Narrow state surprise-billing protection** — § 514C.16 covers ER scenarios only; no general OON-at-INN ancillary-services protection like Georgia's § 33-20E-1 et seq. Federal NSA is the primary protection for non-ER surprise scenarios.
4. **No ground-ambulance balance-billing protection** — Iowa has not closed the federal NSA's ground-ambulance gap. Patients are fully exposed for OON ground-ambulance bills.
5. **No state credit-reporting restriction** — Iowa relies on FCRA and voluntary bureau changes; no codified state ban on medical-debt furnishing as of this writing.
6. **No state charity-care mandate** — federal § 501(r) is the floor; for-profit and county/municipal hospitals have no state FAP duty.
