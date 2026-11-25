"""Shared helpers for validating and verifying one Rhapsody API sync."""

import ast
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

_INTERFACE_PATTERN = re.compile(r"^# Rhapsody API Validation: (IRP[A-Za-z0-9_]+)$", re.MULTILINE)
_WRAPPER_PATTERN = re.compile(r"^- Target wrapper: `([^`]+)` \(`([^`]+)`\)$", re.MULTILINE)
_JAVA_PACKAGE_PATTERN = re.compile(r"^- Java package: `([A-Za-z0-9_.]+)`$", re.MULTILINE)
_RST_INTERFACE_ANCHOR = ".. _rhapsody-java-interface-"


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


def parse_wrapper_public_members(wrapper_source: str, wrapper_class: str) -> List[str]:
    """Return the wrapper class's public members, sorted.

    The RST page is an API reference of the Python wrapper, so coverage is
    defined over this set: public methods and properties (underscore-private
    helpers and dunders are implementation details).
    """
    tree = ast.parse(wrapper_source)
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == wrapper_class:
            names = {item.name for item in node.body if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) and not item.name.startswith("_")}
            return sorted(names)
    return []


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


_PROPERTY_DECORATORS = {"property", "cached_property"}
_PROPERTY_ACCESSOR_DECORATORS = {"getter", "setter"}
_LEGACY_BINDING_HELPERS = {"_get_method_or_property", "_set_method_or_property"}


def _is_python_property_accessor(node: ast.AST) -> bool:
    """Return True when a function is a ``@property`` getter or setter."""
    if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return False
    for decorator in node.decorator_list:
        if isinstance(decorator, ast.Name) and decorator.id in _PROPERTY_DECORATORS:
            return True
        if isinstance(decorator, ast.Attribute) and decorator.attr in _PROPERTY_ACCESSOR_DECORATORS:
            return True
    return False


def _collect_bindings(root_node: ast.AST) -> List[Tuple[str, str, int]]:
    """Extract (com_member, expected_shape, call_arity) triples from one subtree.

    Recognised binding forms (per AGENTS.md / SKILL §3):
      * ``self.call_com(lambda: self._com.Name(...))`` -> ("Name", "method", arg_count)
      * ``self.get_com_property(self._com, "Name")``  -> ("Name", "property", 0)
      * ``self.set_com_property(self._com, "Name", ...)`` -> ("Name", "property", 0)

    ``call_arity`` is the number of arguments the lambda passes to the COM
    member (0 for property access, which passes no positional COM arguments).
    Any ``call_com`` / ``get_com_property`` / ``set_com_property`` attribute
    call is recognised -- in synced wrappers these are the classmethods
    inherited from ``ComHelper`` via ``self.`` -- because the call target is
    not what determines the COM member; the lambda body / property argument is.
    """
    bindings: List[Tuple[str, str, int]] = []
    for candidate in ast.walk(root_node):
        if not isinstance(candidate, ast.Call) or not isinstance(candidate.func, ast.Attribute):
            continue
        attr = candidate.func.attr
        if attr == "call_com" and candidate.args:
            lam = candidate.args[0]
            if isinstance(lam, ast.Lambda) and isinstance(lam.body, ast.Call) and isinstance(lam.body.func, ast.Attribute):
                if isinstance(lam.body.func.value, ast.Attribute) and lam.body.func.value.attr == "_com":
                    bindings.append((lam.body.func.attr, "method", len(lam.body.args)))
        elif attr in ("get_com_property", "set_com_property") and len(candidate.args) >= 2:
            arg = candidate.args[1]
            if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                bindings.append((arg.value, "property", 0))
    return bindings


def parse_wrapper_bindings(wrapper_source: str) -> List[Tuple[str, str, int]]:
    """Extract every synced COM binding in a wrapper module."""
    return _collect_bindings(ast.parse(wrapper_source))


