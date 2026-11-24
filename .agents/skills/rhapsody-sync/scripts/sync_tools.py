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


def _is_weak_getter_assertion(expression: ast.expr) -> bool:
    """Return whether an assertion proves only non-None/type/count/truthiness."""
    if isinstance(expression, ast.Constant):
        return True
    if isinstance(expression, ast.Compare):
        if len(expression.ops) == 1 and isinstance(expression.ops[0], ast.IsNot):
            comparator = expression.comparators[0]
            return isinstance(comparator, ast.Constant) and comparator.value is None
        operands = [expression.left, *expression.comparators]
        return any(isinstance(operand, ast.Call) and isinstance(operand.func, ast.Name) and operand.func.id == "len" for operand in operands)
    if isinstance(expression, ast.Call):
        return isinstance(expression.func, ast.Name) and expression.func.id == "isinstance"
    return isinstance(expression, (ast.Name, ast.Attribute))


def verify_getter_assertions(path: Path, property_names: Set[str]) -> List[str]:
    """Reject getter tests that assert only non-None/type/count/truthiness.

    SKILL section 5 requires a getter integration test to create the real
    related object, then assert identity or value; an empty collection or a
    non-``None`` return is not evidence that retrieval works.
    """
    issues: List[str] = []
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) or not node.name.startswith("test_"):
            continue
        member = node.name[len("test_") :]
        if member not in property_names:
            continue
        assertions = [statement for statement in ast.walk(node) if isinstance(statement, ast.Assert)]
        if not assertions or all(_is_weak_getter_assertion(assertion.test) for assertion in assertions):
            issues.append(f"getter test {node.name} at line {node.lineno} only asserts non-None/type/count; create the related object and assert identity/value (SKILL section 5)")
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
    owned_properties = _owned_property_names(absolute_wrapper.read_text(encoding="utf-8")) if absolute_wrapper.is_file() else set()
    for label, test_base in (("Unit", "unit"), ("Integration", "integration")):
        test_dir = root / "tests" / test_base / model_segment
        test_path = first_existing(test_dir, "test_{stem}.py")
        if test_path is None:
            issues.append(f"{label} test file not found for {simple_name}: {test_dir / f'test_{class_stem}.py'}")
        elif wrapper_class not in test_path.read_text(encoding="utf-8"):
            issues.append(f"{label} test file does not exercise {wrapper_class}: {test_path}")
        else:
            issues.extend(verify_no_skip_or_xfail(test_path, allow_reasoned_skip=label == "Integration"))
            if label == "Integration":
                issues.extend(verify_integration_exception_catches(test_path.read_text(encoding="utf-8")))
                issues.extend(verify_no_empty_finally(test_path))
                issues.extend(verify_getter_assertions(test_path, owned_properties))
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
    wrapper_source = absolute_wrapper.read_text(encoding="utf-8") if absolute_wrapper.is_file() else ""
    public_members = parse_wrapper_public_members(wrapper_source, wrapper_class)
    undocumented = [name for name in public_members if not re.search(rf"\b{re.escape(name)}\b", rst_section)]
    if undocumented:
        issues.append(f"RST section for {simple_name} omits public wrapper member documentation: {', '.join(undocumented)}")

    if not java_doc.is_file():
        issues.append(f"JavaDoc page does not exist: {java_doc}")
    return issues
