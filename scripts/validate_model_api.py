"""Compare a Rhapsody model wrapper with its Java and pywin32 APIs."""

import argparse
import ast
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

if __package__ in (None, ""):  # running as `python scripts/validate_model_api.py`
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.pywin32_authority import AuthorityData, load_authority  # noqa: E402

_TYPELIB_DESCRIPTION = "Rhapsody2 1.0 Type Library"
_HELPER_NAMES = {"_get_method_or_property", "_set_method_or_property"}
Rows = List[Tuple[str, str, str, str, str]]
_AUTHORITY_INFO_STATUSES = {"ACCESSOR_ALIAS_MISMATCH", "METHOD_PROPERTY_MISMATCH", "PYTHON_ONLY_MEMBER", "JAVA_ONLY_MEMBER"}
_AUTHORITY_BACKLOG_STATUSES = {"MISSING_PYTHON_WRAPPER", "PYWIN32_ONLY_MEMBER"}


class _InterfacePageParser(HTMLParser):
    """Collect method anchors and direct superinterfaces from one Javadoc page."""

    def __init__(self) -> None:
        super().__init__()
        self.method_names: Set[str] = set()
        self.method_signatures: Dict[str, Set[str]] = {}
        self.superinterfaces: Set[str] = set()
        self._awaiting_superinterfaces = False
        self._in_superinterfaces = False

    def handle_data(self, data: str) -> None:
        if "All Superinterfaces:" in data:
            self._awaiting_superinterfaces = True

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        attributes = dict(attrs)
        if tag == "dd" and self._awaiting_superinterfaces:
            self._in_superinterfaces = True
            self._awaiting_superinterfaces = False

        if tag != "a":
            return

        anchor_name = attributes.get("name")
        if anchor_name and "(" in anchor_name:
            method_name = anchor_name.split("(", maxsplit=1)[0]
            if method_name:
                self.method_names.add(method_name)
                self.method_signatures.setdefault(method_name, set()).add(anchor_name)

        href = attributes.get("href")
        if self._in_superinterfaces and href:
            parent_name = Path(href.split("#", maxsplit=1)[0]).stem
            if parent_name.startswith("IRP"):
                self.superinterfaces.add(parent_name)

    def handle_endtag(self, tag: str) -> None:
        if tag == "dd" and self._in_superinterfaces:
            self._in_superinterfaces = False


def _validate_interface_name(interface_name: str) -> None:
    if not interface_name.startswith("IRP") or not interface_name.isidentifier() or len(interface_name) == 3:
        raise ValueError(f"Invalid Java interface name {interface_name!r}; expected a name such as IRPClass")


def collect_java_members(interface_name: str, docs_root: Path) -> Set[str]:
    """Return methods declared by an interface and all documented superinterfaces."""
    _validate_interface_name(interface_name)
    visited: Set[str] = set()

    def visit(current_name: str) -> Set[str]:
        if current_name in visited:
            return set()
        visited.add(current_name)
        page_path = docs_root / f"{current_name}.html"
        if not page_path.is_file():
            raise FileNotFoundError(f"Java API documentation not found: {page_path}")

        parser = _InterfacePageParser()
        parser.feed(page_path.read_text(encoding="utf-8", errors="replace"))
        members = set(parser.method_names)
        for parent_name in sorted(parser.superinterfaces):
            members.update(visit(parent_name))
        return members

    return visit(interface_name)


def collect_java_signatures(interface_name: str, docs_root: Path) -> Dict[str, Set[str]]:
    """Return documented method signatures, including those from superinterfaces."""
    _validate_interface_name(interface_name)
    visited: Set[str] = set()
    signatures: Dict[str, Set[str]] = {}

    def visit(current_name: str) -> None:
        if current_name in visited:
            return
        visited.add(current_name)
        page_path = docs_root / f"{current_name}.html"
        if not page_path.is_file():
            raise FileNotFoundError(f"Java API documentation not found: {page_path}")

        parser = _InterfacePageParser()
        parser.feed(page_path.read_text(encoding="utf-8", errors="replace"))
        for method_name, method_anchors in parser.method_signatures.items():
            signatures.setdefault(method_name, set()).update(f"{current_name}.{anchor}" for anchor in method_anchors)
        for parent_name in sorted(parser.superinterfaces):
            visit(parent_name)

    visit(interface_name)
    return signatures


