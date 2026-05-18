# Worked example — one session, three bills

A synthetic patient walking through one full session with the kit loaded into an LLM. The patient's name and details are fictional. The flow shown here mirrors `llm/workflow.md`.

---

## Setup

The patient has the kit loaded into their LLM of choice (Claude or ChatGPT with file uploads, a local model with a context window of at least 64k tokens). They've uploaded `llm/system_prompt.md`, the `rules/` folder, `references/laws_federal.md`, `references/laws_state_tn.md`, all of `schemas/`, all of `templates/`, and `tracker/tracker_template.csv`. The patient is in Tennessee.

They start the session with no prior tracker (this is their first time).

---

## Turn 1 — Patient

> I have three medical bills I want to dispute. I'm in Tennessee.

## Turn 1 — LLM

> Got it. I'm going to follow the workflow in `llm/workflow.md`. State-law defaults will be Tennessee per `references/laws_state_tn.md`. Upload the bills when you're ready. If you have photos, PDFs, scanned paper, or even pasted text, all are fine. If you have an Explanation of Benefits (EOB) from your insurance company that matches any of these bills, upload that too.

---

## Turn 2 — Patient uploads three bill images

Bills uploaded:

- **Bill A:** "TriExample General Hospital" — $1,500 patient balance after insurance, statement date 2026-04-30, dates of service 2026-03-15 through 2026-03-17 (a 3-day inpatient stay), Blue Example Health PPO listed as insurance, no itemized breakdown shown on the summary statement.
- **Bill B:** "Example ER Physicians of TN" — $485 patient balance, same dates of service 2026-03-15, listed as "professional services," coded 99285.
- **Bill C:** "ABC Collections Agency" — $52 claimed balance, lists "AcmeLab" as the original creditor, dated last week, marked as "first written notice."

## Turn 2 — LLM (Phase 1, intake)

> Reading the bills. Initial extraction:
>
> **Bill A** — TriExample General Hospital, inpatient hospital stay 2026-03-15 to 2026-03-17. Account number 327430524. Balance $1,500.00. Statement date 2026-04-30, payment due 2026-05-30. Insurance shown: Blue Example Health. The statement is a summary; I don't see itemized line items.
>
> **Bill B** — Example ER Physicians of TN, professional fee from emergency physicians at the same hospital on 2026-03-15 (the first day of the stay). Account QP-555-9988. Balance $485.00. Coded CPT 99285 (Level 5 ED visit).
>
> **Bill C** — ABC Collections Agency, claiming $52.00 on behalf of "AcmeLab." First written notice. Service date not yet known.
>
> Two important relationships before we build the tracker:
>
> 1. Bills A and B almost certainly belong to the same hospital encounter (same dates, same facility). I'll link them under encounter_id E-2026-001.
> 2. Bill C is the only one from a third-party collector. Different playbook — we have a 30-day FDCPA validation window.
>
> Confirm the extracted fields look right, or tell me what to correct, and I'll save these rows to the tracker.

## Turn 3 — Patient

> Looks right. The hospital was Saint Example Medical Center, but they bill as "TriExample General Hospital" — same thing.

## Turn 3 — LLM (Phase 2, diagnosis)

> Saved. Adding a note to Bill A's `notes` field. Now I'm running the diagnosis checks on each.
>
> **Bill A — findings:** `no_itemization`. You only have a summary; we need the itemized bill before we can check for upcoding, duplicates, or services not received. Tennessee Code Annotated § 68-11-220 entitles you to one within 30 days of a written request.
>
> **Bill B — findings:** `possible_upcoding_99285`. CPT 99285 requires medical decision-making of high complexity per the AMA's 2023 E/M guidelines (see `references/cpt_codes_em.md`). Can you tell me roughly how long you spent with the ED physician on 2026-03-15 and what they treated you for? That'll let me confirm whether the coding looks right.
>
> **Bill C — findings:** the bill is from a third-party collector, not the original lab. FDCPA § 1692g gives you 30 days from receipt to demand verification, and during that period they cannot collect. We need to use that window now. I'll also want to know: do you remember receiving lab services from AcmeLab on or near a specific date?

---

## Turn 4 — Patient

> The ER doc spent maybe 15 minutes with me. They diagnosed an ear infection, gave me a prescription, sent me home. The hospital stay was for something else that came up the next day. And I never used AcmeLab — at least not that I remember. AcmeLab might be associated with my primary care doctor's office?

## Turn 4 — LLM

