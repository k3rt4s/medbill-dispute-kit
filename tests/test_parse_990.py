"""test_parse_990.py, verify offline Form 990 XML and dry-run behavior."""

from __future__ import annotations

import importlib
import os
from pathlib import Path
import subprocess
import sys
from typing import Any

import pymupdf
import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))


def parser_with_roots(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Any:
    """Import only after temporary output and credential paths are configured."""
    monkeypatch.setenv("HEALTHBILLS_ROOT", str(tmp_path / "health-root"))
    monkeypatch.setenv("MEDBILL_KIT_ENV_FILE", str(tmp_path / "env-read-sentinel.txt"))
    sys.modules.pop("scripts.parse_990", None)
    return importlib.import_module("scripts.parse_990")


def sample_xml(
    *,
    include_publicity: bool = False,
    incomplete_compensation: bool = False,
    two_facilities: bool = False,
    part_v_narrative: bool = False,
    part_vi_narrative: bool = False,
) -> bytes:
    """Build one fictional namespace-qualified 990 filing with verified element names."""
    publicity = "<IncludesPublicityMeasuresInd>false</IncludesPublicityMeasuresInd>" if include_publicity else ""
    rows = []
    for name, amount in (("Delta Example", "400"), ("Alpha Example", "900"), ("Foxtrot Example", "100"), ("Bravo Example", "800"), ("Echo Example", "300"), ("Charlie Example", "700")):
        related = "" if incomplete_compensation and name == "Alpha Example" else "<ReportableCompFromRltdOrgAmt>10</ReportableCompFromRltdOrgAmt>"
        rows.append(
            "<Form990PartVIISectionAGrp>"
            f"<PersonNm>{name}</PersonNm><TitleTxt>Officer</TitleTxt>"
            f"<ReportableCompFromOrgAmt>{amount}</ReportableCompFromOrgAmt>{related}"
            "<OtherCompensationAmt>1</OtherCompensationAmt>"
            "</Form990PartVIISectionAGrp>"
        )
    second_facility = (
        "<HospitalFcltyPoliciesPrctcGrp><HospitalFacilityName>"
        "<BusinessNameLine1Txt>Sample South Facility</BusinessNameLine1Txt>"
        "</HospitalFacilityName><FacilityNum>2</FacilityNum>"
        "<FPGFamilyIncmLmtFreeDscntInd>false</FPGFamilyIncmLmtFreeDscntInd>"
        "</HospitalFcltyPoliciesPrctcGrp>"
        if two_facilities else ""
    )
    part_v = (
        "<SupplementalInformationGrp><FormAndLineReferenceDesc>Part V</FormAndLineReferenceDesc>"
        "<ExplanationTxt>Facility-policy narrative</ExplanationTxt></SupplementalInformationGrp>"
        if part_v_narrative else ""
    )
    part_vi = (
        "<SupplementalInformationDetail><FormAndLineReferenceDesc>Part VI</FormAndLineReferenceDesc>"
        "<ExplanationTxt>General supplemental narrative</ExplanationTxt></SupplementalInformationDetail>"
        if part_vi_narrative else ""
    )
    return (
        "<Return xmlns=\"http://www.irs.gov/efile\">"
        "<ReturnHeader><TaxYr>2025</TaxYr><Filer><EIN>000000000</EIN>"
        "<BusinessName><BusinessNameLine1Txt>Example Community Hospital</BusinessNameLine1Txt>"
        "<BusinessNameLine2Txt>Testing Division</BusinessNameLine2Txt></BusinessName></Filer></ReturnHeader>"
        "<ReturnData><IRS990>" + "".join(rows) + "</IRS990>"
        "<IRS990ScheduleH>"
        "<FinancialAssistanceAtCostTyp><TotalCommunityBenefitExpnsAmt>1234.50</TotalCommunityBenefitExpnsAmt>"
        "<NetCommunityBenefitExpnsAmt>1111.25</NetCommunityBenefitExpnsAmt><TotalExpensePct>0.0125</TotalExpensePct>"
        "</FinancialAssistanceAtCostTyp><BadDebtExpenseAmt>77</BadDebtExpenseAmt>"
        "<HospitalFcltyPoliciesPrctcGrp><HospitalFacilityName>"
        "<BusinessNameLine1Txt>Example East Facility</BusinessNameLine1Txt>"
        "</HospitalFacilityName><FacilityNum>1</FacilityNum>"
        "<FPGFamilyIncmLmtFreeCarePct>200</FPGFamilyIncmLmtFreeCarePct>"
        "<FPGFamilyIncmLmtDscntCarePct>400</FPGFamilyIncmLmtDscntCarePct>"
        "<FPGFamilyIncmLmtFreeDscntInd>true</FPGFamilyIncmLmtFreeDscntInd>"
        "<EligCriteriaExplainedInd>true</EligCriteriaExplainedInd>" + publicity +
        "<CollectionActivitiesInd>false</CollectionActivitiesInd>"
        "<PermitReportToCreditAgencyInd>true</PermitReportToCreditAgencyInd>"
        "<ReportingToCreditAgencyInd>false</ReportingToCreditAgencyInd>"
        "</HospitalFcltyPoliciesPrctcGrp>" + second_facility + part_v + part_vi +
        "</IRS990ScheduleH></ReturnData></Return>"
    ).encode("utf-8")


def facility_key(parser: Any, path: str) -> str:
    """Return the public output key for one verified per-facility XML leaf."""
    matches = [name for name, spec in parser.FACILITY_FIELDS.items() if spec[0] == path]
    assert len(matches) == 1, f"Expected one FACILITY_FIELDS entry for {path}; found {matches}"
    return matches[0]


def test_verified_namespace_xml_fields_provenance_and_percent_semantics(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Extract current Schedule H fields without confusing ratio and FPG percentages."""
    parser = parser_with_roots(monkeypatch, tmp_path)
    profile = parser.parse_xml(sample_xml(include_publicity=True))

    assert profile["financial_assistance_at_cost"] == {
        "value": "1234.50", "source": "xml", "ref": "Schedule H Part I line 7a(c)"
    }
    assert profile["financial_assistance_expense_pct"] == {
        "value": "1.2500", "source": "xml", "ref": "Schedule H Part I line 7a(f)"
    }
    assert profile["bad_debt_expense"] == {
        "value": "77", "source": "xml", "ref": "Schedule H Part III line 2"
    }
    assert profile["ein"]["value"] == "000000000"  # IRS XML lexical form: nine digits, no display hyphen.
    assert profile["organization_legal_name"]["value"] == "Example Community Hospital Testing Division"

    facility = profile["facilities"]["value"][0]
    assert facility["fpg_free_care_pct"] == {
        "value": "200", "source": "xml", "ref": "Schedule H Part V Section B line 13a"
    }
    assert facility["fpg_discounted_care_pct"] == {
        "value": "400", "source": "xml", "ref": "Schedule H Part V Section B line 13a"
    }
    assert facility["eligibility_criteria_explained"] == {
        "value": True, "source": "xml", "ref": "Schedule H Part V Section B line 13"
    }
    assert facility["fpg_criterion_selected"] == {
        "value": True, "source": "xml", "ref": "Schedule H Part V Section B line 13a"
    }
    assert facility["fap_publicity_measures"] == {
        "value": False, "source": "xml", "ref": "Schedule H Part V Section B line 16"
    }
    assert facility["collection_activities"] == {
        "value": False, "source": "xml", "ref": "Schedule H Part V Section B line 19"
    }


def test_module_imports_without_an_environment_file(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Import the parser without reading or requiring a credential file."""
    missing_env = tmp_path / "does-not-exist.env"
    monkeypatch.setenv("HEALTHBILLS_ROOT", str(tmp_path / "health-root"))
    monkeypatch.setenv("MEDBILL_KIT_ENV_FILE", str(missing_env))
    sys.modules.pop("scripts.parse_990", None)
    parser = importlib.import_module("scripts.parse_990")
    assert parser.ENV_FILE == missing_env
    assert not missing_env.exists()


def test_false_and_missing_facility_answers_stay_distinct(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Preserve stated false and leave omitted elements null rather than treating them alike."""
    parser = parser_with_roots(monkeypatch, tmp_path)
    facility = parser.parse_xml(sample_xml())["facilities"]["value"][0]
    assert facility["collection_activities"]["value"] is False
    assert facility["collection_activities"]["source"] == "xml"
    assert facility["fap_publicity_measures"] == {
        "value": None, "source": None, "ref": "Schedule H Part V Section B line 16"
    }


def test_namespace_free_xml_matches_namespace_qualified_xml(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Accept the same verified element structure whether the IRS namespace is present or absent."""
    parser = parser_with_roots(monkeypatch, tmp_path)
    qualified = sample_xml()
    namespace_free = qualified.replace(b' xmlns="http://www.irs.gov/efile"', b"")
    assert parser.parse_xml(namespace_free) == parser.parse_xml(qualified)


def test_facilities_remain_separate_with_identity_and_missing_fpg_values(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Retain distinct facility records and do not borrow FPG answers across facilities."""
    parser = parser_with_roots(monkeypatch, tmp_path)
    facilities = parser.parse_xml(sample_xml(two_facilities=True))["facilities"]["value"]
    assert len(facilities) == 2
    assert facilities[0]["facility_name_line_1"]["value"] == "Example East Facility"
    assert facilities[0]["facility_number"]["value"] == "1"
    assert facilities[0]["fpg_free_care_pct"]["value"] == "200"
    assert facilities[1]["facility_name_line_1"] == {
        "value": "Sample South Facility", "source": "xml", "ref": "Schedule H Part V Section B heading"
    }
    assert facilities[1]["facility_number"]["value"] == "2"
    assert facilities[1]["fpg_criterion_selected"]["value"] is False
    assert facilities[1]["fpg_free_care_pct"] == {
        "value": None, "source": None, "ref": "Schedule H Part V Section B line 13a"
    }


def test_zero_and_missing_schedule_h_scalars_remain_distinct(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Keep a stated zero while an omitted bad-debt/FAP amount stays null."""
    parser = parser_with_roots(monkeypatch, tmp_path)
    zero_fap = sample_xml().replace(b">1234.50</TotalCommunityBenefitExpnsAmt>", b">0</TotalCommunityBenefitExpnsAmt>")
    profile = parser.parse_xml(zero_fap)
    assert profile["financial_assistance_at_cost"] == {
        "value": "0", "source": "xml", "ref": "Schedule H Part I line 7a(c)"
    }
    assert profile["bad_debt_fap_eligible"] == {
        "value": None, "source": None, "ref": "Schedule H Part III line 3"
    }


def test_part_v_narrative_does_not_substitute_for_part_vi_narrative(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Use SupplementalInformationDetail only for the supported Part VI presence flag."""
    parser = parser_with_roots(monkeypatch, tmp_path)
    part_v_only = parser.parse_xml(sample_xml(part_v_narrative=True))
    part_vi = parser.parse_xml(sample_xml(part_vi_narrative=True))
    assert part_v_only["supplemental_narrative_present"] == {
        "value": None, "source": None, "ref": "Schedule H Part VI"
    }
    assert part_vi["supplemental_narrative_present"] == {
        "value": True, "source": "xml", "ref": "Schedule H Part VI"
    }


def test_permit_and_actual_eca_paths_are_separate(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Keep Schedule H line 18 policy permission distinct from line 19 actual activity."""
    parser = parser_with_roots(monkeypatch, tmp_path)
    permit_path = "PermitReportToCreditAgencyInd"
    actual_path = "ReportingToCreditAgencyInd"
    permit_key = facility_key(parser, permit_path)
    actual_key = facility_key(parser, actual_path)
    assert permit_key != actual_key
    assert parser.FACILITY_FIELDS[permit_key][1].startswith("Schedule H Part V Section B line 18")
    assert parser.FACILITY_FIELDS[actual_key][1].startswith("Schedule H Part V Section B line 19")
    facility = parser.parse_xml(sample_xml())["facilities"]["value"][0]
    assert facility[permit_key]["value"] is True
    assert facility[actual_key]["value"] is False


def test_top_five_compensation_is_descending_and_truncated(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Rank complete D/E/F amounts and return only the top five people."""
    parser = parser_with_roots(monkeypatch, tmp_path)
    compensation = parser.parse_xml(sample_xml())["top_five_compensation"]
    assert compensation["source"] == "xml"
    assert [row["name"]["value"] for row in compensation["value"]] == [
        "Alpha Example", "Bravo Example", "Charlie Example", "Delta Example", "Echo Example"
    ]
    assert [row["total_compensation"]["value"] for row in compensation["value"]] == ["911", "811", "711", "411", "311"]


def test_incomplete_compensation_is_null(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Avoid a misleading rank when an officer lacks one reported D/E/F component."""
    parser = parser_with_roots(monkeypatch, tmp_path)
    assert parser.parse_xml(sample_xml(incomplete_compensation=True))["top_five_compensation"] == {
        "value": None, "source": None, "ref": parser.COMPENSATION_REF
    }


def test_multiple_filings_are_rejected(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Reject a batch-like XML document rather than selecting an arbitrary Form 990."""
    parser = parser_with_roots(monkeypatch, tmp_path)
    original = sample_xml()
    duplicate = original.replace(b"<IRS990ScheduleH>", b"<IRS990></IRS990><IRS990ScheduleH>")
    assert duplicate != original
    assert duplicate.count(b"<IRS990>") == 2
    with pytest.raises(ValueError, match="Multiple IRS990 elements"):
        parser.parse_xml(duplicate)


def write_pdf(tmp_path: Path) -> Path:
    """Create a selectable-text synthetic PDF for the offline PDF dry-run path."""
    path = tmp_path / "synthetic_990.pdf"
    document = pymupdf.open()
    page = document.new_page()
    page.insert_text((72, 72), "SYNTHETIC SAMPLE, NOT A REAL FILING\nExample Community Hospital Form 990", fontsize=11)
    document.save(path)
    document.close()
    return path


def trap_environment(tmp_path: Path) -> tuple[Path, Path]:
    """Install child-process traps for prohibited credential-file reads and networking."""
    trap = tmp_path / "traps"
    trap.mkdir()
    (trap / "openai.py").write_text("raise RuntimeError('openai import forbidden')\n", encoding="utf-8")
    (trap / "sitecustomize.py").write_text(
        "import pathlib, socket\n"
        "_read_text = pathlib.Path.read_text\n"
        "def guarded_read_text(path, *args, **kwargs):\n"
        "    if path.name == 'env-read-sentinel.txt': raise RuntimeError('environment file read forbidden')\n"
        "    return _read_text(path, *args, **kwargs)\n"
        "pathlib.Path.read_text = guarded_read_text\n"
        "socket.create_connection=lambda *a, **k: (_ for _ in ()).throw(RuntimeError('network forbidden'))\n"
        "socket.socket.connect=lambda *a, **k: (_ for _ in ()).throw(RuntimeError('network forbidden'))\n",
        encoding="utf-8",
    )
    env_file = tmp_path / "env-read-sentinel.txt"
    env_file.write_text("must-not-be-read=1\n", encoding="utf-8")
    return trap, env_file


def test_cli_xml_dry_run_returns_zero_and_writes_nothing(tmp_path: Path) -> None:
    """Run XML dry-run through its CLI with output and network access constrained."""
    fixture = tmp_path / "form990_sample.xml"
    fixture.write_bytes(sample_xml())
    trap, env_file = trap_environment(tmp_path)
    health_root = tmp_path / "health-root"
    env = os.environ.copy()
    for key in ("AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_DEPLOYMENT", "OPENAI_API_KEY"):
        env.pop(key, None)
    env.update({
        "HEALTHBILLS_ROOT": str(health_root), "MEDBILL_KIT_ENV_FILE": str(env_file), "PYTHONPATH": str(trap),
    })
    result = subprocess.run(
        [sys.executable, "-B", str(REPO_ROOT / "scripts" / "parse_990.py"), "--xml", str(fixture), "--dry-run"],
        cwd=REPO_ROOT, env=env, capture_output=True, text=True, check=False,
    )
    assert result.returncode == 0, result.stderr
    assert '"financial_assistance_at_cost"' in result.stdout
    assert not (health_root / "_hospital_profiles").exists()


def test_cli_fetch_dry_run_plans_without_fetching_or_creating_target(tmp_path: Path) -> None:
    """Report an explicit XML fetch plan without importing, networking, parsing, or writing."""
    trap, env_file = trap_environment(tmp_path)
    health_root = tmp_path / "health-root"
    target = tmp_path / "not-yet-downloaded.xml"
    env = os.environ.copy()
    for key in ("AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_DEPLOYMENT", "OPENAI_API_KEY"):
        env.pop(key, None)
    env.update({
        "HEALTHBILLS_ROOT": str(health_root), "MEDBILL_KIT_ENV_FILE": str(env_file), "PYTHONPATH": str(trap),
    })
    result = subprocess.run(
        [
            sys.executable, "-B", str(REPO_ROOT / "scripts" / "parse_990.py"), "--xml", str(target),
            "--fetch-from", "https://example.invalid/filing.xml", "--dry-run",
        ],
        cwd=REPO_ROOT, env=env, capture_output=True, text=True, check=False,
    )
    assert result.returncode == 0, result.stderr
    assert '"network": "not invoked"' in result.stdout
    assert not target.exists()
    assert not (health_root / "_hospital_profiles").exists()


def test_cli_pdf_dry_run_without_credentials_returns_clear_two(tmp_path: Path) -> None:
    """Preview PDF extraction without importing OpenAI, reading credentials, calling, or writing."""
    fixture = write_pdf(tmp_path)
    trap, env_file = trap_environment(tmp_path)
    health_root = tmp_path / "health-root"
    env = os.environ.copy()
    for key in ("AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_DEPLOYMENT", "OPENAI_API_KEY"):
        env.pop(key, None)
    env.update({
        "HEALTHBILLS_ROOT": str(health_root), "MEDBILL_KIT_ENV_FILE": str(env_file), "PYTHONPATH": str(trap),
    })
    result = subprocess.run(
        [sys.executable, "-B", str(REPO_ROOT / "scripts" / "parse_990.py"), "--pdf", str(fixture), "--dry-run"],
        cwd=REPO_ROOT, env=env, capture_output=True, text=True, check=False,
    )
    assert result.returncode == 2
    assert "PDF model extraction requires credentials; dry-run made no call or credential-file read." in result.stderr
    assert '"instructions"' in result.stdout
    assert not (health_root / "_hospital_profiles").exists()