def _is_com_object(node: ast.expr) -> bool:
    return isinstance(node, ast.Attribute) and node.attr == "_com" and isinstance(node.value, ast.Name) and node.value.id == "self"


def _class_base_name(node: ast.expr) -> Optional[str]:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def _get_method_com_members(method: ast.FunctionDef) -> Set[str]:
    members: Set[str] = set()
    for node in ast.walk(method):
        if isinstance(node, ast.Attribute) and _is_com_object(node.value):
            members.add(node.attr)

        if not isinstance(node, ast.Call):
            continue
        function_name = node.func.attr if isinstance(node.func, ast.Attribute) else node.func.id if isinstance(node.func, ast.Name) else ""
        if function_name not in _HELPER_NAMES:
            continue
        for argument in node.args[1:3]:
            if isinstance(argument, ast.Constant) and isinstance(argument.value, str):
                members.add(argument.value)
    return members


def resolve_python_wrapper(interface_name: str, models_root: Path) -> Tuple[str, Path]:
    """Return the concrete wrapper class and source path for a Java interface."""
    _validate_interface_name(interface_name)
    if not models_root.is_dir():
        raise FileNotFoundError(f"Python model directory not found: {models_root}")

    is_application_interface = interface_name == "IRPApplication"
    target_class = "RhapsodyApplication" if is_application_interface else "RP" + interface_name[3:]
    source_paths = [models_root.parent / "application.py"] if is_application_interface else sorted(models_root.rglob("*.py"))
    for source_path in source_paths:
        try:
            tree = ast.parse(source_path.read_text(encoding="utf-8"), filename=str(source_path))
        except (OSError, SyntaxError) as exc:
            raise ValueError(f"Could not parse wrapper module {source_path}: {exc}") from exc
        if any(isinstance(node, ast.ClassDef) and node.name == target_class for node in ast.walk(tree)):
            return target_class, source_path
    raise ValueError(f"Python wrapper {target_class} for {interface_name} was not found under {models_root}")


def collect_python_members(interface_name: str, models_root: Path) -> Dict[str, Set[str]]:
    """Map exact COM member names to Python wrapper labels, including wrapper bases."""
    _validate_interface_name(interface_name)
    if not models_root.is_dir():
        raise FileNotFoundError(f"Python model directory not found: {models_root}")

    is_application_interface = interface_name == "IRPApplication"
    source_paths = [models_root.parent / "application.py"] if is_application_interface else sorted(models_root.rglob("*.py"))
    classes: Dict[str, ast.ClassDef] = {}
    for source_path in source_paths:
        try:
            tree = ast.parse(source_path.read_text(encoding="utf-8"), filename=str(source_path))
        except (OSError, SyntaxError) as exc:
            raise ValueError(f"Could not parse model module {source_path}: {exc}") from exc
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and (node.name.startswith("RP") or node.name == "RhapsodyApplication"):
                classes.setdefault(node.name, node)

    target_class = "RhapsodyApplication" if is_application_interface else "RP" + interface_name[3:]
    if target_class not in classes:
        raise ValueError(f"Python model wrapper {target_class} for {interface_name} was not found under {models_root}")

    members: Dict[str, Set[str]] = {}
    visited: Set[str] = set()
    seen_methods: Set[str] = set()

    def visit(class_name: str) -> None:
        if class_name in visited:
            return
        visited.add(class_name)
        class_node = classes.get(class_name)
        if class_node is None:
            return

        for method in class_node.body:
            if not isinstance(method, ast.FunctionDef) or method.name in seen_methods:
                continue
            seen_methods.add(method.name)
            if method.name.startswith("_"):
                continue
            com_members = _get_method_com_members(method)
            if com_members:
                for member_name in com_members:
                    members.setdefault(member_name, set()).add(f"{method.name}() -> {member_name}")
            else:
                local_key = f"python-only:{method.name}"
                members.setdefault(local_key, set()).add(f"{method.name}() (no static COM member)")

        for base in class_node.bases:
            base_name = _class_base_name(base)
            if base_name and base_name.startswith("RP"):
                visit(base_name)

    visit(target_class)
    return members


