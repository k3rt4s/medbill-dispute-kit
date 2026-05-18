# Template — Hospital financial assistance application request

For non-profit hospital bills, this letter triggers the hospital's obligation under IRS § 501(r) to consider you for financial assistance (charity care). Most hospitals have their own application form; submit the form if provided. This letter is for when the hospital is slow to provide one, refuses to acknowledge the patient's eligibility for screening, or proceeds with collection action before completing the eligibility determination.

For non-profit hospitals only. Determine non-profit status by searching the hospital's IRS Form 990 (publicly available at [propublica.org/nonprofits](https://projects.propublica.org/nonprofits/)) or asking. For-profit hospitals are not subject to § 501(r); use `letter_hardship_negotiation.md` instead. Municipal/county hospitals are usually treated as governmental and have their own (often more generous) charity-care frameworks.

[Dollar For](https://dollarfor.org) is a free non-profit that handles this whole process. Strongly recommend the patient run their screener before mailing this letter. Dollar For will file the actual FAP application on the patient's behalf, push the hospital to apply presumptive eligibility, and fight denials. This letter is a parallel paper trail, not a substitute for Dollar For.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

[FINANCIAL ASSISTANCE COORDINATOR or BILLING DEPARTMENT MANAGER]
[HOSPITAL NAME]
[HOSPITAL MAILING ADDRESS]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: Request for Financial Assistance Policy and application —
    Account #[ACCOUNT NUMBER]
    Patient: [PATIENT FULL NAME]
    Date(s) of service: [DATE OF SERVICE]
    Current balance: $[CURRENT BALANCE]

Dear Financial Assistance Coordinator:

I am writing to formally request consideration for financial assistance under your hospital's Financial Assistance Policy ("FAP"), as required by 26 U.S.C. § 501(r) and 26 CFR § 1.501(r).

I. Documents requested

Please provide me, free of charge, the following:

1. Your hospital's complete current **Financial Assistance Policy**.
2. Your hospital's **Plain Language Summary** of the Financial Assistance Policy.
3. Your hospital's **FAP application form**, and instructions for completing it.
4. Your hospital's **Billing and Collections Policy**, including the list of all extraordinary collection actions you may take and the specific timeframes within which you must complete the eligibility determination before initiating any such action.
5. A clear statement of the **amounts generally billed** (AGB) to insured patients for the services on my account, calculated per 26 CFR § 1.501(r)-5, against which my FAP-eligible amount must be capped if I am determined eligible.

II. Statement of financial circumstances

I believe I am eligible for assistance under your FAP based on the following:

[The LLM renders one or more of the blocks below. Do not embellish; understate where possible.]

[BLOCK A — Household income relative to federal poverty level]

My household consists of [N] persons. My household's gross annual income is approximately $[INCOME]. The federal poverty level for a household of [N] for the most recent year is approximately $[FPL]. My household income is approximately [N]% of the federal poverty level. Most non-profit hospital FAPs provide a discount or full coverage at incomes up to [200% / 300% / 400%] of the FPL depending on the institution.

[BLOCK B — Medical-debt burden relative to income]

Inclusive of the above-referenced account, I currently have $[TOTAL MEDICAL DEBT] in medical-debt liability across [N] providers from related care. This amount exceeds [X]% of my gross annual income.

[BLOCK C — Presumptive eligibility indicators]

I am [enrolled in / eligible for] [Medicaid / TennCare / SNAP / WIC / state heating-assistance program / housing assistance / other means-tested public-assistance program]. Many non-profit hospital FAPs treat enrollment in such programs as presumptive eligibility for financial assistance.

[BLOCK D — Other circumstances]

[Briefly state any additional facts that bear on eligibility — job loss, disability, dependents, sole caregiver responsibilities, recent bankruptcy. Two or three sentences; the goal is candor, not pity.]

[END BLOCKS]

III. Procedural protections during the application process

Pursuant to 26 CFR § 1.501(r)-6, while my eligibility application is pending, your hospital must not engage in any "extraordinary collection action" against me — including but not limited to: lawsuits, wage garnishment, credit reporting, denying necessary future medical care because of unpaid bills, or referring this account to an outside collection agency.

If you have already begun any such action, please immediately suspend that action and notify any third-party agent (including any debt collector and any consumer reporting agency) of the suspension.

IV. Application I am submitting

[OPTIONAL — render only if the patient is including a completed application]

I am enclosing my completed Financial Assistance Application along with [list of supporting documents: most recent pay stubs, prior year tax return, household-size documentation, public-assistance enrollment letter, bank statements].

[OR — alternative phrasing if no application is being submitted yet]

Please send me your hospital's FAP application form and I will return it completed within thirty (30) days of receipt, along with supporting documentation.

V. Determination timeline

Please complete the eligibility determination and notify me in writing of the outcome within the timeframes specified in your Billing and Collections Policy. If I am determined eligible, please apply the FAP-discounted amount (capped at amounts generally billed per § 501(r)-5) to my account and provide a corrected statement.

VI. Notice of preservation of rights

I am preserving all rights, including the right to file complaints with:

- The Internal Revenue Service (your hospital's § 501(r) compliance is subject to IRS audit);
- The [STATE] Attorney General's Office, Consumer Protection Division;
- The Centers for Medicare and Medicaid Services, where applicable.

I would prefer to resolve this collaboratively. Please contact me at [PATIENT PHONE] or [PATIENT EMAIL] with questions or requests for additional information.

Sincerely,



[PATIENT FULL NAME]

Account number: [ACCOUNT NUMBER]
Date of service: [DATE OF SERVICE]

Enclosures: copy of bill; [if applicable: completed FAP application and supporting documents]
```

---

## Placeholders and rendering notes

- Most non-profit hospitals publish their FAP and AGB calculation on their website. The LLM should attempt to find both before drafting and reference them by name in the letter ("In your published Financial Assistance Policy dated [DATE], you state that..."). This signals the patient has done the homework.
- Many FAPs set sliding-scale discounts. The patient may be eligible for a partial discount even if not full charity care. The application should be submitted even if the patient is over the income threshold for full free care.
- AGB (Amounts Generally Billed) is the cap: a FAP-eligible patient cannot be charged more than what insured patients are generally charged for the same services. Most hospitals calculate AGB by the "look-back method" — average of insurance-paid amounts over the prior 12 months as a percentage of gross charges. The patient is entitled to know this number.

## Parallel actions

1. **Run the Dollar For screener** at [dollarfor.org](https://dollarfor.org). They handle the application end-to-end and have negotiated relationships with many hospital systems.
2. **Check the hospital's website** for the FAP, application form, Plain Language Summary, and Billing & Collections Policy. Download all four.
3. **Gather documentation** before mailing: most recent pay stubs (2-3 months), prior year tax return, household-size proof (lease, dependents' info), any public-assistance enrollment letter.
4. **If already in collections**: § 501(r)-6 requires the hospital to suspend extraordinary collection action while the application is pending. The letter above triggers that suspension; follow up with any third-party collector directly using `letter_fdcpa_validation.md`.

## When this is not the right template

- **For-profit hospital:** § 501(r) does not apply. Use `letter_hardship_negotiation.md` instead.
- **Municipal/county hospital:** typically has its own charity-care program more generous than federal § 501(r). Ask for that program by name; if the LLM is uncertain, route to `letter_hardship_negotiation.md` as a fallback.
- **Bill that contains errors or upcoding:** dispute the errors first using `letter_initial_dispute.md`. The FAP discount applies to the *corrected* bill, not the original.

## Follow-up

The LLM logs this with `action_type = "fap_application_submitted"`. Set `response_due_by` to 30 days from today (typical FAP processing window varies by institution; 30 days is a reasonable patient-side deadline before escalation).

If the hospital does not respond within 30 days, escalate by (a) submitting an IRS Form 13909 (Tax-Exempt Organization Complaint) for § 501(r) non-compliance, and (b) filing a state attorney general consumer protection complaint. The hospital's tax-exempt status is at stake, which makes § 501(r) compliance a higher-stakes regulatory issue than most billing disputes.
