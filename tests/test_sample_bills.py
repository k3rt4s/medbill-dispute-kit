"""Regress synthetic bill fixtures, schema conformance, and identifier guards."""
from __future__ import annotations

import csv
import datetime as dt
from decimal import Decimal
import importlib.util
import json
from pathlib import Path
import re
import socket
import sys
import tomllib

import pymupdf
import pytest

ROOT = Path(__file__).resolve().parents[1]
GENERATORS = ROOT / "examples" / "sample_bills"
sys.path.insert(0, str(GENERATORS))
from fixture_tools import BANNER

NPI_RE = re.compile(r"(?<!\d)(?!0000000000(?!\d))\d{10}(?!\d)")
SSN_RE = re.compile(r"(?<!\d)\d{3}-\d{2}-\d{4}(?!\d)")
PHONE_RE = re.compile(
    r"(?<!\d)(?:\+?1[ .-]?)?\(?[2-9]\d{2}\)?[ .-](?P<exchange>\d{3})[ .-]\d{4}(?!\d)"
)


def load_module(name: str, path: Path):
    """Load a module by path without importing the whole scripts package."""
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def document_text(path: Path) -> str:
    """Return visible text from a Markdown or PDF fixture."""
    if path.suffix == ".pdf":
        with pymupdf.open(path) as pdf:
            return "\n".join(page.get_text() for page in pdf)
    return path.read_text(encoding="utf-8")


def assert_synthetic_identifiers(text: str) -> None:
    """Reject realistic identifier shapes while allowing reserved fake values."""
    assert not NPI_RE.search(text), "nonzero ten-digit identifier"
    assert not SSN_RE.search(text), "SSN-shaped identifier"
    assert all(
        m.group("exchange") == "555" for m in PHONE_RE.finditer(text)
    ), "phone outside 555 exchange"


@pytest.fixture(scope="module")
def cases(tmp_path_factory):
    """Generate all sample bill cases under pytest's temporary directory."""
    output = tmp_path_factory.mktemp("sample_bills")
    for source in sorted(GENERATORS.glob("generate_cases_*.py")):
        load_module(source.stem, source).generate(output)
    return sorted(output.glob("case_*"))


@pytest.fixture(autouse=True)
def offline(monkeypatch, tmp_path):
    """Prevent accidental network or credential use from fixture tests."""
    def forbidden(*args, **kwargs):
        raise AssertionError("network access is forbidden")

    monkeypatch.setattr(socket, "create_connection", forbidden)
    monkeypatch.setattr(socket.socket, "connect", forbidden)
    monkeypatch.setenv("HEALTHBILLS_ROOT", str(tmp_path / "health"))
    monkeypatch.setenv("MEDBILL_KIT_ENV_FILE", str(tmp_path / "absent-credentials.txt"))
    for key in (
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_DEPLOYMENT",
        "OPENAI_API_KEY",
    ):
        monkeypatch.delenv(key, raising=False)


def test_all_six_cases_exist(cases):
    """All committed generators produce their expected case folders."""
    assert [p.name[:7] for p in cases] == [f"case_{n:02d}" for n in range(1, 7)]


def test_identifier_guard_rejects_prohibited_shapes():
    """Fixture text uses reserved fake identifiers and 555 phone numbers only."""
    assert_synthetic_identifiers("NPI 0000000000; EIN 00-0000000; phone 615-555-0100")
    for prohibited in ("1234567890", "123-45-6789", "615-123-4567", "(615) 123-4567"):
        with pytest.raises(AssertionError):
            assert_synthetic_identifiers(prohibited)


def test_case_files_and_banners_and_identifier_guard(cases):
    """Every generated artifact carries the synthetic banner and fake identifiers."""
    assert cases
    for case in cases:
        readme = (case / "README.md").read_text(encoding="utf-8")
        listed = re.findall(r"^- `([^`]+)`$", readme, re.MULTILINE)
        assert listed and {p.name for p in case.iterdir()} == set(listed) | {"README.md"}
        for path in case.iterdir():
            text = document_text(path)
            assert BANNER in " ".join(text.split()), path
            assert_synthetic_identifiers(text)
            if path.suffix == ".pdf":
                markdown = path.with_suffix(".md").read_text(encoding="utf-8")
                assert " ".join(text.split()) == " ".join(markdown.split())