def collect_generated_members(interface_source: Path, interface_name: str) -> Dict[str, str]:
    """Collect public methods and property-map names from one generated makepy source file."""
    if not interface_source.is_file():
        raise FileNotFoundError(f"Generated pywin32 interface source not found: {interface_source}")
    try:
        tree = ast.parse(interface_source.read_text(encoding="utf-8", errors="replace"), filename=str(interface_source))
    except (OSError, SyntaxError) as exc:
        raise ValueError(f"Could not parse generated pywin32 source {interface_source}: {exc}") from exc

    interface_class = next((node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == interface_name), None)
    if interface_class is None:
        raise ValueError(f"Generated pywin32 source {interface_source} does not define {interface_name}")

    members: Dict[str, str] = {}
    for class_member in interface_class.body:
        if isinstance(class_member, ast.FunctionDef) and not class_member.name.startswith("_"):
            members[class_member.name] = "method"
            continue

        value: Optional[ast.expr]
        if isinstance(class_member, ast.Assign):
            target_names = {target.id for target in class_member.targets if isinstance(target, ast.Name)}
            value = class_member.value
        elif isinstance(class_member, ast.AnnAssign) and isinstance(class_member.target, ast.Name):
            target_names = {class_member.target.id}
            value = class_member.value
        else:
            continue

        if not target_names.intersection({"_prop_map_get_", "_prop_map_put_"}) or value is None or not isinstance(value, ast.Dict):
            continue
        for key in value.keys:
            if isinstance(key, ast.Constant) and isinstance(key.value, str):
                if members.get(key.value) == "method":
                    members[key.value] = "method/property"
                else:
                    members[key.value] = "property"
    return members


def _resolve_generated_interface_source(generated_module_path: Path, interface_name: str) -> Path:
    interface_source = generated_module_path.parent / f"{interface_name}.py"
    return interface_source if interface_source.is_file() else generated_module_path


def collect_registered_pywin32_members(interface_name: str) -> Dict[str, str]:
    """Read a makepy interface from the registered type library without connecting to Rhapsody."""
    _validate_interface_name(interface_name)
    try:
        import win32com.client.gencache as gencache
        import win32com.client.selecttlb as selecttlb

        type_libraries = [spec for spec in selecttlb.EnumTlbs() if spec.desc == _TYPELIB_DESCRIPTION]
        if not type_libraries:
            raise RuntimeError(f"Registered Rhapsody type library {_TYPELIB_DESCRIPTION!r} was not found")
        type_library = type_libraries[0]
        generated_module = gencache.EnsureModule(type_library.clsid, type_library.lcid, int(type_library.major), int(type_library.minor))
        generated_source = getattr(generated_module, "__file__", None)
        if not isinstance(generated_source, str):
            raise RuntimeError("pywin32 did not return the generated Rhapsody type-library source path")
        interface_source = _resolve_generated_interface_source(Path(generated_source), interface_name)
        return collect_generated_members(interface_source, interface_name)
    except Exception as exc:
        raise RuntimeError(f"Could not enumerate pywin32 interface {interface_name}: {exc}") from exc


def _camel_to_snake(name: str) -> str:
    result = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    result = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", result)
    return result.lower()


def _canonical_member_name(member_name: str) -> str:
    if member_name.startswith("python-only:"):
        return member_name
    if member_name.startswith(("get", "set")) and len(member_name) > 3 and member_name[3].isupper():
        member_name = member_name[3:]
    return member_name[:1].lower() + member_name[1:]


