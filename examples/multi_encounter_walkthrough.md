# Worked example — multi-encounter, resume across sessions

A patient with bills from two distinct hospital encounters, processed across three sessions over six weeks. Demonstrates encounter linking, deduplication of follow-up statements, end-of-session save, and start-of-session resume.

Names and details are fictional.

---

## Session 1 (Week 0) — Initial intake

### Setup

Patient has kit loaded into their LLM with the Tennessee state pack and the federal-law reference. No prior tracker.

### Turn 1 — Patient

> I just got hit with a stack of bills from two separate hospital trips this year. I'm in Tennessee. I want to triage all of them.

### Turn 1 — LLM

> Got it. I'll follow `llm/workflow.md` Phase 1 — intake first, then diagnosis, then action selection. Tennessee state-law defaults apply per `references/laws_state_tn.md`. Go ahead and upload the bills. If you have the dates of each hospital trip, telling me up front will help me link related bills under shared encounter IDs.

### Turn 2 — Patient

Uploads 7 bill images/PDFs. Says: "First trip was an ER visit in March, second was a planned outpatient surgery in May."

### Turn 2 — LLM (Phase 1)

> Extracting. Initial grouping by date of service:
>
> **Encounter A — March 14, 2026 ER visit:**
> - Hospital facility fee from Saint Example Hospital — $4,200 balance, account #SE-771234
> - Emergency physician group bill from "Acme ED Physicians" — $612 balance, CPT 99284, account #AEP-2026-0314
> - Radiology professional fee from "Imaging Specialists of TN" — $185 balance, account #IST-99-771
>
> **Encounter B — May 7, 2026 outpatient surgery:**
> - Hospital surgical fee from Saint Example Hospital — $8,950 balance, account #SE-883344
> - Anesthesia bill from "Tennessee Anesthesia Associates" — $1,420 balance, account #TAA-2026-0507
> - Pathology bill from "Lab Partners" — $310 balance, account #LP-883300
>
> **Encounter unclear — single statement uploaded:**
> - Walking boot from "DME Direct" — $385 balance, account #DME-665544. The bill doesn't reference a date of service. Was this related to either encounter, or separate?

### Turn 3 — Patient

> The walking boot was from the May surgery — they gave it to me at discharge.

### Turn 3 — LLM

> Adding the walking boot to Encounter B. Both encounters now have linked rows under shared encounter_ids: E-2026-001 (March ER) with 3 bills, E-2026-002 (May surgery) with 4 bills. Phase 2 diagnosis next.

### Turn 4 — LLM (Phase 2)

> Findings per bill:
>
> **Encounter A:**
> - Saint Example Hospital ($4,200): `no_itemization` — summary statement only.
> - Acme ED Physicians (CPT 99284, $612): `possible_upcoding_99284` until I know the visit details. How long were you with the ED doctor and what did they treat?
> - Imaging Specialists ($185): no findings yet; small amount, probably correct.
>
> **Encounter B:**
> - Saint Example Hospital surgical ($8,950): `no_itemization`.
> - Tennessee Anesthesia ($1,420): need to know — is Saint Example in-network for your plan? If yes, this anesthesia bill may be a No Surprises Act case if Tennessee Anesthesia is out-of-network at an in-network facility.
> - Lab Partners ($310): no findings yet.
> - DME Direct walking boot ($385): `price_above_fair_market` — retail walking boots are $40-$120 on Amazon and at medical supply stores. I'll need to look up the specific brand and model on the bill to nail down a fair-market comparison.

### Turn 5 — Patient

> ED visit was about 20 minutes for a sprained ankle. Saint Example is in-network on my BCBS plan. Tennessee Anesthesia, no idea. The walking boot is a "Aircast SP" — I just looked it up.

### Turn 5 — LLM

> Three updates:
>
> - Acme ED Physicians 99284 → `likely_upcoding_99284` confirmed. 20 minutes for a single sprained-ankle complaint is at most Level 3 (99283), possibly Level 2 (99282). Dispute incoming.
> - Tennessee Anesthesia → `no_surprises_ancillary_oon` flagged if confirmed out-of-network. The federal NSA prohibits balance billing by out-of-network anesthesia at in-network facilities. I'll draft the NSA letter assuming OON; if they're actually in-network, we'll switch to a different track.
> - Aircast SP walking boot retails $48-$75 in the US. The $385 charge is 5-8× retail. `price_above_fair_market` confirmed. Dispute will reference the retail price with sources.

