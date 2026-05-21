# Reading and using a Summary Plan Description (SPD)

The Summary Plan Description is the federally-required plain-language summary of an ERISA-governed health plan. Every plan participant has a right to receive a copy under ERISA § 102 / 29 U.S.C. § 1022. Plan administrators must furnish the SPD within 90 days of a participant's enrollment and within 30 days of a written request thereafter.

The SPD controls when a billing dispute, claim denial, or subrogation issue turns on plan language. Common reasons to pull the SPD:

- Verify in-network cost-sharing for a No Surprises Act claim (the SPD names the in-network deductible, copay, and coinsurance).
- Identify the plan's prior-authorization rules to see whether a denial was procedurally proper.
- Find the internal appeal procedure deadlines (typically 180 days from adverse determination, but the SPD sets the actual window).
- Find the external review procedure (every plan must offer one; the procedure varies).
- Identify the plan's subrogation / reimbursement / equitable-lien language.
- Identify the plan's "made-whole" and "common-fund" overrides for subrogation claims.
- Identify the plan's funding status (self-funded ERISA vs fully insured) — this determines whether state insurance law overlays apply.

This guide describes what to look for and how to use it.

---

## Where to get the SPD

1. The participant's employer HR/benefits portal. Most large employers post current SPDs in the benefits-elections portal.

2. By written request to the plan administrator. ERISA § 104(b)(4) / 29 U.S.C. § 1024(b)(4) gives the participant the right; failure to respond within 30 days triggers `templates/letter_erisa_502c_penalty.md`.

3. From the insurer or TPA. Even when the plan administrator is the employer, the insurer or TPA may have a copy. UnitedHealthcare, BlueCross, Aetna, Cigna all maintain participant portals where the most recent SPD is available.

4. From the U.S. Department of Labor under ERISA § 104(a)(1): the plan administrator files certain plan documents with DOL. The SPD itself is not always among them, but the Form 5500 (the annual return) often references and attaches the SPD or its key provisions.

---

## Key SPD sections to extract

### A. Plan funding status

Look in the introductory pages, the "About this plan" section, or the "Funding" / "Plan information" appendix. The SPD will state one of:

- "This plan is self-funded by [EMPLOYER]. [INSURER] is the third-party administrator." → ERISA self-funded plan; state insurance law generally preempted; the made-whole and common-fund doctrines turn entirely on plan-document language.

- "This plan is fully insured. Benefits are provided through a group insurance contract issued by [INSURER]." → ERISA-governed (if the employer is non-governmental and non-church) but the insurance contract is also regulated by the state's insurance department; state anti-subrogation and state surprise-billing laws may apply.

- "This is a governmental plan." → ERISA exempt; state and federal-employee benefit rules apply instead.

- "This is a church plan." → ERISA exempt unless the plan has elected ERISA coverage under § 410(d) (rare).

### B. Cost-sharing structure

In the "Schedule of benefits" or "Benefits at a glance" section:

- Deductible (individual, family, in-network, out-of-network).
- Out-of-pocket maximum (individual, family, in-network, out-of-network).
- Copay or coinsurance per service category (office visit, ER, ancillary, etc.).
- Whether out-of-network services apply toward the in-network out-of-pocket max (often no, but some plans do).

For NSA-protected services, the patient's cost-sharing is fixed at the in-network amount regardless of provider network status. The SPD's in-network numbers are what the EOB should show for protected services.

### C. Claim-filing and appeal procedures

In the "Claims procedure" or "How to file a claim" section:

- Time limit for filing a claim from date of service (typically 90 days to 1 year).
- Time within which the plan must adjudicate a claim (30 days for non-urgent post-service; 72 hours for urgent care).
- Internal appeal deadline from adverse determination (typically 180 days under 29 CFR § 2560.503-1(h)(3)(i)).
- Number of internal appeal levels (one or two; most plans have one).
- External review procedure (always available under 45 CFR § 147.136 for ACA-applicable plans).
- The plan's discretionary-authority language (whether the SPD grants the plan administrator discretionary authority to interpret the plan — this affects the standard of review on judicial appeal).

### D. Subrogation / reimbursement language

In the "Subrogation" or "Right of recovery" section:

