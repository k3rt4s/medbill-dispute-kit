# Michigan state pack

The fully-worked state-law layer for Michigan patients. The LLM uses this when the patient's state is Michigan. Georgia model at [`laws_state_ga.md`](laws_state_ga.md). All citations verified against public sources as of 2026-05-18. Re-verify annually.

Three things make Michigan unusual on the patient-side billing question, and one of them runs in the patient's favor only sometimes:

1. **No-fault auto insurance is the headline Michigan issue.** Under MCL 500.3105 et seq., if the medical bill stems from a motor-vehicle accident, the patient's auto insurer (PIP) is involved, often as primary payer, and the 2019 reforms (PAs 21 and 22 of 2019) added a Medicare-based fee schedule under MCL 500.3157 that caps provider charges at 200-230% of Medicare. Any accident-related bill that ignores PIP or charges above the fee schedule is disputable on Michigan-specific grounds.
2. **Penalty interest is automatic at 12%.** MCL 500.2006 imposes 12% simple interest on insurer payments not made within 60 days of satisfactory proof of loss. For first-party insureds the interest accrues even when the claim is reasonably in dispute (per the Michigan Supreme Court). This is one of the strongest "soft" levers in the country, and unlike most bad-faith statutes it does not require proving subjective bad intent for a first-party insured to collect interest.
3. **The Michigan Consumer Protection Act is mostly dead against regulated industries.** Per *Smith v. Globe Life Ins.*, 460 Mich. 446 (1999), the MCPA's "specifically authorized" exemption shields entire regulated industries (insurers, banks, often hospitals) from private suit. Do not plead MCPA against an insurer. Hospital billing claims under the MCPA are weaker than in most states; the working tools are MCL 500.2006 (insurer), MCL 500.3157 (auto PIP fee cap), and the federal No Surprises Act.

## Hospital itemization right

