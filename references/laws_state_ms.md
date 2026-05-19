# Mississippi state pack

The fully-worked state-law layer for Mississippi patients. The LLM uses this when the patient's state is Mississippi. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md); neighboring Alabama at [`laws_state_al.md`](laws_state_al.md). All citations verified against public sources as of 2026-05-19. Re-verify annually.

Three things shape Mississippi's patient-side leverage, and one of them is unusually strong:

1. **Mississippi has a state balance-billing statute** at **Miss. Code Ann. § 83-9-5(1)(i)** that, when the insured assigns benefits to the provider in writing, deems the insurer's direct payment as payment in full — the provider is statutorily barred from collecting any amount above that payment (other than copay/coinsurance/deductible). This is materially stronger than Alabama's posture (no state surprise-billing law at all) and pre-dates the federal No Surprises Act by nearly a decade.
2. **Mississippi recognizes a common-law first-party insurance bad-faith tort** with punitive damages, adopted in **Standard Life Ins. Co. of Indiana v. Veal, 354 So. 2d 239 (Miss. 1977)** and refined through *Murphree v. Federal Ins. Co.*, 707 So. 2d 523 (Miss. 1997) and a long line of subsequent decisions. The "no arguable basis" test is plaintiff-strict on liability but the punitive ceiling is meaningful when crossed.
3. **Mississippi recently enacted ground-ambulance reimbursement protection** via **HB 1489 (2024 Regular Session)**, effective July 1, 2024 — the "Mississippi Triage, Treat and Transport to Alternative Destination Act." The minimum reimbursement is the greater of locally-contracted rate or **325% of Medicare**, with the patient held harmless beyond cost-share. The law is under active federal-court challenge by the Mississippi Association of Health Plans (3:24-cv-00379, S.D. Miss.) but remains in force as of this writing.

The structural weaknesses to flag in any MS triage:

- **No standalone hospital-itemization statute.** Miss. Code § 41-9-65 governs hospital-record access ("good cause shown") but does not specifically mandate itemized bills; § 41-10-5 (effective 7/1/2022) requires delivery of medical AND billing records within 30 days of a written request, which is the closest direct lever. Federal § 501(r) and 45 CFR Part 180 are the substantive floor.
- **No general hospital-lien statute.** Mississippi repealed its general hospital lien in 1989; only a narrow burn-care lien (§ 85-7-301 et seq.) remains, and it attaches only to third-party causes of action, not to the patient's home or wages.
- **No state medical-debt credit-reporting law.** Federal FCRA and the 2022-2023 voluntary CRA changes are the only floor.

## Hospital itemization right

