"""restructure_to_billers_eob.py — one-time migration that collapses
the current providers/<slug>/ tree (mixed bills + EOBs) into the new
two-track structure:

    Health_Bills/
      Billers/<biller_slug>/   -- bills, itemizations, collection notices
      EOB/<biller_slug>/       -- Explanation of Benefits documents only
      _archive_old_letters/    -- prior DISPUTE_LETTER.md drafts (the new
                                  state-machine drafts fresh ones)

Rules:
- A file is an EOB if its filename contains "_eob_" anywhere in the
  contents summary, OR the sidecar's classified document_type is
  "eob". All UHC explanation-of-benefits documents follow this naming
  convention from the classifier.
- A file is a bill if it isn't an EOB. Bills include actual provider
  statements, itemizations, collection notices, predeterminations,
  and "NOT A BILL" itemized chargemasters (which still document the
  bill's contents).
- DISPUTE_LETTER.md files in any provider folder get archived to
  Health_Bills/_archive_old_letters/<slug>/ — the state machine in
  draft_letters_by_state.py will draft fresh ones based on the new
  gating rules (must have both EOB and itemization).
- Sidecars (<file>.extracted.txt) follow their source file.

Usage:
    python restructure_to_billers_eob.py
    python restructure_to_billers_eob.py --dry-run
"""

from __future__ import annotations

import argparse
import csv
import datetime
import os
import re
import shutil
import sys
from pathlib import Path

# Default root for the Health_Bills tree. Override at runtime via:
#   --root <path>
# or environment variable HEALTHBILLS_ROOT, or just edit this constant
# on your own workstation. The default is intentionally a placeholder.
DEFAULT_ROOT = Path(
    os.environ.get("HEALTHBILLS_ROOT")
    or (Path.home() / "Health_Bills")
)
# Default location for generated audit logs. Override via --log-dir or
# HEALTHBILLS_LOG_DIR env var.
DEFAULT_LOG_DIR = Path(
    os.environ.get("HEALTHBILLS_LOG_DIR")
    or (Path.home() / ".medbill-dispute-kit" / "tracker")
)

SIDECAR_SUFFIX = ".extracted.txt"

EOB_FILENAME_RE = re.compile(r"_eob_", re.I)
DISPUTE_LETTER_RE = re.compile(r"^DISPUTE_LETTER\.md$", re.I)

# Globals reset in main() based on CLI args.
HEALTH_ROOT: Path = DEFAULT_ROOT
PROVIDERS_DIR: Path = HEALTH_ROOT / "providers"
BILLERS_DIR: Path = HEALTH_ROOT / "Billers"
EOB_DIR: Path = HEALTH_ROOT / "EOB"
ARCHIVE_LETTERS_DIR: Path = HEALTH_ROOT / "_archive_old_letters"
ARCHIVE_EMPTY_DIR: Path = HEALTH_ROOT / "_archive_empty_folders"
LOG_DIR: Path = DEFAULT_LOG_DIR


def relative(p: Path) -> str:
    try:
        return str(p.relative_to(HEALTH_ROOT))
    except ValueError:
        return str(p)


def is_eob_file(path: Path) -> bool:
    """A file is an EOB if (a) its filename was classified as an EOB by
    the upstream classifier (contains "_eob_" in the slug), OR (b) the
    extracted text explicitly identifies it as an Explanation of
    Benefits document from a health plan.

    Important: "THIS IS NOT A BILL" alone is NOT enough — hospital
    itemizations carry that label by law even though they are bill
    artifacts (the documented contents of a bill). The signal we need
    is the document's own title text identifying it as an EOB."""
    if EOB_FILENAME_RE.search(path.name):
        return True
    sc = path.with_name(path.name + SIDECAR_SUFFIX)
    if sc.exists():
        try:
            head = sc.read_text(encoding="utf-8", errors="replace")[:3000]
        except Exception:
            return False
        if re.search(r"explanation\s+of\s+benefits", head, re.I):
            return True
    return False


def is_dispute_letter(path: Path) -> bool:
    return bool(DISPUTE_LETTER_RE.match(path.name))


def unique_in(target_dir: Path, source_name: str) -> Path:
    target_dir.mkdir(parents=True, exist_ok=True)
    candidate = target_dir / source_name
    if not candidate.exists():
        return candidate
    stem, ext = Path(source_name).stem, Path(source_name).suffix
    m = re.search(r"^(.+)_v(\d+)$", stem)
    if m:
        base = m.group(1)
        n = int(m.group(2)) + 1
        while True:
            candidate = target_dir / f"{base}_v{n}{ext}"
            if not candidate.exists():
                return candidate
            n += 1
    n = 2
    while True:
        candidate = target_dir / f"{stem}_{n}{ext}"
        if not candidate.exists():
            return candidate
        n += 1


