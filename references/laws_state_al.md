# Alabama state pack

The fully-worked state-law layer for Alabama patients. The LLM uses this when the patient's state is Alabama. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Two things shape Alabama's patient-side leverage:

1. The **common-law tort of first-party bad faith**, adopted by the Alabama Supreme Court in *Chavers v. National Security Fire & Casualty Co.* (1981) and tested through *Aetna Life Ins. Co. v. Lavoie*, 475 U.S. 813 (1986), is **the** doctrine to know. Punitive damages are available and have been substantial in reported cases. This is the lever against a fully-insured carrier that denies a legitimate medical claim.
2. The **hospital itemization right is request-based, not automatic** — written request triggers a 10-day delivery duty (within 30 days of discharge) or a 30-day delivery duty (after 30 days). Enforcement is by the Attorney General, not by a private right of action under the itemization statute itself. Patients have to lean on the Alabama Deceptive Trade Practices Act (Ala. Code § 8-19) for private enforcement against misleading billing practices.

Alabama has **no enacted state surprise-billing statute** for ground ambulance or otherwise; the federal No Surprises Act is primary. HB 469 (2025 regular session) was introduced to close the ground-ambulance gap but had not been enacted as of this writing. Verify current status before relying.

## Hospital itemization right

- **Statute:** **Ala. Code § 22-21-7** — Itemized statement of services rendered to be furnished patient upon request
- **Source:** [law.justia.com/codes/alabama/title-22/title-1/chapter-21/article-1/section-22-21-7](https://law.justia.com/codes/alabama/title-22/title-1/chapter-21/article-1/section-22-21-7/); statute text at [alisondb.legislature.state.al.us/alison/codeofalabama/1975/22-21-7.htm](http://alisondb.legislature.state.al.us/alison/codeofalabama/1975/22-21-7.htm)
- **What it requires:**
  - The patient (or survivor / legal guardian) must submit a **written request** for the itemized statement. The duty is not automatic — this is the structural difference from Georgia's § 10-1-393(b)(14).
  - If the request is made **within 30 days of discharge**, the hospital or nursing home has **10 days** from receipt of the request to deliver the itemized statement.
  - If the request is made **after 30 days of discharge**, the hospital has **30 days** to deliver.
  - The statement must itemize charges in language comprehensible to an ordinary layman, with the specific nature of services, expenses for each item of service, the constituent components within each hospital department, and unit-price data on rates charged.
- **Scope:** Any hospital in which human patients are given medical care, including emergency rooms and connected outpatient facilities. Nursing homes are explicitly covered.
- **Enforcement:** Section 22-21-7 vests enforcement in the **Alabama Attorney General** — the AG may bring an action against a hospital that fails to comply. There is **no express private right of action** under § 22-21-7 itself. Practical lever: send the written request, document the delay, then either (a) file a consumer complaint with the AG's Consumer Interest Division, or (b) plead a separate cause of action under the Alabama Deceptive Trade Practices Act (§ 8-19-5 / § 8-19-10) if the non-compliance is part of a deceptive billing practice.
- **ERISA:** Not preempted — regulates the provider, not the plan.

## Alabama Deceptive Trade Practices Act (private right of action)

- **Statute:** **Ala. Code §§ 8-19-1 through 8-19-15** — short title "Alabama Deceptive Trade Practices Act" (ADTPA). Listed unlawful practices at **§ 8-19-5**; private right of action at **§ 8-19-10**.
- **Source:** [law.justia.com/codes/alabama/title-8/chapter-19](https://law.justia.com/codes/alabama/title-8/chapter-19/); private right of action at [law.justia.com/codes/alabama/title-8/chapter-19/section-8-19-10](https://law.justia.com/codes/alabama/title-8/chapter-19/section-8-19-10/)
- **Substance of § 8-19-10:** A consumer injured by an unlawful trade practice may recover (i) **actual damages or $100, whichever is greater**, or (ii) up to **three times actual damages** at the court's discretion, plus (iii) **reasonable attorney's fees and costs** in any successful action. The treble multiplier is discretionary, not automatic.
- **Procedural requirement, settlement demand:** Before filing suit, the claimant must send a **written demand for relief** identifying the claimant and reasonably describing the unfair practice and the injury suffered. If the defendant makes a **written tender of settlement within 15 days** of the demand, and the court later finds the tender was sufficient to compensate actual damages, **no additional damages, fees, or costs are recoverable**. Frame any 30-day warning letter to include a specific dollar demand so this fee-shifting safe harbor is triggered cleanly.
- **Frivolous-action risk:** § 8-19-10(a)(3) — if the court finds the action was frivolous, brought in bad faith, or for harassment, **the defendant gets fees and costs**. This cuts both ways and is worth flagging in any patient-side decision to file.
- **Scope, original creditors:** ADTPA generally reaches sellers and lenders engaged in trade or commerce. Application to a hospital's in-house billing department is supported where billing conduct is itself deceptive (misrepresenting amounts owed, charging for services not rendered, asserting collectability on a time-barred or otherwise invalid debt). Alabama appellate authority is thinner than Georgia's FBPA case law on this exact application — frame the deception clearly.
- **Use:** This is the patient's principal private-action lever against deceptive billing practices in Alabama, parallel to Georgia's FBPA § 10-1-399. Lean on it explicitly in any 30-day warning letter to an AL provider.

## Insurance Trade Practices Act

- **Statute:** **Ala. Code §§ 27-12-1 through 27-12-24** — Trade Practices Law (Title 27, Chapter 12). General prohibition at **§ 27-12-2**; specific unfair practices in §§ 27-12-3 through 27-12-19; enforcement procedure at §§ 27-12-20 through 27-12-24.
- **Source:** [law.justia.com/codes/alabama/title-27/chapter-12](https://law.justia.com/codes/alabama/title-27/chapter-12/); list at [law.onecle.com/alabama/title-27/chapter-12](https://law.onecle.com/alabama/title-27/chapter-12/index.html)
- **Substance:** Defines and prohibits unfair methods of competition and unfair or deceptive acts in the business of insurance — misrepresentation, false advertising, defamation, boycott/coercion, false statements, unfair claims-settlement practices, etc. Modeled on the NAIC Unfair Trade Practices Model Act.
- **Critical caveat, no private right of action:** Title 27 Chapter 12 is **regulatory** — enforcement is by the **Alabama Commissioner of Insurance**, not by private litigants. Alabama appellate courts have consistently declined to imply a private right of action under the chapter. The Insurance Department processes a Trade Practices complaint, but it does not generate the patient's own cause of action.
- **Use:** Cite specific § 27-12 violations in your complaint to the Alabama Department of Insurance (below). Use the same violations as evidentiary support — not as standalone counts — in a common-law bad-faith claim (next section). Do not plead Chapter 27-12 as a freestanding count.

## Common-law first-party insurance bad faith

- **Doctrine:** Alabama recognizes the **intentional tort of bad faith refusal to pay a first-party insurance claim**, adopted by the Alabama Supreme Court in *Chavers v. National Security Fire & Casualty Co.*, 405 So. 2d 1 (Ala. 1981) and reaffirmed through *Aetna Life Ins. Co. v. Lavoie* (the 1986 case famous on the federal due-process side, but resting on Alabama's common-law bad-faith doctrine).
- **U.S. Supreme Court context:** *Aetna Life Ins. Co. v. Lavoie*, 475 U.S. 813 (1986) — [supreme.justia.com/cases/federal/us/475/813](https://supreme.justia.com/cases/federal/us/475/813/). The U.S. Supreme Court reversed a $3.5 million Alabama judgment on Fourteenth Amendment due-process grounds (a justice's recusal issue), **not** on the merits of the bad-faith doctrine. *Lavoie* is best understood as confirming that Alabama's common-law bad-faith tort exists and produces real verdicts, while signaling that punitive damages must be administered with constitutional care.
- **Elements (the "Chavers test"):**
  1. an insurance contract between the parties and a breach thereof by the defendant;
  2. an intentional refusal to pay the insured's claim;
  3. the absence of any reasonably legitimate or arguable reason for that refusal (the "debatable reason" standard);
  4. the insurer's actual knowledge of the absence of any legitimate or arguable reason;
  5. if the plaintiff relies on the insurer's intentional failure to investigate, the plaintiff must prove that intentional failure to determine whether a legitimate basis exists.
- **The "debatable reason" rule:** If the insurer has any reasonably arguable basis for denying the claim, there is **no bad faith as a matter of law**. This is a high bar — Alabama is plaintiff-friendly on remedies but plaintiff-strict on liability.
- **Damages:** Actual damages on the policy benefit plus **punitive damages**. Alabama's general cap (Ala. Code § 6-11-21) is the greater of three times compensatory damages or $1.5 million, **but** the cap does not apply to physical-injury cases and is adjusted; bad-faith verdicts have historically been very large. Compensatory damages may include emotional distress.
- **Demand mechanics:** No statutory pre-suit demand letter requirement exists for the common-law tort. Send one anyway — a clear, written, certified demand identifying the policy, the claim, the amount owed, and a payment deadline strengthens the record on the "actual knowledge of no debatable reason" element and helps anchor the punitive case.
- **ERISA preemption:** Common-law bad faith is **preempted** as applied to self-funded ERISA employer plans. *Pilot Life Ins. Co. v. Dedeaux*, 481 U.S. 41 (1987) — federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) fees, no state bad-faith tort. The doctrine is in play for fully-insured plans, Medicaid managed care, and individual/marketplace plans.
- **Third-party bad faith:** Alabama recognizes third-party bad-faith more narrowly (chiefly liability-insurance settlement context). For medical-billing disputes, the patient is the first-party insured; that is the relevant track.

## Surprise billing

- **State statute:** **None enacted.** Alabama has not passed a comprehensive state surprise-billing law analogous to Georgia's O.C.G.A. § 33-20E-1 et seq.
- **Pending legislation:** **HB 469** (2025 regular session, Rep. Oliver) — would prohibit balance billing by out-of-network ground ambulance providers and require insurers to pay the lesser of billed charges or 325% of the Medicare rate. Companion attempt SB 52 (2024 regular session) was indefinitely postponed. As of this writing, HB 469's enacted status is **not confirmed**. Verify at [trackbill.com/bill/alabama-house-bill-469](https://trackbill.com/bill/alabama-house-bill-469-ground-ambulance-services-prohibit-out-of-network-providers-from-balance-billing/2704283/) and [alison.legislature.state.al.us/files/pdf/SearchableInstruments/2025RS/HB469-int.pdf](https://alison.legislature.state.al.us/files/pdf/SearchableInstruments/2025RS/HB469-int.pdf) before relying.
- **Federal floor:** Federal **No Surprises Act** (Pub. L. 116-260, Title I of Division BB, effective Jan 1, 2022) is the primary protection in Alabama. It covers:
  - Emergency services from an out-of-network provider or facility (held to in-network cost-share);
  - Non-emergency services by an OON provider at an in-network facility (ancillary, anesthesia, radiology, pathology, lab);
  - **Air ambulance** (but not ground ambulance — that is the unclosed federal gap and exactly what HB 469 targets).
- **ALDOI guidance:** Alabama Department of Insurance NSA consumer page at [aldoi.gov/currentnewsitem.aspx?ID=1212](https://aldoi.gov/currentnewsitem.aspx?ID=1212) and [aldoi.gov/currentnewsitem.aspx?ID=1229](https://aldoi.gov/currentnewsitem.aspx?ID=1229). ALDOI accepts state-side complaints related to NSA compliance for state-regulated plans.
- **ERISA-preempted self-funded plans:** Federal NSA applies; state route is unavailable regardless.

## Regulatory agencies

### Alabama Department of Insurance (ALDOI)

- **Online complaint:** [aldoi.gov/consumers/filecomplaint.aspx](https://aldoi.gov/consumers/filecomplaint.aspx) (also at [insurance.alabama.gov/Consumers/FileComplaint.aspx](https://insurance.alabama.gov/Consumers/FileComplaint.aspx))
- **Phone:** main **(334) 241-4141** (business hours 8:00 a.m. – 5:00 p.m.); after-hours **(334) 240-4431**
- **Mail:**
  > Alabama Department of Insurance
  > Consumer Services Division
  > P.O. Box 303351
  > Montgomery, AL 36130-3351
- **Physical office:** 201 Monroe Street, Suite 502, Montgomery, AL 36104
- **Authority:** all insurance companies licensed in Alabama, including fully-insured health insurers, HMOs, PPOs, Medicare supplement. Administers the Insurance Trade Practices Act (§ 27-12) and federal NSA compliance for state-regulated plans. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and does not regulate hospitals, providers, or debt collectors (route to AG).

### Alabama Attorney General — Consumer Interest Division

- **Online complaint:** [alabamaag.gov/consumer-complaint](https://www.alabamaag.gov/consumer-complaint/)
- **Phone:** Consumer hotline **1-800-392-5658** (toll-free in AL) or **(334) 242-7335**
- **Mail:**
  > Office of the Attorney General
  > Consumer Interest Division
  > P.O. Box 300152
  > Montgomery, AL 36130
- **Physical office:** 501 Washington Avenue, Montgomery, AL 36104
- **Authority:** enforces the Alabama Deceptive Trade Practices Act (§ 8-19) and Ala. Code § 22-21-7 itemization duty against hospitals. Reach over providers, hospitals, third-party debt collectors. This is the right channel when the dispute is with the hospital's billing department or a collector, not with an insurer.

## Small claims court — District Court Small Claims Docket

- **Court name:** **District Court of [County]**, small claims docket (Alabama does not have a separately constituted "small claims court" — the small claims docket lives inside District Court)
- **Jurisdictional limit:** **$6,000**, codified at **Ala. Code § 12-12-31**
- **Source:** [law.justia.com/codes/alabama/title-12/chapter-12/article-2/section-12-12-31](https://law.justia.com/codes/alabama/title-12/chapter-12/article-2/section-12-12-31/); Alabama Judicial System guide at [judicial.alabama.gov/docs/library/docs/smguide.pdf](https://judicial.alabama.gov/docs/library/docs/smguide.pdf)
- **Filing fees (Ala. Code § 12-19-71, 2024-2025):**
  - Amount in controversy **$1,500 or less**: **$35**
  - Amount **over $1,500 up to $3,000**: **$109**
  - Amount **over $3,000 up to $6,000**: **$198** (small claims docket cap)
  - Above $6,000 the case goes on the regular District Court civil docket (up to $20,000) or Circuit Court
- **Attorney rules:** permitted, not required. Section 12-12-31 specifically permits any party, including an individual, partnership, **or corporation**, to appear with or without an attorney. This means the hospital may send a non-attorney billing-department employee — a real economic-leverage point for self-represented patients, similar to Georgia's Magistrate Court rule.
- **Jury trial:** not available on the small claims docket. Either party may appeal de novo to Circuit Court within 14 days under Ala. Code § 12-12-71 and demand a jury there.

## Statute of limitations

- **Written contracts:** **6 years from breach** — **Ala. Code § 6-2-34**
- **Oral contracts / open accounts:** **3 years from breach** — **Ala. Code § 6-2-38** (note: this is the principal caveat against the user-supplied outline, which guessed 6 years; oral contracts are materially shorter in Alabama)
- **Sale of goods (UCC):** 4 years — Ala. Code § 7-2-725
- **Contracts under seal:** 10 years — Ala. Code § 6-2-33 (specific formal-seal requirements)
- **Source:** § 6-2-34 at [law.justia.com/codes/alabama/title-6/chapter-2/article-2/section-6-2-34](https://law.justia.com/codes/alabama/title-6/chapter-2/article-2/section-6-2-34/); § 6-2-38 at [law.justia.com/codes/alabama/title-6/chapter-2/article-2/section-6-2-38](https://law.justia.com/codes/alabama/title-6/chapter-2/article-2/section-6-2-38/)

Most hospital admissions involve a signed financial-responsibility form — a written contract, so 6 years applies. Implied-in-fact medical-billing arrangements without a signed agreement may be treated as oral contracts or open accounts, in which case the 3-year limit governs. The clock runs from breach (typically the day payment was due and not made), not from discovery.

Partial payment or written acknowledgment of the debt can restart the clock under Alabama tolling rules. **Do not make a partial payment on a time-barred debt without legal advice.**

## Ground ambulance balance-billing

**Not covered by Alabama state law** as of this writing. Federal No Surprises Act explicitly excludes ground ambulance. HB 469 (2025 regular session) would close the gap by capping out-of-network ground-ambulance reimbursement at the lesser of billed charges or 325% of Medicare, with hold-harmless for the patient — verify enacted status before relying.

Until HB 469 (or a successor bill) is enacted, an Alabama patient facing an out-of-network ground-ambulance bill has:

- No state surprise-bill cap.
- No federal NSA protection for ground ambulance.
- Common-law contract defenses (UCC § 2-305 reasonable-price doctrine, unconscionability, no meeting of the minds where no price was disclosed pre-service).
- ADTPA (§ 8-19) if billing practices are themselves deceptive (e.g., misrepresenting in-network status of the ambulance provider).
- Insurance bad-faith common-law tort against the patient's own carrier if the carrier denies coverage in bad faith.

ERISA-preempted self-funded employer plans face the same federal NSA gap; air ambulance is covered by NSA; workers' comp, Medicare, Medicaid are separate regimes.

## Credit reporting

Alabama has **not** enacted a state-specific medical-debt credit-reporting restriction. Patients in Alabama rely on:

- The 2022-2023 voluntary changes by Equifax/Experian/TransUnion (paid medical debt removed; debt under $500 not reported; 1-year delay before reporting).
- Federal FCRA dispute rights (15 U.S.C. §§ 1681i, 1681s-2).

**Federal preemption posture is in flux.** The CFPB issued an October 2025 interpretive rule taking the position that the FCRA preempts state laws restricting medical-debt credit reporting. If that survives challenge, it limits any future Alabama state-level law on this front. Source: [consumerfinanceinsights.com/2025/11/02/cfpb-issues-rule-that-fcra-preempts-state-measures-barring-medical-debt](https://www.consumerfinanceinsights.com/2025/11/02/cfpb-issues-rule-that-fcra-preempts-state-measures-barring-medical-debt/).

For deceptive furnishing of medical-debt information to credit bureaus, ADTPA's general deceptive-practices provisions (§ 8-19-5) may apply, and the patient may have a federal FCRA claim against the furnisher.

## Hospital lien statute

- **Citations:** **Ala. Code §§ 35-11-370 through 35-11-377**
- **Sources:** § 35-11-370 at [codes.findlaw.com/al/title-35-property/al-code-sect-35-11-370](https://codes.findlaw.com/al/title-35-property/al-code-sect-35-11-370/); § 35-11-371 at [law.justia.com/codes/alabama/title-35/chapter-11/article-5/division-15/section-35-11-371](https://law.justia.com/codes/alabama/title-35/chapter-11/article-5/division-15/section-35-11-371/); practitioner overview at [cumberlandtrialjournal.com/2019/12/23/alabamas-amended-hospital-lien-laws](https://cumberlandtrialjournal.com/2019/12/23/alabamas-amended-hospital-lien-laws/)
- **Substance:** A hospital that treats a person injured by another's act or negligence within **one week of the injury** has a lien for reasonable and necessary charges, **but only against the patient's cause of action and any recovery from a third party** liable for the injury (e.g., the at-fault driver and that driver's insurer). **Not a lien on the patient's home, wages, or general bank accounts.**
- **Perfection requirements (§ 35-11-371):**
  - File a verified statement in the office of the **judge of probate of the county where the cause of action accrued**, **before or within 10 days of discharge** of the patient.
  - The verified statement must include the patient's name, address, dates of admission and discharge, amount claimed, and the names and addresses of all persons, firms, or corporations the hospital believes may be liable.
  - **Within one day** of filing, the hospital must mail a copy by **certified mail** to every named potentially liable party.
- **2019 amendment, insurance-first rule:** A hospital may **not** perfect a lien against a patient covered by a health-care payor until the hospital has submitted a properly coded claim to the payor and the claim has been denied. If the patient is covered by primary insurance, the hospital has 20 days after notice of denial to perfect; if the patient is uncovered or covered by a governmental payor (Medicare/Medicaid), the hospital has 20 days after discharge. **Always confirm the insurer-first step was completed** — if not, the lien is invalid and can be challenged.
- **Priority:** A properly perfected hospital lien sits ahead of all other liens against the third-party recovery **except an attorney's lien** (Ala. Code § 34-3-61), which has priority over the hospital.

## Hospital charity care

Alabama has **no state statute** requiring a comprehensive hospital financial-assistance policy beyond federal law. The closest provision is **Article 10A of Title 22, Chapter 21** (**Ala. Code § 22-21-300 et seq.**), which requires each hospital to **disclose** its financial-assistance policy: make written information available, include a statement on each bill that low-income patients may qualify, and post conspicuous signage in admission/registration areas. Source: [law.justia.com/codes/alabama/2017/title-22/title-1/chapter-21/article-10a/section-22-21-300](https://law.justia.com/codes/alabama/2017/title-22/title-1/chapter-21/article-10a/section-22-21-300/). The Article 10A duty is a **disclosure** duty, not a mandate to provide assistance at any particular level.

Non-profit hospitals are bound by **IRS § 501(r)** (federal): required FAP, required disclosure to the public, limits on extraordinary collection actions, capping amounts charged to FAP-eligible patients at amounts generally billed to insured patients. § 501(r) is the binding floor; Alabama does not exceed it.

For-profit hospitals and county/municipal hospitals have no state FAP mandate beyond § 22-21-300's disclosure rule.

Use Dollar For at [dollarfor.org/state_sheet/alabama](https://dollarfor.org/state_sheet/alabama/) for screening.

## Wage garnishment

- **Statute:** **Ala. Code § 5-19-15** (consumer credit transactions); general post-judgment garnishment at **Ala. Code §§ 6-6-370 through 6-6-460**.
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a court judgment. Post-judgment, garnishment is capped at the federal Consumer Credit Protection Act level — 25% of disposable earnings, or the amount by which weekly disposable earnings exceed 30× the federal minimum wage, whichever is less.
- **Use:** In response letters to collectors threatening garnishment without a judgment in hand.

## Quick reference for letter rendering

When the LLM renders an Alabama-bound letter, substitute these defaults:

- **State statute (itemization right):** **Ala. Code § 22-21-7** — request-based (not automatic); 10 days to deliver if requested within 30 days of discharge, 30 days to deliver if requested later. Pair the request with a notice that AG enforcement is available.
- **State insurance department (CC line):** Alabama Department of Insurance, Consumer Services Division, P.O. Box 303351, Montgomery, AL 36130-3351
- **State AG consumer protection (CC line):** Office of the Attorney General, Consumer Interest Division, P.O. Box 300152, Montgomery, AL 36130 ([alabamaag.gov/consumer-complaint](https://www.alabamaag.gov/consumer-complaint/))
- **Small-claims court name:** **District Court of [county], Small Claims Docket**
- **Filing fee (in 30-day warning):** "$35 for claims ≤ $1,500, $109 for $1,500–$3,000, $198 for $3,000–$6,000 (Ala. Code § 12-19-71)"
- **Statute of limitations (in 30-day warning):** "Ala. Code § 6-2-34 (six years for breach of written contract); Ala. Code § 6-2-38 (three years for oral / open account)"
- **For ground ambulance balance bills:** **No state-law protection** as of this writing. Cite federal NSA (limited — air ambulance only), common-law unconscionability, ADTPA § 8-19, and (against insurer) the *Chavers* bad-faith tort. Note HB 469 (2025) as pending if applicable.
- **For provider-side disputes (vs. insurer-side):** Cite **Ala. Code § 8-19-10** (ADTPA private right of action with attorney's fees) in addition to UCC § 2-305 reasonable-price doctrine. Include a written demand for relief with a specific dollar amount so the 15-day settlement-tender mechanism in § 8-19-10 is triggered cleanly.
- **For insurer-side disputes (fully-insured plans):** Lead with **common-law bad faith under *Chavers v. National Security Fire & Casualty Co.* (Ala. 1981)** and *Aetna Life Ins. Co. v. Lavoie*, 475 U.S. 813 (1986). Note that punitive damages are available. Send a written, certified demand identifying the policy, claim, amount, and a payment deadline to anchor the "actual knowledge of no debatable reason" element.

## Key Alabama-specific advantages

Worth keeping in mind when triaging an AL patient's bills:

1. **Common-law bad faith with punitive damages** — Alabama's *Chavers* doctrine is one of the more developed first-party bad-faith regimes in the country. For a fully-insured patient whose carrier denies a clearly-covered medical claim without an arguable basis, this is the lever, and verdicts have historically been substantial. ERISA-preempted for self-funded employer plans.
2. **ADTPA fee-shifting** — § 8-19-10 makes attorney's-fee recovery realistic against a hospital or other provider engaged in deceptive billing. Always pair the ADTPA demand with a written tender-triggering dollar figure so the 15-day safe harbor is invoked on your terms.
3. **AG enforcement of § 22-21-7** — the Attorney General can sue a non-compliant hospital. Even without a private right of action under the itemization statute itself, a credible AG-complaint threat plus an ADTPA private-action threat is real leverage.
4. **District Court non-attorney rule** — corporate defendants can appear without a lawyer on the small claims docket. Same dynamic as Georgia's Magistrate Court: the patient is more likely to face a billing-department staffer than a defense attorney, which raises the economic leverage in small-claims posture.
5. **Hospital-lien insurance-first rule (2019 amendment)** — § 35-11-371 now requires the hospital to submit the claim to the patient's health-care payor and have it denied before perfecting a lien. Always verify this step was completed; a defective lien can be challenged and removed.

## What Alabama does **not** have (vs. Georgia)

For accurate triage, the lever-gaps matter as much as the levers:

- **No automatic itemization duty.** Alabama is request-based, not the six-business-day automatic rule Georgia uses.
- **No comprehensive state surprise-billing act.** Alabama relies on the federal NSA, with HB 469 (2025) still pending on the ground-ambulance gap.
- **No state ground-ambulance balance-billing protection.** Patients are exposed to the federal NSA gap with no state backstop.
- **No statutory § 33-4-6-style bad-faith penalty.** Alabama's bad-faith remedy is common-law (broader on damages, but no fixed 60-day-demand statutory penalty structure).
- **No state medical-debt credit-reporting law.**
- **Smaller small-claims limit, $6,000 vs. Georgia's $15,000** — many medical-bill disputes will exceed the Alabama cap and need the regular District Court civil docket ($20,000) or Circuit Court.
