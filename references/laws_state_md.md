# Maryland state pack

The fully-worked state-law layer for Maryland patients. The LLM uses this when the patient's state is Maryland. Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Three things make Maryland's medical-billing landscape unusually different from every other US state, and the toolkit must treat MD as a special case rather than a typical jurisdiction:

1. **All-payer hospital rate-setting**: Maryland is the only state where the Health Services Cost Review Commission (HSCRC) sets hospital rates that every payer pays. There is no chargemaster discrimination, no insurer-negotiated discount, and no "uninsured patient pays 5x what Aetna pays" pattern. **Most price-gouging arguments do not apply to Maryland hospital charges.** Md. Code, Health-Gen. § 19-201 et seq.
2. **Strong statutory financial-assistance floor**: Md. Code, Health-Gen. § 19-214.1 requires every Maryland acute-care and chronic-care hospital to provide free care to patients at or below 200% FPL, reduced-cost care between 200-500% FPL, and a payment plan for uninsured patients up to 500% FPL. This is a statutory floor, not a voluntary IRS § 501(r) policy.
3. **Medical Debt Protection Act + Fair Medical Debt Reporting Act**: Md. Code, Health-Gen. § 19-214.2 (2021 MDPA) blocks lawsuits for debts ≤ $1,000, imposes a 180-day pre-suit waiting period, and bans adverse credit reporting in that window. HB 1020 (effective October 1, 2025) goes further by banning medical-debt reporting to credit bureaus entirely.

Use this pack against the federal No Surprises Act layer; layer where it adds protection, override where it conflicts.

## All-payer rate-setting (the headline distinctive feature)

