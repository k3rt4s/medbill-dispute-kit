#!/usr/bin/env python3
"""Classify a biller's written reply against letter_dispute_reply blocks.

This module is intentionally offline and deterministic. It reads only the
bundled TOML pattern schema and returns literal text from the supplied reply
as evidence; it does not infer a prior balance, date, or dispute context.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import tomllib
from typing import Any


DEFAULT_RULES_PATH = Path(__file__).resolve().parents[1] / "schemas" / "reply_patterns.toml"


def _load_rules(rules_path: Path) -> dict[str, Any]:
    """Load and minimally validate the bundled reply-pattern configuration."""
    with rules_path.open("rb") as handle:
        rules = tomllib.load(handle)

    meta = rules.get("meta")
    patterns = rules.get("patterns")
    if not isinstance(meta, dict) or not isinstance(patterns, list):
        raise ValueError("reply pattern schema requires meta and patterns")
    if not 0.0 <= float(meta["selection_threshold"]) <= 1.0:
        raise ValueError("selection_threshold must be within [0.0, 1.0]")
    if not 0.0 <= float(meta["ambiguity_margin"]) <= 1.0:
        raise ValueError("ambiguity_margin must be within [0.0, 1.0]")
    return rules


def _literal_matches(reply_text: str, phrases: list[str]) -> list[str]:
    """Return each configured phrase as it appears in reply_text, once."""
    matches: list[str] = []
    for phrase in phrases:
        match = re.search(re.escape(phrase), reply_text, flags=re.IGNORECASE)
        if match:
            matches.append(match.group(0))
    return matches


def classify_dispute_reply(
    reply_text: str, rules_path: Path | None = None,
) -> dict[str, object]:
    """Return scored block candidates and literal evidence for a written reply.

    A reply stays ambiguous if no pattern clears the explicit selection
    threshold or if the two highest scores fall within the configured margin.
    Tied or multiple selected blocks are preserved instead of being guessed
    away. Empty text produces no blocks and remains ambiguous.
    """
    if not isinstance(reply_text, str):
        raise TypeError("reply_text must be a string")

    rules = _load_rules(rules_path or DEFAULT_RULES_PATH)
    meta = rules["meta"]
    threshold = float(meta["selection_threshold"])
    margin = float(meta["ambiguity_margin"])
    score_cap = float(meta["score_cap"])
    penalty = float(meta["negative_phrase_penalty"])

    scores: dict[str, float] = {}
    evidence: dict[str, list[str]] = {}
    for pattern in rules["patterns"]:
        block = str(pattern["block"])
        positive = _literal_matches(reply_text, list(pattern["signals"]))
        negative = _literal_matches(reply_text, list(pattern["negative_signals"]))
        raw_score = len(positive) / len(pattern["signals"])
        score = min(score_cap, max(0.0, raw_score - len(negative) * penalty))
        scores[block] = round(score, 4)
        evidence[block] = positive

    ranked_scores = sorted(scores.values(), reverse=True)
    top_score = ranked_scores[0] if ranked_scores else 0.0
    near_tie = (
        len(ranked_scores) > 1
        and abs(ranked_scores[0] - ranked_scores[1]) <= margin
    )
    ambiguous = top_score < threshold or near_tie
    blocks = [block for block, score in scores.items() if score >= threshold]

    if not reply_text.strip():
        note = "No reply text was supplied; no block can be selected."
    elif ambiguous:
        note = "Confirm the reply with the patient before selecting a letter block."
    elif len(blocks) > 1:
        note = "Multiple reply patterns met the selection threshold."
    else:
        note = "A single reply pattern met the selection threshold."

    return {
        "blocks": blocks,
        "scores": scores,
        "evidence": evidence,
        "ambiguous": ambiguous,
        "notes": note,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reply_text", help="Written reply text to classify")
    parser.add_argument("--rules", type=Path, help="Optional reply-pattern TOML path")
    args = parser.parse_args()
    print(json.dumps(classify_dispute_reply(args.reply_text, args.rules), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
