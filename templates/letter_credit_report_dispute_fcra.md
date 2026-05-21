# Template — FCRA credit-report dispute for medical debt

Use when the disputed medical bill has been reported to one or more credit bureaus and is appearing on the patient's credit report. The Fair Credit Reporting Act, 15 U.S.C. § 1681i, requires consumer reporting agencies (Equifax, Experian, TransUnion, plus specialty bureaus like LexisNexis, Innovis) to reinvestigate disputed items and to notify the furnisher of the dispute. The furnisher (the provider or collection agency) then has its own investigation obligation under 15 U.S.C. § 1681s-2(b).

Marshall Allen flags credit reporting as the single most damaging escalation tactic providers and collectors use. The good news for patients: medical debt reporting is heavily restricted as of recent years.

Current rule environment as of this template version:

- The three major bureaus voluntarily removed paid medical collections from credit reports starting July 2022, removed medical collections under $500 starting April 2023, and extended the reporting window for unpaid medical collections from 180 days to one year before they can appear (effective July 2022).
- CFPB rulemaking finalized in early 2025 prohibits credit reporting of most medical debts entirely (some implementation timing was paused or litigated; verify current effective date before filing).
- Several states (NY, CO, CA, IL, MN, NJ, CT, RI, VT, VA among others) have passed state-law equivalents that go further than the federal rule.

This template invokes both the federal FCRA and (where available) state-law overlays. It is sent to:

1. The consumer reporting agency that is reporting the item (one letter per bureau).
2. The furnisher (provider / hospital / collection agency) reporting the item to the bureaus.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]
Date of birth: [DOB]
Last 4 of SSN: [SSN LAST 4]

[DATE]

[CONSUMER REPORTING AGENCY OR FURNISHER]
[MAILING ADDRESS]

[For CRAs, use:
 Equifax Information Services LLC, PO Box 740256, Atlanta GA 30374
 Experian, PO Box 4500, Allen TX 75013
 TransUnion Consumer Solutions, PO Box 2000, Chester PA 19016]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: Dispute under the Fair Credit Reporting Act, 15 U.S.C. § 1681i —
    Consumer: [PATIENT FULL NAME]
    DOB: [DOB]
    Last 4 of SSN: [SSN LAST 4]
    Tradeline / account in dispute: [ACCOUNT NUMBER ON REPORT]
    Furnisher: [FURNISHER NAME AS LISTED ON REPORT]
    Reported balance: $[REPORTED BALANCE]
    Date opened on report: [DATE OPENED]
    Status on report: [Collection / Charge-off / Past due / Other]

To Consumer Disputes:

I am disputing the tradeline identified above pursuant to the Fair Credit Reporting Act, 15 U.S.C. § 1681i. The tradeline is inaccurate or otherwise improperly reported for the reasons below. I request that you reinvestigate and either correct or delete the item from my consumer report.

I. Identity verification

Enclosed is a copy of (a) a government-issued photo identification, and (b) a recent utility bill or bank statement matching the mailing address above, in case your identity-verification protocol requires them. (I am not required to provide these to dispute a tradeline, but enclosing them avoids a back-and-forth.)

II. Specific inaccuracies and grounds for deletion

[The drafter renders the grounds that apply, drawing from `tracker.csv`. Use the strongest applicable grounds; do not pile every possible argument in if not supported.]

[GROUND A — Federal CFPB medical-debt rule]

This tradeline is for medical debt. Effective [DATE OF FINAL RULE], the CFPB's "Prohibition on Creditors and Consumer Reporting Agencies Concerning Medical Information" rule prohibits a consumer reporting agency from including in any consumer report furnished for a credit decision any information relating to a medical debt of the consumer. I respectfully request that the tradeline be removed in full.

[GROUND B — Voluntary bureau policy: under $500]

The reported balance is $[REPORTED BALANCE], which is under $500. The three major bureaus' April 2023 voluntary policy removed all medical-collection tradelines under $500 from consumer reports. The tradeline appears to be in violation of that policy and should be removed.

[GROUND C — Voluntary bureau policy: paid medical collections]

The medical balance was paid in full on [DATE PAID]. Under the bureaus' July 2022 voluntary policy, paid medical collections are not reported. The tradeline either was never updated to "paid" or is being reported despite the paid status and should be removed.

[GROUND D — State medical-debt-reporting prohibition]

Reporting medical debt is prohibited under [STATE STATUTE — e.g., New York Fair Medical Debt Reporting Act (N.Y. Gen. Bus. Law § 380-t), Colorado HB23-1126]. This tradeline is for medical debt and is therefore unreportable under the law of the state in which I reside. I request immediate removal.

[GROUND E — Account is in active dispute with the furnisher]

The underlying account is in active billing dispute with the furnisher. Specifically:
- On [DATE], I sent the furnisher a written dispute by certified mail (USPS tracking [TRACKING NUMBER]) under the Fair Debt Collection Practices Act, 15 U.S.C. § 1692g (or under the federal No Surprises Act / state itemization statute, as applicable). A copy of that dispute and the green card are attached.
- The furnisher [did not respond / did not adequately validate the debt / responded but the dispute is unresolved as of today].
- An item that the furnisher knows or should know is in active dispute and that the furnisher has not validated is not "complete and accurate" under 15 U.S.C. § 1681s-2(a)(1)(A) and may not be reported. Even if the rule above did not apply, the furnisher's reporting in the face of an unresolved dispute violates the FCRA's furnisher accuracy obligation. I request immediate removal pending resolution of the underlying dispute.

[GROUND F — Account was paid by insurance / should never have been billed to me]

