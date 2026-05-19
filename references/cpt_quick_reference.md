# CPT/HCPCS quick reference for common medical bills

A short cheat sheet of the codes that show up most often on patient bills, with what they describe and what to watch for. Not a substitute for the AMA's official CPT lookup or the CMS Physician Fee Schedule Lookup; intended as a fast-orientation guide for patients reading an itemized bill.

For the documentation requirements that drive correct vs incorrect coding for E/M codes, see `cpt_codes_em.md`. This file complements that one with procedural codes outside the E/M family.

## Important copyright note

CPT codes and full descriptors are AMA copyrighted. This file uses short paraphrased descriptions consistent with fair-use commentary. For authoritative full descriptors, use:

- **AMA CPT free lookup:** [ama-assn.org/practice-management/cpt](https://www.ama-assn.org/practice-management/cpt) (5 searches per day after free signup)
- **CMS Physician Fee Schedule Lookup** (free, no limits): [cms.gov/medicare/physician-fee-schedule/search](https://www.cms.gov/medicare/physician-fee-schedule/search)
- **HCPCS Level II codes** (public domain): [cms.gov/medicare/coding/hcpcsreleasecodesets](https://www.cms.gov/medicare/coding/hcpcsreleasecodesets)

## Evaluation and management (E/M)

See `cpt_codes_em.md` for the full E/M coding rules and documentation requirements. Brief recap:

- **99281-99285** — emergency department visits, Level 1 through Level 5
- **99202-99205** — new-patient office visits
- **99211-99215** — established-patient office visits
- **99221-99239** — hospital inpatient/observation E/M
- **99417** — prolonged time add-on (15-min increments)

## Imaging

| Code  | Description                        | Watch for                                                                                                     |
| ----- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| 70450 | CT head/brain without contrast     | Site-of-service variance is huge; same scan ranges from ~$300 (independent) to ~$3,000+ (hospital outpatient) |
| 70551 | MRI brain without contrast         | Same; ~$400-$4,000                                                                                            |
| 71045 | Chest X-ray, single view           | ~$50-$300                                                                                                     |
| 71046 | Chest X-ray, two views             | ~$100-$400                                                                                                    |
| 74176 | CT abdomen/pelvis without contrast | ~$400-$3,000                                                                                                  |
| 76700 | Abdominal ultrasound, complete     | ~$200-$1,000                                                                                                  |
| 76830 | Transvaginal ultrasound            | ~$200-$800                                                                                                    |
| 77067 | Screening mammography              | ~$100-$400 (often fully covered by insurance under ACA preventive)                                            |
| 78815 | PET-CT skull-to-thigh              | ~$2,000-$8,000                                                                                                |

## Lab

| Code  | Description                            | Watch for |
| ----- | -------------------------------------- | --------- |
| 80048 | Basic metabolic panel                  | ~$10-$150 |
| 80053 | Comprehensive metabolic panel          | ~$15-$250 |
| 80061 | Lipid panel                            | ~$15-$200 |
| 80076 | Hepatic function panel                 | ~$15-$200 |
| 81000 | Urinalysis with microscopy             | ~$5-$50   |
| 82607 | Vitamin B-12 level                     | ~$20-$120 |
| 83036 | Hemoglobin A1C                         | ~$15-$100 |
| 84443 | Thyroid stimulating hormone (TSH)      | ~$15-$150 |
| 85025 | Complete blood count with differential | ~$10-$150 |
| 86592 | Syphilis screening (RPR)               | ~$5-$50   |
| 87086 | Urine culture                          | ~$15-$100 |

Hospital lab departments routinely charge 5-15× what independent labs charge for the same panel. If the lab work was done at a hospital and the price is dramatically higher than the independent-lab equivalent, the dispute is straightforward.

## Common procedures

| Code         | Description                                                   | Watch for                                                                          |
| ------------ | ------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| 17110        | Destruction of benign skin lesion (e.g., wart removal)        | Office vs hospital outpatient is the big variance                                  |
| 36415        | Routine venipuncture (blood draw)                             | Should be a small charge (~$5-$20) on its own line; sometimes inflated to $50-$100 |
| 49083        | Abdominal paracentesis with imaging guidance                  | Hospital outpatient procedure                                                      |
| 64483        | Lumbar epidural injection, single level                       | ~$400-$3,000                                                                       |
| 99151        | Moderate sedation by same physician, age 5+, first 15 minutes | Watch for unbundling with the underlying procedure                                 |
| 95810        | Polysomnography (sleep study)                                 | ~$1,000-$5,000                                                                     |
| 92002, 92004 | Eye exam, new patient                                         | ~$50-$300                                                                          |

## Surgical

| Code         | Description                                        |
| ------------ | -------------------------------------------------- |
| 27447        | Total knee replacement                             |
| 27130        | Total hip replacement                              |
| 27828, 27750 | Tibia fracture treatments                          |
| 33533        | Coronary artery bypass, single graft               |
| 44970        | Laparoscopic appendectomy                          |
| 47562        | Laparoscopic cholecystectomy (gallbladder removal) |
| 49585        | Repair of umbilical hernia                         |
| 64483        | Epidural injection                                 |
| 19120        | Excision of breast lesion                          |

Surgical procedures are where the chargemaster vs. negotiated-rate disparity is largest. Hospital chargemasters often show $100k+ for a procedure that the insurance contract pays $20-30k for. See `rules/05_negotiate_fair_price.md`.

## HCPCS Level II (supplies, drugs, ambulance, DME)

These are public-domain alphanumeric codes maintained by CMS.

### Ambulance

| Code  | Description                                                                    |
| ----- | ------------------------------------------------------------------------------ |
| A0425 | Ground mileage, per statute mile                                               |
| A0426 | Ambulance service, ALS, non-emergency transport                                |
| A0427 | Ambulance service, ALS, level 1 (emergency)                                    |
| A0428 | Ambulance service, BLS, non-emergency                                          |
| A0429 | Ambulance service, BLS, level 1 (emergency)                                    |
| A0430 | Ambulance service, conventional air services, transport, one way (fixed wing)  |
| A0431 | Ambulance service, conventional air services, transport, one way (rotary wing) |
| A0433 | Advanced life support, level 2                                                 |
| A0434 | Specialty care transport                                                       |

For ground-ambulance disputes, see `rules/10_ground_ambulance.md`. For air-ambulance, see `rules/22_air_ambulance.md`.

### Durable medical equipment

| Code  | Description                                           | Retail comparison                         |
| ----- | ----------------------------------------------------- | ----------------------------------------- |
| E0144 | Walker, enclosed, four-sided framed, rigid or folding | $100-$300 retail; bills often $400-$1,000 |
| E0143 | Walker, folding (pickup), adjustable or fixed height  | $30-$100 retail                           |
| E0260 | Hospital bed, semi-electric                           | Rental, but watch for purchase pricing    |
| K0001 | Standard wheelchair                                   | $200-$500 retail; bills often $1,000+     |
| L1832 | Knee orthosis, adjustable knee joints, off-the-shelf  | $50-$200 retail                           |
| L4360 | Walking boot, pneumatic, prefabricated, off-the-shelf | $40-$120 retail (e.g., Aircast SP)        |

Any DME charged by a hospital or hospital-affiliated supplier should be sanity-checked against retail prices on Amazon, medical-supply sites, or the equivalent product's manufacturer page.

### Drugs administered

J-codes are for drugs administered other than oral. Examples:

| Code  | Description                                                                      |
| ----- | -------------------------------------------------------------------------------- |
| J0696 | Injection, ceftriaxone sodium, per 250 mg                                        |
| J1100 | Injection, dexamethasone sodium phosphate, 1 mg                                  |
| J1885 | Injection, ketorolac tromethamine, per 15 mg                                     |
| J7050 | Infusion, normal saline solution, 250 cc                                         |
| J7613 | Albuterol, inhalation solution, FDA-approved final product, non-compounded, 1 mg |

Drugs administered in a hospital setting routinely cost 10-100× more than the same drug at retail. Patient cost-share on these can be substantial.

## CPT and HCPCS modifiers worth recognizing

| Modifier | Meaning                                                                         |
| -------- | ------------------------------------------------------------------------------- |
| -25      | Significant, separately identifiable E/M service on the same day as a procedure |
| -26      | Professional component (vs technical/facility)                                  |
| -50      | Bilateral procedure                                                             |
| -59      | Distinct procedural service                                                     |
| -91      | Repeat clinical diagnostic laboratory test                                      |
| -95      | Telehealth via real-time interactive audio and video                            |
| -93      | Telehealth audio-only                                                           |
| -GA      | Waiver of liability statement on file (Medicare ABN)                            |
| -GT      | Telemedicine via interactive audiovisual telecom (less common since 2017)       |
| -PO      | Excepted service provided at an off-campus outpatient department                |
| -PN      | Non-excepted service at an off-campus outpatient department                     |
| -TC      | Technical component (vs professional)                                           |

Modifier errors (missing -25 when a separately identifiable E/M is billed, missing -91 when a lab is appropriately repeated, etc.) can cause denials at the insurance side that leave the patient with an unadjudicated bill. The fix is usually a corrected claim from the provider, not a patient-side dispute.

## Place-of-service codes

| Code | Place                                                |
| ---- | ---------------------------------------------------- |
| 02   | Telehealth provided other than in the patient's home |
| 10   | Telehealth provided in the patient's home            |
| 11   | Office                                               |
| 21   | Inpatient hospital                                   |
| 22   | On-campus outpatient hospital                        |
| 19   | Off-campus outpatient hospital                       |
| 23   | Emergency room — hospital                            |
| 24   | Ambulatory surgical center                           |
| 31   | Skilled nursing facility                             |
| 32   | Nursing facility                                     |
| 81   | Independent lab                                      |

A common dispute: a service that was actually performed at the patient's home or via telehealth, but billed as POS 22 (on-campus outpatient hospital) to capture a facility fee. The facility fee can add hundreds to a single encounter.

## Where to look prices up

For specific patient-side dispute work, look up the patient's specific code(s) at one or more of:

- **Turquoise Health (patient-facing):** [turquoise.health/patients](https://turquoise.health/patients) — pulls from hospital MRFs
- **FAIR Health Consumer:** [fairhealthconsumer.org](https://www.fairhealthconsumer.org) — commercial-claims data
- **Healthcare Bluebook:** [healthcarebluebook.com](https://www.healthcarebluebook.com) — fair-price benchmarks
- **CMS Physician Fee Schedule Lookup:** the Medicare allowable rate
- **The hospital's own machine-readable file** (see `references/hpt_mrf_format.md` for what to look for)

## Related

- [[cpt_codes_em]] — Evaluation and Management code documentation requirements
- [[hpt_mrf_format]] — Hospital Price Transparency machine-readable file format and how to read one
- [[../rules/03_check_cpt_codes]] — methodology for verifying coding accuracy
- [[../rules/05_negotiate_fair_price]] — using these codes to anchor price negotiations
