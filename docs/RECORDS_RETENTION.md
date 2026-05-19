# Records retention — what to keep and for how long

Medical-bill disputes can take months. Statutes of limitations on related claims run 3-10 years. A patient who throws away a key document early may lose a dispute later. This document is a one-page guide to what to keep, where to keep it, and for how long.

## The short version

**Keep everything related to a medical encounter for at least the longest applicable statute of limitations in your state — typically 6-10 years.** When in doubt, keep.

## What to keep

### From the provider

- **Bills (all versions).** Every statement, including follow-up reminders, has a date stamp that proves what you were told and when.
- **Itemized bills.** Requested via the kit's itemization-request template. These are the core dispute evidence.
- **Pre-service estimates and Good Faith Estimates.** These establish what you expected to pay.
- **Treatment plans you signed.** These define what was agreed to.
- **Discharge papers.** Includes diagnoses, instructions, and (importantly) any documentation of inpatient vs. observation status for Medicare patients.
- **Medical records you've requested.** Get them once, keep them. Re-requesting later costs time and money.
- **Letters from billing departments.** Both their unsolicited communications and their responses to your inquiries.

### From the insurer

- **Insurance ID cards** for the relevant year.
- **Plan documents.** Summary of Benefits and Coverage (SBC), Summary Plan Description (SPD) for ERISA plans, the full plan booklet if you have it.
- **EOBs (Explanation of Benefits).** Every one, even for paid claims, for at least the SOL.
- **Denial letters.** Critical evidence in any appeal.
- **Appeal decisions** (internal and external).
- **Network confirmation letters** — if you confirmed network status in writing before service, keep that.

### From regulators and courts

- **Confirmation numbers** for any state DOI or AG complaint.
- **CMS complaint confirmations** for No Surprises Act, Hospital Price Transparency, or EMTALA.
- **HHS OCR complaint** confirmation for HIPAA or Section 1557.
- **Court filings, judgments, certified-mail receipts** if the dispute reached small claims or higher courts.

### Your own contemporaneous notes

- **Service log.** What happened, who you saw, how long. Written soon after the encounter; memory degrades fast.
- **Phone-call log.** Date, time, person's name, summary of what was said. Especially important for verbal "we'll handle this" promises that vanish.
- **Letters you sent.** Keep copies of every letter, with the certified-mail tracking number.
- **Letters they sent.** With dates and envelopes (date stamps can matter).

### Evidence of fair pricing

- **Screenshots** of Turquoise Health, FAIR Health Consumer, Healthcare Bluebook, GoodRx, Amazon, etc., with timestamps. Pricing changes over time; the screenshot fixes the comparison in time.
- **Hospital MRF excerpts** if you downloaded them — the hospital's own published prices for the procedures at issue.
- **Medicare allowable rates** for the relevant CPT codes — printed from the CMS Physician Fee Schedule Lookup.

### Settlement and payment records

- **Settlement letters** confirming reduced amounts. Critical: must state expressly that the settled amount discharges the entire account.
- **Payment confirmations** (canceled checks, bank statements, credit-card statements showing the payment).
- **Receipts** for certified-mail postage (these are recoverable as costs in small claims).

## What to keep but rarely needs digging out

- Insurance cards from prior years (until SOL passes)
- Pharmacy receipts for prescriptions tied to a contested encounter
- Travel and lodging receipts if treatment was out of area (sometimes relevant in damages calculations)

## What you can probably throw away

- **Marketing material** from the provider's billing partner.
- **Generic newsletters** the hospital sends.
- **Duplicate statements** (keep one of each unique statement; you can throw away clear duplicates as long as the dates are noted).

When in doubt, keep. Digital storage is cheap; recreating a destroyed document is expensive.

## How long to keep

### General rule: keep through the longest applicable statute of limitations

