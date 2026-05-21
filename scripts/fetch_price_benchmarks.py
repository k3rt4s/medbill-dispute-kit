"""fetch_price_benchmarks.py — extract CPT/HCPCS codes from each bill's
sidecar text and produce a per-folder pricing benchmark file.

For every itemized bill the kit knows about, this script:

  1. Reads the bill's `<file>.extracted.txt` sidecar.
  2. Pulls CPT/HCPCS codes that appear next to a dollar amount.
  3. Joins each code against `references/medicare_pfs_common.csv` to
     get the national-rate Medicare allowable.
  4. Computes a ratio (billed / Medicare) so the patient can see
     whether the bill is in fair-market range or wildly above.
  5. Emits `Billers/<slug>/_benchmarks.csv` for downstream use by the
     counter-offer drafter and DOI complaint.

This script makes NO network calls. Medicare PFS data ships with the
kit as a curated public-domain CSV (CY2025 national, non-GPCI-adjusted).
For codes not in the local lookup, the script emits a FAIR Health URL
and a Healthcare Bluebook URL the patient can open manually.

Marshall Allen's UCC § 2-305 "open price term" argument needs evidence
of fair market value. Medicare allowable is the most defensible
benchmark a patient can cite back to a provider. This script produces
that evidence as a structured artifact.

Usage:
   python fetch_price_benchmarks.py
   python fetch_price_benchmarks.py --slug a_specific_biller
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from collections import OrderedDict
from pathlib import Path

HEALTH_ROOT = Path(
    os.environ.get("HEALTHBILLS_ROOT")
    or (Path.home() / "Health_Bills")
)
BILLERS_DIR = HEALTH_ROOT / "Billers"
MRF_DIR = HEALTH_ROOT / "_mrf_lookups"
SIDECAR_SUFFIX = ".extracted.txt"
BILLS_FILENAME = "_bills.csv"
BENCHMARKS_FILENAME = "_benchmarks.csv"

KIT_ROOT = Path(__file__).resolve().parent.parent
MEDICARE_LOOKUP = KIT_ROOT / "references" / "medicare_pfs_common.csv"

# Patient ZIP for FAIR Health URL (optional). Set
# HEALTHBILLS_PATIENT_ZIP on your workstation. The kit ships without
# a default so the public repo does not carry workstation values.
PATIENT_ZIP = (os.environ.get("HEALTHBILLS_PATIENT_ZIP") or "").strip()

# CPT/HCPCS code formats:
#   CPT: 5 digits (e.g. 99284, 71046)
#   HCPCS Level II: 1 letter + 4 digits (e.g. J3490, A0429)
# We require a nearby dollar amount so we don't pick up MRNs / dates
# that happen to look like numbers.
CODE_AND_AMOUNT_RE = re.compile(
    r"(?P<code>\b(?:[A-Z]\d{4}|\d{5})\b)"
    r"(?P<gap>[^\n$]{0,200})"
    r"\$\s*(?P<amount>\d{1,3}(?:,\d{3})*\.\d{2})",
    re.MULTILINE,
)
# Reverse direction: amount then code on same line
AMOUNT_AND_CODE_RE = re.compile(
    r"\$\s*(?P<amount>\d{1,3}(?:,\d{3})*\.\d{2})"
    r"(?P<gap>[^\n$]{0,80})"
    r"(?P<code>\b(?:[A-Z]\d{4}|\d{5})\b)",
    re.MULTILINE,
)

BENCHMARK_COLUMNS = [
    "bill_file", "cpt_code", "description",
    "billed_amount", "medicare_national",
    "ratio_billed_to_medicare",
    "hospital_cash_price", "hospital_min_negotiated",
    "hospital_max_negotiated",
    "fairhealth_url", "bluebook_url",
    "category", "notes",
]


def load_medicare_lookup() -> dict[str, dict]:
    if not MEDICARE_LOOKUP.exists():
        return {}
    with MEDICARE_LOOKUP.open(encoding="utf-8") as fh:
        return {row["cpt_code"]: row for row in csv.DictReader(fh)}


def load_mrf_lookup() -> dict[str, dict]:
    """Aggregate every `_mrf_lookups/mrf_*.csv` file into a single
    {cpt_code: {cash, min_negotiated, max_negotiated}} map. When the
    same CPT appears in multiple hospitals' files, the lowest cash and
    lowest min_negotiated win (most patient-favorable). Returns an
    empty dict if no MRF lookups have been fetched."""
    out: dict[str, dict] = {}
    if not MRF_DIR.is_dir():
        return out
    for mrf_csv in sorted(MRF_DIR.glob("mrf_*.csv")):
        with mrf_csv.open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                code = (row.get("cpt_code") or "").strip().upper()
                if not code:
                    continue
                slot = out.setdefault(code, {})
                for source_col, target_col, prefer in [
                    ("discounted_cash", "cash", "lowest"),
                    ("min_negotiated", "min_negotiated", "lowest"),
                    ("max_negotiated", "max_negotiated", "highest"),
                ]:
                    raw = (row.get(source_col) or "").strip()
                    if not raw:
                        continue
                    try:
                        val = float(raw)
                    except ValueError:
                        continue
                    if target_col not in slot:
                        slot[target_col] = val
                    elif prefer == "lowest":
                        slot[target_col] = min(slot[target_col], val)
                    else:
                        slot[target_col] = max(slot[target_col], val)
    return out


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


def extract_code_amount_pairs(body: str) -> list[tuple[str, float]]:
    """Pull (code, billed_amount) pairs. If a code appears multiple
    times with different amounts, keep the largest (assumed the
    line-level charge, not a partial)."""
    best: dict[str, float] = {}
    for rx in (CODE_AND_AMOUNT_RE, AMOUNT_AND_CODE_RE):
        for m in rx.finditer(body):
            code = m.group("code").upper()
            try:
                amt = float(m.group("amount").replace(",", ""))
            except ValueError:
                continue
            # Skip code-shaped numbers that are clearly not charges
            if amt < 0.01 or amt > 1_000_000:
                continue
            if code not in best or amt > best[code]:
                best[code] = amt
    return sorted(best.items())


def fairhealth_url(code: str) -> str:
    """Build a deep link to FAIR Health Consumer for a given CPT.
    Their search uses a code parameter; with a ZIP we can pre-fill."""
    base = "https://www.fairhealthconsumer.org/medical/search-result"
    if PATIENT_ZIP:
        return f"{base}?cpt={code}&zip={PATIENT_ZIP}"
    return f"{base}?cpt={code}"


def bluebook_url(code: str) -> str:
    """Healthcare Bluebook public search. Full data requires an
    employer-sponsored account but the search lands the patient on the
    relevant page."""
    return f"https://www.healthcarebluebook.com/cpx/p/{code}"


def benchmarks_for_bill(bill_file: str, body: str,
                        lookup: dict[str, dict],
                        mrf_lookup: dict[str, dict]) -> list[dict]:
    pairs = extract_code_amount_pairs(body)
    out: list[dict] = []
    for code, billed in pairs:
        ref = lookup.get(code, {})
        mrf = mrf_lookup.get(code, {})
        # Prefer non-facility for office, facility for ED/inpatient;
        # we can't tell from here, so we average the two if both exist
        # and the spread is small. Otherwise default to non-facility.
        mc = ""
        try:
            f_val = float(ref.get("medicare_national_facility") or 0) or None
            nf_val = float(ref.get("medicare_national_nonfacility") or 0) or None
        except ValueError:
            f_val = nf_val = None
        if f_val and nf_val:
            mc = f"{(f_val + nf_val) / 2:.2f}"
        elif nf_val:
            mc = f"{nf_val:.2f}"
        elif f_val:
            mc = f"{f_val:.2f}"
        ratio = ""
        if mc:
            try:
                ratio = f"{billed / float(mc):.2f}"
            except (ZeroDivisionError, ValueError):
                ratio = ""
        def fmt(v):
            return "" if v is None else f"{v:.2f}"

        out.append({
            "bill_file": bill_file,
            "cpt_code": code,
            "description": ref.get("description", ""),
            "billed_amount": f"{billed:.2f}",
            "medicare_national": mc,
            "ratio_billed_to_medicare": ratio,
            "hospital_cash_price": fmt(mrf.get("cash")),
            "hospital_min_negotiated": fmt(mrf.get("min_negotiated")),
            "hospital_max_negotiated": fmt(mrf.get("max_negotiated")),
            "fairhealth_url": fairhealth_url(code),
            "bluebook_url": bluebook_url(code),
            "category": ref.get("category", ""),
            "notes": ref.get("notes", ""),
        })
    return out


def process_slug(slug_dir: Path,
                 lookup: dict[str, dict],
                 mrf_lookup: dict[str, dict]) -> int:
    bills_csv = slug_dir / BILLS_FILENAME
    if not bills_csv.exists():
        return 0
    rows_out: list[dict] = []
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
            rows_out.extend(benchmarks_for_bill(
                file_name, body, lookup, mrf_lookup,
            ))
    out_path = slug_dir / BENCHMARKS_FILENAME
    if not rows_out:
        # Remove a stale benchmarks file if nothing matched this run
        if out_path.exists():
            out_path.unlink()
        return 0
    with out_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=BENCHMARK_COLUMNS)
        w.writeheader()
        for row in rows_out:
            w.writerow(row)
    return len(rows_out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--slug", help="Only process this biller slug")
    args = ap.parse_args()

    if not BILLERS_DIR.is_dir():
        print(f"[fatal] no Billers/ tree at {BILLERS_DIR}", flush=True)
        return 1

    lookup = load_medicare_lookup()
    if not lookup:
        print(f"[warn] no Medicare lookup at {MEDICARE_LOOKUP}; "
              f"ratios will be blank", flush=True)

    mrf_lookup = load_mrf_lookup()
    if mrf_lookup:
        print(f"[info] merged {len(mrf_lookup)} CPT codes from "
              f"hospital MRF lookups in {MRF_DIR}", flush=True)
    else:
        print(f"[info] no MRF lookups found in {MRF_DIR}; "
              f"hospital_cash_price and hospital_*_negotiated columns "
              f"will be blank", flush=True)

    counts = OrderedDict()
    for slug_dir in sorted(d for d in BILLERS_DIR.iterdir() if d.is_dir()):
        if args.slug and slug_dir.name != args.slug:
            continue
        n = process_slug(slug_dir, lookup, mrf_lookup)
        if n:
            counts[slug_dir.name] = n

    total = sum(counts.values())
    print(f"[done] {total} benchmark rows across {len(counts)} biller(s)",
          flush=True)
    for slug, n in counts.items():
        print(f"  {slug}: {n} CPT rows -> "
              f"Billers/{slug}/{BENCHMARKS_FILENAME}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
