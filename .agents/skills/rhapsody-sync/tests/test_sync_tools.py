"""Tests for the project-local Rhapsody sync helpers."""

import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from typing import Optional

import pytest

SKILL_ROOT = Path(__file__).resolve().parents[1]
SYNC_TOOLS_PATH = SKILL_ROOT / "scripts" / "sync_tools.py"

_REPORT_PACKAGE_PARTS = ("com", "telelogic", "rhapsody", "core")


def _report_path(reports_root: Path, interface_name: str) -> Path:
    return reports_root / Path(*_REPORT_PACKAGE_PARTS) / f"{interface_name}_api_report.md"


_VALID_RST_API_REFERENCE = (
    "API reference\n"
    "-------------\n\n"
    ".. autofunction:: rhapsody_cli.models.com.telelogic.rhapsody.core.model_thing.get_value\n\n"
    ".. autofunction:: rhapsody_cli.models.com.telelogic.rhapsody.core.model_thing.add_example\n"
)


def _load_sync_tools() -> ModuleType:
    if not SYNC_TOOLS_PATH.is_file():
        pytest.fail("skill-local sync_tools.py is missing")
    module_name = "rhapsody_sync_skill_sync_tools"
    if module_name in sys.modules:
        return sys.modules[module_name]
    spec = importlib.util.spec_from_file_location(module_name, SYNC_TOOLS_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def _write_fixture_project(root: Path, rst_deviations: str, with_tests: bool = True) -> Path:
    package_parts = ("com", "telelogic", "rhapsody", "core")
    java_dir = root / "docs" / "java_api" / Path(*package_parts)
    wrapper_dir = root / "src" / "rhapsody_cli" / "models" / Path(*package_parts)
    java_dir.mkdir(parents=True)
    wrapper_dir.mkdir(parents=True)
    (root / "scripts").mkdir()
    (root / "scripts" / "validate_model_api.py").write_text("", encoding="utf-8")
    (root / "docs" / "reports").mkdir(parents=True)
    (root / "docs" / "reports" / "pywin32_authority.json").write_text('{"catalog": {"IRPThing": {}}}', encoding="utf-8")
    (java_dir / "IRPThing.html").write_text("<html>IRPThing</html>", encoding="utf-8")
    (wrapper_dir / "model_thing.py").write_text(
        "class RPThing:\n"
        "    def get_value(self) -> int:\n"
        "        return 0\n\n"
        "    def add_example(self, name: str) -> None:\n"
        "        pass\n\n"
        "    def _helper(self) -> None:\n"
        "        pass\n",
        encoding="utf-8",
    )
    (root / "docs" / "requirements" / Path(*package_parts)).mkdir(parents=True)
    (root / "docs" / "requirements" / Path(*package_parts) / "model_thing.md").write_text("RPThing wraps IRPThing\n", encoding="utf-8")
    (root / "docs" / "api" / Path(*package_parts)).mkdir(parents=True)
    if with_tests:
        for test_base in ("unit", "integration"):
            test_dir = root / "tests" / test_base / "models" / Path(*package_parts)
            test_dir.mkdir(parents=True)
            (test_dir / "test_model_thing.py").write_text("RPThing\n", encoding="utf-8")
    package_name = ".".join(package_parts)
    canonical_import = "rhapsody_cli.models." + package_name + ".model_thing"
    rst = (
        ".. _rhapsody-java-interface-IRPThing:\n\n"
        "IRPThing — RPThing\n"
        "------------------\n\n"
        f"Java package: ``{package_name}``\n\n"
        "JavaDoc description: Example model element.\n\n"
        "Python wrapper: ``RPThing``\n\n"
        f"Canonical Python import: ``{canonical_import}``\n\n"
        f"{rst_deviations}\n"
    )
    (root / "docs" / "api" / Path(*package_parts) / "model_thing.rst").write_text(rst, encoding="utf-8")
    return root


def _write_report(root: Path, java_package: Optional[str] = "com.telelogic.rhapsody.core") -> Path:
    report = _report_path(root / "docs" / "reports", "IRPThing")
    report.parent.mkdir(parents=True)
    java_package_line = f"- Java package: `{java_package}`\n" if java_package else ""
    report.write_text(
        "# Rhapsody API Validation: IRPThing\n\n"
        "## Summary\n"
        f"{java_package_line}"
        "- Target wrapper: `RPThing` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/model_thing.py`)\n\n"
        "## Comparison details\n\n"
        "| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| get_value() -> getValue | getValue (method) | getValue (method) | SIGNATURE_MISMATCH | Review mapping. |\n\n"
        "## Expected Binding Differences\n\n"
        "| Python model wrapper | Java API | pywin32 | Status | Recommended change |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| — | addExample (method) | — | JAVA_ONLY_MEMBER | Verify COM support. |\n",
        encoding="utf-8",
    )
    return report


def test_finds_project_root_from_skill_scripts_directory(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = tmp_path / "repo"
    (root / "scripts").mkdir(parents=True)
    (root / "scripts" / "validate_model_api.py").write_text("", encoding="utf-8")
    (root / "docs" / "java_api").mkdir(parents=True)
    start = root / ".agents" / "skills" / "rhapsody-sync" / "scripts"
    start.mkdir(parents=True)

    assert tools.find_project_root(start) == root


def test_api_report_path_uses_the_java_package_from_javadoc(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = _write_fixture_project(tmp_path / "repo", _VALID_RST_API_REFERENCE)

    report = tools.api_report_path(root, "IRPThing")

    assert report == root / "docs" / "reports" / "com" / "telelogic" / "rhapsody" / "core" / "IRPThing_api_report.md"


def test_api_report_path_finds_package_report_without_javadoc(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = tmp_path / "repo"
    report = root / "docs" / "reports" / "org" / "example" / "rhapsody" / "IRPThing_api_report.md"
    report.parent.mkdir(parents=True)
    report.write_text("# Rhapsody API Validation: IRPThing\n", encoding="utf-8")

    assert tools.api_report_path(root, "IRPThing") == report


def test_builds_validator_command_using_existing_project_script(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = tmp_path / "repo"
    reports = root / "docs" / "reports"

    command = tools.build_validator_command(root, "com.telelogic.rhapsody.core.IRPThing", "authority", reports)

    assert command[1] == str(root / "scripts" / "validate_model_api.py")
    assert command[2] == "IRPThing"
    assert command[command.index("--source") + 1] == "authority"
    assert command[command.index("--path") + 1] == str(reports)


def test_parses_public_wrapper_members() -> None:
    """API-reference coverage is defined over the wrapper's public members:
    public methods and properties, no underscore-private, no dunders."""
    tools = _load_sync_tools()
    source = (
        "class RPThing:\n"
        "    def get_value(self) -> int:\n"
        "        return 0\n\n"
        "    @property\n"
        "    def kind(self) -> str:\n"
        '        return ""\n\n'
        "    def add_example(self, name: str) -> None:\n"
        "        pass\n\n"
        "    def _helper(self) -> None:\n"
        "        pass\n\n"
        "    def __repr__(self) -> str:\n"
        '        return ""\n'
    )

    assert tools.parse_wrapper_public_members(source, "RPThing") == ["add_example", "get_value", "kind"]


def test_verifier_reports_undocumented_public_member(tmp_path: Path) -> None:
    """The RST page is an API reference: every public wrapper member must be
    documented, regardless of the report's deviation tables."""
    tools = _load_sync_tools()
    root = _write_fixture_project(
        tmp_path / "repo",
        ".. autofunction:: rhapsody_cli.models.com.telelogic.rhapsody.core.model_thing.get_value\n",
    )
    report = _write_report(root)

    issues = tools.verify_sync_artifacts(root, "IRPThing", report)

    assert any("add_example" in issue for issue in issues)
    assert not any("get_value" in issue and "omits" in issue for issue in issues)


def test_verifier_accepts_package_requirements_and_complete_api_reference(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = _write_fixture_project(tmp_path / "repo", _VALID_RST_API_REFERENCE)
    report = _write_report(root)

    assert tools.verify_sync_artifacts(root, "IRPThing", report) == []


def test_parses_java_package_from_report() -> None:
    tools = _load_sync_tools()
    report = "# Rhapsody API Validation: IRPThing\n\n## Summary\n- Java package: `com.telelogic.rhapsody.core`\n"

    assert tools.parse_report_java_package(report) == "com.telelogic.rhapsody.core"


def test_verifier_reports_missing_java_package(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = _write_fixture_project(tmp_path / "repo", _VALID_RST_API_REFERENCE)
    report = _write_report(root, java_package=None)

    issues = tools.verify_sync_artifacts(root, "IRPThing", report)

    assert any("Java package" in issue and "missing" in issue.lower() for issue in issues)


def test_verifier_reports_java_package_mismatch(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = _write_fixture_project(tmp_path / "repo", _VALID_RST_API_REFERENCE)
    report = _write_report(root, java_package="com.example.other")

    issues = tools.verify_sync_artifacts(root, "IRPThing", report)

    assert any("com.example.other" in issue and "com.telelogic.rhapsody.core" in issue for issue in issues)


def test_irpclass_report_declares_java_package() -> None:
    tools = _load_sync_tools()
    # Resolve the repo root without the docs/java_api marker: this check validates a
    # committed offline artifact and must run on machines without the JavaDoc tree.
    root = next(
        candidate for candidate in SYNC_TOOLS_PATH.parents if (candidate / "scripts" / "validate_model_api.py").is_file() and _report_path(candidate / "docs" / "reports", "IRPClass").is_file()
    )
    report = _report_path(root / "docs" / "reports", "IRPClass")

    assert tools.parse_report_java_package(report.read_text(encoding="utf-8")) == "com.telelogic.rhapsody.core"


def test_offline_blocker_exits_without_report_and_catalog(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    reports = tmp_path / "docs" / "reports"
    reports.mkdir(parents=True)
    (reports / "pywin32_authority.json").write_text('{"catalog": {"IRPClass": {}}}', encoding="utf-8")

    blocker = tools.offline_authority_blocker(tmp_path, "IRPState")

    assert blocker is not None
    assert "docs/reports/com/telelogic/rhapsody/core/IRPState_api_report.md" in blocker
    assert "--source typelib" in blocker


def test_offline_blocker_asks_for_rebuild_when_report_exists(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    reports = tmp_path / "docs" / "reports"
    reports.mkdir(parents=True)
    (reports / "pywin32_authority.json").write_text('{"catalog": {"IRPClass": {}}}', encoding="utf-8")
    _report_path(reports, "IRPState").parent.mkdir(parents=True)
    _report_path(reports, "IRPState").write_text("# Rhapsody API Validation: IRPState\n", encoding="utf-8")

    blocker = tools.offline_authority_blocker(tmp_path, "IRPState")

    assert blocker is not None
    assert "--source reports" in blocker


def test_offline_blocker_clear_when_catalog_covers_interface(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    reports = tmp_path / "docs" / "reports"
    reports.mkdir(parents=True)
    (reports / "pywin32_authority.json").write_text('{"catalog": {"IRPState": {}}}', encoding="utf-8")

    assert tools.offline_authority_blocker(tmp_path, "IRPState") is None


def test_offline_blocker_exits_when_snapshot_file_missing(tmp_path: Path) -> None:
    tools = _load_sync_tools()

    blocker = tools.offline_authority_blocker(tmp_path, "IRPState")

    assert blocker is not None
    assert "docs/reports/com/telelogic/rhapsody/core/IRPState_api_report.md" in blocker


def test_verifier_requires_unit_and_integration_test_files(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = _write_fixture_project(
        tmp_path / "repo",
        _VALID_RST_API_REFERENCE,
        with_tests=False,
    )
    report = _write_report(root)

    issues = tools.verify_sync_artifacts(root, "IRPThing", report)

    assert any("Unit test file not found" in issue for issue in issues)
    assert any("Integration test file not found" in issue for issue in issues)


def test_verifier_accepts_mirror_test_files_exercising_the_class(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = _write_fixture_project(
        tmp_path / "repo",
        _VALID_RST_API_REFERENCE,
    )
    report = _write_report(root)

    issues = tools.verify_sync_artifacts(root, "IRPThing", report)

    assert not any("test file" in issue for issue in issues)


def _write_application_fixture(root: Path) -> Path:
    """Fixture for an application-layer wrapper: application.py, not under models/."""
    package_parts = ("com", "telelogic", "rhapsody", "core")
    package_name = ".".join(package_parts)
    java_dir = root / "docs" / "java_api" / Path(*package_parts)
    java_dir.mkdir(parents=True)
    (java_dir / "IRPApplication.html").write_text("<html>IRPApplication</html>", encoding="utf-8")
    (root / "scripts").mkdir(parents=True)
    (root / "scripts" / "validate_model_api.py").write_text("", encoding="utf-8")
    (root / "docs" / "reports").mkdir(parents=True)
    (root / "docs" / "reports" / "pywin32_authority.json").write_text('{"catalog": {"IRPApplication": {}}}', encoding="utf-8")

    app_dir = root / "src" / "rhapsody_cli"
    app_dir.mkdir(parents=True)
    (app_dir / "application.py").write_text(
        "class RhapsodyApplication:\n"
        "    def get_build_no(self) -> str:\n"
        '        return ""\n\n'
        "    def connect(self) -> None:\n"
        "        pass\n\n"
        "    def _attach(self) -> None:\n"
        "        pass\n",
        encoding="utf-8",
    )
    for layer in ("unit", "integration"):
        test_dir = root / "tests" / layer
        test_dir.mkdir(parents=True)
        (test_dir / "test_application.py").write_text("RhapsodyApplication\n", encoding="utf-8")

    req_dir = root / "docs" / "requirements" / Path(*package_parts)
    req_dir.mkdir(parents=True)
    (req_dir / "irp_application.md").write_text("RhapsodyApplication wraps IRPApplication\n", encoding="utf-8")
    api_dir = root / "docs" / "api" / Path(*package_parts)
    api_dir.mkdir(parents=True)
    (api_dir / "irp_application.rst").write_text(
        ".. _rhapsody-java-interface-IRPApplication:\n\n"
        "IRPApplication\n==============\n\n"
        f"Java package: ``{package_name}``\n\n"
        "Python wrapper: ``RhapsodyApplication``\n\n"
        "Canonical Python import: ``rhapsody_cli.application``\n\n"
        "API reference\n"
        "-------------\n\n"
        ".. autofunction:: rhapsody_cli.application.RhapsodyApplication.get_build_no\n\n"
        ".. autofunction:: rhapsody_cli.application.RhapsodyApplication.connect\n",
        encoding="utf-8",
    )
    report = _report_path(root / "docs" / "reports", "IRPApplication")
    report.parent.mkdir(parents=True)
    report.write_text(
        "# Rhapsody API Validation: IRPApplication\n\n"
        "## Summary\n"
        f"- Java package: `{package_name}`\n"
        "- Target wrapper: `RhapsodyApplication` (`src/rhapsody_cli/application.py`)\n\n"
        "## Comparison details\n\n"
        "| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| get_build_no() -> getBuildNo | getBuildNo (method) | BuildNo (property) | COM_MEMBER_NOT_EXPOSED | Document. |\n\n"
        "## Expected Binding Differences\n\n"
        "| Python model wrapper | Java API | pywin32 | Status | Recommended change |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| — | — | — | — | — |\n\n"
        "## Wrapper Backlog\n\n"
        "| Python model wrapper | Java API | pywin32 | Status | Recommended change |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| — | someJavaOnlyMember (method) | — | MISSING_PYTHON_WRAPPER | Intentionally unsupported. |\n",
        encoding="utf-8",
    )
    return report


def test_verifier_accepts_application_layer_wrapper(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = tmp_path / "repo"
    report = _write_application_fixture(root)

    assert tools.verify_sync_artifacts(root, "IRPApplication", report) == []


def test_verifier_does_not_require_report_deviation_rows_in_rst(tmp_path: Path) -> None:
    """Deviations live in the generated report; the RST is an API reference and
    must not be required to repeat report members (backlog or otherwise)."""
    tools = _load_sync_tools()
    root = tmp_path / "repo"
    report = _write_application_fixture(root)

    assert tools.verify_sync_artifacts(root, "IRPApplication", report) == []
    assert not hasattr(tools, "extract_deviation_members")


def test_binding_check_flags_absent_com_member(tmp_path: Path) -> None:
    """A wrapper calling a Java-named member absent from pywin32 must fail Step 8."""
    tools = _load_sync_tools()
    (tmp_path / "docs" / "reports").mkdir(parents=True)
    (tmp_path / "docs" / "reports" / "pywin32_authority.json").write_text('{"catalog": {"IRPType": {}}}', encoding="utf-8")
    wrapper = """
class IRPType:
    def get_thing(self):
        return self.call_com(lambda: self._com.getThing())
"""
    issues = tools.verify_wrapper_bindings(tmp_path, "IRPType", wrapper)
    assert any("getThing" in issue and "absent" in issue.lower() for issue in issues)


def test_binding_check_flags_wrong_shape(tmp_path: Path) -> None:
    """A property-shaped COM member called via call_com must be flagged."""
    tools = _load_sync_tools()
    (tmp_path / "docs" / "reports").mkdir(parents=True)
    (tmp_path / "docs" / "reports" / "pywin32_authority.json").write_text('{"catalog": {"IRPType": {"thing": "property"}}}', encoding="utf-8")
    wrapper = """
class IRPType:
    def get_thing(self):
        return self.call_com(lambda: self._com.thing())
"""
    issues = tools.verify_wrapper_bindings(tmp_path, "IRPType", wrapper)
    assert any("thing" in issue and "shape" in issue.lower() for issue in issues)


def test_binding_check_accepts_valid_bindings(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    (tmp_path / "docs" / "reports").mkdir(parents=True)
    (tmp_path / "docs" / "reports" / "pywin32_authority.json").write_text('{"catalog": {"IRPType": {"Thing": "method", "flag": "property"}}}', encoding="utf-8")
    wrapper = """
class IRPType:
    def get_thing(self):
        return self.call_com(lambda: self._com.Thing())

    @property
    def flag(self):
        return self.get_com_property(self._com, "flag")

    @flag.setter
    def flag(self, value):
        self.set_com_property(self._com, "flag", value)
"""
    assert tools.verify_wrapper_bindings(tmp_path, "IRPType", wrapper) == []


def test_binding_check_flags_property_member_exposed_as_plain_method(tmp_path: Path) -> None:
    """SKILL §3: a property-shaped COM member must be surfaced as @property."""
    tools = _load_sync_tools()
    (tmp_path / "docs" / "reports").mkdir(parents=True)
    (tmp_path / "docs" / "reports" / "pywin32_authority.json").write_text('{"catalog": {"IRPType": {"flag": "property"}}}', encoding="utf-8")
    wrapper = """
class IRPType:
    def get_flag(self):
        return self.get_com_property(self._com, "flag")
"""
    issues = tools.verify_wrapper_bindings(tmp_path, "IRPType", wrapper)
    assert any("flag" in issue and "@property" in issue for issue in issues)


def test_binding_check_flags_method_member_exposed_as_property(tmp_path: Path) -> None:
    """SKILL §3: a method-shaped COM member must not be surfaced as @property."""
    tools = _load_sync_tools()
    (tmp_path / "docs" / "reports").mkdir(parents=True)
    (tmp_path / "docs" / "reports" / "pywin32_authority.json").write_text('{"catalog": {"IRPType": {"Thing": "method"}}}', encoding="utf-8")
    wrapper = """
class IRPType:
    @property
    def thing(self):
        return self.call_com(lambda: self._com.Thing())
"""
    issues = tools.verify_wrapper_bindings(tmp_path, "IRPType", wrapper)
    assert any("Thing" in issue and "@property" in issue for issue in issues)


def test_binding_check_flags_legacy_dual_binding_helper(tmp_path: Path) -> None:
    """SKILL §4: synced wrappers must not keep _get_method_or_property probes."""
    tools = _load_sync_tools()
    (tmp_path / "docs" / "reports").mkdir(parents=True)
    (tmp_path / "docs" / "reports" / "pywin32_authority.json").write_text('{"catalog": {"IRPType": {"Thing": "method"}}}', encoding="utf-8")
    wrapper = """
class IRPType:
    def get_thing(self):
        return self._get_method_or_property("Thing")
"""
    issues = tools.verify_wrapper_bindings(tmp_path, "IRPType", wrapper)
    assert any("_get_method_or_property" in issue for issue in issues)


def test_binding_check_flags_direct_com_access(tmp_path: Path) -> None:
    """SKILL §3: COM members are reached only through call_com or the property helpers."""
    tools = _load_sync_tools()
    (tmp_path / "docs" / "reports").mkdir(parents=True)
    (tmp_path / "docs" / "reports" / "pywin32_authority.json").write_text('{"catalog": {"IRPType": {"Thing": "method"}}}', encoding="utf-8")
    wrapper = """
class IRPType:
    def get_thing(self):
        return self._com.Thing()
"""
    issues = tools.verify_wrapper_bindings(tmp_path, "IRPType", wrapper)
    assert any("self._com.Thing" in issue for issue in issues)


def test_integration_check_allows_only_not_implemented_error() -> None:
    tools = _load_sync_tools()
    ok = """
def test_stub():
    with pytest.raises(NotImplementedError):
        wrapper.java_only_method()
"""
    assert tools.verify_integration_exception_catches(ok) == []


def test_integration_check_flags_disallowed_exceptions() -> None:
    tools = _load_sync_tools()
    bad = """
def test_a():
    with pytest.raises(AttributeError):
        wrapper.method()
def test_b():
    with pytest.raises(RhapsodyRuntimeException):
        wrapper.method()
def test_c():
    with pytest.raises((TypeError, ValueError)):
        wrapper.method()
"""
    issues = tools.verify_integration_exception_catches(bad)
    assert len(issues) == 3
    assert any("AttributeError" in i for i in issues)
    assert any("RhapsodyRuntimeException" in i for i in issues)
    assert any("TypeError" in i and "ValueError" in i for i in issues)


def test_integration_check_flags_try_except_handlers() -> None:
    """Section 5 forbids try/except in integration test bodies: a caught
    failure masquerades as a pass. try/finally cleanup stays allowed."""
    tools = _load_sync_tools()
    bad = """
def test_a():
    try:
        assert wrapper.method() is not None
    except Exception:
        pass
"""
    issues = tools.verify_integration_exception_catches(bad)
    assert len(issues) == 1
    assert "try/except" in issues[0]


def test_integration_check_allows_try_finally_cleanup() -> None:
    """try/finally cleanup without an except clause catches nothing; the
    canonical mirrored integration tests rely on it, and the documented
    NotImplementedError stub assertion stays permitted."""
    tools = _load_sync_tools()
    ok = """
def test_a():
    element = package.add_element("x")
    try:
        assert element is not None
    finally:
        element.delete_from_project()
    with pytest.raises(NotImplementedError):
        wrapper.java_only_method()
"""
    assert tools.verify_integration_exception_catches(ok) == []


def test_signature_arity_mismatch_detected(tmp_path: Path) -> None:
    """A wrapper call with wrong arg count is reported against pywin32 signatures."""
    import importlib.util

    spec = importlib.util.spec_from_file_location("valmod", SYNC_TOOLS_PATH.parents[4] / "scripts" / "validate_model_api.py")
    val = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(val)
    signatures = {"FindThing": {"count": 2, "names": ["a", "b"], "types": ["str", "str"], "codes": [8, 8]}}
    arities = {"FindThing": [1]}
    rows = val.build_signature_rows({"FindThing": {"find_thing() -> FindThing"}}, signatures, arities, {})
    assert any("SIGNATURE_ARITY_MISMATCH" in r[3] for r in rows)


def test_signature_type_mismatch_detected(tmp_path: Path) -> None:
    import importlib.util

    spec = importlib.util.spec_from_file_location("valmod2", SYNC_TOOLS_PATH.parents[4] / "scripts" / "validate_model_api.py")
    val = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(val)
    signatures = {"SetThing": {"count": 1, "names": ["v"], "types": ["str"], "codes": [8]}}
    arities = {"SetThing": [1]}
    arg_types = {"SetThing": ["int"]}
    rows = val.build_signature_rows({"SetThing": {"set_thing() -> SetThing"}}, signatures, arities, arg_types)
    assert any("SIGNATURE_TYPE_MISMATCH" in r[3] for r in rows)


def test_verify_wrapper_bindings_flags_arity_mismatch(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    """Step 8 enforces the signature arity the skill documents: a wrapper
    calling an exposed member with the wrong argument count fails."""
    (tmp_path / "docs" / "reports").mkdir(parents=True)
    (tmp_path / "docs" / "reports" / "pywin32_authority.json").write_text(
        '{"catalog": {"IRPType": {"FindThing": "method"}}, "signatures": {"IRPType": {"FindThing": {"count": 2, "names": ["a", "b"], "types": ["str", "str"], "codes": [8, 8]}}}}',
        encoding="utf-8",
    )
    wrapper = """
class IRPType:
    def find_thing(self, a):
        return self.call_com(lambda: self._com.FindThing(a))
"""

    issues = tools.verify_wrapper_bindings(tmp_path, "IRPType", wrapper)

    assert any("arity" in issue.lower() and "FindThing" in issue for issue in issues)


def test_verify_wrapper_bindings_accepts_matching_arity(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    (tmp_path / "docs" / "reports").mkdir(parents=True)
    (tmp_path / "docs" / "reports" / "pywin32_authority.json").write_text(
        '{"catalog": {"IRPType": {"FindThing": "method"}}, "signatures": {"IRPType": {"FindThing": {"count": 2, "names": ["a", "b"], "types": ["str", "str"], "codes": [8, 8]}}}}',
        encoding="utf-8",
    )
    wrapper = """
class IRPType:
    def find_thing(self, a, b):
        return self.call_com(lambda: self._com.FindThing(a, b))
"""

    assert tools.verify_wrapper_bindings(tmp_path, "IRPType", wrapper) == []


def test_verify_wrapper_bindings_skips_arity_when_signature_absent(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    """Without a committed signature for the member there is no arity
    evidence — the binding check stays limited to existence and shape."""
    (tmp_path / "docs" / "reports").mkdir(parents=True)
    (tmp_path / "docs" / "reports" / "pywin32_authority.json").write_text(
        '{"catalog": {"IRPType": {"FindThing": "method"}}}',
        encoding="utf-8",
    )
    wrapper = """
class IRPType:
    def find_thing(self, a):
        return self.call_com(lambda: self._com.FindThing(a))
"""

    assert tools.verify_wrapper_bindings(tmp_path, "IRPType", wrapper) == []


def _write_test_file(tmp_path: Path, body: str) -> Path:
    test_file = tmp_path / "test_model_thing.py"
    test_file.write_text(body, encoding="utf-8")
    return test_file


def test_skip_marker_check_flags_pytest_mark_skip_in_unit_test(tmp_path: Path) -> None:
    """Section 4: unit tests must all run, so any skip marker is rejected."""
    tools = _load_sync_tools()
    test_file = _write_test_file(
        tmp_path,
        "import pytest\n\n\n" '@pytest.mark.skip(reason="live precondition unavailable")\n' "def test_thing() -> None:\n" "    assert True\n",
    )

    issues = tools.verify_no_skip_or_xfail(test_file)

    assert len(issues) == 1
    assert "pytest.mark.skip" in issues[0]


def test_skip_marker_check_allows_reasoned_skip_for_integration(tmp_path: Path) -> None:
    """Section 4: an approved integration skip needs a non-empty reason."""
    tools = _load_sync_tools()
    test_file = _write_test_file(
        tmp_path,
        "import pytest\n\n\n" '@pytest.mark.skip(reason="live precondition unavailable")\n' "def test_thing() -> None:\n" "    assert True\n",
    )

    assert tools.verify_no_skip_or_xfail(test_file, allow_reasoned_skip=True) == []


def test_skip_marker_check_flags_reasoned_skip_without_reason(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    test_file = _write_test_file(
        tmp_path,
        "import pytest\n\n\n" "@pytest.mark.skip\n" "def test_thing() -> None:\n" "    assert True\n",
    )

    issues = tools.verify_no_skip_or_xfail(test_file, allow_reasoned_skip=True)

    assert len(issues) == 1
    assert "pytest.mark.skip" in issues[0]


def test_skip_marker_check_flags_pytest_mark_xfail(tmp_path: Path) -> None:
    """Section 4/5: xfail is never permitted for a model-class test."""
    tools = _load_sync_tools()
    test_file = _write_test_file(
        tmp_path,
        "import pytest\n\n\n" "@pytest.mark.xfail\n" "def test_thing() -> None:\n" "    assert True\n",
    )

    issues = tools.verify_no_skip_or_xfail(test_file)

    assert len(issues) == 1
    assert "pytest.mark.xfail" in issues[0]


def test_skip_marker_check_flags_pytest_skip_call(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    test_file = _write_test_file(tmp_path, "import pytest\n\n\ndef test_thing() -> None:\n    pytest.skip('later')\n")

    issues = tools.verify_no_skip_or_xfail(test_file)

    assert len(issues) == 1
    assert "pytest.skip" in issues[0]


def test_empty_finally_check_flags_pass_only_cleanup_shell(tmp_path: Path) -> None:
    """Section 5: a `finally: pass` shell is not real cleanup."""
    tools = _load_sync_tools()
    test_file = _write_test_file(
        tmp_path,
        "def test_thing() -> None:\n    try:\n        assert True\n    finally:\n        pass\n",
    )

    issues = tools.verify_no_empty_finally(test_file)

    assert len(issues) == 1
    assert "finally" in issues[0]


def test_empty_finally_check_accepts_real_cleanup(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    test_file = _write_test_file(
        tmp_path,
        "def test_thing(element) -> None:\n    try:\n        assert element is not None\n    finally:\n        element.delete_from_project()\n",
    )

    assert tools.verify_no_empty_finally(test_file) == []


def test_skip_and_empty_finally_checks_accept_normal_test_file(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    test_file = _write_test_file(
        tmp_path,
        "import pytest\n\n\n" "def test_thing() -> None:\n" "    with pytest.raises(NotImplementedError):\n" "        raise NotImplementedError\n",
    )

    assert tools.verify_no_skip_or_xfail(test_file) == []
    assert tools.verify_no_empty_finally(test_file) == []


def test_verifier_flags_skip_marker_and_empty_finally_in_mirrored_integration_test(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = _write_fixture_project(tmp_path / "repo", _VALID_RST_API_REFERENCE)
    report = _write_report(root)
    integration_test = root / "tests" / "integration" / "models" / Path(*_REPORT_PACKAGE_PARTS) / "test_model_thing.py"
    integration_test.write_text(
        "import pytest\n\nRPThing\n\n\n" "@pytest.mark.xfail\n" "def test_thing() -> None:\n" "    try:\n" "        assert True\n" "    finally:\n" "        pass\n",
        encoding="utf-8",
    )

    issues = tools.verify_sync_artifacts(root, "IRPThing", report)

    assert any("pytest.mark.xfail" in issue for issue in issues)
    assert any("finally" in issue for issue in issues)


def test_verifier_applies_skip_checks_to_unit_test_files(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = _write_fixture_project(tmp_path / "repo", _VALID_RST_API_REFERENCE)
    report = _write_report(root)
    unit_test = root / "tests" / "unit" / "models" / Path(*_REPORT_PACKAGE_PARTS) / "test_model_thing.py"
    unit_test.write_text(
        "import pytest\n\nRPThing\n\n\n" "@pytest.mark.skip\n" "def test_thing() -> None:\n" "    try:\n" "        assert True\n" "    finally:\n" "        pass\n",
        encoding="utf-8",
    )

    issues = tools.verify_sync_artifacts(root, "IRPThing", report)

    assert any("pytest.mark.skip" in issue for issue in issues)
    assert not any("finally" in issue for issue in issues)


def test_getter_assertion_check_flags_non_none_only(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    test_file = _write_test_file(
        tmp_path,
        "def test_packages(project) -> None:\n    assert project.packages is not None\n",
    )

    issues = tools.verify_getter_assertions(test_file, {"packages"})

    assert len(issues) == 1
    assert "test_packages" in issues[0]


def test_getter_assertion_check_flags_count_only(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    test_file = _write_test_file(
        tmp_path,
        "def test_components(project) -> None:\n    assert len(project.components) > 0\n",
    )

    issues = tools.verify_getter_assertions(test_file, {"components"})

    assert len(issues) == 1
    assert "test_components" in issues[0]


def test_getter_assertion_check_accepts_membership_assertion(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    test_file = _write_test_file(
        tmp_path,
        "def test_packages(project) -> None:\n    created = project.add_package('p')\n    assert created in list(project.packages)\n",
    )

    assert tools.verify_getter_assertions(test_file, {"packages"}) == []


def test_inherited_assertion_scan_flags_base_only_assertion(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    models_dir = tmp_path / "src" / "rhapsody_cli" / "models" / "com" / "telelogic" / "rhapsody" / "core"
    models_dir.mkdir(parents=True)
    (models_dir / "base_thing.py").write_text("class BaseThing:\n    @property\n    def name(self) -> str:\n        return ''\n", encoding="utf-8")
    wrapper_source = "class RPThing(BaseThing):\n    @property\n    def own_value(self) -> int:\n        return 0\n"
    test_file = _write_test_file(tmp_path, "def test_add(thing) -> None:\n    assert thing.name == 'x'\n")

    notes = tools.collect_inherited_assertion_notes(tmp_path, wrapper_source, "RPThing", test_file)

    assert len(notes) == 1
    assert "name" in notes[0]


def test_inherited_assertion_scan_ignores_own_member_assertion(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    models_dir = tmp_path / "src" / "rhapsody_cli" / "models" / "com" / "telelogic" / "rhapsody" / "core"
    models_dir.mkdir(parents=True)
    (models_dir / "base_thing.py").write_text("class BaseThing:\n    @property\n    def name(self) -> str:\n        return ''\n", encoding="utf-8")
    wrapper_source = "class RPThing(BaseThing):\n    @property\n    def own_value(self) -> int:\n        return 0\n"
    test_file = _write_test_file(tmp_path, "def test_own(thing) -> None:\n    assert thing.own_value == 1\n")

    assert tools.collect_inherited_assertion_notes(tmp_path, wrapper_source, "RPThing", test_file) == []


def test_getter_assertion_check_flags_empty_only_getter_test(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    test_file = _write_test_file(
        tmp_path,
        "def test_get_source_artifacts_empty(classifier) -> None:\n    assert classifier.source_artifacts == []\n",
    )

    issues = tools.verify_getter_assertions(test_file, {"source_artifacts"})

    assert len(issues) == 1
    assert "test_get_source_artifacts_empty" in issues[0]


def test_getter_assertion_check_flags_get_prefixed_non_none_test(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    test_file = _write_test_file(
        tmp_path,
        "def test_get_packages(project) -> None:\n    assert project.packages is not None\n",
    )

    issues = tools.verify_getter_assertions(test_file, {"packages"})

    assert len(issues) == 1
    assert "test_get_packages" in issues[0]


def test_getter_assertion_check_accepts_empty_state_with_populated_sibling(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    test_file = _write_test_file(
        tmp_path,
        "def test_packages(project) -> None:\n"
        "    created = project.add_package('p')\n"
        "    assert created in list(project.packages)\n"
        "\n"
        "def test_packages_empty(project) -> None:\n"
        "    assert project.packages == []\n",
    )

    assert tools.verify_getter_assertions(test_file, {"packages"}) == []


def test_getter_assertion_check_flags_truthiness_only(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    test_file = _write_test_file(
        tmp_path,
        "def test_packages(project) -> None:\n    assert not project.packages\n",
    )

    issues = tools.verify_getter_assertions(test_file, {"packages"})

    assert len(issues) == 1
    assert "test_packages" in issues[0]


def test_getter_assertion_check_ignores_non_getter_tests(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    test_file = _write_test_file(
        tmp_path,
        "def test_add_package(project) -> None:\n    assert project.add_package('p') is not None\n",
    )

    assert tools.verify_getter_assertions(test_file, {"packages"}) == []
