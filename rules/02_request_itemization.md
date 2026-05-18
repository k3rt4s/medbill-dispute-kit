# Rule 02 — Request the itemized bill

You cannot dispute a bill you can't see. Most "bills" providers send are summary statements showing only a total. The itemized bill — every charge, every CPT code, every supply, every date — is what you actually need.

## The rule

If your bill is a summary, request an itemized bill in writing within the first week. Send it via certified mail with return receipt. State the applicable state statute. Give a 30-day deadline.

Most states require providers to furnish itemized bills on request. Tennessee's statute, used as this kit's worked example, is **TN Code § 68-11-220**, which requires hospitals to provide itemized statements within 30 days of a written request made within one year of discharge. For other states, see `references/laws_state_template.md`.

## What to ask for, explicitly

In your request, ask for all of:

1. A complete itemized statement showing each service, supply, and medication
2. The CPT/HCPCS code and revenue code for each line item
3. The CPT/HCPCS code description in plain English
4. The date and time each service was provided
5. The provider (NPI and name) for each charge
6. The Explanation of Benefits (EOB) from the insurance company for that bill, if applicable
7. The hospital's chargemaster price for each CPT, and the contracted rate paid by the insurance company (if applicable). The Hospital Price Transparency Rule (45 CFR Part 180) requires hospitals to make these prices public; you are entitled to see what was applied to your case.

Asking for all of this up front is more efficient than serial requests.

## Why this is the first dispute action, every time

- Until you have line items, you don't know what you're being charged for. You can't tell whether a charge is duplicated, upcoded, billed for a service you didn't receive, or correctly priced.
- The act of requesting itemization signals to the billing department that you're a non-default patient — most patients never ask. Some bills get adjusted down at this stage before you even challenge them.
- The 30-day statutory clock starts the formal paper trail you'll need if this ends in small claims court or a state complaint.

## What to do if they refuse or delay

- After 30 days, send a follow-up citing the statute and warning that you will file a complaint.
- File the complaint. In Tennessee that goes to TDCI (1-800-342-4029) and, for hospital-specific issues, the Tennessee Health Facilities Commission (1-877-287-0010).
- In your eventual dispute letter or court filing, the provider's refusal to itemize is itself evidence supporting your claim that charges are wrong.

## Template

Use `templates/letter_itemization_request.md`. Render it with the patient's information and the correct state statute. The default citation in the template is Tennessee; the LLM substitutes for other states using `references/laws_state_template.md`.

## Related rules

- [[03_check_cpt_codes]] — what to do once you have line items
- [[06_small_claims]] — where this paper trail ends up if the provider stonewalls

## Hospital-bill-specific note

A hospital's itemized bill is only for hospital services. Separate professional bills (ER physician group, hospitalist, anesthesiology, radiology, pathology, lab) usually arrive separately from different entities. If you've had a hospital encounter, expect 3-6 separate bills. Each one needs its own itemization request. The tracker's `encounter_id` field links them.
