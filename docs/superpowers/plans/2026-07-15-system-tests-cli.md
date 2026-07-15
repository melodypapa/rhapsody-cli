# CLI System Tests (Subprocess End-to-End) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement subprocess-based system tests that invoke `rhapsody-cli` directly as a command-line tool against a live Rhapsody instance, covering all 6 command groups with CRUD lifecycle and CLI parsing tests.

**Architecture:** Pure subprocess approach — all operations (setup, act, verify, teardown) go through `subprocess.run()` invoking `python -m rhapsody_cli.cli.main`. Session-scoped test project created via CLI `project new`. Per-test isolation via UUID-suffixed element names and CLI `delete` cleanup.

**Tech Stack:** Python 3.8+, pytest, subprocess, json, uuid. No external test dependencies.

**Reference Document:** `docs/java_api/` — IBM Rhapsody Java API Javadoc (`com.telelogic.rhapsody.core`). The CLI wraps the Java API method-for-method (snake_case), so this Javadoc is the authoritative reference for the COM methods invoked by each CLI subcommand. Open `docs/java_api/index.html` in a browser to navigate. Key interfaces per command group:

| Command Group | Java API Interface | Key Methods Exercised |
|---------------|--------------------|-----------------------|
| `project` | `IRPApplication`, `IRPProject` | `createNewProject`, `openProject`, `activeProject`, `getProjects`, `close` |
| `package` | `IRPPackage`, `IRPProject` | `addPackage`, `addNestedPackage`, `getPackages`, `getNestedPackages`, `deleteFromProject` |
| `class` | `IRPClass`, `IRPClassifier` | `addClass`, `getClasses`, `addAttribute`, `addOperation`, `addGeneralization`, `findNestedClassifierRecursive` |
| `attribute` | `IRPAttribute`, `IRPClassifier` | `addAttribute`, `findAttribute`, `deleteAttribute`, `getAttributes` |
| `operation` | `IRPOperation`, `IRPClassifier` | `addOperation`, `findInterfaceItem`, `deleteOperation`, `getOperations` |
| `port` | `IRPPort`, `IRPClassifier` | `getPorts`, `deletePort` (via classifier) |

## Global Constraints

- All CLI invocations via `subprocess.run()` with `timeout=30`, `capture_output=True`, `text=True`
- CLI module: `rhapsody_cli.cli.main` (invoked as `python -m rhapsody_cli.cli.main <args>`)
- All system tests marked with `@pytest.mark.system`
- Tests auto-skip when no Rhapsody instance is available (session-scoped skip in conftest)
- Unique element names via `uuid.uuid4().hex[:8]` suffix to prevent cross-test interference
- Cleanup in `finally` blocks via CLI `delete` commands
- No Python API imports for test operations (pure subprocess)
- Existing file `tests/system/cli/test_element_cli_subprocess.py` is deleted in Task 1

## CLI Command Reference (for test authors)

### Command Groups & Subcommands

| Group | Subcommands | Notes |
|-------|------------|-------|
| `project` | `new`, `open`, `list`, `close` | `new` takes positional `project_location` + `project_name` |
| `package` | `create`, `delete`, `view`, `list`, `update` | `create` has optional `--path` (defaults to root) |
| `class` | `create`, `delete`, `view`, `list`, `link`, `update` | `delete`/`view` accept `--path` OR `--guid` |
| `attribute` | `create`, `delete`, `view`, `list`, `update` | `create` requires `--path` |
| `operation` | `create`, `delete`, `view`, `list`, `update` | `create` requires `--path` |
| `port` | `create`, `delete`, `view`, `list`, `update` | `create` requires `--path` |

### Key Argument Patterns

- `create`: `--path <parent_path>` (required for class/attribute/operation/port; optional for package), `--input <json_file>` or positional `attributes` (inline JSON), `--verbose`
- `delete`: `--path <element_path>` (or `--guid` for class), `--verbose`
- `view`: `--path <element_path>` (or `--guid` for class), `--format table|json|csv`, `--output <file>`, `--verbose`
- `list`: `--path <container_path>`, `--format table|json|csv`, `--output <file>`, `--verbose`
- `link`: `--path <class_path>`, `--add <target_name>` or `--remove <target_name>`, `--type generalization`, `--verbose`
- `update`: `--path <element_path>`, `--input <json_file>` or positional `attributes`, `--verbose`
- `project new`: positional `project_location`, positional `project_name`, `--verbose`
- `project open`: positional `project_path`, `--verbose`
- `project list`: `--verbose` only (no path)
- `project close`: `--verbose` only

### JSON Input Format for `create`

```json
{"name": "MyClass", "description": "A test class", "attributes": ["attr1"], "operations": ["op1"]}
```

- `name` is required
- Array form `[{"name": "Cls1"}, {"name": "Cls2"}]` creates multiple elements

### Path Format

- Paths use `/` or `\` separator: `PkgName/ClassName` (see `PathResolver.normalize()`)
- The leading `Root` segment (case-insensitive) is optional and stripped — it is an alias for the project root, NOT the project's actual name
- The project name (e.g., `SystemTestProject`) is NOT a valid first path segment: `PathResolver` navigates from the root's *children*, and the root does not contain a child named after itself
- To reference a top-level package: use `PkgName` (not `ProjectName/PkgName`)
- To reference a nested element: use `PkgName/ClassName` (not `ProjectName::PkgName::ClassName`)
- For `package create`, omit `--path` entirely to create at project root (the action defaults to root when `--path` is falsy)
- For `package list`/`view`/`delete`, `--path` must resolve to a `Package` element (NOT a `Project`) — there is currently no CLI way to list root-level packages

---

### Task 1: Infrastructure — conftest, helpers, pytest marker, delete old test

**Files:**
- Modify: `pyproject.toml` (add `system` marker)
- Modify: `tests/system/conftest.py` (add Rhapsody skip logic)
- Create: `tests/system/cli/conftest.py` (CLI helpers + fixtures)
- Delete: `tests/system/cli/test_element_cli_subprocess.py`

**Interfaces:**
- Produces: `_run_cli(*args)` helper, `_run_cli_json(*args)` helper, `cli_project` fixture, `rhapsody_available` fixture

- [ ] **Step 1: Add `system` marker to pyproject.toml**

In `pyproject.toml`, find the `[tool.pytest.ini_options]` section and add `system` to the markers list:

```toml
markers = [
    "integration: marks tests as integration tests (require Rhapsody)",
    "system: marks tests as system tests (subprocess CLI, require Rhapsody)",
]
```

- [ ] **Step 2: Update tests/system/conftest.py with Rhapsody skip logic**

Replace the entire contents of `tests/system/conftest.py` with:

```python
"""System test configuration.

System tests invoke the CLI as a real subprocess. Tests requiring
Rhapsody auto-skip when no instance is available.
"""

