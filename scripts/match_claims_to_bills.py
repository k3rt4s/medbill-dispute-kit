"""match_claims_to_bills.py — link each EOB claim row to the bill row
it adjudicates, using:

1. Deterministic rules (cheap, no API):
   - Same biller_slug.
   - Patient responsibility on the claim equals current_balance on the
     bill within $0.50, OR equals total_billed within $0.50.
   - Date-of-service overlap between the claim and the bill (DOS
     ranges intersect, OR the claim's DOS is within 60 days of the
     bill's statement_date if DOS isn't on the bill).

2. Azure OpenAI gpt-5.2 fallback (only when deterministic returns
   AMBIGUOUS — 0 or >1 candidates) with a strict "respond UNKNOWN if
   not confident" prompt.

Outputs:
   C:/Code_data/medbill-dispute-kit/tracker/matches.csv
   one row per attempted match with:
     - bill_id (a stable Bills/<slug>/<file> identifier)
     - claim_id (Bills/<slug>/<file> + claim_number)
     - match_type: deterministic | azure | unmatched
     - confidence: high | medium | low | none
     - rationale: short text

Usage:
   python match_claims_to_bills.py
   python match_claims_to_bills.py --dry-run
"""

from __future__ import annotations

import argparse
import csv
import datetime
import json
import os
import re
import sys
from pathlib import Path

HEALTH_ROOT = Path(
    os.environ.get("HEALTHBILLS_ROOT")
    or (Path.home() / "Health_Bills")
)
BILLERS_DIR = HEALTH_ROOT / "Billers"
EOB_DIR = HEALTH_ROOT / "EOB"
LOG_DIR = Path(
    os.environ.get("HEALTHBILLS_LOG_DIR")
    or (Path.home() / ".medbill-dispute-kit" / "tracker")
)
ENV_FILE = Path(
    os.environ.get("MEDBILL_KIT_ENV_FILE")
    or (Path.home() / ".medbill-dispute-kit" / ".env")
)

MATCHES_CSV = LOG_DIR / "matches.csv"
BILLS_CSV = "_bills.csv"
CLAIMS_CSV = "_claims.csv"

AMOUNT_TOLERANCE = 0.50
DOS_FALLBACK_WINDOW_DAYS = 60

OUT_COLUMNS = [
    "match_id", "match_type", "confidence",
    "bill_slug", "bill_file", "bill_account", "bill_statement_date",
    "bill_dos_start", "bill_total_billed", "bill_current_balance",
    "claim_slug", "claim_file", "claim_number",
    "claim_dos_start", "claim_patient_responsibility",
    "claim_provider_rendering", "claim_biller_entity",
    "rationale",
]


def parse_float(s) -> float | None:
    if s is None or s == "":
        return None
    try:
        return float(str(s).replace(",", "").replace("$", ""))
    except (TypeError, ValueError):
        return None


def parse_date(s) -> datetime.date | None:
    if not s:
        return None
    s = str(s).strip()
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", s):
        return None
    try:
        return datetime.date.fromisoformat(s)
    except ValueError:
        return None


def load_bills_for_slug(slug: str) -> list[dict]:
    csv_path = BILLERS_DIR / slug / BILLS_CSV
    if not csv_path.exists():
        return []
    with csv_path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def load_claims_for_slug(slug: str) -> list[dict]:
    csv_path = EOB_DIR / slug / CLAIMS_CSV
    if not csv_path.exists():
        return []
    with csv_path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def list_slugs() -> list[str]:
    seen: set[str] = set()
    for root in (BILLERS_DIR, EOB_DIR):
        if not root.is_dir():
            continue
        for d in root.iterdir():
            if d.is_dir():
                seen.add(d.name)
    return sorted(seen)


def dos_overlap(claim: dict, bill: dict) -> tuple[bool, str]:
    """Return (overlap, reason). DOS ranges that intersect, or any
    fallback rule (claim DOS within window of statement_date) qualify."""
    c_start = parse_date(claim.get("dos_start"))
    c_end = parse_date(claim.get("dos_end")) or c_start
    b_start = parse_date(bill.get("dos_start"))
    b_end = parse_date(bill.get("dos_end")) or b_start
    stmt = parse_date(bill.get("statement_date"))

    if c_start and b_start:
        if (c_start <= (b_end or b_start)) and ((c_end or c_start) >= b_start):
            return True, f"DOS intersect ({c_start}..{c_end} ∩ {b_start}..{b_end})"
        if stmt and abs((c_start - stmt).days) <= DOS_FALLBACK_WINDOW_DAYS:
            return True, f"claim DOS {c_start} within {DOS_FALLBACK_WINDOW_DAYS}d of stmt {stmt}"
    if c_start and stmt and not b_start:
        if abs((c_start - stmt).days) <= DOS_FALLBACK_WINDOW_DAYS:
            return True, f"claim DOS {c_start} within {DOS_FALLBACK_WINDOW_DAYS}d of stmt {stmt} (no bill DOS)"
    return False, "no DOS overlap"


