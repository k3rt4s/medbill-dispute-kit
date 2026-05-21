"""fetch_mrf.py — pull a hospital's machine-readable price file and
extract per-CPT prices for use in the counter-offer letter.

The federal Hospital Price Transparency Rule (45 CFR Part 180) requires
every US hospital to publish a complete machine-readable file of
standard charges. The format varies: CMS template JSON or CSV (the
post-July-2024 schema), Turquoise / TransparentRx legacy CSV / JSON,
or Epic-native wide CSV. This script content-sniffs which format the
file uses and pulls the relevant rows for a requested CPT list.

Output: `<HEALTHBILLS_ROOT>/_mrf_lookups/mrf_<hospital_slug>_<YYYYMMDD>.csv`
with one row per CPT containing the hospital's gross, cash, min/max
negotiated, and per-payer rates where available.

The script uses only the standard library (urllib + csv + json) so it
has no extra runtime dependencies.

Usage:
    python fetch_mrf.py --url https://example.com/standard-charges.json \\
        --hospital-slug example_general \\
        --cpts 99284,99285,71046,80053

    python fetch_mrf.py --url https://example.com/standard-charges.csv \\
        --hospital-slug example_general \\
        --cpts-file cpts.txt
"""

from __future__ import annotations

import argparse
import csv
import datetime
import io
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

HEALTH_ROOT = Path(
    os.environ.get("HEALTHBILLS_ROOT")
    or (Path.home() / "Health_Bills")
)
MRF_DIR = HEALTH_ROOT / "_mrf_lookups"

USER_AGENT = (
    "medbill-dispute-kit fetch_mrf.py "
    "(github.com/k3rt4s/medbill-dispute-kit)"
)
# 50 MB safety cap. Many hospital MRFs are large (hundreds of MB);
# a serious patient workflow should stream, but the kit's lookup is
# expected to target smaller files or hospital-specific summary files.
MAX_BYTES = 50 * 1024 * 1024

OUT_COLUMNS = [
    "cpt_code", "description", "gross_charge", "discounted_cash",
    "min_negotiated", "max_negotiated", "payer_specific_rates",
    "source_url", "retrieved", "format",
]


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as fh:
        data = fh.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise SystemExit(
            f"[fatal] MRF at {url} exceeds {MAX_BYTES} byte safety cap; "
            f"consider downloading manually and using a streaming parser."
        )
    return data


def detect_format(data: bytes) -> str:
    """Return one of: 'cms_json' | 'cms_csv' | 'turquoise_csv' |
    'transparentrx_json' | 'epic_csv' | 'unknown'."""
    head = data[:8192].decode("utf-8", errors="replace").strip()
    if head.startswith("{") or head.startswith("["):
        if '"standard_charge_information"' in head:
            return "cms_json"
        if '"PriceTransparency"' in head or '"ItemCode"' in head:
            return "transparentrx_json"
        return "cms_json"  # best-effort assume CMS
    # CSV-ish
    first_line = head.splitlines()[0].lower() if head else ""
    if "standard_charge|gross" in first_line or "code|1" in first_line:
        return "cms_csv"
    if "cpt_hcpcs_code" in first_line or "negotiated_rate" in first_line:
        return "turquoise_csv"
    if "billable_code" in first_line and "list_price" in first_line:
        return "epic_csv"
    return "unknown"


def safe_float(v) -> float | None:
    if v is None or v == "":
        return None
    try:
        return float(str(v).replace(",", "").replace("$", "").strip())
    except (TypeError, ValueError):
        return None


def fmt(value: float | None) -> str:
    return "" if value is None else f"{value:.2f}"


def parse_cms_json(data: bytes, wanted: set[str],
                   url: str) -> list[dict]:
    obj = json.loads(data.decode("utf-8", errors="replace"))
    rows: list[dict] = []
    for entry in obj.get("standard_charge_information", []):
        codes = [
            (c.get("code") or "").strip().upper()
            for c in entry.get("code_information", [])
            if (c.get("type") or "").upper() in ("CPT", "HCPCS")
        ]
        match = next((c for c in codes if c in wanted), None)
        if not match:
            continue
        for sc in entry.get("standard_charges", []):
            gross = safe_float(sc.get("gross_charge"))
            cash = safe_float(sc.get("discounted_cash"))
            mn = safe_float(sc.get("minimum"))
            mx = safe_float(sc.get("maximum"))
            payers = []
            for p in sc.get("payers_information", []):
                pn = p.get("payer_name", "")
                ln = p.get("plan_name", "")
                rate = safe_float(p.get("standard_charge_dollar"))
                if rate is not None:
                    payers.append(f"{pn}/{ln}:{rate:.2f}")
            rows.append({
                "cpt_code": match,
                "description": entry.get("description", ""),
                "gross_charge": fmt(gross),
                "discounted_cash": fmt(cash),
                "min_negotiated": fmt(mn),
                "max_negotiated": fmt(mx),
                "payer_specific_rates": ";".join(payers),
                "source_url": url,
                "retrieved": datetime.date.today().isoformat(),
                "format": "cms_json",
            })
    return rows


