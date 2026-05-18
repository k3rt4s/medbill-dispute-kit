# California state pack

The fully-worked state-law layer for California patients. The LLM uses this when the patient's state is California. Tennessee equivalent at [`laws_state_tn.md`](laws_state_tn.md); Georgia equivalent at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

California is the single most patient-favorable state in this kit. Four structural advantages, in addition to the federal floor:

1. The **Hospital Fair Pricing Act** (Health & Safety Code § 127400 et seq.) applies to **all general acute-care hospitals** (non-profit, for-profit, district, county), not just § 501(r) non-profits, and caps charges at the Medicare/Medi-Cal/highest-government-payor rate for eligible patients.
2. **AB 716 closes the federal No Surprises Act's ground-ambulance gap** for fully-insured Californians and caps uninsured/self-pay ambulance liability at the Medi-Cal or Medicare rate.
3. **SB 1061** bans medical debt from California credit reports entirely (effective Jan 1, 2025) and voids the debt itself if knowingly reported in violation.
4. California has the country's strongest first-party insurance **bad-faith** doctrine — *Gruenberg / Egan* tort liability with full consequential and emotional-distress damages, plus *Brandt* fees, for fully-insured plans.

## Hospital itemization right

California does not have a single "itemized statement on request" statute analogous to Tennessee's § 68-11-220 or Georgia's § 10-1-393(b)(14). The patient's right to an itemized hospital bill operates through three layered sources:

- **Statute (notice duty):** **Cal. Health & Safety Code § 127425** (added by AB 532, expanded by AB 1020, Ch. 473 Stats. 2021), which requires hospitals to **inform the patient how to obtain an itemized hospital bill** and to include that statement in pre-collection notices. Codifies the patient's right to request the itemized bill and ties downstream debt-collection actions to honoring it.
- **Source:** [leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=127425](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=127425.); AB 1020 chaptered text at [leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202120220AB1020](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202120220AB1020)
- **Companion uninsured-estimate duty:** **Cal. Health & Safety Code § 1339.585** requires the hospital, upon request of a person without health coverage, to provide a written estimate of expected charges plus charity-care information. This is a pre-service estimate, not a post-service itemized bill, so it does **not** answer the itemization request directly.
- **Source:** [leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=1339.585](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=1339.585.)
- **Debt-buyer parallel:** **Cal. Civ. Code § 1788.52(c)** requires a debt buyer to produce requested debt documentation **within 15 calendar days** of a written debtor request, and § 1788.52(f) imports the § 127425 notice for hospital-originated debt. If the requested itemized bill is held by a debt collector rather than the hospital, this is the operative deadline.
- **Source:** [leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1788.52](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1788.52.)
- **Federal backstop:** HIPAA Privacy Rule's right of access (45 C.F.R. § 164.524) gives the patient a federal right to billing records held in the designated record set, with a 30-day response deadline (one 30-day extension permitted). See [`laws_federal.md`](laws_federal.md).
- **Caveats:** No California statute sets an explicit response deadline on the hospital's delivery of the requested itemized bill itself; the practical levers are the 15-day debt-buyer deadline (§ 1788.52(c)) and the 30-day HIPAA right of access. AB 1020 enforcement is by HCAI (see Hospital Bill Complaint Program below), **not** a private right of action.

**Letter pattern:** Request the itemized bill in writing, cite **Health & Safety Code § 127425** for the hospital's notice/disclosure duty, cite **45 C.F.R. § 164.524** for the 30-day HIPAA deadline as a floor, and if the bill is in collections also cite **Cal. Civ. Code § 1788.52(c)** for a 15-day production deadline. Cross-reference HCAI's Hospital Bill Complaint Program as the regulatory escalation.

## Unfair Insurance Practices Act

- **Statute:** **Cal. Ins. Code § 790.03 et seq.** — the Unfair Insurance Practices Act (UIPA); enumerated unfair claims-settlement acts at **§ 790.03(h)**
- **Source:** [leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=INS&sectionNum=790.03](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=INS&sectionNum=790.03.); regulations at 10 C.C.R. § 2695.1 et seq. (Fair Claims Settlement Practices Regulations)
- **Substance:** Prohibits 16 enumerated unfair claims-settlement practices — misrepresenting policy provisions, failing to acknowledge claims promptly, denying without reasonable investigation, not attempting good-faith settlement where liability is reasonably clear, compelling insureds to litigate to recover amounts ultimately due, etc.
- **Critical caveat — Moradi-Shalal:** Cal. Supreme Court in **Moradi-Shalal v. Fireman's Fund Ins. Cos.**, 46 Cal.3d 287 (1988), held there is **no private right of action** under § 790.03(h). Overruled *Royal Globe Ins. Co. v. Superior Court*, 23 Cal.3d 880 (1979), prospectively. Source: [scocal.stanford.edu/opinion/moradi-shalal-v-firemans-fund-ins-companies-28538](https://scocal.stanford.edu/opinion/moradi-shalal-v-firemans-fund-ins-companies-28538).
- **Enforcement:** Insurance Commissioner only, via administrative action (cease-and-desist, monetary penalties under Cal. Ins. Code §§ 790.035, 790.05).
- **UCL workaround:** Conduct that violates § 790.03 can still ground a **Business & Professions Code § 17200** (Unfair Competition Law) claim brought on grounds **independent** of § 790.03. *Zhang v. Superior Court*, 57 Cal.4th 364 (2013). UCL remedies are limited to injunction and restitution — no damages, no fees — but the threat of class-wide injunctive relief is itself leverage.
- **Use in this kit:** Cite § 790.03 violations when filing a CDI or DMHC regulatory complaint, and when pleading the predicate "unlawful" prong of a UCL claim. Do not plead § 790.03 as a stand-alone count for damages.
- **ERISA:** Preempted as applied to self-funded employer plans; intact for fully-insured, individual/marketplace, and government plans.

