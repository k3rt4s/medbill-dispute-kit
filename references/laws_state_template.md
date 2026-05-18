# State-law template

How to build a state-law layer for a state the kit doesn't yet have a dedicated file for. The fully-worked example is Tennessee at [`laws_state_tn.md`](laws_state_tn.md); Georgia at [`laws_state_ga.md`](laws_state_ga.md). Use those two as models when adding new states.

**The LLM must warn the patient that any state-law citation produced from this template should be verified against the state's official code website before mailing.** Wrong citations in dispute letters weaken the patient's position.

## When to use this file

- The patient's state does not yet have a dedicated `laws_state_<two-letter>.md` file.
- A contributor is building a new state pack and wants a checklist of what to find.

## Required items per state

A complete state pack covers all of:

### 1. Hospital itemization statute

- **Citation:** the state's statute requiring providers to furnish itemized bills on request
- **Response deadline:** 30 days is common; some states are 60
- **Request window:** how long after discharge a patient may request

If the state has no such statute, say so explicitly — the patient still has the federal Hospital Price Transparency Rule (45 CFR Part 180) as a fallback, but the state-law leverage is weaker.

### 2. Unfair Claims Settlement Practices Act

- **Citation:** most states have a near-identical version of the NAIC model act
- **Private right of action?** Critical: in many states (including Tennessee), this is **regulator-only**. In others (e.g. Texas under Chapter 541 of the Insurance Code) it gives the consumer a private cause of action. The state pack must say which.

### 3. Bad-faith remedy

- **Citation:** the statute or, in some states, the common-law bad-faith cause of action
- **Demand-and-wait requirement:** how long must the insurer be in default before suit?
- **Penalty/damages:** typical penalty cap, attorneys' fees, punitives availability
- **ERISA preemption:** flag that bad-faith state-law claims are usually preempted for ERISA-covered self-funded plans

### 4. State surprise-billing statute (if broader than federal NSA)

- Some states (CA AB 72, NY Article 49, TX SB 1264, MD all-payer, WA Balance Billing Protection Act, GA HB 888) have broader protections than the federal floor. Where state law is broader, it usually still applies — the federal Act is a floor, not a ceiling.
- Where no broader state law exists, say so; the federal No Surprises Act stands alone.

### 5. Ground-ambulance protection

The federal NSA explicitly excludes ground ambulance. Some states (CA, MD, NY, OH, others) have closed this gap. Most have not. Verify and document the state's posture.

### 6. State insurance department complaint contact

- Office name (varies: Department of Insurance, Department of Commerce and Insurance, Office of the Commissioner of Insurance, etc.)
- Phone (consumer line)
- Online complaint portal URL
- Mailing address
- Email
- Authority: confirm they have jurisdiction over fully-insured health plans (they do); flag that they do **not** have jurisdiction over ERISA-covered self-funded plans (in which case route to DOL EBSA at 1-866-444-3272)

### 7. State attorney general consumer protection

- Phone
- Online complaint portal
- Authority over providers, hospitals, and debt collectors under the state's UDAP (Unfair and Deceptive Acts and Practices) act

### 8. Small-claims court

- Court name (Justice Court, Magistrate Court, Civil Court, General Sessions Court, Small Claims Court — terminology varies)
- Jurisdictional limit
- Typical filing fee
- Attorney rules: required, permitted, or prohibited

### 9. Statute of limitations

- Written contract — most states 4 to 6 years
- Oral contract — usually shorter
- The relevant citation (for the 30-day warning letter and any small-claims filing)

### 10. Medical-debt credit-reporting protections (state-level)

- Does the state restrict medical debt on credit reports beyond the 2022 voluntary bureau changes? NY (2024) is the leading example; CO, IL have variants.
- Cite the statute if it exists.

### 11. Charity-care / financial-assistance state statutes

- IRS § 501(r) is the federal floor for non-profit hospitals (see `laws_federal.md`)
- Some states (WA, MD, IL, CT, NY, NJ, CA, OR) have additional state-level charity-care requirements
- Verify and document

### 12. Hospital lien statute

- Most states allow hospitals to file liens against personal-injury settlement proceeds
- Rarely relevant to general billing disputes, but important if the bill stems from an accident

## Resources for finding the equivalents

- **Justia state codes:** [law.justia.com/codes](https://law.justia.com/codes/) — searchable by state
- **Cornell Legal Information Institute:** [law.cornell.edu](https://www.law.cornell.edu/)
- **State insurance department directory (NAIC):** [content.naic.org/state-insurance-departments](https://content.naic.org/state-insurance-departments)
- **State attorney general directory (NAAG):** [naag.org/find-my-ag](https://www.naag.org/find-my-ag/)
- **State court small-claims directory:** the state's judicial-branch website (Google "[State] small claims court limit")
- **State surprise-billing legislation tracker:** [commonwealthfund.org](https://www.commonwealthfund.org/) and [napbc-natlhealthlaw.org](https://healthlaw.org/) publish state-by-state summaries

## Warning the LLM must surface

After looking up a state-specific citation for the first time in a session, the LLM must say:

> I found the citation through public sources, but state law changes and citations can be reorganized. Before mailing this letter, please verify the statute number on your state's official code website or with a local consumer-law attorney. For a high-stakes letter, free 30-minute consultations are common via the state bar referral service.

This is not optional. Citing a wrong statute number in a dispute letter weakens the patient's position. Better to write "the applicable [State] hospital itemization statute" if uncertain than to cite the wrong number.

## Contribution checklist for new state packs

A PR adding a new `laws_state_<xx>.md`:

1. Covers all 12 required items above (or says explicitly "no such statute in this state").
2. Sources every citation with a URL.
3. Notes the date the contributor last verified the citations.
4. Follows the structure of `laws_state_tn.md` and `laws_state_ga.md`.
5. Adds an entry to `BUILD_PLAN.md` marking the state shipped.
6. Adds an entry to `CHANGELOG.md` under the next version block.
