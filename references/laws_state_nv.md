# Nevada state pack

The fully-worked state-law layer for Nevada patients. The LLM uses this when the patient's state is Nevada. For other states, use `laws_state_template.md` to find equivalents, or one of the dedicated state files (Georgia: `laws_state_ga.md`, Tennessee: `laws_state_tn.md`, etc.).

All citations verified against public sources as of 2026-05-19. Re-verify annually.

Three things make Nevada's patient-side leverage unusually strong:

1. The **Unfair Claims Settlement Practices Act has an express private right of action for first-party insureds** at NRS § 686A.310(2). This is the headline Nevada advantage — most states' UCSPA statutes are regulator-only. Allstate Ins. Co. v. Miller, 212 P.3d 318 (Nev. 2009) and Wohlers & Co. v. Bartgis, 969 P.2d 949 (Nev. 1998) anchor the first-party doctrine.
2. The **Deceptive Trade Practices Act (NRS Chapter 598)** is a strong UDAP statute reaching original creditors, including hospital billing departments, with a private right of action under NRS § 41.600.
3. The **2021 medical-debt collection law (NRS §§ 649.366-.368)** imposes a mandatory 60-day pre-collection notification and caps collection fees at 5% — a Nevada-specific procedural lever against collectors.

The biggest Nevada gap relative to peer states is **ground ambulance** — Nevada's surprise-billing statute does not close the federal No Surprises Act gap for ground ambulance, so Nevada patients remain exposed to ground-ambulance balance bills.

## Hospital itemization right

