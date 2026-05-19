# Rule 18 — TRICARE billing

TRICARE is the health-care program for active-duty service members, retirees, National Guard and Reserve members, and their families. It has its own statute, its own rate schedule, its own provider network rules, and its own appeal process — none of which look like commercial or Medicare appeals.

This rule fires whenever the patient is a TRICARE beneficiary with a medical bill. It does not displace the kit's other rules; it adds TRICARE-specific overlays.

## The basics

- **Authority:** 10 U.S.C. § 1071-1110b; implementing regulations at 32 CFR Part 199.
- **Administrator:** Defense Health Agency (DHA) within the Department of Defense.
- **Regional contractors (2026):** Humana Military (East Region), TriWest Healthcare Alliance (West Region). Contractor changed from Health Net to TriWest effective 2024.
- **Patient-facing website:** [tricare.mil](https://www.tricare.mil)

## What's protected

### TRICARE-authorized providers

A TRICARE-authorized provider has agreed to:

- Accept the TRICARE maximum allowable charge (TMAC) as payment in full, plus the patient's cost-share.
- **Not balance-bill** the patient for amounts above TMAC for covered services.

Providers fall into three categories:

1. **Network providers** — under contract with the TRICARE regional contractor. Cannot balance-bill. Cost-share is lowest.
2. **TRICARE-authorized non-network providers** — authorized to treat TRICARE patients and agree to TRICARE rules (including the 15% balance-billing cap; see below). Cost-share is higher.
3. **Non-authorized providers** — not authorized to provide services to TRICARE patients. Treatment by them is typically not covered.

### The 15% balance-billing cap

Federal law (10 U.S.C. § 1079(h)) caps the amount a TRICARE-authorized non-network provider may charge above the TMAC. For most services, the cap is **115% of the allowable charge**. A provider charging more is in violation of federal law.

### Active-duty service members

Active-duty service members under TRICARE Prime have **zero out-of-pocket cost** for authorized care. Any bill an active-duty member receives is a billing error, almost without exception. Refer immediately to the regional contractor.

## When this rule fires

- A TRICARE beneficiary receives a bill that includes balance-billed amounts above the TMAC.
- A TRICARE beneficiary's claim was denied or partially denied and the patient wants to appeal.
- An active-duty service member receives any bill for authorized care.
- A TRICARE claim was processed as out-of-network when the patient believes the provider should have been treated as network.

## The patient's playbook

### 1. Confirm provider's TRICARE status

Use the regional contractor's provider lookup at [humanamilitary.com](https://www.humanamilitary.com) (East) or [tricare.mil/west](https://www.tricare.mil/west) (West). A provider may be authorized for TRICARE Standard/Select but not Prime, or vice versa.

### 2. Pull the TRICARE Explanation of Benefits

Patients log in at [tricare.mil](https://www.tricare.mil) or the regional contractor's portal. The TRICARE EOB shows:

- The amount billed by the provider
- The TRICARE allowable charge
- The amount TRICARE paid
- The patient's cost-share
- Any deductible applied

Any provider-billed amount exceeding the TRICARE allowable charge plus patient cost-share is suspect.

### 3. For a balance-billing violation

Send the provider a letter citing the 15% cap (10 U.S.C. § 1079(h) and 32 CFR § 199.7(h)) and demand the bill be corrected. Use `templates/letter_initial_dispute.md` adapted with TRICARE citations.

Parallel: contact the regional contractor to report the billing violation. Contractors investigate and can revoke a provider's TRICARE authorization for repeated balance-billing.

### 4. For a denial appeal

TRICARE has its own appeal process under 32 CFR § 199.10:

- **Reconsideration** by the regional contractor — 90-day filing window from the date of the initial determination.
- **Formal review** by the DHA — for non-medical-necessity appeals.
- **Hearing** — for cases above $300 in dispute on appealable issues.
- **Final decision** by the Director, DHA.
- **Federal court** — possible for some final decisions under the Administrative Procedure Act.

### 5. Beneficiary Counseling and Assistance Coordinator (BCAC)

Every TRICARE region has a BCAC who provides free help to beneficiaries with claims, billing, and appeals. Find the BCAC at the patient's military treatment facility or via the regional contractor's website.

### 6. Military Health System Patient Advocate

The patient advocate at the patient's military treatment facility can help with billing disputes and appeals. Free and confidential.

## What does not apply

- **No Surprises Act**: TRICARE is federally administered; the NSA's balance-billing prohibitions overlap with TRICARE's existing prohibitions. Cite both for emphasis but TRICARE's 15% cap is the primary federal floor.
- **State surprise-billing laws**: state insurance laws generally do not apply to TRICARE. ERISA-style preemption doesn't apply (TRICARE is not an ERISA plan), but federal supremacy does.
- **State bad-faith statutes**: do not apply to TRICARE.

## When the kit's other rules still apply

- **Hospital itemization right** under state law: state hospital-itemization statutes generally do apply to TRICARE patients seen at state-licensed hospitals.
- **HIPAA right of access**: applies. See `rules/14_hipaa_right_of_access.md`.
- **EMTALA**: applies. See `rules/13_emtala.md`.
- **State UDAP statutes**: may apply to a non-TRICARE-related billing pattern by a TRICARE-authorized provider.

## Tracker tagging

- `findings`: `tricare_balance_billing_violation`, `tricare_active_duty_bill_error`, `tricare_denial`
- `next_action`: `report_to_regional_contractor`, `request_bcac_help`, `file_tricare_appeal`

## When to escalate to congressional inquiry

A TRICARE billing or claims problem that does not resolve through the regional contractor, BCAC, and DHA can often be escalated via a constituent-services request to the patient's US Representative or Senator. Congressional offices have dedicated DoD liaisons who can move stuck cases.

## Related

- `templates/letter_initial_dispute.md` — adapt with TRICARE citations
- [[19_va_community_care]] — Veterans Affairs Mission Act / Community Care (a separate federal program, often confused with TRICARE)
- `references/laws_federal.md` — TRICARE statutory authority overview
