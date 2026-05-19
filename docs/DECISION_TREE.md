# Decision tree — which template applies

A fast-reference flowchart-style document. Use this when you have a specific bill in hand and need to pick the right template quickly. The LLM follows the same logic in `llm/workflow.md`, but having a printable single-page reference is useful when the LLM is unavailable or when you want to sanity-check the model's recommendation.

## Step 1 — What kind of bill is it?

- **Bill from a healthcare provider** (hospital, doctor, lab, ambulance, durable medical equipment vendor) → **Step 2**.
- **Letter from a debt collector** that says "this is an attempt to collect a debt" → **`templates/letter_fdcpa_validation.md`** (if within 30 days of first contact).
- **Denial letter from your insurance company** (no provider bill yet, or the bill is paid pending appeal) → **Step 3** (Insurance denial).
- **Hospital lien notice** (filed against your personal-injury settlement) → **`templates/letter_auto_med_pay.md` Variant C**.
- **Insurance company demanding repayment of a paid claim** (subrogation) → consult `rules/15_auto_med_pay.md`.

## Step 2 — Is the provider bill itemized?

- **No** — the bill is a summary statement only → **`templates/letter_itemization_request.md`**.
- **Yes** — proceed to **Step 4**.

## Step 3 — Insurance denial

Identify the plan type. This is the most important question in any insurance denial appeal.

- **Employer-sponsored, self-funded ERISA** (most large-employer plans) → **`templates/letter_insurance_appeal_erisa.md`**.
- **Employer-sponsored, fully-insured** → also use `letter_insurance_appeal_erisa.md` but the state insurance department complaint at `templates/complaint_state_doi.md` is more powerful here.
- **Medicare (Part A/B/C/D)** → **`templates/letter_medicare_appeal.md`** and `rules/12_medicare_appeals.md`.
- **Medicaid / state managed care (e.g., TennCare)** → **`templates/letter_medicaid_appeal.md`**.
- **TRICARE** → consult `rules/18_tricare.md` and contact a Beneficiary Counseling and Assistance Coordinator (BCAC).
- **VA Community Care** → consult `rules/19_va_community_care.md` and contact a VA Patient Advocate or Veterans Service Organization.
- **Dental insurance** → **`templates/letter_dental_dispute.md`**.
- **Individual market ACA plan** → use `letter_insurance_appeal_erisa.md` but adapt the legal citations (no ERISA, use ACA appeal rules in 45 CFR § 147.136).

## Step 4 — What's wrong with the bill?

Most bills have more than one issue. Pick the most leveraged dispute first:

### 4a — Did emergency care happen?

- **Service was emergency, provider was out-of-network or facility was out-of-network** → **`templates/letter_no_surprises_violation.md`** (federal No Surprises Act).
- **You were denied emergency screening or stabilization or were inappropriately transferred** → **`templates/complaint_emtala.md`** (federal EMTALA).

### 4b — Was the patient at an in-network facility but the bill is from an out-of-network ancillary?

(Anesthesiology, radiology, pathology, lab, hospitalist, intensivist, neonatology, assistant surgeon)

- **Yes** → **`templates/letter_no_surprises_violation.md`** (federal No Surprises Act).

### 4c — Is the bill for a ground ambulance?

- **Yes, and the patient's state is on the protected list** (CA, CO, DE, GA, IL, ME, MD, NY, OH, VT, WA) **and** the plan is not ERISA self-funded → **`templates/letter_ground_ambulance.md` Variant A**.
- **Yes, but the state is not on the list or the plan is ERISA self-funded** → **`templates/letter_ground_ambulance.md` Variant B**.

### 4d — Is the bill from an accident (motor vehicle, slip-and-fall, etc.)?

- **Yes** → consult `rules/15_auto_med_pay.md`. Force the correct payer order. Variant A demands med-pay/PIP. Variant B forces hospital to bill health insurance. Variant C challenges a hospital lien.

### 4e — Is the bill from a work-related injury?

