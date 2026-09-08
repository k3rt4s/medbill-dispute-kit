# Rule 03, Check the CPT codes against what actually happened

E/M documentation re-checked against public AMA guidance as of 2026-09-07: [revision overview](https://www.ama-assn.org/practice-management/cpt/cpt-evaluation-and-management) and [2023 guidelines](https://www.ama-assn.org/system/files/2023-e-m-descriptors-guidelines.pdf). Office MDM-or-time selection is also described in [2026 AMA guidance](https://www.ama-assn.org/practice-management/ama-steps-forward-program/pearl-week-when-bill-mdm-vs-time). This check covers selection basis and code families; it does not certify every January 2026 code-set change or the historical time-range tables below. Verify those against the applicable licensed release before use.

Each line on an itemized bill carries a Current Procedural Terminology (CPT) or HCPCS code. The code determines the price. A code that overstates the complexity of the encounter overstates the price.

## The rule

For every CPT code on the bill, verify three things:

1. The code description matches what the patient describes happening.
2. For evaluation-and-management codes (E/M codes, the visit-level codes), the documentation requirements for the assigned level are actually met.
3. The code is not duplicated, bundled inappropriately, or paired with another code in a way the AMA's CPT rules prohibit.

If any check fails, dispute that line.

## The E/M code structure

E/M codes are where the most common patient-side errors live. Each visit type has 4-5 levels, and each level has documentation requirements in CPT guidance and applicable payer rules. A higher level pays more, sometimes 3-5x more, so providers have an incentive to code high. E/M documentation requirements are summarized in `references/cpt_codes_em.md`. The short version:

**Emergency department visits (99281-99285):**

- 99281 has a separate service definition; do not infer its use from triage alone.
- For 99282 through 99285, review the documented MDM level: straightforward, low, moderate, or high respectively. Time and the extent of history/exam do not select the ED level.

**Office or outpatient visits (99202-99205 new patient, 99211-99215 established):**

Each level corresponds to time spent and medical decision-making complexity. Under the 2021 office-visit revision, selection uses either total time or medical decision-making (MDM), where the code permits it; history and exam alone no longer determine the level.

**The patient's job:**

You don't need to be a coder. You need to ask, "given what I described to the doctor, what they did, and how long it took, does the assigned level match the documentation requirements?" A short encounter alone does not establish an incorrect ED code; request the documentation supporting the MDM level.

## Concrete pattern: upcoded ER visit

A patient questioning a high-level ED code should request the documented MDM supporting it. A short visit or focused examination alone does not establish overcoding.

Dispute language: "Please identify the clinical documentation supporting the billed ED MDM level and correct the claim if that level is unsupported." Do not select a replacement code from duration or the patient's recollection alone.

## Concrete pattern: separately billed services that should be bundled

Some procedures include the work that other CPT codes describe, and CMS rules ("National Correct Coding Initiative" edits) prohibit billing both. If your itemized bill includes a procedure plus a small ancillary code that the procedure should include, that's a bundling violation. NCCI edits are publicly searchable on the CMS website.

## Concrete pattern: facility fee on a non-facility visit

Some hospital-owned outpatient clinics tack on a "facility fee" in addition to the doctor's professional fee. If the visit was at a clinic that doesn't function like a hospital department, the facility fee may be improper. Ask: "What service does this facility fee represent that is not already included in the professional fee?"

## Tools

- `references/cpt_codes_em.md`, the documentation requirements you'll cite
- A free CPT-code lookup (e.g. AAPC, codify, or the AMA's free patient-facing CPT lookup) for codes not covered in references/

## Related rules

- [[02_request_itemization]], you need the codes before you can check them
- [[05_negotiate_fair_price]], the same line item may be correctly coded and still wildly overpriced; these are separate disputes
