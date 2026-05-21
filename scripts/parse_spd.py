"""parse_spd.py — extract the structured profile from a Summary Plan
Description PDF using Azure OpenAI gpt-5.2.

The SPD is the federally-required plain-language summary of an ERISA
health plan (ERISA § 102 / 29 U.S.C. § 1022). The dispute drafter
reads the parsed profile to render plan-aware ERISA appeal letters,
subrogation responses, and IDR-initiation requests. See
`references/spd_parsing_guide.md` for the field descriptions.

The script takes a PDF, renders each page to a JPEG, and asks gpt-5.2
to extract the structured fields. Output is a single JSON file at
`<HEALTHBILLS_ROOT>/_spd_profiles/<plan_slug>.json`.

PDFs vary in length; the script caps at the first 60 pages of an SPD
which covers the introductory plan information, schedule of benefits,
claims procedure, subrogation, and ERISA rights for almost every plan
in current use. Pass `--max-pages` to override.

Usage:
    python parse_spd.py --pdf path/to/spd.pdf --plan-slug acme_ppo_2026
    python parse_spd.py --pdf path/to/spd.pdf --plan-slug acme_ppo_2026 --max-pages 80
"""

from __future__ import annotations

import argparse
import base64
import io
import json
import os
import re
import sys
from pathlib import Path

HEALTH_ROOT = Path(
    os.environ.get("HEALTHBILLS_ROOT")
    or (Path.home() / "Health_Bills")
)
SPD_OUT_DIR = HEALTH_ROOT / "_spd_profiles"

ENV_FILE = Path(
    os.environ.get("MEDBILL_KIT_ENV_FILE")
    or (Path.home() / ".medbill-dispute-kit" / ".env")
)

SLUG_SAFE = re.compile(r"[^a-z0-9_]+")


def safe_slug(s: str) -> str:
    return SLUG_SAFE.sub("_", s.lower().strip()).strip("_") or "spd"


def load_env(env_path: Path) -> None:
    if not env_path.exists():
        sys.exit(f"[fatal] env file not found at {env_path}")
    for ln in env_path.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#") or "=" not in ln:
            continue
        k, _, v = ln.partition("=")
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


def render_pdf_pages(pdf_path: Path, max_pages: int) -> list[bytes]:
    """Render PDF pages to JPEG bytes via PyMuPDF (fitz). Cap at
    max_pages so the prompt stays affordable. ~150 dpi is enough for
    text extraction without bloating the request."""
    try:
        import fitz  # PyMuPDF
    except ImportError:
        sys.exit(
            "[fatal] PyMuPDF (fitz) is required. "
            "Install with: pip install PyMuPDF"
        )
    images: list[bytes] = []
    with fitz.open(pdf_path) as doc:
        n_pages = min(len(doc), max_pages)
        for i in range(n_pages):
            page = doc.load_page(i)
            pix = page.get_pixmap(dpi=150)
            images.append(pix.tobytes("jpeg"))
    return images


SYSTEM_PROMPT = """You are a senior ERISA benefits analyst extracting a
structured profile from a Summary Plan Description (SPD). Read every
page provided. Return a single JSON object with the keys below.
Use null for any field you cannot determine from the text. Do not
guess; null is the correct answer when the SPD does not state the
value. Use US dollars as plain numbers (no $ sign, no commas).

Required keys:
{
  "plan_name": "string or null",
  "plan_sponsor": "string or null",
  "plan_administrator": "string or null",
  "funding": "self_funded | fully_insured | governmental | church | unknown",
  "tpa": "string or null (third-party administrator if self-funded)",
  "insurer": "string or null (issuer if fully insured)",
  "in_network_deductible_individual": "number or null",
  "in_network_deductible_family": "number or null",
  "in_network_oop_max_individual": "number or null",
  "in_network_oop_max_family": "number or null",
  "out_network_oop_max_individual": "number or null",
  "out_network_oop_max_family": "number or null",
  "claim_filing_deadline_days": "number or null (from DOS)",
  "internal_appeal_deadline_days": "number or null (from adverse determination)",
  "internal_appeal_levels": "number or null",
  "external_review_available": "true | false | null",
  "subrogation_clause_present": "true | false | null",
  "reimbursement_clause_present": "true | false | null",
  "made_whole_disclaimed": "true | false | null",
  "common_fund_disclaimed": "true | false | null",
  "discretionary_authority_clause": "true | false | null",
  "nsa_ancillary_implementation": "true | false | null",
  "prior_authorization_required_categories": ["array of strings or empty"],
  "medical_necessity_definition_quoted": "string or null (verbatim quote, max 500 chars)",
  "subrogation_clause_quoted": "string or null (verbatim quote, max 1500 chars)",
  "appeal_procedure_quoted": "string or null (verbatim quote, max 1500 chars)",
  "extracted_at": "YYYY-MM-DD (today)"
}

Output the JSON object only, no preamble or commentary, no fenced
code block."""


def call_extractor(images: list[bytes]) -> dict:
    from openai import OpenAI
    client = OpenAI(
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        base_url=os.environ["AZURE_OPENAI_ENDPOINT"].rstrip("/")
        + "/openai/v1/",
    )
    deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    user_content: list[dict] = [
        {"type": "text",
         "text": "Extract the SPD profile from the pages below."},
    ]
    for img in images:
        b64 = base64.b64encode(img).decode("ascii")
        user_content.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{b64}"},
        })
    resp = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_content},
        ],
        response_format={"type": "json_object"},
        max_completion_tokens=4096,
    )
    text = (resp.choices[0].message.content or "").strip()
    return json.loads(text)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pdf", required=True,
                    help="Path to the SPD PDF.")
    ap.add_argument("--plan-slug", required=True,
                    help="Short slug used in the output filename.")
    ap.add_argument("--max-pages", type=int, default=60,
                    help="Render only the first N pages (default 60).")
    args = ap.parse_args()

    pdf_path = Path(args.pdf).expanduser().resolve()
    if not pdf_path.exists():
        sys.exit(f"[fatal] SPD not found at {pdf_path}")

    load_env(ENV_FILE)
    print(f"[render] {pdf_path} (first {args.max_pages} pages)",
          flush=True)
    images = render_pdf_pages(pdf_path, args.max_pages)
    print(f"[extract] sending {len(images)} pages to Azure",
          flush=True)

    profile = call_extractor(images)
    SPD_OUT_DIR.mkdir(parents=True, exist_ok=True)
    slug = safe_slug(args.plan_slug)
    out_path = SPD_OUT_DIR / f"{slug}.json"
    out_path.write_text(
        json.dumps(profile, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    print(f"[done] -> {out_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
