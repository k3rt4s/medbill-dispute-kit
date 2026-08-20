# Hawaii state pack

The fully-worked state-law layer for Hawaii patients. The LLM uses this when the patient's state is Hawaii. Tennessee equivalent at [`laws_state_tn.md`](laws_state_tn.md); Georgia at [`laws_state_ga.md`](laws_state_ga.md); California at [`laws_state_ca.md`](laws_state_ca.md).

All citations verified against public sources as of 2026-08-19. Re-verify annually. A short list of claims this pack could **not** verify appears at the end, under "Verification gaps." Do not fill those gaps with a guess.

Hawaii is different from every other state in this kit for one reason: the **Prepaid Health Care Act** (HRS Chapter 393), a 1974 law that requires most Hawaii employers to buy health coverage for their employees. Because it predates and survived a direct fight with ERISA, it changes which regulator a Hawaii patient complains to for some plans in ways that do not apply anywhere else in the kit. The rest of this pack's federal layer (No Surprises Act, IRS 501(r), CMS price transparency, ERISA generally) is covered in [`laws_federal.md`](laws_federal.md) and is not repeated here except where the Hawaii-specific overlay changes the analysis.

## The Prepaid Health Care Act and ERISA: two systems, one patient

This section is the reason this pack exists. Read it before routing a Hawaii patient's appeal anywhere.

**What the Act does.** HRS Chapter 393 requires almost every Hawaii employer with a "regular employee," defined as someone working at least twenty hours a week in non-seasonal work, and paid above a statutory wage floor, to enroll that employee in a "prepaid health care plan" meeting minimum benefit standards (**HRS §§ 393-3, 393-7, 393-11**). The employer must pay at least half the premium, and the employee's share is capped at 1.5% of wages (**HRS § 393-13**). An employee already covered elsewhere (a federal-law plan, a spouse's plan, Medicaid) can file a waiver (**HRS § 393-17**). Enforcement of the coverage mandate itself sits with the Director of the Department of Labor and Industrial Relations (DLIR), not with the Insurance Division (**HRS §§ 393-31 to 393-34**).

**Why this collides with ERISA.** ERISA's preemption clause (29 U.S.C. § 1144(a)) wipes out state laws that "relate to" employee benefit plans. Hawaii's Act, requiring employers to structure and pay for a specific kind of benefit plan, is about as direct a hit as that clause was written to catch. A federal court held exactly that: **Standard Oil Co. of California v. Agsalud, 442 F. Supp. 695 (N.D. Cal. 1977), aff'd, 633 F.2d 760 (9th Cir. 1980), aff'd by an equally divided Court, 454 U.S. 801 (1981)**. The citations to this history are preserved in the official case notes to HRS § 393-1 itself.

**The narrow fix.** Hawaii's congressional delegation got Congress to carve the Act back out of preemption: **29 U.S.C. § 1144(b)(5)**, added by **Pub. L. No. 97-473, § 301** (signed January 14, 1983). The text is narrow and worth reading closely:

- Subparagraph (A) exempts the Hawaii Prepaid Health Care Act from ERISA preemption.
- Subparagraph (B) takes most of that back: the exemption does **not** cover any state tax law relating to employee benefit plans, and it does **not** cover "any amendment of the Hawaii Prepaid Health Care Act enacted after September 2, 1974, to the extent it provides for more than the effective administration of such Act as in effect on such date." In plain terms, only the 1974 version of the mandate, administered as it existed then, is protected. Substantive expansions since then are exposed to ordinary ERISA preemption again. A 1978 amendment to the Act was itself later held preempted on this basis: **Council of Hawaii Hotels v. Agsalud, 594 F. Supp. 449 (D. Haw. 1984)**, cited in the same official case notes.
- Subparagraph (C) preserves ERISA's Part 1 (reporting and disclosure) and Part 4 (fiduciary responsibility) provisions over the Hawaii Act "as in effect on or after January 14, 1983." That means the exemption protects Hawaii's power to require an employer to buy the coverage; it does **not** exempt the resulting plan from ERISA's federal fiduciary duties, disclosure rules, or claims-procedure regulation once the plan exists.