import shutil
import sys
from pathlib import Path

import pytest

from rhapsody_cli import RhapsodyApplication

# Add unit directory to Python path so imports from unit tests work
sys.path.insert(0, str(Path(__file__).parent.parent / "unit"))

TEST_PROJECT_DIR = Path(__file__).parent.parent.parent / "demos" / "test_project_system"
TEST_PROJECT_NAME = "SystemTestProject"


@pytest.fixture(scope="session")
def rhapsody_available() -> bool:
    """Check if a running Rhapsody instance is available."""
    try:
        app = RhapsodyApplication.connect(attach_only=True)
        app.get_is_hidden_ui()
        return True
    except Exception:
        return False


@pytest.fixture(scope="session")
def _require_rhapsody(rhapsody_available: bool) -> None:
    """Skip tests that require Rhapsody when no instance is available.

    Not autouse — test classes that need Rhapsody must request this fixture
    explicitly (typically via an autouse=True wrapper in the class). This allows
    CLI parsing tests to run without Rhapsody.
    """
    if not rhapsody_available:
        pytest.skip("No running Rhapsody available — skipping system tests", allow_module_level=False)


@pytest.fixture(scope="session")
def test_project_dir() -> Path:
    """Session-scoped test project directory."""
    if TEST_PROJECT_DIR.exists():
        shutil.rmtree(TEST_PROJECT_DIR)
    TEST_PROJECT_DIR.mkdir(parents=True, exist_ok=True)
    return TEST_PROJECT_DIR
```

- [ ] **Step 3: Create tests/system/cli/conftest.py with CLI helpers and fixtures**

Create `tests/system/cli/conftest.py`:

```python
"""CLI system test helpers and fixtures.

Provides subprocess CLI invocation helpers and a session-scoped
test project created via the CLI itself.
"""

import json
import subprocess
import sys
import uuid
from pathlib import Path
from typing import Any, List

import pytest


def _run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    """Run the CLI as a subprocess.

    Args:
        *args: CLI arguments (e.g., "class", "create", "--path", "Pkg")

    Returns:
        CompletedProcess with stdout, stderr, returncode.
    """
    cmd = [sys.executable, "-m", "rhapsody_cli.cli.main", *args]
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=30,
    )


def _run_cli_json(*args: str) -> Any:
    """Run the CLI with --format json and parse the JSON output.

    Args:
        *args: CLI arguments (without --format json, which is added automatically)

    Returns:
        Parsed JSON data from stdout.

    Raises:
        AssertionError: If the process exits non-zero or JSON parsing fails.
    """
    result = _run_cli(*args, "--format", "json")
    assert result.returncode == 0, f"CLI failed: {result.stderr}"
    return json.loads(result.stdout)


def _unique_name(prefix: str = "Test") -> str:
    """Generate a unique element name with UUID suffix.

    Args:
        prefix: Prefix for the name (e.g., "Cls", "Pkg")

    Returns:
        A unique name like "TestCls_a1b2c3d4".
    """
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


@pytest.fixture(scope="session")
def cli_project(test_project_dir: Path) -> str:
    """Session-scoped test project created via CLI.

    Creates a new project using `rhapsody-cli project new` and yields
    the project name. The project stays open for the duration of the session
    (the `project close` CLI command is a no-op in subprocess mode — it
    checks `self._project` which is always None in a fresh process, rather
    than calling `app.active_project()`).

    Returns:
        The project name string.
    """
    project_name = "SystemTestProject"

    # Create project via CLI
    result = _run_cli("project", "new", str(test_project_dir), project_name)
    assert result.returncode == 0, f"Failed to create project: {result.stderr}"

    yield project_name

    # NOTE: project close is a no-op in subprocess mode (CLI bug).
    # The project remains open in the Rhapsody instance after the session.
    _run_cli("project", "close")
```

- [ ] **Step 4: Delete the old test_element_cli_subprocess.py**

Delete `tests/system/cli/test_element_cli_subprocess.py`. Its tests will be replaced by `test_cli_parsing.py` in Task 2.

- [ ] **Step 5: Verify infrastructure loads correctly**

Run: `python -c "import tests.system.cli.conftest; print('OK')"`
Expected: `OK` (no import errors)

Also run: `pytest tests/system/ --co -q 2>&1 | head -5`
Expected: Either collected tests or "no tests ran" — no collection errors.

- [ ] **Step 6: Commit**

```bash
git add pyproject.toml tests/system/conftest.py tests/system/cli/conftest.py
git rm tests/system/cli/test_element_cli_subprocess.py
git commit -m "test: add system test infrastructure (conftest, CLI helpers, markers)"
```

---

### Task 2: CLI Parsing Tests (No Rhapsody Required)

**Files:**
- Create: `tests/system/cli/test_cli_parsing.py`

**Interfaces:**
- Consumes: `_run_cli` from `tests/system/cli/conftest.py`

- [ ] **Step 1: Write the test file**

Create `tests/system/cli/test_cli_parsing.py`:

```python
"""CLI parsing and argument validation tests.

These tests do NOT require a running Rhapsody instance — they test
the CLI's argument parsing, help output, and error handling.
"""

import pytest

from tests.system.cli.conftest import _run_cli


