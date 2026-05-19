# Massachusetts state pack

The fully-worked state-law layer for Massachusetts patients. The LLM uses this when the patient's state is Massachusetts. Tennessee equivalent at [`laws_state_tn.md`](laws_state_tn.md); Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md); New York equivalent at [`laws_state_ny.md`](laws_state_ny.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Three things make Massachusetts' patient-side leverage unusually strong:

1. **Chapter 93A is the single most powerful UDAP statute in the country for medical-billing disputes.** M.G.L. c. 93A, § 9 requires a **mandatory 30-day written demand letter** before suit. If the recipient does not make a "reasonable" written tender within 30 days, and the court later finds the underlying conduct was willful or knowing, the court **shall award not less than two times and up to three times actual damages**, plus **reasonable attorney's fees and costs**. The treble-damages mechanic is automatic on a finding of willfulness — it is not a discretionary uplift. This is the headline lever in every MA dispute.
2. **A Chapter 176D, § 3(9) violation by an insurer is a per se violation of Chapter 93A** for consumer plaintiffs under § 9. Massachusetts is one of the few states where insurance unfair-claims-settlement practices come bundled with a private right of action, mandatory demand mechanic, and statutory multipliers.
3. **Near-universal coverage under Chapter 58 (2006)** shifts the typical dispute profile. Most MA medical-bill cases are insurance-side disputes (coverage denials, balance bills, surprise charges, EOB miscalculations) rather than uninsured-patient charity-care cases. The kit's workflows should default to "patient has coverage" and route the patient to Chapter 93A / 176D leverage first.

Treat the Chapter 93A demand-letter mechanic as the single most important MA-specific cite in any dispute letter.

## Hospital itemization right

