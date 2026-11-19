# CLI Simplification Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reduce the CLI surface to active commands (`connect`, `disconnect`, `status`, `version`, `export`, `import`, `project`, `package`, `class`), suspend `attribute`/`operation`/`port` with an explicit notice, promote package-level `export`/`import` to individual single-level commands, and verify every kept command against live Rhapsody.

**Architecture:** All changes are dispatch-level in `cli/cli.py` (a `SUSPENDED_COMMANDS` set + two new single-level branches reusing `PackageExportAction`/`PackageImportAction`) plus slimming `ProjectCommand`/`PackageCommand.get_actions()`. No action or model implementation changes; suspended implementations and their unit tests stay untouched.

**Tech Stack:** Python 3.8+ stdlib argparse, pytest with `unittest.mock`, ruff/black/mypy, live IBM Rhapsody COM (Windows) for the final smoke task.

**Spec:** `docs/superpowers/specs/2026-11-19-cli-simplification-design.md`

## Global Constraints

- Branch: `docs/cli-simplification` (spec commit already on it). Never commit to `main`.
- Python 3.8 compatible: use `typing.Set`/`Optional`/`List` (no builtin generics in annotations, no PEP 604 unions).
- Forbidden: `from __future__ import annotations`, `Any` in annotations, AI attribution in commits.
- ruff rules E, F, I, UP, B, N; black line-length 200, target py38; mypy strict.
- Quality gate (run before every "done" claim): `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
- Unit tests must never touch real COM — mock the action classes / `_connect_app` as shown.
- `print()` in CLI code only for user-facing output with a `NOTE:` comment (existing convention in `cli.py`).
- Commit style: conventional commits (`feat:`, `test:`, `docs:`, `refactor:`), no `Co-authored-by`.

---

### Task 1: Suspended-command mechanism in `cli.py`

**Files:**
- Modify: `src/rhapsody_cli/cli/cli.py`
- Test: `tests/unit/cli/test_cli.py`

**Interfaces:**
- Produces: module constant `SUSPENDED_COMMANDS: Set[str]` in `rhapsody_cli.cli.cli`; suspended command behavior (stderr notice, `SystemExit(2)`) that Task 4's system tests and Task 7's smoke rely on; `_usage()` renders three sections (Single-Level / Two-Level / Suspended). Task 2 later appends `export`/`import` to the lists.

- [ ] **Step 1: Write the failing tests**

Append to `tests/unit/cli/test_cli.py` (add `import pytest` to the imports at the top; keep the existing imports and two tests unchanged):

```python
class TestSuspendedCommands:
    """Tests for the suspended-command mechanism (attribute/operation/port)."""

    @pytest.mark.parametrize("command", ["attribute", "operation", "port"])
    def test_suspended_command_prints_notice_and_exits_2(self, command: str, capsys: pytest.CaptureFixture[str]) -> None:
        """A suspended command prints a notice to stderr and exits with code 2."""
        with patch("sys.argv", ["rhapsody-cli", command, "list"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
        assert exc_info.value.code == 2
        captured = capsys.readouterr()
        assert f"command '{command}' is temporarily suspended" in captured.err

    def test_suspended_check_fires_before_dispatch(self) -> None:
        """The suspended check must reject the command before any command group is constructed."""
        with patch("sys.argv", ["rhapsody-cli", "attribute", "list"]):
            with patch("rhapsody_cli.cli.cli.AttributeCommand") as mock_command_cls:
                with pytest.raises(SystemExit):
                    main()
        mock_command_cls.assert_not_called()

    def test_unknown_command_still_rejected(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Unknown commands keep the existing 'Unknown command' usage-error path."""
        with patch("sys.argv", ["rhapsody-cli", "definitely_not_real"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
        assert exc_info.value.code == 2
        assert "Unknown command" in capsys.readouterr().stderr


class TestUsageText:
    """Tests for the top-level usage rendering."""

    def test_help_lists_active_and_suspended_sections(self, capsys: pytest.CaptureFixture[str]) -> None:
        """--help renders Single-Level, Two-Level, and Suspended sections."""
        with patch("sys.argv", ["rhapsody-cli", "--help"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
        assert exc_info.value.code == 0
        out = capsys.readouterr().out
        assert "Single-Level Commands:" in out
        assert "Two-Level Commands:" in out
        assert "Suspended Commands" in out
        for active in ("project", "package", "class"):
            assert f"  {active} " in out
        for suspended in ("attribute", "operation", "port"):
            assert f"  {suspended} " in out
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `pytest tests/unit/cli/test_cli.py -v`
Expected: FAIL — `test_suspended_command_prints_notice_and_exits_2` and `test_suspended_check_fires_before_dispatch` fail because `attribute` still dispatches to `AttributeCommand`; `test_help_lists_active_and_suspended_sections` fails because usage has no Suspended section. (`test_unknown_command_still_rejected` may already pass — that is acceptable.)

- [ ] **Step 3: Implement the mechanism in `cli.py`**

Three edits to `src/rhapsody_cli/cli/cli.py`:

Edit 1 — extend the typing import and add the constant after `logger = logging.getLogger(__name__)`:

```python
from typing import Optional, Set
```

```python
logger = logging.getLogger(__name__)

# Command groups that are temporarily suspended: implementations are retained
# (actions/, commands/ and their tests) but dispatch rejects them with an
# explicit notice. Re-enable by removing the name here, from _usage(), and
# re-adding the dispatch/get_actions() wiring.
SUSPENDED_COMMANDS: Set[str] = {"attribute", "operation", "port"}
```

Edit 2 — insert the suspension check in `main()` directly after the `--help` check (before the verbose/logging setup):

```python
    # Check for help
    if command_name in ("-h", "--help"):
        _usage("")

    # Suspended commands: reject with an explicit notice before any dispatch
    if command_name in SUSPENDED_COMMANDS:
        # NOTE: Suspension notice to stderr (mirrors usage-on-error behavior).
        print(f"rhapsody-cli: command '{command_name}' is temporarily suspended.", file=sys.stderr)
        print("Active commands: connect, disconnect, status, version, project, package, class", file=sys.stderr)
        sys.exit(2)
```

Edit 3 — rewrite the command list part of `_usage()` (options block and the rest of the function unchanged):

```python
    commands_text = "Single-Level Commands:\n"
    commands_text += "  connect     Connect to Rhapsody\n"
    commands_text += "  disconnect  Disconnect from Rhapsody\n"
    commands_text += "  status      Show connection status\n"
    commands_text += "  version     Show CLI version\n\n"
    commands_text += "Two-Level Commands:\n"
    commands_text += "  class       Manage classes\n"
    commands_text += "  package     Manage packages\n"
    commands_text += "  project     Manage projects\n\n"
    commands_text += "Suspended Commands (temporarily disabled, implementations retained):\n"
    commands_text += "  attribute   Manage attributes\n"
    commands_text += "  operation   Manage operations\n"
    commands_text += "  port        Manage ports\n"
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `pytest tests/unit/cli/test_cli.py -v`
Expected: all PASS (the 2 pre-existing tests plus the 6 new ones).

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/cli/cli.py tests/unit/cli/test_cli.py
git commit -m "feat: suspend attribute/operation/port commands at dispatch with explicit notice"
```

---

### Task 2: Single-level `export` / `import` commands

**Files:**
- Modify: `src/rhapsody_cli/cli/cli.py`
- Test: `tests/unit/cli/test_cli.py`

**Interfaces:**
- Consumes: `PackageExportAction` / `PackageImportAction` from `rhapsody_cli.actions.package_action` — no-arg constructors; `execute(args: argparse.Namespace)` reads `args.path` (`None` = project root), `args.file`, `args.verbose`. These are the exact argument names `add_path_argument` / `init_arguments` already register inside the two-level flow.
- Produces: `rhapsody-cli export [--path P] --file F` and `rhapsody-cli import [--path P] --file F` single-level commands; the usage text and suspension notice now list `export`/`import` as active.

- [ ] **Step 1: Write the failing tests**

Append to `tests/unit/cli/test_cli.py`:

```python
class TestSingleLevelExchangeCommands:
    """Tests for the single-level export/import commands."""

    def test_export_dispatches_with_file_and_default_root_path(self) -> None:
        with patch("rhapsody_cli.cli.cli.PackageExportAction") as mock_action_cls:
            mock_instance = MagicMock()
            mock_action_cls.return_value = mock_instance
            with patch("sys.argv", ["rhapsody-cli", "export", "--file", "out.yaml"]):
                main()
        mock_instance.execute.assert_called_once()
        args = mock_instance.execute.call_args[0][0]
        assert args.file == "out.yaml"
        assert args.path is None

    def test_export_dispatches_with_explicit_path(self) -> None:
        with patch("rhapsody_cli.cli.cli.PackageExportAction") as mock_action_cls:
            mock_instance = MagicMock()
            mock_action_cls.return_value = mock_instance
            with patch("sys.argv", ["rhapsody-cli", "export", "--path", "Sensors", "--file", "sensors.yaml"]):
                main()
        args = mock_instance.execute.call_args[0][0]
        assert args.path == "Sensors"
        assert args.file == "sensors.yaml"

    def test_import_dispatches_with_file_and_explicit_path(self) -> None:
        with patch("rhapsody_cli.cli.cli.PackageImportAction") as mock_action_cls:
            mock_instance = MagicMock()
            mock_action_cls.return_value = mock_instance
            with patch("sys.argv", ["rhapsody-cli", "import", "--path", "Sensors", "--file", "in.yaml"]):
                main()
        mock_instance.execute.assert_called_once()
        args = mock_instance.execute.call_args[0][0]
        assert args.path == "Sensors"
        assert args.file == "in.yaml"

    def test_export_requires_file_argument(self, capsys: pytest.CaptureFixture[str]) -> None:
        with patch("sys.argv", ["rhapsody-cli", "export"]):
            with pytest.raises(SystemExit) as exc_info:
                main()
        assert exc_info.value.code == 2
        assert "required" in capsys.readouterr().err.lower()
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `pytest tests/unit/cli/test_cli.py::TestSingleLevelExchangeCommands -v`
Expected: FAIL — the first three fall through to the two-level dispatch and end in `Unknown command` (`_usage` → SystemExit with `execute` never called on the mock); `test_export_requires_file_argument` fails because the error is "Unknown command", not a `required` argparse error.

- [ ] **Step 3: Implement in `cli.py`**

Edit 1 — add the import next to the session action import:

```python
from rhapsody_cli.actions.package_action import PackageExportAction, PackageImportAction
```

Edit 2 — add two branches to the single-level chain in `main()`, after the `version` branch and before the `# Two-level commands (existing)` comment:

```python
        elif command_name == "export":
            action = PackageExportAction()
            parser = argparse.ArgumentParser(prog="rhapsody-cli export")
            parser.add_argument("--path", default=None, help="Path to package (defaults to root)")
            parser.add_argument("--file", required=True, help="Output YAML file path")
            parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
            parsed_args = parser.parse_args(command_args)
            action.execute(parsed_args)
            return

        elif command_name == "import":
            action = PackageImportAction()
            parser = argparse.ArgumentParser(prog="rhapsody-cli import")
            parser.add_argument("--path", default=None, help="Path to target package (defaults to root)")
            parser.add_argument("--file", required=True, help="Input YAML file path")
            parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
            parsed_args = parser.parse_args(command_args)
            action.execute(parsed_args)
            return
```

Edit 3 — update the two places that enumerate active commands to include `export`/`import`:

In `main()`'s suspension notice:

```python
        print("Active commands: connect, disconnect, status, version, export, import, project, package, class", file=sys.stderr)
```

In `_usage()`, single-level section becomes:

```python
    commands_text = "Single-Level Commands:\n"
    commands_text += "  connect     Connect to Rhapsody\n"
    commands_text += "  disconnect  Disconnect from Rhapsody\n"
    commands_text += "  status      Show connection status\n"
    commands_text += "  version     Show CLI version\n"
    commands_text += "  export      Export a package to a YAML file\n"
    commands_text += "  import      Import a YAML file into a package\n\n"
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `pytest tests/unit/cli/test_cli.py -v`
Expected: all PASS (previous tests still green — the Task 1 tests assert only the "temporarily suspended" phrase and section headers, which are unchanged).

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/cli/cli.py tests/unit/cli/test_cli.py
git commit -m "feat: add single-level export/import commands reusing package exchange actions"
```

---

### Task 3: Remove export/import subcommands from project/package groups

**Files:**
- Modify: `src/rhapsody_cli/commands/project_command.py`
- Modify: `src/rhapsody_cli/commands/package_command.py`
- Test: `tests/unit/commands/test_project_command.py`
- Test: `tests/unit/commands/test_package_command.py`

**Interfaces:**
- Consumes: nothing new.
- Produces: `ProjectCommand.get_actions()` returns exactly `[ProjectOpenAction, ProjectListAction, ProjectCloseAction, ProjectNewAction]`; `PackageCommand.get_actions()` returns exactly `[create, delete, view, list, update]`. `ProjectExportAction`/`ProjectImportAction` remain defined in `project_action.py` (unwired, per spec) — do **not** delete them or their tests in `tests/unit/actions/test_project_action.py`.

- [ ] **Step 1: Update the failing tests first**

In `tests/unit/commands/test_package_command.py`:
- Replace `test_registers_all_seven_subcommands` with:

```python
    def test_registers_all_five_subcommands(self) -> None:
        """UTS_PKG_00025: Test that all 5 subcommands are registered (export/import moved to top level)."""
        cmd = PackageCommand(["create", "--path", "Sensors", '{"name":"Test"}'])
        actions = cmd.get_actions()
        command_ids = [a.command_id for a in actions]

        assert "create" in command_ids
        assert "delete" in command_ids
        assert "view" in command_ids
        assert "list" in command_ids
        assert "update" in command_ids
        assert "export" not in command_ids
        assert "import" not in command_ids
        assert len(actions) == 5
```

- Delete the entire `TestPackageCommandExportImportRegistration` class (lines 41-61).

In `tests/unit/commands/test_project_command.py`:
- Delete the entire `TestProjectCommandExportImportRegistration` class (lines 127-151) and replace it with:

```python
class TestProjectCommandRegistration:
    """Tests that ProjectCommand registers exactly the four active subcommands."""

    def test_get_actions_returns_four_actions(self) -> None:
        """ProjectCommand.get_actions() must return exactly 4 actions (export/import moved to top level)."""
        cmd = ProjectCommand(["open", "MyProject.rpy"])
        actions = cmd.get_actions()
        command_ids = [a.command_id for a in actions]

        assert command_ids == ["open", "list", "close", "new"]
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `pytest tests/unit/commands/test_package_command.py tests/unit/commands/test_project_command.py -v`
Expected: FAIL — the groups still register export/import, so `len(actions) == 5` / `== 4` and the `"export" not in command_ids` assertions fail.

- [ ] **Step 3: Slim the command groups**

`src/rhapsody_cli/commands/project_command.py` — remove `ProjectExportAction` and `ProjectImportAction` from the import block so it reads:

```python
from rhapsody_cli.actions.project_action import (
    ProjectCloseAction,
    ProjectListAction,
    ProjectNewAction,
    ProjectOpenAction,
)
```

and `get_actions()` becomes:

```python
    def get_actions(self) -> List[AbstractAction]:
        """Return the project subcommand actions."""
        return [
            ProjectOpenAction(),
            ProjectListAction(),
            ProjectCloseAction(),
            ProjectNewAction(),
        ]
```

Also update the class and `__init__` docstrings that say "open, list, close, new, export, import" to "open, list, close, new".

`src/rhapsody_cli/commands/package_command.py` — remove `PackageExportAction` and `PackageImportAction` from the import block and from `get_actions()` (keep `PackageCreateAction`, `PackageDeleteAction`, `PackageViewAction`, `PackageListAction`, `PackageUpdateAction`). Update the docstrings that say "create, delete, view, list, update, export, import" to "create, delete, view, list, update".

- [ ] **Step 4: Run the tests to verify they pass**

Run: `pytest tests/unit/commands/test_package_command.py tests/unit/commands/test_project_command.py tests/unit/actions/test_project_action.py tests/unit/actions/test_package_action.py -v`
Expected: all PASS — including the action-level tests for `ProjectExportAction`/`ProjectImportAction`, which still exist unwired.

- [ ] **Step 5: Run the full unit suite to catch cross-references**

Run: `pytest tests/unit -q`
Expected: PASS. If any other module asserts on project/package export/import subcommands, update it the same way (search with `rg -l "project.*export|package.*export" tests/unit`).

- [ ] **Step 6: Commit**

```bash
git add src/rhapsody_cli/commands/project_command.py src/rhapsody_cli/commands/package_command.py tests/unit/commands/test_project_command.py tests/unit/commands/test_package_command.py
git commit -m "refactor: remove export/import subcommands from project and package groups"
```

---

### Task 4: Update system parsing tests for suspension

**Files:**
- Test: `tests/system/cli/test_cli_parsing.py`

**Interfaces:**
- Consumes: the suspension behavior implemented in Task 1 (stderr notice contains "temporarily suspended", exit code 2), exercised via the existing `_run_cli` subprocess helper (runs `[sys.executable, "-m", "rhapsody_cli.cli.main", *args]`).

- [ ] **Step 1: Replace the three obsolete tests**

In `tests/system/cli/test_cli_parsing.py`, delete `test_attribute_create_missing_path`, `test_operation_create_missing_path`, and `test_port_create_missing_path` and replace them with:

```python
    @pytest.mark.parametrize("command", ["attribute", "operation", "port"])
    def test_suspended_command_shows_notice(self, command: str) -> None:
        """Test that suspended command groups print a suspension notice and exit 2."""
        result = _run_cli(command, "create")
        assert result.returncode == 2
        assert "temporarily suspended" in result.stderr

    def test_usage_lists_suspended_section(self) -> None:
        """Test that --help shows active and suspended command sections."""
        result = _run_cli("--help")
        assert result.returncode == 0
        assert "Suspended Commands" in result.stdout
        assert "attribute" in result.stdout
```

- [ ] **Step 2: Verify collection offline (system tests need Windows + Rhapsody to actually run)**

Run: `pytest tests/system/cli/test_cli_parsing.py --collect-only -q`
Expected: collection succeeds with no import/syntax errors (execution is CI/live-only per AGENTS.md).

- [ ] **Step 3: Commit**

```bash
git add tests/system/cli/test_cli_parsing.py
git commit -m "test: expect suspension notice for attribute/operation/port in system parsing tests"
```

---

### Task 5: Documentation updates

**Files:**
- Modify: `README.md`
- Modify: `docs/user_guide/cli_tools.rst`
- Modify: `CLAUDE.md`
- Modify: `AGENTS.md`

**Interfaces:**
- Consumes: the final command surface (Tasks 1-3).
- Produces: docs matching reality. No code interfaces.

- [ ] **Step 1: Update `README.md`**

Five targeted edits:

- Feature bullet (line 18) — replace:

```markdown
- **CLI Tools**: Single-level commands for session management (connect, disconnect, status, version) and two-level commands for project, package, class, operation, attribute, and port management
```

with:

```markdown
- **CLI Tools**: Single-level commands for session management (`connect`, `disconnect`, `status`, `version`) and model exchange (`export`, `import`), plus two-level commands for `project`, `package`, and `class` management
```

- Command list (lines 89-91) — replace:

```markdown
**Single-Level Commands**: `connect`, `disconnect`, `status`, `version`

**Two-Level Commands**: `project`, `package`, `class`, `attribute`, `operation`, `port`
```

with:

```markdown
**Single-Level Commands**: `connect`, `disconnect`, `status`, `version`, `export`, `import`

**Two-Level Commands**: `project`, `package`, `class`
```

- Replace the whole `#### Attribute, Operation, and Port Management` section (from that heading through the `rhapsody-cli attribute delete ...` example, just before `### Command Options`) with:

````markdown
#### Model Import/Export

`export` and `import` are single-level commands operating at package
granularity (`--path` optional, defaults to the project root, so exporting
the root covers the whole model):

```bash
rhapsody-cli export --file model.yaml
rhapsody-cli export --path Sensors --file sensors.yaml
rhapsody-cli import --file model.yaml
rhapsody-cli import --path Sensors --file model.yaml
```

#### Suspended Commands

`attribute`, `operation`, and `port` are temporarily suspended: running them
prints a notice and exits with code 2. Their implementations remain in the
codebase (`src/rhapsody_cli/actions/`), and they can be re-enabled by
removing them from `SUSPENDED_COMMANDS` in `src/rhapsody_cli/cli/cli.py`.
````

- Changelog — insert above `### v0.2.1 (2026-07-26)`:

```markdown
### Unreleased

- **Breaking**: Suspended the `attribute`, `operation`, and `port` command groups — running them now prints a suspension notice and exits with code 2 (implementations retained; re-enable via `SUSPENDED_COMMANDS` in `src/rhapsody_cli/cli/cli.py`)
- **Breaking**: Removed the `project export`/`project import` subcommands (project-level exchange is superseded by package-level commands; `ProjectExportAction`/`ProjectImportAction` remain in the codebase unwired)
- Added single-level `export` and `import` commands for YAML-based model exchange at package granularity (`--path` optional, defaults to project root), reusing `PackageExportAction`/`PackageImportAction`
- Removed `export`/`import` subcommands from the `package` group (now top-level commands)
```

- Verify no other stale references: `rg -n "attribute|operation|port" README.md` — the remaining mentions should only be inside the new Suspended section and the changelog history. Fix any stragglers in the CLI usage sections (do not touch the Python API sections or the supported-elements list, where "attribute/operation" refer to model concepts, not CLI commands).

- [ ] **Step 2: Update `docs/user_guide/cli_tools.rst`**

- Command Structure (lines 13-16) — replace the two bullet lines with:

```rst
* **Single-Level Commands**: Direct actions (connect, disconnect, status, version, export, import)
* **Two-Level Commands**: Action groups with subcommands (project, package, class)

Command groups ``attribute``, ``operation``, and ``port`` are temporarily
suspended: running them prints a notice and exits with code 2 (their
implementations remain in the codebase).
```

- The `Element Commands` section (from the `Element Commands` heading at line 222 through the end of the ``element delete`` examples, i.e. everything before the `Package Commands` heading at line 345) documents commands removed in v0.2.0. Replace the entire section with a `Class Commands` section:

```rst
Class Commands
--------------

Classes are managed through the ``class`` command group with the
subcommands ``create``, ``view``, ``list``, ``link``, ``update``, and
``delete``. All subcommands except ``create`` require ``--path`` (or
``--guid``) to identify the class.

``class create`` - Create a Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli class create --path PARENT_PATH ATTRIBUTES

Create one or more classes under the package/classifier at
``PARENT_PATH``. ``ATTRIBUTES``/``--input`` accepts inline JSON or a
JSON file; ``name`` is required.

**Example:**

.. code-block:: bash

   rhapsody-cli class create --path pkg '{"name": "TemperatureSensor"}'

``class view`` / ``class list``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli class view --path pkg/TemperatureSensor [--format table|json|csv]
   rhapsody-cli class list --path pkg [--format table|json|csv]

``class link`` - Link a Generalization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli class link --path pkg/Child --add BaseName

``class update`` / ``class delete``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   rhapsody-cli class update --path pkg/TemperatureSensor '{"isAbstract": true}'
   rhapsody-cli class delete --path pkg/TemperatureSensor
```

- Add a `Model Import/Export` section and a `Suspended Commands` section immediately after the `Package Commands` section (before `Common Use Cases`):

```rst
Model Import/Export
-------------------

``export`` and ``import`` are single-level commands for YAML-based model
exchange, operating at package granularity. ``--path`` is optional and
defaults to the project root, so exporting the root covers the whole
model.

.. code-block:: bash

   # Export the whole model (root package) to YAML
   rhapsody-cli export --file model.yaml

   # Export one package
   rhapsody-cli export --path pkg/Sensors --file sensors.yaml

   # Import a YAML file into the root package
   rhapsody-cli import --file model.yaml

   # Import a YAML file into a package
   rhapsody-cli import --path pkg/Sensors --file model.yaml

Suspended Commands
------------------

The ``attribute``, ``operation``, and ``port`` command groups are
temporarily suspended. Running them prints a notice on stderr and exits
with code 2. Their implementations remain in
``src/rhapsody_cli/actions/`` and can be re-enabled by removing them
from ``SUSPENDED_COMMANDS`` in ``src/rhapsody_cli/cli/cli.py``.
```

- Fix stale `element` references outside the removed section — run `rg -n "element " docs/user_guide/cli_tools.rst` and update the remaining occurrences in `Common Use Cases`, `Script Integration`, `Advanced Tips`, and `Environment Variables` to use current commands. Exact replacements:

- In `Create a New Project with Model`:

```rst
   # Add a class inside the new package
   rhapsody-cli class create --path ExistingPackage/MyPackage '{"name": "MyClass"}'

   # View what we created
   rhapsody-cli class view --path ExistingPackage/MyPackage/MyClass
```

- In `Query and Export`:

```rst
   # Export the whole model to YAML
   rhapsody-cli export --file elements.yaml
```

(and delete the `rhapsody-cli --output json element query --recursive > elements.json` line)

- In `Script Integration` (both bash and Python examples): replace `["rhapsody-cli", "--output", "json", "element", "query"]` with `["rhapsody-cli", "export", "--file", "model.yaml"]` and adjust the surrounding prose/comments to describe exporting instead of querying.
- In `Using Redirection` / `Piping Output` / `Environment Variables`: replace `element query` examples with `rhapsody-cli export --file model.yaml` or `rhapsody-cli project list` (keep the same redirection/piping/env-var point being illustrated). Note: `--format` is the real output-format flag in this CLI; the `--output json` / `RHAPSODY_OUTPUT` examples are stale — replace `set RHAPSODY_OUTPUT=json` with:

```rst
Pass ``--format`` after the command group:

.. code-block:: bash

   rhapsody-cli class list --path pkg --format json
```

- [ ] **Step 3: Update `CLAUDE.md`**

- Replace the `### Running the CLI` block (lines 97-106):

````markdown
### Running the CLI

```bash
rhapsody-cli connect
rhapsody-cli project open path/to/project.rpy
rhapsody-cli project list
rhapsody-cli class list --path SomePackage
```

**Active single-level commands:** `connect` | `disconnect` | `status` | `version` | `export` | `import`
**Active two-level command groups:** `project` | `package` | `class`
**Suspended (dispatch rejects with a notice, implementations retained):** `attribute` | `operation` | `port` — see `SUSPENDED_COMMANDS` in `src/rhapsody_cli/cli/cli.py`.
````

- Dispatch flow item 1 (line ~149) — replace:

```markdown
1. `main()` reads `sys.argv[1]` as the command group name (`element` | `io` | `project`)
```

with:

```markdown
1. `main()` reads `sys.argv[1]` as the command name, rejects names in `SUSPENDED_COMMANDS` (`attribute` | `operation` | `port`) with a notice and exit code 2, then routes single-level commands (`connect` | `disconnect` | `status` | `version` | `export` | `import`) directly to their actions and two-level groups (`project` | `package` | `class`) to `AbstractCommand` subclasses
```

- Actions example (line ~160) — replace `e.g. \`ElementAddAction\` → \`element add\`` with `e.g. \`ClassCreateAction\` → \`class create\``.

- [ ] **Step 4: Update `AGENTS.md`**

Line 13 table cell — replace the trailing sentence:

```markdown
**Actual command groups:** `class`, `attribute`, `operation`, `package`, `port`, `project` (not `element`/`io` — older docs are stale).
```

with:

```markdown
**Actual command groups:** active `project`, `package`, `class` plus single-level `connect`, `disconnect`, `status`, `version`, `export`, `import`. `attribute`, `operation`, `port` are suspended at dispatch (`SUSPENDED_COMMANDS` in `cli/cli.py`) — implementations retained. (`element`/`io` no longer exist.)
```

- [ ] **Step 5: Verify docs consistency**

Run: `rg -n "element add|element query|element view|element delete|io\b" README.md CLAUDE.md docs/user_guide/cli_tools.rst AGENTS.md`
Expected: no stale CLI-command references remain (model-concept words like "attribute keys" are fine). Build check if Sphinx is installed: `sphinx-build -b html docs docs/_build/html -q` — must not fail on cli_tools.rst.

- [ ] **Step 6: Commit**

```bash
git add README.md docs/user_guide/cli_tools.rst CLAUDE.md AGENTS.md
git commit -m "docs: document active vs suspended CLI commands and single-level export/import"
```

---

### Task 6: Full quality gate

**Files:**
- Possibly any file flagged by the gate.

- [ ] **Step 1: Run the gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit -q`
Expected: all green. Typical fallout to fix if flagged: unused imports left in `project_command.py`/`package_command.py` (ruff F401) — remove the unused `AbstractAction`/action imports only if truly unused; line-length or formatting drift — run `black src/ tests/` and re-check.

- [ ] **Step 2: Fix anything flagged, re-run until green, commit**

```bash
git add -A
git commit -m "chore: pass quality gate after CLI simplification"
```

(If nothing was flagged, skip this commit.)

---

### Task 7: Live smoke verification (Windows + real Rhapsody)

**Files:**
- Modify: this plan file (record results in the checklist at the end).
- Possibly fix files if bugs are found.

**Interfaces:**
- Consumes: the complete CLI surface from Tasks 1-3; a running, licensed Rhapsody instance on this machine.
- Produces: evidence that every kept command works end-to-end; bug fixes (TDD) if anything fails.

- [ ] **Step 1: Prepare a scratch workspace**

```bash
mkdir -p build/smoke
rhapsody-cli status || true   # expect "not connected" or a stale-session notice
```

Never open real user models in this task; everything happens under `build/smoke/`.

- [ ] **Step 2: Session commands**

```bash
rhapsody-cli version
rhapsody-cli status
rhapsody-cli connect --no-gui
rhapsody-cli status
```

Expected: `version` prints the CLI version; first `status` shows disconnected; `connect` launches/attaches Rhapsody and creates a session; second `status` shows connected. If `connect` fails, debug per `tests/system/cli/conftest.py` (session-scoped fixture uses the Python API `RhapsodyApplication.connect()` the same way).

- [ ] **Step 3: Project commands**

```bash
rhapsody-cli project new build/smoke SmokeProj
rhapsody-cli project list
rhapsody-cli project open build/smoke/SmokeProj.rpy   # skip if `new` already opened it
rhapsody-cli project close
rhapsody-cli project open build/smoke/SmokeProj.rpy
```

Expected: `new` creates `build/smoke/SmokeProj.rpy` (and typically opens it); `list` shows SmokeProj; `close`/`open` cycle cleanly.

- [ ] **Step 4: Package commands**

```bash
rhapsody-cli package create '{"name": "Sensors"}'
rhapsody-cli package create --path Sensors '{"name": "Actuators"}'
rhapsody-cli package view --path Sensors --format json
rhapsody-cli package list --path Sensors
rhapsody-cli package update --path Sensors/Actuators '{"description": "Updated"}'
rhapsody-cli package delete --path Sensors/Actuators
```

Expected: each succeeds; `view --format json` returns JSON with name/GUID; `delete` removes Actuators.

- [ ] **Step 5: Class commands**

```bash
rhapsody-cli class create --path Sensors '{"name": "BaseSensor"}'
rhapsody-cli class create --path Sensors '{"name": "TemperatureSensor"}'
rhapsody-cli class view --path Sensors/TemperatureSensor --format json
rhapsody-cli class list --path Sensors
rhapsody-cli class link --path Sensors/TemperatureSensor --add BaseSensor
rhapsody-cli class update --path Sensors/TemperatureSensor '{"isAbstract": false}'
rhapsody-cli class delete --path Sensors/TemperatureSensor
```

Expected: each succeeds; `link` creates a generalization from TemperatureSensor to BaseSensor.

- [ ] **Step 6: Export / import roundtrip**

```bash
rhapsody-cli export --file build/smoke/root.yaml
rhapsody-cli package create '{"name": "Reimported"}'
rhapsody-cli export --path Sensors --file build/smoke/sensors.yaml
rhapsody-cli import --path Reimported --file build/smoke/sensors.yaml
rhapsody-cli package list --path Reimported
```

Expected: both exports write non-empty YAML; the import recreates the Sensors content under `Reimported`; `package list --path Reimported` shows the imported package(s).

- [ ] **Step 7: Suspension + teardown**

```bash
rhapsody-cli attribute list; echo "exit=$?"
rhapsody-cli operation list; echo "exit=$?"
rhapsody-cli port list; echo "exit=$?"
rhapsody-cli project close
rhapsody-cli disconnect
rhapsody-cli status
```

Expected: each suspended command prints the notice on stderr and exits 2; disconnect clears the session; final `status` shows disconnected.

- [ ] **Step 8: Bug-fix loop for any failure**

For every step that failed: (1) write a failing unit test reproducing the bug following the Task 1/2 test patterns, (2) fix the action/command code, (3) re-run `pytest tests/unit -q` green, (4) re-run that smoke step. Commit each fix:

```bash
git add -A && git commit -m "fix: <what the smoke test exposed>"
```

- [ ] **Step 9: Record results**

Append to this plan file below the checklist:

| # | Command | Expected | Actual | Result |
| --- | ------- | -------- | ------ | ------ |
| 1 | `version` | prints version | | PASS/FAIL |
| 2 | `status` (disconnected) | disconnected notice | | PASS/FAIL |
| 3 | `connect --no-gui` | session created | | PASS/FAIL |
| 4 | `status` (connected) | connected | | PASS/FAIL |
| 5 | `project new` | SmokeProj.rpy created | | PASS/FAIL |
| 6 | `project list` | lists SmokeProj | | PASS/FAIL |
| 7 | `project open` | opens | | PASS/FAIL |
| 8 | `project close` | closes | | PASS/FAIL |
| 9 | `package create` (root/nested) | created | | PASS/FAIL |
| 10 | `package view --format json` | JSON out | | PASS/FAIL |
| 11 | `package list` | lists | | PASS/FAIL |
| 12 | `package update` | updated | | PASS/FAIL |
| 13 | `package delete` | deleted | | PASS/FAIL |
| 14 | `class create` ×2 | created | | PASS/FAIL |
| 15 | `class view --format json` | JSON out | | PASS/FAIL |
| 16 | `class list` | lists | | PASS/FAIL |
| 17 | `class link` | generalization added | | PASS/FAIL |
| 18 | `class update` | updated | | PASS/FAIL |
| 19 | `class delete` | deleted | | PASS/FAIL |
| 20 | `export` root | YAML written | | PASS/FAIL |
| 21 | `export --path Sensors` | YAML written | | PASS/FAIL |
| 22 | `import --path Reimported` | content recreated | | PASS/FAIL |
| 23 | `attribute list` | suspension notice, exit 2 | | PASS/FAIL |
| 24 | `operation list` | suspension notice, exit 2 | | PASS/FAIL |
| 25 | `port list` | suspension notice, exit 2 | | PASS/FAIL |
| 26 | `disconnect` + `status` | session cleared | | PASS/FAIL |

- [ ] **Step 10: Final gate + commit**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit -q`
Expected: green. Then commit the recorded results:

```bash
git add docs/superpowers/plans/2026-11-19-cli-simplification.md
git commit -m "test: record live CLI smoke results for simplified command surface"
```

---

## Self-Review Notes

- Spec coverage: suspension mechanics (Task 1), export/import promotion (Task 2), group slimming + retained unwired `ProjectExport/ImportAction` (Task 3), system tests (Task 4), docs incl. CLAUDE.md/AGENTS.md stale sections (Task 5), gate (Task 6), live smoke of every kept subcommand incl. export/import roundtrip (Task 7). Re-enablement path documented in `cli.py` comment + docs.
- Spec deviation (improvement): the spec's smoke fixture said "scratch copy of `demos/test_project/TestProject.rpy`", but no ready-made `.rpy` exists in the repo (only the `TestProject_rpy/` split-unit directory). Task 7 instead creates the scratch project with the CLI's own `project new` — which is itself one of the commands under test.
- Type consistency: `SUSPENDED_COMMANDS: Set[str]` (typing.Set, py38-safe); mock assertions target `execute.call_args[0][0]` Namespace attributes `path`/`file`/`verbose`, matching the inline parser definitions and `Package{Export,Import}Action`'s existing argument names.

---

## Execution Results (2026-11-19)

All tasks completed on branch `docs/cli-simplification`. Live smoke run against
Rhapsody 10.0.3 (`Rhapsody2.Application.1`) with scratch project under
`build/smoke/` (created via `project new`, cleaned up afterward).

| # | Command | Result | Notes |
| --- | ------- | ------ | ----- |
| 1 | `version` | PASS | prints CLI version |
| 2 | `status` (disconnected) | PASS | "Session timed out" notice, exit 0 |
| 3 | `connect --no-gui` | PASS | launched Rhapsody, session file created |
| 4 | `status` (connected) | PASS (after fix 1) | shows connection info + `Rhapsody version: 10.0.3` |
| 5 | `project new` (absolute) | PASS | SmokeProj.rpyx created + opened |
| 5b | `project new` (relative) | PASS (after fix 2) | initially failed with raw COM E_FAIL |
| 6 | `project list` | PASS | renders table |
| 7 | `project open` | PASS (after fix 3) | missing file now rejected with clear error, exit 1 |
| 8 | `project close` | PASS | |
| 9 | `package create` (root/nested) | PASS | |
| 10 | `package view --format json` | PASS | name/GUID/description/metaClass/fullPath |
| 11 | `package list` | PASS | |
| 12 | `package update` | PASS | |
| 13 | `package delete` | PASS | |
| 14 | `class create` x2 | PASS | |
| 15 | `class view --format json` | PASS | full class dict incl. flags |
| 16 | `class list` | PASS | |
| 17 | `class link` | PASS (after fix 4) | generalization verified in-model via probe |
| 18 | `class update` (description) | PASS (after fix 5 note) | description persists; `isAbstract` is a known Rhapsody COM limitation (writes never persist) — reported loudly |
| 19 | `class delete` | PASS | |
| 20 | `export` (root, no --path) | PASS (after fix 6) | 611 B YAML of active project |
| 21 | `export --path Sensors` | PASS | 265 B YAML |
| 22 | `import --path Reimported` | PASS (after fix 7) | classes + generalization verified in-model via probe |
| 23 | `attribute list` | PASS | suspension notice, exit 2 |
| 24 | `operation list` | PASS | suspension notice, exit 2 |
| 25 | `port list` | PASS | suspension notice, exit 2 |
| 26 | `disconnect` + `status` | PASS | session cleared, "Not connected" |

Bugs found by smoke and fixed via TDD (failing unit test first, all in this branch):

1. `status`/`version` crashed (`getVersion` missing on property-style Prog ID) — `get_version` now falls back to the bare `version` member (callable or plain).
2. `project new` with a relative path failed with raw COM E_FAIL — location resolved to absolute.
3. `project open` on a missing file exited 0 silently — now exits 1 with "Project file not found".
4. `class link` / `class create --superclasses` called a nonexistent model method — now resolve via `findNestedElementRecursive(name, "Class")`.
5. Scalar JSON items in class/package bulk-create crashed with AttributeError — recorded as per-item errors.
6. `export`/`import` with `--path` omitted failed ("Path 'None' does not resolve") — default to the active project root.
7. `import` generalization wiring used non-functional `addNewAggr`/`setDerivedClass`/`setBaseClass` COM calls — now wires via `IRPClassifier::addGeneralization` and tolerates Prog IDs that return no handle.

Known limitation (Rhapsody COM, not fixable in this codebase): `isAbstract`
writes are accepted but never persisted by `Rhapsody2.Application.1`;
`RPClass.set_is_abstract` refuses loudly. Documented in README + user guide.
