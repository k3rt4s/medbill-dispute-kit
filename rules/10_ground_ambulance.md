# Rule 10 — Ground ambulance balance billing

The federal No Surprises Act explicitly excludes ground ambulance from its balance-billing protections. This is the single largest gap in federal law. Ground ambulance bills are the most common surprise medical bill that remains legal under federal law, and they routinely run $1,500-$5,000 for short transports.

State law is the patient's only structural protection here. A patchwork of about a dozen states have closed the gap; the rest have not.

## The rule

For any ground ambulance bill:

1. **Check state law first.** Whether the patient has any legal protection depends entirely on the state where the service was rendered, not where the patient lives.
2. If the patient's state has a ground-ambulance protection, route the bill through the state's mechanism (analogous to a No Surprises Act dispute). Use the state-specific citation in the dispute letter.
3. If the patient's state does **not** have a ground-ambulance protection, the dispute is on three other tracks running in parallel:
   - **Insurance reprocessing**: most plans pay something for out-of-network ambulance under their out-of-network benefits; verify the plan paid what it owed and that any deductible was applied correctly.
   - **Unreasonable pricing**: UCC § 2-305 (open-price term, see `references/laws_federal.md`) and state UDAP statutes apply. The Medicare ambulance fee schedule is the floor anchor.
   - **Hardship**: most municipal ambulance services run hardship programs; non-municipal services almost always have unofficial discounts available on request.

## State protections (as of 2026-05-18)

The current state list is fluid; verify before relying. A non-exhaustive list of states that have enacted ground-ambulance balance-billing protections:

| State      | Statute                                        | Effective                                                  | Notes                                                                                                                                               |
| ---------- | ---------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| California | Health & Safety Code § 1797.225                | 2024-01-01                                                 | Limits balance billing for ground ambulance                                                                                                         |
| Colorado   | C.R.S. § 25.5-4-414                            | 2025-01-01                                                 | Comprehensive ground ambulance protection                                                                                                           |
| Delaware   | 18 Del. C. § 3370A                             | 2024                                                       |                                                                                                                                                     |
| Georgia    | O.C.G.A. § 33-20E-1 et seq. (HB 286 amendment) | 2024-01-01                                                 | Patient held harmless; insurer pays greater of negotiated rate, U&C, or 180% of Medicare. See [`laws_state_ga.md`](../references/laws_state_ga.md). |
| Illinois   | 215 ILCS 5/356z.3a                             | 2023                                                       |                                                                                                                                                     |
| Maine      | 24-A M.R.S. § 4303-E                           | 2022                                                       |                                                                                                                                                     |
| Maryland   | Md. Code, Ins. § 15-1632                       | 2024                                                       |                                                                                                                                                     |
| New York   | N.Y. Pub. Health Law § 4906                    | 2022                                                       |                                                                                                                                                     |
| Ohio       | Ohio Rev. Code § 3902.50                       | 2023                                                       |                                                                                                                                                     |
| Vermont    | 8 V.S.A. § 4089b                               | 2023                                                       |                                                                                                                                                     |
| Washington | Wash. Rev. Code § 48.49.030                    | Balance Billing Protection Act extends to ground ambulance |                                                                                                                                                     |

States not on this list have no specific ground-ambulance balance-billing protection as of this writing. Tennessee is one of them.

Re-verify your state's current status using the Commonwealth Fund's state-protection tracker at [commonwealthfund.org](https://www.commonwealthfund.org/), the National Conference of State Legislatures (NCSL) ambulance-billing tracker, or your state insurance department.

## ERISA preemption (critical)

Every state ground-ambulance protection is **preempted as to self-funded ERISA employer plans**. If the patient's plan is self-funded (most large-employer plans), state law does not apply — even if the patient is in a state with strong protections. The only available leverage for self-funded plans is general negotiation under UCC § 2-305 and the federal Patient-Provider Dispute Resolution process if the patient is technically self-pay for this bill.

The LLM must ask the patient: is your health plan self-funded or fully-insured? If the patient doesn't know, ask them to check their plan documents or call HR. The Summary Plan Description typically discloses this.

## How to dispute a ground-ambulance bill in a protected state

Use `templates/letter_ground_ambulance.md` with the state-specific citation substituted. The letter pattern is similar to a No Surprises Act dispute (`letter_no_surprises_violation.md`), but the legal basis is state-law balance-billing prohibition rather than federal NSA. CC the state insurance department.

## How to dispute a ground-ambulance bill in an unprotected state

There is no specific legal hook prohibiting the balance bill. The dispute is on the merits:

### Track 1 — Insurance side

Verify the plan paid what it owed:

1. Did the plan apply your out-of-network deductible / out-of-pocket maximum correctly?
2. Did the plan pay the Medicare-equivalent rate or higher? Some plans contractually pay 200% of Medicare for ambulance services. Pull the plan's Summary Plan Description and check.
3. If the plan denied or paid less than reasonable-and-customary, appeal using `templates/letter_insurance_appeal_erisa.md` (for ERISA plans) or the equivalent for non-ERISA plans.

### Track 2 — Provider side, fair-price argument

The Medicare ambulance fee schedule sets a defensible floor. The CMS Ambulance Fee Schedule lookup is at [cms.gov/medicare/medicare-fee-for-service-payment/ambulancefeeschedule](https://www.cms.gov/medicare/medicare-fee-for-service-payment/ambulancefeeschedule). A common pattern: an ambulance provider charges $3,500; Medicare allows ~$450 for the same transport; the plan paid 200% of Medicare ($900); the patient is left with $2,600 in "balance." The provider's $3,500 charge is the chargemaster, not the negotiated rate. Argue down using UCC § 2-305 and Medicare as the floor.

Use `templates/letter_initial_dispute.md` with a single price-gouging block; cite the Medicare ambulance fee schedule and any state UDAP statute.

### Track 3 — Hardship and municipal-discount path

For municipal ambulance services (city or county-owned): most run formal financial-assistance programs. Ask in writing for the municipality's ambulance billing financial-assistance policy. Many waive the balance entirely for low-income residents.

For private ambulance providers: most have unofficial discounts. Calling the billing department and asking "what's the cash discount if I pay today?" frequently produces 30-50% off without any further negotiation.

## When to escalate to small claims

Ground-ambulance disputes are common small-claims cases. The disputed amounts are typically well under the state's jurisdictional limit, the legal arguments are simple (Medicare rate as the floor, UCC § 2-305 as the lever, state UDAP as the hammer), and the corporate defendant's cost to defend exceeds any plausible recovery. Use the same escalation ladder as in `rules/06_small_claims.md`.

## Subscription services (a partial workaround for chronic risk)

If the patient relies on ambulance services regularly (e.g. dialysis transport) or lives in an area with frequent need, some municipalities offer **ambulance subscription services** for $50-$150/year that cap the patient's responsibility regardless of the bill. This is a prevention strategy, not a dispute strategy, but worth mentioning to patients in unprotected states who anticipate future need.

## Related rules

- [[04_no_surprises_act]] — the federal Act that does not cover ground ambulance
- [[05_negotiate_fair_price]] — the playbook when state law gives you no specific hook
- [[06_small_claims]] — where unresolved ground-ambulance disputes often land
- [[07_appeal_insurance_denial]] — for the insurance-side track
