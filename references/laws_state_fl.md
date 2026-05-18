# Florida state pack

The fully-worked state-law layer for Florida patients. The LLM uses this when the patient's state is Florida. Tennessee equivalent at [`laws_state_tn.md`](laws_state_tn.md); Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Florida is, on the whole, less patient-favorable than New York or California. The hospital-itemization right is narrower, the small-claims cap is lower, there is no state-level ground-ambulance protection in force, and the FDUTPA-equivalent route against original creditors is weaker than Georgia's FBPA. The structural headline that flips the leverage back toward the patient is **Fla. Stat. § 624.155 — the Civil Remedy Notice statute**. Florida is one of a handful of states with a true first-party bad-faith remedy against health insurers, complete with a statutory 60-day cure period, damages that can exceed policy limits, and recovery of attorney's fees. The CRN is the single most important Florida-specific tool when the dispute is insurer-side. Use it.

Two other structural notes:

- **Hospital "extraordinary collection actions" are heavily regulated** under Fla. Stat. § 395.3011 (added by HB 7089, effective July 1, 2024), which forces hospitals and ambulatory surgical centers to send the financial-assistance policy, attempt insurance billing, and wait out specified periods before they may sue, sell the debt, or report it to credit bureaus.
- **The medical-debt statute of limitations against the patient is now three years**, not five, for facility-based medical debt that has been referred to a collector — also HB 7089. Citing the wrong (older) five-year period in a dispute letter hands the hospital an avoidable win.

## 1. Hospital itemization right