def verify_wrapper_bindings(root: Path, interface_name: str, wrapper_source: str) -> List[str]:
    """Check every wrapper COM binding against the committed pywin32 catalog.

    A wrapper member must forward to exactly one pywin32-exposed member, with a
    method-shaped member called via ``call_com`` and a property-shaped member
    read/written via ``get_com_property`` / ``set_com_property``. Names are
    matched case-insensitively (COM identifiers are case-insensitive and the
    catalog preserves the type library's PascalCase). A member absent from the
    catalog, or bound with the wrong shape, is a sync defect and fails Step 8.
    The Python-facing shape must follow the catalog too: a property-shaped
    member is exposed as ``@property`` and a method-shaped member is not.
    Direct ``self._com.<Name>`` access and the legacy
    ``_get_method_or_property`` / ``_set_method_or_property`` probes are
    forbidden. When the authority carries a ``signatures`` section, a method
    binding whose call arity falls outside the declared parameter band
    (``required``..``count``) fails Step 8 as well — a correct member name with
    the wrong argument count still fails at runtime. Members without a
    committed signature are checked for existence and shape only.
    """
    catalog_path = root / "docs" / "reports" / "pywin32_authority.json"
    if not catalog_path.is_file():
        return [f"pywin32 authority catalog not found: {catalog_path}"]
    authority_data = json.loads(catalog_path.read_text(encoding="utf-8"))
    entries = authority_data.get("catalog", {}).get(interface_name)
    if entries is None:
        return [f"pywin32 catalog has no entry for {interface_name}"]
    lowered = {str(name).lower(): (name, shape) for name, shape in entries.items()}
    lowered_signatures = {str(name).lower(): sig for name, sig in authority_data.get("signatures", {}).get(interface_name, {}).items()}
    issues: List[str] = []

    def check_binding(owner: ast.AST, member: str, shape: str, arity: int) -> None:
        found = lowered.get(member.lower())
        if found is None:
            issues.append(f"{interface_name} binding '{member}' is absent from the pywin32 catalog")
            return
        if found[1] != shape:
            issues.append(f"{interface_name} binding '{member}' is {shape}-shaped in the wrapper but the pywin32 catalog declares '{found[0]}' as {found[1]}")
            return
        if isinstance(owner, (ast.FunctionDef, ast.AsyncFunctionDef)):
            is_property = _is_python_property_accessor(owner)
            if shape == "property" and not is_property:
                issues.append(f"{interface_name} member '{owner.name}' binds property-shaped COM member '{found[0]}' but is not a Python @property (SKILL section 3)")
            elif shape == "method" and is_property:
                issues.append(f"{interface_name} member '{owner.name}' is a Python @property but binds method-shaped COM member '{found[0]}' (SKILL section 3)")
        if shape != "method":
            return
        signature = lowered_signatures.get(member.lower())
        count_val = signature.get("count") if isinstance(signature, dict) else None
        if not isinstance(count_val, int):
            return
        required_val = signature.get("required")
        required = int(required_val) if isinstance(required_val, int) else int(count_val)
        if arity > int(count_val) or arity < required:
            issues.append(f"{interface_name} binding '{member}' has call arity {arity} but the pywin32 signature declares {int(count_val)} parameter(s) ({required} required)")

    tree = ast.parse(wrapper_source)
    for class_node in (node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)):
        for function in class_node.body:
            if not isinstance(function, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            for member, shape, arity in _collect_bindings(function):
                check_binding(function, member, shape, arity)

    for candidate in ast.walk(tree):
        if isinstance(candidate, ast.Call) and isinstance(candidate.func, ast.Attribute) and candidate.func.attr in _LEGACY_BINDING_HELPERS:
            issues.append(f"{interface_name} uses legacy {candidate.func.attr} at line {candidate.lineno}; bind exactly one pywin32 member (SKILL section 4)")

    call_com_nodes: Set[int] = set()
    for candidate in ast.walk(tree):
        if isinstance(candidate, ast.Call) and isinstance(candidate.func, ast.Attribute) and candidate.func.attr == "call_com" and candidate.args:
            if isinstance(candidate.args[0], ast.Lambda):
                for inner in ast.walk(candidate.args[0]):
                    call_com_nodes.add(id(inner))
    for candidate in ast.walk(tree):
        if not isinstance(candidate, ast.Attribute) or id(candidate) in call_com_nodes:
            continue
        if not isinstance(candidate.value, ast.Attribute) or candidate.value.attr != "_com":
            continue
        if not isinstance(candidate.value.value, ast.Name) or candidate.value.value.id != "self":
            continue
        issues.append(f"{interface_name} accesses self._com.{candidate.attr} directly at line {candidate.lineno}; use call_com or the property helpers (SKILL section 3)")
    return issues


def verify_integration_exception_catches(test_source: str) -> List[str]:
    """Integration tests may only assert NotImplementedError (Java-only stubs).

    Any other exception assertion (pytest.raises(AttributeError,
    RhapsodyRuntimeException, TypeError, ValueError, ...) blesses a wrong
    binding and is forbidden by SKILL section 5. try/except handlers in test
    bodies are likewise forbidden — a caught failure masquerades as a pass —
    while try/finally cleanup without an except clause stays allowed (the
    canonical mirrored integration tests rely on it for object cleanup).
    """
    issues: List[str] = []
    tree = ast.parse(test_source)
    allowed = {"NotImplementedError"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Try) and node.handlers:
            issues.append(f"try/except handler at line {node.lineno} catches exceptions in an integration test (SKILL section 5); assert the real outcome or record a blocker")
        if not isinstance(node, ast.With):
            continue
        for item in node.items:
            ce = item.context_expr
            if not (isinstance(ce, ast.Call) and isinstance(ce.func, ast.Attribute) and ce.func.attr == "raises"):
                continue
            if not ce.args:
                issues.append(f"pytest.raises() with no exception type at line {node.lineno}")
                continue
            exc_node = ce.args[0]
            if isinstance(exc_node, ast.Name):
                names = {exc_node.id}
            elif isinstance(exc_node, ast.Tuple):
                names = {e.id for e in exc_node.elts if isinstance(e, ast.Name)}
            else:
                names = set()
            bad = names - allowed
            if bad:
                issues.append(f"integration test asserts disallowed exception(s) {sorted(bad)} at line {node.lineno} (only NotImplementedError for JavaDoc-defined/pywin32-absent stubs is allowed)")
    return issues


_FORBIDDEN_TEST_MARKERS = {"skip", "xfail"}


def _forbidden_marker_name(node: ast.AST) -> Optional[str]:
    """Return ``skip``/``xfail`` for a ``<module>.mark.<name>`` decorator."""
    target = node.func if isinstance(node, ast.Call) else node
    if not isinstance(target, ast.Attribute) or target.attr not in _FORBIDDEN_TEST_MARKERS:
        return None
    if isinstance(target.value, ast.Attribute) and target.value.attr == "mark":
        return target.attr
    return None


def _has_nonempty_skip_reason(decorator: ast.AST) -> bool:
    """Return whether a ``@pytest.mark.skip`` decorator carries ``reason="..."``."""
    if not isinstance(decorator, ast.Call):
        return False
    for keyword in decorator.keywords:
        if keyword.arg != "reason":
            continue
        return isinstance(keyword.value, ast.Constant) and isinstance(keyword.value.value, str) and bool(keyword.value.value.strip())
    return False


def verify_no_skip_or_xfail(path: Path, allow_reasoned_skip: bool = False) -> List[str]:
    """Model-class tests must run: no xfail, runtime skip, or unexplained skip.

    SKILL section 4 forbids ``pytest.xfail``, ``pytest.skip(...)``, and
    ``pytest.xfail(...)`` outright, and forbids skip markers in unit tests.
    An integration test may carry ``@pytest.mark.skip(reason="...")`` only with
    explicit user approval and a ledger entry; the machine check enforces the
    non-empty reason, while the approval and ledger check remain manual.
    """
    issues: List[str] = []
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            for decorator in node.decorator_list:
                marker = _forbidden_marker_name(decorator)
                if marker is None:
                    continue
                if marker == "skip" and allow_reasoned_skip and _has_nonempty_skip_reason(decorator):
                    continue
                issues.append(f"pytest.mark.{marker} at line {node.lineno} is forbidden in a model-class test (SKILL section 4); fix the fixture or record a blocker")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in _FORBIDDEN_TEST_MARKERS:
            receiver = node.func.value
            if isinstance(receiver, ast.Name) and receiver.id == "pytest":
                issues.append(f"pytest.{node.func.attr}() at line {node.lineno} is forbidden in a model-class test (SKILL section 4); fix the fixture or record a blocker")
    return issues


def verify_no_empty_finally(path: Path) -> List[str]:
    """A ``finally`` block must perform real cleanup, not just ``pass``.

    SKILL section 5 forbids a ``finally: pass`` shell: it looks like cleanup
    while leaving the created objects in the session-shared project.
    ``try``/``finally`` blocks with at least one real statement stay allowed.
    """
    issues: List[str] = []
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if not isinstance(node, ast.Try) or not node.finalbody:
            continue
        if all(isinstance(statement, ast.Pass) for statement in node.finalbody):
            issues.append(f"finally block at line {node.lineno} contains only 'pass' (SKILL section 5); clean up the created objects or record a blocker")
    return issues


def _owned_property_names(wrapper_source: str) -> Set[str]:
    tree = ast.parse(wrapper_source)
    names: Set[str] = set()
    for node in ast.walk(tree):
        if _is_python_property_accessor(node):
            names.add(node.name)
    return names


def _is_empty_collection_literal(expression: ast.expr) -> bool:
    """Return whether the expression is a literal empty list/tuple/set/dict."""
    if isinstance(expression, ast.Dict):
        return not expression.keys
    if isinstance(expression, (ast.List, ast.Tuple, ast.Set)):
        return not expression.elts
    return False


def _is_weak_getter_assertion(expression: ast.expr) -> bool:
    """Return whether an assertion proves only non-None/type/count/truthiness."""
    if isinstance(expression, ast.Constant):
        return True
    if isinstance(expression, ast.UnaryOp) and isinstance(expression.op, ast.Not):
        return True
    if isinstance(expression, ast.Compare):
        if len(expression.ops) == 1 and isinstance(expression.ops[0], ast.IsNot):
            comparator = expression.comparators[0]
            return isinstance(comparator, ast.Constant) and comparator.value is None
        if any(_is_empty_collection_literal(comparator) for comparator in expression.comparators):
            return True
        if len(expression.ops) == 1 and isinstance(expression.ops[0], ast.GtE):
            comparator = expression.comparators[0]
            if isinstance(comparator, ast.Constant) and comparator.value == 0:
                return True
        operands = [expression.left, *expression.comparators]
        return any(isinstance(operand, ast.Call) and isinstance(operand.func, ast.Name) and operand.func.id == "len" for operand in operands)
    if isinstance(expression, ast.Call):
        return isinstance(expression.func, ast.Name) and expression.func.id == "isinstance"
    return isinstance(expression, (ast.Name, ast.Attribute))


_GETTER_TEST_SUFFIXES = ("_empty_state", "_empty")


def _getter_property_for_test(test_name: str, property_names: Set[str]) -> Optional[str]:
    """Map ``test_<property>`` / ``test_get_<property>[_empty]`` to a wrapper property."""
    if not test_name.startswith("test_"):
        return None
    member = test_name[len("test_") :]
    if member.startswith("get_"):
        member = member[len("get_") :]
    for suffix in _GETTER_TEST_SUFFIXES:
        if member.endswith(suffix):
            member = member[: -len(suffix)]
            break
    return member if member in property_names else None


def _collect_getter_coverage(path: Path, property_names: Set[str]) -> Dict[str, List[Tuple[str, int, bool]]]:
    """Map each owned property to its integration tests and whether they are weak."""
    coverage: Dict[str, List[Tuple[str, int, bool]]] = {}
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        member = _getter_property_for_test(node.name, property_names)
        if member is None:
            continue
        assertions = [statement for statement in ast.walk(node) if isinstance(statement, ast.Assert)]
        weak = not assertions or all(_is_weak_getter_assertion(assertion.test) for assertion in assertions)
        coverage.setdefault(member, []).append((node.name, node.lineno, weak))
    return coverage


_BLOCKER_HEADING = "## P0 integration-test blockers"


def _parse_blocker_members(root: Path, interface_name: str) -> Set[str]:
    """Return backticked member names recorded as blockers for one interface."""
    path = getter_matrix_path(root).parent / "index.md"
    if not path.is_file():
        return set()
    lines = path.read_text(encoding="utf-8").splitlines()
    start = next((index for index, line in enumerate(lines) if line.strip().startswith(_BLOCKER_HEADING)), None)
    if start is None:
        return set()
    members: Set[str] = set()
    for line in lines[start + 1 :]:
        if line.startswith("## "):
            break
        cells = _split_table_row(line)
        if cells is None or len(cells) < 2 or cells[0].strip() != interface_name:
            continue
        members.update(re.findall(r"`([^`]+)`", cells[1]))
    return members


def verify_getter_assertions(path: Path, property_names: Set[str], blocked: Optional[Set[str]] = None) -> List[str]:
    """Reject getter properties covered only by non-None/type/count/empty assertions.

    SKILL section 5 requires at least one getter integration test per property
    that creates the real related object and asserts identity or value. An
    empty-state test (``test_<property>_empty``) is an additional case, not a
    substitute, so a property fails when every matching test is weak.
    """
    issues: List[str] = []
    for member, tests in _collect_getter_coverage(path, property_names).items():
        if member in (blocked or set()):
            continue
        if all(weak for _, _, weak in tests):
            names = ", ".join(f"{name} (line {lineno})" for name, lineno, _ in tests)
            issues.append(f"getter {member!r} is only covered by weak assertions: {names}; create the related object and assert identity/value (SKILL section 5)")
    return issues


_GETTER_MATRIX_RELATIVE = Path("docs") / "reports" / "sync-todo" / "getter-matrix.md"
_GETTER_MATRIX_HEADER = "| Java getter / Python member | Integration test | Assertion | Status |"
_GETTER_MATRIX_SEPARATOR = "| --- | --- | --- | --- |"
_MATRIX_ASSERTION_STATUS = {"identity/value": "OK", "weak": "WEAK", "none": "MISSING"}
_GETTER_MATRIX_PREAMBLE = (
    "# Getter fixture matrix\n\n"
    "Machine-readable record of one integration test per owned getter, checked by `verify_sync.py` Step 8.\n"
    "Regenerate an interface section with\n"
    "`python .agents/skills/rhapsody-sync/scripts/verify_sync.py <INTERFACE> --write-getter-matrix`,\n"
    "then replace a `MISSING` or `WEAK` row with the test that really asserts the getter.\n"
)


def getter_matrix_path(root: Path) -> Path:
    """Return the committed machine-readable Getter fixture matrix path."""
    return root / _GETTER_MATRIX_RELATIVE


def _relative_to_root(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def _getter_matrix_rows(root: Path, test_path: Path, property_names: Set[str]) -> Dict[str, Tuple[str, str, str]]:
    """Derive (test reference, assertion kind, status) for every owned property."""
    coverage = _collect_getter_coverage(test_path, property_names) if test_path.is_file() else {}
    relative_test = _relative_to_root(root, test_path)
    rows: Dict[str, Tuple[str, str, str]] = {}
    for prop in sorted(property_names):
        tests = coverage.get(prop, [])
        strong = [name for name, _, weak in tests if not weak]
        if strong:
            rows[prop] = (f"{relative_test}::{strong[0]}", "identity/value", "OK")
        elif tests:
            rows[prop] = (f"{relative_test}::{tests[0][0]}", "weak", "WEAK")
        else:
            rows[prop] = ("—", "none", "MISSING")
    return rows


def render_getter_matrix_section(root: Path, interface_name: str, property_names: Set[str], test_path: Path) -> str:
    """Render the ``## <INTERFACE>`` matrix section for one wrapper."""
    lines = [f"## {interface_name}", "", _GETTER_MATRIX_HEADER, _GETTER_MATRIX_SEPARATOR]
    for prop, (test_ref, assertion, status) in _getter_matrix_rows(root, test_path, property_names).items():
        test_cell = f"`{test_ref}`" if test_ref != "—" else "—"
        lines.append(f"| `{prop}` | {test_cell} | {assertion} | {status} |")
    return "\n".join(lines) + "\n"


def _extract_matrix_section(text: str, interface_name: str) -> Optional[str]:
    lines = text.splitlines()
    marker = f"## {interface_name}"
    start: Optional[int] = None
    for index, line in enumerate(lines):
        if line.strip() == marker:
            start = index + 1
            break
    if start is None:
        return None
    end = len(lines)
    for index in range(start, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break
    return "\n".join(lines[start:end])


def _parse_matrix_rows(section: str) -> Dict[str, Tuple[str, str, str]]:
    rows: Dict[str, Tuple[str, str, str]] = {}
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) < 4 or cells[0] == "Java getter / Python member" or set(cells[0]) <= {"-", ":", " "}:
            continue
        prop = cells[0].strip("`").strip()
        test_ref = cells[1].strip("`").strip() if cells[1].startswith("`") else cells[1]
        rows[prop] = (test_ref, cells[2], cells[3])
    return rows


def upsert_getter_matrix_section(root: Path, interface_name: str, section: str) -> Path:
    """Insert or replace one interface section, preserving every other section."""
    path = getter_matrix_path(root)
    text = path.read_text(encoding="utf-8") if path.is_file() else _GETTER_MATRIX_PREAMBLE
    lines = text.rstrip("\n").splitlines()
    marker = f"## {interface_name}"
    start: Optional[int] = None
    for index, line in enumerate(lines):
        if line.strip() == marker:
            start = index
            break
    section_lines = section.rstrip("\n").splitlines()
    if start is None:
        lines = lines + [""] + section_lines
    else:
        end = len(lines)
        for index in range(start + 1, len(lines)):
            if lines[index].startswith("## "):
                end = index
                break
        lines = lines[:start] + section_lines + [""] + lines[end:]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(re.sub(r"\n{3,}", "\n\n", "\n".join(lines)) + "\n", encoding="utf-8")
    return path


def verify_getter_matrix(root: Path, interface_name: str, property_names: Set[str], test_path: Path, strict: bool = False, blocked: Optional[Set[str]] = None) -> List[str]:
    """Check the committed Getter fixture matrix covers every owned getter.

    The matrix is a machine-readable companion to SKILL section 1: one row per
    owned property, an assertion kind (``identity/value``, ``weak``, ``none``),
    a status consistent with that kind, and an integration test reference that
    resolves to a real test. Coverage status itself is reported by
    ``verify_getter_assertions``; this check owns structure, staleness, and
    dangling references.
    """
    if not property_names:
        return []
    hint = f"run `python .agents/skills/rhapsody-sync/scripts/verify_sync.py {interface_name} --write-getter-matrix`"
    matrix_path = getter_matrix_path(root)
    if not matrix_path.is_file():
        return [f"Getter fixture matrix not found: {matrix_path}; {hint}"]
    section = _extract_matrix_section(matrix_path.read_text(encoding="utf-8"), interface_name)
    if section is None:
        return [f"Getter fixture matrix has no '## {interface_name}' section; {hint}"]
    rows = _parse_matrix_rows(section)
    issues: List[str] = []
    for prop in sorted(property_names):
        if prop not in rows:
            issues.append(f"Getter fixture matrix is missing a row for {interface_name}.{prop}; {hint}")
    for prop in sorted(set(rows) - set(property_names)):
        issues.append(f"Getter fixture matrix has a stale row for {interface_name}.{prop}: the wrapper no longer exposes that property; {hint}")
    for prop, (test_ref, assertion, status) in rows.items():
        expected_status = _MATRIX_ASSERTION_STATUS.get(assertion)
        if expected_status is None:
            issues.append(f"Getter fixture matrix row {interface_name}.{prop} has an unknown assertion '{assertion}' (expected identity/value, weak, or none)")
            continue
        if strict and assertion in {"weak", "none"} and prop not in (blocked or set()):
            issues.append(f"Getter fixture matrix row {interface_name}.{prop} is '{assertion}' but not recorded as a blocker; add a populated test or a blocker row in index.md")
        if status != expected_status:
            issues.append(f"Getter fixture matrix row {interface_name}.{prop} records status '{status}' for assertion '{assertion}'; expected '{expected_status}'")
        if test_ref == "—":
            continue
        file_part, _, test_name = test_ref.partition("::")
        test_file = root / file_part
        if not test_file.is_file():
            issues.append(f"Getter fixture matrix row {interface_name}.{prop} references a missing test file: {file_part}")
        elif test_name and test_name not in test_file.read_text(encoding="utf-8"):
            issues.append(f"Getter fixture matrix row {interface_name}.{prop} references a missing test: {test_ref}")
    return issues


def _find_integration_test(root: Path, wrapper_path: Path, interface_name: str) -> Path:
    """Resolve the mirrored integration test path for a wrapper, existing or not."""
    java_snake = _java_interface_snake(interface_name)
    stems = [wrapper_path.stem] if wrapper_path.stem == java_snake else [wrapper_path.stem, java_snake]
    try:
        rel_parent = wrapper_path.parent.relative_to(root / "src" / "rhapsody_cli")
    except ValueError:
        rel_parent = Path()
    if rel_parent.parts and rel_parent.parts[0] == "models":
        test_dir = root / "tests" / "integration" / rel_parent
    else:
        test_dir = root / "tests" / "integration"
    for stem in stems:
        candidate = test_dir / f"test_{stem}.py"
        if candidate.is_file():
            return candidate
    return test_dir / f"test_{stems[0]}.py"


def write_getter_matrix(root: Path, interface_name: str, report_path: Path) -> Path:
    """Regenerate one interface's matrix section from the wrapper and its tests."""
    simple_name, _java_package, _java_doc = find_java_doc(root, interface_name)
    _wrapper_class, source_path = parse_report_target(report_path.read_text(encoding="utf-8"))
    wrapper_path, _canonical = _canonical_import(root, source_path)
    property_names = _owned_property_names(wrapper_path.read_text(encoding="utf-8")) if wrapper_path.is_file() else set()
    test_path = _find_integration_test(root, wrapper_path, simple_name)
    section = render_getter_matrix_section(root, simple_name, property_names, test_path)
    return upsert_getter_matrix_section(root, simple_name, section)


_GETTER_DIFF_RELATIVE = Path("docs") / "reports" / "sync-todo" / "getter-catalog-diff.md"
_GETTER_DIFF_HEADER = "| Python getter | COM member | Binding shape | Catalog shape | Status |"
_GETTER_DIFF_SEPARATOR = "| --- | --- | --- | --- | --- |"
_GETTER_DIFF_CATALOG_HEADER = "| Catalog property | Derived Python name | Status |"
_GETTER_DIFF_CATALOG_SEPARATOR = "| --- | --- | --- |"
_GETTER_DIFF_STATUSES = ("match", "catalog-missing", "shape-mismatch", "no-binding", "stub", "catalog-only")
_GETTER_DIFF_MISSING = "—"
_GETTER_DIFF_PREAMBLE = (
    "# Getter implementation vs pywin32 catalog\n\n"
    "Per-owned-getter comparison of the Python binding against `docs/reports/pywin32_authority.json`.\n"
    "Regenerate one interface section with\n"
    "`python .agents/skills/rhapsody-sync/scripts/verify_sync.py <INTERFACE> --write-getter-diff`.\n\n"
    "Statuses: `match` — the bound COM member exists with the catalog's shape; `catalog-missing` — the bound member is absent\n"
    "from the catalog; `shape-mismatch` — the binding form differs from the catalog shape; `no-binding` — the property is pure\n"
    "Python; `stub` — the property raises `NotImplementedError` (see the stub evidence ledger); `catalog-only` — a catalog\n"
    "property has no Python property with the derived snake_case name anywhere in the wrapper MRO, a candidate gap for human\n"
    "review rather than a failure.\n\n"
    "## Summary\n\n"
    "| Status | Count |\n"
    "| --- | --- |\n"
    "| match | 0 |\n"
    "| catalog-missing | 0 |\n"
    "| shape-mismatch | 0 |\n"
    "| no-binding | 0 |\n"
    "| stub | 0 |\n"
    "| catalog-only | 0 |\n"
)


def getter_catalog_diff_path(root: Path) -> Path:
    """Return the committed Getter implementation-vs-catalog diff report path."""
    return root / _GETTER_DIFF_RELATIVE


def _property_getter_nodes(wrapper_source: str) -> List[Tuple[str, ast.AST]]:
    """Return the ``@property`` getter names and nodes declared in a wrapper module."""
    getters: List[Tuple[str, ast.AST]] = []
    tree = ast.parse(wrapper_source)
    for class_node in (node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)):
        for function in class_node.body:
            if not isinstance(function, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            decorators = {getattr(decorator, "id", None) or getattr(decorator, "attr", None) for decorator in function.decorator_list}
            if decorators & _PROPERTY_DECORATORS:
                getters.append((function.name, function))
    return getters


def _diff_code_cell(value: str) -> str:
    return _GETTER_DIFF_MISSING if value == _GETTER_DIFF_MISSING else f"`{value}`"


def _getter_diff_binding_rows(wrapper_source: str, catalog: Dict[str, str]) -> List[Tuple[str, str, str, str, str]]:
    """Return (Python getter, COM member, binding shape, catalog shape, status) rows."""
    lowered = {str(name).lower(): (str(name), str(shape)) for name, shape in catalog.items()}
    rows: List[Tuple[str, str, str, str, str]] = []
    for name, getter in _property_getter_nodes(wrapper_source):
        bindings = _collect_bindings(getter)
        if not bindings:
            status = "stub" if any(_raises_not_implemented(candidate) for candidate in ast.walk(getter)) else "no-binding"
            rows.append((name, _GETTER_DIFF_MISSING, _GETTER_DIFF_MISSING, _GETTER_DIFF_MISSING, status))
            continue
        for member, shape, _arity in bindings:
            found = lowered.get(member.lower())
            if found is None:
                rows.append((name, member, shape, _GETTER_DIFF_MISSING, "catalog-missing"))
            elif found[1] != shape:
                rows.append((name, member, shape, found[1], "shape-mismatch"))
            else:
                rows.append((name, found[0], shape, found[1], "match"))
    return rows


def _base_class_name(node: ast.expr) -> Optional[str]:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    if isinstance(node, ast.Subscript):
        return _base_class_name(node.value)
    return None


def _wrapper_class_index(root: Path) -> Dict[str, List[Tuple[Set[str], List[str]]]]:
    """Index every model wrapper class by name: (property names, base class names)."""
    index: Dict[str, List[Tuple[Set[str], List[str]]]] = {}
    models_root = root / "src" / "rhapsody_cli" / "models"
    if not models_root.is_dir():
        return index
    for path in sorted(models_root.rglob("*.py")):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except (OSError, SyntaxError, UnicodeDecodeError):
            continue
        for class_node in (node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)):
            properties: Set[str] = set()
            for function in class_node.body:
                if not isinstance(function, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                decorators = {getattr(decorator, "id", None) or getattr(decorator, "attr", None) for decorator in function.decorator_list}
                if decorators & _PROPERTY_DECORATORS:
                    properties.add(function.name)
            bases = [name for name in (_base_class_name(base) for base in class_node.bases) if name]
            index.setdefault(class_node.name, []).append((properties, bases))
    return index


def _mro_property_names(index: Dict[str, List[Tuple[Set[str], List[str]]]], class_name: str, seen: Optional[Set[str]] = None) -> Set[str]:
    """Return property names declared by a class and its resolvable in-repo bases."""
    visited = seen if seen is not None else set()
    if class_name in visited:
        return set()
    visited.add(class_name)
    names: Set[str] = set()
    for properties, bases in index.get(class_name, []):
        names |= properties
        for base in bases:
            names |= _mro_property_names(index, base, visited)
    return names


# Documented naming drift: catalog property name -> actual Python property name.
# These are deliberately not "catalog-only" gaps because the wrapper exposes the
# value under a different snake_case name.
_CATALOG_NAME_ALIASES: Dict[str, Dict[str, str]] = {
    "IRPOperation": {"return_type": "returns"},
}

# Catalog properties with no own-JavaDoc declaration on the interface and no
# Python property by design. Recorded per interface; verified 2026-11-25 that
# IRPArgument/IRPAttribute/IRPPort do not declare these in their own JavaDoc,
# and IRPCollection exposes Items through get_item/count/iteration instead.
_CATALOG_NOT_APPLICABLE: Dict[str, Set[str]] = {
    "IRPArgument": {"declaration", "defaultValue", "type", "typeOf", "valueSpecifications"},
    "IRPAttribute": {"declaration", "defaultValue", "type", "typeOf", "valueSpecifications"},
    "IRPCollection": {"Items", "interfaceName"},
    "IRPPort": {
        "ObjectAsObjectType",
        "instantiatedBy",
        "inverse",
        "isNavigable",
        "isSymmetric",
        "multiplicity",
        "ofClass",
        "otherClass",
        "qualifier",
        "relationLabel",
        "relationLinkName",
        "relationRoleName",
        "relationType",
        "visibility",
    },
}


def _catalog_only_properties(index: Dict[str, List[Tuple[Set[str], List[str]]]], wrapper_class: str, catalog: Dict[str, str]) -> List[Tuple[str, str]]:
    """Return catalog properties with no derived-name Python property in the wrapper MRO."""
    known = _mro_property_names(index, wrapper_class)
    aliases = _CATALOG_NAME_ALIASES.get(wrapper_class, {})
    not_applicable = {name.casefold() for name in _CATALOG_NOT_APPLICABLE.get(wrapper_class, set())}
    candidates: List[Tuple[str, str]] = []
    for member, shape in catalog.items():
        if str(shape) != "property":
            continue
        derived = _java_interface_snake(str(member))
        if derived in known or aliases.get(derived) in known:
            continue
        if str(member).casefold() in not_applicable:
            continue
        candidates.append((str(member), derived))
    return sorted(candidates)


def render_getter_catalog_diff_section(root: Path, interface_name: str, wrapper_class: str, wrapper_source: str, catalog: Dict[str, str]) -> str:
    """Render the ``## <INTERFACE>`` diff section for one wrapper."""
    lines = [f"## {interface_name}", "", _GETTER_DIFF_HEADER, _GETTER_DIFF_SEPARATOR]
    for name, member, shape, catalog_shape, status in _getter_diff_binding_rows(wrapper_source, catalog):
        lines.append(f"| {_diff_code_cell(name)} | {_diff_code_cell(member)} | {shape} | {catalog_shape} | {status} |")
    lines.extend(["", "### Catalog properties with no matching Python property", "", _GETTER_DIFF_CATALOG_HEADER, _GETTER_DIFF_CATALOG_SEPARATOR])
    candidates = _catalog_only_properties(_wrapper_class_index(root), wrapper_class, catalog)
    if candidates:
        lines.extend(f"| `{member}` | `{derived}` | catalog-only |" for member, derived in candidates)
    else:
        lines.append(f"| {_GETTER_DIFF_MISSING} | {_GETTER_DIFF_MISSING} | {_GETTER_DIFF_MISSING} |")
    return "\n".join(lines) + "\n"


def _getter_catalog_diff_counts(text: str) -> Dict[str, int]:
    counts = {status: 0 for status in _GETTER_DIFF_STATUSES}
    for line in text.splitlines():
        cells = _split_table_row(line)
        if cells is None or cells[-1] not in counts:
            continue
        if len(cells) == 5 or (len(cells) == 3 and cells[-1] == "catalog-only"):
            counts[cells[-1]] += 1
    return counts


def _rewrite_getter_catalog_diff_summary(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    start: Optional[int] = None
    for index, line in enumerate(lines):
        if line.strip() == "## Summary":
            start = index
            break
    if start is None:
        return
    end = len(lines)
    for index in range(start + 1, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break
    counts = _getter_catalog_diff_counts(text)
    summary = ["## Summary", "", "| Status | Count |", "| --- | --- |"]
    summary.extend(f"| {status} | {counts[status]} |" for status in _GETTER_DIFF_STATUSES)
    lines = lines[:start] + summary + [""] + lines[end:]
    path.write_text(re.sub(r"\n{3,}", "\n\n", "\n".join(lines)) + "\n", encoding="utf-8")


def upsert_getter_catalog_diff_section(root: Path, interface_name: str, section: str) -> Path:
    """Insert or replace one interface diff section, then refresh the summary."""
    path = getter_catalog_diff_path(root)
    text = path.read_text(encoding="utf-8") if path.is_file() else _GETTER_DIFF_PREAMBLE
    lines = text.rstrip("\n").splitlines()
    marker = f"## {interface_name}"
    start: Optional[int] = None
    for index, line in enumerate(lines):
        if line.strip() == marker:
            start = index
            break
    section_lines = section.rstrip("\n").splitlines()
    if start is None:
        lines = lines + [""] + section_lines
    else:
        end = len(lines)
        for index in range(start + 1, len(lines)):
            if lines[index].startswith("## "):
                end = index
                break
        lines = lines[:start] + section_lines + [""] + lines[end:]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(re.sub(r"\n{3,}", "\n\n", "\n".join(lines)) + "\n", encoding="utf-8")
    _rewrite_getter_catalog_diff_summary(path)
    return path


def write_getter_catalog_diff(root: Path, interface_name: str, report_path: Path) -> Path:
    """Regenerate one interface's getter-vs-catalog diff section."""
    simple_name, _package = split_interface_name(interface_name)
    wrapper_class, source_path = parse_report_target(report_path.read_text(encoding="utf-8"))
    wrapper_path, _canonical = _canonical_import(root, source_path)
    if not wrapper_path.is_file():
        raise FileNotFoundError(f"Wrapper source does not exist: {wrapper_path}")
    authority = json.loads((root / "docs" / "reports" / "pywin32_authority.json").read_text(encoding="utf-8"))
    catalog = authority.get("catalog", {}).get(simple_name, {})
    if not isinstance(catalog, dict) or not catalog:
        raise ValueError(f"pywin32 catalog has no entry for {simple_name}")
    section = render_getter_catalog_diff_section(root, simple_name, wrapper_class, wrapper_path.read_text(encoding="utf-8"), catalog)
    return upsert_getter_catalog_diff_section(root, simple_name, section)


_NOT_IMPLEMENTED_LEDGER_RELATIVE = Path("docs") / "reports" / "sync-todo" / "index.md"
_NOT_IMPLEMENTED_LEDGER_HEADING = "## NotImplementedError stubs"
_NOT_IMPLEMENTED_BASES = {"not-exposed", "java-doc-unimplemented", "runtime-stub"}
_ISO_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_COM_REFERENCE_PATTERN = re.compile(r"::(\w+)\(")


def _raises_not_implemented(node: ast.AST) -> bool:
    """Return whether an AST node raises ``NotImplementedError`` directly."""
    return isinstance(node, ast.Raise) and isinstance(node.exc, ast.Call) and isinstance(node.exc.func, ast.Name) and node.exc.func.id == "NotImplementedError"


def _collect_not_implemented_stubs(wrapper_source: str) -> List[Tuple[str, str, str, str]]:
    """Return (Python member, COM member, docstring, class name) for every stub.

    The COM member comes from the docstring's ``Reference:
    com.telelogic...IRPX::member(...)`` line. Without that line a stub has no
    JavaDoc evidence and fails Step 8.
    """
    stubs: List[Tuple[str, str, str, str]] = []
    tree = ast.parse(wrapper_source)
    for class_node in (node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)):
        for function in class_node.body:
            if not isinstance(function, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if not any(_raises_not_implemented(candidate) for candidate in ast.walk(function)):
                continue
            docstring = ast.get_docstring(function) or ""
            reference = _COM_REFERENCE_PATTERN.search(docstring)
            stubs.append((function.name, reference.group(1) if reference else "", docstring, class_node.name))
    return stubs


def _split_table_row(line: str) -> Optional[List[str]]:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return None
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def _accessor_property_names(member: str) -> List[str]:
    """Return a member plus the pywin32 property name of a get/set accessor."""
    names = [member]
    if len(member) > 3 and member[:3].lower() in {"get", "set"} and member[3].isupper():
        names.append(member[3].lower() + member[4:])
    return names


def _parse_not_implemented_ledger(root: Path, interface_name: str) -> Tuple[Dict[str, Tuple[str, str, str, str, str]], List[str]]:
    """Return this interface's ledger rows keyed by Python member and parse issues."""
    path = root / _NOT_IMPLEMENTED_LEDGER_RELATIVE
    if not path.is_file():
        return {}, [f"NotImplementedError evidence ledger not found: {path}"]
    lines = path.read_text(encoding="utf-8").splitlines()
    start: Optional[int] = None
    for index, line in enumerate(lines):
        if line.strip() == _NOT_IMPLEMENTED_LEDGER_HEADING:
            start = index + 1
            break
    if start is None:
        return {}, [f"{path} has no '{_NOT_IMPLEMENTED_LEDGER_HEADING}' section"]
    rows: Dict[str, Tuple[str, str, str, str, str]] = {}
    for line in lines[start:]:
        if line.startswith("## "):
            break
        cells = _split_table_row(line)
        if cells is None or len(cells) < 6:
            continue
        member = cells[1].strip("`").strip()
        if cells[0].strip("`").strip() != interface_name or not member or member == "Python member" or set(cells[0]) <= {"-", ":", " "}:
            continue
        rows[member] = (member, cells[2].strip("`").strip(), cells[3].strip().lower(), cells[4].strip(), cells[5].strip())
    return rows, []


def _test_asserts_not_implemented(path: Path, member: str) -> bool:
    """Return whether a test function asserts this stub raises NotImplementedError."""
    try:
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source)
    except (OSError, SyntaxError, UnicodeDecodeError):
        return False
    for function in (node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))):
        segment = ast.get_source_segment(source, function) or ""
        if member in segment and "NotImplementedError" in segment and "raises" in segment:
            return True
    return False


def verify_not_implemented_evidence(root: Path, interface_name: str, wrapper_source: str, unit_test_path: Optional[Path], integration_test_path: Optional[Path]) -> List[str]:
    """Check every NotImplementedError stub against its ledger evidence row.

    SKILL section 4 permits a stub only in one of three evidence states:
    ``not-exposed`` (the Java member is absent from the pywin32 catalog and is
    listed in ``documented_unavailable``), ``java-doc-unimplemented`` (JavaDoc
    itself declares the member unimplemented), or ``runtime-stub`` (pywin32
    exposes the member but the documented call is proven ineffective and the
    user approved the deviation with a date). ``docs/reports/sync-todo/index.md``
    records one row per stub; a missing row, a stale row, a basis inconsistent
    with the catalog, a runtime stub without an approval date, or a stub that
    neither mirrored test asserts fails Step 8.
    """
    stubs = _collect_not_implemented_stubs(wrapper_source)
    ledger_rows, parse_issues = _parse_not_implemented_ledger(root, interface_name)
    if not stubs:
        return [f"NotImplementedError evidence ledger row for {interface_name}.{member} is stale: the wrapper no longer raises NotImplementedError" for member in sorted(ledger_rows)]
    if parse_issues:
        return parse_issues

    catalog_path = root / "docs" / "reports" / "pywin32_authority.json"
    authority: object = json.loads(catalog_path.read_text(encoding="utf-8")) if catalog_path.is_file() else {}
    catalog: object = authority.get("catalog", {}).get(interface_name, {}) if isinstance(authority, dict) else {}
    unavailable: object = authority.get("documented_unavailable", {}).get(interface_name, []) if isinstance(authority, dict) else {}
    catalog_names = {str(name).lower(): str(name) for name in catalog} if isinstance(catalog, dict) else {}
    unavailable_names = {str(name).lower() for name in unavailable} if isinstance(unavailable, list) else set()

    issues: List[str] = []
    stub_members = {member for member, _, _, _ in stubs}
    for member in sorted(set(ledger_rows) - stub_members):
        issues.append(f"NotImplementedError evidence ledger row for {interface_name}.{member} is stale: the wrapper no longer raises NotImplementedError")

    for member, reference, docstring, _class_name in stubs:
        row = ledger_rows.get(member)
        if row is None:
            issues.append(f"{interface_name}.{member} raises NotImplementedError without an evidence row in {root / _NOT_IMPLEMENTED_LEDGER_RELATIVE}")
            continue
        _recorded, recorded_com, basis, evidence, approved = row
        if not reference:
            issues.append(f"{interface_name}.{member} stub docstring has no 'Reference: com.telelogic...::{member}(...)' line, so its JavaDoc member cannot be verified")
        elif recorded_com.lower() not in {name.lower() for name in _accessor_property_names(reference)}:
            issues.append(f"{interface_name}.{member} ledger records COM member '{recorded_com}' but its JavaDoc Reference names '{reference}'")
        if basis not in _NOT_IMPLEMENTED_BASES:
            issues.append(f"{interface_name}.{member} ledger basis '{basis}' is unknown (expected one of {', '.join(sorted(_NOT_IMPLEMENTED_BASES))})")
            continue
        if evidence in {"", "—", "-"}:
            issues.append(f"{interface_name}.{member} ledger has no evidence text")
        candidates = {name.lower() for name in _accessor_property_names(recorded_com or reference)}
        exposed = sorted(catalog_names[name] for name in candidates if name in catalog_names)
        exact_exposed = bool(reference) and reference.lower() in catalog_names
        if basis == "not-exposed":
            if reference and reference.lower() not in unavailable_names:
                issues.append(f"{interface_name}.{member} is recorded 'not-exposed' but '{reference}' is not listed in documented_unavailable")
            if exact_exposed:
                issues.append(f"{interface_name}.{member} is recorded 'not-exposed' but the catalog exposes '{catalog_names[reference.lower()]}'")
        elif basis == "runtime-stub":
            if reference and reference.lower() in unavailable_names:
                issues.append(f"{interface_name}.{member} is recorded 'runtime-stub' but '{reference}' is listed in documented_unavailable")
            if not exposed:
                issues.append(f"{interface_name}.{member} is recorded 'runtime-stub' but the catalog exposes no member among {', '.join(sorted(candidates))}")
            if not _ISO_DATE_PATTERN.match(approved):
                issues.append(f"{interface_name}.{member} runtime stub has no user approval date in the ledger (expected YYYY-MM-DD, found '{approved}')")
            if "pywin32" not in docstring.lower() and "catalog" not in docstring.lower():
                issues.append(f"{interface_name}.{member} runtime stub docstring does not cite the pywin32 catalog entry")
        else:
            if "not implemented" not in docstring.lower():
                issues.append(f"{interface_name}.{member} is recorded 'java-doc-unimplemented' but its docstring does not quote the JavaDoc's 'not implemented' statement")
            if not exposed:
                issues.append(f"{interface_name}.{member} is recorded 'java-doc-unimplemented' but the catalog exposes no member among {', '.join(sorted(candidates))}")
        for label, test_path in (("unit", unit_test_path), ("integration", integration_test_path)):
            if test_path is None or not _test_asserts_not_implemented(test_path, member):
                issues.append(f"{interface_name}.{member} stub is not asserted as pytest.raises(NotImplementedError) in the {label} test file")
    return issues


def verify_sync_artifacts(root: Path, interface_name: str, report_path: Path, strict_getters: bool = False) -> List[str]:
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
    wrapper_source = absolute_wrapper.read_text(encoding="utf-8") if absolute_wrapper.is_file() else ""

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
    owned_properties = _owned_property_names(wrapper_source) if wrapper_source else set()
    test_paths: Dict[str, Path] = {}
    blockers = _parse_blocker_members(root, simple_name)
    for label, test_base in (("Unit", "unit"), ("Integration", "integration")):
        test_dir = root / "tests" / test_base / model_segment
        test_path = first_existing(test_dir, "test_{stem}.py")
        if test_path is None:
            issues.append(f"{label} test file not found for {simple_name}: {test_dir / f'test_{class_stem}.py'}")
        elif wrapper_class not in test_path.read_text(encoding="utf-8"):
            issues.append(f"{label} test file does not exercise {wrapper_class}: {test_path}")
        else:
            test_paths[label] = test_path
            issues.extend(verify_no_skip_or_xfail(test_path, allow_reasoned_skip=label == "Integration"))
            if label == "Integration":
                issues.extend(verify_integration_exception_catches(test_path.read_text(encoding="utf-8")))
                issues.extend(verify_no_empty_finally(test_path))
                issues.extend(verify_getter_assertions(test_path, owned_properties, blockers))
                issues.extend(verify_getter_matrix(root, simple_name, owned_properties, test_path, strict=strict_getters, blocked=blockers))
    issues.extend(verify_not_implemented_evidence(root, simple_name, wrapper_source, test_paths.get("Unit"), test_paths.get("Integration")))
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
        "API reference heading": "api reference",
    }
    lowered_rst_section = rst_section.lower()
    for label, value in required_values.items():
        if value.lower() not in lowered_rst_section:
            issues.append(f"RST section for {simple_name} is missing {label}: {value}")

    # The RST page is a JavaDoc-style API reference of the Python wrapper: it
    # must document every public member. Deviations live in the generated
    # report, not here.
    public_members = parse_wrapper_public_members(wrapper_source, wrapper_class)
    undocumented = [name for name in public_members if not re.search(rf"\b{re.escape(name)}\b", rst_section)]
    if undocumented:
        issues.append(f"RST section for {simple_name} omits public wrapper member documentation: {', '.join(undocumented)}")

    if not java_doc.is_file():
        issues.append(f"JavaDoc page does not exist: {java_doc}")
    return issues
