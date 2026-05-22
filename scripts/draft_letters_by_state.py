"""draft_letters_by_state.py — state-machine letter generator.

For each (biller_slug, account_number) dispute group in tracker.csv,
draft the single most-appropriate letter based on the gate state:

  - has_eob == "N" AND eob_request_sent_date is empty
      -> draft letter_request_eob.md (to the insurer, cc the biller)
      -> ALSO draft email_biller_eob_requested.md (courtesy email,
         only if a biller email is detectable in the bill text)

  - has_itemization == "N" AND itemization_request_sent_date is empty
      -> draft letter_itemization_request.md (to the biller)

  - has_eob == "Y" AND has_itemization == "Y"
      AND dispute_letter_sent_date is empty
      -> draft the appropriate dispute template:
           collection_notice keywords -> letter_fdcpa_validation.md
           emergency / NSA keywords   -> letter_no_surprises_violation.md
           dental denial / appeal     -> letter_dental_dispute.md
                                          + letter_insurance_appeal_erisa.md
           else                       -> letter_initial_dispute.md

Within a dispute group (same biller + same account_number), only the
latest-statement-date bill is the canonical row. The others are marked
"superseded" in the output and no letter is drafted for them.

Output letters live in:
  Billers/<biller_slug>/<bill_id>_<letter_kind>.md

The script writes the per-letter path back into tracker.csv columns:
`drafted_eob_request`, `drafted_itemization_request`,
`drafted_dispute_letter`. Manual sent-date entry is on you; this
script only DRAFTS.

Azure OpenAI gpt-5.2 is only called when actually drafting a letter
(template + bill + EOB + law context -> ready-to-mail Markdown).
Skipped folders / already-drafted letters never trigger a call.

Usage:
   python draft_letters_by_state.py
   python draft_letters_by_state.py --force  # overwrite existing drafts
   python draft_letters_by_state.py --dry-run
"""

from __future__ import annotations

import argparse
import csv
import datetime
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kit_config import load_kit_config, str_str_dict  # noqa: E402

HEALTH_ROOT = Path(
    os.environ.get("HEALTHBILLS_ROOT")
    or (Path.home() / "Health_Bills")
)
BILLERS_DIR = HEALTH_ROOT / "Billers"
EOB_DIR = HEALTH_ROOT / "EOB"
MEDICAL_HISTORY = HEALTH_ROOT / "MEDICAL_HISTORY.md"

# Kit templates + references resolve relative to this script file so the
# scripts/ folder stays portable.
KIT_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = KIT_ROOT / "templates"
REFERENCES_DIR = KIT_ROOT / "references"

LOG_DIR = Path(
    os.environ.get("HEALTHBILLS_LOG_DIR")
    or (Path.home() / ".medbill-dispute-kit" / "tracker")
)
TRACKER_CSV = LOG_DIR / "tracker.csv"

ENV_FILE = Path(
    os.environ.get("MEDBILL_KIT_ENV_FILE")
    or (Path.home() / ".medbill-dispute-kit" / ".env")
)

SIDECAR_SUFFIX = ".extracted.txt"

# tracker.csv columns we read and (some of which we write back)
TRACKER_COLUMNS = [
    "bill_id", "encounter_id",
    "biller_slug", "biller_name", "doc_type", "account_number",
    "file", "statement_date", "dos_start", "dos_end",
    "total_billed", "current_balance",
    "has_eob", "matched_claim_numbers", "has_itemization",
    "itemization_signals", "benchmarks_available",
    "findings",
    "status", "next_action", "next_action_due",
    "eob_request_sent_date", "eob_request_tracking",
    "itemization_request_sent_date", "itemization_request_tracking",
    "dispute_letter_sent_date", "dispute_letter_tracking",
    "thirty_day_warning_sent_date", "thirty_day_warning_tracking",
    "counter_offer_amount",
    "counter_offer_sent_date", "counter_offer_tracking",
    "doi_complaint_sent_date", "doi_complaint_tracking",
    "doi_complaint_number",
    "small_claims_filed_date", "small_claims_case_number",
    "small_claims_court",
    "drafted_eob_request", "drafted_itemization_request",
    "drafted_dispute_letter", "dispute_template_used",
    "drafted_counter_offer", "drafted_doi_complaint",
    "drafted_small_claims_civil_warrant",
    "drafted_hipaa_records_request",
    "response_due_date", "notes",
]

BENCHMARKS_FILENAME = "_benchmarks.csv"
COUNTER_OFFER_MULTIPLIER = 2.0  # 200% of Medicare allowable, see template


_KIT_CONFIG = load_kit_config(HEALTH_ROOT)

# Per-folder dispute-template overrides for known cases. Populated
# from kit_config.toml [folder_template_overrides] table on the
# workstation. Empty in the public kit; the content-based picker
# below will pick a template from the bill/EOB text when no override
# applies. Example workstation config:
#
#   [folder_template_overrides]
#   my_er_ancillary_radiology_slug = "no_surprises"  # ER ancillary, NSA
#   my_dental_insurer_slug         = "dental_dispute"  # dental denial in flight
#   my_lab_collector_slug          = "fdcpa"  # collection notices
FOLDER_TEMPLATE_OVERRIDES: dict[str, str] = str_str_dict(
    _KIT_CONFIG.get("folder_template_overrides")
)

