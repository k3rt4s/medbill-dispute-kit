"""analyze_self_pay_election.py — compare insured-billing vs self-pay
election for a given encounter and recommend the cheaper path.

The federal No Surprises Act at 45 CFR § 149.610(c)(3) lets a patient
elect self-pay even when insured. Self-pay then qualifies the patient
for the federal GFE / PPDR framework and decouples the bill from
plan-vs-provider dynamics. But self-pay also means losing the plan's
allowed-amount ceiling and any progress against the deductible.

Marshall Allen's argument is that for many patients with high
deductibles, mid-priced shoppable services, and access to charity
care, the self-pay path costs less than the insurance path. This
script makes that comparison concrete per bill, using the bill's CPT
codes, the Medicare benchmark, the hospital's MRF cash price (if
fetched), the patient's plan summary from the SPD profile (if
parsed), and the FAP eligibility threshold.

Output: `<HEALTHBILLS_ROOT>/_self_pay_analyses/<bill_id>.json` plus a
human-readable summary printed to stdout.

Usage:
   python analyze_self_pay_election.py --bill-id B-abc1234567
   python analyze_self_pay_election.py --slug a_specific_biller
   python analyze_self_pay_election.py  # analyze every bill
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from pathlib import Path

HEALTH_ROOT = Path(
    os.environ.get("HEALTHBILLS_ROOT")
    or (Path.home() / "Health_Bills")
)
BILLERS_DIR = HEALTH_ROOT / "Billers"
ANALYSES_DIR = HEALTH_ROOT / "_self_pay_analyses"
MRF_DIR = HEALTH_ROOT / "_mrf_lookups"
SPD_DIR = HEALTH_ROOT / "_spd_profiles"

LOG_DIR = Path(
    os.environ.get("HEALTHBILLS_LOG_DIR")
    or (Path.home() / ".medbill-dispute-kit" / "tracker")
)
TRACKER_CSV = LOG_DIR / "tracker.csv"

# Federal poverty level for a household of 1 in CY2025. The drafter
# scales by household size below. Treasury Reg. § 1.501(r)-5 thresholds
# typically reference percentages of FPL.
FPL_HOUSEHOLD_1_2025 = 15060.00
FPL_ADDL_PERSON_2025 = 5380.00

# Default counter-offer anchor (200% of Medicare). Patient can override
# via HEALTHBILLS_COUNTER_OFFER_MULTIPLIER env var.
COUNTER_OFFER_MULTIPLIER = float(
    os.environ.get("HEALTHBILLS_COUNTER_OFFER_MULTIPLIER") or 2.0
)


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def fpl_for_household(size: int) -> float:
    if size < 1:
        return FPL_HOUSEHOLD_1_2025
    return FPL_HOUSEHOLD_1_2025 + max(0, size - 1) * FPL_ADDL_PERSON_2025


def safe_float(v) -> float | None:
    if v in (None, ""):
        return None
    try:
        return float(str(v).replace(",", "").replace("$", "").strip())
    except (TypeError, ValueError):
        return None


def load_benchmarks_for_bill(slug: str, bill_file: str) -> list[dict]:
    bench = BILLERS_DIR / slug / "_benchmarks.csv"
    if not bench.exists():
        return []
    return [r for r in read_csv(bench)
            if r.get("bill_file") == bill_file]


def load_latest_spd_profile() -> dict:
    if not SPD_DIR.is_dir():
        return {}
    candidates = sorted(SPD_DIR.glob("*.json"),
                         key=lambda p: p.stat().st_mtime)
    if not candidates:
        return {}
    try:
        return json.loads(candidates[-1].read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def insurance_path_cost(canonical: dict,
                        spd: dict) -> tuple[float, str]:
    """Estimate patient cost under the insurance path.

    Best-case: in-network, patient already met deductible -> only the
    coinsurance + copay applies up to OOP max.

    Conservative case (what the kit uses by default): patient has not
    met deductible. Patient pays the full bill up to the in-network
    deductible, then coinsurance up to OOP max."""
    bill_total = safe_float(canonical.get("current_balance")) or 0.0
    if bill_total <= 0:
        return 0.0, "balance is zero or unknown"

    deductible = safe_float(spd.get("in_network_deductible_individual"))
    oop_max = safe_float(spd.get("in_network_oop_max_individual"))

    if deductible is None and oop_max is None:
        # No plan data on file; assume the bill is roughly what
        # the patient owes after the EOB applied in-network rates.
        return bill_total, (
            "no SPD profile on file; using current_balance as the "
            "insured-path proxy. Parse the SPD via scripts/parse_spd.py "
            "for a precise estimate."
        )

    # Apply deductible: assume the patient has not met it yet, which
    # is conservative.
    paid_toward_deductible = min(bill_total, deductible or 0.0)
    after_deductible = bill_total - paid_toward_deductible
    # Assume 20% coinsurance after deductible (the most common plan
    # design). The patient can override via tracker.csv `notes`.
    coinsurance = after_deductible * 0.20
    patient_pays = paid_toward_deductible + coinsurance
    if oop_max is not None:
        patient_pays = min(patient_pays, oop_max)
    return patient_pays, (
        f"in-network deductible ${deductible:.2f}, assume 20% "
        f"coinsurance after, capped at OOP max ${oop_max or 0:.2f}"
    )


def self_pay_path_cost(benchmark_rows: list[dict],
                       mrf_rows: list[dict],
                       canonical: dict,
                       fap_eligible: bool) -> tuple[float, str]:
    """Estimate patient cost under self-pay election.

    Anchor preference: lowest of (FAP-eligible AGB / hospital's
    published cash price / 200% Medicare allowable). Each anchor only
    applies when supporting data is present."""
    bill_total = safe_float(canonical.get("current_balance")) or 0.0

    # 200% Medicare sum across the benchmark rows
    medicare_sum = sum(
        (safe_float(r.get("medicare_national")) or 0.0)
        for r in benchmark_rows
    )
    medicare_anchor = medicare_sum * COUNTER_OFFER_MULTIPLIER
    medicare_codes = sum(
        1 for r in benchmark_rows
        if (safe_float(r.get("medicare_national")) or 0) > 0
    )
    medicare_basis = (
        f"{COUNTER_OFFER_MULTIPLIER:.1f}x Medicare across "
        f"{medicare_codes} codes"
    ) if medicare_codes > 0 else "(no Medicare data)"

    # Hospital cash price from MRF, if present
    mrf_by_code = {r.get("cpt_code"): r for r in mrf_rows}
    cash_total = 0.0
    cash_codes = 0
    for r in benchmark_rows:
        cpt = r.get("cpt_code")
        mrf_row = mrf_by_code.get(cpt)
        if mrf_row:
            cash = safe_float(mrf_row.get("discounted_cash"))
            if cash is not None:
                cash_total += cash
                cash_codes += 1
    cash_anchor = cash_total if cash_codes > 0 else None
    cash_basis = (
        f"hospital published cash price across {cash_codes} codes"
    ) if cash_anchor is not None else "(no MRF data)"

    # FAP: if FAP-eligible, the AGB (Amounts Generally Billed) cap
    # applies. Conservative estimate: 60% of bill_total when FAP-
    # eligible, since AGB varies by hospital but is typically 40-70%
    # of chargemaster. The kit does not bundle hospital-specific AGB.
    fap_anchor = bill_total * 0.60 if fap_eligible else None
    fap_basis = "AGB cap ~60% of bill (estimated)" if fap_eligible else None

    candidates: list[tuple[float, str]] = []
    if medicare_anchor > 0:
        candidates.append((medicare_anchor, medicare_basis))
    if cash_anchor is not None:
        candidates.append((cash_anchor, cash_basis))
    if fap_anchor is not None:
        candidates.append((fap_anchor, fap_basis))

    if not candidates:
        return bill_total, (
            "no benchmark, MRF, or FAP data available; self-pay path "
            "defaults to the full bill. Run fetch_price_benchmarks.py "
            "and/or fetch_mrf.py, or set --fap-eligible to refine."
        )
    # Pick the lowest anchor (most patient-favorable)
    candidates.sort(key=lambda t: t[0])
    return candidates[0]


def analyze_bill(canonical: dict, spd: dict,
                 fap_eligible: bool) -> dict:
    slug = canonical.get("biller_slug", "")
    bill_file = canonical.get("file", "")
    benchmarks = load_benchmarks_for_bill(slug, bill_file)

    mrf_rows: list[dict] = []
    if MRF_DIR.is_dir():
        # Best-effort: read every MRF lookup CSV; merging across
        # multiple hospitals would be unusual but safe.
        for mrf_csv in MRF_DIR.glob("mrf_*.csv"):
            mrf_rows.extend(read_csv(mrf_csv))

    insurance_cost, insurance_basis = insurance_path_cost(canonical, spd)
    self_pay_cost, self_pay_basis = self_pay_path_cost(
        benchmarks, mrf_rows, canonical, fap_eligible,
    )
    saving = insurance_cost - self_pay_cost
    recommendation = (
        "self-pay (cheaper)" if self_pay_cost < insurance_cost
        else "insurance (cheaper or unclear)"
    )
    if abs(saving) < 25.0:
        recommendation = "neutral (within $25)"

    return {
        "bill_id": canonical.get("bill_id", ""),
        "biller_slug": slug,
        "file": bill_file,
        "current_balance": canonical.get("current_balance", ""),
        "spd_profile_loaded": bool(spd),
        "fap_eligible_input": fap_eligible,
        "insurance_path_estimated_cost": f"{insurance_cost:.2f}",
        "insurance_path_basis": insurance_basis,
        "self_pay_path_estimated_cost": f"{self_pay_cost:.2f}",
        "self_pay_path_basis": self_pay_basis,
        "estimated_saving_self_pay_vs_insurance": f"{saving:.2f}",
        "recommendation": recommendation,
        "caveats": [
            "This is an estimate. The actual outcome depends on plan "
            "language, FAP screening, and provider negotiation.",
            "Self-pay election under NSA § 149.610(c)(3) requires the "
            "patient to be unambiguous with the provider that the "
            "claim is not being submitted to insurance.",
            "Self-pay loses progress toward the in-network deductible "
            "and OOP max. If multiple bills are expected in the same "
            "plan year, factor that loss in.",
            "The kit's FAP anchor uses a 60% AGB estimate. Real AGB "
            "varies; pull the hospital's published AGB from its FAP "
            "before relying on the FAP anchor.",
        ],
    }


def print_summary(report: dict) -> None:
    print()
    print(f"--- Bill {report['bill_id']} ({report['biller_slug']}) ---")
    print(f"  Current balance:      ${report['current_balance']}")
    print(f"  Insurance-path est:   ${report['insurance_path_estimated_cost']}")
    print(f"    basis: {report['insurance_path_basis']}")
    print(f"  Self-pay-path est:    ${report['self_pay_path_estimated_cost']}")
    print(f"    basis: {report['self_pay_path_basis']}")
    print(f"  Saving (self-pay -):  ${report['estimated_saving_self_pay_vs_insurance']}")
    print(f"  Recommendation:       {report['recommendation']}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--bill-id", help="Only analyze this bill_id.")
    ap.add_argument("--slug", help="Only analyze bills in this slug.")
    ap.add_argument("--fap-eligible", action="store_true",
                    help="Apply the FAP / AGB-eligibility anchor "
                         "(treats patient as FAP-eligible).")
    ap.add_argument("--household-size", type=int, default=0,
                    help="If supplied with --household-income, the "
                         "script computes FPL eligibility instead of "
                         "requiring --fap-eligible.")
    ap.add_argument("--household-income", type=float, default=0.0,
                    help="Annual gross income, USD.")
    ap.add_argument("--fap-fpl-threshold", type=float, default=200.0,
                    help="Hospital's FAP cutoff as a percentage of "
                         "FPL (default 200, common range 100-400).")
    args = ap.parse_args()

    tracker_rows = read_csv(TRACKER_CSV)
    if not tracker_rows:
        sys.exit(f"[fatal] no tracker.csv at {TRACKER_CSV}")

    spd = load_latest_spd_profile()
    if not spd:
        print("[info] no SPD profile in _spd_profiles/; insurance-path "
              "estimate will be conservative", flush=True)

    fap_eligible = args.fap_eligible
    if args.household_size > 0 and args.household_income > 0:
        fpl = fpl_for_household(args.household_size)
        ratio = args.household_income / fpl * 100
        fap_eligible = ratio <= args.fap_fpl_threshold
        print(f"[info] household income {args.household_income:.0f} / "
              f"FPL {fpl:.0f} = {ratio:.0f}% of FPL; FAP threshold "
              f"{args.fap_fpl_threshold:.0f}%; eligible: {fap_eligible}",
              flush=True)

    ANALYSES_DIR.mkdir(parents=True, exist_ok=True)
    n_analyzed = 0
    for row in tracker_rows:
        if args.bill_id and row.get("bill_id") != args.bill_id:
            continue
        if args.slug and row.get("biller_slug") != args.slug:
            continue
        if row.get("status") in ("superseded", "closed", "settled"):
            continue
        report = analyze_bill(row, spd, fap_eligible)
        out_path = ANALYSES_DIR / f"{report['bill_id']}.json"
        out_path.write_text(
            json.dumps(report, indent=2, sort_keys=True),
            encoding="utf-8",
        )
        print_summary(report)
        n_analyzed += 1

    print(f"\n[done] {n_analyzed} bill(s) analyzed -> {ANALYSES_DIR}",
          flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
