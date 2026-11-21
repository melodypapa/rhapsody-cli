"""Shared helpers for validating and verifying one Rhapsody API sync."""

import json
import re
import sys
from pathlib import Path
from typing import List, Optional, Set, Tuple

_INTERFACE_PATTERN = re.compile(r"^# Rhapsody API Validation: (IRP[A-Za-z0-9_]+)$", re.MULTILINE)
_WRAPPER_PATTERN = re.compile(r"^- Target wrapper: `([^`]+)` \(`([^`]+)`\)$", re.MULTILINE)
_JAVA_PACKAGE_PATTERN = re.compile(r"^- Java package: `([A-Za-z0-9_.]+)`$", re.MULTILINE)
_MEMBER_PATTERN = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")
_RST_INTERFACE_ANCHOR = ".. _rhapsody-java-interface-"
_REPORT_SECTIONS = {"Comparison details", "Expected Binding Differences", "Wrapper Backlog"}


def split_interface_name(interface_name: str) -> Tuple[str, Optional[str]]:
    """Return the simple IRP interface name and optional Java package."""
    parts = interface_name.rsplit(".", maxsplit=1)
    simple_name = parts[-1]
    if not simple_name.startswith("IRP") or not simple_name.isidentifier():
        raise ValueError(f"Expected a Java interface such as IRPClass, got {interface_name!r}")
    package_name = parts[0] if len(parts) == 2 else None
    return simple_name, package_name


def find_project_root(start: Path) -> Path:
    """Find the repository root from a working directory or a nested skill path."""
    candidate_start = start.parent if start.is_file() or start.suffix else start
    for candidate in (candidate_start, *candidate_start.parents):
        if (candidate / "scripts" / "validate_model_api.py").is_file() and (candidate / "docs" / "java_api").is_dir():
            return candidate.resolve()
    raise FileNotFoundError(f"Could not find rhapsody-cli project root above {start}")


def find_java_doc(root: Path, interface_name: str) -> Tuple[str, str, Path]:
    """Resolve an interface JavaDoc page and its declared package path."""
    simple_name, package_name = split_interface_name(interface_name)
    docs_root = root / "docs" / "java_api"
    if package_name is not None:
        java_doc = docs_root.joinpath(*package_name.split("."), f"{simple_name}.html")
        if not java_doc.is_file():
            raise FileNotFoundError(f"JavaDoc not found for {interface_name}: {java_doc}")
    else:
        matches = [path for path in docs_root.rglob(f"{simple_name}.html") if "class-use" not in path.parts]
        if not matches:
            raise FileNotFoundError(f"JavaDoc not found for {simple_name} under {docs_root}")
        if len(matches) > 1:
            paths = ", ".join(str(path.relative_to(docs_root)) for path in sorted(matches))
            raise ValueError(f"JavaDoc name {simple_name} is ambiguous; use a fully qualified name: {paths}")
        java_doc = matches[0]
    package_parts = java_doc.parent.relative_to(docs_root).parts
    if not package_parts:
        raise ValueError(f"JavaDoc page has no package directory: {java_doc}")
    return simple_name, ".".join(package_parts), java_doc