The medical claim underlying the account was [paid in full by my health insurance plan / would have been paid in full but the furnisher failed to bill insurance / is subject to the No Surprises Act and the balance asserted is not enforceable against me]. A copy of the Explanation of Benefits dated [EOB DATE], claim [CLAIM NUMBER], is attached as Exhibit B. The balance the furnisher is reporting is incorrect on its face.

[GROUND G — Account is not mine / identity theft]

I have no knowledge of this account. I did not receive the services giving rise to this account, and the account did not originate with me. If this is the result of identity theft, I have filed an identity-theft report with the Federal Trade Commission at IdentityTheft.gov; the FTC report number is [FTC REPORT NUMBER], and a copy is attached. Under 15 U.S.C. § 1681c-2, I am entitled to blocking of any information resulting from identity theft, and I request that the tradeline be blocked immediately.

[GROUND H — Outdated reporting]

The account is more than [seven (7)] years old from the date of first delinquency. Under 15 U.S.C. § 1681c(a)(4), accounts past the reporting period must be removed. I request removal.

III. Relief requested

I request that:

1. You reinvestigate the disputed item under 15 U.S.C. § 1681i and provide me with the results of your reinvestigation in writing within thirty (30) days (or forty-five (45) days if I am providing additional information during the reinvestigation window).

2. You notify the furnisher of this dispute and obtain documentation from the furnisher sufficient to either verify or delete the tradeline. Verification by automated dispute-handling system is not sufficient where, as here, the dispute identifies specific documentary inaccuracies.

3. If the tradeline cannot be verified as accurate, complete, and lawfully reportable, you delete the tradeline from my consumer report and notify me of the deletion.

4. You provide me with the name, address, and telephone number of the furnisher used in the reinvestigation, the procedures used, and a copy of any documentation relied upon (15 U.S.C. § 1681i(a)(6)(B)).

5. You notify all other consumer reporting agencies to which the tradeline was furnished of the dispute and any resulting deletion.

IV. Notice to furnisher (parallel)

A separate copy of this letter is being sent to the furnisher identified above so that the furnisher's own investigation obligation under 15 U.S.C. § 1681s-2(b) is triggered. The furnisher is now on notice of the dispute and may not continue to report the item to other bureaus without complying with the accuracy and investigation requirements of § 1681s-2.

V. Reservation of rights

If the reinvestigation does not result in deletion of the tradeline or correction of the specific inaccuracies above, I reserve the right to:

- File a complaint with the Consumer Financial Protection Bureau at consumerfinance.gov/complaint;
- File a complaint with my state attorney general's consumer protection division;
- File a private right of action under 15 U.S.C. § 1681n (willful noncompliance) or § 1681o (negligent noncompliance), with statutory and actual damages, attorney's fees and costs.

Please direct your written response to the address above.

Sincerely,



[PATIENT FULL NAME]

DOB: [DOB]
Last 4 of SSN: [SSN LAST 4]
Disputed tradeline: [FURNISHER NAME], account [ACCOUNT NUMBER ON REPORT]

Enclosures:
A — Copy of the relevant page from the credit report showing the tradeline
B — Explanation of Benefits, claim [CLAIM NUMBER], dated [EOB DATE]
C — Prior dispute letter to the furnisher dated [DATE], USPS tracking [TRACKING #], with green card
D — Copy of paid receipt / proof of payment (if applicable)
E — Copy of FTC IdentityTheft.gov report (if applicable)
F — Government-issued photo identification (front and back)
G — Recent utility bill or bank statement matching mailing address
```

---

## Placeholders and rendering notes

- Send a separate letter to each bureau that is reporting the item. Do not send one letter to "all three" — the bureaus' dispute systems are independent and each must receive its own filing.
- Send a parallel letter to the furnisher with the same enclosures, using the furnisher's mailing address (often a collection agency's address rather than the original provider's).
- The federal CFPB medical-debt rule has been the subject of litigation and political reversal at points; the drafter should check the current effective status before sending. If the rule is not in effect, omit Ground A and lean on Grounds B, C, D, E, F.
- For state-law grounds: the drafter loads `references/laws_state_<code>.md` and `references/medical_debt_protection_by_state.md` to find the state-specific medical-debt-reporting statute, if any. Do not invent state law.

## Before sending

The drafter confirms:

1. The patient has actually pulled a current credit report from all three bureaus (annualcreditreport.com — free weekly under the post-pandemic permanent rule). The dispute must reference the actual tradeline as it appears, not as it was described in a collection letter.
2. The underlying medical bill has been disputed in writing with the furnisher first, with certified-mail tracking. The FCRA dispute is the secondary track; the FDCPA / billing dispute is the primary track.
3. The patient's identity-verification documents (ID, utility bill) are ready to include with the letter. Some bureaus refuse to process disputes without them.

## Parallel actions

- File simultaneous CFPB complaints against the bureau and the furnisher at consumerfinance.gov/complaint. The CFPB process is fast (most companies respond within 15 days) and creates a federal record of the dispute.
- For collection agencies as furnishers: send the FDCPA validation request via `templates/letter_fdcpa_validation.md` if not already sent.
- Pull a fresh credit report after 45 days to confirm the dispute resulted in deletion or update.

## Follow-up

- 30 days from postmark to each bureau: expect a written reinvestigation result. If "verified as accurate" without addressing the specific grounds in this letter, the bureau likely used an automated dispute-handling system in apparent violation of § 1681i(a)(4) — escalate to CFPB and consider a private right of action.
- 45 days post-reinvestigation: pull a fresh report. Confirm the tradeline is deleted or updated as the bureau's response says it was. If not, escalate.
- If the tradeline is deleted: keep the reinvestigation result letter; furnishers occasionally re-report old items, and the reinvestigation letter is the proof that the dispute was already resolved in the patient's favor.
