# Template — Combined dispute across all providers in one encounter

Use when a single care encounter generated bills from three or more separate providers (typical pattern: hospital facility + ER physician group + radiology + anesthesia + pathology + ambulance) and the dispute theory is the same for all of them. The classic case is a No Surprises Act ancillary-provider scenario: the patient went to an in-network facility, every billable clinician inside that facility is treated as in-network for cost-sharing purposes under § 300gg-111(b), and any out-of-network ancillary bill is balance-billed in violation of federal law.

Rather than mail four separate dispute letters that each have to be re-argued from scratch, this template generates one combined letter that:

- Names every provider in the encounter and the bill from each.
- States the encounter-wide legal theory once.
- Lists each disputed amount in a per-provider table.
- Demands a coordinated response.

The recipient is one of: (a) the in-network facility, when the facility's role is to ensure compliance for ancillary providers under the federal NSA disclosure rules; (b) the patient's plan, when the plan should have processed the entire encounter under NSA in-network cost-sharing; or (c) every provider in the encounter in parallel, with each receiving a copy showing the full encounter context. The drafter selects based on the dispute theory.

---

```letter
[PATIENT FULL NAME]
[STREET ADDRESS]
[CITY, STATE ZIP]
Phone: [PATIENT PHONE]
Email: [PATIENT EMAIL]

[DATE]

[RECIPIENT — chosen by the drafter from one of: the in-network facility, the plan administrator, or each provider in parallel]
[RECIPIENT MAILING ADDRESS]

VIA CERTIFIED MAIL — RETURN RECEIPT REQUESTED
USPS Tracking: [CERTIFIED MAIL TRACKING NUMBER]

cc by certified mail with full enclosure set:
    Each other provider in the encounter (see Section II below)
    [PATIENT'S HEALTH PLAN — Member Services]
    [STATE] Department of Insurance, Consumer Services
    Federal No Surprises Help Desk (cms.gov/nosurprises)

RE: Combined encounter dispute under the No Surprises Act —
    Patient: [PATIENT FULL NAME]
    DOB: [DOB]
    Member ID: [MEMBER ID]
    Encounter ID (internal): [ENCOUNTER_ID]
    Date(s) of service: [DATE OF SERVICE]
    In-network facility: [FACILITY NAME]
    Total balance asserted across all providers: $[TOTAL ASSERTED]

To [RECIPIENT NAME]:

I received care during the encounter referenced above. The facility, [FACILITY NAME], is in-network on my health plan, [INSURER NAME], member ID [MEMBER ID]. Following the encounter, I received separate bills from [N] different providers connected to the encounter, summarized in Section II below. Several of those providers are billing me at out-of-network rates, in apparent violation of the federal No Surprises Act, 42 U.S.C. § 300gg-111(b), which protects patients from balance-billing for out-of-network ancillary services rendered at an in-network facility.

This letter addresses the encounter as a whole rather than each bill in isolation. The legal posture below applies uniformly across the providers identified.

I. Encounter-wide legal posture

The patient went to an in-network facility for the date(s) of service above. The facility was contractually in-network on the patient's plan; the patient's cost-sharing for the visit was expected to be the in-network cost-sharing under the plan.

Under § 300gg-111(b), if a patient receives ancillary services at an in-network facility from an out-of-network ancillary provider (anesthesiology, emergency medicine, pathology, radiology, neonatology, laboratory services, or assistant-surgery services), the patient's cost-sharing is required to be calculated as if the ancillary provider were in-network. The provider may not balance-bill the patient for any amount above that cost-sharing.

The notice-and-consent exception under § 300gg-111(d) does not apply because (a) the service categories above are statutorily excluded from the notice-and-consent exception, and (b) no compliant 72-hour-advance written notice was provided to me.

II. Providers in the encounter

[The drafter renders this table from `tracker.csv` rows sharing `encounter_id` with the canonical bill. One row per provider.]

| #   | Provider             | Provider type       | Network status (per EOB) | Billed | EOB allowed | Patient cost-sharing per EOB | Provider asserting | Spread     |
| --- | -------------------- | ------------------- | ------------------------ | -----: | ----------: | ---------------------------: | -----------------: | ---------: |
| 1   | [FACILITY NAME]      | hospital_facility   | in_network               | $[X1]  | $[Y1]       | $[Z1]                        | $[Z1]              | $0         |
| 2   | [ER PHYSICIAN GROUP] | emergency_physician | out_of_network           | $[X2]  | $[Y2]       | $[Z2]                        | $[X2]              | $[X2 − Z2] |
| 3   | [RADIOLOGY GROUP]    | radiology           | out_of_network           | $[X3]  | $[Y3]       | $[Z3]                        | $[X3]              | $[X3 − Z3] |
| 4   | [ANESTHESIA GROUP]   | anesthesiology      | out_of_network           | $[X4]  | $[Y4]       | $[Z4]                        | $[X4]              | $[X4 − Z4] |

Total billed across all providers: $[SUM X]
Total EOB-allowed: $[SUM Y]
Total cost-sharing per EOB: $[SUM Z]
Total balance-billed to me above in-network cost-sharing: $[SUM SPREAD]

III. Demand

I demand:

1. **For the in-network facility** (provider 1, if applicable): confirm in writing whether the facility provided me with the required No Surprises Act disclosure regarding the network status of ancillary providers, and, if not, take such steps as your facility's compliance program requires.

2. **For each out-of-network ancillary provider** (providers 2–N above): rebill me at no more than the in-network cost-sharing amount per the EOB, withdraw any prior statements asserting the balance-billed amount, and withdraw any collection referral on this account. The plan-vs-provider dispute over the spread is properly resolved through the federal IDR process under 45 CFR § 149.510, not by balance-billing me.

3. **For the plan** (CC'd above): if any of the ancillary providers' claims were adjudicated as out-of-network cost-sharing in violation of § 300gg-111, reprocess the claims at in-network cost-sharing and notify the providers of the reprocessing.

4. **Confirmation in writing** of the steps each provider and the plan is taking, within thirty (30) calendar days of the date stamped on the USPS certified-mail receipt above.

IV. Coordinated handling

Because the encounter involves multiple providers and the same legal theory across all, I respectfully ask that the recipients coordinate their response with each other. A patient should not have to litigate the same NSA argument N separate times against N separate billing departments for a single visit. The kit's `tracker.csv` for this encounter is available on request to demonstrate the documentation chain.

V. Response window and consequence of non-response

Please respond within thirty (30) calendar days of the date of the USPS certified-mail receipt. If a substantive written response addressing the encounter as a whole is not received within that window, I will:

1. File a complaint with the federal No Surprises Help Desk at cms.gov/nosurprises or 1-800-985-3059, attaching this letter and the encounter table above.

2. File a complaint with the [STATE] Department of Insurance, Consumer Services, asserting that each out-of-network ancillary provider is balance-billing in violation of § 300gg-111.

3. Forward this letter to the U.S. Department of Labor, Employee Benefits Security Administration, asserting that the plan failed to protect me from balance-billing during the encounter.

4. If court action becomes necessary, file a single declaratory-judgment action joining all providers in the encounter, citing the encounter-wide theory above.

VI. Privilege

This letter is sent under Federal Rule of Evidence 408 as an offer of compromise. No statement is an admission of liability for any amount. This letter is not a release of any claim and is sent without prejudice.

Please direct your response to the address above.

Sincerely,



[PATIENT FULL NAME]

DOB: [DOB]
Member ID: [MEMBER ID]
Encounter ID (internal): [ENCOUNTER_ID]
Date(s) of service: [DATE OF SERVICE]

Enclosures:
A — Copy of the bill from each provider listed in Section II
B — Copy of the EOB for each claim corresponding to those bills
C — Line-item benchmark analysis across the encounter
D — (If applicable) Copy of any NSA disclosure that was provided at registration

Coordinated CC list (each receives the full enclosure set with a cover note identifying this letter as the encounter-wide combined dispute):
- [PROVIDER 1 NAME], [PROVIDER 1 ADDRESS]
- [PROVIDER 2 NAME], [PROVIDER 2 ADDRESS]
- [PROVIDER 3 NAME], [PROVIDER 3 ADDRESS]
- [PROVIDER 4 NAME], [PROVIDER 4 ADDRESS]
- [PATIENT'S HEALTH PLAN], [PLAN ADDRESS]
- [STATE] Department of Insurance, [DOI ADDRESS]
```