# Patterns that pick the dispute template if no override applies
DISPUTE_TEMPLATE_PICKER: list[tuple[re.Pattern, str]] = [
    (re.compile(
        r"collection\s+notice|third[\s-]?party\s+collection|"
        r"sent\s+to\s+collections?|"
        r"referred?\s+to\s+(an?\s+)?outside\s+collection",
        re.I,
    ), "fdcpa"),
    (re.compile(
        r"(dental\s+(denial|appeal|grievance|adverse))|"
        r"(humana\s+dental.*upheld)",
        re.I,
    ), "dental_dispute"),
    (re.compile(
        r"emergency\s+room\s+(visit|services|admission)|"
        r"emergency\s+department\s+(visit|services|admission)|"
        r"place\s+of\s+service\s*:?\s*(emergency|ER\b)|"
        r"surprise\s+bill|no\s+surprises\s+act",
        re.I,
    ), "no_surprises"),
    (re.compile(
        r"claim\s+denied|denial\s+of\s+(coverage|claim|benefits)|"
        r"appeal\s+(decision|determination|upheld)|"
        r"adverse\s+benefit\s+determination",
        re.I,
    ), "erisa_appeal"),
]

TEMPLATE_PATHS = {
    "itemization": TEMPLATES_DIR / "letter_itemization_request.md",
    "initial_dispute": TEMPLATES_DIR / "letter_initial_dispute.md",
    "no_surprises": TEMPLATES_DIR / "letter_no_surprises_violation.md",
    "fdcpa": TEMPLATES_DIR / "letter_fdcpa_validation.md",
    "erisa_appeal": TEMPLATES_DIR / "letter_insurance_appeal_erisa.md",
    "dental_dispute": TEMPLATES_DIR / "letter_dental_dispute.md",
    "request_eob": TEMPLATES_DIR / "letter_request_eob.md",
    "email_biller_eob_requested":
        TEMPLATES_DIR / "email_biller_eob_requested.md",
    "counter_offer":
        TEMPLATES_DIR / "letter_negotiation_counter_offer.md",
    "doi_complaint": TEMPLATES_DIR / "complaint_state_doi.md",
    "small_claims_civil_warrant":
        TEMPLATES_DIR / "small_claims_civil_warrant.md",
    "records_request_hipaa":
        TEMPLATES_DIR / "letter_records_request_hipaa.md",
    "good_faith_estimate_request":
        TEMPLATES_DIR / "letter_good_faith_estimate_request.md",
    "ppdr_initiate": TEMPLATES_DIR / "letter_ppdr_initiate.md",
    "challenge_hospital_lien":
        TEMPLATES_DIR / "letter_challenge_hospital_lien.md",
    "subrogation_response":
        TEMPLATES_DIR / "letter_subrogation_response.md",
    "credit_report_dispute_fcra":
        TEMPLATES_DIR / "letter_credit_report_dispute_fcra.md",
    "request_insurer_initiate_idr":
        TEMPLATES_DIR / "letter_request_insurer_initiate_idr.md",
    "auto_med_pay": TEMPLATES_DIR / "letter_auto_med_pay.md",
    "wc_carrier_redirect":
        TEMPLATES_DIR / "letter_wc_carrier_redirect.md",
    "dispute_reply": TEMPLATES_DIR / "letter_dispute_reply.md",
    "erisa_502c_penalty":
        TEMPLATES_DIR / "letter_erisa_502c_penalty.md",
    "encounter_combined":
        TEMPLATES_DIR / "encounter_combined_dispute.md",
}

# Sidecar keyword detectors for accident- and work-related care. The
# drafter inspects the canonical bill's sidecar text once per group
# and routes to the matching redirect template in parallel with the
# regular dispute flow.
WC_INJURY_RE = re.compile(
    r"\b(workers?[\s']?\s*comp(?:ensation)?|work[-\s]?related\s+injury|"
    r"on[-\s]?the[-\s]?job|occupational\s+injury|first\s+report\s+of\s+injury|"
    r"WC\s+claim|workplace\s+injury|injured\s+at\s+work)\b",
    re.I,
)
AUTO_INJURY_RE = re.compile(
    r"\b(motor[-\s]?vehicle\s+(?:accident|collision)|MVA\b|"
    r"auto(?:mobile)?\s+(?:accident|collision)|car\s+(?:accident|crash)|"
    r"PIP\s+(?:claim|coverage)|med[-\s]?pay\s+(?:claim|coverage)|"
    r"third[-\s]?party\s+(?:auto|liability)\s+(?:insurer|carrier))\b",
    re.I,
)