- **Statute:** **MCL 333.20201(2)(j)** — Patient's Bill of Rights, in the Public Health Code (Act 368 of 1978, Article 17). The patient or resident is "entitled to receive and examine an explanation of his or her bill regardless of the source of payment and to receive, upon request, information relating to financial assistance available through the health facility or agency." MCL 333.20201(2)(k) adds, for nursing home and home-for-the-aged residents, a monthly itemized statement.
- **Source:** [legislature.mi.gov/Laws/MCL?objectName=mcl-333-20201](https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-333-20201); [law.justia.com/codes/michigan/chapter-333/statute-act-368-of-1978/article-17/division-368-1978-17-201/section-333-20201](https://law.justia.com/codes/michigan/2021/chapter-333/statute-act-368-of-1978/article-17/division-368-1978-17-201/section-333-20201/)
- **What it requires:**
  - Every licensed health facility must adopt and post a written policy describing patient rights, including the right to an explanation of the bill on request.
  - The right is to an "explanation," not specifically an itemized CPT/HCPCS bill. In practice hospitals satisfy the duty by producing the same UB-04 / itemized statement they use for insurer billing, but the statute does not name a deadline.
  - No private right of action is expressly created; the enforcement mechanism is the patient-rights policy plus a complaint to the Michigan Department of Licensing and Regulatory Affairs (LARA), Bureau of Community and Health Systems.
- **Scope:** All licensed health facilities — hospitals, nursing homes, hospices, home-for-the-aged, freestanding surgical outpatient facilities, county medical-care facilities. Outpatient physician offices not licensed as facilities are not covered by Article 17 directly.
- **Federal backstop:** The federal Hospital Price Transparency Rule (45 CFR Part 180) and a hospital's federal Patient Self-Determination obligations cover the gap. Make the written request anyway to crystallize the paper trail.
- **Caveat:** Michigan's hospital-itemization right is one of the weaker state-level versions in the country. Cite it for the principle, but lean on the federal price-transparency rule and any signed financial-responsibility agreement for substantive leverage.

## Uniform Trade Practices Act (UTPA)

- **Statute:** **MCL 500.2001 et seq.** — Chapter 20 of the Insurance Code of 1956 (Act 218 of 1956). Listed unfair claims-settlement practices at **MCL 500.2026**.
- **Source:** [legislature.mi.gov/Laws/MCL?objectName=mcl-Act-218-of-1956](https://www.legislature.mi.gov/Laws/Index?ObjectName=mcl-chap500); [law.justia.com/codes/michigan/2006/mcl-chap500/mcl-218-1956-20.html](https://law.justia.com/codes/michigan/2006/mcl-chap500/mcl-218-1956-20.html)
- **Substance:** Prohibits insurers from misrepresenting policy provisions, failing to acknowledge claims promptly, denying without a reasonable investigation, and a list of similar unfair claims-settlement practices.
- **Critical caveat — no private right of action:** Michigan courts have consistently held there is **no private cause of action under Chapter 20 of the Insurance Code**. *Young v. Michigan Mutual Ins. Co.*, 139 Mich. App. 600 (1984), and subsequent cases bar UTPA tort claims by insureds. A narrow window existed before March 28, 2001 (private actions through MCPA § 445.911 piggybacked on Chapter 20), but Public Act 432 of 2000 closed that window. Today UTPA enforcement is by DIFS only — administrative fines, license sanctions, cease-and-desist orders.
- **Use:** Cite UTPA violations in your complaint to DIFS (see below) and as evidentiary support for collecting MCL 500.2006 penalty interest. Do not plead UTPA as a standalone count in litigation.

## Bad-faith / penalty-interest remedy

- **Statute:** **MCL 500.2006** — Timely-payment requirement and 12% penalty interest. Part of the UTPA Chapter but operating as a self-executing penalty.
- **Source:** [legislature.mi.gov/Laws/MCL?objectName=MCL-500-2006](https://www.legislature.mi.gov/Laws/MCL?objectName=MCL-500-2006); analysis at [michbar.org/file/barjournal/article/documents/pdf4article3401.pdf](https://www.michbar.org/file/barjournal/article/documents/pdf4article3401.pdf)
- **Substance:**
  - An insurer must pay benefits on a timely basis (60 days after receipt of satisfactory proof of loss for first-party insureds, or 30 days after benefits become payable, whichever is later, depending on policy type).
  - **First-party insureds:** Benefits paid late bear 12% simple interest per annum, starting 60 days after satisfactory proof of loss. Per the Michigan Supreme Court in *Nickola v. MIC General Ins. Co.*, 500 Mich. 115 (2017), this interest accrues for first-party insureds **even when the claim is reasonably in dispute**. No bad-faith showing required.
  - **Third-party tort claimants:** Same 12% rate, but only if the insurer's liability "is not reasonably in dispute, the insurer has refused payment in bad faith, and the bad faith was determined by a court of law."
  - Untimely payment without paying the statutory interest is itself an unfair trade practice under MCL 500.2026.
- **No common-law bad-faith tort:** Michigan does **not** recognize a stand-alone first-party bad-faith tort cause of action separate from MCL 500.2006. *Roberts v. Auto-Owners Ins. Co.*, 422 Mich. 594 (1985), and progeny limit insured remedies to the contract damages plus § 2006 penalty interest plus, in narrow cases, mental-anguish damages where intent to cause mental harm is proved.
- **Attorney's fees:** Not directly recoverable under § 2006. Available indirectly under MCR 2.405 case-evaluation sanctions and (in the no-fault PIP context) MCL 500.3148 (unreasonable refusal or delay), but those operate on different triggers.
- **ERISA preemption:** § 2006 is preempted as applied to self-funded ERISA employer plans. For ERISA self-funded plans the federal remedy is 29 U.S.C. § 1132(a)(1)(B) plus possible § 1132(g) attorney's fees. The statute is in play for fully-insured plans, Medicaid managed care, individual/marketplace plans, and Michigan PIP auto coverage.

## Surprise billing — PA 234 of 2020

- **Statute:** **MCL 333.24501 et seq.** — Article 18 of the Public Health Code, "Surprise Medical Billing," added by Public Act 234 of 2020. Companion PA 235 of 2020 amended the Insurance Code. Effective October 22, 2020 (signed) with operational provisions starting in 2021.
- **Note on the user-supplied citation:** The kit's intake form cites "MCL 500.3406z." Michigan's surprise-billing rules sit in the **Public Health Code at MCL 333.24501-333.24517**, not in Chapter 500 of the Insurance Code. PA 235 of 2020 added related Insurance Code amendments, but the consumer-facing surprise-billing prohibitions live in Public Health Code Article 18. Use **MCL 333.24501 et seq.** in dispute letters.
- **Sources:** [legislature.mi.gov/Laws/MCL?objectName=MCL-333-24501](https://www.legislature.mi.gov/Laws/MCL?objectName=MCL-333-24501); statute text [legislature.mi.gov/documents/mcl/pdf/mcl-368-1978-18.pdf](http://www.legislature.mi.gov/documents/mcl/pdf/mcl-368-1978-18.pdf); DIFS consumer summary [michigan.gov/difs/utilization-review/surprise-medical-billing](https://www.michigan.gov/difs/utilization-review/surprise-medical-billing); DIFS 2024 annual report [michigan.gov/difs/-/media/Project/Websites/difs/ORRA/2024_Surprise_Medical_Billing_Annual_Report.pdf](https://www.michigan.gov/difs/-/media/Project/Websites/difs/ORRA/2024_Surprise_Medical_Billing_Annual_Report.pdf)

### What it prohibits

- Balance billing for **emergency services** rendered by a nonparticipating provider at any hospital ED (MCL 333.24507).
- Balance billing for **post-stabilization** services by a nonparticipating provider after admission within 72 hours following an ED visit at a participating facility.
- Balance billing for **non-emergency services** by a nonparticipating provider at a participating facility unless the patient received a written disclosure (12-point font, statutory form per MCL 333.24509) and signed consent at least 14 days in advance.
- Patient cost-sharing capped at the in-network amount; counts toward the in-network deductible and out-of-pocket maximum.

### What it does NOT cover

- **Ground ambulance — not covered.** See ground-ambulance section below. This is the largest gap in Michigan's framework.
- Self-funded ERISA employer plans (preempted; federal NSA applies).
- Workers' compensation, Medicare, Medicaid (federal frameworks apply).

### Caveats

- Disputes between provider and insurer over reimbursement amount go through DIFS-administered arbitration; the patient is held harmless from the rate dispute and is not a party.
- The 14-day advance written disclosure is the provider's loophole — a patient who signed it at admission usually has no Michigan-law surprise-billing protection for that scheduled non-emergency service. The federal NSA imposes additional rules on the form and content of the notice that may invalidate a defective consent.

## Michigan's no-fault auto insurance system

This is the most distinctive Michigan issue. Any medical bill stemming from a motor-vehicle accident, even years after the accident, sits inside the no-fault framework.

- **Statute:** **MCL 500.3101 et seq.** — Michigan No-Fault Insurance Act (Insurance Code Chapter 31). Key provisions:
  - **MCL 500.3105** — PIP scope (insurer pays accidental bodily injury benefits regardless of fault).
  - **MCL 500.3107** — Allowable expenses (medical, attendant care, lost wages, replacement services).
  - **MCL 500.3116** — Reimbursement / lien-like right of the PIP insurer against third-party recovery.
  - **MCL 500.3135** — Tort liability limited to threshold injuries.
  - **MCL 500.3148** — Attorney fees for unreasonable refusal or delay of PIP benefits.
  - **MCL 500.3157** — Provider fee cap (post-2019 reform).
- **Source:** [legislature.mi.gov/Laws/MCL?objectName=mcl-500-3105](https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-500-3105); [legislature.mi.gov/Laws/MCL?objectName=mcl-500-3157](https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-500-3157); DIFS auto-insurance FAQ [michigan.gov/autoinsurance/frequently-asked-questions](https://www.michigan.gov/autoinsurance/frequently-asked-questions)

### Pre-2019 baseline (still relevant for old bills)

Before July 1, 2020 effective date of PAs 21 and 22 of 2019, Michigan required mandatory unlimited lifetime PIP medical coverage. Auto insurer paid 100% of "reasonable and customary" medical charges for accident injuries, with no fee schedule. For accidents before July 1, 2021, the old framework controls.

### Post-2019 reform (PAs 21 and 22 of 2019, effective July 1, 2020 forward)

- **PIP medical coverage is tiered.** Drivers may select $50,000 (Medicaid-enrolled), $250,000, $500,000, or unlimited. Some drivers may opt out entirely if they have Qualified Health Coverage (Medicare A+B, or non-auto-excluding health coverage with deductible ≤ $6,000).
- **Provider fee schedule.** MCL 500.3157 caps charges to PIP insurers at a percentage of Medicare:
  - 200% of Medicare for treatment after July 1, 2023, in general.
  - 230% for Level I/II trauma centers, indigent-volume hospitals, and certain rehab facilities.
  - 240% for treatment July 1, 2022 - July 1, 2023; 245% for July 1, 2021 - July 1, 2022.
  - Where Medicare has no equivalent code, the cap is 55% of the provider's January 1, 2019 charge.
- **Coordinated vs. uncoordinated.** Patients with health insurance often elect "coordinated" PIP, which is cheaper but makes the health plan primary for auto-related medical claims. Uncoordinated PIP makes the auto insurer primary. **Always check which the patient elected before assuming primary payer.**

### How this affects medical-bill disputes

- **Bills above the fee schedule are not collectible from the patient.** MCL 500.3157 is a cap on provider charges, not a floor; any balance billing to the patient above the statutory cap is disputable. Hospitals and rehab facilities have litigated this aggressively since 2021; the Michigan Court of Appeals confirmed the cap applies in *Andary v. USAA Casualty Ins. Co.*, after Supreme Court remand in 2023.
- **The patient is held harmless from the provider-insurer rate dispute.** If a provider bills the patient because the PIP insurer paid less than the provider charged, dispute on the basis that MCL 500.3157 and the no-fault scheme route the rate dispute to the insurer, not the patient.
- **Sleeper issue: re-billed bills after PIP exhaustion.** If the patient elected a $50,000 or $250,000 PIP cap and exhausted it, providers may try to bill the patient or their health plan for the balance. Health insurers cannot deny coverage purely on the ground that the bill "should have been PIP," but coordination-of-benefits disputes proliferate. Cite MCL 500.3109a (coordination provisions) and the patient's health plan's COB language.
- **Attorney fees under MCL 500.3148.** If the PIP insurer's denial or delay is "unreasonable," the no-fault statute awards attorney's fees against the insurer — uniquely strong consumer remedy in PIP cases. This is independent of MCL 500.2006 penalty interest and stacks with it.

### Caveat

The 2019 reform's retroactivity has been heavily litigated. *Andary v. USAA* (Michigan Supreme Court, 2023) held the fee schedule and attendant-care hour limits **cannot be applied retroactively** to accidents that occurred before June 11, 2019. For pre-June-2019 accidents, the unlimited "reasonable and customary" framework governs. For accidents on or after June 11, 2019, the fee schedule applies once it took effect on July 1, 2021.

## Regulatory agencies

### Michigan Department of Insurance and Financial Services (DIFS)

- **Online complaint portal:** [difs.state.mi.us/Complaints/FileComplaint.aspx](https://difs.state.mi.us/Complaints/FileComplaint.aspx); landing page [michigan.gov/difs/consumers/complaint](https://www.michigan.gov/difs/consumers/complaint)
- **Consumer hotline:** **877-999-6442** (Mon-Fri 8 a.m. - 5 p.m. ET)
- **Mail:**
  > Department of Insurance and Financial Services
  > Office of Consumer Services
  > P.O. Box 30220
  > Lansing, MI 48909-7720
- **Fax:** 517-284-8837
- **Email:** difscomplaints@michigan.gov
- **Authority:** All insurance companies licensed in Michigan, including fully-insured health insurers, HMOs, PPOs, Medicare supplement, and auto PIP insurers. Administers the Surprise Medical Billing Act (PA 234 of 2020) and UTPA Chapter 20. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and does not regulate providers, hospitals, or non-insurance debt collectors directly.

### Michigan Attorney General — Consumer Protection Division

- **Online complaint:** [secure.ag.state.mi.us/complaints/consumer.aspx](https://secure.ag.state.mi.us/complaints/consumer.aspx); landing page [michigan.gov/ag/complaints](https://www.michigan.gov/ag/complaints)
- **Phone:** consumer line **517-335-7599**; toll-free in Michigan **877-765-8388**
- **Mail:**
  > Michigan Department of Attorney General
  > Consumer Protection Division
  > P.O. Box 30213
  > Lansing, MI 48909
- **Authority:** Enforces the Michigan Consumer Protection Act, MCL 445.901 et seq., and debt-collection rules. Importantly, AG enforcement is **not limited** by the *Smith v. Globe Life* private-action bar — the AG retains parens-patriae authority even where private plaintiffs are barred. This makes the AG complaint a more meaningful lever in Michigan than the private-litigation MCPA threat. Useful when the dispute is with a hospital's in-house billing department or a non-bank, non-insurance debt collector.

### LARA Bureau of Community and Health Systems (BCHS)

- **Complaint portal:** [michigan.gov/lara/bureau-list/bchs/file-complaint](https://www.michigan.gov/lara/bureau-list/bchs/file-complaint)
- **Authority:** Licensing complaints against hospitals, nursing homes, and other Article 17 health facilities, including violations of the Patient's Bill of Rights under MCL 333.20201. Use this channel for itemization-right violations.

## Michigan Consumer Protection Act (MCPA) — limited

- **Statute:** **MCL 445.901 et seq.** (Public Act 331 of 1976). Listed unfair practices at **MCL 445.903**; private right of action at **MCL 445.911**.
- **Source:** [legislature.mi.gov](https://www.legislature.mi.gov/Laws/Index?ObjectName=mcl-act-331-of-1976); analysis at [michbar.org/file/journal/pdf/pdf4article2070.pdf](https://www.michbar.org/file/journal/pdf/pdf4article2070.pdf) ("The Michigan Consumer Protection Act is Virtually Dead")
- **Substance:** Prohibits unfair, unconscionable, or deceptive methods, acts, or practices in trade or commerce. Provides actual damages or $250, whichever is greater, plus reasonable attorney's fees for private plaintiffs (MCL 445.911).
- **Critical caveat — *Smith v. Globe Life* (1999):** The Michigan Supreme Court held in *Smith v. Globe Life Ins. Co.*, 460 Mich. 446 (1999), that the MCPA's exemption for transactions "specifically authorized" by a regulatory scheme bars private MCPA claims against **any** business in a regulated industry — including insurers, banks, securities dealers, and (in some applications) hospitals. The court read "specifically authorized" to mean the general transaction is authorized, not the specific misconduct. As a result, **most Michigan businesses defending an MCPA suit can move to dismiss on regulated-industry grounds.**
- **Practical posture:**
  - Do not plead MCPA against an insurer (UTPA exclusivity plus *Smith*).
  - MCPA against an in-house hospital billing department is weaker than in most states. Hospitals are licensed under Article 17 and argue *Smith* covers their general billing activity.
  - MCPA against a third-party debt collector is the strongest remaining application, alongside federal FDCPA.
  - The MCPA's **AG enforcement remains intact** — the *Smith* bar limits private actions but not state enforcement.

## Small claims court

- **Court name:** **District Court, Small Claims Division**
- **Jurisdictional limit:** **$7,000**, codified at **MCL 600.8401**
- **Source:** [legislature.mi.gov/Laws/MCL?objectName=mcl-600-8401](https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-600-8401); SCAO bench book [courts.michigan.gov/4a52b3/siteassets/publications/benchbooks/dcmm/dcmmresponsivehtml5.zip/DCMM/Ch_7_Small_Claims/Small_Claims_Division.htm](https://www.courts.michigan.gov/4a52b3/siteassets/publications/benchbooks/dcmm/dcmmresponsivehtml5.zip/DCMM/Ch_7_Small_Claims/Small_Claims_Division.htm); consumer overview [michiganlegalhelp.org/resources/money-debt-and-consumer-issues/overview-of-small-claims-court](https://michiganlegalhelp.org/resources/money-debt-and-consumer-issues/overview-of-small-claims-court)
- **Filing fees (statewide):**
  - $30 for claims $1 - $600
  - $50 for claims $601 - $1,750
  - $70 for claims $1,751 - $7,000
  - Plus service fees (typically $26 certified mail or higher by personal service).
- **Attorney rules:** **Attorneys are prohibited** in the Small Claims Division (MCL 600.8408). Either party may unilaterally remove the case to the regular District Court civil docket and bring counsel; doing so also restores jury-trial rights and full appeal rights, at the cost of formal pleadings and discovery.
- **Jury trial:** Not available in Small Claims Division. Removal to District Court restores jury right.
- **Appeals:** No appeal from the Small Claims Division judgment — by electing small claims the parties waive appeal. This is the cost of the simplified procedure. Either party who wants appeal rights must remove to District Court before judgment.
- **Use:** Strong forum for $7,000-and-under disputes precisely because corporate creditors cannot bring counsel. Hospital billing departments must send a non-attorney representative.

## Statute of limitations

- **Written contracts:** **6 years from breach** — MCL 600.5807(9). The general residual rule for breach of contract claims not otherwise specified.
- **Account stated / open account:** 6 years, generally treated under the same residual rule.
- **Oral contracts:** 6 years (Michigan applies the same 6-year period across most contract claims; this is uniform compared with states that split oral/written at 4/6).
- **Source:** [legislature.mi.gov/Laws/MCL?objectName=mcl-600-5807](https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-600-5807); [law.justia.com/codes/michigan/2022/chapter-600/statute-act-236-of-1961/division-236-1961-58/section-600-5807](https://law.justia.com/codes/michigan/2022/chapter-600/statute-act-236-of-1961/division-236-1961-58/section-600-5807/)
- **Trigger:** Clock runs from the date of breach, typically the day payment was due and not made, not from when the damages were discovered.
- **Tolling:** Partial payment or a written acknowledgment of the debt can restart or extend the clock under MCL 600.5866. **Do not make a partial payment on a time-barred debt without legal advice.** Michigan applies the "new promise" doctrine narrowly but recognizes it.

## Ground-ambulance balance billing

**Not covered by Michigan state law.** Michigan's PA 234 of 2020 surprise-billing framework covers air ambulance (post-2022 amendments) but **explicitly leaves out ground ambulance**. Bridge Michigan reporting (2024) and DIFS guidance both confirm. Source: [bridgemi.com/michigan-health-watch/michigan-ended-surprise-medical-bills-left-out-ground-ambulances/](https://bridgemi.com/michigan-health-watch/michigan-ended-surprise-medical-bills-left-out-ground-ambulances/); [michigan.gov/difs/-/media/Project/Websites/difs/Publication/Health/FIS-PUB_8540.pdf](https://www.michigan.gov/difs/-/media/Project/Websites/difs/Publication/Health/FIS-PUB_8540.pdf).

For ground-ambulance balance bills in Michigan, the patient relies on:

- Federal No Surprises Act — also excludes ground ambulance (the federal gap).
- **No-fault PIP** — if the ambulance run is auto-accident related, the bill is a PIP claim governed by MCL 500.3157's fee schedule (200-230% of Medicare), and the patient is held harmless from the rate dispute. This is the single most useful Michigan-specific ground-ambulance protection, but only when an accident triggered the ride.
- Workers' compensation fee schedule under Mich. Admin. Code R. 418.10926 (work-related rides only).
- Direct negotiation with the ambulance service; many county-operated services have informal financial-hardship policies.

Medical-debt bills SB 449-451 (2025-2026 session, passed Senate March 2026) would impose new restrictions on ambulance billing along with broader hospital reforms, but had not been enacted as of this writing.

## Medical-debt credit reporting

Michigan has **no state-specific medical-debt credit-reporting restriction in force** as of 2026-05-18. Patients in Michigan rely on:

- The 2022-2023 voluntary changes by Equifax/Experian/TransUnion (paid medical debt removed; debt under $500 not reported; 1-year delay before reporting).
- Federal FCRA dispute rights (15 U.S.C. §§ 1681i, 1681s-2).

**Pending legislation (2025-2026 session):** Senate Bills 449, 450, and 451 (the Michigan medical-debt package) passed the Senate in March 2026. SB 451 would prohibit reporting most medical debt to credit bureaus and bar collectors from threatening credit reporting over medical bills. SB 449-450 would codify hospital financial-assistance requirements and limit collections (no foreclosure or wage garnishment for medical debt; cap late fees and interest). House action pending as of this writing. **Check enactment status before relying.** Source: [legislature.mi.gov/documents/2025-2026/billanalysis/Senate/pdf/2025-SFA-0449-G.pdf](https://legislature.mi.gov/documents/2025-2026/billanalysis/Senate/pdf/2025-SFA-0449-G.pdf); [michiganpublic.org/health/2026-03-12/michigan-senate-passes-medical-debt-bills](https://www.michiganpublic.org/health/2026-03-12/michigan-senate-passes-medical-debt-bills).

**Federal preemption posture is in flux.** The CFPB issued an October 2025 interpretive rule taking the position that the FCRA preempts state laws restricting medical-debt credit reporting. If that survives challenge, it would limit the effect of SB 451 if enacted.

## Hospital charity care

Michigan has **no state statute** that broadly mandates a hospital financial-assistance policy. The user's intake form references "MCL 333.21513a" — there is no such section in current Michigan code; that citation appears to be a transposition error.

What Michigan actually has:

- **County medical-care facilities and public hospitals** — county boards of trustees have statutory authority to determine indigency and discount care under various provisions of the Public Health Code (e.g., MCL 333.21501 et seq. for county medical-care facilities). The level of charity care is discretionary, not mandated.
- **Federal IRS § 501(r)** — non-profit hospitals nationally must adopt a written Financial Assistance Policy (FAP), publicize it, screen for FAP eligibility before extraordinary collection actions, and limit charges to amounts generally billed. This is the operative legal floor for most Michigan hospitals (the great majority of MI hospitals are non-profit).
- **Pending SB 449 (2025-2026)** would codify, for hospitals with more than 100 beds, a state-law charity-care mandate at up to 100% discount for income at or below 350% FPL and a mandatory write-off where the bill exceeds 30% of annual household income. Not yet enacted.
- **Healthy Michigan Plan / Medicaid expansion** — for eligible low-income patients, presumptive eligibility through the hospital is often available and is the strongest single charity-care lever.

Use **Dollar For** at [dollarfor.org/state_sheet/michigan](https://dollarfor.org/state_sheet/michigan/) for screening. They maintain the operational rules of every major Michigan hospital's FAP.

## Hospital lien

Michigan does **not have a stand-alone hospital lien statute** of the kind found in Georgia (O.C.G.A. § 44-14-470) or many other states. The user's intake form references "MCL 333.16401" — that section defines the practice of chiropractic and is not a hospital lien statute. There is no MCL 333.16401 hospital lien.

What Michigan actually has in place of a hospital lien:

- **MCL 500.3116** — PIP insurer's lien-like reimbursement right against the patient's third-party tort recovery. Operates inside the no-fault scheme, not as a general hospital lien.
- **Medicaid lien — MCL 400.106(1)(b)(ii)** — state reimbursement against third-party recoveries, with federal preemption issues post-*Wos v. E.M.A.*, 568 U.S. 627 (2013).
- **Contractual subrogation** — most hospital admission agreements include subrogation language allowing the hospital to be reimbursed from a settlement; this is contract, not lien.
- **MCL 600.6303** — collateral source rule with 10-day post-verdict notice requirement for lien-holders, more applicable to ERISA plans and Medicare than to hospital direct liens.

**Practical implication:** When a Michigan provider claims it has a "lien" on a personal-injury settlement, scrutinize whether the claim arises from MCL 500.3116 (PIP reimbursement), a Medicaid lien, or a contractual subrogation clause. If it is contractual, the standard rules of contract interpretation, made-whole doctrine, and equitable subrogation apply, and the "lien" terminology is often overstated.

## Wage garnishment

- **Statute:** **MCL 600.4011 et seq.** (garnishment generally); **MCL 600.4012** (post-judgment); federal cap incorporated via **15 U.S.C. § 1673**
- **Substance:** Medical-bill creditors cannot garnish wages without first obtaining a court judgment. Post-judgment, garnishment is capped at the federal 25% of disposable earnings (or the amount by which weekly disposable earnings exceed 30× the federal minimum wage, whichever is less).
- **Use:** In response letters to collectors threatening garnishment without a judgment in hand. Pending SB 449-451 (2025-2026) would prohibit wage garnishment for medical debt entirely if enacted.

## Quick reference for letter rendering

When the LLM renders a Michigan-bound letter, substitute these defaults:

- **State statute (itemization right):** **MCL 333.20201(2)(j)** — Patient's Bill of Rights, right to an explanation of the bill on request. Pair with the federal Hospital Price Transparency Rule (45 CFR Part 180) for stronger leverage.
- **State insurance department (CC line):** Department of Insurance and Financial Services, Office of Consumer Services, P.O. Box 30220, Lansing, MI 48909-7720 ([michigan.gov/difs](https://www.michigan.gov/difs/)); consumer line 877-999-6442
- **State AG consumer protection (CC line):** Michigan Department of Attorney General, Consumer Protection Division, P.O. Box 30213, Lansing, MI 48909 ([michigan.gov/ag](https://www.michigan.gov/ag/)); 877-765-8388
- **Small-claims court name:** **District Court of [judicial district], Small Claims Division** (e.g., "37th District Court, Small Claims Division")
- **Filing fee (in 30-day warning):** "$30 - $70 depending on claim amount, plus service fee, capped at the small-claims limit of $7,000"
- **Statute of limitations (in 30-day warning):** "MCL 600.5807(9) (six years for breach of written contract)"
- **For insurer late-payment disputes:** Cite **MCL 500.2006** (12% penalty interest, automatic for first-party insureds after 60 days). This is the single highest-leverage Michigan-specific cite against an insurer.
- **For motor-vehicle-accident bills:** Cite **MCL 500.3157** (PIP provider fee cap, 200-230% of Medicare) and **MCL 500.3148** (PIP attorney's fees for unreasonable delay). Confirm the patient's PIP election (coordinated vs. uncoordinated) and accident date relative to June 11, 2019 and July 1, 2021 cutoffs.
- **For surprise out-of-network ED bills:** Cite **MCL 333.24501 et seq.** (PA 234 of 2020); federal NSA stacks on top.
- **Do NOT plead:** MCPA against insurers (UTPA exclusivity); UTPA in court (no private right of action); common-law bad faith (Michigan does not recognize it as a stand-alone tort).

## Key Michigan-specific advantages

Worth keeping in mind when triaging a Michigan patient's bills:

1. **Automatic 12% penalty interest for first-party insureds (MCL 500.2006).** No bad-faith showing required for first-party claimants. After day 60 from satisfactory proof of loss, interest accrues even if the claim is reasonably in dispute. Always invoke when an insurer drags its feet on a fully-insured health-plan claim.
2. **No-fault PIP fee cap (MCL 500.3157).** For any motor-vehicle accident bill, the patient is held harmless from the provider-insurer rate dispute, and the cap is 200-230% of Medicare. A provider trying to balance bill the patient above the fee schedule is acting outside the no-fault framework and the bill is disputable on statutory grounds.
3. **No-fault attorney's fees (MCL 500.3148).** Independent of penalty interest, attorney's fees against the PIP insurer for "unreasonable refusal or delay." Among the strongest insurance-consumer attorney-fee provisions in the country, making private representation economically feasible.
4. **Attorney-prohibited small claims (MCL 600.8408).** Up to $7,000, hospital billing departments cannot bring counsel. Either side may remove to District Court to restore counsel rights, but removal forces them to litigate formally — an asymmetric cost shift that favors the patient.
5. **AG consumer protection works around the MCPA private-action bar.** *Smith v. Globe Life* killed private MCPA suits against regulated industries but did not touch AG enforcement. A well-documented complaint to the Michigan AG's Consumer Protection Division retains real teeth, especially against hospital billing practices and non-bank debt collectors.

## Notes on user-supplied citations

The intake form for this Michigan pack referenced two statute numbers that do not match Michigan's current code:

- **"MCL 500.3406z"** for surprise billing — the operative Michigan surprise-billing provisions are in the **Public Health Code at MCL 333.24501 et seq.** (added by PA 234 of 2020). PA 235 of 2020 added related Insurance Code amendments but the consumer-facing prohibitions sit in Article 18 of the Public Health Code. Use **MCL 333.24501 et seq.**
- **"MCL 333.21513a"** for charity care — no such section exists in current Michigan code. Michigan has no broad statutory charity-care mandate; non-profit hospitals operate under federal IRS § 501(r). Pending SB 449 (2025-2026) would create a state-law mandate but is not yet enacted.
- **"MCL 333.16401"** for hospital lien — this section defines chiropractic practice and is not a lien statute. Michigan does not have a stand-alone hospital lien statute; the operative provisions for accident-related billing are MCL 500.3116 (no-fault PIP reimbursement) and contractual subrogation clauses.

A future maintainer should update the project intake form to remove these incorrect cite stubs.
