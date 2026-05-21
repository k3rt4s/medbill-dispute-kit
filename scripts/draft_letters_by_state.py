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
    "bill_id", "biller_slug", "biller_name", "doc_type", "account_number",
    "file", "statement_date", "dos_start", "dos_end",
    "total_billed", "current_balance",
    "has_eob", "matched_claim_numbers", "has_itemization",
    "itemization_signals",
    "status", "next_action", "next_action_due",
    "eob_request_sent_date", "eob_request_tracking",
    "itemization_request_sent_date", "itemization_request_tracking",
    "dispute_letter_sent_date", "dispute_letter_tracking",
    "thirty_day_warning_sent_date", "thirty_day_warning_tracking",
    "drafted_eob_request", "drafted_itemization_request",
    "drafted_dispute_letter", "dispute_template_used",
    "response_due_date", "notes",
]

# Per-folder dispute-template overrides for known cases. Populate this
# on YOUR workstation with biller slugs whose dispute template is
# already known, e.g.:
#
#   FOLDER_TEMPLATE_OVERRIDES = {
#       "quantum_radiology": "no_surprises",   # ER ancillary, NSA
#       "humana": "dental_dispute",             # dental denial in flight
#       "labcorp": "fdcpa",                     # collection notices
#   }
#
# Empty by default in the public kit — the content-based picker below
# will pick a template from the bill/EOB text on its own.
FOLDER_TEMPLATE_OVERRIDES: dict[str, str] = {}

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
}


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
# letter). Empty by default; populate on your own workstation.
#
# Example:
#   BILLER_STATE_OVERRIDES = {
#       "wellstar_health_system": "ga",  # services rendered in Georgia
#   }
BILLER_STATE_OVERRIDES: dict[str, str] = {}

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
                supporting_law: str, history: str) -> str:
    client, deployment = vision_client()
    template_text = load_template(template_key)
    system = (
        "You are a senior medical-billing advocate drafting a single "
        "formal letter. Use the kit template as structure; substitute "
        "every placeholder with concrete values from the bill / EOB "
        "evidence; cite real federal and state statutes; tone firm, "
        "specific. Output the letter only — no preamble, no fenced "
        "code block, no commentary. Header at top: patient name + "
        "address + phone + email. Then date, then recipient block. "
        "Keep the [CERTIFIED MAIL TRACKING NUMBER] placeholder. State "
        "a 15 or 30 business-day response window. CC the relevant "
        "state insurance department; for services rendered in Georgia "
        "also cc the GA OCI; cc the federal CMS No Surprises Help "
        "Desk for NSA letters. Close with signature + account # + "
        "date of service. Do not invent values that aren't in the "
        "evidence."
    )
    user = (
        f"# Letter kind\n{letter_kind}\n\n"
        f"# Kit template ({template_key})\n{template_text}\n\n"
        f"# Patient identity\n{history}\n\n"
        f"# Law context\n{supporting_law}\n\n"
        f"# Bill / EOB evidence\n{evidence}\n"
    )
    resp = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        max_completion_tokens=4096,
    )
    return (resp.choices[0].message.content or "").strip()


def draft_letter_if_needed(canonical: dict, all_rows: list[dict],
                           letter_kind: str, template_key: str,
                           dest: Path, force: bool, dry_run: bool) -> str | None:
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
        sent_eob = canonical.get("eob_request_sent_date", "").strip()
        sent_item = canonical.get("itemization_request_sent_date", "").strip()
        sent_dispute = canonical.get("dispute_letter_sent_date", "").strip()
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

        # Dispute letter (only when BOTH gates are open)
        if has_eob and has_item and not sent_dispute:
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
            )
            if path:
                written[bill_id + "_dispute"] = path
                canonical["drafted_dispute_letter"] = str(
                    Path(path).relative_to(HEALTH_ROOT)
                )
                canonical["dispute_template_used"] = template_key

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
