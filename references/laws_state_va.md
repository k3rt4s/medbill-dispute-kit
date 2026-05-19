# Virginia state pack

The fully-worked state-law layer for Virginia patients. The LLM uses this when the patient's state is Virginia. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md), Tennessee at [`laws_state_tn.md`](laws_state_tn.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Three things make Virginia's patient-side leverage unusually strong:

1. The **Virginia Consumer Protection Act** carries **treble damages for willful violations plus attorney's fees** (Va. Code § 59.1-204), and it reaches the hospital as an original creditor — not just third-party collectors. This is the single highest-leverage cite in any VA medical-billing letter.
2. **Attorneys are statutorily barred from representing parties in Virginia small claims court** (Va. Code § 16.1-122.4). Corporate defendants must send a non-lawyer officer or employee, which heavily favors a prepared pro se patient.
3. The **Medical Debt Protection Act** (Va. Code § 59.1-611 et seq., effective July 1, 2026) caps interest at 3% per annum, blocks home foreclosure and personal-property liens for medical debt, and prohibits wage garnishment for patients eligible for financial assistance. Va. Code § 59.1-444.4 (effective July 1, 2025) already bars medical-care facilities, licensed health professionals, EMS agencies, and collectors from reporting medical debt to credit bureaus at all.

## Hospital itemization right

