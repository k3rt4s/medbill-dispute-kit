"""parse_990.py, extract provenance-bearing hospital profiles from Form 990 XML or PDF.

XML mappings are verified against IRS TY2025 MeF stylesheets and Schedule H,
reviewed 2026-09-07: https://www.irs.gov/pub/irs-schema/PY2026R1.zip and
https://www.irs.gov/pub/irs-pdf/f990sh.pdf. Unknown/absent fields stay null.
This is a supported-element extractor, not a full IRS schema validator.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
import json
import os
from pathlib import Path
import re
import sys
from typing import Any
import urllib.request
import xml.etree.ElementTree as ET

HEALTH_ROOT = Path(os.environ.get("HEALTHBILLS_ROOT") or (Path.home() / "Health_Bills"))
HOSPITAL_OUT_DIR = HEALTH_ROOT / "_hospital_profiles"
ENV_FILE = Path(os.environ.get("MEDBILL_KIT_ENV_FILE") or (Path.home() / ".medbill-dispute-kit" / ".env"))
SLUG_SAFE = re.compile(r"[^a-z0-9_]+")
MAX_INPUT_BYTES = 25 * 1024 * 1024

# Paths are relative to IRS990ScheduleH; columns distinguish gross and net cost.
SCHEDULE_FIELDS = {
    "financial_assistance_at_cost": ("FinancialAssistanceAtCostTyp/TotalCommunityBenefitExpnsAmt", "Schedule H Part I line 7a(c)", "amount"),
    "financial_assistance_net_cost": ("FinancialAssistanceAtCostTyp/NetCommunityBenefitExpnsAmt", "Schedule H Part I line 7a(e)", "amount"),
    "financial_assistance_expense_pct": ("FinancialAssistanceAtCostTyp/TotalExpensePct", "Schedule H Part I line 7a(f)", "ratio_pct"),
    "medicaid_net_expense": ("UnreimbursedMedicaidGrp/NetCommunityBenefitExpnsAmt", "Schedule H Part I line 7b(e)", "amount"),
    "other_means_tested_net_expense": ("UnreimbursedCostsGrp/NetCommunityBenefitExpnsAmt", "Schedule H Part I line 7c(e)", "amount"),
    "other_community_benefits_net_expense": ("TotalOtherBenefitsGrp/NetCommunityBenefitExpnsAmt", "Schedule H Part I line 7j(e)", "amount"),
    "net_community_benefit_expense": ("TotalCommunityBenefitsGrp/NetCommunityBenefitExpnsAmt", "Schedule H Part I line 7k(e)", "amount"),
    "community_building_net_expense": ("TotalCommuntityBuildingActyGrp/NetCommunityBenefitExpnsAmt", "Schedule H Part II line 10(e)", "amount"),
    "bad_debt_expense": ("BadDebtExpenseAmt", "Schedule H Part III line 2", "amount"),
    "bad_debt_fap_eligible": ("BadDebtExpenseAttributableAmt", "Schedule H Part III line 3", "amount"),
    "medicare_surplus_or_shortfall": ("MedicareSurplusOrShortfallAmt", "Schedule H Part III line 7", "amount"),
}
FACILITY_FIELDS: dict[str, tuple[str, str, str]] = {
    "facility_name_line_1": ("HospitalFacilityName/BusinessNameLine1Txt", "Schedule H Part V Section B heading", "text"),
    "facility_name_line_2": ("HospitalFacilityName/BusinessNameLine2Txt", "Schedule H Part V Section B heading", "text"),
    "facility_number": ("FacilityNum", "Schedule H Part V Section B heading (Part V Section A line numbers)", "text"),
    "eligibility_criteria_explained": ("EligCriteriaExplainedInd", "Schedule H Part V Section B line 13", "bool"),
    "fpg_criterion_selected": ("FPGFamilyIncmLmtFreeDscntInd", "Schedule H Part V Section B line 13a", "bool"),
    "fpg_free_care_pct": ("FPGFamilyIncmLmtFreeCarePct", "Schedule H Part V Section B line 13a", "pct"),
    "fpg_discounted_care_pct": ("FPGFamilyIncmLmtDscntCarePct", "Schedule H Part V Section B line 13a", "pct"),
    "fap_publicity_measures": ("IncludesPublicityMeasuresInd", "Schedule H Part V Section B line 16", "bool"),
    "permits_credit_reporting": ("PermitReportToCreditAgencyInd", "Schedule H Part V Section B line 18a", "bool"),
    "permits_debt_sale": ("PermitSellingDebtInd", "Schedule H Part V Section B line 18b", "bool"),
    "permits_care_deferral": ("PermitDeferDenyRqrPaymentInd", "Schedule H Part V Section B line 18c", "bool"),
    "permits_legal_process": ("PermitLegalJudicialProcessInd", "Schedule H Part V Section B line 18d", "bool"),
    "collection_activities": ("CollectionActivitiesInd", "Schedule H Part V Section B line 19", "bool"),
    "reported_to_credit_agency": ("ReportingToCreditAgencyInd", "Schedule H Part V Section B line 19a", "bool"),
    "sold_debt": ("EngagedSellingDebtInd", "Schedule H Part V Section B line 19b", "bool"),
    "deferred_care": ("EngageDeferDenyRqrPaymentInd", "Schedule H Part V Section B line 19c", "bool"),
    "engaged_legal_process": ("EngagedLegalJudicialProcessInd", "Schedule H Part V Section B line 19d", "bool"),
    "provided_written_notice": ("ProvidedWrittenNoticeInd", "Schedule H Part V Section B line 20a", "bool"),
    "orally_notified": ("MadeEffortOrallyNotifyInd", "Schedule H Part V Section B line 20b", "bool"),
    "processed_fap_application": ("ProcessedFAPApplicationInd", "Schedule H Part V Section B line 20c", "bool"),
    "presumptive_eligibility_determination": ("MadePresumptiveEligDetermInd", "Schedule H Part V Section B line 20d", "bool"),
}
IDENTITY_REFS = {"filing_year": "Form 990 heading (tax year)", "ein": "Form 990 heading D", "organization_legal_name": "Form 990 heading C"}
COMPENSATION_REF = "Form 990 Part VII Section A line 1a columns D+E+F"


def safe_slug(value: str) -> str:
    return SLUG_SAFE.sub("_", value.lower().strip()).strip("_") or "hospital"


def load_env(path: Path) -> None:
    """Read credentials only for an explicitly invoked non-dry-run PDF fallback."""
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def field(value: Any, ref: str, source: str = "xml") -> dict[str, Any]:
    return {"value": value, "source": source if value is not None else None, "ref": ref}


def one(parent: ET.Element | None, path: str) -> ET.Element | None:
    """Require a unique direct path; repeated scalar values are ambiguous."""
    if parent is None:
        return None
    matches = parent.findall(path)
    return matches[0] if len(matches) == 1 else None


def text(parent: ET.Element | None, path: str) -> str | None:
    element = one(parent, path)
    if element is None or list(element):
        return None
    return (element.text or "").strip() or None


def scalar(value: str | None, kind: str) -> Any:
    if value is None:
        return None
    if kind == "bool":
        return {"true": True, "1": True, "false": False, "0": False, "X": True}.get(value)
    if kind in ("amount", "ratio_pct", "pct"):
        try:
            number = Decimal(value)
        except InvalidOperation:
            return None
        if not number.is_finite():
            return None
        if kind == "ratio_pct":
            number *= 100
        return format(number, "f")
    return value


def extract_fields(parent: ET.Element | None, specs: dict[str, tuple[str, str, str]]) -> dict[str, Any]:
    return {name: field(scalar(text(parent, path), kind), ref) for name, (path, ref, kind) in specs.items()}


def unique_descendant(root: ET.Element, name: str) -> ET.Element | None:
    matches = list(root.iter(name))
    if len(matches) > 1:
        raise ValueError(f"Multiple {name} elements: supply one filing, not a batch")
    return matches[0] if matches else None


def top_compensation(core: ET.Element | None) -> dict[str, Any]:
    """Rank only complete reported D/E/F totals; no missing component means zero."""
    rows = [] if core is None else core.findall("Form990PartVIISectionAGrp")
    if not rows:
        return field(None, COMPENSATION_REF)
    result = []
    for row in rows:
        amounts = [scalar(text(row, key), "amount") for key in ("ReportableCompFromOrgAmt", "ReportableCompFromRltdOrgAmt", "OtherCompensationAmt")]
        name = text(row, "PersonNm")
        if name is None or any(value is None for value in amounts):
            # Incomplete entries could outrank the others; do not claim a top five.
            return field(None, COMPENSATION_REF)
        total = sum((Decimal(value) for value in amounts), Decimal(0))
        result.append({
            "name": field(name, "Form 990 Part VII Section A line 1a(A)"),
            "title": field(text(row, "TitleTxt"), "Form 990 Part VII Section A line 1a(A)"),
            "total_compensation": field(format(total, "f"), COMPENSATION_REF),
        })
    result.sort(key=lambda row: Decimal(row["total_compensation"]["value"]), reverse=True)
    return field(result[:5], COMPENSATION_REF)


def parse_xml(data: bytes | str) -> dict[str, Any]:
    """Extract a single supplied filing, preserving missing or ambiguous scalars."""
    if len(data) > MAX_INPUT_BYTES:
        raise ValueError("XML input exceeds the 25 MiB limit")
    root = ET.fromstring(data)
    # ElementTree never fetches external entities; local-name paths accept the
    # default IRS namespace and namespace-free synthetic fixtures identically.
    for element in root.iter():
        element.tag = element.tag.rsplit("}", 1)[-1]
    header = unique_descendant(root, "ReturnHeader")
    schedule = unique_descendant(root, "IRS990ScheduleH")
    core = unique_descendant(root, "IRS990")
    if core is None and schedule is None:
        raise ValueError("No IRS990 or IRS990ScheduleH element found")
    profile = extract_fields(schedule, SCHEDULE_FIELDS)
    first = text(header, "Filer/BusinessName/BusinessNameLine1Txt")
    if header is not None and not header.findall("Filer/BusinessName"):
        first = text(header, "Filer/BusinessNameLine1Txt")
    second = text(header, "Filer/BusinessName/BusinessNameLine2Txt")
    identity = {"filing_year": text(header, "TaxYr"), "ein": text(header, "Filer/EIN"), "organization_legal_name": " ".join(v for v in (first, second) if v) if first else None}
    profile.update({name: field(value, IDENTITY_REFS[name]) for name, value in identity.items()})
    facilities = [] if schedule is None else schedule.findall("HospitalFcltyPoliciesPrctcGrp")
    profile["facilities"] = field([extract_fields(facility, FACILITY_FIELDS) for facility in facilities] or None, "Schedule H Part V Section B")
    narratives = [] if schedule is None else schedule.findall("SupplementalInformationDetail")
    present = any(text(narrative, "ExplanationTxt") for narrative in narratives)
    profile["supplemental_narrative_present"] = field(True if present else None, "Schedule H Part VI")
    profile["top_five_compensation"] = top_compensation(core)
    return profile


def pdf_request(path: Path) -> dict[str, Any]:
    import pymupdf
    with pymupdf.open(path) as pdf:
        pages = [page.get_text() for page in pdf]
    if not any(page.strip() for page in pages):
        raise ValueError("PDF has no text layer; supply IRS XML or an OCR text-layer PDF")
    refs = {name: spec[1] for name, spec in SCHEDULE_FIELDS.items()} | IDENTITY_REFS
    return {"instructions": "Extract only explicitly stated values as scalars, otherwise null. Amounts are plain dollar strings; percentages are percentage points. Do not infer legal compliance. Return only requested keys in a JSON object.", "fields": refs, "pages": pages}


def call_pdf_model(request: dict[str, Any]) -> dict[str, Any]:
    load_env(ENV_FILE)
    required = ("AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_DEPLOYMENT")
    if any(not os.environ.get(key) for key in required):
        raise ValueError("PDF model extraction requires Azure credentials; use --xml for offline extraction")
    from openai import OpenAI
    client = OpenAI(api_key=os.environ[required[0]], base_url=os.environ[required[1]].rstrip("/") + "/openai/v1/")
    response = client.chat.completions.create(model=os.environ[required[2]], messages=[{"role": "user", "content": json.dumps(request)}], response_format={"type": "json_object"}, max_completion_tokens=4096)
    candidate = json.loads(response.choices[0].message.content or "{}")
    if not isinstance(candidate, dict):
        raise ValueError("PDF model response was not a JSON object")
    profile = {}
    for name, ref in request["fields"].items():
        value = candidate.get(name)
        if not isinstance(value, (str, int, float)) or isinstance(value, bool):
            value = None
        elif name in SCHEDULE_FIELDS:
            # The prompt requests display percentages, so never scale again.
            value = scalar(str(value), "amount")
        else:
            value = str(value)
        profile[name] = field(value, ref, "model")
    # This deliberately bounded PDF fallback cannot reliably reconstruct repeated
    # facility or compensation tables. Keep the XML profile shape and honest nulls.
    profile["facilities"] = field(None, "Schedule H Part V Section B")
    profile["supplemental_narrative_present"] = field(None, "Schedule H Part VI")
    profile["top_five_compensation"] = field(None, COMPENSATION_REF)
    return profile


def fetch_input(url: str, target: Path) -> None:
    """Download only on explicit request; never overwrite a supplied local file."""
    if not url.startswith(("https://", "http://")):
        raise ValueError("--fetch-from requires an HTTP(S) URL")
    if target.exists():
        raise ValueError("Fetch target already exists; choose a new --xml/--pdf path")
    with urllib.request.urlopen(url, timeout=30) as response:
        data = response.read(MAX_INPUT_BYTES + 1)
    if len(data) > MAX_INPUT_BYTES:
        raise ValueError("Downloaded input exceeds the 25 MiB limit")
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("xb") as stream:
        stream.write(data)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--xml", type=Path)
    source.add_argument("--pdf", type=Path)
    parser.add_argument("--org-slug", help="Optional output slug; defaults to extracted legal name")
    parser.add_argument("--fetch-from", help="Explicit download URL; --xml/--pdf names a new target path")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    target = (args.xml or args.pdf).expanduser().resolve()
    try:
        if args.fetch_from:
            if args.dry_run:
                print(json.dumps({"fetch_from": args.fetch_from, "target": str(target), "network": "not invoked"}))
                return 0
            fetch_input(args.fetch_from, target)
        if args.xml:
            profile = parse_xml(target.read_bytes())
        else:
            request = pdf_request(target)
            if args.dry_run:
                print(json.dumps(request, indent=2))
                if not all(os.environ.get(key) for key in ("AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_DEPLOYMENT")):
                    print("[notice] PDF model extraction requires credentials; dry-run made no call or credential-file read.", file=sys.stderr)
                    return 2  # Item-specific brief overrides the generic dry-run exit code.
                return 0
            profile = call_pdf_model(request)
        if args.dry_run:
            print(json.dumps(profile, indent=2))
            return 0
        year = profile["filing_year"]["value"]
        legal_name = args.org_slug or profile["organization_legal_name"]["value"]
        if not isinstance(year, str) or not re.fullmatch(r"\d{4}", year) or not legal_name:
            raise ValueError("Output requires a stated four-digit filing year and organization name/--org-slug")
        HOSPITAL_OUT_DIR.mkdir(parents=True, exist_ok=True)
        output = HOSPITAL_OUT_DIR / f"{safe_slug(legal_name)}_{year}.json"
        output.write_text(json.dumps(profile, indent=2, allow_nan=False) + "\n", encoding="utf-8")
        print(f"[done] -> {output}")
        return 0
    except (OSError, ValueError, ET.ParseError) as exc:
        print(f"[fatal] {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
