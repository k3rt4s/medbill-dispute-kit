# Hospital MRF (Machine-Readable File) vendor adapters

The federal Hospital Price Transparency Rule (45 CFR Part 180), in force since January 1, 2021, requires every US hospital to publish a complete machine-readable file of standard charges. The rule specifies what data must appear but does not mandate a single format. As a result, hospitals publish MRFs in three major schemas, with three major vendors handling most of the actual production. Pulling a specific CPT's price out of any given MRF requires knowing which schema the file follows.

This reference describes the formats and the major vendor patterns so a patient (or `scripts/fetch_mrf.py`) can navigate them.

---

## CMS template (the federal schema, July 2024 onward)

CMS published a versioned template at github.com/CMSgov/hospital-price-transparency. Hospitals subject to enforcement after July 2024 are expected to publish in the CMS template, which can be either JSON or CSV.

### JSON schema (CMS template v2.x)

Top-level structure:

```json
{
  "hospital_name": "Example General Hospital",
  "last_updated_on": "2026-04-15",
  "version": "2.0.0",
  "hospital_location": [ { "address": "...", "city": "...", "state": "..." } ],
  "affirmation": { ... },
  "standard_charge_information": [
    {
      "description": "CT abdomen with contrast",
      "code_information": [
        { "code": "74160", "type": "CPT" }
      ],
      "standard_charges": [
        {
          "minimum": 280.50,
          "maximum": 1850.00,
          "gross_charge": 1850.00,
          "discounted_cash": 425.00,
          "payers_information": [
            {
              "payer_name": "Aetna",
              "plan_name": "POS",
              "standard_charge_dollar": 412.00,
              "standard_charge_methodology": "fee schedule"
            },
            {
              "payer_name": "BlueCross BlueShield",
              "plan_name": "PPO",
              "standard_charge_dollar": 388.00,
              "standard_charge_methodology": "fee schedule"
            }
          ]
        }
      ]
    }
  ]
}
```

To find a specific CPT, iterate `standard_charge_information[].code_information[]`, match on `code` + `type == "CPT"`, then read `standard_charges[0]` for the gross / cash / negotiated rates.

### CSV schema (CMS template v2.x)

Wide-format. Each row is one line item (one billable code + one setting). Columns include:

- `description`
- `code|1`, `code|1|type`, `code|2`, `code|2|type` (up to three code columns)
- `setting` (inpatient | outpatient | both)
- `standard_charge|gross`
- `standard_charge|discounted_cash`
- `standard_charge|min`
- `standard_charge|max`
- `standard_charge|[payer]|[plan]|negotiated_dollar` (one column per payer-plan combination)
- `standard_charge|[payer]|[plan]|methodology`

To find a specific CPT, filter rows where `code|1 == "<CPT>"` (or `code|2`, etc.), then read the matching `standard_charge|*` columns.

---

## Pre-CMS-template legacy formats (2021–2024)

Most hospitals still publish in one of three legacy patterns, especially for files generated before July 2024. The kit's MRF adapter must handle these.

### Format A — Turquoise Health flat CSV

Vendor: Turquoise Health (commonly referenced as "Turquoise" in filenames).

Columns (typical):

- `cpt_hcpcs_code`
- `description`
- `gross_charge`
- `cash_price`
- `negotiated_rate_inpatient`
- `negotiated_rate_outpatient`
- `payer_name`
- `plan_name`

One row per (code, payer, plan). Many hospitals produce 50,000-200,000 rows in this format.

### Format B — TransparentRx / Trizetto JSON

Older nested JSON pattern:

```json
{
  "PriceTransparency": {
    "Items": [
      {
        "ItemCode": "74160",
        "ItemCodeType": "CPT",
        "Description": "CT abdomen with contrast",
        "GrossCharge": 1850.00,
        "CashPrice": 425.00,
        "Rates": [
          { "Payer": "Aetna", "Rate": 412.00 },
          { "Payer": "BCBS", "Rate": 388.00 }
        ]
      }
    ]
  }
}
```

