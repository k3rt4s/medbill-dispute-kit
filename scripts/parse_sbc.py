"""parse_sbc.py, extract a structured plan profile from an SBC PDF text layer."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

HEALTH_ROOT = Path(os.environ.get("HEALTHBILLS_ROOT") or (Path.home() / "Health_Bills"))
SBC_OUT_DIR = HEALTH_ROOT / "_sbc_profiles"
ENV_FILE = Path(os.environ.get("MEDBILL_KIT_ENV_FILE") or (Path.home() / ".medbill-dispute-kit" / ".env"))
SLUG_SAFE = re.compile(r"[^a-z0-9_]+")
MONEY = r"\$[\d,]+(?:\.\d{2})?"
SERVICE_LABELS = {
    "primary_care_visit_cost_sharing": r"Primary care visit(?: to treat an injury or illness)?",
    "specialist_visit_cost_sharing": r"Specialist visit",
    "diagnostic_test_cost_sharing": r"Diagnostic test",
    "imaging_cost_sharing": r"Imaging(?: \(CT/PET scans, MRIs\))?",
    "emergency_room_cost_sharing": r"Emergency room care",
    "emergency_medical_transportation_cost_sharing": r"Emergency medical transportation",
    "urgent_care_cost_sharing": r"Urgent care",
    "hospital_stay_facility_fee_cost_sharing": r"Facility fee \(e\.g\., hospital room\)",
    "hospital_stay_physician_fee_cost_sharing": r"Physician/surgeon fee",
}
FLAT_FIELDS = {
    "plan_name", "plan_year_start", "plan_year_end", "coverage_period",
    "in_network_deductible_individual", "in_network_deductible_family",
    "out_network_deductible_individual", "out_network_deductible_family",
    "in_network_oop_max_individual", "in_network_oop_max_family",
    "out_network_oop_max_individual", "out_network_oop_max_family",
    "out_of_pocket_exclusions", "overall_annual_plan_limit",
    "referral_needed_for_specialist", "network_provider_check_url", "plan_phone_number",
    "erisa_subject", "grievance_appeal_contact", *SERVICE_LABELS,
}


def safe_slug(value: str) -> str:
    """Return a filesystem-safe lowercase profile slug."""
    return SLUG_SAFE.sub("_", value.lower().strip()).strip("_") or "sbc"


def load_env(env_path: Path) -> None:
    """Load model credentials only when a non-dry-run fallback is invoked."""
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        if key.strip() and key.strip() not in os.environ:
            os.environ[key.strip()] = value.strip().strip('"').strip("'")


def field(value: Any = None, source: str | None = None, page: int | None = None) -> dict[str, Any]:
    """Build the required value, source, and page provenance envelope."""
    return {"value": value, "source": source, "page": page}


def empty_profile() -> dict[str, dict[str, Any]]:
    """Return every supported SBC field as an explicit null envelope."""
    return {name: field() for name in FLAT_FIELDS}


def read_pdf_pages(pdf_path: Path) -> list[str]:
    """Read each PDF text layer with PyMuPDF without rendering or networking."""
    try:
        import pymupdf
    except ImportError as exc:
        raise RuntimeError("PyMuPDF is required to parse an SBC PDF.") from exc
    with pymupdf.open(pdf_path) as document:
        return [page.get_text("text") for page in document]


def find_page(pages: list[str], pattern: str, flags: int = re.IGNORECASE) -> tuple[int | None, re.Match[str] | None]:
    """Return the first page and match for a pattern, or a null pair."""
    for index, text in enumerate(pages):
        match = re.search(pattern, text, flags)
        if match:
            return index, match
    return None, None


def labeled_value(pages: list[str], label: str) -> dict[str, Any]:
    """Extract a conservative one-line labeled value."""
    page, match = find_page(pages, rf"{label}\s*:\s*([^\n]+)")
    return field(match.group(1).strip(), "text", page) if match else field()


def question_region(pages: list[str], question: str) -> tuple[int | None, str]:
    """Return one SBC question region without crossing into the next question."""
    page, match = find_page(pages, question)
    if match is None or page is None:
        return None, ""
    tail = pages[page][match.end():]
    next_question = re.search(r"\n\s*(?:What|Are|Is|Do)\b[^\n?]*\?", tail, re.IGNORECASE)
    return page, tail[:next_question.start()] if next_question else tail


def network_amounts(region: str, label: str, stop_label: str) -> tuple[str, str] | None:
    """Extract explicitly labeled individual and family amounts from one network column."""
    match = re.search(label, region, re.IGNORECASE)
    if match is None:
        return None
    column = region[match.end():]
    stop = re.search(stop_label, column, re.IGNORECASE)
    if stop:
        column = column[:stop.start()]
    def labeled_amount(person_label: str) -> str | None:
        matches = re.findall(
            rf"(?:({MONEY})\s*(?:{person_label})\b|(?:{person_label})\b\s*({MONEY}))",
            column,
            re.IGNORECASE,
        )
        values = {first or second for first, second in matches}
        return values.pop() if len(values) == 1 else None

    individual = labeled_amount(r"individual|person")
    family = labeled_amount(r"family")
    return (individual, family) if individual is not None and family is not None else None


def set_limits(profile: dict[str, dict[str, Any]], pages: list[str], question: str, prefix: str) -> None:
    """Populate flat in- and out-of-network individual/family limit fields."""
    page, region = question_region(pages, question)
    if page is None:
        return
    in_pair = network_amounts(region, r"In[- ]Network", r"Out[- ]of[- ]Network")
    out_pair = network_amounts(region, r"Out[- ]of[- ]Network", r"\Z")
    if in_pair:
        profile[f"in_network_{prefix}_individual"] = field(in_pair[0], "text", page)
        profile[f"in_network_{prefix}_family"] = field(in_pair[1], "text", page)
    if out_pair:
        profile[f"out_network_{prefix}_individual"] = field(out_pair[0], "text", page)
        profile[f"out_network_{prefix}_family"] = field(out_pair[1], "text", page)


def service_value(pages: list[str], label: str) -> dict[str, Any]:
    """Extract a same-line or next-line cost value without crossing another row."""
    page, match = find_page(pages, label)
    if match is None or page is None:
        return field()
    region = pages[page][match.end():]
    headings = "|".join(SERVICE_LABELS.values())
    boundary = re.search(
        rf"\n\s*(?:(?:{headings})|(?:What|Are|Is|Do)\b[^\n?]*\?)",
        region,
        re.IGNORECASE,
    )
    if boundary:
        region = region[:boundary.start()]
    remainder = region.splitlines()
    candidates = [(remainder[0].lstrip(" :") if remainder else ""), *[line.strip() for line in remainder[1:4]]]
    for candidate in candidates:
        if re.search(r"(?:\$|\d+%|No charge)", candidate, re.IGNORECASE):
            return field(candidate, "text", page)
    return field()


def extract_profile(pages: list[str]) -> dict[str, dict[str, Any]]:
    """Extract only text-supported SBC facts and preserve null for every gap."""
    profile = empty_profile()
    for name, label in {
        "plan_name": "Plan(?: Name)?", "plan_year_start": "Plan year start",
        "plan_year_end": "Plan year end", "coverage_period": "Coverage Period",
        "out_of_pocket_exclusions": "Not included in the out-of-pocket limit",
        "overall_annual_plan_limit": "Overall annual limit on what the plan pays",
        "referral_needed_for_specialist": "Referral needed to see a specialist",
        "network_provider_check_url": "Network provider check URL", "plan_phone_number": "Plan phone number",
        "erisa_subject": "Are you covered by a plan subject to ERISA", "grievance_appeal_contact": "Grievance/appeal contact",
    }.items():
        profile[name] = labeled_value(pages, label)
    set_limits(profile, pages, r"What is the overall(?: annual)? deductible\?", "deductible")
    set_limits(profile, pages, r"What is the out-of-pocket limit\?", "oop_max")
    for name, label in SERVICE_LABELS.items():
        profile[name] = service_value(pages, label)
    return profile


def unresolved_fields(profile: dict[str, dict[str, Any]]) -> list[str]:
    """List leaf fields that remain unsupported by deterministic extraction."""
    return sorted(name for name, value in profile.items() if value["source"] is None)


def build_model_request(pages: list[str], missing: list[str]) -> dict[str, Any]:
    """Build the bounded fallback request without importing a client or reading credentials."""
    return {"fields": missing, "instructions": "Return only requested keys with scalar values. Do not guess.", "text": "\n\n".join(f"[page {index}]\n{text}" for index, text in enumerate(pages))}


def merge_model_fields(profile: dict[str, dict[str, Any]], candidate: object) -> dict[str, dict[str, Any]]:
    """Merge only supported scalar model values into fields still unsupported by text."""
    if not isinstance(candidate, dict):
        return profile
    for name, value in candidate.items():
        if name not in FLAT_FIELDS or profile[name]["source"] is not None:
            continue
        if isinstance(value, (str, int, float, bool)) and not isinstance(value, dict):
            profile[name] = field(value, "model", None)
    return profile


def call_model_fallback(request: dict[str, Any]) -> object:
    """Call the optional fallback only after deterministic extraction leaves fields null."""
    load_env(ENV_FILE)
    from openai import OpenAI
    required = ("AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_DEPLOYMENT")
    missing = [name for name in required if not os.environ.get(name)]
    if missing:
        raise RuntimeError(f"model fallback requires: {', '.join(missing)}")
    client = OpenAI(api_key=os.environ["AZURE_OPENAI_API_KEY"], base_url=os.environ["AZURE_OPENAI_ENDPOINT"].rstrip("/") + "/openai/v1/")
    response = client.chat.completions.create(model=os.environ["AZURE_OPENAI_DEPLOYMENT"], messages=[{"role": "user", "content": json.dumps(request)}], response_format={"type": "json_object"}, max_completion_tokens=2048)
    return json.loads((response.choices[0].message.content or "{}"))


def main() -> int:
    """Parse an SBC PDF and write or preview its provenance-bearing profile."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", required=True, help="Path to the SBC PDF.")
    parser.add_argument("--plan-slug", required=True, help="Slug used in the output filename.")
    parser.add_argument("--dry-run", action="store_true", help="Parse and preview fallback request without network access.")
    args = parser.parse_args()
    pdf_path = Path(args.pdf).expanduser().resolve()
    if not pdf_path.is_file():
        print(f"[fatal] SBC not found at {pdf_path}", file=sys.stderr)
        return 2
    try:
        pages = read_pdf_pages(pdf_path)
    except RuntimeError as exc:
        print(f"[fatal] {exc}", file=sys.stderr)
        return 2
    profile = extract_profile(pages)
    request = build_model_request(pages, unresolved_fields(profile))
    if args.dry_run:
        print(json.dumps(profile, indent=2, sort_keys=True))
        print("[dry-run] model request preview follows; no environment file, client import, or network call occurred.")
        print(json.dumps(request, indent=2, sort_keys=True))
        return 0
    if request["fields"]:
        try:
            profile = merge_model_fields(profile, call_model_fallback(request))
        except RuntimeError as exc:
            print(f"[notice] {exc}; unresolved fields remain null.")
    SBC_OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = SBC_OUT_DIR / f"{safe_slug(args.plan_slug)}.json"
    out_path.write_text(json.dumps(profile, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"[done] -> {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
