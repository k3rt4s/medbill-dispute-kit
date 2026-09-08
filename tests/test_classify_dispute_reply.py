"""Tests for the deterministic written-dispute-reply classifier."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import re

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = PROJECT_ROOT / "schemas" / "reply_patterns.toml"
TEMPLATE_PATH = PROJECT_ROOT / "templates" / "letter_dispute_reply.md"


# These source definitions keep the fictional fixtures reproducible in a fresh
# clone. The test writes JSON copies to pytest's tmp_path, which is directed to
# the data-root basetemp by the required test command.
FIXTURE_SPECS = (
    {
        "id": "a_obvious", "coverage_block": "A",
        "reply": "Fictional notice: Our billing policy follows standard billing procedures; our policy is to send this response.",
        "expected_blocks": ["A"], "expected_ambiguous": False,
    },
    {
        "id": "a_borderline", "coverage_block": "A",
        "reply": "Fictional notice: Our billing policy appears in the printed handout.",
        "expected_blocks": [], "expected_ambiguous": True,
    },
    {
        "id": "b_obvious", "coverage_block": "B",
        "reply": "Fictional statement: This new statement lists the amount due and repeats the balance due.",
        "expected_blocks": ["B"], "expected_ambiguous": False,
    },
    {
        "id": "b_borderline", "coverage_block": "B",
        "reply": "Fictional statement: The amount due appears in the mailing.",
        "expected_blocks": [], "expected_ambiguous": True,
    },
    {
        "id": "c_obvious", "coverage_block": "C",
        "reply": "Fictional review: We have reviewed your account, the balance is correct, and we reviewed and determined no change.",
        "expected_blocks": ["C"], "expected_ambiguous": False,
    },
    {
        "id": "c_borderline", "coverage_block": "C",
        "reply": "Fictional review: We have reviewed your account.",
        "expected_blocks": [], "expected_ambiguous": True,
    },
    {
        "id": "d_obvious", "coverage_block": "D",
        "reply": "Fictional offer: A payment plan, hardship discount, and monthly payments are available.",
        "expected_blocks": ["D"], "expected_ambiguous": False,
    },
    {
        "id": "d_borderline", "coverage_block": "D",
        "reply": "Fictional offer: A payment plan may be discussed.",
        "expected_blocks": [], "expected_ambiguous": True,
    },
    {
        "id": "e_obvious", "coverage_block": "E",
        "reply": "Fictional contact note: Please call, call our billing department, or contact us by phone.",
        "expected_blocks": ["E"], "expected_ambiguous": False,
    },
    {
        "id": "e_borderline", "coverage_block": "E",
        "reply": "Fictional contact note: Please call when convenient.",
        "expected_blocks": [], "expected_ambiguous": True,
    },
    {
        "id": "multiple_b_c", "coverage_block": "B",
        "reply": "Fictional statement review: This new statement lists the amount due and balance due. We have reviewed your account, the balance is correct, and reviewed and determined no change.",
        "expected_blocks": ["B", "C"], "expected_ambiguous": True,
    },
    {
        "id": "vague", "coverage_block": "",
        "reply": "Fictional reply received.",
        "expected_blocks": [], "expected_ambiguous": True,
    },
)


def _load_module():
    spec = importlib.util.spec_from_file_location(
        "classify_dispute_reply", PROJECT_ROOT / "scripts" / "classify_dispute_reply.py",
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CLASSIFIER = _load_module()


@pytest.fixture
def generated_fixture_dir(tmp_path: Path) -> Path:
    """Materialize fixture JSON under pytest's externally configured basetemp."""
    fixture_dir = tmp_path / "replies"
    fixture_dir.mkdir()
    for fixture in FIXTURE_SPECS:
        (fixture_dir / f"{fixture['id']}.json").write_text(
            json.dumps(fixture, indent=2) + "\n", encoding="utf-8",
        )
    return fixture_dir


def test_fixture_set_has_required_coverage(generated_fixture_dir: Path) -> None:
    materialized = [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(generated_fixture_dir.glob("*.json"))
    ]
    assert {item["id"]: item for item in materialized} == {
        item["id"]: item for item in FIXTURE_SPECS
    }
    assert len(FIXTURE_SPECS) >= 10
    for block in "ABCDE":
        assert sum(item["coverage_block"] == block for item in FIXTURE_SPECS) >= 2
    assert any(item["id"] == "multiple_b_c" for item in FIXTURE_SPECS)
    assert any(item["id"] == "vague" for item in FIXTURE_SPECS)


@pytest.mark.parametrize("fixture", FIXTURE_SPECS, ids=lambda item: item["id"])
def test_classifier_matches_fictional_fixtures(fixture: dict) -> None:
    result = CLASSIFIER.classify_dispute_reply(fixture["reply"])
    assert result["blocks"] == fixture["expected_blocks"]
    assert result["ambiguous"] is fixture["expected_ambiguous"]
    assert all(0.0 <= score <= 1.0 for score in result["scores"].values())
    for items in result["evidence"].values():
        for evidence in items:
            assert evidence in fixture["reply"]


def test_empty_reply_is_ambiguous_with_no_blocks() -> None:
    result = CLASSIFIER.classify_dispute_reply("")
    assert result["blocks"] == []
    assert result["ambiguous"] is True
    assert all(items == [] for items in result["evidence"].values())


def test_schema_blocks_match_actual_template_markers() -> None:
    rules = CLASSIFIER._load_rules(SCHEMA_PATH)
    schema_blocks = {pattern["block"] for pattern in rules["patterns"]}
    template_blocks = set(re.findall(r"\[BLOCK ([A-E]),", TEMPLATE_PATH.read_text(encoding="utf-8")))
    assert schema_blocks == template_blocks == set("ABCDE")


def test_classifier_has_no_network_or_credentials_dependency() -> None:
    source = (PROJECT_ROOT / "scripts" / "classify_dispute_reply.py").read_text(encoding="utf-8").lower()
    for forbidden in ("requests", "urllib", "http", "socket", "openai", "azure", "api_key", "dotenv"):
        assert forbidden not in source
