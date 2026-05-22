"""Shared kit_config.toml loader for the local-ops pipeline scripts.

The kit's workstation-local overrides (which biller slugs are
correspondence-only, which slugs route to a known dispute template,
which slugs add an extra state pack) load from a single TOML file
outside the kit's source tree. The default location is
`<HEALTHBILLS_ROOT>/kit_config.toml`; override via the
`MEDBILL_KIT_CONFIG_FILE` env var.

Behavior:
- Missing file returns an empty dict (the kit ships with safe empty
  defaults so the pipeline works without configuration).
- Parse errors emit a single warning to stderr and return an empty
  dict, so misconfiguration is visible without crashing the pipeline.
- All exported lookup helpers (`str_list`, `str_str_dict`) are
  defensive: they accept any TOML value and return a sanitized
  Python collection of the expected shape, ignoring entries that
  don't match. This protects the consumers from downstream type
  errors when the operator hand-edits the config.
"""
from __future__ import annotations

import os
import sys
import tomllib
from pathlib import Path

__all__ = ["load_kit_config", "str_list", "str_str_dict"]


def load_kit_config(health_root: Path) -> dict:
    """Load kit_config.toml; return empty dict on missing or unreadable."""
    config_path = Path(
        os.environ.get("MEDBILL_KIT_CONFIG_FILE")
        or (health_root / "kit_config.toml")
    )
    if not config_path.exists():
        return {}
    try:
        with config_path.open("rb") as fh:
            return tomllib.load(fh)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        print(
            f"[warn] could not parse kit config at {config_path}: {exc}",
            file=sys.stderr,
            flush=True,
        )
        return {}


def str_list(raw) -> list[str]:
    """Coerce a TOML value to a list of strings, dropping non-strings."""
    if not isinstance(raw, list):
        return []
    return [x for x in raw if isinstance(x, str)]


def str_str_dict(raw) -> dict[str, str]:
    """Coerce a TOML table to {str: str}, dropping mismatched entries."""
    if not isinstance(raw, dict):
        return {}
    return {
        k: v
        for k, v in raw.items()
        if isinstance(k, str) and isinstance(v, str)
    }
