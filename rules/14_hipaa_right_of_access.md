# Rule 14 — HIPAA right of access

A patient's right to obtain a copy of their own medical records is a federal entitlement, not a courtesy the provider may grant or deny at will. HIPAA's Privacy Rule sets the framework, with explicit deadlines and fee caps. When a provider stalls or charges unreasonable amounts for records, the patient has both a federal complaint route (HHS Office for Civil Rights) and significant leverage on any underlying billing dispute.

This rule fires whenever the patient needs records to support a billing dispute, an insurance appeal, or a small-claims filing — and the provider is dragging their feet.

## The statute

- **Citation:** 45 CFR § 164.524 (right of access); 45 CFR § 164.526 (right to amend)
- **HHS OCR resource:** [hhs.gov/hipaa/for-individuals/medical-records/index.html](https://www.hhs.gov/hipaa/for-individuals/medical-records/index.html)
- **Right-of-access fact sheet:** [hhs.gov/hipaa/for-professionals/privacy/guidance/access](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/access)

## What the patient is entitled to

Under 45 CFR § 164.524:

1. **Designated record set:** any PHI the covered entity maintains about the patient in a designated record set, including medical records, billing records, claims processing, and case management information.
2. **Form and format:** the patient may request the records in any **readily producible** form (PDF, paper, email, electronic transfer). If the patient asks for an electronic copy and the records exist electronically, the entity must provide them electronically.
3. **Timeline:** the entity must provide access **within 30 days of the request** (with a single 30-day extension permitted, with written notice and reason). Many states require faster turnaround for state-licensed entities.
4. **Fee cap:** entities may charge only a **reasonable, cost-based fee** for: labor for copying, supplies (paper or electronic media), and postage. **Per-page fees that exceed cost are not permitted.** Search fees, fees for "creating a summary," and access fees for electronic records (beyond actual cost) are not permitted.
5. **Third-party transmission:** the patient may direct the entity to transmit a copy to a designated third party (an attorney, another provider). The same fee cap applies.

## What the patient is **not** entitled to under § 164.524

- Records the entity does not maintain (the entity cannot create new records to satisfy a request).
- Psychotherapy notes (which are separately protected).
- Information compiled in reasonable anticipation of civil, criminal, or administrative actions.

For grounds 2 and 3, the entity may still need to provide other records in the designated record set even when those specific items are excluded.

## When this rule fires

- The patient needs an itemized bill, EOB, clinical records, or imaging to support a dispute, and the provider is not responding within 30 days.
- The provider quoted a fee that exceeds reasonable cost-based pricing (e.g., $1.50/page for electronic records, $50 retrieval fee, "search and review" fees).
- The provider insists on a specific form (e.g., faxed authorization on their letterhead) when the regulation gives the patient the choice of form.
- The provider claims the records are not available, are too old, or are otherwise inaccessible without producing the actual records.

## The patient's playbook

1. **Send a written request** specifying the records sought, the form (paper, electronic, transmission to a third party), and the patient's chosen delivery method. Reference 45 CFR § 164.524.
2. **Calendar the 30-day deadline** from the date of the request.
3. **If the provider does not respond, sends a partial response, or charges an excessive fee**, send a follow-up letter citing the regulation and explicitly invoking the OCR complaint process.
4. **File an OCR complaint** at [hhs.gov/hipaa/filing-a-complaint](https://www.hhs.gov/hipaa/filing-a-complaint/index.html). The complaint must be filed within 180 days of when the patient knew or should have known of the act or omission. OCR investigates and can impose corrective-action plans and resolution agreements; entities have paid $80,000-$240,000+ per right-of-access violation in recent OCR settlements.
5. **State medical-records statute parallel route**: most states have their own medical-records-access statutes with shorter timelines (e.g., 14-21 days) and lower or capped per-page fees. Use both routes in parallel where the state law is stronger.

## How this connects to billing disputes

Patients often need:

- The complete **itemized bill** with CPT codes and clinical notes to verify what services were actually rendered → support `letter_initial_dispute.md` and CPT coding analysis under `rules/03_check_cpt_codes.md`.
- The **clinical record** to verify diagnosis and medical decision making → support No Surprises Act analysis and CPT severity coding disputes.
- The **EOB and the underlying claim** → support insurance-appeal letters under `rules/07_appeal_insurance_denial.md`.
- **Records of attempted prior authorization** → support claims-handling disputes.

A provider that won't produce these documents on a billing dispute is creating its own evidentiary record of non-cooperation — useful in any subsequent state-DOI complaint or small-claims filing.

## Fee guidance

HHS OCR guidance on reasonable cost-based fees (from the agency's published examples):

- **Electronic records, electronic transmission:** typically free or a few dollars at most.
- **Electronic records, transmitted on USB or CD:** cost of the media (~$5) plus minimal labor.
- **Paper records, paper copies:** per-page rate must reflect actual cost; many entities charge $0.10-$0.25/page in line with this.
- **Paper records, electronic scan:** cost of scanning labor (typically minutes for routine records) plus electronic-storage cost.
- **Records older than the entity's electronic system:** if retrieval requires unusual labor, a higher fee may be defensible, but only with documentation.

Per-page fees above $1 for electronic records, "search fees," or "review fees" are facially inconsistent with OCR guidance.

## Tracker tagging

The LLM logs HIPAA right-of-access work with new findings:

- `findings`: `records_request_delayed`, `records_request_excessive_fee`, `records_request_denied`
- `next_action`: `request_records_hipaa`, `file_ocr_complaint`

## When to escalate to OCR

The OCR complaint is high-leverage; it is the federal-regulator route. Trigger when:

- 30 days have passed since a written request, with no response or insufficient response.
- The fee quoted is materially above OCR's guidance.
- The entity refuses to transmit records to a third party the patient designated.
- The entity insists on procedures not permitted by the regulation (e.g., a specific form, notarization, in-person pickup).

Most providers comply once OCR is mentioned; few want the formal investigation.

## Related

- `templates/complaint_hipaa_access.md` — for the OCR complaint
- [[02_request_itemization]] — overlapping but distinct: state itemization statutes vs. HIPAA records access
- [[07_appeal_insurance_denial]] — records access is often a prerequisite to a credible appeal