# Form-label checkbox blocks on provider billing forms commonly read
# "Please indicate if applicable: AUTO ACCIDENT / WORKER'S COMPENSATION
# / Date of Injury". These are field labels, not narrative statements
# that the patient was actually in an MVA or sustained a workplace
# injury. The detector must strip these blocks before counting keyword
# hits to avoid mis-routing every bill with a UB-04-style form layout
# to WC / auto-medpay redirect.
#
# `_FORM_HEADER_RE` matches the "please indicate if applicable" header
# at any position within a line (OCR sometimes prefixes line numbers).
# `_FORM_LABEL_TOKENS_RE` is the keyword confirmation that gates
# stripping — without one of these tokens appearing in the next 10
# lines after the header, the header is left alone (so a narrative
# sentence containing "please indicate if applicable" does not
# accidentally suppress later legitimate WC / auto content).
_FORM_HEADER_RE = re.compile(
    r"please\s+indicate\s+if\s+applicable", re.I,
)
_FORM_LABEL_TOKENS_RE = re.compile(
    r"\b(auto\s+accident|worker'?s?\s+comp|date\s+of\s+injury)\b",
    re.I,
)
_FORM_BLOCK_MAX_LINES = 10

DOI_PORTALS = REFERENCES_DIR / "doi_portals.md"


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


_client = None
_deployment = None


def vision_client():
    global _client, _deployment
    if _client is not None:
        return _client, _deployment
    load_env(ENV_FILE)
    from openai import OpenAI
    _client = OpenAI(
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        base_url=os.environ["AZURE_OPENAI_ENDPOINT"].rstrip("/") + "/openai/v1/",
    )
    _deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    return _client, _deployment


def read_sidecar_body(sidecar: Path) -> str:
    try:
        text = sidecar.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        if ln.strip() == "# ---":
            return "\n".join(lines[i+1:])
    return text


def read_tracker() -> list[dict]:
    if not TRACKER_CSV.exists():
        return []
    with TRACKER_CSV.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write_tracker(rows: list[dict]) -> None:
    TRACKER_CSV.parent.mkdir(parents=True, exist_ok=True)
    with TRACKER_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=TRACKER_COLUMNS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in TRACKER_COLUMNS})


def dispute_key(row: dict) -> tuple[str, str]:
    """Group rows that represent the same underlying dispute."""
    slug = row.get("biller_slug", "")
    acct = (row.get("account_number") or "").strip()
    if acct:
        return (slug, f"acct:{acct}")
    dos = (row.get("dos_start") or "").strip()
    if dos:
        return (slug, f"dos:{dos}")
    return (slug, f"file:{row.get('file', '')}")


_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def pick_canonical(rows: list[dict]) -> dict:
    """Pick the canonical bill row within a dispute group: prefer the
    latest valid ISO statement_date, then fall back to dos_start,
    then to file name for deterministic tie-breaking. Rows whose
    statement_date is missing or malformed sort last (treated as
    `0000-00-00` so they don't randomly outrank a real date)."""
    def sort_key(r: dict) -> tuple[str, str, str]:
        stmt = (r.get("statement_date") or "").strip()
        stmt_norm = stmt if _DATE_RE.match(stmt) else "0000-00-00"
        dos = (r.get("dos_start") or "").strip()
        dos_norm = dos if _DATE_RE.match(dos) else "0000-00-00"
        return (stmt_norm, dos_norm, r.get("file", ""))
    return sorted(rows, key=sort_key, reverse=True)[0]


def _strip_form_label_blocks(body: str) -> str:
    """Remove "please indicate if applicable:" form-label checkbox
    blocks from sidecar text. Iterates line by line, looking for the
    header phrase; when found, scans the next `_FORM_BLOCK_MAX_LINES`
    for canonical form-label tokens (AUTO ACCIDENT / WORKER'S COMP /
    DATE OF INJURY). If at least one matches, drops the header line
    and every line through the LAST token line within the window —
    preserving anything after that boundary. Narrative text mentioning
    "please indicate if applicable" without nearby form tokens is left
    untouched, and the strip never over-runs into adjacent content."""
    lines = body.split("\n")
    keep: list[str] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if _FORM_HEADER_RE.search(line):
            window_end = min(i + 1 + _FORM_BLOCK_MAX_LINES, n)
            last_token = -1
            for j in range(i + 1, window_end):
                if _FORM_LABEL_TOKENS_RE.search(lines[j]):
                    last_token = j
            if last_token >= 0:
                i = last_token + 1
                continue
        keep.append(line)
        i += 1
    return "\n".join(keep)


