# Indiana state pack

The fully-worked state-law layer for Indiana patients. The LLM uses this when the patient's state is Indiana. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Two things make Indiana's patient-side leverage distinctive:

1. **Common-law first-party bad faith is recognized** — Indiana is one of the minority of states whose supreme court adopted a tort cause of action for an insurer's bad-faith refusal to pay a first-party claim, with punitive damages on the table. See *Erie Ins. Co. v. Hickman*, 622 N.E.2d 515 (Ind. 1993).
2. **Strong price-transparency regime** — Indiana's 2020-2021 surprise billing reform (SEA 3 / IC 27-1-46 and IC 25-1-9.8) makes good-faith estimates a **mandatory pre-service deliverable** from both facilities and practitioners, and the 2023 HEA 1004 layered hospital price-benchmarking on top. A patient who was billed materially above the estimate has a direct documentary lever.

A note on user-provided cites:

- **IC 16-21-9 is not the itemized-billing chapter.** It is "Provision of Charitable Care by Nonprofit Hospitals" (community benefits plan and annual reporting). The price-transparency / good-faith estimate provisions live in **IC 27-1-46** (provider facilities) and **IC 25-1-9.8** (practitioners). Itemized statements are not granted by a single Indiana statute the way Georgia's FBPA grants one; the right comes from federal § 501(r), federal CoP for participating hospitals, contract/UDAP theory, and the IDOI complaint process.
- **IC 27-1-37 is not the surprise-billing chapter.** Indiana's balance-billing prohibition is at **IC 27-8-10-3.2** (HMO balance-billing prohibition) plus the IC 25-1-9.8 / IC 27-1-46 consent-and-estimate framework. The ground ambulance protection (HEA 1385, effective Jan 1, 2025) is codified in the IC 27-8 line as well.

Both corrections are reflected in the relevant sections below.

## Hospital itemization right

