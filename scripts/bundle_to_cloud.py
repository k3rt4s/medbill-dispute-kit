"""bundle_to_cloud.py — push evidence bundles to an encrypted offsite
destination via rclone.

Marshall Allen's discipline: every paper trail needs an offsite copy.
A house fire, a hard-drive failure, or a compromised laptop must not
destroy the months of certified-mail receipts, drafted letters, and
benchmark analyses that prove your case.

This script is a thin wrapper around rclone. rclone supports 70+
storage backends (Backblaze B2, Wasabi, S3, Google Drive, OneDrive,
SFTP, Mega, Box, etc.) and includes client-side encryption via its
"crypt" backend. The kit does not bundle credentials or assume a
backend; the user configures rclone once with `rclone config` and
sets the remote name + path via env vars below.

Required env vars:

    HEALTHBILLS_CLOUD_REMOTE   rclone remote name, e.g. "b2crypt"
    HEALTHBILLS_CLOUD_PATH     destination path, e.g.
                               "medbill_disputes/_bundles"

The destination becomes `<remote>:<path>`. rclone will create the path
on first run.

Usage:
    python bundle_to_cloud.py                       # push every bundle
    python bundle_to_cloud.py --bundle B-abc12345_20260521.zip
    python bundle_to_cloud.py --since 2026-05-01    # only newer bundles
    python bundle_to_cloud.py --dry-run

This script does not delete local bundles. To prune local copies after
a successful push, use rclone's own retention features or a separate
cleanup script.
"""

from __future__ import annotations

import argparse
import datetime
import os
import shutil
import subprocess
import sys
from pathlib import Path

HEALTH_ROOT = Path(
    os.environ.get("HEALTHBILLS_ROOT")
    or (Path.home() / "Health_Bills")
)
BUNDLES_DIR = HEALTH_ROOT / "_bundles"


def find_rclone() -> str:
    """Return path to rclone executable or exit with installation note."""
    found = shutil.which("rclone") or shutil.which("rclone.exe")
    if not found:
        sys.exit(
            "[fatal] rclone not found on PATH. Install from "
            "rclone.org/downloads, then run `rclone config` to set up "
            "an encrypted remote. See "
            "rclone.org/crypt for the crypt-backend walkthrough."
        )
    return found


def parse_iso_date(s: str) -> datetime.date | None:
    try:
        return datetime.date.fromisoformat(s)
    except ValueError:
        return None


def bundle_date(name: str) -> datetime.date | None:
    """Extract the YYYYMMDD stamp from a bundle filename
    'B-xxx_YYYYMMDD.zip'."""
    stem = name.split(".")[0]
    if "_" not in stem:
        return None
    stamp = stem.rsplit("_", 1)[1]
    if len(stamp) != 8 or not stamp.isdigit():
        return None
    try:
        return datetime.date(int(stamp[:4]),
                             int(stamp[4:6]),
                             int(stamp[6:]))
    except ValueError:
        return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--bundle",
                    help="Only push this specific bundle filename.")
    ap.add_argument("--since",
                    help="ISO date; only push bundles dated >= this.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print what would be pushed; do not call rclone.")
    args = ap.parse_args()

    remote = os.environ.get("HEALTHBILLS_CLOUD_REMOTE")
    path = os.environ.get("HEALTHBILLS_CLOUD_PATH")
    if not remote or not path:
        sys.exit(
            "[fatal] set HEALTHBILLS_CLOUD_REMOTE (rclone remote name) "
            "and HEALTHBILLS_CLOUD_PATH (destination path) env vars. "
            "Run `rclone config` first if you have not configured a "
            "remote yet."
        )
    dest = f"{remote}:{path.strip('/')}"

    if not BUNDLES_DIR.is_dir():
        sys.exit(
            f"[fatal] no bundles directory at {BUNDLES_DIR}. Run "
            f"scripts/bundle_evidence.py first to produce bundles."
        )

    rclone = find_rclone()

    since: datetime.date | None = None
    if args.since:
        since = parse_iso_date(args.since)
        if since is None:
            sys.exit(f"[fatal] invalid --since date: {args.since}")

    targets: list[Path] = []
    for p in sorted(BUNDLES_DIR.glob("*.zip")):
        if args.bundle and p.name != args.bundle:
            continue
        if since:
            bd = bundle_date(p.name)
            if bd is None or bd < since:
                continue
        targets.append(p)

    if not targets:
        print("[done] nothing to push", flush=True)
        return 0

    for t in targets:
        rel = t.relative_to(HEALTH_ROOT)
        cmd = [
            rclone, "copy", str(t), dest,
            "--progress",
            "--immutable",  # never overwrite existing remote files
        ]
        if args.dry_run:
            print(f"[would push] {rel} -> {dest}/{t.name}", flush=True)
            continue
        print(f"[push] {rel} -> {dest}/{t.name}", flush=True)
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as exc:
            print(f"[error] rclone failed for {t.name}: {exc}",
                  flush=True)
            return 1

    if args.dry_run:
        print(f"[dry-run] {len(targets)} bundle(s) would be pushed",
              flush=True)
    else:
        print(f"[done] {len(targets)} bundle(s) pushed", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
