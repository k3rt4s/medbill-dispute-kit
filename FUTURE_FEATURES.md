# Future features

Engineering-language backlog of work not yet scheduled. Sits under [USER_STORIES.md](USER_STORIES.md) (the user-value master) and [BUILD_PLAN.md](BUILD_PLAN.md) (the shipped-work tracker). When an item here is ready to ship, it moves into BUILD_PLAN.md with a version target and gets a corresponding story in USER_STORIES.md.

Items here are not promises. The kit is open-source; contributors are welcome to pick any of these up. Each item lists the rough shape of the work, the kit components that would change, and a one-line note on why it has not shipped yet.

---

## Scored index

Every unshipped feature in this file, scored with `ai_development/docs/board-scoring.md` on
2026-09-06 at the workspace hour value. Keep this current: when a feature is added, moved or
dropped, change its line here rather than a number in the prose below.

The features now being worked are listed under "On the work board" instead, without their score
blocks, because the board copy carries them and the scorer would otherwise count each twice.

The two below are contact-needed. Spanish localization, the outcomes bank, the advocate
variant and the chargemaster comparison helper were pruned on 2026-09-08 because none had
an actionable next step inside this project.

- **turquoise**, Turquoise Health API for live cross-hospital negotiated rates. Points at "Turquoise Health API integration". Contact-needed: refreshed 2026-09-08 evidence confirms a public API exists, but published terms do not permit the contemplated public-kit use without written vendor authorization. Earlier memo: `C:\Code_data\medbill-dispute-kit\reports\vendor_memo_turquoise_2026-09-06.md`; refresh memo: `C:\Code_Data\medbill-dispute-kit\reports\vendor_memos_refresh_2026-09-08.md`. `score: kind=feature gain=1/3/8 p=0.1 freq=4 hours=2/4/8 ai=15 risk=0.1x3 rev=two-way conf=assessed id=turquoise`
  `return: likelihood about 4 benchmark lookups a year, at about 1 in 10 that Turquoise licenses their API for open-source non-commercial use at all, estimated, since they have never been asked; impact the counter-offer letter anchors on the bundled Medicare fee-schedule table and manual FAIR Health lookups instead of live negotiated rates, a weaker reasonable-price argument worth 1 to 8 h of negotiation leverage each time; evidence scripts/fetch_price_benchmarks.py and references/medicare_pfs_common.csv read on 2026-09-06, plus 2026-09-08 review of Turquoise API docs and public non-commercial/community terms showing written permission is needed for public dissemination`
  - worker: sonnet 8/14/22 h, only after the memo comes back yes
- **dollarfor**, Dollar For charity-care screener integration. Points at "Dollar For screener integration". Contact-needed: refreshed 2026-09-08 evidence could not verify public API or integration terms because Dollar For's robots policy blocks the research user agents; this is a verification gap, not proof that no supported workflow exists. Earlier memo: `C:\Code_data\medbill-dispute-kit\reports\vendor_memo_dollarfor_2026-09-06.md`; refresh memo: `C:\Code_Data\medbill-dispute-kit\reports\vendor_memos_refresh_2026-09-08.md`. `score: kind=feature gain=2/5/15 p=0.15 freq=2 hours=1.5/3/6 ai=10 risk=0.1x2 rev=two-way conf=assessed id=dollarfor`
  `return: likelihood about 2 charity-care screens a year, at about 3 in 20 that Dollar For has or offers an API to integrate against, estimated, since they have never been asked; impact the patient is pointed at dollarfor.org by hand and the tracker never learns the screener result or the case number, 2 to 15 h of charity-care value missed each time the patient does not follow through unprompted; evidence templates/letter_hardship_negotiation.md and references/resources.md naming Dollar For as the recommended first step, the tracker schema having no column for a screener result, and 2026-09-08 review finding public API and integration terms unverified because Dollar For's robots policy blocks the research user agents`
  - worker: sonnet 8/12/18 h, only after the memo comes back yes

## Turquoise Health API integration

`scripts/fetch_price_benchmarks.py` currently bundles a static Medicare PFS table and constructs FAIR Health / Healthcare Bluebook URLs for manual lookup. Turquoise Health's API would give live pricing data across hospitals, including the negotiated rates buried in MRFs but normalized for cross-comparison.

Turquoise's API is commercial. Use would require:

- A credentialing flow for kit users (the API is not free).
- A cache layer to avoid re-querying for the same code in the same ZIP.
- A fallback to the existing static Medicare table when the API is unavailable.

As of 2026-09-08, public terms do not authorize this kit to reproduce or transmit
Turquoise data in patient-facing letters or tracker output without written permission.

Expected effort: 10-20 hours, contingent on Turquoise's commercial terms for open-source non-commercial use.

## Dollar For screener integration

Dollar For (dollarfor.org) is a non-profit that screens patients for hospital charity care under § 501(r) and, when eligible, files the FAP application on the patient's behalf. They are referenced in `templates/letter_hardship_negotiation.md` and `references/resources.md` as the recommended first step before formal dispute action.

A scripted integration would:

- Detect non-profit hospitals from the bill's biller_name (cross-referencing the IRS Tax Exempt Organization Search).
- Run the patient through the Dollar For eligibility screener via API (if Dollar For offers one) or via a deep-link workflow (if not).
- Update tracker.csv with the screener result and Dollar For case number.

As of 2026-09-08, public API and integration terms could not be verified because
Dollar For's robots policy blocks the research user agents. A direct vendor response
is needed before implementation.

Expected effort: 10-20 hours, contingent on Dollar For having or offering an API.

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