def _classify_deviation(
    python_member_names: Set[str],
    python_labels: Set[str],
    java_member_names: Set[str],
    pywin32_members: Dict[str, str],
) -> Tuple[str, str]:
    python_com_names = {name for name in python_member_names if not name.startswith("python-only:")}
    pywin32_names = set(pywin32_members)
    statuses: List[str] = []

    if not python_labels:
        if java_member_names and pywin32_names:
            statuses.append("MISSING_PYTHON_WRAPPER")
        elif java_member_names:
            statuses.append("JAVA_ONLY_MEMBER")
        elif pywin32_names:
            statuses.append("PYWIN32_ONLY_MEMBER")
    elif not java_member_names:
        statuses.append("JAVA_DOC_MISSING" if pywin32_names else "PYTHON_ONLY_MEMBER")
    elif not pywin32_names:
        statuses.append("PYWIN32_MEMBER_MISSING")

    wrapper_names = {label.split("()", maxsplit=1)[0] for label in python_labels}
    expected_wrapper_names = {_camel_to_snake(name) for name in java_member_names}
    if python_labels and java_member_names and not expected_wrapper_names.issubset(wrapper_names):
        statuses.append("PYTHON_METHOD_NAME_MISMATCH")
    if python_com_names and pywin32_names and not python_com_names.intersection(pywin32_names):
        statuses.append("COM_MEMBER_NOT_EXPOSED")
    if java_member_names and pywin32_names and java_member_names != pywin32_names:
        statuses.append("ACCESSOR_ALIAS_MISMATCH")
    if java_member_names and pywin32_members and any(kind != "method" for kind in pywin32_members.values()):
        statuses.append("METHOD_PROPERTY_MISMATCH")

    property_names = sorted(name for name, kind in pywin32_members.items() if "property" in kind)
    if "MISSING_PYTHON_WRAPPER" in statuses:
        recommendation = "Implement the Python wrapper or mark this API member intentionally unsupported."
    elif "JAVA_ONLY_MEMBER" in statuses:
        recommendation = "Verify the Java documentation against the installed COM type library."
    elif "PYWIN32_ONLY_MEMBER" in statuses:
        recommendation = "Confirm this version-specific member should be wrapped; otherwise classify it as unsupported."
    elif "PYTHON_ONLY_MEMBER" in statuses:
        recommendation = "Keep this as a local facade helper or map it to a documented API member."
    elif "PYWIN32_MEMBER_MISSING" in statuses:
        recommendation = "Use a member exposed by the registered type library or verify the Rhapsody version."
    elif "JAVA_DOC_MISSING" in statuses:
        recommendation = "Confirm this COM member is a supported extension and document its status."
    elif "COM_MEMBER_NOT_EXPOSED" in statuses and property_names:
        missing_calls = sorted(python_com_names - pywin32_names)
        missing_call_text = " and ".join(missing_calls)
        recommendation = f"Use the {', '.join(property_names)} property or a getter/setter fallback instead of calling {missing_call_text} directly."
    elif "COM_MEMBER_NOT_EXPOSED" in statuses:
        recommendation = "Change the COM call to a member exposed by the registered pywin32 interface."
    elif "PYTHON_METHOD_NAME_MISMATCH" in statuses:
        recommendation = "Rename the Python method to the snake_case Java API name or document the alias."
    elif "METHOD_PROPERTY_MISMATCH" in statuses:
        recommendation = "Use a property-aware getter/setter fallback or document the binding mismatch."
    else:
        recommendation = "Review the related API spellings and document the intended mapping."

    return "; ".join(statuses), recommendation


def apply_pywin32_authority(rows: Rows, interface_name: str, authority: AuthorityData) -> Tuple[Rows, Rows, Rows]:
    """Split raw deviations into actionable, informational, and backlog rows."""
    deviations: Rows = []
    informational: Rows = []
    backlog: Rows = []
    aliases = authority["documented_aliases"].get(interface_name, {})
    unavailable = set(authority["documented_unavailable"].get(interface_name, []))

    for row in rows:
        statuses = row[3].split("; ")
        remaining: List[str] = []
        for status in statuses:
            if status in _AUTHORITY_INFO_STATUSES:
                continue
            if status == "PYTHON_METHOD_NAME_MISMATCH":
                wrapper_names = {label.split("()", maxsplit=1)[0] for label in row[0].split("; ") if label != "—"}
                if wrapper_names and all(name in aliases for name in wrapper_names):
                    continue
            if status == "PYWIN32_MEMBER_MISSING":
                java_names = {entry[: -len(" (method)")] for entry in row[1].split("; ") if entry.endswith(" (method)")}
                if java_names and java_names.issubset(unavailable):
                    continue
            remaining.append(status)

        if any(status in _AUTHORITY_BACKLOG_STATUSES for status in remaining):
            backlog.append(row)
        elif remaining:
            deviations.append((row[0], row[1], row[2], "; ".join(remaining), row[4]))
        elif any(status in _AUTHORITY_INFO_STATUSES for status in statuses):
            informational.append(row)

    return deviations, informational, backlog


