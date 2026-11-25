"""Verify one class sync against the validator report and project documentation."""

import argparse
import sys
from pathlib import Path
from typing import List, Optional

from sync_tools import api_report_path, find_project_root, verify_sync_artifacts


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Verify package, requirements, and RST artifacts for one Rhapsody interface")
    parser.add_argument("interface", help="Java interface, such as IRPClass; a fully qualified name is also accepted")
    parser.add_argument("--root", type=Path, help="Project root; discovered from the current directory when omitted")
    parser.add_argument("--report", type=Path, help="Validator report; defaults to docs/reports/<java.package.path>/<INTERFACE>_api_report.md")
    parser.add_argument("--strict-inherited", action="store_true", help="Fail when an integration assertion references only inherited members")
    args = parser.parse_args(argv)

    try:
        root = find_project_root(args.root or Path(__file__).resolve())
        report_path = args.report or api_report_path(root, args.interface)
        if not report_path.is_absolute():
            report_path = root / report_path
        inherited_notes: List[str] = []
        issues = verify_sync_artifacts(root, args.interface, report_path, inherited_notes=inherited_notes, strict_inherited=args.strict_inherited)
    except (FileNotFoundError, OSError, ValueError) as exc:
        print(f"Sync verification could not run: {exc}", file=sys.stderr)
        return 2

    for note in inherited_notes:
        print(f"NOTE: {note}", file=sys.stderr)
    if issues:
        for issue in issues:
            print(f"FAIL: {issue}", file=sys.stderr)
        return 1
    print(f"Sync artifacts verified for {args.interface}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
