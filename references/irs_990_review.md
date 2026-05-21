# Reading a non-profit hospital's IRS Form 990

Approximately 2,900 of the 5,200 acute-care hospitals in the United States are organized as 501(c)(3) tax-exempt entities. Each one must file IRS Form 990 annually and, since 2009, must include Schedule H — Hospitals as part of the filing. Schedule H discloses charity-care spending, community-benefit activity, billing-and-collection policy, debt-collection practices, and compensation of top executives.

Marshall Allen and other patient-advocacy writers (Pat Palmer, Sarah Kliff, Jay Hancock) repeatedly cite Schedule H as a pressure tool: a hospital that bills patients $200,000 for a $20,000 service while claiming $50M in community benefit on its 990 has an obvious credibility problem when challenged.

This reference explains what to pull from a 990 and how to use it.

---

## Where to find the 990

- **ProPublica Nonprofit Explorer** at projectsroprublica.org/nonprofits — free, searchable, includes 990s back to 2001 for most hospitals. The fastest single source.
- **GuideStar (Candid)** at candid.org — free with registration; same underlying IRS data.
- **IRS Tax Exempt Organization Search** at apps.irs.gov/app/eos — the original source; works but less convenient than ProPublica.
- The hospital's own website — § 501(r)(4)(B) requires posting the FAP, FAP application, and plain-language summary, but not the full 990. Some hospitals link the 990 anyway.

Filings have an 18- to 24-month lag. A 990 filed in November 2025 typically covers fiscal year 2024.

---

## Key fields to extract (in order of dispute utility)

### Schedule H, Part I — Financial Assistance and Certain Other Community Benefits

- **Part I, Line 7a — Financial Assistance at Cost**: dollars the hospital reports spending on patients eligible for charity care under its FAP. Most defensible Schedule H number for patient-advocacy purposes.

- **Part I, Line 7e — Net Community Benefit Expense**: total community-benefit number the hospital points to in PR. Includes Medicaid shortfalls (a subsidy the hospital chose to accept) and education/research spending unrelated to charity care. Use cautiously.

- **Part I, Line 7g — Bad Debt**: amount of patient debt the hospital wrote off as uncollectible. Distinct from charity care: bad debt is debt the hospital tried to collect and failed. A hospital with high bad debt and low charity-care spending may be screening too narrowly for FAP eligibility.

### Schedule H, Part V — Facility Information

- **Section A — Hospital Facilities**: list of every facility under the EIN. A multi-hospital system may report consolidated 990 data; the patient should pull the system-level filing.
- **Section B — Facility Policies and Practices**: per-facility yes/no responses to questions including:
  - Has the facility conducted a Community Health Needs Assessment (CHNA) in the last three years?
  - Does the facility have a written FAP?
  - Does the FAP specify income eligibility criteria, the basis for calculating AGB (Amounts Generally Billed), and the methods for applying?
  - Does the facility have an Emergency Medical Care Policy?
  - Does the facility have a written debt-collection policy?
  - Does the facility delay or deny medically necessary care to individuals with outstanding bills (a violation of § 501(r) if "Yes")?

A "No" answer to any of the CHNA / FAP / EMC policy questions is direct evidence of § 501(r) non-compliance and a strong attachment to an IRS Form 13909 complaint.

### Schedule H, Part VI — Supplemental Information

Free-text narrative on:

- Community building activities (housing, education, environmental improvements).
- Affiliated organizations and how community benefit is allocated.
- The hospital's method for determining whether an account is eligible for FAP before extraordinary collection action.

The narrative is where hospitals describe their "reasonable efforts" to determine eligibility before suing patients. If the narrative says the hospital uses a vendor or screens every patient for FAP, and the patient was sued without being screened, the narrative is exhibit A in the dispute.

### Form 990, Part VII — Compensation of Officers, Directors, Trustees, Key Employees

The CEO and top-5 highest-compensated employees are listed with total compensation. Hospital CEO compensation in the multi-million-dollar range while bad-debt and charity-care numbers are anemic is a routine pressure point.