### Turn 6 — LLM (Phase 3)

> Action selection across all 7 bills, sorted by deadline:
>
> 1. **Acme ED Physicians ($612, 99284)** — `initial_dispute` with upcoding finding.
> 2. **Tennessee Anesthesia ($1,420)** — `dispute_no_surprises_violation` if confirmed OON. First we should call BCBS to confirm.
> 3. **Saint Example Hospital both encounters** — `request_itemization` for both. Tennessee Code § 68-11-220 gives them 30 days.
> 4. **DME Direct walking boot** — `initial_dispute` with price-gouging finding.
> 5. **Imaging Specialists, Lab Partners** — `monitor` for now; small amounts, likely correct; revisit if Saint Example's itemized bill turns up anything material.
>
> Want me to draft all four letters tonight?

### Turn 6 — Patient

> Yes. I'll call BCBS tomorrow to confirm the anesthesia network status.

### Turn 7 — LLM (Phase 4)

Renders four letters in `letter` fenced blocks, each conforming to the relevant template. All flag `[NEEDS USER INPUT: certified mail tracking #]` since the patient hasn't been to the post office yet.

### Turn 8 — LLM (Phase 5)

> Saving tracker. Here it is — 7 rows under 2 encounter_ids:
>
> ```csv
> bill_id,encounter_id,provider_name,...
> B-2026-001,E-2026-001,Saint Example Hospital,...
> B-2026-002,E-2026-001,Acme ED Physicians,...
> ...
> ```
>
> **Save as:** `tracker_2026-05-18.csv`
>
> **Session summary:** 7 bills logged across 2 hospital encounters. 4 disputes drafted (1 upcoding, 1 No Surprises Act candidate pending insurance confirmation, 1 itemization request × 2 hospitals, 1 price-gouging on walking boot).
>
> **Overdue:** none.
>
> **Due in next 7 days:** none.
>
> **Highest-priority next action:** confirm Tennessee Anesthesia's network status with BCBS, then mail all four letters certified. Bring me the tracking numbers and the network confirmation next session.

---

## Session 2 (Week 1) — Resume, send letters, receive responses

### Turn 1 — Patient

> Back. I confirmed Tennessee Anesthesia was out-of-network. I mailed all four letters last week. Here's my tracker.

Uploads `tracker_2026-05-18.csv`.

### Turn 1 — LLM (Conversation entry)

> Read the tracker. 7 bills, 2 encounters, all open. No overdue items.
>
> Good news on Tennessee Anesthesia being OON — that confirms the No Surprises Act applies. Did you mail the NSA letter and the others?

### Turn 2 — Patient

> Yes, all four certified. Tracking numbers:
> - Acme ED Physicians: 9407XXXXXXXX1234
> - Tennessee Anesthesia: 9407XXXXXXXX1235
> - Saint Example (March): 9407XXXXXXXX1236
> - Saint Example (May): 9407XXXXXXXX1237
> - DME Direct: 9407XXXXXXXX1238

### Turn 2 — LLM

> Saving the tracking numbers to each bill's `certified_mail_last` field and logging the actions:
>
> - Acme ED → `action_type = initial_dispute_letter_sent`, date_sent = 2026-05-20, response_due_by = 2026-06-10
> - Tennessee Anesthesia → `action_type = no_surprises_letter_sent`, date_sent = 2026-05-20, response_due_by = 2026-06-10
> - Saint Example × 2 → `action_type = requested_itemization`, response_due_by = 2026-06-19 (30 days per TN § 68-11-220)
> - DME Direct → `action_type = initial_dispute_letter_sent`, response_due_by = 2026-06-10
>
> Anything new from the providers since?

### Turn 3 — Patient

> Saint Example sent me a letter saying they "received my request and will process within 30 days." Tennessee Anesthesia called and said they're "looking into it." Nothing else.