- **Statute:** **NRS § 449.243** — "Itemized list of charges required; use of Uniform Billing and Claims Forms authorized; contracted rates; summary of charges"
- **Source:** [law.justia.com/codes/nevada/chapter-449/statute-449-243](https://law.justia.com/codes/nevada/chapter-449/statute-449-243/); statute index at [leg.state.nv.us/NRS/NRS-449.html](https://www.leg.state.nv.us/NRS/NRS-449.html)
- **What it requires:**
  - Hospitals must itemize charges **on a daily basis** for all services, equipment, supplies, and medicines, with specificity and in language understandable to an ordinary lay person.
  - The itemized list must be **timely provided after the patient is discharged at no additional cost**. The statute does not set a specific day count; "timely" is the operative word.
  - The hospital shall provide to any patient **upon request** a copy of the billing prepared under this section.
  - Uniform Billing and Claims Forms (UB-04 or equivalent established by the American Hospital Association) are authorized.
  - Hospitals must also prepare a **summary of charges for common services** for admitted patients and make it available to the public.
- **Scope:** All hospitals licensed in Nevada under NRS Chapter 449. Outpatient and ambulatory-surgery centers are also licensed under Chapter 449 and subject to the same general billing-transparency framework.
- **Private right of action:** Not on the face of § 449.243 itself. Enforcement is via the Nevada Division of Public and Behavioral Health (licensure) and the Bureau of Consumer Protection (deceptive-billing overlay under NRS Chapter 598).
- **Use:** Cite § 449.243 in the itemization-request letter to crystallize the duty and the timing demand. Pair with NRS § 598.0915 (deceptive trade practices) when the hospital refuses or stonewalls.

> Note: The user's brief asked whether this lived at NRS 449.255 or NRS 439B. The correct citation is **NRS 449.243**. NRS 449.255 deals with rate schedules; NRS Chapter 439B addresses cost-restraint and indigent-care obligations, not the line-item itemization right itself.

## Unfair Claims Settlement Practices Act — with private right of action

- **Statute:** **NRS § 686A.310** — "Unfair practices in settling claims; liability of insurer for damages"
- **Sources:** [law.justia.com/codes/nevada/chapter-686a/statute-686a-310](https://law.justia.com/codes/nevada/chapter-686a/statute-686a-310/); statute index at [leg.state.nv.us/Division/Legal/LawLibrary/NRS/NRS-686A.html](https://www.leg.state.nv.us/division/legal/lawlibrary/nrs/NRS-686A.html); plain-language explainer at [nevada.public.law/statutes/nrs_686a.310](https://nevada.public.law/statutes/nrs_686a.310)
- **Substance:** Subsection 1 enumerates 16 unfair claims-settlement practices — misrepresenting policy provisions, failing to acknowledge claims promptly, failing to adopt reasonable standards for prompt investigation, refusing to pay without conducting a reasonable investigation, not attempting in good faith to effectuate prompt fair settlement where liability is reasonably clear, etc.
- **Private right of action — the Nevada-specific lever:** Subsection 2 of § 686A.310 expressly states: *"an insurer is liable to its insured for any damages sustained by the insured as a result of the commission of any act set forth in subsection 1 as an unfair practice."* This is **codified, not judge-made**, and is the single most important Nevada-specific advantage in the insurance-side dispute toolkit.
- **First-party doctrine:** Confirmed in **Allstate Insurance Co. v. Miller, 125 Nev. 300, 212 P.3d 318 (2009)** — Nevada Supreme Court held the insurer's duty of good faith and fair dealing is enforceable through § 686A.310 by the first-party insured, with damages including the underlying loss plus consequential damages (emotional distress where proved) and, on a separate count, punitive damages under NRS § 42.005 if oppression, fraud, or malice is shown by clear and convincing evidence.
- **Third-party bar:** Gunny v. Allstate Ins. Co., 108 Nev. 344, 830 P.2d 1335 (1992) held there is **no third-party private right of action** under § 686A.310. The first-party / third-party distinction matters — only the insured (or assignee of the insured's rights) may sue, not a stranger to the policy.
- **No bad-faith pleading required for the statute:** A claimant need not prove common-law bad faith to recover under § 686A.310. Proof of any enumerated unfair practice that causes damage is sufficient. Pleading both § 686A.310 and common-law bad faith (see next section) is standard.
- **ERISA preemption:** § 686A.310 is **preempted** as applied to self-funded ERISA employer plans. The federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) attorney's fees — no state statutory remedy. § 686A.310 is in play for fully-insured plans, individual/marketplace plans, Medicaid managed care, and PEBP (Public Employees' Benefits Program, which is not ERISA).

## Common-law bad faith (first-party)

- **Leading case:** **Albert H. Wohlers & Co. v. Bartgis, 114 Nev. 1249, 969 P.2d 949 (1998)**, amended on reh'g 1999
- **Source:** [law.justia.com/cases/nevada/supreme-court/1999/28142-1.html](https://law.justia.com/cases/nevada/supreme-court/1999/28142-1.html); FindLaw mirror at [caselaw.findlaw.com/court/nv-supreme-court/1111170.html](https://caselaw.findlaw.com/court/nv-supreme-court/1111170.html)
- **Substance:** Nevada recognizes a first-party common-law tort of bad-faith refusal to pay, parallel to the statutory § 686A.310 claim. Wohlers affirmed a jury verdict of $8,757.75 in contract damages, $275,000 in emotional-distress compensatory damages, and $8,000,000 in punitive damages against the insurer and policy administrator in a medical-insurance dispute. The case is the standard Nevada citation for combined contract + tort + punitive recovery in a health-insurance bad-faith setting.
- **Elements:** (1) existence of a contract, (2) insurer's breach of the implied covenant of good faith and fair dealing, (3) the breach was unreasonable or without proper cause, (4) damages.
- **Damages:** Contract damages, consequential damages (including emotional distress in egregious cases), and punitive damages under NRS § 42.005 (capped at the greater of $300,000 or 3x compensatory, with exceptions, see § 42.005(2)).
- **Relationship to § 686A.310:** Plead in the alternative. The statutory claim has no malice/oppression requirement; the common-law claim opens the door to punitive damages without the statutory ceiling cap on damages-as-pleaded.
- **ERISA:** Same preemption posture as § 686A.310 — preempted for self-funded employer plans.

## Surprise Billing — AB 469 (2019), codified at NRS §§ 439B.700-.760

- **Statute:** **NRS §§ 439B.700 through 439B.760**, enacted by **Assembly Bill 469 (2019)**, effective **January 1, 2020**
- **Sources:** statute index at [leg.state.nv.us/nrs/nrs-439B.html](https://www.leg.state.nv.us/nrs/nrs-439B.html); definitions at [law.justia.com/codes/nevada/chapter-439b/statute-439b-700](https://law.justia.com/codes/nevada/chapter-439b/statute-439b-700/); AB 469 history at [leg.state.nv.us/App/NELIS/REL/80th2019/Bill/6896/Overview](https://www.leg.state.nv.us/App/NELIS/REL/80th2019/Bill/6896/Overview); DOI consumer FAQ at [doi.nv.gov/Consumers/Health_and_Accident_Insurance/Balance_Billing_FAQs](https://doi.nv.gov/Consumers/Health_and_Accident_Insurance/Balance_Billing_FAQs/)
- **Pre-NSA significance:** AB 469 was enacted **before** the federal No Surprises Act and is the stronger of the two for in-scope plans. Nevada deserves credit for being one of the early-mover states (~9 months ahead of the NSA's January 1, 2022 effective date).

### What it prohibits

- Balance billing for **medically necessary emergency services** rendered by an out-of-network (OON) provider or facility — the patient pays only the in-network cost-share (copay, coinsurance, deductible).
- Balance billing for **non-emergency services** rendered by an OON provider at an **in-network facility** (ancillary services — anesthesia, radiology, pathology, lab, etc.) where the patient lacked meaningful choice of provider.
- **24-hour stabilization-and-transfer protocol:** AB 469 requires the OON provider to coordinate transfer of the patient to an in-network facility within 24 hours once stabilized, after which the OON balance-billing protection lapses if the patient declines transfer in writing.
- Provider-payer rate disputes go to a state-administered resolution process: claims under $5,000 use Nevada's internal IDR; claims $5,000+ go to American Arbitration Association arbitration with reporting to the Office for Consumer Health Assistance (Nevada CHA).

### Where Nevada goes beyond — and falls short of — the federal NSA

- **Beyond NSA:** Nevada's statute predates the federal NSA and operates as a floor where the federal scheme defers to state law for fully-insured plans (NSA § 9816(a)(3) "specified state law" rule). For PEBP enrollees, Nevada-specific resolution applies.
- **Falls short:** **Ground ambulance is not covered** by NRS §§ 439B.700-.760. The Nevada DOI Balance Billing FAQ explicitly confirms: "The federal law doesn't address ground ambulance, so you may be responsible for these charges." Nevada has not closed this gap (contrast Georgia O.C.G.A. § 33-20E, which added ground ambulance via HB 286 in 2024).

### Caveats

- **ERISA preemption:** AB 469 does not directly reach self-funded ERISA employer plans. NRS § 439B.757 creates an **opt-in mechanism** for self-funded plans — plans that opt in get Nevada protections; plans that opt out fall back to the federal NSA. Always verify the plan's election status before relying on state-law protections.
- Excludes air ambulance (covered separately by the federal NSA), workers' compensation, Medicare, and Medicaid fee-for-service.
- The state law and federal NSA layer rather than displace; the patient gets the stronger of the two protections for any given service.

## Regulatory agencies

### Nevada Division of Insurance (DOI)

- **Online complaint portal:** [doi.nv.gov/Consumers/File-A-Complaint](https://doi.nv.gov/Consumers/File-A-Complaint/)
- **Contact page:** [doi.nv.gov/contact-us](https://doi.nv.gov/contact-us/)
- **Phone:**
  - Northern Nevada: **(775) 687-0700**
  - Southern Nevada: **(702) 486-4009**
  - Toll-free (statewide): **(888) 872-3234**
- **Offices:**
  > **Las Vegas:** 3300 W. Sahara Ave., Suite 275, Las Vegas, NV 89102
  >
  > **Carson City:** 1818 E. College Pkwy, Suite 103, Carson City, NV 89706
- **Authority:** All insurers licensed in Nevada, including fully-insured health insurers, HMOs, PPOs, Medicare supplement carriers. Administers AB 469 surprise-billing protections and § 686A.310 UCSPA. **No authority over self-funded ERISA plans that have opted out** (route to DOL EBSA at 1-866-444-3272); does not regulate providers, hospitals, or debt collectors (route to AG / Financial Institutions Division for collectors).

### Nevada Attorney General — Bureau of Consumer Protection (BCP) / Office of Consumer Affairs

- **Bureau page:** [ag.nv.gov/About/Consumer_Protection/Bureau_of_Consumer_Protection](https://ag.nv.gov/About/Consumer_Protection/Bureau_of_Consumer_Protection/)
- **Online complaint:** through the AG site; for in-state issues also Office for Consumer Health Assistance (CHA) at [dhhs.nv.gov/Programs/CHA](https://dhhs.nv.gov/Programs/CHA/) and **(888) 333-1597**
- **Phone:** Las Vegas (702) 486-3132; Carson City (775) 684-1100
- **Mail:**
  > Office of the Attorney General, Bureau of Consumer Protection
  > 100 N. Carson Street, Carson City, NV 89701
  >
  > (Las Vegas office: 8945 W. Russell Road, Suite 204, Las Vegas, NV 89148)
- **Authority — strong UDAP reach:**
  - Enforces the **Nevada Deceptive Trade Practices Act (NDTPA), NRS Chapter 598**. Statute index: [leg.state.nv.us/nrs/NRS-598.html](https://www.leg.state.nv.us/nrs/NRS-598.html); compiled at [law.justia.com/codes/nevada/chapter-598](https://law.justia.com/codes/nevada/chapter-598/).
  - "Deceptive trade practice" definitions are at NRS § 598.0915 ([nevada.public.law/statutes/nrs_598.0915](https://nevada.public.law/statutes/nrs_598.0915)) and §§ 598.0917-.0925.
  - **Private right of action under NRS § 41.600(2)(e):** any victim of consumer fraud (defined to include any deceptive trade practice under NRS Chapter 598) may bring a civil action and recover **damages, equitable relief, costs, and reasonable attorney's fees**.
  - Reaches **original creditors** including hospitals and their in-house billing departments — broader than the federal FDCPA which targets third-party collectors. This is the right hook for misrepresented charges, phantom services, and upcoding by the hospital itself.

### Financial Institutions Division (FID) — for medical-debt collectors

- **Authority:** Licenses and regulates collection agencies in Nevada under NRS Chapter 649. Administers the 2021 medical-debt collection law (NRS §§ 649.366-.368).
- **Phone:** Las Vegas (702) 486-4120; Carson City (775) 684-1830
- **Use:** File a complaint with FID against any collector that violates the 60-day notification rule, the 5% fee cap, or the voluntary-payment-during-notification protections in §§ 649.366-.368.

## Small claims court — Justice Court

- **Court name:** **Justice Court** (each township has one; called "Justice's Court" in some statutes)
- **Statute:** **NRS § 73.010** — "Jurisdiction of justice courts for small claims"
- **Sources:** [law.justia.com/codes/nevada/chapter-73/statute-73-010](https://law.justia.com/codes/nevada/chapter-73/statute-73-010/); chapter index at [leg.state.nv.us/nrs/NRS-073.html](https://www.leg.state.nv.us/nrs/NRS-073.html); Nevada Courts overview at [nvcourts.gov/aoc/discover_nevada_justice/small_claims_court](https://nvcourts.gov/aoc/discover_nevada_justice/small_claims_court); Civil Law Self-Help Center at [civillawselfhelpcenter.org/self-help/small-claims/overview-of-small-claims](https://www.civillawselfhelpcenter.org/self-help/small-claims/overview-of-small-claims)
- **Jurisdictional limit:** **$10,000** for money-only claims. Plaintiff may waive amounts above $10,000 to fit the case in small claims; claim-splitting to avoid the limit is prohibited.
- **Filing fees (Clark County / Las Vegas Justice Court, indicative 2024-2025):**
  - Claims up to $2,500: ~$30-$50
  - Claims $2,500.01-$5,000: ~$65-$75
  - Claims $5,000.01-$7,500: ~$110-$120
  - Claims $7,500.01-$10,000: **~$196**
  - Each Justice Court sets its own schedule under NRS § 4.060; verify with the specific township court before filing.
- **Attorney rules:** **Permitted, not required.** Either party may hire counsel. However, **attorney's fees are not recoverable** in small claims (NRS § 69.030 / § 69.050 except as provided by NRS § 597.860 / § 597.870 for certain consumer matters). This shifts the small-claims economics — the corporate defendant's counsel is paid out-of-pocket either way.
- **Jury trial:** Not available in Justice Court for small claims. Either party may appeal de novo to District Court.
- **Corporate representation:** Corporations and LLCs may appear through a designated officer, employee, or authorized representative in small claims under Justice Court rules — pro se corporate appearance is recognized for small claims, similar to (but narrower than) Georgia's Magistrate Court rule.

## Statute of limitations

- **Written contracts:** **6 years from breach** — **NRS § 11.190(1)(b)** ("An action upon a contract, obligation or liability founded upon an instrument in writing")
- **Oral contracts / open accounts:** **4 years from breach** — **NRS § 11.190(2)(c)**
- **Sources:** [law.justia.com/codes/nevada/chapter-11/statute-11-190](https://law.justia.com/codes/nevada/chapter-11/statute-11-190/); chapter index at [leg.state.nv.us/nrs/nrs-011.html](https://www.leg.state.nv.us/nrs/nrs-011.html); plain-language at [getthewin.com/resources/nrs-11-190](https://getthewin.com/resources/nrs-11-190/)
- **Accrual:** The clock runs from the **date of breach** (typically the day payment was due and not made), not from contract formation. For ongoing arrangements, NRS § 11.190 also provides that the period runs from "the last transaction or the last item charged or last credit given," and any payment on principal or interest restarts the limitation from the date of the last payment — the classic partial-payment revival rule.

Most hospital admissions involve a signed financial-responsibility form — a written contract, so **6 years** applies. Implied-in-fact billing arrangements without a signed agreement may be treated as open accounts or oral contracts (**4 years**). **Do not make a partial payment on a time-barred debt without legal advice** — under § 11.190, a partial payment will restart the clock from the payment date.

## Ground ambulance balance-billing

**Not covered by Nevada state law.** AB 469 (2019), codified at NRS §§ 439B.700-.760, **does not include ground ambulance** in its surprise-billing protections. The federal No Surprises Act also excludes ground ambulance. Nevada patients receiving ground-ambulance services from an out-of-network provider are exposed to balance billing.

This is the single largest gap in Nevada's patient-protection regime relative to peer states. Georgia (O.C.G.A. § 33-20E, as amended by HB 286 effective Jan 1, 2024), Colorado (C.R.S. § 25-3.5-1001 et seq.), and others have closed this gap; Nevada has not.

Practical implications for Nevada patients:

- For a ground-ambulance balance bill, the kit's leverage points shift to: (a) NDTPA / NRS Chapter 598 if charges are misrepresented or grossly excessive, (b) the medical-debt collection notice protections in NRS §§ 649.366-.368 before any collector action, (c) negotiation against the U&C rate as the only honest market benchmark, and (d) for indigent patients, NRS § 439B.320 indigent-care obligations.
- AB 393 (2023 session) was introduced to add ground ambulance to the surprise-billing scheme but did not pass. Re-verify the 2025 session enactment status before relying on this section.

## Credit reporting and medical-debt collection

Nevada **does not** have a state statute prohibiting medical-debt credit reporting outright (as of this writing). However, Nevada has a strong **pre-collection notification framework** that operates as a de facto delay on credit reporting:

- **Statute:** **NRS §§ 649.366-.368**, enacted by **SB 248 (2021)**, effective July 1, 2021
- **Sources:** [law.justia.com/codes/nevada/chapter-649/statute-649-366](https://law.justia.com/codes/nevada/chapter-649/statute-649-366/) (notification); [law.justia.com/codes/nevada/chapter-649/statute-649-367](https://law.justia.com/codes/nevada/chapter-649/statute-649-367/) (voluntary payment protections); [law.justia.com/codes/nevada/chapter-649/statute-649-368](https://law.justia.com/codes/nevada/chapter-649/statute-649-368/) (prohibited practices)
- **What it requires:**
  - A collection agency must send written notification by mail **at least 60 days before taking any action to collect** a medical debt, including the name of the provider, the date of service, and the amount.
  - **During the 60-day notification period, the collector may not report the debt to any credit reporting agency.** This is the operative credit-reporting restriction.
  - Collection fees are capped at **5%** of the debt collected.
  - Payments made during the notification period are treated as voluntary — the collector cannot use them as an admission of the debt for accrual or statute-of-limitations purposes.
- **Pending legislation:** **AB 204 (2025-2026 session)** would extend the prohibition by banning medical-debt reporting to credit bureaus altogether. Not enacted as of this writing — verify before relying on it.

**Federal preemption posture is in flux.** The CFPB issued an October 2025 interpretive rule asserting that the FCRA preempts state laws restricting medical-debt credit reporting. If that survives challenge, it limits any future Nevada law. The CFPB also finalized (January 2025) a separate rule removing medical debt from credit reports nationally; that rule's status is also under litigation.

For deceptive furnishing of medical-debt information to credit bureaus, the NDTPA's general deceptive-practices provisions may apply via NRS § 598.0915 (private remedy under § 41.600), in addition to a federal FCRA claim against the furnisher under 15 U.S.C. § 1681s-2.

## Hospital charity care

Nevada imposes **partial state-law obligations beyond federal § 501(r)**:

- **NRS § 439B.260** — Major hospitals (200+ licensed beds) must reduce or discount the total billed charge by **at least 30 percent** for hospital services provided to **inpatients** who (a) have no insurance or other contractual payment source, (b) are not eligible for state or federal public assistance, and (c) make reasonable arrangements within **30 days after discharge** to pay the hospital bill. Source: [law.justia.com/codes/nevada/2010/title40/chapter439b/nrs439b-260.html](https://law.justia.com/codes/nevada/2010/title40/chapter439b/nrs439b-260.html).
- **NRS §§ 439B.300-.340** — Hospitals must provide care to a "proportionate share" of indigent patients; counties pay for indigent inpatient care above the hospital's minimum obligation. Definitions at [nevada.public.law/statutes/nrs_439b.310](https://nevada.public.law/statutes/nrs_439b.310). The county-payment mechanism is at NRS § 439B.330.
- **NAC § 439B.325** — Major hospitals must disclose to uninsured patients the availability of the 30% discount and how to request it. Source: [law.cornell.edu/regulations/nevada/NAC-439B-325](https://www.law.cornell.edu/regulations/nevada/NAC-439B-325).
- **Federal floor:** Non-profit hospitals remain bound by IRS § 501(r). For-profit and county/municipal hospitals are bound by Nevada-specific obligations above, not by § 501(r).
- **Use:** For uninsured Nevada patients at major hospitals (200+ beds — covers most acute-care hospitals in the Las Vegas and Reno markets), cite **NRS § 439B.260** to demand the **automatic 30% discount** as a non-discretionary statutory entitlement, distinct from any "financial assistance policy" offered by the hospital. Pair with Dollar For at [dollarfor.org/state_sheet/nevada](https://dollarfor.org/state_sheet/nevada/) for federal-side screening.

## Hospital lien statute

- **Citations:** **NRS §§ 108.590 through 108.660** — Liens of Hospitals subchapter, Chapter 108 (Statutory Liens)
- **Sources:** [law.justia.com/codes/nevada/chapter-108/statute-108-590](https://law.justia.com/codes/nevada/chapter-108/statute-108-590/); chapter index at [leg.state.nv.us/nrs/nrs-108.html](https://www.leg.state.nv.us/nrs/nrs-108.html); related notice/perfection statute at [law.justia.com/codes/nevada/2022/chapter-108/statute-108-610](https://law.justia.com/codes/nevada/2022/chapter-108/statute-108-610/)
- **Substance (§ 108.590):** When a person receives hospitalization on account of an injury and claims damages from a third party responsible for the injury, the hospital has a lien upon any sum awarded by **judgment, settlement, or compromise** for the reasonable value of hospital services rendered before the date of judgment/settlement. **The lien attaches to the third-party recovery, not to the patient's home, wages, or bank accounts.**
- **Limitation:** The lien is **not valid** against persons covered by NRS Chapters 616A-616D (workers' compensation) or Chapter 617 (occupational diseases) — workers' comp claims are excluded.
- **Perfection requirements (NRS § 108.610):**
  - Record a verified **notice of lien with the county recorder** of (a) the county where the hospital is located, **and** (b) the county where the injury was suffered (if different).
  - **Serve a certified copy by registered or certified mail** on the person alleged to be responsible for causing the injury, **before** the date of judgment, settlement, or compromise.
- **Use:** Always confirm the hospital perfected its lien correctly. Failure to record in both counties (when applicable) or failure to serve the at-fault party by certified mail before settlement invalidates the lien. Also confirm the underlying charges are "reasonable" — Nevada follows the reasonable-value rule, not full-billed-charges, so the lien is challengeable on quantum.

## Wage garnishment

- **Statute:** **NRS § 31.295** and the writ-of-execution scheme in NRS Chapter 31; federal Consumer Credit Protection Act caps apply under NRS § 31.295(2).
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a court judgment. Post-judgment, garnishment is capped at the federal 25% of disposable earnings, or the amount by which weekly disposable earnings exceed 50× the Nevada minimum wage, whichever is less (Nevada's 50x multiplier is more protective than the federal 30x for low-wage earners; verify current minimum wage).
- **Use:** In response letters to collectors threatening garnishment without a judgment in hand.

## Quick reference for letter rendering

When the LLM renders a Nevada-bound letter, substitute these defaults:

- **State statute (itemization right):** **NRS § 449.243** — daily itemization with timely post-discharge delivery; copy provided on patient request.
- **State insurance department (CC line):** Nevada Division of Insurance, Consumer Services, 1818 E. College Pkwy, Suite 103, Carson City, NV 89706 (or Las Vegas office at 3300 W. Sahara Ave., Suite 275, Las Vegas, NV 89102). Toll-free **(888) 872-3234**.
- **State AG consumer protection (CC line):** Office of the Attorney General, Bureau of Consumer Protection, 100 N. Carson Street, Carson City, NV 89701.
- **Small-claims court name:** **Justice Court of [township], [county] County, Nevada**
- **Filing fee (in 30-day warning):** "$30-$196 depending on claim amount and township"
- **Statute of limitations (in 30-day warning):** "NRS § 11.190(1)(b) (six years for breach of written contract)"
- **For insurer-side disputes:** Cite **NRS § 686A.310(2)** for the codified private right of action, **plus** common-law bad faith per *Wohlers v. Bartgis*. The combined claim opens damages, attorney's fees (where contractually or statutorily available), and punitive damages under NRS § 42.005.
- **For provider-side disputes (vs. insurer-side):** Cite **NRS Chapter 598 (Deceptive Trade Practices)** and the **NRS § 41.600(2)(e)** private right of action with attorney's fees and costs. Hospital in-house billing departments are reachable as original creditors.
- **For collector-side disputes:** Cite **NRS §§ 649.366-.368** (60-day notification, 5% fee cap, voluntary-payment protections). Demand documentation that the 60-day notice was sent before any collection or credit-reporting action.

## Key Nevada-specific advantages

Worth keeping in mind when triaging a Nevada patient's bills:

1. **§ 686A.310(2) statutory private right of action** — the single biggest Nevada-specific lever. Most states' UCSPA statutes are regulator-only; Nevada's is codified-private. Damages for any enumerated unfair practice without proving common-law bad faith.
2. **Wohlers v. Bartgis common-law bad faith** — punitive damages on top of the statutory claim, well-precedented in a medical-insurance fact pattern. Plead in the alternative.
3. **NDTPA original-creditor reach** — NRS Chapter 598 + NRS § 41.600 private right of action reaches the hospital's in-house billing department, with attorney's fees recoverable. Mention in any 30-day warning to providers.
4. **NRS § 439B.260 automatic 30% uninsured discount** — non-discretionary statutory entitlement at major hospitals (200+ beds). Demand it directly, do not wait for a "financial assistance policy" determination.
5. **60-day medical-debt collection notice (§§ 649.366-.368)** — procedural lever against collectors; verify the notice was properly sent before any collection action, and confirm the 5% fee cap is observed.
6. **Justice Court small-claims economics** — corporations can appear pro se, attorney fees not recoverable by either side, $10,000 cap. The economic asymmetry favors a patient with a clean documentary case.

## Notable Nevada-specific weaknesses

Worth flagging in any case-screening conversation:

1. **No ground-ambulance protection** — AB 469 left this gap and the 2023 fix didn't pass. Federal NSA also excludes ground ambulance. Nevada patients are exposed to balance billing on ground-ambulance bills; the only state-law leverage is NDTPA (deceptive/excessive charges) or quantum challenge.
2. **No standalone medical-debt credit-reporting prohibition** — only the 60-day notification window in § 649.366. AB 204 (2025-2026 session) would change this; verify enactment before relying on it.
3. **ERISA opt-out for self-funded plans (§ 439B.757)** — self-funded employer plans can opt out of Nevada's surprise-billing scheme. Always verify the plan's election before relying on state-law protections; opted-out plans fall back to the federal NSA.
4. **Small claims attorney-fee bar** — NRS § 69.030 / § 69.050 generally preclude attorney-fee recovery in small claims. Cuts both ways economically but reduces fee-shifting leverage in the smallest-dollar disputes.
