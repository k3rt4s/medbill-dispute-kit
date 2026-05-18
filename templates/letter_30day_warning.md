# Template — 30-day warning before small claims

Use when an initial dispute letter has gone unanswered for 30+ days and the disputed amount is within the state's small-claims jurisdictional limit. This is the formal pre-litigation notice. CC the state insurance department, the state attorney general's consumer protection division, and the Better Business Bureau.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

[BILLING DEPARTMENT MANAGER / ADMINISTRATOR]
[PROVIDER NAME]
[PROVIDER MAILING ADDRESS]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

                    FORMAL 30-DAY NOTICE
              OF INTENT TO FILE SMALL-CLAIMS ACTION

RE: Account #[ACCOUNT NUMBER]
    Patient: [PATIENT FULL NAME]
    Date(s) of service: [DATE OF SERVICE]
    Disputed amount: $[TOTAL DISPUTED AMOUNT]

Dear [PROVIDER NAME]:

This letter serves as formal notice that I intend to file a civil action against [PROVIDER NAME] in [STATE SMALL-CLAIMS COURT NAME — e.g. Tennessee General Sessions Court] if the disputed charges on the above-referenced account are not corrected within thirty (30) days from the date of this letter.

Chronology of good-faith resolution efforts:

- [DATE] — Initial bill received.
- [DATE] — Written request for itemized statement sent (certified mail tracking #[NUMBER]).
- [DATE] — Itemized statement received / itemization request remained unanswered.
- [DATE] — Formal dispute letter sent (certified mail tracking #[NUMBER]) identifying [N] specific findings with supporting evidence.
- [List all subsequent contacts, calls, follow-up letters, with dates and tracking numbers.]

To date, I have received no substantive response addressing the disputed charges.

Disputed charges (incorporated by reference from my [DATE] dispute letter):

[Concise restatement of the disputed line items and the total disputed amount.]

Legal basis:

- Uniform Commercial Code § 2-305(2) requires that an open-price term be fixed in good faith. The charges identified in my prior letter exceed fair-market rates for these CPT codes by [N]× in this geographic area.
- [If applicable: state hospital itemization statute] required production of an itemized statement within thirty (30) days of my request.
- [If applicable: No Surprises Act, Public Law 116-260, prohibits balance billing in the circumstances identified.]
- [If applicable: state unfair claims settlement practices statute.]

If this matter is not resolved by [DATE 30 DAYS FROM TODAY], I will file a claim in [STATE SMALL-CLAIMS COURT NAME] seeking:

1. Reduction of the disputed amount ($[TOTAL DISPUTED AMOUNT]) to fair-market rates;
2. Recovery of my filing fee (approximately $[FILING FEE]) and service-of-process costs;
3. Any additional remedies permitted by law, including pre-judgment interest.

Economic analysis for your consideration:

The disputed amount is $[TOTAL DISPUTED AMOUNT]. Defending a small-claims case in [STATE] typically costs a corporate defendant several hundred dollars per hour in legal fees, plus staff time preparing for and attending hearing. It is economically rational to correct the disputed charges now.

I have copied this letter to the following regulators and oversight bodies:

- [STATE INSURANCE DEPARTMENT NAME] — Consumer Insurance Services
- [STATE ATTORNEY GENERAL] — Division of Consumer Affairs
- Better Business Bureau (consumer review)
- [If applicable: Centers for Medicare and Medicaid Services — No Surprises Help Desk]

I remain willing to resolve this without court action. I can be reached at [PATIENT PHONE] or [PATIENT EMAIL]. I am preserving all legal rights, including any rights under ERISA § 502(a) for any portion of this dispute that involves an ERISA-covered health plan.

If I do not hear from you within thirty (30) days, I will file in [STATE SMALL-CLAIMS COURT NAME] without further notice.

Sincerely,



[PATIENT FULL NAME]

Account number: [ACCOUNT NUMBER]
Date of service: [DATE OF SERVICE]

cc:
    [STATE INSURANCE DEPARTMENT NAME], Consumer Insurance Services, [ADDRESS]
    [STATE ATTORNEY GENERAL], Division of Consumer Affairs, [ADDRESS]
    Better Business Bureau, [LOCAL BBB OFFICE]
    [If applicable: Centers for Medicare and Medicaid Services, No Surprises Help Desk]

Enclosures: copies of prior correspondence and certified-mail receipts; itemized bill with disputed lines highlighted; fair-market price evidence
```

---

## Placeholders and rendering notes

- For Tennessee, `[STATE SMALL-CLAIMS COURT NAME]` is "Tennessee General Sessions Court" and `[FILING FEE]` is approximately "$55-$150 depending on county." For other states, the LLM looks these up using `references/laws_state_template.md`.
- The CC list is meaningful. The LLM should populate real agency names and mailing addresses, not generic placeholders. Send actual copies to those CC'd agencies via certified mail; the cc-line on the letter is what creates the pressure.

## Pre-flight check before sending

The LLM should confirm with the patient:

1. The disputed amount is within the state's small-claims limit (Tennessee: $25,000).
2. The state's statute of limitations has not run (typically 3-6 years for breach of contract).
3. The patient is actually prepared to file if the provider does not respond. The threat must be credible.

## Follow-up

The LLM logs this with `action_type = "30day_warning_sent"`. If 30 days pass without resolution, transition the bill's `next_action` to `small_claims`.
