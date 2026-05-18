# Rule 03 — Check the CPT codes against what actually happened

Each line on an itemized bill carries a Current Procedural Terminology (CPT) or HCPCS code. The code determines the price. A code that overstates the complexity of the encounter overstates the price.

## The rule

For every CPT code on the bill, verify three things:

1. The code description matches what the patient describes happening.
2. For evaluation-and-management codes (E/M codes — the visit-level codes), the documentation requirements for the assigned level are actually met.
3. The code is not duplicated, bundled inappropriately, or paired with another code in a way the AMA's CPT rules prohibit.

If any check fails, dispute that line.

## The E/M code structure

E/M codes are where the most common patient-side errors live. Each visit type has 4-5 levels, and each level has documentation requirements set by CMS. A higher level pays more — sometimes 3-5x more — so providers have an incentive to code high. CMS documentation requirements are detailed in `references/cpt_codes_em.md`. The short version:

**Emergency department visits (99281-99285):**

- 99281 — Level 1, straightforward problem (minor)
- 99282 — Level 2, low-complexity
- 99283 — Level 3, moderate-complexity
- 99284 — Level 4, moderate-to-high complexity
- 99285 — Level 5, high complexity, comprehensive evaluation

**Office or outpatient visits (99202-99205 new patient, 99211-99215 established):**

Each level corresponds to time spent and medical decision-making complexity. As of the 2021 CMS revision, the dominant factor is either total time or medical decision-making (MDM); history and exam alone no longer determine the level.

**The patient's job:**

You don't need to be a coder. You need to ask, "given what I described to the doctor, what they did, and how long it took, does the assigned level match the documentation requirements?" If the encounter was 15 minutes with a focused exam for one straightforward problem and the bill shows 99285, the bill is wrong.

## Concrete pattern: upcoded ER visit

Patient goes to ER for one defined complaint, sees a doctor for 15-20 minutes, gets a simple intervention (X-ray, basic blood work, prescription), goes home. Bill arrives coded 99285. 99285 requires a comprehensive history, a comprehensive exam, and high-complexity medical decision-making. A 20-minute visit for a single straightforward problem doesn't meet those requirements.

Dispute language: "CPT 99285 requires comprehensive history, comprehensive examination, and high-complexity medical decision-making per CMS documentation guidelines. The encounter on [date] was approximately [N] minutes, addressed a single chief complaint, and involved a focused examination with straightforward medical decision-making. The appropriate code is 99282 or 99283. Please recode and reissue the corrected bill, or provide documentation justifying Level 5."

## Concrete pattern: separately billed services that should be bundled

Some procedures include the work that other CPT codes describe, and CMS rules ("National Correct Coding Initiative" edits) prohibit billing both. If your itemized bill includes a procedure plus a small ancillary code that the procedure should include, that's a bundling violation. NCCI edits are publicly searchable on the CMS website.

## Concrete pattern: facility fee on a non-facility visit

Some hospital-owned outpatient clinics tack on a "facility fee" in addition to the doctor's professional fee. If the visit was at a clinic that doesn't function like a hospital department, the facility fee may be improper. Ask: "What service does this facility fee represent that is not already included in the professional fee?"

## Tools

- `references/cpt_codes_em.md` — the documentation requirements you'll cite
- A free CPT-code lookup (e.g. AAPC, codify, or the AMA's free patient-facing CPT lookup) for codes not covered in references/

## Related rules

- [[02_request_itemization]] — you need the codes before you can check them
- [[05_negotiate_fair_price]] — the same line item may be correctly coded and still wildly overpriced; these are separate disputes