> Three updates to the tracker:
>
> **Bill A** — keeping `no_itemization` as the only finding for now. Once we get the itemized statement, we'll rerun the checks.
>
> **Bill B** — `possible_upcoding_99285` is now `likely_upcoding_99285`. A 15-minute encounter for an ear infection with a prescription is at most Level 3 (99283), possibly Level 2 (99282). The price difference is significant. I'll set up a dispute.
>
> **Bill C** — `services_not_received_suspected`. Combined with FDCPA validation, that's the lead. The collector will need to produce a signed order or requisition; if they can't, the debt isn't yours.
>
> Phase 3, action selection. Sorted by deadline:
>
> 1. **Bill C** — `letter_fdcpa_validation.md`, due **before [DATE 30 DAYS FROM TODAY's RECEIPT]** (FDCPA window).
> 2. **Bill A** — `letter_itemization_request.md`, today or tomorrow. Tennessee statute gives the hospital 30 days to respond.
> 3. **Bill B** — `letter_initial_dispute.md` with the upcoding finding, today or tomorrow. Don't wait.
>
> All three letters need to be sent by certified mail with return receipt. Cost: about $4.50 each at USPS. Bring the letters and your envelopes; the post office gives you the tracking numbers.
>
> Want me to draft all three? I'll render the letters and you can review before printing.

---

## Turn 5 — Patient

> Yes, draft all three.

## Turn 5 — LLM (Phase 4, draft)

> Rendering three letters. I'm using:
>
> - Your name and address from the bills (let me know if there's a current address that differs).
> - Tennessee Code § 68-11-220 for the itemization request.
> - AMA 2023 E/M guidelines for the upcoding dispute on Bill B.
> - FDCPA § 1692g for Bill C.
>
> Anything marked `[NEEDS USER INPUT]` is something I need from you before mailing. After each letter I'll list those.

[The LLM produces three letters, each in a fenced `letter` block per `llm/output_contracts.md`. Each letter has `[NEEDS USER INPUT: certified mail tracking #]` since the patient hasn't been to the post office yet, plus a few other gaps to fill in.]

> Before you print these:
>
> - The FDCPA letter (Bill C) is time-sensitive. The 30-day clock runs from when *you received* the collector's letter, not when they sent it. When did the ABC Collections letter arrive in your mailbox?
> - Bill C — you said you don't remember using AcmeLab. Pull your insurance EOB history (your insurance portal will have it). If there's no EOB for AcmeLab, that's evidence supporting "service not received."
> - Bill B — I cited "approximately 15 minutes" in the dispute language. Once you remember the actual visit duration more precisely, we can tighten it up.

---

## Turn 6 — Patient

> The collector letter arrived on April 30. I haven't checked my EOBs yet but I will.

## Turn 6 — LLM

> Good — that means the FDCPA 30-day window closes on May 30. We have time. I'll log the dates in the action log.
>
> Recap of state to save when we wrap:
>
> - 3 bills tracked, all `open`.
> - Bill C is `next_action = file_fdcpa_validation`, due May 30.
> - Bill A is `next_action = request_itemization`, due 30 days after the hospital receives your request.
> - Bill B is `next_action = initial_dispute`, due 15 business days after the hospital receives.
>
> Anything else this session?

---

## Turn 7 — Patient

> No, this is enough. Save my progress.

## Turn 7 — LLM (Phase 5, wrap)

> Tracker saved. Here it is:
>
> ```csv
> bill_id,encounter_id,provider_name,provider_type,account_number,statement_date,date_of_service_start,date_of_service_end,total_billed,current_balance,insurance_carrier,in_network_status,was_emergency,findings,next_action,next_action_due,last_action_taken,last_action_date,certified_mail_last,status,last_statement_date,notes
> B-2026-001,E-2026-001,TriExample General Hospital,hospital,327430524,2026-04-30,2026-03-15,2026-03-17,12500.00,1500.00,Blue Example Health,in_network,false,no_itemization,request_itemization,2026-05-30,received_bill,2026-04-30,,open,2026-04-30,"Also known as Saint Example Medical Center; 3-day inpatient stay"
> B-2026-002,E-2026-001,Example ER Physicians of TN,emergency_physician,QP-555-9988,2026-04-15,2026-03-15,,485.00,485.00,Blue Example Health,in_network,true,likely_upcoding_99285,initial_dispute,2026-05-30,received_bill,2026-04-15,,open,2026-04-15,"15-min visit for ear infection; CPT 99285 not supported by encounter complexity"
> B-2026-003,,ABC Collections Agency,other,COL-12345,2026-04-30,,,52.00,52.00,,unknown,false,services_not_received_suspected,file_fdcpa_validation,2026-05-30,received_bill,2026-04-30,,open,2026-04-30,"Third-party collector claiming AcmeLab; patient does not recall service. FDCPA 30-day window closes 2026-05-30."
> ```
>
> **Save your tracker as:** `tracker_2026-05-18.csv`
>
> **Session summary:** Three bills logged, three letters drafted. Two are time-sensitive (FDCPA on Bill C, dispute on Bill B if you want to move fast).
>
> **Overdue:** none.
>
> **Due in the next 7 days:** none — Bill C's FDCPA window is the most urgent at 12 days away, but it's not due tomorrow.
>
> **Highest-priority next action:** print the three letters tonight, sign them, take them to the post office tomorrow morning with $15 for certified mail. Bring me the tracking numbers and I'll update the tracker.
>
> **Save the three letter files** to your own folder (not in the tracker). The tracker holds state; letters live alongside it.

---

## What this example shows

- **Phase 1 intake** consolidates raw uploads into structured bill records and links related bills under one `encounter_id`.
- **Phase 2 diagnosis** runs every applicable check and asks targeted questions only when needed. The model didn't ask the patient to describe every detail of the hospital stay; it asked specifically about the ED visit because that's where the upcoding finding lived.
- **Phase 3 action selection** sorts by deadline. FDCPA's 30-day window is the most leveraged deadline of the three, so it leads.
- **Phase 4 draft** produces complete letters, not checklists. The patient walks away with paper ready to mail.
- **Phase 5 wrap** emits the complete CSV (all rows, even unchanged), gives an explicit save filename, and surfaces the single highest-priority next action.

## What this example does not show

- **Resume next session.** When the patient comes back, they upload `tracker_2026-05-18.csv` and the LLM reads it first; that flow is documented in `llm/system_prompt.md` Conversation entry.
- **Multi-state cases.** If the patient had bills from both TN and GA, the LLM would route each bill to its own state pack.
- **Insurance denials.** If a bill came with a claim denial, the LLM would route it through `rules/07_appeal_insurance_denial.md` and the ERISA appeal template instead of the standard dispute path.
- **No Surprises Act violations.** If Bill B had been an out-of-network ED physician at an in-network hospital, the LLM would use `letter_no_surprises_violation.md` instead of the upcoding dispute. Bill C as a collector debt would still go through FDCPA validation.

Read `llm/workflow.md` for the full process and `rules/` for the individual decision points the model is applying.
