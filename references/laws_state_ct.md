# Connecticut state pack

The fully-worked state-law layer for Connecticut patients. The LLM uses this when the patient's state is Connecticut. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md), Tennessee at [`laws_state_tn.md`](laws_state_tn.md). All citations verified against public sources as of 2026-05-19. Re-verify annually.

Three things make Connecticut's patient-side leverage unusually strong:

1. The **Medical Debt Reform Act (Public Act 24-6, effective July 1, 2024)** voids any medical debt reported to a credit rating agency by a provider, hospital, or collection entity. This is one of the strongest state-level credit-reporting protections in the country.
2. **CUTPA via CUIPA** (Mead v. Burns doctrine) gives patients a private cause of action for unfair insurance settlement practices with **punitive damages, attorney's fees, and class-action standing** — a remedy the Georgia UCSPA explicitly forecloses.
3. The **hospital-side collection statute (PA 21-129, eff. Oct 1, 2022)** caps interest on hospital debt at **5% per year**, blocks foreclosure on the patient's primary residence, and blocks wage garnishment for any patient eligible for the hospital's bed fund.

The single notable Connecticut weakness, relative to states like Georgia: **the state Surprise Billing law explicitly excludes ground ambulance.** Connecticut patients hit by an out-of-network ground-ambulance bill have no state-law balance-bill cap; federal NSA does not cover ground ambulance either, leaving a gap.

## Hospital itemization right

