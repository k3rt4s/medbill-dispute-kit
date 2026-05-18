# Template — State insurance department / consumer affairs complaint

Use to file a formal complaint with the patient's state insurance department or attorney general's consumer protection division. This template is the **content** of the complaint; the LLM renders it as a letter, and the patient submits it via the state's online portal (preferred), email, or mail. Most state portals accept attached letters.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]
Date of birth: [DOB]

[DATE]

[STATE INSURANCE DEPARTMENT OR AG OFFICE — full name]
[OFFICE ADDRESS]

[For Tennessee, default:
 Tennessee Department of Commerce and Insurance
 Consumer Insurance Services
 500 James Robertson Parkway, 4th Floor
 Nashville, TN 37243-0574
 — or submit online at https://www.tn.gov/commerce/insurance/consumer-resources/file-a-complaint.html ]

Submitted via: [ONLINE PORTAL / CERTIFIED MAIL — TRACKING NUMBER]

RE: Formal complaint —
    Complainant: [PATIENT FULL NAME]
    Subject company: [PROVIDER OR INSURER NAME]
    [INSURER STATE LICENSE #, if known]
    [PROVIDER NPI, if available]
    Account / Claim #: [NUMBER]
    Date(s) of service: [DATE OF SERVICE]
    Amount in dispute: $[AMOUNT]

Dear [Department / Office]:

I am filing a formal complaint against [PROVIDER OR INSURER NAME] regarding [the bill / the denial of claim] referenced above. I respectfully request that your office investigate and require the company to bring its conduct into compliance with applicable law.

I. Summary of facts (chronological)

1. On [DATE], I [received the service / submitted the claim / received the bill / received the denial].
2. On [DATE], I [first action — phone call / letter / email] requesting [resolution].
3. On [DATE], [provider/insurer's response or non-response].
4. [Continue as needed.]
5. As of the date of this complaint, the dispute remains unresolved.

II. Specific conduct at issue

[The LLM picks the applicable category or categories.]

[CATEGORY A — Failure to provide itemized bill]

[PROVIDER] failed to provide an itemized statement within [thirty (30) days for Tennessee] of my written request dated [DATE]. This appears to violate [STATE STATUTE — e.g. Tennessee Code § 68-11-220].

[CATEGORY B — Balance billing in violation of the No Surprises Act]

[PROVIDER] balance-billed me for [emergency services / out-of-network ancillary services at an in-network facility / out-of-network air ambulance] in apparent violation of the federal No Surprises Act (Public Law 116-260, Division BB, Title I, effective January 1, 2022). A parallel complaint has been filed with the federal No Surprises Help Desk.

[CATEGORY C — Improper claim denial / unfair claims practice]

[INSURER] denied claim #[NUMBER] dated [DATE] for [SERVICE]. The denial reason cited, [REASON], does not match the plan's Summary Plan Description and was issued without [a reasonable investigation / adequate clinical review]. This appears to violate [STATE STATUTE — e.g. Tennessee Code § 56-8-105 (unfair claims practices)].

[CATEGORY D — Bad-faith failure to pay]

[INSURER] has refused to pay claim #[NUMBER] for more than sixty (60) days following my written demand dated [DATE], without substantial legal grounds. This conduct appears to violate [STATE BAD-FAITH STATUTE — e.g. Tennessee Code § 56-7-105].

[CATEGORY E — Price gouging / charges set in bad faith]

[PROVIDER] charged amounts substantially in excess of fair-market rates and the provider's own posted prices under the federal Hospital Price Transparency Rule (45 CFR Part 180), in violation of the duty to set an open-price term in good faith under UCC § 2-305(2). Specifics are documented in the attached materials.

[CATEGORY F — Hospital Price Transparency non-compliance]

[HOSPITAL] does not appear to have published a complete machine-readable file of standard charges as required by 45 CFR § 180.50. A parallel complaint has been filed with the Centers for Medicare and Medicaid Services.

III. Relief requested

I respectfully ask that your office:

1. Open an investigation into the conduct described above.
2. Require [PROVIDER OR INSURER] to [issue a corrected itemized bill / reprocess the claim at in-network cost-sharing / approve the disputed service / refund the overpayment].
3. Take any enforcement action appropriate under applicable law.
4. Provide me a copy of the company's written response to this complaint, as well as your office's findings, once the investigation is complete.

IV. Attempts to resolve directly

Prior to filing this complaint, I attempted to resolve the matter directly with [PROVIDER OR INSURER] by the following means:

- [DATE], [phone / letter] — [summary; certified-mail tracking # if applicable]
- [DATE], [phone / letter] — [summary]
- [continue]

V. Documents enclosed

- Copy of the disputed bill / Explanation of Benefits / denial letter
- Copies of my prior dispute correspondence with the provider/insurer
- Certified-mail tracking receipts demonstrating delivery
- Evidence of fair-market pricing (Turquoise Health, FAIR Health Consumer, etc.) for price-related complaints
- [Other supporting documents]

VI. Authorization

I authorize the [Department / Office] to share this complaint and supporting documents with [PROVIDER OR INSURER] for purposes of investigation and response.

I declare under penalty of perjury under the laws of [STATE] that the foregoing is true and correct to the best of my knowledge.

Sincerely,



[PATIENT FULL NAME]

Date of birth: [DOB]
Address: [STREET ADDRESS, CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

Enclosures (list)
```

---

## Placeholders and rendering notes

- Many state portals collect this information through web forms rather than a free-form letter. The LLM should produce both: (a) the letter, for the patient's records and as an upload if the portal accepts attachments, and (b) a paragraph-by-paragraph summary suitable for pasting into a web form's "describe your complaint" field.
- For Tennessee, the default agency is TDCI Consumer Insurance Services (insurance issues) or the Tennessee AG Division of Consumer Affairs (provider/collector issues under the Tennessee Consumer Protection Act). The LLM should pick based on whether the bad actor is a licensed insurer or a provider/collector.
- The "under penalty of perjury" line is appropriate for most state-AG submissions and many state-DOI submissions, but check the specific portal's requirements. If the portal has its own attestation, omit the line from the letter to avoid conflict.

## Categories and routing

- **Tennessee:**
  - Insurer disputes (denials, slow pay, unfair practices) → TDCI
  - Provider / hospital / debt collector → TN AG Consumer Affairs
  - Hospital MRF non-compliance → CMS (federal) in parallel
  - Dental insurance issues → TDCI (post-2024 § 56-2-305 enforcement)
- For other states, the LLM uses `references/laws_state_template.md` to find the right agency.

## Follow-up

The LLM logs this with `action_type = "state_doi_complaint_filed"` and notes the complaint number once the patient provides it after submission. State complaints typically receive a confirmation number immediately and a substantive response within 30-90 days.
