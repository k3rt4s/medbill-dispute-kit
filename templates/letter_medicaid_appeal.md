# Template — Medicaid / state-managed-care appeal

Medicaid appeals are state-administered. Every state runs its own program with its own appeal rules — though the federal floor at 42 CFR Part 431 Subpart E and 42 CFR § 438.402-424 (managed care) imposes minimum standards everywhere. The kit covers Tennessee's TennCare as the worked example; for other states, adapt the citations using the state-specific Medicaid agency's appeal rules.

This template applies to:

- **Fee-for-service Medicaid** — denials by the state Medicaid agency.
- **Medicaid managed care** — denials by an MCO ("plan") contracted with the state Medicaid agency. The federal rules at 42 CFR Part 438 require a two-step process: internal appeal to the MCO first, then state fair hearing.
- **CHIP** (Children's Health Insurance Program) — similar two-step structure.

Does **not** apply to: Medicare (use `templates/letter_medicare_appeal.md`), commercial / ERISA / individual-market plans (use `templates/letter_insurance_appeal_erisa.md`).

## Two-step structure for Medicaid managed care

Federal regulations (42 CFR § 438.402) require enrollees to first exhaust the MCO's internal appeal before requesting a state fair hearing. The LLM must determine which step the patient is at:

1. **Step 1 — MCO internal appeal.** Filed within **60 days** of the MCO's notice of adverse benefit determination. MCO must decide within 30 days (standard) or 72 hours (expedited).
2. **Step 2 — State fair hearing.** Filed within **120 days** of the MCO's appeal decision (some states shorter — verify). Heard by a state administrative law judge.

For fee-for-service Medicaid, step 1 is the state fair hearing directly.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

[Pick one based on the step:
 Step 1: [MCO NAME] Member Appeals Department
         [MCO MAILING ADDRESS]
 Step 2: [STATE MEDICAID AGENCY] Office of Administrative Hearings
         [STATE OAH MAILING ADDRESS]]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: [Step 1: Request for internal appeal of adverse benefit determination
     Step 2: Request for state fair hearing]
    Member: [PATIENT FULL NAME]
    Medicaid ID: [MEDICAID ID]
    [Step 1: MCO name: [MCO NAME]; Member ID: [MEMBER ID]]
    Service / benefit at issue: [SERVICE OR BENEFIT]
    Date(s) of service or denial: [DATE(S)]
    Notice of denial dated: [DATE OF NOTICE]

Dear [Appeals Department / Office of Administrative Hearings]:

I am requesting [an internal appeal / a state fair hearing] of the denial dated [DATE OF NOTICE] concerning [SERVICE OR BENEFIT]. The denial is in error and should be reversed for the reasons set forth below.

I. Service or benefit at issue

[Describe the service or benefit, date, provider, and clinical context. Example:
On [DATE], my doctor ordered [SERVICE]. Your notice dated [DATE] denied coverage with the stated reason: "[REASON]." I respectfully disagree for the following reasons.]

II. Why the denial is in error

[The LLM renders one or more of these blocks based on the actual denial reason.]

[BLOCK A — Medical necessity]

The service is medically necessary for my condition. My treating provider, [PROVIDER NAME, NPI, CREDENTIALS], has determined that this service is required to [treat the condition / prevent serious deterioration / restore function]. Their written statement of medical necessity is attached as Exhibit A.

[BLOCK B — EPSDT (Early and Periodic Screening, Diagnostic, and Treatment) for under-21 enrollees]

The denied service is required as Early and Periodic Screening, Diagnostic, and Treatment under 42 U.S.C. § 1396d(r) and 42 CFR § 441.50 et seq. EPSDT entitles Medicaid enrollees under age 21 to all medically necessary health care, diagnostic services, treatment, and other measures described in 42 U.S.C. § 1396d(a) needed to correct or ameliorate a defect, physical and mental illness, or condition, **regardless of whether the service is otherwise covered under the state plan.** The Supreme Court confirmed this comprehensive scope in [Frew v. Hawkins / O'Bannon v. Town Court Nursing Center / other governing case in the patient's jurisdiction]. The denied service falls within EPSDT and must be approved.

[BLOCK C — Coverage policy misapplied]

The denial relies on a coverage policy or criterion that does not apply to my situation, or that has been incorrectly interpreted. Specifically: [explain — cite the state Medicaid manual provision or the MCO's coverage policy and how the patient's case differs from the denial rationale].

[BLOCK D — Continuation of services pending appeal (Aid Paid Pending)]

I am also requesting continuation of services during the pendency of this appeal under 42 CFR § 438.420 (managed care) or 42 CFR § 431.230 (fee-for-service). I have requested this appeal within 10 days of the notice and the previously authorized service has not yet ended. I understand that if my appeal is denied, I may be liable for the cost of services received during the appeal.

[BLOCK E — Wrong patient or incorrect data]

The denial appears to rest on incorrect demographic or clinical information about me. Specifically: [explain]. I am attaching corrected information as Exhibit [X].

[END BLOCKS]

III. Documentation requested

Pursuant to 42 CFR § 438.406(b)(5) (managed care) or 42 CFR § 431.242 (fee-for-service), please provide me, free of charge, all documents, records, and other information relevant to the denial, including:

1. The complete case file and clinical record reviewed in making the denial.
2. Any clinical guideline, medical necessity criterion, or coverage policy used to evaluate the request.
3. The qualifications of the reviewer who made the denial.
4. The state Medicaid coverage policy or MCO contract provision relied on.

IV. Procedural requests

1. Please confirm in writing receipt of this appeal request and the assigned case number.
2. Please decide this appeal within the timeframes required by 42 CFR § 438.408 (managed care) — generally **30 days standard, 72 hours expedited** — or by state law for fee-for-service.
3. If the denial is upheld in whole or in part, please simultaneously provide the specific reasons in writing, identify the policies or evidence relied on, and inform me of my right to advance to a state fair hearing (Step 1) or to seek judicial review (Step 2), with the applicable deadlines.

V. Expedited review (render only if applicable)

I request **expedited** review pursuant to 42 CFR § 438.410 (managed care). Waiting for a standard decision could seriously jeopardize my life, health, or ability to attain, maintain, or regain maximum function. Specifically: [state the clinical urgency]. My treating provider's supporting statement is attached as Exhibit B.

VI. Representative

[Render only if applicable.]

I have authorized [REPRESENTATIVE NAME] to represent me in this appeal. Please copy [REPRESENTATIVE NAME] on all correspondence at [REPRESENTATIVE ADDRESS / PHONE / EMAIL].

VII. Documentation enclosed

- Exhibit A: Treating provider's written statement of medical necessity dated [DATE]
- Exhibit B: [As applicable: clinical records, prior-treatment history, expedited-review supporting statement]
- Exhibit C: Copy of the denial notice dated [DATE]
- [Other exhibits as needed]

Sincerely,



[PATIENT FULL NAME]

Medicaid ID: [MEDICAID ID]
[For managed care: Plan name and Member ID]
Date of service: [DATE OF SERVICE]
Date of denial: [DATE OF DENIAL NOTICE]

cc:
    [STATE MEDICAID OMBUDSMAN, if any]
    [Treating provider]
    [Patient's representative if any]
    [Legal aid or Medicaid-advocacy organization if engaged]

Enclosures: as listed in Section VII
```

---

## Tennessee worked example — TennCare

Tennessee's Medicaid program is **TennCare**, a fully-capitated managed-care system. Three MCOs currently serve TennCare members statewide:

- **Amerigroup Tennessee** (a Wellpoint subsidiary)
- **BlueCare Tennessee** (BlueCross BlueShield of Tennessee Medicaid line)
- **UnitedHealthcare Community Plan of Tennessee**

For a TennCare appeal:

### Step 1 — MCO internal appeal

- File with the MCO's member appeals department, named on the denial notice.
- **60 days** from the denial notice.
- MCO decides within 30 days standard, 72 hours expedited.

### Step 2 — TennCare Solutions / state fair hearing

After the MCO's internal appeal decision:

- **TennCare Solutions** (TennCare's appeal-handling office) accepts the fair-hearing request.
- **Phone:** **1-800-878-3192** (TTY: 1-877-779-3103)
- **Online:** [tn.gov/tenncare/members-applicants/appeals.html](https://www.tn.gov/tenncare/members-applicants/appeals.html)
- **Mail:** TennCare Solutions, P.O. Box 593, Nashville, TN 37202-0593
- **Fax:** 1-888-345-5575
- Filing deadline varies by service category; typically **40-60 days** from the MCO decision. Verify on the denial notice.

### Tennessee-specific advocacy resources

- **Tennessee Justice Center** ([tnjustice.org](https://www.tnjustice.org)) — non-profit law firm that helps TennCare enrollees with appeals at no cost.
- **Legal Aid Society of Middle Tennessee** ([las.org](https://www.las.org)) — covers Nashville and the middle TN region.

---

## State-specific adaptation

For Medicaid programs other than TennCare, the LLM substitutes the state's program name and appeal-handling office. Common patterns to look up before drafting:

- **State Medicaid agency name** (e.g. Medi-Cal in California, Medicaid in most states).
- **State Medicaid managed-care contract list** — which MCO is the patient enrolled in?
- **State fair hearing office** — usually the state's Office of Administrative Hearings or equivalent.
- **State Medicaid ombudsman** — many states have one; useful CC line.
- **State legal-aid or Medicaid-advocacy non-profit** — every state has at least one.

Find the state's appeal page by searching "[State name] Medicaid appeal" and following the official state government link (.gov domain only).

## Placeholders and rendering notes

- The LLM must determine: is this fee-for-service Medicaid or managed care? Which MCO? Which step (internal appeal or fair hearing)?
- Most managed care denials are issued by the MCO, not the state. The patient must complete the MCO internal appeal before requesting a state fair hearing.
- Aid Paid Pending (Block D) is a critical protection but creates patient liability if the appeal is lost. The LLM must explain this trade-off to the patient before rendering Block D.

## Free help

- **Tennessee Justice Center** (for TN): [tnjustice.org](https://www.tnjustice.org)
- **National Health Law Program** ([healthlaw.org](https://www.healthlaw.org)) — publishes Medicaid-appeal guides and runs a legal-services referral network.
- **State legal-aid directory** — search "[state] legal aid Medicaid."

## Follow-up

The LLM logs Step 1 with `action_type = "medicaid_mco_appeal_filed"` and Step 2 with `action_type = "medicaid_fair_hearing_filed"`. Set `response_due_by` to 30 days for standard MCO appeals, 72 hours for expedited, and per the state's published fair-hearing timeline for Step 2.

## Related

- [[letter_insurance_appeal_erisa.md]] — commercial / employer plans (different framework)
- [[letter_medicare_appeal.md]] — Medicare (different framework)
- [[../rules/07_appeal_insurance_denial]] — general insurance-denial-appeal patterns
