"""Run the repository API validator for one JavaDoc interface."""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List, Optional

from sync_tools import build_validator_command, find_java_doc, find_project_root, offline_authority_blocker


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Validate one Rhapsody wrapper against JavaDoc and pywin32")
    parser.add_argument("interface", help="Java interface, such as IRPClass; a fully qualified name is also accepted")
    parser.add_argument("--source", choices=("authority", "typelib"), default="authority", help="COM member catalog source")
    parser.add_argument("--root", type=Path, help="Project root; discovered from the current directory when omitted")
    parser.add_argument("--reports-dir", type=Path, help="Report output directory; defaults to docs/reports")
    args = parser.parse_args(argv)

    try:
        root = find_project_root(args.root or Path(__file__).resolve())
        interface_name, java_package, _ = find_java_doc(root, args.interface)
        if java_package != "com.telelogic.rhapsody.core":
            raise ValueError(f"The repository validator currently reads JavaDoc from com.telelogic.rhapsody.core, but {interface_name} is declared in {java_package}")
        reports_dir = args.reports_dir or root / "docs" / "reports"
        if not reports_dir.is_absolute():
            reports_dir = root / reports_dir
        if args.source == "authority":
            blocker = offline_authority_blocker(root, interface_name)
            if blocker is not None:
                print(blocker, file=sys.stderr)
                return 2
        command = build_validator_command(root, interface_name, args.source, reports_dir)
        result = subprocess.run(command, cwd=root, check=False)
    except (FileNotFoundError, OSError, ValueError) as exc:
        print(f"Validation setup failed: {exc}", file=sys.stderr)
        return 2

    report_path = reports_dir / f"{interface_name}_api_report.md"
    if report_path.is_file():
        print(f"API report: {report_path}")
    if result.returncode == 0:
        print("Validator found no actionable deviations.")
    elif result.returncode == 1:
        print("Validator found deviations; review the report and verify their RST entries.", file=sys.stderr)
    else:
        print(f"Validator failed with exit code {result.returncode}.", file=sys.stderr)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
