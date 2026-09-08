"""fixture_tools.py, write synthetic bill documents under an explicit data root."""
from __future__ import annotations

import json
import textwrap
from pathlib import Path

import pymupdf

BANNER = (
    "SYNTHETIC SAMPLE, NOT A REAL BILL. Generated for regression testing. "
    "All names, numbers and addresses are fictional."
)
DEFAULT_OUTPUT = Path("C:/Code_data/medbill-dispute-kit/examples/sample_bills")


def write_pdf(path: Path, body: str) -> None:
    """Create a readable text-layer PDF from the synthetic source rendering."""
    doc = pymupdf.open()
    page = doc.new_page(width=612, height=792)
    y = 42.0
    for original in body.splitlines():
        lines = textwrap.wrap(original, width=88, replace_whitespace=False) or [""]
        for line in lines:
            if y > 746:
                page = doc.new_page(width=612, height=792)
                y = 42.0
            page.insert_text((38, y), line, fontname="cour", fontsize=10)
            y += 14
    doc.set_metadata({"title": "Synthetic regression fixture", "subject": BANNER})
    doc.save(path)
    doc.close()


def write_case(
    output: Path,
    case_name: str,
    title: str,
    bills: list[dict],
    tracker_rows: list[dict],
    documents: dict[str, str],
    explanation: str,
) -> Path:
    """Write one case; bill and tracker envelopes keep their vocabularies separate."""
    target = output.resolve() / case_name
    repo = Path(__file__).resolve().parents[2]
    if target.is_relative_to(repo):
        raise ValueError("Generated fixtures must be outside the repository")
    target.mkdir(parents=True, exist_ok=True)
    for stem, body in documents.items():
        content = BANNER + "\n\n" + body.strip() + "\n"
        (target / f"{stem}.md").write_text(content, encoding="utf-8")
        write_pdf(target / f"{stem}.pdf", content)
    expected = {"notes": BANNER, "bills": bills, "tracker_rows": tracker_rows}
    (target / "expected.json").write_text(
        json.dumps(expected, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
    )
    files = ["expected.json"] + [f"{stem}.{ext}" for stem in documents for ext in ("md", "pdf")]
    readme = BANNER + f"\n\n# {title}\n\n{explanation}\n\nFiles:\n\n"
    readme += "\n".join(f"- `{name}`" for name in files) + "\n"
    (target / "README.md").write_text(readme, encoding="utf-8")
    return target
