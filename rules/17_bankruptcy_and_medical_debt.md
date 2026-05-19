# Rule 17 — Bankruptcy and medical debt

Medical debt is the leading cause of US personal bankruptcy. For patients whose medical debt exceeds their realistic ability to repay, bankruptcy is not a failure to use the kit's other rules — it is an additional tool that can discharge medical debt in months when the other tools cannot.

This rule explains when bankruptcy is the right move, when it is the wrong move, and how to coordinate with the kit's other dispute paths. It is not a substitute for an attorney; non-trivial bankruptcies should be filed by counsel. The kit's role is to help the patient identify when to consult counsel and what to bring.

## The two patient-relevant chapters

**Chapter 7 — straight liquidation.** Most patient medical-debt bankruptcies. Wipes out unsecured medical debt entirely, typically within 3-4 months of filing. Requires passing the **means test** (income below a state-specific median, or a more permissive disposable-income calculation). Filing fee approximately $338; fee waiver available for income below 150% of federal poverty level.

**Chapter 13 — repayment plan.** A 3-5 year repayment plan supervised by the court. Used when the patient has regular income but cannot manage current debts, or when Chapter 7 isn't available (income too high for means test, or recent prior discharge). Medical debt is treated as unsecured; typically receives a fraction of its face value.

## When bankruptcy is the right tool

Yes:

- **Medical debt exceeds patient's net worth and there is no realistic path to repayment** within a few years.
- Other debts (credit cards, medical-debt collections, predatory consumer loans) are compounding the problem.
- The patient is being sued by a hospital or collector and the lawsuit will go to judgment before any kit-based dispute can resolve.
- Wage garnishment or bank-account levy is imminent.
- The patient's stress and life-quality cost of carrying the debt is significant.

No, or not yet:

- **The bill is wrong** — dispute it first. Bankruptcy discharges a wrong bill at the cost of a 7-year credit-report mark; far better to defeat the wrong bill outright. Use the kit's regular dispute tools.
- **The bill is dispute-eligible under No Surprises Act, EMTALA, or state surprise-billing law** — these federal/state protections can eliminate the bill entirely. Use them.
- **The patient qualifies for IRS § 501(r) charity care or a state-specific charity-care program** — apply for those first. Charity care produces a clean reduction without credit-report impact.
- **The amount is small enough that the bankruptcy filing fee and attorney's fees exceed the debt** (rough threshold: $2,000-$3,000 in total medical debt). Other debts may still justify filing.
- **The patient owns significant non-exempt assets** (a high-equity home above the state exemption, a paid-off vehicle above the vehicle exemption, etc.). Chapter 7 trustees can liquidate non-exempt assets; the patient may lose more than they gain.

## Medical-debt-specific bankruptcy mechanics

- **Medical debt is unsecured.** It has no priority and no collateral. In Chapter 7, it is discharged with the credit-card debt and similar unsecured obligations. In Chapter 13, it shares pro rata in whatever the plan pays.
- **Medical debt cannot trigger non-dischargeability.** Unlike taxes, child support, student loans (mostly), and fraud-tinged debts, medical debt has no special non-dischargeability rule. A pre-petition medical debt is fully dischargeable.
- **Hospital liens against personal-injury settlements** are different. A perfected lien may survive bankruptcy because it attaches to specific property (the settlement proceeds). Strip-and-avoid procedures exist but require an attorney.
- **Recent treatment is fine.** There is no rule that disqualifies recently-incurred medical debt. The "presumption of fraud" rules for credit-card purchases shortly before filing do not apply to medical care.
- **The automatic stay** under 11 U.S.C. § 362 stops collection activity, lawsuits, wage garnishment, and bank levies the moment the petition is filed. Hospitals continuing to collect after the stay is in effect are violating federal law and the patient (or the bankruptcy trustee) may recover damages.

## The coordination problem

