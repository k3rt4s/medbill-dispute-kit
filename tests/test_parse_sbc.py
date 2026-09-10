"""test_parse_sbc.py, verify deterministic SBC parsing with fictional text-layer fixtures."""

from __future__ import annotations

import importlib
import os
import subprocess
import sys
from pathlib import Path

import pymupdf

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))
from scripts import parse_sbc


def build_fixture(tmp_path: Path, name: str, lines: list[str]) -> Path:
    """Create a selectable-text fictional SBC fixture in pytest's data-root temp path."""
    path = tmp_path / name
    document = pymupdf.open()
    page = document.new_page(width=612, height=792)
    page.insert_textbox(pymupdf.Rect(36, 36, 576, 756), "\n".join(lines), fontsize=8, fontname="helv")
    document.save(path)
    document.close()
    return path


def bespoke_fixture(tmp_path: Path) -> Path:
    """Build labeled fixture text for basic plan metadata and services."""
    return build_fixture(tmp_path, "sbc_sample.pdf", [
        "Summary of Benefits and Coverage", "Plan: Example Health Plan", "Plan year start: 01/01/2026", "Plan year end: 12/31/2026",
        "Coverage Period: 01/01/2026 - 12/31/2026", "What is the overall annual deductible?", "In-Network: $1,234 individual / $2,468 family",
        "Out-of-Network: $3,210 individual / $6,420 family", "What is the out-of-pocket limit?", "In-Network: $5,678.50 individual / $9,999 family",
        "Out-of-Network: $7,777 individual / $12,345 family", "Not included in the out-of-pocket limit: Premiums and balance-billed charges",
        "Overall annual limit on what the plan pays: No", "Referral needed to see a specialist: No", "Network provider check URL: https://example.invalid/network",
        "Plan phone number: 555-010-0123", "Primary care visit: $25 copay per visit", "Specialist visit: $50 copay per visit",
        "Diagnostic test: 20% coinsurance", "Imaging: 30% coinsurance", "Emergency room care: 20% coinsurance", "Emergency medical transportation: $150 copay",
        "Urgent care: $75 copay per visit", "Facility fee (e.g., hospital room): $500 per day", "Physician/surgeon fee: 20% coinsurance",
    ])


def standard_multiline_fixture(tmp_path: Path) -> Path:
    """Build table-like multiline text using standard SBC question headings."""
    return build_fixture(tmp_path, "sbc_standard_multiline.pdf", [
        "Summary of Benefits and Coverage", "What is the overall deductible?", "In-Network", "$1,234 Individual", "$2,468 Family",
        "Out-of-Network", "$3,210 Individual", "$6,420 Family", "Are there services covered before you meet your deductible?", "Yes",
        "What is the out-of-pocket limit?", "In-Network", "$5,678.50 Individual", "$9,999 Family", "Out-of-Network", "$7,777 Individual", "$12,345 Family",
        "What is not included in the out-of-pocket limit?", "Premiums", "Primary care visit to treat an injury or illness", "$25 copay per visit",
        "Specialist visit", "$50 copay per visit", "Diagnostic test", "20% coinsurance", "Imaging", "30% coinsurance",
    ])


def test_flat_spd_vocabulary_and_text_provenance(tmp_path: Path) -> None:
    """Extract flat deductible/OOP values and multiple fictional service rows."""
    profile = parse_sbc.extract_profile(parse_sbc.read_pdf_pages(bespoke_fixture(tmp_path)))
    assert profile["in_network_deductible_individual"] == {"value": "$1,234", "source": "text", "page": 0}
    assert profile["in_network_deductible_family"]["value"] == "$2,468"
    assert profile["out_network_oop_max_individual"]["value"] == "$7,777"
    assert profile["in_network_oop_max_individual"]["value"] == "$5,678.50"
    for name in ("primary_care_visit_cost_sharing", "specialist_visit_cost_sharing", "diagnostic_test_cost_sharing", "imaging_cost_sharing"):
        assert profile[name]["source"] == "text"
    assert profile["erisa_subject"] == {"value": None, "source": None, "page": None}


def test_standard_multiline_regions_do_not_mix_network_columns(tmp_path: Path) -> None:
    """Extract standard SBC headings and stop each network region before the next column."""
    profile = parse_sbc.extract_profile(parse_sbc.read_pdf_pages(standard_multiline_fixture(tmp_path)))
    assert profile["in_network_deductible_individual"]["value"] == "$1,234"
    assert profile["out_network_deductible_family"]["value"] == "$6,420"
    assert profile["in_network_oop_max_individual"]["value"] == "$5,678.50"
    assert profile["out_network_oop_max_family"]["value"] == "$12,345"
    assert profile["primary_care_visit_cost_sharing"] == {"value": "$25 copay per visit", "source": "text", "page": 0}
    assert profile["erisa_subject"]["source"] is None


