# Missouri state pack

The fully-worked state-law layer for Missouri patients. The LLM uses this when the patient's state is Missouri. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Three things make Missouri's patient-side leverage unusually strong:

1. The **vexatious refusal-to-pay statute** at RSMo § 375.296 / § 375.420 carries a statutory penalty of **20% of the first $1,500 plus 10% of the excess, plus reasonable attorney's fees** on top of the underlying loss. Unlike many states' bad-faith remedies, Missouri's is purely statutory and the attorney-fee shift is mandatory once the jury finds vexatious refusal.
2. The **statute of limitations on written contracts is 10 years** (RSMo § 516.110), tied for the longest in the United States. Medical bills tied to a signed financial-responsibility form are well within this window for years longer than in most states, but conversely so are the hospital's collection rights, so the SOL cuts both ways and must be checked carefully.
3. The **Missouri Merchandising Practices Act** (RSMo § 407.020 et seq.) is a powerful UDAP statute that reaches the hospital as an original creditor, with discretionary punitive damages and prevailing-party attorney's fees under RSMo § 407.025.

## Hospital itemization and cost-estimate right

- **Statute:** **RSMo § 191.875** — Healthcare provider, written estimate of cost required, when.
- **Source:** [revisor.mo.gov/main/OneSection.aspx?section=191.875](https://revisor.mo.gov/main/OneSection.aspx?section=191.875)
- **What it requires:**
  - Upon **written request by a patient** that includes a medical treatment plan from the patient's health care provider, the provider must deliver a written estimate of cost **within three (3) business days** by mail, electronically, or in person.
  - Estimate must be based on the entered information and typical-utilization assumptions, with a required disclosure that the actual bill may differ.
- **Scope:** Cost **estimates** for a particular health care service or procedure. The statute does not separately mandate post-treatment itemized bills the way Georgia § 10-1-393(b)(14) does, but a written request for an itemized statement is the standard practice and is reinforced by:
  - Federal hospital price transparency rules (45 CFR Part 180).
  - Federal No Surprises Act good-faith-estimate requirements for self-pay/uninsured patients.
  - The Missouri Patient Bill of Rights as adopted by individual facilities and by 19 CSR licensure rules.
- **Caveats:**
  - § 191.875 specifies **no penalty** for non-compliance and **no private right of action**. Enforcement runs through the Department of Health and Senior Services and licensure complaints.
  - The "medical treatment plan from the patient's health care provider" predicate makes this awkward to invoke for surprise post-treatment disputes; use it pre-procedure or pair with an MMPA letter post-bill.
- **ERISA:** Not preempted, regulates the provider, not the plan.

## Vexatious refusal to pay

- **Statute:** **RSMo § 375.296** (additional damages) and **RSMo § 375.420** (penalty formula).
- **Source:** [revisor.mo.gov/main/OneSection.aspx?section=375.296](https://revisor.mo.gov/main/OneSection.aspx?section=375.296); [revisor.mo.gov/main/OneSection.aspx?section=375.420](https://revisor.mo.gov/main/OneSection.aspx?section=375.420); Justia mirror at [law.justia.com/codes/missouri/title-xxiv/chapter-375/section-375-296/](https://law.justia.com/codes/missouri/title-xxiv/chapter-375/section-375-296/)
- **Substance:** In any action against an insurer on a contract of insurance, if the insurer has refused for 30 days after due demand to make payment, and the refusal was vexatious and without reasonable cause, the court or jury may award:
  - The underlying loss; plus
  - A statutory penalty of **20% of the first $1,500 of the loss**, plus **10% of the amount of the loss in excess of $1,500**; plus
  - **Reasonable attorney's fees**.
- **§ 375.296 vs. § 375.420:** § 375.420 is the original bad-faith provision applying when the policyholder filed suit on the policy. § 375.296 is the parallel section that applies the same penalty/fee formula when the action is brought by an assignee or beneficiary (e.g., a third-party claimant where the policyholder has admitted liability). For medical billing the action is typically by the insured, so § 375.420 is the operative citation; § 375.296 covers the assignment scenarios.
- **Procedural requirements:**
  - Send a written demand by certified mail identifying the policy, the claim, the amount demanded, and the basis.
  - Wait **30 days** after due demand. Payment within 30 days defeats the claim; payment after day 30 does not abate the action.
- **Standard:** "Vexatious and without reasonable cause" is more than negligence. A bona-fide dispute over coverage, the amount owed, or the existence of liability defeats the claim. The bar is meaningfully lower than the "frivolous and unfounded" standard some states require, but Missouri courts have repeatedly held that an honest dispute is not vexatious refusal.
- **Coverage:** "Any contract of insurance," including health insurance, accident and sickness, and disability. First-party.
- **ERISA preemption:** § 375.420 and § 375.296 are **preempted** as applied to self-funded ERISA employer plans. For ERISA self-funded plans the federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) fees. The statute remains in play for fully-insured plans, Medicaid managed care, and individual/marketplace plans.

## Common-law bad faith

Missouri also recognizes a common-law tort of bad-faith refusal to settle in the **third-party** liability context (insurer's duty to settle within policy limits when defending its insured). It is **not** a remedy for first-party medical-bill claims, those go through § 375.296 / § 375.420 above. Cite the common-law tort only when relevant (e.g., a liability insurer refusing to settle a related personal-injury claim within limits).

## Unfair Claims Settlement Practices Act

- **Statute:** **RSMo § 375.1000 to § 375.1018**, with the enumerated improper practices at **§ 375.1007**.
- **Source:** [revisor.mo.gov/main/OneSection.aspx?section=375.1007](https://revisor.mo.gov/main/OneSection.aspx?section=375.1007); implementing regulations at 20 CSR 100-1.010 et seq.
- **Substance:** Prohibits insurers from engaging in a defined list of improper claims-handling practices, misrepresenting policy provisions, failing to acknowledge communications promptly, failing to investigate reasonably, denying without reasonable basis, compelling litigation by offering substantially less than the amount eventually paid, and more, when committed with such frequency as to indicate a general business practice.
- **Critical caveat:** **No private right of action.** Missouri courts have repeatedly held that § 375.1000 to § 375.1018 do not create a private cause of action; enforcement rests with the Director of the Department of Commerce and Insurance through administrative cease-and-desist orders, fines, and license actions.
- **Use:** Cite UCSPA violations in your complaint to the DCI (see below) and as evidentiary support for a § 375.420 vexatious-refusal claim. Do not plead UCSPA as a standalone count in litigation.

## Surprise billing, unanticipated out-of-network care

- **Statute:** **RSMo § 376.690** — Unanticipated out-of-network care, billing limitations.
- **Source:** [revisor.mo.gov/main/OneSection.aspx?section=376.690](https://revisor.mo.gov/main/OneSection.aspx?section=376.690)
- **Substance:**
  - Defines "unanticipated out-of-network care" as care received in an **in-network facility** from an **out-of-network professional** between the time the patient presents with an emergency medical condition and the time of discharge.
  - Prohibits the out-of-network professional from balance-billing the patient for any difference between the carrier reimbursement (set by the statute's methodology) and billed charges.
  - Patient cost-share is limited to the in-network amount.
- **Scope, the limits to know:**
  - **Emergency only.** Missouri's statute does **not** cover non-emergency ancillary services at an in-network facility (anesthesia, radiology, pathology) the way the federal No Surprises Act does. For those, the federal NSA is the operative protection.
  - **No ground-ambulance coverage.** RSMo § 376.690 contains no reference to ground ambulance, and Missouri has not enacted a separate ground-ambulance balance-billing protection as of this writing. Bills tracked in 2024-2025 sessions (e.g., SB 7, SB 94) addressed reimbursement and operations, not consumer balance-billing protection.
- **Federal No Surprises Act is the primary protection for Missouri patients.** RSMo § 376.690 predates and overlaps the NSA but is narrower. The federal NSA covers:
  - Emergency services from OON providers/facilities.
  - Non-emergency services from OON providers at in-network facilities (ancillary services).
  - Air ambulance (not ground).
  - Patient cost-share capped at in-network amount; the patient is held harmless from rate disputes.
- **ERISA:** RSMo § 376.690 does not reach self-funded ERISA plans; those rely on the federal NSA.

## Missouri Merchandising Practices Act

- **Statute:** **RSMo § 407.010 et seq.**, with the unlawful-practices definition at **§ 407.020** and the private cause of action at **§ 407.025**.
- **Sources:** [revisor.mo.gov/main/OneSection.aspx?section=407.020](https://revisor.mo.gov/main/OneSection.aspx?section=407.020); [revisor.mo.gov/main/OneSection.aspx?section=407.025](https://revisor.mo.gov/main/OneSection.aspx?section=407.025); Justia chapter index at [law.justia.com/codes/missouri/title-xxvi/chapter-407/](https://law.justia.com/codes/missouri/title-xxvi/chapter-407/)
- **Substance:** Declares unlawful any "act, use or employment by any person of any deception, fraud, false pretense, false promise, misrepresentation, unfair practice or the concealment, suppression, or omission of any material fact in connection with the sale or advertisement of any merchandise." Missouri courts have consistently held that "merchandise" includes health-care services and that hospitals/providers fall within MMPA reach.
- **Private right of action under § 407.025:**
  - Plaintiff must be a person who **purchased or leased merchandise primarily for personal, family, or household purposes** and suffered an ascertainable loss.
  - Recoverable: **actual damages**, **punitive damages** (discretionary), **injunctive and other equitable relief**, and **reasonable attorney's fees** to the prevailing party.
- **2020 SB 591 reforms, important caveats:**
  - The plaintiff must plead and prove (i) reasonable consumer conduct in the circumstances, (ii) that the alleged unlawful practice would have caused a reasonable person to enter the transaction, and (iii) individual damages calculable "with a reasonable degree of certainty."
  - Courts must dismiss as a matter of law where the claim does not show a likelihood that the practice would mislead a reasonable consumer.
  - The 2020 amendments tightened class-action prerequisites and capped attorney's fees to time reasonably expended (no contingency-multiplier fee awards).
- **Why it matters for medical bills:** MMPA reaches **original creditors** (the hospital, the physician group), not just third-party debt collectors. This is broader than the federal FDCPA. Useful when the dispute is with the hospital's in-house billing department, the practice involves upcoding, billing for services not rendered, misrepresenting in-network status, or misrepresenting financial-assistance eligibility.
- **ERISA:** Not preempted as applied to provider conduct (it regulates the provider, not the plan).

## Regulatory agencies

### Missouri Department of Commerce and Insurance (DCI)

- **Online complaint:** [insurance.mo.gov/consumers/complaints/](https://insurance.mo.gov/consumers/complaints/index.php); SBS-hosted form at [sbs.naic.org/solar-web/pages/public/onlineComplaintForm/onlineComplaintForm.jsf?state=MO](https://sbs.naic.org/solar-web/pages/public/onlineComplaintForm/onlineComplaintForm.jsf?state=MO)
- **Phone:** Consumer Hotline **1-800-726-7390**; main office **(573) 751-4126**
- **Mail:**
  > Missouri Department of Commerce and Insurance
  > Division of Consumer Affairs
  > Harry S Truman State Office Building
  > 301 W. High St., Room 530
  > P.O. Box 690
  > Jefferson City, MO 65102-0690
- **Authority:** All insurance companies licensed in Missouri, including fully-insured health insurers, HMOs, Medicare supplement, and the producers/agents. Administers RSMo § 376.690 unanticipated-OON-care protections and the UCSPA at § 375.1000 et seq. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and does not regulate providers, hospitals, or debt collectors (route to AG, or Department of Health and Senior Services for licensure).

### Missouri Attorney General, Consumer Protection Division

- **Online complaint:** [ago.mo.gov/file-a-complaint](https://ago.mo.gov/file-a-complaint); direct form at [app.ago.mo.gov/app/consumercomplaint](https://app.ago.mo.gov/app/consumercomplaint)
- **Phone:** Consumer Protection Hotline **1-800-392-8222**
- **Email:** consumer.help@ago.mo.gov
- **Mail:**
  > Missouri Attorney General's Office
  > Consumer Protection Division
  > Supreme Court Building
  > 207 W. High St.
  > P.O. Box 899
  > Jefferson City, MO 65102
- **Authority:** Enforces the MMPA (§ 407.020 et seq.) and Missouri's debt-collection consumer-protection rules. Reach over providers, hospitals, third-party debt collectors, **and original creditors**, exactly the gap not covered by DCI. Useful when the dispute is with the hospital's in-house billing department or a collector.

## Small claims court, Associate Circuit Court Small Claims Division

- **Court name:** **Small Claims Division of the Circuit Court** (each circuit's Associate Circuit Court sits as the small claims court).
- **Jurisdictional limit:** **$5,000**, exclusive of interest and costs, codified at **RSMo § 482.305**.
- **Source:** [revisor.mo.gov/main/OneSection.aspx?section=482.305](https://revisor.mo.gov/main/OneSection.aspx?section=482.305); rules at [courts.mo.gov/page.jsp?id=682](https://www.courts.mo.gov/page.jsp?id=682)
- **Filing fees:** vary by county, typical 2024-2025 range **$35-$100** for filing plus service, with additional per-defendant service costs. Confirm with the local circuit clerk before filing.
- **Attorney rules:** permitted, not required (RSMo § 482.310). Corporations and unincorporated associations may appear through an officer or authorized employee without it constituting the unauthorized practice of law, useful when the corporate defendant is a hospital or collection agency.
- **Jury trial:** not available in the Small Claims Division. Either party may apply for a trial de novo before an associate circuit judge within **10 days** of judgment under RSMo § 482.365, which can be a jury trial if demanded.
- **Discovery and pleadings:** Simplified, designed for pro se litigants. The Missouri Supreme Court's Small Claims Rules govern.

## Statute of limitations

- **Written contracts:** **10 years from breach**, **RSMo § 516.110(1)** — "an action upon any writing, whether sealed or unsealed, for the payment of money or property." Tied for longest in the United States.
- **Oral contracts and implied/open accounts:** **5 years**, **RSMo § 516.120(1)** — "all actions upon contracts, obligations or liabilities, express or implied, except those mentioned in section 516.110."
- **Sources:** [revisor.mo.gov/main/OneSection.aspx?section=516.110](https://revisor.mo.gov/main/OneSection.aspx?section=516.110); [revisor.mo.gov/main/OneSection.aspx?section=516.120](https://revisor.mo.gov/main/OneSection.aspx?section=516.120)

Most hospital admissions involve a signed financial-responsibility form, treated as a written contract under § 516.110, so **10 years** applies. Implied-in-fact medical billing without a signed agreement (rare, but possible for an unconscious ER patient, certain ambulance encounters) may be treated as an oral/implied contract under § 516.120, so 5 years.

The clock runs from breach (typically the day payment was due and not made). **Partial payment, written acknowledgment, or a new promise to pay can restart the clock** under Missouri's "new promise" doctrine. **Do not make a partial payment on a time-barred debt without legal advice.**

## Ground ambulance balance billing

**Not protected by Missouri state law as of 2026-05-18.** RSMo § 376.690 (unanticipated OON care) is limited to in-network-facility scenarios and contains no ground-ambulance language. The federal No Surprises Act explicitly excludes ground ambulance.

Practical implication for Missouri patients: a balance bill from a ground-ambulance provider has **no state or federal statutory hold-harmless mechanism**. The leverage tools that remain are:

- Negotiate down using FAIR Health benchmarks and Medicare ground-ambulance fee schedules.
- File an insurance complaint with DCI if the carrier processed the claim unreasonably (UCSPA-style violations).
- File an MMPA complaint with the AG if the billed amount is so grossly above usual-and-customary that it constitutes a deceptive practice.
- Apply for hospital financial assistance if the patient was transported to a non-profit hospital (federal § 501(r)).
- Watch the federal Advisory Committee on Ground Ambulance and Patient Billing recommendations and any Missouri-specific legislation in the next session.

## Credit reporting

Missouri has not enacted a state-specific medical-debt credit-reporting restriction. Patients in Missouri rely on:

- The 2022-2023 voluntary changes by Equifax, Experian, and TransUnion (paid medical debt removed; debt under $500 not reported; 1-year delay before reporting).
- Federal FCRA dispute rights (15 U.S.C. §§ 1681i, 1681s-2).
- The CFPB's January 2025 final rule barring medical debt from consumer credit reports (currently enjoined/non-enforced pending litigation and the 2025 administration's stand-down).

**Federal preemption posture is in flux.** The CFPB issued an October 2025 interpretive rule taking the position that the FCRA preempts state laws restricting medical-debt credit reporting. Because Missouri has not passed such a law, the preemption fight does not directly affect Missouri patients today, but it forecloses a likely future state-level fix.

For deceptive furnishing of medical-debt information to credit bureaus, MMPA § 407.020 may apply to the furnisher, and the patient retains the federal FCRA claim.

## Hospital lien statute

- **Citations:** **RSMo § 430.225 to § 430.250**.
- **Sources:** [revisor.mo.gov/main/OneSection.aspx?section=430.225](https://revisor.mo.gov/main/OneSection.aspx?section=430.225); [revisor.mo.gov/main/OneSection.aspx?section=430.230](https://revisor.mo.gov/main/OneSection.aspx?section=430.230)
- **Substance:** Hospitals, clinics, physicians, surgeons, chiropractors, podiatrists, dentists, physical therapists, and optometrists may file a lien for reasonable charges, **only against the patient's claim for (a) damages from a tort-feasor, or (b) benefits from an insurance carrier**. **Not a lien on the patient's home, wages, or bank accounts.**
- **Cap on aggregate recovery:** Practitioner liens collectively are limited to **50% of the net proceeds** of the patient's third-party recovery, with proportional distribution if liens exceed that cap. "Net proceeds" means recovery after attorney's fees and litigation expenses. The 50% cap is a meaningful patient protection.
- **Perfection requirements:** Written notice by certified mail to the patient, the tort-feasor, and the tort-feasor's insurer. Notice must contain the injured person's name and address, the date of the accident, the name and location of the hospital/provider, and the names of those alleged liable. Specific timing requirements appear in §§ 430.230 to 430.245; confirm against the current statute before relying on a deadline.
- **Release:** A provider electing to take payment via the lien releases the patient from further liability on the cost of services.

## Hospital charity care

Missouri has **no state statute** requiring a hospital financial-assistance policy beyond federal law. Non-profit hospitals are bound by IRS § 501(r) (federal); for-profit and county/municipal hospitals have no Missouri-specific FAP mandate.

The Missouri Hospital Industry Data Institute publishes voluntary uncompensated-care data, and most Missouri non-profit hospitals maintain a written FAP for § 501(r) compliance. Cite § 501(r) and Notice 2015-46 in dispute letters to non-profit hospitals.

Use Dollar For at [dollarfor.org/state_sheet/missouri](https://dollarfor.org/state_sheet/missouri/) for screening.

## Wage garnishment

- **Statute:** **RSMo § 525.030** (general garnishment) and federal CCPA limits (15 U.S.C. § 1673).
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a court judgment. Post-judgment, garnishment is capped at the **lesser of (i) 25% of disposable earnings, or (ii) the amount by which weekly disposable earnings exceed 30× the federal minimum wage**, with a more protective **10% cap** for the head of a family supporting a spouse or minor children under § 525.030(2).
- **Use:** In response letters to collectors threatening garnishment without a judgment in hand, and to assert the head-of-family 10% cap where applicable.

## Quick reference for letter rendering

When the LLM renders a Missouri-bound letter, substitute these defaults:

- **State statute (itemization/estimate right):** **RSMo § 191.875**, written estimate within 3 business days upon written request that includes a treatment plan. For post-treatment itemized statements, frame the request under § 191.875 plus federal hospital price transparency rules and reasonable-billing-practice standards.
- **State insurance department (CC line):** Missouri Department of Commerce and Insurance, Division of Consumer Affairs, Harry S Truman State Office Building, 301 W. High St., Room 530, P.O. Box 690, Jefferson City, MO 65102-0690.
- **State AG consumer protection (CC line):** Missouri Attorney General, Consumer Protection Division, Supreme Court Building, 207 W. High St., P.O. Box 899, Jefferson City, MO 65102.
- **Small-claims court name:** **Small Claims Division of the Circuit Court of [county]**.
- **Filing fee (in 30-day warning):** "$35-$100 depending on county".
- **Statute of limitations (in 30-day warning):** "RSMo § 516.110 (ten years for an action upon any writing for the payment of money)".
- **For insurer-side disputes:** Cite **RSMo § 375.420** vexatious refusal-to-pay, including the 20% / 10% / attorney's fee penalty formula and the 30-day post-demand window. This is the single highest-leverage Missouri-specific cite when the dispute is with the carrier.
- **For provider-side disputes (vs. insurer-side):** Cite **RSMo § 407.020 / § 407.025** (Missouri Merchandising Practices Act) for the prevailing-party attorney's-fee shift and discretionary punitive damages. Note in the demand that MMPA reaches original creditors.
- **For emergency-OON balance bills at in-network facilities:** Cite **RSMo § 376.690** alongside the federal No Surprises Act. Missouri's statute is narrower (emergency only), so the NSA does most of the work for non-emergency ancillary balance bills.
- **For ground-ambulance balance bills:** No state or federal hold-harmless. Use negotiation tools, financial-assistance screening, and MMPA where the charge is grossly excessive.

## Key Missouri-specific advantages

Worth keeping in mind when triaging a Missouri patient's bills:

1. **Vexatious refusal-to-pay with mandatory attorney's-fee shift** — § 375.420's 20% / 10% / fee formula on top of the underlying loss is one of the more patient-friendly first-party insurance remedies in the country. Reference the statute in every demand to a Missouri-licensed carrier, the 30-day clock alone moves a meaningful percentage of stalled claims.
2. **10-year SOL on written contracts** — tied for longest in the United States. The window cuts both ways (it also extends the hospital's collection window), so verify the dispute is genuinely live before invoking SOL as a defense. The long window is, however, a strong argument for early, definitive resolution rather than letting a bill drift.
3. **MMPA reach over original creditors with fee shift and punitives** — the hospital's in-house billing department can be liable for deceptive practices (misrepresenting amounts, misrepresenting in-network status, misrepresenting financial-assistance eligibility, billing for services not rendered, upcoding). Mention in any 30-day warning letter to a Missouri provider.
4. **Corporate-rep rule in small claims** — corporate defendants may appear through a non-attorney officer/employee, so a hospital is more likely to face the case with a billing-department staffer than with defense counsel, raising the economic leverage of a small-claims filing.
5. **§ 430.225 hospital lien is capped at 50% of net third-party recovery** — a meaningful patient protection when a hospital lien attaches to a personal-injury settlement. Always verify lien perfection (certified-mail notice with the required elements); imperfect liens are unenforceable.