def detect_injury_routing(canonical: dict) -> str:
    """Inspect the canonical bill's sidecar text for accident or
    work-injury markers. Returns 'wc' if work-related markers dominate,
    'auto' if motor-vehicle markers dominate, or '' if neither is
    present. WC takes priority when both match because the WC carrier
    is the statutorily-required first payer on a work-related auto
    incident (e.g., a delivery driver in an MVA on the job)."""
    slug = canonical.get("biller_slug", "")
    file = canonical.get("file", "")
    sidecar = BILLERS_DIR / slug / (file + SIDECAR_SUFFIX)
    if not sidecar.exists():
        return ""
    body = read_sidecar_body(sidecar)
    if not body:
        return ""
    # Strip "please indicate if applicable:" form-label blocks so the
    # AUTO ACCIDENT / WORKER'S COMPENSATION checkbox labels on the bill
    # template don't trigger the detector. Without this, every UB-04
    # / CMS-1500 / Imagine-Pay style bill that prints those labels (Y/N
    # fields, not positive answers) gets mis-routed to the WC or auto-
    # medpay track. The suppression is line-anchored, keyword-gated
    # (requires AUTO ACCIDENT / WORKER'S COMP / DATE OF INJURY in the
    # next 10 lines), and handles arbitrary OCR line lengths.
    body_for_detection = _strip_form_label_blocks(body)
    wc_hits = len(WC_INJURY_RE.findall(body_for_detection))
    auto_hits = len(AUTO_INJURY_RE.findall(body_for_detection))
    if wc_hits >= 1 and wc_hits >= auto_hits:
        return "wc"
    if auto_hits >= 1:
        return "auto"
    return ""


def gather_encounter_siblings(canonical: dict,
                               all_rows: list[dict]) -> str:
    """Return a short summary of OTHER bills (different biller_slug)
    sharing this bill's encounter_id. Used as extra prompt context so
    the drafter can reference the full encounter when applying NSA
    ancillary-provider protection and other encounter-wide arguments."""
    eid = (canonical.get("encounter_id") or "").strip()
    if not eid:
        return ""
    slug = canonical.get("biller_slug", "")
    sibs = [
        r for r in all_rows
        if r.get("encounter_id") == eid
        and r.get("biller_slug") != slug
    ]
    if not sibs:
        return ""
    lines = [
        f"Encounter {eid} also produced bills from the following "
        f"other providers (consider NSA ancillary protection and "
        f"cross-reference in the letter where applicable):",
        "",
    ]
    for s in sibs:
        lines.append(
            f"- {s.get('biller_slug', '')} "
            f"({s.get('biller_name', '')}): "
            f"DOS {s.get('dos_start', '')} to {s.get('dos_end', '')}, "
            f"billed ${s.get('total_billed', '')}, "
            f"current ${s.get('current_balance', '')}, "
            f"has_eob={s.get('has_eob', '')}, "
            f"has_itemization={s.get('has_itemization', '')}"
        )
    return "\n".join(lines)


def read_benchmarks(slug: str) -> list[dict]:
    """Return the rows of Billers/<slug>/_benchmarks.csv if present."""
    bench = BILLERS_DIR / slug / BENCHMARKS_FILENAME
    if not bench.exists():
        return []
    with bench.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def compute_counter_offer(canonical: dict,
                          benchmark_rows: list[dict]) -> str:
    """Default counter-offer = COUNTER_OFFER_MULTIPLIER * sum(Medicare
    allowables) for codes whose Medicare rate is known. If no codes
    have Medicare data, fall back to 20% of current_balance. The
    drafter writes this into counter_offer_amount; the user can
    override it in tracker.csv before re-running with --force."""
    medicare_sum = 0.0
    n_with_rate = 0
    for row in benchmark_rows:
        try:
            rate = float(row.get("medicare_national") or 0)
        except ValueError:
            continue
        if rate > 0:
            medicare_sum += rate
            n_with_rate += 1
    if n_with_rate > 0:
        return f"{medicare_sum * COUNTER_OFFER_MULTIPLIER:.2f}"
    # Fallback: 20% of current balance
    try:
        bal = float(canonical.get("current_balance") or 0)
    except ValueError:
        bal = 0.0
    if bal > 0:
        return f"{bal * 0.20:.2f}"
    return ""


def filter_overpriced_benchmarks(rows: list[dict],
                                  threshold: float = 1.50) -> list[dict]:
    """Keep only the line items materially over Medicare."""
    out: list[dict] = []
    for r in rows:
        try:
            ratio = float(r.get("ratio_billed_to_medicare") or 0)
        except ValueError:
            continue
        try:
            spread = (float(r.get("billed_amount") or 0)
                      - float(r.get("medicare_national") or 0))
        except ValueError:
            spread = 0.0
        if ratio >= threshold or spread >= 200.0:
            out.append(r)
    return out


def format_benchmark_table(rows: list[dict]) -> str:
    """Render the overpriced rows as a markdown table for the LLM
    prompt. The counter-offer template references this section."""
    if not rows:
        return "(no overpriced line items)"
    lines = [
        "| CPT/HCPCS | Description | Billed | Medicare | Ratio |",
        "|-----------|-------------|-------:|---------:|------:|",
    ]
    for r in rows:
        lines.append(
            f"| {r.get('cpt_code', '')} "
            f"| {r.get('description', '')} "
            f"| ${r.get('billed_amount', '')} "
            f"| ${r.get('medicare_national', '')} "
            f"| {r.get('ratio_billed_to_medicare', '')}x |"
        )
    return "\n".join(lines)


