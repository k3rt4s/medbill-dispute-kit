# Template — Attorney intake packet

Use when the patient has run the kit's dispute flow to a point where engaging counsel makes sense and needs a clean one-document summary to hand to an attorney for an intake consult. The packet is two pages: page one is the case summary; page two is the artifact index. The attorney decides whether to take the case based on page one and can find anything they want on page two.

This is not a fee agreement and is not legal advice. It is a fact pack that converts months of certified-mail receipts and tracker rows into something an attorney can absorb in five minutes.

When to use:

- A hospital lien is interfering with a tort settlement and a personal-injury attorney is already handling the underlying case.
- The dispute has been through DOI complaint, 30-day warning, and small claims is the next escalation but the amount in controversy approaches or exceeds the jurisdictional limit.
- A debt collector is violating FDCPA and a consumer-protection attorney could litigate on contingency.
- The plan is denying ERISA appeals and the patient wants ERISA-specific counsel.
- A state-court declaratory-judgment action is the next step and the patient wants representation rather than appearing pro se.

Most kit users will not need this template. Most disputes resolve through the certified-mail-and-DOI-complaint flow without ever reaching an attorney. This is for the cases where the kit's flow is producing diminishing returns.

---

```letter
Attorney Intake Packet — [PATIENT FULL NAME]

Prepared: [DATE]
Patient: [PATIENT FULL NAME], DOB [DOB]
Address: [STREET ADDRESS, CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

---

PAGE 1 — CASE SUMMARY

Type of case (check what applies):
[ ] Hospital lien dispute (tort-recovery interference)
[ ] Medical-debt dispute (provider directly)
[ ] Medical-debt dispute (third-party collector / FCRA reporting)
[ ] ERISA appeal / plan-administrator denial
[ ] No Surprises Act balance-billing violation
[ ] State surprise-billing or consumer-protection violation
[ ] Subrogation / reimbursement dispute with plan
[ ] § 501(r) FAP-screening failure (non-profit hospital)
[ ] Workers' comp / auto-medpay payer redirect
[ ] Other: ___________________________________

Amount in controversy: $[AMOUNT]
Parties:
  - Provider/hospital: [PROVIDER NAME], [PROVIDER ADDRESS], NPI [NPI], EIN [EIN]
  - Insurer: [INSURER NAME], [PLAN NAME], member ID [MEMBER ID], group [GROUP NUMBER]
  - Plan funding: [self-funded / fully insured / governmental / church]
  - Collector (if any): [COLLECTOR NAME], [COLLECTOR ADDRESS]
  - At-fault party / their insurer (if accident-related): [NAME, ADDRESS]
  - Patient's state of residence at time of service: [STATE]
  - Service rendered in state: [STATE]

One-paragraph factual narrative:

[2-4 sentences. The drafter renders this from the canonical bill row, the encounter context if any, and the action log. Example pattern: "On [DOS], I received [service] from [provider]. The total billed was $[X]; my plan adjudicated the claim at $[Y]; the provider is asserting $[Z]. The plan's EOB shows [in-network / OON] cost-sharing of $[W]. On [date], the provider [refused / failed to respond to] my written dispute. As of today, the dispute remains unresolved and [next escalation] is the planned next step. I want counsel to [specific ask]."]

Specific legal theories the dispute has invoked (from prior correspondence):

[The drafter lists each theory cited in a prior letter, with the controlling authority.]

- [42 U.S.C. § 300gg-111 — NSA balance-billing prohibition / § 300gg-111(b) ancillary protection]
- [45 CFR Part 180 — Hospital Price Transparency Rule]
- [UCC § 2-305(2) (or state common-law analogue) — good-faith open price term]
- [STATE STATUTE — e.g., Tenn. Code § 68-11-220 itemization, GA O.C.G.A. § 10-1-393(b)(14) FBPA]
- [15 U.S.C. § 1692g — FDCPA validation; § 1692e — false or misleading representations]
- [15 U.S.C. § 1681i — FCRA reinvestigation; § 1681s-2(b) — furnisher accuracy]
- [29 U.S.C. § 1024(b)(4) — ERISA plan-document right; § 1132(c)(1) — § 502(c) statutory penalty; § 1133 — claims procedure]
- [26 U.S.C. § 501(r) — non-profit hospital obligations; § 1.501(r)-6 — reasonable efforts before collection action]
- [STATE WC STATUTE — anti-balance-billing for work-related injuries]
- [Hospital-lien statute — STATE-SPECIFIC]

What I have already done (chronological):

[The drafter pulls from the action log, summarized to date / event:]

- [DATE]: [Action] (USPS tracking [N], response [received / none])
- [DATE]: [Action]
- ...

What I want from counsel:

[The drafter renders the specific ask based on the case type. Examples:]

- "Review the hospital lien for compliance with [STATE] statute and demand withdrawal or reduction to the EOB-allowed amount."
- "File a declaratory-judgment action in [COUNTY] [STATE] court establishing the reasonable price under UCC § 2-305."
- "File an ERISA § 502(a)(1)(B) action to recover plan benefits and the § 502(c)(1) penalty."
- "Represent me in a state-DOI / state-AG enforcement action against the collector under [STATE CONSUMER PROTECTION ACT]."
- "Review my dispute history and recommend whether to escalate to court or settle."

Fee posture (what I am asking):

[The drafter renders one. Example patterns:]

- "I can pay an hourly consult fee of up to $[N] for a one-time review."
- "I prefer contingency if the case supports it; my expected total recovery is $[N] given the amount in controversy and the available statutory fees."
- "I am applying for legal-aid eligibility separately; if you accept legal-aid referrals, that is my preferred path."
- "I am asking for pro-bono review only; if the case requires fee-based work, I will decide then."

Statute-of-limitations posture:

- The original date of service was [DOS]. The state's written-contract SOL is [N] years; SOL expiry is approximately [DATE].
- The plan's internal-appeals deadline ran on [DATE] (extended to [DATE] if extension was requested).
- The federal IDR or PPDR deadline (if applicable) is [DATE].
- The state-DOI complaint expects a 30-90-day response; I filed on [DATE].

---

PAGE 2 — ARTIFACT INDEX

The artifacts below are organized in the patient's evidence bundle (`<HEALTHBILLS_ROOT>/_bundles/<bill_id>_<date>.zip`), which is available on request. The MANIFEST.md inside the bundle indexes every artifact by category.

Bill and EOB:
- Bill from [PROVIDER]: account [ACCOUNT NUMBER], dated [STATEMENT DATE], current balance $[BALANCE]
- EOB from [INSURER]: claim [CLAIM NUMBER], dated [EOB DATE]
- Itemization on file: [YES — line-count, NO]
- HIPAA medical record on file: [YES — request date, response date, NO]

Dispute correspondence:
- Initial dispute letter: [DATE], USPS tracking [N], response [received / none / non-substantive]
- Counter-offer letter: [DATE], USPS tracking [N], counter-offer amount $[OFFER]
- 30-day warning: [DATE], USPS tracking [N]
- Second written dispute: [DATE], USPS tracking [N]

Regulatory complaints:
- State DOI complaint: [DATE], confirmation [N], status
- State AG complaint: [DATE], confirmation [N], status
- Federal NSA complaint: [DATE], reference [N], status
- CMS HPT complaint: [DATE], reference [N], status
- IRS Form 13909: [DATE], status

Pricing evidence:
- Medicare PFS benchmark file: `Billers/<slug>/_benchmarks.csv`
- Hospital MRF excerpt: `_mrf_lookups/mrf_<slug>_<date>.csv`
- Audit findings (NCCI, duplicates, modifier-25): `Billers/<slug>/_audit.csv`

Plan documents:
- SPD: [received / requested / refused], date
- Plan-document request via § 1024(b)(4): [DATE]
- § 502(c)(1) penalty demand letter: [DATE], computed penalty $[N]

Encounter context (if multi-provider):
- Encounter ID: [E-YYYY-NNN]
- Total providers in encounter: [N]
- Providers: [list]
- Combined encounter dispute letter: [DATE]

Accident context (if applicable):
- Date of injury: [DATE]
- Type: [MVA / slip-and-fall / on-the-job / etc.]
- At-fault party: [NAME]
- Liability insurer: [NAME], claim [N]
- WC carrier: [NAME], claim [N]
- Hospital lien: filed [DATE], amount $[N], instrument [N]

State and federal context:
- Patient state of residence at DOS: [STATE]
- Service-rendered state: [STATE]
- State packs referenced in dispute: [LIST from references/laws_state_<code>.md]
- Federal authorities cited: [LIST from rules/ folder]

---

Prepared by the patient using medbill-dispute-kit. Not legal advice; not work product. Provided to counsel as background for an intake consult.
```

