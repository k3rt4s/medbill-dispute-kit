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

## On the work board

Moved 2026-09-06 to `C:\Code_data\medbill-dispute-kit\WORK_BOARD.md`, which carries each one's
score block, return block, worker estimate and lane brief. They keep their prose sections below.

- **states-10**, "State coverage, long tail". Moved 2026-09-06, Lane 2.
- **litigation-hold**, "Litigation-hold notice template". Moved 2026-09-06, Lane 4.
- **prebill-verify**, "Pre-bill insurance-verification helper". Moved 2026-09-06, Lane 4.
- **parse-990**, "parse_990.py, auto-extract Schedule H data". Moved 2026-09-06, Lane 5.
- **parse-sbc**, "Insurance plan SBC (Summary of Benefits and Coverage) parser". Moved 2026-09-06, Lane 5.
- **dedup-v2**, "Better deduplication across re-OCR runs". Moved 2026-09-06, Lane 6.
- **reply-classifier**, "Automated dispute-reply classifier". Moved 2026-09-06, Lane 7.
- **security-scope**, "SECURITY.md scope statement, reconcile with the local-ops pipeline". Moved 2026-09-06, Lane 9.

---

## State coverage, long tail

Ten states do not yet have a dedicated pack. The kit can still run for patients in these states using `references/laws_state_template.md` as a generic skeleton; what's missing is a worked-out file matching the 12-section structure of the existing packs.

| State         | Code | Notable considerations the pack should cover                                               |
| ------------- | ---- | ------------------------------------------------------------------------------------------ |
| Alaska        | AK   | Different SOL pattern; remote-care logistics; AK Insurance Code Title 21                   |
| Delaware      | DE   | DE Code Title 18 Insurance; small-claims jurisdictional limit; Justice of the Peace courts |
| Maine         | ME   | Maine Revised Statutes Title 24-A; LD 1101 medical-debt protections (2023)                 |
| Montana       | MT   | MCA Title 33; 8-year SOL on contracts                                                      |
| North Dakota  | ND   | NDCC Title 26.1; small-claims jurisdictional limit                                         |
| New Hampshire | NH   | RSA Title XXXVII; surprise-billing protections SB 591 (2024)                               |
| Rhode Island  | RI   | RIGL Title 27; medical-debt credit-reporting ban (Act 76, 2023)                            |
| South Dakota  | SD   | SDCL Title 58; community-impact patterns                                                   |
| Vermont       | VT   | 18 V.S.A. § 9456 hospital FAP requirements; Act 76 (2023) credit-reporting ban             |
| Wyoming       | WY   | WS Title 26; 10-year SOL on contracts                                                      |

Each state pack is ~150-300 lines of Markdown citing actual state statutes with URLs. Contribution checklist lives in `CONTRIBUTING.md`. Issue template at `.github/ISSUE_TEMPLATE/state_pack_request.yml`.

Expected effort per state: 3-6 hours of research and writing.

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

## parse_990.py, auto-extract Schedule H data

`references/irs_990_review.md` walks through what to pull from a non-profit hospital's IRS Form 990 / Schedule H manually. A scripted parser would:

- Accept a hospital EIN or ProPublica Nonprofit Explorer URL.
- Download the most recent 990 (the IRS publishes them as XML).
- Extract Schedule H Part I (charity-care numbers, community-benefit expense, bad debt), Part V Section B (facility-level policy responses), and Part VII (top-executive compensation).
- Emit a structured JSON profile per hospital that the IRS-13909 drafter and the hardship-negotiation drafter consume.

The 990 XML format is well-documented but verbose. Mapping XML elements to Schedule H fields is the bulk of the work.

Expected effort: 20-30 hours including test coverage against a half-dozen real 990 filings.

## Insurance plan SBC (Summary of Benefits and Coverage) parser

The ACA requires every plan to publish a standardized two-to-four-page Summary of Benefits and Coverage. The SBC is structurally consistent across plans (the ACA prescribes the format), making it more parseable than the Summary Plan Description. A parser would extract deductible / OOP-max / coinsurance / copay / coverage-tier data into a structured profile separate from the SPD profile.

The kit currently has `scripts/parse_spd.py`; an SBC parser would complement it. The SBC is patient-facing; the SPD is the full plan terms.

Expected effort: 15-25 hours.

## Automated dispute-reply classifier

The aging-letter ladder (`templates/letter_dispute_reply.md`) has five blocks (A-E) for the common patterns of non-substantive provider response: form letter, new statement at the original balance, conclusory "we reviewed" letter, hardship offer when the dispute was about coding, invitation-to-call when the patient requested writing. The user currently selects which blocks apply manually.

A classifier could read the provider's response sidecar (OCR'd from the provider's letter) and recommend which blocks fire. Implementation: a small Azure OpenAI prompt with the five block descriptions and the response text, returning a multi-label JSON.

Expected effort: 4-8 hours.

## Pre-bill insurance-verification helper

For a patient considering elective care, a helper that drafts a verification-of-benefits demand letter to the insurer plus a Good Faith Estimate demand to the provider, and tracks both responses, would let the patient know what they're signing up for before service. Currently the kit's flow assumes the bill has already arrived.

Expected effort: 10-15 hours; partly templated work, partly drafter integration.

## Better deduplication across re-OCR runs

`schemas/deduplication_rules.toml` defines how follow-up statements collapse onto an existing bill row. Currently the rules match on `account_number + provider_tax_id + DOS + balance`. Edge cases that occasionally still produce duplicates: account-number reformat on a system migration, provider-name rebrand mid-dispute, partial-payment-induced balance shifts.

A v2 dedup ruleset would add content-hashing of itemized line items as a secondary key, and would surface ambiguous matches to the user for confirmation rather than silently merging.

Expected effort: 15-25 hours including regression coverage.

## Litigation-hold notice template

When a patient anticipates litigation (the kit's small-claims escalation reaches that point regularly), federal and most state rules permit a "litigation hold" notice instructing the recipient not to destroy relevant records. A template would issue the hold to the provider, the collector if any, and the patient's plan.

The kit currently does not address evidence-spoliation risk explicitly; the implicit assumption is that providers keep records for their own statutory periods. A litigation-hold notice would close that gap.

Expected effort: 4-6 hours for the template plus drafter integration.

## SECURITY.md scope statement, reconcile with the local-ops pipeline

`SECURITY.md:3` opens with "The kit ships no executable code by default... The optional helper script in `scripts/` uses the Python standard library only. The repository is therefore low-risk by design." That sentence is accurate for `validate_tracker.py` and `deadline_watch.py`, and it is singular because it was written when those were the only two scripts. `scripts/` now also holds the local-ops pipeline (`classify_rename_medical_bills.py` through `bundle_to_cloud.py`), which sends bill and EOB text to Azure OpenAI and writes patient PII under `~/.medbill-dispute-kit/`. The in-scope list at `SECURITY.md:7` was already pluralized to "helper scripts"; the opening paragraph was not.

The risk is not a vulnerability, it is a reader who cites `SECURITY.md` as evidence that nothing in `scripts/` reaches the network or takes a dependency, and is wrong about the half of it that does. `scripts/README.md` documents the pipeline's network use correctly, so the two files currently disagree.

Work: split the claim so the two trust models are named separately rather than averaged, and decide whether the out-of-scope list should say anything about the Azure endpoint a patient configures themselves. Any wording change to a published security policy is a maintainer call, not a mechanical edit, which is why this is recorded here rather than patched. Recorded 2026-08-20.

Expected effort: under an hour once the wording is decided.

---

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