@pytest.mark.system
class TestCLIParsing:
    """Test CLI argument parsing, help, and error messages."""

    def test_cli_help_command(self) -> None:
        """Test that --help returns 0 and shows usage."""
        result = _run_cli("--help")
        assert result.returncode == 0
        assert "Usage:" in result.stdout or "usage:" in result.stdout.lower()

    def test_cli_no_arguments_shows_usage(self) -> None:
        """Test that running with no arguments shows usage and exits 0."""
        result = _run_cli()
        # main._usage("") prints usage to stdout and exits 0 (no error)
        assert result.returncode == 0
        assert "Usage:" in result.stdout or "usage:" in result.stdout.lower()

    def test_cli_invalid_command(self) -> None:
        """Test that unknown commands are rejected."""
        result = _run_cli("invalid_command_xyz")
        assert result.returncode != 0
        assert "Unknown command" in result.stderr or "invalid choice" in result.stderr.lower() or "Error" in result.stderr

    def test_cli_verbose_flag_accepted(self) -> None:
        """Test that --verbose flag is accepted at subcommand level."""
        result = _run_cli("class", "list", "--path", "DummyPkg", "--verbose")
        # May fail with Rhapsody error, but should not have unrecognized arguments
        assert "unrecognized arguments" not in result.stderr.lower()

    def test_class_create_missing_path(self) -> None:
        """Test that class create without --path shows usage error."""
        result = _run_cli("class", "create")
        assert result.returncode != 0
        assert "required" in result.stderr.lower() or "usage:" in result.stderr.lower()

    def test_class_create_missing_input(self) -> None:
        """Test that class create with --path but no input shows error."""
        result = _run_cli("class", "create", "--path", "TestProject::Pkg")
        assert result.returncode != 0
        # Should complain about missing input data
        assert "input" in result.stderr.lower() or "attributes" in result.stderr.lower() or "error" in result.stderr.lower()

    def test_class_delete_missing_arguments(self) -> None:
        """Test that class delete without --path or --guid shows error."""
        result = _run_cli("class", "delete")
        assert result.returncode != 0
        assert "error" in result.stderr.lower() or "usage" in result.stderr.lower()

    def test_package_delete_missing_path(self) -> None:
        """Test that package delete without --path shows usage error."""
        result = _run_cli("package", "delete")
        assert result.returncode != 0
        assert "required" in result.stderr.lower() or "usage:" in result.stderr.lower()

    def test_attribute_create_missing_path(self) -> None:
        """Test that attribute create without --path shows usage error."""
        result = _run_cli("attribute", "create")
        assert result.returncode != 0
        assert "required" in result.stderr.lower() or "usage:" in result.stderr.lower()

    def test_operation_create_missing_path(self) -> None:
        """Test that operation create without --path shows usage error."""
        result = _run_cli("operation", "create")
        assert result.returncode != 0
        assert "required" in result.stderr.lower() or "usage:" in result.stderr.lower()

    def test_port_create_missing_path(self) -> None:
        """Test that port create without --path shows usage error."""
        result = _run_cli("port", "create")
        assert result.returncode != 0
        assert "required" in result.stderr.lower() or "usage:" in result.stderr.lower()

    def test_project_open_missing_arguments(self) -> None:
        """Test that project open without project_path shows usage error."""
        result = _run_cli("project", "open")
        assert result.returncode != 0
        assert "required" in result.stderr.lower() or "usage:" in result.stderr.lower()

    def test_project_new_missing_arguments(self) -> None:
        """Test that project new without arguments shows usage error."""
        result = _run_cli("project", "new")
        assert result.returncode != 0
        assert "required" in result.stderr.lower() or "usage:" in result.stderr.lower()

    def test_class_list_with_invalid_format(self) -> None:
        """Test that invalid --format value is rejected."""
        result = _run_cli("class", "list", "--path", "Dummy", "--format", "xml")
        assert result.returncode != 0
        assert "invalid choice" in result.stderr.lower() or "usage" in result.stderr.lower()

    def test_class_view_missing_path_and_guid(self) -> None:
        """Test that class view without --path or --guid shows error."""
        result = _run_cli("class", "view")
        assert result.returncode != 0
        assert "error" in result.stderr.lower() or "usage" in result.stderr.lower()
```

- [ ] **Step 2: Run the parsing tests**

Run: `pytest tests/system/cli/test_cli_parsing.py -v --tb=short -p no:cacheprovider`
Expected: All tests pass (they don't require Rhapsody — the `TestCLIParsing` class does not request `_require_rhapsody`).

- [ ] **Step 3: Commit**

```bash
git add tests/system/cli/test_cli_parsing.py tests/system/conftest.py
git commit -m "test: add CLI parsing system tests (help, errors, missing args)"
```

---

### Task 3: Project CLI System Tests

**Files:**
- Create: `tests/system/cli/test_project_cli.py`

**Interfaces:**
- Consumes: `_run_cli` from `tests/system/cli/conftest.py`, `_require_rhapsody` from `tests/system/conftest.py`

- [ ] **Step 1: Write the test file**

Create `tests/system/cli/test_project_cli.py`:

```python
"""System tests for the `project` CLI command group.

Tests project lifecycle: new, list, close, open — all via subprocess.

Known CLI bug: `project close` checks `self._project` (always None in
subprocess mode) instead of calling `app.active_project()`, so it is a
no-op. Tests that depend on close are marked xfail until the CLI is fixed.
"""

import pytest

from tests.system.cli.conftest import _run_cli


@pytest.mark.system
class TestProjectCLI:
    """Test project CLI commands via subprocess."""

    @pytest.fixture(autouse=True)
    def _require_rhapsody(self, _require_rhapsody: None) -> None:
        """Skip these tests if no Rhapsody instance is available."""

    def test_project_new_creates_project(self, test_project_dir) -> None:
        """Test that `project new` creates a project and it appears in list."""
        import shutil

        project_dir = test_project_dir / "new_test"
        project_dir.mkdir(parents=True, exist_ok=True)
        project_name = f"ProjNew_{__import__('uuid').uuid4().hex[:8]}"

        try:
            result = _run_cli("project", "new", str(project_dir), project_name)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify project appears in list
            list_result = _run_cli("project", "list")
            assert list_result.returncode == 0
            assert project_name in list_result.stdout
        finally:
            shutil.rmtree(project_dir, ignore_errors=True)

    def test_project_list_shows_open_project(self, cli_project: str) -> None:
        """Test that `project list` shows the open project."""
        result = _run_cli("project", "list")
        assert result.returncode == 0
        assert cli_project in result.stdout

    @pytest.mark.xfail(
        reason="CLI bug: project close checks self._project (always None in "
        "subprocess mode) instead of app.active_project(); no-op until fixed"
    )
    def test_project_close_removes_from_list(self, test_project_dir) -> None:
        """Test that `project close` removes project from list."""
        import shutil

        project_dir = test_project_dir / "close_test"
        project_dir.mkdir(parents=True, exist_ok=True)
        project_name = f"ProjClose_{__import__('uuid').uuid4().hex[:8]}"

        try:
            _run_cli("project", "new", str(project_dir), project_name)
            _run_cli("project", "close")

            result = _run_cli("project", "list")
            assert result.returncode == 0
            assert project_name not in result.stdout
        finally:
            shutil.rmtree(project_dir, ignore_errors=True)

    @pytest.mark.xfail(
        reason="CLI bug: project close is a no-op in subprocess mode; cannot "
        "close before re-opening"
    )
    def test_project_open_existing_project(self, test_project_dir) -> None:
        """Test that `project open` opens a previously created project."""
        import shutil

        project_dir = test_project_dir / "open_test"
        project_dir.mkdir(parents=True, exist_ok=True)
        project_name = f"ProjOpen_{__import__('uuid').uuid4().hex[:8]}"

        try:
            # Create and close
            _run_cli("project", "new", str(project_dir), project_name)
            _run_cli("project", "close")

            # Re-open
            project_file = project_dir / f"{project_name}.rpy"
            result = _run_cli("project", "open", str(project_file))
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify in list
            list_result = _run_cli("project", "list")
            assert list_result.returncode == 0
            assert project_name in list_result.stdout
        finally:
            shutil.rmtree(project_dir, ignore_errors=True)
