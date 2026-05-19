# Nebraska state pack

The fully-worked state-law layer for Nebraska patients. The LLM uses this when the patient's state is Nebraska. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md); Tennessee at [`laws_state_tn.md`](laws_state_tn.md). All citations verified against public sources as of 2026-05-19. Re-verify annually.

Three things shape Nebraska's patient-side posture:

1. The **hospital itemization duty is request-based, not automatic** — fourteen days from written request, codified at Neb. Rev. Stat. § 71-464. Weaker than Georgia's automatic six-business-day rule but stronger than states with no itemization statute.
2. **First-party insurance bad-faith is a recognized common-law tort** under *Braesch v. Union Ins. Co.* (1991), giving fully-insured policyholders a tort remedy that the Unfair Insurance Trade Practices Act denies on its own.
3. **Nebraska's small-claims forum bars attorneys at trial**, which structurally favors pro se patients against in-house hospital billing departments who must appear without counsel.

## Hospital itemization right

- **Statute:** **Neb. Rev. Stat. § 71-464** — enacted Laws 2009, LB288, § 32
- **Source:** [law.justia.com/codes/nebraska/chapter-71/statute-71-464](https://law.justia.com/codes/nebraska/chapter-71/statute-71-464/); official text at [nebraskalegislature.gov/laws/statutes.php?statute=71-464](https://nebraskalegislature.gov/laws/statutes.php?statute=71-464)
- **What it requires:**
  - Upon **written request** of a patient or a patient's representative, a health care facility or health care practitioner facility shall provide an itemized billing statement, **including diagnostic codes**, without charge.
  - The statement must be provided **within fourteen (14) days after the request**.
- **Trigger:** Request-based — the duty does not arise automatically. The patient must send a written request to start the 14-day clock. Always send certified mail to crystallize the date.
- **Scope:** Both inpatient and outpatient settings, and reaches "health care practitioner facilities" (physician offices, clinics) as well as hospitals. Broader provider reach than Georgia's inpatient-only rule, narrower trigger.
- **Private right of action:** No express private remedy in § 71-464 itself. Non-compliance can be cited as a deceptive or unconscionable practice under the **Nebraska Consumer Protection Act** (§ 59-1602, see below) or **Uniform Deceptive Trade Practices Act** (§ 87-303), which both carry private remedies.
- **ERISA:** Not preempted — regulates the provider, not the plan.

## Unfair Insurance Trade Practices Act

- **Statute:** **Neb. Rev. Stat. § 44-1525** (listed practices); the chapter generally is § 44-1521 et seq.
- **Source:** [nebraskalegislature.gov/laws/statutes.php?statute=44-1525](https://nebraskalegislature.gov/laws/statutes.php?statute=44-1525); [codes.findlaw.com/ne/chapter-44-insurance/ne-rev-st-sect-44-1525](https://codes.findlaw.com/ne/chapter-44-insurance/ne-rev-st-sect-44-1525.html)
- **Substance:** Enumerates 14 categories of unfair trade practices in the business of insurance — misrepresentative comparisons of policy benefits, deceptive advertising, failure to respond to department inquiries within 15 working days, unfair discrimination in rates, failure to maintain complaint records, and related conduct. To be actionable, the practice must either be "committed flagrantly and in conscious disregard" of the act or "committed with such frequency as to indicate a general business practice."
- **Critical caveat:** **No private right of action.** Nebraska Supreme Court annotations to § 44-1525 state: "Sections of Nebraska Unfair Competition Act and Trade Practices Act governing insurance business do not contemplate private suits but only suits by State Director of Insurance." Enforcement is by the Nebraska Director of Insurance only.
- **Use:** Cite UITPA violations in your complaint to the Nebraska Department of Insurance and as evidentiary support for a *Braesch* common-law bad-faith claim. Do not plead UITPA as a standalone count in litigation.

## Bad-faith failure to pay (common-law tort)

- **Authority:** **Braesch v. Union Ins. Co., 237 Neb. 44, 464 N.W.2d 769 (1991)** — first-party insurance bad-faith recognized as an independent tort
- **Source:** [law.justia.com/cases/nebraska/supreme-court/1991/772-4.html](https://law.justia.com/cases/nebraska/supreme-court/1991/772-4.html); [courtlistener.com/opinion/1835332/braesch-v-union-ins-co](https://www.courtlistener.com/opinion/1835332/braesch-v-union-ins-co/)
- **Substance:** Nebraska was the 36th jurisdiction to recognize first-party insurance bad-faith. To prevail, the policyholder must show (1) **absence of a reasonable basis** for denying benefits of the policy, and (2) the insurer's **knowledge or reckless disregard** of the lack of a reasonable basis for denying the claim. The standard is essentially the *Anderson v. Continental* test adopted from Wisconsin.
- **Damages:** Common-law tort recovery — actual damages including emotional distress, plus potentially **punitive-equivalent extra-contractual damages** (Nebraska does not allow true punitives; analogous relief comes through extra-contractual compensatory awards). No statutory penalty cap.
- **Standing:** Only (1) an injured policyholder who is also a "covered person" or (2) a policyholder who is also a beneficiary may bring the tort. The Nebraska Supreme Court has recently narrowed standing to **exclude** medical providers holding assignments of benefits (see *Millard Gutter Co. v. Farm Bureau* (2021) and progeny — contractors-with-assignment cannot sue for bad faith).
- **ERISA preemption:** *Braesch* bad-faith is **preempted** as applied to self-funded ERISA employer plans. For ERISA self-funded plans, the federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) fees — no state tort recovery. The claim remains in play for fully-insured plans, Medicaid managed care, and individual/marketplace plans.
- **Procedural notes:** No statutory 60-day demand requirement (unlike Georgia's § 33-4-6). A written demand is still a near-universal practice point — it forces the insurer to articulate its denial rationale and is best evidence on the "reasonable basis" prong.

## Out-of-Network Emergency Medical Care Act (Nebraska surprise-billing layer)

- **Statute:** **Neb. Rev. Stat. §§ 44-6834 to 44-6850** — Out-of-Network Emergency Medical Care Act
- **Original enactment:** LB 997 (2020), effective January 1, 2021
- **Sources:** [nebraskalegislature.gov/laws/statutes.php?statute=44-6834](https://nebraskalegislature.gov/laws/statutes.php?statute=44-6834); [nebraskalegislature.gov/laws/statutes.php?statute=44-6849](https://nebraskalegislature.gov/laws/statutes.php?statute=44-6849); DOI consumer summary at [doi.nebraska.gov/consumer/no-surprises-act-new-protection-surprise-balance-bills](https://doi.nebraska.gov/consumer/no-surprises-act-new-protection-surprise-balance-bills)

### What it prohibits

- Balance billing for **emergency services** rendered by an out-of-network (OON) health care professional or facility.
- Patient cost-sharing is held to the in-network amount and counts toward the in-network deductible and out-of-pocket maximum.
- The insurer-provider payment dispute is resolved between them under § 44-6850; the patient is not a party.

### Payment standard (§ 44-6849)

A claim or payment is presumed reasonable if based on the higher of:

- the contracted rate under any then-existing in-network contract between the insurer and the OON provider for the same or similar services, or
- **175% of the Medicare rate** for the same or similar services in the same geographic area.

This is the rate that backstops the federal NSA's qualifying-payment-amount methodology for Nebraska emergency services.

### Where Nebraska falls short of states like Georgia

- **Emergency services only.** Does not extend to non-emergency ancillary OON services at in-network facilities (anesthesia, radiology, pathology). Federal NSA fills this gap for fully-insured and self-funded plans.
- **Does not cover ground ambulance.** No state-law balance-billing protection for ground ambulance — and the federal NSA explicitly excludes it. This is Nebraska's biggest patient-protection gap.
- **ERISA preemption:** does not reach self-funded employer plans; those rely on the federal NSA only.

### Caveats

- Excludes air ambulance (federal NSA covers it), workers' compensation, Medicare, and Medicaid.
- The Nebraska DOI has a Collaborative Enforcement Agreement with federal agencies and is the initial point of contact for federal-NSA noncompliance complaints originating in Nebraska.

## Regulatory agencies

### Nebraska Department of Insurance (NDOI)

- **Online complaint:** [doi.nebraska.gov/consumer/file-complaint](https://doi.nebraska.gov/consumer/file-complaint)
- **Phone:** main **(402) 471-2201**; Consumer Hotline (in-state) **1-877-564-7323**; TDD **(800) 833-7352**
- **Email:** doi.insurancecomplaints@nebraska.gov
- **Mail:**
  > Nebraska Department of Insurance
  > PO Box 95087
  > Lincoln, NE 68509-5087
- **Authority:** all insurance companies licensed in Nebraska, including fully-insured health insurers, HMOs, and PPOs. Administers the Out-of-Network Emergency Medical Care Act and UITPA. Initial point of contact for federal NSA complaints in Nebraska under the Collaborative Enforcement Agreement. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and does not regulate providers or debt collectors directly (route to AG).

### Nebraska Attorney General — Consumer Protection Division (Consumer Affairs Response Team)

- **Online complaint:** [protectthegoodlife.nebraska.gov](https://protectthegoodlife.nebraska.gov/) and [ago.nebraska.gov/consumer-protection](https://ago.nebraska.gov/consumer-protection); complaint portal at [nebraska.gov/apps-ago-complaints](https://www.nebraska.gov/apps-ago-complaints/)
- **Phone:** Consumer Affairs Response Team **(402) 471-2785**; toll-free **(800) 727-6432**
- **Email:** ago.consumer@nebraska.gov
- **Mail:**
  > Nebraska Attorney General
  > Consumer Protection Division
  > 1445 K Street, Room 2115
  > Lincoln, NE 68508
- **Authority:** enforces the **Nebraska Consumer Protection Act** (Neb. Rev. Stat. § 59-1601 et seq.) — UDAP statute prohibiting unfair, unconscionable, or deceptive acts in trade or commerce — and the **Uniform Deceptive Trade Practices Act** (§ 87-301 et seq.). Reach over providers, hospitals, third-party debt collectors, and original creditors. NCPA carries civil penalties up to $2,000 per violation (state-prosecuted) and a private remedy with actual damages, attorney's fees, and discretionary enhanced damages under § 59-1609.

### Nebraska Consumer Protection Act — private right of action

- **Statute:** **Neb. Rev. Stat. § 59-1602** (substantive prohibition), **§ 59-1609** (private remedy)
- **Source:** [nebraskalegislature.gov/laws/statutes.php?statute=59-1602](https://nebraskalegislature.gov/laws/statutes.php?statute=59-1602); [law.justia.com/codes/nebraska/chapter-59/statute-59-1601](https://law.justia.com/codes/nebraska/chapter-59/statute-59-1601/)
- **Substance:** "Unfair methods of competition and unfair or deceptive acts or practices in the conduct of any trade or commerce shall be unlawful." § 59-1609 lets an injured person file in district court for an injunction, actual damages, costs, and reasonable attorney's fees. The court may increase damages to an amount bearing reasonable relation to actual harm, except § 59-1602 violations are capped at $1,000 in enhanced damages.
- **Use:** Best Nebraska-specific lever against the **original creditor** (the hospital itself), parallel to Georgia's FBPA reach. Useful for misrepresentation of charges, upcoding, billing for services not rendered, misrepresenting in-network status, or coercive collection.

## Small claims court — County Court Small Claims docket

- **Court name:** **Small Claims Court** (a docket within the County Court; each Nebraska county has a County Court)
- **Jurisdictional limit:** **$3,900** historically per Neb. Rev. Stat. § 25-2802 and adjusted every five years. Currently **$6,000 from July 1, 2024 through June 30, 2025**, then **$7,500 from July 1, 2025 through June 30, 2030** per LB 139 (2024).
- **Source:** [nebraskalegislature.gov/laws/statutes.php?statute=25-2802](https://nebraskalegislature.gov/laws/statutes.php?statute=25-2802); [nebraskajudicial.gov/administration/news/nebraska-increases-jurisdictional-limits-small-claims-and-county-courts](https://nebraskajudicial.gov/administration/news/nebraska-increases-jurisdictional-limits-small-claims-and-county-courts)
- **Filing fees:** approximately $25 filing fee plus sheriff/process service. Varies by county; confirm with the County Court clerk.
- **Attorney rules:** **Attorneys are not permitted to represent parties at trial in Small Claims Court** (Neb. Rev. Stat. § 25-2804). The statute allows attorney appearance only "for the purpose of filing a motion for a new trial or to set aside, vacate, or modify a default judgment" — i.e., post-judgment relief only. A defendant can transfer the matter to the regular County Court docket (at least two days before the scheduled hearing, with the requisite fees) specifically to bring counsel. This bar applies to both sides — a corporate defendant such as a hospital must appear through a non-attorney officer or employee.
- **Jury trial:** not available in Small Claims Court. Either party may appeal de novo to District Court, where a jury is available.
- **Caveat — claim count limit:** Nebraska Rev. Stat. § 25-2803 limits any one plaintiff to **two small-claims filings per week** and **ten per calendar year** (with limited carve-outs for assignees). Most patient disputes are single filings, but be aware if you are bundling multiple bills.

## Statute of limitations

- **Written contracts:** **5 years from breach** — Neb. Rev. Stat. § 25-205
- **Oral contracts / statutory liabilities:** **4 years from breach** — Neb. Rev. Stat. § 25-206
- **Source:** [nebraskalegislature.gov/laws/statutes.php?statute=25-205](https://nebraskalegislature.gov/laws/statutes.php?statute=25-205); [nebraskalegislature.gov/laws/statutes.php?statute=25-206](https://nebraskalegislature.gov/laws/statutes.php?statute=25-206)

Most hospital admissions involve a signed financial-responsibility form — a written contract, so 5 years applies. Implied-in-fact medical billing arrangements without a signed agreement, and visits where the only writing is the patient registration card, may be treated as oral or partly-oral contracts (4 years). Nebraska courts apply the **shorter four-year period to any contract that is partly oral and partly written**, so a missing or unclear signed agreement defaults the limitations period to 4 years. The clock runs from breach (typically the day payment was due and not made), not from when the patient discovered the dispute.

Partial payment or written acknowledgment of the debt can restart the limitations clock under Nebraska law. **Do not make a partial payment on a time-barred medical bill without legal advice.**

## Ground ambulance balance billing

**Not covered by Nebraska state law.** Nebraska's Out-of-Network Emergency Medical Care Act (§§ 44-6834 to 44-6850) applies to emergency services rendered at health care facilities but does not extend balance-billing protections to ground ambulance services. The federal No Surprises Act also explicitly excludes ground ambulance.

This is the largest gap in Nebraska patient protection. As of April 1, 2025, 19 states have enacted ground-ambulance balance-billing protections; Nebraska is **not** one of them. A patient receiving an out-of-network ground ambulance balance bill in Nebraska has no direct state-law shield. Defensive levers in that situation:

- Challenge "reasonable value" under UCC § 2-305 and common-law principles when no price was disclosed or agreed.
- Cite the Nebraska Consumer Protection Act if the ambulance provider misrepresented network status, charges, or insurance coverage.
- Use Nebraska DOI's consumer-help process and request a federal NSA advisory determination, since federal regulators monitor non-NSA-applicable ambulance complaints for legislative purposes.
- Request charity-care/financial-assistance screening with the ambulance provider directly.

## Credit reporting

Nebraska has **not** enacted a state-specific medical-debt credit-reporting restriction. Nebraska is absent from the list of 14 states (CA, CO, CT, IL, ME, MD, MN, NJ, NY, NC, RI, VT, VA, WA) that prohibit medical debt on credit reports, and from the 5 states that restrict how and when it can appear (DE, FL, ID, NV, UT).

Patients in Nebraska rely on:

- The 2022-2023 voluntary changes by Equifax/Experian/TransUnion (paid medical debt removed; debt under $500 not reported; 1-year delay before reporting).
- Federal FCRA dispute rights (15 U.S.C. §§ 1681i, 1681s-2).
- The Nebraska Consumer Protection Act for deceptive furnishing of medical-debt information (UDAP angle on the furnisher).

**Federal preemption posture is in flux.** The CFPB issued an October 2025 interpretive rule taking the position that the FCRA preempts state laws restricting medical-debt credit reporting. If that survives challenge it limits the practical effect of any future Nebraska statute.

LB 779 (introduced 2025 session by Sen. Danielle Conrad) would prohibit health care facilities from charging interest or late fees on medical debt until 90 days after final invoice and cap interest at 3%. The bill had not been enacted as of this writing.

## Hospital lien statute

- **Citation:** **Neb. Rev. Stat. § 52-401**
- **Source:** [nebraskalegislature.gov/laws/statutes.php?statute=52-401](https://nebraskalegislature.gov/laws/statutes.php?statute=52-401); [law.justia.com/codes/nebraska/chapter-52/statute-52-401](https://law.justia.com/codes/nebraska/chapter-52/statute-52-401/)
- **Substance:** Physicians, nurses, chiropractors, hospitals, and emergency medical service providers may claim a lien for "usual and customary charges" for treatment of an injured person. The lien attaches **only to the sum awarded the injured person in judgment or obtained by settlement or compromise** from the party causing the injury. **Not a lien on the patient's home, wages, or bank accounts.**
- **Attachment vs. perfection:** The lien **attaches upon admission** to the hospital for treatment and is enforceable against the patient automatically, but **perfection is required to enforce against third parties** (the tortfeasor or the tortfeasor's insurer). Actual knowledge by the third party that the hospital treated the patient is **not** sufficient — written notice is required.
- **Perfection requirement:** Serve a **written notice** upon the person or corporation from whom damages are claimed, stating the lien amount and the nature of the services. If suit is already pending, filing notice in the pending action is sufficient. Nebraska Supreme Court requires "at least substantial compliance" with the notice requirements.
- **Effect on third-party insurers:** Upon perfection, the tortfeasor's insurer has a duty not to impair the lien. An insurer that settles directly with the injured patient despite a perfected lien is liable to the hospital directly for the lien amount.
- **Patient-side practice points:**
  - In a personal-injury settlement, **demand proof of perfection** (date and method of notice) before treating any lien as enforceable.
  - Many providers fail the substantial-compliance test — verify before negotiating reductions.
  - The lien cap is "usual and customary charges," not chargemaster. Push back on inflated chargemaster rates in lien negotiations.

## Hospital charity care

Nebraska has **no state statute** requiring a hospital financial-assistance policy beyond what federal law mandates. Non-profit hospitals are bound by IRS § 501(r) (federal FAP, plain-language summary, public posting, 240-day pre-collection period). For-profit and county/municipal hospitals have no state FAP mandate, though county "overseer of the poor" obligations under Neb. Rev. Stat. § 68-104 et seq. provide indirect indigent-care backstops.

The **Nebraska Medical Debt Relief Act** (Neb. Rev. Stat. § 45-1301 et seq., effective July 19, 2024) created a state program through the State Treasurer that contracts with a medical-debt relief coordinator to purchase and discharge medical debt of Nebraska residents at or below 400% of the federal poverty line, or with medical debt at least 5% of household income. Source: [nebraskalegislature.gov/laws/statutes.php?statute=45-1303](https://nebraskalegislature.gov/laws/statutes.php?statute=45-1303). This is downstream relief (debt discharge after the fact), not an upfront FAP obligation, but it is a uniquely Nebraska-specific lever — cite eligibility in dispute letters when the patient qualifies, both for moral suasion and because providers can sell qualifying accounts into the program.

Use Dollar For at [dollarfor.org/state_sheet/nebraska](https://dollarfor.org/state_sheet/nebraska/) for screening.

## Wage garnishment

- **Statute:** **Neb. Rev. Stat. § 25-1558** (tracks federal Consumer Credit Protection Act)
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a court judgment. Post-judgment, garnishment is capped at the lesser of (a) **25% of disposable earnings** (15% for the head of a family), (b) the amount by which weekly disposable earnings exceed 30 times the federal minimum hourly wage, or (c) any further reduction the court orders.
- **Source:** [nebraskalegislature.gov/laws/statutes.php?statute=25-1558](https://nebraskalegislature.gov/laws/statutes.php?statute=25-1558)
- **Proposed change:** LB 174 (2025 session) would cap medical-debt garnishment at **10% of disposable earnings** (20% if not head of family). Not enacted as of this writing — use the standard 25%/15% caps in dispute letters and check status before filing.
- **Use:** In response letters to collectors threatening garnishment without a judgment in hand, and in head-of-family hardship claims.

## Quick reference for letter rendering

When the LLM renders a Nebraska-bound letter, substitute these defaults:

- **State statute (itemization right):** **Neb. Rev. Stat. § 71-464** — written request triggers a 14-day duty to deliver an itemized statement with diagnostic codes at no charge. The dispute letter should embed a written request to start the clock.
- **State insurance department (CC line):** Nebraska Department of Insurance, PO Box 95087, Lincoln, NE 68509-5087 ([doi.nebraska.gov/consumer/file-complaint](https://doi.nebraska.gov/consumer/file-complaint))
- **State AG consumer protection (CC line):** Nebraska Attorney General, Consumer Protection Division, 1445 K Street, Room 2115, Lincoln, NE 68508 ([protectthegoodlife.nebraska.gov](https://protectthegoodlife.nebraska.gov/))
- **Small-claims court name:** **Small Claims Court of [county] County, Nebraska**
- **Small-claims jurisdictional limit (in 30-day warning):** **"$7,500 effective July 1, 2025, under Neb. Rev. Stat. § 25-2802 as amended by LB 139 (2024)"** — use the prior $6,000 figure if the contemplated filing date is before July 1, 2025
- **Filing fee (in 30-day warning):** "approximately $25 plus service costs, varies by county"
- **Statute of limitations (in 30-day warning):** "Neb. Rev. Stat. § 25-205 (five years for breach of written contract); § 25-206 (four years if oral or partly oral)"
- **For provider-side disputes (vs. insurer-side):** Cite the **Nebraska Consumer Protection Act § 59-1602** with private remedy under **§ 59-1609** (actual damages, attorney's fees, discretionary enhanced damages) in addition to UCC § 2-305.
- **For insurer-side bad-faith disputes (fully-insured only):** Cite the *Braesch v. Union Ins. Co.* common-law tort. There is **no statutory 60-day demand requirement** (unlike Georgia); a written demand is still best practice. Note ERISA preemption for self-funded plans.
- **For ground-ambulance balance bills:** Note that **no state-law protection applies** — focus on UCC § 2-305, NCPA misrepresentation theories, and charity-care/financial-assistance screening including the Nebraska Medical Debt Relief Program.

## Key Nebraska-specific advantages

Worth keeping in mind when triaging a Nebraska patient's bills:

1. **No attorneys at trial in Small Claims Court** — Neb. Rev. Stat. § 25-2804 bars counsel for both sides at trial. A hospital must appear through a non-lawyer employee, structurally favoring a prepared pro se patient. Hospitals can transfer out of Small Claims to County Court to bring counsel, but only if they file two days before the hearing and pay the additional fee, which raises their economic friction noticeably.
2. **NCPA original-creditor reach with attorney's fees** — § 59-1609 makes fee recovery realistic against the hospital itself (not just third-party collectors), mirroring Georgia's FBPA leverage. Mention in any 30-day warning letter.
3. **Braesch first-party bad-faith tort with no statutory cap** — unlike Georgia's § 33-4-6 50%-or-$5,000 statutory penalty, Nebraska tort recovery is uncapped (extra-contractual compensatory damages, no statutory ceiling). Strong leverage in fully-insured bad-faith disputes; useless against self-funded ERISA plans.
4. **Medical Debt Relief Program eligibility** — patients at or below 400% FPL (or with medical debt ≥5% of household income) may be eligible to have their debt purchased and discharged through the State Treasurer's program under § 45-1301 et seq. (effective July 19, 2024). Useful lever when negotiating with providers willing to sell into the program.
5. **Hospital-lien notice strictness** — *Substantial-compliance* perfection requirements under § 52-401 are frequently breached. In any personal-injury settlement context, demand proof of written-notice perfection before treating a hospital lien as enforceable.

## Known gaps and weaknesses

For completeness:

1. **No ground-ambulance balance-billing protection.** The single largest Nebraska patient-protection gap. Federal NSA does not fill it either.
2. **No state-law medical-debt credit-reporting restriction.** Relies on FCRA and voluntary CRA changes.
3. **Itemization right is request-based, not automatic.** Less leverage than Georgia's automatic six-business-day rule.
4. **UITPA has no private right of action.** All insurance-practice misconduct claims must channel through NDOI complaint or the *Braesch* common-law tort.
5. **Bad-faith standing narrowed.** Recent Nebraska decisions (e.g., *Millard Gutter Co.* (2021)) exclude assignment-holding medical providers from *Braesch* standing — relevant if a provider claims the patient assigned bad-faith rights along with benefits.
