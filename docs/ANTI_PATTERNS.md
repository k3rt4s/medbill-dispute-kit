# Anti-patterns

Common mistakes patients make when disputing medical bills. Reading these once before starting a dispute saves significant grief. The kit's other rules tell you what to do; this document tells you what not to do.

## Paying the first bill

The single most common patient-side mistake. The bill arrives, the due date is in three weeks, and the patient pays. Once paid, the leverage to dispute drops by an order of magnitude. The provider now has the money; you are now seeking a refund, which is harder than refusing payment.

**Don't do this.** Read the bill, identify any issues, dispute before paying. If the bill turns out to be correct and you can afford it, pay then.

## Setting up auto-debit on a billing portal

You went to the hospital's payment portal, saw "make this easy — auto-debit each month," and clicked yes. Now the provider takes money from your account every month regardless of any dispute.

Auto-debit removes your single biggest piece of leverage in any dispute. The kit's standard letters explicitly refuse auto-debit because of this dynamic.

**Don't do this.** If you set up auto-debit and now want to dispute, cancel it first — through your bank if necessary. Then dispute.

## Calling the billing department instead of writing

Phone calls do not create a paper trail. The billing-department rep can say anything to you, and if you can't prove it later, it didn't happen. The kit's escalation ladder runs on certified-mail letters because the certified-mail tracking and the letter content are reproducible evidence.

**Don't do this exclusively.** A phone call to clarify what's on a bill is fine. A phone call to negotiate is fine if you immediately follow up with an email or letter summarizing the conversation. A phone call to dispute and accept whatever the rep tells you is not.

## Ignoring the bill entirely

The bill arrives, the patient is overwhelmed, and they put it in a drawer. Eventually it goes to collections, the credit-report clock starts running, and the original dispute leverage is gone.

**Don't do this.** If you can't address a bill today, at minimum: write the issue date on your calendar, set a reminder for two weeks out, file the bill where you'll see it. Then dispute, even if briefly.

## Disputing in vague terms

"This is too much, please reduce it" is not a dispute. The billing department cannot act on it. The kit's letters identify specific issues (this CPT code is upcoded, this line is duplicated, this price is X times the local fair-market rate) because specificity is what produces movement.

**Don't do this.** Identify the specific issue. Cite the specific authority. Make a specific dollar offer.

## Threatening too much, too early

"I will sue you in small claims court if you don't reduce this by 95%" sent in your first letter looks unhinged. The kit's escalation ladder has stages for a reason: initial dispute is polite-and-specific; 30-day warning is firm-and-formal; small claims filing is the actual escalation.

**Don't do this.** Match your posture to the stage of the dispute. Initial letters are matter-of-fact. Warning letters are formal. Court filings are clinical.

## Threatening too little

The opposite mistake: sending three letters that all say "could you please consider reducing this?" The provider has no reason to take you seriously if you never escalate. The 30-day warning is the kit's recommended escalation tool because it imposes a real cost on the provider while keeping the door open to settlement.

**Don't do this.** Escalate when escalation is warranted. Polite forever produces polite ignoring.

## Conceding on the first counter-offer

The provider responds with a 25% reduction. Patient says "great, I'll take it" — even though the disputed amount was 60% of the bill. The provider's first counter-offer is rarely their best.

**Don't do this.** Reasonable rule of thumb: if their offer is below half the disputed amount, push back once with new evidence or a new argument. They will often go higher.

## Conceding non-disputed amounts as a "good-faith gesture"

The patient owes $400, disputes $300, and decides to pay the undisputed $100 immediately as a sign of good faith. Two problems: (a) the partial payment can be interpreted as an admission that the rest is owed if the negotiation fails; (b) once you've paid the undisputed portion, the provider has less incentive to settle the disputed portion.

**Don't do this.** Wait for resolution before paying any portion. If you absolutely must pay something, do it via a clearly-marked "payment under protest, without prejudice to claims" with a written note.

## Letting the statute of limitations run

State statutes of limitations for medical-debt actions are typically 3-6 years. If a hospital sues you within that window, defending is harder than disputing pre-suit. Don't let an unresolved dispute drift until the provider files a collection lawsuit.

**Don't do this.** If a dispute is stuck, escalate with the 30-day warning. If the warning fails, file in small claims yourself. Don't let the provider drive the timeline.

