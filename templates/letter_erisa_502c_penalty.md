# Template — ERISA § 502(c) statutory penalty claim

Use when the patient sent a written request for plan documents under ERISA § 104(b)(4) / 29 U.S.C. § 1024(b)(4) and the plan administrator failed to furnish the documents within 30 days. ERISA § 502(c)(1) / 29 U.S.C. § 1132(c)(1) imposes a per-day statutory penalty (currently up to $110/day per ERISA § 502(c)(1), as adjusted for inflation under 29 CFR § 2575.502c-1) the participant or beneficiary can claim. The penalty is payable to the participant, not the plan, and is in addition to any other relief.

This applies most often when:

- The patient requested an Explanation of Benefits or claim file under § 1024(b)(4) and did not get one.
- The patient requested the Summary Plan Description, plan document, summary annual report, or fiduciary breach disclosure and did not get it.
- The plan's subrogation vendor asserted a recovery claim without providing the plan-document language they were relying on, despite a written request.

The court has discretion on the dollar amount per day, but the maximum is well-established and the kit's template asks for the statutory maximum from the date the 30-day window closed.

This is a federal cause of action. Filing usually happens in federal district court for the district where the plan is administered or where the breach occurred. The letter below is the pre-suit demand that creates the documentary record and gives the plan administrator a last opportunity to cure.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

[PLAN ADMINISTRATOR LEGAL NAME]
[c/o PLAN SPONSOR if applicable]
[MAILING ADDRESS FOR PLAN ADMINISTRATOR]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

