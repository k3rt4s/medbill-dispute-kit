"""Structural checks for the LLM-read deduplication rules document."""

from __future__ import annotations

import re
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RULES_PATH = ROOT / "schemas" / "deduplication_rules.toml"
BILL_PATH = ROOT / "schemas" / "bill.toml"
TRACKER_PATH = ROOT / "schemas" / "tracker.toml"
FIELD_REFERENCE = re.compile(r"(?:new|existing)\.([a-z_]+)")
REQUIRED_RULE_KEYS = {"id", "weight", "match", "action", "description"}


def _load_toml(path: Path) -> dict:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def _available_fields() -> set[str]:
    bill = _load_toml(BILL_PATH)
    tracker = _load_toml(TRACKER_PATH)
    return set(bill["fields"]) | {column["name"] for column in tracker["columns"]}


def test_rules_file_is_valid_toml_and_is_version_0_2_0() -> None:
    rules = _load_toml(RULES_PATH)

    assert rules["meta"]["schema"] == "deduplication_rules"
    assert rules["meta"]["schema_version"] == "0.2.0"
    assert rules["meta"]["notes"]


def test_each_rule_has_required_keys_and_unique_id() -> None:
    rules = _load_toml(RULES_PATH)["rules"]
    ids = []

    for rule in rules:
        assert REQUIRED_RULE_KEYS <= set(rule)
        assert isinstance(rule["weight"], int)
        assert rule["match"]
        assert rule["action"]
        assert rule["description"]
        ids.append(rule["id"])

    assert len(ids) == len(set(ids))


def test_match_field_references_exist_in_bill_or_tracker_schema() -> None:
    available_fields = _available_fields()
    rules = _load_toml(RULES_PATH)["rules"]
    references = {
        field
        for rule in rules
        for field in FIELD_REFERENCE.findall(rule["match"])
    }

    assert references
    assert references <= available_fields


def test_explicit_score_bands_are_complete_and_non_overlapping() -> None:
    bands = _load_toml(RULES_PATH)["score_bands"]

    assert bands["create_new_row_min"] == 0
    assert bands["create_new_row_min"] <= bands["create_new_row_max"]
    assert bands["create_new_row_max"] + 1 == bands["ask_patient_min"]
    assert bands["ask_patient_min"] <= bands["ask_patient_max"]
    assert bands["ask_patient_max"] + 1 == bands["merge_without_asking_min"]
    assert bands["merge_without_asking_min"] <= bands["merge_without_asking_max"]
    assert bands["merge_without_asking_max"] == 100
    assert "maximum weight" in bands["aggregation"]
    assert "Do not add weights" in bands["aggregation"]
    assert bands["precedence"]


def test_v2_rules_include_conservative_guards_and_payment_exception() -> None:
    rules = {rule["id"]: rule for rule in _load_toml(RULES_PATH)["rules"]}

    assert rules["exact_account_number"]["weight"] == 100
    assert "normalize(new.account_number)" in rules["exact_account_number"]["match"]
    assert "both normalized account numbers are nonempty" in rules["exact_account_number"]["match"]
    assert "both statement numbers are nonempty" in rules["exact_statement_number"]["match"]
    assert rules["itemized_content_hash"]["weight"] == 90
    assert "new.line_items" in rules["itemized_content_hash"]["match"]
    assert "new.provider_type == existing.provider_type" in rules["itemized_content_hash"]["match"]
    assert "both dates of service are nonempty" in rules["itemized_content_hash"]["match"]
    assert "both patient_account_id values are nonempty" in rules["itemized_content_hash"]["match"]
    assert "both encounter_id values are nonempty" in rules["itemized_content_hash"]["match"]
    assert "new.patient_account_id == existing.patient_account_id" in rules["itemized_content_hash"]["match"]
    assert "new.encounter_id == existing.encounter_id" in rules["itemized_content_hash"]["match"]
    assert "NOT (both patient_account_id values are nonempty" in rules["itemized_content_hash"]["match"]
    assert "NOT (both encounter_id values are nonempty" in rules["itemized_content_hash"]["match"]
    assert rules["two_of_three_match"]["action"] == "candidate_for_confirmation"
    assert "are each nonempty on both records" in rules["two_of_three_match"]["match"]
    assert "new.total_patient_paid > existing.total_patient_paid" in rules["balance_trajectory"]["match"]
    assert "<= 0.01" in rules["balance_trajectory"]["match"]
    assert "30 through 89" in rules["ambiguous_match_prompt_user"]["match"]
    assert "maximum eligible identity-rule score" in rules["ambiguous_match_prompt_user"]["match"]


def test_rules_touched_by_v2_have_dated_notes() -> None:
    rules = {rule["id"]: rule for rule in _load_toml(RULES_PATH)["rules"]}

    for rule_id in (
        "exact_account_number",
        "itemized_content_hash",
        "balance_trajectory",
        "ambiguous_match_prompt_user",
    ):
        assert "2026-09-07" in rules[rule_id]["notes"]
