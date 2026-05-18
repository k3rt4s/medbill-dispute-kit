#!/usr/bin/env python3
"""
validate_tracker.py

Optional helper for medbill-dispute-kit. Validates a tracker CSV against the
TOML schemas in ../schemas/. Standard library only; no external dependencies.

Usage:
    python validate_tracker.py path/to/tracker.csv
    python validate_tracker.py path/to/tracker.csv --schemas-dir ../schemas

Exit codes:
    0 — file is valid
    1 — file is invalid; problems printed to stderr
    2 — usage error or file not found

The script checks:
    - All required columns present, in the order specified by schemas/tracker.toml
    - Date fields parse as ISO 8601 (YYYY-MM-DD)
    - Decimal fields parse as decimal numbers
    - Enum fields contain only allowed values (sourced from schemas/bill.toml)
    - Semicolon-separated findings entries match the controlled vocabulary
    - Boolean fields contain only "true", "false", or empty

This script does not validate logical correctness (e.g., that a bill flagged
as `dispute_state_balance_billing` is actually in a state with such a
statute). It only validates structural conformance.
"""

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Iterable


# ---------------------------------------------------------------------------
# Minimal TOML reader
#
# We only need to pull enum lists and required-field flags out of the schema
# files. Python 3.11+ has tomllib; we use that. For 3.10 and earlier, the
# script will print a clear message and exit.
# ---------------------------------------------------------------------------

try:
    import tomllib
except ModuleNotFoundError:
    sys.stderr.write(
        "validate_tracker.py requires Python 3.11+ (for tomllib). "
        "If you are on 3.10 or earlier, run `pip install tomli` and replace "
        "`import tomllib` with `import tomli as tomllib`.\n"
    )
    sys.exit(2)


# ---------------------------------------------------------------------------
# Schema loading
# ---------------------------------------------------------------------------


def load_schemas(schemas_dir: Path) -> dict:
    """Return a dict with the bits of the schemas this script cares about."""
    bill_path = schemas_dir / "bill.toml"
    tracker_path = schemas_dir / "tracker.toml"

    if not bill_path.exists():
        raise FileNotFoundError(f"missing {bill_path}")
    if not tracker_path.exists():
        raise FileNotFoundError(f"missing {tracker_path}")

    with bill_path.open("rb") as f:
        bill = tomllib.load(f)
    with tracker_path.open("rb") as f:
        tracker = tomllib.load(f)

    # Tracker columns: ordered list of {name, type, required}.
    tracker_columns = tracker.get("columns", [])

    # Bill enums and findings vocabulary.
    bill_fields = bill.get("fields", {})
    findings_vocab = (
        bill_fields.get("findings", {}).get("controlled_vocabulary", [])
    )
    next_action_enum = bill_fields.get("next_action", {}).get("enum", [])
    status_enum = bill_fields.get("status", {}).get("enum", [])
    provider_type_enum = bill_fields.get("provider_type", {}).get("enum", [])
    in_network_enum = bill_fields.get("in_network_status", {}).get("enum", [])

    return {
        "tracker_columns": tracker_columns,
        "findings_vocab": set(findings_vocab),
        "next_action_enum": set(next_action_enum),
        "status_enum": set(status_enum),
        "provider_type_enum": set(provider_type_enum),
        "in_network_enum": set(in_network_enum),
    }


# ---------------------------------------------------------------------------
# Cell-level validators
# ---------------------------------------------------------------------------


DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DECIMAL_RE = re.compile(r"^-?\d+(\.\d+)?$")


def validate_date(value: str) -> str | None:
    if value == "":
        return None  # caller decides whether empty is acceptable
    if not DATE_RE.match(value):
        return f"not ISO 8601 YYYY-MM-DD: {value!r}"
    return None


def validate_decimal(value: str) -> str | None:
    if value == "":
        return None
    if not DECIMAL_RE.match(value):
        return f"not a decimal: {value!r}"
    return None


