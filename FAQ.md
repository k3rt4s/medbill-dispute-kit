# FAQ

## About the kit

**What is this kit, in one sentence?**

A pack of Markdown rules, TOML schemas, and letter templates you load into any large language model along with your medical bills, and it walks you through analyzing, deduplicating, and disputing them across the months-long process.

**Who is it for?**

US patients with one or more medical bills they suspect are wrong, unfair, or unaffordable. Also useful for friends or family helping someone else navigate medical bills. Not for outside-US bills, veterinary bills, or non-medical disputes.

**Do I need to write code or run anything?**

No. The kit is instruction-only. You upload the files to an LLM (Claude.ai, ChatGPT, Gemini, a local model — any with file upload) and tell it you want to dispute medical bills. The LLM does the work using the rules in the kit. The only optional code is a small Python tracker validator in `scripts/`.

**Is this legal advice?**

No. It is a structured way to apply public laws and well-documented consumer-protection patterns. If your dispute exceeds ~$10,000, involves suspected fraud, involves an injury claim, or you are uncomfortable proceeding alone, talk to a lawyer. Free 30-minute consultations are common via state bar referral services, and legal-aid organizations exist in every state.

**Why the open license?**

The methodology is Marshall Allen's, who died in 2024 and whose successor non-profit the [Marshall Allen Project](https://www.marshallallenproject.org/) continues the work. Surprise medical bills are a national problem. Free distribution of the tools is the point.

## Using the kit

**Which LLM should I use?**

Any of the major ones work. Claude or GPT with file upload and a long context window will handle the whole kit in one shot. See [`llm/compatibility.md`](llm/compatibility.md) for specifics. For very short-context models, use the staged load described in [`llm/QUICKSTART_short_context.md`](llm/QUICKSTART_short_context.md).

**Does my data leave my computer?**

That depends on the LLM you use. Cloud LLMs (Claude.ai, ChatGPT, Gemini) process your bills on their servers; check their privacy policies. Local LLMs (Ollama, LM Studio, llama.cpp) keep everything on your machine. The kit itself ships no telemetry and connects to nothing.

**What if I'm not in Tennessee or Georgia?**

The kit ships dedicated state packs for Tennessee, Georgia, California, Texas, New York, and Florida. For any other state, the LLM uses `references/laws_state_template.md` to find your state's equivalent statutes and warns you to verify before mailing. Contributing your state's pack as a PR is welcome.

**My bill is from a non-US provider. Will this work?**

No. The kit's rules and statutes are US-only.

## Common patient questions

**The bill due date is in 5 days. What do I do?**

Do not panic and do not pay. The due date on the bill is the provider's preferred date, not a legal deadline. Your actual deadline — the point at which the bill could become collectible or affect your credit — is typically 180+ days out under federal rules. You have time to verify the bill before paying.

**I missed the 30-day deadline for [itemization / FDCPA validation / something else]. What now?**

Most deadlines in the kit are "best practice" deadlines that increase your leverage, not statutes of limitations. Missing a 30-day window for FDCPA validation, for example, doesn't bar you from disputing the debt — it just means you don't get the automatic collection-pause that § 1692g provides. The dispute itself remains available. Tell the LLM what deadline you missed and it will route to the next-best path.

**The hospital sent me to collections. Is it too late to dispute?**

No. Collections doesn't change the underlying merits of the bill. If a third-party collector is now involved, use `templates/letter_fdcpa_validation.md` to demand verification from the collector while you continue disputing with the original provider. For credit-report effects, the 2022 voluntary bureau changes mean paid medical debt and sub-$500 collections are no longer reported.

**I already paid the bill. Can I still dispute it?**

Yes, but the leverage is lower. You're now seeking a refund rather than refusing payment. The same evidence applies; the timeline drags out because the provider has your money. For small amounts a refund is sometimes uneconomic to pursue; for larger amounts (no Surprises Act violations, clear coding errors, services not received), small claims court is still the realistic venue.

**My bill is for $50,000. Is small claims really the right venue?**

If the disputed amount is above your state's small-claims jurisdictional limit (Tennessee $25,000; Georgia $15,000; California $12,500; Texas $20,000; New York $5,000-$10,000; Florida $8,000), small claims is not available. Options: split the claim into separately-actionable parts if defensible, settle for an amount within the limit, or move to regular civil court with counsel.

**My insurer denied the whole claim. Now what?**

Different path from a billing dispute. Use `templates/letter_insurance_appeal_erisa.md` for ERISA-covered employer plans, `templates/letter_medicare_appeal.md` for Medicare, `templates/letter_medicaid_appeal.md` for Medicaid. Internal appeal first, then external review. State complaint in parallel. See [`rules/07_appeal_insurance_denial.md`](rules/07_appeal_insurance_denial.md).

**I can't afford the bill even at a fair price.**

