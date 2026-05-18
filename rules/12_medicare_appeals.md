# Rule 12 — Medicare appeals

Medicare uses a five-level appeal structure that is entirely different from ERISA-plan or commercial-plan appeals. The deadlines are short, the forms are specific, and the language patients use in their requests determines which level of review they get. This rule walks the LLM through each level.

Applies to: Original Medicare (Parts A and B), Medicare Advantage (Part C), and Medicare Part D prescription-drug plans. Each has its own variant of the five-level structure; this rule covers them together with subsection callouts.

Does **not** apply to: Medicaid (use `templates/letter_medicaid_appeal.md`), TRICARE, VA, federal employee plans.

## When this rule fires

The LLM uses Medicare appeals when:

- A bill stems from a denied Medicare claim ("Medicare did not cover this service") and the patient wants the denial reversed.
- The patient received an **MSN** (Medicare Summary Notice), an **EOB** from a Medicare Advantage plan, or a **denial of organization determination** showing a denied claim.
- The patient has a **Part D coverage determination** denying a drug.

If the dispute is purely about the amount Medicare paid (and the provider is billing the patient for the contractual write-off), that is a **provider-side dispute**, not a Medicare appeal. Use `templates/letter_initial_dispute.md` for that.

## The five levels at a glance

| Level | Original Medicare (A/B)    | Medicare Advantage (Part C) | Part D                      | Filing deadline from prior decision |
| ----- | -------------------------- | --------------------------- | --------------------------- | ----------------------------------- |
| 1     | Redetermination by the MAC | Reconsideration by the plan | Redetermination by the plan | **120 days**                        |
| 2     | Reconsideration by a QIC   | IRE review (Maximus)        | IRE review (Maximus)        | 180 days (60 for Part D)            |
| 3     | OMHA / ALJ hearing         | OMHA / ALJ hearing          | OMHA / ALJ hearing          | 60 days                             |
| 4     | Medicare Appeals Council   | Medicare Appeals Council    | Medicare Appeals Council    | 60 days                             |
| 5     | Federal District Court     | Federal District Court      | Federal District Court      | 60 days                             |

**AIC (amount-in-controversy) thresholds:** Level 3 (ALJ) requires the disputed amount to meet a published threshold (~$190 as of 2026, adjusted annually). Level 5 (federal court) requires ~$1,900 (also adjusted). Multiple denials can sometimes be aggregated to meet the threshold.

## Level 1 — Redetermination (Parts A and B)

