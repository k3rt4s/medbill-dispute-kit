# State-law template

The kit ships with Tennessee fully worked out as the example. For patients in other states, the LLM walks through this template to find equivalents. **The LLM must warn the patient that any state-law citation it produces from this template should be verified before sending mail.**

## Tennessee — the worked example

### Hospital itemization right

- **Statute:** **Tenn. Code § 68-11-220**
- **Source:** [law.justia.com/codes/tennessee/title-68/health/chapter-11/part-2/section-68-11-220](https://law.justia.com/codes/tennessee/title-68/health/chapter-11/part-2/section-68-11-220/)
- **What it requires:**
  - Within 10 days of discharge (or 10 days after charges can be determined), the hospital must send a statement containing the charge/expense information required on the uniform claim form.
  - Upon **written request** by the patient (or authorized representative, insurer, employer, or payer), the hospital **shall provide a more detailed itemized statement** of services and expenses.
  - **30-day** response deadline.
  - Request must be made **within 1 year of discharge**.

### Unfair claims settlement practices

- **Statute:** **Tenn. Code § 56-8-105**
- **Source:** [law.justia.com/codes/tennessee/title-56/chapter-8/part-1/section-56-8-105](https://law.justia.com/codes/tennessee/title-56/chapter-8/part-1/section-56-8-105/)
- **Substance:** Enumerates 15+ unfair practices, including misrepresenting policy provisions, failing to acknowledge communications promptly, failing to investigate claims with reasonable promptness, not attempting to effectuate prompt fair settlement where liability is reasonably clear, compelling insureds to litigate by offering substantially less than amounts ultimately recovered.
- **Critical caveat:** Tennessee courts have held there is **no private right of action** under § 56-8-105. Enforcement is by the TDCI Commissioner. Cite this statute when filing a regulatory complaint, not when suing in court.

### Bad faith failure to pay

- **Statute:** **Tenn. Code § 56-7-105**
- **Source:** [law.justia.com/codes/tennessee/title-56/chapter-7/part-1/section-56-7-105](https://law.justia.com/codes/tennessee/title-56/chapter-7/part-1/section-56-7-105/)
- **Substance:** Insurer refusing to pay a loss within **60 days after demand**, where the refusal is not in good faith and causes additional expense or loss, is liable for the loss plus interest plus up to **25% penalty**.
- **Prerequisites:** policy due and payable; formal demand made; 60-day wait period observed; refusal not in good faith.
- **This is a private right of action.** Pair with § 56-8-105 (regulatory) for the strongest TN insurer dispute.
- **Caveat:** strictly construed by Tennessee courts; not bad faith if the insurer had "substantial legal grounds" to deny. Likely **preempted by ERISA** for ERISA-covered self-funded plans.

### Dental insurance reform

- **Statute:** **Tenn. Code § 56-2-305** (enacted via HB949/SB677, effective July 1, 2024)
- **Source:** [tndental.org/dental-insurance-reform](https://www.tndental.org/dental-insurance-reform)
- **What it does:** Adds penalties to the existing Non-Covered Services Law; addresses dental-plan downcoding, bundling, and virtual-credit-card payment restrictions. Enforced by TDCI.

### Regulatory agencies

- **Tennessee Department of Commerce and Insurance (TDCI), Consumer Insurance Services**
  - Online complaint: [tn.gov/commerce/insurance/consumer-resources/file-a-complaint.html](https://www.tn.gov/commerce/insurance/consumer-resources/file-a-complaint.html)
  - Phone: **615-741-2218** or **1-800-342-4029**
  - Email: CIS.Complaints@state.tn.us
  - Mail: 500 James Robertson Parkway, 4th Floor, Nashville, TN 37243-0574
  - Fax: 615-532-7389
  - For insurer disputes (denials, slow pay, misrepresentation)
- **Tennessee Attorney General, Division of Consumer Affairs**
  - Complaint portal: [core.tn.gov](https://core.tn.gov)
  - Phone: 615-741-4737
  - Email: consumer.affairs@ag.tn.gov
  - For provider/hospital/collector disputes under the Tennessee Consumer Protection Act
- **Tennessee Health Facilities Commission**
  - For facility-level complaints against hospitals
  - Phone: 1-877-287-0010

### Small claims court

- **Court name:** General Sessions Court (civil)
- **Jurisdictional limit:** **$25,000** — highest in the US
- **Source:** [ctas.tennessee.edu/eli/jurisdiction-general-sessions-court](https://www.ctas.tennessee.edu/eli/jurisdiction-general-sessions-court)
- **Filing fees:** typically $55-$150 (varies by county)
- **Attorney:** not required, permitted
- **Service:** by sheriff or certified mail
- **Appeals:** decisions appealable de novo to Circuit Court within **10 days**, so plan for the possibility that a hospital drags it up

---

## Looking up equivalents in other states

For each Tennessee item above, find the equivalent in the patient's state. Resources to use:

- **Justia state codes:** [law.justia.com/codes/](https://law.justia.com/codes/) — searchable by state
- **Cornell Legal Information Institute:** [law.cornell.edu](https://www.law.cornell.edu/)
- **State insurance department directory:** [naic.org/state_web_map.htm](https://content.naic.org/state-insurance-departments)
- **State attorney general directory:** [naag.org](https://www.naag.org/find-my-ag/)
- **State court small-claims directory:** Google "[State] small claims court limit" and check the state's judicial branch site.

### Items to find for each state

1. The hospital itemization statute (analogous to TN § 68-11-220). Most states have one; some give 30 days, some 60.
2. The unfair claims settlement practices statute (most states have a near-identical version of the NAIC model act).
3. The bad-faith remedy or, if no specific statute, the common-law bad-faith cause of action.
4. The state insurance department complaint portal and phone number.
5. The state attorney general consumer protection portal.
6. The small-claims court name, dollar limit, filing fee, and whether an attorney is permitted.
7. Any state-level **surprise-billing** statute that may be broader than the federal No Surprises Act (e.g. California AB 72, New York Article 49, Texas SB 1264, Maryland's all-payer model, Washington Balance Billing Protection Act). State law that is broader than the federal floor still applies.
8. Any state-level **ground ambulance** balance-billing statute (the federal Act does not cover ground ambulance).
9. Any state-level **medical debt credit-reporting** restrictions (e.g. New York's 2024 law prohibiting medical debt on credit reports).

### Warning the LLM must surface

After looking up a state-specific citation for the first time in a session, the LLM must say:

> "I found the citation through public sources, but state law changes and citations can be reorganized. Before mailing this letter, please verify the statute number on your state's official code website or with a local consumer-law attorney. For a high-stakes letter, free 30-minute consultations are common via the state bar referral service."

This is not optional. Citing a wrong statute number in a dispute letter weakens the patient's position. Better to write "the applicable [State] hospital itemization statute" if uncertain than to cite the wrong number.

---

## State quick reference (skeleton)

Contributors are welcome to fill in additional states. Each state should have its own subsection following the Tennessee template above. Required fields per state:

- Hospital itemization statute number and response deadline
- Unfair claims practices statute number and whether there's a private right of action
- Bad-faith remedy (statute or common law)
- Surprise-billing statute (if broader than federal NSA)
- Ground-ambulance protection (if any)
- State insurance department: name, phone, online complaint URL
- State attorney general consumer protection: phone, online complaint URL
- Small-claims court: name, limit, filing fee
- Notable: state-specific medical-debt credit-reporting restrictions

PRs that add a state pack should include source URLs for each citation and the date the contributor last verified the citation.