## Bad-faith failure to pay (Gruenberg / Egan)

- **Common-law tort:** Breach of the **implied covenant of good faith and fair dealing**, recognized as an independent tort against an insurer in first-party claims.
- **Foundational cases:**
  - **Gruenberg v. Aetna Ins. Co.**, 9 Cal.3d 566 (1973) — first recognized the tort in first-party claims; the implied covenant means neither party will injure the other's right to receive the benefits of the contract. Source: [law.justia.com/cases/california/supreme-court/3d/9/566.html](https://law.justia.com/cases/california/supreme-court/3d/9/566.html).
  - **Egan v. Mutual of Omaha Ins. Co.**, 24 Cal.3d 809 (1979) — an insurer breaches the covenant when it fails to conduct a reasonable investigation before denying a claim; an insurer "cannot reasonably and in good faith deny payments to its insured without thoroughly investigating the foundation for its denial." Source: [law.justia.com/cases/california/supreme-court/3d/24/809.html](https://law.justia.com/cases/california/supreme-court/3d/24/809.html).
  - **Brandt v. Superior Court**, 37 Cal.3d 813 (1985) — attorney's fees incurred to compel payment of the policy benefit are recoverable as tort damages ("Brandt fees").
- **Substance:** California allows recovery of (1) the contract benefit, (2) all consequential damages proximately caused by the bad-faith conduct including emotional distress (no physical-injury requirement), (3) Brandt fees, and (4) punitive damages under Cal. Civ. Code § 3294 on a showing of oppression, fraud, or malice by clear and convincing evidence.
- **Standard:** Bad faith requires conduct that is unreasonable or without proper cause. Mere negligence is not enough; a *genuine dispute* over coverage defeats bad faith (*Chateau Chamberay Homeowners Assn. v. Associated Int'l Ins. Co.*, 90 Cal.App.4th 335 (2001)). Once liability becomes reasonably clear, continued refusal can convert a coverage dispute into bad faith.
- **ERISA:** **Preempted** for self-funded ERISA employer plans (*Pilot Life Ins. Co. v. Dedeaux*, 481 U.S. 41 (1987)). For ERISA self-funded plans, the federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) attorney's fees — no state bad-faith penalty. Intact for fully-insured plans, individual/marketplace plans, and self-funded plans not covered by ERISA (e.g., church plans, government plans).
- **Why it matters:** California's bad-faith doctrine is the most expansive in the US. Even without a damages claim ripe for litigation, a credible *Gruenberg/Egan* citation in a demand letter to a fully-insured carrier carries substantial weight.

## Surprise billing (AB 72)

- **Statutes:**
  - **Cal. Health & Safety Code § 1371.9** (Knox-Keene plans), § 1371.30, § 1371.31
  - **Cal. Ins. Code § 10112.8, § 10112.81, § 10112.82** (PPO/indemnity insurers regulated by CDI)
- **Enactment:** AB 72 (2016), Ch. 492 Stats. 2016, effective July 1, 2017
- **Sources:** [leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201520160AB72](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201520160AB72); CDI consumer fact sheet at [insurance.ca.gov/01-consumers/110-health/60-resources/nosuprisebills.cfm](https://www.insurance.ca.gov/01-consumers/110-health/60-resources/nosuprisebills.cfm)
- **What it does:** For **non-emergency services** rendered by an out-of-network provider at an in-network facility (the "ancillary services" scenario — anesthesia, radiology, pathology, lab, assistant surgeon), the patient is liable only for the **in-network cost-share**. Amounts above that count toward the in-network deductible and out-of-pocket maximum. Out-of-network providers may not balance bill above the in-network cost-share.
- **Insurer reimbursement:** the greater of (i) the average contracted rate or (ii) **125% of the Medicare rate** for the same service in the same geographic area (Ins. Code § 10112.82). Independent dispute-resolution process administered by DMHC/CDI for provider-payer rate disputes; the patient is held harmless from the rate fight.
- **Emergency services:** AB 72 expressly does not apply to emergency services, but California already prohibits balance billing of emergency-services patients enrolled in Knox-Keene plans under *Prospect Medical Group, Inc. v. Northridge Emergency Medical Group*, 45 Cal.4th 497 (2009) (the "Prospect" rule — emergency providers must seek payment from the plan, not the patient). Source: [law.justia.com/cases/california/supreme-court/4th/45/497.html](https://law.justia.com/cases/california/supreme-court/4th/45/497.html).
- **Interaction with federal No Surprises Act (NSA):** California's law and the federal NSA layer rather than displace; the patient gets whichever is more protective. The federal NSA reaches **self-funded ERISA plans** that AB 72 cannot reach; AB 72 still applies to fully-insured plans regulated by California. For Knox-Keene plans, AB 72's reimbursement methodology (125% Medicare floor) is more favorable to providers than the federal NSA's qualifying-payment-amount methodology; this does **not** change the patient's in-network cost-share cap.
- **Caveats:**
  - Self-funded ERISA plans: federal NSA applies, AB 72 does not.
  - Medi-Cal managed care, Medicare, workers' compensation: excluded from AB 72; separate balance-billing protections apply (Medi-Cal at Welf. & Inst. Code § 14019.4; Medicare at federal limiting-charge rules).
  - Air ambulance: federal NSA covers.
  - Ground ambulance: AB 72 did not cover; AB 716 (below) closed that gap effective Jan 1, 2024.

## Independent Medical Review (IMR)

- **Statutes:**
  - **DMHC IMR (Knox-Keene plans):** Cal. Health & Safety Code §§ 1370.4 (experimental/investigational), 1374.30 (medical-necessity IMR), 1374.30–1374.36 generally
  - **CDI IMR (PPO/indemnity plans):** Cal. Ins. Code §§ 10169–10169.5
- **Sources:** [leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=1374.30](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=1374.30.); DMHC IMR portal at [healthhelp.ca.gov](https://healthhelp.ca.gov); program reports at [dmhc.ca.gov/fileacomplaint/independentmedicalreviewandcomplaintreports.aspx](https://www.dmhc.ca.gov/fileacomplaint/independentmedicalreviewandcomplaintreports.aspx)
- **Substance:** Free external review by an independent physician of a health plan's denial based on medical necessity, experimental/investigational status, or emergency-services determination. The IMR physician's decision is **binding on the plan**; the patient retains the right to sue if the IMR is adverse.
- **Process:**
  - **Eligibility:** the patient must generally first exhaust the plan's internal grievance process (30 days for standard, 3 days for urgent). Cal. Health & Safety Code § 1368.01 allows the IMR to be filed in parallel with or after the grievance for urgent cases or after 30 days of plan inaction.
  - **No fee.** The IMR is free to the enrollee; the plan pays the cost.
  - **Timeline:** standard determination within **30 days** of all records being received; **expedited** within **3 business days** (and as fast as 72 hours) where there is an imminent and serious threat to the enrollee's health.
  - **File via:** DMHC online IMR/Complaint Form at [healthhelp.ca.gov](https://healthhelp.ca.gov) for Knox-Keene plans (the great majority of California HMOs and many PPOs that opted into DMHC jurisdiction); CDI online IMR for non-Knox-Keene PPO/indemnity plans regulated by CDI.
- **Success rates:** DMHC's annual reports show that roughly **65-75% of IMR outcomes favor the enrollee**, counting both IMR-overturned denials and plan-reversed denials before IMR completion. 2024 reporting cited overall favorable-to-enrollee rate near 73%. Confirm current year via [dmhc.ca.gov/DataResearch.aspx](https://www.dmhc.ca.gov/DataResearch.aspx) and the CHHS open-data dataset at [data.chhs.ca.gov/dataset/independent-medical-review-imr-determinations-trend](https://data.chhs.ca.gov/dataset/independent-medical-review-imr-determinations-trend).
- **Caveats:**
  - IMR covers **medical-necessity, coverage-of-experimental-treatment, and emergency-services** disputes. It does **not** cover purely contractual coverage disputes (e.g., "this service is excluded by the plan language") or billing/balance-billing disputes — those use the DMHC/CDI complaint process.
  - **ERISA preemption:** California's IMR has been held to **survive ERISA preemption** for fully-insured plans because the federal claims-procedure regulation (29 C.F.R. § 2560.503-1(c)(4)) and the ACA external-review requirement (29 C.F.R. § 2590.715-2719) explicitly defer to state external-review processes. Self-funded ERISA plans use the federal IRO process under the ACA.
  - **Self-pay/uninsured patients:** IMR is an insured-member remedy. Not available for uninsured patients — those route via the Hospital Bill Complaint Program or direct dispute.

## Department of Managed Health Care (DMHC) — Knox-Keene plans

- **Online complaint / IMR portal:** [healthhelp.ca.gov](https://healthhelp.ca.gov) (the DMHC Help Center)
- **Phone (Help Center):** **1-888-466-2219**; TDD **1-877-688-9891**
- **Email:** Helpline@dmhc.ca.gov
- **Hours:** Monday-Friday 8:00 a.m. - 6:00 p.m. Pacific, with after-hours/holiday coverage for urgent issues.
- **Mail:** Help Center, Department of Managed Health Care, 980 9th Street, Suite 500, Sacramento, CA 95814 (the downtown office is appointment-only; mail and online routing preferred)
- **Source:** [dmhc.ca.gov/AbouttheDMHC/ContactUs.aspx](https://www.dmhc.ca.gov/AbouttheDMHC/ContactUs.aspx)
- **Authority over:** all **Knox-Keene-licensed health care service plans** — virtually all California HMOs (including Kaiser, Anthem Blue Cross HMO, Blue Shield HMO, Health Net HMO, Aetna HMO), most Medi-Cal managed care plans, dental and vision plans that opted in, and a substantial number of PPO products operated by entities that hold a Knox-Keene license. Administers the IMR program, AB 72 enforcement for Knox-Keene plans, and Knox-Keene grievance enforcement. **No authority** over self-funded ERISA plans (route to DOL EBSA at 1-866-444-3272); shared jurisdiction with CDI on some PPO products (use the plan's evidence-of-coverage to confirm regulator).

## Department of Insurance (CDI) — PPO and indemnity plans

- **Online complaint:** [insurance.ca.gov/01-consumers/101-help/](https://www.insurance.ca.gov/01-consumers/101-help/) — direct portal at [cdiapps.insurance.ca.gov/CP/login/](https://cdiapps.insurance.ca.gov/CP/login/)
- **Phone (Consumer Hotline):** **1-800-927-4357 (1-800-927-HELP)**; TTY 1-800-482-4833
- **Hours:** Monday-Friday 8:00 a.m. - 5:00 p.m. Pacific
- **Mail (health claims):**
  > California Department of Insurance
  > Consumer Services Division - Health Claims Bureau
  > 300 South Spring Street, South Tower
  > Los Angeles, CA 90013
- **Authority over:** indemnity health insurance plans, most PPO plans not under DMHC, life, auto, homeowners, and other lines. Administers AB 72 for CDI-regulated plans and CDI's parallel IMR under Cal. Ins. Code § 10169. **No authority** over self-funded ERISA plans, Knox-Keene plans (route to DMHC), or providers/hospitals/debt collectors.
- **Route-of-first-resort heuristic:** if the plan card shows an HMO, EPO, or "Kaiser/Health Net HMO/Anthem HMO" type, file with DMHC; if the card shows an indemnity PPO not under DMHC, file with CDI. When in doubt, file with DMHC — DMHC will refer to CDI if it lacks jurisdiction; CDI will not always forward to DMHC.

## Attorney General — Consumer Protection

- **Online complaint:** [oag.ca.gov/report](https://oag.ca.gov/report); business-complaint form at [oag.ca.gov/contact/consumer-complaint-against-business-or-company](https://oag.ca.gov/contact/consumer-complaint-against-business-or-company)
- **Phone (Public Inquiry Unit):** **1-800-952-5225** (in-state) or **1-916-210-6276**
- **Mail:**
  > California Department of Justice
  > Attn: Public Inquiry Unit
  > P.O. Box 944255
  > Sacramento, CA 94244-2550
- **Healthcare Rights and Access (HRA) unit:** handles healthcare privacy/civil-rights complaints, medical-debt complaints, and deceptive/unfair healthcare-marketplace practices. Does not provide individual legal representation; pattern-and-practice referrals trigger enforcement. Source: [oag.ca.gov/consumers/general/health-care](https://oag.ca.gov/consumers/general/health-care).
- **Authority over:** providers, hospitals, debt collectors, and original creditors for unfair/deceptive practices under the Unfair Competition Law (Bus. & Prof. Code § 17200) and the Consumer Legal Remedies Act (Civ. Code § 1750 et seq.). Useful where DMHC/CDI lacks reach — especially provider-side billing disputes and original-creditor (hospital) conduct.

## Hospital Bill Complaint Program (HCAI)

- **Online complaint portal:** [hbcp.hcai.ca.gov](https://hbcp.hcai.ca.gov)
- **Program page:** [hcai.ca.gov/affordability/hospital-fair-billing-program/hospital-bill-complaint-program/](https://hcai.ca.gov/affordability/hospital-fair-billing-program/hospital-bill-complaint-program/)
- **Mail:**
  > Department of Health Care Access and Information
  > Hospital Bill Complaint Program
  > 2020 West El Camino Avenue, Suite 1101
  > Sacramento, CA 95833
- **Authority over:** all general acute-care hospitals licensed under Cal. Health & Safety Code § 1250(a). Investigates non-compliance with the Hospital Fair Pricing Act (charity care, discount payment, debt collection practices, § 127425 notices). **No jurisdiction** over general billing/fee disputes, Good Faith Estimates under the federal NSA, or balance billing by an ER-room physician (other than facility charges). Enforcement of charity-care and Fair Pricing Act rights transferred to HCAI effective Jan 1, 2024.

## Small claims court

- **Statute:** **Cal. Code Civ. Proc. § 116.220** (jurisdiction); **§ 116.530** (attorney prohibition at the initial hearing)
- **Sources:** [leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=116.220](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=116.220.); [leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=116.530](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=116.530.)
- **Court name:** **Small Claims Division** of the Superior Court of California (one per county)
- **Jurisdictional limits (set by SB 71, effective Jan 1, 2024):**
  - **Natural person (individual or sole proprietor):** **$12,500**
  - **Entity (corporation, LLC, partnership, association, public entity):** **$6,250**
  - **COVID-19 rental-debt actions and certain personal-injury claims arising from automobile accidents involving uninsured-motorist exposure:** higher caps in narrow scenarios; not relevant to medical-billing disputes.
  - **Frequency limit:** unlimited claims up to $2,500; not more than two claims per calendar year above $2,500 (§ 116.231).
- **Attorney rule (§ 116.530):** **No attorney may take part in the conduct or defense of a small claims action at the initial hearing**, with narrow exceptions (an attorney appearing in her own case as an individual; an attorney-partnership in which all partners are attorneys, etc.). Attorneys may advise either party before or after the hearing and may represent a party on appeal. **This is a structural advantage for self-represented patients** — corporate defendants generally must send a non-attorney officer or employee, and a hospital-billing-office staffer is rarely a formidable witness.
- **Corporate appearance:** Cal. Code Civ. Proc. § 116.540 permits a corporation, partnership, or other entity to appear through a regular employee, officer, or director (no attorney). The plaintiff must appear personally — no agents.
- **Filing fees:**
  - Claims up to $1,500: $30
  - Claims $1,501 - $5,000: $50
  - Claims $5,001 - $12,500 (individuals only): $75
  - Frequent-filer surcharge if more than 12 claims in the prior 12 months
  - Fee waivers available via FW-001 for low-income plaintiffs
  - Source: [courts.ca.gov/selfhelp-smallclaims.htm](https://www.courts.ca.gov/selfhelp-smallclaims.htm)
- **Appeal:** Defendants may appeal to the Superior Court (civil division) for a **trial de novo** within **30 days** of the clerk's notice of entry. Cal. Code Civ. Proc. § 116.710. Plaintiffs may not appeal but may appeal a denial of a motion to vacate. Attorneys are permitted on appeal.
- **Jury trial:** not available in Small Claims; the de novo appeal does not afford a jury either — it is a bench trial in the Superior Court.

## Statute of limitations

- **Written contracts:** **4 years from breach** — **Cal. Code Civ. Proc. § 337(a)**
- **Oral contracts:** **2 years from breach** — **Cal. Code Civ. Proc. § 339(1)**
- **Open book accounts:** 4 years — Cal. Code Civ. Proc. § 337(b) (calculated from the last entry on the account)
- **Statutory liability (e.g., violations of the Hospital Fair Pricing Act, Knox-Keene):** generally 3 years — Cal. Code Civ. Proc. § 338
- **Unfair Competition Law:** 4 years — Bus. & Prof. Code § 17208
- **Source:** [leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=337](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=337.); [leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=339](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=339.)

Most hospital admissions involve a signed financial-responsibility form, which is a written contract — **4 years** under § 337(a). Medical care without a signed agreement may be treated as an oral or implied contract (2 years under § 339) or as an open book account (4 years under § 337(b)). The discovery rule may toll the start of the clock for fraudulent concealment. Partial payment or written acknowledgment can restart the clock (Cal. Code Civ. Proc. § 360). **Do not make a partial payment on a time-barred debt without legal advice.**

## Ground ambulance balance-billing (AB 716)

- **Statute:** **Cal. Health & Safety Code §§ 1371.56, 1797.124, 1797.233** and **Cal. Ins. Code § 10126.66** (added by **AB 716**, Ch. 539 Stats. 2023, effective Jan 1, 2024)
- **Sources:** [leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB716](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB716); CHBRP analysis at [chbrp.org/sites/default/files/bill-documents/AB716/AB%20716%20Final.pdf](https://www.chbrp.org/sites/default/files/bill-documents/AB716/AB%20716%20Final.pdf)
- **What it does:**
  - **Fully-insured patients:** an out-of-network ground-ambulance provider may collect from the enrollee no more than the **in-network cost-sharing amount**; the insurer pays the OON provider at the rate set by the local emergency medical services agency (or 325% of Medicare in certain scenarios; the rate-setting mechanism is in § 1797.124 and detailed in EMS Authority annual reports).
  - **Uninsured / self-pay patients (HSC § 1797.233):** an OON ground-ambulance provider may not require the patient to pay more than the **established Medi-Cal or Medicare fee-for-service rate, whichever is greater**, for the transport. This is a stand-alone cap that applies regardless of insurance status.
  - **No adverse credit reporting for 12 months** after initial billing (HSC § 1797.233).
  - Rate transparency: EMS Authority publishes county-by-county maximum allowable rates annually under § 1797.124.
- **Coverage scope:** approximately 14 million Californians covered by fully-insured plans. **Does not apply** to self-funded ERISA plans (federal NSA excludes ground ambulance, so the **federal floor is zero** for those patients).
- **Caveats:**
  - Self-funded ERISA plans: **no protection** for the balance-bill amount; the uninsured/self-pay cap in § 1797.233 still applies if the patient is treated as self-pay by the provider.
  - Medi-Cal beneficiaries: separately protected by Welf. & Inst. Code § 14019.4.
  - Air ambulance: federal NSA covers.
- **This is the highest-leverage California-specific cite for any ground-ambulance balance bill dated on or after Jan 1, 2024.**

## Medical-debt credit reporting (SB 1061)

- **Statute:** **Cal. Civ. Code § 1785.13(a)(8)** (added/amended by **SB 1061**, Ch. 691 Stats. 2024), with conforming changes to Cal. Civ. Code §§ 1785.27, 1788.14, 1788.18, 1788.30, and adding § 1785.13(j); enforcement and voidance language in § 1785.27(g).
- **Sources:** [leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB1061](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB1061); Attorney General alert at [oag.ca.gov/news/press-releases/california-it-remains-illegal-medical-debt-appear-credit-reports-attorney](https://oag.ca.gov/news/press-releases/california-it-remains-illegal-medical-debt-appear-credit-reports-attorney)
- **What it does:**
  - **Effective Jan 1, 2025:** prohibits any person, including a healthcare provider or its agent, from furnishing medical-debt information to a consumer credit reporting agency, regardless of the amount. Prohibits CRAs from including medical debt on a California consumer credit report and from using it in any credit decision.
  - **Voidance:** if a person knowingly violates the furnishing prohibition, the medical debt itself is **void and unenforceable** — this is unusual and aggressive remedial language not present in most state credit-reporting laws.
  - **Effective July 1, 2025:** any contract or financial agreement creating a medical debt must include specific consumer-protection language; absence renders the debt void and unenforceable.
- **Caveats:**
  - **Federal preemption is contested.** The CFPB's October 2025 interpretive rule took the position that the federal FCRA preempts state credit-reporting restrictions on medical debt. California maintains SB 1061 is intact; litigation outcomes will be controlling. As of the date of this pack, the Cal AG's public guidance is that SB 1061 remains enforceable.
  - **Scope:** covers all medical debt held by any furnisher. Does not bar furnishers from internal credit decisions or from suing for the debt (subject to § 1788.14/§ 1788.18 and the SOL).
  - **Does not displace** the 2022-2023 voluntary CRA changes (paid medical debt removed; debt under $500 not reported; 1-year delay before reporting) — those still apply nationwide.

## Hospital Fair Pricing Act

- **Statute:** **Cal. Health & Safety Code §§ 127400-127446**, as amended by **AB 1020** (Ch. 473 Stats. 2021) and **AB 2297** (Ch. 543 Stats. 2024)
- **Sources:** [leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=HSC&division=107.&title=&part=2.&chapter=2.5.&article=1.](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=HSC&division=107.&title=&part=2.&chapter=2.5.&article=1.); HCAI laws page at [hcai.ca.gov/affordability/hospital-fair-billing-program/laws-and-regulations/](https://hcai.ca.gov/affordability/hospital-fair-billing-program/laws-and-regulations/)
- **Scope:** **all general acute-care hospitals** licensed under § 1250(a) — non-profit, for-profit, district, and county. This is the structural CA-specific advantage over federal § 501(r), which reaches only non-profit hospitals.
- **Substance:**
  - Each hospital must maintain a written charity-care policy and a written discount-payment policy.
  - **Eligibility:** uninsured patients or patients with high medical costs at or below **400% of the federal poverty level** (FPL) are eligible. AB 2297 (2024) extended the income threshold up from 350% and prohibited consideration of monetary assets.
  - **Cap on charges:** for eligible patients, the hospital may charge no more than the highest payment the hospital would expect to receive from a government program (Medicare, Medi-Cal, etc.), and for the lowest-income tier, the patient is fully eligible for charity care.
  - **No liens on the patient's primary residence**; no wage garnishments without first determining ineligibility for charity care/discount-payment.
  - **No adverse credit reporting** before completion of the eligibility determination, and following SB 1061, **never** for medical debt.
  - **Extended payment plan** at the patient's option, negotiated based on family income and essential living expenses; statutory cap on interest.
  - **180-day pre-collection window** before assignment to collections, credit reporting, or suit (HSC § 127425(a)).
  - **§ 127425 notice** required before any collection action — includes the patient's right to request an itemized bill, charity-care application, and the eligibility-screening process.
- **Enforcement:**
  - **HCAI Hospital Bill Complaint Program** (see Regulatory Agencies above) investigates and enforces; civil penalties under HSC § 127446.
  - **Patient remedies:** under HSC § 127446 and §§ 127440-127442, a patient who paid more than they should have under a hospital's policies is entitled to reimbursement plus interest. No express private right of action for damages beyond restitution, but the violation also predicates a UCL § 17200 action and may ground common-law claims (unjust enrichment, fraudulent concealment, money had and received).
- **Why it matters:** this is the kit's single most important California-specific cite for any **uninsured, underinsured, or financially eligible patient** facing an acute-care hospital bill — irrespective of whether the hospital is non-profit. Federal § 501(r) is silent for for-profit hospitals; § 127400 et seq. is not.

## Hospital lien

- **Statute:** **Cal. Civ. Code §§ 3045.1-3045.6**
- **Source:** [law.justia.com/codes/california/2005/civ/3045.1-3045.6.html](https://law.justia.com/codes/california/2005/civ/3045.1-3045.6.html); leginfo at [leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CIV&division=4.&title=&part=4.&chapter=4.](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CIV&division=4.&title=&part=4.&chapter=4.)
- **Substance:** A hospital may file a lien against **proceeds of the patient's personal-injury claim against a third party** (e.g., the at-fault driver) for the reasonable and necessary charges of treatment, **capped at 50% of the net recovery** (after attorney's fees and costs and prior liens).
- **Perfection:** notice by **registered or certified mail, return receipt** to the third party and its insurer **before payment of proceeds** to the injured patient (§ 3045.3-3045.4).
- **Scope:** lien attaches only to third-party tort settlement proceeds, **not** to the patient's home, wages, or bank accounts.
- **Use:** rarely controlling in routine billing disputes; matters when the bill stems from an accident with a third-party tortfeasor. Verify notice compliance — defects invalidate the lien.

## Wage garnishment

- **Statute:** **Cal. Code Civ. Proc. §§ 706.010-706.154** (Wage Garnishment Law); exemption procedure at § 706.105; necessary-expenses exemption at § 706.051
- **Source:** [leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CCP&division=&title=9.&part=2.&chapter=5.](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CCP&division=&title=9.&part=2.&chapter=5.)
- **Substance:** Medical-debt creditors cannot garnish wages without first obtaining a court judgment. Post-judgment, garnishment is limited to the **lesser of** (a) 25% of disposable earnings or (b) the amount by which weekly disposable earnings exceed **40 times the state minimum wage** (CCP § 706.050; California's threshold is higher than the federal 30× floor in the CCPA). For high earners, additional restrictions in CCP § 706.052.
- **Necessary-expenses exemption (§ 706.051):** the debtor may apply to exempt the portion of earnings necessary for support of the debtor and family — frequently reduces or eliminates the garnishable amount for low-income debtors.
- **Fair Pricing Act overlay:** under HSC § 127425, the hospital must screen for charity-care/discount-payment eligibility before pursuing collection; a garnishment pursued in violation of that screening is itself a Fair Pricing Act violation and subject to HCAI enforcement.
- **Use:** in response letters to collectors threatening garnishment without a judgment in hand, and in opposition to wage-garnishment notices where charity-care eligibility was never offered.

## Quick reference for letter rendering

When the LLM renders a California-bound letter, substitute these defaults:

| Topic                                                   | Citation / Authority                                                                                                                                                                                   |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Hospital itemization right                              | **Cal. Health & Safety Code § 127425** + **45 C.F.R. § 164.524** (HIPAA, 30-day deadline) + **Cal. Civ. Code § 1788.52(c)** (15-day if in collections)                                                 |
| Hospital charity-care duty                              | **Cal. Health & Safety Code §§ 127400-127446** (Hospital Fair Pricing Act); applies to **all** acute-care hospitals                                                                                    |
| Pre-collection 180-day rule                             | **Cal. Health & Safety Code § 127425**                                                                                                                                                                 |
| Uninsured pre-service estimate                          | **Cal. Health & Safety Code § 1339.585**                                                                                                                                                               |
| Unfair claims practices (regulatory only)               | **Cal. Ins. Code § 790.03(h)** (no private action per *Moradi-Shalal* 46 Cal.3d 287)                                                                                                                   |
| Bad-faith failure to pay (common law)                   | *Gruenberg v. Aetna*, 9 Cal.3d 566 (1973); *Egan v. Mutual of Omaha*, 24 Cal.3d 809 (1979); *Brandt v. Superior Ct.*, 37 Cal.3d 813 (1985) — fully-insured plans only; ERISA-preempted for self-funded |
| Surprise billing (non-emergency at in-network facility) | **Cal. Health & Safety Code § 1371.9** (Knox-Keene); **Cal. Ins. Code §§ 10112.8, 10112.81, 10112.82** (PPO/indemnity)                                                                                 |
| Emergency-services balance billing                      | *Prospect Med. Group*, 45 Cal.4th 497 (2009) (Knox-Keene); AB 72 emergency provisions                                                                                                                  |
| Ground ambulance balance billing                        | **Cal. Health & Safety Code §§ 1371.56, 1797.233**; **Cal. Ins. Code § 10126.66** (AB 716, effective Jan 1, 2024)                                                                                      |
| Medical-debt credit reporting ban                       | **Cal. Civ. Code § 1785.13(a)(8)** (SB 1061, Jan 1, 2025)                                                                                                                                              |
| Independent Medical Review (Knox-Keene)                 | **Cal. Health & Safety Code §§ 1370.4, 1374.30**; file at [healthhelp.ca.gov](https://healthhelp.ca.gov)                                                                                               |
| Independent Medical Review (PPO/indemnity)              | **Cal. Ins. Code §§ 10169-10169.5**; file via CDI                                                                                                                                                      |
| State insurance regulator (HMO/Knox-Keene)              | DMHC Help Center, 1-888-466-2219, [healthhelp.ca.gov](https://healthhelp.ca.gov)                                                                                                                       |
| State insurance regulator (PPO/indemnity)               | CDI Consumer Hotline, 1-800-927-4357, 300 South Spring Street, South Tower, Los Angeles, CA 90013                                                                                                      |
| Hospital billing regulator (Fair Pricing Act)           | HCAI Hospital Bill Complaint Program, [hbcp.hcai.ca.gov](https://hbcp.hcai.ca.gov), 2020 W. El Camino Ave., Ste. 1101, Sacramento, CA 95833                                                            |
| State AG consumer protection                            | Cal. AG Public Inquiry Unit, 1-800-952-5225, P.O. Box 944255, Sacramento, CA 94244-2550, [oag.ca.gov/report](https://oag.ca.gov/report)                                                                |
| Small-claims court name                                 | **Small Claims Division, Superior Court of California, County of [county]**                                                                                                                            |
| Small-claims limit                                      | **$12,500** (natural person); **$6,250** (entity) — Cal. Code Civ. Proc. § 116.220                                                                                                                     |
| Filing fee                                              | $30 / $50 / $75 depending on amount in controversy                                                                                                                                                     |
| Attorney rule                                           | **No attorneys at initial hearing** under Cal. Code Civ. Proc. § 116.530                                                                                                                               |
| Statute of limitations (written contract)               | **4 years** — Cal. Code Civ. Proc. § 337(a)                                                                                                                                                            |
| Statute of limitations (oral contract)                  | **2 years** — Cal. Code Civ. Proc. § 339(1)                                                                                                                                                            |
| UCL claim (insurer or provider)                         | **Bus. & Prof. Code § 17200** — restitution + injunction only, but 4-year SOL and class potential                                                                                                      |

## Key California-specific advantages

Worth keeping in mind when triaging a California patient's bills:

1. **Hospital Fair Pricing Act reaches every acute-care hospital.** Unlike federal § 501(r), § 127400 et seq. binds for-profit, district, and county hospitals — not just non-profits. The patient's charity-care entitlement and the 180-day pre-collection window apply universally. This is the single most important opening cite for an uninsured or 400%-FPL-eligible CA patient.

2. **Bad-faith tort is the strongest in the US.** *Gruenberg/Egan* allow consequential damages including emotional distress (no physical-injury requirement), *Brandt* fees, and punitives — none of which is available under ERISA. For a fully-insured CA carrier acting unreasonably on a coverage or denial decision, a credible bad-faith citation in a demand letter is high-leverage. Verify the plan is **not** self-funded ERISA before citing.

3. **Ground ambulance is covered.** AB 716 closes the federal NSA's biggest gap for fully-insured patients; § 1797.233 also caps uninsured/self-pay ambulance liability at the Medi-Cal or Medicare rate, which is **far below** the typical billed charge. Always check whether a ground-ambulance bill post-dates Jan 1, 2024.

4. **SB 1061 voids medical debt knowingly reported to a CRA.** Most state credit-reporting reforms simply bar the reporting and impose civil penalties. California's voidance language means a furnisher's knowing violation can destroy the debt itself. Watch the FCRA-preemption fight; until the law is enjoined or overridden, cite it.

5. **IMR is free, fast, and the patient wins more often than not.** ~73% of IMR outcomes favor the enrollee, the process takes 30 days, and the decision binds the plan. Always advise an IMR for any medical-necessity denial on a fully-insured Knox-Keene plan; the cost of trying is zero.

6. **No attorneys at small claims (initial hearing).** Cal. Code Civ. Proc. § 116.530 prevents corporate defendants from bringing counsel. Combined with the $12,500 cap for individuals, this makes small claims a viable forum for many medical-billing disputes; the cost-asymmetry runs in the patient's favor because the hospital must send a non-lawyer employee.

7. **Surprise billing is doubly covered.** AB 72 + the federal NSA layer. For emergency services, *Prospect Medical Group* gives Knox-Keene enrollees an absolute bar on balance billing. Use whichever provides the most protection.

8. **HCAI Hospital Bill Complaint Program** is an active, no-fee enforcement venue for Fair Pricing Act violations and the only path that can order **restitution plus interest** to a patient who overpaid. Pair with an AG complaint for pattern-and-practice referrals.
