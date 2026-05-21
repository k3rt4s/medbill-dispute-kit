"""bundle_evidence.py — zip the complete artifact set for each dispute
group into one archive for offsite backup or court exhibit packaging.

Marshall Allen's discipline: never go to a phone call, a complaint
filing, or a court date without the full evidence packet. This script
walks tracker.csv, picks the canonical bill per dispute group, and
produces `<HEALTHBILLS_ROOT>/_bundles/<bill_id>_<YYYYMMDD>.zip` with:

  - The original bill PDF and its sidecar
  - The matched EOB PDF(s) and their sidecars
  - Every drafted letter for the group (request_eob, request_itemization,
    counter_offer, dispute, doi_complaint, small_claims_civil_warrant)
  - The benchmark CSV row for the bill, if available
  - The audit CSV rows for the bill, if available
  - The action log filtered to this bill_id, if available
  - A MANIFEST.md describing what's in the bundle and what's missing

The bundle is timestamped per run so you can re-bundle later and keep
the earlier snapshot. The script never deletes prior bundles.

Usage:
    python bundle_evidence.py                       # bundle every group
    python bundle_evidence.py --bill-id B-abc12345
    python bundle_evidence.py --slug a_specific_biller
"""

from __future__ import annotations

import argparse
import csv
import datetime
import os
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

HEALTH_ROOT = Path(
    os.environ.get("HEALTHBILLS_ROOT")
    or (Path.home() / "Health_Bills")
)
BILLERS_DIR = HEALTH_ROOT / "Billers"
EOB_DIR = HEALTH_ROOT / "EOB"
BUNDLES_DIR = HEALTH_ROOT / "_bundles"
SIDECAR_SUFFIX = ".extracted.txt"

LOG_DIR = Path(
    os.environ.get("HEALTHBILLS_LOG_DIR")
    or (Path.home() / ".medbill-dispute-kit" / "tracker")
)
TRACKER_CSV = LOG_DIR / "tracker.csv"
ACTIONS_CSV = LOG_DIR / "actions.csv"
MATCHES_CSV = LOG_DIR / "matches.csv"

LETTER_KIND_SUFFIXES = [
    "_LETTER_REQUEST_EOB.md",
    "_LETTER_REQUEST_ITEMIZATION.md",
    "_LETTER_COUNTER_OFFER.md",
    "_DISPUTE_LETTER.md",
    "_COMPLAINT_DOI.md",
    "_SMALL_CLAIMS_CIVIL_WARRANT.md",
]


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def matched_eob_files(bill_slug: str, bill_file: str,
                       matches: list[dict]) -> list[Path]:
    files: list[Path] = []
    for m in matches:
        if m.get("bill_slug") != bill_slug:
            continue
        if m.get("bill_file") != bill_file:
            continue
        eob_file = (m.get("eob_file") or "").strip()
        if not eob_file:
            continue
        candidate = EOB_DIR / bill_slug / eob_file
        if candidate.exists():
            files.append(candidate)
    return files


def add_if_exists(zf: zipfile.ZipFile, src: Path, arcname: str,
                  manifest: list[str], missing: list[str]) -> None:
    if src.exists():
        zf.write(src, arcname=arcname)
        manifest.append(f"- INCLUDED: {arcname}")
    else:
        missing.append(f"- MISSING: {arcname}  ({src})")


def write_filtered_csv(zf: zipfile.ZipFile, src: Path, arcname: str,
                       filter_fn) -> int:
    """Write rows from src CSV into the zip filtered by filter_fn(row)."""
    if not src.exists():
        return 0
    rows = [r for r in read_csv(src) if filter_fn(r)]
    if not rows:
        return 0
    fieldnames = list(rows[0].keys())
    import io
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fieldnames)
    w.writeheader()
    for r in rows:
        w.writerow(r)
    zf.writestr(arcname, buf.getvalue())
    return len(rows)


