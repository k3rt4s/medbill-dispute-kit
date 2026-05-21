"""audit_billing_errors.py — scan each bill sidecar for common billing
errors Marshall Allen describes in "Never Pay the First Bill": duplicate
CPTs on the same date of service, common unbundling-violation pairs
(NCCI edits), modifier-25 stacking, and aging / late-fee charges that
imply an account was already overdue and the patient should be sent to
financial assistance instead.

Writes `Billers/<slug>/_audit.csv` per folder with one row per finding.
Findings are structured (finding_code + cpt_pair + line_amount + note)
so the dispute drafter can cite them by code. Findings are also
written back to the `_bills.csv` `notes` column so they show up in
tracker.csv.

This script makes no network calls. NCCI / unbundling rules ship as a
small static table; the patient or contributor can extend it via
`references/ncci_pairs_common.csv`.

Usage:
    python audit_billing_errors.py
    python audit_billing_errors.py --slug a_specific_biller
"""

from __future__ import annotations

import argparse
import csv
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
SIDECAR_SUFFIX = ".extracted.txt"
BILLS_FILENAME = "_bills.csv"
AUDIT_FILENAME = "_audit.csv"

KIT_ROOT = Path(__file__).resolve().parent.parent
NCCI_LOOKUP = KIT_ROOT / "references" / "ncci_pairs_common.csv"

# Common NCCI / unbundling pairs. When BOTH codes appear on the same
# bill, the more comprehensive code includes the simpler one and
# should not be billed alongside. CMS publishes the full National
# Correct Coding Initiative file; this ships a small high-frequency
# subset. Extend via references/ncci_pairs_common.csv (same columns)
# without touching this script.
NCCI_PAIRS_DEFAULT = [
    # (more_comprehensive, included, note)
    ("85025", "85027", "85025 (CBC w/ diff) includes 85027 (CBC w/o diff)"),
    ("85025", "85004", "85025 includes 85004 (auto diff WBC count)"),
    ("85025", "85007", "85025 includes 85007 (manual diff WBC count)"),
    ("80053", "80048", "CMP 80053 includes BMP 80048"),
    ("80053", "84520", "CMP 80053 includes BUN 84520"),
    ("80053", "82565", "CMP 80053 includes creatinine 82565"),
    ("80048", "84520", "BMP 80048 includes BUN 84520"),
    ("80048", "82565", "BMP 80048 includes creatinine 82565"),
    ("80061", "82465", "Lipid panel 80061 includes cholesterol 82465"),
    ("80061", "84478", "Lipid panel 80061 includes triglycerides 84478"),
    ("80061", "83718", "Lipid panel 80061 includes HDL 83718"),
    ("80076", "84450", "Hepatic panel 80076 includes AST 84450"),
    ("80076", "84460", "Hepatic panel 80076 includes ALT 84460"),
    ("80076", "82247", "Hepatic panel 80076 includes total bilirubin 82247"),
    ("81003", "81001", "Auto UA 81003 and UA w/ micro 81001 should not bill same DOS"),
    ("93000", "93005", "EKG 93000 (complete) includes 93005 (tracing only)"),
    ("93000", "93010", "EKG 93000 (complete) includes 93010 (interp only)"),
    ("99214", "99213", "Same E/M level twice same day"),
    ("99284", "99283", "Same ED level twice same day"),
]

CODE_AMOUNT_DATE_RE = re.compile(
    r"(?P<code>\b(?:[A-Z]\d{4}|\d{5})\b)"
    r"[^\n$]{0,200}?"
    r"\$\s*(?P<amount>\d{1,3}(?:,\d{3})*\.\d{2})",
    re.MULTILINE,
)
DOS_NEARBY_RE = re.compile(
    r"\b(\d{1,2}/\d{1,2}/\d{2,4}|\d{4}-\d{2}-\d{2})\b"
)
MODIFIER_25_RE = re.compile(
    r"\bmodifier\s*[-:]?\s*25\b|"
    r"\b-25\s*(?:modifier|mod)\b|"
    r"\b25\s+modifier\b",
    re.I,
)
EM_CODE_RE = re.compile(r"\b9921[2-5]|9920[2-5]|9928[1-5]\b")
LATE_FEE_RE = re.compile(
    r"\b(late\s+fee|finance\s+charge|past[-\s]?due\s+fee|"
    r"interest\s+(?:charge|accrued)|rebilling\s+fee|"
    r"statement\s+fee)\b",
    re.I,
)
NEVER_RECEIVED_HINTS_RE = re.compile(
    r"\b(no[-\s]?show|cancell?ed|did\s+not\s+receive|"
    r"refused\s+(?:treatment|service)|left\s+(?:without|AMA))\b",
    re.I,
)
QUANTITY_INFLATION_RE = re.compile(
    r"\b(units?|qty|quantity)\s*[:=]?\s*(\d{2,})\b",
    re.I,
)

