"""Verify one class sync against the validator report and project documentation."""

import argparse
import sys
from pathlib import Path
from typing import List, Optional

from sync_tools import api_report_path, find_project_root, verify_sync_artifacts, write_getter_catalog_diff, write_getter_matrix


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Verify package, requirements, and RST artifacts for one Rhapsody interface")
    parser.add_argument("interface", help="Java interface, such as IRPClass; a fully qualified name is also accepted")
    parser.add_argument("--root", type=Path, help="Project root; discovered from the current directory when omitted")
    parser.add_argument("--report", type=Path, help="Validator report; defaults to docs/reports/<java.package.path>/<INTERFACE>_api_report.md")
    parser.add_argument("--write-getter-matrix", action="store_true", help="Regenerate this interface's Getter fixture matrix section from the wrapper and integration tests")
    parser.add_argument("--write-getter-diff", action="store_true", help="Regenerate this interface's getter-vs-pywin32-catalog diff section")
    parser.add_argument("--strict-getters", action="store_true", help="Fail on WEAK/MISSING getter matrix rows unless the member is recorded as a blocker")
    parser.add_argument("--strict-inherited", action="store_true", help="Fail when an integration assertion references only inherited members")
    args = parser.parse_args(argv)

    try:
        root = find_project_root(args.root or Path(__file__).resolve())
        report_path = args.report or api_report_path(root, args.interface)
        if not report_path.is_absolute():
            report_path = root / report_path
        if args.write_getter_matrix:
            matrix_path = write_getter_matrix(root, args.interface, report_path)
            print(f"Getter fixture matrix updated: {matrix_path}")
            return 0
        if args.write_getter_diff:
            diff_path = write_getter_catalog_diff(root, args.interface, report_path)
            print(f"Getter catalog diff updated: {diff_path}")
            return 0
        inherited_notes: List[str] = []
        issues = verify_sync_artifacts(
            root,
            args.interface,
            report_path,
            strict_getters=args.strict_getters,
            inherited_notes=inherited_notes,
            strict_inherited=args.strict_inherited,
        )
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