### Form 990, Schedule J — Compensation Information

For each highly compensated executive, Schedule J shows base salary, bonus, retirement, deferred compensation, and non-taxable benefits. Total compensation packages can run 3-5x the headline salary.

### Form 990, Part III — Statement of Program Service Accomplishments

Top three program services with revenue, expense, and grant numbers. Use to verify the hospital's claimed program scope matches what the patient observed.

---

## How to use the 990 in a dispute

### 1. As a citation in the hardship-negotiation or initial-dispute letter

When the bill is from a non-profit hospital and the patient is FAP-eligible, the dispute letter can cite Schedule H specifics:

> Your facility reported $[CHARITY CARE NUMBER] in financial assistance at cost on Schedule H, Part I, Line 7a of your most recent IRS Form 990 (filed [DATE], covering fiscal year [YEAR]). Your published FAP indicates eligibility for patients at [N]% of the federal poverty level. Based on my household income of $[INCOME] and household size of [N], I am at [N]% of FPL and within your published eligibility tier. Please process my account through your FAP rather than continue collection activity.

### 2. As supporting evidence in a state DOI / AG complaint

Schedule H Part V Section B answers are sworn declarations to the IRS. A patient who can show the hospital answered "Yes" to having a written debt-collection policy and "No" to delaying care for outstanding bills, but then experienced exactly that pattern, has a state-level consumer-protection claim.

### 3. As the substantive basis of an IRS Form 13909 complaint

If the hospital's conduct is inconsistent with the 990 answers — for example, the hospital reports having a FAP but the patient was sued without being screened — file IRS Form 13909 (Tax-Exempt Organization Complaint Referral). The IRS does not typically revoke 501(c)(3) status over a single complaint, but it does add the complaint to the file used for the next IRS audit cycle and can lead to follow-up correspondence with the hospital.

Mailing address:
IRS EO Examinations Classification Office
1100 Commerce Street, MC 4910 DAL
Dallas, TX 75242
Or fax to 214-413-5415.

### 4. As leverage in CFO escalation

CFOs respond to Form 990 references in a way they do not respond to general billing complaints. A letter that quotes the CFO's own filing back to them carries weight that the same letter would not have if it cited generic federal law alone. See `references/phone_call_scripts.md` Script 5 (CFO escalation).

---

## What the 990 will not tell you

- The 990 does not show the patient-by-patient screening record. A hospital may report "Yes, we screen for FAP" on Schedule H Part V Section B and have screened only 10% of eligible patients. The 990 reports the policy; only the patient's own experience tells the story of the practice.

- The 990's charity-care number is reported at COST (the hospital's accounting cost), not at chargemaster billed amount. A hospital that bills $200,000 and writes off the full $200,000 to charity care reports only the cost of providing that care (say, $40,000) on Schedule H Line 7a. The patient should not assume the reported number reflects what the patient was billed.

- The 990 is current as of the fiscal year filed. Hospital billing policy can change between filings. Verify the FAP on the hospital's website is the current one before relying on it.

---

## Auditing tools the kit does not ship

A power user can extract every hospital's Schedule H Part I and Part V data into a spreadsheet and compute charity-care-as-percentage-of-net-revenue trends across years. The dataset is open; the IRS publishes 990 e-filings as XML at irs.gov/charities-non-profits/form-990-series-downloads. The kit does not bundle a 990 parser because the value-per-effort ratio is much lower than the templates and audits that do ship. If a contributor builds one, a pull request adding a `scripts/parse_990.py` would be welcome.

---

## Related templates and references

- `templates/letter_financial_assistance_application.md` — § 501(r) FAP application.
- `templates/letter_hardship_negotiation.md` — references FAP and § 501(r) duties.
- `templates/complaint_state_doi.md` — Category B / E / F for consumer-protection violations the 990 may help establish.
- `references/medical_debt_protection_by_state.md` — state-level charity-care screening mandates.