def validate_boolean(value: str) -> str | None:
    if value in ("", "true", "false"):
        return None
    return f"not a boolean ('true', 'false', or empty): {value!r}"


def validate_findings(value: str, vocab: set[str]) -> str | None:
    if value == "":
        return None
    tokens = [t.strip() for t in value.split(";") if t.strip()]
    bad = [t for t in tokens if t not in vocab]
    if bad:
        return f"findings tokens not in controlled vocabulary: {bad}"
    return None


# ---------------------------------------------------------------------------
# Per-row validation
# ---------------------------------------------------------------------------


def validate_row(
    row: dict,
    columns: list[dict],
    schemas: dict,
    row_number: int,
) -> Iterable[str]:
    """Yield error strings for this row."""
    for col in columns:
        name = col["name"]
        col_type = col.get("type", "string")
        required = col.get("required", False)
        value = (row.get(name) or "").strip()

        if required and value == "":
            yield f"row {row_number}: required column {name!r} is empty"
            continue

        if value == "":
            continue

        if col_type == "date":
            problem = validate_date(value)
            if problem:
                yield f"row {row_number}: column {name!r}: {problem}"
        elif col_type == "decimal":
            problem = validate_decimal(value)
            if problem:
                yield f"row {row_number}: column {name!r}: {problem}"
        elif col_type == "boolean":
            problem = validate_boolean(value)
            if problem:
                yield f"row {row_number}: column {name!r}: {problem}"

        # Enum checks tied to specific column names
        if name == "findings":
            problem = validate_findings(value, schemas["findings_vocab"])
            if problem:
                yield f"row {row_number}: column 'findings': {problem}"
        elif name == "next_action" and value not in schemas["next_action_enum"]:
            yield (
                f"row {row_number}: column 'next_action': value {value!r} "
                f"not in enum"
            )
        elif name == "status" and value not in schemas["status_enum"]:
            yield (
                f"row {row_number}: column 'status': value {value!r} "
                f"not in enum"
            )
        elif name == "provider_type" and value not in schemas["provider_type_enum"]:
            yield (
                f"row {row_number}: column 'provider_type': value {value!r} "
                f"not in enum"
            )
        elif name == "in_network_status" and value not in schemas["in_network_enum"]:
            yield (
                f"row {row_number}: column 'in_network_status': value {value!r} "
                f"not in enum"
            )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("csv_path", help="Path to tracker CSV to validate")
    parser.add_argument(
        "--schemas-dir",
        default=None,
        help="Path to schemas directory (defaults to ../schemas relative to this script)",
    )
    args = parser.parse_args()

    csv_path = Path(args.csv_path).resolve()
    if not csv_path.exists():
        sys.stderr.write(f"file not found: {csv_path}\n")
        return 2

    if args.schemas_dir:
        schemas_dir = Path(args.schemas_dir).resolve()
    else:
        schemas_dir = Path(__file__).resolve().parent.parent / "schemas"

    try:
        schemas = load_schemas(schemas_dir)
    except FileNotFoundError as e:
        sys.stderr.write(f"{e}\n")
        return 2

    columns = schemas["tracker_columns"]
    expected_header = [c["name"] for c in columns]

    errors: list[str] = []

    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            sys.stderr.write("empty CSV\n")
            return 1

        if header != expected_header:
            sys.stderr.write("CSV header does not match tracker.toml column order.\n")
            sys.stderr.write(f"expected: {expected_header}\n")
            sys.stderr.write(f"got:      {header}\n")
            return 1

        dict_reader = csv.DictReader(
            csv_path.open("r", encoding="utf-8", newline=""),
        )
        for i, row in enumerate(dict_reader, start=2):  # row 1 is the header
            errors.extend(validate_row(row, columns, schemas, i))

    if errors:
        for err in errors:
            sys.stderr.write(err + "\n")
        sys.stderr.write(f"\n{len(errors)} validation error(s).\n")
        return 1

    print(f"OK: {csv_path.name} validates against {schemas_dir.name}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