def gather_evidence_text(canonical: dict) -> str:
    """Return concatenated sidecar text from the canonical bill plus
    any related EOB(s) for the same biller_slug. Capped to ~30k chars
    so the prompt stays affordable."""
    parts: list[str] = []
    slug = canonical.get("biller_slug", "")
    file = canonical.get("file", "")
    bill_sc = BILLERS_DIR / slug / (file + SIDECAR_SUFFIX)
    if bill_sc.exists():
        parts.append(f"## BILL (Billers/{slug}/{file})\n"
                     + read_sidecar_body(bill_sc)[:8000])
    eob_dir = EOB_DIR / slug
    if eob_dir.is_dir():
        for sc in sorted(eob_dir.glob(f"*{SIDECAR_SUFFIX}")):
            parts.append(f"\n## EOB (EOB/{slug}/{sc.name[:-len(SIDECAR_SUFFIX)]})\n"
                         + read_sidecar_body(sc)[:6000])
    return "\n".join(parts)[:30_000]


def pick_dispute_template(slug: str, evidence: str) -> str:
    if slug in FOLDER_TEMPLATE_OVERRIDES:
        return FOLDER_TEMPLATE_OVERRIDES[slug]
    for pat, key in DISPUTE_TEMPLATE_PICKER:
        if pat.search(evidence):
            return key
    return "initial_dispute"


def load_template(key: str) -> str:
    path = TEMPLATE_PATHS.get(key)
    if not path or not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


# Map biller slug -> additional US state code whose state-pack should
# also be loaded into the law context when drafting letters for that
# slug. Use this when services were rendered in a different state from
# the patient's residence (e.g., a Tennessee resident treated at a
# Georgia hospital still wants GA state-specific citations in the
# letter). Populated from kit_config.toml [biller_state_overrides]
# table on the workstation. Empty in the public kit.
#
# Example workstation config:
#   [biller_state_overrides]
#   my_out_of_state_hospital_slug = "ga"  # services rendered in Georgia
BILLER_STATE_OVERRIDES: dict[str, str] = str_str_dict(
    _KIT_CONFIG.get("biller_state_overrides")
)

# Patient's home state code (two-letter, lowercase). Used to load the
# kit's state-specific law pack into every letter's context. Override
# via $HEALTHBILLS_PATIENT_STATE env var. Default loads federal only
# — letters will work, just without state citations.
PATIENT_STATE = (os.environ.get("HEALTHBILLS_PATIENT_STATE") or "").lower()


def load_law_for_slug(slug: str) -> str:
    parts: list[str] = []
    fed = REFERENCES_DIR / "laws_federal.md"
    if fed.exists():
        parts.append("## Federal\n" + fed.read_text(encoding="utf-8"))

    state_codes = set()
    if PATIENT_STATE:
        state_codes.add(PATIENT_STATE)
    if slug in BILLER_STATE_OVERRIDES:
        state_codes.add(BILLER_STATE_OVERRIDES[slug])
    for code in sorted(state_codes):
        state_md = REFERENCES_DIR / f"laws_state_{code}.md"
        if state_md.exists():
            parts.append(f"## {code.upper()}\n"
                         + state_md.read_text(encoding="utf-8"))

    return "\n\n".join(parts)[:25_000]


def read_medical_history() -> str:
    if not MEDICAL_HISTORY.exists():
        return ""
    return MEDICAL_HISTORY.read_text(encoding="utf-8")[:8000]


def call_draft(letter_kind: str, template_key: str,
                canonical: dict, evidence: str,
                supporting_law: str, history: str,
                extras: dict | None = None) -> str:
    client, deployment = vision_client()
    template_text = load_template(template_key)
    system = (
        "You are a senior medical-billing advocate drafting a single "
        "formal letter or filing. Use the kit template as structure; "
        "substitute every placeholder with concrete values from the "
        "evidence; cite real federal and state statutes; tone firm, "
        "specific. Output the letter only — no preamble, no fenced "
        "code block, no commentary. Header at top: patient name + "
        "address + phone + email. Then date, then recipient block. "
        "Keep the [CERTIFIED MAIL TRACKING NUMBER] placeholder. State "
        "a 15 or 30 business-day response window where applicable. CC "
        "the relevant state insurance department; for services "
        "rendered in Georgia also cc the GA OCI; cc the federal CMS "
        "No Surprises Help Desk for NSA letters. Close with signature "
        "+ account # + date of service. Do not invent values that "
        "aren't in the evidence."
    )
    extras_block = ""
    if extras:
        for k, v in extras.items():
            if v:
                extras_block += f"\n# {k}\n{v}\n"
    user = (
        f"# Letter kind\n{letter_kind}\n\n"
        f"# Kit template ({template_key})\n{template_text}\n\n"
        f"# Patient identity\n{history}\n\n"
        f"# Law context\n{supporting_law}\n"
        f"{extras_block}\n"
        f"# Bill / EOB evidence\n{evidence}\n"
    )
    resp = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        max_completion_tokens=6144,
    )
    return (resp.choices[0].message.content or "").strip()