```

- [ ] **Step 2: Run the project tests (requires Rhapsody)**

Run: `pytest tests/system/cli/test_project_cli.py -v --tb=short`
Expected: All tests pass if Rhapsody is running with a test project.

- [ ] **Step 3: Commit**

```bash
git add tests/system/cli/test_project_cli.py
git commit -m "test: add project CLI system tests (new, list, close, open)"
```

---

### Task 4: Package CLI System Tests

**Files:**
- Create: `tests/system/cli/test_package_cli.py`

**Interfaces:**
- Consumes: `_run_cli`, `_run_cli_json`, `_unique_name`, `cli_project` from `tests/system/cli/conftest.py`

- [ ] **Step 1: Write the test file**

Create `tests/system/cli/test_package_cli.py`:

```python
"""System tests for the `package` CLI command group.

Tests package CRUD lifecycle via subprocess against a live Rhapsody project.

Path notes: Paths use "/" separator. The project name is NOT a valid path
segment — omit --path to create at root. `package list/view/delete` require
a Package path (not Project), so root-level packages are verified via
`package view`, not `package list`.
"""

import json
import uuid

import pytest

from tests.system.cli.conftest import _run_cli, _unique_name


@pytest.mark.system
class TestPackageCLI:
    """Test package CLI commands via subprocess."""

    @pytest.fixture(autouse=True)
    def _require_rhapsody(self, _require_rhapsody: None) -> None:
        """Skip these tests if no Rhapsody instance is available."""

    @staticmethod
    def _create_root_package(name: str) -> str:
        """Create a package at project root via CLI and return its path.

        Args:
            name: Package name to create.

        Returns:
            Package path (just the name, since root-level packages have no parent prefix).
        """
        pkg_json = json.dumps({"name": name})
        result = _run_cli("package", "create", "--input", pkg_json)
        assert result.returncode == 0, f"Failed to create root package: {result.stderr}"
        return name

    @staticmethod
    def _create_nested_package(parent_path: str, name: str) -> str:
        """Create a nested package under a parent via CLI and return its path.

        Args:
            parent_path: Parent package path (e.g., "ParentPkg").
            name: Package name to create.

        Returns:
            Full path of the created package (e.g., "ParentPkg/ChildPkg").
        """
        pkg_json = json.dumps({"name": name})
        result = _run_cli("package", "create", "--path", parent_path, "--input", pkg_json)
        assert result.returncode == 0, f"Failed to create nested package: {result.stderr}"
        return f"{parent_path}/{name}"

    def test_package_create_at_root(self, cli_project: str) -> None:
        """Test creating a package at project root (omit --path)."""
        pkg_name = _unique_name("Pkg")
        pkg_json = json.dumps({"name": pkg_name})

        # Omit --path to create at project root
        result = _run_cli("package", "create", "--input", pkg_json)
        assert result.returncode == 0, f"Failed: {result.stderr}"

        # Verify via package view (package list cannot operate on project root)
        view_result = _run_cli("package", "view", "--path", pkg_name, "--format", "json")
        assert view_result.returncode == 0, f"View failed: {view_result.stderr}"
        data = json.loads(view_result.stdout)
        assert data["name"] == pkg_name

        # Cleanup
        _run_cli("package", "delete", "--path", pkg_name)

    def test_package_create_nested(self, cli_project: str) -> None:
        """Test creating a nested package under another package."""
        parent_name = _unique_name("ParentPkg")
        child_name = _unique_name("ChildPkg")

        try:
            # Create parent at root
            parent_path = self._create_root_package(parent_name)

            # Create child under parent
            child_path = self._create_nested_package(parent_path, child_name)

            # Verify child appears in parent's list
            list_result = _run_cli("package", "list", "--path", parent_path, "--format", "json")
            assert list_result.returncode == 0
            packages = json.loads(list_result.stdout)
            assert child_name in packages
        finally:
            # Cleanup parent (deletes children too)
            _run_cli("package", "delete", "--path", parent_name)

    def test_package_view_existing(self, cli_project: str) -> None:
        """Test viewing an existing package."""
        pkg_name = _unique_name("ViewPkg")
        pkg_path = self._create_root_package(pkg_name)

        try:
            result = _run_cli("package", "view", "--path", pkg_path, "--format", "json")
            assert result.returncode == 0, f"Failed: {result.stderr}"
            data = json.loads(result.stdout)
            assert data["name"] == pkg_name
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_package_view_nonexistent(self, cli_project: str) -> None:
        """Test viewing a non-existent package returns error."""
        result = _run_cli("package", "view", "--path", f"NonExistentPkg_{uuid.uuid4().hex[:8]}")
        assert result.returncode != 0
        assert "error" in result.stderr.lower() or "not found" in result.stderr.lower() or "failed" in result.stderr.lower()

    def test_package_list_in_package(self, cli_project: str) -> None:
        """Test listing nested packages within a package."""
        parent_name = _unique_name("ListParent")
        child1_name = _unique_name("Child1")
        child2_name = _unique_name("Child2")

        try:
            parent_path = self._create_root_package(parent_name)
            self._create_nested_package(parent_path, child1_name)
            self._create_nested_package(parent_path, child2_name)

            result = _run_cli("package", "list", "--path", parent_path, "--format", "json")
            assert result.returncode == 0
            packages = json.loads(result.stdout)
            assert child1_name in packages
            assert child2_name in packages
        finally:
            _run_cli("package", "delete", "--path", parent_name)

    def test_package_delete_existing(self, cli_project: str) -> None:
        """Test deleting an existing package."""
        pkg_name = _unique_name("DelPkg")
        pkg_path = self._create_root_package(pkg_name)

        result = _run_cli("package", "delete", "--path", pkg_path)
        assert result.returncode == 0, f"Failed: {result.stderr}"

        # Verify package is gone
        view_result = _run_cli("package", "view", "--path", pkg_path)
        assert view_result.returncode != 0

    def test_package_delete_nonexistent(self, cli_project: str) -> None:
        """Test deleting a non-existent package returns error."""
        result = _run_cli("package", "delete", "--path", f"NonExistentDel_{uuid.uuid4().hex[:8]}")
        assert result.returncode != 0
        assert "error" in result.stderr.lower() or "failed" in result.stderr.lower()

    def test_package_create_invalid_json(self, cli_project: str) -> None:
        """Test that invalid JSON input returns error."""
        result = _run_cli("package", "create", "--input", "{invalid json}")
        assert result.returncode != 0
        assert "json" in result.stderr.lower() or "error" in result.stderr.lower()
```

- [ ] **Step 2: Run the package tests (requires Rhapsody)**

Run: `pytest tests/system/cli/test_package_cli.py -v --tb=short`
Expected: All tests pass.

- [ ] **Step 3: Commit**

```bash
git add tests/system/cli/test_package_cli.py
git commit -m "test: add package CLI system tests (create, view, list, delete)"
```

---

### Task 5: Class CLI System Tests

**Files:**
- Create: `tests/system/cli/test_class_cli.py`

**Interfaces:**
- Consumes: `_run_cli`, `_run_cli_json`, `_unique_name`, `cli_project` from `tests/system/cli/conftest.py`

- [ ] **Step 1: Write the test file**

Create `tests/system/cli/test_class_cli.py`:

```python
"""System tests for the `class` CLI command group.

Tests class CRUD lifecycle and link (generalization) via subprocess.

Path notes: Paths use "/" separator. Packages are created at root by
omitting --path. Class paths are "PkgName/ClassName".
"""

