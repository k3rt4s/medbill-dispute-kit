# medbill-dispute-kit

An LLM-droppable instruction toolkit for analyzing US medical bills, deduplicating follow-up statements, and running a months-long dispute process with letters, complaints, and a tracking spreadsheet that you carry between sessions.

The ruleset is built primarily from Marshall Allen's *Never Pay the First Bill* (Portfolio, 2021) and his reporting at ProPublica, plus the federal No Surprises Act, the CMS Hospital Price Transparency Rule, ERISA appeal rights, UCC § 2-305, and state-level consumer protections. See [references/](references/) for the full citation list.

## What this is

A pack of Markdown rules, TOML schemas, and letter templates that you load into any large language model (Claude, GPT, Gemini, a local model) along with one or more medical bills. The model uses the rules to:

1. Read your uploaded bills (photos, PDFs, statements, EOBs)
2. Deduplicate, because most "new" bills are follow-up statements for the same charge
3. Produce an organized tracking spreadsheet you download, edit, and re-upload across the months-long process
4. For each bill, recommend the next concrete action: request itemization, check CPT severity coding, dispute the charge, file a state complaint, draft an ERISA appeal, or escalate to small claims
5. Draft the letter or complaint for you, citing the actual law that applies to your situation

This repo is the instruction layer. It does not run code. You drop these files into your LLM of choice and let the model do the work.

## Quick start

1. Clone or download this repo.
2. Open your LLM (Claude.ai, ChatGPT, a local model with file upload, etc.) and start a new conversation.
3. Upload `llm/system_prompt.md`, every file under `rules/`, every file under `references/`, every file under `schemas/`, every file under `templates/`, and `tracker/tracker_template.csv`. For long-context models, all of it fits in one shot. For shorter-context models, follow the prompts in [llm/system_prompt.md](llm/system_prompt.md) for a staged load.
4. Tell the model "I want to dispute medical bills" and upload your first bill image or PDF.
5. The model will follow [llm/workflow.md](llm/workflow.md): extract the bill into the tracker, deduplicate against prior statements, recommend the next action, and offer to draft the letter.
6. Download the updated tracker after each session. Re-upload it next time alongside any new statements you've received.

A worked walkthrough lives at [llm/workflow.md](llm/workflow.md).

## What's in the box

| Folder                       | What it holds                                                                                                                            | Who uses it                               |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| [`llm/`](llm/)               | Top-level prompt, end-to-end workflow, and output contracts                                                                              | The LLM you're driving                    |
| [`rules/`](rules/)           | The principles and tactics extracted from Allen's work, one rule per file                                                                | The LLM, as its operating manual          |
| [`references/`](references/) | Federal laws, dedicated state packs (TN, GA, CA, TX, NY, FL), state-law template for new states, CPT codes, glossary, external resources | The LLM, when it needs to cite something  |
| [`schemas/`](schemas/)       | TOML schemas describing bill records, tracker rows, dispute actions, and dedup logic                                                     | The LLM, when producing structured output |
| [`templates/`](templates/)   | Letter and complaint templates with placeholders                                                                                         | The LLM, when drafting correspondence     |
| [`tracker/`](tracker/)       | Downloadable CSV tracker plus column dictionary                                                                                          | You, between sessions                     |
| [`examples/`](examples/)     | Worked-example sessions showing the kit handling real bill patterns                                                                      | You, before your first session            |
| [`scripts/`](scripts/)       | Optional helpers (currently: a Python tracker-CSV validator)                                                                             | You, optionally, between sessions         |

State packs currently shipped: [Tennessee](references/laws_state_tn.md), [Georgia](references/laws_state_ga.md), [California](references/laws_state_ca.md), [Texas](references/laws_state_tx.md), [New York](references/laws_state_ny.md), [Florida](references/laws_state_fl.md). For any other state, the LLM uses [`references/laws_state_template.md`](references/laws_state_template.md) to find your state's equivalents (with a warning to verify before mailing). Contributing a state pack is the single most useful PR — see [CONTRIBUTING.md](CONTRIBUTING.md).