- **Statute:** **Conn. Gen. Stat. § 19a-509** (formerly § 19-590a) — Hospital and nursing home admission forms. Hospital bills.
- **Source:** [law.justia.com/codes/connecticut/title-19a/chapter-368v/section-19a-509-formerly-sec-19-590a](https://law.justia.com/codes/connecticut/title-19a/chapter-368v/section-19a-509-formerly-sec-19-590a/); CT Office of Health Strategy consumer summary at [portal.ct.gov/ohs/knowledge-base/articles/file-or-find-data/consumer-assistance-process/detailed-hospital-bills](https://portal.ct.gov/ohs/knowledge-base/articles/file-or-find-data/consumer-assistance-process/detailed-hospital-bills)
- **What it requires:**
  - Upon written request by a self-pay patient, the hospital must provide an itemized bill **within 30 days** of the request.
  - The itemized bill must identify, **in plain language**, each individual service, supply, or medication and the specific charge for each.
  - All hospital admission forms must include a conspicuous notice that a self-pay patient may request an itemized bill, and must specify the name and contact information of a person to contact.
- **Scope:** Statute is written around self-pay patients, but in practice any patient can invoke it. For insured patients, federal Hospital Price Transparency rules (45 C.F.R. Part 180) and HIPAA right-of-access (45 C.F.R. § 164.524) provide parallel itemization paths.
- **Trigger:** Unlike Georgia (where the duty is automatic on inpatient discharge), Connecticut's right is **request-driven** — send a written request to start the 30-day clock.
- **Private right of action:** No express PRA in the statute itself. Enforcement is by the Office of Health Strategy. However, a hospital's refusal to provide an itemized bill in the face of a written request, particularly while continuing to attempt collection, may constitute an unfair or deceptive practice actionable under **CUTPA § 42-110b** (see below).
- **ERISA:** Not preempted — regulates the provider, not the plan.

> Note on § 19a-508c: this is the **facility-fee disclosure** statute (notice that outpatient services at hospital-based facilities may carry a separate facility fee), not the itemization statute. Cite § 19a-508c when disputing an undisclosed facility fee, cite § 19a-509 when requesting the itemized bill itself.

## Connecticut Unfair Trade Practices Act (CUTPA)

- **Statute:** **Conn. Gen. Stat. § 42-110a et seq.**; private action and remedies at **§ 42-110g**
- **Source:** [law.justia.com/codes/connecticut/title-42/chapter-735a/section-42-110g](https://law.justia.com/codes/connecticut/title-42/chapter-735a/section-42-110g/); practitioner overview at [halloransage.com/publication/what-you-need-to-know-about-the-connecticut-unfair-trade-practices-act-cutpa](https://halloransage.com/publication/what-you-need-to-know-about-the-connecticut-unfair-trade-practices-act-cutpa/)
- **Substance:** Section 42-110b prohibits "unfair methods of competition and unfair or deceptive acts or practices in the conduct of any trade or commerce." This reaches hospitals, physician practices, and third-party collection agents acting in their billing capacity.
- **Remedies under § 42-110g:**
  - **Actual damages** — including the disputed billed amount.
  - **Punitive damages** in the court's discretion, on a showing of reckless indifference or intentional/wanton violation of the plaintiff's rights. No statutory cap; Connecticut courts have awarded multiples of compensatory damages where conduct warrants.
  - **Reasonable attorney's fees and costs** to a prevailing plaintiff.
  - **Class actions** — § 42-110g(b) expressly authorizes class actions, attorneys' fees, and costs for class counsel.
  - **Injunctive and other equitable relief** in the court's discretion.
- **Procedural requirements:**
  - Pre-suit demand is **not** required by statute (unlike Georgia's FBPA 30-day ante-litem). The kit's standard 30-day warning letter is good practice and creates the evidentiary record of reckless indifference needed for punitives.
  - Plaintiff must mail a copy of the complaint to the **Attorney General and the Commissioner of Consumer Protection** on the date suit is filed (§ 42-110g(c)).
  - Statute of limitations: **3 years** from the act complained of — § 42-110g(f).
- **Why it matters:** CUTPA reaches **original creditors** (the hospital and its in-house billing department), not just third-party debt collectors. This closes the same gap the federal FDCPA leaves open.

## Connecticut Unfair Insurance Practices Act (CUIPA) — accessed via CUTPA

- **Statute:** **Conn. Gen. Stat. § 38a-815 et seq.** (CUIPA); listed unfair practices at **§ 38a-816**
- **Source:** [Connecticut Insurance Department](https://portal.ct.gov/cid); CUIPA/CUTPA interplay treatment in *State v. Acordia, Inc.*, 310 Conn. 1 (2013), and *Mead v. Burns*, 199 Conn. 651 (1986)
- **Substance:** Prohibits insurers from engaging in unfair claim-settlement practices — misrepresenting policy provisions, failing to acknowledge claims promptly, refusing to pay claims without conducting a reasonable investigation, compelling insureds to litigate by offering substantially less than amounts ultimately recovered, etc.
- **No standalone private right of action.** CUIPA itself is enforced administratively by the Insurance Commissioner. Connecticut courts have repeatedly dismissed direct CUIPA claims.
- **The CUTPA workaround (Mead v. Burns / Acordia framework):**
  - A patient may bring a **CUTPA claim predicated on a CUIPA violation**. This is the only available common-law route for unfair-claims-settlement damages against an insurer in Connecticut.
  - The plaintiff must plead and prove the unfair acts occurred with **such frequency as to indicate a general business practice** — a single act of misconduct is insufficient. *Mead v. Burns*, 199 Conn. 651.
  - After *Acordia* (2013), insurance-related CUTPA claims must be based on a CUIPA violation or another insurance-specific statute. There is no "freestanding" CUTPA claim against an insurer for insurance-related conduct.
- **Use in dispute letters:** Cite both § 38a-816 (the specific unfair practice) and § 42-110b (the CUTPA hook). The "general business practice" element is typically established by other claimants' patterns documented in CID enforcement actions or news coverage.

## Bad-faith failure to pay

- **Common-law doctrine:** Implied covenant of good faith and fair dealing in every insurance contract; tortious bad faith available where an insurer unreasonably and in bad faith withholds payment.
- **Anchor case:** ***Buckman v. People Express, Inc.***, 205 Conn. 166, 530 A.2d 596 (1987) — Connecticut Supreme Court's definition: bad faith "implies the conscious doing of a wrong because of dishonest purpose or moral obliquity ... a state of mind affirmatively operating with furtive design or ill will."
- **Source:** *Buckman v. People Express* opinion via Justia; treatment at [chartwelllaw.com/bad-faith-claims-map/connecticut](https://www.chartwelllaw.com/bad-faith-claims-map/connecticut) and [alfainternational.com/compendium/insurance-law/connecticut](https://www.alfainternational.com/compendium/insurance-law/connecticut/)
- **Double-pronged framework:** Connecticut bad-faith litigation typically pleads two counts:
  1. **Common-law bad faith** — tort claim under Buckman. Requires more than negligence or honest mistake. Damages: contract damages plus consequential, with punitive damages available under common-law standards (typically capped at attorney's fees and costs, *not* a separate multiplier).
  2. **CUTPA-via-CUIPA** — statutory claim per Mead v. Burns. Adds the statutory punitive-damages discretion and attorney's-fee shifting of § 42-110g.
- **No 60-day pre-suit demand** equivalent to Georgia's § 33-4-6 — Connecticut bad faith is a pure common-law cause of action with no statutory waiting period. The kit's 30-day warning letter remains good practice for evidentiary purposes.
- **ERISA preemption:** Both prongs are **preempted** as applied to self-funded ERISA employer plans. For self-funded plans, the federal remedy is 29 U.S.C. § 1132(a)(1)(B). The state-law claims are in play for fully-insured plans, Medicaid managed care, and individual/marketplace plans.
- **Bad faith standard:** Connecticut requires "dishonest purpose or moral obliquity" — a high bar. Honest mistake, even unreasonable mistake, is not enough.

## Surprise Billing — Connecticut No Surprises Act

- **Statute:** **Conn. Gen. Stat. § 38a-477aa** — Cost-sharing and health care provider reimbursements for emergency services, urgent crisis center services and surprise bills
- **Original enactment:** Public Act 15-146, effective July 1, 2016 (Connecticut was one of the earliest state surprise-billing laws, predating the federal NSA by six years)
- **Subsequent amendments:** PA 22-47 added urgent crisis center services and refined the surprise-bill definition (effective Jan 1, 2023)
- **Source:** [law.justia.com/codes/connecticut/title-38a/chapter-700c/section-38a-477aa](https://law.justia.com/codes/connecticut/title-38a/chapter-700c/section-38a-477aa/); Connecticut Insurance Department summary at [portal.ct.gov/cid/knowledge-base/articles/no-surprise-act](https://portal.ct.gov/cid/knowledge-base/articles/no-surprise-act); OLR report at [cga.ct.gov/2022/rpt/pdf/2022-R-0012.pdf](https://cga.ct.gov/2022/rpt/pdf/2022-R-0012.pdf)

### What it prohibits

- Balance billing for **emergency services** rendered by an out-of-network (OON) provider — patient pays only in-network cost-sharing.
- Balance billing for **non-emergency services** rendered by an OON provider at an **in-network** facility (ancillary services — anesthesia, radiology, pathology, lab, etc.).
- Balance billing for **air ambulance services** by non-participating providers.
- Patient cost-sharing is capped at the in-network amount and counts toward the in-network deductible and out-of-pocket maximum.

### Where Connecticut's law sits relative to the federal No Surprises Act

- Connecticut's law predates and largely parallels the federal NSA for fully-insured plans regulated by Connecticut.
- For services not clearly within the federal NSA, the Connecticut law may still apply (state-regulated plans).
- The federal NSA covers self-funded ERISA plans, where the Connecticut statute does not.

### Critical caveat — ground ambulance is NOT covered

**Conn. Gen. Stat. § 38a-477aa expressly excludes ground ambulance services** from its definition of "health care provider" — § 38a-477aa, read with § 20-7f, excludes individuals licensed under chapters 368d and 384d (ambulance services, EMTs, paramedics). The statute instead established an advisory committee to study the issue. As of this writing, no Connecticut statute caps ground-ambulance balance bills for OON services.

Combined with the federal NSA's exclusion of ground ambulance, Connecticut patients hit by an OON ground-ambulance bill have **no balance-bill cap** under either state or federal law. This is the single largest gap in Connecticut's patient protections and the inverse of Georgia's position post-HB 286.

For ground-ambulance disputes, leverage shifts to:

- Common-law reasonable-value defense (UCC § 2-305 / quantum meruit principles)
- Insurer's CUTPA-via-CUIPA exposure for unreasonable claim payment
- CUTPA against the ambulance provider for excessive billing

### Other caveats

- **ERISA preemption:** the Act does not reach self-funded ERISA employer plans. Those are covered by the federal NSA.
- Excludes workers' compensation, Medicare, and Medicaid.
- Only applies to plans regulated by Connecticut (fully insured); self-funded plans rely on the federal NSA.

## Regulatory agencies

### Connecticut Insurance Department (CID)

- **Online complaint:** [portal.ct.gov/cid/file-a-complaint](https://portal.ct.gov/cid/file-a-complaint)
- **Phone:** main **(860) 297-3800**; toll-free Consumer Affairs **1-800-203-3447**
- **Mail (street):**
  > Connecticut Insurance Department
  > Consumer Affairs Division
  > 153 Market Street, 7th Floor
  > Hartford, CT 06103
- **Mail (PO Box for complaints):**
  > Connecticut Insurance Department
  > P.O. Box 816
  > Hartford, CT 06142-0816
- **Authority:** all insurance companies licensed in Connecticut, including fully-insured health insurers, HMOs, PPOs, Medicare supplement. Administers § 38a-477aa (surprise billing) and CUIPA. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and does not regulate providers, hospitals, or debt collectors (route to AG/DCP).

### Office of the Healthcare Advocate (OHA)

- **Online help:** [portal.ct.gov/oha/get-help](https://portal.ct.gov/oha/get-help)
- **Phone:** toll-free **1-866-466-4446** (Mon-Fri 8:00-4:30)
- **Email:** Healthcare.Advocate@ct.gov
- **Authority:** Independent state agency that provides free assistance to Connecticut consumers with surprise medical bills, insurance denials, appeals, and billing disputes. Not a regulator, but an advocacy/intake channel that often resolves disputes informally before they reach CID or court. Always CC OHA on hospital and insurer dispute letters for Connecticut patients.

### Connecticut Attorney General — Consumer Protection Section

- **Online complaint:** [dir.ct.gov/ag/complaint](https://www.dir.ct.gov/ag/complaint/); landing page at [portal.ct.gov/AG/Common/Complaint-Form-Landing-page](https://portal.ct.gov/AG/Common/Complaint-Form-Landing-page)
- **Phone:** Consumer Assistance Unit **(860) 808-5420**
- **Authority:** enforces CUTPA (§ 42-110a et seq.) against hospitals, providers, and debt collectors. Reach over **original creditors** as well as third-party collectors — closes the gap that the federal FDCPA leaves open. Use for hospital-side billing disputes, deceptive collection practices, and any pattern of misconduct supporting class treatment.

### Connecticut Department of Consumer Protection (DCP)

- **Phone:** main **(860) 713-6300**; toll-free **1-800-842-2649**
- **Online:** [portal.ct.gov/dcp/contact](https://portal.ct.gov/dcp/contact)
- **Authority:** Licenses and oversees consumer collection agencies under Conn. Gen. Stat. § 36a-800 et seq. File DCP complaints when the dispute is with a third-party debt collector rather than the hospital itself. DCP and AG jointly receive CUTPA suit notices under § 42-110g(c).

## Small claims court — Superior Court Small Claims Session

- **Court name:** **Superior Court, Small Claims Session** (not a separate court — a division of the Superior Court). Sessions held at each Judicial District courthouse and at some Geographical Area courthouses.
- **Jurisdictional limit:** **$5,000**, codified at **Conn. Gen. Stat. § 51-15** and Conn. Practice Book § 24-1
- **Source:** [law.justia.com/codes/connecticut/title-51/chapter-870/section-51-15](https://law.justia.com/codes/connecticut/title-51/chapter-870/section-51-15); CT Judicial Branch FAQ at [jud.ct.gov/faq/smallclaims.html](https://www.jud.ct.gov/faq/smallclaims.html)
- **Filing fees (2024-2025):** **$95** for claims up to $2,500; **$175** for claims $2,500-$5,000 (Conn. Gen. Stat. § 52-259). Statewide fees, not county-by-county.
- **Limited exceptions to the $5,000 cap:** Up to $15,000 for home-improvement-contract claims with certified contractors, and uncapped recovery for security-deposit claims by residential tenants. Neither typically applies to medical-bill disputes.
- **Attorney rules:** **Attorneys are permitted but not required.** Connecticut is more attorney-friendly in small claims than many states — defendants in medical-bill disputes commonly appear with counsel. Plan accordingly.
- **Jury trial:** Not available in Small Claims Session. Either party may move to transfer the case to the regular civil docket of the Superior Court, where jury demand is available — but transfer costs filing fees and triggers formal discovery, which usually defeats the small-claims economic logic for patient plaintiffs.
- **Useful Connecticut-specific procedure:** Small Claims judgments are **not appealable as of right** by the defendant. A small-claims judgment for the patient is effectively final once the 20-day post-judgment window closes, with very limited grounds for reopening.

**Above the cap:** Claims exceeding $5,000 must be filed in the Superior Court's regular civil docket. Filing fees there are significantly higher (~$360 entry fee under § 52-259) and formal discovery applies.

## Statute of limitations

- **Written contracts:** **6 years from the act or occurrence complained of** — **Conn. Gen. Stat. § 52-576**
- **Oral (executory) contracts:** **3 years** — Conn. Gen. Stat. § 52-581
- **Executed oral contracts (e.g., services rendered):** **6 years** — § 52-576 (the same provision covers "actions for account" and implied/executed contracts)
- **CUTPA claims:** **3 years from the act complained of** — § 42-110g(f)
- **Tort (including common-law bad faith):** **3 years** — § 52-577 (negligence) or § 52-584 (personal injury, 2 yrs from discovery, 3 yrs from act)
- **Source:** [law.justia.com/codes/connecticut/title-52/chapter-926/section-52-576](https://law.justia.com/codes/connecticut/title-52/chapter-926/section-52-576/); [findlaw.com/state/connecticut-law/connecticut-civil-statute-of-limitations-laws.html](https://www.findlaw.com/state/connecticut-law/connecticut-civil-statute-of-limitations-laws.html)

Most hospital admissions involve a signed financial-responsibility form — a written contract, so **6 years** applies under § 52-576. Implied-in-fact medical billing without any signed agreement is treated as an executed oral contract or open account, which also falls under § 52-576's 6-year window (the executory/3-year route at § 52-581 rarely applies to medical bills because services have been rendered).

The clock runs from breach (typically the day payment was due and not made), not from when damages are discovered.

Partial payment or written acknowledgment of the debt **restarts the clock**. **Do not make a partial payment on a time-barred debt without legal advice** — it can revive a stale claim under Connecticut's acknowledgment doctrine.

## Ground ambulance balance-billing

**Not covered by Connecticut state law.** § 38a-477aa expressly excludes ambulance services, EMTs, and paramedics from the definition of "health care provider" subject to surprise-billing protections. The federal No Surprises Act also excludes ground ambulance. Connecticut patients receiving OON ground ambulance have no balance-bill cap under either layer.

**Patient leverage in CT ground-ambulance disputes:**

1. **Reasonable-value defense** — under UCC § 2-305 / quantum meruit, the patient owes only the reasonable value of services. Cite Medicare and Medicaid rate schedules for the same trip as benchmarks.
2. **CUTPA-via-CUIPA against the insurer** — if the insurer paid an unreasonably low rate forcing balance billing, that may be a § 38a-816 unfair practice and a CUTPA claim under § 42-110g.
3. **CUTPA against the ambulance provider** — billing rates several multiples above Medicare may constitute an unfair practice, particularly where the patient had no meaningful choice of provider.
4. **OHA assistance** — the Office of the Healthcare Advocate has substantial informal-resolution success even where the statute does not apply.
5. **Look for municipal-ambulance grant or hardship policies** — many CT municipal ambulance services waive or reduce charges for residents who request it.

This is the highest-friction area for Connecticut patients. Set expectations accordingly when triaging.

## Credit reporting — Medical Debt Reform Act (Public Act 24-6)

- **Statute:** **Public Act 24-6, "An Act Concerning the Reporting of Medical Debt"** (codified in Conn. Gen. Stat. § 36a-800 et seq. and amendments to Title 38a)
- **Effective date:** **July 1, 2024**
- **Source:** [cga.ct.gov/2024/act/Pa/pdf/2024PA-00006-R00SB-00395-PA.PDF](https://cga.ct.gov/2024/act/Pa/pdf/2024PA-00006-R00SB-00395-PA.PDF); Governor's signing statement at [portal.ct.gov/governor/news/press-releases/2024/05-2024/governor-lamont-signs-law-prohibiting-medical-debt-from-being-reported-to-credit-rating-agencies](https://portal.ct.gov/governor/news/press-releases/2024/05-2024/governor-lamont-signs-law-prohibiting-medical-debt-from-being-reported-to-credit-rating-agencies)

### What it prohibits

- **No reporting of medical debt to credit rating agencies** by Connecticut health care providers, hospitals, or collection entities, for any portion of the debt.
- **Reported debt is void.** Any medical debt that has been reported to a credit agency in violation of the Act is unenforceable as a matter of law.
- **Contract requirement.** Providers and hospitals must include contractual provisions in any debt-collection contract prohibiting the collector from reporting the medical debt to credit agencies.

### Scope

- Applies to "medical debt" — debt arising from health care goods or services, including hospital care, medical equipment, and prescriptions.
- **Carve-out for general credit cards:** debt charged to a general-purpose credit card is not covered, **unless** the card was issued under a credit plan specifically for health care services or goods (covers Care Credit, hospital-branded medical credit cards, and similar products).

### Why it matters — the highest-leverage Connecticut-specific cite

For any Connecticut patient whose medical debt has been or might be reported to Equifax, Experian, or TransUnion:

- Send a written notice to the provider, hospital, and any collector demanding written confirmation that no portion of the debt has been or will be reported.
- If reported, the debt is **void** by operation of law — the entire claim collapses, not just the portion that was reported.
- This is materially stronger than the 2022-2023 voluntary CRA changes (which removed only paid debt and small balances) and stronger than any other state credit-reporting protection.

### Federal preemption posture

The CFPB issued an October 2025 interpretive rule taking the position that the FCRA preempts state laws restricting medical-debt credit reporting. If that survives challenge, it could limit PA 24-6's reach over the **furnisher-to-CRA reporting step**. However:

- The state-law claim against the in-state provider/collector for collecting on void debt is independent of FCRA reporting mechanics.
- The CFPB rule has been challenged in federal court; as of this writing it is not in final effect.

### Prior law (PA 21-129, effective Oct 1, 2022)

For debts arising before July 1, 2024, the earlier statute remains relevant:

- 1-year delay before any medical debt could be reported to credit rating agencies.
- No foreclosure on the patient's primary residence to collect medical debt.
- No wage garnishment for any patient eligible for the hospital's bed fund.
- **Interest cap: 5% per year, pre- and post-judgment**, on hospital-services debt (Conn. Gen. Stat. § 37-3a).

The PA 21-129 protections remain in force for non-credit-reporting issues (foreclosure, garnishment, interest cap).

## Hospital charity care — state-mandated free bed funds

- **Statutes:** **Conn. Gen. Stat. § 19a-509b** (Hospital bed funds), supported by **§ 19a-649** (hospital reporting on charity care to the Office of Health Strategy)
- **Source:** [law.justia.com/codes/connecticut/title-19a/chapter-368v/section-19a-509b](https://law.justia.com/codes/connecticut/title-19a/chapter-368v/section-19a-509b/); [uwc.211ct.org/free-bed-funds-at-hospitals](https://uwc.211ct.org/free-bed-funds-at-hospitals/); Dollar For at [dollarfor.org/state_sheet/connecticut](https://dollarfor.org/state_sheet/connecticut/)
- **Substance:** Connecticut has a **comprehensive state-mandated hospital financial-assistance regime**, going materially beyond federal IRS § 501(r):
  - Each hospital holding or administering a "free bed fund" must make a one-page English/Spanish summary available describing the fund and how to apply, in the admissions office, ER, social services, billing office, and at any collection agent.
  - Hospital staff (social workers, discharge planners, billing personnel) must be trained on the fund's eligibility and application process.
  - Patients are entitled to **reapply** upon rejection; funds may become available annually.
  - Applicants must receive **written notice** of any award or rejection, with reasons stated.
  - Patients who cannot pay an outstanding bill must be **allowed to apply or reapply** for the bed fund.
- **Coverage:** Applies to all Connecticut hospitals administering bed funds — historically a near-universal practice for non-profit hospitals; for-profit and specialty hospitals should be verified individually.
- **Companion reporting (§ 19a-649):** Hospitals must report annual charity-care and reduced-cost services data to the Office of Health Strategy. The OHS publishes hospital-by-hospital data which can be cited in dispute letters.
- **Use in dispute letters:** Cite § 19a-509b's application/reapplication rights, the written-notice requirement, and the connection to § 19a-509 itemization. A hospital that has not provided the one-page summary or denied an application without written reasons is in violation of the statute — a CUTPA hook.

Connecticut's free-bed-fund regime is one of the strongest state-mandated FA layers in the country. For any Connecticut patient with income below ~400% of the federal poverty level, screening for bed-fund eligibility is the highest-leverage first move — write-offs can be 100%.

## Hospital lien statute

- **Citation:** **Conn. Gen. Stat. § 49-73** — Liens on accident and liability policies in favor of hospitals and ambulance services
- **Source:** [law.justia.com/codes/connecticut/title-49/chapter-847/section-49-73](https://law.justia.com/codes/connecticut/title-49/chapter-847/section-49-73/)
- **Substance:** A tax-exempt hospital, ambulance owner/operator, or municipal/state-owned hospital may file a lien on the proceeds of any accident-and-liability insurance policy covering injuries sustained by the patient. The lien attaches **only to the third-party insurance proceeds**, to the extent of the actual cost of services and materials.
  - **Not a lien on the patient's home, wages, or bank accounts.** Strictly a third-party-recovery lien.
  - Covers injuries **not covered by Workers' Compensation** (WC has its own subrogation regime).
- **Notice and perfection:**
  - Hospital must serve written notice on the insurer identifying the patient, the insurer, the amount expended, and an estimated amount to be expended.
  - When the insurer's liability is fixed, the insurer pays the hospital directly **if all interested parties agree** on the amount; if not, any party may bring an action of interpleader in the Judicial District where the hospital is located.
  - Service on non-resident insurers may be made on the Insurance Commissioner; non-resident treated patients are presumed to have appointed the Secretary of the State as their agent for service of process in interpleader.
- **Combined with PA 21-129/24-6:** The hospital lien statute does **not** authorize a lien on the patient's primary residence, and PA 21-129 further blocks any attempt to foreclose on the residence to collect any portion of medical debt. The lien is a narrow third-party-recovery tool, not a general collection device.

## Wage garnishment

- **Statute:** **Conn. Gen. Stat. § 52-361a et seq.** (wage execution) and § 52-350a (post-judgment remedies)
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a court judgment. Post-judgment, Connecticut caps wage execution at the lesser of (i) 25% of disposable earnings or (ii) the amount by which weekly disposable earnings exceed 40× the federal minimum wage — Connecticut's "40 times" rule is **more protective** than the federal CCPA's "30 times" rule.
- **Medical-debt-specific bar (PA 21-129):** Hospitals and their affiliates may not seek wage execution against any patient who is **eligible for the hospital's bed fund**, regardless of judgment status. This is a Connecticut-specific overlay materially stronger than the federal CCPA cap.
- **Use:** In response letters to collectors threatening garnishment without a judgment in hand, or threatening garnishment of a bed-fund-eligible patient.

## Key Connecticut-specific advantages

Worth keeping in mind when triaging a CT patient's bills:

1. **Medical Debt Reform Act (PA 24-6)** — Any medical debt reported to a credit rating agency is **void**. This is the most powerful single-statute lever in the kit's CT pack. Always check whether the debt has been or might be furnished to a CRA, and lead with this in dispute letters.
2. **CUTPA punitive damages and attorney's fees** — § 42-110g makes class actions and fee recovery realistic. Mention in any 30-day warning letter to CT providers, insurers, or collectors.
3. **State-mandated free bed funds (§ 19a-509b)** — Reapplication right, written-rejection requirement, and trained-staff mandate are unusually strong. Screen every patient under ~400% FPL for bed-fund eligibility before negotiating.
4. **5% interest cap on hospital debt (§ 37-3a)** — Stops runaway interest accruals that inflate small bills into unmanageable judgments. Calculate the lawful balance using 5% and contest any higher figure.
5. **Office of the Healthcare Advocate** — Free, neutral, effective informal-resolution channel. CC OHA on substantive dispute letters; many disputes settle before the formal regulatory or court step.
6. **CUTPA-via-CUIPA framework** — Closes the no-private-action gap that defeats UCSPA claims in other states. Plead carefully (general business practice requirement) and the insurer faces statutory punitives and fees.

## Key Connecticut-specific weakness

**Ground ambulance is not covered by state surprise-billing law.** This is the single largest gap in CT patient protections. Federal NSA also excludes ground ambulance, so a CT patient hit by an OON ground-ambulance bill faces the same exposure as a patient in a state with no surprise-billing law at all. Manage expectations and fall back to reasonable-value, CUTPA, and OHA leverage when this fact pattern appears.

## Quick reference for letter rendering

When the LLM renders a Connecticut-bound letter, substitute these defaults:

- **State statute (itemization right):** **Conn. Gen. Stat. § 19a-509** — request itemized bill in writing, 30-day delivery requirement, plain language required.
- **State insurance department (CC line):** Connecticut Insurance Department, Consumer Affairs Division, P.O. Box 816, Hartford, CT 06142-0816 (or 153 Market Street, 7th Floor, Hartford, CT 06103 for courier delivery)
- **State healthcare advocate (CC line, default for any CT letter):** Office of the Healthcare Advocate, 450 Capitol Avenue, MS#51OHA, P.O. Box 340308, Hartford, CT 06134-0308 (Healthcare.Advocate@ct.gov; 1-866-466-4446)
- **State AG consumer protection (CC line):** Connecticut Attorney General, 165 Capitol Avenue, Hartford, CT 06106 ([portal.ct.gov/ag](https://portal.ct.gov/ag); Consumer Assistance Unit (860) 808-5420)
- **Small-claims court name:** **Superior Court, Small Claims Session — Judicial District of [district]**
- **Filing fee (in 30-day warning):** "$95 for claims up to $2,500, $175 for claims $2,500-$5,000"
- **Statute of limitations (in 30-day warning):** "Conn. Gen. Stat. § 52-576 (six years for breach of written contract and for actions for account)"
- **For credit-reporting issues (lead with this in any CT letter):** Cite **Public Act 24-6 (eff. July 1, 2024)**, codified at Conn. Gen. Stat. § 36a-800 et seq. — any medical debt reported to a credit rating agency is **void** as a matter of Connecticut law.
- **For provider-side disputes (vs. insurer-side):** Cite **CUTPA § 42-110b and § 42-110g** — actual damages, punitive damages, attorney's fees, class actions. No pre-suit demand required, but the kit's standard 30-day warning creates the evidentiary record of reckless indifference.
- **For insurer-side disputes:** Cite **CUIPA § 38a-816** for the specific unfair practice and **CUTPA § 42-110b** for the cause of action, plus **Buckman v. People Express** common-law bad faith. Plead the "general business practice" element (Mead v. Burns) — cite CID enforcement history if available.
- **For ground-ambulance balance bills:** Do **not** cite § 38a-477aa — it expressly excludes ambulance services. Use reasonable-value (UCC § 2-305 / quantum meruit) and CUTPA against the insurer or ambulance provider as appropriate.
- **For bed-fund eligibility (any CT patient under ~400% FPL):** Cite **Conn. Gen. Stat. § 19a-509b** — patient is entitled to a one-page application summary, written notice of any award or rejection with reasons, and the right to reapply.
- **For interest disputes:** Cite **Conn. Gen. Stat. § 37-3a** — interest on hospital-services debt capped at 5% per year, pre- and post-judgment.