def move_pair(source: Path, dest: Path, dry_run: bool) -> tuple[Path, Path | None]:
    """Move source + its sidecar to dest. Returns (dest_path, dest_sidecar)."""
    sc_src = source.with_name(source.name + SIDECAR_SUFFIX)
    sc_dest = dest.with_name(dest.name + SIDECAR_SUFFIX) if sc_src.exists() else None
    if dry_run:
        return dest, sc_dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    source.rename(dest)
    if sc_src.exists():
        sc_src.rename(sc_dest)
    return dest, sc_dest


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=str(DEFAULT_ROOT),
                    help="Health_Bills tree root. Defaults to "
                         "$HEALTHBILLS_ROOT or ~/Health_Bills.")
    ap.add_argument("--log-dir", default=str(DEFAULT_LOG_DIR),
                    help="Where to write audit CSVs.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    global HEALTH_ROOT, PROVIDERS_DIR, BILLERS_DIR, EOB_DIR
    global ARCHIVE_LETTERS_DIR, ARCHIVE_EMPTY_DIR, LOG_DIR
    HEALTH_ROOT = Path(args.root)
    PROVIDERS_DIR = HEALTH_ROOT / "providers"
    BILLERS_DIR = HEALTH_ROOT / "Billers"
    EOB_DIR = HEALTH_ROOT / "EOB"
    ARCHIVE_LETTERS_DIR = HEALTH_ROOT / "_archive_old_letters"
    ARCHIVE_EMPTY_DIR = HEALTH_ROOT / "_archive_empty_folders"
    LOG_DIR = Path(args.log_dir)

    if not PROVIDERS_DIR.is_dir():
        print(f"[main] no providers/ dir at {PROVIDERS_DIR}; nothing to do",
              flush=True)
        return 0

    moves: list[dict] = []

    # Walk providers/<slug>/<files>
    for slug_dir in sorted(d for d in PROVIDERS_DIR.iterdir() if d.is_dir()):
        slug = slug_dir.name
        for f in sorted(slug_dir.iterdir()):
            if not f.is_file():
                continue
            # Skip sidecars; they get moved with their source.
            if f.name.endswith(SIDECAR_SUFFIX):
                continue

            if is_dispute_letter(f):
                target = unique_in(ARCHIVE_LETTERS_DIR / slug, f.name)
                action = "archive_old_letter"
            elif is_eob_file(f):
                target = unique_in(EOB_DIR / slug, f.name)
                action = "eob"
            else:
                target = unique_in(BILLERS_DIR / slug, f.name)
                action = "bill"

            dest, sc_dest = move_pair(f, target, args.dry_run)
            moves.append({
                "action": action,
                "source_slug": slug,
                "source": relative(f),
                "destination": relative(dest),
                "sidecar_destination": relative(sc_dest) if sc_dest else "",
                "dry_run": str(args.dry_run),
            })
            print(f"[{action}] {relative(f)}  ->  {relative(dest)}",
                  flush=True)

    # Remove now-empty providers/ folders
    if not args.dry_run and PROVIDERS_DIR.is_dir():
        for d in sorted(PROVIDERS_DIR.iterdir()):
            if d.is_dir() and not any(d.iterdir()):
                try:
                    d.rmdir()
                    print(f"[rmdir] providers/{d.name}/", flush=True)
                except OSError:
                    pass
        # Move any non-empty leftover providers/* into _archive_empty_folders/
        for d in sorted(PROVIDERS_DIR.iterdir() if PROVIDERS_DIR.is_dir() else []):
            if d.is_dir():
                target = ARCHIVE_EMPTY_DIR / d.name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(d), str(target))
                print(f"[archive_residual] providers/{d.name}/ -> "
                      f"_archive_empty_folders/", flush=True)
        # Remove providers/ itself if empty
        try:
            PROVIDERS_DIR.rmdir()
            print(f"[rmdir] providers/  (empty)", flush=True)
        except OSError:
            pass

    # Write audit log
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_csv = LOG_DIR / f"restructure_audit_{ts}.csv"
    with log_csv.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["action", "source_slug", "source", "destination",
                        "sidecar_destination", "dry_run"],
            extrasaction="ignore",
        )
        w.writeheader()
        for r in moves:
            w.writerow(r)

    by_action: dict[str, int] = {}
    for r in moves:
        by_action[r["action"]] = by_action.get(r["action"], 0) + 1
    print("\n[summary]", flush=True)
    for a, n in sorted(by_action.items()):
        print(f"  {a:24s}  {n}", flush=True)
    print(f"\n[main] log: {log_csv}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