---

## Placeholders and rendering notes

- `[RECIPIENT]` — when the encounter has a clearly in-network facility, address to the facility's patient-experience executive or compliance officer. When the encounter involves out-of-network billing across multiple ancillary providers without a single anchor facility, address to the patient's plan administrator with each provider on the CC list. The drafter picks based on whether the canonical bill's biller_slug matches a facility-type provider and the bill's `in_network_status` is `in_network`.
- The Section II table is built from `tracker.csv` filtered to the canonical bill's `encounter_id`. The drafter sums billed, EOB-allowed, and cost-sharing across the table for the totals row.
- The encounter must have at least one provider type that qualifies for NSA ancillary protection (anesthesiology, emergency_physician, pathology, radiology, neonatology, lab, assistant_surgery). If the encounter does not, this template does not apply; use the per-provider `letter_no_surprises_violation.md` or `letter_initial_dispute.md` instead.

## Before sending

The drafter confirms:

1. The encounter has 3+ distinct biller_slugs sharing an `encounter_id`.
2. At least one provider in the encounter is OON and billing above the EOB-allowed amount.
3. The facility is in-network. If the facility is OON, the legal theory shifts to ordinary out-of-network billing without the NSA ancillary protection, and this template is the wrong tool.
4. The EOBs for the encounter are on file (matched via `matches.csv`). Without EOBs the encounter-wide network analysis cannot be supported.

## Parallel actions (same day as mailing)

- File the federal No Surprises complaint at cms.gov/nosurprises and the state DOI complaint via `templates/complaint_state_doi.md`, both referencing the encounter ID.
- Forward the encounter table to the patient's plan ERISA fiduciary contact via `templates/letter_insurance_appeal_erisa.md` if the plan adjudicated any of the claims at OON cost-sharing.

## Follow-up

- 30 days from postmark, no coordinated response → escalate to federal complaint + state DOI complaint as outlined in Section V.
- If only some providers respond and resolve: keep the encounter open in `tracker.csv` and proceed against the non-responding providers individually via `letter_dispute_reply.md`.
- If the plan re-adjudicates at in-network cost-sharing: confirm the new EOBs match across all providers; some providers will need a corrected bill from the plan before they will withdraw their statement.
