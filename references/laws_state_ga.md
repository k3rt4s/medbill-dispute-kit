# Georgia state pack

The fully-worked state-law layer for Georgia patients. The LLM uses this when the patient's state is Georgia. Tennessee equivalent at [`laws_state_tn.md`](laws_state_tn.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Two things make Georgia's patient-side leverage unusually strong:

1. The **hospital itemization duty is automatic** — six business days from inpatient discharge, no written request required — and it lives in the Fair Business Practices Act with a **private right of action**.
2. The **Surprise Billing Consumer Protection Act covers ground ambulance** (effective Jan 1, 2024 via HB 286), which the federal No Surprises Act does not. This closes the single biggest balance-billing gap in federal law.

## Hospital itemization right

- **Statute:** **O.C.G.A. § 10-1-393(b)(14)** — part of the Georgia Fair Business Practices Act (FBPA), O.C.G.A. § 10-1-390 et seq.
- **Source:** [law.justia.com/codes/georgia/title-10/chapter-1/article-15/part-2/section-10-1-393](https://law.justia.com/codes/georgia/title-10/chapter-1/article-15/part-2/section-10-1-393/); consumer summary at [consumer.georgia.gov/consumer-topics/hospital-billing-practices](https://consumer.georgia.gov/consumer-topics/hospital-billing-practices)
- **What it requires:**
  - Within **six (6) business days** of an inpatient discharge, the hospital or long-term care facility must deliver an itemized statement of all charges for which the patient or third-party payor is being billed.
  - The duty is **automatic** — no written request is required. Sending a written request anyway creates a useful paper trail.
- **Scope:** Inpatient discharges from a hospital or long-term care facility. Outpatient, ER-only, and ambulatory-surgery visits are not directly covered by this subsection (general FBPA prohibitions still apply).
- **Private right of action:** Yes, under O.C.G.A. § 10-1-399 (see below). Actual damages, treble damages for intentional violations, plus attorney's fees, but only after a 30-day ante-litem demand.
- **ERISA:** Not preempted — regulates the provider, not the plan.

## FBPA private right of action

- **Statute:** **O.C.G.A. § 10-1-399**
- **Substance:** A patient injured by an unfair-or-deceptive practice (including § 10-1-393(b)(14), billing for services never rendered, upcoding, misrepresenting in-network status) may recover **actual damages, treble damages for intentional violations, and reasonable attorney's fees**.
- **Procedural requirement:** Send a written ante-litem demand at least **30 days before filing suit** by registered/certified mail or statutory overnight delivery, identifying the unfair practice and the relief sought.
- **Why it matters:** Georgia's FBPA reaches **original creditors** (the hospital itself), not just third-party debt collectors. This is broader than the federal FDCPA and is a meaningful Georgia-specific lever against the hospital's in-house billing department.

## Unfair Claims Settlement Practices Act

- **Statute:** **O.C.G.A. § 33-6-30 et seq.** (UCSPA Article); listed practices at **§ 33-6-34**; no-private-action bar at **§ 33-6-37**
- **Source:** [law.justia.com/codes/georgia/2010/title-33/chapter-6/article-2/](https://law.justia.com/codes/georgia/2010/title-33/chapter-6/article-2/); implementing regulations at [rules.sos.ga.gov/gac/120-2-20](https://rules.sos.ga.gov/gac/120-2-20)
- **Substance:** Prohibits insurers from engaging in a defined list of unfair claims-settlement practices — misrepresenting policy provisions, failing to acknowledge claims promptly, denying without a reasonable investigation, etc.
- **Critical caveat:** **No private right of action.** Section 33-6-37 expressly states: "Nothing contained in this article shall be construed to create or imply a private cause of action for a violation of this article." Enforcement is by the Georgia Commissioner of Insurance only. Federal and state courts have repeatedly dismissed UCSPA claims brought by insureds.
- **Use:** Cite UCSPA violations in your complaint to the OCI (see below) and as evidentiary support for a § 33-4-6 bad-faith claim. Do not plead UCSPA as a standalone count in litigation.

## Bad-faith failure to pay

- **Statute:** **O.C.G.A. § 33-4-6** (first-party insurance bad-faith)
- **Source:** [law.justia.com/codes/georgia/title-33/chapter-4/section-33-4-6](https://law.justia.com/codes/georgia/title-33/chapter-4/section-33-4-6/)
- **Substance:** Three elements: (1) a loss covered by a policy of insurance; (2) the insurer refuses to pay within **60 days after written demand** by the policyholder; (3) the refusal was in bad faith (a "frivolous and unfounded refusal"). Damages: the underlying loss, plus a statutory penalty of **up to 50% of the insurer's liability for the loss, or $5,000, whichever is greater**, plus reasonable attorney's fees.
- **Procedural requirements:**
  - Send the demand in writing by certified mail, identifying (i) the policy, (ii) the loss, and (iii) the demand for payment.
  - Wait 60 days; payment within 60 days defeats the bad-faith claim entirely. Payment after day 60 does **not** abate the action.
  - Plaintiff must serve the Commissioner of Insurance and the Consumers' Insurance Advocate with notice of the action (procedural step in the statute).
- **Coverage:** "Any policy of insurance" — including health insurance (accident and sickness). First-party only; third-party motor-vehicle claims use § 33-4-7.
- **ERISA preemption:** § 33-4-6 is **preempted** as applied to self-funded ERISA employer plans. For ERISA self-funded plans, the federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) attorney's fees — no state bad-faith penalty. The statute is in play for fully-insured plans, Medicaid managed care, and individual/marketplace plans.
- **Bad faith standard:** Requires more than negligence or honest mistake. Courts require a "frivolous and unfounded" refusal or conscious disregard.

## Surprise Billing Consumer Protection Act

- **Statute:** **O.C.G.A. § 33-20E-1 et seq.** — Georgia Surprise Billing Consumer Protection Act
- **Original enactment:** HB 888 (2020), effective January 1, 2021
- **Expansion:** **HB 286 (2023), effective January 1, 2024**, added ground ambulance coverage
- **Implementing regulations:** Ga. Comp. R. & Regs. Ch. **120-2-106**
- **Sources:** [law.justia.com/codes/georgia/title-33/chapter-20e](https://law.justia.com/codes/georgia/title-33/chapter-20e/); [rules.sos.ga.gov/gac/120-2-106](https://rules.sos.ga.gov/gac/120-2-106); consumer summary at [georgiawatch.org/what-georgia-consumers-should-know-about-state-and-federal-protections-against-surprise-medical-bills](https://georgiawatch.org/what-georgia-consumers-should-know-about-state-and-federal-protections-against-surprise-medical-bills/)

### What it prohibits

- Balance billing for **emergency services** from an out-of-network (OON) provider or facility.
- Balance billing for **non-emergency services** rendered by an OON provider at an **in-network** facility (ancillary services — anesthesia, radiology, pathology, lab, etc.).
- Balance billing for **ground ambulance** from an OON provider (since Jan 1, 2024).
- Patient cost-sharing is capped at the in-network amount and counts toward the in-network deductible and out-of-pocket maximum.

### Where Georgia goes beyond the federal No Surprises Act

- Covers a broader set of facilities: birthing centers, hospices, and diagnostic/treatment centers explicitly included.
- Extends to mental-health emergencies treated outside hospitals.
- **Covers ground ambulance** — the federal NSA does not. Insurer pays the provider the greater of (i) the negotiated rate with participating providers, (ii) the usual and customary rate, or (iii) **180% of the Medicare rate**. The patient is held harmless from any rate dispute.
- State-administered baseball-style arbitration under § 33-20E-9 for provider-payer rate disputes; the patient is not a party.

### Caveats

- **ERISA preemption:** the Act does not reach self-funded ERISA employer plans. Those are covered (if at all) only by the federal NSA.
- Excludes air ambulance (federal NSA covers it), workers' compensation, Medicare, and Medicaid.
- Only applies to plans regulated by Georgia (fully insured); pre-2024 policies are not retroactively covered for ground ambulance.
- Patients should receive both state-law and federal NSA disclosures from providers; protections layer rather than displace.

## Regulatory agencies

### Office of the Commissioner of Insurance and Safety Fire (OCI / Georgia Department of Insurance)

- **Online complaint:** [oci.georgia.gov/file-consumer-insurance-complaint](https://oci.georgia.gov/file-consumer-insurance-complaint) (direct portal at [ociapp.oci.ga.gov/ConsumerService/Complaint.aspx](https://ociapp.oci.ga.gov/ConsumerService/Complaint.aspx))
- **Phone:** main **(404) 656-2070**; toll-free Consumer Services **1-800-656-2298**
- **Mail:**
  > Office of Commissioner of Insurance and Safety Fire
  > Consumer Services Division
  > 2 Martin Luther King, Jr. Drive
  > West Tower, Suite 716
  > Atlanta, GA 30334
- **Authority:** all insurance companies licensed in Georgia, including fully-insured health insurers, HMOs, PPOs, Medicare supplement. Administers the Surprise Billing Consumer Protection Act and UCSPA. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and does not regulate providers, hospitals, or debt collectors (route to AG).

### Georgia Attorney General — Consumer Protection Division

- **Online complaint:** [consumer.georgia.gov/resolve-your-dispute/how-do-i-file-complaint](https://consumer.georgia.gov/resolve-your-dispute/how-do-i-file-complaint)
- **Phone:** main **(404) 651-8600**; toll-free in Georgia **1-800-869-1123**
- **Authority:** enforces the FBPA, including § 10-1-393(b)(14) hospital itemization, and Georgia's debt-collection consumer-protection rules. Reach over providers, hospitals, third-party debt collectors, **and original creditors** — exactly the gap not covered by OCI. Useful when the dispute is with the hospital's in-house billing department.

## Small claims court — Magistrate Court

- **Court name:** **Magistrate Court** (one per county; Georgia does not have a separately named "small claims court")
- **Jurisdictional limit:** **$15,000**, codified at **O.C.G.A. § 15-10-2(5)**
- **Source:** [law.justia.com/codes/georgia/title-15/chapter-10/article-1/section-15-10-2](https://law.justia.com/codes/georgia/title-15/chapter-10/article-1/section-15-10-2/)
- **Filing fees:** typical 2024-2025 ranges $45-$105 initial filing including service on one defendant, $25-$50 per additional defendant. Varies by county.
- **Attorney rules:** permitted, not required. Designed for pro se litigants — simplified pleadings, limited formal discovery, relaxed evidence rules. Corporations and LLCs may appear through a non-attorney officer or employee under O.C.G.A. § 15-10-23 (Georgia-specific advantage for self-represented parties).
- **Jury trial:** not available in Magistrate Court. Either party may demand a jury by appealing de novo to State or Superior Court within 30 days (O.C.G.A. § 15-10-41).

**Heads up:** HB 792 (2025-2026 session) was introduced to raise the limit to $30,000 but had not been enacted as of this writing. Use $15,000 in dispute letters; check enactment status before filing if your dispute is between $15k and $30k.

## Statute of limitations

- **Written contracts:** **6 years from breach** — O.C.G.A. § 9-3-24
- **Oral contracts / open accounts:** **4 years from breach** — O.C.G.A. § 9-3-26 (oral) / § 9-3-25 (open account)
- **Contracts under seal:** 20 years — O.C.G.A. § 9-3-23 (rare; specific formal-seal requirements)
- **Source:** [law.justia.com/codes/georgia/2020/title-9/chapter-3/article-2/section-9-3-24](https://law.justia.com/codes/georgia/2020/title-9/chapter-3/article-2/section-9-3-24/); [law.justia.com/codes/georgia/title-9/chapter-3/article-2/section-9-3-26](https://law.justia.com/codes/georgia/title-9/chapter-3/article-2/section-9-3-26/)

Most hospital admissions involve a signed financial-responsibility form — a written contract, so 6 years applies. Implied-in-fact medical-billing arrangements without a signed agreement may be treated as open accounts or oral contracts (4 years). The clock runs from breach (typically the day payment was due and not made), not from when damages are discovered.

Partial payment or written acknowledgment of the debt can restart or extend the clock (O.C.G.A. § 9-3-110, 9-3-112). **Do not make a partial payment on a time-barred debt without legal advice.**

## Ground ambulance balance-billing

**Covered by Georgia state law as of January 1, 2024**, via O.C.G.A. § 33-20E-1 et seq. as amended by HB 286 (2023). See "Surprise Billing Consumer Protection Act" above.

For policies issued, delivered, or renewed in Georgia on or after January 1, 2024, an insured patient receiving ground ambulance from an out-of-network provider may be billed no more than the in-network cost-share. This is the single most important Georgia-specific protection because the **federal No Surprises Act explicitly excludes ground ambulance** — Georgia is one of the states that closes the gap.

ERISA-preempted for self-funded employer plans; excludes air ambulance, workers' comp, Medicare, Medicaid.

## Credit reporting

Georgia has not enacted a state-specific medical-debt credit-reporting restriction. HB 765 ("Medical Debt Protection Act," 2025-2026 session) would have, but had not been enacted as of this writing. Patients in Georgia rely on:

- The 2022-2023 voluntary changes by Equifax/Experian/TransUnion (paid medical debt removed; debt under $500 not reported; 1-year delay before reporting)
- Federal FCRA dispute rights (15 U.S.C. §§ 1681i, 1681s-2)

**Federal preemption posture is in flux.** The CFPB issued an October 2025 interpretive rule taking the position that the FCRA preempts state laws restricting medical-debt credit reporting. If that survives challenge, it limits the effect of any state-level law Georgia might pass.

For deceptive furnishing of medical-debt information to credit bureaus, the FBPA's general deceptive-practices provisions may apply via § 10-1-393(b), and the patient may have a federal FCRA claim against the furnisher.

## Hospital lien statute

- **Citations:** **O.C.G.A. §§ 44-14-470 through 44-14-477**
- **Sources:** [law.justia.com/codes/georgia/title-44/chapter-14/article-8/part-8/section-44-14-470](https://law.justia.com/codes/georgia/title-44/chapter-14/article-8/part-8/section-44-14-470/); [law.justia.com/codes/georgia/title-44/chapter-14/article-8/part-8/section-44-14-471](https://law.justia.com/codes/georgia/title-44/chapter-14/article-8/part-8/section-44-14-471/)
- **Substance:** Hospitals, nursing homes, physician practices, chiropractic practices, and traumatic burn-care practices may file a lien for reasonable charges, **only against the patient's cause of action against a third party** who caused the injury (e.g., the at-fault driver in a car wreck). **Not a lien on the patient's home, wages, or bank accounts.**
- **Perfection requirements:**
  - At least 15 days' written notice by certified mail to the patient and to all known liable parties and their insurers before filing.
  - File the verified statement within **75 days after discharge** (hospitals, nursing homes, burn care) or **90 days after first treatment** (physician/chiropractic practices).
- **2023 amendment:** under § 44-14-471(c), the provider must first submit the bill to the patient's health insurer and have the claim rejected before any lien is enforceable. **Always confirm this insurer-first step was attempted** — failure to do so invalidates the lien.

## Hospital charity care

Georgia has **no state statute** requiring a hospital financial-assistance policy beyond federal law. Non-profit hospitals are bound by IRS § 501(r) (federal); for-profit and county/municipal hospitals have no state FAP mandate.

Hospitals receiving funds from Georgia's **Indigent Care Trust Fund** (O.C.G.A. § 31-8-150 et seq.) have additional obligations to serve indigent patients; cite ICTF participation in a dispute letter where applicable. Source: [dch.georgia.gov/providers/provider-types/hospital-providers/indigent-care-trust-fund](https://dch.georgia.gov/providers/provider-types/hospital-providers/indigent-care-trust-fund).

Use Dollar For at [dollarfor.org/state_sheet/georgia](https://dollarfor.org/state_sheet/georgia/) for screening.

## Wage garnishment

- **Statute:** **O.C.G.A. § 18-4-5** (tracks federal Consumer Credit Protection Act)
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a court judgment. Post-judgment, garnishment is capped at the federal 25% of disposable earnings (or the amount by which weekly disposable earnings exceed 30× the federal minimum wage, whichever is less).
- **Use:** In response letters to collectors threatening garnishment without a judgment in hand.

## Quick reference for letter rendering

When the LLM renders a Georgia-bound letter, substitute these defaults:

- **State statute (itemization right):** **O.C.G.A. § 10-1-393(b)(14)** — automatic 6 business days after inpatient discharge, no request required. The dispute language can either (a) note non-compliance with the automatic duty, or (b) make a written request anyway to crystallize the paper trail.
- **State insurance department (CC line):** Office of Commissioner of Insurance and Safety Fire, Consumer Services Division, 2 Martin Luther King, Jr. Drive, West Tower, Suite 716, Atlanta, GA 30334
- **State AG consumer protection (CC line):** Georgia Attorney General, Consumer Protection Division, 2 Martin Luther King, Jr. Drive, Atlanta, GA 30334 ([consumer.georgia.gov](https://consumer.georgia.gov))
- **Small-claims court name:** **Magistrate Court of [county]**
- **Filing fee (in 30-day warning):** "$45-$105 depending on county"
- **Statute of limitations (in 30-day warning):** "O.C.G.A. § 9-3-24 (six years for breach of written contract)"
- **For ground ambulance balance bills:** Cite O.C.G.A. § 33-20E-1 et seq. as amended by HB 286 (effective Jan 1, 2024). This is the single highest-leverage Georgia-specific cite when applicable.
- **For provider-side disputes (vs. insurer-side):** Cite **O.C.G.A. § 10-1-399** (FBPA private right of action with attorney's fees) in addition to UCC § 2-305. The 30-day ante-litem demand requirement is satisfied by the kit's standard 30-day warning letter, provided the letter is sent certified.

## Key Georgia-specific advantages

Worth keeping in mind when triaging a GA patient's bills:

1. **Original-creditor reach** — FBPA reaches the hospital itself, not just third-party collectors. The hospital's in-house billing department can be liable for deceptive practices (misrepresenting amounts, threatening lawsuits without intent, contacting at prohibited hours).
2. **Attorney's fees recovery** — FBPA § 10-1-399 makes fee recovery realistic for a successful patient. Mention in any 30-day warning letter to GA providers.
3. **Ground ambulance** — Georgia is one of the states that closed the federal NSA's biggest gap. Always check whether a ground-ambulance bill post-dates Jan 1, 2024.
4. **Magistrate Court non-attorney rule** — corporate defendants can appear through a non-lawyer employee, which means the patient is more likely to face a billing-department staffer than a defense attorney. The economic leverage in small claims is even higher in GA than elsewhere because the corporate side knows it doesn't get to bring expensive counsel.