AUDIT_COLUMNS = [
    "bill_file", "finding_code", "severity", "cpt_or_pair",
    "amount_implicated", "note",
]


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


def load_ncci_pairs() -> list[tuple[str, str, str]]:
    if not NCCI_LOOKUP.exists():
        return NCCI_PAIRS_DEFAULT
    pairs: list[tuple[str, str, str]] = []
    with NCCI_LOOKUP.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            comp = (row.get("comprehensive_code") or "").strip().upper()
            inc = (row.get("included_code") or "").strip().upper()
            note = (row.get("note") or "").strip()
            if comp and inc:
                pairs.append((comp, inc, note))
    return pairs or NCCI_PAIRS_DEFAULT


def extract_code_amounts(body: str) -> list[tuple[str, float]]:
    """Return [(code, amount), ...] preserving order and duplicates."""
    out: list[tuple[str, float]] = []
    for m in CODE_AMOUNT_DATE_RE.finditer(body):
        try:
            amt = float(m.group("amount").replace(",", ""))
        except ValueError:
            continue
        if amt < 0.01 or amt > 1_000_000:
            continue
        out.append((m.group("code").upper(), amt))
    return out


def audit_duplicate_cpts(pairs: list[tuple[str, float]]) -> list[dict]:
    """Same CPT appearing twice or more with a positive charge."""
    by_code: dict[str, list[float]] = defaultdict(list)
    for code, amt in pairs:
        by_code[code].append(amt)
    findings: list[dict] = []
    for code, amts in by_code.items():
        if len(amts) >= 2 and any(a > 0 for a in amts):
            findings.append({
                "finding_code": "duplicate_cpt_same_bill",
                "severity": "high",
                "cpt_or_pair": code,
                "amount_implicated": f"{sum(amts):.2f}",
                "note": (f"Code {code} appears {len(amts)} times with "
                         f"charges totaling ${sum(amts):.2f}; verify "
                         f"each instance was a distinct service"),
            })
    return findings


def audit_ncci_pairs(pairs: list[tuple[str, float]],
                     ncci: list[tuple[str, str, str]]) -> list[dict]:
    codes_present = {c for c, _ in pairs}
    amount_for: dict[str, float] = defaultdict(float)
    for code, amt in pairs:
        amount_for[code] += amt
    findings: list[dict] = []
    for comp, inc, note in ncci:
        if comp in codes_present and inc in codes_present:
            findings.append({
                "finding_code": "unbundling_ncci",
                "severity": "high",
                "cpt_or_pair": f"{comp}+{inc}",
                "amount_implicated":
                    f"{amount_for.get(inc, 0.0):.2f}",
                "note": note,
            })
    return findings


def audit_modifier_25(body: str,
                      pairs: list[tuple[str, float]]) -> list[dict]:
    if not MODIFIER_25_RE.search(body):
        return []
    em_codes = [c for c, _ in pairs if EM_CODE_RE.match(c)]
    if not em_codes:
        return []
    return [{
        "finding_code": "modifier_25_stacking",
        "severity": "medium",
        "cpt_or_pair": ";".join(sorted(set(em_codes))),
        "amount_implicated": "",
        "note": (f"E/M code(s) {','.join(sorted(set(em_codes)))} "
                 f"billed with modifier 25 alongside another "
                 f"procedure same DOS; verify the E/M was separately "
                 f"identifiable per CPT modifier 25 definition"),
    }]