- **Statute:** **Md. Code, Health-Gen. § 19-201 et seq.** (HSCRC enabling statute), with rate-setting authority at **§ 19-207** and **§ 19-219**
- **Source:** [hscrc.maryland.gov/Pages/About-Us.aspx](https://hscrc.maryland.gov/Pages/About-Us.aspx); [hscrc.maryland.gov/documents/pdr/GeneralInformation/MarylandAll-PayorHospitalSystem.pdf](https://hscrc.maryland.gov/documents/pdr/GeneralInformation/MarylandAll-PayorHospitalSystem.pdf); [commonwealthfund.org Maryland All-Payer Approach](https://www.commonwealthfund.org/publications/newsletter-article/maryland-all-payer-approach-nonpayment)
- **Substance:** Maryland has, since 1971, operated the only state-set all-payer hospital rate system in the US. Every payer, Medicare, Medicaid, commercial insurers, self-insured employer plans, and uninsured patients, pays the same HSCRC-approved rate for the same service at a given hospital. No chargemaster, no negotiated discount, no "list price" markup. Effective July 1, 1977, HSCRC obtained a federal Medicare waiver, currently administered under the AHEAD Model (CMS agreement signed November 1, 2024, successor to the TCOC Model).
- **What this means for the kit:**
  - The normal "you charged me $50,000 but Aetna pays you $8,000 for the same procedure" argument does **not** work in Maryland. Hospital rates are not differentiated by payer.
  - Price-disparity disputes shift from "compare to negotiated rates" to "compare to the HSCRC-approved rate for the specific facility and CPT/DRG." HSCRC publishes approved rates; mismatches between billed and approved are the real lever.
  - The kit's letters for MD hospital bills should pivot from market-rate comparison to **HSCRC compliance**, asking the hospital to confirm each line item matches its current HSCRC-approved rate.
- **Important scope limit:** All-payer applies to **hospital** services (inpatient, outpatient, ER) at HSCRC-regulated facilities. **Physician professional fees, ambulance, freestanding ambulatory-surgery centers, and post-acute care are not under HSCRC.** A hospital bill is HSCRC-rate-set; the surgeon's bill that comes separately is not.
- **No private right of action against rate violations.** Patients raise HSCRC rate compliance with the Commission itself, with the hospital's billing department citing § 19-207, or as a defense if the hospital sues. HSCRC complaint contact: [hscrc.maryland.gov](https://hscrc.maryland.gov/).

## Hospital itemization right

- **Statute:** **Md. Code, Health-Gen. § 19-214.1** (financial assistance policy + patient information sheet); **COMAR 10.07.01** patient bill of rights (hospital licensing regs); **COMAR 10.37.10.26** (HSCRC patient rights and obligations)
- **Source:** Md. Code, Health-Gen. § 19-214.1 at [mgaleg.maryland.gov section=19-214.1](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=ghg&section=19-214.1&enactments=false); [findlaw.com Md. Health-Gen. § 19-214.1](https://codes.findlaw.com/md/health-general/md-code-health-gen-sect-19-214-1/); [COMAR 10.07.01 patient rights via Cornell LII](https://www.law.cornell.edu/regulations/maryland/COMAR-10-07-01-36); [COMAR 10.37.10.26](https://www.law.cornell.edu/regulations/maryland/COMAR-10-37-10-26)
- **What it requires:**
  - The hospital's patient information sheet must include "patient rights and obligations regarding hospital billing" and disclose that physician charges are billed separately.
  - Under COMAR 10.07.01 (hospital licensing) and HSCRC regs at COMAR 10.37.10.26, hospitals must make a **fully itemized billing statement, including date of service and unit charge, available on request of the patient**.
  - Patients also have the right to **a written estimate of total charges** for non-emergency services, procedures, and supplies before the encounter.
  - Notice of the patient information sheet (and financial assistance policy) must be provided before discharge and in each collection communication.
- **Scope:** Acute-care and chronic-care hospitals regulated by HSCRC. Outpatient services billed by hospital are covered; physician practice billing is governed by other rules (COMAR 10.32 and AG consumer protection authority).
- **Caveat:** Unlike Georgia, the right is **on request**, not automatic delivery within a deadline. The kit should always include an itemized-billing demand by certified mail to create the paper trail.
- **ERISA:** Not preempted, regulates the provider, not the plan.

## Maryland Consumer Protection Act (the strongest provider-side lever)

- **Statute:** **Md. Code, Com. Law § 13-101 et seq.** (Maryland Consumer Protection Act); private right of action at **§ 13-408**
- **Source:** [mgaleg.maryland.gov Com. Law § 13-101](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcl&section=13-101&enactments=false); private cause of action at [law.justia.com Md. Com. Law § 13-408](https://law.justia.com/codes/maryland/commercial-law/title-13/subtitle-4/section-13-408/)
- **Substance:** Prohibits "unfair, abusive, or deceptive trade practices" in the sale or offer for sale of consumer goods, services, realty, or credit. Coverage includes false or misleading representations, failure to state material facts, deceptive billing, and many practices commonly seen in medical billing disputes (charging for services not rendered, upcoding, misrepresenting in-network status, deceptive collection communications).
- **Private right of action (§ 13-408):**
  - "Any person may bring an action to recover for injury or loss sustained ... as the result of a practice prohibited by this title."
  - **Actual damages plus reasonable attorney's fees** are recoverable. Bad-faith or frivolous filings expose the plaintiff to fees.
  - No administrative-exhaustion prerequisite; the consumer can file directly in District or Circuit Court.
- **Critical caveat, the medical-services carve-out:** Under § 13-104(1) and case law (e.g., Hogan v. Md. State Dental Ass'n, Md. Court of Appeals authority), a CPA action **may not be brought to recover for injuries sustained as a result of the professional services provided by a health care provider**. Billing and collection conduct is generally treated as commercial/administrative, not "professional services," and remains actionable, but malpractice-flavored claims are excluded. **Plead carefully: frame as deceptive billing, deceptive collection, false representation, not as a quality-of-care complaint.**
- **Why it matters:** The CPA reaches the **hospital itself, the physician practice, and any debt collector**, original creditors included. Attorney's-fees recovery makes the case economically realistic for the patient. This is Maryland's closest equivalent to Georgia's FBPA private right of action.
- **ERISA:** Provider-side claims (against hospitals, doctors, collectors) are not preempted because the conduct is not "relating to" an ERISA plan. CPA claims against insurers regulated by Maryland may overlap with the Insurance Article; route insurer disputes through MIA first (see § 27-303 below).

## Unfair Claim Settlement Practices Act

- **Statute:** **Md. Code, Ins. § 27-303** (listed unfair practices); **§ 27-304** (general-business-practice violation, broader liability); administrative-only enforcement except through the § 27-1001 → § 3-1701 pathway below
- **Source:** [law.justia.com Md. Ins. § 27-303](https://law.justia.com/codes/maryland/insurance/title-27/subtitle-3/section-27-303/); [mgaleg.maryland.gov Ins. § 27-303 PDF](https://mgaleg.maryland.gov/2022RS/Statute_Web/gin/27-303.pdf)
- **Substance:** Prohibits insurers, nonprofit health service plans, and HMOs from misrepresenting policy provisions, refusing to pay claims for arbitrary or capricious reasons, failing to settle promptly when liability is clear, failing to provide a reasonable explanation for denial, attempting to settle based on altered applications without consent, and similar practices.
- **Private right of action:**
  - **No direct private right of action** under § 27-303 itself; Maryland courts treat it as administratively enforced by the Insurance Commissioner.
  - **Indirect lever**: a § 27-303 violation can be the predicate for the administrative-then-judicial bad-faith pathway under Ins. § 27-1001 → Cts. & Jud. Proc. § 3-1701 (next section), which **does** carry actual damages, attorney's fees, and interest.
  - The Maryland Insurance Administration investigates § 27-303 complaints and may impose administrative penalties, order claim payment, and refer patterns of conduct to the Attorney General.
- **Use:** Cite § 27-303 violations explicitly in the MIA complaint and in the § 27-1001 administrative filing. Do not plead § 27-303 as a standalone count in litigation.

## Bad-faith failure to pay

- **Statute:** **Md. Code, Cts. & Jud. Proc. § 3-1701** (judicial remedy) paired with **Md. Code, Ins. § 27-1001** (administrative prerequisite)
- **Source:** [law.justia.com Md. Cts. & Jud. Proc. § 3-1701](https://law.justia.com/codes/maryland/courts-and-judicial-proceedings/title-3/subtitle-17/section-3-1701/); [findlaw.com Md. Cts. & Jud. Proc. § 3-1701](https://codes.findlaw.com/md/courts-and-judicial-proceedings/md-code-cts-and-jud-proc-sect-3-1701.html); [law.justia.com Md. Ins. § 27-1001](https://law.justia.com/codes/maryland/2017/insurance/title-27/subtitle-10/section-27-1001/); MIA overview at [insurance.maryland.gov insurer-good-faith-requirements](https://insurance.maryland.gov/Pages/insurer-good-faith-requirements.aspx)
- **Substance:** A first-party insured may recover **actual damages (capped at the policy limit), expenses and litigation costs including reasonable attorney's fees, and interest** when the insurer fails to act in good faith on a covered claim.
- **"Good faith" definition:** "An informed judgment based on honesty and diligence supported by evidence the insurer knew or should have known at the time the insurer made a decision on a claim." Less demanding than Georgia's "frivolous and unfounded" standard.
- **Procedural requirements (this is the part that trips most plaintiffs):**
  - File a complaint with the **Maryland Insurance Administration (MIA)** under Ins. § 27-1001 **first**.
  - Include all proof-of-loss documents, the applicable coverage, the claim amount, and the actual damages alleged.
  - The insurer has **30 days** to respond.
  - The MIA issues a decision; only then can a § 3-1701 civil action be filed in court.
- **Scope, what it covers:**
  - First-party claims under **property and casualty policies** and **individual disability policies**.
  - **Health insurance** sits in a more limited posture, the § 27-1001 / § 3-1701 framework historically targeted first-party P&C and individual disability; many MD courts have read this narrowly. For health-claim denials, the strongest avenues remain (a) MIA complaint under § 27-303, (b) the carrier's internal appeal then external review process, and (c) any contract or breach-of-contract action under the policy.
- **Exhaustion exceptions:** MIA exhaustion is waived if (1) the dispute is within District Court small-claims jurisdiction ($5,000 or less), (2) the parties agree to waive, or (3) the policy limit exceeds $1,000,000 on a commercial policy.
- **Damages cap:** Actual damages may not exceed the policy limit. **Attorney's fees may not exceed one-third of actual damages recovered.**
- **ERISA preemption:** § 3-1701 is preempted as applied to self-funded ERISA employer plans. For self-funded plans, the federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) attorney's fees, no state bad-faith remedy.

## Balance billing and surprise medical bills (MD-regulated plans only)

- **Statutes and regulations:** Md. Code, Ins. **Title 15** (health insurance) with HMO-specific provisions; HSCRC all-payer model implements no-balance-billing as a structural feature for hospital services; federal No Surprises Act (45 C.F.R. Part 149) layers on top.
- **Source:** [insurance.maryland.gov Federal No Surprises Act (Maryland summary)](https://insurance.maryland.gov/Consumer/Pages/Federal-No-Surprises-Act.aspx); [umms.org No Surprises Act + MD protections](https://www.umms.org/patients-visitors/hospital-charges/no-surprises-act)
- **What it covers:**
  - **HMO plans governed by Maryland law:** balance billing prohibited for covered services, **including ground ambulance**. Md. HMO law has prohibited balance billing of HMO enrollees for decades.
  - **PPO/EPO plans governed by Maryland law:** when hospital-based or on-call physicians accept assignment-of-benefits payment from the insurer, they may **not** balance bill for covered services and may not ask the patient to waive that protection.
  - **Fully-insured plans** in an ER setting: state-law balance-billing protections apply on top of the federal NSA.
  - **Hospital services across all payers:** because Maryland operates the all-payer model, hospitals are paid the HSCRC-approved rate and the structural "out-of-network markup" problem does not exist at the facility-fee level. This is unique nationwide.
- **What it does not cover:**
  - **Self-funded ERISA employer plans** are not governed by Md. Code, Ins. Title 15. They rely on the federal NSA only.
  - **Air ambulance** is covered by the federal NSA, not by separate Maryland statute.
  - **Out-of-state providers billing Maryland residents** for services rendered outside Maryland fall outside MD jurisdiction.
- **Federal interaction:** Where MD law is silent (e.g., ERISA self-funded), federal NSA controls. Where both apply, the higher patient protection wins, MD's HMO rules are often broader.

## Regulatory agencies

### Maryland Insurance Administration (MIA)

- **Online complaint portal:** [enterprise.insurance.maryland.gov/consumer](https://enterprise.insurance.maryland.gov/consumer/) (Enterprise Complaint Tracking System); landing page at [insurance.maryland.gov/Consumer/pages/fileacomplaint.aspx](https://insurance.maryland.gov/Consumer/pages/fileacomplaint.aspx)
- **Phone:** main **(410) 468-2000**; toll-free **1-800-492-6116**; TTY **1-800-735-2258**
- **Mail:**
  > Maryland Insurance Administration
  > Attn: Consumer Complaint Investigation, Life and Health / Appeals and Grievance
  > 200 St. Paul Place, Suite 2700
  > Baltimore, MD 21202
- **Fax:** (410) 468-2270 (Appeals and Grievance) / (410) 468-2260 (Life and Health)
- **Authority:** all insurance carriers licensed in Maryland, including fully-insured health insurers, HMOs, PPOs, nonprofit health service plans (CareFirst), Medicare supplement. Administers the bad-faith framework under Ins. § 27-1001 (administrative prerequisite to § 3-1701) and the UCSPA at Ins. § 27-303. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272); coordinate with the Attorney General's People's Insurance Counsel Division for consumer-side advocacy.

### Maryland Attorney General, Consumer Protection Division (CPD)

- **Online complaint portal:** [portal.oag.state.md.us/cpdportal](https://portal.oag.state.md.us/cpdportal/?q=Home)
- **Phone:** main **(410) 576-6300**; Spanish **(410) 230-1712**; toll-free **1-888-743-0023**
- **Mail:**
  > Office of the Attorney General, Consumer Protection Division
  > 200 St. Paul Place
  > Baltimore, MD 21202
- **Authority:** enforces the Maryland Consumer Protection Act (Md. Code, Com. Law § 13-101 et seq.), the Maryland Consumer Debt Collection Act, and related deceptive-practice statutes. Reach over hospitals, physician practices, third-party debt collectors, **and original creditors**. The CPD's **Health Education and Advocacy Unit** (HEAU) is the Maryland-specific consumer-side body that helps patients navigate billing disputes, appeals, and financial-assistance claims under Md. Code, Health-Gen. § 19-214.1 reconsideration rights. Distinctively Maryland: HEAU sits inside the AG, not the Department of Health.

## Small claims, Maryland District Court

- **Court name:** **District Court of Maryland**, Small Claims docket (one per county)
- **Jurisdictional limit:** **$5,000** for small claims, codified at **Md. Code, Cts. & Jud. Proc. § 4-405**
- **Source:** [law.justia.com Md. Cts. & Jud. Proc. § 4-405](https://law.justia.com/codes/maryland/courts-and-judicial-proceedings/title-4/subtitle-4/section-4-405/); [mdcourts.gov/legalhelp/smallclaims](https://www.mdcourts.gov/legalhelp/smallclaims); current fee schedule at [mdcourts.gov DCA-109](https://www.mdcourts.gov/sites/default/files/court-forms/dca109_10.2024wm.pdf)
- **Filing fees:** Small claims (≤ $5,000) filing fee per the DCA-109 cost schedule (verify current value before filing; was **$36** for ≤ $5,000 small claims as of the October 2024 schedule). Service-of-process by certified mail, sheriff, or constable adds a separate fee.
- **Attorney rules:** permitted but not required. Designed for pro se litigants; simplified pleadings, relaxed evidence rules. **Corporations and LLCs may appear through an officer or full-time employee in small claims** (Md. Rule 3-201), useful for patients facing a hospital that may send a billing-office employee rather than counsel.
- **Above $5,000 up to $30,000:** District Court still has jurisdiction but the case proceeds as a regular civil action with formal discovery and stricter evidence rules. Above $30,000, file in Circuit Court.
- **Jury trial:** not available in District Court. Either party may demand a jury for claims over $20,000 by removing the case to Circuit Court (Md. Code, Cts. & Jud. Proc. § 4-402(e)).
- **Affidavit judgment** available where the claim is supported by sworn documentation (Md. Rule 3-306), efficient for liquidated medical-bill counterclaims.

## Statute of limitations

- **Default (most contracts, including unsealed medical billing):** **3 years from accrual** under **Md. Code, Cts. & Jud. Proc. § 5-101**
- **Specialty (contracts under seal):** **12 years** under § 5-102 (rare; requires the formal "under seal" execution, almost never present in hospital paperwork)
- **Source:** [law.justia.com Md. Cts. & Jud. Proc. § 5-101](https://law.justia.com/codes/maryland/courts-and-judicial-proceedings/title-5/subtitle-1/section-5-101/); [peoples-law.org statute-limitations](https://www.peoples-law.org/statute-limitations)

Maryland is a **short-SOL state**. Three years runs from the date the cause of action accrues, which for unpaid medical bills is typically the day payment was due. This is materially shorter than Georgia (6 yr written / 4 yr open account), so MD defendants have a stronger time-bar defense against old hospital bills.

Partial payment, written acknowledgment, or a new promise to pay can restart the clock under common-law principles. **Do not make a partial payment on a time-barred debt without legal advice.** Contractual provisions shortening the SOL further may be enforceable if reasonable.

## Ground ambulance balance billing

Maryland's ground-ambulance protection is **structurally different** from Georgia's, because of the HMO and assignment-of-benefits framework:

- **HMO enrollees governed by Maryland law:** balance billing for ground ambulance is prohibited under longstanding HMO law, treated as a covered service that must be paid in full by the HMO.
- **PPO/EPO enrollees governed by Maryland law:** if the ground-ambulance provider accepts assignment of benefits from the carrier, no balance billing of the patient.
- **Local-government ground ambulance** (most jurisdictions in MD use county fire/EMS): when the local-government provider accepts assignment of benefits from a Maryland-regulated plan, the patient may not be balance billed.
- **No single "Maryland Ground Ambulance Balance Billing Act"** has been enacted under the "Md. Code, Ins. § 15-1632" citation; the protections live in the HMO subtitle (Ins. Title 15, Subtitle 1) and individual contract provisions. **Re-verify the precise statute by enrollment type** before citing in a letter.
- **Federal No Surprises Act:** does **not** cover ground ambulance. This is the one major area where Maryland-regulated patients are better-protected than the federal floor, but only for state-regulated plans.
- **ERISA-preempted for self-funded employer plans**: those rely on federal NSA gaps, which leave ground ambulance largely unprotected.

For the LLM: when a Maryland patient presents a ground-ambulance bill, **first determine plan type** (HMO / PPO / EPO / self-funded ERISA / Medicare / Medicaid), then route to the correct protection.

## Credit reporting, Maryland Fair Medical Debt Reporting Act

- **Statute:** **HB 1020 (2025 session), Maryland Fair Medical Debt Reporting Act**, codified in Maryland Commercial Law Article; effective **October 1, 2025**
- **Source:** [mgaleg.maryland.gov HB1020 details](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/HB1020); [HB 1020 enrolled text](https://mgaleg.maryland.gov/2025RS/bills/hb/hb1020e.pdf); MD OFR guidance at [natlawreview.com Maryland OFR guidance](https://natlawreview.com/article/maryland-ofr-issues-guidance-new-medical-debt-collection-laws); commentary at [mdaccesstojustice.org Fair Medical Debt Reporting Act](https://www.mdaccesstojustice.org/news-insights/ending-the-credit-crisis-of-illness-the-fair-medical-debt-reporting-act/)
- **Substance:**
  - Medical providers, their agents, and debt collectors **may not disclose any portion of a medical debt to a consumer reporting agency**.
  - Consumer reporting agencies **may not create, furnish, or maintain a report containing adverse information that the agency knows or should know relates to medical debt**.
  - Any post-October 1, 2025 contract between a provider and a collector for sale or collection of medical debt must include a no-credit-reporting provision; a contract without it is **void and unenforceable**.
  - The law does **not** cancel medical debt or eliminate the patient's obligation to pay; it only bars the credit-reporting channel.
- **Note on the user's original cite ("HB 1020 / SB 957, 2024"):** the **2024** version of this legislation did not pass; the version that did pass and took effect is the **2025 session HB 1020**. Cite the 2025 act, effective October 1, 2025.
- **Older but related law (still good law):** **Md. Code, Health-Gen. § 19-214.2 (Medical Debt Protection Act, 2021 HB 565 / SB 514)** prohibits a hospital from reporting adverse information to a consumer reporting agency or filing a civil action for at least **180 days** after the initial bill is issued. § 19-214.2 specifically targets hospital debt, while HB 1020 covers all medical debt.
- **Federal preemption posture:** the CFPB's October 2025 interpretive rule asserting FCRA preemption of state medical-debt credit-reporting restrictions remains contested. If it is upheld, it may limit HB 1020's reach for entries furnished to nationwide CRAs; Maryland's contract-voiding provision likely survives because it regulates the underlying provider-collector relationship, not the CRA directly.
- **Source:** [HB 565 (2021) Medical Debt Protection Act](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/SB0514?ys=2021RS); analysis at [publicjustice.org medical debt protection act passes](https://www.publicjustice.org/en/news/the-medical-debt-protection-act-passes/)

## Hospital charity care (statutory floor)

- **Statute:** **Md. Code, Health-Gen. § 19-214.1** (financial assistance policy), with debt-collection obligations at **§ 19-214.2** (Medical Debt Protection Act)
- **Source:** [Md. Code, Health-Gen. § 19-214.1 mgaleg](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=ghg&section=19-214.1&enactments=false); [findlaw.com § 19-214.1](https://codes.findlaw.com/md/health-general/md-code-health-gen-sect-19-214-1/); [dollarfor.org/state_sheet/maryland](https://dollarfor.org/state_sheet/maryland/)
- **Mandatory minimums every HSCRC-regulated acute-care and chronic-care hospital must provide:**
  - **Free medically necessary care** to patients with family income at or below **200% of the federal poverty level (FPL)**.
  - **Reduced-cost medically necessary care** to patients with family income above 200% FPL, calculated at the time of service or updated to reflect a financial-circumstances change within **240 days** after the initial bill.
  - **Payment plan** available to uninsured patients with family income between **200% and 500% FPL**.
  - **Reduced-cost medically necessary care** to patients below **500% FPL who have a financial hardship** (a separate threshold from the 200%/240-day rule).
  - Notice of the financial assistance policy **before discharge** and in **every collection communication**.
  - Patient information sheet posted in conspicuous places throughout the hospital in at least 10-point type, in simplified language, and in languages spoken by limited-English-proficient populations of at least 5% of the service area.
- **Reconsideration right:** patients may request reconsideration of denied financial assistance; the Health Education and Advocacy Unit (HEAU) in the AG's office assists.
- **Medical Debt Protection Act overlay (§ 19-214.2):**
  - Hospital may not file a collection lawsuit for at least **180 days after the initial bill**.
  - Hospital may not file a lawsuit for any debt of **$1,000 or less**.
  - Hospital must send a **45-day written notice of intent to sue** by certified and first-class mail, in simplified language and at least 10-point type.
  - Hospital must determine whether the patient is eligible for financial accommodations before suing.
  - Complaint to collect must include an itemized statement of remaining debt, an affidavit, a copy of the most recent bill, and other specified documents.
- **Use Dollar For at [dollarfor.org/state_sheet/maryland](https://dollarfor.org/state_sheet/maryland/) for screening.** Maryland's statutory floor is more aggressive than federal § 501(r), and HEAU + reconsideration creates a real administrative path.

## Hospital lien statute

- **Statute:** **Md. Code, Com. Law § 16-601 et seq.** (Hospital's Lien)
- **Source:** [law.justia.com Md. Com. Law § 16-601](https://law.justia.com/codes/maryland/commercial-law/title-16/subtitle-6/section-16-601/); [mgaleg.maryland.gov § 16-601](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gcl&section=16-601)
- **Substance:**
  - A hospital that furnished medical services to a patient injured in an accident **not covered by Maryland Workers' Compensation** has a lien on **50% of the recovery** the patient (or estate) collects in judgment, settlement, or compromise of a third-party claim.
  - The lien secures "reasonable and necessary" charges, **capped at the rate the Workers' Compensation Commission allows** for the same services.
  - The lien is **subordinate to the attorney's lien** for professional services in collecting damages.
- **Perfection:** file a notice of lien with the **clerk of the circuit court of the county where the services were rendered**. Maryland's perfection requirements are lighter than Georgia's, no statutory 15-day pre-filing notice to the patient.
- **What the lien does not reach:** the patient's home, wages, bank account, or any source of recovery other than the third-party tort claim. It is **not a general medical-debt lien**.
- **The user's cite "§ 16-601.1" does not exist as a separate codified section**; the operative provision is § 16-601 with related sections § 16-602 (priority), § 16-603 (notice/enforcement). Cite **§ 16-601** as the umbrella, with subordinate citations as applicable.

## Maryland-specific patient advantages

When triaging a Maryland patient's bills, keep these in mind:

1. **HSCRC all-payer rates**: the "you charged me more than what insurers pay" line of attack does not work in MD because rates are uniform across all payers. Pivot to **HSCRC-rate compliance**: ask the hospital to confirm that each line item matches the HSCRC-approved rate for that facility and DRG/CPT.
2. **Mandatory statutory financial assistance**: § 19-214.1 floors are higher and more enforceable than the federal § 501(r) defaults. **Always screen for 200% / 500% FPL eligibility before any settlement discussion.** Reconsideration is a real path; HEAU helps.
3. **180-day pre-suit window and $1,000 lawsuit floor**: § 19-214.2 makes it economically irrational for a hospital to sue on small bills (≤ $1,000 absolutely barred; ≤ a few thousand impractical given the 45-day notice + 180-day delay + financial-assistance-eligibility determination prerequisites). Use this to slow-walk small disputed bills.
4. **HEAU inside the AG's office**: unique consumer-side advocate that lives in the Office of the Attorney General, not the Department of Health. HEAU intervenes in hospital billing and insurance disputes and is more user-friendly than MIA or HSCRC for first-stop complaints.
5. **CPA private right of action + attorney's fees**: Md. Com. Law § 13-408 makes fee recovery realistic for deceptive-billing claims, original creditors included. Cite in any 30-day demand letter against a Maryland provider's billing department.
6. **Short 3-year SOL**: many old hospital bills are already time-barred under Cts. & Jud. Proc. § 5-101. Compute the SOL from the date payment was due (typically the bill's due date), not the date the debt was sold to a collector.
7. **HMO ground-ambulance protection (state-regulated only)**: HMO enrollees should never be balance-billed for ground ambulance. PPO/EPO enrollees with assignment-of-benefits ambulance providers also protected.
8. **Medical-debt credit-reporting ban (HB 1020, effective October 1, 2025)**: any medical-debt entry on a Maryland resident's credit report after that date is presumptively unlawful. Dispute via § 1681i of the FCRA and reference HB 1020 in the dispute letter.

## Quick reference for letter rendering

When the LLM renders a Maryland-bound letter, substitute these defaults:

- **State statute (itemization right):** request under **Md. Code, Health-Gen. § 19-214.1**, **COMAR 10.07.01**, and **COMAR 10.37.10.26**. Itemization is provided **on request**, not automatically; send certified mail to create the paper trail.
- **State rate-setting cite (when challenging hospital line items):** **Md. Code, Health-Gen. § 19-201 et seq.** and the HSCRC-approved rate schedule for the specific facility. Ask for confirmation each line matches the HSCRC-approved unit price.
- **State consumer protection statute (provider-side disputes):** **Md. Code, Com. Law § 13-101 et seq.** with **§ 13-408** private right of action (actual damages + attorney's fees). Plead as deceptive billing or deceptive collection, not as a quality-of-care claim.
- **State insurance department (CC line):** Maryland Insurance Administration, Consumer Complaint Investigation, 200 St. Paul Place, Suite 2700, Baltimore, MD 21202 ([insurance.maryland.gov](https://insurance.maryland.gov))
- **State AG consumer protection (CC line):** Office of the Attorney General, Consumer Protection Division, 200 St. Paul Place, Baltimore, MD 21202 ([marylandattorneygeneral.gov](https://www.marylandattorneygeneral.gov/Pages/CPD/default.aspx)); for billing-specific assistance, **Health Education and Advocacy Unit (HEAU)** at the same address.
- **Small-claims court name:** **District Court of Maryland for [county/Baltimore City]**, small-claims docket
- **Small-claims limit (in 30-day warning):** **$5,000** under Md. Code, Cts. & Jud. Proc. § 4-405
- **Filing fee (in 30-day warning):** approximately **$36** for small claims per the District Court Cost Schedule DCA-109 (verify current)
- **Statute of limitations (in 30-day warning):** **Md. Code, Cts. & Jud. Proc. § 5-101 (three years from accrual)**
- **For hospital debt collection disputes:** cite **Md. Code, Health-Gen. § 19-214.2** (Medical Debt Protection Act, 180-day pre-suit period, $1,000 floor, 45-day notice requirement) alongside the federal FDCPA.
- **For credit-reporting disputes (entries dated on or after October 1, 2025):** cite **Maryland Fair Medical Debt Reporting Act (HB 1020, 2025 session)** and federal FCRA 15 U.S.C. § 1681i.
- **For ground ambulance balance bills:** route by plan type: HMO governed by Md. law (Md. Code, Ins. Title 15 Subtitle 1, balance billing prohibited); PPO/EPO with assignment-of-benefits (balance billing prohibited); self-funded ERISA (federal NSA only, no ground-ambulance protection).
- **For bad-faith insurance disputes:** file MIA complaint under **Md. Code, Ins. § 27-1001** **first** (administrative prerequisite), then civil action under **Md. Code, Cts. & Jud. Proc. § 3-1701** for actual damages, expenses, attorney's fees (capped at 1/3 of damages), and interest. Note narrow application to first-party P&C and individual disability; health-claim denials use § 27-303 + carrier appeals + external review.