import json
import uuid

import pytest

from tests.system.cli.conftest import _run_cli, _unique_name


@pytest.mark.system
class TestClassCLI:
    """Test class CLI commands via subprocess."""

    @pytest.fixture(autouse=True)
    def _require_rhapsody(self, _require_rhapsody: None) -> None:
        """Skip these tests if no Rhapsody instance is available."""

    @staticmethod
    def _create_package(name: str) -> str:
        """Create a package at project root via CLI and return its path."""
        pkg_json = json.dumps({"name": name})
        result = _run_cli("package", "create", "--input", pkg_json)
        assert result.returncode == 0, f"Failed to create package: {result.stderr}"
        return name

    @staticmethod
    def _create_class(pkg_path: str, name: str) -> str:
        """Create a class via CLI and return its full path."""
        cls_json = json.dumps({"name": name})
        result = _run_cli("class", "create", "--path", pkg_path, "--input", cls_json)
        assert result.returncode == 0, f"Failed to create class: {result.stderr}"
        return f"{pkg_path}/{name}"

    def test_class_create_under_package(self, cli_project: str) -> None:
        """Test creating a class under a package."""
        pkg_name = _unique_name("Pkg")
        cls_name = _unique_name("Cls")
        pkg_path = self._create_package(pkg_name)
        cls_path = f"{pkg_path}/{cls_name}"

        try:
            cls_json = json.dumps({"name": cls_name})
            result = _run_cli("class", "create", "--path", pkg_path, "--input", cls_json)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify via list
            list_result = _run_cli("class", "list", "--path", pkg_path, "--format", "json")
            assert list_result.returncode == 0
            classes = json.loads(list_result.stdout)
            assert cls_name in classes
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_view_existing(self, cli_project: str) -> None:
        """Test viewing an existing class."""
        pkg_name = _unique_name("ViewPkg")
        cls_name = _unique_name("ViewCls")
        pkg_path = self._create_package(pkg_name)
        cls_path = self._create_class(pkg_path, cls_name)

        try:
            result = _run_cli("class", "view", "--path", cls_path, "--format", "json")
            assert result.returncode == 0, f"Failed: {result.stderr}"
            data = json.loads(result.stdout)
            assert data["name"] == cls_name
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_view_nonexistent(self, cli_project: str) -> None:
        """Test viewing a non-existent class returns error."""
        pkg_name = _unique_name("NoClsPkg")
        pkg_path = self._create_package(pkg_name)

        try:
            result = _run_cli("class", "view", "--path", f"{pkg_path}/NonExistent_{uuid.uuid4().hex[:8]}")
            assert result.returncode != 0
            assert "error" in result.stderr.lower() or "failed" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_list_in_package(self, cli_project: str) -> None:
        """Test listing classes in a package."""
        pkg_name = _unique_name("ListPkg")
        cls1_name = _unique_name("Cls1")
        cls2_name = _unique_name("Cls2")
        pkg_path = self._create_package(pkg_name)
        self._create_class(pkg_path, cls1_name)
        self._create_class(pkg_path, cls2_name)

        try:
            result = _run_cli("class", "list", "--path", pkg_path, "--format", "json")
            assert result.returncode == 0
            classes = json.loads(result.stdout)
            assert cls1_name in classes
            assert cls2_name in classes
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_delete_existing(self, cli_project: str) -> None:
        """Test deleting an existing class."""
        pkg_name = _unique_name("DelPkg")
        cls_name = _unique_name("DelCls")
        pkg_path = self._create_package(pkg_name)
        cls_path = self._create_class(pkg_path, cls_name)

        try:
            result = _run_cli("class", "delete", "--path", cls_path)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify class is gone
            list_result = _run_cli("class", "list", "--path", pkg_path, "--format", "json")
            assert list_result.returncode == 0
            classes = json.loads(list_result.stdout)
            assert cls_name not in classes
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_delete_nonexistent(self, cli_project: str) -> None:
        """Test deleting a non-existent class returns error."""
        pkg_name = _unique_name("NoDelPkg")
        pkg_path = self._create_package(pkg_name)

        try:
            result = _run_cli("class", "delete", "--path", f"{pkg_path}/NonExistent_{uuid.uuid4().hex[:8]}")
            assert result.returncode != 0
            assert "error" in result.stderr.lower() or "failed" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_link_generalization(self, cli_project: str) -> None:
        """Test adding a generalization link between classes."""
        pkg_name = _unique_name("LinkPkg")
        parent_cls_name = _unique_name("ParentCls")
        child_cls_name = _unique_name("ChildCls")
        pkg_path = self._create_package(pkg_name)
        parent_path = self._create_class(pkg_path, parent_cls_name)
        child_path = self._create_class(pkg_path, child_cls_name)

        try:
            # Add generalization: child -> parent
            result = _run_cli("class", "link", "--path", child_path, "--add", parent_cls_name)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify by viewing child class
            view_result = _run_cli("class", "view", "--path", child_path, "--format", "json")
            assert view_result.returncode == 0
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_create_with_attributes(self, cli_project: str) -> None:
        """Test creating a class with attributes and operations in JSON."""
        pkg_name = _unique_name("AttrPkg")
        cls_name = _unique_name("AttrCls")
        pkg_path = self._create_package(pkg_name)

        try:
            cls_json = json.dumps({
                "name": cls_name,
                "attributes": ["attr1", "attr2"],
                "operations": ["op1"],
            })
            result = _run_cli("class", "create", "--path", pkg_path, "--input", cls_json)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify via view
            view_result = _run_cli("class", "view", "--path", f"{pkg_path}/{cls_name}", "--format", "json")
            assert view_result.returncode == 0
            data = json.loads(view_result.stdout)
            assert "attr1" in data["attributes"]
            assert "attr2" in data["attributes"]
            assert "op1" in data["operations"]
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_class_create_invalid_json(self, cli_project: str) -> None:
        """Test that invalid JSON input returns error."""
        pkg_name = _unique_name("BadJsonPkg")
        pkg_path = self._create_package(pkg_name)

        try:
            result = _run_cli("class", "create", "--path", pkg_path, "--input", "{invalid}")
            assert result.returncode != 0
            assert "json" in result.stderr.lower() or "error" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)