- **Yes, workers' comp claim accepted, but bill came to you directly** → consult `rules/16_workers_comp.md`. Redirect to WC carrier; balance billing is prohibited.
- **Yes, but workers' comp claim is contested or denied** → file the WC appeal in state's WC system, run health insurance as the interim payer.

### 4f — Is the bill from a telehealth visit?

- **Yes, and there's a coding or coverage issue** → consult `rules/20_telehealth.md`. Most issues are POS code or modifier errors, or state telehealth-parity violations.

### 4g — Is the ER visit CPT severity-coded too high?

(99284 or 99285 for a short, low-complexity visit; 99214 or 99215 for a brief office visit)

- **Yes** → **`templates/letter_initial_dispute.md`** with CPT upcoding block. Cite the AMA 2023 E/M documentation requirements from `references/cpt_codes_em.md`.

### 4h — Is the bill price-gouging?

(Charge is significantly above Medicare allowable, hospital's posted cash price, or fair-market range from Turquoise Health / FAIR Health Consumer)

- **Yes** → **`templates/letter_initial_dispute.md`** with price-gouging block. Cite UCC § 2-305(2) (open price term, good faith).

### 4i — Is the bill for a service you didn't receive?

- **Yes** → **`templates/letter_initial_dispute.md`** with services-not-received block.

### 4j — Are there duplicate line items?

- **Yes** → **`templates/letter_initial_dispute.md`** with duplicate-charge block.

### 4k — Is the bill correctly coded but you cannot afford it?

For **non-profit hospital bills** (most US hospitals):

- → **`templates/letter_financial_assistance_application.md`** (IRS § 501(r) FAP application).
- Plus: screen at [Dollar For](https://dollarfor.org) for free help.

For **for-profit hospitals** or any other provider:

- → **`templates/letter_hardship_negotiation.md`** (hardship reduction anchored to Medicare allowable).

### 4l — Self-pay/uninsured patient + final bill more than $400 over Good Faith Estimate?

- → consult `rules/11_ppdr_walkthrough.md` and file Patient-Provider Dispute Resolution at the federal IDR portal.

### 4m — Hospital has not posted a compliant Hospital Price Transparency machine-readable file?

- → **`templates/complaint_cms_hpt.md`** (CMS complaint, parallel to your underlying dispute).

### 4n — Provider won't release your medical or billing records?

- → **`templates/complaint_hipaa_access.md`** (HHS Office for Civil Rights complaint).

## Step 5 — After 30 days of no substantive response

If you sent an initial dispute letter (4g-4j above) and the provider has not responded substantively within 15-30 days:

- → **`templates/letter_30day_warning.md`** (CC state insurance department, state AG, BBB).

## Step 6 — After the 30-day warning expires

If the 30-day warning has been ignored:

- → **`templates/complaint_state_doi.md`** (file state complaint).
- → File in small claims court if the disputed amount is within your state's jurisdictional limit. See `rules/06_small_claims.md` and `examples/small_claims_walkthrough.md`.

## Step 7 — If the debt has been overwhelming

If medical debt has put you in a position where no realistic repayment is possible:

- → consult `rules/17_bankruptcy_and_medical_debt.md`. Bankruptcy may be the right tool. Try the dispute, charity-care, and hardship paths first; bankruptcy is the last move, not the first.

## Edge cases that don't fit the tree

- **Multiple bills from one hospital encounter** (hospital + ER physician group + radiologist + anesthesiologist) — apply the tree to each separately. They often have different issues.
- **An old bill that's been ignored for months** — your state's statute of limitations matters. See your state pack.
- **A bill while you're already in dispute** — log it in the tracker and treat as continuation, not a new fight.
- **A bill from a non-US provider** — out of scope for this kit.
- **A veterinary bill** — out of scope.

## When the LLM disagrees

If you walk through this tree and arrive at a different template than the LLM recommends, ask the LLM to explain its reasoning. Either the LLM is missing something specific to your case, or the tree is missing a nuance. Both are useful feedback; the latter goes in a GitHub issue.

## Print this

This document is intentionally short. Print it. Keep a copy in the folder where you store your bills. The LLM is the day-to-day tool; this is the index.
