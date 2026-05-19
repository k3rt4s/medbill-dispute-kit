# Washington state pack

The fully-worked state-law layer for Washington patients. The LLM uses this when the patient's state is Washington. Georgia equivalent at [`laws_state_ga.md`](/k3rt4s/medbill-dispute-kit/blob/main/references/laws_state_ga.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Three things make Washington's patient-side leverage unusually strong:

1.  The **Charity Care Act is the most generous in the country** — Tier 1 (large) hospitals must provide **100% free care** to patients up to **300% of the federal poverty level** and sliding-scale discounts up to **400% FPL**, codified at RCW 70.170.060 and expanded by HB 1616 (2022).
2.  The **Insurance Fair Conduct Act** (RCW 48.30.015) gives any first-party insured an explicit **private right of action with treble damages and attorney's fees** for an unreasonable denial of coverage or benefits — patient-favorable in a way most states' UCSPAs are not.
3.  The **Balance Billing Protection Act covers ground ambulance** (effective Jan 1, 2025 via SSB 5986), **all medical-debt credit reporting is banned** (RCW 70.54.475, 2025), and the **Consumer Protection Act** (RCW 19.86) provides treble damages plus attorney's fees as a backstop for almost every billing-side bad act. Washington's enforcement stack is layered in a way few other states match.

## Hospital itemized statement and patient-billing rights

