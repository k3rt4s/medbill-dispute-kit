# Template — Dispute reply (second written dispute)

Use when the patient sent the initial dispute letter, the provider or insurer replied, but the reply did not address the substance of the dispute. Common non-responses:

- A new statement at the original balance with no reference to the dispute.
- A form letter that recites general billing policy without addressing the specific line items challenged.
- A "we have reviewed your account and the balance is correct" letter with no analysis.
- An offer of a payment plan or hardship discount when the dispute was about coding or NSA preemption, not affordability.
- An invitation to call billing when the patient has specifically requested written correspondence.

The second written dispute re-anchors the case before escalating to the 30-day warning. It is shorter and sharper than the initial dispute: it identifies what was unaddressed, restates the legal basis, and gives the recipient a final written opportunity to respond on the merits before the patient files a DOI complaint or proceeds to small claims.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

[BILLING DEPARTMENT MANAGER / PATIENT FINANCIAL SERVICES]
[PROVIDER NAME]
[PROVIDER MAILING ADDRESS]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: Second written dispute — your reply of [PRIOR RESPONSE DATE] did not address the substance —
    Account #[ACCOUNT NUMBER]
    Patient: [PATIENT FULL NAME]
    Date(s) of service: [DATE OF SERVICE]
    Balance asserted: $[CURRENT BALANCE]
    Initial dispute letter dated: [INITIAL DISPUTE DATE]
    Initial dispute USPS tracking: [INITIAL DISPUTE TRACKING]
    Your reply dated: [PRIOR RESPONSE DATE]

To Billing / Patient Financial Services:

On [INITIAL DISPUTE DATE] I sent your office a written dispute on the above-referenced account by certified mail. Your office responded on [PRIOR RESPONSE DATE]. The response did not address the substance of the dispute. This letter re-states the open items and gives you a final written opportunity to respond on the merits before I file a complaint with the [STATE] Department of Insurance / Department of Commerce and Insurance and the [STATE] Attorney General's Division of Consumer Affairs, and (if applicable) initiate a civil action in [COUNTY] [STATE] small-claims / general-sessions court.

I. What you said and what it did not address

[The drafter renders one or more of the blocks below based on what was in the prior response.]

[BLOCK A — Form letter / general billing policy]

Your response reciting your office's general billing policy does not address the specific line items I challenged. The dispute is line-item specific. My initial dispute identified [N] specific items (summarized in Section II below); your response did not analyze any of them by code, amount, or evidence.

[BLOCK B — New statement at the same balance]

Your response was a new statement at the same balance. Re-issuing a statement is not a response to a dispute; it restates the position I am disputing. The dispute remains open and the balance asserted is not enforceable until you provide a written response addressing the items in Section II below.

[BLOCK C — Conclusory "we have reviewed" letter]

Your response stated that you "reviewed" the account and concluded the balance is correct, without showing any analysis. A bare conclusion is not a response. Under [STATE] consumer-protection law and the FDCPA validation rules where they apply, a creditor or collector responding to a written dispute must address the substance. Please provide:

(a) the specific evidence in the medical record supporting each disputed line item;
(b) the specific contractual or statutory basis for each disputed amount;
(c) the office's response to each numbered item in Section II below.

[BLOCK D — Hardship / payment-plan offer when the dispute was about coding or NSA]

Your response offered a hardship discount or payment plan. The dispute is not about affordability. I am not asking you to reduce the balance because I cannot pay; I am stating that the balance as asserted is not enforceable because [the line items violate NCCI unbundling rules / the No Surprises Act fixes my cost-sharing at the in-network amount / the EOB-allowed amount is lower than what you are billing me / the itemized bill has not been provided despite a written request, which violates [STATE STATUTE]]. A hardship offer does not resolve a coding, NSA, or statutory-compliance dispute.

[BLOCK E — Invitation to call]

Your response asked me to call. I have specifically requested written correspondence and have indicated I will not negotiate by phone. The reasons are documentation and a clear paper trail, and they apply equally to your office. Please respond in writing.

II. The open items from my initial dispute

[The drafter renders a numbered list from the original dispute letter and from the audit / benchmark findings on file. Each item shows the specific code or charge in dispute, the basis for the dispute, and what response would resolve it.]

1. [CPT/HCPCS or charge line]: $[AMOUNT]. Basis for dispute: [duplicate of code X same DOS / unbundled from comprehensive code Y / billed at chargemaster vs the EOB allowed amount of $Z / charged for a service not documented in the medical record per HIPAA records request dated [DATE]]. Resolution requested: [refund or write-off; corrected statement showing the line removed or reduced to the EOB allowed amount].

2. [Next item, same structure.]

3. [Continue.]

III. Legal posture

Each of the bases above stands on independent legal grounds:

- For NSA-protected services: 42 U.S.C. § 300gg-111 fixes my cost-sharing at the in-network amount; balance-billing above that is preempted.
- For EOB-vs-bill discrepancies: the plan-allowed amount adjudicated by my health plan is the contractual ceiling; any spread the provider is asserting is a plan-vs-provider dispute, not a patient dispute.
- For NCCI / unbundling: federal coding rules and most state insurance regulations prohibit billing the comprehensive code and the sub-code on the same DOS.
- For services not documented in the medical record: a billed service without supporting documentation is not collectible and (depending on intent) may be reportable to the [STATE] Attorney General's Medicaid Fraud Control Unit / federal HHS-OIG.
- For chargemaster pricing well above fair-market: UCC § 2-305(2) requires the open price term to be set in good faith; a chargemaster price multiple times the Medicare allowable, the office's own published cash price, and the rate every commercial payer pays for the same service is not a good-faith open price.

IV. Hold on collections

I respectfully restate my request that collection activity on this account be held pending resolution of the open items above. Pursuant to your office's published billing-dispute policy [or, for accounts referred to a third-party collector, pursuant to 15 U.S.C. § 1692g], please confirm in writing that:

(a) no further statements will be issued until the open items are addressed;
(b) the account will not be referred to a collection agency while the dispute is open;
(c) no negative information will be reported to any consumer credit reporting agency on this account while the dispute is open.

V. Final response window

Please respond in writing within fifteen (15) business days from the date of the USPS certified-mail receipt above. The response must address each numbered item in Section II by name, code, and amount, and must include the evidence and statutory or contractual basis supporting your position.

If a substantive written response is not received within that window, I will:

1. File a complaint with the [STATE] Department of Insurance / Department of Commerce and Insurance using the kit's `complaint_state_doi.md` template, attaching the full dispute history (this letter, the initial dispute, your non-responsive reply, the medical record, the EOB, the line-item benchmark analysis).

2. File a parallel complaint with the [STATE] Attorney General's Division of Consumer Affairs.

3. Mail the 30-day warning letter (`letter_30day_warning.md`) starting the small-claims clock.

4. If applicable, file a parallel CMS Hospital Price Transparency complaint.

VI. Privilege and offer of compromise

This letter is sent under [STATE] Rule of Evidence 408 (or its federal equivalent) as a continued offer of compromise. No statement is an admission of liability for any amount, and any concession in this letter is contingent on a written settlement that fully resolves the account.

Please direct your response to the address above.

Sincerely,



[PATIENT FULL NAME]

Account number: [ACCOUNT NUMBER]
Date of service: [DATE OF SERVICE]
Prior correspondence:
- Initial dispute dated [INITIAL DISPUTE DATE], USPS tracking [INITIAL DISPUTE TRACKING]
- Your reply dated [PRIOR RESPONSE DATE]

Enclosures:
A — Copy of my initial dispute letter dated [INITIAL DISPUTE DATE]
B — Copy of your reply dated [PRIOR RESPONSE DATE]
C — Copy of the bill being disputed
D — Copy of the EOB for the corresponding claim
E — Line-item benchmark analysis (Medicare PFS rates)
F — Audit findings (NCCI / duplicate / late-fee / quantity flags)

cc:
- file
```

---

## Placeholders and rendering notes

- `[PRIOR RESPONSE DATE]` and the response blocks (A–E) are the heart of this letter. The drafter selects blocks based on what was in the provider's reply, which the user records in `tracker.csv` `notes` (or in the action log via `scripts/log_interaction.py --action response_received`). If the user has not characterized the reply, the drafter renders block C (conclusory) as the safest default.
- Section II numbered items come from the audit findings (`_audit.csv`), benchmark overpriced rows (`_benchmarks.csv`), and any structured findings the user added to the bill row's `findings` field.
- The "15 business days" window in Section V is deliberately tighter than the initial dispute's 30-day window. This letter is the bridge to escalation, not a fresh negotiation.

## Before sending

The drafter confirms:

1. `dispute_letter_sent_date` is populated and at least 14 calendar days have elapsed since the postmark.
2. A reply has actually been received. If 30+ days have passed with no reply at all, the right tool is `letter_30day_warning.md`, not this letter.
3. The user has recorded what was in the reply (block A, B, C, D, or E). If unrecorded, the drafter selects block C as a conservative default and notes that the user should refine before mailing.

## Parallel actions (same day as mailing)

- Update `tracker.csv` `notes` with "second written dispute mailed [DATE], USPS tracking [N]".
- Log the action via `scripts/log_interaction.py --action initial_dispute_letter_sent --note "second written dispute"`.
- Refresh `_audit.csv` and `_benchmarks.csv` if either has changed since the initial dispute; the enclosures should be current.

## Follow-up

- 15 business days from postmark with no substantive response → draft `letter_30day_warning.md`.
- 15 business days with a substantive response that resolves some items but not others → draft a focused third letter addressing only the remaining items (or proceed to DOI complaint on the remaining items alone, depending on what's left in dispute).
- Substantive response that resolves the dispute → record outcome in `tracker.csv` and update `status` to `settled` if payment is the resolution, `closed` if a write-off is the resolution.