### Turn 3 — LLM

> Both are good signals — neither is pushing back hard. Logging both as `received` responses. I'll calendar the next checkpoints.

### Turn 4 — Patient

> Also, two more bills arrived this morning. Photos attached.

Uploads two new statements.

### Turn 4 — LLM

> Running dedup against the existing tracker.
>
> **Statement 1** — Acme ED Physicians, account #AEP-2026-0314 (same as existing B-2026-002), balance $612, statement date 2026-05-25. This is a **follow-up statement** for the bill I already have, not a new bill. The dispute is in flight; this is a routine 30-day statement that crossed our letter in the mail. Updating `last_statement_date` on B-2026-002 to 2026-05-25. No new row.
>
> **Statement 2** — From a new entity, "Doctors Imaging Group," account #DIG-2026-0314, balance $415. The date of service is 2026-03-14 — that matches Encounter A (March ER). But Imaging Specialists of TN (B-2026-003) is also from that date. Did you have two separate imaging studies that day, or is this a duplicate billing for the same study?

### Turn 5 — Patient

> I had one X-ray. Looks like both groups are billing me for it.

### Turn 5 — LLM

> That's worth investigating. Two professional fees from two radiology groups for the same X-ray is unusual unless one is the facility and one is the read. Adding Doctors Imaging Group as B-2026-008 under encounter E-2026-001 with `findings = duplicate_line` and asking for clarification before disputing. I'll draft a phone-call script for you to call Doctors Imaging tomorrow and ask: "Who exactly performed the read on the X-ray at Saint Example on March 14? Is your fee for the same read that Imaging Specialists is billing me for, or is this a different service?"

### Turn 6 — Patient

> Will do. Save state.

### Turn 6 — LLM (Phase 5)

> Tracker now has 8 bills across 2 encounters. **Save as:** `tracker_2026-05-25.csv`.
>
> **Session summary:** confirmed Tennessee Anesthesia was OON. Logged 5 sent letters with certified-mail tracking. Identified a potential duplicate-billing situation between Imaging Specialists and Doctors Imaging Group for the same X-ray.
>
> **Overdue:** none.
>
> **Due in next 7 days:** none.
>
> **Highest-priority next action:** call Doctors Imaging Group to clarify the X-ray billing. If it's a duplicate, dispute it; if it's a separate legitimate service, log and monitor.

---

## Session 3 (Week 6) — Responses received

### Turn 1 — Patient

> Update time. Some movement.

Uploads `tracker_2026-05-25.csv`.

### Turn 1 — LLM (Conversation entry)

> Read. 8 bills, 2 encounters. **Overdue:** the 30-day response window for Acme ED Physicians and Tennessee Anesthesia closed on 2026-06-10; if you haven't received a substantive response, we should send 30-day warning letters. **Due in next 7 days:** Saint Example itemization deadline 2026-06-19.
>
> Tell me what's happened.

### Turn 2 — Patient

> Acme ED Physicians wrote back. They recoded the visit to 99283 and reduced my balance from $612 to $385. I'm willing to settle there.
>
> Tennessee Anesthesia reprocessed at in-network — my responsibility dropped to $185 and I'm willing to settle there too.
>
> Saint Example sent itemized bills for both encounters. I haven't reviewed them yet.
>
> Doctors Imaging Group — I called and they confirmed they billed for the same read Imaging Specialists already billed me for. They agreed to withdraw the bill in full.
>
> DME Direct — silence.

### Turn 2 — LLM

> Excellent. Logging:
>
> - **B-2026-002 (Acme ED Physicians):** `action_type = settlement_accepted`, amount $385 (was $612), status → `settled`. Net savings $227.
> - **B-2026-005 (Tennessee Anesthesia):** `action_type = settlement_accepted`, amount $185 (was $1,420). Status → `settled`. Net savings $1,235. The NSA reprocessing was the lever here.
> - **B-2026-008 (Doctors Imaging Group):** `action_type = writeoff_received`, amount $0 (was $415). Status → `closed_written_off`. Net savings $415.
> - **DME Direct (B-2026-007):** still `open`, response was due 2026-06-10 with no response. Next action: send 30-day warning. I'll draft.
> - **Saint Example itemized bills (B-2026-001, B-2026-004):** the itemized statements have arrived; now we run a fresh diagnosis on the line items. Can you upload them?
>
> Running savings to date: $227 + $1,235 + $415 = **$1,877** on 8 bills, with the two largest bills still being examined.