cc by certified mail:
    [PLAN SPONSOR — typically the employer]
    [PLAN'S INSURER / THIRD-PARTY ADMINISTRATOR if separate]
    [U.S. Department of Labor, Employee Benefits Security Administration, regional office]

RE: Notice of § 502(c)(1) statutory-penalty claim for failure to provide plan documents —
    Participant: [PATIENT FULL NAME]
    DOB: [DOB]
    Member ID: [MEMBER ID]
    Plan name: [PLAN NAME]
    Plan number: [PLAN NUMBER]
    Plan sponsor: [PLAN SPONSOR NAME]
    Plan administrator: [PLAN ADMINISTRATOR NAME]
    Documents originally requested on: [REQUEST DATE]
    Tracking number of original request: [ORIGINAL TRACKING]
    Calendar days since request: [N DAYS SINCE REQUEST]

To the Plan Administrator:

I am a participant in the plan referenced above. On [REQUEST DATE] I sent the plan administrator a written request for plan documents pursuant to ERISA § 104(b)(4) / 29 U.S.C. § 1024(b)(4), by certified mail with USPS tracking [ORIGINAL TRACKING]. A copy of that request is attached as Exhibit A.

As of the date of this letter, [N CALENDAR DAYS SINCE REQUEST] calendar days have elapsed since the request. The plan administrator has [failed to furnish any of the requested documents / furnished an incomplete set, see Exhibit B]. The plan administrator did not invoke a documented administrative exception or extension under any applicable regulation.

I. Authority

ERISA § 104(b)(4) / 29 U.S.C. § 1024(b)(4) requires the plan administrator to provide, upon written request by a participant or beneficiary, copies of:

(a) the latest updated summary plan description;
(b) the latest annual report;
(c) any terminal report;
(d) the bargaining agreement, trust agreement, contract, or other instruments under which the plan is established or operated.

The DOL has interpreted the right of access to extend to claim files, individual benefit determinations, and any document on which a benefit determination was based, pursuant to 29 CFR § 2560.503-1(h).

The plan administrator's duty under § 104(b)(4) attaches "within 30 days" of the written request. Failure to comply triggers § 502(c)(1) / 29 U.S.C. § 1132(c)(1), which provides that the administrator "may in the court's discretion be personally liable to such participant or beneficiary in the amount of up to $110 a day from the date of such failure or refusal" (the $100 statutory amount under § 502(c)(1) is adjusted for inflation under 29 CFR § 2575.502c-1).

II. The penalty calculation

The 30-day clock began on [REQUEST DATE + 30 DAYS] and continues until the plan administrator cures the failure by furnishing the requested documents in full.

As of today, the accrued statutory penalty is:

- Days past the 30-day window: [N DAYS PAST WINDOW]
- Maximum per-day amount: $110 (29 CFR § 2575.502c-1)
- Maximum cumulative penalty as of today: $[MAX PENALTY = DAYS × 110]

The penalty continues to accrue at $110 per day for each day the failure continues.

III. Demand

I demand, within fifteen (15) calendar days of the date of this letter:

1. Production of every document originally requested on [REQUEST DATE], in full, by mail to the address above (or by encrypted electronic delivery if I expressly authorize), without further redactions beyond what ERISA permits.

2. A check made payable to me in the amount of $[DEMANDED PENALTY], representing the accrued statutory penalty under § 502(c)(1) computed at $110 per day from [REQUEST DATE + 30 DAYS] through the date of this letter, less any reasonable reduction the plan administrator wishes to propose based on a defense I should consider before filing suit (e.g., a documented administrative obstacle outside the administrator's control).

3. Written confirmation of the steps the plan administrator is taking to ensure that future § 104(b)(4) requests will be honored within the 30-day statutory window.

IV. Consequence of non-cure

If the plan administrator does not cure within 15 calendar days, I will:

1. File a civil action in the United States District Court for the [DISTRICT — typically where the plan is administered or where I reside] under 29 U.S.C. § 1132(a)(1)(A) and § 1132(c)(1) seeking the statutory penalty, plus reasonable attorney's fees and costs of suit under § 1132(g).

2. File a parallel complaint with the U.S. Department of Labor, Employee Benefits Security Administration. The DOL regional office for the patient's jurisdiction can investigate plan-document violations and, in some cases, file an enforcement action.

3. Notify the IRS of the plan's apparent non-compliance, which may bear on the plan's qualified status under § 401(a) or the sponsor's deduction for plan contributions.

V. Reservation of substantive claims

This letter addresses only the § 502(c)(1) statutory penalty for failure to produce documents. Nothing in this letter waives, releases, or compromises my underlying substantive claims, including but not limited to:

- Any claim for benefits under § 502(a)(1)(B);
- Any claim for breach of fiduciary duty under § 502(a)(2) or § 502(a)(3);
- Any claim under the No Surprises Act or other federal statutes incorporated by reference into the plan's compliance obligations.

I expressly reserve the right to add any of those claims to the contemplated civil action.

VI. Privilege

This letter is sent under Federal Rule of Evidence 408 as an offer of compromise. No statement is an admission for any other purpose.

Please direct your written response to the address above.

Sincerely,



[PATIENT FULL NAME]

Member ID: [MEMBER ID]
Plan name: [PLAN NAME]

Enclosures:
A — Copy of the § 104(b)(4) request dated [REQUEST DATE], with USPS green card
B — Copy of any partial response from the plan administrator, if any
C — Copy of the plan's most recent Summary of Benefits and Coverage (if previously received)
D — Computation of the accrued penalty
```

---

## Placeholders and rendering notes

- `[REQUEST DATE]` and `[ORIGINAL TRACKING]` come from the action log. The drafter pulls them via `scripts/log_interaction.py` rows where `action_type = "ebsa_intervention_request"` or where the user logged a manual records-request action linked to the bill_id.
- The $110/day amount reflects 29 CFR § 2575.502c-1 as inflation-adjusted through recent DOL updates. Confirm the current published amount before relying on the dollar number.
- Suit can be filed in any district that has personal jurisdiction over the plan administrator (where the plan is administered, where the plan sponsor is headquartered, or where the breach occurred, depending on the circuit). The drafter does not pick the district; that goes to counsel before filing.

## Before sending

The drafter confirms:

1. The original § 104(b)(4) request was actually sent (action log shows the corresponding action), was sent in writing, and identified specific documents.
2. At least 45 calendar days have elapsed since the request (the 30-day statutory window plus a small buffer to account for postal transit and a courtesy grace period before invoking the penalty).
3. No partial cure has occurred. If the plan furnished some documents, the drafter renders Exhibit B with the list of what was produced and what is still missing, and computes the penalty only on the still-missing items.

## Parallel actions (same day as mailing)

- File a parallel DOL EBSA complaint at askebsa.dol.gov or 1-866-444-3272. DOL's investigation is independent of the § 502(c) penalty claim and creates additional pressure.
- If the missing documents are tied to an active billing or subrogation dispute, send a short status letter to the provider or recovery vendor noting that the plan administrator's non-response is impeding resolution and that the patient is preserving the § 502(c) claim.

## Follow-up

- 15 days from postmark with full cure → record the action as resolved; consider whether to accept a reduced penalty in exchange for releasing the § 502(c) claim, or pursue the full statutory amount.
- 15 days from postmark with no cure → consult counsel before filing the federal action. The § 502(c) penalty is straightforward but the court has discretion on the per-day amount, and many courts reduce the award when the patient cannot show specific harm from the delay. Building a record of specific harm (e.g., "I could not pursue my appeal because I did not have the SPD") helps maximize the award.

## What this is not

- This is not a substitute for the underlying benefit claim. Pursuing § 502(c) does not waive the benefit claim and does not toll the SOL on benefit claims. Pursue both tracks in parallel.

- This is not an FDCPA validation letter. § 1692g applies to debt collectors, not plan administrators. The two statutes operate independently; the kit has `letter_fdcpa_validation.md` for the debt-collector case.
