# LLM compatibility notes

The kit works with any reasonably capable LLM. This file describes what to expect from major models and how to adapt the load pattern when the model has constraints.

Last verified: 2026-05-18. Model capabilities change frequently; if anything below feels stale, trust the model's current documentation over this file.

## What the kit needs from the LLM

| Capability                         | Required?          | Why                                                                                         |
| ---------------------------------- | ------------------ | ------------------------------------------------------------------------------------------- |
| File upload (images, PDFs, text)   | Yes                | Bills come in as photos, PDFs, or pasted statements                                         |
| Vision (OCR + reasoning on images) | Strongly preferred | Phone photos of paper bills are the most common input                                       |
| Long context (≥ 64k tokens)        | Strongly preferred | Full kit + tracker + multiple bills together                                                |
| Reasoning ability                  | Yes                | The dedup logic, CPT severity check, and No Surprises Act flow require multi-step reasoning |
| Markdown output                    | Yes                | Letter rendering and tracker CSV emission                                                   |
| Code-block fidelity                | Yes                | CSV and TOML round-trip through the conversation                                            |

## Recommended: long-context cloud models

These can hold the whole kit plus your bills in a single conversation without staging.

### Claude (claude.ai)

- **Models:** Claude Sonnet 4.6, Claude Opus 4.7. Both work well.
- **Context window:** 200k tokens standard, 1M tokens on Opus 4.7 (long-context tier).
- **File upload:** images, PDFs, plain text, code. Drag-and-drop or paste.
- **Vision:** strong. Reads paper bills, photos of EOBs, scanned PDFs.
- **Strengths:** careful with the workflow, follows output contracts well, good at citing reasons.
- **Caveats:** session-only memory by default. Save the tracker to your own files between sessions and re-upload.

### ChatGPT (chat.openai.com)

- **Models:** GPT-5, GPT-5 Pro for higher-quality reasoning.
- **Context window:** 128k-200k tokens depending on model.
- **File upload:** images, PDFs, documents. Strong vision.
- **Strengths:** broad knowledge of US regulations, fast.
- **Caveats:** has a habit of helpful summarization where you want verbatim citations; remind it to cite rule files by name.

### Gemini (gemini.google.com)

- **Models:** Gemini 2.5 Pro, Gemini 3.
- **Context window:** 1M-2M tokens on Pro and Ultra tiers — largest available.
- **File upload:** images, PDFs, native Google Drive integration.
- **Strengths:** the longest context, useful if you're carrying months of history.
- **Caveats:** sometimes less precise on legal citation than Claude or GPT. Cross-check citations.

## Local / open-source models

These run on your machine. Privacy advantage: your bills never leave your computer. Performance trade-off: depending on model size and your hardware, may be slower or less accurate than cloud models.

### Llama 3.1 / 3.3 (70B and larger)

- **Tooling:** Ollama, LM Studio, llama.cpp.
- **Context window:** 128k tokens on 3.1/3.3.
- **File handling:** depends on the front-end. LM Studio and Open WebUI handle file upload; raw llama.cpp does not.
- **Vision:** Llama 3.2 Vision (11B and 90B) handles images; text-only Llama variants do not.
- **Best for:** users who want full local privacy and have at least 64 GB of RAM (for 70B at q4) or a serious GPU.

### Qwen 2.5 / 3 (72B and larger)

- **Tooling:** Ollama, vLLM.
- **Context window:** 32k-128k depending on variant.
- **Vision:** Qwen-VL models for images.
- **Strengths:** competitive with Llama on legal reasoning, strong multilingual.

### Smaller local models (7B-13B)

- Generally underpowered for this kit. They will follow basic instructions but miss nuance on No Surprises Act routing, CPT severity, or multi-bill deduplication.
- If you must use a small local model, switch to the short-context load pattern in `QUICKSTART_short_context.md` and accept that you'll guide the model more actively.

## What about Gemini in Google Workspace, Copilot in 365, ChatGPT in Outlook?

These embedded variants typically have shorter context limits and less reliable file-handling than the standalone product. Workable for short questions but not recommended for running the full kit.

## Adapting to context size

| Context window   | Strategy                                                                                                                                                |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1M+ tokens       | Load everything up front. No staging needed.                                                                                                            |
| 200k tokens      | Load everything; do not add long PDFs of plan documents in the same conversation as the kit                                                             |
| 100k tokens      | Load `llm/`, all of `rules/`, all of `schemas/`, your state pack, `references/laws_federal.md`. Load templates and the rest of `references/` on demand. |
| 32k tokens       | Use the staged load in `QUICKSTART_short_context.md`.                                                                                                   |
| Under 32k tokens | Not recommended. Use a different model.                                                                                                                 |

## Behaviors to watch for

### The model tries to summarize legal citations

Tell it: "Cite the exact statute as it appears in the state pack. Do not paraphrase legal citations." Repeat as needed; this drift is common across all major models.

### The model invents URLs

Some models will fabricate URLs that look plausible but don't resolve. Always cross-check any URL the model emits, especially for state-statute citations.

### The model "knows" the deadline

Models will sometimes apply outdated deadlines (e.g., pre-2022 No Surprises Act rules). Treat dates in the kit's rule and reference files as authoritative over the model's general knowledge.

### The model adapts the tracker schema

The schemas in `schemas/*.toml` are precise. If the model emits a tracker CSV with renamed columns or different value formats, point it back to the schema. The kit's value comes from clean round-trips.

### The model refuses an emergency action

Some models will hedge on small-claims threats, refuse to draft what they consider "legalistic" language, or insert excessive disclaimers. The kit's letter templates are based on public consumer-protection patterns; the model is permitted to follow them. If the model balks, paste the template and say "render this letter using my facts."

## Privacy considerations

- **Cloud LLMs:** read each provider's privacy policy. Most enterprise/team tiers offer "no training on your data" guarantees. Free tiers often do not.
- **Bill images:** they contain PII (your name, address, MBI, account numbers, sometimes diagnoses). Treat accordingly.
- **Trackers between sessions:** store them with the same care as your bank statements. The kit's `.gitignore` excludes them by default.
- **Letter drafts:** PII-rich. Keep them on your local machine or your password-protected cloud storage, not in shared / public locations.

## When to switch models mid-process

- If your current model is missing context or getting confused, save your tracker, summarize the open actions, and start fresh with a different model. The tracker CSV is portable.
- For high-stakes legal letters (small claims, ERISA appeal at $5,000+, federal court), consider running the same draft through two different models and comparing. Where they agree, trust. Where they differ, dig in.
