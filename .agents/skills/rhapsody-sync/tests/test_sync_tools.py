"""Tests for the project-local Rhapsody sync helpers."""

import importlib.util
import sys
from pathlib import Path
from types import ModuleType

import pytest

SKILL_ROOT = Path(__file__).resolve().parents[1]
SYNC_TOOLS_PATH = SKILL_ROOT / "scripts" / "sync_tools.py"


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


def _write_fixture_project(root: Path, rst_deviations: str) -> Path:
    package_parts = ("com", "telelogic", "rhapsody", "core")
    java_dir = root / "docs" / "java_api" / Path(*package_parts)
    wrapper_dir = root / "src" / "rhapsody_cli" / "models" / Path(*package_parts)
    java_dir.mkdir(parents=True)
    wrapper_dir.mkdir(parents=True)
    (root / "scripts").mkdir()
    (root / "scripts" / "validate_model_api.py").write_text("", encoding="utf-8")
    (java_dir / "IRPThing.html").write_text("<html>IRPThing</html>", encoding="utf-8")
    (wrapper_dir / "model_thing.py").write_text("class RPThing: pass\n", encoding="utf-8")
    (root / "docs" / "requirements").mkdir()
    (root / "docs" / "requirements" / "swr_elem_requirements.md").write_text("RPThing wraps IRPThing\n", encoding="utf-8")
    (root / "docs" / "api").mkdir()
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
    (root / "docs" / "api" / "elements.rst").write_text(rst, encoding="utf-8")
    return root


def _write_report(root: Path) -> Path:
    report = root / "docs" / "reports" / "IRPThing_api_report.md"
    report.parent.mkdir(parents=True)
    report.write_text(
        "# Rhapsody API Validation: IRPThing\n\n"
        "## Summary\n"
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
    root = _write_fixture_project(
        tmp_path / "repo",
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
        "     - JavaDoc-only\n",
    )
    report = _write_report(root)

    assert tools.verify_sync_artifacts(root, "IRPThing", report) == []