```

- [ ] **Step 2: Run the class tests (requires Rhapsody)**

Run: `pytest tests/system/cli/test_class_cli.py -v --tb=short`
Expected: All tests pass.

- [ ] **Step 3: Commit**

```bash
git add tests/system/cli/test_class_cli.py
git commit -m "test: add class CLI system tests (create, view, list, delete, link)"
```

---

### Task 6: Attribute CLI System Tests

**Files:**
- Create: `tests/system/cli/test_attribute_cli.py`

**Interfaces:**
- Consumes: `_run_cli`, `_unique_name`, `cli_project` from `tests/system/cli/conftest.py`

- [ ] **Step 1: Write the test file**

Create `tests/system/cli/test_attribute_cli.py`:

```python
"""System tests for the `attribute` CLI command group.

Tests attribute CRUD lifecycle via subprocess against a live Rhapsody project.

Path notes: Paths use "/" separator. Attribute view/delete require TWO
args: --path <class_path> AND --name <attr_name> (or --guid). They do NOT
accept a combined element path.
"""

import json
import uuid

import pytest

from tests.system.cli.conftest import _run_cli, _unique_name


@pytest.mark.system
class TestAttributeCLI:
    """Test attribute CLI commands via subprocess."""

    @pytest.fixture(autouse=True)
    def _require_rhapsody(self, _require_rhapsody: None) -> None:
        """Skip these tests if no Rhapsody instance is available."""

    @staticmethod
    def _create_package_and_class(pkg_name: str, cls_name: str) -> tuple[str, str]:
        """Create a package at root and a class under it.

        Returns:
            Tuple of (pkg_path, cls_path). Both use "/" separator.
        """
        pkg_json = json.dumps({"name": pkg_name})
        result = _run_cli("package", "create", "--input", pkg_json)
        assert result.returncode == 0, f"Failed to create package: {result.stderr}"
        pkg_path = pkg_name

        cls_json = json.dumps({"name": cls_name})
        result = _run_cli("class", "create", "--path", pkg_path, "--input", cls_json)
        assert result.returncode == 0, f"Failed to create class: {result.stderr}"
        cls_path = f"{pkg_path}/{cls_name}"
        return pkg_path, cls_path

    def test_attribute_create_under_class(self, cli_project: str) -> None:
        """Test creating an attribute under a class."""
        pkg_name = _unique_name("AttrPkg")
        cls_name = _unique_name("AttrCls")
        attr_name = _unique_name("myAttr")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            attr_json = json.dumps({"name": attr_name})
            result = _run_cli("attribute", "create", "--path", cls_path, "--input", attr_json)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify via list
            list_result = _run_cli("attribute", "list", "--path", cls_path, "--format", "json")
            assert list_result.returncode == 0
            attributes = json.loads(list_result.stdout)
            assert attr_name in attributes
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_attribute_view_existing(self, cli_project: str) -> None:
        """Test viewing an existing attribute via --path + --name."""
        pkg_name = _unique_name("ViewPkg")
        cls_name = _unique_name("ViewCls")
        attr_name = _unique_name("viewAttr")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            attr_json = json.dumps({"name": attr_name})
            _run_cli("attribute", "create", "--path", cls_path, "--input", attr_json)

            # View uses --path <class_path> --name <attr_name> (NOT a combined path)
            result = _run_cli("attribute", "view", "--path", cls_path, "--name", attr_name, "--format", "json")
            assert result.returncode == 0, f"Failed: {result.stderr}"
            data = json.loads(result.stdout)
            assert data["name"] == attr_name
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_attribute_view_nonexistent(self, cli_project: str) -> None:
        """Test viewing a non-existent attribute returns error."""
        pkg_name = _unique_name("NoAttrPkg")
        cls_name = _unique_name("NoAttrCls")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            # View uses --path + --name (not a combined path)
            result = _run_cli(
                "attribute", "view",
                "--path", cls_path,
                "--name", f"NonExistent_{uuid.uuid4().hex[:8]}",
            )
            assert result.returncode != 0
            assert "error" in result.stderr.lower() or "failed" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_attribute_list_in_class(self, cli_project: str) -> None:
        """Test listing attributes in a class."""
        pkg_name = _unique_name("ListPkg")
        cls_name = _unique_name("ListCls")
        attr1_name = _unique_name("attr1")
        attr2_name = _unique_name("attr2")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            _run_cli("attribute", "create", "--path", cls_path, "--input", json.dumps({"name": attr1_name}))
            _run_cli("attribute", "create", "--path", cls_path, "--input", json.dumps({"name": attr2_name}))

            result = _run_cli("attribute", "list", "--path", cls_path, "--format", "json")
            assert result.returncode == 0
            attributes = json.loads(result.stdout)
            assert attr1_name in attributes
            assert attr2_name in attributes
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_attribute_delete_existing(self, cli_project: str) -> None:
        """Test deleting an existing attribute via --path + --name."""
        pkg_name = _unique_name("DelPkg")
        cls_name = _unique_name("DelCls")
        attr_name = _unique_name("delAttr")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            _run_cli("attribute", "create", "--path", cls_path, "--input", json.dumps({"name": attr_name}))

            # Delete uses --path <class_path> --name <attr_name> (NOT a combined path)
            result = _run_cli("attribute", "delete", "--path", cls_path, "--name", attr_name)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify attribute is gone
            list_result = _run_cli("attribute", "list", "--path", cls_path, "--format", "json")
            assert list_result.returncode == 0
            attributes = json.loads(list_result.stdout)
            assert attr_name not in attributes
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_attribute_delete_nonexistent(self, cli_project: str) -> None:
        """Test deleting a non-existent attribute returns error."""
        pkg_name = _unique_name("NoDelPkg")
        cls_name = _unique_name("NoDelCls")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            # Delete uses --path + --name
            result = _run_cli(
                "attribute", "delete",
                "--path", cls_path,
                "--name", f"NonExistent_{uuid.uuid4().hex[:8]}",
            )
            assert result.returncode != 0
            assert "error" in result.stderr.lower() or "failed" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_attribute_create_invalid_json(self, cli_project: str) -> None:
        """Test that invalid JSON input returns error."""
        pkg_name = _unique_name("BadJsonPkg")
        cls_name = _unique_name("BadJsonCls")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            result = _run_cli("attribute", "create", "--path", cls_path, "--input", "{invalid}")
            assert result.returncode != 0
            assert "json" in result.stderr.lower() or "error" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)
```

- [ ] **Step 2: Run the attribute tests (requires Rhapsody)**

Run: `pytest tests/system/cli/test_attribute_cli.py -v --tb=short`
Expected: All tests pass.

- [ ] **Step 3: Commit**

```bash
git add tests/system/cli/test_attribute_cli.py
git commit -m "test: add attribute CLI system tests (create, view, list, delete)"
```

---

### Task 7: Operation CLI System Tests

**Files:**
- Create: `tests/system/cli/test_operation_cli.py`

**Interfaces:**
- Consumes: `_run_cli`, `_unique_name`, `cli_project` from `tests/system/cli/conftest.py`

- [ ] **Step 1: Write the test file**

Create `tests/system/cli/test_operation_cli.py`:

```python
"""System tests for the `operation` CLI command group.

Tests operation CRUD lifecycle via subprocess against a live Rhapsody project.

Path notes: Paths use "/" separator. Operation view/delete require TWO
args: --path <class_path> AND --name <op_name> (or --guid). They do NOT
accept a combined element path.
"""