Letter templates currently shipped: itemized-bill request, initial dispute, 30-day warning before small claims, No Surprises Act violation, ERISA insurance appeal, state insurance department complaint, hardship negotiation (for correctly-billed but unaffordable charges), FDCPA § 1692g validation request (for third-party collectors), ground-ambulance dispute (federal NSA doesn't cover this; two variants by state law), IRS § 501(r) Financial Assistance application (for non-profit hospital bills), CMS Hospital Price Transparency complaint (for hospitals that won't publish their MRF), Medicare appeal (Levels 1 and 2 for Parts A/B/C/D), Medicaid appeal (MCO internal plus state fair hearing, TennCare worked example), and dental insurance dispute (downcoding, bundling, frequency-limit denials). Process walkthroughs for federal Patient-Provider Dispute Resolution and the five-level Medicare appeal structure live in [`rules/`](rules/).

Supporting documentation: [`FAQ.md`](FAQ.md) for common patient questions, [`references/glossary.md`](references/glossary.md) for the alphabet soup, [`llm/compatibility.md`](llm/compatibility.md) for model-specific guidance, and [`llm/QUICKSTART_short_context.md`](llm/QUICKSTART_short_context.md) for LLMs under 32k tokens.

## The methodology in one paragraph

Most US medical bills contain errors. Hospitals and insurers price-discriminate aggressively and rely on patients not contesting the bill. Federal law (No Surprises Act, ERISA appeal rights, the Hospital Price Transparency Rule) and state law (itemized-bill statutes, unfair claims practices acts) give patients real leverage, but only if used in the right order and with the right paper trail. This kit captures that order — request itemization → verify CPT coding → check for No Surprises Act violations → negotiate at fair market rate → escalate through state complaint → small claims — and stocks the templates needed at each step.

## Why this exists

Marshall Allen spent fifteen years documenting how the US healthcare system charges people and concluded that the single highest-leverage thing patients can do is stop paying the first bill until they've checked it. He died May 19, 2024; his successor nonprofit, the [Marshall Allen Project](https://www.marshallallenproject.org/), continues the work. This repo turns the playbook he left behind into something an LLM can run alongside you.

## Limits and disclaimers

This is not legal advice. It is a structured way to apply public laws and well-documented consumer-protection patterns to medical billing disputes. The state-law layer ships with Tennessee and Georgia fully worked out; for other states the kit guides the LLM to look up your state's equivalents using the patterns in [references/laws_state_template.md](references/laws_state_template.md). If your dispute involves more than ~$10,000, suspected fraud, or potential malpractice, talk to a lawyer. Free 30-minute consultations are common, and legal-aid organizations exist in every state.

The kit is jurisdictionally US-only.

## Contributing

PRs welcome, particularly:

- State-specific law packs analogous to the Tennessee worked example
- Additional letter templates (collections disputes under the FDCPA, hospital financial-assistance applications under § 501(r), Good Faith Estimate disputes, etc.)
- Schema improvements to the tracker
- Real-world dedup edge cases that the LLM gets wrong

Keep this repo free of personally identifying information. Examples should use synthetic or clearly fictionalized patient data.

## License

MIT. See [LICENSE](LICENSE).

## Credits

- Marshall Allen, *Never Pay the First Bill*, Portfolio/Penguin Random House, 2021. Allen's published reporting at ProPublica, including the Surgeon Scorecard project, informs much of the ruleset.
- Lori Todd, the "Insurance Warrior," whose appeal-letter format Allen credits and which informs [templates/letter_insurance_appeal_erisa.md](templates/letter_insurance_appeal_erisa.md).
- *All The Hacks* podcast with Chris Hutchins, episode "Hacking Healthcare" with Marshall Allen, which is the proximate source for the worked examples in this kit.