- **Primary statute (records + billing, effective 7/1/2022):** **Miss. Code Ann. § 41-10-5** — Health care providers must provide medical records **and billing records** in their possession to the patient (or representative) within **30 days** of a valid written request. Enacted by Laws, 2022, ch. 435, SB 2725, § 1.
- **Secondary statute (record access, older):** **Miss. Code Ann. § 41-9-65** — Hospital records remain hospital property, subject to reasonable access by the patient, personal representative, heirs, attending personnel, and authorized nominees upon **"good cause shown"** and payment of reasonable charges. Pre-dates § 41-10-5 and is the older general-access rule for the hospital-record category specifically.
- **Source:** § 41-10-5 at [codes.findlaw.com/ms/title-41-public-health/ms-code-sect-41-10-5](https://codes.findlaw.com/ms/title-41-public-health/ms-code-sect-41-10-5/); § 41-9-65 background at [law.justia.com/codes/mississippi/title-41/chapter-9](https://law.justia.com/codes/mississippi/title-41/chapter-9/); Mississippi Bar consumer summary at [msbar.org/for-the-public/consumer-information/a-patients-right-to-information](https://www.msbar.org/for-the-public/consumer-information/a-patients-right-to-information/)
- **What an MS patient should do:**
  - Send a written request under **§ 41-10-5** for "all medical records and billing records, including itemized statements of charges, in your possession or custody" by certified mail. The 30-day clock starts on receipt of the valid request.
  - If the provider returns a summary or balance-only statement rather than a true itemized charge-line list (rev codes / CPT / HCPCS / NDC where applicable), document the deficiency and treat it as non-compliance with § 41-10-5's "billing records" duty.
  - For hospital-record-specific requests, anchor a parallel demand on **§ 41-9-65**'s "reasonable access … upon good cause shown" standard; the existence of a disputed bill is itself good cause.
- **Enforcement:** There is **no express private right of action** under § 41-10-5 itself. Practical lever is (a) administrative complaint to the Mississippi State Department of Health (hospital licensure), or (b) a separate cause of action under the **Mississippi Consumer Protection Act (§ 75-24-5)** if non-compliance is part of a deceptive billing practice, with the procedural requirements noted in the MCPA section below.
- **ERISA:** Not preempted — regulates the provider, not the plan.

## Mississippi Consumer Protection Act (private right of action)

- **Statutes:** **Miss. Code Ann. §§ 75-24-1 through 75-24-29** — short title "Mississippi Consumer Protection Act" (MCPA). Listed unlawful practices at **§ 75-24-5**; AG enforcement at **§ 75-24-9**; **private right of action at § 75-24-15**.
- **Source:** [law.justia.com/codes/mississippi/title-75/chapter-24/general-provisions/section-75-24-15](https://law.justia.com/codes/mississippi/title-75/chapter-24/general-provisions/section-75-24-15/); chapter index at [law.justia.com/codes/mississippi/title-75/chapter-24](https://law.justia.com/codes/mississippi/title-75/chapter-24/); practitioner overview at [maronmarvel.com/from-safety-to-subpoenas-a-quick-guide-to-the-mississippi-consumer-protection-act](https://www.maronmarvel.com/from-safety-to-subpoenas-a-quick-guide-to-the-mississippi-consumer-protection-act/)
- **Substance of § 75-24-15:** A consumer who purchases or leases goods or services primarily for personal, family, or household purposes and suffers any ascertainable loss of money or property as a result of a § 75-24-5 unfair-or-deceptive practice may bring an action to recover the loss or assert it as a setoff/counterclaim.
- **Critical procedural prerequisite — informal dispute settlement:** The plaintiff must **first** make a reasonable attempt to resolve the claim through an **informal dispute settlement program approved by the Attorney General**. Failure to plead and prove this step is a common dismissal vector. The standard kit's 30-day demand letter, sent certified with a specific dollar demand, is the patient's record-building tool for this prerequisite — pair it with a request to engage in informal dispute resolution.
- **Class actions prohibited:** Every private action must be maintained in the name of and for the sole use and benefit of the individual person — **no class actions are permitted under MCPA**. This is a structural limit on aggregation.
- **Attorney's fees, one-way against the plaintiff:** Section 75-24-15 permits the **prevailing defendant** to recover attorney's fees and costs if the court finds the action was frivolous or filed for harassment/delay. A prevailing **plaintiff** is **not** entitled to fee recovery under § 75-24-15 itself — this is the principal structural difference from Georgia's FBPA § 10-1-399 or Alabama's ADTPA § 8-19-10. Frame the cost-benefit accordingly before filing.
- **Punitive damages:** Available under MCPA in appropriate cases, but subject to Mississippi's general punitive-damages statute (Miss. Code § 11-1-65), which requires a separate evidentiary phase and applies caps based on defendant net worth.
- **Scope, original creditors:** MCPA reaches sellers of goods and services in trade or commerce. Application to a hospital's in-house billing department is supported where billing conduct is itself deceptive (misrepresenting amounts owed, charging for services not rendered, asserting collectability on a time-barred or otherwise invalid debt).
- **Use:** This is the patient's principal private-action lever against deceptive billing practices in Mississippi, parallel to Alabama's ADTPA. Lean on it in any 30-day warning letter to an MS provider, but recognize the asymmetric fee-shifting and the AG informal-dispute prerequisite.

## Insurance Trade Practices Act

- **Statutes:** **Miss. Code Ann. §§ 83-5-29 through 83-5-51** — Insurance Trade Practices Law. Purpose declaration at § 83-5-29; general prohibition at § 83-5-33; specific unfair practices defined at § 83-5-35 (including unfair claims-settlement practices).
- **Source:** § 83-5-29 at [codes.findlaw.com/ms/title-83-insurance/ms-code-sect-83-5-29](https://codes.findlaw.com/ms/title-83-insurance/ms-code-sect-83-5-29/); § 83-5-35 at [codes.findlaw.com/ms/title-83-insurance/ms-code-sect-83-5-35](https://codes.findlaw.com/ms/title-83-insurance/ms-code-sect-83-5-35/); regulations at [mid.ms.gov/mississippi-insurance-department/legal/regulations](https://www.mid.ms.gov/mississippi-insurance-department/legal/regulations/)
- **Substance:** Defines and prohibits unfair methods of competition and unfair or deceptive acts in the business of insurance — misrepresentation, false advertising, defamation, boycott/coercion, false statements, unfair claims-settlement practices. Modeled on the NAIC Unfair Trade Practices Model Act.
- **Critical caveat, no private right of action:** Mississippi appellate authority treats Chapter 5, Article 1 (the Trade Practices Law) as **regulatory only**. Enforcement is by the **Mississippi Commissioner of Insurance**, not by private litigants. Mississippi has **no statutory "unfair claims practices" private cause of action** equivalent to those in some other states. Practitioners describe Mississippi as a state where the regulatory framework exists but the private remedy lives in **common-law bad faith** (next section), not in the Trade Practices statute itself.
- **Use:** Cite specific § 83-5-35 violations in your complaint to the Mississippi Insurance Department (below). Use the same violations as evidentiary support — not as standalone counts — in a common-law bad-faith claim. Do not plead Chapter 83-5 as a freestanding count.

## Common-law first-party insurance bad faith

- **Leading case:** **Standard Life Ins. Co. of Indiana v. Veal, 354 So. 2d 239 (Miss. 1977)** — the Mississippi Supreme Court first recognized extra-contractual and punitive damages where an insurer "arbitrarily" refuses to pay a legitimate claim. The Veal jury awarded $1,008 in actual damages plus $25,000 in punitive damages on a decreasing-term life policy, and the Supreme Court affirmed the extra-contractual theory.
- **Refining cases:** *Murphree v. Federal Ins. Co.*, 707 So. 2d 523 (Miss. 1997) — clarified that even if the insurer lacks a reasonable basis for denial, punitive damages are recoverable only on the additional showing of "malice, gross negligence, or reckless disregard for the rights of the insured." Subsequent Mississippi Supreme Court and Fifth Circuit decisions (applying Mississippi law) have reaffirmed the two-prong structure.
- **Source:** Veal background at [case-law.vlex.com/vid/standard-life-ins-co-894402218](https://case-law.vlex.com/vid/standard-life-ins-co-894402218); Mississippi bad-faith practitioner summaries at [chartwelllaw.com/bad-faith-claims-map/mississippi](https://www.chartwelllaw.com/bad-faith-claims-map/mississippi) and [holcombgroup.com/mississippi-insurance-law-part-2](https://holcombgroup.com/mississippi-insurance-law-part-2/)
- **User-prompt correction:** The prompt referenced *Tighe v. Crosthwait* (Miss. 1995) as the seminal MS bad-faith case. That citation does not match — *Tighe v. Crosthwait* (1995) is a **medical-malpractice** voir-dire decision concerning juror exposure to tort-reform media, not a first-party bad-faith case. The seminal Mississippi first-party bad-faith authority is **Standard Life v. Veal (Miss. 1977)**, and that is the cite used here.
- **Elements (the Veal/Murphree test for punitive damages):**
  1. an insurance contract between the parties and a breach by the insurer;
  2. the insurer lacked an arguable or legitimate basis for denying the claim;
  3. the insurer acted with willful or malicious wrong, or gross and reckless disregard for the insured's rights.
- **The "arguable basis" rule:** If the insurer has any reasonably arguable basis for denying the claim, there is **no bad faith as a matter of law** and punitive damages are unavailable. This is a high bar — Mississippi is plaintiff-friendly on the punitive ceiling but plaintiff-strict on getting past directed verdict.
- **Damages:**
  - **Actual damages:** the policy benefit owed, plus consequential extra-contractual damages caused by the wrongful denial (including emotional distress in appropriate cases, and attorney's fees as a measure of damages — a Mississippi-specific feature distinct from a statutory fee-shift).
  - **Punitive damages:** available, subject to **Miss. Code § 11-1-65** (the general punitive cap), which scales by defendant net worth: $20 million for >$1 billion net worth down to 2% of net worth for ≤$50 million. Bifurcated trial required.
- **Demand mechanics:** No statutory pre-suit demand letter requirement. Send one anyway — a clear, written, certified demand identifying the policy, the claim, the amount owed, and a payment deadline strengthens the record on the "no arguable basis" element and helps anchor the punitive case.
- **ERISA preemption:** Common-law bad faith is **preempted** as applied to self-funded ERISA employer plans. *Pilot Life Ins. Co. v. Dedeaux*, 481 U.S. 41 (1987) — itself a Mississippi case — federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) fees, no state bad-faith tort. The doctrine is in play for fully-insured plans, Medicaid managed care, and individual/marketplace plans.

## Balance billing — Miss. Code § 83-9-5(1)(i)

- **Statute:** **Miss. Code Ann. § 83-9-5(1)(i)** (originally enacted 2013; enforcement powers expanded 2019).
- **Source:** [codes.findlaw.com/ms/title-83-insurance/ms-code-sect-83-9-5](https://codes.findlaw.com/ms/title-83-insurance/ms-code-sect-83-9-5.html); MID consumer overview at [midhelps.org/insurance-guide/balance-billing](https://www.midhelps.org/insurance-guide/balance-billing/); MID balance-billing FAQ at [mid.ms.gov/healthcare/questionsanswers/TopicTwo.pdf](https://www.mid.ms.gov/healthcare/questionsanswers/TopicTwo.pdf)
- **What it requires:** If the insured provides the insurer with **written direction** that all or any portion of policy indemnities or benefits be paid directly to a licensed health-care provider, the insurer **shall pay the provider directly**, and **that payment is considered payment in full**. The provider **may not bill or collect from the insured any amount above that payment**, other than the deductible, coinsurance, copayment, or charges for equipment/services requested by the insured that are non-covered benefits.
- **Mechanics, what the patient must do:**
  - Execute a written assignment of benefits (AOB) directing the carrier to pay the provider directly. Many hospital intake packets already include an AOB clause — the patient should keep a copy.
  - Provide written notice of the AOB to the insurer (the carrier's claims department address).
  - Once the AOB is in place and the carrier pays, the provider is **statutorily barred** from balance-billing for the difference between billed charges and the AOB payment.
- **Enforcement:** Disputes between provider and insured under § 83-9-5 may be resolved by the **Commissioner of Insurance**. The 2019 amendment expanded the Commissioner's enforcement authority. **File a complaint with the Mississippi Insurance Department Consumer Services Division** when a provider balance-bills after an AOB-routed payment has been made.
- **Federal partnership:** The MID has a **Collaborative Enforcement Agreement with CMS** for federal No Surprises Act compliance, layered on top of § 83-9-5. The state mechanism and the federal NSA mechanism cover overlapping but not identical fact patterns; use both where available.
- **Scope / caveats:**
  - **Requires written AOB.** Without one, § 83-9-5(1)(i) does not bar balance billing. This is the structural difference from NSA-style rules that hold the patient harmless regardless of AOB status.
  - **Dentists excluded** by the terms of § 83-9-5(1)(i).
  - **ERISA preemption:** State balance-billing rule does **not reach self-funded ERISA employer plans** — those plans are covered (if at all) only by the federal NSA. About 60% of insured Mississippians have employer-sponsored coverage and a substantial portion of that is self-funded.
  - **No express private right of action** under § 83-9-5 itself for damages; the route is MID complaint or use the violation as a deceptive-practice predicate under the MCPA.
- **Use:** This is the **single highest-leverage MS-specific cite** for any balance-billing dispute where the patient has fully-insured state-regulated coverage and assigned benefits. Lead with it in dispute letters.

## Ground ambulance reimbursement — HB 1489 (2024)

- **Statute:** **Miss. Code Ann. § 83-9-353** (and related sections; codified in Title 83, Chapter 9, by **HB 1489, 2024 Regular Session** — the "Mississippi Triage, Treat and Transport to Alternative Destination Act"). Signed by Governor Reeves May 2, 2024; **effective July 1, 2024**.
- **Source:** Bill text (as sent to Governor) at [billstatus.ls.state.ms.us/documents/2024/html/HB/1400-1499/HB1489SG.htm](https://billstatus.ls.state.ms.us/documents/2024/html/HB/1400-1499/HB1489SG.htm); LegiScan mirror at [legiscan.com/MS/text/HB1489/id/2934012](https://legiscan.com/MS/text/HB1489/id/2934012); MID 2024 Legislative Summary at [mid.ms.gov/wp-content/uploads/2024/06/2024_Legislative_Summary.pdf](https://www.mid.ms.gov/wp-content/uploads/2024/06/2024_Legislative_Summary.pdf); news coverage at [wdam.com/2024/07/26/new-law-expected-be-boon-patients-ambulance-services-mississippi](https://www.wdam.com/2024/07/26/new-law-expected-be-boon-patients-ambulance-services-mississippi/)
- **What it requires:**
  - The **minimum allowable reimbursement** by any policy of accident-and-sickness insurance to a ground-ambulance service provider is the **greater of**:
    1. the rate contracted between the provider and a county, municipality, or special-purpose district, **or**
    2. **325% of the Medicare reimbursement rate** for services originating in rural areas.
  - If billed charges are less than that minimum, the minimum is the provider's billed charges.
  - The insurer's payment is **payment in full** for covered services, except for cost-share (copay, coinsurance, deductible).
  - Coverage extends to **assess-and-treat-in-place, triage, alternative-destination transport** (e.g., to FQHCs or urgent care), and encounters that do not result in transport — services historically not reimbursed.
- **Patient-side effect:** A state-regulated insured cannot be balance-billed beyond cost-share for in-scope ambulance services post-July 1, 2024. This is the **single biggest patient-side gain in the 2024 session** and a meaningful close of the federal NSA's ground-ambulance gap for state-regulated coverage.
- **Pending federal challenge:** **Mississippi Association of Health Plans v. Chaney**, Cause No. 3:24-cv-00379-HTW-LGI (S.D. Miss., filed 2024) — MAHP filed a constitutional challenge arguing the Act is impermissibly vague (14th Amendment) and exceeds state authority over interstate commerce. Mississippi Ambulance Alliance filed an amicus brief defending the statute. **Track the litigation** before relying on HB 1489 in 2026+ disputes; the Act is in force as of this writing.
- **Caveats:**
  - **ERISA-preempted self-funded plans** are outside the Act's reach (same gap as § 83-9-5 generally and as the federal NSA's group-health framework).
  - **Air ambulance** is covered by the federal NSA, not HB 1489.
  - **Medicare, Medicaid, workers' compensation** are separate reimbursement regimes; HB 1489 does not displace them.
- **Use:** For any ground-ambulance balance bill incurred **on or after July 1, 2024** by a state-regulated insured, this is the lead state-law cite. Pair it with the federal NSA emergency-services rule for emergency transports (the NSA does not directly cover ground ambulance, but ER-related transport may pull in NSA emergency-services protections at the destination facility).

## Regulatory agencies

### Mississippi Insurance Department (MID)

- **Online complaint:** [mid.ms.gov/mississippi-insurance-department/consumers/file-a-complaint](https://www.mid.ms.gov/mississippi-insurance-department/consumers/file-a-complaint/) (company complaint at [mid.ms.gov/mississippi-insurance-department/consumers/file-a-complaint/file-company-complaint](https://www.mid.ms.gov/mississippi-insurance-department/consumers/file-a-complaint/file-company-complaint/))
- **Phone:** Consumer Help Line **1-800-562-2957** (toll-free); Jackson area **(601) 359-2453**
- **Email:** [consumer@mid.ms.gov](mailto:consumer@mid.ms.gov)
- **Fax:** (601) 359-1077
- **Mail:**
  > Mississippi Insurance Department
  > Attn: Consumer Services Division
  > P.O. Box 79
  > Jackson, MS 39205
- **Physical office:** 1001 Woolfolk State Office Building, 501 N. West Street, Jackson, MS 39201
- **Authority:** all insurance companies licensed in Mississippi, including fully-insured health insurers, HMOs, PPOs, Medicare supplement. Administers the Insurance Trade Practices Law (§ 83-5), § 83-9-5 balance-billing prohibition, HB 1489 ambulance reimbursement, and federal NSA compliance under the CMS collaborative-enforcement agreement. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272). Does not regulate hospitals, providers, or debt collectors directly (route to AG).

### Mississippi Attorney General — Consumer Protection Division

- **Online complaint:** [attorneygenerallynnfitch.com/divisions/consumer-protection](https://attorneygenerallynnfitch.com/divisions/consumer-protection/); complaint form PDF at [ago.state.ms.us/wp-content/uploads/2020/07/Approved-Consumer-Complaint-Form-7.23.20.pdf](https://www.ago.state.ms.us/wp-content/uploads/2020/07/Approved-Consumer-Complaint-Form-7.23.20.pdf)
- **Phone:** Consumer Protection Division **(601) 359-3680**
- **Mail:**
  > Office of the Attorney General
  > Consumer Protection Division
  > P.O. Box 22947
  > Jackson, MS 39225-2947
- **Director (as of this writing):** Crystal Utley Secoy
- **Authority:** enforces the Mississippi Consumer Protection Act (§ 75-24). Reach over providers, hospitals, third-party debt collectors, and original creditors engaged in deceptive practices. **This is the right channel when the dispute is with the hospital's billing department or a collector, not with an insurer.** The AG also runs the **informal dispute settlement program** that is a procedural prerequisite to a private § 75-24-15 action — engage that program before filing.

## Small claims court — Justice Court

- **Court name:** **Justice Court of [County]** (82 Justice Courts statewide, 198 judges; 4-year partisan elected terms)
- **Jurisdictional limit:** **$3,500**, codified at **Miss. Code Ann. § 9-11-9** and related sections; the small-claims framework at **Miss. Code §§ 11-9-101 through 11-9-147**
- **Source:** Mississippi Judiciary at [courts.ms.gov/trialcourts/justicecourt/justicecourt.php](https://courts.ms.gov/trialcourts/justicecourt/justicecourt.php); Rules of Justice Court at [courts.ms.gov/research/rules/msrulesofcourt/Rules%20of%20Justice%20Court.pdf](https://courts.ms.gov/research/rules/msrulesofcourt/Rules%20of%20Justice%20Court.pdf); Mississippi Center for Justice overview at [mscenterforjustice.org/justice-court-the-court-of-the-people](https://mscenterforjustice.org/justice-court-the-court-of-the-people/)
- **Attorney rules:** permitted, not required for individual parties. The court is designed for pro se litigants — informal proceedings, simplified pleadings, relaxed evidence rules; not bound by the Mississippi Rules of Civil Procedure. **A corporation filing a small-claims case must retain an attorney** — Mississippi's rule cuts the opposite way from Georgia's Magistrate Court rule (which lets corporations appear through a non-lawyer employee). This is a meaningful pro-patient asymmetry on the **incoming-direction** (the patient is the plaintiff suing a hospital) but a disadvantage on the **outgoing-direction** (a hospital suing the patient must hire counsel, which raises its cost-to-collect).
- **Filing fees:** typical 2024-2025 range $50-$80 plus service of process, varies by county. Confirm with the specific Justice Court clerk.
- **Jury trial:** not available in Justice Court. Either party may appeal de novo to the **County Court** (where one exists) or **Circuit Court** within 30 days under Miss. Code § 11-51-91 and demand a jury there.
- **Bills above $3,500:** **County Court** (where established, currently 21 counties) has concurrent jurisdiction up to $200,000; **Circuit Court** is the court of general civil jurisdiction above $3,500 elsewhere.

## Statute of limitations

- **General catch-all (3 years):** **Miss. Code Ann. § 15-1-49** — three years from accrual for any action "for which no other period of limitation is prescribed."
- **Open accounts, account stated, unwritten contracts (3 years):** **Miss. Code Ann. § 15-1-29** — three years from accrual, except an unwritten employment contract is one year.
- **Sale of goods, UCC (6 years):** Miss. Code Ann. § 75-2-725 — four years on goods sales, with limited tolling.
- **Written contracts (no separate longer statute):** Mississippi does **not** have a separate longer SOL for written contracts; the general 3-year rule under § 15-1-49 applies. **This is the principal difference from Georgia (6 years on written contracts) and Alabama (6 years on written contracts).**
- **Source:** § 15-1-49 at [law.justia.com/codes/mississippi/title-15/chapter-1/section-15-1-49](https://law.justia.com/codes/mississippi/title-15/chapter-1/section-15-1-49/); § 15-1-29 at [law.justia.com/codes/mississippi/title-15/chapter-1/section-15-1-29](https://law.justia.com/codes/mississippi/title-15/chapter-1/section-15-1-29/); practitioner overview at [harrislawfirm.com/articles/mississippi-statute-limitations-civil-cases](https://harrislawfirm.com/articles/mississippi-statute-limitations-civil-cases/)
- **User-prompt correction:** The prompt suggested § 15-1-29 carries a 3-year written-contract SOL for medical bills via partial-payment cases. The statute on its face covers **open accounts, account stated, and unwritten contracts** — not written contracts. Mississippi case law treats most hospital admission forms (signed financial-responsibility agreements) as written contracts and applies § 15-1-49's three-year catch-all, **not** § 15-1-29. The bottom-line three-year clock is the same either way, but the proper citation depends on whether a signed financial-responsibility form exists. **In practice, 3 years applies to medical-billing disputes in Mississippi regardless of which section is the technically correct cite.**

Partial payment or written acknowledgment of the debt can restart the clock under Mississippi tolling doctrine. **Do not make a partial payment on a time-barred debt without legal advice.**

## Surprise billing — federal floor plus § 83-9-5 + HB 1489

Mississippi's state-law surprise-billing layer is built from two pieces that pre-date the federal NSA and one piece that closes the federal gap:

1. **§ 83-9-5(1)(i) AOB-route balance-billing prohibition** (2013, expanded 2019) — applies whenever the insured assigns benefits to the provider in writing. Predates the federal NSA by nearly a decade.
2. **HB 1489 / Triage-Treat-Transport Act** (2024, effective July 1, 2024) — ground ambulance protection at the greater of local contract rate or 325% Medicare.
3. **Federal No Surprises Act** (Pub. L. 116-260, Title I of Division BB, effective Jan 1, 2022) — covers ER services from OON providers/facilities, non-emergency OON services at in-network facilities, and **air ambulance**. The federal NSA does **not** cover ground ambulance — that is exactly what HB 1489 closes for state-regulated coverage.

The MID enforces all three through the collaborative agreement with CMS. Mississippi's state-side framework is materially more protective than its neighbor Alabama's (no state surprise-billing law at all) but less protective than Georgia's § 33-20E-1 et seq. (no required-AOB precondition, broader provider-rate dispute mechanism).

**Self-funded ERISA plans** sit outside the state-side protections; the federal NSA is the only floor.

## Credit reporting

Mississippi has **not** enacted a state-specific medical-debt credit-reporting restriction. Patients in Mississippi rely on:

- The 2022-2023 voluntary changes by Equifax/Experian/TransUnion (paid medical debt removed; debt under $500 not reported; one-year delay before reporting).
- Federal FCRA dispute rights (15 U.S.C. §§ 1681i, 1681s-2).
- The MCPA's general deceptive-practices provisions (§ 75-24-5) where furnishing of medical-debt information to credit bureaus is itself deceptive (misrepresenting amount, status, or validity).

**Federal preemption posture is in flux.** The CFPB issued an October 2025 interpretive rule taking the position that the FCRA preempts state laws restricting medical-debt credit reporting. If that survives challenge, it constrains any future Mississippi state-level law on this front. Source: [consumerfinanceinsights.com/2025/11/02/cfpb-issues-rule-that-fcra-preempts-state-measures-barring-medical-debt](https://www.consumerfinanceinsights.com/2025/11/02/cfpb-issues-rule-that-fcra-preempts-state-measures-barring-medical-debt/).

For deceptive furnishing of medical-debt information to credit bureaus, MCPA § 75-24-5 may apply (subject to the informal-dispute-settlement prerequisite and asymmetric fee-shifting under § 75-24-15), and the patient may have a federal FCRA claim against the furnisher.

## Hospital lien statute

- **General hospital lien: none.** Mississippi's general hospital lien statute was **repealed in 1989** and has not been re-enacted. Mississippi is one of a small number of states with no general statutory hospital lien against third-party recoveries. Multiple bills since 2011 have attempted reinstatement and none have passed.
- **Narrow surviving lien — traumatic burn care only:** **Miss. Code Ann. §§ 85-7-301 through 85-7-317**, "Qualifying Providers of Burn Care Lien for Causes of Action."
- **Source:** § 85-7-301 at [codes.findlaw.com/ms/title-85-debtor-creditor-relationship/ms-code-sect-85-7-301.html](https://codes.findlaw.com/ms/title-85-debtor-creditor-relationship/ms-code-sect-85-7-301.html); chapter index at [law.justia.com/codes/mississippi/title-85/chapter-7/article-19](https://law.justia.com/codes/mississippi/title-85/chapter-7/article-19/); 50-state lien chart at [mwl-law.com/wp-content/uploads/2019/09/HOSPITAL-LIEN-LAWS-IN-ALL-50-STATES-CHART-00215685x9EBBF.pdf](https://www.mwl-law.com/wp-content/uploads/2019/09/HOSPITAL-LIEN-LAWS-IN-ALL-50-STATES-CHART-00215685x9EBBF.pdf)
- **Substance of the burn-care lien:** A hospital designated as a burn center by the State Department of Health (or qualifying physician practice providing care to such a patient) has a lien for reasonable charges for uncompensated traumatic burn care, **only upon the patient's causes of action against third parties** who caused the injuries that necessitated the care. **Not a lien on the patient's home, wages, or other property.**
- **Pre-care settlements unaffected:** § 85-7-311 expressly provides that any settlement or release executed **before the patient's entry into the qualifying hospital** is not affected by the lien chapter.
- **Patient-side practical effect:** For any hospital bill that is **not** burn-center treatment for a third-party-caused injury, Mississippi providers have **no statutory lien lever** against the patient's recovery from a tortfeasor. This is a meaningful pro-patient gap: a hospital pursuing collection in Mississippi must use ordinary contract-collection routes (suit on the bill, judgment, post-judgment enforcement), not a statutory third-party-recovery lien. Verify carefully if a provider asserts a lien against a personal-injury settlement — outside burn care, the assertion likely has no statutory footing.

## Hospital charity care

Mississippi has **no state statute** requiring a comprehensive hospital financial-assistance policy beyond federal law.

- **Federal floor:** Non-profit hospitals are bound by **IRS § 501(r)** — required FAP, required disclosure to the public, limits on extraordinary collection actions, capping amounts charged to FAP-eligible patients at amounts generally billed to insured patients. § 501(r) is the binding floor.
- **§ 501(r) collection timing:** Federal rules require **120 days** after first post-discharge bill before extraordinary collection actions, and **240 days** for FAP eligibility determination. Mississippi non-profit hospitals must observe these federal timelines.
- **State Medicaid disproportionate share floor:** Hospitals participating in Mississippi Medicaid's disproportionate-share program (Miss. Code § 43-13-117) have downstream charity obligations tied to that participation, but no general FAP mandate beyond § 501(r).
- **For-profit and county/municipal hospitals** have **no state FAP mandate**.

Use Dollar For at [dollarfor.org/state_sheet/mississippi](https://dollarfor.org/state_sheet/mississippi/) for screening.

## Wage garnishment

- **Statutes:** **Miss. Code Ann. §§ 11-35-1 through 11-35-61** (general post-judgment garnishment procedure); federal Consumer Credit Protection Act cap applies.
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a court judgment. Post-judgment, garnishment is capped at the federal level — 25% of disposable earnings, or the amount by which weekly disposable earnings exceed 30× the federal minimum wage, whichever is less. Mississippi does **not** prohibit wage garnishment for medical debt as some states (NC, SC, TX, PA) do — judgment-creditor garnishment is available.
- **Use:** In response letters to collectors threatening garnishment without a judgment in hand. Confirm any garnishment threat is backed by an actual writ from a Mississippi court of competent jurisdiction.

## Quick reference for letter rendering

When the LLM renders a Mississippi-bound letter, substitute these defaults:

- **State statute (records and billing right):** **Miss. Code Ann. § 41-10-5** — 30 days from valid written request for medical AND billing records (effective 7/1/2022). Pair with § 41-9-65's "good cause shown" reasonable-access rule for hospital records specifically. There is no standalone itemization-duty statute analogous to Georgia's § 10-1-393(b)(14).
- **State insurance department (CC line):** Mississippi Insurance Department, Consumer Services Division, P.O. Box 79, Jackson, MS 39205 ([mid.ms.gov](https://www.mid.ms.gov), 1-800-562-2957)
- **State AG consumer protection (CC line):** Office of the Attorney General, Consumer Protection Division, P.O. Box 22947, Jackson, MS 39225-2947 ([attorneygenerallynnfitch.com/divisions/consumer-protection](https://attorneygenerallynnfitch.com/divisions/consumer-protection/), (601) 359-3680)
- **Small-claims court name:** **Justice Court of [county]**
- **Filing fee (in 30-day warning):** "approximately $50-$80 plus service of process, varies by county"
- **Statute of limitations (in 30-day warning):** "Miss. Code Ann. § 15-1-49 (three-year general limitation) or § 15-1-29 (three years for open accounts and unwritten contracts) — three years in either case"
- **For ground ambulance balance bills (post-July 1, 2024):** Cite **HB 1489 (2024 Regular Session), codified in Miss. Code Title 83, Chapter 9** — 325% of Medicare minimum reimbursement, patient held harmless beyond cost-share. State-regulated plans only; not self-funded ERISA. Note pending federal challenge in 3:24-cv-00379-HTW-LGI (still in force).
- **For balance-billing disputes generally:** Cite **Miss. Code Ann. § 83-9-5(1)(i)** — if a written AOB exists, the insurer's direct payment is payment in full and the provider is statutorily barred from balance-billing above cost-share. Confirm AOB documentation before relying.
- **For provider-side deceptive-billing disputes:** Cite **Miss. Code Ann. § 75-24-5 and § 75-24-15** (MCPA private right of action). **Engage the AG's informal dispute settlement program first** — that prerequisite is a common dismissal vector. Note the asymmetric fee-shifting (prevailing defendant can recover fees on a frivolous claim; prevailing plaintiff cannot).
- **For insurer-side disputes (fully-insured plans):** Lead with **common-law bad faith under *Standard Life Ins. Co. v. Veal*, 354 So. 2d 239 (Miss. 1977), refined by *Murphree v. Federal Ins. Co.*, 707 So. 2d 523 (Miss. 1997)**. Punitive damages available subject to Miss. Code § 11-1-65 caps. Send a written, certified demand identifying the policy, claim, amount owed, and a payment deadline to anchor the "no arguable basis" element.

## Key Mississippi-specific advantages

Worth keeping in mind when triaging an MS patient's bills:

1. **§ 83-9-5(1)(i) AOB-route balance-billing prohibition** — pre-dates the federal NSA by nearly a decade and treats the insurer's direct payment as payment in full. When a written assignment of benefits is in place, the provider is statutorily barred from balance-billing above cost-share. This is the **headline patient-side lever** in MS and is materially stronger than Alabama's posture (no state law at all).
2. **HB 1489 ground-ambulance protection (effective July 1, 2024)** — Mississippi is one of ~19 states that have closed the federal NSA's ground-ambulance gap for state-regulated plans. 325% of Medicare is a high reimbursement floor by national comparison. Track the MAHP federal-court challenge but rely on the statute until enjoined.
3. **Veal/Murphree bad-faith with punitive damages** — Mississippi's first-party bad-faith doctrine produces real punitive verdicts when the "no arguable basis" prong is crossed. ERISA-preempted for self-funded plans, but fully in play for fully-insured and individual-market coverage. Mississippi's punitive caps (§ 11-1-65) are higher than most states for larger defendants.
4. **No general hospital lien** — Mississippi's repealed-1989 posture means hospitals have no statutory lien against personal-injury recoveries (outside the narrow burn-care exception). Providers must use ordinary judgment-collection routes, which is a measurable structural advantage for MS patients with concurrent tort claims.
5. **MID + CMS collaborative enforcement** — the Mississippi Insurance Department has a formal partnership with CMS for federal NSA compliance, layered on top of § 83-9-5. State-side complaints get federal cooperation; this is a real-world enforcement multiplier.

## What Mississippi does **not** have (vs. Georgia)

For accurate triage, the lever-gaps matter as much as the levers:

- **No automatic itemization duty.** Mississippi is request-based via § 41-10-5 (30 days) and § 41-9-65 ("good cause shown"), not the six-business-day automatic rule Georgia uses.
- **No itemization-statute private right of action.** Itemization-failure claims have to be re-pleaded through MCPA § 75-24-15 (with its informal-dispute prerequisite and asymmetric fee-shifting).
- **No prevailing-plaintiff attorney's fees under MCPA.** § 75-24-15 allows only the prevailing defendant to recover fees, and only on a frivolousness finding. This is the largest single MCPA-vs-FBPA gap.
- **No state medical-debt credit-reporting law.**
- **Smaller small-claims limit, $3,500 vs. Georgia's $15,000.** Most material medical-bill disputes will exceed the Justice Court cap and need County Court (where established) or Circuit Court.
- **Shorter written-contract SOL.** Mississippi's general three-year rule applies to medical-bill written contracts; Georgia gives written contracts six years.
- **No standalone surprise-billing act on the Georgia/HB 286 model** — Mississippi's protection lives in the older § 83-9-5 AOB-conditioned rule plus HB 1489's ground-ambulance carve-out, rather than a comprehensive single-statute framework.