def build_deviation_rows(python_members: Dict[str, Set[str]], java_members: Set[str], pywin32_members: Dict[str, str]) -> List[Tuple[str, str, str, str, str]]:
    """Group accessor/property aliases and report missing or differently shaped API families."""
    python_names: Dict[str, Set[str]] = {}
    python_labels: Dict[str, Set[str]] = {}
    java_names: Dict[str, Set[str]] = {}
    pywin32_names: Dict[str, Dict[str, str]] = {}

    for member_name, labels in python_members.items():
        key = _canonical_member_name(member_name)
        python_names.setdefault(key, set()).add(member_name)
        python_labels.setdefault(key, set()).update(labels)
    for member_name in java_members:
        key = _canonical_member_name(member_name)
        java_names.setdefault(key, set()).add(member_name)
    for member_name, kind in pywin32_members.items():
        key = _canonical_member_name(member_name)
        pywin32_names.setdefault(key, {})[member_name] = kind

    rows: List[Tuple[str, str, str, str, str]] = []
    all_families = set(python_names) | set(java_names) | set(pywin32_names)
    for family in sorted(all_families):
        python_member_names = python_names.get(family, set())
        python_wrapper_labels = python_labels.get(family, set())
        java_member_names = java_names.get(family, set())
        pywin32_member_names = pywin32_names.get(family, {})
        statuses, recommendation = _classify_deviation(python_member_names, python_wrapper_labels, java_member_names, pywin32_member_names)

        if not statuses:
            continue

        python_cell = "; ".join(sorted(python_wrapper_labels)) if python_wrapper_labels else "—"
        java_cell = "; ".join(f"{name} (method)" for name in sorted(java_member_names)) or "—"
        pywin32_cell = "; ".join(f"{name} ({kind})" for name, kind in sorted(pywin32_member_names.items())) or "—"
        rows.append((python_cell, java_cell, pywin32_cell, statuses, recommendation))
    return rows


def render_report(rows: List[Tuple[str, str, str, str, str]]) -> str:
    """Render deviations as a stable five-column plain-text table."""
    headers = ("Python model wrapper", "Java API", "pywin32", "Comparison status", "Recommended change")
    column_widths = [len(header) for header in headers]
    for row in rows:
        for index, cell in enumerate(row):
            column_widths[index] = max(column_widths[index], len(cell))

    def format_row(cells: Tuple[str, str, str, str, str]) -> str:
        return " | ".join(cell.ljust(column_widths[index]) for index, cell in enumerate(cells))

    lines = [format_row(headers), "-+-".join("-" * width for width in column_widths)]
    lines.extend(format_row(row) for row in rows)
    return "\n".join(lines)


def _append_report_table(lines: List[str], heading: str, rows: Rows) -> None:
    lines.extend(["", heading, "", "| Python model wrapper | Java API | pywin32 | Status | Recommended change |", "| --- | --- | --- | --- | --- |"])
    if not rows:
        lines.append("| — | — | — | — | — |")
        return
    for row in rows:
        escaped_cells = [cell.replace("|", "\\|").replace("\n", "<br>") for cell in row]
        lines.append("| " + " | ".join(escaped_cells) + " |")