- **Statute:** **M.G.L. c. 111, § 70E** — Patients' and Residents' Rights (the Massachusetts Patient Bill of Rights)
- **Source:** [malegislature.gov/Laws/GeneralLaws/PartI/TitleXVI/Chapter111/Section70E](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXVI/Chapter111/Section70E); [mass.gov/info-details/mass-general-laws-c111-ss-70e](https://www.mass.gov/info-details/mass-general-laws-c111-ss-70e); [law.justia.com/codes/massachusetts/part-i/title-xvi/chapter-111/section-70e](https://law.justia.com/codes/massachusetts/part-i/title-xvi/chapter-111/section-70e/)
- **What it requires:**
  - On **reasonable request**, the facility must provide an **itemized bill** reflecting laboratory charges, pharmaceutical charges, and third-party credits, with a right to examine an explanation of the bill regardless of source of payment.
  - The patient may also obtain a copy of any itemized bill or statement of charges the facility submitted to a third party, and direct that a copy be sent to the patient's attending physician.
- **Scope:** "Facility" is defined broadly to include hospitals, clinics, infirmaries, convalescent and nursing homes, rest homes, charitable homes for the aged, and state-operated veterans' homes. § 70E reaches both inpatient and outpatient hospital settings; freestanding physician offices not licensed as a "facility" are outside § 70E and fall back to federal Good Faith Estimate and price-transparency rules.
- **Trigger:** request-based — unlike Georgia's automatic 6-business-day duty, MA requires the patient to make a "reasonable request." Send the request in writing (certified, return receipt) to crystallize the trigger date.
- **Private right of action:** **Yes.** § 70E expressly states that any person whose rights under the section are violated may bring a civil action under M.G.L. c. 231, §§ 60B–60E, **in addition to any other action allowed by law or regulation**. That phrase "in addition to" preserves a parallel Chapter 93A claim where the violation also involved unfair or deceptive billing conduct.
- **Caveat — sections 70F and 70G are different:** § 70F governs HIV testing consent and confidentiality; § 70G governs genetic-information confidentiality. Neither addresses itemized billing. Use § 70E.
- **ERISA:** Not preempted — regulates the provider/facility, not the plan.

Use § 70E as the citation in `templates/letter_itemization_request.md` for any Massachusetts patient.

## Unfair Claim Settlement Practices Act

- **Statute:** **M.G.L. c. 176D, § 3(9)** — fourteen enumerated unfair claim settlement practices
- **Sources:** [malegislature.gov/Laws/GeneralLaws/PartI/TitleXXII/Chapter176D/Section3](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXXII/Chapter176d/Section3); [codes.findlaw.com/ma/part-i-administration-of-the-government-ch-1-182/ma-gen-laws-ch-176d-sect-3](https://codes.findlaw.com/ma/part-i-administration-of-the-government-ch-1-182/ma-gen-laws-ch-176d-sect-3/)
- **Substance:** Prohibits insurers (and entities "in the business of insurance") from misrepresenting policy provisions, failing to acknowledge or act reasonably promptly on claims, failing to adopt reasonable claim-investigation standards, refusing to pay without conducting a reasonable investigation, failing to affirm or deny coverage within a reasonable time after proof of loss, and **failing to effectuate prompt, fair, and equitable settlements of claims in which liability has become reasonably clear**.
- **Private right of action — via Chapter 93A:** **Yes, for consumers under c. 93A, § 9.** Massachusetts appellate courts have held that a violation of c. 176D, § 3(9) is a per se violation of Chapter 93A when asserted by a consumer plaintiff under § 9. The consumer does not need to independently prove an unfair or deceptive practice under c. 93A, § 2 — proving the § 3(9) violation suffices.
- **Business plaintiffs (§ 11) differ:** Business plaintiffs proceeding under c. 93A, § 11 must independently establish a § 2 violation; a § 3(9) violation alone is not enough. This distinction matters only when the patient is suing through a business entity (rare in medical-bill disputes).
- **Procedural prerequisite:** the c. 93A, § 9 demand letter (see next section). § 176D claims and § 93A claims are pleaded together and demand-lettered together.
- **ERISA preemption:** § 176D / § 93A claims against self-funded ERISA employer plans are preempted. Fully insured plans, Medicare supplement, Medicaid managed care, individual/marketplace plans, and ACA-Marketplace plans purchased through the Health Connector are all in play.

## Chapter 93A — Consumer Protection Act

- **Statute:** **M.G.L. c. 93A, § 9** — civil actions and remedies for consumers (substantive prohibition at § 2)
- **Sources:** [malegislature.gov/Laws/GeneralLaws/PartI/TitleXV/Chapter93A/Section9](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXV/Chapter93A/Section9); [law.justia.com/codes/massachusetts/part-i/title-xv/chapter-93a/section-9](https://law.justia.com/codes/massachusetts/part-i/title-xv/chapter-93a/section-9/); [malegislature.gov/Laws/GeneralLaws/PartI/TitleXV/Chapter93A](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXV/Chapter93A)
- **Substance:** Chapter 93A, § 2 prohibits "unfair methods of competition and unfair or deceptive acts or practices in the conduct of any trade or commerce." Healthcare billing — hospitals, physician practices, ambulance services, debt collectors, and insurers — is "trade or commerce" under § 2. The Attorney General has rule-making authority under § 2(c), and a violation of those rules (940 CMR series) is a per se § 2 violation.
- **The mandatory demand-letter mechanic — § 9(3):**
  - A consumer plaintiff **must** send a written demand for relief to each prospective defendant **at least 30 days before filing suit**.
  - The letter must (a) identify the claimant, (b) reasonably describe the unfair or deceptive act or practice, and (c) describe the injury suffered and the relief demanded.
  - The recipient has **30 days from receipt** to make a written tender of settlement.
  - **No demand letter is required** if the prospective defendant has no place of business or assets within Massachusetts, or for counterclaims/cross-claims.
- **Damages — § 9(3):**
  - **Floor:** the greater of actual damages or **$25**.
  - **Multiplier:** if the court finds that the act or practice was a **willful or knowing** violation of § 2, **or** that **the refusal to grant relief upon demand was made in bad faith with knowledge or reason to know** that the conduct violated § 2, the court **shall** award **not less than two and up to three times** actual damages. The statute uses "shall" — the multiplier is mandatory, not discretionary, once willfulness or bad-faith refusal is found.
  - **Attorney's fees and costs:** mandatory for a prevailing claimant under § 9(4), regardless of whether multipliers are awarded.
- **Settlement-tender shield — § 9(3):** A defendant that makes a **reasonable written tender** within 30 days, and whose tender is rejected, may file the tender and an affidavit in the subsequent action and **cap recovery at the relief tendered** if the court later finds the tender was reasonable in relation to the actual injury. This is why a well-drafted demand letter quantifies damages tightly — a vague demand invites a token tender that caps the case.
- **Statute of limitations for § 93A actions:** **4 years** under M.G.L. c. 260, § 5A (separate from the 6-year contract limit; see "Statute of limitations" below).
- **ERISA:** § 93A claims against self-funded ERISA employer plans are preempted; against providers and against fully insured carriers they are not.

This is **the** Massachusetts lever. In any letter to a MA hospital, billing department, debt collector, or insurer, the 30-day Chapter 93A demand letter is the primary mechanism — it is cheap, statutory, and creates immediate exposure to mandatory treble damages and fee-shifting if ignored or answered in bad faith.

## Balance billing — surprise-bill protections

- **Statutes:** **M.G.L. c. 176O, § 6** (cost-sharing for OON emergency services), companion provisions throughout c. 176O, federal No Surprises Act layered on top, and Division of Insurance Bulletin 2022-02 / 2022-03 implementing federal NSA in MA.
- **Sources:** [malegislature.gov/Laws/GeneralLaws/PartI/TitleXXII/Chapter176O](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXXII/Chapter176O); [mass.gov/info-details/federal-no-surprises-act-resources-and-consumer-disclosures](https://www.mass.gov/info-details/federal-no-surprises-act-resources-and-consumer-disclosures)
- **What state law provides:**
  - HMO and PPO carriers in MA must pay a "reasonable" amount for OON emergency services and must hold the enrollee harmless for amounts beyond in-network cost-share.
  - Provider directory accuracy obligations live at c. 176O, § 28 (this section addresses directory contents, audits, customer-service contact, and updates — **not** standalone surprise-billing protections; the headline surprise-billing rule is in § 6 plus the layered federal NSA).
  - The Massachusetts Health Policy Commission and Division of Insurance jointly oversee provider-payer dispute resolution.
- **What federal NSA adds:** the federal No Surprises Act (effective Jan 1, 2022) is broader than the pre-existing MA framework for emergency services, OON providers at in-network facilities, and air ambulance. For fully insured MA plans and ERISA self-funded plans alike, federal NSA protections **layer on top of** MA law — they do not displace it.
- **Caveat — § 28 is the wrong cite for surprise billing:** c. 176O, § 28 is about provider-directory accuracy. The substantive cost-sharing and hold-harmless rules sit elsewhere in c. 176O (particularly § 6). When drafting MA surprise-bill letters, cite **c. 176O, § 6** and the **federal NSA (45 C.F.R. Part 149)** together. § 28 only matters when the dispute turns on whether the carrier mis-listed a provider as in-network (a frequent driver of surprise bills in practice).
- **ERISA:** c. 176O does not reach self-funded ERISA employer plans. Federal NSA does.

## Regulatory agencies

### Massachusetts Division of Insurance (DOI)

- **Online complaint:** [mass.gov/how-to/filing-an-insurance-complaint](https://www.mass.gov/how-to/filing-an-insurance-complaint)
- **Phone:** Consumer Service Unit **(617) 521-7794**; toll-free **1-877-563-4467**
- **Email:** CSSComplaints@mass.gov
- **Mail:**
  > Office of Consumer Affairs and Business Regulation
  > Division of Insurance, Consumer Service Section
  > 1000 Washington Street, Suite 810
  > Boston, MA 02118-6200
- **Authority:** all insurance companies licensed in Massachusetts, including fully-insured health insurers, HMOs, PPOs, Medicare supplement, and the carriers that participate in the Health Connector marketplace. Administers c. 176D and c. 176O. **No authority over self-funded ERISA plans** (route to U.S. DOL EBSA at 1-866-444-3272), and does not regulate providers, hospitals, or debt collectors (route to the Attorney General).

### Massachusetts Attorney General — Consumer Advocacy & Response Division and Health Care Division

- **Consumer Hotline (CARD):** **(617) 727-8400**, Monday–Friday 8:00 a.m. – 4:00 p.m.
- **Health Care Helpline (Health Care Division):** **(888) 830-6277**, Monday/Wednesday/Friday 9:00 a.m. – 2:00 p.m.; offers free mediation in appropriate cases
- **Online complaint:** [mass.gov/how-to/file-a-consumer-complaint](https://www.mass.gov/how-to/file-a-consumer-complaint); medical-billing track at [mass.gov/how-to/file-a-health-care-complaint](https://www.mass.gov/how-to/file-a-health-care-complaint)
- **Mail:**
  > Office of the Attorney General
  > Consumer Advocacy & Response Division
  > One Ashburton Place, 18th Floor
  > Boston, MA 02108
- **Authority:** enforces **Chapter 93A** against any entity engaged in trade or commerce, including hospitals, physician practices, ambulance companies, billing companies, and debt collectors. The AG's Health Care Division is unusually active — it has brought repeated public enforcement actions against hospitals and billing companies for deceptive billing, surprise charges, and aggressive collection practices, and runs a free mediation program. **CC the AG's Health Care Division on any MA medical-billing dispute letter** — this materially escalates leverage with the provider.

## Small claims court — District Court Small Claims Session

- **Court name:** **District Court Small Claims Session** (or **Boston Municipal Court Small Claims Session** for claims in Boston); housing-related small claims may also be filed in the Housing Court.
- **Jurisdictional limit:** **$7,000**, codified at **M.G.L. c. 218, § 21**
- **Source:** [malegislature.gov/Laws/GeneralLaws/PartIII/TitleI/Chapter218/Section21](https://malegislature.gov/Laws/GeneralLaws/PartIII/TitleI/Chapter218/Section21); [mass.gov/info-details/small-claims-court](https://www.mass.gov/info-details/small-claims-court)
- **Filing fees:** approximately **$40 to $150 depending on damages sought** — $40 for claims under $500, scaling up to $150 for claims of $5,001–$7,000. Service of process via the court clerk by first-class mail is included in the filing fee.
- **Attorney rules:** permitted, not required. Designed for pro se litigants — simplified pleadings, no formal discovery, relaxed evidence rules. A clerk-magistrate (not a judge) usually presides at the first hearing.
- **Important exceptions to the $7,000 cap (§ 21):**
  - No dollar limit for **property damage caused by a motor vehicle**.
  - The **$7,000 cap is on actual damages claimed**, but the **judgment** may exceed $7,000 when the case is brought under Chapter 93A and the court awards **double or treble damages plus attorney's fees** on a base claim that did not exceed $7,000. This is statutorily preserved by § 21 and is a Massachusetts-specific advantage: a $5,000 Chapter 93A claim can yield a $15,000 judgment plus fees in small claims.
- **Jury trial:** plaintiff waives jury trial by filing in small claims. The **defendant** may claim a jury trial under § 23, in which case the case transfers to the regular civil docket. Jury-trial right belongs to the defendant in this forum.
- **Appeal:** plaintiff has no appeal as of right from an adverse small-claims judgment (the plaintiff chose the forum). The defendant may appeal for trial *de novo*.

## Statute of limitations

- **Contract actions (written or oral) — 6 years:** M.G.L. c. 260, § 2 — "Actions of contract … shall, except as otherwise provided, be commenced only within six years next after the cause of action accrues." Applies to credit-card debt, medical-bill collection actions, and oral or written hospital-financial-responsibility agreements.
- **Chapter 93A actions — 4 years:** M.G.L. c. 260, § 5A.
- **Tort actions (non-medical-malpractice) — 3 years:** M.G.L. c. 260, § 2A.
- **Contracts under seal — 20 years:** M.G.L. c. 260, § 1.
- **Sources:** [malegislature.gov/Laws/GeneralLaws/PartIII/TitleV/Chapter260/Section2](https://malegislature.gov/Laws/GeneralLaws/PartIII/TitleV/Chapter260/Section2); [law.justia.com/codes/massachusetts/part-iii/title-v/chapter-260/section-2](https://law.justia.com/codes/massachusetts/part-iii/title-v/chapter-260/section-2/)

Most hospital admissions involve a signed financial-responsibility form — a written contract under c. 260, § 2 (6 years from breach, typically the day payment was due and not made). A partial payment or written acknowledgment may re-start the limitations clock under common-law principles. **Do not advise a patient to make a partial payment on a time-barred MA medical debt without legal advice.** Note also that the four-year c. 93A clock can expire before the underlying 6-year contract clock — a patient who waits 5 years to assert a Chapter 93A claim about a hospital's deceptive billing in year 1 may lose the 93A treble-damages lever even though the underlying debt is still timely.

## Ground-ambulance balance billing

**Massachusetts has not enacted a comprehensive ground-ambulance balance-billing prohibition as of 2026-05-18.** Multiple bills have been filed across recent sessions — H.1261 ("An Act protecting patients from surprise bills related to emergency ambulance service") was reintroduced in the 194th General Court; H.5042 is a related vehicle. None had been enacted as of this writing.

Current MA-specific ground-ambulance protections are partial and primarily reach **uninsured/self-pay patients and municipally regulated rates** rather than insured-patient balance bills:

- **Uninsured/self-pay:** under existing MA practice and various pending bills, providers serving uninsured patients cannot demand more than the CMS-published Medicare ambulance rate.
- **Municipal rate-setting:** municipalities set ambulance rates and report them to the Center for Health Information and Analysis (CHIA), which publishes them annually. Carriers that pay at the municipal-established rate are deemed to have paid in full for that emergency transport.
- **Collection-practice limits in pending legislation:** the bills would bar wage garnishment, primary-residence liens, credit-bureau reporting, and lawsuits as collection mechanisms for emergency ambulance bills. **Confirm enactment status before relying on these.**

**Federal No Surprises Act explicitly excludes ground ambulance**, and Massachusetts has not (yet) closed that gap. For now, an insured MA patient hit with a ground-ambulance balance bill has thinner leverage than the equivalent patient in Georgia, New York, or Illinois — all of which have enacted state-level ground-ambulance protections. The strongest available lever in MA is to attack the bill via **Chapter 93A** (unfair or deceptive billing where charges materially exceed reasonable value or municipal rate) and to file a DOI complaint against the patient's carrier under **c. 176D**.

## Credit reporting

**Massachusetts has not enacted a medical-debt credit-reporting ban as of 2026-05-18.** Bills (H.419, H.4073, H.4809) are pending in the 194th General Court; Governor Healey announced regulatory action in late 2024 directing the Division of Banks and Commissioner of Insurance to file regulations restricting medical-debt credit reporting. As of this writing, the regulations are pending and not yet final.

For now, Massachusetts patients rely on:

- The 2022-2023 voluntary changes by Equifax/Experian/TransUnion (paid medical debt removed; balances under $500 not reported; 1-year delay before reporting unpaid medical debt).
- **Federal FCRA dispute rights** (15 U.S.C. §§ 1681i, 1681s-2).
- **Federal CFPB action**: the CFPB finalized a rule in January 2025 banning medical debt from credit reports nationally; that rule has been subject to legal challenge. Status as of 2026-05-18: **verify before relying on it** — the regulatory landscape is unsettled.
- **State Chapter 93A** for furnishing demonstrably false or deceptive medical-debt information to a CRA — pair with a federal FCRA § 1681s-2 claim against the furnisher.

When Massachusetts passes a clean medical-debt credit-reporting ban, update this section. Until then, treat MA as **no state-specific protection** beyond what federal law and voluntary CRA policy provide.

## Hospital charity care — Health Safety Net

- **Statutory basis:** **M.G.L. c. 118E, §§ 64–69** (Health Safety Net Trust Fund); MassHealth administrative regulations at 101 CMR 613; HSN eligibility regulations at 101 CMR 613.04 and 614. The frequently-mis-cited "§ 9" of c. 118E is the **MassHealth eligibility** statute, not the HSN charge-care statute; the HSN enabling provisions sit at §§ 64–69.
- **Sources:** [malegislature.gov/Laws/GeneralLaws/PartI/TitleXVII/Chapter118E](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXVII/Chapter118E); [mass.gov/info-details/eligibility-for-health-care-benefits-for-masshealth-the-health-safety-net-and-childrens-medical-security-plan](https://www.mass.gov/info-details/eligibility-for-health-care-benefits-for-masshealth-the-health-safety-net-and-childrens-medical-security-plan)
- **Substance:** The Health Safety Net reimburses acute hospitals and community health centers for medically necessary services provided to **eligible uninsured and underinsured Massachusetts residents** with family income **below 400% of the federal poverty level**, plus a medical-hardship pathway for higher-income patients with catastrophic expenses.
- **Mandatory screening:** hospitals and community health centers **must screen each applicant for HSN reimbursement** for other coverage sources (MassHealth, ConnectorCare, employer coverage) and document the result. If the patient is potentially MassHealth-eligible (c. 118E, § 9A), the hospital must assist with the application. This screening obligation is itself a leverage point — a hospital that failed to screen the patient before sending a bill to collections has, in the kit's view, conducted "unfair or deceptive" billing under c. 93A.
- **Medical hardship pathway:** even patients above 400% FPL can qualify for partial relief if medical expenses exceed a sliding-scale percentage of income (typically 7.5%–40% of countable income, depending on income tier).
- **How it differs from a federal-501(r) charity-care policy:** HSN is a **state-administered single program** funded by an assessment on insurers and hospitals, not a hospital-by-hospital charity-care policy. Non-profit hospitals also remain bound by IRS § 501(r); for-profit and state-operated facilities sit only inside HSN.
- **Use:** Dollar For at [dollarfor.org/state_sheet/massachusetts](https://dollarfor.org/state_sheet/massachusetts/) screens for HSN and individual-hospital FAPs.

## Hospital lien statute

- **Statutes:** **M.G.L. c. 111, §§ 70A–70B** — hospital and HMO liens on the patient's tort recovery against a third-party tortfeasor
- **Sources:** [malegislature.gov/Laws/GeneralLaws/PartI/TitleXVI/Chapter111/Section70A](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXVI/Chapter111/Section70A); [law.justia.com/codes/massachusetts/part-i/title-xvi/chapter-111/section-70a](https://law.justia.com/codes/massachusetts/part-i/title-xvi/chapter-111/section-70a/)
- **Substance:** A hospital or HMO that furnished medical services to a person injured in an accident (not covered by workers' compensation) has a lien for **reasonable and necessary charges** against the **net amount payable to the injured person from any damages** recovered from the third party who caused the injury.
- **Critical scope limits:**
  - The lien attaches **only to the patient's tort recovery against the third-party tortfeasor**. **Not** a lien on the patient's home, wages, or bank accounts.
  - Does not apply where the patient's injury is covered by workers' compensation.
- **Perfection — § 70B requirements:**
  - Hospital must file a written notice containing the injured person's name and address, the accident date, and the name of the alleged liable party.
  - Notice must be served by certified mail on the injured person and on the defendant (or the defendant's insurer) **before** settlement payout.
  - A lien not properly perfected before disbursement is generally unenforceable against the settlement funds, though the underlying debt remains.
- **Billed-charges versus negotiated-rate tactic:** hospitals often perfect c. 111 § 70A liens at full "chargemaster" rates rather than the much lower negotiated rate the hospital would have accepted from the patient's health insurer. Push back hard on this — request an itemized statement (c. 111 § 70E), require the hospital to first bill the patient's insurer at the negotiated rate (no MA statute mandates insurer-first, but the practice is increasingly required by hospital-FAP policies and is a viable c. 93A "unfair practice" argument when the lien is for inflated retail rates).

## Massachusetts Health Reform Act — Chapter 58 of the Acts of 2006

- **Source:** [malegislature.gov/Laws/SessionLaws/Acts/2006/Chapter58](https://malegislature.gov/Laws/SessionLaws/Acts/2006/Chapter58); [mahealthconnector.org/20-years-of-chapter-58-brief](https://www.mahealthconnector.org/20-years-of-chapter-58-brief)
- **Effect:** Established the Health Connector (the state's individual-market marketplace), expanded MassHealth eligibility to ~300% FPL for children, created Commonwealth Care subsidies, and imposed an individual mandate. Massachusetts has the highest insured rate in the country — approximately 97-98% of residents have coverage.
- **How it affects the kit's workflows:**
  - **Default presumption:** a MA patient with a medical bill **has insurance**. Workflows should start with the EOB analysis path, not the uninsured-patient path.
  - **Charity-care is narrow but real:** HSN catches the uninsured 2-3% plus the underinsured. Workflows should screen for HSN eligibility before defaulting to hospital-by-hospital FAPs.
  - **Insurance-side disputes dominate:** the typical MA case is denied coverage, balance billing despite in-network status, EOB miscalculation, or out-of-pocket maximum mis-tracking. The Chapter 93A + Chapter 176D combination is the headline lever.
  - **Connector / ConnectorCare plans are fully insured** and regulated by the MA Division of Insurance — they are **not** ERISA-preempted. Cite c. 176D and file DOI complaints freely for Connector plans.
- **ConnectorCare premium and cost-sharing subsidies:** patients up to 500% FPL may qualify; an uninsured-looking bill may actually be a coverage-gap issue, where re-enrollment through the Connector is the better fix than a charity-care application.

## Wage garnishment

- **Statute:** **M.G.L. c. 246, § 28**
- **Substance:** A medical-bill creditor cannot garnish wages without first obtaining a **court judgment**. Post-judgment, MA caps garnishment at the **lesser of** (a) **15% of weekly gross wages** or (b) the amount by which weekly disposable earnings exceed **50 times the state or federal minimum wage** (whichever is greater). The MA cap is **stricter than the federal CCPA 25% cap** — Massachusetts wages are better protected than the federal floor.
- **Use:** in response letters to collectors threatening garnishment without a judgment in hand. Also valuable to mention in a settlement negotiation — the actual recoverable percentage is much lower in MA than the collector's letter implies.

## Quick reference for letter rendering

When the LLM renders a Massachusetts-bound letter, substitute these defaults:

- **State statute (itemization right):** **M.G.L. c. 111, § 70E** — itemized bill on reasonable request; private right of action under c. 231, §§ 60B–60E "in addition to" any other remedy.
- **State insurance department (CC line):** Division of Insurance, Consumer Service Section, 1000 Washington Street, Suite 810, Boston, MA 02118-6200 ([mass.gov/how-to/filing-an-insurance-complaint](https://www.mass.gov/how-to/filing-an-insurance-complaint)); CSSComplaints@mass.gov
- **State AG consumer protection (CC line):** Office of the Attorney General, Consumer Advocacy & Response Division, One Ashburton Place, 18th Floor, Boston, MA 02108; Health Care Helpline (888) 830-6277 for billing disputes specifically.
- **Small-claims court name:** **District Court Small Claims Session, [Division of patient's home county]** (or **Boston Municipal Court Small Claims Session** in Suffolk County / Boston).
- **Filing fee (in 30-day warning):** "$40–$150 depending on amount claimed"
- **Statute of limitations (in 30-day warning):** "M.G.L. c. 260, § 2 (six years for breach of written contract); M.G.L. c. 260, § 5A (four years for Chapter 93A claims)"
- **For insurer disputes:** Cite **M.G.L. c. 176D, § 3(9)** plus **M.G.L. c. 93A, § 9** together. The 30-day demand letter is mandatory and is satisfied by the kit's standard 30-day warning letter, provided it is sent **certified mail, return receipt requested**, identifies the unfair practice, describes the injury, and demands specific relief.
- **For provider/hospital disputes:** Cite **M.G.L. c. 93A, § 9** directly (no separate § 176D hook required — § 93A § 2 reaches "trade or commerce" generally, which includes hospital billing). Same 30-day mandatory demand mechanic.
- **For collection-agency disputes:** Cite **M.G.L. c. 93A, § 9** plus the AG's debt-collection regulations at **940 CMR 7.00**. Violations of 940 CMR 7.00 are per se § 93A § 2 violations.
- **Treble-damages framing:** Every MA dispute letter should put the recipient on explicit notice that "failure to respond with a reasonable tender within 30 days exposes you to mandatory double or treble damages plus attorney's fees under M.G.L. c. 93A, § 9(3) and (4) upon a court finding of willfulness or bad-faith refusal." This sentence does the work — it is statutorily accurate, not bluster, and it routinely moves billing departments that ignore non-MA dispute letters.

## Key Massachusetts-specific advantages

Worth keeping in mind when triaging a MA patient's bills:

1. **Chapter 93A mandatory 30-day demand + mandatory treble damages.** This is the single most powerful UDAP mechanic in any U.S. state. The multiplier is "shall award not less than two times" on a willfulness finding — not discretionary. The demand-letter procedure converts every MA dispute into a structured negotiation with a hard 30-day clock and a statutory hammer. Use this aggressively.
2. **Mandatory attorney's-fee shifting under c. 93A, § 9(4).** Fee recovery is statutory, not discretionary. This makes plaintiffs' counsel willing to take MA medical-billing cases that would be uneconomic in fee-American-Rule states. Even a $4,000 dispute is litigation-viable in MA where it would not be in New York.
3. **Insurance unfair-claims-settlement practices come with a private right of action.** c. 176D § 3(9) violations are per se c. 93A violations for consumers. Massachusetts is one of the few states where the patient does not have to first persuade a regulator to act before suing a misbehaving carrier.
4. **AG's Health Care Division actively mediates billing disputes for free.** The (888) 830-6277 helpline and free mediation program is unusual nationally — most state AGs route to private mediation or just acknowledge complaints. The MA AG has brought public enforcement actions against hospitals for surprise billing, balance billing, and aggressive collection, and CCing the AG materially escalates leverage.
5. **Small-claims c. 93A multiplier.** Under c. 218, § 21, a $7,000 small-claims case under Chapter 93A can yield a judgment exceeding $7,000 once doubling/trebling and fees are applied. Massachusetts is one of the few states where the small-claims forum does not cap the practical recovery on a c. 93A claim.
6. **Near-universal coverage shifts the kit's default workflow.** Most MA cases are insurance-side (denials, balance bills, EOB errors) rather than uninsured-patient charity-care. The kit's MA branch should start with EOB analysis, not financial-assistance applications. Reserve the HSN/MassHealth track for the ~2-3% genuinely uninsured slice.
7. **Stricter wage-garnishment protection (15% / 50×MW) than the federal CCPA 25% floor.** Mention this in any collector-response letter — it caps practical pressure even after a judgment.
8. **Caveat — Massachusetts has no ground-ambulance protection yet.** This is the one notable gap compared to Georgia, New York, and Illinois. Watch H.1261 and successor bills; until enactment, route ground-ambulance disputes through c. 93A (unfair-billing theory) plus a DOI complaint against the carrier under c. 176D, § 3(9).
