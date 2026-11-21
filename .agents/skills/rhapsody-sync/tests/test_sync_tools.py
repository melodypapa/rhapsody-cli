"""Tests for the project-local Rhapsody sync helpers."""

import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from typing import Optional

import pytest

SKILL_ROOT = Path(__file__).resolve().parents[1]
SYNC_TOOLS_PATH = SKILL_ROOT / "scripts" / "sync_tools.py"

_VALID_RST_DEVIATIONS = (
    ".. list-table:: API deviations\n"
    "   :header-rows: 1\n\n"
    "   * - JavaDoc member/signature\n"
    "     - COM/pywin32 exposure\n"
    "     - Python implementation\n"
    "     - Deviation and treatment\n"
    "   * - ``getValue``\n"
    "     - ``getValue (method)``\n"
    "     - ``get_value``\n"
    "     - Mismatch\n"
    "   * - ``addExample``\n"
    "     - unavailable\n"
    "     - no wrapper\n"
    "     - JavaDoc-only\n"
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
    (java_dir / "IRPThing.html").write_text("<html>IRPThing</html>", encoding="utf-8")
    (wrapper_dir / "model_thing.py").write_text("class RPThing: pass\n", encoding="utf-8")
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
    report = root / "docs" / "reports" / "IRPThing_api_report.md"
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


def test_builds_validator_command_using_existing_project_script(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = tmp_path / "repo"
    reports = root / "docs" / "reports"

    command = tools.build_validator_command(root, "com.telelogic.rhapsody.core.IRPThing", "authority", reports)

    assert command[1] == str(root / "scripts" / "validate_model_api.py")
    assert command[2] == "IRPThing"
    assert command[command.index("--source") + 1] == "authority"
    assert command[command.index("--path") + 1] == str(reports)


def test_extracts_deviation_members_from_validator_report() -> None:
    tools = _load_sync_tools()
    report = (
        "## Comparison details\n"
        "| wrapper | Java API | COM | status | recommendation |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| get_value() -> getValue | getValue (method) | value (property) | MISMATCH | Fix it. |\n"
        "## Expected Binding Differences\n"
        "| wrapper | Java API | COM | status | recommendation |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| — | addExample (method) | — | JAVA_ONLY_MEMBER | Check it. |\n"
    )

    assert tools.extract_deviation_members(report) == {"get_value", "getValue", "value", "addExample"}


def test_verifier_reports_missing_deviation_from_rst(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = _write_fixture_project(tmp_path / "repo", ".. list-table:: API deviations\n")
    report = _write_report(root)

    issues = tools.verify_sync_artifacts(root, "IRPThing", report)

    assert any("getValue" in issue for issue in issues)
    assert any("addExample" in issue for issue in issues)


def test_verifier_accepts_package_requirements_and_complete_rst_deviations(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = _write_fixture_project(tmp_path / "repo", _VALID_RST_DEVIATIONS)
    report = _write_report(root)

    assert tools.verify_sync_artifacts(root, "IRPThing", report) == []


def test_parses_java_package_from_report() -> None:
    tools = _load_sync_tools()
    report = "# Rhapsody API Validation: IRPThing\n\n## Summary\n- Java package: `com.telelogic.rhapsody.core`\n"

    assert tools.parse_report_java_package(report) == "com.telelogic.rhapsody.core"


def test_verifier_reports_missing_java_package(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = _write_fixture_project(tmp_path / "repo", _VALID_RST_DEVIATIONS)
    report = _write_report(root, java_package=None)

    issues = tools.verify_sync_artifacts(root, "IRPThing", report)

    assert any("Java package" in issue and "missing" in issue.lower() for issue in issues)


def test_verifier_reports_java_package_mismatch(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = _write_fixture_project(tmp_path / "repo", _VALID_RST_DEVIATIONS)
    report = _write_report(root, java_package="com.example.other")

    issues = tools.verify_sync_artifacts(root, "IRPThing", report)

    assert any("com.example.other" in issue and "com.telelogic.rhapsody.core" in issue for issue in issues)


def test_irpclass_report_declares_java_package() -> None:
    tools = _load_sync_tools()
    # Resolve the repo root without the docs/java_api marker: this check validates a
    # committed offline artifact and must run on machines without the JavaDoc tree.
    root = next(
        candidate
        for candidate in SYNC_TOOLS_PATH.parents
        if (candidate / "scripts" / "validate_model_api.py").is_file() and (candidate / "docs" / "reports" / "IRPClass_api_report.md").is_file()
    )
    report = root / "docs" / "reports" / "IRPClass_api_report.md"

    assert tools.parse_report_java_package(report.read_text(encoding="utf-8")) == "com.telelogic.rhapsody.core"


def test_offline_blocker_exits_without_report_and_catalog(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    reports = tmp_path / "docs" / "reports"
    reports.mkdir(parents=True)
    (reports / "pywin32_authority.json").write_text('{"catalog": {"IRPClass": {}}}', encoding="utf-8")

    blocker = tools.offline_authority_blocker(tmp_path, "IRPState")

    assert blocker is not None
    assert "docs/reports/IRPState_api_report.md" in blocker
    assert "--source typelib" in blocker


def test_offline_blocker_asks_for_rebuild_when_report_exists(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    reports = tmp_path / "docs" / "reports"
    reports.mkdir(parents=True)
    (reports / "pywin32_authority.json").write_text('{"catalog": {"IRPClass": {}}}', encoding="utf-8")
    (reports / "IRPState_api_report.md").write_text("# Rhapsody API Validation: IRPState\n", encoding="utf-8")

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
    assert "IRPState_api_report.md" in blocker


def test_verifier_requires_unit_and_integration_test_files(tmp_path: Path) -> None:
    tools = _load_sync_tools()
    root = _write_fixture_project(
        tmp_path / "repo",
        ".. list-table:: API deviations\n   :header-rows: 1\n\n"
        "   * - JavaDoc member/signature\n     - COM/pywin32 exposure\n     - Python implementation\n     - Deviation and treatment\n"
        "   * - ``getValue``\n     - ``getValue (method)``\n     - ``get_value``\n     - Mismatch\n"
        "   * - ``addExample``\n     - unavailable\n     - no wrapper\n     - JavaDoc-only\n",
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
        ".. list-table:: API deviations\n   :header-rows: 1\n\n"
        "   * - JavaDoc member/signature\n     - COM/pywin32 exposure\n     - Python implementation\n     - Deviation and treatment\n"
        "   * - ``getValue``\n     - ``getValue (method)``\n     - ``get_value``\n     - Mismatch\n"
        "   * - ``addExample``\n     - unavailable\n     - no wrapper\n     - JavaDoc-only\n",
    )
    report = _write_report(root)

    issues = tools.verify_sync_artifacts(root, "IRPThing", report)

    assert not any("test file" in issue for issue in issues)
