# Kansas state pack

The fully-worked state-law layer for Kansas patients. The LLM uses this when the patient's state is Kansas. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-19. Re-verify annually.

Two things make Kansas's patient-side leverage distinctive:

1. The **Kansas Consumer Protection Act (KCPA)** carries a private right of action with **mandatory attorney's fees to a prevailing consumer** (K.S.A. 50-634(e)) and reaches original creditors, not just third-party debt collectors. It also reaches "unconscionable" pricing under K.S.A. 50-627 — a useful theory against grossly inflated chargemaster bills.
2. **Small claims court excludes attorneys** as a default (K.S.A. 61-2714). A corporate creditor that wants counsel triggers the patient's right to counsel too, which usually means neither side lawyers up. Combined with the $10,000 jurisdictional limit (raised from $4,000 effective July 1, 2024), this gives a self-represented patient a near-symmetric venue.

Working against the patient, Kansas does **not** recognize a common-law first-party bad-faith tort (*Spencer v. Aetna*, 1980), there is **no private right of action under the Kansas Unfair Trade Practices Act**, and Kansas's only state-level surprise-billing statute (HB 2325, 2021-22 session) **died in committee** — federal No Surprises Act is the only protection.

## Hospital itemization right

- **Source of duty:** **K.A.R. § 28-34-3b(a)(9)** — Kansas Administrative Regulation, patient rights in licensed medical care facilities, implementing K.S.A. § 65-431 (hospital licensure).
- **Source:** [law.cornell.edu/regulations/kansas/K-A-R-28-34-3b](https://www.law.cornell.edu/regulations/kansas/K-A-R-28-34-3b); enabling statute at [ksrevisor.gov/statutes/chapters/ch65/065_004_0031.html](https://www.ksrevisor.gov/statutes/chapters/ch65/065_004_0031.html)
- **What it requires:** "Each patient has the right to examine and receive a detailed explanation of the patient's bill." Triggered by request; not automatic on discharge.
- **Caveat on the citation:** Kansas **does not** have a clean statutory itemization right comparable to Georgia's O.C.G.A. § 10-1-393(b)(14). The two K.S.A. sections sometimes cited in this space are not on point:
  - **K.S.A. § 65-468** — definitions for rural health networks; unrelated to billing.
  - **K.S.A. § 65-4906** — immunity of medical-malpractice screening panels; unrelated to billing.
  The operative rule is the K.A.R. patient-rights regulation, plus federal levers (No Surprises Act §§ 2799B-3 and 2799B-6 good-faith estimate / itemized-bill provisions for uninsured/self-pay patients, and 45 C.F.R. § 164.524 HIPAA right of access to billing records).
- **Practical use:** A written request citing K.A.R. § 28-34-3b(a)(9) plus the federal No Surprises Act good-faith-estimate rules is the strongest combined demand. There is no statutory deadline in the K.A.R. itself; HIPAA imposes a 30-day deadline for billing records held in the designated record set.
- **Private right of action:** No direct private right under the K.A.R., but a refusal can support a KCPA claim (deceptive or unconscionable conduct under K.S.A. 50-626 / 50-627) and a HIPAA complaint to HHS OCR.
- **ERISA:** Not preempted — regulates the provider, not the plan.

## Kansas Consumer Protection Act (KCPA)

- **Statute:** **K.S.A. § 50-623 et seq.** — Kansas Consumer Protection Act
- **Key sections:**
  - § 50-626 — deceptive acts and practices
  - § 50-627 — unconscionable acts and practices
  - § 50-634 — private remedies
  - § 50-636 — civil penalties (up to $10,000 per violation; up to $20,000 against a protected consumer such as elder, disabled, etc.)
- **Source:** [law.justia.com/codes/kansas/chapter-50/article-6/section-50-623](https://law.justia.com/codes/kansas/chapter-50/article-6/section-50-623/); [ksrevisor.gov/statutes/chapters/ch50/050_006_0034.html](https://ksrevisor.gov/statutes/chapters/ch50/050_006_0034.html)
- **Substance:** Broad UDAP. § 50-626 prohibits deceptive practices (misrepresentations about price, services, network status, etc.) — actual deception is **not required**, the practice is unlawful if it could deceive. § 50-627 prohibits unconscionable practices, including pricing that "grossly exceeds" comparable market pricing or that exploits a consumer's inability to protect their interests (relevant when a chargemaster bill is multiples of the negotiated or Medicare rate).
- **Private right of action:** **Yes**, under § 50-634. A consumer may recover the greater of **actual damages or a civil penalty of up to $10,000 per violation** (court discretion), plus reasonable attorney's fees under § 50-634(e), plus costs. A **protected consumer** (age 60+, disabled, military, etc.) may also recover punitive damages under § 50-636(c)(2). No pre-suit notice requirement.
- **Reach:** Original creditors are within scope — the hospital's own billing department is a "supplier" engaged in a "consumer transaction." This is broader than the federal FDCPA, which only reaches third-party debt collectors.
- **Use in medical-bill disputes:**
  - Deceptive: billing for services not rendered, upcoding, misrepresenting in-network status, misrepresenting amounts owed after insurance adjustment, threatening lawsuit without intent.
  - Unconscionable: chargemaster-level billing of self-pay or out-of-network patients at multiples of the prevailing rate; financial-responsibility forms presented under duress.

## Kansas Unfair Trade Practices Act (insurance UDAP)

- **Statute:** **K.S.A. § 40-2401 et seq.** — Kansas Unfair Trade Practices Act (insurance)
- **Key sections:** § 40-2403 (definitions), § 40-2404 (listed prohibited practices, including unfair claims settlement), § 40-2406-2407 (Commissioner enforcement)
- **Source:** [ksrevisor.gov/statutes/chapters/ch40/040_024_0001.html](https://ksrevisor.gov/statutes/chapters/ch40/040_024_0001.html); [ksrevisor.gov/statutes/chapters/ch40/040_024_0004.html](https://ksrevisor.gov/statutes/chapters/ch40/040_024_0004.html)
- **Substance:** Prohibits insurers from engaging in defined unfair claims-settlement practices — misrepresenting policy provisions, failing to acknowledge claims promptly, denying without a reasonable investigation, etc. § 40-2404(9) requires "frequency as to indicate a general business practice" for those acts to constitute an unfair practice.
- **Critical caveat:** **No private right of action.** Kansas federal and state courts have repeatedly held that K.S.A. 40-2401 et seq. does not authorize a private cause of action by the insured. Enforcement is by the Kansas Insurance Commissioner only. See, e.g., *Bonnel v. Bank of America*, 284 F. Supp. 2d 1284, 1289 (D. Kan. 2003) ("the Kansas unfair claims settlement practices statute does not authorize a private cause of action").
- **Use:** Cite UTPA violations in your complaint to the Kansas Department of Insurance (see below) and as evidentiary support for any K.S.A. 40-256 attorney-fee claim. **Do not plead UTPA as a standalone count in litigation.**

## Bad faith — Kansas does not recognize the tort

- **Leading case:** ***Spencer v. Aetna Life & Casualty Ins. Co.***, 227 Kan. 914, 611 P.2d 149 (1980)
- **Source:** [law.justia.com/cases/kansas/supreme-court/1980/51946-0.html](https://law.justia.com/cases/kansas/supreme-court/1980/51946-0.html)
- **Holding:** "The tort of bad faith is not recognized in Kansas." First-party insureds are limited to **statutory remedies**, principally K.S.A. 40-256 (attorney's fees where the insurer refused payment "without just cause or excuse"), K.S.A. 40-908 (property losses), and K.S.A. 40-3111 (PIP). The Court reasoned that the legislative scheme — Commissioner enforcement plus fee-shifting statutes — was adequate to deter insurer misconduct.
- **K.S.A. § 40-256 attorney's fee remedy:**
  - Source: [ksrevisor.gov/statutes/chapters/ch40/040_002_0056.html](https://ksrevisor.gov/statutes/chapters/ch40/040_002_0056.html)
  - **Substance:** If the insurer refuses payment of a loss covered under any policy without just cause or excuse, the court **shall** award the prevailing insured reasonable attorney's fees on top of any judgment.
  - "Without just cause or excuse" is interpreted as a frivolous, unfounded, or vexatious refusal — more than negligence or honest mistake, less than the punitive standard. No statutory penalty multiplier (unlike Georgia's § 33-4-6 50% penalty).
- **Practical impact vs. Georgia:** A Kansas health-insurance bad-faith plaintiff cannot recover a 50% statutory penalty, cannot recover emotional-distress damages on a bad-faith tort theory, and is limited to: (i) the contract benefits, (ii) attorney's fees under § 40-256, and (iii) interest. This is a meaningful reduction in leverage versus Georgia.
- **ERISA preemption:** § 40-256 is preempted as applied to self-funded ERISA plans. For ERISA self-funded plans the federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) attorney's fees.

## Surprise billing — federal NSA only

- **Kansas state law:** **None in force.** HB 2325 ("End Surprise Medical Bills Act," 2021-22 session) **died in committee** on May 23, 2022, and was not enacted. A reintroduced version (HB 2325, 2023-24 session) also did not become law.
- **Source:** [kslegislature.gov/li_2022/b2021_22/measures/hb2325](https://www.kslegislature.gov/li_2022/b2021_22/measures/hb2325/); status confirmed via the legislature's bill-history record.
- **Operative protection:** The **federal No Surprises Act** (Pub. L. 116-260, Div. BB; 42 U.S.C. §§ 300gg-111 et seq.; 45 C.F.R. Part 149), effective January 1, 2022.
  - Prohibits balance billing for **emergency services** from OON providers/facilities.
  - Prohibits balance billing for **non-emergency services** at in-network facilities by OON ancillary providers (anesthesia, radiology, pathology, lab, hospitalist, intensivist, neonatology, assistant surgeon).
  - Covers **air ambulance**.
  - **Does not cover ground ambulance.**
  - Provides good-faith-estimate rights to uninsured/self-pay patients (§ 2799B-6) and a Patient-Provider Dispute Resolution process if the bill exceeds the estimate by $400+.
- **State enforcement of federal NSA:** Kansas signed a collaborative enforcement agreement with CMS — the Kansas Department of Insurance enforces NSA provisions against KS-licensed health insurers; CMS retains direct enforcement against providers and facilities in Kansas. See [getcoveredkansas.org/no-surprises-act-information-and-resources](https://getcoveredkansas.org/no-surprises-act-information-and-resources).
- **ERISA:** NSA applies to self-funded ERISA plans (it is federal law), so it covers the entire commercial market — unlike state surprise-billing laws.

## Ground ambulance — no Kansas protection

- **Kansas state law:** **None.** Kansas has not enacted a ground-ambulance balance-billing protection.
- **Federal:** The No Surprises Act **explicitly excludes ground ambulance**. The federal Advisory Committee on Ground Ambulance and Patient Billing (GAPB) issued recommendations in 2023, but Congress has not acted.
- **Practical posture:** A Kansas patient who receives an out-of-network ground-ambulance bill has **no state-law balance-billing protection**. Available levers:
  - Negotiate down to the in-network or Medicare rate (no statutory backing, but the federal advisory committee's recommended rates are useful reference points).
  - KCPA § 50-627 unconscionable pricing if the charge grossly exceeds prevailing rates.
  - Charity-care application if the provider is non-profit and subject to IRS § 501(r).
  - Municipal-EMS billing-policy review if the ambulance is operated by a city or county; many Kansas municipal EMS providers have written write-off policies for residents.
- This is the single biggest gap in Kansas-side leverage relative to states like Georgia and Colorado.

## Regulatory agencies

### Kansas Department of Insurance (KID)

- **Online complaint:** [insurance.kansas.gov/complaint](https://insurance.kansas.gov/complaint/)
- **Phone:** main **(785) 296-3071**; Consumer Assistance Hotline **1-800-432-2484**
- **Email:** KDOI@ks.gov
- **Mail:**
  > Kansas Department of Insurance
  > Consumer Assistance Division
  > 1300 SW Arrowhead Road
  > Topeka, KS 66604
- **Authority:** all insurance companies, HMOs, PPOs, Medicare supplement, and health insurers licensed in Kansas. Administers the Unfair Trade Practices Act (K.S.A. 40-2401 et seq.) and external-review process (K.S.A. 40-22a13 et seq. — 120-day window after adverse decision). Enforces the federal No Surprises Act against KS-licensed insurers under a collaborative-enforcement agreement with CMS. **No authority over self-funded ERISA plans** (route to U.S. DOL EBSA, 1-866-444-3272) and does not regulate hospitals, providers, or debt collectors (route to AG).

### Kansas Attorney General — Consumer Protection Division

- **Online complaint:** [ag.ks.gov/file-a-complaint/consumer-protection](https://www.ag.ks.gov/file-a-complaint/consumer-protection) (also at [InYourCornerKansas.org](https://www.inyourcornerkansas.org))
- **Phone:** Consumer Protection Hotline **1-800-432-2310**; direct **(785) 296-3751**
- **Fax:** (785) 291-3699
- **Mail:**
  > Office of the Kansas Attorney General
  > Consumer Protection Division
  > 120 SW 10th Avenue, 2nd Floor
  > Topeka, KS 66612
- **Authority:** enforces the Kansas Consumer Protection Act (K.S.A. 50-623 et seq.) including against hospitals, physician practices, and original creditors, plus state debt-collection rules. Operates a mediation program for individual disputes. Reach over hospitals, providers, third-party debt collectors, **and original creditors** — exactly the gap not covered by KID. The most useful agency for hospital-billing-department disputes.

## Small claims court — Kansas District Court (Small Claims docket)

- **Court name:** Kansas District Court — small claims procedure (no separate court; each judicial district hears small claims under chapter 61, article 27)
- **Jurisdictional limit:** **$10,000** as of July 1, 2024 (L. 2024, ch. 22, § 1), codified at **K.S.A. § 61-2703**. The user-facing materials in many counties still reference the old **$4,000** limit; verify with the specific clerk before filing.
- **Statutes:** **K.S.A. § 61-2701 through § 61-2714** — Small Claims Procedure Act
- **Source:** [ksrevisor.gov/statutes/chapters/ch61/061_027_0003.html](https://www.ksrevisor.gov/statutes/chapters/ch61/061_027_0003.html); [law.justia.com/codes/kansas/chapter-61/article-27](https://law.justia.com/codes/kansas/chapter-61/article-27/)
- **Filing fees:** typical 2024-2025 ranges:
  - Claims up to $500 — **$35-$49** (varies by district)
  - Claims $500.01 to $10,000 — **$55-$69** (varies by district)
- **Claim cap per claimant:** Each plaintiff is limited to **20 small-claims actions per calendar year** (K.S.A. § 61-2704(b)).
- **Attorney rules:** **K.S.A. § 61-2714.** **Attorneys are not permitted to represent a party in Kansas small claims court.** If any party uses an attorney (or is an attorney representing themselves), every other party then becomes entitled to attorney representation. In practice, corporate defendants such as hospital billing offices appear through a non-attorney officer/employee, which removes their legal-fee advantage entirely. **This is one of Kansas's strongest patient-side levers.**
- **Jury trial:** **Not available** in small claims. Either party dissatisfied with the magistrate's judgment may appeal de novo to the district court within **14 days** under K.S.A. § 61-2709, where jury trial and full procedure apply.
- **Heads up on the limit change:** The 2024 amendment raising the cap to $10,000 means many Kansas medical-bill disputes (which often sit in the $4,000-$10,000 range) now fit in small claims for the first time. Patients should use $10,000 in dispute letters citing the venue. Confirm the local clerk's current intake forms reflect the new limit before filing.

## Statute of limitations

- **Written contracts:** **5 years from breach** — **K.S.A. § 60-511(1)**
- **Oral / implied / open-account contracts:** **3 years from breach** — **K.S.A. § 60-512(1)**
- **Source:** [law.justia.com/codes/kansas/chapter-60/article-5/section-60-511](https://law.justia.com/codes/kansas/chapter-60/article-5/section-60-511/); [law.justia.com/codes/kansas/chapter-60/article-5/section-60-512](https://law.justia.com/codes/kansas/chapter-60/article-5/section-60-512/)

Most hospital admissions involve a signed financial-responsibility form — a written contract, so **5 years** applies. Implied-in-fact billing arrangements without a signed agreement (or where the signed form does not cover the specific charge) are treated as open accounts or oral contracts and run **3 years**. The clock runs from breach (typically the day payment was due and not made), not from when damages are discovered.

Partial payment, acknowledgment in writing, or a new written promise can restart the clock. **Do not make a partial payment on a time-barred medical debt without legal advice** — it can revive an otherwise dead claim.

## Credit reporting

Kansas has **not enacted a state-specific medical-debt credit-reporting restriction.** Kansas is not among the 14 states that have prohibited the practice as of 2025. Patients in Kansas rely on:

- The 2022-2023 voluntary changes by Equifax/Experian/TransUnion (paid medical debt removed; debt under $500 not reported; 1-year delay before reporting).
- Federal FCRA dispute rights (15 U.S.C. §§ 1681i, 1681s-2) against furnishers and CRAs.

**Federal status is in flux.** The CFPB's January 2025 final rule prohibiting medical-debt reporting on most consumer reports has been stayed by pending litigation and was effectively halted by a 2025 administration order. The October 2025 CFPB interpretive rule (FCRA preempts state medical-debt-reporting laws) is also under challenge. As of this writing, no Kansas-specific protection applies, and the patient's leverage is federal FCRA dispute and the 2023 CRA voluntary policies.

For deceptive furnishing of medical-debt information to credit bureaus, the KCPA's deceptive-practices provisions (K.S.A. 50-626) may reach the furnisher, and the patient has a federal FCRA furnisher-duty claim (15 U.S.C. § 1681s-2(b)) once a dispute is filed with the CRA.

## Charity care — federal § 501(r) floor

Kansas has **no general state statute** mandating a hospital financial-assistance policy applicable to all hospitals. Non-profit hospitals are bound by IRS **§ 501(r)** (federal): written FAP, plain-language summary, no extraordinary collection actions for 120 days post-billing, and limitation-on-amounts-generally-billed (AGB) for FAP-eligible patients.

Kansas-specific layers:

- **County indigent-care funding:** K.S.A. § 19-4601 et seq. allows counties with 175,000-250,000 residents to levy property taxes for indigent medical care at or below 100% FPL. Application deadline is **at least 240 days from the first post-discharge bill**, residency requirement is one year in the county.
- **Charitable Health Care Provider Act:** K.S.A. § 75-6102, § 75-6116 — extends Kansas Tort Claims Act coverage to volunteer providers serving indigent patients; not a charity-care mandate but supports the safety-net network.
- **Emergency-services copay prohibition:** Kansas administrative rules prohibit requiring a copay before emergency services are stabilized; mirrors EMTALA.

For-profit hospitals and county/municipal hospitals have **no state FAP mandate** beyond what their local governing body adopts. Use [dollarfor.org/state_sheet/kansas](https://dollarfor.org/state_sheet/kansas/) for screening tools and Hospital-specific FAPs.

## Hospital lien statute

- **Citation:** **K.S.A. § 65-406**
- **Sources:** [ksrevisor.gov/statutes/chapters/ch65/065_004_0006.html](https://ksrevisor.gov/statutes/chapters/ch65/065_004_0006.html); [law.justia.com/codes/kansas/chapter-65/article-4/section-65-406](https://law.justia.com/codes/kansas/2021/chapter-65/article-4/section-65-406/)
- **Substance:** A hospital providing emergency or other services to a patient **injured in an accident not covered by workers' compensation** may file a lien against the patient's recovery from the third-party tortfeasor — judgment or settlement. The lien attaches to "the reasonable and necessary charges" for treatment up to the date of payment.
- **Not a lien on the patient's home, wages, or bank accounts.** It is purely a lien on the third-party recovery.
- **$5,000 threshold:** When the lien claim exceeds **$5,000**, the **first $5,000 is fully enforceable**, and the portion above $5,000 is enforceable **only to the extent that enforcement constitutes an equitable distribution** of the settlement or judgment "under the circumstances" — a court determines equity if the parties cannot stipulate. This is a meaningful patient-side limitation, equity considerations include the patient's net recovery, attorney's fees from the underlying tort case, comparative negligence allocations, etc.
- **Workers' comp exception:** No lien if the injury is covered by Kansas Workers' Compensation. The exclusivity bar applies.
- **Perfection:** The hospital must file a verified statement of the lien with the clerk of the district court of the county where services were rendered, before the third-party claim is paid; courts have voided liens filed after the patient already received settlement funds. Verify perfection timing on every claim — defective perfection is a complete defense.

## Wage garnishment

- **Statute:** **K.S.A. § 60-2310**
- **Source:** [ksrevisor.gov/statutes/chapters/ch60/060_023_0010.html](https://ksrevisor.gov/statutes/chapters/ch60/060_023_0010.html)
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a court judgment. Post-judgment garnishment is capped at the lesser of (i) 25% of disposable earnings, (ii) the amount by which weekly disposable earnings exceed 30× the federal minimum hourly wage, or (iii) the amount of the plaintiff's claim. Tracks the federal Consumer Credit Protection Act cap.
- **Illness exemption:** If the debtor has been prevented from working for more than two weeks due to illness of the debtor or family member, garnishment may be paused for **two months after recovery** upon the debtor's affidavit. Useful where the underlying medical debt arose from the same incapacitating illness.
- **Assignment penalty:** If the original creditor sells or assigns the account to a collection agency, **neither the original creditor nor the assignee may use wage garnishment** at all (K.S.A. 60-2310(d)). This is a Kansas-specific patient advantage — confirm whether the debt has been assigned; if so, garnishment is statutorily barred.
- **Use:** In response letters to collectors threatening garnishment without a judgment, and especially when the original hospital has assigned the debt.

## Quick reference for letter rendering

When the LLM renders a Kansas-bound letter, substitute these defaults:

- **State source for itemization right:** **K.A.R. § 28-34-3b(a)(9)** (patient rights, implementing K.S.A. § 65-431); supplement with the federal NSA good-faith-estimate provisions (45 C.F.R. § 149.610) and HIPAA right of access (45 C.F.R. § 164.524, 30-day deadline).
- **State insurance department (CC line):** Kansas Department of Insurance, Consumer Assistance Division, 1300 SW Arrowhead Road, Topeka, KS 66604 — phone 1-800-432-2484
- **State AG consumer protection (CC line):** Office of the Kansas Attorney General, Consumer Protection Division, 120 SW 10th Avenue, 2nd Floor, Topeka, KS 66612 — phone 1-800-432-2310
- **Small-claims venue:** District Court of [county] of Kansas — small claims procedure
- **Small-claims limit (in 30-day warning):** **$10,000** (raised July 1, 2024 from $4,000)
- **Filing fee (in 30-day warning):** "$55-$69 depending on district for claims over $500"
- **Statute of limitations (in 30-day warning):** "K.S.A. § 60-511(1) (five years for breach of written contract)" — drop to "K.S.A. § 60-512(1) (three years for oral/implied contracts)" only if there is no signed financial-responsibility form
- **For provider-side disputes (vs. insurer-side):** Cite **K.S.A. § 50-626 (deceptive)** and/or **§ 50-627 (unconscionable)** with the private remedy under **§ 50-634 (actual damages or up to $10,000 civil penalty per violation, plus mandatory attorney's fees to a prevailing consumer)**. No pre-suit notice required.
- **For insurer-side disputes:** Cite **K.S.A. § 40-256** (attorney's fees on refusal "without just cause or excuse"). Do **not** cite K.S.A. 40-2401 et seq. as a private cause of action. Note in any settlement posture that Kansas does not recognize a common-law bad-faith tort (*Spencer v. Aetna*).
- **For ground-ambulance balance bills:** No state statute. Combine KCPA § 50-627 (unconscionable pricing) with negotiation toward the in-network or Medicare rate.

## Key Kansas-specific advantages

Worth keeping in mind when triaging a Kansas patient's bills:

1. **KCPA mandatory attorney's fees** — § 50-634(e) requires fee award to a prevailing consumer when the supplier has violated the act. Mandatory, not discretionary. This is the single highest-leverage cite for any provider-side dispute and outperforms Georgia's discretionary FBPA fee provision in clarity.
2. **KCPA "unconscionable" theory** — § 50-627 reaches grossly inflated pricing in a way most states' UDAPs do not. Chargemaster billing of self-pay patients at multiples of negotiated rates is a textbook KCPA § 50-627 case (see *State ex rel. Stovall v. ConfiMed.com*, 272 Kan. 1313 (2002) for the unconscionability framework).
3. **Civil penalty per violation** — up to **$10,000 per violation** under § 50-636, $20,000 if the consumer is a "protected consumer" (age 60+, disabled, military). Each separate misrepresentation is a separate violation.
4. **Small-claims attorney exclusion** — K.S.A. § 61-2714's default no-attorney rule is unusually strong. Corporate creditors that want to bring counsel into small claims trigger the patient's counter-right to counsel, which normally means neither side does. Combined with the new **$10,000 limit** (effective July 1, 2024), this makes small claims a viable forum for most medical-bill disputes without lawyer cost on either side.
5. **Assignment-bars-garnishment rule** — K.S.A. § 60-2310(d) blocks wage garnishment entirely once the original creditor has sold or assigned the account. Confirm assignment status on every threatened garnishment.
6. **Hospital-lien equity ceiling** — K.S.A. § 65-406's "above $5,000 only to the extent equitable" rule lets patients challenge inflated lien claims in personal-injury settlements through equitable-distribution proceedings.

## Key Kansas-specific disadvantages

Worth flagging upfront so patient expectations are calibrated:

1. **No common-law bad-faith tort** — *Spencer v. Aetna* limits insurance recoveries to contract benefits plus K.S.A. § 40-256 attorney's fees. No 50% statutory penalty, no emotional-distress damages on a bad-faith theory.
2. **No private right of action under the insurance UTPA** (K.S.A. 40-2401 et seq.) — Commissioner enforcement only.
3. **No state surprise-billing law** — Federal NSA is the only protection. Self-funded ERISA plans rely entirely on the federal regime (which does cover them); fully insured plans get federal coverage layered with KID enforcement against the insurer.
4. **No ground-ambulance protection** — neither state nor federal law shields the patient from ground-ambulance balance billing.
5. **No state medical-debt credit-reporting restriction** — patient relies on federal FCRA and CRA voluntary policies.
6. **No general state charity-care mandate** for hospitals — § 501(r) is the floor for non-profits, with no equivalent for for-profits.