def offline_authority_blocker(root: Path, interface_name: str) -> Optional[str]:
    """Return the blocker for offline validation, or None when committed COM evidence exists."""
    reports_dir = root / "docs" / "reports"
    try:
        authority = json.loads((reports_dir / "pywin32_authority.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        authority = {}
    if interface_name in authority.get("catalog", {}):
        return None
    if (reports_dir / f"{interface_name}_api_report.md").is_file():
        return f"The authority catalog lacks {interface_name}. Rebuild it from the committed reports with: python scripts/pywin32_authority.py --source reports"
    return (
        f"Offline sync cannot proceed: docs/reports/{interface_name}_api_report.md does not exist and "
        f"{interface_name} is absent from docs/reports/pywin32_authority.json. "
        "Run the sync on a machine with Rhapsody (--source typelib) or commit a generated report first."
    )


def build_validator_command(root: Path, interface_name: str, source: str, report_dir: Path) -> List[str]:
    """Build a command delegating to the repository's canonical validator."""
    simple_name, _ = split_interface_name(interface_name)
    return [
        sys.executable,
        str(root / "scripts" / "validate_model_api.py"),
        simple_name,
        "--source",
        source,
        "--path",
        str(report_dir),
    ]


def parse_report_target(report_text: str) -> Tuple[str, str]:
    """Return the wrapper class and repository-relative source path in a report."""
    match = _WRAPPER_PATTERN.search(report_text)
    if match is None:
        raise ValueError("API report is missing its target wrapper summary")
    return match.group(1), match.group(2)


def parse_report_java_package(report_text: str) -> Optional[str]:
    """Return the Java package declared in a validator report's Summary, if present."""
    match = _JAVA_PACKAGE_PATTERN.search(report_text)
    return match.group(1) if match else None


def extract_deviation_members(report_text: str) -> Set[str]:
    """Collect API names from the validator's comparison, binding, and backlog tables."""
    members: Set[str] = set()
    active_section: Optional[str] = None
    for line in report_text.splitlines():
        if line.startswith("## "):
            active_section = line[3:].strip()
            continue
        if active_section not in _REPORT_SECTIONS or not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 4 or cells[0] == "Python model wrapper" or all(set(cell) <= {"-", " "} for cell in cells):
            continue
        for cell in cells[:3]:
            members.update(_MEMBER_PATTERN.findall(cell))
    return members


def _get_rst_interface_section(rst_text: str, interface_name: str) -> Optional[str]:
    anchor = f"{_RST_INTERFACE_ANCHOR}{interface_name}:"
    start = rst_text.find(anchor)
    if start < 0:
        return None
    next_anchor = rst_text.find(_RST_INTERFACE_ANCHOR, start + len(anchor))
    return rst_text[start:] if next_anchor < 0 else rst_text[start:next_anchor]


def _canonical_import(root: Path, source_path: str) -> Tuple[Path, str]:
    wrapper_path = Path(source_path)
    if wrapper_path.is_absolute():
        absolute_path = wrapper_path
    else:
        absolute_path = root / wrapper_path
    source_root = root / "src"
    try:
        module_parts = absolute_path.resolve().relative_to(source_root.resolve()).with_suffix("").parts
    except ValueError as exc:
        raise ValueError(f"Wrapper source is outside the Python src directory: {source_path}") from exc
    if not module_parts:
        raise ValueError(f"Wrapper source does not identify a Python module: {source_path}")
    return absolute_path, ".".join(module_parts)


def verify_sync_artifacts(root: Path, interface_name: str, report_path: Path) -> List[str]:
    """Check package placement, requirement entry, and RST coverage against a validator report."""
    issues: List[str] = []
    try:
        simple_name, java_package, java_doc = find_java_doc(root, interface_name)
    except (OSError, ValueError) as exc:
        return [str(exc)]
    if not report_path.is_file():
        return [f"API report not found: {report_path}"]
    report_text = report_path.read_text(encoding="utf-8")
    report_match = _INTERFACE_PATTERN.search(report_text)
    if report_match is None or report_match.group(1) != simple_name:
        issues.append(f"API report does not match Java interface {simple_name}: {report_path}")
        return issues

    report_java_package = parse_report_java_package(report_text)
    if report_java_package is None:
        issues.append(f"API report for {simple_name} is missing the '- Java package: `<package>`' Summary line")
    elif report_java_package != java_package:
        issues.append(f"API report declares Java package '{report_java_package}' but JavaDoc declares '{java_package}' for {simple_name}")

    try:
        wrapper_class, source_path = parse_report_target(report_text)
        absolute_wrapper, canonical_import = _canonical_import(root, source_path)
    except ValueError as exc:
        return [str(exc)]
    package_dir = Path(*java_package.split("."))
    expected_package_dir = root / "src" / "rhapsody_cli" / "models" / package_dir
    if absolute_wrapper.parent.resolve() != expected_package_dir.resolve():
        issues.append(f"Wrapper package mismatch: expected {expected_package_dir}, found {absolute_wrapper.parent}")
    if not absolute_wrapper.is_file():
        issues.append(f"Wrapper source does not exist: {absolute_wrapper}")

    class_stem = absolute_wrapper.stem

    # Unit and integration tests mirror the wrapper's package and must exercise the class.
    models_root = root / "src" / "rhapsody_cli" / "models"
    rel_pkg = absolute_wrapper.parent.relative_to(models_root)
    for label, test_base in (("Unit", "unit"), ("Integration", "integration")):
        test_path = root / "tests" / test_base / "models" / rel_pkg / f"test_{class_stem}.py"
        if not test_path.is_file():
            issues.append(f"{label} test file not found for {simple_name}: {test_path}")
        elif wrapper_class not in test_path.read_text(encoding="utf-8"):
            issues.append(f"{label} test file does not exercise {wrapper_class}: {test_path}")
    requirements_path = root / "docs" / "requirements" / package_dir / f"{class_stem}.md"
    if not requirements_path.is_file():
        issues.append(f"Class requirement document not found: {requirements_path}")
    else:
        requirement_text = requirements_path.read_text(encoding="utf-8")
        if simple_name not in requirement_text or wrapper_class not in requirement_text:
            issues.append(f"Requirement document does not identify both {simple_name} and {wrapper_class}")

    rst_path = root / "docs" / "api" / package_dir / f"{class_stem}.rst"
    if not rst_path.is_file():
        issues.append(f"RST API document not found: {rst_path}")
        return issues
    rst_section = _get_rst_interface_section(rst_path.read_text(encoding="utf-8"), simple_name)
    if rst_section is None:
        issues.append(f"RST API document has no section anchor for {simple_name}: {_RST_INTERFACE_ANCHOR}{simple_name}:")
        return issues
    required_values = {
        "Java package": java_package,
        "Java interface": simple_name,
        "Python wrapper": wrapper_class,
        "canonical Python import": canonical_import,
        "JavaDoc member/signature header": "javadoc member/signature",
        "COM/pywin32 header": "com/pywin32",
        "Python implementation header": "python implementation",
        "deviation/treatment header": "deviation and treatment",
    }
    lowered_rst_section = rst_section.lower()
    for label, value in required_values.items():
        if value.lower() not in lowered_rst_section:
            issues.append(f"RST section for {simple_name} is missing {label}: {value}")

    deviation_members = extract_deviation_members(report_text)
    if deviation_members:
        if ".. list-table::" not in rst_section:
            issues.append(f"RST section for {simple_name} has deviations but no reStructuredText list-table")
        missing_members = sorted(member for member in deviation_members if member not in rst_section)
        if missing_members:
            issues.append(f"RST section for {simple_name} omits reported deviation members: {', '.join(missing_members)}")
    elif "no deviations" not in lowered_rst_section:
        issues.append(f"RST section for {simple_name} should explicitly state that there are no deviations")

    if not java_doc.is_file():
        issues.append(f"JavaDoc page does not exist: {java_doc}")
    return issues
