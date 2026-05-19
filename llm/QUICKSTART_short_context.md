# Quickstart — short-context LLMs

If your LLM has under 32k tokens of context, you cannot load the entire kit in one shot. Use this staged-load pattern instead.

This applies to: smaller local models (Llama 3 8B, Mistral 7B variants), older chatbot interfaces with truncated context, mobile LLM apps with size limits.

## Stage 1 — Boot

Load these three files and tell the model to follow the system prompt. Total: ~15k tokens.

1. [`llm/system_prompt.md`](system_prompt.md)
2. [`llm/workflow.md`](workflow.md)
3. [`rules/00_principles.md`](../rules/00_principles.md)

Tell the model:

> Read these three files. The system prompt defines your role; the workflow is the end-to-end process; the principles are the foundation. Once you've read them, ask me what state I'm in and what I want to do.

## Stage 2 — State pack

The model asks your state. Load the relevant state file:

- Tennessee: [`references/laws_state_tn.md`](../references/laws_state_tn.md)
- Georgia: [`references/laws_state_ga.md`](../references/laws_state_ga.md)
- California: [`references/laws_state_ca.md`](../references/laws_state_ca.md)
- Texas: [`references/laws_state_tx.md`](../references/laws_state_tx.md)
- New York: [`references/laws_state_ny.md`](../references/laws_state_ny.md)
- Florida: [`references/laws_state_fl.md`](../references/laws_state_fl.md)
- Pennsylvania: [`references/laws_state_pa.md`](../references/laws_state_pa.md)
- Illinois: [`references/laws_state_il.md`](../references/laws_state_il.md)
- Ohio: [`references/laws_state_oh.md`](../references/laws_state_oh.md)
- North Carolina: [`references/laws_state_nc.md`](../references/laws_state_nc.md)
- Michigan: [`references/laws_state_mi.md`](../references/laws_state_mi.md)
- Washington: [`references/laws_state_wa.md`](../references/laws_state_wa.md)
- New Jersey: [`references/laws_state_nj.md`](../references/laws_state_nj.md)
- Virginia: [`references/laws_state_va.md`](../references/laws_state_va.md)
- Arizona: [`references/laws_state_az.md`](../references/laws_state_az.md)
- Massachusetts: [`references/laws_state_ma.md`](../references/laws_state_ma.md)
- Colorado: [`references/laws_state_co.md`](../references/laws_state_co.md)
- Maryland: [`references/laws_state_md.md`](../references/laws_state_md.md)
- Missouri: [`references/laws_state_mo.md`](../references/laws_state_mo.md)
- Minnesota: [`references/laws_state_mn.md`](../references/laws_state_mn.md)
- Indiana: [`references/laws_state_in.md`](../references/laws_state_in.md)
- Wisconsin: [`references/laws_state_wi.md`](../references/laws_state_wi.md)
- South Carolina: [`references/laws_state_sc.md`](../references/laws_state_sc.md)
- Alabama: [`references/laws_state_al.md`](../references/laws_state_al.md)
- Kentucky: [`references/laws_state_ky.md`](../references/laws_state_ky.md)
- Oregon: [`references/laws_state_or.md`](../references/laws_state_or.md)
- Oklahoma: [`references/laws_state_ok.md`](../references/laws_state_ok.md)
- Connecticut: [`references/laws_state_ct.md`](../references/laws_state_ct.md)
- Utah: [`references/laws_state_ut.md`](../references/laws_state_ut.md)
- Iowa: [`references/laws_state_ia.md`](../references/laws_state_ia.md)
- Nevada: [`references/laws_state_nv.md`](../references/laws_state_nv.md)
- Arkansas: [`references/laws_state_ar.md`](../references/laws_state_ar.md)
- Kansas: [`references/laws_state_ks.md`](../references/laws_state_ks.md)
- Mississippi: [`references/laws_state_ms.md`](../references/laws_state_ms.md)
- New Mexico: [`references/laws_state_nm.md`](../references/laws_state_nm.md)
- Nebraska: [`references/laws_state_ne.md`](../references/laws_state_ne.md)
- Other: load [`references/laws_state_template.md`](../references/laws_state_template.md) and ask the model to look up your state's equivalents (warn it to verify before mailing).

Also load: [`references/laws_federal.md`](../references/laws_federal.md).

## Stage 3 — Bill ingest

Load: [`schemas/bill.toml`](../schemas/bill.toml), [`schemas/deduplication_rules.toml`](../schemas/deduplication_rules.toml).

Then upload your bills. The model should produce a TOML record per bill conforming to `schemas/bill.toml`.

If you're returning from a prior session, upload your `tracker.csv` and [`schemas/tracker.toml`](../schemas/tracker.toml) first. The model will summarize open actions.

## Stage 4 — Diagnosis

For each bill, load the rule that matches the model's preliminary finding:

- No itemization → load [`rules/02_request_itemization.md`](../rules/02_request_itemization.md)
- Possible upcoding → load [`rules/03_check_cpt_codes.md`](../rules/03_check_cpt_codes.md) and [`references/cpt_codes_em.md`](../references/cpt_codes_em.md)
- No Surprises Act candidate → load [`rules/04_no_surprises_act.md`](../rules/04_no_surprises_act.md)
- Price gouging → load [`rules/05_negotiate_fair_price.md`](../rules/05_negotiate_fair_price.md) and [`rules/09_pricing_resources.md`](../rules/09_pricing_resources.md)
- Ground ambulance → load [`rules/10_ground_ambulance.md`](../rules/10_ground_ambulance.md)
- PPDR-eligible → load [`rules/11_ppdr_walkthrough.md`](../rules/11_ppdr_walkthrough.md)
- Insurance denial → load [`rules/07_appeal_insurance_denial.md`](../rules/07_appeal_insurance_denial.md)
- Medicare denial → load [`rules/12_medicare_appeals.md`](../rules/12_medicare_appeals.md)
- EMTALA / emergency-care refusal → load [`rules/13_emtala.md`](../rules/13_emtala.md)
- HIPAA records-access denial → load [`rules/14_hipaa_right_of_access.md`](../rules/14_hipaa_right_of_access.md)
- Accident-related billing → load [`rules/15_auto_med_pay.md`](../rules/15_auto_med_pay.md)
- Work-related injury → load [`rules/16_workers_comp.md`](../rules/16_workers_comp.md)
- Bankruptcy candidate → load [`rules/17_bankruptcy_and_medical_debt.md`](../rules/17_bankruptcy_and_medical_debt.md)
- TRICARE → load [`rules/18_tricare.md`](../rules/18_tricare.md)
- VA Community Care → load [`rules/19_va_community_care.md`](../rules/19_va_community_care.md)
- Telehealth visit → load [`rules/20_telehealth.md`](../rules/20_telehealth.md)
- Section 1557 / civil-rights angle → load [`rules/21_section_1557.md`](../rules/21_section_1557.md)
- Air ambulance → load [`rules/22_air_ambulance.md`](../rules/22_air_ambulance.md)
- ACA marketplace plan denial → load [`rules/23_aca_marketplace.md`](../rules/23_aca_marketplace.md)
- Medicare observation-status issue → load [`rules/24_observation_status.md`](../rules/24_observation_status.md)
- Third-party collector → no extra rule needed; go to Stage 5 with the FDCPA template.

## Stage 5 — Draft

For each action the workflow chooses, load only that template:

| Action                     | Template                                               |
| -------------------------- | ------------------------------------------------------ |
| Request itemization        | `templates/letter_itemization_request.md`              |
| Initial dispute            | `templates/letter_initial_dispute.md`                  |
| 30-day warning             | `templates/letter_30day_warning.md`                    |
| No Surprises Act violation | `templates/letter_no_surprises_violation.md`           |
| ERISA appeal               | `templates/letter_insurance_appeal_erisa.md`           |
| Medicare appeal            | `templates/letter_medicare_appeal.md`                  |
| Medicaid appeal            | `templates/letter_medicaid_appeal.md`                  |
| Dental dispute             | `templates/letter_dental_dispute.md`                   |
| Hardship negotiation       | `templates/letter_hardship_negotiation.md`             |
| FDCPA validation           | `templates/letter_fdcpa_validation.md`                 |
| FAP application            | `templates/letter_financial_assistance_application.md` |
| Ground-ambulance dispute   | `templates/letter_ground_ambulance.md`                 |
| State insurance complaint  | `templates/complaint_state_doi.md`                     |
| CMS HPT complaint          | `templates/complaint_cms_hpt.md`                       |
| EMTALA complaint           | `templates/complaint_emtala.md`                        |
| HIPAA right-of-access OCR  | `templates/complaint_hipaa_access.md`                  |
| Auto med-pay (3 variants)  | `templates/letter_auto_med_pay.md`                     |

Plus: [`llm/output_contracts.md`](output_contracts.md) for the rendering format.

The model produces the letter. Review it, give feedback, iterate.

## Stage 6 — Save state

Load: [`schemas/tracker.toml`](../schemas/tracker.toml), [`tracker/tracker_columns.md`](../tracker/tracker_columns.md).

Tell the model: "Emit the complete tracker as a CSV per the schema. Tell me what filename to save it as."

Save the CSV to your computer.

## Stage 7 — Resume next time

Next session, load:

1. `llm/system_prompt.md`
2. `llm/workflow.md`
3. Your saved `tracker.csv`
4. Your state pack
5. `references/laws_federal.md`

Tell the model: "Read the tracker. Tell me what's overdue, what's due in the next 7 days, and the next action."

Then resume from Stage 4 for whichever bill is up.

## Tips

- **Don't try to skip stages.** Small models lose track when fed too much in one prompt. Stage-by-stage is slower but more reliable.
- **One bill at a time** if the model is small. Big models can multiplex multiple bills; small ones struggle.
- **Save trackers compulsively.** Even mid-session if you're worried about losing state. The tracker is the durable record.
- **Don't expect the model to learn between sessions.** Without the tracker re-loaded, every session is fresh.
- **If the model gets confused**, paste the workflow.md file again and tell it to follow it strictly.