def parse_transparentrx_json(data: bytes, wanted: set[str],
                              url: str) -> list[dict]:
    obj = json.loads(data.decode("utf-8", errors="replace"))
    items = (obj.get("PriceTransparency", {}).get("Items")
             or obj.get("Items") or [])
    rows: list[dict] = []
    for it in items:
        code = (it.get("ItemCode") or it.get("ProcedureCode")
                or it.get("Code") or it.get("CPTCode")
                or it.get("HCPCSCode") or "").strip().upper()
        if code not in wanted:
            continue
        gross = safe_float(it.get("GrossCharge") or it.get("ListPrice"))
        cash = safe_float(it.get("CashPrice") or it.get("DiscountedCash"))
        rates = it.get("Rates") or []
        payer_rates = []
        rate_values = []
        for r in rates:
            payer = r.get("Payer", "")
            val = safe_float(r.get("Rate"))
            if val is not None:
                rate_values.append(val)
                payer_rates.append(f"{payer}:{val:.2f}")
        mn = min(rate_values) if rate_values else None
        mx = max(rate_values) if rate_values else None
        rows.append({
            "cpt_code": code,
            "description": it.get("Description", ""),
            "gross_charge": fmt(gross),
            "discounted_cash": fmt(cash),
            "min_negotiated": fmt(mn),
            "max_negotiated": fmt(mx),
            "payer_specific_rates": ";".join(payer_rates),
            "source_url": url,
            "retrieved": datetime.date.today().isoformat(),
            "format": "transparentrx_json",
        })
    return rows


def parse_cms_csv(data: bytes, wanted: set[str],
                  url: str) -> list[dict]:
    text = data.decode("utf-8", errors="replace")
    reader = csv.DictReader(io.StringIO(text))
    rows: list[dict] = []
    for r in reader:
        code = ""
        for k in ("code|1", "code|2", "code|3"):
            if (r.get(k) or "").strip().upper() in wanted:
                code = (r.get(k) or "").strip().upper()
                break
        if not code:
            continue
        gross = safe_float(r.get("standard_charge|gross"))
        cash = safe_float(r.get("standard_charge|discounted_cash"))
        mn = safe_float(r.get("standard_charge|min"))
        mx = safe_float(r.get("standard_charge|max"))
        payer_rates = []
        for k, v in r.items():
            if (k and k.startswith("standard_charge|")
                    and k.endswith("|negotiated_dollar")):
                rate = safe_float(v)
                if rate is None:
                    continue
                middle = k[len("standard_charge|"):
                            -len("|negotiated_dollar")]
                payer_rates.append(f"{middle}:{rate:.2f}")
        rows.append({
            "cpt_code": code,
            "description": r.get("description", ""),
            "gross_charge": fmt(gross),
            "discounted_cash": fmt(cash),
            "min_negotiated": fmt(mn),
            "max_negotiated": fmt(mx),
            "payer_specific_rates": ";".join(payer_rates),
            "source_url": url,
            "retrieved": datetime.date.today().isoformat(),
            "format": "cms_csv",
        })
    return rows


def parse_turquoise_csv(data: bytes, wanted: set[str],
                        url: str) -> list[dict]:
    text = data.decode("utf-8", errors="replace")
    reader = csv.DictReader(io.StringIO(text))
    by_code: dict[str, dict] = {}
    for r in reader:
        code = (r.get("cpt_hcpcs_code") or r.get("cpt_code") or
                r.get("code") or "").strip().upper()
        if code not in wanted:
            continue
        gross = safe_float(r.get("gross_charge") or r.get("list_price"))
        cash = safe_float(r.get("cash_price") or r.get("discounted_cash"))
        rate = safe_float(r.get("negotiated_rate_outpatient")
                          or r.get("negotiated_rate_inpatient")
                          or r.get("negotiated_rate"))
        payer = r.get("payer_name") or r.get("payer", "")
        plan = r.get("plan_name") or r.get("plan", "")
        bucket = by_code.setdefault(code, {
            "cpt_code": code,
            "description": r.get("description", ""),
            "gross": [],
            "cash": [],
            "rates": [],
            "payer_rates": [],
        })
        if gross is not None:
            bucket["gross"].append(gross)
        if cash is not None:
            bucket["cash"].append(cash)
        if rate is not None:
            bucket["rates"].append(rate)
            bucket["payer_rates"].append(
                f"{payer}/{plan}:{rate:.2f}"
            )
    rows: list[dict] = []
    for b in by_code.values():
        rows.append({
            "cpt_code": b["cpt_code"],
            "description": b["description"],
            "gross_charge": fmt(max(b["gross"]) if b["gross"] else None),
            "discounted_cash": fmt(min(b["cash"]) if b["cash"] else None),
            "min_negotiated": fmt(min(b["rates"]) if b["rates"] else None),
            "max_negotiated": fmt(max(b["rates"]) if b["rates"] else None),
            "payer_specific_rates": ";".join(b["payer_rates"]),
            "source_url": url,
            "retrieved": datetime.date.today().isoformat(),
            "format": "turquoise_csv",
        })
    return rows