def amount_match(claim: dict, bill: dict) -> tuple[bool, str]:
    claim_amt = parse_float(claim.get("patient_responsibility"))
    bill_balance = parse_float(bill.get("current_balance"))
    bill_billed = parse_float(bill.get("total_billed"))
    if claim_amt is None or claim_amt <= 0:
        return False, "claim patient_responsibility is zero/null"
    if bill_balance is not None and \
            abs(claim_amt - bill_balance) <= AMOUNT_TOLERANCE:
        return True, f"claim ${claim_amt:.2f} ~= bill balance ${bill_balance:.2f}"
    if bill_billed is not None and \
            abs(claim_amt - bill_billed) <= AMOUNT_TOLERANCE:
        return True, f"claim ${claim_amt:.2f} ~= bill billed ${bill_billed:.2f}"
    return False, (f"claim ${claim_amt:.2f} != bill balance "
                   f"${bill_balance!r} / billed ${bill_billed!r}")


def deterministic_match(claim: dict, bills: list[dict]) -> list[tuple[dict, list[str]]]:
    """Return all bills that match claim deterministically with rationales."""
    candidates: list[tuple[dict, list[str]]] = []
    for bill in bills:
        amt_ok, amt_msg = amount_match(claim, bill)
        if not amt_ok:
            continue
        dos_ok, dos_msg = dos_overlap(claim, bill)
        if not dos_ok:
            continue
        candidates.append((bill, [amt_msg, dos_msg]))
    return candidates


def load_env(env_path: Path) -> None:
    if not env_path.exists():
        return
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


AZURE_SYSTEM = """\
You are linking a UHC EOB claim entry to a provider bill statement.
The two documents should describe the same transaction if they are
truly a match. Required signals for a confident match:
- Patient responsibility on the EOB closely matches the bill's
  current balance or total billed (within $0.50)
- Date of service on the claim falls within a reasonable window of
  the bill's statement / service date
- Provider/biller name on the EOB is the same entity as the bill's
  biller (or at least an obvious doing-business-as variant)

Be conservative. The cost of a wrong match is a misdirected dispute
letter. If you are not confident, respond with status="UNKNOWN".

Respond with JSON only:
{
  "status": "MATCH" | "NO_MATCH" | "UNKNOWN",
  "matched_bill_file": "<file name from candidates if status=MATCH, else null>",
  "rationale": "short single sentence"
}
"""