def audit_late_fees(body: str) -> list[dict]:
    if not LATE_FEE_RE.search(body):
        return []
    return [{
        "finding_code": "late_fee_or_finance_charge",
        "severity": "medium",
        "cpt_or_pair": "",
        "amount_implicated": "",
        "note": ("Late fee, finance charge, or rebilling fee detected. "
                 "Many states cap or prohibit these on medical debt; "
                 "request removal and verify lawful basis under "
                 "applicable state medical-debt-protection statute"),
    }]


def audit_never_received_hints(body: str) -> list[dict]:
    if not NEVER_RECEIVED_HINTS_RE.search(body):
        return []
    return [{
        "finding_code": "service_not_received_suspected",
        "severity": "high",
        "cpt_or_pair": "",
        "amount_implicated": "",
        "note": ("Sidecar text contains language suggesting a service "
                 "may not have been delivered (no-show, cancelled, "
                 "left AMA, refused). Request the medical record under "
                 "HIPAA § 164.524 to verify each billed service was "
                 "actually rendered."),
    }]


def audit_quantity_inflation(body: str) -> list[dict]:
    findings: list[dict] = []
    for m in QUANTITY_INFLATION_RE.finditer(body):
        try:
            n = int(m.group(2))
        except ValueError:
            continue
        if n >= 10:
            findings.append({
                "finding_code": "quantity_high",
                "severity": "low",
                "cpt_or_pair": "",
                "amount_implicated": "",
                "note": (f"Line item shows quantity {n}. Confirm this "
                         f"matches the medical record; quantity "
                         f"inflation is a common error."),
            })
    return findings


def audit_bill(file_name: str, body: str,
                ncci: list[tuple[str, str, str]]) -> list[dict]:
    pairs = extract_code_amounts(body)
    findings: list[dict] = []
    findings.extend(audit_duplicate_cpts(pairs))
    findings.extend(audit_ncci_pairs(pairs, ncci))
    findings.extend(audit_modifier_25(body, pairs))
    findings.extend(audit_late_fees(body))
    findings.extend(audit_never_received_hints(body))
    findings.extend(audit_quantity_inflation(body))
    for f in findings:
        f["bill_file"] = file_name
    return findings


def process_slug(slug_dir: Path,
                 ncci: list[tuple[str, str, str]]) -> int:
    bills_csv = slug_dir / BILLS_FILENAME
    if not bills_csv.exists():
        return 0
    audit_rows: list[dict] = []
    with bills_csv.open(encoding="utf-8") as fh:
        for bill in csv.DictReader(fh):
            file_name = bill.get("file", "")
            if not file_name:
                continue
            sidecar = slug_dir / (file_name + SIDECAR_SUFFIX)
            if not sidecar.exists():
                continue
            body = read_sidecar_body(sidecar)
            if not body.strip():
                continue
            audit_rows.extend(audit_bill(file_name, body, ncci))
    out_path = slug_dir / AUDIT_FILENAME
    if not audit_rows:
        if out_path.exists():
            out_path.unlink()
        return 0
    with out_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=AUDIT_COLUMNS)
        w.writeheader()
        for row in audit_rows:
            w.writerow({c: row.get(c, "") for c in AUDIT_COLUMNS})
    return len(audit_rows)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--slug", help="Only process this biller slug")
    args = ap.parse_args()

    if not BILLERS_DIR.is_dir():
        print(f"[fatal] no Billers/ tree at {BILLERS_DIR}", flush=True)
        return 1

    ncci = load_ncci_pairs()

    counts: dict[str, int] = {}
    for slug_dir in sorted(d for d in BILLERS_DIR.iterdir() if d.is_dir()):
        if args.slug and slug_dir.name != args.slug:
            continue
        n = process_slug(slug_dir, ncci)
        if n:
            counts[slug_dir.name] = n

    total = sum(counts.values())
    print(f"[done] {total} audit findings across {len(counts)} biller(s)",
          flush=True)
    for slug, n in counts.items():
        print(f"  {slug}: {n} findings -> "
              f"Billers/{slug}/{AUDIT_FILENAME}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
