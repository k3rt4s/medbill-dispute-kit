# Template — FDCPA § 1692g debt-validation request

Use within **30 days** of the first written contact from a **third-party debt collector** (or debt buyer) about a medical debt. Triggers the federal Fair Debt Collection Practices Act's validation requirement: until the collector produces the requested verification, they must cease collection activity.

**Important limit:** the FDCPA applies only to third-party collectors and debt buyers, not to the original hospital or physician's office collecting its own debt. If the bill is from the hospital you saw or its in-house billing department, this template does not apply. Use `letter_initial_dispute.md` or `letter_hardship_negotiation.md` instead.

If you cannot tell whether the entity contacting you is the original provider or a third-party collector, look at how they refer to themselves on the letter (e.g. "We are a debt collector. This is an attempt to collect a debt." is the FDCPA-mandated mini-Miranda for collectors).

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE — must be within 30 days of the collector's first written communication]

[COLLECTOR NAME]
[COLLECTOR MAILING ADDRESS]
[CITY, STATE ZIP]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: Notice of dispute and request for validation —
    Account/reference #: [COLLECTOR ACCOUNT NUMBER]
    Alleged original creditor: [ORIGINAL CREDITOR NAME, if known]
    Alleged amount: $[AMOUNT CLAIMED]

To whom it may concern:

This letter is timely notice, within thirty (30) days of your initial written communication dated [DATE OF COLLECTOR'S FIRST LETTER], that I dispute the validity of the alleged debt referenced above. Pursuant to the Fair Debt Collection Practices Act, 15 U.S.C. § 1692g(b), you must cease collection activity until you provide the verification required by the Act.

I. Verification requested

Please provide all of the following in writing:

1. **The name and address of the original creditor**, including the original medical provider whose alleged services give rise to this debt.
2. **A copy of the original signed contract** between me and the original creditor pursuant to which the alleged debt arose.
3. **An itemized statement** from the original creditor showing the services rendered, the dates of service, the CPT/HCPCS codes, and the amounts charged.
4. **A copy of the Explanation of Benefits** (EOB) from any insurance company that processed the claim, if applicable.
5. **An accounting** of all payments, adjustments, and write-offs applied to the underlying account, demonstrating how you arrive at the claimed balance.
6. **The complete chain of assignment** from the original creditor to your agency (and any prior assignees), with the date and consideration of each transfer. For debt buyers, provide the bill of sale or assignment agreement showing your purchase of the account.
7. **Proof of your authority** to collect this debt in [STATE], including evidence of licensure as a debt collector in this state to the extent required by [STATE] law.
8. **The date of last activity** on the underlying account, so I can confirm the alleged debt is not beyond the applicable statute of limitations.

II. Cease and limit communications

Pursuant to 15 U.S.C. § 1692c, please direct all further communications to the address above, in writing. Do not contact me by telephone, do not contact my place of employment, and do not contact third parties about this alleged debt.

III. Notice of preservation of rights

I am preserving all rights and remedies under federal and state law, including:

- The Fair Debt Collection Practices Act, 15 U.S.C. §§ 1692-1692p, which provides a private right of action against debt collectors for statutory violations;
- Any rights I may have under [STATE]'s consumer protection statutes;
- Any rights I may have under the Fair Credit Reporting Act, 15 U.S.C. §§ 1681-1681x, including the right to dispute inaccurate furnishing of information to consumer reporting agencies.

IV. No payment until validation

Until you provide the verification requested above, I will not pay any portion of the alleged debt. Any partial payment is not an admission of the validity of the alleged debt. I am not refusing to pay a valid debt; I am exercising my statutory right to verification before payment.

If you cannot produce the verification requested above, you must withdraw your collection activity, notify any consumer reporting agency to which you have reported this alleged debt, and confirm to me in writing that the matter is closed.

Sincerely,



[PATIENT FULL NAME]

Account/reference #: [COLLECTOR ACCOUNT NUMBER]

Enclosure: copy of the collector's initial communication dated [DATE]
```

---

## Placeholders and rendering notes

- **Timing is critical.** The 30-day window for § 1692g notice runs from the date the patient received the collector's first communication, not the date the collector sent it. After 30 days, the patient can still demand verification, but the FDCPA's automatic cessation-of-collection-pending-verification protection no longer applies.
- The LLM must ask the patient: (a) what date did you receive the collector's first letter, and (b) is this collector the original creditor or a separate company? If (b) is "original creditor," do not use this template.
- The certified-mail tracking number is essential evidence that the dispute was sent within 30 days.

## What happens next

Most third-party collectors cannot produce the full chain of documentation requested. Outcomes typically follow one of these paths:

1. The collector cannot validate and quietly closes the file. You receive a "deletion" letter or simply no further contact. Confirm by checking your credit reports 30-60 days later.
2. The collector returns the debt to the original creditor. You may then receive new collection attempts from the original creditor or a different collector. If a new collector contacts you, the § 1692g clock resets and you can send this letter to them.
3. The collector produces some documentation but cannot produce a signed contract or complete chain of assignment. In that case, send a follow-up letter pointing out the specific gaps; do not pay until the gaps are filled.
4. The collector produces complete documentation. At that point the debt is "validated" under § 1692g. You may then dispute the underlying bill on its merits (use `letter_initial_dispute.md`) or negotiate (use `letter_hardship_negotiation.md`).

## Parallel actions

- **Check your credit reports** at [annualcreditreport.com](https://www.annualcreditreport.com) for any tradeline the collector has reported. If the collector has reported a disputed debt without noting the dispute, that's an FCRA furnisher violation; document it.
- **State complaint** if the collector violates the FDCPA in any respect (continues contact after this letter, contacts third parties, threatens legal action without basis, etc.): file with the Consumer Financial Protection Bureau at [consumerfinance.gov/complaint](https://www.consumerfinance.gov/complaint/) and with your state attorney general.

## Statute of limitations on the underlying debt

Most state breach-of-contract statutes of limitation are 3-6 years. **Do not make a payment on a time-barred debt without legal advice** — a partial payment can restart the clock in some states. The LLM should ask the patient for the date of last service or last activity and warn if the alleged debt may already be time-barred under the patient's state law.

## Follow-up

The LLM logs this with `action_type = "credit_report_dispute_filed"` (closest match in the current `action.toml` enum; expand the enum to add `fdcpa_validation_request` in a future schema revision). Set `response_due_by` to 30 days from the date the certified letter is delivered (per the return receipt), not from the date it was sent.
