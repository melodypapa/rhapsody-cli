"""Committed pywin32 authority snapshot and documented binding exceptions."""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, TypedDict

if __package__ in (None, ""):  # running as `python scripts/pywin32_authority.py`
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
AUTHORITY_PATH = REPOSITORY_ROOT / "docs" / "reports" / "pywin32_authority.json"
_REPORT_SUFFIX = "_api_report.md"


class AuthorityData(TypedDict):
    catalog: Dict[str, Dict[str, str]]
    documented_aliases: Dict[str, Dict[str, str]]
    documented_unavailable: Dict[str, List[str]]


def export_catalog_from_reports(reports_dir: Path) -> Dict[str, Dict[str, str]]:
    """Read the pywin32 column of generated reports into an offline catalog."""
    catalog: Dict[str, Dict[str, str]] = {}
    for report_path in sorted(reports_dir.rglob("*" + _REPORT_SUFFIX)):
        interface_name = report_path.name[: -len(_REPORT_SUFFIX)]
        members: Dict[str, str] = {}
        for line in report_path.read_text(encoding="utf-8").splitlines():
            if not line.startswith("| ") or line.startswith("| Python model wrapper") or line.startswith("| ---"):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) < 5:
                continue
            for entry in cells[2].split("; "):
                if entry == "—":
                    continue
                name, separator, kind_with_paren = entry.rpartition(" (")
                if not separator or not kind_with_paren.endswith(")"):
                    continue
                members[name] = kind_with_paren[:-1]
        catalog[interface_name] = members
    return catalog


def build_authority(reports_dir: Path) -> AuthorityData:
    """Build a fresh authority file with no documented exceptions yet."""
    return AuthorityData(
        catalog=export_catalog_from_reports(reports_dir),
        documented_aliases={},
        documented_unavailable={},
    )


def build_authority_from_typelib(reports_dir: Path) -> AuthorityData:
    """Build a complete snapshot from the registered Rhapsody type library.

    Validation reports list only deviations, so exporting their pywin32 column
    yields an incomplete catalog. The registered type library is the
    authoritative source when it is available.
    """
    from scripts.validate_model_api import collect_registered_pywin32_members

    catalog: Dict[str, Dict[str, str]] = {}
    for report_path in sorted(reports_dir.rglob("*" + _REPORT_SUFFIX)):
        interface_name = report_path.name[: -len(_REPORT_SUFFIX)]
        catalog[interface_name] = collect_registered_pywin32_members(interface_name)
    return AuthorityData(catalog=catalog, documented_aliases={}, documented_unavailable={})


def load_authority(path: Path = AUTHORITY_PATH) -> AuthorityData:
    """Load the committed authority snapshot."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Could not load pywin32 authority from {path}: {exc}") from exc
    return AuthorityData(
        catalog=data["catalog"],
        documented_aliases=data["documented_aliases"],
        documented_unavailable=data["documented_unavailable"],
    )


def write_authority(data: AuthorityData, path: Path) -> None:
    """Write the authority snapshot as stable, reviewable JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Export a pywin32 catalog from the registered type library or generated reports")
    parser.add_argument("--reports-dir", type=Path, default=REPOSITORY_ROOT / "docs" / "reports")
    parser.add_argument("--source", choices=("typelib", "reports"), default="typelib")
    parser.add_argument("--output", type=Path, default=AUTHORITY_PATH)
    args = parser.parse_args()
    builder = build_authority_from_typelib if args.source == "typelib" else build_authority
    write_authority(builder(args.reports_dir), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