import json
import uuid

import pytest

from tests.system.cli.conftest import _run_cli, _unique_name


@pytest.mark.system
class TestOperationCLI:
    """Test operation CLI commands via subprocess."""

    @pytest.fixture(autouse=True)
    def _require_rhapsody(self, _require_rhapsody: None) -> None:
        """Skip these tests if no Rhapsody instance is available."""

    @staticmethod
    def _create_package_and_class(pkg_name: str, cls_name: str) -> tuple[str, str]:
        """Create a package at root and a class under it.

        Returns:
            Tuple of (pkg_path, cls_path). Both use "/" separator.
        """
        pkg_json = json.dumps({"name": pkg_name})
        result = _run_cli("package", "create", "--input", pkg_json)
        assert result.returncode == 0, f"Failed to create package: {result.stderr}"
        pkg_path = pkg_name

        cls_json = json.dumps({"name": cls_name})
        result = _run_cli("class", "create", "--path", pkg_path, "--input", cls_json)
        assert result.returncode == 0, f"Failed to create class: {result.stderr}"
        cls_path = f"{pkg_path}/{cls_name}"
        return pkg_path, cls_path

    def test_operation_create_under_class(self, cli_project: str) -> None:
        """Test creating an operation under a class."""
        pkg_name = _unique_name("OpPkg")
        cls_name = _unique_name("OpCls")
        op_name = _unique_name("myOp")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            op_json = json.dumps({"name": op_name})
            result = _run_cli("operation", "create", "--path", cls_path, "--input", op_json)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify via list
            list_result = _run_cli("operation", "list", "--path", cls_path, "--format", "json")
            assert list_result.returncode == 0
            operations = json.loads(list_result.stdout)
            assert op_name in operations
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_operation_view_existing(self, cli_project: str) -> None:
        """Test viewing an existing operation via --path + --name."""
        pkg_name = _unique_name("ViewPkg")
        cls_name = _unique_name("ViewCls")
        op_name = _unique_name("viewOp")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            op_json = json.dumps({"name": op_name})
            _run_cli("operation", "create", "--path", cls_path, "--input", op_json)

            # View uses --path <class_path> --name <op_name> (NOT a combined path)
            result = _run_cli("operation", "view", "--path", cls_path, "--name", op_name, "--format", "json")
            assert result.returncode == 0, f"Failed: {result.stderr}"
            data = json.loads(result.stdout)
            assert data["name"] == op_name
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_operation_view_nonexistent(self, cli_project: str) -> None:
        """Test viewing a non-existent operation returns error."""
        pkg_name = _unique_name("NoOpPkg")
        cls_name = _unique_name("NoOpCls")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            # View uses --path + --name (not a combined path)
            result = _run_cli(
                "operation", "view",
                "--path", cls_path,
                "--name", f"NonExistent_{uuid.uuid4().hex[:8]}",
            )
            assert result.returncode != 0
            assert "error" in result.stderr.lower() or "failed" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_operation_list_in_class(self, cli_project: str) -> None:
        """Test listing operations in a class."""
        pkg_name = _unique_name("ListPkg")
        cls_name = _unique_name("ListCls")
        op1_name = _unique_name("op1")
        op2_name = _unique_name("op2")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            _run_cli("operation", "create", "--path", cls_path, "--input", json.dumps({"name": op1_name}))
            _run_cli("operation", "create", "--path", cls_path, "--input", json.dumps({"name": op2_name}))

            result = _run_cli("operation", "list", "--path", cls_path, "--format", "json")
            assert result.returncode == 0
            operations = json.loads(result.stdout)
            assert op1_name in operations
            assert op2_name in operations
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_operation_delete_existing(self, cli_project: str) -> None:
        """Test deleting an existing operation via --path + --name."""
        pkg_name = _unique_name("DelPkg")
        cls_name = _unique_name("DelCls")
        op_name = _unique_name("delOp")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            _run_cli("operation", "create", "--path", cls_path, "--input", json.dumps({"name": op_name}))

            # Delete uses --path <class_path> --name <op_name> (NOT a combined path)
            result = _run_cli("operation", "delete", "--path", cls_path, "--name", op_name)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify operation is gone
            list_result = _run_cli("operation", "list", "--path", cls_path, "--format", "json")
            assert list_result.returncode == 0
            operations = json.loads(list_result.stdout)
            assert op_name not in operations
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_operation_delete_nonexistent(self, cli_project: str) -> None:
        """Test deleting a non-existent operation returns error."""
        pkg_name = _unique_name("NoDelPkg")
        cls_name = _unique_name("NoDelCls")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            # Delete uses --path + --name
            result = _run_cli(
                "operation", "delete",
                "--path", cls_path,
                "--name", f"NonExistent_{uuid.uuid4().hex[:8]}",
            )
            assert result.returncode != 0
            assert "error" in result.stderr.lower() or "failed" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_operation_create_invalid_json(self, cli_project: str) -> None:
        """Test that invalid JSON input returns error."""
        pkg_name = _unique_name("BadJsonPkg")
        cls_name = _unique_name("BadJsonCls")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            result = _run_cli("operation", "create", "--path", cls_path, "--input", "{invalid}")
            assert result.returncode != 0
            assert "json" in result.stderr.lower() or "error" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)
```

- [ ] **Step 2: Run the operation tests (requires Rhapsody)**

Run: `pytest tests/system/cli/test_operation_cli.py -v --tb=short`
Expected: All tests pass.

- [ ] **Step 3: Commit**

```bash
git add tests/system/cli/test_operation_cli.py
git commit -m "test: add operation CLI system tests (create, view, list, delete)"
```

---

### Task 8: Port CLI System Tests

**Files:**
- Create: `tests/system/cli/test_port_cli.py`

**Interfaces:**
- Consumes: `_run_cli`, `_unique_name`, `cli_project` from `tests/system/cli/conftest.py`

- [ ] **Step 1: Write the test file**

Create `tests/system/cli/test_port_cli.py`:

```python
"""System tests for the `port` CLI command group.

Tests port CRUD lifecycle via subprocess against a live Rhapsody project.

Path notes: Paths use "/" separator. Port view/delete require TWO
args: --path <class_path> AND --name <port_name> (or --guid). They do NOT
accept a combined element path.
"""

import json
import uuid

import pytest

from tests.system.cli.conftest import _run_cli, _unique_name