def render_markdown_report(
    interface_name: str,
    rows: Rows,
    wrapper_class: str,
    wrapper_path: str,
    java_signatures: Dict[str, Set[str]],
    member_counts: Tuple[int, int, int],
    authoritative: bool = False,
    informational_rows: Optional[Rows] = None,
    backlog_rows: Optional[Rows] = None,
) -> str:
    """Render a comparison summary, five-column deviation table, and AI repair guidance."""
    status_counts: Dict[str, int] = {}
    for row in rows:
        for status in row[3].split("; "):
            status_counts[status] = status_counts.get(status, 0) + 1

    lines = [
        f"# Rhapsody API Validation: {interface_name}",
        "",
        "## Summary",
        f"- Target wrapper: `{wrapper_class}` (`{wrapper_path}`)",
        f"- Members: Python `{member_counts[0]}`, Java `{member_counts[1]}`, pywin32 `{member_counts[2]}`",
        f"- Deviations: `{len(rows)}`",
        "- Deviations by status:",
    ]
    if status_counts:
        lines.extend(f"  - `{status}`: {count}" for status, count in sorted(status_counts.items()))
    else:
        lines.append("  - None")

    if authoritative:
        lines.extend(
            [
                "",
                f"- Informational binding differences (expected): `{len(informational_rows or [])}`",
                f"- Wrapper backlog (supported members without wrappers): `{len(backlog_rows or [])}`",
            ]
        )

    lines.extend(
        [
            "",
            "## Comparison details",
            "",
            "| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in rows:
        escaped_cells = [cell.replace("|", "\\|").replace("\n", "<br>") for cell in row]
        lines.append("| " + " | ".join(escaped_cells) + " |")
    if not rows and not authoritative:
        lines.append("| — | — | — | PASS | No change needed. |")

    if authoritative:
        _append_report_table(lines, "## Expected Binding Differences", informational_rows or [])
        _append_report_table(lines, "## Wrapper Backlog", backlog_rows or [])

    lines.extend(["", "## AI Fix Guidance"])
    if not rows:
        lines.append("No deviations require changes.")
        return "\n".join(lines) + "\n"

    for index, row in enumerate(rows, start=1):
        python_cell, java_cell, pywin32_cell, status, recommendation = row
        java_names = [entry[: -len(" (method)")] for entry in java_cell.split("; ") if entry.endswith(" (method)")]
        expected_python_names = sorted({_camel_to_snake(name) for name in java_names})
        signatures = sorted(signature for name in java_names for signature in java_signatures.get(name, set()))
        lines.extend(
            [
                "",
                f"### Finding {index}: {status}",
                f"- **Target:** `{wrapper_class}` in `{wrapper_path}`",
                f"- **Current Python wrapper/COM call:** {python_cell}",
                f"- **Expected Python method(s):** {', '.join(f'`{name}`' for name in expected_python_names) or '—'}",
                f"- **Java signature(s):** {', '.join(f'`{signature}`' for signature in signatures) or '—'}",
                f"- **pywin32 member(s):** {pywin32_cell}",
                f"- **Recommended change:** {recommendation}",
                "- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.",
            ]
        )
    return "\n".join(lines) + "\n"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare one Rhapsody model wrapper with Java docs and pywin32 members")
    parser.add_argument("java_interface", help="Java API interface name, for example IRPClass")
    parser.add_argument(
        "--source",
        choices=("typelib", "authority"),
        default="typelib",
        help="pywin32 member source: registered type library (Windows) or committed authority snapshot (offline)",
    )
    parser.add_argument(
        "--path",
        type=Path,
        help="Output directory for the Markdown report (default: current working directory)",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_arg_parser().parse_args(argv)
    authority = load_authority()
    repository_root = Path(__file__).resolve().parents[1]
    docs_root = repository_root / "docs" / "java_api" / "com" / "telelogic" / "rhapsody" / "core"
    models_root = repository_root / "src" / "rhapsody_cli" / "models"
    report_directory = args.path or Path.cwd()
    report_path = report_directory / f"{args.java_interface}_api_report.md"

    try:
        wrapper_class, wrapper_source = resolve_python_wrapper(args.java_interface, models_root)
        java_members = collect_java_members(args.java_interface, docs_root)
        java_signatures = collect_java_signatures(args.java_interface, docs_root)
        python_members = collect_python_members(args.java_interface, models_root)
        if args.source == "authority":
            pywin32_members = authority["catalog"].get(args.java_interface)
            if pywin32_members is None:
                raise ValueError(f"No pywin32 authority snapshot for {args.java_interface}")
        else:
            pywin32_members = collect_registered_pywin32_members(args.java_interface)
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    raw_rows = build_deviation_rows(python_members, java_members, pywin32_members)
    if args.source == "authority":
        rows, informational_rows, backlog_rows = apply_pywin32_authority(raw_rows, args.java_interface, authority)
    else:
        rows, informational_rows, backlog_rows = raw_rows, [], []

    try:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        python_method_names = {label.split("()", maxsplit=1)[0] for labels in python_members.values() for label in labels}
        member_counts = (len(python_method_names), len(java_members), len(pywin32_members))
        wrapper_path = wrapper_source.relative_to(repository_root).as_posix()
        markdown = render_markdown_report(
            args.java_interface,
            rows,
            wrapper_class,
            wrapper_path,
            java_signatures,
            member_counts,
            authoritative=(args.source == "authority"),
            informational_rows=informational_rows,
            backlog_rows=backlog_rows,
        )
        report_path.write_text(markdown, encoding="utf-8")
    except OSError as exc:
        print(f"Error writing Markdown report to {report_path}: {exc}", file=sys.stderr)
        return 2

    return 0 if not rows else 1


if __name__ == "__main__":
    raise SystemExit(main())
