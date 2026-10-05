"""Tests that the Ollama-routed scripts tolerate a leading <think> block and build a local client, with no model call."""

import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = REPO_ROOT / "scripts"
THINK = "<think>\nweighing the candidates {not json}\n</think>\n"


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class FakeClient:
    def __init__(self, content: str):
        self.content = content
        self.kwargs = None
        self.chat = SimpleNamespace(completions=SimpleNamespace(create=self._create))

    def _create(self, **kwargs):
        self.kwargs = kwargs
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=self.content))])


def test_index_parse_survives_a_leading_think_block():
    mod = load("index_bills_and_claims")
    client = FakeClient(THINK + '```json\n{"ok": 1}\n```')
    assert mod.call_vision_text(client, "qwen3:8b", "sys", "body") == {"ok": 1}
    assert client.kwargs["extra_body"] == {"think": False}


def test_match_parse_survives_a_leading_think_block(monkeypatch):
    mod = load("match_claims_to_bills")
    client = FakeClient(THINK + '{"match": "UNKNOWN"}')
    monkeypatch.setattr(mod, "vision_client", lambda: (client, "qwen3:8b"))
    assert mod.llm_match({"file": "a"}, [{"file": "b"}]) == {"match": "UNKNOWN"}


def test_clients_point_at_local_ollama_and_honor_ollama_host(monkeypatch):
    monkeypatch.setenv("OLLAMA_HOST", "gpu-box:11434")
    monkeypatch.delenv("MEDBILL_TEXT_MODEL", raising=False)
    client, model = load("index_bills_and_claims").make_client()
    assert str(client.base_url).startswith("http://gpu-box:11434/v1") and model == "qwen3:8b"
    monkeypatch.delenv("OLLAMA_HOST")
    client, _ = load("classify_rename_medical_bills").make_client()
    assert str(client.base_url).startswith("http://localhost:11434/v1")