*   **Statute:** **RCW 70.41.400** — patient billing, written statement, medical-debt reporting prohibition, CPA hook
*   **Sources:** [app.leg.wa.gov/RCW/default.aspx?cite=70.41.400](https://app.leg.wa.gov/RCW/default.aspx?cite=70.41.400); estimate right at [app.leg.wa.gov/rcw/default.aspx?cite=70.01.030](https://app.leg.wa.gov/rcw/default.aspx?cite=70.01.030); charity-care notice baked into hospital billing statements via RCW 70.170.060
*   **What it requires:**
    *   Prior to or upon discharge, a hospital must furnish each inpatient a written statement identifying every physician group or professional partner that may bill separately, with billing-inquiry phone numbers on the first page of every hospital billing statement.
    *   Under RCW 70.01.030, every health care provider and facility must, **upon patient request**, provide an estimate of fees and charges for a specific service, visit, or stay. Hospitals licensed under chapter 70.41 RCW may satisfy this by providing the RCW 70.41.400 statement plus contact information.
    *   Itemization in the strict CPT/HCPCS line-item sense is not codified as an automatic duty in RCW 70.41 (Washington has no analog to Georgia's automatic-6-business-day rule). The lever is the **collection-side disclosure**: any medical-debt collector contacting a Washington consumer since 2019 must disclose, in writing, the consumer's right to request an itemized statement, and **collection must pause** until the itemized statement is delivered (Collection Agency Act, chapter 19.16 RCW; AGO and OIC enforcement).
*   **Scope:** Hospitals licensed under chapter 70.41 RCW. Outpatient and ambulatory-surgery providers fall under RCW 70.01.030 and Title 18 RCW provider licensing rules.
*   **Private right of action:** Yes, indirectly. RCW 70.41.400(3) and RCW 70.54.475(2) expressly declare any violation an unfair or deceptive act under chapter 19.86 RCW (Consumer Protection Act), unlocking **treble damages (up to $25,000) plus reasonable attorney's fees** under RCW 19.86.090.
*   **ERISA:** Not preempted — regulates the provider, not the plan.

## CPA private right of action

*   **Statute:** **RCW 19.86.090** — civil action for damages, treble damages, attorney's fees, under the Consumer Protection Act (chapter 19.86 RCW)
*   **Source:** [app.leg.wa.gov/rcw/default.aspx?cite=19.86.090](https://app.leg.wa.gov/rcw/default.aspx?cite=19.86.090)
*   **Substance:** Any person injured in business or property by an unfair or deceptive act in trade or commerce may sue in superior court (or district court, with the same fee-shifting) to recover actual damages, **plus discretionary treble damages capped at $25,000**, **plus reasonable attorney's fees and costs**. The five-element CPA test (Hangman Ridge) requires: (1) unfair or deceptive act, (2) in trade or commerce, (3) public-interest impact, (4) injury to business or property, (5) causation.
*   **Why it matters for medical bills:**
    *   The legislature has expressly declared multiple billing-side acts to be unfair or deceptive per se: medical-debt credit reporting (RCW 70.41.400, 70.54.475), sale or assignment of medical debt within 120 days of first bill (RCW 70.54.470), and most collection-agency rule violations (chapter 19.16 RCW). Per-se status removes the public-interest element from dispute.
    *   The CPA reaches **original creditors** — the hospital itself, not only third-party collectors — and is layered on top of the federal FDCPA.
*   **Procedural notes:** No ante-litem demand requirement under the CPA itself. The kit's standard 30-day warning letter is best practice, not a statutory prerequisite.

## Unfair Claims Settlement Practices Regulation

*   **Regulation:** **WAC 284-30-330** — specific unfair claims settlement practices defined (issued under the Insurance Commissioner's authority in RCW 48.30.010)
*   **Sources:** [app.leg.wa.gov/wac/default.aspx?cite=284-30-330](https://app.leg.wa.gov/wac/default.aspx?cite=284-30-330); LII mirror at [law.cornell.edu/regulations/washington/WAC-284-30-330](https://www.law.cornell.edu/regulations/washington/WAC-284-30-330)
*   **Substance:** Defines 19+ specific unfair practices an insurer cannot engage in: misrepresenting policy provisions, failing to acknowledge claims promptly (10 working days), failing to investigate reasonably, refusing to pay without a reasonable investigation, compelling litigation by offering substantially less than the eventual recovery, denying without a basis in the policy, etc.
*   **Use:** Cite WAC 284-30-330 violations in (a) complaints to the Office of the Insurance Commissioner, (b) as evidentiary support for an IFCA claim (RCW 48.30.015), and (c) as one of the two predicate-violation tracks IFCA itself recognizes (the other being unreasonable denial of coverage).
*   **Caveat:** WAC 284-30-330 violations alone do **not** create a CPA cause of action against the insurer (the Supreme Court in *Perez-Crisantos v. State Farm*, 187 Wn.2d 669 (2017), narrowed IFCA's regulatory-violation track to unreasonable-denial cases — see next section). They remain useful as OIC complaint material and as bad-faith evidence.

## Insurance Fair Conduct Act (IFCA)

*   **Statute:** **RCW 48.30.015** — Insurance Fair Conduct Act (2007)
*   **Sources:** [app.leg.wa.gov/rcw/default.aspx?cite=48.30.015](https://app.leg.wa.gov/rcw/default.aspx?cite=48.30.015); OIC overview at [insurance.wa.gov/laws-rules/insurance-fair-conduct-act-ifca](https://www.insurance.wa.gov/laws-rules/insurance-fair-conduct-act-ifca)
*   **Substance:** Any **first-party claimant** to a policy of insurance who is **unreasonably denied** a claim for coverage or payment of benefits may sue in superior court for:
    *   **Actual damages**, plus
    *   **Costs, including reasonable attorney's fees and litigation costs** (mandatory, not discretionary), plus
    *   **Discretionary treble damages** (up to three times actual damages) for unreasonable denial.
*   **Procedural requirements:**
    *   Send written notice of the basis for the cause of action to the insurer **and** to the Office of the Insurance Commissioner at least **20 days before filing**, by regular, registered, or certified mail.
    *   Payment by the insurer within the 20-day window can moot the claim.
*   **Coverage:** All first-party insurance policies, including health insurance. Third-party claims (suing someone else's insurer) are not covered.
*   **Scope narrowing (Perez-Crisantos, 2017):** The Washington Supreme Court held that IFCA creates a private cause of action **only for unreasonable denial of a claim for coverage or payment of benefits** — not for free-standing violations of the WAC 284-30 regulations. Cite IFCA when the insurer denied the claim or refused to pay; cite WAC 284-30-330 violations as supporting evidence of unreasonableness, not as the cause of action itself.
*   **ERISA preemption:** **IFCA is preempted as applied to self-funded ERISA employer plans.** For ERISA self-funded plans, the remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) attorney's fees — no state treble damages. IFCA is in play for fully-insured plans, individual/marketplace plans, public-employee plans (PEBB/SEBB), and Medicaid managed care.

## Common-law bad faith

*   **Leading case:** **Coventry Associates v. American States Insurance Co.**, 136 Wn.2d 269, 961 P.2d 933 (1998)
*   **Sources:** [law.justia.com/cases/washington/supreme-court/1998/65850-1-1.html](https://law.justia.com/cases/washington/supreme-court/1998/65850-1-1.html); MRSC mirror at [courts.mrsc.org/supreme/136wn2d/136wn2d0269.htm](http://courts.mrsc.org/supreme/136wn2d/136wn2d0269.htm)
*   **Substance:** Washington recognizes insurance bad faith as a **separate common-law tort** independent of the contract claim. *Coventry* held that an insured may maintain a bad-faith and CPA action against its insurer for a bad-faith **investigation** even where the coverage denial was ultimately correct. The duty of good faith is separate from the duty to indemnify, and a plaintiff's damages are not capped by the contract — general tort damages (including emotional distress and consequential losses) are recoverable.
*   **Standard:** The insurer's conduct must be unreasonable, frivolous, or unfounded — more than mere negligence or honest mistake, but the bar is lower than IFCA's "unreasonable denial of coverage" because *Coventry* extends to bad-faith **handling**, not just bad-faith outcome.
*   **Why it matters:** A patient with an insurer that delays, fails to investigate, requests duplicative documentation, or denies on shifting grounds can plead all of (a) breach of contract, (b) common-law bad faith (*Coventry*), (c) IFCA (RCW 48.30.015) if coverage was unreasonably denied, and (d) CPA (chapter 19.86 RCW) — each with independent damages and the latter two with fee shifting. Few states stack as cleanly.
*   **ERISA:** Common-law bad faith is preempted as applied to self-funded ERISA plans.

## Balance Billing Protection Act

*   **Statute:** **Chapter 48.49 RCW** — Balance Billing Protection Act (BBPA), originally enacted 2019 (HB 1065), effective **January 1, 2020**
*   **Ground-ambulance expansion:** **SSB 5986 (2024)**, codified at RCW 48.49.200 through 48.49.215, effective for health plans issued or renewed on or after **January 1, 2025**
*   **Implementing regulations:** Chapter **284-43B WAC**
*   **Sources:** [app.leg.wa.gov/RCW/default.aspx?cite=48.49&full=true](https://app.leg.wa.gov/RCW/default.aspx?cite=48.49&full=true); OIC consumer page at [insurance.wa.gov/insurance-resources/health-insurance/how-health-insurance-works/what-consumers-need-know-about-surprise-or-balance-billing](https://www.insurance.wa.gov/insurance-resources/health-insurance/how-health-insurance-works/what-consumers-need-know-about-surprise-or-balance-billing); SSB 5986 rulemaking at [insurance.wa.gov/laws-rules/legislation-and-rulemaking/rulemaking/implementation-ssb-5986-and-updates-balance-billing-protection-act-bbpa-r-2024-01](https://www.insurance.wa.gov/laws-rules/legislation-and-rulemaking/rulemaking/implementation-ssb-5986-and-updates-balance-billing-protection-act-bbpa-r-2024-01)

### What it prohibits

*   Balance billing for **emergency services** from a nonparticipating provider or facility (RCW 48.49.020(1)).
*   Balance billing for **nonemergency services** rendered by a nonparticipating provider at a **participating facility** — ancillary services (anesthesia, radiology, pathology, lab, hospitalist, etc.) (RCW 48.49.020(2)).
*   Balance billing for **air ambulance** services (RCW 48.49.020(3)).
*   Balance billing for **behavioral health emergency services** (RCW 48.49.020(4)).
*   Balance billing for **ground ambulance** by a nonparticipating ground ambulance services organization (RCW 48.49.200), for plans issued or renewed on or after Jan 1, 2025.
*   Patient cost-sharing is capped at the in-network amount and counts toward the in-network deductible and out-of-pocket maximum.

### Where Washington goes beyond the federal No Surprises Act

*   **Covers ground ambulance.** The federal NSA explicitly excludes ground ambulance. Washington's payment-rate floor for ground ambulance is the **lesser of (i) the billed charge or (ii) 325% of the current Medicare rate** for the same service in the same geographic area (or, if available, a local-government-set rate filed with the OIC). Operative until December 31, 2027.
*   **Behavioral-health emergencies** are expressly covered (broader than NSA).
*   **Participating self-funded ERISA plans:** Washington's BBPA allows self-funded plans to **voluntarily elect** into the state framework (RCW 48.49.020(5)); the OIC publishes a list. When a self-funded plan has opted in, the state protections apply on top of the federal NSA.
*   Overpayments must be refunded within 30 business days with 12% annual interest on any delayed refund.

### Caveats

*   ERISA self-funded employer plans that have **not** opted in are covered only by the federal NSA — still no ground ambulance protection.
*   Workers' compensation, Medicare, and Medicaid have their own frameworks.
*   Patient must receive both state-law and federal NSA disclosures from providers; protections layer rather than displace.

## Medical-debt credit reporting ban

*   **Statutes:** **RCW 70.41.400(3)** (hospitals, physician groups, professional partners) and **RCW 70.54.475** (any person, provider, facility, or licensed collection agency), 2025
*   **Sources:** [app.leg.wa.gov/rcw/default.aspx?cite=70.41.400](https://app.leg.wa.gov/rcw/default.aspx?cite=70.41.400); [app.leg.wa.gov/rcw/default.aspx?cite=70.54.475](https://app.leg.wa.gov/rcw/default.aspx?cite=70.54.475); SB 5480 (2025) enacted at [washingtonstatestandard.com/2025/04/22/wa-bill-to-keep-medical-debt-off-credit-reports-signed-into-law](https://washingtonstatestandard.com/2025/04/22/wa-bill-to-keep-medical-debt-off-credit-reports-signed-into-law/)
*   **Substance:** Hospitals, physician groups, professional partners, health care providers, health care facilities, and licensed collection agencies **may not furnish information relating to a medical debt to a consumer credit reporting agency**. **A medical debt is void and unenforceable** if the prohibition is violated. The legislature has declared each violation an unfair or deceptive act under chapter 19.86 RCW, importing the CPA's treble damages and attorney's fees.
*   **Sale or assignment restriction:** RCW 70.54.470 (2019) prohibits any provider or facility from selling or assigning medical debt to a collection agency until **at least 120 days** after the initial billing statement was sent.
*   **Federal preemption posture:** The CFPB issued an October 2025 interpretive rule taking the position that the federal FCRA preempts state laws restricting medical-debt credit reporting. The Washington statute may be challenged on that ground; the state law remains in force unless and until a court holds otherwise. Until then, **a Washington patient whose hospital, provider, or collector furnishes medical debt to a CRA can plead the debt void plus CPA treble damages**.

## Regulatory agencies

### Office of the Insurance Commissioner (OIC)

*   **Online complaint:** [insurance.wa.gov/complaints-appeals-fraud/complaints/file-complaint-or-check-your-complaint-status](https://www.insurance.wa.gov/complaints-appeals-fraud/complaints/file-complaint-or-check-your-complaint-status)
*   **Phone:** Consumer Hotline **1-800-562-6900** (toll-free, 8:30 a.m.-4:30 p.m. PT, Mon-Fri); main office **(360) 725-7080**
*   **Mail:**

    > Washington State Office of the Insurance Commissioner Consumer Protection Division P.O. Box 40255 Olympia, WA 98504-0255

*   **Authority:** all insurance companies licensed in Washington, including fully-insured health insurers, HMOs, PPOs, Medicare supplement, and self-funded plans that opted into the BBPA. Administers the Balance Billing Protection Act, IFCA, and WAC 284-30 unfair-claims rules. **No authority over self-funded ERISA plans** that did not opt in (route to DOL EBSA at 1-866-444-3272) and does not regulate hospitals or debt collectors directly (route to AG and DOL).

### Washington Attorney General — Consumer Protection Division

*   **Online complaint:** [atg.wa.gov/file-complaint](https://www.atg.wa.gov/file-complaint)
*   **Phone:** in-state toll-free **1-800-551-4636**; main **(206) 464-6684** (10 a.m.-3 p.m. PT, Mon-Fri)
*   **Authority:** enforces the **Consumer Protection Act (chapter 19.86 RCW)**, the Collection Agency Act (chapter 19.16 RCW), the medical-debt credit-reporting ban (RCW 70.54.475), and the medical-debt sale restriction (RCW 70.54.470). Reach over providers, hospitals, third-party debt collectors, **and original creditors**. The AG also brings injunctive cases — the April 2026 settlement that erased $1.5M of medical debt against a Washington collection agency was an AG enforcement action under chapter 19.86 RCW. CC the AG on any 30-day warning letter where the dispute involves a Washington hospital, in-house billing department, or collection agency.

## Small claims court — District Court Small Claims Department

*   **Court name:** **Small Claims Department of District Court** (one per county)
*   **Jurisdictional limit:** **$10,000** for natural persons; **$5,000** for corporations, LLCs, and other entities — codified at **RCW 12.40.010**
*   **Sources:** [app.leg.wa.gov/rcw/default.aspx?cite=12.40&full=true](https://app.leg.wa.gov/rcw/default.aspx?cite=12.40&full=true); AGO guide at [atg.wa.gov/small-claims-court-0](https://www.atg.wa.gov/small-claims-court-0)
*   **Filing fees:** **$35 to $50** depending on county. Most populous counties (King, Pierce, Snohomish, Thurston, Clark) charge $50. Service costs are extra.
*   **Attorney rules:** **Attorneys are prohibited** from appearing in the Small Claims Department under **RCW 12.40.080** without the judicial officer's consent. This is one of the strongest pro se forums in the country — no lawyer on either side by default. A patient may consult an attorney before the hearing but cannot bring one to the hearing unless the judge specifically permits it. The narrow exception covers transfers from the regular district court docket where counsel was already of record.
*   **Corporate appearance:** corporations and LLCs may appear through an officer, employee, or other authorized representative (not a lawyer) under RCW 12.40.080.
*   **Jury trial:** not available in the Small Claims Department. A losing party may appeal de novo to superior court, where regular rules and attorneys apply (RCW 12.40.120).

## Statute of limitations

*   **Written contracts:** **6 years from breach** — **RCW 4.16.040(1)** (action upon a contract in writing, or liability express or implied arising out of a written agreement)
*   **Oral contracts / open accounts / account stated:** **3 years from breach** — **RCW 4.16.080(3)** (action upon a contract or liability, express or implied, not in writing)
*   **CPA actions:** **4 years from accrual** — RCW 19.86.120
*   **Sources:** [app.leg.wa.gov/RCW/default.aspx?cite=4.16.040](https://app.leg.wa.gov/RCW/default.aspx?cite=4.16.040); [app.leg.wa.gov/rcw/default.aspx?cite=4.16&full=true](https://app.leg.wa.gov/rcw/default.aspx?cite=4.16&full=true)

Most hospital admissions involve a signed financial-responsibility form — a written contract, so 6 years applies. Implied-in-fact billing arrangements without a signed agreement are governed by the 3-year unwritten-contract bar. The clock runs from breach (typically the day payment was due and not made).

Partial payment or written acknowledgment of a debt can restart the clock in Washington (the doctrine of revival applies, though the rule is narrower than in some states — generally requires a signed written acknowledgment or an unequivocal new promise). **Do not make a partial payment on a time-barred debt without legal advice.**

## Ground-ambulance balance billing

**Covered by Washington state law as of January 1, 2025**, via SSB 5986 (2024), codified at RCW 48.49.200 et seq. and chapter 284-43B WAC. See "Balance Billing Protection Act" above.

For health plans issued, delivered, or renewed in Washington on or after January 1, 2025, an enrollee receiving covered ground ambulance services from a nonparticipating organization may be billed **no more than the in-network cost-share**. The carrier pays the ground ambulance organization the lesser of the billed charge or **325% of the current published Medicare rate** for the same service in the same geographic area (or a local-government-set rate filed with the OIC where available). This is one of the most patient-favorable rate floors in the country and closes the single biggest balance-billing gap left by the federal No Surprises Act.

ERISA-preempted for self-funded employer plans that have not opted in; excludes workers' comp, Medicare, Medicaid. Plans renewed before Jan 1, 2025 are not retroactively covered.

## Credit reporting and medical debt

Washington has, as of 2025, the broadest medical-debt credit-reporting ban in the country (see "Medical-debt credit reporting ban" above):

*   **RCW 70.41.400(3)** — hospitals, physician groups, professional partners may not furnish to CRAs; debt is void if violated.
*   **RCW 70.54.475** (2025) — extends the ban to any person, provider, facility, or licensed collection agency; debt is void if violated; CPA per-se violation.
*   **RCW 70.54.470** (2019) — no sale or assignment of medical debt to a collection agency until 120 days after first bill.

Patients also retain:

*   Federal FCRA dispute rights (15 U.S.C. §§ 1681i, 1681s-2).
*   The 2022-2023 voluntary changes by Equifax/Experian/TransUnion (paid medical debt removed; debt under $500 not reported; 1-year delay before reporting).

**Federal preemption posture:** the CFPB's October 2025 interpretive rule asserts FCRA preemption of state medical-debt CRA bans. The Washington bans remain in force pending litigation; Jon's general rule when drafting WA letters is to plead the state statute as the primary lever and the CPA treble-damages remedy as the consequence, with the federal FCRA cited in the alternative.

## Hospital lien statute

*   **Citations:** **Chapter 60.44 RCW** — lien of doctors, nurses, hospitals, ambulance services (RCW 60.44.010 through 60.44.060)
*   **Sources:** [app.leg.wa.gov/rcw/default.aspx?cite=60.44&full=true](https://app.leg.wa.gov/rcw/default.aspx?cite=60.44&full=true); industry overview at [adlergiersch.com/provider-blog/should-health-care-providers-make-medical-liens-part-of-their-billing-practices](https://www.adlergiersch.com/provider-blog/should-health-care-providers-make-medical-liens-part-of-their-billing-practices/)
*   **Substance:** Operators of an ambulance service or hospital, and licensed nurses, practitioners, physicians, and surgeons rendering service for a person who suffered a **traumatic injury**, have a lien on the injured person's **claim, right of action, and/or money against a tort-feasor or the tort-feasor's insurer** — for the reasonable value of service, plus costs and reasonable attorney's fees. **Not a lien on the patient's home, wages, or bank accounts.**
*   **Perfection requirements (RCW 60.44.020):**
    *   Provider must either enforce the lien on its own behalf, or designate a licensed collection agency to do so.
    *   Provider must disclose use of liens as part of its billing and collection practices.
    *   File a notice of claim with the county auditor within **20 days** after the date of injury or receipt of care (the strictest deadline of any state hospital-lien statute).
*   **2015 amendments (HB 1503):** tightened the disclosure and collection-agency-designation requirements. Failure to comply with the disclosure or filing rules **invalidates the lien**.
*   **Settlement effect:** no settlement between the patient and tort-feasor (or the insurer) discharges the lien unless the settlement provides for payment, or a written release is filed in court or delivered. Within **30 days** after payment or settlement, the lien claimant must execute and deliver a release; unjustified delay triggers court-ordered costs, fees, and damages.

## Hospital charity care — most generous in the United States

*   **Statute:** **RCW 70.170.060** — charity-care duties, last expanded by HB 1616 (2022)
*   **Sources:** [app.leg.wa.gov/rcw/default.aspx?cite=70.170.060](https://app.leg.wa.gov/rcw/default.aspx?cite=70.170.060); WA DOH overview at [doh.wa.gov/data-statistical-reports/healthcare-washington/hospital-and-patient-data/hospital-patient-information-and-charity-care](https://doh.wa.gov/data-statistical-reports/healthcare-washington/hospital-and-patient-data/hospital-patient-information-and-charity-care)

### Tier 1 (large hospitals and health systems — most patients)

*   **100% free care** for patients and guarantors with household income up to **300% of the federal poverty level**.
*   **75% discount** for income from **301-350% FPL**.
*   **50% discount** for income from **351-400% FPL**.

### Tier 2 (smaller hospitals, critical-access, and some specialty hospitals)

*   **100% free care** for income up to **200% FPL**.
*   **75% discount** for income from **201-250% FPL**.
*   **50% discount** for income from **251-300% FPL**.

### Reference values

For a family of four in 2025: 300% FPL ≈ **$96,450**, 400% FPL ≈ **$128,600**. For a single person in 2025: 300% FPL ≈ **$46,950**, 400% FPL ≈ **$62,600**. These thresholds make Washington's charity-care floor by far the most generous in the country (compare California at 400% federal poverty for free care only at qualifying facilities; most states have no analog at all).

### Enforcement

*   Hospitals must screen every patient for charity-care eligibility before any collection activity, and must **post and prominently display notice of charity-care availability** in admissions areas, the emergency department, and the billing office, in multiple languages.
*   Written billing statements must include information about potential eligibility.
*   A violation is enforceable by the Washington DOH and through the CPA (RCW 19.86) via the AG and private suits.
*   Screening tool: **Dollar For** at [dollarfor.org/state_sheet/washington](https://dollarfor.org/state_sheet/washington/) — Dollar For is itself headquartered in Vancouver, WA and has the deepest charity-care expertise of any non-profit in this space.

## Wage garnishment — medical debt has a special exemption

*   **Statute:** **RCW 6.27.150** — exemption of earnings from garnishment, with **medical-debt-specific bracket**
*   **Source:** [app.leg.wa.gov/rcw/default.aspx?cite=6.27.150](https://app.leg.wa.gov/rcw/default.aspx?cite=6.27.150)
*   **Substance:** For **medical debt**, the exempt portion of weekly disposable earnings is the **greater of (i) 60 times the state minimum hourly wage, or (ii) 80% of disposable earnings** — substantially more protective than the standard consumer-debt exemption (greater of 35× minimum wage or 80%) and more protective than the federal CCPA floor (25%). Medical-debt creditors cannot garnish wages without first obtaining a court judgment.
*   **Use:** In response letters to medical-debt collectors threatening garnishment without a judgment, and in pleadings post-judgment to claim the medical-debt exemption explicitly.

## Quick reference for letter rendering

When the LLM renders a Washington-bound letter, substitute these defaults:

*   **State statute (itemization right):** Washington has no automatic 6-day inpatient itemization rule. The lever is **RCW 70.41.400** (written billing statement, billing-inquiry phone numbers, charity-care notice, medical-debt credit-reporting ban) **plus the Collection Agency Act disclosure** (chapter 19.16 RCW) requiring debt collectors to disclose the consumer's right to request an itemized statement, with collection paused on receipt of the request.
*   **State insurance department (CC line):** Office of the Insurance Commissioner, Consumer Protection Division, P.O. Box 40255, Olympia, WA 98504-0255 ([insurance.wa.gov](https://www.insurance.wa.gov))
*   **State AG consumer protection (CC line):** Washington Attorney General, Consumer Protection Division, 1125 Washington Street SE, P.O. Box 40100, Olympia, WA 98504-0100 ([atg.wa.gov/file-complaint](https://www.atg.wa.gov/file-complaint))
*   **Small-claims court name:** **Small Claims Department, District Court of \[county\]**
*   **Filing fee (in 30-day warning):** "$35 to $50 depending on county"
*   **Statute of limitations (in 30-day warning):** "RCW 4.16.040 (six years for breach of written contract)" — or "RCW 4.16.080(3) (three years for unwritten contract)" if no signed financial-responsibility form
*   **For insurer-side disputes (denial / unreasonable handling):** Cite **RCW 48.30.015 (IFCA)** — actual damages, mandatory attorney's fees, discretionary treble damages — and the 20-day pre-suit notice requirement. Cite **WAC 284-30-330** for each specific unfair practice, and *Coventry Associates v. American States Ins. Co.*, 136 Wn.2d 269 (1998), for common-law bad-faith handling.
*   **For provider-side disputes (vs. hospital or in-house billing):** Cite **RCW 19.86.090 (CPA)** with treble damages (capped at $25,000) and mandatory attorney's fees. If the dispute involves credit reporting, cite **RCW 70.54.475** (debt void if reported). If the dispute involves a sale to a collection agency within 120 days of first bill, cite **RCW 70.54.470**.
*   **For ground ambulance balance bills (post-Jan 1, 2025 plans):** Cite **RCW 48.49.200** — patient liable only for in-network cost-share, carrier pays the lesser of billed charge or 325% Medicare rate. This is the single highest-leverage Washington-specific cite when applicable.
*   **For charity care:** Cite **RCW 70.170.060** with the patient's tier (1 or 2) and FPL band. For a four-person household earning under $96,450 (2025), Tier 1 hospitals owe 100% free care, period.

## Key Washington-specific advantages

Worth keeping in mind when triaging a WA patient's bills:

1.  **Charity Care Act is the most generous in the country.** Tier 1 hospitals must zero a bill outright for any household at or under 300% FPL. Always screen for charity care before any other lever — it disposes of most disputes without litigation.
2.  **IFCA + CPA + common-law bad faith stack.** A single unreasonable denial of a health-insurance claim can support all three causes of action with independent damages and (for IFCA and CPA) **mandatory attorney's fees** on a plaintiff's win. Few states have all three layers.
3.  **Medical debt is unenforceable if credit-reported.** Hospitals, providers, facilities, and licensed collection agencies that furnish medical-debt information to a CRA void the debt and trigger a CPA treble-damages claim. This is unique in scope and remedy.
4.  **Ground ambulance protected from Jan 1, 2025.** Washington's payment-rate floor (lesser of billed charge or 325% Medicare) is one of the most patient-favorable rate-shifts in the country and closes the federal NSA's biggest gap.
5.  **Small claims is attorney-free.** RCW 12.40.080 bars lawyers from appearing without judicial consent, on either side. The economic and psychological leverage of suing a hospital's billing department in a forum the hospital cannot bring counsel into is enormous.
6.  **Wage-garnishment exemption is medical-debt-specific.** RCW 6.27.150 gives medical-debt judgments their own (more protective) exemption bracket — greater of 60× minimum wage or 80% of disposable earnings, vs. 35×/80% for ordinary consumer debt.
7.  **120-day no-sale rule.** RCW 70.54.470 means any debt sold to a collection agency within 120 days of the first bill is unlawful at the point of sale; the patient can plead that violation as a CPA per-se claim against both the original creditor and the buyer.