Field names vary slightly: `ItemCode`, `ProcedureCode`, `Code`, `HCPCSCode`, `CPTCode` all appear. Always check the first three or four item records before writing a parser.

### Format C — Epic-native wide CSV

Hospitals that use Epic's billing-export workflow often publish an Epic-native CSV with columns:

- `BILLABLE_CODE`
- `CODE_TYPE` ("CPT" / "HCPCS" / "DRG" / "REV")
- `DESCRIPTION`
- `LIST_PRICE` (chargemaster / gross)
- `CASH_PRICE`
- `MIN_NEGOTIATED`
- `MAX_NEGOTIATED`
- one column per payer's contracted rate, named after the payer (`AETNA_RATE`, `BCBS_RATE`, etc.)

---

## How to find a hospital's MRF URL

1. Try the hospital's website footer first. The CMS rule requires a "machine-readable file" link to be discoverable from the hospital's price-transparency landing page, which is typically linked from the footer or the "Billing & Insurance" page.

2. Try the URL pattern `https://[hospital-domain]/pricing-transparency` or `/price-transparency` or `/standard-charges`. About half of hospitals use this pattern.

3. Try [PatientRightsAdvocate Hospital Price Files Finder](https://hospitalpricingfiles.patientrightsadvocate.org). They maintain a community-sourced index of MRF URLs across thousands of hospitals.

4. Try [Turquoise Health patient search](https://turquoise.health/patients). Their search includes the underlying MRF URL when available.

5. If none of the above work, CMS requires the file location be searchable; you can file a CMS complaint at cms.gov/hospital-price-transparency/contact-us alleging the hospital is non-compliant with the discoverability requirement.

---

## What the kit's `fetch_mrf.py` does

The script accepts a hospital MRF URL and a list of CPT codes, downloads the file, detects the format from a small content-sniffing pass over the first ~10 KB, parses the relevant rows, and emits `mrf_lookup_<hospital_slug>.csv` with one row per requested code per published rate band:

| Column               | Meaning                                         |
| -------------------- | ----------------------------------------------- |
| cpt_code             | CPT/HCPCS requested                             |
| gross_charge         | Hospital's published gross / chargemaster price |
| discounted_cash      | Hospital's published cash-pay rate              |
| min_negotiated       | Lowest payer-specific negotiated rate           |
| max_negotiated       | Highest payer-specific negotiated rate          |
| payer_specific_rates | Semicolon-joined list of payer:rate pairs       |
| source_url           | The MRF URL used                                |
| retrieved            | ISO date the MRF was fetched                    |

The output CSV slots in as Exhibit X for any of the dispute-letter templates that argue the patient's billed amount exceeds the hospital's own published cash price.

---

## Caveats

- MRFs can be inaccurate. Some hospitals publish stale data; others publish data that does not match what payers are actually contracted at. Use as a starting benchmark, not a final authority.

- MRFs may not include every CPT a hospital actually bills. Hospitals are required to publish 300 shoppable services in a consumer-friendly format and the full machine-readable file with all standard charges, but compliance is uneven. The absence of a code from the MRF is itself a finding that may belong in a CMS complaint.

- The kit's adapter handles the four formats above plus simple variants. Hospitals using highly custom formats will not parse cleanly; in that case, the patient can either inspect the file manually or file a CMS complaint that the file is not in a machine-readable format compliant with 45 CFR § 180.50.

---

## Related templates and scripts

- `scripts/fetch_mrf.py` — the adapter referenced above.
- `scripts/fetch_price_benchmarks.py` — Medicare PFS baseline; the MRF lookup adds a second benchmark column.
- `templates/letter_negotiation_counter_offer.md` — the primary use case for MRF data in a letter.
- `templates/complaint_cms_hpt.md` — file when the MRF is missing, incomplete, or non-machine-readable.
- `references/resources.md` — Turquoise Health, PatientRightsAdvocate, hospital MRF lookup pointers.
