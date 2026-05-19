# Worked example — small claims court filing

A patient files in small claims court against a hospital that ignored a documented dispute. Walks through the kit's small-claims escalation: filing decision, evidence preparation, the hearing, and post-judgment collection.

Names and details are fictional. The patient is in Tennessee, where small claims is the General Sessions Court with a $25,000 jurisdictional limit (the highest in the US).

---

## Background

Patient had a hospital walking-boot dispute that began six months ago. Initial dispute letter (referencing $385 charge for an Aircast SP walking boot retailing at $48-$75 nationally) was ignored. 30-day warning letter cc'd to Tennessee TDCI and the AG's consumer-protection division was also ignored. Patient's tracker shows:

- Bill: $385 (DME Direct, the medical-device vendor associated with the hospital)
- Disputed amount: $310 (over the high end of fair-market $75)
- Letters sent: initial dispute (certified, response 0); 30-day warning (certified, response 0)
- Time since first letter: 6 months
- Total spent on certified mail: ~$15

Disputed amount well under Tennessee's $25,000 small-claims limit. Patient decides to file.

---

## Session 1 — Filing decision and preparation

### Turn 1 — Patient

> The walking boot people never responded. Time to file in small claims.

Uploads current `tracker_dispute.csv` showing the open dispute.

### Turn 1 — LLM

> Reading the tracker. Bill B-walking-boot, disputed amount $310, two certified letters sent with no response, 30-day warning window expired 5 months ago. You're well within Tennessee's 6-year breach-of-contract SOL.
>
> Pre-flight check before filing:
>
> 1. **Is the disputed amount worth filing for?** $310 minus the ~$120 filing/service fee leaves $190 net if you win. Plus the time spent preparing and attending. For some people that's not worth it; for others the principle and the deterrent effect are worth more than the dollars. Your call.
> 2. **Are you sure the case is in good shape?** Two certified letters with no response is strong on paper; the defendant cannot claim they didn't know.
> 3. **Are you prepared to attend the hearing?** Tennessee General Sessions is informal but a non-appearance is a default loss.
>
> Want to proceed?

### Turn 2 — Patient

> Yes. Worth doing on principle.

### Turn 2 — LLM

