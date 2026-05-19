# Rule 16 — Workers' compensation medical bills

When an injury or illness arises out of and in the course of employment, workers' compensation is the exclusive remedy in nearly all US states. Workers' comp has its own medical-fee schedule, its own provider network, its own claims process, and — critically — its own balance-billing prohibition. A worker who receives a balance bill for accepted workers' comp care is being charged something they almost certainly do not owe.

This rule fires whenever a medical bill stems from a work-related injury or illness.

## Headline rule

**A worker with an accepted workers' comp claim cannot be balance-billed by the treating provider for accepted services.** The provider's only recovery for workers' comp services is the state's workers' comp fee schedule, paid by the workers' comp insurer or self-insured employer. If a provider tries to bill the patient, the bill is improper.

## How workers' comp differs from ordinary medical billing

| Element              | Ordinary medical                          | Workers' comp                                                           |
| -------------------- | ----------------------------------------- | ----------------------------------------------------------------------- |
| Who pays             | Health insurance + patient cost-sharing   | Workers' comp carrier or self-insured employer; no patient cost-sharing |
| Fee schedule         | Plan-negotiated rates (Medicare-anchored) | State workers' comp fee schedule                                        |
| Provider choice      | Patient's choice (within plan network)    | State-dependent; many states allow employer designation initially       |
| Balance billing      | Permitted in some scenarios               | **Prohibited** for accepted claims                                      |
| Appeals              | Plan internal → external review → court   | State workers' comp board → board appeals → court of appeals            |
| Patient cost-sharing | Deductible / coinsurance / copay          | **Zero** for accepted claims                                            |

## When this rule fires

The kit fires this rule when:

- A patient describes a work-related injury or illness and shows a related medical bill.
- A bill explicitly references workers' compensation (the worker's comp carrier, the employer, a WC claim number).
- A provider is balance-billing for what should have been a workers' comp service.
- A workers' comp claim was denied or contested and the provider is now seeking payment from the patient personally.

## The patient's playbook

### 1. Report the injury / open the claim

Each state has a deadline for reporting work-related injuries to the employer. Common deadlines: 30 days in many states; some shorter. Reporting in writing creates the paper trail.

The employer files a First Report of Injury with the workers' comp carrier. The carrier then accepts or contests the claim.

### 2. Confirm the claim status

A bill stuck in the wrong place often results from claim-status confusion:

- **Claim accepted:** medical bills go to the workers' comp carrier. The provider should not bill the patient.
- **Claim contested or under investigation:** providers sometimes bill the patient as a fallback. This is improper if the claim is eventually accepted, but it does happen.
- **Claim denied:** the patient may have to use health insurance and pursue a workers' comp appeal in parallel. Subrogation rights become complicated.

### 3. If a provider bills you while a WC claim is open or accepted

Send the provider a letter (template variant B below) identifying:

- The workers' comp carrier and claim number
- The accepted-status confirmation (if any)
- A demand to redirect the bill to the workers' comp carrier and to remove the patient from collection

### 4. If the WC claim is denied

Two parallel tracks:

- **Workers' comp appeal** in the state's workers' comp board / commission. State-specific procedure.
- **Bill payment via health insurance pending the appeal.** Health insurance may cover the care with subrogation rights against any eventual workers' comp recovery.

### 5. If the WC claim is accepted but the provider sends a balance bill anyway

This is a common pattern when the provider is not familiar with workers' comp rules or is testing whether the patient will pay. Send a firm letter citing the state's workers' comp statute and the prohibition on balance billing. CC the state workers' comp board.

## Key state-specific statutes

Each state has its own workers' comp statute. Common patterns:

- **Tennessee:** Tenn. Code Ann. § 50-6-101 et seq. Workers' Compensation Act. Balance-billing prohibition at § 50-6-204. Bureau of Workers' Compensation handles complaints.
- **California:** Cal. Lab. Code § 3200 et seq. Cal. Code Regs. tit. 8, § 9789.30 fee schedule. Strict balance-billing prohibition; provider penalties for improper billing.
- **Texas:** Tex. Lab. Code § 401 et seq. Texas is unusual: employers can opt out of state workers' comp ("non-subscribers"). For non-subscribers, ordinary medical-billing rules apply with negligence-litigation potential.
- **New York:** N.Y. Workers' Comp. Law § 13. Workers' Compensation Board handles disputes.
- **Florida:** Fla. Stat. § 440. WC providers must accept fee schedule; balance billing prohibited.
- **Pennsylvania:** 77 P.S. § 1 et seq. WCA. Stable balance-billing prohibition; Bureau of Workers' Compensation Board handles disputes.
- **Illinois:** 820 ILCS 305/. Illinois Workers' Compensation Commission.
- **Ohio:** Ohio Rev. Code § 4123. Bureau of Workers' Compensation (state-run monopoly). Different from most states.

## When this is not the right frame

- **The patient is an independent contractor** rather than an employee — workers' comp typically does not apply; the patient may have employer-side common-law negligence claims if applicable.
- **The injury is not work-related** — ordinary medical-billing rules apply.
- **The patient is in Texas with a non-subscriber employer** — workers' comp does not apply; the patient may have negligence claims and ordinary medical-billing rules apply to the medical care.
- **Federal workers** — different system (Federal Employees' Compensation Act, administered by DOL OWCP).
- **Maritime workers** — Jones Act and Longshore and Harbor Workers' Compensation Act, different again.

## Free help

- **State workers' comp ombudsman or worker-information office** in every state. Free counseling on the claims process.
- **Plaintiff-side workers' comp attorneys** generally work on contingency capped by state statute (often 20-25% of the recovery, fee-shifted in some states).

## Tracker tagging

- `findings`: `work_related_injury`, `wc_claim_accepted`, `wc_claim_denied`, `wc_balance_billing_improper`
- `next_action`: `redirect_to_wc_carrier`, `file_wc_appeal`, `engage_wc_attorney`
- Different `provider_type` is not needed; workers' comp routes through ordinary provider categories.

## Common pitfalls

- **Confusing employer's group health plan with workers' comp.** Some employers' health plans cover work-related injuries with subrogation back to the WC carrier; some do not. Confirm before assuming health insurance applies.
- **Missing the WC reporting deadline.** Many states are unforgiving; the claim is barred if not reported within the state-specific window.
- **Settling personal-injury claims against third parties without coordinating WC subrogation.** Third-party tortfeasor settlements (e.g., the contractor who caused the accident) typically have WC subrogation rights; coordinate before settling.

## Related

- [[15_auto_med_pay]] — for accident-related billing where the auto-insurance / WC interaction matters
- `references/laws_state_*.md` — state-specific WC statutes and procedures
- This rule does not yet ship a dedicated workers' comp template. The patient's primary tools are direct contact with the state workers' comp board, a workers' comp attorney for contested claims, and the general dispute templates (`letter_initial_dispute.md` with WC-specific citations) for improper balance bills.
