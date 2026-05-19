# Start here

A copy-paste quickstart for the patient who just landed on this repo and wants to dispute a medical bill tonight. If you have ten minutes and a stack of bills, this page is your runway.

## What this kit does

You upload medical bills to an LLM (Claude, ChatGPT, Gemini, or a local model). Loaded with this kit's instruction files, the LLM extracts the bills into a tracking spreadsheet, deduplicates follow-up statements, identifies issues (No Surprises Act violations, upcoded ER visits, services not received, price gouging), and drafts the dispute letters for you. You carry the tracker forward across sessions over the months-long process.

Not legal advice. A structured way to apply public laws.

## The three-minute setup

1. **Pick an LLM.** Claude (claude.ai) and ChatGPT (chat.openai.com) handle this kit cleanly. Gemini (gemini.google.com) also works. For privacy, a local model like Llama 3.3 70B with vision works but takes more horsepower.
2. **Clone or download this repo.** `git clone https://github.com/k3rt4s/medbill-dispute-kit.git` or download as ZIP from GitHub.
3. **Start a new conversation with your LLM.** Upload the kit files.

## What to upload

For long-context LLMs (Claude Opus, Claude Sonnet 4.6+, GPT-5, Gemini 2.5 Pro), upload everything:

- All files in [`llm/`](../llm/)
- All files in [`rules/`](../rules/)
- All files in [`references/`](../references/) — but if your state has a dedicated pack, you only need that one state file plus `laws_federal.md` plus `cpt_codes_em.md` plus `resources.md` plus `glossary.md`
- All files in [`schemas/`](../schemas/)
- All files in [`templates/`](../templates/)
- [`tracker/tracker_template.csv`](../tracker/tracker_template.csv) and [`tracker/tracker_columns.md`](../tracker/tracker_columns.md)

For short-context LLMs, follow [`llm/QUICKSTART_short_context.md`](../llm/QUICKSTART_short_context.md).

## The opening prompt

Paste this into the conversation after uploading:

> I want to dispute medical bills. I'm in [STATE]. Please read the system prompt and workflow files I uploaded. Then ask me what I want to do this session.

The LLM will read the files, confirm your state, and ask whether you're starting fresh or resuming with an existing tracker.

## Common first scenarios

### "I just got a stack of bills and don't know where to start"

Upload them all (photos or PDFs are fine). Tell the LLM:

> I'm starting fresh. Here are [N] bills I want to triage.

The LLM walks you through Phase 1 (intake) and Phase 2 (diagnosis) before asking which to dispute first.

### "I got a bill that seems way too high"

Upload the bill. Tell the LLM:

> I think this bill is wildly overpriced. Help me figure out what a fair price would be and draft a dispute letter.

The LLM will diagnose the bill, point you at the right transparency tools to look up fair pricing, and draft the letter.

### "My insurance denied a claim"

Upload the bill and the denial letter. Tell the LLM:

> My insurance denied this claim. Help me appeal.

The LLM will identify your plan type (ERISA, Medicare, Medicaid, individual market, etc.) — the very first move in any denial appeal — and route to the right appeal track.

### "A debt collector is calling me about a medical bill"

Upload the collector's letter. Tell the LLM:

> I received this letter from a debt collector less than 30 days ago. Help me respond.

The LLM will draft an FDCPA § 1692g validation request that forces the collector to either prove the debt or stop collecting.

### "I want to apply for hospital financial assistance"

Tell the LLM:

> This is a bill from a non-profit hospital. I think I qualify for charity care.

The LLM will draft an IRS § 501(r) Financial Assistance Policy application letter that triggers the hospital's federal obligation to suspend collection action while your eligibility is reviewed. It will also point you at Dollar For (dollarfor.org), a free non-profit that handles the entire process.

### "I have an old bill that's been overdue for months"

Tell the LLM:

> I've been getting bills for [N] months and ignoring them. Now what?

The LLM will check whether the bill has been sent to collections, calculate your statute-of-limitations clock for your state, and recommend a path forward.

### "I'm in financial hardship and just can't pay"

Tell the LLM:

> The bill is correctly coded but I can't afford it. What are my options?

