# CPT codes — E/M (evaluation and management)

Documentation requirements for the visit-level codes that drive the largest fraction of patient-side billing disputes. These are the codes patients most often see upcoded.

## Copyright note

CPT codes are owned by the American Medical Association. The five-digit codes themselves are public, but the AMA's full descriptors are copyrighted. This file contains short paraphrased summaries (fair-use commentary). For authoritative full descriptors, use:

- **AMA CPT lookup** (free, 5 searches per day after free signup): [ama-assn.org/practice-management/cpt](https://www.ama-assn.org/practice-management/cpt)
- **CMS Physician Fee Schedule Lookup** (free, no limits): [cms.gov/medicare/physician-fee-schedule/search](https://www.cms.gov/medicare/physician-fee-schedule/search)

The LLM should not redistribute full AMA CPT descriptors verbatim. Paraphrase or link.

---

## Emergency Department visits — 99281 through 99285

Source for E/M revisions: [AMA 2023 E/M descriptors and guidelines (PDF)](https://www.ama-assn.org/system/files/2023-e-m-descriptors-guidelines.pdf). ACEP coverage of the 2023 changes: [acep.org](https://www.acep.org/freestanding/newsroom/fs-newsroom-articles/april2023/2023-ama-cpt-documentation-guideline-changes-for-ed-em-codes-99281-99285).

### Code selection driver

For ED codes (99281-99285), the level is selected by **medical decision-making (MDM) complexity only**. Time is **not** a factor for ED codes (unlike office codes). The 2023 revision aligned ED MDM with the 2021 office-visit framework.

### The five levels

| Code  | MDM complexity                        | Typical clinical pattern                                                                                                   |
| ----- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 99281 | minimal / may not require a physician | nurse triage, minor problem                                                                                                |
| 99282 | straightforward                       | one self-limited or minor problem                                                                                          |
| 99283 | low                                   | one stable chronic illness, or acute uncomplicated illness/injury                                                          |
| 99284 | moderate                              | undiagnosed new problem with uncertain prognosis, or one chronic illness with mild exacerbation                            |
| 99285 | high                                  | one or more chronic illnesses with severe exacerbation, or acute illness/injury posing a threat to life or bodily function |

### MDM elements (must satisfy 2 of 3 for the level)

1. **Number and complexity of problems addressed** at the encounter
2. **Amount and complexity of data reviewed and analyzed** (records, tests, independent interpretations)
3. **Risk of complications, morbidity, or mortality** from the patient's management

### What patients should ask

For a billed 99284 or 99285:

- Was your problem one of the patterns at that level? An ankle sprain treated with an ACE wrap is not 99285. A heart attack is.
- How many tests did the physician personally interpret? How many records from outside sources?
- What was the actual treatment plan, and what was its risk profile?

A 15-20 minute visit for one straightforward complaint with focused exam and simple management is 99282 or 99283, not 99285.

### Dispute language

> CPT 99285 requires medical decision-making of **high** complexity per AMA 2023 E/M guidelines. The encounter on [date] presented one chief complaint, involved [specific tests/imaging], required straightforward/low/moderate management with no acute threat to life or bodily function. The appropriate code is 99282/99283/99284. Please recode and reissue the corrected bill, or provide the clinical documentation that supports high-complexity MDM as defined by the AMA.

---

## Office or other outpatient visits — 99202 through 99215

Source: [AMA E/M revisions FAQs](https://www.ama-assn.org/practice-management/cpt/cpt-evaluation-and-management-em-revisions-faqs).

### Code selection driver (since January 1, 2021)

The level is selected by **either** total time on the day of the encounter **or** medical decision-making complexity. History and exam are no longer scoring factors. 99201 was deleted in 2021.

### Time ranges

**New patient (no encounter with this practice in 3+ years):**

| Code  | Total time on date of encounter | MDM equivalent  |
| ----- | ------------------------------- | --------------- |
| 99202 | 15-29 minutes                   | straightforward |
| 99203 | 30-44 minutes                   | low             |
| 99204 | 45-59 minutes                   | moderate        |
| 99205 | 60-74 minutes                   | high            |

**Established patient:**

| Code  | Total time on date of encounter | MDM equivalent  |
| ----- | ------------------------------- | --------------- |
| 99211 | (no specific time; nurse visit) | minimal         |
| 99212 | 10-19 minutes                   | straightforward |
| 99213 | 20-29 minutes                   | low             |
| 99214 | 30-39 minutes                   | moderate        |
| 99215 | 40-54 minutes                   | high            |

**99417** is an add-on code for prolonged time beyond 99205 or 99215, in 15-minute increments.

### What patients should ask

For a billed 99214 or 99215:

- How long was your encounter, total, including the doctor's review of records before and notes after?
- Was the MDM moderate or high (matching the table above)?

If neither the time nor the MDM supports the billed level, the bill is wrong.

### Dispute language

> CPT 99215 requires either 40-54 minutes of total time on the date of the encounter or medical decision-making of high complexity, per AMA E/M guidelines effective January 1, 2021. The encounter on [date] took approximately [N] minutes total and involved [low/moderate/high]-complexity decision-making. The appropriate code is 99213/99214. Please recode and reissue the corrected bill.

---

## Other E/M categories not covered here

- Hospital inpatient/observation E/M codes (99221-99239) follow a similar MDM-or-time structure since 2023
- Subsequent hospital and consultation codes have their own time/MDM tables
- Telehealth modifiers (95, 93, GT, GQ) may apply

For these, point the patient to AMA or CMS lookup tools rather than paraphrasing here.

---

## NCCI edits (bundling)

The Medicare National Correct Coding Initiative publishes pairs of CPT codes that should not be billed together. If your itemized bill has both members of an NCCI pair, that's a bundling violation.

- **NCCI edit lookup:** [cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits)
- The full edit files are downloadable quarterly from CMS.

For most patient disputes, the NCCI edits matter when you see two codes for closely related services on the same date. Use the CMS edit checker to confirm.
