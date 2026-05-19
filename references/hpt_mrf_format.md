# Hospital Price Transparency machine-readable file format

The CMS Hospital Price Transparency Rule (45 CFR Part 180) requires every US hospital to publish a machine-readable file of its standard charges. The MRF is the strongest single piece of pricing evidence a patient can use in a billing dispute — it's the hospital's own statement of what it charges, in a format the hospital is legally required to maintain.

This document covers how to find the MRF, how to read it, and what to do with the data.

## Where the MRF lives

CMS requires hospitals to:

1. **Host the MRF at a discoverable URL.** The current CMS standard requires hospitals to put a "txt" file at `<hospital-website>/cms-hpt.txt` that links to the actual MRF. The MRF itself is typically named with a standardized pattern: `{ein}_{hospital-name}_standardcharges.{json|csv}`.
2. **Make the file freely accessible** without login, paywall, terms of service, or user accounts.
3. **Update it at least annually.**
4. **Use the CMS-defined template format** (mandatory since July 1, 2024).

Quick way to find a hospital's MRF:

- **Search:** `[hospital name] price transparency machine readable file`
- **Standardized location:** `https://[hospital-domain]/cms-hpt.txt` (the txt file links to the actual MRF)
- **Aggregators:**
  - [Turquoise Health](https://turquoise.health) — patient-facing search
  - [PatientRightsAdvocate.org Hospital Price Files Finder](https://hospitalpricingfiles.patientrightsadvocate.org)
  - [Hospital Pricing Files (CMS-hosted aggregator)](https://hospitalpricingfiles.org)

If you can't find the MRF in any reasonable amount of time, the hospital is likely non-compliant. File a CMS HPT complaint using `templates/complaint_cms_hpt.md`.

## What's in the file

The CMS template requires hospitals to include for each item or service:

- **Description** of the item or service
- **Code(s)**: CPT, HCPCS, MS-DRG, NDC, APC, or other applicable
- **Code type** (CPT, HCPCS, etc.)
- **Setting**: inpatient, outpatient
- **Drug unit of measure** (for J-codes)
- **Modifier**(s) where applicable
- **Gross charge** (the chargemaster price)
- **Discounted cash price** (the cash-pay rate the hospital accepts)
- **Payer-specific negotiated charges** — separate rate for each contracted insurer
- **De-identified minimum negotiated charge** across all payers
- **De-identified maximum negotiated charge** across all payers
- **Methodology** description (fee schedule, percent of charges, per diem, case rate, etc.)
- **Median allowed amount** (CY 2026 OPPS rule addition)
- **10th and 90th percentile allowed amounts** with 12-15 month lookback (CY 2026 addition)

Hospital must also include a self-attestation of accuracy signed by the CEO or delegated executive.

## How to read the file

### File format

The CMS template comes in two flavors: CSV and JSON. The CSV is human-readable; the JSON is structured for automated processing. Patients can usually work with the CSV.

### Common columns (CSV)

A CMS-template CSV will have columns including:

```text
description, code | 1, code | 1 | type, modifiers, setting, drug_unit_of_measurement, drug_type_of_measurement, standard_charge | gross, standard_charge | discounted_cash, standard_charge | payer_X | plan_Y | negotiated_dollar, standard_charge | payer_X | plan_Y | negotiated_percentage, standard_charge | payer_X | plan_Y | negotiated_algorithm, estimated_amount, standard_charge | min, standard_charge | max, additional_payer_notes
```

The structure is:

- Rows: each service or item
- Columns: payer-specific rates plus min/max and cash price

### What to look for

For a patient disputing a bill:

1. **Find the row** for the CPT code(s) on the bill.
2. **Note the gross charge** (chargemaster). This is what the hospital charged.
3. **Note the discounted cash price.** This is what an uninsured patient would pay if they asked.
4. **Find the patient's insurance company in the payer columns.** That's the contracted rate the hospital agreed to accept from that insurer.
5. **Compare to the patient's actual bill.** If the patient was charged more than the contracted rate (when insured) or more than the cash price (when uninsured), the bill is wrong on its face.

### Common patterns

- **Chargemaster prices are typically 3-10× the contracted rate.** The chargemaster is the starting point for everything; almost no one actually pays it.
- **The cash price is typically 1.5-3× the lowest contracted rate.** Hospitals discount cash patients but not as much as they discount their largest commercial insurers.
- **Medicare and Medicaid contracted rates are usually the lowest** in the file.
- **The minimum negotiated rate is often Medicaid;** the maximum is often a less-favored commercial insurer.

## Common compliance failures

Hospitals frequently:

- **Omit the cash price** entirely or replace it with "call for price"
- **Omit payer-specific rates** for one or more major insurers
- **Use percentage-of-something rates** ("85% of Medicare") without specifying the base value, making the actual dollar amount unknowable
- **Include placeholder values** ("N/A," "[redacted]") for required fields
- **Post the MRF behind a login or terms-of-service acceptance** in violation of the access requirement
- **Post a clearly outdated MRF** with no recent attestation date

Each of these is a CMS HPT complaint hook. See `templates/complaint_cms_hpt.md`.

## Using the MRF in a dispute letter

A patient with the hospital's MRF can argue directly from the hospital's own published prices:

> Your hospital's machine-readable file of standard charges, published at [URL] and dated [DATE], lists the contracted rate for [PATIENT'S INSURANCE PLAN] for CPT [CODE] as $[CONTRACTED RATE]. The bill I received charges $[BILLED AMOUNT] for the same code. This bill is inconsistent with your own published contracted rate. Please reissue the bill at the contracted rate, less any insurance payment that has already been made.

This argument is harder for the hospital to refuse than a fair-market argument from third-party data, because the hospital itself published the contradictory price.

## Examples by hospital system

Major hospital systems' MRFs (these URLs may change; verify):

- **HCA Healthcare**: facility-specific MRF on each TriStar / HCA hospital's website
- **Ascension**: market-specific MRF on each Ascension hospital's website
- **Kaiser Permanente**: regional-specific MRFs
- **Cleveland Clinic**: aggregate MRF at clevelandclinic.org
- **Mayo Clinic**: facility-specific MRFs at mayoclinic.org

For patient-side work, the kit recommends starting at [Turquoise Health](https://turquoise.health/patients) which aggregates and parses MRFs from thousands of hospitals into a searchable interface.

## When the MRF supports the hospital

Sometimes the MRF supports the hospital's bill — the contracted rate matches what was charged. In that case, the dispute is on different grounds: medical necessity, coding accuracy, services not received, or the contract itself. The MRF only resolves the price-vs-published-price question.

## Limits and caveats

- **MRFs change over time.** A patient using last year's MRF to dispute this year's bill may find the rates have moved. Take a dated screenshot or download when collecting evidence.
- **Some payer-specific rates are dynamic.** A "percent of Medicare" rate changes whenever Medicare rates change. Cite the methodology, not just the dollar number.
- **Self-pay patients with insurance have unusual leverage.** A self-pay patient who has insurance but chose not to use it should be charged the cash price, not the gross charge. The MRF documents the cash price.
- **Algorithm-based rates ("X% of [proprietary base]")** can be opaque. The CMS rule requires sufficient disclosure that the patient can determine the dollar amount; opaque algorithms are themselves a compliance issue.

## Related

- [[../rules/05_negotiate_fair_price]] — using MRFs as the primary anchor for negotiation
- [[../templates/complaint_cms_hpt]] — for hospitals that don't publish a compliant MRF
- [[../templates/letter_initial_dispute]] — the dispute letter that cites the MRF
- [[cpt_quick_reference]] — common CPT codes to look up in the MRF