- **Statute:** **Fla. Stat. § 395.301** (itemized statements) and § 395.3011 (collection prerequisites)
- **Source:** [leg.state.fl.us — § 395.301](http://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0300-0399/0395/Sections/0395.301.html); [leg.state.fl.us — § 395.3011](http://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0300-0399/0395/Sections/0395.3011.html)
- **What § 395.301 requires:**
  - The hospital, ambulatory surgical center, or urgent care center must furnish an itemized statement **within 7 days after discharge or after the patient's request, whichever is later** (§ 395.301(1)(e)1.).
  - Questions about the bill must be answered in writing **within 7 business days** of receipt (§ 395.301(5)).
  - Formal grievances must be answered **within 7 business days** of filing (§ 395.301(6)).
  - The itemized statement must show specific services by date and provider, unit pricing, the component services that make up bundled charges, facility fees with an explanation, payment status, drug names (not codes), therapy details (date, type, length), and which physicians bill separately. **Generalized line items like "miscellaneous" or "other" are expressly prohibited.**
- **Scope:** Licensed hospitals, ambulatory surgical centers, and urgent care centers. Not freestanding physician offices (federal Hospital Price Transparency Rule at 45 CFR Part 180 is a weaker fallback there).
- **Written request requirement:** The statute does not explicitly require a written request, but make one anyway by certified mail to crystallize the 7-day clock.
- **Private right of action:** No direct private remedy in § 395.301 itself. Enforcement is via AHCA (the Agency for Health Care Administration) and, for the collection-side restrictions, § 395.3011 acts as an affirmative defense and a basis to challenge any hospital collection action.

Use Fla. Stat. § 395.301 as the citation in `templates/letter_itemization_request.md` for any Florida patient, and pair it with the § 395.3011 collection-pause language when the bill has already been referred for collection.

## 2. Florida Unfair Insurance Trade Practices Act

- **Statute:** **Fla. Stat. § 626.9541** (the Unfair Insurance Trade Practices Act, part of the broader Chapter 626 Part IX)
- **Source:** [leg.state.fl.us — § 626.9541](http://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0600-0699/0626/Sections/0626.9541.html)
- **Substance:** Enumerates the unfair methods of competition and unfair or deceptive acts in the insurance business. Subsection (1)(i) lists the unfair claim-settlement practices specifically: misrepresenting pertinent facts or policy provisions, failing to acknowledge communications, failing to adopt reasonable investigation standards, denying claims without a reasonable investigation, failing to confirm coverage status, failing to explain denials in writing, failing to pay PIP claims timely, and (for systemic offenders) committing any of these with a frequency that indicates a general business practice.
- **Private right of action posture (critical):** § 626.9541 itself is enforced by the Office of Insurance Regulation and the Department of Financial Services. There is **no standalone private cause of action under § 626.9541**. The private remedy is built one statute over: **Fla. Stat. § 624.155 expressly converts certain § 626.9541(1)(i) violations into civil causes of action** once the Civil Remedy Notice is filed and the 60-day cure period has run. See § 3 below.
- **How to use it:** Plead the § 626.9541 violation as a factual predicate inside the § 624.155 Civil Remedy Notice (CRN). Do not plead § 626.9541 as a standalone count.

## 3. Florida Civil Remedy / first-party bad faith

- **Statute:** **Fla. Stat. § 624.155** (Civil Remedy)
- **Source:** [leg.state.fl.us — § 624.155](http://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0600-0699/0624/Sections/0624.155.html); [DFS Civil Remedy portal](https://apps.fldfs.com/civilremedy/); [DFS Civil Remedy and Required Legal Notices page](https://www.myfloridacfo.com/division/consumers/civilremedy)
- **What it does:** Florida is one of the relatively few states with a first-party statutory bad-faith remedy against health insurers. § 624.155 lets a person (including an insured) sue an insurer that:
  - Violates listed provisions of § 626.9541(1)(i) (the unfair-claim-settlement practices listed above);
  - Fails to attempt in good faith to settle when, in fairness, it could and should;
  - Makes payments without a statement showing the coverage under which the payment is made;
  - Fails to promptly settle when the obligation to settle has become reasonably clear, in order to influence settlement under another coverage.
- **The Civil Remedy Notice (CRN) prerequisite:** Before suit, the claimant must file a CRN with the Department of Financial Services **on a DFS-provided form** and serve it on the insurer. The CRN must specify:
  - The statutory provision (and exact statutory language) allegedly violated;
  - The facts and circumstances giving rise to the violation;
  - The names of any individuals involved;
  - The relevant policy language (if available to the claimant);
  - A statement that the notice perfects the right to pursue the civil remedy.
- **60-day cure window:** If, within 60 days after the insurer receives the CRN, the damages are paid or the violation is corrected, no action lies. Payment after day 60 does **not** abate the action.
- **Damages:** Damages reasonably foreseeable as a result of the violation, which **may exceed policy limits**. Punitive damages where the violation occurs with sufficient frequency to indicate a general business practice and is willful, wanton, malicious, or in reckless disregard. **Prevailing claimant recovers court costs and reasonable attorney's fees.**
- **Filing mechanics:** File the CRN electronically through the DFS Civil Remedy filing system at [apps.fldfs.com/civilremedy](https://apps.fldfs.com/civilremedy/). The portal generates a unique CRN number; keep it.
- **ERISA preemption:** § 624.155 is **preempted as applied to self-funded ERISA employer plans**. The federal remedy for those is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) fees — no Florida bad-faith damages. § 624.155 remains in play for fully-insured group plans, Florida-issued individual and marketplace plans, Medicare supplement, and HMO products regulated under Chapter 641.

This is the Florida-specific headline. Any insurer-side dispute that has been bouncing for more than 60 days without resolution should at least be evaluated for CRN filing.

## 4. Florida balance-billing law

- **Statutes:**
  - **Fla. Stat. § 627.64194** — balance-billing prohibition for **PPOs and EPOs**, emergency and certain non-emergency services. Source: [leg.state.fl.us — § 627.64194](http://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0600-0699/0627/Sections/0627.64194.html).
  - **Fla. Stat. § 641.513** — emergency services and care from HMOs, including the prohibition on prior authorization and the OON reimbursement formula. Source: [leg.state.fl.us — § 641.513](http://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0600-0699/0641/Sections/0641.513.html).
- **What they prohibit:**
  - An out-of-network provider may not collect, or attempt to collect, from the insured/subscriber any amount in excess of applicable copayments, coinsurance, and deductibles for covered **emergency services**, regardless of the provider's contract status (§§ 627.64194(2)-(3), 641.513).
  - For **non-emergency services rendered at an in-network facility** where the insured had no opportunity to select a participating provider, the same balance-billing prohibition applies (§ 627.64194(4)).
  - The patient's cost-sharing is calculated as if the provider were in-network.
- **Insurer payment formula:** The insurer pays the OON provider the lesser of (i) the provider's charges, (ii) the usual and customary rate for the community where services were provided, or (iii) the mutually agreed rate (§§ 627.64194(3)(b), 641.513(5)). Disputes between provider and insurer over the rate may go to voluntary state dispute resolution; the patient is held harmless.
- **Scope (pre-NSA history):**
  - § 641.513 has applied to HMOs since 1996.
  - § 627.64194 was added by HB 221 (chapter 2016-222), effective July 1, 2016, extending the HMO balance-billing prohibition to PPOs and EPOs. Amended by chapter 2018-24 (technical) and chapter 2021-112 (conforming amendments).
  - Florida thus had statutory surprise-billing protection roughly **five and a half years before the federal No Surprises Act** (effective Jan 1, 2022). For services rendered between July 2016 and Jan 2022 to PPO/EPO/HMO patients, Fla. Stat. § 627.64194 or § 641.513 is the operative authority.
  - For services on or after Jan 1, 2022, the federal NSA and the Florida statute layer rather than displace; cite both.
- **What they do not reach:**
  - **Self-funded ERISA employer plans.** Federal NSA applies, but the Florida balance-billing prohibition does not.
  - **Ground ambulance.** Excluded from both Florida law and the federal NSA — see § 9 below.
  - **Indemnity/fee-for-service insurance** outside the PPO/EPO/HMO frame.
  - **Workers' compensation, Medicare, Medicaid** (different reimbursement frameworks).

## 5. Regulatory agency — consumer complaints route to DFS, not OIR

The Florida insurance-regulator landscape has a structural quirk worth getting right. **OIR (the Office of Insurance Regulation)** regulates the insurance industry (rate filings, solvency, market conduct, surprise-billing rule enforcement against carriers). **Consumer complaints, however, are handled by a separate agency — the Department of Financial Services (DFS), Division of Consumer Services.** Send patient complaints to DFS. Send Civil Remedy Notices to DFS. Cite OIR only when the matter is genuinely about insurer market conduct that the patient is escalating beyond the consumer-complaint channel.

### Florida Department of Financial Services (DFS), Division of Consumer Services

- **Online complaint / portal:** [Consumer Assistance Portal — assistcon.myfloridacfo.gov](https://assistcon.myfloridacfo.gov/en-US/); start at [myfloridacfo.com/division/consumers/needourhelp](https://www.myfloridacfo.com/division/consumers/needourhelp)
- **Civil Remedy filing system (§ 624.155 CRNs only):** [apps.fldfs.com/civilremedy](https://apps.fldfs.com/civilremedy/)
- **Phone:**
  - Insurance Consumer Helpline (in FL, toll-free): **1-877-MY-FL-CFO (1-877-693-5236)**
  - Out-of-state: **(850) 413-3089**
  - TDD: 1-800-640-0886
- **Email:** Consumer.Services@MyFloridaCFO.com
- **Mail:**
  > Florida Department of Financial Services
  > Division of Consumer Services
  > 200 East Gaines Street
  > Tallahassee, FL 32399-0322
- **Authority over:** insurers, HMOs, agents, adjusters, and insurance-related complaints. Routes provider-side complaints to AHCA or AG as appropriate.

### Florida Office of Insurance Regulation (OIR) — secondary, market-conduct level

- **Web:** [floir.com](https://floir.com/) (contact at [floir.gov/about-us/contact-us](https://floir.gov/about-us/contact-us))
- **Authority:** carrier licensure, rate filings, solvency, market conduct. **OIR does not generally take individual consumer complaints — that is DFS's job.** Cite OIR only in escalations that turn on the carrier's pattern of practice (e.g. a market-conduct examination request) rather than an individual claim dispute.

### Florida Agency for Health Care Administration (AHCA)

- **Web:** [ahca.myflorida.com](https://ahca.myflorida.com/)
- **Authority:** hospital licensure, facility complaints, enforcement of §§ 395.301 and 395.3011 against hospitals and ambulatory surgical centers. Route hospital itemization-failure or facility-billing complaints here.

## 6. Florida Attorney General — Consumer Protection

- **Online complaint:** [myfloridalegal.com/consumer-protection/consumer-complaint-form](https://www.myfloridalegal.com/consumer-protection/consumer-complaint-form); landing at [myfloridalegal.com/consumer-protection](https://www.myfloridalegal.com/consumer-protection)
- **Phone:**
  - Florida toll-free: **1-866-9-NO-SCAM (1-866-966-7226)**
  - Direct: **(850) 414-3990**
- **Mail:**
  > Office of the Attorney General
  > PL-01, The Capitol
  > Tallahassee, FL 32399-1050
- **Authority:** enforces the Florida Deceptive and Unfair Trade Practices Act (FDUTPA, Fla. Stat. § 501.201 et seq.) against providers, debt collectors, and businesses generally. Use for hospital/provider/collector disputes, particularly when the conduct is deceptive (false amounts owed, threats of legal action with no intent to sue, contact at prohibited hours).
- **FDUTPA private right of action:** Yes — Fla. Stat. § 501.211 provides a private cause of action with **actual damages and attorney's fees** to the prevailing party. Mention in 30-day warning letters to providers and collectors. Note that "actual damages" under FDUTPA is narrower than Georgia's FBPA treble-damages remedy.

## 7. Florida small claims court

- **Court name:** **County Court, Small Claims Division** (one per county)
- **Jurisdictional limit:** **$8,000** in principal damages, exclusive of interest, costs, and attorney's fees. Governed by Florida Small Claims Rules (Fla. Sm. Cl. R. 7.010 et seq.).
- **Source:** [Florida Small Claims Rules — effective Jan 1, 2026 PDF](https://www-media.floridabar.org/uploads/2025/12/2026_07-JAN-Small-Claims-Rules-1-1-2026.pdf); [Florida Courts — Small Claims](https://help.flcourts.gov/Other-Resources/Small-Claims)
- **Filing fees (clerk's schedule):**
  - Claims up to $100: **$55**
  - Claims $101 to $500: **$80**
  - Claims $501 to $2,500: **$175**
  - Claims $2,501 to $8,000: **$300**
- **Attorney rules:** permitted, not required. Designed for pro se litigants — simplified pleadings, mandatory pretrial conference under Rule 7.090, and relaxed evidence rules at the pretrial stage.
- **Pretrial conference:** Florida small claims uses a mandatory pretrial conference where the parties must appear in person; mediation is typically attempted before trial. Treat this as the leverage point — many billing disputes resolve at the pretrial mediation step.
- **Appeals:** to the Circuit Court within **30 days** of judgment under Fla. R. App. P. 9.030 and 9.110. **The appeal is on the record, not de novo** — this is the opposite of Tennessee. Plan accordingly: any record you want on appeal must be built at the County Court level (request a court reporter or recording).

**Heads up for 2026-and-later:** The Florida Supreme Court approved expanded county-court civil jurisdiction in 2025; the small-claims cap was not raised in that round, but a future bill could move it. Verify the cap before filing if the dispute is between $8k and the prevailing general civil limit.

## 8. Statute of limitations

Florida has a special, **shorter** clock for medical debt — do not default to the generic five-year written-contract period when a hospital, ambulatory surgical center, or urgent care center is involved.

- **Medical-facility debt (hospitals, ASCs, urgent care):** **3 years** from the date the facility refers the debt to a third-party collector — **Fla. Stat. § 95.11(4)** as amended by HB 7089 (effective July 1, 2024). This supersedes the older 5-year written-contract period for these defendants.
- **Breach of written contract (general):** **5 years** — Fla. Stat. § 95.11(2)(b)
- **Breach of oral contract / open account (general):** **4 years** — Fla. Stat. § 95.11(3)(j) (in the 2024 statute numbering; older sources cite § 95.11(3)(k))
- **Source:** [leg.state.fl.us — § 95.11](http://www.leg.state.fl.us/Statutes/index.cfm?App_mode=Display_Statute&URL=0000-0099/0095/Sections/0095.11.html)

In a Florida dispute letter, cite the three-year facility-debt period for hospital and ASC bills, and reserve the five-year written-contract period for non-facility provider bills (private physician practice billing, for example). Getting this wrong in a written demand to a hospital lets them respond, accurately, that the patient has misread the statute.

Partial payment or written acknowledgement can restart the clock. **Do not make a partial payment on a time-barred medical bill without legal advice.**

## 9. Ground-ambulance balance-billing — no Florida protection in force

**Florida has not enacted ground-ambulance balance-billing protection.** HB 425 (2025 session) proposed requiring health insurers and HMOs to reimburse out-of-network ground ambulance providers at the lesser of 325% of the Medicare rate or billed charges, with the patient held to in-network cost-sharing only, but the bill **died in the Commerce Committee on June 16, 2025**.

- **Source on HB 425:** [Florida Senate HB 425 (2025) bill page](https://www.flsenate.gov/Session/Bill/2025/425); [house staff analysis PDF](https://www.flsenate.gov/Session/Bill/2025/425/Analyses/h0425a.HFS.PDF)
- **Practical impact:** A Florida patient who receives a balance bill from an out-of-network ground ambulance has no Florida state-law remedy. The federal No Surprises Act also excludes ground ambulance. The remaining levers are general negotiation (UCC § 2-305 reasonable price, see `rules/05_negotiate_fair_price.md`), the hospital's own financial assistance policy if the ambulance is hospital-owned, and FDUTPA if the billing conduct itself is deceptive. **This is the single largest gap in Florida's balance-billing protections.**
- **Watch:** A successor bill to HB 425 is likely in the 2026 session. Verify status at [flsenate.gov](https://www.flsenate.gov/) before assuming the gap remains open.

## 10. Florida medical-debt credit-reporting

Florida has not enacted an outright ban on medical debt in credit reports (unlike New York, Colorado, and several others). What Florida did enact, via **HB 7089 (2024)** at **Fla. Stat. § 395.3011**, is a procedural restriction: hospitals, ambulatory surgical centers, and urgent care centers may not report a medical debt to a credit bureau as part of an "extraordinary collection action" until the facility has:

- Provided written notice of its financial-assistance policy;
- Sent an itemized bill;
- Billed any applicable insurance and waited for the insurer's response;
- Allowed the patient a reasonable period to apply for financial assistance;
- Waited at least 30 days after sending written notice (by certified mail or other traceable method) that collection action will begin.

Reporting before completing those steps is a violation of § 395.3011 and supports a complaint to AHCA and a defense to any collection lawsuit. It also feeds into a potential FDUTPA claim.

The general voluntary changes from Equifax/Experian/TransUnion (paid medical debt removed; debt under $500 not reported; one-year delay before reporting) continue to apply nationwide, including to Florida patients. See [`laws_federal.md`](laws_federal.md).

**Federal preemption posture is in flux.** The CFPB issued an October 2025 interpretive rule asserting that the FCRA preempts state restrictions on medical-debt credit reporting. If that survives challenge, it would limit the future utility of state laws like § 395.3011 for the credit-reporting piece specifically (the collection-pause and FAP-notice pieces remain provider conduct rules and are not FCRA-preempted). Source: [Stateline coverage](https://stateline.org/2025/11/06/new-trump-administration-rule-would-override-state-medical-debt-protections/).

## 11. Florida hospital charity-care obligations

Florida has a layered charity-care framework that goes meaningfully beyond the federal IRS § 501(r) floor.

- **Public Medical Assistance Trust Fund (PMATF):** **Fla. Stat. §§ 395.701 through 395.7017**. The PMATF is funded by an annual assessment on hospital net operating revenues for inpatient and outpatient services. Hospitals participating in the PMATF (effectively all licensed Florida hospitals) take on indigent-care obligations as part of the regulatory framework. Source: [Florida Senate — Chapter 395](https://www.flsenate.gov/Laws/Statutes/2022/Chapter395/All).
- **Definition of charity care:** Florida defines charity care as services rendered to a patient whose family income is at or below 150% of the federal poverty guideline, or where charges exceed 25% of annual family income with no other source of payment.
- **Hospital disclosure obligations:** Under § 395.301 and related provisions, each licensed facility must publish its financial-assistance policy, application process, payment-plan options, and charity-care criteria on its website. Source: [FHA Charity Care issue brief](https://fha.org/common/Uploaded%20files/FHA/Health%20Care%20Issues/Updated%20Briefs%200525/Issue%20Brief%20on%20Charity%20Care.pdf).
- **Health Care Responsibility Act (HCRA):** Fla. Stat. §§ 154.301-154.331. For qualified indigent patients receiving out-of-county emergency care at a participating hospital, financial responsibility ultimately lies with the patient's home county. Source: [AHCA HCRA handbook PDF](https://ahca.myflorida.com/content/download/10590/file/HCRAHB_Chapter_1.pdf).
- **§ 395.3011 collection pause for charity-care applicants:** A hospital may not pursue extraordinary collection actions while the patient's financial-assistance application is pending. This makes the application itself a powerful pause tool, separate from whether the patient ultimately qualifies.
- **Practical use:** Always apply. Screen via [Dollar For](https://dollarfor.org/state_sheet/florida) ([florida state sheet](https://dollarfor.org/state_sheet/florida/)) for help identifying the correct FAP and submitting. The application alone triggers the § 395.3011 pause.

## 12. Florida hospital lien statute

Florida is unusual: it does not have a statewide hospital lien statute. Following the **2012 Florida Supreme Court decision in Shands Teaching Hospital v. Mercury Insurance** ([Justia opinion summary](https://floridasupremecourtopinions.justia.com/2012/06/07/shands-teaching-hospital-and-clinics-inc-v-mercury-ins-co-of-florida/)), the statewide framework of special acts authorizing county hospital liens was held unconstitutional under article III, § 11(a)(9) of the Florida Constitution.

Hospital lien rights in Florida now exist **only by county ordinance** in the counties that have enacted them. Approximately nine counties have valid county ordinances, including Miami-Dade and Broward. Many other counties operated under special acts that are now invalid; whether a particular county currently has an enforceable lien framework requires verifying both the existence of a county ordinance and its post-2012 status.

- **Source:** [Carlton Fields analysis of Shands](https://www.carltonfields.com/insights/publications/2012/florida-supreme-court-declares-hospital-lien-law-u); [MWL hospital-lien chart, FL 67 counties](https://www.mwl-law.com/wp-content/uploads/2022/03/FLORIDA-HOSPITAL-LIEN-LAWS-IN-ALL-67-COUNTIES.pdf)
- **Scope (where valid):** A hospital lien typically attaches to the patient's cause of action against a third-party tortfeasor and the resulting settlement or judgment. It does **not** attach to the patient's home, wages, or general bank accounts.
- **Practical use:** If a Florida patient receives a hospital-lien notice, the first step is to confirm whether the county has a valid post-Shands ordinance (not a defunct special act). If the only authority cited is a pre-2012 special act, the lien is likely invalid and should be challenged at the front end. This is a meaningful, often-missed Florida-specific defense.

## 13. Florida medical-debt collections protections

Beyond the federal FDCPA (15 U.S.C. § 1692 et seq.) which applies to all third-party debt collectors nationwide, Florida adds:

- **Florida Consumer Collection Practices Act (FCCPA):** **Fla. Stat. § 559.55 et seq.** The FCCPA reaches **original creditors** (the hospital itself) as well as third-party collectors — broader than the federal FDCPA on that score. Prohibits the same general categories (false representations, harassment, unauthorized contact, threats of legal action without intent). **Private right of action with actual damages, statutory damages up to $1,000, punitive damages where appropriate, and attorney's fees** under § 559.77.
- **§ 395.3011 collection pause:** see § 11 above. Hospital and ASC collection must stop during pending insurance appeals, grievance procedures, payment plans, or financial-assistance applications.
- **3-year SOL on medical-facility debt:** see § 8 above.
- **FDUTPA:** Fla. Stat. § 501.201 et seq. — deceptive practices in collection (false amounts, threats of garnishment when no judgment exists, etc.) are actionable under FDUTPA with attorney's fees under § 501.211.

When responding to a Florida debt collector, cite the FCCPA in addition to the federal FDCPA in `templates/letter_fdcpa_validation.md`. The FCCPA's reach against the original creditor (the hospital) is a Florida-specific advantage the federal FDCPA does not provide.

## 14. Florida-specific patient-side advantages

Worth keeping in mind when triaging a Florida patient's bills:

1. **§ 624.155 Civil Remedy Notice** — Florida's structural headline. A real first-party bad-faith remedy against the health insurer, with a 60-day cure window, damages that may exceed policy limits, and **mandatory attorney's fees to the prevailing claimant**. File electronically at [apps.fldfs.com/civilremedy](https://apps.fldfs.com/civilremedy/). Use any time an insurer dispute is stuck more than 60 days.
2. **§ 395.3011 collection pause** — The hospital cannot sue, sell the debt, lien property, or report the debt to credit bureaus while a grievance, insurance appeal, payment plan, or financial-assistance application is pending. The application itself is the pause trigger; the patient does not need to qualify for the pause to take effect.
3. **3-year SOL on medical-facility debt** — Significantly shorter than most states' contract SOLs. Many hospital "old debt" demand letters are actually past the limitations period; verify before paying.
4. **§ 627.64194 / § 641.513 surprise-billing pre-NSA** — For services rendered in Florida between July 2016 and Jan 2022 to PPO/EPO/HMO patients, the Florida statute is the operative authority and predates the federal NSA. Useful for legacy disputes.
5. **FCCPA reach against original creditors** — Unlike the federal FDCPA, the FCCPA reaches the hospital's in-house billing department directly, with statutory damages and attorney's fees.
6. **Hospital lien invalidity by default** — Post-Shands, only ~9 counties have valid hospital lien ordinances. A lien notice from any other county is presumptively defective and should be challenged.
7. **Itemized statement detail mandate** — Fla. Stat. § 395.301 expressly prohibits "miscellaneous" or "other" line items. Any bill containing those categories is in itself a § 395.301 violation that supports an AHCA complaint and an itemization-failure letter.

## Quick reference for letter rendering

When the LLM renders a Florida-bound letter, substitute these defaults:

| Field                                                         | Florida value                                                                                                                                                                                                                    |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| State statute (itemization right)                             | **Fla. Stat. § 395.301** — 7-day response deadline; itemized detail mandated; no "miscellaneous" categories permitted                                                                                                            |
| State collection-pause statute                                | **Fla. Stat. § 395.3011** — extraordinary collection actions barred without prerequisites                                                                                                                                        |
| State insurance consumer agency (CC line)                     | Florida Department of Financial Services, Division of Consumer Services, 200 East Gaines Street, Tallahassee, FL 32399-0322; helpline 1-877-693-5236                                                                             |
| State insurance market-conduct regulator                      | Florida Office of Insurance Regulation (OIR) at [floir.com](https://floir.com/) — secondary, market-conduct only                                                                                                                 |
| Hospital regulator (facility complaints)                      | Florida Agency for Health Care Administration (AHCA) at [ahca.myflorida.com](https://ahca.myflorida.com/)                                                                                                                        |
| State AG consumer protection (CC line)                        | Florida Attorney General, Consumer Protection Division, PL-01 The Capitol, Tallahassee, FL 32399-1050; hotline 1-866-966-7226                                                                                                    |
| Bad-faith / unfair-claims remedy                              | **Civil Remedy Notice under Fla. Stat. § 624.155** — file electronically at [apps.fldfs.com/civilremedy](https://apps.fldfs.com/civilremedy/); 60-day cure window; damages may exceed policy limits; attorney's fees recoverable |
| Surprise-billing statute (PPO/EPO)                            | **Fla. Stat. § 627.64194** (PPO/EPO emergency + ancillary OON at in-network facility)                                                                                                                                            |
| Surprise-billing statute (HMO)                                | **Fla. Stat. § 641.513** (HMO emergency services)                                                                                                                                                                                |
| Ground-ambulance protection                                   | **None in force**; HB 425 (2025) died in committee. Use UCC § 2-305 negotiation and FAP application                                                                                                                              |
| Small-claims court name                                       | **County Court, Small Claims Division**                                                                                                                                                                                          |
| Small-claims jurisdictional limit                             | **$8,000** principal damages                                                                                                                                                                                                     |
| Small-claims filing fee (in 30-day warning)                   | "$55-$300 depending on claim amount"                                                                                                                                                                                             |
| Small-claims appeal nature                                    | On the record to Circuit Court within 30 days (not de novo — preserve the record below)                                                                                                                                          |
| Statute of limitations (hospital/ASC debt, in 30-day warning) | **"Fla. Stat. § 95.11(4) (three years for medical-facility debt referred to a collector)"** — do **not** default to the 5-year written-contract period for hospital bills                                                        |
| Statute of limitations (other written contracts)              | Fla. Stat. § 95.11(2)(b) — 5 years                                                                                                                                                                                               |
| Statute of limitations (oral / open account)                  | Fla. Stat. § 95.11(3)(j) — 4 years                                                                                                                                                                                               |
| State debt-collection statute                                 | **FCCPA, Fla. Stat. § 559.55 et seq.** — reaches original creditors; private cause of action with attorney's fees under § 559.77                                                                                                 |
| State deceptive practices statute                             | **FDUTPA, Fla. Stat. § 501.201 et seq.** — private cause of action with attorney's fees under § 501.211                                                                                                                          |

## Key Florida-specific structural notes

Florida is, on the surface, a less patient-favorable state than New York, California, or Colorado: smaller small-claims cap, narrower itemization window, no ground-ambulance protection, no outright medical-debt credit-reporting ban. But two pieces of Florida law tilt the leverage meaningfully back toward the patient when invoked correctly:

1. **The § 624.155 Civil Remedy Notice** is the strongest first-party bad-faith remedy in the kit's covered states. The 60-day cure window plus mandatory attorney's fees creates real economic pressure on insurers, and the damages-may-exceed-policy-limits provision changes the calculus on disputed denials. Treat the CRN as the headline lever for any Florida insurer dispute.
2. **The § 395.3011 collection-action freeze** plus the **3-year SOL** on medical-facility debt together make Florida one of the harder states for a hospital to maintain aggressive collection. A patient who (a) applies for financial assistance and (b) keeps the application open buys themselves both a § 395.3011 pause and time toward the 3-year SOL.

When triaging a Florida case, ask first: is this insurer-side or provider-side? Insurer-side disputes → CRN under § 624.155. Provider-side disputes → § 395.301 itemization demand + § 395.3011 collection-pause assertion + financial-assistance application + FCCPA invocation if collection conduct is problematic. The ground-ambulance gap and the hospital-lien-by-county quirk are the two areas where Florida law is materially worse than the federal floor or peer states — flag those explicitly when they appear.