@pytest.mark.system
class TestPortCLI:
    """Test port CLI commands via subprocess."""

    @pytest.fixture(autouse=True)
    def _require_rhapsody(self, _require_rhapsody: None) -> None:
        """Skip these tests if no Rhapsody instance is available."""

    @staticmethod
    def _create_package_and_class(pkg_name: str, cls_name: str) -> tuple[str, str]:
        """Create a package at root and a class under it.

        Returns:
            Tuple of (pkg_path, cls_path). Both use "/" separator.
        """
        pkg_json = json.dumps({"name": pkg_name})
        result = _run_cli("package", "create", "--input", pkg_json)
        assert result.returncode == 0, f"Failed to create package: {result.stderr}"
        pkg_path = pkg_name

        cls_json = json.dumps({"name": cls_name})
        result = _run_cli("class", "create", "--path", pkg_path, "--input", cls_json)
        assert result.returncode == 0, f"Failed to create class: {result.stderr}"
        cls_path = f"{pkg_path}/{cls_name}"
        return pkg_path, cls_path

    def test_port_create_under_class(self, cli_project: str) -> None:
        """Test creating a port under a class."""
        pkg_name = _unique_name("PortPkg")
        cls_name = _unique_name("PortCls")
        port_name = _unique_name("myPort")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            port_json = json.dumps({"name": port_name})
            result = _run_cli("port", "create", "--path", cls_path, "--input", port_json)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify via list
            list_result = _run_cli("port", "list", "--path", cls_path, "--format", "json")
            assert list_result.returncode == 0
            ports = json.loads(list_result.stdout)
            assert port_name in ports
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_port_view_existing(self, cli_project: str) -> None:
        """Test viewing an existing port via --path + --name."""
        pkg_name = _unique_name("ViewPkg")
        cls_name = _unique_name("ViewCls")
        port_name = _unique_name("viewPort")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            port_json = json.dumps({"name": port_name})
            _run_cli("port", "create", "--path", cls_path, "--input", port_json)

            # View uses --path <class_path> --name <port_name> (NOT a combined path)
            result = _run_cli("port", "view", "--path", cls_path, "--name", port_name, "--format", "json")
            assert result.returncode == 0, f"Failed: {result.stderr}"
            data = json.loads(result.stdout)
            assert data["name"] == port_name
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_port_view_nonexistent(self, cli_project: str) -> None:
        """Test viewing a non-existent port returns error."""
        pkg_name = _unique_name("NoPortPkg")
        cls_name = _unique_name("NoPortCls")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            # View uses --path + --name (not a combined path)
            result = _run_cli(
                "port", "view",
                "--path", cls_path,
                "--name", f"NonExistent_{uuid.uuid4().hex[:8]}",
            )
            assert result.returncode != 0
            assert "error" in result.stderr.lower() or "failed" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_port_list_in_class(self, cli_project: str) -> None:
        """Test listing ports in a class."""
        pkg_name = _unique_name("ListPkg")
        cls_name = _unique_name("ListCls")
        port1_name = _unique_name("port1")
        port2_name = _unique_name("port2")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            _run_cli("port", "create", "--path", cls_path, "--input", json.dumps({"name": port1_name}))
            _run_cli("port", "create", "--path", cls_path, "--input", json.dumps({"name": port2_name}))

            result = _run_cli("port", "list", "--path", cls_path, "--format", "json")
            assert result.returncode == 0
            ports = json.loads(result.stdout)
            assert port1_name in ports
            assert port2_name in ports
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_port_delete_existing(self, cli_project: str) -> None:
        """Test deleting an existing port via --path + --name."""
        pkg_name = _unique_name("DelPkg")
        cls_name = _unique_name("DelCls")
        port_name = _unique_name("delPort")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            _run_cli("port", "create", "--path", cls_path, "--input", json.dumps({"name": port_name}))

            # Delete uses --path <class_path> --name <port_name> (NOT a combined path)
            result = _run_cli("port", "delete", "--path", cls_path, "--name", port_name)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify port is gone
            list_result = _run_cli("port", "list", "--path", cls_path, "--format", "json")
            assert list_result.returncode == 0
            ports = json.loads(list_result.stdout)
            assert port_name not in ports
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_port_delete_nonexistent(self, cli_project: str) -> None:
        """Test deleting a non-existent port returns error."""
        pkg_name = _unique_name("NoDelPkg")
        cls_name = _unique_name("NoDelCls")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            # Delete uses --path + --name
            result = _run_cli(
                "port", "delete",
                "--path", cls_path,
                "--name", f"NonExistent_{uuid.uuid4().hex[:8]}",
            )
            assert result.returncode != 0
            assert "error" in result.stderr.lower() or "failed" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)

    def test_port_create_invalid_json(self, cli_project: str) -> None:
        """Test that invalid JSON input returns error."""
        pkg_name = _unique_name("BadJsonPkg")
        cls_name = _unique_name("BadJsonCls")
        pkg_path, cls_path = self._create_package_and_class(pkg_name, cls_name)

        try:
            result = _run_cli("port", "create", "--path", cls_path, "--input", "{invalid}")
            assert result.returncode != 0
            assert "json" in result.stderr.lower() or "error" in result.stderr.lower()
        finally:
            _run_cli("package", "delete", "--path", pkg_path)
```

- [ ] **Step 2: Run the port tests (requires Rhapsody)**

Run: `pytest tests/system/cli/test_port_cli.py -v --tb=short`
Expected: All tests pass.

- [ ] **Step 3: Commit**

```bash
git add tests/system/cli/test_port_cli.py
git commit -m "test: add port CLI system tests (create, view, list, delete)"
```

---

### Task 9: Verify Full Suite & Quality Gate

**Files:**
- No new files — verification only

- [ ] **Step 1: Run all system tests together**

Run: `pytest tests/system/ -v --tb=short`
Expected: All tests pass (or skip if no Rhapsody).

- [ ] **Step 2: Run parsing tests only (no Rhapsody needed)**

Run: `pytest tests/system/cli/test_cli_parsing.py -v --tb=short`
Expected: All tests pass.

- [ ] **Step 3: Run unit tests to confirm no regressions**

Run: `pytest tests/unit/ -v --tb=short`
Expected: All tests pass, no regressions.

- [ ] **Step 4: Run ruff and black checks**

Run: `ruff check tests/system/ && black --check tests/system/`
Expected: No errors.

- [ ] **Step 5: Run mypy**

Run: `mypy tests/system/`
Expected: No errors (or only win32com-related ignores).

- [ ] **Step 6: Final commit if any fixes were needed**

If any fixes were applied during verification:

```bash
git add tests/system/
git commit -m "test: fix system test issues found during verification"
```

- [ ] **Step 7: Verify test count**

Run: `pytest tests/system/ --co -q 2>&1 | tail -5`
Expected: Shows collection of ~50+ test cases across all files.
