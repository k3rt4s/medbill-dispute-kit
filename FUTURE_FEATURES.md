# Future features

Engineering-language backlog of work not yet scheduled. Sits under [USER_STORIES.md](USER_STORIES.md) (the user-value master) and [BUILD_PLAN.md](BUILD_PLAN.md) (the shipped-work tracker). When an item here is ready to ship, it moves into BUILD_PLAN.md with a version target and gets a corresponding story in USER_STORIES.md.

Items here are not promises. The kit is open-source; contributors are welcome to pick any of these up. Each item lists the rough shape of the work, the kit components that would change, and a one-line note on why it has not shipped yet.

---

## Scored index

No unshipped features remained as of 2026-09-08; two token-cost items were added 2026-10-02, listed at the end of the Scored index. The final two vendor-gated ideas, Turquoise Health API integration and Dollar For screener integration, were deleted because both require external vendor permission or confirmation before there is actionable project work.

Added 2026-10-02 from the workspace token audit, two cost items:

- **mb-ocr-whitespace-collapse**, Collapse OCR sidecar whitespace before the 80k cut. `scripts/index_bills_and_claims.py` `call_vision_text` (about lines 300-306) sends `body[:80_000]` from `read_sidecar_body` (about lines 218-227) to Azure OpenAI with no whitespace collapse, so OCR layout runs of spaces and blank lines are billed and also push real content past the 80k cut. Fix: `body = re.sub(r"[ \t]+", " ", re.sub(r"\n{3,}", "\n\n", body))` before slicing. Estimate 5 to 15 percent of body tokens per bill and EOB sidecar. Source: workspace token audit 2026-10-02 (read-only code review); savings are estimates, not measured, so measure on real inputs before and after.
  `score: kind=cost gain=0.05/0.1/0.3 hours=0.25/0.5/1 p=0.7 rev=two-way conf=opinion id=mb-ocr-whitespace-collapse`
  `return: likelihood high that sidecars carry layout whitespace runs, estimated from code reading only, no sidecar measured; impact 5 to 15 percent fewer body tokens per bill and EOB call, plus less content lost past the 80k cut; evidence the cited lines, no changelog entry`
  - worker: haiku 0.25/0.5/1 h
- **mb-fallback-request-compact**, Compact the parse_990 and parse_sbc fallback requests. `scripts/parse_990.py` (about lines 189 and 200) and `scripts/parse_sbc.py` (about lines 191 and 215) send `json.dumps(request)` holding whole uncollapsed PDF page text; default `ensure_ascii=True` turns bullets, smart quotes and section signs into `\uXXXX` escapes that cost more tokens. Fix: collapse page whitespace and use `json.dumps(request, ensure_ascii=False, separators=(",", ":"))`. Estimate 5 to 15 percent, fallback path only. Source: workspace token audit 2026-10-02 (read-only code review); savings are estimates, not measured, so measure on real inputs before and after.
  `score: kind=cost gain=0.02/0.05/0.2 hours=0.25/0.5/1 p=0.7 rev=two-way conf=opinion id=mb-fallback-request-compact`
  `return: likelihood moderate, the fallback runs only when XML or regex extraction misses fields, frequency not counted; impact 5 to 15 percent of that request's tokens, estimated from code reading only; evidence the cited lines, no changelog entry`
  - worker: haiku 0.25/0.5/1 h

## How to pick something up

1. Open a GitHub issue at [k3rt4s/medbill-dispute-kit/issues](https://github.com/k3rt4s/medbill-dispute-kit/issues) saying which item you're picking up.
2. Reference the relevant sub-bullets above so the scope is shared.
3. Open a PR when ready. The reviewer will check against `CONTRIBUTING.md` and the corresponding USER_STORIES.md story if one exists.
4. If shipped, the item moves to `BUILD_PLAN.md` (with version), gets a story in `USER_STORIES.md` (status `shipped`), and an entry in `CHANGELOG.md`.

## Related

- [USER_STORIES.md](USER_STORIES.md), user-value master.
- [BUILD_PLAN.md](BUILD_PLAN.md), shipped-and-shipping-soon engineering work.
- [roadmap.json](roadmap.json), machine-readable feature roster.
- [CONTRIBUTING.md](CONTRIBUTING.md), PR guidelines.
