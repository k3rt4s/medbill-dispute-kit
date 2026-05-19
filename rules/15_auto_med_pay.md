# Rule 15 — Auto med-pay and accident-related medical bills

When a patient is treated for injuries from a motor-vehicle accident, the billing path is different from ordinary medical billing. Multiple potential payers exist, the order matters, and the patient is exposed to surprise bills if any of them are skipped or mishandled.

This rule fires whenever a medical bill stems from an accident — vehicle, on-the-job injury caused by a third party, slip-and-fall on someone else's property — where another party's insurance may be primary.

## The payers, in typical priority order

For motor-vehicle accidents:

1. **The at-fault driver's bodily injury liability insurance** — typically the largest pot of money but only pays at settlement, often months after treatment.
2. **The injured driver's own med-pay coverage** (or **PIP** in no-fault states) — pays accident-related medical bills regardless of fault, usually up to a $1,000-$10,000 limit, available immediately.
3. **The injured driver's UM/UIM (uninsured/underinsured motorist) coverage** — applies if the at-fault driver was uninsured or under-insured.
4. **The patient's health insurance** — pays as if the medical bill were not accident-related, usually with subrogation rights against the eventual liability settlement.
5. **The patient out-of-pocket** — typically only the deductible/coinsurance, and only after the above have been exhausted.

Some hospitals, sensing they can recover more from a liability settlement than from a health-insurance contracted rate, refuse to bill health insurance and try to **hospital lien** the patient's eventual settlement. This is a major patient-side problem.

## Where the patient gets hurt

The four most common pathologies in accident-related medical billing:

1. **Hospital refuses to bill the patient's health insurance** and instead files a hospital lien against the patient's personal-injury settlement. The hospital then claims its full chargemaster amount from the settlement, instead of the contracted insurance rate it would have accepted — eating into the patient's recovery.
2. **Health insurer denies the claim** because the bill is "accident-related" and they want auto med-pay to be primary, even though med-pay limits are exhausted.
3. **Auto insurer pays med-pay** but the medical provider also collects from the patient and from the eventual liability settlement — a triple-recovery problem.
4. **The patient does not know about med-pay** on their own auto policy and never invokes it; the provider routes the bill through health insurance with subrogation, which reduces the patient's eventual settlement.

## The rule for patients

For any accident-related medical bill:

1. **Pull all available coverages.** Get the declarations page on the patient's own auto policy. Confirm med-pay or PIP limits. Confirm UM/UIM limits. Get the at-fault driver's insurance information.
2. **Determine the correct payment order for your state.** State law varies:
   - **No-fault states** (FL, HI, KS, KY, MA, MI, MN, NJ, NY, ND, PA, UT) — PIP is primary, regardless of fault. Health insurance is usually secondary.
   - **Choice no-fault** (KY, NJ, PA) — patient may have elected limited tort or full tort; this changes the primary-payer order.
   - **Tort states** — the at-fault driver's BI liability is the eventual primary; med-pay and health insurance act as immediate-pay sources to be reimbursed at settlement.
3. **Invoke med-pay or PIP if it exists.** This is "free money" up to the policy limit and should not be skipped.
4. **Force the hospital to bill the patient's health insurance.** Even if the hospital prefers to file a lien against the settlement, most states require the hospital to bill insurance first. See state hospital-lien rules — many states (including Georgia at O.C.G.A. § 44-14-471(c) as amended 2023) require insurance-first attempts before any lien is enforceable.
5. **Track subrogation correctly.** When health insurance pays an accident-related bill, the insurer typically has a subrogation right to be reimbursed from the patient's eventual settlement. Make sure the subrogation amount reflects what the insurer actually paid (the contracted rate), not the chargemaster, and that the **made-whole doctrine** is applied where state law provides it.
6. **Reject hospital chargemaster recovery from settlements.** If a hospital tries to take its chargemaster amount from the patient's settlement (instead of the contracted insurance rate), challenge under state hospital-lien statutes and unconscionability doctrines.

## State-specific notes

**No-fault states with patient-favorable PIP frameworks:**

- **Michigan**: historically unlimited lifetime medical PIP under the no-fault Act (MCL § 500.3105 et seq.); 2019 reforms allow capped options ($50k, $250k, $500k, unlimited). Critical: Michigan PIP often supersedes health insurance for auto-related care.
- **New York**: $50,000 mandatory PIP (Reg 68; N.Y. Ins. Law § 5103). PIP is primary; insurers and providers fight over allocation.
- **Florida**: $10,000 PIP. PIP is primary up to limit. Hospital-friendly statutory regime.

**Tort states with patient-favorable made-whole doctrines:**

- **Tennessee**: made-whole doctrine recognized; subrogation only after the insured is fully compensated.
- **California**: made-whole doctrine + common-fund doctrine; insurer subrogation reduced by proportional attorney's fees.

**Tort states with hospital-lien constraints:**

- **Georgia**: O.C.G.A. § 44-14-471(c) requires insurance-first attempt; lien defective without it.
- **Florida**: hospital liens are county-by-county post-Shands.
- **Tennessee**: § 29-22-101 — hospital lien against settlement, with statutory caps.

## When this rule fires

The kit fires this rule when:

- A new bill is identified as accident-related (the patient mentions a car accident, slip-and-fall, on-the-job injury caused by a third party, etc.).
- A bill arrives from a hospital that says "this is being handled under your auto policy" or "we are not billing your health insurance" without further explanation.
- The patient discloses a hospital lien against a pending personal-injury settlement.
- The patient's health insurer denied a claim as "accident-related — submit to auto carrier."

## The patient's playbook

1. **Document the accident** — police report, photos, witness contact info, the at-fault driver's insurance info. Even months later, this is recoverable.
2. **Open the auto-insurance claims** — both your own (med-pay/PIP, UM/UIM) and the at-fault driver's BI liability. Each gets a claim number.
3. **Tell every provider** that the bill is accident-related and identify all potential payers. Many providers will route to the wrong payer if not directed.
4. **Get the hospital lien information** if applicable. If the hospital intends to lien your settlement, ask for the perfection details (date of notice, parties served, statutory citation). Most state hospital-lien statutes have strict perfection requirements; defects are common.
5. **Retain a personal-injury attorney** if the accident is non-trivial. Most PI attorneys work on contingency (typically 33-40%) and the recovery they obtain — including from health-insurance subrogation reductions and lien defeats — usually nets above what the patient would have recovered alone. The kit's other rules apply to billing minutiae; an attorney handles the settlement.
6. **For the patient working alone**: use `templates/letter_auto_med_pay.md` to force the auto insurer to apply med-pay/PIP correctly and `templates/letter_initial_dispute.md` (with the state hospital-lien citation) to push back on chargemaster-based lien recovery.

## Tracker tagging

- `findings`: `accident_related`, `hospital_lien_threatened`, `subrogation_overreach_suspected`
- `next_action`: `invoke_med_pay`, `force_health_insurance_bill`, `challenge_hospital_lien`

## When this is the wrong frame

- **Workers' comp injuries** route through workers' comp, not auto. See `rules/16_workers_comp.md`.
- **Medical malpractice** during ordinary care is its own track; not accident-related billing.
- **Slips and falls on the patient's own property** — no third-party tortfeasor; ordinary medical-billing rules apply.

## Related

- `templates/letter_auto_med_pay.md` — auto-insurer demand for proper med-pay/PIP application
- [[02_request_itemization]] — needed for any hospital lien dispute
- [[05_negotiate_fair_price]] — patient should anchor any lien-reduction negotiation to Medicare or contracted-rate
- `references/laws_state_*.md` — state-specific hospital-lien rules