def draft_letter_if_needed(canonical: dict, all_rows: list[dict],
                           letter_kind: str, template_key: str,
                           dest: Path, force: bool, dry_run: bool,
                           extras: dict | None = None) -> str | None:
    """Returns the destination path string if a letter was written
    (or would be written in dry-run); empty if skipped."""
    if dest.exists() and not force:
        return str(dest)
    if dry_run:
        print(f"  [would draft] {letter_kind:24s} -> "
              f"{dest.relative_to(HEALTH_ROOT)}", flush=True)
        return str(dest)
    slug = canonical.get("biller_slug", "")
    evidence = gather_evidence_text(canonical)
    if not evidence.strip():
        print(f"  [skip] {letter_kind}: no evidence text available",
              flush=True)
        return None
    print(f"  [draft] {letter_kind:24s} template={template_key} -> "
          f"{dest.relative_to(HEALTH_ROOT)}", flush=True)
    try:
        text = call_draft(
            letter_kind=letter_kind,
            template_key=template_key,
            canonical=canonical,
            evidence=evidence,
            supporting_law=load_law_for_slug(slug),
            history=read_medical_history(),
            extras=extras,
        )
    except Exception as exc:
        print(f"  [error] {exc}", flush=True)
        return None
    if not text:
        print(f"  [error] empty response from model", flush=True)
        return None
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    return str(dest)