> Filing checklist for Tennessee General Sessions Court — Civil docket:
>
> 1. **Court of proper venue.** Where DME Direct is registered or where the dispute occurred. From the address on the bills, DME Direct is in Davidson County. We file in Davidson County General Sessions Court.
> 2. **Civil warrant form.** That's General Sessions's name for the small-claims complaint. Available at the clerk's office and online.
> 3. **Defendant's name as legally registered.** Look up DME Direct's registered agent with the Tennessee Secretary of State at [tnbear.tn.gov](https://tnbear.tn.gov). Use the registered legal name and the registered-agent address for service.
> 4. **Filing fee.** Davidson County: approximately $76 for the civil warrant plus ~$45 for sheriff service. Total ~$121.
> 5. **Statement of claim.** Short, factual, no legal jargon. Three sentences max.
> 6. **Exhibits to gather.** I'll list them after the filing.
>
> Let me draft the statement of claim for you.

### Turn 3 — LLM (statement of claim)

> ```text
> Statement of Claim
>
> On [date of service], Plaintiff was charged $385 by Defendant for an Aircast SP walking boot, an item that retails between $48 and $75 nationally. Plaintiff disputed the charge in writing on [date1] and [date2], both via certified mail, requesting reduction to a fair-market amount of $75. Defendant did not respond.
>
> Plaintiff seeks recovery of $310 (the difference between $385 charged and $75 fair-market amount), plus filing fee and service costs. Plaintiff relies on Uniform Commercial Code § 2-305(2) (open price term must be set in good faith) and the Tennessee Consumer Protection Act (Tenn. Code Ann. § 47-18-104) prohibition on unfair and deceptive trade practices.
> ```
>
> This is short on purpose. General Sessions doesn't require detailed pleading; the case will be presented orally with exhibits at the hearing.

### Turn 4 — LLM (exhibits checklist)

> Bring three copies of every exhibit to the hearing (one for the judge, one for the defendant, one for you). Label A, B, C, etc.
>
> - **Exhibit A:** The original bill from DME Direct, $385.
> - **Exhibit B:** Your initial dispute letter dated [date1], with the USPS certified-mail green card showing receipt.
> - **Exhibit C:** Your 30-day warning letter dated [date2], with the USPS certified-mail green card showing receipt.
> - **Exhibit D:** Printout of Amazon, Walmart, and one medical-supply-site listings for the same Aircast SP walking boot, dated and timestamped. Three sources is better than one.
> - **Exhibit E:** Printout of the relevant Tennessee Consumer Protection Act provision (Tenn. Code Ann. § 47-18-104) and UCC § 2-305 from Justia or another authoritative source.
> - **Exhibit F:** Your tracker showing the chronology of contact attempts and no responses. Optional but tells the story well.
>
> Don't bring anything irrelevant. The judge wants a clean story.

### Turn 5 — Patient

> Got it. Filing tomorrow.

### Turn 5 — LLM (Phase 5)

> Updating the tracker:
>
> - `next_action` for the walking-boot bill → `small_claims`
> - `next_action_due` → date of the hearing (clerk will assign after filing; typically 30-60 days out)
> - `action_type` logged: `small_claims_prep`
>
> Save the tracker. Bring me your filing confirmation (case number, hearing date) next session.

---

## Session 2 — One week later

### Turn 1 — Patient

> Filed. Case #GS-2026-cv-12345. Hearing on July 22, 2026 at 9:00 AM, Courtroom 3B. Total filing + service was $121.

### Turn 1 — LLM

> Logged:
>
> - `action_type = "small_claims_filed"`
> - Date filed: today
> - Hearing date: 2026-07-22 9:00 AM Courtroom 3B
> - Filing/service fee: $121 (this will be sought as part of the recovery)
>
> Two weeks before the hearing, we'll do a mock walkthrough. Save the tracker.

---

## Session 3 — Two weeks before hearing

### Turn 1 — Patient

> Hearing is in two weeks. Walk me through it.

### Turn 1 — LLM

> Tennessee General Sessions civil hearings are informal. Here's the rough sequence:
>
> 1. **Calendar call.** The clerk reads case names. You answer "present, Your Honor." If the defendant doesn't answer, you may get a default judgment without a hearing — be prepared either way.
> 2. **If defendant appears.** The judge will call your case to the bench or have you both sit down at a table. Each side gets a few minutes to present. Strict rules of evidence don't apply; the judge weighs what's helpful.
> 3. **Your presentation.** Two to three minutes. Stick to your story. I'll give you a script.
> 4. **Defendant's response.** They'll respond. Don't interrupt. Take notes.
> 5. **Your rebuttal.** Brief. Address their points; don't repeat what you already said.
> 6. **Judge's questions.** Answer them directly. "Yes Your Honor / No Your Honor / I don't know Your Honor / The bill is at Exhibit A."
> 7. **Judgment.** May be on the spot or by mail. In Davidson County General Sessions, on-the-spot is common.
>
> Your presentation script:
>
> > "Your Honor, on [date of service], I was charged $385 by [DME Direct] for an Aircast SP walking boot — Exhibit A. The same item retails at $48 to $75 nationally — Exhibit D. I disputed the charge in writing on [date1] and [date2] by certified mail, requesting reduction to $75 — Exhibits B and C. The defendant did not respond.
> >
> > Under Uniform Commercial Code Section 2-305, when a contract leaves the price open, the seller must fix it in good faith and the price must be reasonable. A 5-to-7x markup over the retail price is not reasonable and is not in good faith. I'm asking the court to enter judgment for $310 plus my filing costs of $121."
>
> Total: about 90 seconds. Long enough to make the point, short enough that the judge doesn't lose patience.

### Turn 2 — Patient

> What if they show up and argue?

### Turn 2 — LLM

> Possible counter-arguments from a billing-department rep:
>
> 1. **"The patient agreed to the chargemaster price at admission."** Counter: the admission form did not disclose specific item prices. UCC § 2-305 applies when the price is left open; signing a generic agreement does not establish the price.
> 2. **"The chargemaster reflects cost recovery for uninsured charity care."** Counter: this is a policy argument, not a legal one. The hospital's accounting choices do not justify charging this individual patient more than the fair-market price for a single item.
> 3. **"The patient could have brought their own walking boot."** Counter: the walking boot was issued at discharge as part of care. The patient was not offered alternatives.
> 4. **"This is a contract dispute, not a UCC dispute."** Counter: in Tennessee, the UCC at Tenn. Code Ann. § 47-2-305 applies to sales of goods. A walking boot is a good.
> 5. **"$385 is reasonable in the hospital context."** Counter: the kit's Exhibit D shows what reasonable looks like nationally for this specific item. The judge can weigh that.
>
> Don't get drawn into rhetorical fights. Be polite, address each point briefly, return to your facts.

### Turn 3 — Patient

> What if I lose?

### Turn 3 — LLM

> Defendant gets a judgment for $385 (the bill amount). They can collect via wage garnishment, bank levy, or hospital lien — same as if you'd never filed. Net cost to you of filing: $121 in filing/service fees plus a few hours of time. Some judges award the defendant a token cost (rare for small-claims).
>
> Tennessee allows de novo appeal to Circuit Court within 10 days of judgment. For $310, the appeal cost and effort generally outweigh the recovery. Most people don't appeal.

### Turn 4 — Patient

> What if I win and they don't pay?

### Turn 4 — LLM

> Possible. Judgment-collection steps after a Tennessee General Sessions win:
>
> 1. **Wait 10 days** for the defendant's appeal window to close.
> 2. **Request a writ of execution** from the clerk. Tells the sheriff to levy on the defendant's bank account or seize personal property.
> 3. **Garnishment of bank account or wages.** Defendant is a business; bank-account garnishment is easier than wage garnishment.
> 4. **Examination on judgment.** Court order requiring the defendant's officer to appear and disclose assets.
> 5. **In rare cases — judgment lien on the defendant's real property.** For a $310 judgment this is overkill but the option exists.
>
> Most corporate defendants pay the judgment promptly once the appeal window closes. Refusing to pay a $310 judgment costs them more in legal fees than paying.

---

## Hearing day

The patient appears at 9:00 AM. Defendant — represented by a billing-department supervisor, not an attorney — appears. The judge calls the case at 9:18.

Patient presents the script. Defendant argues #1 (the admission-form agreement) and #5 (chargemaster reasonable). Patient rebuts briefly. Judge asks two questions: (a) was the walking boot returned? (no), (b) did the patient sign for the walking boot specifically? (no, only a generic admission form).

Judge enters judgment for $310 plus $121 in costs. Total: $431.

---

## Session 4 — One week after hearing

### Turn 1 — Patient

> Won the case. They paid the $431. Closing this out.

### Turn 1 — LLM

> Logging:
>
> - `action_type = "small_claims_hearing"`, outcome = won, judgment $310 + $121 costs
> - `action_type = "payment_received"`, $431 from DME Direct
> - Bill status → `settled`
> - Notes: judgment entered 2026-07-22; payment received 2026-07-29
>
> Final tracker. Save as `tracker_2026-07-29.csv`.
>
> **Session summary:** $310 disputed → $431 recovered (including filing fees). Net: $310 minus the time spent. Time was probably 8-12 hours over six months. Hourly rate equivalent: $25-$40 if measured purely in dollar terms; significantly higher when accounting for the precedent set with DME Direct on future patients' bills.

---

## What this example shows

- **The escalation ladder works.** Three letters and a small-claims filing produced a result that two letters and silence did not. The threat of filing produced no movement, but the actual filing did.
- **Preparation is mostly paperwork.** Statement of claim under 200 words; exhibits assembled in an hour; mock-presentation practice in 15 minutes.
- **The hearing is brief.** Forty-five minutes including calendar call; the actual presentation was 90 seconds.
- **Most corporate defendants pay after losing.** A $310 judgment is uneconomic to appeal.

## What this example does not show

- **A case where the defendant is well-counseled.** Larger hospitals sometimes send attorneys; the dynamic changes but the patient's case does not weaken.
- **A case the patient loses.** It happens. The cost is the filing fee and time; not the underlying bill (which the patient still owed before filing).
- **Multi-defendant cases.** Common for hospital encounters where the hospital, physician group, and equipment vendor are separate entities. Each is a separate suit (or one suit with multiple defendants, depending on the case).
- **Cases exceeding the state small-claims cap.** Above the cap, the patient is in regular civil court with formal pleading and discovery, and an attorney is usually appropriate.

See [`walkthrough.md`](walkthrough.md) for a simpler three-bill single-session walkthrough, [`multi_encounter_walkthrough.md`](multi_encounter_walkthrough.md) for a multi-encounter multi-session walkthrough, and [`insurance_denial_walkthrough.md`](insurance_denial_walkthrough.md) for an ERISA appeal walkthrough.
