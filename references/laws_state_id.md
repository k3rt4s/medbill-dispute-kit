# Idaho state pack

The fully-worked state-law layer for Idaho patients. The LLM uses this when the patient's state is Idaho. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md); Colorado equivalent at [`laws_state_co.md`](laws_state_co.md). All citations verified against public sources as of 2026-08-19. Re-verify annually.

One thing makes Idaho's patient-side leverage unusual, and it is worth understanding in full before anything else:

The **Idaho Patient Act (Idaho Code Title 48, Chapter 3)** requires a health care provider to complete a specific, timed sequence of billing and notice steps before it may take any "extraordinary collection action" against a patient, meaning selling the debt, reporting it to a credit bureau, suing, garnishing wages, or filing a lien. Skip a step, and the patient owes **no collection costs, fees, attorney's fees, or interest** on that action, and may recover **actual damages or $1,000, whichever is greater** (up to **three times actual damages or $3,000** for a willful violation), plus the patient's own attorney's fees. This is a private right of action the patient can raise as a defense to a collection suit or bring affirmatively. It is the single most important Idaho-specific fact in this pack.

## Hospital itemization right

Idaho does not have a freestanding hospital-itemization statute like Tennessee's. The itemization duty is folded into the Idaho Patient Act itself:

- **Statute:** **Idaho Code § 48-304(1)(b)**, referencing the "consolidated summary of services" defined at **§ 48-303**
- **Source:** [legislature.idaho.gov/statutesrules/idstat/title48/t48ch3/sect48-304](https://legislature.idaho.gov/statutesrules/idstat/title48/t48ch3/sect48-304/); [legislature.idaho.gov/statutesrules/idstat/title48/t48ch3/sect48-303](https://legislature.idaho.gov/statutesrules/idstat/title48/t48ch3/sect48-303/)
- **What it requires:** the health care facility must deliver the patient a consolidated summary of services, free of charge, within 60 days, containing patient and facility identification, the visit date and duration, a general description of goods and services, and a clear notice that "this is not a bill."
- A facility may skip the separate consolidated summary if the patient instead gets a single final notice before extraordinary collection action from one billing entity, itemizing every charge, every reduction, and the final amount owed (§ 48-309).
- There is no separate "request within one year" window like Tennessee's. The summary and the final notice are automatic obligations tied to the collection timeline below, not something the patient must ask for. A written request is still worth sending to create a paper trail.

See the full Idaho Patient Act section below for how this fits into the larger sequence.

## The Idaho Patient Act

- **Statute:** **Idaho Code §§ 48-301 through 48-315**, enacted 2020 (H.B. 515, ch. 139), amended 2022 (H.B. 774, ch. 263) and 2024 (H.B. 501, reconciling the lien statute)
- **Source:** [legislature.idaho.gov/statutesrules/idstat/title48/t48ch3](https://legislature.idaho.gov/statutesrules/idstat/title48/t48ch3/); background summary at [hollandhart.com/idaho-patient-act-changes](https://www.hollandhart.com/idaho-patient-act-changes)
- **Legislative intent (§ 48-302):** the legislature found that "medical billing practices have little visibility to Idaho citizens," leaving consumers in collections for debts they never understood, and that existing law "enables excessive attorney's fees" without giving judges clear guidance. The Act exists to govern fair collection of health care debt.

### The five-part sequence before extraordinary collection action

Under **§ 48-304(1)**, no person may engage in an extraordinary collection action against a patient unless all of the following have happened, in order:

1. **(a) Timely billing.** The provider submits its charges to the patient's third-party payor (or to the patient directly, if uninsured) within **45 days** of the date of service or the date of discharge, whichever is later.
2. **(b) Consolidated summary.** The patient receives the free consolidated summary of services described above, within **60 days**.
3. **(c) Final notice.** The patient receives, free of charge, a **final notice before extraordinary collection action**: an itemized statement of charges, reductions, and the final amount owed, naming the billing entity's contact information.
4. **(d) No stacking of charges.** The provider does not charge or allow interest, fees, or other ancillary charges to accrue until at least **60 days** after the patient receives the final notice or the consolidated summary, whichever is later.
5. **(e) Waiting period.** At least **90 days** have passed since the patient received the final notice before any extraordinary collection action begins. That window can shrink to **45 days** only if the provider gave the patient separate written notice, at least 30 days in advance, that the shorter period would apply.

**Extraordinary collection action** is defined at § 48-303 to include: selling, transferring, or assigning the debt to a third party; reporting adverse information to a consumer reporting agency; and commencing any judicial or legal action, including a lawsuit, wage garnishment, or lien.

**Ordinary collection is not restricted.** Section 48-312 makes clear the Act does not stop a provider from demanding and collecting payment by any means short of an extraordinary collection action, phone calls, statements, and payment-plan offers are unaffected.

### Grace period for a provider that missed a deadline (§ 48-306)

If a provider misses the 45-day billing deadline or the 60-day summary deadline, it is not permanently barred. It gets an additional **45 days** to cure a missed § 48-304(1)(a) deadline, or an additional **180 days** to cure a missed § 48-304(1)(b) deadline. If it cures within that window and satisfies every other requirement, it may proceed. Even then, **the patient owes no costs, expenses, or fees, including attorney's fees, in that collection action.**

### What a violation costs the collecting party

- **No fee or cost liability (§ 48-305):** a patient has no liability for costs, expenses, or fees, including attorney's fees, to any party that pursued extraordinary collection action without complying with § 48-304. Even where a judgment is obtained in a compliant case, courts may award no more than **$350** (uncontested judgment) or **$750** (contested judgment), or 100% of the outstanding principal if that is less; **$75** for a first successful writ of attachment against a garnishee and **$25** for each subsequent one. A patient who prevails in a contested case recovers all of their own costs, expenses, and fees, including attorney's fees, from the non-prevailing party.
- **Damages for noncompliance (§ 48-311):** a party that fails to comply is liable to the patient for **actual damages or $1,000, whichever is greater**. For a willful or knowing violation, a court may award up to **three times actual damages or $3,000, whichever is greater**. The prevailing patient also recovers costs and reasonable attorney's fees.
- **Source:** [legislature.idaho.gov/statutesrules/idstat/title48/t48ch3/sect48-305](https://legislature.idaho.gov/statutesrules/idstat/title48/t48ch3/sect48-305/); [legislature.idaho.gov/statutesrules/idstat/title48/t48ch3/sect48-311](https://legislature.idaho.gov/statutesrules/idstat/title48/t48ch3/sect48-311/)

### How this interacts with hospital liens

A 2024 amendment (H.B. 501) reconciled the Patient Act's timing with Idaho's hospital-lien statute, see "Hospital lien statute" below. In short: a hospital lien tied to a third-party payor claim can now be filed within a defined 90-day-plus-30-day window that lines up with the Patient Act's own billing-adjustment timeline, instead of conflicting with it.

**Practical takeaway for the LLM:** whenever an Idaho patient reports a collection call, a credit-bureau entry, a lawsuit, a garnishment, or a lien on a medical debt, the first question is always whether the provider completed all five § 48-304 steps, in order, with the correct deadlines. If any step was skipped or came late (and the cure window in § 48-306 wasn't used), that is an immediate, statutory, fee-shifting defense, not just a negotiating point.

## Unfair claims settlement practices

- **Statute:** **Idaho Code § 41-1329**, Unfair Claim Settlement Practices, part of Title 41 (Insurance), Chapter 13 (Trade Practices and Frauds)
- **Source:** [legislature.idaho.gov/statutesrules/idstat/title41/t41ch13/sect41-1329](https://legislature.idaho.gov/statutesrules/idstat/title41/t41ch13/sect41-1329/)
- **Substance:** deems it an unfair or deceptive insurance practice, when done intentionally or with enough frequency to show a general business practice, to misrepresent policy facts, fail to acknowledge claim communications promptly, skip a reasonable investigation, refuse to pay without investigating, fail to attempt prompt and equitable settlement once liability is reasonably clear, or fail to explain the basis for a denial, among 14 enumerated practices.
- **Critical caveat: no private right of action.** Idaho courts have held § 41-1329 does not itself let an insured sue the insurer. Enforcement runs through the Insurance Director.
- **Administrative penalty (§ 41-1329A):** the director, after a hearing, may impose a civil penalty up to **$10,000** and may suspend or revoke the insurer's certificate of authority. **Source:** [legislature.idaho.gov/statutesrules/idstat/title41/t41ch13/sect41-1329a](https://legislature.idaho.gov/statutesrules/idstat/title41/t41ch13/sect41-1329a/)
- **Use:** cite § 41-1329 in a Department of Insurance complaint (see below), not as a standalone count in a lawsuit.

## Bad-faith failure to pay

Idaho has no standalone first-party bad-faith statute comparable to Tennessee's or Georgia's. The remedy is a **common-law tort**, recognized in *White v. Unigard Mutual Insurance Co.*, 112 Idaho 94, 730 P.2d 1014 (1986): Idaho's Supreme Court held there is a tort action, distinct from a breach-of-contract claim, for an insurer's bad faith in settling a first-party claim.

- **Elements:** the insurer intentionally and unreasonably denied or withheld payment; the claim was not "fairly debatable"; the denial was not the result of an honest, good-faith mistake; and the resulting harm is not fully compensable by ordinary contract damages.
- **Standard:** an insurer that challenges a "fairly debatable" claim, or whose delay results from an honest mistake, has not acted in bad faith. The patient must show more than a wrong decision, the insurer must have acted unreasonably given what it knew.
- **Fee-shifting companion, § 41-1839:** separate from the bad-faith tort, an insurer that fails to pay the amount "justly due" within **30 days** of a proof-of-loss statement (60 days for uninsured/underinsured motorist claims) is liable for the patient's attorney's fees in any resulting action, unless the insurer tenders the full amount before suit or a court finds nothing was owed. **Source:** [legislature.idaho.gov/statutesrules/idstat/title41/t41ch18/sect41-1839](https://legislature.idaho.gov/statutesrules/idstat/title41/t41ch18/sect41-1839/)
- **ERISA preemption:** the common-law bad-faith tort is a state-law claim and is typically preempted for self-funded ERISA employer plans. It remains available for fully-insured plans, individual/marketplace coverage, and Medicaid managed care where state regulation reaches.

## Surprise billing

Idaho does not have a state surprise-billing statute broader than the federal No Surprises Act. A 2018 attempt to expand state-level balance-billing protection for out-of-network care at in-network facilities and in emergencies (H.B. 495) did not advance. Idaho's only pre-existing balance-billing protections are narrow: a prohibition on balance billing by Medicaid managed-care organizations under contract, and a workers'-compensation billing cap under Idaho Code § 72-102(2). Neither reaches ordinary private-insurance out-of-network billing. For Idaho patients, the federal No Surprises Act is the operative protection, see [`laws_federal.md`](laws_federal.md) and the Idaho Department of Insurance's own summary at [doi.idaho.gov/consumers/health-insurance/nosurprises](https://doi.idaho.gov/consumers/health-insurance/nosurprises/).

## Ground ambulance balance-billing

**No Idaho state-level protection.** The federal No Surprises Act explicitly excludes ground ambulance, and Idaho has not enacted its own ground-ambulance balance-billing law. The DOI's own No Surprises Act page confirms the federal protections "generally do not apply to ... ground ambulance services." A ground-ambulance balance bill in Idaho has to be disputed through ordinary negotiation, the ambulance provider's own financial-assistance policy if any, or a challenge to the reasonableness of the charge, not through a surprise-billing statute.

## Idaho Consumer Protection Act

- **Statute:** **Idaho Code § 48-601 et seq.**; private right of action at **§ 48-608**; two-year limitation period at **§ 48-619**
- **Source:** [legislature.idaho.gov/statutesrules/idstat/title48/t48ch6/sect48-608](https://legislature.idaho.gov/statutesrules/idstat/title48/t48ch6/sect48-608/); [legislature.idaho.gov/statutesrules/idstat/title48/t48ch6/sect48-619](https://legislature.idaho.gov/statutesrules/idstat/title48/t48ch6/sect48-619/)
- **Substance:** a person who suffers an ascertainable loss from an unfair or deceptive practice may recover **actual damages or $1,000, whichever is greater**. Courts may additionally award punitive damages "in cases of repeated or flagrant violations" (§ 48-608(1)). Elderly or disabled patients get an enhanced remedy: **$15,000 or treble actual damages, whichever is greater**, if the offender knew or should have known of their status and specific harm thresholds are met.
- **Insurers are exempt.** **Section 48-605** carves out "persons subject to chapter 13, title 41, Idaho Code," meaning insurance claims-handling conduct is not reachable here, it stays inside § 41-1329 (regulator-only). **Source:** [legislature.idaho.gov/statutesrules/idstat/title48/t48ch6/sect48-605](https://legislature.idaho.gov/statutesrules/idstat/title48/t48ch6/sect48-605/)
- **Practical use:** the exemption is written narrowly to insurers and to conduct affirmatively permitted by another regulator. It does not on its face exempt hospitals or billing companies, so a deceptive-billing practice by a provider (misrepresenting the amount owed, misrepresenting in-network status, billing for services never rendered) is a plausible ICPA claim in addition to any Idaho Patient Act violation. No Idaho appellate decision applying § 48-608 specifically to hospital billing was found in this research, treat this as a supporting theory, not a guaranteed win.
- **Two-year clock:** shorter than the Patient Act's implied deadlines and shorter than the contract statute of limitations below, so do not wait to invoke it.

## Regulatory agencies

### Idaho Department of Insurance (DOI), Consumer Affairs

- **Online complaint:** [sbs.naic.org/solar-web/pages/public/onlineComplaintForm/onlineComplaintForm.jsf?state=id](https://sbs.naic.org/solar-web/pages/public/onlineComplaintForm/onlineComplaintForm.jsf?state=id&dswid=-8584); complaint info page at [doi.idaho.gov/consumers/file-a-complaint](https://doi.idaho.gov/consumers/file-a-complaint/)
- **Phone:** **(208) 334-4250** or toll-free **(800) 721-3272**
- **Email:** consumeraffairs@doi.idaho.gov
- **Mail:** 700 W. State Street, 3rd Floor, P.O. Box 83720, Boise, ID 83720-0043
- **Authority over:** insurers licensed in Idaho, including fully-insured health plans, HMOs, and Medicare supplement. Enforces § 41-1329 (unfair claims practices) and administers No Surprises Act complaints for state-regulated plans. **No authority over self-funded ERISA plans**, route those to DOL EBSA at **1-866-444-3272**. Does not regulate hospitals, providers, or debt collectors.
- Before filing, complete your plan's internal appeal if the complaint concerns an employer health plan.

### Idaho Attorney General, Consumer Protection Division

- **Complaint info and form:** [ag.idaho.gov/consumer-protection/consumer-complaints](https://www.ag.idaho.gov/consumer-protection/consumer-complaints/); complaint form at [ag.idaho.gov/content/uploads/2025/09/CPDComplaintForm.pdf](https://www.ag.idaho.gov/content/uploads/2025/09/CPDComplaintForm.pdf)
- **Phone:** **(208) 334-2424**; toll-free **1-800-432-3545**
- **Mail:** Consumer Protection Division, Bldg. 8, First Floor, 11331 W. Chinden Blvd., Boise, ID 83714
- **Fax:** (208) 334-4151
- **Important:** do not e-mail the completed complaint form, the office states it will not be received that way. Mail or fax it.
- **Authority over:** enforces the Idaho Consumer Protection Act (§ 48-601 et seq.). Complaints are voluntarily mediated; the office does not represent individual consumers in litigation, but a pattern of complaints can prompt a state enforcement action. Reaches hospitals, provider billing offices, and debt collectors for deceptive practices, subject to the insurer carve-out described above.

## Small claims court

- **Court name:** **Small Claims Department of the Magistrate's Division** (Idaho does not have a separately named small-claims court, it is a division of the magistrate court)
- **Jurisdictional limit:** **$15,000**, per **Idaho Code § 1-2301**, raised from $5,000 by **Senate Bill 1330 (2026)**, effective **July 1, 2026**
- **Source:** [legislature.idaho.gov/statutesrules/idstat/title1/t1ch23/sect1-2301](https://legislature.idaho.gov/statutesrules/idstat/title1/t1ch23/sect1-2301/); effective-date confirmation at [isb.idaho.gov/blog/amendments-to-idaho-rules-for-small-claims-actions-rule-15-effective-july-1-2026](https://isb.idaho.gov/blog/amendments-to-idaho-rules-for-small-claims-actions-rule-15-effective-july-1-2026/)
- **No punitive damages or pain-and-suffering awards** are available in small claims (§ 1-2301).
- **Filing fee:** **$33**, per **Idaho Code § 1-2303(3)**. **Source:** [legislature.idaho.gov/statutesrules/idstat/title1/t1ch23/sect1-2303](https://legislature.idaho.gov/statutesrules/idstat/title1/t1ch23/sect1-2303/)
- **Attorney rules:** **prohibited** at the hearing itself. Idaho Rules for Small Claims Actions, **Rule 8(b)**, bars any attorney from appearing with or for a party in a small-claims hearing, though an attorney may appear afterward in execution/collection proceedings, or as a party in their own right. **Source:** [isc.idaho.gov/rules-procedure/irsca](https://isc.idaho.gov/rules-procedure/irsca)

Because this limit only just rose from $5,000 to $15,000, a dispute that would have needed the regular magistrate civil docket a year ago may now fit comfortably in small claims, where the provider's billing department cannot bring a lawyer and the patient can represent themselves.

## Statute of limitations

- **Written contracts:** **5 years**, **Idaho Code § 5-216**. **Source:** [legislature.idaho.gov/statutesrules/idstat/title5/t5ch2/sect5-216](https://legislature.idaho.gov/statutesrules/idstat/title5/t5ch2/sect5-216/)
- **Oral or implied contracts:** **4 years**, **Idaho Code § 5-217**. **Source:** [legislature.idaho.gov/statutesrules/idstat/title5/t5ch2/sect5-217](https://legislature.idaho.gov/statutesrules/idstat/title5/t5ch2/sect5-217/)
- **Idaho Consumer Protection Act:** **2 years** from accrual, § 48-619 (see above).

Most hospital admissions involve a signed financial-responsibility form, a written contract, so the 5-year clock applies. An implied billing arrangement without a signature is more likely treated as oral (4 years). The clock runs from breach, typically the date payment was due and unpaid. Partial payment or a written acknowledgment of the debt can restart the clock under Idaho's general accrual rules. **Do not make a partial payment on an old medical debt without legal advice first.**

## Credit reporting

Idaho has no standalone statute banning medical debt from credit reports, unlike Colorado's outright furnishing prohibition. What Idaho has instead is the Patient Act's timing restriction: credit-bureau reporting is itself an "extraordinary collection action" under § 48-303, so it cannot happen until the full § 48-304 sequence (45/60/60/90-day timeline above) is satisfied. Report early, and the furnisher owes the same fee-bar and damages exposure described above.

Beyond that, Idaho patients rely on the 2022-2023 voluntary changes by Equifax, Experian, and TransUnion: paid medical collections are removed, unpaid medical debt gets a one-year reporting delay, and collections under $500 are excluded. See [`laws_federal.md`](laws_federal.md).

## Idaho charity care

Idaho has no state-level charity-care or financial-assistance mandate beyond the federal floor. Non-profit hospitals remain bound by **IRS § 501(r)** (see `laws_federal.md`): a written Financial Assistance Policy, limits on amounts charged to FAP-eligible patients, and a 240-day application window after the first post-discharge bill. Idaho's own contribution is procedural, not substantive: because reporting the debt or suing over it is an extraordinary collection action under the Patient Act, a hospital that has not finished its own billing/notice sequence cannot escalate collection regardless of whether the patient ever applied for charity care.

Use Dollar For at [dollarfor.org/state_sheet/idaho](https://dollarfor.org/state_sheet/idaho/) to screen for FAP eligibility and get help applying.

## Hospital lien statute

- **Statute:** **Idaho Code §§ 45-701 through 45-704B**, Hospital and Nursing Care Liens
- **Source:** [legislature.idaho.gov/statutesrules/idstat/title45/t45ch7/sect45-701](https://legislature.idaho.gov/statutesrules/idstat/title45/t45ch7/sect45-701/); [legislature.idaho.gov/statutesrules/idstat/title45/t45ch7/sect45-702](https://legislature.idaho.gov/statutesrules/idstat/title45/t45ch7/sect45-702/)
- **Substance:** a hospital has a lien for its reasonable charges upon any cause of action, claim, or settlement the injured patient has against a third party (e.g., an at-fault driver). **Not a lien on the patient's home, wages, or bank accounts** outside that third-party recovery.
- **Perfection requirements:** the hospital must file a verified statement (patient name and address, hospital name, admission/discharge dates, amount claimed, and the names of parties claimed liable) with the county recorder, then mail a copy by certified mail to every party claimed liable within **1 day** of filing.
- **Filing deadline (2024 amendment, H.B. 501):** where there is no third-party payor, the lien must be filed before or within **90 days** after discharge or the last day of treatment. Where there is a third-party payor, it must be filed during that same 90-day window but only after contracted billing adjustments are finalized, with an additional **30-day** window after the hospital actually receives the third-party payment.
- **Practical note:** this is only relevant when the bill stems from an accident with a liable third party (car crash, slip-and-fall). It rarely applies to ordinary billing disputes.

## Wage garnishment

- **Statute:** **Idaho Code § 11-712** (maximum garnishment), **§ 11-207** (exemption)
- **Substance:** a medical-bill creditor cannot garnish wages without first obtaining a court judgment. Post-judgment, Idaho follows the federal Consumer Credit Protection Act formula exactly: garnishment is capped at the lesser of **25% of disposable earnings** or the amount by which weekly disposable earnings exceed **30 times the federal minimum wage**. Idaho does not add extra protection beyond the federal floor, unlike Colorado's 20%/40x standard.
- **Use:** in response letters to a collector threatening garnishment before any judgment has been entered.

## Quick reference for letter rendering

| Element                                          | Idaho value                                                                                                                                              |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Centerpiece statute**                          | Idaho Patient Act, Idaho Code §§ 48-301 to 48-315                                                                                                        |
| **Billing deadline (provider to payor/patient)** | 45 days from service or discharge, § 48-304(1)(a)                                                                                                        |
| **Itemization / consolidated summary**           | 60 days, free of charge, § 48-304(1)(b), § 48-303                                                                                                        |
| **Waiting period before collection**             | 90 days from final notice (45 days with 30-day advance written notice), § 48-304(1)(e)                                                                   |
| **Violation remedy**                             | Actual damages or $1,000 (up to 3x or $3,000 if willful), plus attorney's fees, § 48-311; patient owes no fees/costs if provider didn't comply, § 48-305 |
| **Unfair claims settlement (insurer)**           | Idaho Code § 41-1329, regulator-only, no private right of action                                                                                         |
| **Bad faith (insurer)**                          | Common-law tort, *White v. Unigard*, 112 Idaho 94, 730 P.2d 1014 (1986); fee-shifting under § 41-1839                                                    |
| **Consumer protection (provider)**               | Idaho Code § 48-608, actual damages or $1,000, 2-year limitation (§ 48-619)                                                                              |
| **Surprise billing**                             | No state statute broader than federal NSA                                                                                                                |
| **Ground ambulance**                             | No Idaho protection                                                                                                                                      |
| **Insurance dept (CC line)**                     | Idaho Department of Insurance, Consumer Affairs, 700 W. State Street, 3rd Floor, P.O. Box 83720, Boise, ID 83720-0043                                    |
| **AG consumer protection (CC line)**             | Idaho Attorney General, Consumer Protection Division, Bldg. 8, First Floor, 11331 W. Chinden Blvd., Boise, ID 83714                                      |
| **Small-claims court**                           | Small Claims Department of the Magistrate's Division                                                                                                     |
| **Small-claims limit**                           | $15,000 (Idaho Code § 1-2301, effective July 1, 2026)                                                                                                    |
| **Filing fee**                                   | $33 (Idaho Code § 1-2303)                                                                                                                                |
| **Attorneys in small claims**                    | Prohibited at hearing, Idaho R. Small Claims Actions 8(b)                                                                                                |
| **Statute of limitations (written contract)**    | 5 years, Idaho Code § 5-216                                                                                                                              |
| **Hospital lien**                                | Idaho Code §§ 45-701 to 45-704B, 90-day filing window (2024 amendment)                                                                                   |

## Key Idaho-specific advantages

1. **The Idaho Patient Act's fee-shifting bar is automatic and does not require the patient to sue first.** If a provider skipped a step in the 45/60/90-day sequence, § 48-305 already means the patient owes no collection costs or attorney's fees on that action, this is a defense to raise immediately, including as an answer in a collection lawsuit or small-claims case, not just grounds for a separate suit.
2. **The Act gives the patient both a shield and a sword.** Unlike Idaho's insurance UCSPA (regulator-only, no private right of action), the Patient Act lets the patient recover actual damages or statutory damages directly, with attorney's fees, under § 48-311.
3. **The small-claims limit just tripled.** Idaho Code § 1-2301 rose from $5,000 to $15,000 effective July 1, 2026. Many hospital-billing disputes that would have needed the regular magistrate civil docket a year ago now fit in small claims, where attorneys are barred from the hearing itself.
4. **The Idaho Consumer Protection Act reaches providers, not just insurers.** Section 48-605 exempts insurers (they stay under Title 41 Chapter 13) but does not exempt hospitals or billing companies, giving a second, independent theory (§ 48-608, actual damages or $1,000) alongside any Patient Act claim for deceptive billing conduct. Its 2-year clock is shorter than the Patient Act's own timeline, so raise it early.
5. **The hospital-lien statute got a 2024 fix.** If a bill stems from an accident with a liable third party, confirm the hospital's lien was filed inside the reconciled 90-day (or 90-plus-30-day) window; a late-filed lien is vulnerable to challenge.

## Verification gaps

Claims that appeared in secondary sources during this research but could not be confirmed against the statute text itself were left out of this pack rather than guessed at:

- **A reported "115% of insurer rates / 200% of Medicare rate" cap on uninsured-patient charges.** One AI-generated consumer site attributed this to the Idaho Patient Act. It does not appear anywhere in Idaho Code §§ 48-301 through 48-315 as retrieved from the Idaho Legislature's own site, and a law-firm summary of the same chapter does not mention it either. Treat this as unverified; do not cite it in a letter.
- **Whether the Attorney General's Consumer Protection Division treats an Idaho Patient Act violation as within its own enforcement authority**, as opposed to purely a private civil remedy under § 48-311. The Act itself does not name a state regulator. A complaint to the AG may still be worth filing if the same conduct is also a deceptive practice under the Idaho Consumer Protection Act, but do not represent the AG as an IPA enforcement body without confirming with the office directly.
- **Whether any published Idaho appellate decision has applied the Idaho Consumer Protection Act (§ 48-608) to hospital or provider billing conduct specifically.** The statute's text and its exemption list (§ 48-605) support the theory, but no such case was located in this research.
- **The Idaho Attorney General's exact current street address.** Sources conflicted between "954 W. Jefferson" and "700 W. Jefferson Street, Suite 210" for the main office and a separate Chinden Boulevard address for the Consumer Protection Division specifically; this pack uses the Chinden Boulevard address for the Division because it is confirmed by the office's own 2025 complaint form and the office's current consumer-protection page, but confirm before mailing anything time-sensitive.
