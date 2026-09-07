"""Regression checks for DOI portal section boundaries and state coverage."""
from __future__ import annotations

import importlib.util
import re
import socket
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture
def drafter(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """Import against an isolated test root without touching personal settings."""
    monkeypatch.setenv("HEALTHBILLS_ROOT", str(tmp_path))
    monkeypatch.setenv("HEALTHBILLS_LOG_DIR", str(tmp_path / "logs"))
    monkeypatch.setenv("MEDBILL_KIT_CONFIG_FILE", str(tmp_path / "missing-config.toml"))
    monkeypatch.setenv("MEDBILL_KIT_ENV_FILE", str(tmp_path / "missing-credentials.txt"))

    def no_network(*args, **kwargs):
        raise AssertionError("DOI lookup must not access the network")

    monkeypatch.setattr(socket.socket, "connect", no_network)
    spec = importlib.util.spec_from_file_location(
        "doi_test_drafter", ROOT / "scripts" / "draft_letters_by_state.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_tennessee_and_lowercase(drafter) -> None:
    block = drafter.doi_portal_extract("TN")
    assert block.startswith("## TN,")
    assert "DOI:" in block and "AG:" in block
    assert drafter.doi_portal_extract("tn") == block
    assert "\n## " not in block


@pytest.mark.parametrize("code", ["ZZ", ""])
def test_unknown_or_empty_state(drafter, code: str) -> None:
    assert drafter.doi_portal_extract(code) == ""


def test_every_shipped_state_has_one_complete_section(drafter) -> None:
    body = (ROOT / "references" / "doi_portals.md").read_text(encoding="utf-8")
    codes = re.findall(r"^## ([A-Z]{2}), ", body, flags=re.MULTILINE)
    assert len(codes) == 36
    assert len(set(codes)) == len(codes)
    for code in codes:
        block = drafter.doi_portal_extract(code)
        assert block.startswith(f"## {code}, "), code
        assert "DOI:" in block and "AG:" in block, code
        assert "\n## " not in block, code