## Confusing the EOB with a bill

The Explanation of Benefits from your insurance company is not a bill. The line "your responsibility: $300" on an EOB is an estimate; the provider's actual bill is what you owe. If you pay $300 to your insurance company because the EOB said so, you have paid the wrong entity for nothing.

**Don't do this.** Wait for the provider's bill. Verify it matches the EOB. Then dispute or pay.

## Paying based on a verbal estimate

Provider says "this'll be about $500." Patient agrees. Bill arrives at $3,200. Patient is told "well, that was just an estimate."

**Don't rely on verbal estimates.** For scheduled non-emergency services where you're uninsured or self-pay, you are entitled to a Good Faith Estimate in writing under the No Surprises Act. Get it in writing. If the final bill exceeds it by $400+, you can file PPDR (see `rules/11_ppdr_walkthrough.md`).

## Going to small claims for the wrong dispute

Small claims is for definite-amount disputes between $100 and the state limit ($5,000-$25,000 depending on state). Trying to use small claims to litigate complex insurance-denial appeals, medical-malpractice claims, or class-action-suitable patterns is the wrong forum.

**Don't do this.** ERISA denials go to federal court. Medical malpractice goes to regular civil court with counsel. Mass-pattern disputes go to consumer-protection authorities. Small claims is for "this bill is wrong by this amount" cases.

## Filing bankruptcy as a first move

Bankruptcy discharges medical debt cleanly but carries a 7-10 year credit-report mark and can affect employment, housing, and security clearances. It's appropriate when the debt is genuinely unmanageable; it's not the first move on a $400 bill you disagree with.

**Don't do this.** Bankruptcy is the kit's last move, not the first. Dispute, apply for charity care, hardship-negotiate, and only then consider bankruptcy. The exception is patients already in crisis — see `rules/17_bankruptcy_and_medical_debt.md`.

## Hiring a "medical billing advocate" who takes a percentage

A subset of paid billing-advocate services take a percentage of any reduction they obtain. Some are good; many are mediocre at best. For a $500 dispute, a 30% fee on a 50% reduction nets the patient $175 vs $250 if they had done it themselves. For a $50,000 dispute, the math changes.

**Don't reflexively pay for what you can do yourself.** The kit exists because most disputes are within the reach of a patient with patience, certified mail, and the right templates. For high-stakes cases, paid advocates may be worth it; verify their track record before committing to a percentage fee.

## Posting bill details on social media

A patient posts a picture of their EOB to Facebook to complain. The post is public. The EOB contains PII: name, MBI, account numbers, sometimes diagnoses.

**Don't do this.** Even if you want to share your story publicly, redact aggressively first. The kit's `.gitignore` excludes bill files because they should not be in public version control. Social-media posts are version control with no privacy.

## Letting the LLM make a key legal-citation decision without verification

The LLM is imperfect. State-law citations change. Recent legislation may not be in the model's training data. If the LLM cites a statute number that turns out to be wrong, your dispute letter weakens.

**Don't do this.** For high-stakes letters, verify any specific statute citation against the state's official code website (Justia, Cornell LII, or the state's own legislative database). The kit's state packs note the verification date for exactly this reason.

## Treating the dispute as a personal battle with the billing-department rep

The billing-department rep on the phone is not your enemy. They are a worker following a script and a flowchart, with limited authority and no personal stake. Getting angry at them produces nothing useful and may color the documented record of your dispute.

**Don't do this.** Be respectful. Get the rep's name and call-time. Ask for a supervisor only if the conversation has gone in circles. Save the firmness for the written letters where it does work.

## Not saving the tracker

The patient runs three sessions with the LLM, then loses the tracker CSV. Next session has no continuity. Things slip.

**Don't do this.** Save the tracker after every session with the date in the filename. Keep a copy on your local computer and (if you accept the privacy trade-off) backed up to a private cloud folder. The tracker is the durable record; everything else flows from it.

## Forgetting that the provider can be wrong about state law

The hospital's billing-department supervisor may genuinely believe their state's hospital-itemization statute is different from what it actually is. They may say "we don't have to itemize until 60 days," even though the statute says 30. Don't accept their representation as definitive; verify against the actual statute.

**Don't do this.** When the rep cites state law, ask them for the specific statute number. Look it up. If they're wrong, point it out (politely) and proceed.