Patients in difficult financial situations sometimes find themselves running multiple tracks at once: a § 501(r) FAP application, a state insurance department complaint, a 30-day warning letter, and a looming bankruptcy decision. The kit's posture:

1. **If bankruptcy is on the table, talk to a bankruptcy attorney first.** Pre-bankruptcy moves (paying some bills, transferring assets to family, large purchases) can be scrutinized and reversed by the trustee. Don't make moves until you have a plan.
2. **Continue the kit's disputes if they will conclude before bankruptcy filing.** A bill resolved through dispute is a debt that doesn't go into the bankruptcy.
3. **Stop active disputes once the bankruptcy is filed.** The automatic stay protects the patient; the trustee handles the rest. Letters to billing departments after filing should be the bankruptcy attorney's job.
4. **Don't pay random small debts on the eve of filing.** Pre-petition payments to favored creditors can be "preferences" the trustee claws back.

## Free and low-cost help

- **State legal aid organizations** every state. Most accept bankruptcy intake; some have dedicated bankruptcy clinics.
- **Federal bankruptcy attorney referral panels** via the state bar, often with reduced consultation fees.
- **Upsolve** (upsolve.org) — non-profit that helps low-income filers complete Chapter 7 pro se for free. Good for straightforward cases under the means-test income threshold.
- **Public-interest bankruptcy clinics** at many law schools.
- **NACA** (National Association of Consumer Advocates) — directory of consumer-protection attorneys including bankruptcy.

## Chapter 7 means test (high level)

Filed using Form 122A-1. Step 1: current monthly income (average over the 6 months before filing). Step 2: compare to state-specific median. If below median, presumed eligible. If above, additional calculation on Form 122A-2 deducts allowable expenses; if remaining disposable income is below a threshold, still eligible. Patient should not attempt the means test alone for non-trivial cases.

## Means-test medical-deduction angle

The means test allows deduction of "reasonably necessary" out-of-pocket health expenses (insurance premiums, prescription costs, recurring medical needs). Patients with ongoing chronic conditions often find their disposable income falls dramatically once these are correctly counted. An attorney handles this.

## Credit-report impact

- Chapter 7 stays on the credit report for **10 years from filing**.
- Chapter 13 stays for **7 years from filing**.
- Individual discharged debts may continue to appear with a "discharged" notation.
- Credit recovery typically begins within 1-2 years of discharge for filers who manage other credit obligations responsibly post-discharge.

## When the patient has already been sued

A lawsuit on medical debt is a strong signal that bankruptcy may be the right move:

- Once judgment is entered, the creditor gets wage garnishment, bank levy, and lien rights.
- A bankruptcy filed before judgment is much cleaner. After judgment, the judgment itself is dischargeable (unsecured) but pre-judgment activity that's already happened is not undone.
- If a lawsuit is filed, contact a bankruptcy attorney immediately; do not let the case go to default.

## Tracker tagging

The LLM logs bankruptcy-related cases with:

- `findings`: `bankruptcy_candidate`, `bankruptcy_filed`, `automatic_stay_active`
- `next_action`: `consult_bankruptcy_counsel`, `monitor` (after filing)

Note: once bankruptcy is filed, the kit's role on most bills is to track them as "automatically stayed" and let the attorney handle. Re-engage post-discharge if needed.

## Limits

- The kit does not draft bankruptcy petitions, schedules, statements of financial affairs, or means-test calculations. These require an attorney for any non-trivial case, and Upsolve for very simple cases. The kit's role is to identify whether bankruptcy is on the table and to surface the right next step.

## Related

- [[01_never_pay_first]] — applies even more strongly when bankruptcy is being considered; do not preferentially pay one creditor over another in the run-up
- [[15_auto_med_pay]] — hospital lien situations interact with bankruptcy in complex ways
- `references/laws_federal.md` — the FDCPA continues to apply during bankruptcy and gives the patient additional remedies if a collector violates the automatic stay