- Whether the plan asserts a right to subrogation (against the third-party tortfeasor) or to reimbursement (from the participant's recovery) or both.
- Whether the plan's language expressly disclaims the made-whole doctrine.
- Whether the plan's language expressly disclaims the common-fund (attorney's-fees) reduction.
- Whether the plan's right attaches at the moment of the injury, the filing of the claim, or the receipt of the recovery — affects priority over other liens.
- The plan's first-priority-lien language: "constructive trust" or "equitable lien" wording activates the Sereboff line of cases.

### E. Prior authorization and medical necessity

In the "Medical necessity" or "Prior authorization" section:

- Which service categories require prior authorization (typically inpatient stays, certain imaging, certain procedures, certain drugs).
- The plan's medical-necessity definition (the plan's own definition, which may be narrower than community medical standards).
- The consequence of failing to obtain prior authorization (denial, reduced benefit, or penalty).
- The exception for emergency services (NSA requires the plan to cover emergency services regardless of prior authorization).

### F. Network rules and out-of-network coverage

In the "Provider network" or "Out-of-network" section:

- The directory or look-up tool the plan publishes for in-network providers.
- The cost-sharing applied when an in-network provider is unavailable (often the plan promises in-network cost-sharing for OON ancillary at IN facility — this is the plan's express NSA implementation).
- The "covered charges" definition for OON services (e.g., usual-and-customary, percentage of Medicare, fee schedule). This determines the plan's allowed amount for OON claims.

### G. ERISA disclosures and rights notice

Required by 29 CFR § 2520.102-3(t), this section lists:

- The right to obtain copies of plan documents under § 104(b)(4).
- The right to file a civil action under § 502(a).
- The right to receive a Summary of Material Modifications (SMM) when the plan changes.
- The right to a Summary of Benefits and Coverage (SBC) under the ACA.

If this section is missing, the SPD is incomplete and the participant can demand corrected documents.

---

## How to use the extracted SPD data

The kit's `scripts/parse_spd.py` reads an SPD PDF and emits a structured profile that the dispute drafter consumes:

```json
{
  "plan_name": "Example Health Plan",
  "plan_sponsor": "Example Corp",
  "plan_administrator": "Example Corp Benefits Committee",
  "funding": "self_funded",
  "tpa": "UnitedHealthcare",
  "in_network_deductible_individual": 1500.00,
  "in_network_oop_max_individual": 5000.00,
  "out_network_oop_max_individual": null,
  "internal_appeal_deadline_days": 180,
  "external_review_available": true,
  "subrogation_clause_present": true,
  "made_whole_disclaimed": true,
  "common_fund_disclaimed": false,
  "discretionary_authority_clause": true,
  "nsa_ancillary_implementation": true,
  "extracted_at": "2026-05-21"
}
```

The drafter reads this file when rendering:

- ERISA appeal letters (cites the plan's actual deadlines and appeal procedure).
- Subrogation responses (cites whether the plan disclaimed made-whole and common-fund, since the patient's posture depends on it).
- IDR-initiation requests (cites the plan's own NSA-ancillary implementation language).
- 502(c) penalty letters (cites the plan's funding status to confirm ERISA applicability).

---

## Caveats

- The SPD is a summary. The underlying plan document is what the court applies. If the SPD and the plan document conflict, the participant can argue the SPD controls under the Cigna v. Amara doctrine; the plan can argue the plan document controls. Pull both if possible.

- SPDs are written by lawyers for the plan, not for the participant. The plain-language style is a relative thing. Ambiguity tends to be resolved against the drafter (the plan) under contra proferentem, but courts have eroded that principle in ERISA cases.

- The kit's parser is best-effort. SPDs vary widely in length (40 to 200 pages) and structure. Verify any extracted field against the actual SPD text before relying on it in a letter.

---

## Related templates and scripts

- `scripts/parse_spd.py` — the parser that produces the structured profile.
- `templates/letter_insurance_appeal_erisa.md` — ERISA appeal that cites the parsed deadlines.
- `templates/letter_subrogation_response.md` — uses parsed made-whole / common-fund flags.
- `templates/letter_erisa_502c_penalty.md` — invokes the SPD-access right.
- `templates/letter_request_insurer_initiate_idr.md` — uses parsed NSA-ancillary language.