**What this means for routing an appeal.** The practical result is that the PHCA mandate and the ordinary ERISA/insurance analysis run on two separate tracks, and a Hawaii patient's complaint has to be sorted into the right one:

1. **"My employer isn't giving me any qualifying coverage at all," or "my employer is mishandling premium withholding."** This is a DLIR non-coverage matter under HRS §§ 393-11, 393-13, 393-31 to 393-34, not an insurance-claim appeal. It does not matter whether the plan the employer eventually provides is insured or self-funded; the mandate to offer coverage is the same either way.
2. **"My claim was denied," or "my insurer is slow-walking my claim."** This runs through the ordinary national ERISA/insurance analysis, exactly as it would in any other state pack in this kit, with one extra Hawaii-specific option layered on top for insured plans (HRS Chapter 432E's external review, below):
   - **Government employer (state or county, including the Hawaii Employer-Union Health Benefits Trust Fund) or church employer:** not an ERISA plan at all. Appeals run through the plan's own administrative process and, for insurance-regulated conduct, the Hawaii Insurance Division.
   - **Private employer, self-funded plan** (the employer bears the claims risk, often through a third-party administrator): an ERISA plan. Claims and denials go through the plan's ERISA claims procedure, then DOL EBSA (1-866-444-3272) or a federal civil action under 29 U.S.C. § 1132(a)(1)(B). The Hawaii Insurance Division has no jurisdiction over the self-funded plan itself.
   - **Private employer, fully-insured plan** (premiums paid to a licensed insurer or HMO that bears the risk): still an ERISA plan for claims-procedure purposes, but the insurance policy itself is subject to Hawaii insurance law under ERISA's savings clause. The Hawaii Insurance Division can investigate the insurer's claims-handling conduct (HRS Chapter 431, below), and the patient can also use HRS Chapter 432E's internal/external review process alongside the ERISA appeal.
3. Ask the employer's benefits office, or read the Summary Plan Description, to find out which of these three the plan actually is. "Self-funded," "self-insured," or "the plan sponsor bears the risk" points to track 2; "this is an insurance policy issued by [carrier]" points to track 3. The insurer's logo on the ID card does not resolve this; a self-funded plan is commonly administered by a familiar insurance brand and still is not an ERISA-insured plan.

**Where this is genuinely unclear.** Whether a specific dispute falls inside the narrow, 1974-frozen scope of the PHCA exemption, versus outside it and therefore preempted, is a fact-specific legal question that has already produced real, effort-intensive litigation (the two cases above). This pack does not have the authority to resolve a live dispute over that boundary, and neither does a patient acting alone. If a Hawaii patient's problem is specifically "does the PHCA mandate reach my situation" rather than the more common "my claim was denied" or "my employer isn't covering me at all," say so plainly and point them to an employment-benefits attorney or the DLIR directly, rather than asserting an answer.

## Hospital itemization right

No Hawaii statute requiring hospitals to produce an itemized bill on patient request could be verified for this pack. HRS Chapter 432E (Patients' Bill of Rights and Responsibilities Act) covers complaint and appeal procedures for insurance determinations, not itemized billing, and general "patient rights" language published by individual Hawaii hospitals appears to be internal policy rather than a codified state right.

Use the federal fallback instead: the HIPAA Privacy Rule's right of access, **45 C.F.R. § 164.524**, gives every patient a federal right to billing records held in the provider's designated record set, with a **30-day response deadline** (one 30-day extension permitted). See [`laws_federal.md`](laws_federal.md). Pair this with the federal Hospital Price Transparency Rule (45 CFR Part 180) if the hospital's posted standard charges are needed for comparison.

## Unfair claims settlement practices

- **Statute:** **HRS §§ 431:13-102, 431:13-103** (through 431:13-108), part of the Hawaii Insurance Code's Unfair Methods of Competition and Unfair or Deceptive Acts or Practices article.
- **Source:** [codes.findlaw.com/hi/division-2-business/hi-rev-st-sect-431-13-102](https://codes.findlaw.com/hi/division-2-business/hi-rev-st-sect-431-13-102/); [codes.findlaw.com/hi/division-2-business/hi-rev-st-sect-431-13-103](https://codes.findlaw.com/hi/division-2-business/hi-rev-st-sect-431-13-103/)
- **Substance:** § 431:13-102 bars unfair or deceptive acts or practices in the business of insurance. § 431:13-103(11) defines unfair claims-settlement practices, including misrepresenting policy provisions, and **failing to respond with reasonable promptness, in no case more than fifteen working days, to communications** about a claim. It also requires an insurer to offer payment **within thirty calendar days** of affirming liability once the amount is determined, and to investigate claims reasonably before denying them.
- **Critical caveat:** **No private right of action.** The NAIC's own private-rights-of-action survey confirms Hawaii's remedy under §§ 431:13-103 to 431:13-108 is administrative only, enforced by the Insurance Commissioner. Source: [content.naic.org, "Private Rights of Action for Unfair Claims Settlement Practices"](https://content.naic.org/sites/default/files/model-law-chart-mc-55-private-rights-of-action-for-unfair-claims-settlement-practices.pdf) (Hawaii row). Cite this statute in an Insurance Division complaint, not as a stand-alone count in a lawsuit.

## Bad-faith failure to pay

- **Case:** **Best Place, Inc. v. Penn America Ins. Co., 82 Haw. 120, 920 P.2d 334 (1996)**.
- **Source:** confirmed via the NAIC private-rights-of-action chart cited above, which lists this exact citation and holding for Hawaii.
- **Substance:** Hawaii recognizes an independent tort for an insurer's breach of the implied covenant of good faith and fair dealing in handling a first-party claim, giving the insured a private cause of action separate from the underlying contract claim. This is a common-law remedy, not a statute; it exists precisely because § 431:13-103 (above) does not give the insured a private right of action.
- **Third-party claims:** Hawaii courts have held there is **no independent third-party bad-faith action**, though an insured can assign their own bad-faith claim to a third party, who can then pursue it. **Simmons v. Puu, 94 P.3d 667 (Haw. 2004)**; **Hough v. Pacific Ins. Co., 927 P.2d 858 (Haw. 1996)**. Same NAIC chart source.
- **ERISA preemption:** As in every other state, a common-law bad-faith tort claim against a self-funded ERISA plan is preempted; the federal remedy for that plan type is 29 U.S.C. § 1132(a)(1)(B), with no state bad-faith penalty available. The Best Place tort is available for fully-insured plans, individual/marketplace plans, and plans that are not ERISA plans at all (government, church). See the routing framework above to determine which applies.

## Surprise billing

No Hawaii statute broader than the federal No Surprises Act, comparable to California's AB 72, New York's Article 49, Texas's SB 1264, Maryland's all-payer model, Washington's Balance Billing Protection Act, or Georgia's HB 888, could be verified for this pack. The one Hawaii-specific provision located, **HRS § 431:26-104** (part of Article 26, Health Benefit Plan Network Access and Adequacy), is a narrower thing: it requires a health carrier's contract with a participating (in-network) provider to include a hold-harmless clause barring that provider from billing the patient beyond copays, coinsurance, and deductibles, including if the carrier becomes insolvent or breaches the contract (**HRS § 431:26-104(b), (c)**).

- **Source:** [codes.findlaw.com/hi/division-2-business/hi-rev-st-sect-432e-1](https://codes.findlaw.com/hi/division-2-business/hi-rev-st-sect-432e-1/) references the Article 26 "health carrier" definition; substance of § 431:26-104 confirmed via [managedcarelegaldatabase.org's summary of HRS Title 24, Chapter 431, Article 26](https://www.managedcarelegaldatabase.org/state-law/title-24-insurance-chapter-431-insurance-code-article-26-health-benefit-plan-network-access-and-adequacy-2).
- **Do not confuse this with out-of-network surprise-billing protection.** § 431:26-104 protects a patient from being billed by their own in-network provider if the carrier fails to pay that provider. It does not address an out-of-network emergency provider or facility billing the patient directly, which is exactly the scenario the federal No Surprises Act already covers. For Hawaii patients, the operative protection against out-of-network surprise bills is the federal NSA; see [`laws_federal.md`](laws_federal.md).

## Ground ambulance balance-billing

No Hawaii statute closing the federal No Surprises Act's ground-ambulance gap could be verified for this pack, despite a genuine effort to find one (including checking the Commonwealth Fund's state ground-ambulance tracker, which could not be retrieved directly). As with most states, ground ambulance in Hawaii is not protected beyond ordinary contract and billing-practice review. If a Hawaii patient's dispute involves a ground-ambulance bill, use the general pattern in [`rules/10_ground_ambulance.md`](../rules/10_ground_ambulance.md) rather than assuming a state-specific protection exists.

## Hawaii's internal and external review process (HRS Chapter 432E)

- **Statute:** **HRS §§ 432E-1 (definitions), 432E-5 (complaints and appeals procedure)**, the Patients' Bill of Rights and Responsibilities Act.
- **Source:** [codes.findlaw.com/hi/division-2-business/hi-rev-st-sect-432e-5](https://codes.findlaw.com/hi/division-2-business/hi-rev-st-sect-432e-5/); [codes.findlaw.com/hi/division-2-business/hi-rev-st-sect-432e-1](https://codes.findlaw.com/hi/division-2-business/hi-rev-st-sect-432e-1/)
- **Substance:** A "health carrier" (an entity subject to Hawaii's insurance laws or the Insurance Commissioner's jurisdiction) must decide an **expedited internal appeal within 72 hours** of the request, and must send its **final internal determination within 60 days** of the complaint. The final-determination notice must tell the enrollee they have **130 days to request an external review**.
- **Scope, and the gap in the statutory text:** § 432E-1's definitions do not explicitly exclude self-funded ERISA plans from "health carrier." The general federal deemer-clause doctrine, applied identically in this kit's California pack for the DMHC/IMR process, is that a self-funded employer plan is not "engaged in the business of insurance" and so falls outside a state's insurance-regulatory definitions regardless of state statutory wording; self-funded plans instead use the federal external-review process under 29 C.F.R. § 2590.715-2719. This is the standard national rule, not something confirmed specifically for Hawaii's Chapter 432E by a court, so treat it as the well-established default rather than a certainty for every possible plan structure. See the routing framework above.

## Regulatory agencies

### Hawaii Insurance Division (Department of Commerce and Consumer Affairs)

- **Mailing address (health/general complaints):** Insurance Division, State of Hawaii, P.O. Box 3614, Honolulu, Hawaii 96811.
- **Phone:** (808) 586-2790.
- **Source:** [files.hawaii.gov/dcca/ins/consumer/filing_a_complaint/how-to-file-a-complaint-against-all-other-insurers/complaint_form.pdf](https://files.hawaii.gov/dcca/ins/consumer/filing_a_complaint/how-to-file-a-complaint-against-all-other-insurers/complaint_form.pdf), the Division's own Complaint/Inquiry Form.
- **Authority over:** insurers and HMOs licensed in Hawaii, including fully-insured health plans, administering the Unfair Claims Settlement Practices article and HRS Chapter 432E's external review. **No authority over self-funded ERISA plans** (route to DOL EBSA, 1-866-444-3272) and no authority over hospitals, physicians, or debt collectors directly.
- The Division's main website (cca.hawaii.gov/ins) lists an additional toll-free consumer line reported at 1-844-808-DCCA (3222); this could not be independently confirmed by direct retrieval for this pack (see Verification gaps), so lead with the mailing address and phone number above, which were confirmed directly from the Division's own complaint form.

### Hawaii Department of Labor and Industrial Relations (DLIR), Prepaid Health Care Act enforcement

- **Authority:** enforcement of the coverage mandate itself, HRS §§ 393-11, 393-31 to 393-34, sits with the DLIR Director, not the Insurance Division. Use this track for "my employer isn't providing coverage at all" complaints, not for a denied claim under a plan that already exists.
- Current contact details for DLIR's non-coverage investigation unit could not be independently confirmed by direct retrieval for this pack (see Verification gaps). Direct the patient to search "Hawaii DLIR Prepaid Health Care" or start at the Department's main site rather than mailing to an unconfirmed address.

### Office of Consumer Protection (Department of Commerce and Consumer Affairs)

- **Address (as of the most recent form this pack could retrieve, 2013):** State of Hawaii Office of Consumer Protection, 235 South Beretania Street, Honolulu, Hawaii 96813.
- **Phone (as of the same document):** (808) 586-2630; neighbor-island callers can reach the same Consumer Resource Center toll-free with a five-digit extension.
- **Source:** [files.hawaii.gov/dcca/ocp/brochures/complaint/WEB%20CF%202013.pdf](https://files.hawaii.gov/dcca/ocp/brochures/complaint/WEB%20CF%202013.pdf), the Office's own complaint brochure. This document is dated 2013; confirm the current suite number and phone at cca.hawaii.gov/ocp before mailing, since DCCA has since consolidated several of its intake lines under a general number reported elsewhere as 1-844-808-DCCA (3222), which this pack could not independently confirm.
- **Authority over:** unfair or deceptive acts or practices in trade or commerce, reaching providers, hospitals' billing offices, and third-party debt collectors under Hawaii's general consumer-protection law. Route provider- and collector-side disputes here rather than to the Insurance Division.

## Small claims court

- **Court name:** **Small Claims Division of the District Court**, one per judicial circuit.
- **Jurisdictional limit:** **$5,000**, exclusive of interest and costs. A claim for return of a residential security deposit may be brought regardless of amount, but that exception has no bearing on medical-billing disputes.
- **Statute:** **HRS § 633-27**.
- **Source:** [codes.findlaw.com/hi/division-4-courts-and-judicial-proceedings/hi-rev-st-sect-633-27](https://codes.findlaw.com/hi/division-4-courts-and-judicial-proceedings/hi-rev-st-sect-633-27/)
- **Filing fee:** **$35**, waivable on a showing of financial hardship.
- **Source:** [legalnavigatorhawaii.org, "Small Claims Actions"](https://legalnavigatorhawaii.org/resource/small-claims-actions/)
- **Attorney rule:** the statute does not generally bar attorneys; they are permitted but uncommon at this dollar ceiling. Attorneys are expressly barred only in one unrelated context, residential security-deposit disputes, which does not apply to a medical bill.

## Statute of limitations

- **Written and oral contracts:** **six years**, **HRS § 657-1** ("Actions for the recovery of any debt founded upon any contract, obligation, or liability... shall be commenced within six years next after the cause of action accrued, and not after.").
- **Source:** [data.capitol.hawaii.gov, HRS 657-1](https://data.capitol.hawaii.gov/hrscurrent/Vol13_Ch0601-0676/HRS0657/HRS_0657-0001.htm)

Hawaii does not distinguish written from oral contracts for this six-year period the way many states do; both get six years under the same section. Most hospital admissions involve a signed financial-responsibility form, so this six-year clock is the one to use in a 30-day warning letter and in evaluating whether a small-claims filing is time-barred. Do not wait the full six years; the paper trail is stronger while events are recent.

## Credit reporting

No Hawaii statute restricting medical debt on credit reports beyond the 2022-2023 voluntary bureau changes (paid medical collections removed, one-year reporting delay, collections under $500 excluded) could be verified for this pack. Hawaii has not joined the roughly fifteen states (California, Colorado, Connecticut, and others) that have passed a state-level medical-debt credit-reporting ban.

Hawaii did enact **Act 220 (2026)** (Senate Bill 3025), creating a Medical Debt Acquisition and Forgiveness Program inside the state's Office of Wellness and Resilience, which buys and cancels qualifying residents' medical debt (income at or below 400% of the federal poverty level, or medical debt exceeding 5% of annual income). This is a debt-cancellation program, not a credit-reporting law, and as of this pack's verification date only a small fraction of its funding had been appropriated. It does not itself guarantee correction of a credit report; a patient whose debt is cancelled under this program should still request written confirmation and check their credit report afterward.

- **Source:** [getoutofdebt.org, "Hawaii Just Passed a Law to Automatically Erase Medical Debt"](https://getoutofdebt.org/264946/hawaii-medical-debt-law-automatically-erase)

## Hospital lien statute

- **Statute:** **HRS § 507-4** ("Liens for services in personal injury cases").
- **Source:** [codes.findlaw.com/hi/division-3-property-family/hi-rev-st-sect-507-4](https://codes.findlaw.com/hi/division-3-property-family/hi-rev-st-sect-507-4/)
- **Substance:** A hospital, dentist, doctor, physician, or surgeon that treated a person for personal injuries may file a lien against a **judgment** that person later recovers for those injuries, by filing notice with the clerk of the circuit court before the judgment is satisfied. Where multiple providers hold liens and the recovery is insufficient to pay all of them in full, they share the proceeds proportionally rather than by priority of filing. Liens may be enforced by foreclosure in circuit court.
- **Scope:** attaches only to a personal-injury judgment or settlement against a third party (for example, an at-fault driver), not to the patient's home, wages, or bank accounts, and rarely matters outside an accident-related bill.

## Hawaii charity care

Hawaii has **no state-specific charity-care statute** beyond the federal floor. Non-profit hospitals remain bound by IRS § 501(r) (see [`laws_federal.md`](laws_federal.md)); Hawaii adds no additional state-level income threshold or discount requirement on top of that federal rule, and for-profit facilities have no charity-care mandate at all.

- **Source:** [dollarfor.org/state_sheet/hawaii](https://dollarfor.org/state_sheet/hawaii/), which also reports that Hawaii's federal-floor practice generally allows 240 days from the first post-discharge bill to apply, and 120 days from that first bill before a non-profit hospital may sell the debt or report it to a credit bureau.

Use the standard federal pattern: request the hospital's Financial Assistance Policy in writing, screen through [Dollar For](https://dollarfor.org) for free help applying, and apply before the account moves to collections.

## Quick reference for letter rendering

When the LLM renders a Hawaii-bound letter, substitute these defaults:

- **Itemized-bill request citation:** no state statute; cite **45 C.F.R. § 164.524** (HIPAA right of access, 30-day deadline, one 30-day extension).
- **Which regulator to CC on a claim-denial letter:** determine insured vs. self-funded vs. government/church first (see the routing framework above). Fully-insured private-employer plan: CC the Hawaii Insurance Division. Self-funded private-employer plan: CC DOL EBSA, not the Insurance Division. Government or church plan: CC the plan administrator and, if insured, the Insurance Division.
- **Insurance Division (CC line):** Insurance Division, State of Hawaii, P.O. Box 3614, Honolulu, Hawaii 96811, (808) 586-2790.
- **Provider- and collector-side complaints:** Office of Consumer Protection, Department of Commerce and Consumer Affairs, 235 South Beretania Street, Honolulu, Hawaii 96813 (confirm current suite/phone before mailing; see Verification gaps).
- **Employer non-coverage complaints (PHCA):** Hawaii Department of Labor and Industrial Relations, non-coverage enforcement under HRS §§ 393-11, 393-31 to 393-34 (confirm current contact before mailing; see Verification gaps).
- **Small-claims court name:** Small Claims Division, District Court of the [circuit] Circuit.
- **Filing fee (in a 30-day warning letter):** "$35, waivable for financial hardship."
- **Statute of limitations (in a 30-day warning letter):** "HRS § 657-1 (six years for a debt founded on contract, written or oral)."
- **Unfair claims settlement citation (regulatory complaint only, not a lawsuit):** HRS §§ 431:13-102, 431:13-103.
- **Bad-faith citation (private lawsuit, fully-insured or non-ERISA plans only):** *Best Place, Inc. v. Penn America Ins. Co.*, 82 Haw. 120, 920 P.2d 334 (1996).

## Key Hawaii-specific considerations

1. **The PHCA/ERISA split is the single most important routing decision in a Hawaii case.** Getting it wrong sends a denied-claim appeal to an agency with no jurisdiction, or misses the one track (DLIR non-coverage) that has no equivalent in any other state pack in this kit. Work through the routing framework above before drafting anything.
2. **The unfair-claims-settlement statute is regulator-only, exactly like most states.** Hawaii's real private leverage against an insurer is the common-law *Best Place* bad-faith tort, available for fully-insured and non-ERISA plans, not the statute itself.
3. **HRS Chapter 432E gives insured-plan patients an extra, fast internal-appeal clock** (72 hours expedited, 60 days standard) plus a 130-day window to escalate to external review, on top of whatever the plan's own ERISA-required internal appeal already provides. This is a genuine Hawaii-specific advantage for a patient on a fully-insured plan, and it is easy to miss because it looks, at first glance, like a duplicate of the federal process.
4. **The small-claims ceiling is comparatively low ($5,000)** and the filing fee comparatively cheap ($35). For a mid-sized disputed balance, this is a realistic, low-cost forum; for a larger bill, plan for regular district or circuit court instead.
5. **Do not assume ground-ambulance or broader surprise-billing protection exists.** Unlike California, Georgia, New York, Texas, Maryland, and Washington, Hawaii does not appear to have closed either gap as of this pack's verification date. Treat these as open federal-floor-only issues rather than assuming a state-law fallback.

## Verification gaps

The following could not be confirmed against a source this pack could directly retrieve, despite a genuine attempt. Do not treat these as settled until confirmed independently:

- **Current phone/address for the Hawaii Insurance Division's general consumer line and online complaint portal.** The Division's own complaint-form PDF (2010 revision) gave P.O. Box 3614, Honolulu, HI 96811 and (808) 586-2790, which this pack used as the primary contact. Search-engine summaries (not independently fetched) suggest a newer consolidated toll-free line, 1-844-808-DCCA (3222); this pack could not load cca.hawaii.gov directly (it returned HTTP 403 to every automated fetch attempt) to confirm that number or the current online portal URL.
- **Current phone/address for the Office of Consumer Protection.** The only document this pack could retrieve directly was a complaint brochure dated 2013, which may have a stale suite number and phone extension. cca.hawaii.gov/ocp could not be loaded directly for the same reason as above.
- **Current DLIR contact details for Prepaid Health Care Act non-coverage complaints.** labor.hawaii.gov returned HTTP 403 to every automated fetch attempt. This pack confirmed the correct enforcement authority and statutory basis (HRS §§ 393-31 to 393-34, the DLIR Director) directly from the official statute text, but could not confirm a current phone number, email, or complaint-form identifier.
- **Whether any Hawaii statute extends surprise-billing or balance-billing protection beyond the federal No Surprises Act, including for ground ambulance.** Search-tool summaries repeatedly asserted a "Hawaii Act 189" providing ground-ambulance balance-billing protection. This pack made a sustained, multi-angle effort to verify that claim (direct searches for the act's text, the Hawaii session-laws archive, and the Commonwealth Fund's state ground-ambulance tracker) and found no primary source confirming it; every direct search for "Act 189" text returned unrelated Hawaii legislation. That claim is deliberately **excluded** from this pack rather than included on the strength of a search summary alone.
- **The precise holdings of *Best Place, Inc. v. Penn America Ins. Co.*, *Standard Oil Co. of California v. Agsalud*, and *Council of Hawaii Hotels v. Agsalud*.** This pack confirmed the case names, citations, and general holdings through secondary sources (an NAIC regulatory chart, and the official case notes appended to HRS Chapter 393's text), but could not load the opinions themselves (law.justia.com and courtlistener.com either blocked automated retrieval or returned no usable text). The citations and general holdings described above are consistent across every source checked, but a contributor should read the opinions directly before relying on this pack for anything beyond the general shape of the doctrine.