| Type of claim                                           | Statute of limitations (typical)         | Document retention guide                |
| ------------------------------------------------------- | ---------------------------------------- | --------------------------------------- |
| Breach of written contract (most medical-bill disputes) | 3-10 years by state                      | Keep at least 10 years                  |
| Breach of oral contract                                 | 2-6 years by state                       | Keep at least 6 years                   |
| ERISA claim under § 502(a)                              | Federal rule, generally 6 years          | Keep at least 8 years                   |
| Medical malpractice                                     | 1-3 years by state (with discovery rule) | Keep at least 5 years                   |
| Bad-faith claims                                        | 2-6 years by state                       | Keep at least 8 years                   |
| Federal criminal fraud (rare)                           | 5-10 years                               | Keep indefinitely if fraud suspected    |
| HIPAA right-of-access violation                         | 180-day OCR complaint window             | Keep at least 1 year (faster)           |
| FDCPA violation                                         | 1 year                                   | Keep 2 years (collector communications) |
| EMTALA civil action                                     | 2 years from violation                   | Keep at least 3 years                   |

**Conservative rule for the kit:** keep medical-billing dispute records for at least **10 years from the date of last activity**. Some patients keep longer. Storage is cheap.

### After bankruptcy

If you file Chapter 7 and discharge medical debt, keep the bankruptcy paperwork (discharge order, schedules) **forever**. You may need to prove discharge if a creditor surfaces later.

### After a confirmed settlement

If a dispute settled and the provider confirmed the account is closed:

- Keep the settlement confirmation **at least 7 years**. Some collectors try to collect on settled accounts years later; the settlement letter is the dispositive evidence.
- Keep the payment confirmation **at least 7 years**.

### After a small-claims judgment

Keep the judgment, the writ of execution (if any), and any payment-receipt evidence **at least 10 years**. Judgments are enforceable for long periods under state law.

## Where to keep

### Physical originals

A binder or accordion folder per major encounter. Labels by date. Stored in a fire-resistant location (a safe is overkill for most; a metal filing cabinet is sufficient).

### Digital copies

Scan everything that matters (use the phone camera if no scanner). Store in:

- A dedicated folder on your computer with a clear naming convention (e.g., `2026-03-15_TriExample-Hospital_ER-visit/`)
- A backup location: external drive, encrypted cloud storage. Not a public cloud folder; medical paperwork contains PII.
- (Optional, paranoid) Print critical documents to PDF/A or other long-term archival formats. Standard PDFs from phone scans are usually fine for 10+ years.

### Naming convention

The kit's recommended naming pattern:

```text
medical-records/
├── 2026-03-15_TriExample-Hospital_ER-visit/
│   ├── 01_original-bill_2026-04-30.pdf
│   ├── 02_itemized-bill_2026-05-15.pdf
│   ├── 03_EOB_BCBS_2026-04-22.pdf
│   ├── 04_my-dispute-letter_2026-05-18.pdf
│   ├── 05_certified-mail-receipt_2026-05-18.pdf
│   └── 06_their-response_2026-06-05.pdf
└── tracker_2026-05-18.csv
```

Numbered prefixes for chronological order. Dates in filenames for instant context.

## Tracker integration

The kit's tracker CSV is the index. Each row's `notes` field should reference where the original documents are stored (file path or physical-folder label). The tracker should not contain the documents themselves; that bloats it and creates PII problems if shared.

## What to scan immediately

For ongoing disputes, scan and digitize within 48 hours of receipt:

- Any provider or insurer correspondence
- Any certified-mail green card returned to you
- Any payment confirmation
- Any settlement letter

A document lost in a stack of paper before you scanned it is functionally lost.

## Disposal

When the retention period has passed and you're confident the dispute is concluded:

- **Shred** anything with personal identifiers (Medicare Beneficiary ID, account numbers, full date of birth)
- **Securely delete** digital copies (not just trash-can deletion; use a file-shredder utility for PII)
- **Keep** any settlement confirmations and bankruptcy discharge orders indefinitely

## Insurance: a special note

Keep insurance documents for **the year of coverage plus 10 years**. Even after switching plans, prior years' EOBs and plan documents may matter for disputes that surface later. Insurance companies routinely change their position on prior denials; old EOBs are evidence.

## When the patient is incapacitated or deceased

For caregivers and executors:

- Keep all medical-bill documents at least through probate plus 5 years.
- Medical debt is dischargeable in bankruptcy and not personally inherited (except in narrow filial-responsibility-statute states); but creditors will try.
- Settlement and discharge documents protect the estate from future collection attempts.

## One more thing

If the kit's escalation ladder reached small claims and beyond, **keep the entire file forever**. The judgment is your defense if anyone tries to collect later, and the file is your record of how it went.