def azure_match(claim: dict, bills: list[dict]) -> dict | None:
    if not bills:
        return None
    try:
        client, deployment = vision_client()
    except Exception:
        return None
    candidate_blob = ""
    for i, bill in enumerate(bills, 1):
        candidate_blob += (
            f"\n--- candidate bill {i} ---\n"
            f"file: {bill.get('file')}\n"
            f"biller_name_raw: {bill.get('biller_name_raw')}\n"
            f"account_number: {bill.get('account_number')}\n"
            f"statement_date: {bill.get('statement_date')}\n"
            f"dos_start: {bill.get('dos_start')}\n"
            f"dos_end: {bill.get('dos_end')}\n"
            f"total_billed: ${bill.get('total_billed')}\n"
            f"current_balance: ${bill.get('current_balance')}\n"
        )
    user = (
        f"# Claim entry from an EOB\n"
        f"file: {claim.get('file')}\n"
        f"claim_number: {claim.get('claim_number')}\n"
        f"provider_rendering: {claim.get('provider_rendering_raw')}\n"
        f"biller_entity: {claim.get('biller_entity_raw')}\n"
        f"network_status: {claim.get('network_status')}\n"
        f"dos_start: {claim.get('dos_start')}\n"
        f"dos_end: {claim.get('dos_end')}\n"
        f"patient_responsibility: ${claim.get('patient_responsibility')}\n"
        f"\n# Candidate bills (same biller slug)\n"
        f"{candidate_blob}\n"
    )
    try:
        resp = client.chat.completions.create(
            model=deployment,
            messages=[
                {"role": "system", "content": AZURE_SYSTEM},
                {"role": "user", "content": user},
            ],
            max_completion_tokens=512,
        )
    except Exception as exc:
        print(f"  [azure error] {exc}", flush=True)
        return None
    raw = (resp.choices[0].message.content or "").strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true",
                    help="Compute matches but don't write the CSV.")
    args = ap.parse_args()

    slugs = list_slugs()
    print(f"[main] {len(slugs)} slug(s) to consider", flush=True)

    rows: list[dict] = []
    counters = {"deterministic_1": 0, "deterministic_n": 0,
                "azure_match": 0, "azure_unknown": 0,
                "unmatched_no_candidate": 0}

    for slug in slugs:
        bills = load_bills_for_slug(slug)
        claims = load_claims_for_slug(slug)
        if not claims and not bills:
            continue
        if not claims:
            for b in bills:
                rows.append({
                    "match_id": f"{slug}/{b.get('file')}/bill-only",
                    "match_type": "bill_only",
                    "confidence": "none",
                    "bill_slug": slug, "bill_file": b.get("file"),
                    "bill_account": b.get("account_number"),
                    "bill_statement_date": b.get("statement_date"),
                    "bill_dos_start": b.get("dos_start"),
                    "bill_total_billed": b.get("total_billed"),
                    "bill_current_balance": b.get("current_balance"),
                    "rationale": "no claims for this slug",
                })
            continue
        if not bills:
            for c in claims:
                rows.append({
                    "match_id": f"{slug}/{c.get('file')}/{c.get('claim_number')}/claim-only",
                    "match_type": "claim_only",
                    "confidence": "none",
                    "claim_slug": slug, "claim_file": c.get("file"),
                    "claim_number": c.get("claim_number"),
                    "claim_dos_start": c.get("dos_start"),
                    "claim_patient_responsibility":
                        c.get("patient_responsibility"),
                    "claim_provider_rendering":
                        c.get("provider_rendering_raw"),
                    "claim_biller_entity": c.get("biller_entity_raw"),
                    "rationale": "no bills for this slug",
                })
            continue

        for claim in claims:
            candidates = deterministic_match(claim, bills)
            if len(candidates) == 1:
                bill, rationales = candidates[0]
                rows.append(build_match_row(
                    slug, bill, claim,
                    match_type="deterministic", confidence="high",
                    rationale="; ".join(rationales),
                ))
                counters["deterministic_1"] += 1
                continue
            if len(candidates) > 1:
                # Multiple deterministic candidates -> ask Azure
                model_out = azure_match(claim, [c[0] for c in candidates])
                if model_out and model_out.get("status") == "MATCH":
                    picked_file = model_out.get("matched_bill_file")
                    picked = next(
                        (b for b, _ in candidates
                         if b.get("file") == picked_file),
                        None,
                    )
                    if picked is not None:
                        rows.append(build_match_row(
                            slug, picked, claim,
                            match_type="azure", confidence="medium",
                            rationale=(model_out.get("rationale") or "")
                                + " (multiple deterministic candidates)",
                        ))
                        counters["azure_match"] += 1
                        continue
                # Either no clear pick or model returned UNKNOWN
                rows.append(build_match_row(
                    slug, None, claim,
                    match_type="azure_unknown", confidence="low",
                    rationale=f"{len(candidates)} candidates; model: "
                              f"{(model_out or {}).get('status', 'no response')}",
                ))
                counters["azure_unknown"] += 1
                continue
            # No deterministic match — try azure across all bills for slug
            model_out = azure_match(claim, bills)
            if model_out and model_out.get("status") == "MATCH":
                picked_file = model_out.get("matched_bill_file")
                picked = next(
                    (b for b in bills if b.get("file") == picked_file),
                    None,
                )
                if picked is not None:
                    rows.append(build_match_row(
                        slug, picked, claim,
                        match_type="azure", confidence="medium",
                        rationale=model_out.get("rationale", ""),
                    ))
                    counters["azure_match"] += 1
                    continue
            rows.append(build_match_row(
                slug, None, claim,
                match_type="unmatched", confidence="none",
                rationale=f"no deterministic match; model: "
                          f"{(model_out or {}).get('status', 'no response')}",
            ))
            counters["unmatched_no_candidate"] += 1

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    if not args.dry_run:
        with MATCHES_CSV.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=OUT_COLUMNS, extrasaction="ignore")
            w.writeheader()
            for r in rows:
                w.writerow(r)
        print(f"\n[done] {MATCHES_CSV}", flush=True)
    else:
        print(f"\n[dry-run] would write {len(rows)} rows", flush=True)
    print(f"[counters] {counters}", flush=True)
    return 0


def build_match_row(slug: str, bill: dict | None, claim: dict,
                    match_type: str, confidence: str,
                    rationale: str) -> dict:
    row = {
        "match_id": f"{slug}/{claim.get('file')}/{claim.get('claim_number', 'noclaim')}",
        "match_type": match_type,
        "confidence": confidence,
        "claim_slug": slug,
        "claim_file": claim.get("file", ""),
        "claim_number": claim.get("claim_number", ""),
        "claim_dos_start": claim.get("dos_start", ""),
        "claim_patient_responsibility":
            claim.get("patient_responsibility", ""),
        "claim_provider_rendering":
            claim.get("provider_rendering_raw", ""),
        "claim_biller_entity": claim.get("biller_entity_raw", ""),
        "rationale": rationale,
    }
    if bill is not None:
        row.update({
            "bill_slug": slug,
            "bill_file": bill.get("file", ""),
            "bill_account": bill.get("account_number", ""),
            "bill_statement_date": bill.get("statement_date", ""),
            "bill_dos_start": bill.get("dos_start", ""),
            "bill_total_billed": bill.get("total_billed", ""),
            "bill_current_balance": bill.get("current_balance", ""),
        })
    return row


if __name__ == "__main__":
    sys.exit(main())
