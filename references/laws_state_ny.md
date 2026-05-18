# New York state pack

The fully-worked state-law layer for New York patients. The LLM uses this when the patient's state is New York. Tennessee equivalent at [`laws_state_tn.md`](laws_state_tn.md); Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Three things make New York's patient-side leverage unusually strong:

1. The **Fair Medical Debt Reporting Act** (effective Dec 13, 2023) bans medical debt from credit reports outright. No grace period, no dollar threshold — flat prohibition on furnishers and CRAs.
2. The **Hospital Financial Assistance Law** (PHL § 2807-k(9-a), expanded 2024) requires every general hospital licensed by NY (not just non-profits) to offer sliding-scale FA up to 400% FPL, plus a 180-day moratorium on suing for medical debt and a 5%-of-income payment-plan cap.
3. The **Consumer Credit Fairness Act** (effective Apr 7, 2022) cut the statute of limitations for consumer credit (including medical-debt) actions from 6 years to **3 years** under CPLR § 214-i, and partial payment no longer restarts the clock.

Treat these three as the structural headlines in any NY dispute strategy.

## Hospital itemization right

- **Statute:** **N.Y. Pub. Health Law § 2831** (consolidated itemized hospital bills); related patient-rights provisions at **§ 2803(1)(g)** and the NY Hospital Patients' Bill of Rights
- **Sources:** [codes.findlaw.com/ny/public-health-law/pbh-sect-2831](https://codes.findlaw.com/ny/public-health-law/pbh-sect-2831/); [health.ny.gov/publications/1500](https://www.health.ny.gov/publications/1500/)
- **What it requires:**
  - After discharge, release, or completion of treatment, the general hospital must furnish a **consolidated itemized bill** within **seven (7) days** of discharge or of the patient's request, whichever is later.
  - The bill must consolidate all charges for one hospital visit, label each charge as paid, assigned to an insurer, or owed by the patient, and identify the date and provider of each service.
  - Patients have an independent statutory right under § 2803(1)(g) to receive an itemized bill and an explanation of all charges.
- **Scope:** General hospitals licensed under Article 28. Outpatient-only physician practices are not bound by § 2831 itself but are bound by federal price-transparency rules and by the federal Good Faith Estimate requirement for uninsured/self-pay patients.
- **N.Y. Pub. Health Law § 18 is a different statute** — it governs patient access to **medical records** (and limits charges to ~75¢/page), not itemized bills. Cite § 2831 for itemization; cite § 18 only when the dispute concerns medical-record copies.

Use § 2831 as the citation in `templates/letter_itemization_request.md` for any New York patient.

## Unfair Claim Settlement Practices Act

- **Statute:** **N.Y. Ins. Law § 2601**
- **Sources:** [codes.findlaw.com/ny/insurance-law/isc-sect-2601](https://codes.findlaw.com/ny/insurance-law/isc-sect-2601/); [law.justia.com/codes/new-york/2014/isc/article-26](https://law.justia.com/codes/new-york/2014/isc/article-26/)
- **Substance:** Prohibits insurers from knowingly misrepresenting policy provisions, failing to acknowledge claims promptly, failing to adopt reasonable investigation standards, and failing to attempt in good faith to effectuate prompt, fair, and equitable settlements where liability has become reasonably clear.
- **Critical caveat:** **No private right of action.** The New York Court of Appeals has repeatedly held that § 2601 is enforced solely by the Superintendent of the Department of Financial Services. Cite § 2601 in a DFS complaint, not as a standalone cause of action in court. A 2025 bill (S166-A) would create a private right of action under a new § 2601-a; status pending as of this writing — verify before relying on it.
- **Use:** Always file the DFS complaint citing § 2601 in parallel with any litigation strategy. The DFS complaint is free, generates a paper trail, and frequently moves the carrier in ways litigation cannot.

## Bad-faith failure to pay

- **Posture:** New York has **no first-party bad-faith statute** comparable to Georgia's O.C.G.A. § 33-4-6 or Tennessee's § 56-7-105. The remedy is **common-law only**, and the standard is materially harder to meet than in California, Texas, or Georgia.
- **Sources:** *Pavia v. State Farm*, 82 N.Y.2d 445 (1993); *Bi-Economy Mkt., Inc. v. Harleysville Ins. Co.*, 10 N.Y.3d 187 (2008); [lbcclaw.com/assets/uploads/pdfs/Insurance-Coverage-Review-Bad-Faith-Under-NY-Law.pdf](https://lbcclaw.com/assets/uploads/pdfs/Insurance-Coverage-Review-Bad-Faith-Under-NY-Law.pdf)
- **Standard:** *Pavia* requires the insured to show the insurer's conduct constituted a "**gross disregard**" of the insured's interests — more than negligence, more than ordinary breach. *Bi-Economy* did not create a freestanding bad-faith tort; it held that consequential damages reasonably foreseeable at contracting are recoverable for breach of the implied covenant of good faith and fair dealing.
- **Damages:** Compensatory (policy proceeds, interest, plus *Bi-Economy* consequential damages). **No statutory penalty.** Punitives are theoretically available but require conduct aimed at the public generally, not just the policyholder, under *Rocanova v. Equitable Life Assurance Soc'y*, 83 N.Y.2d 603 (1994) — practically unattainable in a single-claim health-insurance dispute.
- **No-attorney's-fees default:** New York follows the American Rule; fees are not recoverable for bad faith absent contract or statute.
- **ERISA preemption:** as elsewhere, common-law bad-faith claims against self-funded ERISA employer plans are preempted. The federal remedy is 29 U.S.C. § 1132(a)(1)(B).
- **Practical takeaway:** For NY insurer disputes, the **stronger lever is N.Y. Gen. Bus. Law § 349** (see "Other NY-specific patient-side advantages" below), which has a private right of action, statutory $50 minimum damages, treble damages up to $1,000 for willful violations, and attorney's fees. Pair § 349 with a DFS complaint citing Ins. Law § 2601.

## Surprise billing — Emergency Medical Services and Surprise Bills Law

- **Statutes:** **N.Y. Fin. Servs. Law Article 6 (§§ 601-608)**; companion provisions in **N.Y. Ins. Law §§ 3217-a, 3217-b, 3241, 3242, 4324** and **N.Y. Pub. Health Law § 24**. External-appeal mechanism at **N.Y. Ins. Law § 4914** / **N.Y. Pub. Health Law § 4914**.
- **Enacted:** Part H of Chapter 60 of the Laws of New York (2014), effective **March 31, 2015**. New York was the first state in the nation to enact comprehensive surprise-billing protection — predating the federal No Surprises Act by ~7 years.
- **Sources:** [health.ny.gov/regulations/public_health_law/surprise_bill_law/index.htm](https://health.ny.gov/regulations/public_health_law/surprise_bill_law/index.htm); [dfs.ny.gov/consumers/health_insurance/surprise_medical_bills](https://www.dfs.ny.gov/consumers/health_insurance/surprise_medical_bills); [law.justia.com/codes/new-york/fis/article-6/603](https://law.justia.com/codes/new-york/fis/article-6/603/)

### What it covers

- **Emergency services** from out-of-network (OON) providers at any hospital — patient pays in-network cost-sharing only.
- **Surprise bills** from OON providers at in-network hospitals or ambulatory surgical centers when (a) a participating provider was unavailable, (b) an OON provider rendered services without the patient's knowledge, or (c) unforeseen services were required.
- **Out-of-network referrals** by an in-network physician to an OON provider without proper written disclosure.
- **Ancillary services** (emergency medicine, anesthesia, pathology, radiology, laboratory, neonatology, assistant surgeon, hospitalist, intensivist) at in-network facilities.

### Independent Dispute Resolution (IDR)

- Patient signs a one-page **Assignment of Benefits / Hold-Harmless form** holding the patient harmless from any amount beyond in-network cost-share.
- Provider and insurer enter **baseball-style arbitration**. The IDR reviewer chooses between the provider's offer and the insurer's offer (no middle-ground splits). Determination within **30 days**.
- Patient is **not a party** to the IDR; the patient's only obligation is the in-network cost-share. The dispute is between the carrier and the provider.

### Ground ambulance

- The Surprise Bill Law and related Ins. Law provisions (§§ 3216(h)(24), 3221(l)(15), 4303(aa)) extend hold-harmless protection to **ground ambulance**: when an authorized insurer makes any payment toward an OON emergency ground-ambulance claim, the ambulance provider may not balance-bill the patient. If the insurer fully denies the claim, the ambulance provider may bill the patient, but the patient retains the right to challenge the bill.
- This closes the single biggest gap in the federal No Surprises Act, which excludes ground ambulance entirely.
- See also "Ground-ambulance protection" section below.

### How it interacts with the federal No Surprises Act (NSA)

- The NY state law applies to **fully-insured plans** issued or delivered in New York and to certain OON situations at NY hospitals regardless of plan type for the purposes of provider-patient hold-harmless.
- **Self-funded ERISA employer plans** are governed by the federal NSA (effective Jan 1, 2022), not by NY state law for cost-sharing determinations — although NY's hospital-side provider-conduct provisions (PHL § 24 disclosure rules, the hold-harmless form) still bind providers regardless of the patient's plan type.
- **Self-funded plans can opt into** NY's IDR via the federal NSA's "specified state law" framework; some do, most do not. Check the patient's plan documents.
- Where both apply, protections layer (NY's broader scope on ancillary services, NY's ground-ambulance hold-harmless) rather than displace.

### Caveats

- Excludes air ambulance (federal NSA covers it for fully-insured and self-funded alike).
- Excludes Medicare, Medicaid, and workers' compensation.
- The hold-harmless form is a paperwork prerequisite — providers occasionally fail to provide it; patients should request it in writing if not offered.

## External appeal / Independent Review Organization (IRO)

- **Statutes:** **N.Y. Ins. Law § 4914** and **N.Y. Pub. Health Law § 4914** (parallel provisions for insurer-regulated plans and HMO-regulated plans respectively)
- **Sources:** [law.justia.com/codes/new-york/isc/article-49/title-2/4914](https://law.justia.com/codes/new-york/isc/article-49/title-2/4914/); [dfs.ny.gov/complaints/file_external_appeal](https://www.dfs.ny.gov/complaints/file_external_appeal); [newyork.public.law/laws/n.y._insurance_law_section_4914](https://newyork.public.law/laws/n.y._insurance_law_section_4914)
- **Process:**
  - Trigger: a final adverse determination from the plan (or joint waiver of internal appeal) on a medical-necessity, experimental/investigational, out-of-network, or rare-disease denial.
  - **Filing window: 4 months** from the patient's receipt of the final adverse determination notice.
  - File via the DFS external-appeal portal or by mailing the DFS external-appeal application.
  - Assignment to a state-certified External Appeal Agent (IRO) — a different organization from the plan's internal reviewers.
  - **Standard decision: 30 days** (with up to 5 additional business days if the IRO requests more information).
  - **Expedited decision: 72 hours** (when delay would significantly increase risk to health or jeopardize ability to regain maximum function).
- **Filing fee:** Up to **$25 per appeal**, capped at **$75 per plan year**. Waived for Medicaid, Child Health Plus, Family Health Plus, or upon hardship attestation. **Returned if the IRO overturns the denial.**
- **Binding effect:** The IRO's decision is **binding on the plan**. The plan must implement coverage consistent with the determination. The decision is **not binding on the patient** — the patient may still pursue civil remedies, though as a practical matter overturned denials end the dispute.
- **Use:** Always exhaust the internal appeal first (the plan must give an internal appeal decision before the external clock can start, unless jointly waived). The external appeal is one of the highest-value patient tools NY offers — free or near-free, binding on the carrier, and decided by an independent third party.

## Regulatory agencies

### New York State Department of Financial Services (DFS)

- **Online complaint portal:** [dfs.ny.gov/complaint](https://www.dfs.ny.gov/complaint)
- **Phone:** main **(212) 480-6400** or **(518) 474-6600**; consumer assistance toll-free **1-800-342-3736**
- **Mailing addresses:**
  > NY State Department of Financial Services
  > Consumer Assistance Unit
  > 1 State Street, New York, NY 10004
  >
  > -- or --
  >
  > NY State Department of Financial Services
  > Consumer Assistance Unit
  > 1 Commerce Plaza, Albany, NY 12257
- **Fax:** (212) 480-6282
- **Authority:** all insurers and HMOs licensed in New York, including fully-insured health insurers, Medicare supplement, HMOs, surprise-billing protections, external appeals under Ins. Law § 4914. **No authority over self-funded ERISA plans** (route to U.S. DOL EBSA at 1-866-444-3272). Administers Ins. Law § 2601 enforcement.

### New York Attorney General — Health Care Bureau

- **Health Care Helpline (dedicated):** **1-800-428-9071**
- **Online complaint:** [ag.ny.gov/file-complaint/health-care](https://ag.ny.gov/file-complaint/health-care); web form at [pcf.ag.ny.gov/form/HCF](https://pcf.ag.ny.gov/form/HCF)
- **Bureau page:** [ag.ny.gov/bureau/health-care-bureau](https://ag.ny.gov/bureau/health-care-bureau)
- **Authority:** New York is unusual in having a dedicated AG Health Care Bureau (not just a generic consumer bureau routing health complaints). It handles disputes with providers, hospitals, insurers, debt collectors, and pharmacies, and routinely secures restitution — over $1.5M recovered for consumers in 2025. The intake specialist assigns a Bureau advocate or routes to the appropriate agency. Pair the Health Care Bureau complaint with a DFS filing for insurer disputes (Bureau pressures the provider/insurer relationship; DFS regulates the carrier).
- **Use this Bureau, not the generic Consumer Frauds line (1-800-771-7755), for any health-care billing dispute.** The Health Care Bureau has subject-matter expertise and historically delivers better outcomes than the generic consumer line.

### New York Attorney General — Consumer Frauds and Protection Bureau

- **Online complaint:** [ag.ny.gov/file-complaint/consumer](https://ag.ny.gov/file-complaint/consumer)
- **Phone:** **1-800-771-7755**
- **Use only when:** the complaint is not health-care-specific (debt collector misconduct unrelated to medical bills, etc.).

### New York State Department of Health (DOH)

- **Hospital complaints (facility/quality):** **1-800-804-5447** ([health.ny.gov/facilities/hospital/complaints.htm](https://www.health.ny.gov/facilities/hospital/complaints.htm))
- **Authority:** licensing and patient-care quality at NY-licensed hospitals. Does **not** handle billing disputes (route those to AG Health Care Bureau or DFS). Useful only when the dispute also implicates patient-care quality, sanitation, or facility licensure.

## Small claims court

- **Court names:** New York has two parallel small-claims tracks depending on geography:
  - **NYC Civil Court — Small Claims Part** (the five boroughs)
  - **City Court — Small Claims Part** (outside NYC, in cities)
  - **Town Court or Village Justice Court — Small Claims Part** (outside NYC, in towns and villages)
- **Jurisdictional limits:**
  - **NYC Civil Court Small Claims: $10,000** (raised from $5,000 in 2020)
  - **Other City Courts: $5,000**
  - **Town and Village Justice Courts: $3,000**
- **Source:** [nycourts.gov/courts/nyc/smallclaims/fees.shtml](https://ww2.nycourts.gov/courts/nyc/smallclaims/fees.shtml); [legalatoms.com/new-york/how-much-money-can-you-sue-for-in-new-york-small-claims-court](https://legalatoms.com/new-york/how-much-money-can-you-sue-for-in-new-york-small-claims-court/); [lawhelpny.org/resource/your-guide-to-small-claims-in-city-town-and-village-courts](https://www.lawhelpny.org/resource/your-guide-to-small-claims-in-city-town-and-village-courts)
- **Filing fees (NYC Civil Court Small Claims):**
  - Claims ≤ $1,000: **$15.00**
  - Claims > $1,000 to $5,000: **$20.00**
  - Filing fees in City/Town/Village courts vary but are typically $10-$20.
  - Fee waivers available on poor-person application.
- **Attorney rules:** Attorneys permitted but uncommon. Courts are designed for pro se litigants; rules of evidence are relaxed. Corporations and LLCs may appear through an authorized officer or employee.
- **Jury trial:** Not available on the small-claims side. Either party may demand removal to a regular civil docket, which restores the full civil rules (and admits a jury).
- **Service:** Court clerk mails the notice of claim by certified mail and first-class mail. Patient pays postage. Defendant must answer or appear.

**Heads up:** A 2025 NY Senate Bill (S2636) would raise the City/Town/Village limit to $10,000, matching NYC. Status pending as of this writing — verify before filing a claim between $3,000 and $10,000 outside NYC.

## Statute of limitations

- **Breach of written contract (general):** **6 years** from breach — **CPLR § 213(2)**
- **Breach of oral contract:** **6 years** from breach — same statute (NY is unusual; most states differentiate oral from written)
- **Consumer credit transactions (including medical debt sued upon by a provider, hospital, or assignee):** **3 years** from the date of breach — **CPLR § 214-i** (enacted by the Consumer Credit Fairness Act, effective April 7, 2022)
- **N.Y. Gen. Bus. Law § 349 (deceptive practices):** **3 years** from the date of injury — *Gaidon v. Guardian Life Ins. Co.*, 96 N.Y.2d 201 (2001)
- **Sources:** [law.justia.com/codes/new-york/cvp/article-2/213](https://law.justia.com/codes/new-york/cvp/article-2/213/); [legalservicesli.org/new-consumer-credit-debt-statute-of-limitations](https://legalservicesli.org/new-consumer-credit-debt-statute-of-limitations/)

**Critical NY-specific rule:** Under CPLR § 214-i and the Consumer Credit Fairness Act, **a partial payment on a consumer credit debt no longer restarts or revives the statute of limitations.** This is the opposite of the common-law default and is one of the strongest patient protections in the country. Even an acknowledgment in writing does not revive a time-barred consumer-credit claim. Patients can pay $10 toward an old medical bill in NY without resetting the clock — though there is rarely a reason to.

**Which statute applies to a medical bill?**

- When the **hospital or provider sues the patient directly** to collect an unpaid bill, courts have applied the **3-year CPLR § 214-i** clock as a "consumer credit transaction" because the patient assumes the obligation in a consumer context. This is the dominant posture post-2022.
- When the suit is on a **separately-signed written financial-responsibility contract** with explicit payment terms, an argument for the 6-year CPLR § 213(2) clock may be available to the provider, but the consumer-credit characterization typically controls.
- **For dispute letters: cite the 3-year § 214-i clock** as the applicable limitation period for any medical-debt collection action against a New York patient.

## Ground-ambulance protection

**Covered by New York state law** via the Emergency Medical Services and Surprise Bills Law (effective 2015) and the related Ins. Law amendments at **§§ 3216(h)(24), 3221(l)(15), 4303(aa)**. See "Surprise billing" above.

- **Statute:** N.Y. Ins. Law §§ 3216(h)(24), 3221(l)(15), 4303(aa); related provisions in N.Y. Fin. Servs. Law Article 6
- **Sources:** [pmc.ncbi.nlm.nih.gov/articles/PMC11911222](https://pmc.ncbi.nlm.nih.gov/articles/PMC11911222/) (peer-reviewed analysis of NY's ground-ambulance regulation); [patientfairness.com/new-york-state-medical-billing-consumer-protections](https://www.patientfairness.com/new-york-state-medical-billing-consumer-protections)
- **Substance:** Ground-ambulance providers may not balance-bill the patient when the authorized insurer or HMO has made any payment on the OON emergency claim. When the insurer fully denies, the ambulance provider may bill the patient, but the patient retains right to challenge.
- **Note on PHL § 4906:** The prompt referenced "N.Y. Pub. Health Law § 4906 effective 2022" — that specific citation does not match a discrete ground-ambulance statute in NY. NY's protection is older (2014/2015 Surprise Bill Law era) and lives in the Insurance Law provisions above, not at PHL § 4906. PHL § 4906 in Article 49 actually relates to utilization review reconsideration. **Cite the Insurance Law trio (3216(h)(24), 3221(l)(15), 4303(aa)) for ground-ambulance balance-billing protection, not PHL § 4906.**
- **ERISA preemption:** does not reach self-funded ERISA employer plans. For those, only the federal NSA applies — and the federal NSA **excludes** ground ambulance. This is a meaningful gap that the patient should be aware of: a NY resident on a self-funded employer plan does not get NY's ground-ambulance protection.
- **Excludes:** air ambulance (federal NSA covers it), workers' comp, Medicare, Medicaid.

## Medical-debt credit reporting — Fair Medical Debt Reporting Act (FMDRA)

- **Statute:** **N.Y. Gen. Bus. Law § 380-j(f)(1)(iv)** (amended), with companion provisions in **N.Y. Pub. Health Law Article 49-A** and definitional provisions added by the 2024 technical amendment (S.B. 8373)
- **Enacted:** SB 4907A / AB 6275A, signed by Governor Hochul December 13, 2023, **effective immediately on signing (Dec 13, 2023)**. The 2024 technical correction (SB 8373, signed Nov 22, 2024) refined the definition of "medical debt" and applies retroactively to Dec 13, 2023.
- **Sources:** [ag.ny.gov/resources/individuals/health-care-insurance/Reporting-medical-debt](https://ag.ny.gov/resources/individuals/health-care-insurance/Reporting-medical-debt); [advocacy.consumerreports.org/press_release/new-york-governor-signs-ban-on-reporting-medical-debt-to-credit-reporting-agencies](https://advocacy.consumerreports.org/press_release/new-york-governor-signs-ban-on-reporting-medical-debt-to-credit-reporting-agencies/); [cssny.org/news/entry/new-york-leading-in-attacking-medical-debt](https://www.cssny.org/news/entry/new-york-leading-in-attacking-medical-debt); [law.justia.com/codes/new-york/pbh/article-49-a](https://law.justia.com/codes/new-york/pbh/article-49-a/)
- **What it prohibits:**
  - **Hospitals, health-care professionals, and ambulance service providers** may not furnish medical debt information to consumer reporting agencies (CRAs).
  - **CRAs** (Equifax, Experian, TransUnion, and any other) may not place or maintain medical debt on a New York consumer's credit report — **regardless of when the debt arose**, including pre-2023 debt.
  - Health-care providers must include **contractual prohibitions** in agreements with debt collectors, preventing those collectors from reporting medical debt.
- **Carve-out:** Medical charges placed on a **general-purpose credit card** (Visa, MasterCard, etc.) remain reportable as ordinary credit-card debt. **Medical credit cards** marketed for medical use (CareCredit, etc.) are not exempt — the statute targets the function, not just the label.
- **Federal preemption posture:** The CFPB issued an October 2025 interpretive rule asserting that the federal FCRA preempts state-level medical-debt credit-reporting restrictions. **That interpretive position is being challenged in court.** As of this writing, NY's FMDRA is the operative rule for consumers and reporting agencies in New York; the AG and DFS continue to enforce it. Patients should still cite FMDRA in dispute letters and credit-bureau disputes; the federal preemption question may eventually narrow it but has not done so yet.
- **Use:** This is the single highest-leverage credit-reporting cite a NY patient has. Send a § 380-j(f) violation letter to the furnisher and a separate dispute to the CRA. If either fails to remove the entry, file with the NY AG Health Care Bureau and DFS.

## Hospital Financial Assistance Law

- **Statute:** **N.Y. Pub. Health Law § 2807-k(9-a)** (financial-assistance requirements for general hospitals); amended significantly by **S.1366-B / A.6027-A**, signed October 22, 2023, effective for most provisions in **2024**.
- **Sources:** [codes.findlaw.com/ny/public-health-law/pbh-sect-2807-k](https://codes.findlaw.com/ny/public-health-law/pbh-sect-2807-k/); [health.ny.gov/facilities/hospital/financial_assist/law](https://www.health.ny.gov/facilities/hospital/financial_assist/law/); [nycbar.org/reports/support-for-legislation-that-amends-the-hospital-financial-assistance-law](https://www.nycbar.org/reports/support-for-legislation-that-amends-the-hospital-financial-assistance-law/); [nixonpeabody.com/insights/alerts/2024/10/23/nysdoh-guidance-on-new-healthcare-payment-laws](https://www.nixonpeabody.com/insights/alerts/2024/10/23/nysdoh-guidance-on-new-healthcare-payment-laws); [hancocklaw.com/publications/healthcare-law-alert-update-new-requirements-for-hospital-financial-assistance-programs](https://www.hancocklaw.com/publications/healthcare-law-alert-update-new-requirements-for-hospital-financial-assistance-programs-and-for-healthcare-providers-accepting-and-assisting-patients-in-applying-for-medical-credit-cards-or-medical-installment-loans-to-pay-for-health-care-services/)
- **Scope:** **All general hospitals licensed under Article 28 by the NY DOH** — not just non-profits, not just ICTF participants. This is the major NY-specific structural protection: the federal IRS § 501(r) FAP mandate applies only to non-profit hospitals; NY's law extends to **for-profits, public hospitals, and government-run facilities** alike.
- **Eligibility (effective 2024 amendments):**
  - **≤ 200% FPL:** all charges waived; no nominal payment may be collected.
  - **200%-300% FPL:** sliding-scale reduction up to a **maximum of 10% of the Medicaid rate** for the service.
  - **300%-400% FPL:** sliding-scale reduction up to a **maximum of 20% of the Medicaid rate** for the service.
  - **"Underinsured":** patients whose out-of-pocket medical costs in the prior 12 months exceeded **10% of gross annualized income** are also eligible.
- **Immigration status:** **Cannot be used as an eligibility criterion.** PHL § 2807-k(9-a)(g).
- **Uniform Application Form:** All NY-licensed hospitals must use the DOH's Uniform Hospital Financial Assistance Application. Patients can demand the form by name.
- **Collection restrictions (2024 amendments):**
  - **180-day moratorium**: hospitals and their debt-collection agents may not commence a civil action against a patient for medical-debt nonpayment for at least **180 days** after issuing the first post-service bill — and even after 180 days, only after the hospital has made reasonable efforts to determine the patient's FA eligibility.
  - **Pre-suit FA affidavit**: any lawsuit to recover unpaid medical debt must include a sworn affidavit from the hospital's Chief Financial Officer confirming the patient's income is above 400% FPL based on the hospital's reasonable determination. **A complaint filed without this affidavit is procedurally defective** — patients sued without one have a clean dismissal argument.
  - **No home liens, no foreclosure, no wage garnishment** for medical debt collection by a hospital or its agent (statutory prohibition layered on top of CPLR 5201's existing exemptions).
  - **Installment plans capped at 5% of gross monthly income**, with the first payment due no sooner than 180 days after the date of service or discharge, whichever is later. (Prior cap was 10%; reduced by the 2023/2024 amendments.)
- **Use:** Whenever a NY hospital sends a collection letter or files suit, demand the Uniform Application Form by name and assert the 180-day moratorium plus the 5%-of-income payment-plan ceiling. If sued, immediately check for the § 2807-k(9-a) CFO affidavit; if missing, move to dismiss.

## Consumer Disclosure Information for Hospital Bills

- **Statute:** The NY consumer-disclosure framework for hospital bills lives in multiple sections, not in a single § 2803-o (despite the prompt's reference; § 2803-o actually addresses mastectomy and lymph-node-dissection patient care, **not billing disclosure**). The relevant disclosure provisions are:
  - **N.Y. Pub. Health Law § 24** — health-plan participation disclosure; out-of-network referral disclosure; consent-to-OON-services requirements.
  - **N.Y. Pub. Health Law § 2803(1)(g)** and the **Hospital Patients' Bill of Rights** (10 NYCRR § 405.7) — itemized bill and explanation of all charges; access to standard-charge list.
  - **N.Y. Pub. Health Law § 2830** — regulation of facility-fee billing; written notice required prior to date of service for any facility fee that may not be covered by the patient's plan; plain language; 12-point bold typeface; available in the top six languages spoken in the hospital's service area.
- **Sources:** [law.justia.com/codes/new-york/pbh/article-28/2803](https://law.justia.com/codes/new-york/pbh/article-28/2803/); [codes.findlaw.com/ny/public-health-law/pbh-sect-2830](https://codes.findlaw.com/ny/public-health-law/pbh-sect-2830/); [health.ny.gov/regulations/public_health_law/surprise_bill_law/docs/hospital_disclosure_ltr.pdf](https://www.health.ny.gov/regulations/public_health_law/surprise_bill_law/docs/hospital_disclosure_ltr.pdf)
- **Substance:**
  - Hospitals must post and provide on request a list of standard charges and the health plans in which the hospital participates.
  - Physicians scheduling a procedure must verbally and in writing disclose any non-participation in the patient's plan (§ 24(1)). If the physician maintains a public website listing plan participation, written disclosure may be satisfied by directing the patient to the site.
  - Facility fees not covered by the patient's plan require **advance notice** stating the fee amount, the purpose of the fee, and that it may not be covered, in plain 12-point bold language. **Failure to provide this notice in advance bars collection of the facility fee.**
- **Use:** When a NY patient is hit with a facility fee they were never told about, the § 2830 advance-notice rule is the cleanest defense. The hospital bears the burden of showing compliant disclosure; absent that, the fee is not collectible.

## Medical-debt collections protections — Consumer Credit Fairness Act (CCFA)

- **Statutes:** **CPLR § 214-i** (3-year SOL for consumer credit transactions); amendments to **CPLR §§ 3015, 306-b, 308, 3215, 5014, 5232, 5511**, and others, governing pleading specificity, default-judgment requirements, and notice requirements in consumer-credit actions.
- **Enacted:** Chapter 593 of the Laws of 2021 (signed Nov 8, 2021), effective **April 7, 2022**. Further amendments expanded scope and tightened plaintiff requirements in subsequent sessions.
- **Sources:** [legalservicesli.org/new-consumer-credit-debt-statute-of-limitations](https://legalservicesli.org/new-consumer-credit-debt-statute-of-limitations/); [ny-bankruptcy.com/what-is-the-nys-consumer-credit-fairness-act](https://www.ny-bankruptcy.com/what-is-the-nys-consumer-credit-fairness-act/); [thelangelfirm.com/debt-collection-defense-blog/2021/september/15-faq-s-about-statute-of-limitations-debt-colle](https://www.thelangelfirm.com/debt-collection-defense-blog/2021/september/15-faq-s-about-statute-of-limitations-debt-colle/)
- **Key features (as applied to medical debt):**
  - **3-year SOL** under CPLR § 214-i for any consumer-credit transaction, **including medical debt** sued upon by a hospital, provider, or assignee/debt buyer.
  - **Partial payment does not restart the clock.** Acknowledgment in writing does not revive a time-barred consumer-credit debt.
  - **Pleading specificity:** the complaint must attach the underlying contract, a chain-of-assignment for purchased debt, an itemized account of charges and payments, and the name/address of the original creditor.
  - **Mandatory notice to defendant** by the court clerk by mail of the action, in addition to service of process by the plaintiff.
  - **Stricter default-judgment requirements:** the plaintiff must file additional affidavits and the court must wait a longer notice period before entering default. Designed to curb "sewer service" debt-collection default judgments.
- **Use:** When a hospital or debt buyer sues a NY patient for an old medical bill, the **first defense** is the 3-year clock. Many medical-debt suits are filed 4-6 years post-service under habits inherited from the prior 6-year regime; these are dismissible on SOL grounds. Pair with a § 2807-k(9-a) CFO-affidavit challenge if the plaintiff is a hospital.

## Hospital lien statute

- **Statute:** **N.Y. Lien Law § 189** ("Liens of hospitals")
- **Sources:** [codes.findlaw.com/ny/lien-law/lie-sect-189](https://codes.findlaw.com/ny/lien-law/lie-sect-189/); [law.justia.com/codes/new-york/lie/article-8/189](https://law.justia.com/codes/new-york/lie/article-8/189/); [newyork.public.law/laws/n.y._lien_law_section_189](https://newyork.public.law/laws/n.y._lien_law_section_189)
- **Substance:** Charitable, state, county, city, town, or village hospitals may file a lien against a patient's **right of action or settlement proceeds against a third-party tortfeasor** for personal injuries received within **one week prior** to emergency treatment or hospital admission. **The lien attaches only to tort recoveries**, not to the patient's home, wages, or bank accounts.
- **Perfection requirements:**
  - **Written notice** by registered or certified mail, prepaid, to the allegedly liable third party (or their insurer), giving the patient's name and address, the date of accident, the hospital's name and location, and identifying the liable party — **before any payment** to the patient.
  - **Additional notice of lien filed with the county clerk** after discharge, showing the total accrued hospital charges.
- **Duration:** A filed lien is valid for **10 years**; refileable in 10-year increments by filing within 90 days before expiration.
- **No-Lien Law interaction:** Under **N.Y. Gen. Oblig. Law § 5-335**, most private health insurers (other than self-funded ERISA, Medicare, Medicaid, workers' comp, no-fault) are **barred** from asserting subrogation or reimbursement claims against personal-injury settlements. This is independent of Lien Law § 189, which addresses the hospital's own lien for unpaid charges, not the insurer's recovery.

## Wage garnishment protections

- **Statute:** **CPLR § 5231** (income execution); see also **CPLR § 5205** (exemptions from satisfaction of money judgments)
- **Sources:** [law.justia.com/codes/new-york/cvp/article-52/5231](https://law.justia.com/codes/new-york/cvp/article-52/5231/); [nolo.com/legal-encyclopedia/new-york-income-execution-wage-garnishment-law.html](https://www.nolo.com/legal-encyclopedia/new-york-income-execution-wage-garnishment-law.html)
- **Cap:** A judgment creditor may garnish the **lesser of**:
  - **10% of gross earnings**, OR
  - **25% of disposable earnings** (after legally required deductions), but only the portion of disposable earnings that exceeds **30× the federal or state minimum wage** (whichever is greater).
  - If disposable earnings are less than 30× minimum wage, **nothing may be garnished**.
- **Medical-debt-specific overlay:** PHL § 2807-k(9-a) prohibits **hospitals and their collection agents from garnishing wages** for medical-debt collection regardless of CPLR § 5231 — i.e., even with a judgment in hand, a NY hospital cannot garnish wages. Non-hospital medical providers (private practices, ambulances if not hospital-affiliated) remain bound by the CPLR § 5231 cap. Third-party debt collectors collecting on behalf of a hospital are also bound by the prohibition because they act as the hospital's agents.
- **Procedure:** Garnishment requires a money judgment first. Pre-judgment wage attachment is not permitted in NY for medical debt. The judgment debtor must receive notice and has 20 days to respond before garnishment begins.

## Other NY-specific patient-side advantages

### N.Y. Gen. Bus. Law § 349 — Deceptive Acts and Practices (with private right of action)

- **Statute:** **N.Y. Gen. Bus. Law § 349**
- **Source:** [codes.findlaw.com/ny/general-business-law/gbs-sect-349](https://codes.findlaw.com/ny/general-business-law/gbs-sect-349/); [law.justia.com/codes/new-york/gbs/article-22-a/349](https://law.justia.com/codes/new-york/gbs/article-22-a/349/)
- **Substance:** Prohibits "deceptive acts or practices in the conduct of any business, trade or commerce." Subsection (h) gives **any person injured by such an act** a private right of action.
- **Three-element test:** (1) the defendant engaged in a consumer-oriented act or practice, (2) the act was materially misleading, (3) plaintiff suffered injury as a result.
- **Damages:** Actual damages or **$50 statutory minimum**, whichever is greater. **Treble damages up to $1,000** for willful or knowing violations. **Reasonable attorney's fees** at the court's discretion.
- **As applied to medical bills:** Misrepresenting in-network status, billing for services not rendered, upcoding, dunning for time-barred debt, threatening credit-report reporting in violation of FMDRA, and similar deceptive practices in billing are actionable. The NY Court of Appeals held in *Riordan v. Nationwide Mutual Fire Ins. Co.* and progeny that § 349 reaches insurer claims-handling conduct that is consumer-oriented (not preempted by the Insurance Law for that purpose, per *Riordan* and *New York Univ. v. Cont'l Ins. Co.*, 87 N.Y.2d 308 (1995)).
- **Why this matters in NY:** Because NY lacks a statutory first-party bad-faith claim, § 349 is the **functional substitute** for the bad-faith remedies CA, GA, and TX patients use. The fee-shifting provision makes plaintiff-side litigation economic even on smaller disputes.
- **Source:** [hnrklaw.com/HNRK-Coverage-Corner-Blog/new-york-insurance-law-does-not-preempt-claim-against-insurer-for-deceptive-practices-under-section-349-of-the-general-business-law](https://www.hnrklaw.com/HNRK-Coverage-Corner-Blog/new-york-insurance-law-does-not-preempt-claim-against-insurer-for-deceptive-practices-under-section-349-of-the-general-business-law)

### N.Y. Gen. Bus. Law Article 29-H — State debt-collection statute

- **Statute:** **N.Y. Gen. Bus. Law §§ 600-603** (and § 603-B private right of action provision)
- **Source:** [law.justia.com/codes/new-york/gbs/article-29-h](https://law.justia.com/codes/new-york/gbs/article-29-h/)
- **Substance:** State-law parallel to the federal Fair Debt Collection Practices Act (FDCPA), but **reaches original creditors as well as third-party collectors** (unlike the federal FDCPA, which is third-party-only). Prohibits abusive frequency or hours of contact, false threats, and similar practices.
- **Use:** When a NY hospital's in-house billing department engages in FDCPA-style misconduct (threatening lawsuits without intent to sue, contacting at prohibited hours, contacting third parties about the debt), cite Article 29-H — the federal FDCPA does not reach the hospital itself, but Article 29-H does.

### General Obligations Law § 5-335 — Anti-subrogation/No-Lien Law

- **Statute:** **N.Y. Gen. Oblig. Law § 5-335**
- **Source:** [law.justia.com/codes/new-york/gob/article-5/title-3/5-335](https://law.justia.com/codes/new-york/gob/article-5/title-3/5-335/)
- **Substance:** Bars most private health insurers from asserting reimbursement or subrogation claims against personal-injury settlements. Self-funded ERISA, Medicare, Medicaid, workers' comp, and certain no-fault claims are exceptions.
- **Use:** In personal-injury contexts where a NY patient's insurer asserts a reimbursement claim against settlement proceeds, § 5-335 is often a complete defense. Confirm plan type first — self-funded ERISA plans escape this protection.

### NY's external-appeal IRO database

- DFS publishes IRO decision summaries. Patients drafting an external appeal can search for prior decisions involving similar conditions, denial rationales, or specific insurers. Source: [dfs.ny.gov/complaints/file_external_appeal](https://www.dfs.ny.gov/complaints/file_external_appeal). This is a meaningful advantage over states whose external-review decisions are not published.

### NY Health Care Bureau's track record

- The AG's Health Care Bureau recovered $1.53M for consumers in 2025 alone (handling 4,890 complaints). The Bureau is unusual in routinely contacting providers and insurers on individual consumer cases — it is not a pure regulatory filing cabinet. This makes it materially more useful than a generic AG consumer line.

## Quick reference for letter rendering

When the LLM renders a New York-bound letter, substitute these defaults:

| Field                                      | Value                                                                                                                                                                                                                        |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| State itemization statute                  | **N.Y. Pub. Health Law § 2831** — consolidated itemized bill within 7 days of discharge or request                                                                                                                           |
| State insurance regulator (CC line)        | NY State Department of Financial Services, Consumer Assistance Unit, 1 State Street, New York, NY 10004 (also: 1 Commerce Plaza, Albany, NY 12257); 1-800-342-3736; [dfs.ny.gov/complaint](https://www.dfs.ny.gov/complaint) |
| State AG (CC line, for billing disputes)   | NY Attorney General — Health Care Bureau, 28 Liberty Street, New York, NY 10005; Helpline 1-800-428-9071; [ag.ny.gov/file-complaint/health-care](https://ag.ny.gov/file-complaint/health-care)                               |
| Small-claims court name                    | **NYC Civil Court, Small Claims Part** ($10,000 cap) inside the five boroughs; **City Court, Small Claims Part** ($5,000) or **Town/Village Justice Court, Small Claims Part** ($3,000) elsewhere                            |
| Filing fee (in 30-day warning)             | "$15-$20 in NYC Civil Court depending on claim amount; $10-$20 in City/Town/Village courts"                                                                                                                                  |
| Statute of limitations (in 30-day warning) | "**CPLR § 214-i (three years for consumer credit transactions, including medical debt)** under the Consumer Credit Fairness Act, effective April 7, 2022. Partial payment does not restart the clock."                       |
| Ground-ambulance citation                  | N.Y. Ins. Law §§ 3216(h)(24), 3221(l)(15), 4303(aa) (NOT PHL § 4906)                                                                                                                                                         |
| Hospital financial-assistance citation     | **N.Y. Pub. Health Law § 2807-k(9-a)** — sliding scale to 400% FPL, 180-day pre-suit moratorium, 5%-of-income payment-plan cap, CFO affidavit required for collection suit                                                   |
| Credit-reporting citation                  | **Fair Medical Debt Reporting Act** (N.Y. Gen. Bus. Law § 380-j(f); N.Y. Pub. Health Law Article 49-A), effective Dec 13, 2023                                                                                               |
| Surprise-billing citation                  | **N.Y. Fin. Servs. Law Art. 6 (§§ 601-608)** + companion **N.Y. Ins. Law §§ 3217-a, 3241, 3242, 4324** + **N.Y. Pub. Health Law § 24**                                                                                       |
| External-appeal citation                   | **N.Y. Ins. Law § 4914 / N.Y. Pub. Health Law § 4914** — 4-month filing window, $25 fee (max $75/year), 30-day decision, binding on plan                                                                                     |
| Bad-faith strategy                         | Cite N.Y. Gen. Bus. Law § 349 (private RoA, $50 minimum, treble to $1,000, attorney's fees) instead of common-law bad faith. File DFS complaint citing Ins. Law § 2601 in parallel.                                          |
| Deceptive-practices citation               | **N.Y. Gen. Bus. Law § 349** — private right of action, attorney's fees recoverable                                                                                                                                          |
| Debt-collector misconduct citation         | **N.Y. Gen. Bus. Law Article 29-H (§§ 600-603)** — reaches original creditors, unlike federal FDCPA                                                                                                                          |
| Wage-garnishment posture                   | Hospitals **cannot** garnish wages for medical debt (PHL § 2807-k(9-a)). Other providers limited to CPLR § 5231 (lesser of 10% gross or 25% disposable above 30× minimum wage).                                              |

## Key New York-specific advantages

Worth keeping in mind when triaging a NY patient's bills:

1. **Fair Medical Debt Reporting Act** — Complete prohibition on medical debt in credit reports, including pre-2023 debt. No grace period, no dollar threshold. The strongest medical-credit protection of any state. **Federal preemption is being asserted by the CFPB but contested**; FMDRA remains operative in NY pending resolution.
2. **3-year statute of limitations** on medical-debt collection actions, under CPLR § 214-i (Consumer Credit Fairness Act, effective April 7, 2022). **Partial payment does not restart the clock.** This shrinks the window for hospital collection actions dramatically and gives NY patients clean SOL defenses against any medical-debt suit older than 3 years.
3. **Universal Hospital Financial Assistance Law** — PHL § 2807-k(9-a) binds **every** general hospital licensed by NY (not just non-profits), with eligibility to 400% FPL, a 180-day pre-suit moratorium, a 5%-of-income payment-plan cap, and a mandatory CFO affidavit on any collection lawsuit. A lawsuit missing the affidavit is dismissible on its face.
4. **Wage-garnishment prohibition for hospital collections** — Layered on top of CPLR § 5231's general caps. Hospitals and their agents simply cannot garnish wages in NY for medical debt.
5. **Section 349 as a bad-faith substitute** — NY's lack of statutory bad-faith is offset by Gen. Bus. Law § 349's private right of action with $50 minimum, treble damages up to $1,000, and attorney's fees. This makes plaintiff-side recovery economic at scales bad-faith doctrine would not.
6. **Dedicated AG Health Care Bureau** — 1-800-428-9071 — with subject-matter expertise and a documented track record of recovery for consumers. Use this over the generic AG Consumer Frauds line for any health-care dispute.
7. **First-mover advantage on surprise billing** — NY's 2014/2015 Surprise Bill Law predates the federal NSA by seven years and remains broader in some respects (ground ambulance for fully-insured plans, ancillary-service coverage, hospital-side disclosure obligations regardless of plan type).
8. **External-appeal regime** — $25/$75 max fee (refunded on win), 4-month filing window, 30-day binding decision, free for Medicaid/Child Health Plus. The IRO database lets patients tailor appeals to historical decision patterns.

These eight together make New York one of the two or three most patient-favorable states in the country for medical-bill disputes, alongside California and Massachusetts.