def test_expected_field_sets_and_required_values(cases):
    """Generated expected.json files match the public bill schema and tracker."""
    fields = tomllib.loads((ROOT / "schemas" / "bill.toml").read_text())["fields"]
    header = next(csv.reader((ROOT / "tracker" / "tracker_template.csv").read_text().splitlines()))
    for case in cases:
        expected = json.loads((case / "expected.json").read_text())
        assert set(expected) == {"notes", "bills", "tracker_rows"}
        assert len(expected["bills"]) == len(expected["tracker_rows"]) >= 1
        for bill, row in zip(expected["bills"], expected["tracker_rows"]):
            assert set(bill) <= fields.keys()
            assert set(row) <= set(header)
            assert row["bill_id"] == bill["bill_id"]
            assert isinstance(row["has_eob"], bool)
            assert isinstance(row["has_itemization"], bool)
            for name, spec in fields.items():
                if spec.get("required"):
                    assert name in bill and bill[name] not in (None, "", [])
                if name not in bill:
                    continue
                value = bill[name]
                if "enum" in spec:
                    assert value in spec["enum"]
                kind = spec["type"]
                if kind == "date":
                    assert dt.date.fromisoformat(value).isoformat() == value
                elif kind == "decimal":
                    assert not isinstance(value, bool) and Decimal(str(value)).is_finite()
                elif kind == "boolean":
                    assert isinstance(value, bool)
                elif kind == "string":
                    assert isinstance(value, str)
                elif kind == "array<string>":
                    assert isinstance(value, list) and all(isinstance(v, str) for v in value)
                if name == "findings":
                    assert set(value) <= set(spec["controlled_vocabulary"])
            for line in bill.get("line_items", []):
                assert set(line) == {"description", "cpt_code", "charge", "units", "date"}
                assert Decimal(str(line["charge"])).is_finite()
                assert Decimal(str(line["units"])) > 0
                dt.date.fromisoformat(line["date"])


def test_tracker_csv_accepts_expected_values(cases, tmp_path, monkeypatch):
    """Synthetic tracker rows pass the public tracker validator."""
    validator = load_module("sample_tracker_validator", ROOT / "scripts" / "validate_tracker.py")
    header = next(csv.reader((ROOT / "tracker" / "tracker_template.csv").read_text().splitlines()))

    def cell(value):
        if isinstance(value, bool):
            return str(value).lower()
        if isinstance(value, list):
            return ";".join(value)
        return str(value) if value is not None else ""

    target = tmp_path / "synthetic_tracker.csv"
    with target.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=header)
        writer.writeheader()
        for case in cases:
            for row in json.loads((case / "expected.json").read_text())["tracker_rows"]:
                writer.writerow({key: cell(value) for key, value in row.items()})
    monkeypatch.setattr(sys, "argv", ["validate_tracker.py", str(target)])
    assert validator.main() == 0


def test_pure_itemization_detector(cases):
    """The pure itemization heuristic agrees with generated expected rows."""
    indexer = load_module("sample_indexer", ROOT / "scripts" / "index_bills_and_claims.py")
    for case in cases:
        expected = json.loads((case / "expected.json").read_text())
        bills = [
            p for p in sorted(case.glob("*.md"))
            if p.name != "README.md" and "eob" not in p.stem.lower()
        ]
        assert len(bills) == len(expected["tracker_rows"])
        for document, row in zip(bills, expected["tracker_rows"]):
            actual, signals = indexer.detect_is_itemized(document.read_text(encoding="utf-8"))
            assert actual is row["has_itemization"], (document.name, signals)


def test_followup_and_multi_provider_expectations(cases):
    """Follow-up and multi-provider fixtures encode their intended relationships."""
    by_number = {
        int(case.name[5:7]): json.loads((case / "expected.json").read_text())
        for case in cases
    }
    first, followup = by_number[1]["bills"][0], by_number[4]["bills"][0]
    for key in ("account_number", "bill_id", "encounter_id", "provider_name", "line_items"):
        assert first[key] == followup[key]
    balance_delta = Decimal(str(first["current_balance"])) - Decimal(str(followup["current_balance"]))
    paid_delta = Decimal(str(followup["total_patient_paid"])) - Decimal(str(first["total_patient_paid"]))
    assert balance_delta == paid_delta
    encounter = by_number[3]["bills"]
    assert len(encounter) == len({b["bill_id"] for b in encounter}) == 3
    assert len({b["provider_type"] for b in encounter}) == 3
    assert len({b["encounter_id"] for b in encounter}) == 1
