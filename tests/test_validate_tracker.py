"""Tests for scripts/validate_tracker.py.

Run with:
    python -m pytest tests/

The validator script is imported by path because it lives outside the test
package. Tests construct temporary CSVs to confirm both happy and unhappy
paths.
"""

import csv
import importlib.util
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = REPO_ROOT / "scripts" / "validate_tracker.py"
SCHEMAS_DIR = REPO_ROOT / "schemas"


@pytest.fixture(scope="module")
def validator_module():
    """Import the validator script as a module."""
    spec = importlib.util.spec_from_file_location("validate_tracker", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["validate_tracker"] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def schemas(validator_module):
    return validator_module.load_schemas(SCHEMAS_DIR)


def _write_csv(tmp_path: Path, header: list[str], rows: list[list[str]]) -> Path:
    path = tmp_path / "tracker.csv"
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)
    return path


def _example_row(schemas) -> list[str]:
    """Return a row that satisfies all required columns and types."""
    columns = schemas["tracker_columns"]
    values: dict[str, str] = {}
    for col in columns:
        name = col["name"]
        col_type = col.get("type", "string")
        if name == "bill_id":
            values[name] = "B-2026-001"
        elif name == "encounter_id":
            values[name] = "E-2026-001"
        elif name == "provider_name":
            values[name] = "Example General Hospital"
        elif name == "provider_type":
            values[name] = "hospital"
        elif name == "account_number":
            values[name] = "ACCT123456"
        elif name == "statement_date":
            values[name] = "2026-04-30"
        elif name == "date_of_service_start":
            values[name] = "2026-03-15"
        elif name == "date_of_service_end":
            values[name] = "2026-03-17"
        elif name == "total_billed":
            values[name] = "12500.00"
        elif name == "current_balance":
            values[name] = "1500.00"
        elif name == "insurance_carrier":
            values[name] = "Example Health Plan"
        elif name == "in_network_status":
            values[name] = "in_network"
        elif name == "was_emergency":
            values[name] = "false"
        elif name == "findings":
            values[name] = "no_itemization"
        elif name == "next_action":
            values[name] = "request_itemization"
        elif name == "next_action_due":
            values[name] = "2026-05-18"
        elif name == "last_action_taken":
            values[name] = "received_bill"
        elif name == "last_action_date":
            values[name] = "2026-04-30"
        elif name == "certified_mail_last":
            values[name] = ""
        elif name == "status":
            values[name] = "open"
        elif name == "last_statement_date":
            values[name] = "2026-04-30"
        elif name == "notes":
            values[name] = "test row"
        else:
            values[name] = ""
    return [values[c["name"]] for c in columns]


def test_load_schemas_returns_expected_keys(schemas):
    assert "tracker_columns" in schemas
    assert "findings_vocab" in schemas
    assert "next_action_enum" in schemas
    assert "status_enum" in schemas
    assert "provider_type_enum" in schemas
    assert "in_network_enum" in schemas
    assert len(schemas["tracker_columns"]) > 0


def test_valid_row_passes(tmp_path, schemas, validator_module):
    header = [c["name"] for c in schemas["tracker_columns"]]
    rows = [_example_row(schemas)]
    csv_path = _write_csv(tmp_path, header, rows)
    sys.argv = ["validate_tracker.py", str(csv_path), "--schemas-dir", str(SCHEMAS_DIR)]
    rc = validator_module.main()
    assert rc == 0


def test_missing_required_column_fails(tmp_path, schemas, validator_module):
    header = [c["name"] for c in schemas["tracker_columns"]]
    row = _example_row(schemas)
    # Empty out a required field; bill_id is required.
    bill_id_idx = header.index("bill_id")
    row[bill_id_idx] = ""
    csv_path = _write_csv(tmp_path, header, [row])
    sys.argv = ["validate_tracker.py", str(csv_path), "--schemas-dir", str(SCHEMAS_DIR)]
    rc = validator_module.main()
    assert rc == 1


def test_bad_date_format_fails(tmp_path, schemas, validator_module):
    header = [c["name"] for c in schemas["tracker_columns"]]
    row = _example_row(schemas)
    idx = header.index("statement_date")
    row[idx] = "04/30/2026"  # not ISO 8601
    csv_path = _write_csv(tmp_path, header, [row])
    sys.argv = ["validate_tracker.py", str(csv_path), "--schemas-dir", str(SCHEMAS_DIR)]
    rc = validator_module.main()
    assert rc == 1


def test_bad_decimal_format_fails(tmp_path, schemas, validator_module):
    header = [c["name"] for c in schemas["tracker_columns"]]
    row = _example_row(schemas)
    idx = header.index("current_balance")
    row[idx] = "1,500"  # comma not allowed
    csv_path = _write_csv(tmp_path, header, [row])
    sys.argv = ["validate_tracker.py", str(csv_path), "--schemas-dir", str(SCHEMAS_DIR)]
    rc = validator_module.main()
    assert rc == 1


def test_bad_enum_value_fails(tmp_path, schemas, validator_module):
    header = [c["name"] for c in schemas["tracker_columns"]]
    row = _example_row(schemas)
    idx = header.index("status")
    row[idx] = "completely_made_up_status"
    csv_path = _write_csv(tmp_path, header, [row])
    sys.argv = ["validate_tracker.py", str(csv_path), "--schemas-dir", str(SCHEMAS_DIR)]
    rc = validator_module.main()
    assert rc == 1


def test_bad_findings_token_fails(tmp_path, schemas, validator_module):
    header = [c["name"] for c in schemas["tracker_columns"]]
    row = _example_row(schemas)
    idx = header.index("findings")
    row[idx] = "no_itemization;invented_finding_xyz"
    csv_path = _write_csv(tmp_path, header, [row])
    sys.argv = ["validate_tracker.py", str(csv_path), "--schemas-dir", str(SCHEMAS_DIR)]
    rc = validator_module.main()
    assert rc == 1


def test_header_order_mismatch_fails(tmp_path, schemas, validator_module):
    columns = schemas["tracker_columns"]
    header = [c["name"] for c in columns]
    # Swap two adjacent columns
    header[0], header[1] = header[1], header[0]
    rows = [_example_row(schemas)]
    csv_path = _write_csv(tmp_path, header, rows)
    sys.argv = ["validate_tracker.py", str(csv_path), "--schemas-dir", str(SCHEMAS_DIR)]
    rc = validator_module.main()
    assert rc == 1