- **Statute:** **Va. Code § 54.1-2404** — itemized statements required upon request
- **Source:** [law.lis.virginia.gov/vacode/title54.1/chapter24/section54.1-2404](https://law.lis.virginia.gov/vacode/title54.1/chapter24/section54.1-2404/)
- **What it requires:** Any health care provider licensed or certified by a board within the Department of Health Professions must furnish an itemized statement of charges upon patient request, **regardless of whether a bill has been or will be submitted to any third-party payor** (including Medicaid or state/local hospitalization programs).
- **Scope:** Reaches the individually-licensed provider (physician, nurse, dentist, chiropractor, physical therapist, pharmacist, etc.). Hospitals as institutions are reached indirectly through the licensed providers practicing within them; in practice every Virginia hospital honors itemization requests.
- **Timeframe:** Statute does not specify a deadline. Industry norm in Virginia is **30 days from request**, consistent with the practical guidance published by Virginia consumer-services offices ([fairfaxcounty.gov/cableconsumer/csd/medical-billing](https://www.fairfaxcounty.gov/cableconsumer/csd/medical-billing)). Always send the request in writing by certified mail to crystallize the timeline.
- **Written request:** Not required by the statute (it says "upon the request"), but a written certified-mail request is strongly recommended for the paper trail.
- **Related statute — price transparency (different right):** Va. Code § 32.1-137.05 requires hospitals to (a) post a machine-readable file of standard charges and (b) furnish an advance estimate of patient responsibility for elective procedures, on at least three days' notice. This is a pre-service estimate right, not a post-service itemization right. Source: [law.lis.virginia.gov/vacode/title32.1/chapter5/section32.1-137.05](https://law.lis.virginia.gov/vacode/title32.1/chapter5/section32.1-137.05/).
- **Private right of action:** Not directly under § 54.1-2404, but a refusal can be pleaded as a deceptive practice under the Virginia Consumer Protection Act (see below).

## Virginia Consumer Protection Act

- **Statute:** **Va. Code § 59.1-196 et seq.** — Virginia Consumer Protection Act of 1977 (VCPA); private remedies at **§ 59.1-204**
- **Source:** [law.lis.virginia.gov/vacode/title59.1/chapter17](https://law.lis.virginia.gov/vacode/title59.1/chapter17/); [law.lis.virginia.gov/vacode/title59.1/chapter17/section59.1-204](https://law.lis.virginia.gov/vacode/title59.1/chapter17/section59.1-204/)
- **Substance:** Prohibits a long list of "prohibited practices" in consumer transactions, including misrepresentations about the source, characteristics, or amount of a charge, billing for services not rendered, upcoding, and false statements about the patient's payment obligations.
- **Private right of action:** **Yes — and this is the heart of Virginia's patient leverage.**
  - **Actual damages or $500**, whichever is greater
  - **Treble damages up to three times actual damages, or $1,000, whichever is greater, for willful violations**
  - **Reasonable attorney's fees and court costs**
- **"Cure offer" caveat:** § 59.1-204.1 lets a supplier deliver a "cure offer" before filing its initial response. If the patient rejects a valid cure offer and the eventual damages don't exceed it, the patient can lose attorney's-fees recovery for everything after the cure offer. Plan the demand letter and the litigation accordingly.
- **Reach:** Covers the hospital itself as an original creditor, the physician practice, the third-party collector, and the debt buyer. Broader than the federal FDCPA, which only reaches third-party collectors.
- **ERISA:** Not preempted — regulates the provider's billing conduct, not the plan.

## Unfair Insurance Practices Act

- **Statute:** **Va. Code § 38.2-510** — unfair claims settlement practices
- **Source:** [law.lis.virginia.gov/vacode/title38.2/chapter5/section38.2-510](https://law.lis.virginia.gov/vacode/title38.2/chapter5/section38.2-510/)
- **Substance:** Lists 17 unfair claims-settlement practices when committed with sufficient frequency to indicate a general business practice — misrepresenting policy provisions, failing to acknowledge claims promptly, refusing claims without reasonable investigation, compelling litigation by lowballing, failing to explain denials, etc.
- **Critical caveat — no private right of action:** Subsection (B) expressly states: "No violation of this section shall of itself be deemed to create any cause of action in favor of any person other than the Commission." Enforcement is by the SCC Bureau of Insurance only. Virginia federal and state courts have repeatedly dismissed § 38.2-510 claims brought by insureds.
- **Preservation clause:** The same subsection adds, "nothing in this subsection shall impair the right of any person to seek redress at law or equity for any conduct for which action may be brought." So while § 38.2-510 itself doesn't support a private suit, the underlying conduct may still ground a breach-of-contract or common-law bad-faith claim.
- **Use:** Cite § 38.2-510 violations in a complaint to the Bureau of Insurance (see below) and as evidentiary support for breach-of-contract or common-law bad faith. Do not plead § 38.2-510 as a standalone count in litigation.

## Bad-faith failure to pay

Virginia bad-faith law is **fragmented by line of insurance**, which is unusual.

### Motor-vehicle insurance — statutory

- **Statute:** **Va. Code § 8.01-66.1** — improper denial of motor vehicle insurance claims
- **Source:** [law.lis.virginia.gov/vacode/title8.01/chapter3/section8.01-66.1](https://law.lis.virginia.gov/vacode/title8.01/chapter3/section8.01-66.1/)
- **Substance:** When a court finds an auto insurer denied a property-damage, medical-expense, third-party liability (capped at $3,500), or UM/UIM claim not in good faith, the patient/insured recovers **double the amount of the judgment**, **interest from 30 days after written claim**, plus **attorney's fees and costs**. UIM cap on the doubled portion is $500,000.
- **Scope:** Motor-vehicle insurance only. Not available for general health insurance.

### Health insurance and other lines — common law

- For non-motor-vehicle insurance (including health policies), Virginia recognizes a **common-law breach of the implied covenant of good faith and fair dealing**, but recovery for ordinary bad faith is limited to contract damages — the unpaid benefits, plus interest and possibly attorney's fees. Punitive damages require an independent tort (e.g., fraud).
- **Procedural:** Send a written demand by certified mail identifying the policy, the loss, and the relief sought. Wait a reasonable period (30-60 days is conventional) before suing.
- **ERISA preemption:** State-law bad-faith claims are preempted as applied to self-funded ERISA employer plans. The federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) attorney's fees. State-law claims remain available for fully-insured plans, Medicaid managed care, individual/marketplace plans, and motor-vehicle med-pay.

## Balance Billing Protection Act

- **Statute:** **Va. Code § 38.2-3445** (emergency-services coverage requirement) and **§ 38.2-3445.01** (balance-billing prohibition) — together with the surrounding § 38.2-3445.02 through § 38.2-3445.07 — comprise Virginia's Balance Billing Protection Act
- **Effective:** **January 1, 2021** (HB 1251/SB 172, 2020 session)
- **Implementing regulations:** 14 VAC 5-405-10 et seq.
- **Sources:** [law.lis.virginia.gov/vacode/title38.2/chapter34/section38.2-3445.01](https://law.lis.virginia.gov/vacode/title38.2/chapter34/section38.2-3445.01/); [scc.virginia.gov/consumers/insurance/health-insurance-consumer/balance-billing-protection](https://www.scc.virginia.gov/consumers/insurance/health-insurance-consumer/balance-billing-protection/)

### What it prohibits

- Balance billing for **emergency services** from an out-of-network (OON) provider or facility.
- Balance billing for **non-emergency services** rendered by an OON provider at an **in-network** facility (surgical or ancillary services — anesthesia, radiology, pathology, lab, hospitalist).
- Patient cost-sharing capped at the in-network amount and counted toward the in-network deductible and out-of-pocket maximum.
- Carrier pays the OON provider the "commercially reasonable" rate based on a Virginia All-Payer Claims Database benchmark; provider/carrier disputes go to baseball-style arbitration with the patient held harmless.

### Caveats

- **Ground ambulance is NOT covered.** Virginia has not extended the Balance Billing Protection Act to ground ambulance services as of this writing. The federal No Surprises Act also excludes ground ambulance, leaving Virginia patients exposed.
- **Air ambulance:** covered by the federal NSA, not by Virginia state law.
- **ERISA preemption:** the Act does not reach self-funded ERISA employer plans; those are covered (if at all) only by the federal NSA. Self-funded plans may **opt in** to Virginia's framework — about a quarter of Virginia self-funded plans have done so.
- Excludes workers' compensation, Medicare, and Medicaid.

## Regulatory agencies

### Virginia Bureau of Insurance (within the State Corporation Commission)

- **Online complaint:** [scc.virginia.gov/consumers/insurance/file-an-insurance-complaint](https://www.scc.virginia.gov/consumers/insurance/file-an-insurance-complaint/); balance-billing-specific form on the BBPA page
- **Phone:** toll-free **1-877-310-6560**; Richmond direct **(804) 371-9185**
- **Balance-billing email:** BBVA@scc.virginia.gov; general BOI: bureauofinsurance@scc.virginia.gov
- **Mail:**
  > State Corporation Commission
  > Bureau of Insurance, Consumer Services Section
  > P.O. Box 1157
  > Richmond, VA 23218
- **Authority:** all insurance companies licensed in Virginia, including fully-insured health insurers, HMOs, Medicare supplement. Administers the Balance Billing Protection Act and § 38.2-510 (unfair claims settlement). **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and does not regulate providers, hospitals, or debt collectors (route to AG).
- **Important:** Bureau of Insurance does **not** accept complaints by phone or email. File via the online portal, mail, or fax (804-371-9944 for life/health).

### Virginia Attorney General — Consumer Protection Section

- **Online complaint:** [oag.state.va.us/consumercomplaintform](https://www.oag.state.va.us/consumercomplaintform); topic selector at [oag.state.va.us/ComplaintTopicSelector](https://www.oag.state.va.us/ComplaintTopicSelector/Category/Directory)
- **Phone:** Virginia toll-free **(800) 552-9963**; Richmond/outside-Virginia **(804) 786-2042**; hours 8:30 a.m.–5:00 p.m. Mon–Fri
- **Mail:**
  > Office of the Attorney General
  > Consumer Protection Section
  > 900 East Main Street
  > Richmond, VA 23219
- **Authority:** enforces the Virginia Consumer Protection Act (§ 59.1-196 et seq.), including against hospitals and physician practices as original creditors. This is the right venue for billing-fraud, upcoding, and deceptive-collection complaints — the gap not covered by the Bureau of Insurance.

## Small claims court — General District Court, Small Claims Division

- **Court name:** **Small Claims Division of the General District Court** of the relevant city or county
- **Jurisdictional limit:** **$5,000, exclusive of interest** — Va. Code **§ 16.1-122.2**
- **Source:** [law.lis.virginia.gov/vacode/title16.1/chapter6/section16.1-122.2](https://law.lis.virginia.gov/vacode/title16.1/chapter6/section16.1-122.2/); chapter at [law.lis.virginia.gov/vacodefull/title16.1/chapter6/article5](https://law.lis.virginia.gov/vacodefull/title16.1/chapter6/article5/)
- **Filing fees:** **typically $30–$75** depending on the locality and service method. The Virginia Courts office has a fee calculator at [vacourts.gov/gdfees_calc_app](https://www.vacourts.gov/gdfees_calc_app).
- **Attorney rule — Va. Code § 16.1-122.4:** **Attorneys are statutorily barred from representing parties in small claims court.** "All parties shall be represented by themselves" with narrow exceptions:
  - **Business entities** (corporations, partnerships, LLCs) appear through an owner, officer, member, or employee — **but explicitly not through an attorney in a representative capacity**. An attorney may appear pro se on his own claim only.
  - A party who cannot understand or participate may be represented by a non-attorney friend or relative familiar with the facts.
  - A defendant may retain counsel specifically to **remove** the case to the General District Court regular docket before decision.
- **Jury trial:** not available in small claims. A defendant who wants a jury must remove to General District Court (no jury there either — jury demand requires further appeal de novo to Circuit Court within 10 days of judgment).

## Statute of limitations

- **Written, signed contracts:** **5 years from breach** — Va. Code § 8.01-246(2)
- **Unwritten contracts (or written but unsigned):** **3 years from breach** — Va. Code § 8.01-246(4)
- **Source:** [law.lis.virginia.gov/vacode/title8.01/chapter4/section8.01-246](https://law.lis.virginia.gov/vacode/title8.01/chapter4/section8.01-246/)

Most Virginia hospital admissions involve a signed financial-responsibility form — a written, signed contract, so **5 years** applies. ER or implied-in-fact arrangements without a signed agreement default to 3 years. The clock runs from breach (typically the day payment was due and not made), not from when damages are discovered.

**Pending change:** The 2024-2025 legislative session passed legislation that would shorten the medical-debt statute of limitations to **3 years** as part of the Medical Debt Protection Act package. Confirm enactment status and effective date before relying on the 5-year period for medical-debt-specific contracts.

Partial payment or written acknowledgment of the debt can restart or extend the clock under Va. Code § 8.01-229. **Do not make a partial payment on a time-barred debt without legal advice.**

## Ground ambulance balance-billing

**Not covered by Virginia state law.** Virginia is **not** on the list of states (Colorado, Delaware, Florida, Illinois, Maine, Maryland, New York, Ohio, Vermont, West Virginia) that have closed the federal No Surprises Act ground-ambulance gap.

For a Virginia patient receiving a balance bill from an out-of-network ground ambulance provider:

- **Federal NSA does not protect them.**
- **Virginia § 38.2-3445.01 does not reach ground ambulance.**
- Remaining levers: (a) the Virginia Consumer Protection Act if the bill is misrepresented or upcoded; (b) common-law breach of contract if the patient's plan defined the rate; (c) reasonableness-of-charges defense at the General District Court small-claims level (Va. Code § 8.01-413.01 lets the patient challenge the reasonableness of medical bills); (d) the Medical Debt Protection Act's collection-conduct limits (effective July 1, 2026).

HB 730 (2024 session) was a different bill (not ground-ambulance balance billing). Virginia ground-ambulance protection remains a legislative gap as of this writing.

## Credit reporting

- **Statute:** **Va. Code § 59.1-444.4** — Reporting of medical debt prohibited; civil penalty
- **Effective:** **July 1, 2025**
- **Source:** [law.lis.virginia.gov/vacode/title59.1/chapter35.1/section59.1-444.4](https://law.lis.virginia.gov/vacode/title59.1/chapter35.1/section59.1-444.4/)
- **Substance:** Medical care facilities, licensed health professionals, and emergency medical services agencies **cannot report any portion of a medical debt to a consumer reporting agency**. Collection entities are likewise barred from reporting medical-debt collection efforts.
- **Enforcement:** A violation is a "prohibited practice" under the Virginia Consumer Protection Act (Chapter 17 of Title 59.1), which means all VCPA remedies apply — actual damages or $500, **treble damages up to $1,000 or 3× actual for willful violations**, attorney's fees, court costs.
- **Related — bill-reasonableness statute:** Va. Code § 8.01-413.01 lets a patient or defendant challenge the reasonableness of medical bills in any civil action, with the burden on the provider to prove charges are reasonable.
- **Federal preemption posture is in flux.** The CFPB's October 2025 interpretive rule takes the position that the federal FCRA preempts state laws restricting medical-debt credit reporting. If that survives challenge, it may limit § 59.1-444.4. Pleading both the state-law violation and a federal FCRA furnisher claim hedges the patient's position.

## Medical Debt Protection Act (effective July 1, 2026)

- **Statute:** **Va. Code §§ 59.1-611, 59.1-612, 59.1-613**
- **Source:** [law.lis.virginia.gov/vacodefull/title59.1/chapter59](https://law.lis.virginia.gov/vacodefull/title59.1/chapter59/)
- **Substance:**
  - **Interest/late fees:** No interest or late fees for the first **90 days** after the due date. Thereafter capped at **3% per annum** of the medical debt.
  - **Extraordinary collection actions** — five forbidden methods: causing arrest, body attachment writs, foreclosing on real property, placing liens on personal property, and wage garnishment of patients eligible for financial assistance.
  - **120-day cooling-off period:** Creditors cannot pursue any extraordinary collection action until 120 days after the final-invoice due date.
  - **30-day pre-collection notice required** with information about financial assistance.
  - **Refund duty:** Patients must be refunded within 60 days if they've overpaid after financial assistance is applied.
  - **Debt-sale restrictions:** When debt is sold, the seller must contractually bind the buyer to the same rate cap and prohibition on extraordinary collection.
- **Enforcement:** Va. Code § 59.1-613; ties into VCPA remedies.
- **Use:** Once effective, this is among the strongest medical-debt patient-protection regimes in the country. For collection conduct after July 1, 2026, cite the Act alongside the VCPA in any 30-day warning letter.

## Hospital charity care

- **Statute:** **Va. Code § 32.1-137.01** — Posting of charity care policies
- **Source:** [law.lis.virginia.gov/vacode/title32.1/chapter5/section32.1-137.01](https://law.lis.virginia.gov/vacode/title32.1/chapter5/section32.1-137.01/)
- **What it requires:** Every Virginia hospital must (a) post charity-care policy information conspicuously in admissions areas, emergency departments, and waiting rooms; (b) include charity-care information with billing statements sent to uninsured patients; (c) display the policy on the hospital's website; and (d) make the information available in languages other than English for Title VI compliance. Materials must include **specific eligibility criteria and procedures for applying**.
- **Substantive charity-care mandate:** Virginia does not have a general state statute setting minimum charity-care eligibility levels for all hospitals. However, hospitals applying for a Certificate of Public Need must commit to providing free care for patients **up to 200% of the Federal Poverty Level**. Federal IRS § 501(r) governs non-profit hospitals.
- **Annual reporting:** Virginia hospitals report charity care, discounted care, and financial assistance under RGA § 32.1-276.5; see annual reports at [rga.lis.virginia.gov](https://rga.lis.virginia.gov/) (e.g., RD638, RD117, RD118).
- **Use:** Cite § 32.1-137.01 when a hospital has failed to disclose or apply its financial-assistance policy. Pair with the federal § 501(r) violation for non-profit hospitals.
- Use Dollar For at [dollarfor.org/state_sheet/virginia](https://dollarfor.org/state_sheet/virginia/) for screening.

## Hospital lien statute

- **Citations:** **Va. Code §§ 8.01-66.2 through 8.01-66.10**
- **Sources:** [law.lis.virginia.gov/vacode/title8.01/chapter3/section8.01-66.2](https://law.lis.virginia.gov/vacode/title8.01/chapter3/section8.01-66.2/); [law.lis.virginia.gov/vacode/title8.01/chapter3/section8.01-66.3](https://law.lis.virginia.gov/vacode/title8.01/chapter3/section8.01-66.3/)
- **Substance:** Hospitals, nursing homes, physicians, nurses, physical therapists, pharmacies, and emergency-medical-services providers may file a lien for services rendered to an injured person, **only against the patient's cause of action against the third-party tortfeasor** who caused the injury. **Not a lien on the patient's home, wages, or bank accounts.**
- **Statutory caps on the lien amount:**
  - Hospitals and nursing homes: up to **$2,500**
  - Physicians, nurses, physical therapists, pharmacies (each): up to **$750**
  - EMS providers/agencies (each): up to **$200**
- **Priority:** Hospital liens are **inferior** to the attorney's lien for representing the injured person (Va. Code § 8.01-66.3). This means the patient's lawyer gets paid first from the settlement, then the hospital from the remainder up to the statutory cap.
- **Once the Medical Debt Protection Act is in effect (July 1, 2026):** the broader prohibition on personal-property liens and home foreclosure for medical debt (Va. Code § 59.1-612) applies to creditors generally, but the third-party tortfeasor-claim lien under § 8.01-66.2 is a distinct mechanism preserved by the act. Confirm the lien is on the tort claim, not on the patient's personal property.

## Wage garnishment

- **Statute:** **Va. Code § 34-29** (state version of the federal Consumer Credit Protection Act limit) — caps garnishment of disposable earnings at the federal 25% / 30× federal minimum wage formula
- **For medical debt specifically:** Once the Medical Debt Protection Act (§ 59.1-612) is in effect July 1, 2026, garnishment of patients eligible for financial assistance is **prohibited entirely** as an "extraordinary collection action." Even before then, garnishment requires a court judgment, so a collector threatening garnishment without an active judgment violates Virginia and federal collection rules.
- **Use:** In response letters to collectors threatening garnishment without a judgment in hand, and to defeat any collection action against a financial-assistance-eligible patient post-July 2026.

## Quick reference for letter rendering

When the LLM renders a Virginia-bound letter, substitute these defaults:

| Field                                                          | Default value                                                                                                                                           |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Itemization statute**                                        | **Va. Code § 54.1-2404** — itemized statement upon request, no specific timeframe (use 30-day demand by certified mail)                                 |
| **State insurance department (CC line)**                       | State Corporation Commission, Bureau of Insurance, Consumer Services Section, P.O. Box 1157, Richmond, VA 23218 (toll-free 1-877-310-6560)              |
| **State AG consumer protection (CC line)**                     | Office of the Attorney General, Consumer Protection Section, 900 East Main Street, Richmond, VA 23219 ([oag.state.va.us](https://www.oag.state.va.us/)) |
| **Small-claims court name**                                    | Small Claims Division of the General District Court of [city or county]                                                                                 |
| **Filing fee (in 30-day warning)**                             | "$30–$75 depending on locality"                                                                                                                         |
| **Statute of limitations (in 30-day warning)**                 | "Va. Code § 8.01-246(2) (five years for breach of written contract); pending 3-year medical-debt-specific limit under the Medical Debt Protection Act"  |
| **Headline cite for hospital/provider disputes**               | **Va. Code § 59.1-204 (Virginia Consumer Protection Act) — treble damages and attorney's fees**                                                         |
| **Headline cite for credit-reporting violations**              | **Va. Code § 59.1-444.4** (effective July 1, 2025) + VCPA remedies                                                                                      |
| **Headline cite for aggressive collection after July 1, 2026** | **Va. Code § 59.1-612** (Medical Debt Protection Act)                                                                                                   |
| **For motor-vehicle med-pay bad-faith**                        | **Va. Code § 8.01-66.1** — double judgment + interest + attorney's fees                                                                                 |
| **For ground ambulance**                                       | No state-law protection; rely on VCPA, bill-reasonableness (§ 8.01-413.01), and contract defenses                                                       |

## Key Virginia-specific advantages

Worth keeping in mind when triaging a VA patient's bills:

1. **Treble damages plus attorney's fees under the Virginia Consumer Protection Act.** Va. Code § 59.1-204 reaches the hospital, the physician practice, the third-party collector, and the debt buyer. Mention this cite in every 30-day warning letter to a Virginia provider — it changes the economics for the billing department immediately.
2. **Small-claims attorney bar.** Va. Code § 16.1-122.4 prevents the corporate defendant from sending a lawyer to small claims court. A prepared pro se patient faces a non-lawyer billing-department employee. This is a structural advantage Virginia shares with only a handful of other states (e.g., California, Michigan), and the $5,000 limit is high enough to cover most disputed bills.
3. **Medical-debt credit-reporting blackout (effective July 1, 2025).** Va. Code § 59.1-444.4 is one of the strongest state-level medical-debt credit-reporting statutes in the country — a flat prohibition, not just a delay or paid-debt-removal rule. Pair with VCPA remedies for treble damages on willful violations.
4. **Medical Debt Protection Act (effective July 1, 2026).** Once live, the 3%-per-annum interest cap, 120-day extraordinary-collection cooling-off period, and personal-property/foreclosure prohibition make Virginia one of the most patient-favorable states in the nation for medical debt. Anticipate citing § 59.1-612 alongside the VCPA on any post-July-2026 letter.
5. **Ground-ambulance gap is a known weakness.** Unlike Georgia, Maryland, and West Virginia, Virginia has not closed the federal NSA's ground-ambulance exclusion. Patients hit with ground-ambulance balance bills should be routed straight to VCPA misrepresentation theories and the reasonableness-of-charges defense (§ 8.01-413.01) rather than expecting state-law balance-billing protection.