---

## Placeholders and rendering notes

- `[next escalation]` in the one-paragraph narrative depends on where the patient is in the state machine. The drafter selects from: file DOI complaint, file 30-day warning, file second written dispute, file small claims civil warrant, file federal NSA complaint, file ERISA § 502(c) penalty action, etc.
- The fee posture block is the most subjective; the drafter renders it from a user input flag (`HEALTHBILLS_ATTORNEY_FEE_POSTURE` env var, or a row in `tracker.csv`'s `notes`) so the patient is not surprised by what the packet says about their willingness to pay.
- The packet is intentionally light on legal argument. Attorneys read fact patterns and statutes; they form their own theories. The packet's job is to make the facts retrievable, not to brief them.

## Before generating

The drafter confirms:

1. The dispute group has at least 3 prior actions in the action log. A patient asking for counsel after one statement letter probably has not exhausted the kit's free flow yet.
2. An evidence bundle exists at `_bundles/<bill_id>_<date>.zip`. The packet's page-2 artifact index references the bundle; without it, the artifact index is hollow.
3. The case-type checkbox at the top of page 1 is filled in. If multiple types apply, check all that apply; do not leave them all blank.

## Parallel actions (when first sending the packet)

- Send the packet by email or upload through the attorney's intake portal, not by certified mail. Attorneys triage email intake faster than paper.
- Send the evidence bundle as a separate ZIP attachment. Most attorney intake systems accept up to 25 MB; if the bundle exceeds that, use a file-share link and include the link in the email.
- After the consult, log the result in `actions.csv` via `scripts/log_interaction.py --action other --note "attorney intake: <attorney name>, declined / accepted / referred"`.

## Follow-up

- If counsel accepts the case, the kit's role ends for the substantive dispute and shifts to documentation. Continue using `log_interaction.py` to track interactions; the attorney may want the log later.
- If counsel declines, ask for the specific reason. Common reasons: amount too small for contingency, statute of limitations is too close, the dispute is too factually mixed, the attorney does not practice in the relevant area. Use the reason to recalibrate next steps (e.g., a different specialty, a state legal-aid referral, pro se in small claims).
- If counsel refers to legal aid: most states' bar associations maintain a lawyer-referral hotline; LSC-funded legal aid programs cover medical-debt cases in many jurisdictions.

## What this is not

- Not a retainer agreement. Counsel will produce their own engagement letter if they accept.
- Not a litigation hold. If you anticipate litigation, also send the provider and any collectors a separate written notice not to destroy records.
- Not a release of any claim. The packet is a recitation of facts and prior procedure; it does not waive or settle anything.

## Related templates and scripts

- `scripts/bundle_evidence.py` — produces the evidence bundle the artifact index references.
- `scripts/log_interaction.py` — populates the action log the narrative pulls from.
- `templates/letter_challenge_hospital_lien.md` — most common single-template motivation for attorney engagement.
- `templates/letter_erisa_502c_penalty.md` — common federal-court doorway.
