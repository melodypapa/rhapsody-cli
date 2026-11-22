"""Shared helpers for validating and verifying one Rhapsody API sync."""

import ast
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
# Every non-MATCH report row is a deviation and requires an RST row — including
# "Wrapper Backlog" members (COM-supported members without Python wrappers):
# unwrapped API surface is a deviation from Java-API parity, with the RST
# recording the "intentionally unsupported" disposition.
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


def api_report_path(root: Path, interface_name: str) -> Path:
    """Return the report path under the interface's Java package directory."""
    simple_name, explicit_package = split_interface_name(interface_name)
    reports_dir = root / "docs" / "reports"
    report_name = f"{simple_name}_api_report.md"
    if explicit_package is not None:
        java_package = explicit_package
    else:
        try:
            _, java_package, _ = find_java_doc(root, simple_name)
        except FileNotFoundError as exc:
            matches = sorted(reports_dir.rglob(report_name))
            if len(matches) == 1:
                return matches[0]
            if len(matches) > 1:
                paths = ", ".join(path.relative_to(reports_dir).as_posix() for path in matches)
                raise ValueError(f"API report for {simple_name} is ambiguous without JavaDoc: {paths}") from exc
            java_package = "com.telelogic.rhapsody.core"
    return reports_dir / Path(*java_package.split(".")) / report_name