### Turn 3 — Patient

Uploads the two itemized hospital bills.

### Turn 3 — LLM (Phase 2 re-run on itemized data)

> Reviewing line items. Notable findings:
>
> **Saint Example Hospital — March ER (B-2026-001):**
> - "Emergency Room Visit Level 5" (CPT 99285) — $2,800. Coding is wrong; you had a 20-minute visit for a sprain. Saint Example's professional service for the ED is what Acme bills separately; this 99285 charge on the hospital side is the facility code, not the physician code. Facility-side ED level coding follows similar logic. `likely_upcoding_99285_facility` flagged.
> - "Operating Room Services" — $480. You didn't have surgery. `service_not_received_suspected` flagged.
> - Standard pharmacy and basic supplies — no findings.
>
> **Saint Example Hospital — May surgery (B-2026-004):**
> - Surgical suite, anesthesia (facility portion), recovery — all consistent with what you said happened.
> - "Walking boot supply" — $0 charged here (good; the bill went to DME Direct separately).
> - Otherwise itemization looks consistent with an outpatient orthopedic procedure.
>
> So we have two new disputes for B-2026-001 (facility upcoding + operating-room charge for a service not received) and B-2026-004 is mostly clean.

### Turn 4 — Patient

> Let's go for B-2026-001 dispute and the DME Direct 30-day warning.

### Turn 4 — LLM (Phase 4)

Renders two letters. The Saint Example dispute cites the operating-room charge with the patient's recollection plus a request for documentation; the DME Direct 30-day warning notes the prior dispute went unanswered and threatens small claims, cc-ing TDCI and the TN AG.

### Turn 5 — LLM (Phase 5)

> Saving. **Save as:** `tracker_2026-06-29.csv`.
>
> **Session summary:** 3 bills resolved with savings totaling $1,877. 1 new dispute (Saint Example facility-side ER upcoding + OR-charge-for-service-not-received). 1 escalation (DME Direct 30-day warning, en route to small claims if ignored).
>
> **Overdue:** none anymore.
>
> **Due in next 7 days:** the new letters' response windows.
>
> **Highest-priority next action:** mail the two new letters certified; track for replies.

---

## What this example shows

- **Encounter linking:** bills from different providers but the same date of service get a shared `encounter_id` so the patient can see the full cost of a hospital trip.
- **Deduplication on follow-ups:** the routine 30-day reminder from Acme ED Physicians is recognized as the same bill (account number match) and merged into the existing row.
- **Same-date-different-bill discrimination:** Doctors Imaging Group's statement looked like a follow-up but had a different account number; the LLM correctly flagged it for clarification rather than auto-merging.
- **Cross-session continuity:** the patient runs three sessions over six weeks, each starting with the saved tracker. The LLM picks up exactly where the prior session left off.
- **Response-driven re-routing:** when Saint Example's itemized bill arrives, the LLM re-runs the diagnosis on the line items and surfaces new findings (facility upcoding, service not received) that weren't visible on the summary statement.
- **Settlement accounting:** as bills resolve, the savings are tallied. The patient walks away with quantified outcomes.

## What this example does not show

- A small-claims filing (DME Direct's 30-day warning has not yet expired).
- An ERISA insurance-denial appeal (no claim denial in this story).
- A patient outside Tennessee (state-law citations would change).
- A bill that needs Medicare or Medicaid appeals (those follow different procedures — see [`letter_medicare_appeal.md`](../templates/letter_medicare_appeal.md) and [`letter_medicaid_appeal.md`](../templates/letter_medicaid_appeal.md)).

See [`walkthrough.md`](walkthrough.md) for the simpler single-session three-bill example, and [`insurance_denial_walkthrough.md`](insurance_denial_walkthrough.md) for the ERISA-appeal flow.