def bundle_one(canonical: dict, members: list[dict],
                matches: list[dict], stamp: str) -> Path | None:
    bill_id = canonical.get("bill_id", "")
    slug = canonical.get("biller_slug", "")
    bill_file = canonical.get("file", "")
    if not bill_id or not slug or not bill_file:
        return None
    bills_folder = BILLERS_DIR / slug
    bundle_path = BUNDLES_DIR / f"{bill_id}_{stamp}.zip"
    BUNDLES_DIR.mkdir(parents=True, exist_ok=True)

    manifest: list[str] = []
    missing: list[str] = []

    with zipfile.ZipFile(bundle_path, "w",
                         compression=zipfile.ZIP_DEFLATED) as zf:
        # Bill artifacts
        bill_src = bills_folder / bill_file
        add_if_exists(zf, bill_src, f"bill/{bill_file}",
                      manifest, missing)
        add_if_exists(zf, bills_folder / (bill_file + SIDECAR_SUFFIX),
                      f"bill/{bill_file}{SIDECAR_SUFFIX}",
                      manifest, missing)

        # Superseded bills in the same group
        for r in members:
            if r["bill_id"] == bill_id:
                continue
            other_file = r.get("file", "")
            if not other_file:
                continue
            other_src = bills_folder / other_file
            add_if_exists(zf, other_src,
                          f"superseded_bills/{other_file}",
                          manifest, missing)
            add_if_exists(zf, bills_folder /
                          (other_file + SIDECAR_SUFFIX),
                          f"superseded_bills/"
                          f"{other_file}{SIDECAR_SUFFIX}",
                          manifest, missing)

        # EOBs matched to this bill
        eobs = matched_eob_files(slug, bill_file, matches)
        for eob in eobs:
            add_if_exists(zf, eob, f"eob/{eob.name}",
                          manifest, missing)
            add_if_exists(zf, eob.parent / (eob.name + SIDECAR_SUFFIX),
                          f"eob/{eob.name}{SIDECAR_SUFFIX}",
                          manifest, missing)

        # All drafted letters for this bill
        for suffix in LETTER_KIND_SUFFIXES:
            letter = bills_folder / f"{bill_id}{suffix}"
            if letter.exists():
                add_if_exists(zf, letter, f"letters/{letter.name}",
                              manifest, missing)

        # Per-folder benchmark and audit CSVs filtered to this bill
        n_bench = write_filtered_csv(
            zf, bills_folder / "_benchmarks.csv",
            "evidence/benchmarks.csv",
            lambda r: r.get("bill_file") == bill_file,
        )
        if n_bench:
            manifest.append(f"- INCLUDED: evidence/benchmarks.csv "
                            f"({n_bench} rows)")
        n_audit = write_filtered_csv(
            zf, bills_folder / "_audit.csv",
            "evidence/audit.csv",
            lambda r: r.get("bill_file") == bill_file,
        )
        if n_audit:
            manifest.append(f"- INCLUDED: evidence/audit.csv "
                            f"({n_audit} rows)")

        # Action log filtered to this bill_id
        n_actions = write_filtered_csv(
            zf, ACTIONS_CSV, "evidence/actions.csv",
            lambda r: r.get("bill_id") == bill_id,
        )
        if n_actions:
            manifest.append(f"- INCLUDED: evidence/actions.csv "
                            f"({n_actions} rows)")

        # Tracker row(s) for this dispute group
        tracker_rows = [r for r in members]
        if tracker_rows:
            import io
            buf = io.StringIO()
            w = csv.DictWriter(
                buf,
                fieldnames=list(tracker_rows[0].keys()),
            )
            w.writeheader()
            for r in tracker_rows:
                w.writerow(r)
            zf.writestr("evidence/tracker_rows.csv", buf.getvalue())
            manifest.append(
                f"- INCLUDED: evidence/tracker_rows.csv "
                f"({len(tracker_rows)} rows in this dispute group)"
            )

        # Manifest
        manifest_text = "\n".join([
            f"# Evidence bundle for {bill_id}",
            f"",
            f"Generated: {stamp}",
            f"Biller slug: {slug}",
            f"Canonical bill file: {bill_file}",
            f"Statement date: {canonical.get('statement_date', '')}",
            f"DOS: {canonical.get('dos_start', '')} -> "
            f"{canonical.get('dos_end', '')}",
            f"Current balance: ${canonical.get('current_balance', '')}",
            f"Status: {canonical.get('status', '')}",
            f"Next action: {canonical.get('next_action', '')}",
            "",
            "## Contents",
            "",
            *manifest,
            "",
        ] + (["## Missing artifacts", ""] + missing
             if missing else []))
        zf.writestr("MANIFEST.md", manifest_text)

    return bundle_path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--bill-id",
                    help="Only bundle this bill_id (canonical row).")
    ap.add_argument("--slug",
                    help="Only bundle dispute groups for this slug.")
    args = ap.parse_args()

    tracker_rows = read_csv(TRACKER_CSV)
    if not tracker_rows:
        print(f"[fatal] no tracker.csv at {TRACKER_CSV}", flush=True)
        return 1
    matches = read_csv(MATCHES_CSV)

    # Group by (slug, account_number) following draft_letters_by_state's
    # convention; superseded rows are bundled together with canonical.
    groups: dict[tuple, list[dict]] = defaultdict(list)
    for row in tracker_rows:
        slug = row.get("biller_slug", "")
        acct = (row.get("account_number") or "").strip()
        if acct:
            key = (slug, f"acct:{acct}")
        else:
            dos = (row.get("dos_start") or "").strip()
            if dos:
                key = (slug, f"dos:{dos}")
            else:
                key = (slug, f"file:{row.get('file', '')}")
        groups[key].append(row)

    stamp = datetime.date.today().strftime("%Y%m%d")
    n_bundles = 0
    for key, members in groups.items():
        if args.slug and key[0] != args.slug:
            continue
        # Pick canonical: the first non-superseded row, or the first row.
        canon = next((r for r in members
                      if r.get("status") != "superseded"), members[0])
        if args.bill_id and canon.get("bill_id") != args.bill_id:
            continue
        path = bundle_one(canon, members, matches, stamp)
        if path:
            print(f"[bundled] {canon.get('bill_id')} -> "
                  f"{path.relative_to(HEALTH_ROOT)}", flush=True)
            n_bundles += 1

    print(f"[done] {n_bundles} bundle(s) in "
          f"{BUNDLES_DIR.relative_to(HEALTH_ROOT)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