def test_missing_service_value_does_not_borrow_the_next_service(tmp_path: Path) -> None:
    """Keep a missing primary-care value null when the next service has a cost."""
    fixture = build_fixture(tmp_path, "sbc_missing_primary.pdf", [
        "Primary care visit to treat an injury or illness",
        "Specialist visit",
        "$50 copay per visit",
        "What is the overall deductible?",
    ])
    profile = parse_sbc.extract_profile(parse_sbc.read_pdf_pages(fixture))
    assert profile["primary_care_visit_cost_sharing"] == {"value": None, "source": None, "page": None}
    assert profile["specialist_visit_cost_sharing"] == {"value": "$50 copay per visit", "source": "text", "page": 0}


def test_repeated_identical_label_still_extracts_the_value(tmp_path: Path) -> None:
    """Keep a network amount when a footnote repeats the same label and value verbatim."""
    fixture = build_fixture(tmp_path, "sbc_repeated_label.pdf", [
        "What is the overall deductible?",
        "In-Network: $1,234 individual / $2,468 family",
        "Individual $1,234 applies once per plan year, see footnote 2",
        "Out-of-Network: $3,210 individual / $6,420 family",
    ])
    profile = parse_sbc.extract_profile(parse_sbc.read_pdf_pages(fixture))
    assert profile["in_network_deductible_individual"]["value"] == "$1,234"
    assert profile["in_network_deductible_family"]["value"] == "$2,468"


def test_conflicting_labeled_amounts_stay_null(tmp_path: Path) -> None:
    """Reject a network amount when two different values carry the same label."""
    fixture = build_fixture(tmp_path, "sbc_conflicting_label.pdf", [
        "What is the overall deductible?",
        "In-Network: $1,234 individual / $2,468 family",
        "Individual $9,999 applies once per plan year, see footnote 2",
        "Out-of-Network: $3,210 individual / $6,420 family",
    ])
    profile = parse_sbc.extract_profile(parse_sbc.read_pdf_pages(fixture))
    assert profile["in_network_deductible_individual"] == {"value": None, "source": None, "page": None}


def test_model_merge_preserves_text_and_rejects_unsupported_evidence(tmp_path: Path) -> None:
    """Merge only known scalar model values into null fields without overwriting text."""
    profile = parse_sbc.extract_profile(parse_sbc.read_pdf_pages(bespoke_fixture(tmp_path)))
    result = parse_sbc.merge_model_fields(profile, {
        "plan_name": "Model must not replace Example Health Plan", "erisa_subject": "Yes", "unknown_field": "invented",
        "grievance_appeal_contact": {"value": "unsupported evidence", "source": "text"},
    })
    assert result["plan_name"]["value"] == "Example Health Plan"
    assert result["erisa_subject"] == {"value": "Yes", "source": "model", "page": None}
    assert "unknown_field" not in result
    assert result["grievance_appeal_contact"] == {"value": None, "source": None, "page": None}


def test_module_imports_without_env(monkeypatch: object) -> None:
    """Import the parser while the configurable environment file is absent."""
    monkeypatch.delenv("MEDBILL_KIT_ENV_FILE", raising=False)  # type: ignore[attr-defined]
    importlib.reload(parse_sbc)


def test_dry_run_never_imports_openai_reads_env_or_uses_network(tmp_path: Path) -> None:
    """Run dry-run behind import and socket traps and require the request preview."""
    fixture = bespoke_fixture(tmp_path)
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
    missing_env = tmp_path / "env-read-sentinel.txt"
    missing_env.write_text("raise-if-read=1\n", encoding="utf-8")
    env = os.environ.copy()
    env.update({"HEALTHBILLS_ROOT": str(tmp_path / "health"), "MEDBILL_KIT_ENV_FILE": str(missing_env), "PYTHONPATH": str(trap)})
    result = subprocess.run([sys.executable, "-B", str(REPO_ROOT / "scripts" / "parse_sbc.py"), "--pdf", str(fixture), "--plan-slug", "example", "--dry-run"], cwd=REPO_ROOT, env=env, capture_output=True, text=True, check=False)
    assert result.returncode == 0, result.stderr
    assert "model request preview" in result.stdout
    assert not (tmp_path / "health" / "_sbc_profiles" / "example.json").exists()