def offline_authority_blocker(root: Path, interface_name: str) -> Optional[str]:
    """Return the blocker for offline validation, or None when committed COM evidence exists."""
    reports_dir = root / "docs" / "reports"
    report_path = api_report_path(root, interface_name)
    report_display_path = report_path.relative_to(root).as_posix()
    try:
        authority = json.loads((reports_dir / "pywin32_authority.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        authority = {}
    if interface_name in authority.get("catalog", {}):
        return None
    if report_path.is_file():
        return f"The authority catalog lacks {interface_name}. Rebuild it from the committed reports with: python scripts/pywin32_authority.py --source reports"
    return (
        f"Offline sync cannot proceed: {report_display_path} does not exist and "
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
    """Collect API names from every non-MATCH report table.

    Covers the comparison table, expected binding differences, and the wrapper
    backlog: unwrapped-but-COM-supported members are deviations too, and the
    RST page must record their "intentionally unsupported" disposition.
    """
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


def _java_interface_snake(simple_name: str) -> str:
    """Convert a Java interface name to the project's snake_case module stem.

    ``IRPApplication`` -> ``irp_application``; ``IRPModelElement`` ->
    ``irp_model_element``. Used for artifacts named after the Java interface rather
    than the Python wrapper module (which differs for application-layer wrappers).
    """
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", simple_name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    return name.lower()


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


def parse_wrapper_bindings(wrapper_source: str) -> List[Tuple[str, str]]:
    """Extract (com_member, expected_shape) pairs from a synced wrapper body.

    Recognised binding forms (per AGENTS.md / SKILL §3):
      * ``call_com(lambda: self._com.Name(...))`` -> ("Name", "method")
      * ``get_com_property(self._com, "Name")``  -> ("Name", "property")
      * ``set_com_property(self._com, "Name", ...)`` -> ("Name", "property")

    Both ``self.call_com`` and ``AbstractRPModelElement.call_com`` (and the
    ``com_utils.call_com`` form) are handled because the call target is not
    what determines the COM member -- the lambda body / property argument is.
    """
    bindings: List[Tuple[str, str]] = []
    tree = ast.parse(wrapper_source)
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
            continue
        attr = node.func.attr
        if attr == "call_com" and node.args:
            lam = node.args[0]
            if isinstance(lam, ast.Lambda) and isinstance(lam.body, ast.Call) and isinstance(lam.body.func, ast.Attribute):
                if isinstance(lam.body.func.value, ast.Attribute) and lam.body.func.value.attr == "_com":
                    bindings.append((lam.body.func.attr, "method"))
        elif attr in ("get_com_property", "set_com_property") and len(node.args) >= 2:
            arg = node.args[1]
            if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                bindings.append((arg.value, "property"))
    return bindings


def verify_wrapper_bindings(root: Path, interface_name: str, wrapper_source: str) -> List[str]:
    """Check every wrapper COM binding against the committed pywin32 catalog.

    A wrapper member must forward to exactly one pywin32-exposed member, with a
    method-shaped member called via ``call_com`` and a property-shaped member
    read/written via ``get_com_property`` / ``set_com_property``. Names are
    matched case-insensitively (COM identifiers are case-insensitive and the
    catalog preserves the type library's PascalCase). A member absent from the
    catalog, or bound with the wrong shape, is a sync defect and fails Step 8.
    """
    catalog_path = root / "docs" / "reports" / "pywin32_authority.json"
    if not catalog_path.is_file():
        return [f"pywin32 authority catalog not found: {catalog_path}"]
    catalog = json.loads(catalog_path.read_text(encoding="utf-8")).get("catalog", {})
    entries = catalog.get(interface_name)
    if entries is None:
        return [f"pywin32 catalog has no entry for {interface_name}"]
    lowered = {str(name).lower(): (name, shape) for name, shape in entries.items()}
    issues: List[str] = []
    for member, shape in parse_wrapper_bindings(wrapper_source):
        found = lowered.get(member.lower())
        if found is None:
            issues.append(f"{interface_name} binding '{member}' is absent from the pywin32 catalog")
        elif found[1] != shape:
            issues.append(
                f"{interface_name} binding '{member}' is {shape}-shaped in the wrapper "
                f"but the pywin32 catalog declares '{found[0]}' as {found[1]}"
            )
    return issues


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
    source_root = root / "src" / "rhapsody_cli"
    try:
        rel_parent = absolute_wrapper.parent.relative_to(source_root)
    except ValueError:
        rel_parent = Path()  # handled by the mismatch check below
    is_model_wrapper = bool(rel_parent.parts) and rel_parent.parts[0] == "models"
    if is_model_wrapper:
        # Model wrappers must live in the canonical Java-package directory.
        expected_package_dir = source_root / "models" / package_dir
    else:
        # Application-layer wrappers (e.g. RhapsodyApplication) stay at the package
        # root: §2's canonical move is N/A for the application layer.
        expected_package_dir = source_root
    if absolute_wrapper.parent.resolve() != expected_package_dir.resolve():
        issues.append(f"Wrapper package mismatch: expected {expected_package_dir}, found {absolute_wrapper.parent}")
    if not absolute_wrapper.is_file():
        issues.append(f"Wrapper source does not exist: {absolute_wrapper}")
    else:
        # Step 3/4 enforcement: every wrapper COM binding must exist in the
        # pywin32 catalog with the correct method/property shape.
        issues.extend(verify_wrapper_bindings(root, simple_name, absolute_wrapper.read_text(encoding="utf-8")))

    class_stem = absolute_wrapper.stem
    java_snake = _java_interface_snake(simple_name)
    # Artifacts may be named after either the wrapper module or the Java interface;
    # these differ for application-layer wrappers (application.py / irp_application).
    candidate_stems = [class_stem] if class_stem == java_snake else [class_stem, java_snake]

    def first_existing(directory: Path, filename_template: str) -> Optional[Path]:
        for stem in candidate_stems:
            candidate = directory / filename_template.format(stem=stem)
            if candidate.is_file():
                return candidate
        return None

    # Unit and integration tests mirror the wrapper's package and must exercise the class.
    model_segment = Path("models") / Path(*rel_parent.parts[1:]) if is_model_wrapper else Path()
    for label, test_base in (("Unit", "unit"), ("Integration", "integration")):
        test_dir = root / "tests" / test_base / model_segment
        test_path = first_existing(test_dir, "test_{stem}.py")
        if test_path is None:
            issues.append(f"{label} test file not found for {simple_name}: {test_dir / f'test_{class_stem}.py'}")
        elif wrapper_class not in test_path.read_text(encoding="utf-8"):
            issues.append(f"{label} test file does not exercise {wrapper_class}: {test_path}")
    requirements_path = first_existing(root / "docs" / "requirements" / package_dir, "{stem}.md")
    if requirements_path is None:
        issues.append(f"Class requirement document not found: {root / 'docs' / 'requirements' / package_dir / f'{class_stem}.md'}")
    else:
        requirement_text = requirements_path.read_text(encoding="utf-8")
        if simple_name not in requirement_text or wrapper_class not in requirement_text:
            issues.append(f"Requirement document does not identify both {simple_name} and {wrapper_class}")

    rst_path = first_existing(root / "docs" / "api" / package_dir, "{stem}.rst")
    if rst_path is None:
        issues.append(f"RST API document not found: {root / 'docs' / 'api' / package_dir / f'{class_stem}.rst'}")
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