The LLM will route you to (a) hospital financial-assistance applications for non-profit hospitals, (b) general hardship-negotiation letters anchored to Medicare allowable rates, and (c) for severe cases, a referral to consider bankruptcy.

## At the end of every session

Tell the LLM:

> Save my progress.

The LLM produces a complete tracker CSV. Save it to your computer (e.g., `tracker_2026-05-18.csv`). Next session, upload it first and the LLM will pick up where you left off.

## What you'll need

- **Original bills.** Photos, PDFs, or pasted text all work.
- **Explanation of Benefits (EOB) from your insurance** if you have insurance. Most plans let you download EOBs from the member portal.
- **Your insurance ID card** to confirm the plan name and (for employer plans) whether it's self-funded or fully insured.
- **Pen, certified-mail envelopes, $5-$15 per letter.** Almost every dispute letter goes via USPS Certified Mail with Return Receipt for the paper trail. Some libraries print certified-mail labels for free.

## What to keep on your computer

A folder per dispute. Suggested structure:

```text
medical-disputes/
├── tracker_2026-05-18.csv          # latest version
├── tracker_archive/                # older versions
├── bills/                          # photos/PDFs of bills (do not commit anywhere)
├── letters/                        # drafted and mailed letters
├── responses/                      # provider/insurer responses
└── evidence/                       # screenshots of fair-market prices, EOBs, etc.
```

Do not put this folder in a public cloud-sync without encryption. These contain PII.

## State packs currently shipped

Tennessee, Georgia, California, Texas, New York, Florida, Pennsylvania, Illinois, Ohio, North Carolina, Michigan, Washington, New Jersey, Virginia, Arizona, Massachusetts. If your state isn't on this list, the kit uses [`references/laws_state_template.md`](../references/laws_state_template.md) to look up your state's statutes — with a warning to verify the citations before mailing.

If you'd like to contribute your state's pack, see [CONTRIBUTING.md](../CONTRIBUTING.md).

## When to call a lawyer

The kit's posture: most disputes under $10,000 are handled fine self-service. Above that, talk to a lawyer. Specifically:

- **Any dispute over $10,000.** Free 30-minute consultations are common via state bar referral services.
- **ERISA insurance denials.** The internal-appeal record locks in; a lawyer at the right stage makes a big difference.
- **EMTALA civil action.** Two-year statute of limitations; counsel needed for the federal claim.
- **Suspected fraud or unauthorized practice.** Criminal referral and counsel needed.
- **Bankruptcy.** Trivial Chapter 7s can be self-filed via [Upsolve](https://upsolve.org). Everything else needs a bankruptcy attorney.

## When the LLM is being dumb

LLMs are imperfect. The kit's [`llm/compatibility.md`](../llm/compatibility.md) describes behaviors to watch for. Common ones:

- **Cites the wrong state's statute.** Paste your state pack again and tell the LLM to use only that state's citations.
- **Won't draft "legalistic" language.** Paste the relevant template directly and tell the LLM to render it with your facts.
- **Forgets context.** Save your tracker, start a new conversation, re-upload.
- **Makes up URLs or statute numbers.** Cross-check anything that looks doubtful. The kit's references are sourced; the LLM's improvisation is not.

## Where to ask for help

- **[FAQ.md](../FAQ.md)** — common patient questions.
- **GitHub Issues:** [github.com/k3rt4s/medbill-dispute-kit/issues](https://github.com/k3rt4s/medbill-dispute-kit/issues). Bugs in the kit, requests for new state packs, content corrections.
- **State-specific patient-advocacy resources:** see [`references/resources.md`](../references/resources.md).
- **For Medicare**: [shiphelp.org](https://www.shiphelp.org) — free SHIP counselor in every state.
- **For ERISA self-funded plans**: DOL EBSA at 1-866-444-3272, free informal intervention.

## What this kit will not do

- File a lawsuit for you.
- Talk to a billing department on your behalf.
- Guarantee any specific dispute outcome.
- Cover bills outside the US.
- Cover veterinary, dental-only-cosmetic, or non-medical bills.

What it will do is structure the dispute process so you know what to do next and why.

## One more thing

Almost every bill you contest will produce some movement. Even when the dispute does not eliminate the bill entirely, it usually produces a meaningful reduction. The system bets you won't push back. Pushing back is most of the work.
