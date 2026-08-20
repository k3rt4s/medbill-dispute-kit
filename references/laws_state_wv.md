# West Virginia state pack

The fully-worked state-law layer for West Virginia patients. The LLM uses this when the patient's state is West Virginia. Kentucky equivalent at [`laws_state_ky.md`](laws_state_ky.md), Virginia at [`laws_state_va.md`](laws_state_va.md). All citations verified against public sources as of 2026-08-19. Re-verify annually.

Four things make West Virginia's patient-side leverage distinctive:

1. **The West Virginia Consumer Credit and Protection Act (WVCCPA) treats the hospital's own billing office as a "debt collector."** W. Va. Code § 46A-2-122 defines "debt collector" as "any person or organization engaging directly or indirectly in debt collection," with no blanket exclusion for a creditor collecting its own claim. This is broader than the federal FDCPA, which exempts original creditors entirely. A West Virginia patient can invoke the Article 2 debt-collection catalog (oppression, deception, unconscionable means) directly against the hospital, not just against a third-party collection agency, and can sue for actual damages plus a **$1,000-per-violation statutory penalty** under § 46A-5-101.
2. **Wage garnishment for a medical debt judgment is capped at 20% of disposable earnings**, W. Va. Code § 46A-2-130 and the parallel general-execution cap at § 38-5A-3, both tighter than the federal Consumer Credit Protection Act's 25% ceiling (15 U.S.C. § 1673). This is a concrete, quantifiable way state law beats the federal floor.
3. **The WVCCPA requires a 45-day cure notice before suit**, W. Va. Code § 46A-5-108, which means a WVCCPA claim is not filed cold. The patient (or their attorney) must send written notice by certified mail identifying the violation; the creditor gets 45 days to cure (20 if suit is already filed). This is a real procedural step, not a formality to skip.
4. **Hayseeds, Inc. v. State Farm Fire & Cas. Co.**, 177 W. Va. 323, 352 S.E.2d 73 (1986), gives West Virginia one of the most patient-favorable first-party bad-faith rules in the country: once the insured substantially prevails against the insurer, the insurer owes attorney's fees (presumptively one-third of the policy proceeds) and consequential damages, **regardless of whether the initial denial was in good faith or bad faith**.

Two things cut against the patient and are flagged below: the state's **hospital itemization statute was repealed in 2024 with no replacement** (federal price transparency is the fallback), and West Virginia's new **ground-ambulance balance-billing protection does not take effect until policies issued on or after January 1, 2027**, so it does not help a patient with a ground-ambulance bill today.

## Hospital itemization right

