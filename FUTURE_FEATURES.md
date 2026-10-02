# Future features

Engineering-language backlog of work not yet scheduled. Sits under [USER_STORIES.md](USER_STORIES.md) (the user-value master) and [BUILD_PLAN.md](BUILD_PLAN.md) (the shipped-work tracker). When an item here is ready to ship, it moves into BUILD_PLAN.md with a version target and gets a corresponding story in USER_STORIES.md.

Items here are not promises. The kit is open-source; contributors are welcome to pick any of these up. Each item lists the rough shape of the work, the kit components that would change, and a one-line note on why it has not shipped yet.

---

## Scored index

No unshipped features remained as of 2026-09-08; the two token-cost items filed from the 2026-10-02 audit were both rejected after measurement and are recorded below so they are not filed again. The final two vendor-gated ideas, Turquoise Health API integration and Dollar For screener integration, were deleted because both require external vendor permission or confirmation before there is actionable project work.

Added 2026-10-02 from the workspace token audit:

- mb-ocr-whitespace-collapse, rejected 2026-10-02 after measurement: across 82 real OCR sidecars, a whitespace collapse removes 0.4 to 0.7 percent of characters and no sidecar comes near the 80,000-character cut, so there is nothing to save. A full space-run collapse would also erase EOB column alignment.
- mb-fallback-request-compact, rejected 2026-10-02 after measurement: compacting the `json.dumps(request)` that `scripts/parse_990.py` and `scripts/parse_sbc.py` send on the model fallback path (collapsed page whitespace, `ensure_ascii=False`, compact separators) saves 0.4 to 2.3 percent of the request, measured by running 19 real text-layer PDFs through the kit's own request builders. The estimate from code reading was 5 to 15 percent. The fallback runs only when XML or regex extraction misses fields, so the saving rounds to nothing.

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