Two paths. (1) For non-profit hospitals: apply for charity care under IRS § 501(r) using `templates/letter_financial_assistance_application.md`, and run the [Dollar For](https://dollarfor.org) screener. (2) For any provider: negotiate a hardship reduction using `templates/letter_hardship_negotiation.md`. Both can run in parallel. Neither requires admitting the original bill is correct.

**The doctor's billing department says I have to pay or they won't see me anymore.**

If this is a non-profit hospital and you have an open § 501(r) FAP application, denying future care while the application is pending is itself a violation of 26 CFR § 1.501(r)-6. For non-emergency outpatient relationships, you cannot be denied future care for an unpaid bill if you are working through the dispute process in good faith. For emergencies, EMTALA prohibits denial of stabilizing treatment regardless of bills. Document the threat and add it to a state attorney general complaint.

**My ambulance bill is $4,000. Is that protected by the No Surprises Act?**

If it was **air ambulance**, yes. If it was **ground ambulance**, federal NSA does **not** cover it. About a dozen states (CA, CO, DE, GA, IL, ME, MD, NY, OH, VT, WA) have closed the gap with state laws. See [`rules/10_ground_ambulance.md`](rules/10_ground_ambulance.md). Tennessee and Florida are not on the list.

## Process questions

**The hospital isn't responding to my dispute letter. How long should I wait?**

Send the initial dispute letter, give 15 business days for substantive response. If silence, send a follow-up referencing the prior letter. After 30 days total, escalate with the 30-day warning before small claims. CC the state insurance department, attorney general, and BBB. That usually breaks the silence; if not, file.

**Do I need a lawyer for small claims court?**

No. Small claims is specifically designed for self-represented parties. Many states even prohibit attorneys at the initial hearing (e.g., California). Bring the documents, present them chronologically, stick to facts. The kit's `rules/06_small_claims.md` covers preparation in detail.

**The provider settled for less than I demanded. Should I take it?**

Usually yes. A settlement at 60-70% of the disputed amount in 2-3 months beats spending another 6-12 months in small claims court for the remaining 30-40%. Get the settlement in writing. Have it state expressly that the settled amount discharges the entire account; otherwise the provider may try to bill the remainder later.

**What if I make my bill worse by complaining?**

Providers cannot lawfully retaliate against patients for filing complaints. Many states have explicit anti-retaliation provisions. In practice, billing departments rarely retaliate because the complaint creates a documented paper trail that strengthens the patient's position in any subsequent dispute. The risk is overwhelmingly upside.

**Can I just settle quickly to make this go away?**

You can, and sometimes it's the right call (especially for small amounts at the bottom of your priority list). But quick settlement without first asking for an itemization usually means paying inflated charges. At minimum, ask "is this the best you can do?" Most billing departments will reduce 20-40% on the first ask.

## Edge cases

**My bill is more than a year old. Is it still disputable?**

Likely yes. The relevant statute of limitations for the provider to collect from you ranges from 3-6 years depending on state. The dispute process can be initiated any time before that. Specific state-by-state details in the state packs.

**The provider went out of business. Where do I send the dispute?**

Send to the listed billing address; if returned, send to the registered agent of the corporate entity (look up at the secretary of state for the state of incorporation). If the practice was acquired by another entity, send to that successor; medical-bill obligations don't typically vanish with a sale.

**I have bills from a deceased family member. Am I liable?**

Generally no, unless you co-signed or you have a filial-responsibility statute applicable in your state (rare and rarely enforced). The estate is liable to the extent of assets. Heirs are not personally liable for the decedent's medical debt absent a contractual undertaking. Consult a probate attorney in your state if assets are at stake.

**The provider is on a payment plan with me and now is suing me.**

This is unusual and likely a clerical breakdown rather than intentional. Respond to the lawsuit on time (do not default), file an answer asserting the payment plan as an affirmative defense, attach documentation. If the dollar amount is small, small claims court is the venue. Consider filing a counterclaim under your state's UDAP statute for the trouble.

**Can I use the kit to help my parent / friend?**

Yes. The LLM doesn't care whose bills they are; you'll need their authorization (or Power of Attorney for a parent who can't act for themselves) for most communications to be effective. Letters can be signed by the patient and mailed by you, or signed by an authorized representative with appropriate authority documentation attached.

**My bill is wrong but the provider says they cannot change it because it's already been adjudicated by my insurance.**

A "the insurance already paid, we can't change it" response is almost never accurate. The provider can always issue a corrected claim and refund any insurance overpayment. The patient-side leverage: refuse to pay the disputed portion, document the request for correction, escalate via state insurance department complaint if the provider insists on a wrong bill.

## Contributing

**I'd like to add my state's pack. How?**

Use `references/laws_state_template.md` as the checklist and follow the structure of `laws_state_tn.md` through `laws_state_fl.md` as templates. Source every citation with a URL. Include the verification date in the file header. PR to [github.com/k3rt4s/medbill-dispute-kit](https://github.com/k3rt4s/medbill-dispute-kit). See [`CONTRIBUTING.md`](CONTRIBUTING.md).

**I found a bug in a rule or template.**

Open an issue at the GitHub repo with as much detail as you can — what the rule/template says, what the correct content should be, the source URL for the corrected information. PRs welcome.

**I have a real-world dispute outcome I'd like to share.**

Strip personally identifying information first. Then either open an issue describing the pattern (without names) or PR an example into `examples/`. Outcomes data helps future patients calibrate.