- **Statute:** Indiana has **no statutory analogue** to Georgia's automatic 6-business-day itemized-billing duty (O.C.G.A. § 10-1-393(b)(14)). The right to an itemized statement in Indiana comes from a layered set of sources rather than a single state code section.
- **Sources of the right:**
  - **Federal — 26 U.S.C. § 501(r)(6)** and **26 C.F.R. § 1.501(r)-6** require non-profit hospitals to bill at the "amounts generally billed" (AGB) cap and to make reasonable efforts to determine FAP eligibility before extraordinary collection actions. Receipt of an itemized statement is part of the practical record patients need to verify AGB compliance.
  - **Federal — 42 C.F.R. § 482.13** (Medicare Conditions of Participation, Patient's Rights) requires hospitals to inform patients of charges. Most Indiana hospitals participate in Medicare and are bound.
  - **Hospital licensure regulations — 410 IAC 15-1.4** (Indiana State Department of Health rules for general hospitals) require hospitals to maintain financial records and provide itemization on request as part of the patient's rights framework.
  - **Indiana Deceptive Consumer Sales Act — IC 24-5-0.5** reaches "unfair, abusive, or deceptive" acts in consumer transactions and is the strongest UDAP-style lever when a hospital refuses or evades itemization (see DCSA section below).
- **Practical posture for the kit:** Send a written, certified-mail request for a CPT/HCPCS-coded itemized statement under "federal price transparency and § 501(r) AGB compliance" authority, plus DCSA § 24-5-0.5-3. A 14- to 30-day response window is reasonable. Non-response is itself a fact the IDOI/AG can act on under DCSA.

## Indiana Deceptive Consumer Sales Act (DCSA)

- **Statute:** **IC 24-5-0.5 et seq.** — enumerated deceptive acts at **§ 24-5-0.5-3**, private remedies and enforcement at **§ 24-5-0.5-4**
- **Source:** [law.justia.com/codes/indiana/title-24/article-5/chapter-0-5/section-24-5-0-5-3](https://law.justia.com/codes/indiana/title-24/article-5/chapter-0-5/section-24-5-0-5-3/); [law.justia.com/codes/indiana/title-24/article-5/chapter-0-5/section-24-5-0-5-4](https://law.justia.com/codes/indiana/title-24/article-5/chapter-0-5/section-24-5-0-5-4/)
- **Substance:** A "supplier" (which includes hospitals and providers as sellers of services) may not commit an "unfair, abusive, or deceptive act, omission, or practice in connection with a consumer transaction." Itemization refusals, "phantom" charges, upcoding, misrepresenting in-network status, and threatening unfounded suit are all squarely within § 24-5-0.5-3's enumerated and catchall provisions.
- **Private right of action:** **Yes.** Section 24-5-0.5-4 allows a consumer to recover **actual damages or $500, whichever is greater**, plus **treble damages (or $1,000, whichever is greater) for willful violations**, plus reasonable attorney's fees. This is Indiana's analogue to Georgia's FBPA § 10-1-399 and is the single strongest patient-side state-law cite for provider-side disputes.
- **Procedural note:** Indiana does **not** require an ante-litem demand letter as a precondition to a DCSA suit (contrast Georgia's 30-day FBPA demand). However, an "offer to cure" framework at § 24-5-0.5-5 lets a supplier limit damages by curing within 30 days of receiving notice — practically, this means the kit's 30-day warning letter both creates the cure-demand record and gives the hospital one last off-ramp before suit.
- **Reach over original creditors:** DCSA applies to suppliers directly, not just third-party debt collectors, so it reaches the hospital's in-house billing department. Mirrors the Georgia FBPA advantage.
- **AG enforcement:** The Indiana Attorney General may also bring an action under § 24-5-0.5-4(c) seeking injunctive relief, civil penalties, restitution, and the costs of investigation. Filing a parallel complaint with the AG (see Regulatory Agencies, below) is part of the kit's standard CC line.

## Unfair Claim Settlement Practices Act (UCSPA)

- **Statute:** **IC 27-4-1-4.5** (enumeration of unfair claim settlement practices); complaint mechanism at **IC 27-4-1-5.6**
- **Source:** [law.justia.com/codes/indiana/title-27/article-4/chapter-1/section-27-4-1-4-5](https://law.justia.com/codes/indiana/title-27/article-4/chapter-1/section-27-4-1-4-5/); [codes.findlaw.com/in/title-27-insurance/in-code-sect-27-4-1-4-5](https://codes.findlaw.com/in/title-27-insurance/in-code-sect-27-4-1-4-5/)
- **Substance:** Prohibits insurers from engaging in a defined list of unfair claims-settlement practices — misrepresenting policy provisions, failing to acknowledge claims promptly, refusing to pay without a reasonable investigation, failing to affirm/deny coverage in a reasonable time, not attempting in good faith to effectuate prompt and fair settlements, etc.
- **Critical caveat — no private right of action under the UCSPA itself:** Indiana courts have repeatedly held that IC 27-4-1-4.5 does not create a private cause of action. Enforcement of the statute is exclusively by the **Indiana Department of Insurance Commissioner**. See, e.g., *Allstate Ins. Co. v. Hammond*, 759 N.E.2d 1162 (Ind. Ct. App. 2001).
- **Why it still matters — the bridge to *Hickman*:** Although the statute itself is non-actionable, Indiana recognizes a separate **common-law tort of first-party bad faith** under *Erie Ins. Co. v. Hickman*. The conduct enumerated in § 27-4-1-4.5 is precisely the conduct that supports a *Hickman* bad-faith claim. Plead the bad-faith tort, **cite UCSPA violations as evidence**, and file a parallel IDOI complaint. This three-track posture is materially stronger than Georgia's, where the UCSPA's no-private-action bar at O.C.G.A. § 33-6-37 plus the absence of a common-law bad-faith tort leaves only the statutory § 33-4-6 remedy.
- **Use in dispute letters:** Cite specific § 27-4-1-4.5 subsections (especially (1), (2), (4), (5), (6)) when the dispute is with an insurer over a denied or underpaid claim; the IDOI complaint mechanism is the operative remedy, and the citation primes the *Hickman* tort claim if litigation follows.

## Bad-faith failure to pay (common-law tort)

- **Source case:** ***Erie Ins. Co. v. Hickman by Smith***, **622 N.E.2d 515 (Ind. 1993)** — Indiana Supreme Court formally recognized a tort cause of action for an insurer's breach of the duty of good faith and fair dealing toward its insured.
- **Source:** [law.justia.com/cases/indiana/supreme-court/1993/29s02-9310-cv-1180-4.html](https://law.justia.com/cases/indiana/supreme-court/1993/29s02-9310-cv-1180-4.html)
- **The duty (per *Hickman*):** The obligation of good faith with respect to the discharge of an insurer's contractual obligation includes obligations to:
  1. Refrain from making an **unfounded refusal** to pay policy proceeds.
  2. Refrain from causing **unfounded delay** in making payment.
  3. Refrain from **deceiving** the insured.
  4. Refrain from **exercising any unfair advantage** to pressure an insured into settlement.
- **Standard:** Mere negligence or a good-faith dispute about coverage is insufficient. The insured must show the insurer's conduct was based on a **dishonest purpose, moral obliquity, furtive design, or ill will** — a high bar, but actionable. The presence of a "rational, principled basis" for denial defeats the claim (as it did in *Hickman* itself on the facts).
- **Damages:**
  - Contract damages (the underlying loss the insurer should have paid).
  - **Consequential damages** flowing from the bad-faith conduct (emotional distress, related economic harm in appropriate cases).
  - **Punitive damages** where the bad faith is shown by clear and convincing evidence. Indiana applies a punitive-damage cap (IC 34-51-3-4) of the greater of three times compensatory damages or $50,000, and 75% of any punitive award goes to the state's Violent Crime Victims Compensation Fund.
  - Attorney's fees are **not** automatically recoverable under *Hickman* (contrast Georgia § 33-4-6's penalty-and-fees structure); fees are recoverable only under separate fee-shifting statutes or contract terms.
- **Coverage scope:** First-party only. Applies to fully insured health policies, accident and sickness, individual/marketplace plans. **ERISA-preempted** as applied to self-funded employer plans — for those, the federal remedy is 29 U.S.C. § 1132(a)(1)(B). Plead carefully and confirm plan funding type before relying on *Hickman*.
- **Procedural posture:** No ante-litem demand requirement. Statute of limitations is the four-year contract limitations period under IC 34-11-2-11 for breach-of-contract claims arising from the same conduct, with tort-claim limitations applied separately to the bad-faith count itself.

## Surprise billing — IC 27-1-46, IC 25-1-9.8, IC 27-8-10-3.2

Indiana addresses surprise billing through three interlocking statutes, all driven by the 2020 SEA 3 reform package and refined by HEA 1004 (2023):

### Good-faith estimate from facilities — IC 27-1-46

- **Statute:** **IC 27-1-46** ("Provider Facility Good Faith Estimates")
- **Source:** [law.justia.com/codes/indiana/title-27/article-1/chapter-46](https://law.justia.com/codes/indiana/title-27/article-1/chapter-46/)
- **Substance:** A provider facility (hospital, ambulatory surgery center, etc.) must, on a patient's request, furnish a written good-faith estimate of charges for a non-emergency service **within five (5) business days**. The estimate must include facility charges, employed/contracted staff charges, supplies and materials, and all practitioner charges; must state it is non-binding; must state actual price may vary based on clinical need; and is valid for thirty (30) days.
- **Communication duty:** Facilities must communicate the right to a GFE through **at least three means** (IC 27-1-46-15) — signage, web, intake materials.
- **No charge:** The facility may not charge for providing the estimate.

### Good-faith estimate from practitioners — IC 25-1-9.8

- **Statute:** **IC 25-1-9.8** ("Health Practitioner Good Faith Estimates")
- **Source:** [law.justia.com/codes/indiana/title-25/article-1/chapter-9-8](https://law.justia.com/codes/indiana/title-25/article-1/chapter-9-8/)
- **Substance:** Practitioners regulated under Title 25 (physicians, dentists, etc.) must provide a written good-faith estimate for non-emergency services at least **five (5) business days** before the scheduled service. Waived only for emergencies or services scheduled within five days of being ordered.

### Balance-billing prohibition — IC 27-8-10-3.2

- **Statute:** **IC 27-8-10-3.2** ("Balance Billing")
- **Source:** [law.justia.com/codes/indiana/title-27/article-8/chapter-10/section-27-8-10-3-2](https://law.justia.com/codes/indiana/title-27/article-8/chapter-10/section-27-8-10-3-2/)
- **Substance:** A provider may not bill an HMO enrollee for amounts in excess of the in-network cost-share for **(a) emergency services** and **(b) non-emergency services rendered by an out-of-network provider at an in-network facility**, unless the patient received advance written disclosure of the OON status and the GFE at least five business days in advance and gave informed written consent. The "consent exception" mirrors the federal No Surprises Act notice-and-consent process at 45 C.F.R. § 149.420.
- **Coverage scope:** State-regulated HMO and accident-and-sickness products. **ERISA-preempted** for self-funded plans (federal NSA applies instead). Excludes Medicare and Medicaid.

### Practical posture

Where a non-emergency bill exceeds a written GFE by a material margin (federal benchmark for the NSA patient-provider dispute process is **$400 or more**), the patient may:

1. Demand correction citing IC 27-1-46 / IC 25-1-9.8 GFE non-compliance.
2. File a complaint with the **IDOI Consumer Services Division** (state-regulated plans).
3. Use the federal **Patient-Provider Dispute Resolution (PPDR)** process for self-pay/uninsured patients under the federal NSA, regardless of ERISA status.

## Regulatory agencies

### Indiana Department of Insurance (IDOI) — Consumer Services Division

- **Online complaint:** [in.gov/idoi/consumer-services/complaints/submit-a-complaint-online](https://www.in.gov/idoi/consumer-services/complaints/submit-a-complaint-online/) (Sircon portal at [gov.sircon.com](https://gov.sircon.com/portalAccess.do?service=consumerPortal))
- **Phone:** Toll-free in Indiana **1-800-622-4461**; outside Indiana **(317) 232-2395**
- **Fax:** (317) 234-2103
- **Mail:**
  > Indiana Department of Insurance
  > Attn: Consumer Services Division
  > 311 W. Washington Street, Suite 300
  > Indianapolis, IN 46204-2787
- **Authority:** Licensed insurers, HMOs, accident-and-sickness policies, Medicare supplement. Administers IC 27-1-46, IC 27-4-1-4.5 (UCSPA), IC 27-8-10-3.2 (balance billing), and HEA 1385 (ground ambulance, effective Jan 1, 2025). **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and does not regulate providers, hospitals, or debt collectors (route to AG).
- **Processing:** IDOI states typical complaint intake within 72 hours.

### Indiana Attorney General — Consumer Protection Division

- **Online complaint:** [in.gov/attorneygeneral/consumer-protection-division/file-a-complaint](https://www.in.gov/attorneygeneral/consumer-protection-division/file-a-complaint/) (direct form at [inoag.my.salesforce-sites.com/ConsumerComplaintForm](https://inoag.my.salesforce-sites.com/ConsumerComplaintForm))
- **Phone:** main **(317) 232-6330**; toll-free **1-800-382-5516**
- **Email:** complaints@indiana.gov
- **Fax:** (317) 233-4393
- **Mail:**
  > Office of the Indiana Attorney General
  > Consumer Protection Division
  > Government Center South, 5th Floor
  > 302 W. Washington Street
  > Indianapolis, IN 46204
- **Authority:** Enforces the **Indiana Deceptive Consumer Sales Act (IC 24-5-0.5)** against suppliers, including hospitals' in-house billing departments, providers, and third-party debt collectors. Reach over **original creditors** — the exact gap not covered by IDOI. Use when the dispute is with the hospital's billing office, not with an insurer's claim decision.

## Small claims court

- **Court name:** **Small Claims Docket** of the Circuit Court, Superior Court, or (in Marion County) the township-level Small Claims Court.
- **Jurisdictional limit:** **$10,000**
  - Superior court small claims docket: **IC 33-29-2-4**
  - Circuit court small claims docket: **IC 33-28-3-4**
  - Marion County township small claims courts: **IC 33-34-3-2**
- **Source:** [law.justia.com/codes/indiana/title-33/article-29/chapter-2/section-33-29-2-4](https://law.justia.com/codes/indiana/title-33/article-29/chapter-2/section-33-29-2-4/); Indiana Small Claims Rules at [rules.incourts.gov/Content/small-claims](https://rules.incourts.gov/Content/small-claims/default.htm); manual at [in.gov/courts/publications/small-claims-manual](https://www.in.gov/courts/publications/small-claims-manual/)
- **Filing fees:** Indiana Small Claims service fee is **$10 per named defendant** under IC 33-37-4-6, on top of the base civil filing fee (varies by county, typically **$75-$95**). Full schedule in the Indiana Trial Court Fee Manual at [in.gov/courts/iocs/files/courtmgmt-pubs-trial-court-fee-manual.pdf](https://www.in.gov/courts/iocs/files/courtmgmt-pubs-trial-court-fee-manual.pdf).
- **Attorney rules:** Permitted, not required. Designed for pro se litigants — simplified pleadings, limited formal discovery. **Important Indiana wrinkle:** Indiana Small Claims Rule 8(C) requires a **corporation, partnership, or LLC defendant** to appear through an attorney **unless the claim is $1,500 or less**, in which case a non-attorney officer/employee may appear. This is **less favorable** than Georgia's Magistrate Court rule (which allows non-attorney corporate appearance at any amount); a hospital defendant in Indiana small claims above $1,500 will usually appear with counsel, which raises the corporate side's defense cost and creates settlement leverage but reduces the prospect of facing a billing-clerk pro se.
- **Jury trial:** Not available on the small claims docket. Either party may demand a transfer to the plenary docket (with jury rights) under Indiana Small Claims Rule 8(B), typically within the time set by local rule.

## Statute of limitations

- **Written contracts for the payment of money** (most signed hospital financial-responsibility forms): **6 years** — **IC 34-11-2-9**
  - Source: [law.justia.com/codes/indiana/title-34/article-11/chapter-2/section-34-11-2-9](https://law.justia.com/codes/indiana/title-34/article-11/chapter-2/section-34-11-2-9/)
- **Written contracts other than for the payment of money:** **10 years** — IC 34-11-2-11
- **Oral contracts and accounts (not in writing):** **6 years** — **IC 34-11-2-7**
- **Source (IC 34-11 chapter PDF):** [iga.in.gov/static-documents/5/9/6/c/596ceef4/TITLE34_AR11_ch2.pdf](https://iga.in.gov/static-documents/5/9/6/c/596ceef4/TITLE34_AR11_ch2.pdf)

Most hospital admissions involve a signed financial-responsibility form — a written contract for the payment of money, so **6 years under IC 34-11-2-9** applies. Implied-in-fact medical-billing arrangements without a signed agreement fall under accounts/oral-contract treatment at IC 34-11-2-7 (also 6 years), so Indiana's framework is **uniform at 6 years** for both written and oral contract theories on medical debt — simpler than Georgia's split (6 written / 4 oral).

**Be aware of the *Smither v. Asset Acceptance* line:** Indiana courts have at times applied a different 6-year clock to "closed installment contracts," with the limitations clock starting on the last installment due rather than the first default. The Indiana Supreme Court has more recently harmonized this; do not assume the clock has run on a partially-paid medical debt without checking the most recent payment date.

Partial payment or **written acknowledgment of the debt restarts the clock** under common-law principles applied in Indiana. **Do not make a partial payment on a time-barred medical debt without legal advice** — it can revive the limitations period entirely.

## Ground ambulance balance-billing

- **Statute:** **HEA 1385 (2024)**, amending IC 27-8 and related insurance code — effective **January 1, 2025**
- **Source:** Bill page at [iga.in.gov/legislative/2024/bills/house/1385](https://iga.in.gov/legislative/2024/bills/house/1385); summary at [indianahouserepublicans.com/news/press-releases/barrett-new-law-will-aim-to-shield-patients-from-surprise-ambulance-bills](https://www.indianahouserepublicans.com/news/press-releases/barrett-new-law-will-aim-to-shield-patients-from-surprise-ambulance-bills/); state implementation notes at [in.gov/healthcarereform/no-surprises-act](https://www.in.gov/healthcarereform/no-surprises-act/)
- **Substance:** For policies issued or renewed on or after January 1, 2025, an insured patient transported by an out-of-network ground ambulance provider may be charged **no more than the in-network cost-share** (copay/coinsurance/deductible). The health plan must pay the OON ambulance provider the **lesser of**:
  1. The rate set or approved by the county or municipality where the service originated, or
  2. **400% of the published Medicare rate** for the same service in the same geographic area, or
  3. The ambulance provider's billed charges.
- **Payment-in-full rule:** That payment is deemed payment in full; the provider **may not balance-bill the patient** for any additional amount.
- **Payment timeline:** Plans must pay within 30 days of a clean claim.
- **Why this matters:** Federal No Surprises Act **excludes ground ambulance** — Indiana joined a growing minority of states (Georgia via HB 286, Ohio, Maine, etc.) that close the gap at the state level. For ground-ambulance bills dated **on or after January 1, 2025** for state-regulated plans, this is the single highest-leverage Indiana-specific cite.
- **Caveats:**
  - **ERISA preemption** — the Act does not reach self-funded employer plans. Those are still subject to the federal NSA's exclusion of ground ambulance, meaning no balance-billing protection. Check plan funding type before relying on HEA 1385.
  - Excludes **air ambulance** (federal NSA covers air ambulance), workers' compensation, Medicare, Medicaid.
  - Pre-January-1-2025 dates of service are **not retroactively covered**.

## Credit reporting

Indiana has **not yet enacted** a comprehensive state ban on medical-debt credit reporting comparable to Colorado's or New York's. As of 2026-05-18, Indiana patients rely on:

- **Voluntary credit bureau policy changes** (2022-2023): paid medical debt removed; debt under $500 not reported; one-year delay before reporting unpaid medical debt.
- **Federal FCRA dispute rights** (15 U.S.C. §§ 1681i, 1681s-2) against furnishers and bureaus.
- **DCSA (IC 24-5-0.5)** as a state UDAP overlay where furnishing inaccurate medical-debt information to bureaus is shown to be deceptive.

**Watch list:** HB 1051 (Indiana 2024-2025 session) and similar proposals would prohibit health care providers from reporting medical debt to consumer reporting agencies. Tracking and not yet enacted as of this writing — re-verify status before relying on a state-law cite.

**Federal preemption posture is in flux.** The CFPB issued an October 2025 interpretive rule taking the position that the FCRA preempts state laws restricting medical-debt credit reporting. If sustained, it limits the effect of any Indiana state-level law that subsequently passes.

## Hospital charity care

- **Statute:** **IC 16-21-9** — "Provision of Charitable Care by Nonprofit Hospitals" (community benefits plan and annual reporting, **not** an FAP mandate)
- **Source:** [law.justia.com/codes/indiana/title-16/article-21/chapter-9](https://law.justia.com/codes/indiana/title-16/article-21/chapter-9/)
- **Substance:** Each non-profit Indiana hospital must adopt a mission statement identifying its commitment to community health needs, adopt and publish a **community benefits plan** (charity care, government-sponsored indigent care, education, donations, research, subsidized health services), and file an **annual community benefits report** with the Indiana State Department of Health. Civil penalty up to **$1,000 per day** for delinquent reports under § 16-21-9-8.
- **What IC 16-21-9 does *not* do:** It does not create a hospital-specific FAP mandate or an income-tier discount schedule. The substantive FAP floor for Indiana non-profit hospitals is **federal § 501(r)** (26 U.S.C. § 501(r)(4)-(6) and 26 C.F.R. § 1.501(r)-4 through -6): widely-publicized FAP, AGB caps, prohibition on extraordinary collection actions before FAP eligibility determination.
- **2026 update — IC 16-21-9.5 (effective July 1, 2026):** HB 1271 (2026 session) added **IC 16-21-9.5** requiring hospitals to disclose payment-assistance programs, post signs in specified locations, surface programs in the patient portal, and make reasonable efforts to notify individuals before collection actions begin. This is the closest Indiana has come to a state-law FAP-notice mandate. Re-verify enactment date and final text before citing.
- **For-profit and county/municipal hospitals:** No state FAP mandate. Federal § 501(r) does not apply to for-profits. Lean on DCSA-deception theories and on the hospital's own posted FAP if one exists.
- **Use Dollar For** at [dollarfor.org/state_sheet/indiana](https://dollarfor.org/state_sheet/indiana/) for screening.

## Hospital lien statute

- **Citations:** **IC 32-33-4-1 through 32-33-4-9** — "Hospital Liens"
- **Sources:** [law.justia.com/codes/indiana/title-32/article-33/chapter-4](https://law.justia.com/codes/indiana/title-32/article-33/chapter-4/); perfection procedure at [law.justia.com/codes/indiana/title-32/article-33/chapter-4/section-32-33-4-4](https://law.justia.com/codes/indiana/title-32/article-33/chapter-4/section-32-33-4-4/)
- **Substance:** Hospitals (and emergency ambulance services provided by the hospital) may file a lien for reasonable and necessary charges, **only against the patient's cause of action against a third party** who caused the injury. **Not a lien on the patient's home, wages, or bank accounts.**
- **Perfection requirements:**
  - File a verified statement in the office of the recorder of the county where the hospital is located within **90 days after discharge** OR before final settlement/compromise/resolution of the patient's cause of action, whichever occurs first.
  - The verified statement must include patient name and address, hospital name and address, dates of admission and discharge, amount claimed due, and the names and addresses of any liable third parties.
  - Within **10 days of filing**, the hospital must send a copy by registered mail to each party claimed to be liable, the patient's attorney (if known), and the **Indiana Department of Insurance**.
- **What to check on a presented lien:** Verify (1) the timeliness of the 90-day filing, (2) recorder-of-deeds filing in the correct county, (3) the 10-day registered-mail notice to all listed parties including IDOI, and (4) that the charges reflected on the lien match the hospital's federal § 501(r) AGB-capped amounts (not chargemaster gross charges). A defective lien is unenforceable.
- **Releases and partial settlements:** § 32-33-4-7 requires the lienholder to execute a release once paid; failure exposes the hospital to liability to the patient and to subsequent good-faith purchasers/settlement payors.

## Price transparency — HEA 1004 (2023)

- **Statutes:** **HEA 1004 (2023)** added IC 16-21-18 (nonprofit hospital pricing reporting) and amended IC 27-1 and IC 25-1 GFE provisions to tighten communication duties. The 2023 bill is **distinct from** the 2025 HB 1004 (a separate measure introducing a hospital facility-fee excise tax for charges above 265% of Medicare).
- **Sources:**
  - Enrolled HEA 1004 (2023) PDF: [legiscan.com/IN/text/HB1004/id/2794295/Indiana-2023-HB1004-Enrolled.pdf](https://legiscan.com/IN/text/HB1004/id/2794295/Indiana-2023-HB1004-Enrolled.pdf)
  - Bill page: [iga.in.gov/legislative/2023/bills/house/1004](https://iga.in.gov/legislative/2023/bills/house/1004)
  - IDOI hospital price benchmarking report (2024): [iga.in.gov/publications/agency_report/2024%20Annual%20Report%20-%20Hospital%20Price%20Benchmarking%20Medicare%20Repricing%20Report.pdf](https://iga.in.gov/publications/agency_report/2024%20Annual%20Report%20-%20Hospital%20Price%20Benchmarking%20Medicare%20Repricing%20Report.pdf)
  - Commercial summary: [mdclarity.com/blog/indiana-price-transparency-laws-house-bills-1004-1447](https://www.mdclarity.com/blog/indiana-price-transparency-laws-house-bills-1004-1447)
- **Substance — three layers:**
  1. **Hospital price benchmarking (IC 16-21-18):** Requires IDOI to contract for an annual report comparing nonprofit hospital prices to **285% of Medicare** for the commercially insured market. The first benchmarking report was published in 2024 and is publicly available — useful documentary support for any patient bill that materially exceeds the benchmarked range.
  2. **Strengthened GFE communication duties (IC 27-1-46-15):** Provider facilities must communicate the right to a good-faith estimate through **at least three** distinct means (signage, website, intake materials).
  3. **Federal alignment:** Reinforces compliance with **45 C.F.R. § 180** (federal hospital price transparency rule — machine-readable file of standard charges and a consumer-friendly shoppable services tool).
- **Practical leverage:** Where a bill materially exceeds (a) the patient's written GFE, (b) the hospital's machine-readable file rate for the same CPT/HCPCS codes, or (c) the IDOI-benchmarked 285% Medicare ceiling for the same DRG family, the kit should cite all three transparency layers plus DCSA § 24-5-0.5-3 in the dispute letter.

## Wage garnishment

- **Statute:** **IC 24-4.5-5-105** (consumer-credit wage-garnishment limits, tracks the federal Consumer Credit Protection Act, 15 U.S.C. § 1673)
- **Source:** [law.justia.com/codes/indiana/title-24/article-4-5/chapter-5/section-24-4-5-5-105](https://law.justia.com/codes/indiana/title-24/article-4-5/chapter-5/section-24-4-5-5-105/)
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a **court judgment**. Post-judgment, garnishment is capped at the federal lesser of (i) 25% of disposable earnings or (ii) the amount by which weekly disposable earnings exceed 30× the federal minimum wage.
- **Use:** In response letters to collectors threatening garnishment without a judgment in hand.

## Quick reference for letter rendering

When the LLM renders an Indiana-bound letter, substitute these defaults:

- **State statute (provider-side primary lever):** **IC 24-5-0.5-3 (Deceptive Consumer Sales Act)** plus **IC 24-5-0.5-4** for the private right of action with treble damages and attorney's fees. This is Indiana's analogue to Georgia's FBPA and the strongest patient-side cite against hospitals for itemization refusals, deceptive billing, and unfounded collection conduct.
- **State statute (insurer-side primary lever):** **IC 27-4-1-4.5 (UCSPA, cited for IDOI complaint)** plus a *Hickman* common-law bad-faith count in any litigation. The UCSPA itself is non-actionable, but its enumeration drives the *Hickman* tort.
- **State statute (GFE non-compliance):** **IC 27-1-46** (facility) and **IC 25-1-9.8** (practitioner) for missing or materially-exceeded good-faith estimates.
- **State statute (balance-billing prohibition):** **IC 27-8-10-3.2** for HMO emergency and OON-at-INN scenarios.
- **State insurance department (CC line):** Indiana Department of Insurance, Consumer Services Division, 311 W. Washington Street, Suite 300, Indianapolis, IN 46204-2787
- **State AG consumer protection (CC line):** Office of the Indiana Attorney General, Consumer Protection Division, Government Center South, 5th Floor, 302 W. Washington Street, Indianapolis, IN 46204
- **Small-claims court name:** **Small Claims Docket of the [Circuit/Superior] Court of [County]** (Marion County: **[Township] Small Claims Court**)
- **Filing fee (in 30-day warning):** "approximately $85-$105 depending on county"
- **Statute of limitations (in 30-day warning):** "IC 34-11-2-9 (six years for written contracts for the payment of money)"
- **For ground-ambulance balance bills dated on or after Jan 1, 2025:** Cite **HEA 1385 (2024)** as amending IC 27-8. This is the highest-leverage Indiana-specific cite when applicable.
- **For provider-side disputes (vs. insurer-side):** Cite **IC 24-5-0.5-3 and -4 (DCSA private right of action with treble damages and attorney's fees)** in addition to UCC § 2-305. The DCSA "offer to cure" framework at § 24-5-0.5-5 means the 30-day warning letter doubles as the cure-demand record.

## Key Indiana-specific advantages

Worth keeping in mind when triaging an Indiana patient's bills:

1. **Common-law bad-faith tort (*Hickman*)** — Indiana is one of the minority of states with a judicially-recognized first-party bad-faith tort, putting punitive damages and consequential damages on the table beyond contract recovery. Materially stronger than Georgia's purely statutory § 33-4-6 framework for the right facts.
2. **DCSA private right of action with treble damages and fees** — IC 24-5-0.5-4 provides the same kind of fee-shifting and multiplier remedy as Georgia's FBPA, reaching the hospital directly (not just third-party collectors).
3. **Strong GFE regime (IC 27-1-46 and IC 25-1-9.8)** — written, pre-service, mandatory good-faith estimates with three-channel communication duty. A bill materially above a written GFE is documentary gold.
4. **Ground ambulance closed as of Jan 1, 2025 (HEA 1385)** — Indiana is in the minority of states that fixed the federal NSA's biggest gap. Check whether a ground-ambulance bill post-dates the effective date and whether the plan is state-regulated.
5. **Uniform 6-year SOL** — Both written (IC 34-11-2-9) and oral (IC 34-11-2-7) limitations are 6 years for medical debt, simplifying the SOL analysis compared to Georgia's 6/4 split.

## Indiana-specific weaknesses to flag

1. **No automatic itemized-statement duty** — Indiana has no analogue to Georgia's automatic 6-business-day itemization right under O.C.G.A. § 10-1-393(b)(14). The patient must request the itemization in writing, and the leverage comes from layered federal § 501(r), Medicare CoP, and DCSA-deception theories rather than a single bright-line statute.
2. **UCSPA is non-actionable** — IC 27-4-1-4.5 cannot be pled as a standalone count. The *Hickman* tort is the route, with a high "dishonest purpose/moral obliquity" standard.
3. **Small claims corporate-appearance rule** — Indiana Small Claims Rule 8(C) requires corporate defendants above $1,500 to appear with counsel, reducing the "billing-clerk pro se" leverage that Georgia patients enjoy. Above $1,500, expect a defense attorney across the table.
4. **No state credit-reporting restriction yet** — Indiana relies on FCRA and voluntary bureau changes; no codified state ban on medical-debt furnishing as of this writing.
