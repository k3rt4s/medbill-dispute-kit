# Tennessee state pack

The fully-worked state-law layer for Tennessee patients. The LLM uses this when the patient's state is Tennessee. For other states, use `laws_state_template.md` to find equivalents, or one of the dedicated state files (Georgia: `laws_state_ga.md`, etc.).

All citations verified against public sources as of 2026-05-18. Re-verify annually.

## Hospital itemization right

- **Statute:** **Tenn. Code Ann. § 68-11-220**
- **Source:** [law.justia.com/codes/tennessee/title-68/health/chapter-11/part-2/section-68-11-220](https://law.justia.com/codes/tennessee/title-68/health/chapter-11/part-2/section-68-11-220/)
- **What it requires:**
  - Within 10 days of discharge (or 10 days after charges can be determined), the hospital must send a statement containing the charge/expense information required on the uniform claim form.
  - Upon **written request** by the patient (or authorized representative, insurer, employer, or payer), the hospital **shall provide a more detailed itemized statement** of services and expenses.
  - **30-day response deadline** from receipt of request.
  - Request must be made **within 1 year of discharge**.

Use this as the citation in `templates/letter_itemization_request.md` for any Tennessee patient.

## Unfair claims settlement practices

- **Statute:** **Tenn. Code Ann. § 56-8-105**
- **Source:** [law.justia.com/codes/tennessee/title-56/chapter-8/part-1/section-56-8-105](https://law.justia.com/codes/tennessee/title-56/chapter-8/part-1/section-56-8-105/)
- **Substance:** Enumerates 15+ unfair practices, including misrepresenting policy provisions, failing to acknowledge communications promptly, failing to investigate claims with reasonable promptness, not attempting to effectuate prompt fair settlement where liability is reasonably clear, compelling insureds to litigate by offering substantially less than amounts ultimately recovered.
- **Critical caveat:** Tennessee courts have held there is **no private right of action** under § 56-8-105. Enforcement is by the TDCI Commissioner. Cite this statute when filing a regulatory complaint, not when suing in court.

## Bad-faith failure to pay

- **Statute:** **Tenn. Code Ann. § 56-7-105**
- **Source:** [law.justia.com/codes/tennessee/title-56/chapter-7/part-1/section-56-7-105](https://law.justia.com/codes/tennessee/title-56/chapter-7/part-1/section-56-7-105/)
- **Substance:** Insurer refusing to pay a loss within **60 days after demand**, where the refusal is not in good faith and causes additional expense or loss, is liable for the loss plus interest plus up to **25% penalty**.
- **Prerequisites:** policy due and payable; formal demand made; 60-day wait period observed; refusal not in good faith.
- **This is a private right of action.** Pair with § 56-8-105 (regulatory) for the strongest TN insurer dispute.
- **Caveat:** strictly construed by Tennessee courts; not bad faith if the insurer had "substantial legal grounds" to deny. Likely **preempted by ERISA** for ERISA-covered self-funded plans.

## Dental insurance reform

- **Statute:** **Tenn. Code Ann. § 56-2-305** (enacted via HB949/SB677, effective July 1, 2024)
- **Source:** [tndental.org/dental-insurance-reform](https://www.tndental.org/dental-insurance-reform)
- **What it does:** Adds penalties to the existing Non-Covered Services Law; addresses dental-plan downcoding, bundling, and virtual-credit-card payment restrictions. Enforced by TDCI.
- **Practical use:** If a dental plan downcoded a procedure, bundled a fee into another that should be billed separately, or required the provider to accept virtual-credit-card-only reimbursement, file a TDCI complaint citing § 56-2-305.

## Surprise billing

Tennessee did **not** enact its own pre-No-Surprises-Act surprise-billing statute for fully-insured plans. The federal No Surprises Act (effective Jan 1, 2022) is the operative protection. See [`laws_federal.md`](laws_federal.md). For ground ambulance — which the federal Act excludes — there is no Tennessee state-level protection as of this writing; the dispute path is general negotiation under UCC § 2-305 and the provider's billing practices.

## Regulatory agencies

### Tennessee Department of Commerce and Insurance (TDCI), Consumer Insurance Services

- **Online complaint:** [tn.gov/commerce/insurance/consumer-resources/file-a-complaint.html](https://www.tn.gov/commerce/insurance/consumer-resources/file-a-complaint.html)
- **Phone:** **615-741-2218** or toll-free **1-800-342-4029**
- **Email:** CIS.Complaints@state.tn.us
- **Mail:** 500 James Robertson Parkway, 4th Floor, Nashville, TN 37243-0574
- **Fax:** 615-532-7389
- **Authority over:** insurers, dental plans, health plans (fully insured), agents. Route insurer disputes here.

### Tennessee Attorney General, Division of Consumer Affairs

- **Complaint portal:** [core.tn.gov](https://core.tn.gov)
- **Phone:** 615-741-4737
- **Email:** consumer.affairs@ag.tn.gov
- **Information page:** [tn.gov/attorneygeneral/working-for-tennessee/file-a-consumer-complaint.html](https://www.tn.gov/attorneygeneral/working-for-tennessee/file-a-consumer-complaint.html)
- **Authority over:** providers, hospitals, debt collectors, deceptive practices under the Tennessee Consumer Protection Act. Route provider/hospital/collector disputes here.

### Tennessee Health Facilities Commission

- **Phone:** 1-877-287-0010
- **Authority over:** facility-level complaints against hospitals (licensing, patient care, but **not** billing). Route only patient-care or facility-licensure complaints here.

## Small claims court

- **Court name:** **General Sessions Court** (civil docket)
- **Jurisdictional limit:** **$25,000** — highest in the US
- **Source:** [ctas.tennessee.edu/eli/jurisdiction-general-sessions-court](https://www.ctas.tennessee.edu/eli/jurisdiction-general-sessions-court)
- **Filing fees:** typically $55-$150 (varies by county)
- **Attorney:** not required; permitted
- **Service:** by sheriff or certified mail
- **Appeals:** decisions appealable de novo to Circuit Court within **10 days**

Plan for the possibility that a corporate defendant appeals de novo to Circuit Court. At the General Sessions level you can represent yourself; if the case is appealed and you can't afford counsel, consider whether the disputed amount justifies the further proceedings. Many defendants do not bother to appeal small amounts.

## Statute of limitations

- **Breach of contract (written):** 6 years — Tenn. Code Ann. § 28-3-109
- **Breach of contract (oral):** 6 years — same statute
- **Tort (most):** 1 year — Tenn. Code Ann. § 28-3-104
- **Consumer Protection Act:** 1 year from discovery, 5 years from the deceptive act, whichever is shorter — Tenn. Code Ann. § 47-18-110

Medical billing disputes are usually breach-of-contract claims, so the 6-year clock applies. Don't wait that long; the paper trail is stronger when events are recent.

## Credit reporting

Tennessee did **not** enact a state-level prohibition on medical debt in credit reports (New York did so in 2024; Tennessee has not followed). The 2022 voluntary changes by Equifax/Experian/TransUnion still apply nationwide:

- Paid medical collections are removed from credit reports
- One-year grace period before unpaid medical debt may be reported
- Medical collections under $500 are excluded entirely (effective April 2023)

See [`laws_federal.md`](laws_federal.md) for the federal context.

## Hospital lien law

Tennessee allows hospitals to file liens against personal-injury settlement proceeds for unpaid bills under **Tenn. Code Ann. § 29-22-101** (the Hospital Lien Act). This is rarely relevant to general billing disputes but matters if the bill stems from an accident with a third-party tortfeasor.

## Tennessee charity care

Tennessee non-profit hospitals are subject to IRS § 501(r) (see `laws_federal.md`) but there is no Tennessee-specific charity-care statute that exceeds the federal floor. Use the federal pattern: demand the hospital's Financial Assistance Policy, screen through [Dollar For](https://dollarfor.org), apply if eligible.

## Quick reference for letter rendering

When the LLM renders a Tennessee-bound letter, substitute these defaults:

- State statute (itemization request): **Tennessee Code Annotated § 68-11-220** with 30-day deadline
- State insurance department (CC line): Tennessee Department of Commerce and Insurance, Consumer Insurance Services, 500 James Robertson Parkway, 4th Floor, Nashville, TN 37243-0574
- State AG consumer protection (CC line): Tennessee Attorney General, Division of Consumer Affairs, [core.tn.gov](https://core.tn.gov)
- Small-claims court name: **Tennessee General Sessions Court**
- Filing fee (in 30-day warning): "$55-$150 depending on county"
- Statute of limitations (in 30-day warning): "Tenn. Code Ann. § 28-3-109 (six years for breach of contract)"