def parse_epic_csv(data: bytes, wanted: set[str],
                   url: str) -> list[dict]:
    text = data.decode("utf-8", errors="replace")
    reader = csv.DictReader(io.StringIO(text))
    rows: list[dict] = []
    for r in reader:
        code_type = (r.get("CODE_TYPE") or "").strip().upper()
        if code_type and code_type not in ("CPT", "HCPCS"):
            continue
        code = (r.get("BILLABLE_CODE") or "").strip().upper()
        if code not in wanted:
            continue
        gross = safe_float(r.get("LIST_PRICE"))
        cash = safe_float(r.get("CASH_PRICE"))
        mn = safe_float(r.get("MIN_NEGOTIATED"))
        mx = safe_float(r.get("MAX_NEGOTIATED"))
        payer_rates = []
        for k, v in r.items():
            if k and k.endswith("_RATE") and k not in (
                "MIN_NEGOTIATED", "MAX_NEGOTIATED",
            ):
                rate = safe_float(v)
                if rate is not None:
                    payer_rates.append(f"{k[:-5]}:{rate:.2f}")
        rows.append({
            "cpt_code": code,
            "description": r.get("DESCRIPTION", ""),
            "gross_charge": fmt(gross),
            "discounted_cash": fmt(cash),
            "min_negotiated": fmt(mn),
            "max_negotiated": fmt(mx),
            "payer_specific_rates": ";".join(payer_rates),
            "source_url": url,
            "retrieved": datetime.date.today().isoformat(),
            "format": "epic_csv",
        })
    return rows


PARSERS = {
    "cms_json": parse_cms_json,
    "cms_csv": parse_cms_csv,
    "turquoise_csv": parse_turquoise_csv,
    "transparentrx_json": parse_transparentrx_json,
    "epic_csv": parse_epic_csv,
}


SLUG_SAFE = re.compile(r"[^a-z0-9_]+")


def safe_slug(s: str) -> str:
    s = s.lower().strip()
    return SLUG_SAFE.sub("_", s).strip("_") or "hospital"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--url", required=True,
                    help="URL of the hospital's MRF.")
    ap.add_argument("--hospital-slug", required=True,
                    help="Short slug to identify the hospital "
                         "in the output filename.")
    ap.add_argument("--cpts", default="",
                    help="Comma-separated list of CPT/HCPCS codes "
                         "to look up.")
    ap.add_argument("--cpts-file", default="",
                    help="File with one CPT/HCPCS code per line.")
    args = ap.parse_args()

    codes: set[str] = set()
    if args.cpts:
        for c in args.cpts.split(","):
            c = c.strip().upper()
            if c:
                codes.add(c)
    if args.cpts_file:
        for ln in Path(args.cpts_file).read_text(
            encoding="utf-8"
        ).splitlines():
            ln = ln.strip().upper()
            if ln and not ln.startswith("#"):
                codes.add(ln)
    if not codes:
        sys.exit("[fatal] no CPT codes supplied via --cpts or --cpts-file")

    print(f"[fetch] {args.url}", flush=True)
    data = fetch_bytes(args.url)
    fmt_kind = detect_format(data)
    print(f"[format] detected: {fmt_kind} ({len(data)} bytes)",
          flush=True)
    if fmt_kind == "unknown":
        sys.exit(
            "[fatal] could not detect MRF format. See "
            "references/mrf_vendor_adapters.md for the four supported "
            "formats; inspect the file manually or open a PR adding a "
            "parser for its format."
        )

    parser = PARSERS[fmt_kind]
    rows = parser(data, codes, args.url)
    if not rows:
        print(f"[done] no rows matched the requested CPT(s); the file "
              f"may not include them, or the codes may use a different "
              f"format (e.g., CPT vs HCPCS).", flush=True)
        return 0

    MRF_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.date.today().strftime("%Y%m%d")
    slug = safe_slug(args.hospital_slug)
    out_path = MRF_DIR / f"mrf_{slug}_{stamp}.csv"
    with out_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=OUT_COLUMNS)
        w.writeheader()
        for row in rows:
            w.writerow({c: row.get(c, "") for c in OUT_COLUMNS})

    print(f"[done] {len(rows)} row(s) -> {out_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
