# Template — Request EOB from insurer

Use when a provider bill has arrived but the corresponding Explanation of Benefits (EOB) from the patient's health plan has not. The EOB is needed to verify that the bill matches what the plan adjudicated, to confirm in-network cost-sharing was applied, and to surface any No Surprises Act protection that may apply.

The letter is sent to the plan administrator. A copy is mailed to the billing provider so they know the patient is gathering documentation and should not escalate the bill to collections during the dispute.

The kit also expects an email courtesy notice to the biller if their email is on file. The letter body references that email so the biller has a record of both channels.

Legal basis cited: ERISA § 104(b)(4) / 29 U.S.C. § 1024(b)(4) (right of plan participants to written copies of plan documents on request, including EOBs). State right-of-access language can be added under the relevant state insurance code; the kit's `references/laws_state_*.md` files list those.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

[INSURER NAME] — Member Services / Plan Administrator
[INSURER MAILING ADDRESS]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

RE: Request for Explanation of Benefits — Plan participant [PATIENT FULL NAME]
    Member ID: [MEMBER ID]
    Group: [GROUP NAME / NUMBER]
    Date(s) of service: [DATE OF SERVICE RANGE]
    Provider that billed me: [BILLER NAME]
    Provider invoice / account number: [PROVIDER ACCOUNT NUMBER]
    Amount the provider is asking me to pay: $[BILL BALANCE]

Dear Member Services:

I am a participant in the plan referenced above. The provider listed
above has sent me a bill for the date(s) of service shown, but I have
not received the Explanation of Benefits for that claim. I am writing
to formally request the EOB so I can verify the bill against the
plan's adjudication before paying.

Specifically, I request:

1. A complete EOB covering the claim(s) submitted by the provider for
   the date(s) of service above, showing:
   - the claim number(s) assigned by the plan,
   - the billed amount, allowed amount, plan payment, and patient
     responsibility for each service line,
   - the in-network or out-of-network status of the provider as
     adjudicated,
   - any application of deductible, copay, or coinsurance,
   - any No Surprises Act protections applied.
2. A copy of the plan's coverage rules that were applied to this
   claim, including any out-of-network cost-sharing rules.
3. Confirmation of whether the provider is in-network on my plan.

This request is made pursuant to ERISA § 104(b)(4) (29 U.S.C.
§ 1024(b)(4)), which entitles plan participants to receive copies of
plan documents in writing within thirty (30) days of a written
request. If my plan is governed by state insurance law rather than
ERISA, this request is also made under the applicable state insurance
right-of-access provision.

I am separately notifying the billing provider that I have requested
this EOB. I have asked them to place a hold on collection activity
while I gather the documentation needed to verify their bill, and I
have informed them by email at [BILLER EMAIL OR "no email address
available — paper copy mailed only"] that this written request has
been mailed today.

Please send the requested documents to the address above. If anything
is missing or delayed, please contact me at the phone or email above.

Sincerely,



[PATIENT FULL NAME]

Member ID: [MEMBER ID]
Date(s) of service: [DATE OF SERVICE RANGE]

cc:
    [BILLER NAME], [BILLER ADDRESS] — by certified mail with this letter enclosed
    [BILLER EMAIL OR omit this line] — by email of even date, courtesy notice
```

---

## Placeholders and rendering notes

- `[INSURER NAME]` and `[INSURER MAILING ADDRESS]` come from the EOB-side address block of any earlier EOB the patient has from the same plan. If no prior EOB is on file, the patient's insurance card carries the member services address.
- `[BILLER EMAIL OR ...]` is filled from the bill itself; if no email is on file, the conditional text replaces the email reference.
- The kit ships a parallel courtesy email at `templates/email_biller_eob_requested.md` that the patient sends from a personal account. Both the letter and the email reference each other so the paper trail is symmetric.

## Parallel actions to take the same day

1. **Mail this letter certified to the insurer.** Save the green card.
2. **Mail a paper copy of this letter to the billing provider as a "cc" recipient.** They need to know it's pending; this is the trigger that the dispute is in motion.
3. **Email the biller from `templates/email_biller_eob_requested.md`** (if a biller email is on file). The email re-states what the certified letter says and gives them an alternate channel to acknowledge.
4. **Log the action** in tracker.csv: set `eob_request_sent_date`, `eob_request_tracking_number`, `current_status = gathering_evidence`.

## Follow-up

- Insurer must respond within 30 days under ERISA. If they do not, escalate to a 30-day warning, then a complaint to the state insurance department + a complaint to the DOL Employee Benefits Security Administration (1-866-444-EBSA).
- When the EOB arrives, drop the PDF in `inbox/`, re-run the pipeline; the EOB gets routed and the bill row's `has_eob` flips. The next dispute action becomes available.