- **Former statute:** W. Va. Code § 16-5B-9 required hospitals and similar institutions to furnish one itemized statement of charges to a paying patient on request, at no cost.
- **Status: repealed.** The section was repealed by the 2024 Regular Session's Senate Bill 300. The current page at [code.wvlegislature.gov/16-5B-9](https://code.wvlegislature.gov/16-5B-9/) shows only the former heading marked "[Repealed.]"
- **No replacement found.** A review of the current Article 16-5B index ([code.wvlegislature.gov/16-5B](https://code.wvlegislature.gov/16-5B/)) and the West Virginia Hospital Licensure Rule (W. Va. C.S.R. Title 64, Series 12, [law.cornell.edu/regulations/west-virginia/agency-64/title-64/series-64-12](https://www.law.cornell.edu/regulations/west-virginia/agency-64/title-64/series-64-12)) turned up no current state-law or state-rule itemization right.
- **What this means:** West Virginia patients requesting an itemized bill should cite the **federal Hospital Price Transparency Rule (45 CFR Part 180)** and the general federal price-transparency framework, see [`laws_federal.md`](laws_federal.md). There is no state-law deadline or private remedy to fall back on for a refused itemization request. Send the request in writing by certified mail regardless, for the paper trail.

## West Virginia Consumer Credit and Protection Act (WVCCPA)

- **Statute:** West Virginia Code Chapter 46A. Debt-collection catalog at Article 2, Part relating to debt collection (§§ 46A-2-122 through 46A-2-130-ish); general consumer protection at Article 6; civil liability at Article 5.
- **Source:** [code.wvlegislature.gov/46A-2](https://code.wvlegislature.gov/46A-2/); [code.wvlegislature.gov/46A-5-101](https://code.wvlegislature.gov/46A-5-101/); [code.wvlegislature.gov/46A-6-104](https://code.wvlegislature.gov/46A-6-104/)

### Who and what it covers

- **"Claim," § 46A-2-122:** "Any obligation or alleged obligation of a consumer to pay money arising out of a transaction" where the money, property, insurance, **or service** is primarily for personal, family, or household purposes. Medical care is a service rendered for personal purposes, so a hospital bill is a "claim" under this article.
- **"Debt collector," § 46A-2-122:** "Any person or organization engaging directly or indirectly in debt collection." The only carve-out is for attorneys collecting in their own name as licensed West Virginia counsel. **There is no exclusion for a creditor collecting its own debt**, unlike the federal FDCPA, where a creditor collecting in its own name under its own name is not a "debt collector" at all. This is the single biggest practical difference from the federal floor: the hospital's own billing department and any in-house collector are reachable under this article, not just an outside agency.

### The prohibited-practices catalog

- **§ 46A-2-125, oppression and abuse:** no profane or abusive language; no more than 30 calls per week or 10 telephone conversations per week; no calls at unusual or known-inconvenient times (default convenient window is 8:00 a.m. to 9:00 p.m., local time to the consumer).
- **§ 46A-2-126, unreasonable publication** of the debt to third parties.
- **§ 46A-2-127, fraudulent, deceptive, or misleading representations:** eight enumerated practices, including misrepresenting the character, extent, or amount of the claim, using a false business name, falsely implying government affiliation, and sending simulated legal or official documents.
- **§ 46A-2-128, unfair or unconscionable means:** includes billing the consumer for the collector's own collection fee (subject to a narrow education-loan exception), adding interest or charges not authorized by the underlying obligation, contacting a consumer known to be represented by an attorney more than three business days after notice, and failing to disclose that a time-barred debt cannot be sued upon.
- **Source for all of the above:** [code.wvlegislature.gov/46A-2-125](https://code.wvlegislature.gov/46A-2-125/); [code.wvlegislature.gov/46A-2-127](https://code.wvlegislature.gov/46A-2-127/); [code.wvlegislature.gov/46A-2-128](https://code.wvlegislature.gov/46A-2-128/)

### Civil liability, § 46A-5-101

- **Actual damages**, plus
- **A statutory penalty of $1,000 per violation**, with the aggregate penalty award capped at the greater of **$175,000 or the total alleged/outstanding indebtedness**
- **4-year limitation period**: "no action pursuant to this subsection may be brought more than four years after the violations occurred." This is a separate, shorter clock than the general contract statute of limitations below, it runs from the collection misconduct, not from the original bill.
- **Bona fide error defense:** no liability if the creditor shows the violation was unintentional and resulted from a bona fide error despite procedures reasonably adapted to avoid it.
- **Source:** [code.wvlegislature.gov/46A-5-101](https://code.wvlegislature.gov/46A-5-101/)

### Attorney's fees, § 46A-5-104

Attorney's fees are **discretionary, not automatic**. The court weighs statutory factors before awarding fees to a prevailing consumer, and can award fees to the defendant if the consumer's suit was brought in bad faith for harassment. Do not tell a patient fees are guaranteed; describe this as a fee-shifting possibility the court controls.

- **Source:** [code.wvlegislature.gov/46A-5-104](https://code.wvlegislature.gov/46A-5-104/)

### Right-to-cure notice, § 46A-5-108 (do this before suing)

- The consumer must send **written notice by certified mail** to the creditor's or collector's registered agent or principal place of business, describing the violation and its factual basis.
- The creditor/collector then has **45 days** to make a cure offer (**20 days** if a lawsuit has already been filed).
- If the consumer accepts the cure offer and it is completed within a reasonable time, that is a **complete defense** to the WVCCPA claim, and the creditor can recover its own attorney's fees for defending the (now-cured) action.
- The limitations period is **tolled during the 45-day window**, so sending the notice does not cost the patient time on the clock.
- **Use in the kit:** build this notice-and-wait step into any WVCCPA-based letter for a West Virginia patient. Skipping it is a mistake, not just a formality, the case can be dismissed for failure to give notice.
- **Source:** [code.wvlegislature.gov/46A-5-108](https://code.wvlegislature.gov/46A-5-108/)

### General consumer protection, a separate and broader layer, Article 6

- **Statute:** W. Va. Code § 46A-6-104 declares "unfair methods of competition and unfair or deceptive acts or practices in the conduct of any trade or commerce" unlawful, interpreted consistently with FTC Act guidance.
- **Private right of action, § 46A-6-106:** a consumer who purchases goods or services and suffers a loss from a violation may sue in circuit court for **actual damages or $200, whichever is greater**, plus equitable relief. This is a **different, smaller-dollar** remedy than the Article 5/debt-collection track above, use it for deceptive billing conduct that is not specifically a collection-abuse claim (for example, a hospital's misrepresentation about what insurance would cover, made before any collection activity started).
- **Source:** [code.wvlegislature.gov/46A-6-104](https://code.wvlegislature.gov/46A-6-104/); [code.wvlegislature.gov/46A-6-106](https://code.wvlegislature.gov/46A-6-106/)

### AG enforcement authority

- W. Va. Code § 46A-7-101 creates a Division of Consumer Protection under the Attorney General; § 46A-7-102 gives the AG power to receive complaints, investigate, seek voluntary compliance, and prosecute enforcement actions under the chapter.
- **Source:** [code.wvlegislature.gov/46A-7-101](https://code.wvlegislature.gov/46A-7-101/) (article index at [code.wvlegislature.gov/email/46a-7](https://code.wvlegislature.gov/email/46a-7/))

### ERISA note

Nothing above reaches a self-funded ERISA employer health plan's benefit-denial decisions, those are governed by 29 U.S.C. § 1132(a) (see `laws_federal.md`). The WVCCPA debt-collection catalog does, however, still reach a **hospital's own billing conduct** regardless of how the patient's insurance is structured, because the claim runs against the provider or its collector, not against the health plan.

## West Virginia Unfair Trade Practices Act

- **Statute:** W. Va. Code § 33-11-4, unfair methods of competition and unfair or deceptive acts or practices defined; unfair claims-settlement practices at § 33-11-4(9)
- **Source:** [code.wvlegislature.gov/33-11-4](https://code.wvlegislature.gov/33-11-4/)
- **Substance:** Section (9) lists the standard NAIC-model catalog: misrepresenting policy provisions, failing to acknowledge claims promptly, failing to adopt reasonable claim-investigation standards, refusing to pay without a reasonable investigation, failing to affirm or deny coverage in a reasonable time, and not attempting in good faith to effectuate a prompt, fair, equitable settlement.
- **Claim-handling timeline:** an insurer must notify a first-party claimant in writing within **15 calendar days** of initial notification, and every **30 calendar days** thereafter if more time is needed, and a claim generally cannot remain unsettled and unpaid more than **90 calendar days** from the filing of proof of loss absent a legitimate coverage/liability/damages dispute or claimant fraud.
- **Third-party claimants: no private cause of action.** W. Va. Code § 33-11-4a expressly states that "a third-party claimant may not bring a private cause of action or any other action against any person for an unfair claims settlement practice." The exclusive remedy for a third-party claimant is an **administrative complaint to the Insurance Commissioner within one year** of discovering the alleged violation.
- **Source:** [code.wvlegislature.gov/33-11-4a](https://code.wvlegislature.gov/33-11-4a/)
- **Penalty:** the Commissioner can assess penalties up to **$250,000** if the insurer's unfair claims-settlement practices are found to be a general business practice, an administrative remedy, not a patient's direct recovery.
- **Practical posture for a West Virginia patient:** if the dispute is with your **own** health insurer (first-party), file a Commissioner complaint citing § 33-11-4(9) for the regulatory record, and use the common-law **Hayseeds** bad-faith doctrine below for a direct private remedy. If the dispute is as a **third party** (for example, a claim against another driver's auto insurer for medical expenses from a crash), § 33-11-4a limits you to the administrative complaint, there is no private UTPA suit available.

## Bad-faith failure to pay

- **Case:** ***Hayseeds, Inc. v. State Farm Fire & Cas. Co.***, 177 W. Va. 323, 352 S.E.2d 73 (1986)
- **Source:** [law.justia.com/cases/west-virginia/supreme-court/1986/16782-5.html](https://law.justia.com/cases/west-virginia/supreme-court/1986/16782-5.html)
- **The rule:** when a policyholder substantially prevails in an action to recover insurance benefits, the insurer is liable for the insured's **reasonable attorney's fees** and **net economic loss** caused by the delay in payment (including aggravation and inconvenience), **regardless of whether the insurer's initial refusal to pay was in good faith or bad faith**. Once the breach is established, the good-faith/bad-faith question becomes largely irrelevant to this remedy.
- **Fee measure:** presumptively **one-third of the face amount of the policy**, unless the policy is unusually small or unusually large.
- **Two overlapping but distinct doctrines:** West Virginia recognizes both this common-law/contractual bad-faith rule (**Hayseeds**) and a statutory catalog of unfair claims-settlement conduct (§ 33-11-4(9), above). They are not the same cause of action and have different elements and forums, Hayseeds is a private court remedy for first-party insureds; § 33-11-4(9) is enforced administratively by the Commissioner (and is expressly barred as a private third-party suit under § 33-11-4a).
- **ERISA preemption:** as with every state's common-law bad-faith doctrine, Hayseeds-based claims against a self-funded ERISA employer health plan are preempted. The federal remedy for those plans is 29 U.S.C. § 1132(a)(1)(B) (see `laws_federal.md`). Hayseeds remains available for fully-insured plans, Medicaid managed care, and individual/marketplace coverage.

## Surprise billing

West Virginia has **not** enacted a comprehensive state surprise-billing statute broader than the federal No Surprises Act for general emergency and out-of-network-at-in-network-facility scenarios. The federal NSA (effective January 1, 2022) is the operative substantive protection, see [`laws_federal.md`](laws_federal.md).

- **State enforcement add-on:** W. Va. Code § 33-2-24 gives the Insurance Commissioner express statutory authority to **enforce the federal No Surprises Act** directly against health insurers, medical providers, and health care facilities, with an administrative fine of **up to $10,000 per violation** after notice and hearing (§ 33-2-13), plus the ability to seek injunctive relief in court.
- **Source:** [code.wvlegislature.gov/33-2-24](https://code.wvlegislature.gov/33-2-24/)
- **Practical use:** a West Virginia patient with an NSA violation has **two complaint channels**, not just one: the federal No Surprises Help Desk (1-800-985-3059) and a West Virginia Offices of the Insurance Commissioner complaint citing § 33-2-24. Filing with the state regulator adds a second enforcement track without displacing the federal one.

## Regulatory agencies

### West Virginia Offices of the Insurance Commissioner (OIC), Life and Health Consumer Services

- **Online complaint:** [sbs.naic.org online consumer complaint form, West Virginia](https://sbs.naic.org/solar-web/pages/public/onlineComplaintForm/onlineComplaintForm.jsf?dswid=7997&spanish=N&state=WV) (linked from [wvinsurance.gov/Consumer_Services](https://www.wvinsurance.gov/Consumer_Services))
- **Phone (Life & Health):** (304) 720-8584
- **Phone (general/toll-free):** 1-888-TRY-WVIC (1-888-879-9842); local (304) 558-3386
- **Email (Life & Health):** OICConsumerServicesLH@wv.gov
- **Mail:**
  > WV Offices of the Insurance Commissioner
  > Consumer and Claims Services Division
  > P.O. Box 50540
  > Charleston, WV 25305-0540
- **Authority:** fully-insured health, life, dental, vision, and annuity plans; administers the Unfair Trade Practices Act (§ 33-11) and, per § 33-2-24, has delegated enforcement authority over the federal No Surprises Act. **No authority over self-funded ERISA plans** (route to DOL EBSA at 1-866-444-3272) and does not regulate providers, hospitals, or debt collectors as such (route those to the AG).
- **Source:** [wvinsurance.gov/Consumer_Services](https://www.wvinsurance.gov/Consumer_Services); [wvinsurance.gov/Consumer-Services-P-C](https://www.wvinsurance.gov/Consumer-Services-P-C)

### West Virginia Attorney General, Consumer Protection and Antitrust Division

- **Online complaint:** [wv.accessgov.com/ago/Forms/Page/consumercomplaint/file/1](https://wv.accessgov.com/ago/Forms/Page/consumercomplaint/file/1)
- **Phone:** (304) 558-8986; toll-free 1-800-368-8808
- **Email:** consumer.complaint@wvago.gov
- **Mail:**
  > Office of the Attorney General
  > Consumer Protection and Antitrust Division
  > P.O. Box 1789
  > Charleston, WV 25326
- **Physical address:** State Capitol Complex, Building 6, Suite 401, Charleston, WV 25305
- **Authority:** enforces the WVCCPA (Chapter 46A) generally, including the Article 2 debt-collection catalog and the Article 6 general consumer-protection provisions, against hospitals' in-house billing departments, physician practices, and third-party debt collectors as original creditors or collectors. This is the right venue for billing-fraud, deceptive-billing, and aggressive-collection complaints, the gap not covered by the OIC (which only regulates insurers).
- **Source:** [ago.wv.gov/consumer-protection-and-antitrust-division](https://ago.wv.gov/consumer-protection-and-antitrust-division)

## Small claims court, Magistrate Court civil division

- **Court name:** **Magistrate Court**, civil division, of the relevant county
- **Jurisdictional limit:** **$20,000**, exclusive of interest and costs, W. Va. Code § 50-2-1. This limit was raised from $10,000 to $20,000 by 2025 House Bill 2761.
- **Source:** [code.wvlegislature.gov/50-2-1](https://code.wvlegislature.gov/50-2-1/)
- **Filing fees**, W. Va. Code § 50-3-1, scaled to the amount sought:
  - $500 or less: **$30**
  - $500 to $1,000: **$35**
  - $1,000 to $2,000: **$40**
  - Over $2,000: **$50**
  - Relief other than money damages: **$30**
- **Source:** [code.wvlegislature.gov/50-3-1](https://code.wvlegislature.gov/50-3-1/)
- **Attorney rule:** permitted, not required. W. Va. Code § 50-4-4a: "Any party to a civil action in a magistrate court may appear and conduct such action in person, by agent or by attorney," and appearance by an agent does not constitute the unauthorized practice of law.
- **Source:** [code.wvlegislature.gov/50-4-4a](https://code.wvlegislature.gov/50-4-4a/)
- **Appeal:** a notice of appeal to the circuit court must be filed within **20 days** of judgment (or of the denial of a motion for new trial). A late appeal may still be granted by the circuit court up to 90 days after judgment on a showing of good cause.

## Statute of limitations

- **Written contracts:** **10 years** from breach, W. Va. Code § 55-2-6
- **Oral or unwritten contracts:** **5 years** from breach, same section
- **Source:** [code.wvlegislature.gov/55-2-6](https://code.wvlegislature.gov/55-2-6/)
- **WVCCPA collection-abuse claims specifically:** a separate, shorter **4-year** clock from the date of the violation applies to a civil action under § 46A-5-101 (see above), this runs from the collection misconduct, not from the underlying bill.

Most West Virginia hospital admissions involve a signed financial-responsibility or consent-to-treat form, a written contract, so the 10-year period is the one to use for the underlying billing dispute. Partial payment or written acknowledgment of a debt can restart the clock under general common-law principles applied in West Virginia courts. **Do not make a partial payment on a debt you believe may be time-barred without legal advice.**

## Ground ambulance balance-billing

- **Status: a real but not-yet-operative protection.**
- **Statute:** W. Va. Code § 33-25A-38, "Prohibiting surprise billing of ground emergency medical services by non-participating providers," enacted by 2026 Regular Session Senate Bill 645
- **Source:** [code.wvlegislature.gov/33-25A-38](https://code.wvlegislature.gov/33-25A-38/)
- **What it prohibits:** a non-participating emergency medical services agency is barred from billing the covered individual for any amount beyond the copayment, coinsurance, deductible, and other cost-sharing the individual would owe for an in-network ambulance.
- **Payment rate:** the insurer must pay the **lesser of** 200% of the current CMS-published ambulance rate for the same service in the same geographic area, or the non-participating agency's actual billed charges. Direct payment to the provider is required within 30 days of a clean claim.
- **Effective date:** the section applies to a **health insurance policy issued by an insurer on or after January 1, 2027**. It excludes insurers under contract with the Bureau for Medical Services for Medicaid or CHIP.
- **What this means today:** as of this writing, most West Virginia patients' current health plans were issued **before** January 1, 2027, so this protection is **not yet operative for them**. A ground-ambulance balance bill received now still has **no state-law hold-harmless protection**, the same gap the federal NSA leaves open nationally. An earlier, similar bill (2025 Senate Bill 632) passed the Senate but died in the House Finance Committee without becoming law; SB 645 is the version that succeeded in the 2026 session.
- **Scope caveat:** § 33-25A-38 is codified within Article 25A, the **Health Maintenance Organization Act**. Secondary sources describe the 2026 legislation as reaching "commercial health insurance plans" generally, but this pack could only independently verify the codified text within the HMO article. Confirm whether a parallel provision reaches non-HMO accident-and-sickness insurers (Article 15/16) before relying on this for a PPO or indemnity plan; see the gaps section below.
- **Practical posture for a current ground-ambulance bill:** (a) the general reasonableness of the charge can be challenged directly with the provider; (b) a WVCCPA § 46A-2-127/128 deceptive- or unconscionable-billing theory applies if the bill misrepresents what is owed; (c) for a self-funded ERISA plan, file with DOL EBSA (1-866-444-3272); (d) negotiate using the Medicare ambulance fee schedule as a benchmark, the same 200% figure the 2027 rule will eventually require.

## Credit reporting

West Virginia has **not** enacted a state-level restriction on reporting medical debt to credit bureaus. It is not among the roughly 15 states (California, Colorado, Connecticut, Delaware, Illinois, Maine, Maryland, Minnesota, New Jersey, New York, Oregon, Rhode Island, Vermont, Virginia, Washington) that have passed such laws as of this writing. West Virginia patients rely on:

- The 2022 to 2023 voluntary changes by Equifax, Experian, and TransUnion (paid medical collections removed; one-year delay before reporting; medical collections under $500 excluded).
- Federal FCRA dispute rights (15 U.S.C. §§ 1681i, 1681s-2), see `laws_federal.md`.
- The WVCCPA's general consumer-protection layer (§ 46A-6-104) where furnishing inaccurate medical-debt information to a bureau is part of a broader deceptive pattern.

The federal preemption landscape is unsettled (a federal court vacated the CFPB's 2025 medical-debt credit-reporting rule, and an October 2025 CFPB interpretive position argues the FCRA preempts state medical-debt reporting bans). This affects the states with their own bans more than West Virginia, which has none to preempt, but re-verify annually.

## Hospital charity care

- **No dedicated West Virginia charity-care or financial-assistance statute was found.** West Virginia does not appear to impose FAP eligibility criteria, application windows, or collection-timing rules beyond the federal floor. All West Virginia non-profit hospitals remain subject to **federal IRS § 501(r)** (26 U.S.C. § 501(r); 26 C.F.R. §§ 1.501(r)-1 through -7), covered in `laws_federal.md`: a published Financial Assistance Policy, the "amounts generally billed" cap for FAP-eligible patients, and a reasonable-effort screening requirement before extraordinary collection actions.
- **A related but distinct regulation:** W. Va. Code of State Rules § 110-3-24 ("Charitable Hospitals") sets criteria for a hospital's **property-tax exemption**, requiring a board-approved charity-care plan, posted notices in admitting and emergency areas, and a prohibition on withholding emergency care pending payment assurance. This is a tax-exemption eligibility rule, not a patient-facing billing or collection-timing statute, but it is useful leverage: if a non-profit hospital claims this exemption, it has represented to the state that it maintains a charity-care plan, and a patient can demand to see it.
- **Source:** [law.cornell.edu/regulations/west-virginia/W-Va-C-S-R-SS-110-3-24](https://www.law.cornell.edu/regulations/west-virginia/W-Va-C-S-R-SS-110-3-24)
- **For-profit hospitals:** no federal § 501(r) coverage and no state-law analogue found. Leverage is limited to the WVCCPA deception theory and whatever FAP the hospital has voluntarily adopted.
- **Use Dollar For** at [dollarfor.org/state_sheet/west-virginia](https://dollarfor.org/state_sheet/west-virginia/) for screening; note that Dollar For's own state page states plainly that West Virginia has no charity-care law of its own and federal law applies.

## Hospital lien statute

- **No dedicated West Virginia hospital lien statute was located.** A targeted search of the official code site for lien provisions turned up only unrelated statutes: W. Va. Code Chapter 38 (mechanics', vendors', and judgment liens, none patient-specific) and W. Va. Code § 16-29A (the Hospital Finance Authority Act, which covers **bond financing** liens for hospital construction, not liens against a patient's personal-injury recovery).
- **What this means:** absent a statutory hospital lien, a West Virginia provider seeking to reach a patient's personal-injury settlement must do so by **contractual assignment or letter of protection** signed at admission, by **subrogation** under the patient's own health plan, or by **first obtaining a judgment** and then pursuing ordinary post-judgment collection. A purported "hospital lien" that does not rest on one of these has no independent statutory basis in West Virginia.
- **Demand the basis:** if a hospital or its collector asserts a lien, ask them to identify the specific contract clause, judgment, or subrogation right it rests on. They cannot point to a West Virginia hospital-lien statute, because this pack could not locate one.
- **Caveat:** this is an absence-of-evidence finding, not a certainty. See the gaps section below.

## Wage garnishment

- **Statutes:** W. Va. Code § 46A-2-130 (WVCCPA-specific cap) and § 38-5A-3 (general suggestee-execution cap), both consistent
- **Source:** [code.wvlegislature.gov/46A-2-130](https://code.wvlegislature.gov/46A-2-130/); [code.wvlegislature.gov/38-5A-3](https://code.wvlegislature.gov/38-5A-3/)
- **The cap:** garnishment of disposable weekly earnings may not exceed the **lesser of** (a) **20%** of disposable earnings for that week, or (b) the amount by which weekly disposable earnings exceed **50 times the federal minimum hourly wage**. This is more protective than the federal Consumer Credit Protection Act's 25% ceiling (15 U.S.C. § 1673, see `laws_federal.md`).
- **Hardship relief:** a debtor may petition the court to reduce or eliminate garnishment on a showing of undue hardship to themselves or their family.
- **Priority:** child- and spousal-support withholding orders take priority over an ordinary consumer-debt garnishment.
- **Judgment required first:** garnishment cannot begin without an underlying judgment. A collector who threatens garnishment before obtaining one is making a false or misleading representation actionable under WVCCPA § 46A-2-127.

## Quick reference for letter rendering

When the LLM renders a West Virginia-bound letter, substitute these defaults:

| Field                                                                   | Default value                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Itemization statute**                                                 | None currently in force. W. Va. Code § 16-5B-9 was repealed in 2024 with no replacement; cite the federal Hospital Price Transparency Rule (45 CFR Part 180) instead.                                                                            |
| **Headline cite for collection abuse by the hospital or its collector** | **W. Va. Code § 46A-2-125/127/128** (WVCCPA debt-collection catalog, reaches original creditors) plus **§ 46A-5-101** (actual damages + $1,000/violation statutory penalty). Remember the **45-day cure notice under § 46A-5-108** before suing. |
| **Headline cite for deceptive billing not framed as collection abuse**  | **W. Va. Code § 46A-6-104/106** (general consumer protection, actual damages or $200 minimum)                                                                                                                                                    |
| **State insurance department (CC line)**                                | WV Offices of the Insurance Commissioner, Consumer and Claims Services Division, P.O. Box 50540, Charleston, WV 25305-0540 (toll-free 1-888-TRY-WVIC / 888-879-9842)                                                                             |
| **State AG consumer protection (CC line)**                              | Office of the Attorney General, Consumer Protection and Antitrust Division, P.O. Box 1789, Charleston, WV 25326 (1-800-368-8808)                                                                                                                 |
| **Small-claims court name**                                             | Magistrate Court, civil division, of [county]                                                                                                                                                                                                    |
| **Filing fee (in 30-day warning)**                                      | "$30 to $50 depending on the amount sought, W. Va. Code § 50-3-1"                                                                                                                                                                                |
| **Small-claims jurisdictional ceiling**                                 | "$20,000 under W. Va. Code § 50-2-1"                                                                                                                                                                                                             |
| **Statute of limitations (in 30-day warning)**                          | "W. Va. Code § 55-2-6 (ten years for a signed written contract; five years if unwritten)"                                                                                                                                                        |
| **For insurer bad-faith disputes (first-party)**                        | ***Hayseeds, Inc. v. State Farm***, 177 W. Va. 323, 352 S.E.2d 73 (1986), attorney's fees and consequential damages once the insured substantially prevails, plus a § 33-11-4(9) complaint to the Insurance Commissioner                         |
| **For third-party insurer complaints**                                  | Administrative complaint to the Insurance Commissioner only, § 33-11-4a bars a private suit                                                                                                                                                      |
| **For ground ambulance**                                                | No operative protection yet for policies issued before January 1, 2027; W. Va. Code § 33-25A-38 applies only to policies issued on or after that date                                                                                            |
| **For garnishment threats**                                             | W. Va. Code § 46A-2-130, capped at 20% of disposable earnings, requires a judgment first                                                                                                                                                         |

## Key West Virginia-specific advantages

Worth keeping in mind when triaging a West Virginia patient's bills:

1. **The WVCCPA reaches original creditors, including the hospital's own billing department**, not just third-party collectors. W. Va. Code § 46A-2-122's broad "debt collector" definition is the single biggest structural advantage in this pack, and it is unusual: most states' debt-collection statutes track the FDCPA's original-creditor exclusion. Combine with § 46A-5-101's $1,000-per-violation statutory penalty and the § 46A-5-108 cure-notice procedure for the standard 30-day warning letter.
2. **20% wage-garnishment cap**, W. Va. Code §§ 46A-2-130 and 38-5A-3, meaningfully tighter than the federal 25% CCPA ceiling. Useful for countering a garnishment threat and for framing what is actually at stake if a judgment is entered.
3. **Hayseeds first-party bad-faith doctrine** is one of the more patient-favorable bad-faith rules nationally: attorney's fees and consequential damages follow automatically once the insured substantially prevails, without a separate showing that the insurer acted in bad faith.
4. **A second, state-level enforcement channel for No Surprises Act violations.** W. Va. Code § 33-2-24 lets a patient file with the West Virginia Insurance Commissioner (fines up to $10,000/violation) in addition to the federal NSA Help Desk, doubling the regulatory pressure available for a surprise bill.
5. **No hospital lien statute located.** If this holds up (see gaps below), it is structurally patient-favorable: a West Virginia hospital cannot file a one-sided statutory lien against a personal-injury settlement the way a Georgia or Indiana hospital can. Any lien must rest on contract, subrogation, or judgment.

## West Virginia-specific gaps and unverified items

Flagged here rather than asserted in the sections above, per the kit's citation standard:

1. **Ground-ambulance scope beyond the HMO Act.** W. Va. Code § 33-25A-38 was verified directly against the official code site, but it sits within Article 25A (the Health Maintenance Organization Act). Secondary sources (legislative summaries, bill trackers) describe the underlying 2026 legislation as reaching "commercial health insurance plans" generally, but this pack could not independently verify a parallel provision in the general accident-and-sickness insurance articles (33-15/33-16). Confirm scope against a non-HMO plan before relying on this for a PPO or indemnity-plan patient.
2. **Hospital lien statute, absence not exhaustively proven.** This pack's conclusion that West Virginia has no hospital lien statute rests on (a) a direct search of the official code site for lien-plus-hospital language, which turned up only unrelated bond-financing and mechanics'/judgment-lien provisions, and (b) the fact that another pack in this kit (`laws_state_ky.md`) independently cites a 50-state hospital-lien survey listing West Virginia among the states without one. This pack could not itself retrieve that survey document (the source PDF returned an access error), so the claim rests on the code search plus that secondary citation, not on a fetched primary confirmation of a negative.
3. **Magistrate Court appeal filing fee.** This pack states the 20-day appeal deadline to circuit court with reasonable confidence, but could not independently confirm from a primary source whether a circuit-court filing fee is charged on that appeal, so no fee figure is given for the appeal step.
4. **W. Va. Code of State Rules § 110-3-24 exact interaction with billing/collection timing.** This regulation was confirmed to govern charitable-hospital property-tax exemption and to require a charity-care plan and posted notices, but this pack could not confirm any specific application-window or pre-collection waiting-period requirement tied to it (a figure like "240 days" appears in at least one secondary source describing West Virginia charity care, but that number matches the **federal** § 501(r) extraordinary-collection-action notification period exactly, and this pack could not confirm it is a distinct, additional West Virginia requirement rather than a restatement of the federal rule). It has been omitted rather than asserted as state-specific.
5. **Whether SB 645's effective date (June 11, 2026 enactment; January 1, 2027 policy-issuance trigger) has since been amended.** Verified directly against the codified section as of 2026-08-19; re-check before relying on it for a policy renewal near the transition date.