def doi_portal_extract(state_code: str) -> str:
    """Pull the relevant state's section out of references/doi_portals.md
    for inclusion in the DOI complaint prompt context."""
    if not state_code or not DOI_PORTALS.exists():
        return ""
    body = DOI_PORTALS.read_text(encoding="utf-8")
    header = f"## {state_code.upper()} —"
    idx = body.find(header)
    if idx < 0:
        return ""
    next_idx = body.find("\n## ", idx + len(header))
    if next_idx < 0:
        next_idx = len(body)
    return body[idx:next_idx].strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--force", action="store_true",
                    help="Overwrite existing letter drafts.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Plan only; no Azure calls, no file writes.")
    args = ap.parse_args()

    tracker_rows = read_tracker()
    if not tracker_rows:
        print(f"[fatal] no tracker.csv yet at {TRACKER_CSV}", flush=True)
        return 1

    # Group by dispute_key
    groups: dict[tuple, list[dict]] = defaultdict(list)
    for row in tracker_rows:
        groups[dispute_key(row)].append(row)

    # Mark all rows: canonical or superseded
    canonical_set: set[str] = set()  # bill_ids
    for key, members in groups.items():
        canonical = pick_canonical(members)
        canonical_set.add(canonical["bill_id"])

    print(f"[main] {len(tracker_rows)} tracker rows -> "
          f"{len(groups)} dispute groups", flush=True)

    written: dict[str, str] = {}  # bill_id -> path of letter drafted

    for key, members in groups.items():
        canonical = pick_canonical(members)
        bill_id = canonical["bill_id"]
        slug = canonical["biller_slug"]
        has_eob = canonical.get("has_eob") == "Y"
        has_item = canonical.get("has_itemization") == "Y"
        has_benchmarks = canonical.get("benchmarks_available") == "Y"
        sent_eob = canonical.get("eob_request_sent_date", "").strip()
        sent_item = canonical.get("itemization_request_sent_date", "").strip()
        sent_dispute = canonical.get("dispute_letter_sent_date", "").strip()
        sent_counter = canonical.get("counter_offer_sent_date", "").strip()
        sent_warning = canonical.get(
            "thirty_day_warning_sent_date", "").strip()
        sent_doi = canonical.get("doi_complaint_sent_date", "").strip()
        filed_small_claims = canonical.get(
            "small_claims_filed_date", "").strip()
        status = canonical.get("status", "")
        next_action = canonical.get("next_action", "")
        bills_folder = BILLERS_DIR / slug

        if status == "closed" or next_action == "monitor":
            continue

        print(f"\n[group {key[0]}/{key[1]}] {bill_id} "
              f"(status={status}, next={next_action})", flush=True)

        # Request-EOB letter
        if not has_eob and not sent_eob:
            dest = bills_folder / f"{bill_id}_LETTER_REQUEST_EOB.md"
            if (already := canonical.get("drafted_eob_request")) and \
                    not args.force and dest.exists():
                pass
            else:
                path = draft_letter_if_needed(
                    canonical=canonical, all_rows=members,
                    letter_kind="REQUEST_EOB",
                    template_key="request_eob",
                    dest=dest, force=args.force, dry_run=args.dry_run,
                )
                if path:
                    written[bill_id + "_eob"] = path
                    canonical["drafted_eob_request"] = str(
                        Path(path).relative_to(HEALTH_ROOT)
                    )

        # Request-itemization letter
        if not has_item and not sent_item:
            dest = bills_folder / f"{bill_id}_LETTER_REQUEST_ITEMIZATION.md"
            if (already := canonical.get("drafted_itemization_request")) and \
                    not args.force and dest.exists():
                pass
            else:
                path = draft_letter_if_needed(
                    canonical=canonical, all_rows=members,
                    letter_kind="REQUEST_ITEMIZATION",
                    template_key="itemization",
                    dest=dest, force=args.force, dry_run=args.dry_run,
                )
                if path:
                    written[bill_id + "_item"] = path
                    canonical["drafted_itemization_request"] = str(
                        Path(path).relative_to(HEALTH_ROOT)
                    )

        # Encounter context for any of the main-letter drafts that
        # follow. Computed once and passed via extras.
        encounter_block = gather_encounter_siblings(canonical, tracker_rows)

        # Encounter-combined dispute — drafted once per encounter when
        # the encounter has 4+ distinct billers (a hospital-admission
        # signature pattern with facility + ER physician + radiology +
        # anesthesia or similar) and at least one bill in the
        # encounter has its EOB on file. The LLM uses the EOB evidence
        # to assess network status across the encounter. We anchor the
        # draft to the bill with the alphabetically-first bill_id in
        # the encounter so the letter is only generated once per
        # encounter across runs.
        eid = (canonical.get("encounter_id") or "").strip()
        if eid:
            encounter_members = [
                r for r in tracker_rows
                if r.get("encounter_id") == eid
            ]
            distinct_slugs = {
                r.get("biller_slug", "") for r in encounter_members
            }
            any_eob = any(
                r.get("has_eob") == "Y" for r in encounter_members
            )
            anchor_bill_id = sorted(
                r["bill_id"] for r in encounter_members
            )[0]
            if (len(distinct_slugs) >= 4
                    and any_eob
                    and canonical.get("bill_id") == anchor_bill_id):
                dest = bills_folder / (
                    f"{bill_id}_LETTER_ENCOUNTER_COMBINED.md"
                )
                path = draft_letter_if_needed(
                    canonical=canonical, all_rows=encounter_members,
                    letter_kind="ENCOUNTER_COMBINED",
                    template_key="encounter_combined",
                    dest=dest, force=args.force, dry_run=args.dry_run,
                    extras={"Encounter context": encounter_block},
                )
                if path:
                    written[bill_id + "_encounter"] = path

        # Counter-offer letter (preferred when bill is materially over
        # Medicare, both gates open, and no dispute already sent).
        if (has_eob and has_item and has_benchmarks
                and not sent_dispute and not sent_counter):
            benchmark_rows = read_benchmarks(slug)
            overpriced = filter_overpriced_benchmarks(benchmark_rows)
            # Auto-compute the counter-offer if the user hasn't set
            # one in tracker.csv yet.
            if not canonical.get("counter_offer_amount"):
                canonical["counter_offer_amount"] = compute_counter_offer(
                    canonical, benchmark_rows,
                )
            dest = bills_folder / f"{bill_id}_LETTER_COUNTER_OFFER.md"
            path = draft_letter_if_needed(
                canonical=canonical, all_rows=members,
                letter_kind="COUNTER_OFFER",
                template_key="counter_offer",
                dest=dest, force=args.force, dry_run=args.dry_run,
                extras={
                    "Counter-offer amount":
                        f"${canonical.get('counter_offer_amount', '')}",
                    "Overpriced line items":
                        format_benchmark_table(overpriced),
                    "Encounter context": encounter_block,
                },
            )
            if path:
                written[bill_id + "_counter"] = path
                canonical["drafted_counter_offer"] = str(
                    Path(path).relative_to(HEALTH_ROOT)
                )
                canonical["dispute_template_used"] = "counter_offer"

        # Dispute letter (only when BOTH gates are open and either no
        # benchmark evidence supports the price-gouging frame, or the
        # user has explicitly chosen to skip the counter-offer track).
        elif has_eob and has_item and not sent_dispute and not sent_counter:
            # Use the folder override if available so we don't need to
            # gather evidence twice when not in dry-run; only gather
            # the (cheap) sidecar text for the template picker when
            # actually drafting and no override exists.
            if slug in FOLDER_TEMPLATE_OVERRIDES:
                template_key = FOLDER_TEMPLATE_OVERRIDES[slug]
            elif args.dry_run:
                template_key = "initial_dispute"
            else:
                template_key = pick_dispute_template(
                    slug, gather_evidence_text(canonical),
                )
            dest = bills_folder / f"{bill_id}_DISPUTE_LETTER.md"
            path = draft_letter_if_needed(
                canonical=canonical, all_rows=members,
                letter_kind="DISPUTE",
                template_key=template_key,
                dest=dest, force=args.force, dry_run=args.dry_run,
                extras={"Encounter context": encounter_block},
            )
            if path:
                written[bill_id + "_dispute"] = path
                canonical["drafted_dispute_letter"] = str(
                    Path(path).relative_to(HEALTH_ROOT)
                )
                canonical["dispute_template_used"] = template_key

        # HIPAA records request — when the audit detector has surfaced
        # `service_not_received_suspected` on the canonical bill, we
        # draft the records-access letter automatically so the patient
        # can verify each billed service is in the chart before
        # proceeding with the dispute.
        findings = {
            f.strip() for f in
            (canonical.get("findings") or "").split(";")
            if f.strip()
        }
        if ("service_not_received_suspected" in findings
                and not canonical.get("drafted_hipaa_records_request")):
            dest = bills_folder / (
                f"{bill_id}_LETTER_RECORDS_REQUEST_HIPAA.md"
            )
            path = draft_letter_if_needed(
                canonical=canonical, all_rows=members,
                letter_kind="RECORDS_REQUEST_HIPAA",
                template_key="records_request_hipaa",
                dest=dest, force=args.force, dry_run=args.dry_run,
                extras={"Encounter context": encounter_block},
            )
            if path:
                written[bill_id + "_hipaa"] = path
                canonical["drafted_hipaa_records_request"] = str(
                    Path(path).relative_to(HEALTH_ROOT)
                )

        # WC / auto-medpay redirect — when the bill is for a work-
        # related or motor-vehicle injury, the first move is to
        # redirect billing to the right payer. We draft the redirect
        # in addition to (not instead of) the regular dispute flow so
        # the user can mail it first.
        routing = detect_injury_routing(canonical)
        if routing == "wc":
            dest = bills_folder / (
                f"{bill_id}_LETTER_WC_CARRIER_REDIRECT.md"
            )
            path = draft_letter_if_needed(
                canonical=canonical, all_rows=members,
                letter_kind="WC_REDIRECT",
                template_key="wc_carrier_redirect",
                dest=dest, force=args.force, dry_run=args.dry_run,
                extras={"Encounter context": encounter_block},
            )
            if path:
                written[bill_id + "_wc"] = path
        elif routing == "auto":
            dest = bills_folder / (
                f"{bill_id}_LETTER_AUTO_MED_PAY.md"
            )
            path = draft_letter_if_needed(
                canonical=canonical, all_rows=members,
                letter_kind="AUTO_MED_PAY",
                template_key="auto_med_pay",
                dest=dest, force=args.force, dry_run=args.dry_run,
                extras={"Encounter context": encounter_block},
            )
            if path:
                written[bill_id + "_auto"] = path

        # DOI complaint — parallel pressure track, drafted as soon as
        # the main letter (dispute or counter-offer) is in the queue or
        # already sent. Filed via the state portal same day as mailing.
        if (sent_dispute or sent_counter or canonical.get("drafted_dispute_letter")
                or canonical.get("drafted_counter_offer")) and not sent_doi:
            state_code = (
                BILLER_STATE_OVERRIDES.get(slug) or PATIENT_STATE
            )
            dest = bills_folder / f"{bill_id}_COMPLAINT_DOI.md"
            path = draft_letter_if_needed(
                canonical=canonical, all_rows=members,
                letter_kind="DOI_COMPLAINT",
                template_key="doi_complaint",
                dest=dest, force=args.force, dry_run=args.dry_run,
                extras={
                    "State portal data":
                        doi_portal_extract(state_code),
                    "State code": (state_code or "").upper(),
                },
            )
            if path:
                written[bill_id + "_doi"] = path
                canonical["drafted_doi_complaint"] = str(
                    Path(path).relative_to(HEALTH_ROOT)
                )

        # Small claims civil-warrant — drafted only when the 30-day
        # warning has gone unanswered for 15 days. We don't try to
        # compute "elapsed days" here; the user signals readiness by
        # populating thirty_day_warning_sent_date and clearing any
        # resolution flag. The drafter then produces the warrant.
        if sent_warning and not filed_small_claims:
            dest = bills_folder / (
                f"{bill_id}_SMALL_CLAIMS_CIVIL_WARRANT.md"
            )
            path = draft_letter_if_needed(
                canonical=canonical, all_rows=members,
                letter_kind="SMALL_CLAIMS",
                template_key="small_claims_civil_warrant",
                dest=dest, force=args.force, dry_run=args.dry_run,
                extras={
                    "Counter-offer amount (if any)":
                        canonical.get("counter_offer_amount", ""),
                    "DOI complaint number (if filed)":
                        canonical.get("doi_complaint_number", ""),
                },
            )
            if path:
                written[bill_id + "_small_claims"] = path
                canonical["drafted_small_claims_civil_warrant"] = str(
                    Path(path).relative_to(HEALTH_ROOT)
                )

        # Mark superseded members
        for r in members:
            if r["bill_id"] != bill_id:
                r["status"] = "superseded"
                r["next_action"] = "see_canonical"
                prior_note = (r.get("notes") or "").strip()
                stamp = (f"superseded by {bill_id} on "
                         f"{datetime.date.today().isoformat()}")
                r["notes"] = f"{prior_note}; {stamp}" if prior_note else stamp

    if not args.dry_run:
        write_tracker(tracker_rows)
        print(f"\n[done] {len(written)} letter(s) drafted; "
              f"tracker updated: {TRACKER_CSV}", flush=True)
    else:
        print(f"\n[dry-run] would draft {len(written)} letter(s)",
              flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