- **Who reviews:** The Medicare Administrative Contractor (MAC) that processed the original claim.
- **Deadline to file:** **120 days** from the date on the MSN.
- **Form (recommended, not required):** **CMS-20027** ("Medicare Redetermination Request Form"), available at [cms.gov/medicare/cms-forms/cms-forms/cms-forms-items/cms019024](https://www.cms.gov/medicare/cms-forms/cms-forms/cms-forms-items/cms019024). The form is optional; a written request with the required elements is sufficient.
- **Where to file:** The address on the MSN under "How do I file an appeal?"
- **Decision timeline:** The MAC must decide within **60 days** of receiving the request.
- **What to include:**
  - Patient name and Medicare Beneficiary Identifier (MBI)
  - Specific items or services being appealed
  - Date of service
  - Date of the MSN being appealed (and a copy of the MSN with the disputed items circled)
  - The reason for the appeal (a sentence or two stating why coverage should be granted)
  - Any supporting documentation (treating provider statement, clinical-necessity evidence, plan or LCD/NCD citations)
  - Patient's signature

## Level 1 — Medicare Advantage (Part C)

- **Who reviews:** The Medicare Advantage plan itself (not the MAC).
- **Deadline to file:** **60 days** from the date of the denial notice.
- **Two timelines:**
  - **Standard:** plan must decide within 30 days (services) or 60 days (payment).
  - **Expedited:** when the standard timeframe could seriously jeopardize the enrollee's life, health, or ability to regain maximum function — plan must decide within 72 hours.
- **How to file:** Per the plan's denial notice instructions. Most plans accept written letters, fax, and online portal submissions.
- **Required elements:** same as Level 1 Original Medicare plus the plan's member ID.

## Level 1 — Part D

- **Who reviews:** The Part D plan.
- **Deadline to file:** **60 days** from the coverage-determination notice.
- **Expedited review available** when waiting could harm the enrollee.
- **Common Part D scenarios:**
  - Drug not on formulary → request a **formulary exception**
  - Plan applied a quantity limit or step therapy → request an exception to those requirements
  - Tier exception to reduce the drug's tier
- **Decision timeline:** standard 7 days, expedited 24 hours.

## Level 2 — Reconsideration by an Independent Entity

After Level 1 denial, the next stop is an independent review:

- **Original Medicare A/B:** Qualified Independent Contractor (QIC). Filed with the QIC named in the redetermination decision. **180 days** to file.
- **Medicare Advantage:** Independent Review Entity (IRE) — currently Maximus Federal Services. The plan **must** auto-forward the case to the IRE if it upholds its own denial; the enrollee does not separately file the IRE appeal in Part C, unlike Original Medicare.
- **Part D:** Independent Review Entity (IRE) — Maximus. **60 days** to file after a redetermination denial.

The IRE/QIC reviews the case de novo (fresh look, not deferential). Decisions are usually within 60 days for Part A/B and 30 days for Part D.

## Level 3 — Office of Medicare Hearings and Appeals (OMHA) / ALJ

- **Who reviews:** An Administrative Law Judge at OMHA. Hearings are usually by phone or video.
- **AIC threshold:** approximately **$190** in 2026. Aggregation of related claims is allowed.
- **Filing deadline:** **60 days** from the QIC/IRE decision.
- **Form:** **OMHA-100** ("Request for an ALJ Hearing or Review of a QIC/IRE Reconsideration") at [hhs.gov/about/agencies/omha/the-appeals-process/index.html](https://www.hhs.gov/about/agencies/omha/the-appeals-process/index.html).
- **Decision timeline:** OMHA targets 90 days from request, but real timelines are often much longer.
- **Hearing format:** Patient may appear telephonically. Patient may have a representative (lawyer, family member, advocate). Submit any new evidence in writing in advance of the hearing per OMHA's instructions.

## Level 4 — Medicare Appeals Council

- **Who reviews:** Departmental Appeals Board, Medicare Appeals Council, within HHS.
- **Filing deadline:** **60 days** from the ALJ decision.
- **Standard of review:** Deferential to ALJ findings of fact; de novo on law.
- **Form:** **DAB-101** at [hhs.gov/about/agencies/dab/different-appeals-at-dab/appeals-to-board/medicare-operating-divisions/index.html](https://www.hhs.gov/about/agencies/dab/different-appeals-at-dab/appeals-to-board/medicare-operating-divisions/index.html).

## Level 5 — Federal District Court

- **Who reviews:** US District Court (typically the district in which the patient resides).
- **AIC threshold:** approximately **$1,900** in 2026.
- **Filing deadline:** **60 days** from the Appeals Council decision.
- **Strongly recommend counsel at this level.** ERISA-style administrative-record review applies; the record locked in at OMHA largely controls.

## Patient self-help guidance the LLM should always surface

1. **Read the MSN/EOB carefully.** It will tell the patient which level they're at, what the deadline is, and where to send the appeal. Half of patient-side appeals fail on deadline grounds because the patient missed the date on the notice.
2. **Get a letter from the treating physician.** A one-page letter from the doctor stating that the service was medically necessary and citing the patient's specific clinical condition is the single most useful piece of evidence at every level. The LLM should help the patient draft a request to their physician for this letter.
3. **For coverage-policy denials, find the LCD or NCD.** Medicare publishes Local Coverage Determinations and National Coverage Determinations defining what's covered for specific conditions. If the patient's situation matches an LCD/NCD covered indication, cite it in the appeal. Search at [medicare.gov/coverage](https://www.medicare.gov/coverage) or [cms.gov/medicare/coverage](https://www.cms.gov/medicare/coverage).
4. **State Health Insurance Assistance Programs (SHIPs)** provide free, unbiased Medicare appeal help in every state. The kit's first recommendation for any Medicare-aged patient pursuing an appeal alone is to call the local SHIP. National lookup at [shiphelp.org](https://www.shiphelp.org).
5. **Medicare Rights Center** ([medicarerights.org](https://www.medicarerights.org)) and the **Center for Medicare Advocacy** ([medicareadvocacy.org](https://www.medicareadvocacy.org)) publish free appeal templates and run helplines.

## Why this is a separate track from commercial-plan appeals

- The administrative-record concept is different. In ERISA you lock the record at internal appeal and federal-court review is deferential. In Medicare you have multiple administrative levels with de novo review at QIC/IRE and ALJ levels.
- Standards of review differ: ERISA's "abuse of discretion" vs. Medicare's "preponderance of evidence" at lower levels.
- Counsel is often available on contingency in ERISA disputes for high-value claims. Medicare appeals through ALJ are routinely handled pro se with SHIP counselor support.

## Tracker tagging

The LLM logs Medicare appeals using new schema enums:

- `next_action`: `file_medicare_redetermination` (Level 1), `file_medicare_reconsideration` (Level 2), `file_medicare_alj` (Level 3)
- `action_type` in `action.toml`: `medicare_redetermination_filed`, `medicare_reconsideration_filed`, `medicare_alj_hearing_filed`

## Related rules

- [[07_appeal_insurance_denial]] — commercial / ERISA appeal contrast
- [[02_request_itemization]] — needed at every Medicare appeal level to verify what was billed
- [[09_pricing_resources]] — the patient's underlying bill from a Medicare provider is separately subject to the cost-sharing limits Medicare sets
