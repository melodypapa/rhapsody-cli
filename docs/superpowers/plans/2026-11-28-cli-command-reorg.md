# CLI Command Reorganization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task (Ray's standing preference is direct in-session execution, not subagent fan-out). Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Execute the approved CLI reorganization spec (`docs/superpowers/specs/2026-11-27-cli-command-reorg-design.md`): registry-driven root-parser dispatch, strict-global `--format`/`-v`, one action class per file, shared-helper consolidation, and `export`/`import` promoted to root commands.

**Architecture:** Keep argparse and the PanGu `AbstractCommand` → `AbstractAction` flow. Replace `main()`'s if/elif chains with one root parser built from a `COMMANDS` registry; every entry implements `register(subparsers)` / `run(namespace)`. ~33 action classes move from 5 mega-files into `actions/<domain>/<action>.py` modules with `__init__` re-exports. Pure helpers consolidate into `actions/support.py`; output rendering unifies on the existing base-class helper.

**Tech Stack:** Python 3.8+ stdlib argparse, pytest + unittest.mock (no real COM in tests), ruff/black/mypy gate (see AGENTS.md Quality Gate).

**Execution environment:** Work in a fresh git worktree on a branch cut from `origin/main` (e.g. `refactor/cli-command-reorg`) — Ray's parallel sync automation commits to the shared checkout; the spec and this plan were both written in isolated worktrees for that reason. Commit with explicit paths, never `git add -A`.

**Ground truth for reviewers:** current code at the time of planning: `cli/cli.py` 158 lines (if/elif + `_usage()`), `commands/abstract_command.py` 92 lines, 6 group classes (~36-40 lines each), `actions/abstract_action.py` 274 lines, `session_action.py` 244, `package_action.py` 672 (8 classes), `class_action.py` 739 (7), `operation_action.py` 639 (6), `attribute_action.py` 603 (6), `port_action.py` 573 (6), `project_action.py` 185 (6). Tests: `tests/unit/cli/test_cli.py` (patches `rhapsody_cli.cli.cli.PackageCommand`, asserts `execute(output_format=...)`), `tests/unit/cli/test_core.py` (formatters), `tests/unit/actions/test_*.py` (one per action module, mock-based).

**NOTE on `project export` / `project import`:** these already exist as *project-level* YAML export of the active project (`ProjectExportAction`/`ProjectImportAction`, SWR_XCH_001) and are NOT touched by this plan. Root `export`/`import` come from the *package*-level pair (`--path` defaults to project root).

---

## File Structure (target state)

```
src/rhapsody_cli/
  cli/
    cli.py                    # registry + build_root_parser() + main() (~90 lines)
    formatters.py             # unchanged
    logging_config.py         # unchanged
    path_resolver.py          # unchanged
    main.py                   # unchanged
  commands/
    abstract_command.py       # register()/run() reshape
    attribute_command.py  class_command.py  operation_command.py
    package_command.py    port_command.py     project_command.py
  actions/
    __init__.py
    abstract_action.py        # hierarchy unchanged + RootCommandAction added + csv in _print_formatted_output
    support.py                # NEW pure helpers
    session/                  # connect.py disconnect.py status.py version.py
    transfer/                 # export.py importer.py (root export/import)
    package/                  # base.py create.py delete.py view.py list.py update.py
    class/                    # base.py create.py delete.py list.py view.py link.py update.py
    attribute/                # base.py create.py delete.py list.py view.py update.py
    operation/                # base.py create.py delete.py list.py view.py update.py
    port/                     # base.py create.py delete.py list.py view.py update.py
    project/                  # open.py list.py close.py new.py export.py importer.py
tests/
  unit/cli/
    test_dispatch_characterization.py   # NEW (Task 1)
    test_cli.py                          # rewritten for new contract (Task 8)
  unit/actions/
    test_support.py                      # NEW (Task 10)
    test_transfer.py                     # NEW (Task 7, moved from test_package_action.py)
    (existing per-domain files updated for import paths only)
```

---

## Stage 1 — Characterization tests (no source changes)

### Task 1: Top-level dispatch characterization

**Files:**
- Create: `tests/unit/cli/test_dispatch_characterization.py`

- [x] **Step 1: Write the characterization tests**

```python
"""Characterization tests for the CURRENT top-level CLI dispatch.

These pin today's behavior before the registry refactor. Tests marked with
INTENDED-CHANGE comments are expected to be updated in stage 2 (flag
consolidation + argparse-generated help), everything else must keep passing.
"""

from typing import List, Tuple
from unittest.mock import MagicMock, patch

import pytest

from rhapsody_cli.cli.cli import main
from rhapsody_cli.exceptions import CliExecutionError


ROUTE_CASES: List[Tuple[List[str], str]] = [
    (["connect"], "ConnectAction"),
    (["disconnect"], "DisconnectAction"),
    (["status"], "StatusAction"),
    (["version"], "VersionAction"),
    (["class", "list"], "ClassCommand"),
    (["attribute", "list"], "AttributeCommand"),
    (["package", "list"], "PackageCommand"),
    (["operation", "list"], "OperationCommand"),
    (["port", "list"], "PortCommand"),
    (["project", "list"], "ProjectCommand"),
]

SINGLE_LEVEL = {"ConnectAction", "DisconnectAction", "StatusAction", "VersionAction"}


def _run_main(argv: List[str]) -> dict:
    """Run main() with argv patched, mock-patching every dispatch target.

    Returns the dict of mock objects keyed by target name so tests can assert
    on exactly one being used.
    """
    targets = {name: name for _, name in ROUTE_CASES}
    mocks = {}
    with patch("sys.argv", ["rhapsody-cli"] + argv):
        with patch("rhapsody_cli.cli.cli.ConnectAction") as c, patch(
            "rhapsody_cli.cli.cli.DisconnectAction"
        ) as d, patch("rhapsody_cli.cli.cli.StatusAction") as s, patch(
            "rhapsody_cli.cli.cli.VersionAction"
        ) as v, patch("rhapsody_cli.cli.cli.ClassCommand") as c1, patch(
            "rhapsody_cli.cli.cli.AttributeCommand"
        ) as c2, patch("rhapsody_cli.cli.cli.PackageCommand") as c3, patch(
            "rhapsody_cli.cli.cli.OperationCommand"
        ) as c4, patch("rhapsody_cli.cli.cli.PortCommand") as c5, patch(
            "rhapsody_cli.cli.cli.ProjectCommand"
        ) as c6:
            mocks = {
                "ConnectAction": c, "DisconnectAction": d, "StatusAction": s,
                "VersionAction": v, "ClassCommand": c1, "AttributeCommand": c2,
                "PackageCommand": c3, "OperationCommand": c4, "PortCommand": c5,
                "ProjectCommand": c6,
            }
            del targets
            main()
    return mocks


@pytest.mark.parametrize("argv,target", ROUTE_CASES)
def test_command_routes_to_expected_target(argv: List[str], target: str) -> None:
    mocks = _run_main(argv)
    mock = mocks[target]
    if target in SINGLE_LEVEL:
        mock.return_value.execute.assert_called_once()
    else:
        # Groups receive the output format and dispatch internally.
        mock.return_value.execute.assert_called_once_with(output_format="table")


def test_global_format_flag_before_group_is_passed_to_group() -> None:
    """--format before the group name is string-scanned by main() today."""
    mocks = _run_main(["--format", "json", "package", "list"])
    mocks["PackageCommand"].return_value.execute.assert_called_once_with(output_format="json")


def test_format_flag_after_group_also_works_today() -> None:
    # INTENDED-CHANGE: after stage 2 this errors with argparse exit 2.
    mocks = _run_main(["package", "list", "--format", "json"])
    mocks["PackageCommand"].return_value.execute.assert_called_once_with(output_format="json")


def test_no_arguments_prints_usage_and_exits_2(capsys: pytest.CaptureFixture) -> None:
    with patch("sys.argv", ["rhapsody-cli"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 2
    out = capsys.readouterr().out
    assert "Usage" in out


def test_unknown_command_prints_error_and_exits_2(capsys: pytest.CaptureFixture) -> None:
    with patch("sys.argv", ["rhapsody-cli", "bogus"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 2
    err = capsys.readouterr().err
    assert "Unknown command: bogus" in err


def test_cli_execution_error_exits_with_its_code() -> None:
    with patch("sys.argv", ["rhapsody-cli", "package", "list"]):
        with patch("rhapsody_cli.cli.cli.PackageCommand") as mock_cls:
            mock_cls.return_value.execute.side_effect = CliExecutionError("boom", exit_code=3)
            with pytest.raises(SystemExit) as exc_info:
                main()
    assert exc_info.value.code == 3


def test_generic_exception_exits_1() -> None:
    with patch("sys.argv", ["rhapsody-cli", "package", "list"]):
        with patch("rhapsody_cli.cli.cli.PackageCommand") as mock_cls:
            mock_cls.return_value.execute.side_effect = RuntimeError("kaboom")
            with pytest.raises(SystemExit) as exc_info:
                main()
    assert exc_info.value.code == 1
```

- [x] **Step 2: Run and verify they PASS (characterization, not red/green)**

Run: `pytest tests/unit/cli/test_dispatch_characterization.py -v`
Expected: all PASS. If `test_no_arguments_prints_usage_and_exits_2` fails on message wording, adjust the assertion to the actual `_usage()` output ("Usage" appears in the message).

- [x] **Step 3: Commit**

```bash
git add tests/unit/cli/test_dispatch_characterization.py
git commit -m "test(cli): characterize current dispatch behavior before reorg"
```

### Task 2: Session gate + read-action output characterization

**Files:**
- Modify: `tests/unit/cli/test_dispatch_characterization.py` (append)

- [x] **Step 1: Append the action-level characterization tests**

```python
# ---------------------------------------------------------------------------
# Action-level characterization (session gate + multi-format output)
# ---------------------------------------------------------------------------

from rhapsody_cli.actions.package_action import PackageListAction, PackageViewAction


def test_session_gate_blocks_when_not_connected() -> None:
    action = PackageListAction()
    args = MagicMock()
    with patch("rhapsody_cli.actions.abstract_action.SessionManager") as mock_sm:
        mock_sm.return_value.load.return_value = None
        with pytest.raises(CliExecutionError) as exc_info:
            action.execute(args)
    assert "Not connected. Run 'rhapsody-cli connect' first." in str(exc_info.value)


def test_package_list_format_output_json() -> None:
    action = PackageListAction()
    output = action._format_output(["Alpha", "Beta"], "json")
    import json as _json

    assert _json.loads(output) == ["Alpha", "Beta"]


def test_package_list_format_output_csv() -> None:
    action = PackageListAction()
    output = action._format_output(["Alpha", "Beta"], "csv")
    assert "Alpha" in output
    assert "Beta" in output
    assert "," in output


def test_package_list_format_output_table() -> None:
    action = PackageListAction()
    output = action._format_output(["Alpha", "Beta"], "table")
    assert "Alpha" in output and "Beta" in output
```

- [x] **Step 2: Run and verify PASS**

Run: `pytest tests/unit/cli/test_dispatch_characterization.py -v`
Expected: all PASS (these exercise existing `_format_output` and `SessionAwareAction.execute` with mocks).

- [x] **Step 3: Commit**

```bash
git add tests/unit/cli/test_dispatch_characterization.py
git commit -m "test(cli): characterize session gate and list output formats"
```

---

## Stage 2 — Dispatch overhaul

### Task 3: RootCommandAction base + csv branch in `_print_formatted_output`

**Files:**
- Modify: `src/rhapsody_cli/actions/abstract_action.py`
- Modify: `tests/unit/actions/test_abstract_action.py`

- [x] **Step 1: Write failing tests for the csv branch and RootCommandAction**

Append to `tests/unit/actions/test_abstract_action.py`:

```python
class TestPrintFormattedOutputCsv:
    """The shared output helper must support csv like the per-file copies do."""

    def _action(self, output_format: str) -> RhapsodyContextAction:
        action = RhapsodyContextAction(command_id="probe")
        action.output_format = output_format
        return action

    def test_csv_renders_headers_and_rows(self, capsys: pytest.CaptureFixture) -> None:
        self._action("csv")._print_formatted_output({"a": 1}, ["Name"], [["Alpha"]])
        out = capsys.readouterr().out
        assert "Name" in out and "Alpha" in out

    def test_json_still_renders_payload(self, capsys: pytest.CaptureFixture) -> None:
        self._action("json")._print_formatted_output({"a": 1}, ["Name"], [["Alpha"]])
        assert '"a"' in capsys.readouterr().out

    def test_table_renders_rows(self, capsys: pytest.CaptureFixture) -> None:
        self._action("table")._print_formatted_output({"a": 1}, ["Name"], [["Alpha"]])
        assert "Alpha" in capsys.readouterr().out


class TestRootCommandAction:
    """Top-level single commands satisfy the register/run entry protocol."""

    def test_register_creates_subparser(self) -> None:
        import argparse as _argparse

        action = VersionAction()
        root = _argparse.ArgumentParser()
        subparsers = root.add_subparsers()
        action.register(subparsers)
        assert "version" in subparsers.choices

    def test_run_delegates_to_execute(self) -> None:
        action = VersionAction()
        args = MagicMock()
        with patch.object(action, "execute") as mock_execute:
            action.run(args)
        mock_execute.assert_called_once_with(args)
```

(Adjust the import line at the top of the file: add `RhapsodyContextAction` from `rhapsody_cli.actions.abstract_action` and `VersionAction` from `rhapsody_cli.actions.session_action`; the file already imports MagicMock/patch/pytest.)

- [x] **Step 2: Run to verify FAIL**

Run: `pytest tests/unit/actions/test_abstract_action.py -k "Csv or RootCommand" -v`
Expected: FAIL — `RhapsodyContextAction` has no attribute `register`/`run`; csv falls through to table.

- [x] **Step 3: Implement in `abstract_action.py`**

(a) Extend `_print_formatted_output` (replace the body's format selection):

```python
        if self.output_format == "json" and not force_table:
            output = OutputFormatter.json_format(data)
        elif self.output_format == "csv":
            output = OutputFormatter.csv_format(headers, table_rows)
        else:
            output = OutputFormatter.table(headers, table_rows)
```

(b) Add after `SessionAwareAction` (before `ElementManagementAction`):

```python
class RootCommandAction(AbstractAction):
    """Base for top-level single commands registered directly in the root registry.

    Implements the CliEntry protocol (register/run) by delegating to the
    action's own init_arguments/execute.
    """

    def register(self, subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register this command's subparser in the root parser.

        Args:
            subparsers: The root parser's subparsers action.
        """
        self.init_arguments(subparsers)

    def run(self, namespace: argparse.Namespace) -> None:
        """Execute this command from the parsed root namespace.

        Args:
            namespace: The argparse namespace parsed by the root parser.
        """
        self.execute(namespace)
```

- [x] **Step 4: Run to verify PASS**

Run: `pytest tests/unit/actions/test_abstract_action.py -v`
Expected: all PASS.

- [x] **Step 5: Commit**

```bash
git add src/rhapsody_cli/actions/abstract_action.py tests/unit/actions/test_abstract_action.py
git commit -m "feat(cli): csv in shared output helper; RootCommandAction entry protocol"
```

### Task 4: Reshape `AbstractCommand` to register/run

**Files:**
- Modify: `src/rhapsody_cli/commands/abstract_command.py`
- Modify: `src/rhapsody_cli/commands/{attribute,class,operation,package,port,project}_command.py` (remove `__init__` overrides)
- Modify: `tests/unit/cli/test_cli.py` (keep old contract green until Task 8 rewrites it — old tests patch `PackageCommand` and call `main()`, which still constructs groups, so keep a temporary compatible constructor)

- [x] **Step 1: Write the failing group-protocol test**

Append to `tests/unit/cli/test_dispatch_characterization.py`:

```python
def test_group_satisfies_entry_protocol() -> None:
    """Groups expose register/run against a root subparsers action."""
    import argparse as _argparse

    from rhapsody_cli.commands.package_command import PackageCommand

    group = PackageCommand()
    root = _argparse.ArgumentParser()
    subparsers = root.add_subparsers()
    group.register(subparsers)
    assert "package" in subparsers.choices

    namespace = _argparse.Namespace(subcommand="list")
    action = MagicMock()
    group._sub_commands = {"list": action}
    group.run(namespace)
    action.execute.assert_called_once_with(namespace)
```

- [x] **Step 2: Run to verify FAIL**

Run: `pytest tests/unit/cli/test_dispatch_characterization.py::test_group_satisfies_entry_protocol -v`
Expected: FAIL — `PackageCommand()` takes args; no `register`.

- [x] **Step 3: Reshape `AbstractCommand`**

Replace the whole class body with:

```python
class AbstractCommand:
    """Base class for all CLI command groups.

    Subclasses provide their set of AbstractAction instances via get_actions().
    Each group registers a subparser into the root parser (register) and
    dispatches to the action selected by the parsed namespace (run).
    """

    def __init__(self) -> None:
        """Initialize the group with an empty subcommand map (filled by register)."""
        self._sub_commands: Dict[str, AbstractAction] = {}

    def get_actions(self) -> List[AbstractAction]:
        """Return the list of actions (subcommands) for this command group.

        Subclasses must override this to register their own actions.
        """
        raise NotImplementedError(f"{self.__class__.__name__}.get_actions() must be implemented")

    def register(self, subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register this group's subparser and its actions' sub-subparsers.

        Args:
            subparsers: The root parser's subparsers action.
        """
        name = self._command_name()
        parser = subparsers.add_parser(name, help=f"Manage {name}s")
        actions = self.get_actions()
        self._sub_commands = {action.command_id: action for action in actions}
        sub_parsers = parser.add_subparsers(dest="subcommand", required=True, metavar="<subcommand>")
        for action in actions:
            action.init_arguments(sub_parsers)

    def run(self, namespace: argparse.Namespace) -> None:
        """Dispatch execution to the action selected by the namespace.

        Args:
            namespace: The parsed argparse namespace (from the root parser).

        Raises:
            CliExecutionError: If the requested subcommand is unknown.
        """
        action = self._sub_commands.get(namespace.subcommand)
        if action is None:
            logger.error("Unknown subcommand '%s'", namespace.subcommand)
            raise CliExecutionError(f"Unknown subcommand '{namespace.subcommand}'", exit_code=2)
        action.execute(namespace)

    def _command_name(self) -> str:
        """Get the command name (lowercase class name)."""
        return self.__class__.__name__.replace("Command", "").lower()
```

- [x] **Step 4: Update the 6 group classes**

In each of `attribute_command.py`, `class_command.py`, `operation_command.py`, `package_command.py`, `port_command.py`, `project_command.py`: delete the `__init__` override entirely (constructor now inherited, command name derived from class name). Keep `get_actions()` unchanged. For `package_command.py` the result is:

```python
class PackageCommand(AbstractCommand):
    """Package command group - handles package subcommands (create, delete, view, list, update)."""

    def get_actions(self) -> List[AbstractAction]:
        """Return the package subcommand actions."""
        return [
            PackageCreateAction(),
            PackageDeleteAction(),
            PackageViewAction(),
            PackageListAction(),
            PackageUpdateAction(),
        ]
```

(The export/import entries are removed in Task 6; leave them in `get_actions()` for now so the group still works — they are removed in this same edit ONLY if Task 6 has already landed. To keep tasks independent: leave the current export/import imports in place during Task 4.)

- [x] **Step 5: Make the old main() path work temporarily**

`cli.py::main()` constructs `ClassCommand(command_args)` etc. Keep a legacy constructor path: add to `AbstractCommand`:

```python
    def __init__(self, args: Optional[List[str]] = None) -> None:
        """Initialize the group.

        Args:
            args: Legacy two-tier usage passes raw args for immediate parsing;
                registry usage constructs without args and defers to register().
        """
        self._sub_commands: Dict[str, AbstractAction] = {}
        self._parsed_args: Optional[argparse.Namespace] = None
        self._subcommand: Optional[str] = None
        if args is not None:
            self._legacy_parse(args)

    def _legacy_parse(self, args: List[str]) -> None:
        """Two-tier constructor path (removed when main() moves to the registry)."""
        import argparse as _argparse

        name = self._command_name()
        parser = _argparse.ArgumentParser(prog=f"rhapsody-cli {name}")
        actions = self.get_actions()
        self._sub_commands = {action.command_id: action for action in actions}
        sub_parsers = parser.add_subparsers(dest="subcommand")
        for action in actions:
            action.init_arguments(sub_parsers)
        self._parsed_args = parser.parse_args(args)
        self._subcommand = self._parsed_args.subcommand
        if not self._subcommand:
            parser.print_help()
            raise CliExecutionError(f"Missing subcommand for '{name}'", exit_code=2)

    def execute(self, output_format: str = "table") -> None:
        """Legacy two-tier dispatch (removed with _legacy_parse)."""
        action = self._sub_commands.get(self._subcommand) if self._subcommand else None
        if action is None or self._parsed_args is None:
            raise CliExecutionError(f"Unknown subcommand '{self._subcommand}'", exit_code=2)
        if hasattr(action, "output_format"):
            action.output_format = output_format
        action.execute(self._parsed_args)
```

Run: `pytest tests/unit/cli/ tests/unit/actions/ -q` — everything from Tasks 1-3 plus legacy behavior PASS.

- [x] **Step 6: Commit**

```bash
git add src/rhapsody_cli/commands/ src/rhapsody_cli/actions/abstract_action.py tests/unit/cli/test_dispatch_characterization.py
git commit -m "feat(cli): command groups satisfy register/run entry protocol"
```

### Task 5: Registry + root parser + new main() (flag consolidation + usage text flip)

**Files:**
- Modify: `src/rhapsody_cli/cli/cli.py` (full rewrite)
- Modify: `tests/unit/cli/test_cli.py` (rewrite for the new contract)
- Modify: `tests/unit/cli/test_dispatch_characterization.py` (flip the two INTENDED-CHANGE cases)

- [x] **Step 1: Rewrite the failing-contract tests first**

Replace `tests/unit/cli/test_cli.py` content with:

```python
"""Tests for the registry-driven root CLI dispatcher (rhapsody_cli.cli.cli)."""

import argparse
from typing import List
from unittest.mock import MagicMock, patch

import pytest

from rhapsody_cli.cli.cli import build_registry, build_root_parser, main
from rhapsody_cli.exceptions import CliExecutionError


def test_registry_covers_all_commands() -> None:
    commands = build_registry()
    assert set(commands) == {
        "connect", "disconnect", "status", "version",
        "export", "import",
        "class", "attribute", "operation", "package", "port", "project",
    }


def test_root_parser_registers_every_command() -> None:
    parser = build_root_parser(build_registry())
    subparsers = next(a for a in parser._actions if isinstance(a, argparse._SubParsersAction))
    assert set(subparsers.choices) == set(build_registry())


def test_global_format_propagates_into_group_namespace() -> None:
    parser = build_root_parser(build_registry())
    namespace = parser.parse_args(["--format", "json", "package", "list"])
    assert namespace.format == "json"
    assert namespace.subcommand == "list"


def test_global_format_default_is_table() -> None:
    parser = build_root_parser(build_registry())
    namespace = parser.parse_args(["package", "list"])
    assert namespace.format == "table"


def test_format_after_group_is_rejected() -> None:
    parser = build_root_parser(build_registry())
    with pytest.raises(SystemExit) as exc_info:
        parser.parse_args(["package", "list", "--format", "json"])
    assert exc_info.value.code == 2


def test_unknown_command_exits_2(capsys: pytest.CaptureFixture) -> None:
    with patch("sys.argv", ["rhapsody-cli", "bogus"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 2
    assert "invalid choice" in capsys.readouterr().err


def test_main_runs_selected_entry() -> None:
    namespace = MagicMock(subcommand="list")
    entry = MagicMock()
    with patch("sys.argv", ["rhapsody-cli", "package", "list"]):
        with patch("rhapsody_cli.cli.cli.build_registry") as mock_registry:
            with patch("rhapsody_cli.cli.cli.build_root_parser") as mock_build:
                mock_parser = MagicMock()
                mock_parser.parse_args.return_value = namespace
                mock_build.return_value = mock_parser
                mock_registry.return_value = {"package": entry}
                with patch("rhapsody_cli.cli.cli.CliLoggingConfigurator") as mock_log:
                    main()
    entry.run.assert_called_once_with(namespace)
    mock_log.return_value.configure.assert_called_once()


def test_main_cli_execution_error_uses_exit_code() -> None:
    entry = MagicMock()
    entry.run.side_effect = CliExecutionError("boom", exit_code=3)
    with patch("sys.argv", ["rhapsody-cli", "package", "list"]):
        with patch("rhapsody_cli.cli.cli.build_registry", return_value={"package": entry}):
            with patch("rhapsody_cli.cli.cli.build_root_parser") as mock_build:
                mock_parser = MagicMock()
                mock_parser.parse_args.return_value = MagicMock(verbose=False)
                mock_build.return_value = mock_parser
                with pytest.raises(SystemExit) as exc_info:
                    main()
    assert exc_info.value.code == 3
```

- [x] **Step 2: Rewrite `cli.py`**

Replace the entire file content with:

```python
"""Main CLI entry point: registry-driven root parser (PanGu style)."""

import argparse
import logging
import sys
from typing import Dict, Protocol

from rhapsody_cli.actions.attribute_action import AttributeCreateAction, AttributeDeleteAction, AttributeListAction, AttributeUpdateAction, AttributeViewAction
from rhapsody_cli.actions.session_action import ConnectAction, DisconnectAction, StatusAction, VersionAction
from rhapsody_cli.cli.logging_config import CliLoggingConfigurator
from rhapsody_cli.commands.attribute_command import AttributeCommand
from rhapsody_cli.commands.class_command import ClassCommand
from rhapsody_cli.commands.operation_command import OperationCommand
from rhapsody_cli.commands.package_command import PackageCommand
from rhapsody_cli.commands.port_command import PortCommand
from rhapsody_cli.commands.project_command import ProjectCommand
from rhapsody_cli.exceptions import CliExecutionError

logger = logging.getLogger(__name__)


class CliEntry(Protocol):
    """A top-level CLI command: registers a subparser and runs from the namespace."""

    def register(self, subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Create this entry's subparser under the root subparsers action."""
        ...

    def run(self, namespace: argparse.Namespace) -> None:
        """Execute this entry using values from the parsed namespace."""
        ...


def build_registry() -> Dict[str, CliEntry]:
    """Build the top-level command registry (name -> entry instance)."""
    return {
        "connect": ConnectAction(),
        "disconnect": DisconnectAction(),
        "status": StatusAction(),
        "version": VersionAction(),
        "class": ClassCommand(),
        "attribute": AttributeCommand(),
        "operation": OperationCommand(),
        "package": PackageCommand(),
        "port": PortCommand(),
        "project": ProjectCommand(),
    }


def build_root_parser(commands: Dict[str, CliEntry]) -> argparse.ArgumentParser:
    """Build the root parser with global flags and every registered command.

    Args:
        commands: The command registry from build_registry().

    Returns:
        The fully wired root ArgumentParser.
    """
    parser = argparse.ArgumentParser(prog="rhapsody-cli", description="Rhapsody CLI")
    parser.add_argument("--format", choices=["table", "json", "csv"], default="table", help="Output format (global; use before the command)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug logging")
    subparsers = parser.add_subparsers(dest="command", required=True, metavar="<command>")
    for name, entry in commands.items():
        entry.register(subparsers)
    for name, sub_parser in subparsers.choices.items():
        sub_parser.set_defaults(entry=commands[name])
    return parser


def main() -> None:
    """Main CLI entry point."""
    root_parser = build_root_parser(build_registry())
    namespace = root_parser.parse_args()
    CliLoggingConfigurator(verbose=namespace.verbose).configure()
    try:
        namespace.entry.run(namespace)
    except KeyboardInterrupt:
        # NOTE: Terminal feedback for interactive Ctrl+C; print() to stdout
        # with a leading newline to clear the ^C echo.
        print("\nInterrupted")
        sys.exit(130)
    except SystemExit:
        raise
    except CliExecutionError as e:
        logger.error(str(e))
        sys.exit(e.exit_code)
    except Exception as e:
        logger.error("Command failed: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
```

(Note: single-level actions `ConnectAction` etc. must inherit `RootCommandAction` for the protocol — that change is Task 6 step 3; until then `build_registry` type-checks structurally only if they have register/run. Do Task 6's session-action edits in the same commit if needed to keep the gate green — mypy checks `src/`, and Protocol is structural so plain `AbstractAction` subclasses that lack register/run fail mypy only at the Dict annotation. Simplest sequencing: apply Task 6 step 3 (make session actions inherit `RootCommandAction`) BEFORE running the gate for this task.)

- [x] **Step 3: Make session actions RootCommandActions**

In `src/rhapsody_cli/actions/session_action.py`, change each of the four class declarations to inherit `RootCommandAction` (import it from `abstract_action`):

```python
from rhapsody_cli.actions.abstract_action import RootCommandAction

class ConnectAction(RootCommandAction):
class DisconnectAction(RootCommandAction):
class StatusAction(RootCommandAction):
class VersionAction(RootCommandAction):
```

- [x] **Step 4: Flip the INTENDED-CHANGE characterization tests**

In `tests/unit/cli/test_dispatch_characterization.py`:
- Replace `test_format_flag_after_group_also_works_today` with:

```python
def test_format_flag_after_group_is_rejected() -> None:
    # INTENDED-CHANGE (applied): --format is strictly global now.
    with patch("sys.argv", ["rhapsody-cli", "package", "list", "--format", "json"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 2
```

- Update `test_no_arguments_prints_usage_and_exits_2` for argparse output:

```python
def test_no_arguments_prints_usage_and_exits_2(capsys: pytest.CaptureFixture) -> None:
    with patch("sys.argv", ["rhapsody-cli"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 2
    err = capsys.readouterr().err
    assert "the following arguments are required: command" in err
```

- Update `test_unknown_command_prints_error_and_exits_2`:

```python
def test_unknown_command_prints_error_and_exits_2(capsys: pytest.CaptureFixture) -> None:
    with patch("sys.argv", ["rhapsody-cli", "bogus"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 2
    assert "invalid choice" in capsys.readouterr().err
```

- Delete the now-obsolete `_legacy_parse`/`execute` from `AbstractCommand` (Task 4 step 5's temporary code) and the group-constructs-with-args path.

- [x] **Step 5: Run the full unit gate**

Run: `pytest tests/unit -q`
Expected: PASS except tests referencing `_usage`/legacy execute — fix imports of removed names in `tests/unit/cli/test_cli.py`-adjacent files only; the old `test_cli.py` was replaced in step 1. If `tests/unit/actions/test_session_action.py` asserts `add_verbose_argument` registration, update those assertions in Task 6 (next) — run `pytest tests/unit/actions/test_session_action.py -q` to see.

- [x] **Step 6: Commit**

```bash
git add src/rhapsody_cli/cli/cli.py src/rhapsody_cli/commands/abstract_command.py src/rhapsody_cli/actions/session_action.py tests/unit/cli/
git commit -m "feat(cli): registry-driven root parser; global --format/-v; argparse help"
```

### Task 6: Strip per-subcommand `--format`/`-v` (flag consolidation completion)

**Files:**
- Modify: `src/rhapsody_cli/actions/{attribute,class,operation,package,port,project}_action.py`, `src/rhapsody_cli/actions/session_action.py`
- Modify: `src/rhapsody_cli/actions/abstract_action.py` (delete `add_verbose_argument`)
- Modify: affected tests under `tests/unit/actions/`

- [x] **Step 1: Find every per-subcommand `--format` and `-v` registration**

Run: `grep -n '"--format"\|add_verbose_argument' src/rhapsody_cli/actions/*.py`
Expected: ~10 `--format` registrations (list/view in 5 domain files) and ~38 `add_verbose_argument` calls.

- [x] **Step 2: Delete them all**

For each `list`/`view` action's `init_arguments`, remove the line:

```python
        parser.add_argument("--format", choices=["table", "json", "csv"], default="table", help="Output format")
```

For every other action, remove the line:

```python
        self.add_verbose_argument(parser)
```

Then delete the `add_verbose_argument` static method from `AbstractAction` (lines ~57-69 of `abstract_action.py`).

- [x] **Step 3: Point every printing action at `args.format`**

In every `list`/`view` action's `execute`, the existing call `self._format_output(data, args.format)` already reads `args.format` — with the per-subcommand argument gone, `args.format` now comes from the root parser (argparse propagates root defaults). No code change needed for those. For actions that print via `self.output_format` attribute (set by the legacy injection that no longer exists), add at the top of `execute` (after `super().execute(args)` where present):

```python
        self.output_format = args.format
```

Find candidates: `grep -n "self.output_format" src/rhapsody_cli/actions/*.py | grep -v abstract`.

- [x] **Step 4: Update tests that register/exercise the removed flags**

Run: `pytest tests/unit -q` and fix only assertions that reference `--format` as a subcommand argument or `add_verbose_argument`. Example fix pattern (in any action test that built args namespaces): replace `args.format = "json"` with the same assignment (unchanged — namespace attr name is identical) and delete tests asserting a subparser has a `--format` option.

- [x] **Step 5: Verify grep is clean and gate is green**

Run: `grep -n '"--format"\|add_verbose_argument' src/rhapsody_cli/actions/*.py; pytest tests/unit -q`
Expected: grep finds nothing in actions/ (root parser in cli.py still has it); unit suite PASS.

- [x] **Step 6: Commit**

```bash
git add src/rhapsody_cli/actions/ src/rhapsody_cli/actions/abstract_action.py tests/unit/actions/
git commit -m "feat(cli): consolidate --format/-v as strictly global flags"
```

### Task 7: Promote `export` / `import` to root commands

**Files:**
- Create: `src/rhapsody_cli/actions/transfer/__init__.py`, `src/rhapsody_cli/actions/transfer/export.py`, `src/rhapsody_cli/actions/transfer/importer.py`
- Create: `tests/unit/actions/test_transfer.py`
- Modify: `src/rhapsody_cli/actions/package_action.py` (remove the two classes), `src/rhapsody_cli/commands/package_command.py` (remove from `get_actions()`), `src/rhapsody_cli/cli/cli.py` (register at root)
- Modify: `tests/unit/actions/test_package_action.py` (remove `TestPackageExportAction`/`TestPackageImportAction`)

- [x] **Step 1: Write the transfer tests (moved + retargeted)**

Create `tests/unit/actions/test_transfer.py` (adapt the bodies of the removed `TestPackageExportAction`/`TestPackageImportAction` from `tests/unit/actions/test_package_action.py:687-788`; the assertions stay identical, only imports and class names change):

```python
"""Tests for the root-level export/import commands (SWR_XCH_001)."""

from unittest.mock import MagicMock, patch

import pytest

from rhapsody_cli.actions.transfer.export import ExportAction
from rhapsody_cli.actions.transfer.importer import ImportAction
from rhapsody_cli.exceptions import CliExecutionError


class TestExportAction:
    def test_export_writes_yaml_and_reports(self) -> None:
        action = ExportAction()
        mock_app = MagicMock()
        mock_package = MagicMock()
        with patch.object(action, "_connect_app", return_value=mock_app):
            with patch.object(action, "_resolve_and_validate_package", return_value=mock_package):
                with patch("rhapsody_cli.actions.transfer.export.RhapsodyExporter") as mock_exporter, patch(
                    "rhapsody_cli.actions.transfer.export.RhapsodyYaml"
                ) as mock_yaml:
                    args = MagicMock()
                    args.path = "Sensors"
                    args.file = "out.yaml"
                    action.execute(args)
        mock_exporter.return_value.export.assert_called_once_with(mock_package)
        mock_yaml.return_value.write.assert_called_once_with("out.yaml", mock_exporter.return_value.export.return_value)


class TestImportAction:
    def test_import_reads_yaml_imports_and_saves(self) -> None:
        action = ImportAction()
        mock_app = MagicMock()
        mock_package = MagicMock()
        with patch.object(action, "_connect_app", return_value=mock_app):
            with patch.object(action, "_resolve_and_validate_package", return_value=mock_package):
                with patch("rhapsody_cli.actions.transfer.importer.RhapsodyImporter") as mock_importer, patch(
                    "rhapsody_cli.actions.transfer.importer.RhapsodyYaml"
                ) as mock_yaml:
                    args = MagicMock()
                    args.path = None
                    args.file = "in.yaml"
                    action.execute(args)
        mock_yaml.return_value.read.assert_called_once_with("in.yaml")
        mock_importer.return_value.import_template.assert_called_once_with(mock_yaml.return_value.read.return_value, mock_package)
        mock_app.save_all.assert_called_once()

    def test_requires_package_resolution(self) -> None:
        action = ImportAction()
        with patch.object(action, "_resolve_and_validate_package", side_effect=CliExecutionError("Path 'X' does not resolve to a Package")):
            args = MagicMock()
            args.path = "X"
            args.file = "in.yaml"
            with pytest.raises(CliExecutionError):
                with patch.object(action, "_connect_app", return_value=MagicMock()):
                    action.execute(args)
```

- [x] **Step 2: Run to verify FAIL**

Run: `pytest tests/unit/actions/test_transfer.py -v`
Expected: FAIL — `rhapsody_cli.actions.transfer` does not exist.

- [x] **Step 3: Create the transfer package**

`src/rhapsody_cli/actions/transfer/__init__.py`:

```python
"""Root-level transfer commands (export/import of YAML package payloads)."""

from rhapsody_cli.actions.transfer.export import ExportAction
from rhapsody_cli.actions.transfer.importer import ImportAction

__all__ = ["ExportAction", "ImportAction"]
```

`src/rhapsody_cli/actions/transfer/export.py` — copy `PackageExportAction`'s body verbatim, renaming the class and adding the package-resolution base import:

```python
"""Root `export` command — exports a package to a YAML file (SWR_XCH_001)."""

import argparse

from rhapsody_cli.actions.package_action import AbstractPackageAction
from rhapsody_cli.exceptions import CliExecutionError, RhapsodyConnectionError
from rhapsody_cli.exchange.exporter import RhapsodyExporter
from rhapsody_cli.exchange.yaml_utils import RhapsodyYaml


class ExportAction(AbstractPackageAction):
    """Action for the root `export` command — exports a package to a YAML file."""

    def __init__(self) -> None:
        super().__init__(command_id="export")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        parser = sub_parser.add_parser(self.command_id, help="Export a package to a YAML file")
        self.add_path_argument(parser, required=False, help_text="Path to package (defaults to root)")
        parser.add_argument("--file", required=True, help="Output YAML file path")

    def execute(self, args: argparse.Namespace) -> None:
        super().execute(args)
        try:
            app = self._connect_app()
            package = self._resolve_and_validate_package(args.path)
            exporter = RhapsodyExporter(app=app)
            data = exporter.export(package)
            yaml_io = RhapsodyYaml()
            yaml_io.write(args.file, data)
            self.logger.info("Exported package to %s", args.file)
        except RhapsodyConnectionError as e:
            self._handle_connection_error(e, "export package")
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, "export package")
```

`src/rhapsody_cli/actions/transfer/importer.py` — same pattern for `PackageImportAction` (module named `importer.py` because `import.py` is not a legal module name):

```python
"""Root `import` command — imports a YAML file into a package (SWR_XCH_001)."""

import argparse

from rhapsody_cli.actions.package_action import AbstractPackageAction
from rhapsody_cli.exceptions import CliExecutionError, RhapsodyConnectionError
from rhapsody_cli.exchange.importer import RhapsodyImporter
from rhapsody_cli.exchange.yaml_utils import RhapsodyYaml


class ImportAction(AbstractPackageAction):
    """Action for the root `import` command — imports a YAML file into a package."""

    def __init__(self) -> None:
        super().__init__(command_id="import")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        parser = sub_parser.add_parser(self.command_id, help="Import a YAML file into a package")
        self.add_path_argument(parser, required=False, help_text="Path to target package (defaults to root)")
        parser.add_argument("--file", required=True, help="Input YAML file path")

    def execute(self, args: argparse.Namespace) -> None:
        super().execute(args)
        try:
            app = self._connect_app()
            package = self._resolve_and_validate_package(args.path)
            yaml_io = RhapsodyYaml()
            data = yaml_io.read(args.file)
            importer = RhapsodyImporter(app=app)
            importer.import_template(data, package)
            app.save_all()
            self.logger.info("Imported %s into package", args.file)
        except RhapsodyConnectionError as e:
            self._handle_connection_error(e, "import package")
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, "import package")
```

- [x] **Step 4: Remove the old classes and register at root**

(a) Delete `PackageExportAction` and `PackageImportAction` (lines ~608-672) from `src/rhapsody_cli/actions/package_action.py`; remove their now-unused imports (`RhapsodyExporter`, `RhapsodyImporter`, `RhapsodyYaml`) from that file's header if no other class uses them.

(b) In `src/rhapsody_cli/commands/package_command.py`: remove the `PackageExportAction`/`PackageImportAction` imports and entries from `get_actions()`.

(c) In `src/rhapsody_cli/cli/cli.py`: add to imports `from rhapsody_cli.actions.transfer import ExportAction, ImportAction` and to `build_registry()`:

```python
        "export": ExportAction(),
        "import": ImportAction(),
```

- [x] **Step 5: Remove the moved test classes and run the gate**

Delete `TestPackageExportAction` and `TestPackageImportAction` from `tests/unit/actions/test_package_action.py`.

Run: `pytest tests/unit -q && ruff check src/ tests/ && black --check src/ tests/`
Expected: PASS; also `pytest tests/unit/cli/test_cli.py::test_registry_covers_all_commands -q` already covers the registry keys (Task 5).

- [x] **Step 6: Commit**

```bash
git add src/rhapsody_cli/actions/transfer/ src/rhapsody_cli/actions/package_action.py src/rhapsody_cli/commands/package_command.py src/rhapsody_cli/cli/cli.py tests/unit/actions/
git commit -m "feat(cli): promote export/import to root commands (SWR_XCH_001)"
```

---

## Stage 3 — Shared helpers and unification

### Task 8: `actions/support.py` (pure helpers)

**Files:**
- Create: `src/rhapsody_cli/actions/support.py`
- Create: `tests/unit/actions/test_support.py`
- Modify: the five domain action files (call-site swap)

- [x] **Step 1: Write failing tests for the helpers**

Create `tests/unit/actions/test_support.py`:

```python
"""Tests for pure CLI action helpers (actions.support)."""

import json
from pathlib import Path

import pytest

from rhapsody_cli.actions.support import load_json_mapping, write_text_file


class TestLoadJsonMapping:
    def test_inline_json_object(self) -> None:
        assert load_json_mapping('{"name":"Temp"}') == {"name": "Temp"}

    def test_json_file_reference(self, tmp_path: Path) -> None:
        f = tmp_path / "attrs.json"
        f.write_text('{"name":"FromFile"}')
        assert load_json_mapping(str(f)) == {"name": "FromFile"}

    def test_invalid_json_raises_cli_error(self) -> None:
        from rhapsody_cli.exceptions import CliExecutionError

        with pytest.raises(CliExecutionError):
            load_json_mapping("{not json")


class TestWriteTextFile:
    def test_writes_content(self, tmp_path: Path) -> None:
        target = tmp_path / "out.txt"
        write_text_file(str(target), "hello")
        assert target.read_text() == "hello"

    def test_creates_parent_directories(self, tmp_path: Path) -> None:
        target = tmp_path / "sub" / "out.txt"
        write_text_file(str(target), "hello")
        assert target.read_text() == "hello"

    def test_rejects_unwritable_path(self, tmp_path: Path) -> None:
        from rhapsody_cli.exceptions import CliExecutionError

        with pytest.raises(CliExecutionError):
            write_text_file(str(tmp_path / "nope" / "out.txt"), "x")
```

NOTE: before finalizing these tests, read the current `_load_json_data`/`_write_to_file` bodies in `src/rhapsody_cli/actions/package_action.py` (lines ~232-260 and ~390-398) and port their exact error semantics into `support.py` — the helpers must preserve today's error messages/exit codes (characterization rule). If a copy's semantics differ from another's (e.g. one raises on unwritable path, another logs), keep the strictest common behavior and note the difference in the helper's docstring.

- [x] **Step 2: Run to verify FAIL**

Run: `pytest tests/unit/actions/test_support.py -v`
Expected: FAIL — module does not exist.

- [x] **Step 3: Implement `support.py`**

```python
"""Pure helpers shared by CLI actions (no COM, no session, no I/O beyond files)."""

import json
import logging
from pathlib import Path
from typing import Dict, Union

from rhapsody_cli.exceptions import CliExecutionError

logger = logging.getLogger(__name__)

JsonInput = Union[str, Dict[str, object]]


def load_json_mapping(attributes_input: str) -> Dict[str, object]:
    """Load a JSON object from an inline string or a file path.

    Args:
        attributes_input: Inline JSON object text, or a path to a JSON file
            containing an object.

    Returns:
        The parsed JSON object.

    Raises:
        CliExecutionError: If the input is neither valid JSON nor a readable
            file containing a JSON object.
    """
    candidate = Path(attributes_input)
    if candidate.exists():
        try:
            data = json.loads(candidate.read_text())
        except json.JSONDecodeError as e:
            raise CliExecutionError(f"Invalid JSON in file '{attributes_input}': {e}") from e
    else:
        try:
            data = json.loads(attributes_input)
        except json.JSONDecodeError as e:
            raise CliExecutionError(f"Invalid JSON input: {e}") from e
    if not isinstance(data, dict):
        raise CliExecutionError("JSON input must be an object with string keys")
    return data


def write_text_file(file_path: str, content: str) -> None:
    """Write text content to a file, creating parent directories.

    Args:
        file_path: Destination file path.
        content: Text content to write.

    Raises:
        CliExecutionError: If the file cannot be written.
    """
    target = Path(file_path)
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
    except OSError as e:
        raise CliExecutionError(f"Cannot write to '{file_path}': {e}") from e
```

- [x] **Step 4: Run helpers tests to PASS, then swap the five call sites**

Run: `pytest tests/unit/actions/test_support.py -v` — PASS.

In each of `attribute_action.py`, `class_action.py`, `operation_action.py`, `port_action.py`, `package_action.py`: delete the private `_load_json_data` and `_write_to_file` method bodies (keep a one-line delegator ONLY if the method has 3+ call sites in the same file — otherwise update call sites directly):

```python
    def _load_json_data(self, attributes_input: str) -> Dict[str, object]:
        """Delegates to the shared pure helper (see actions.support)."""
        return load_json_mapping(attributes_input)
```

Add the import `from rhapsody_cli.actions.support import load_json_mapping, write_text_file` to each file.

- [x] **Step 5: Full unit gate**

Run: `pytest tests/unit -q`
Expected: PASS.

- [x] **Step 6: Commit**

```bash
git add src/rhapsody_cli/actions/support.py tests/unit/actions/test_support.py src/rhapsody_cli/actions/
git commit -m "refactor(cli): consolidate JSON-load and file-write helpers into actions.support"
```

### Task 9: Unify read-action output on the base helper

**Files:**
- Modify: `src/rhapsody_cli/actions/{attribute,class,operation,package,port}_action.py` (delete `_format_output`, call base helper)

- [x] **Step 1: Swap each read action to the base helper**

In every `List`/`View` action's `execute` replace the pair

```python
            output = self._format_output(data, args.format)
            ...
            print(output)
```

with:

```python
            self.output_format = args.format
            self._print_formatted_output(json_payload, headers, rows)
```

where `json_payload` is the JSON-appropriate data (the names list for `list`, the collected dict for `view`), `headers`/`rows` are the table form (e.g. `["Name"]` / `[[name] for name in package_names]`). Then delete each file's `_format_output` method. Preserve each action's current table headers — read them from the existing `_format_output` bodies before deleting (e.g. package list uses `["Name"]`; view actions use their `_VIEW_HEADERS` constant — keep those constants).

- [x] **Step 2: Verify characterization output tests still pass**

Run: `pytest tests/unit/cli/test_dispatch_characterization.py -q`
Expected: PASS — output strings unchanged (table via `OutputFormatter.table`, json via `json_format`, csv via the Task 3 csv branch).

- [x] **Step 3: Full gate + commit**

```bash
pytest tests/unit -q && ruff check src/ tests/ && black --check src/ tests/
git add src/rhapsody_cli/actions/
git commit -m "refactor(cli): unify list/view output on the shared formatted-output helper"
```

### Task 10: Shared attribute appliers

**Files:**
- Modify: `src/rhapsody_cli/actions/support.py` (add appliers)
- Modify: `src/rhapsody_cli/actions/{package,class}_action.py` (stereotypes/tags), all five (common core)
- Modify: `tests/unit/actions/test_support.py` (applier tests)

- [x] **Step 1: Add applier tests to `test_support.py`**

```python
class TestApplyCommonAttributes:
    def test_applies_name_description_display_name(self) -> None:
        from rhapsody_cli.actions.support import apply_common_attributes

        element = MagicMock()
        apply_common_attributes(element, {"name": "N", "description": "D", "display_name": "DN"})
        assert element.name == "N"
        assert element.description == "D"
        assert element.display_name == "DN"

    def test_ignores_unknown_keys(self) -> None:
        from rhapsody_cli.actions.support import apply_common_attributes

        element = MagicMock()
        apply_common_attributes(element, {"bogus": 1})
        # no exception; nothing set for bogus key
        assert not hasattr(element, "bogus") or element.bogus != 1


class TestApplyStereotypesAndTags:
    def test_applies_stereotypes_list(self) -> None:
        from rhapsody_cli.actions.support import apply_stereotypes_and_tags

        element = MagicMock()
        apply_stereotypes_and_tags(element, {"stereotypes": ["S1"], "tags": {"k": "v"}})
        assert element.add_stereotype.call_args is not None
        assert element.set_tag_value.call_args is not None
```

Add `from unittest.mock import MagicMock` to the file's imports.

- [x] **Step 2: Read the exact current bodies, then implement**

Read `PackageCreateAction._set_stereotypes` and `_set_tags` (`package_action.py:274-292`) — port their exact element-API calls into `support.py`:

```python
def apply_common_attributes(element: object, attrs: Dict[str, object]) -> None:
    """Apply the attribute keys common to every element type.

    Only sets attributes the element actually exposes; unknown keys are skipped
    (preserving the current per-domain behavior).
    """
    for key in ("name", "description", "display_name"):
        if key in attrs and hasattr(element, key):
            setattr(element, key, attrs[key])


def apply_stereotypes_and_tags(element: object, attrs: Dict[str, object]) -> None:
    """Apply 'stereotypes' (list) and 'tags' (mapping) exactly as package create does today."""
    stereotypes = attrs.get("stereotypes")
    if isinstance(stereotypes, list):
        for stereotype in stereotypes:
            element.add_stereotype(str(stereotype))
    tags = attrs.get("tags")
    if isinstance(tags, dict):
        for tag_name, tag_value in tags.items():
            element.set_tag_value(tag_name, str(tag_value))
```

(If the verbatim bodies differ — e.g. tags go through `add_new_aggr("Tag", ...)` first — port THAT shape; the test above then asserts the actual calls. This is a characterization-preserving move, not a redesign.)

- [x] **Step 3: Point package and class `_set_attributes` at the appliers**

In `package_action.py` `_set_basic_attributes` replace the name/description/display_name block with `apply_common_attributes(package, attrs)`; in `_set_attributes` route the `stereotypes`/`tags` keys to `apply_stereotypes_and_tags`. In `class_action.py` `_set_attributes`, do the same for its name/description/stereotypes/tags handling. Leave `attribute`/`operation`/`port` domain-specific fields as-is.

- [x] **Step 4: Full gate + commit**

```bash
pytest tests/unit -q && ruff check src/ tests/ && black --check src/ tests/
git add src/rhapsody_cli/actions/ tests/unit/actions/test_support.py
git commit -m "refactor(cli): shared attribute appliers for common core and stereotypes/tags"
```

---

## Stage 4 — Per-domain file splits (pure moves)

Each task: create the domain package, move classes verbatim (imports at the top of each new file copied from the source file's header, pruned to what that file needs), write the `__init__.py` re-export, delete the old module, update importers (`commands/*_command.py` and tests), run the gate, commit. **A given class's `Abstract*Action` base moves to `<domain>/base.py` and subclasses import it from there.** After every domain: `pytest tests/unit -q && ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/` (mypy on Python <3.10 per CI; skip locally if the venv is 3.10+ — the documented limitation).

### Task 11: Split `session_action.py` → `actions/session/`

**Files:**
- Create: `src/rhapsody_cli/actions/session/__init__.py`, `connect.py`, `disconnect.py`, `status.py`, `version.py`
- Delete: `src/rhapsody_cli/actions/session_action.py`
- Modify: `src/rhapsody_cli/cli/cli.py` import line; `tests/unit/actions/test_session_action.py`

- [x] **Step 1: Create the package with verbatim moves**

One class per file; `connect.py` gets `ConnectAction` plus its module docstring:

```python
"""Root `connect` command — connects to (or launches) Rhapsody."""

# (class ConnectAction moved verbatim from actions/session_action.py;
#  copy the imports that class actually uses from session_action.py's header)
```

Repeat for `disconnect.py`, `status.py`, `version.py`.

`src/rhapsody_cli/actions/session/__init__.py`:

```python
"""Session command actions."""

from rhapsody_cli.actions.session.connect import ConnectAction
from rhapsody_cli.actions.session.disconnect import DisconnectAction
from rhapsody_cli.actions.session.status import StatusAction
from rhapsody_cli.actions.session.version import VersionAction

__all__ = ["ConnectAction", "DisconnectAction", "StatusAction", "VersionAction"]
```

- [x] **Step 2: Update importers**

`cli.py`: replace `from rhapsody_cli.actions.session_action import ...` with `from rhapsody_cli.actions.session import ConnectAction, DisconnectAction, StatusAction, VersionAction`.
`tests/unit/actions/test_session_action.py`: same import swap.

- [x] **Step 3: Delete the old module, gate, commit**

```bash
git rm src/rhapsody_cli/actions/session_action.py
pytest tests/unit -q && ruff check src/ tests/ && black --check src/ tests/
git add -u src/rhapsody_cli/actions/ src/rhapsody_cli/cli/cli.py tests/unit/actions/test_session_action.py
git commit -m "refactor(cli): split session actions into actions/session/"
```

### Task 12: Split `package_action.py` → `actions/package/`

**Files:**
- Create: `src/rhapsody_cli/actions/package/__init__.py`, `base.py`, `create.py`, `delete.py`, `view.py`, `list.py`, `update.py`
- Delete: `src/rhapsody_cli/actions/package_action.py`
- Modify: `src/rhapsody_cli/commands/package_command.py`, `src/rhapsody_cli/actions/transfer/{export,importer}.py` (base import), `tests/unit/actions/test_package_action.py`

- [x] **Step 1: Move classes verbatim**

`base.py` gets `AbstractPackageAction` (docstring: `"""Package action base: shared path validation (SWR_PKG_0005, SWR_PKG_0010)."""`). `create.py` gets `PackageCreateAction` + the module docstring header lines SWR_PKG_0001/0002/0006/0007; `delete.py` → SWR_PKG_0002; `view.py` → SWR_PKG_0003/0009; `list.py` → SWR_PKG_0004/0008; `update.py` → SWR_PKG_0016. Each file imports `from rhapsody_cli.actions.package.base import AbstractPackageAction` plus only the stdlib/third-party names its class uses (prune `json`, `Path`, `OutputFormatter` etc. per file — ruff F401 will flag leftovers).

`src/rhapsody_cli/actions/package/__init__.py`:

```python
"""Package command actions."""

from rhapsody_cli.actions.package.base import AbstractPackageAction
from rhapsody_cli.actions.package.create import PackageCreateAction
from rhapsody_cli.actions.package.delete import PackageDeleteAction
from rhapsody_cli.actions.package.list import PackageListAction
from rhapsody_cli.actions.package.update import PackageUpdateAction
from rhapsody_cli.actions.package.view import PackageViewAction

__all__ = [
    "AbstractPackageAction",
    "PackageCreateAction",
    "PackageDeleteAction",
    "PackageListAction",
    "PackageUpdateAction",
    "PackageViewAction",
]
```

- [x] **Step 2: Update importers**

`package_command.py`: import from `rhapsody_cli.actions.package`. `transfer/export.py` and `transfer/importer.py`: `from rhapsody_cli.actions.package_action import AbstractPackageAction` → `from rhapsody_cli.actions.package.base import AbstractPackageAction`. `tests/unit/actions/test_package_action.py`: import from `rhapsody_cli.actions.package`.

- [x] **Step 3: Delete, gate, commit**

```bash
git rm src/rhapsody_cli/actions/package_action.py
pytest tests/unit -q && ruff check src/ tests/ && black --check src/ tests/
git add -u src/rhapsody_cli/ tests/unit/actions/test_package_action.py src/rhapsody_cli/actions/transfer/
git commit -m "refactor(cli): split package actions into actions/package/"
```

### Task 13: Split `class_action.py` → `actions/class/`

**Files:**
- Create: `src/rhapsody_cli/actions/class/{__init__,base,create,delete,list,view,link,update}.py`
- Delete: `src/rhapsody_cli/actions/class_action.py`
- Modify: `src/rhapsody_cli/commands/class_command.py`, `tests/unit/actions/test_class_action.py`

- [x] **Step 1: Move classes verbatim**

`base.py` ← `AbstractClassAction`; `create.py` ← `ClassCreateAction`; `delete.py` ← `ClassDeleteAction`; `list.py` ← `ClassListAction`; `view.py` ← `ClassViewAction`; `link.py` ← `ClassLinkAction`; `update.py` ← `ClassUpdateAction`. Each subclass file imports `from rhapsody_cli.actions.class.base import AbstractClassAction` (note: `class` is a keyword — package dir named `class/` is legal as a directory since it's not an import statement, BUT `from rhapsody_cli.actions.class.base import ...` is a SyntaxError. Use `importlib`-free naming: rename the package to `cls` is ugly; the established stdlib workaround is `getattr(__import__...)` — unacceptable. **Rename the subpackage to `classifier/`** and keep the registry key `"class"`.)

Corrected layout: `src/rhapsody_cli/actions/classifier/{__init__,base,create,delete,list,view,link,update}.py`.

`src/rhapsody_cli/actions/classifier/__init__.py`:

```python
"""Class command actions."""

from rhapsody_cli.actions.classifier.base import AbstractClassAction
from rhapsody_cli.actions.classifier.create import ClassCreateAction
from rhapsody_cli.actions.classifier.delete import ClassDeleteAction
from rhapsody_cli.actions.classifier.link import ClassLinkAction
from rhapsody_cli.actions.classifier.list import ClassListAction
from rhapsody_cli.actions.classifier.update import ClassUpdateAction
from rhapsody_cli.actions.classifier.view import ClassViewAction

__all__ = [
    "AbstractClassAction",
    "ClassCreateAction",
    "ClassDeleteAction",
    "ClassLinkAction",
    "ClassListAction",
    "ClassUpdateAction",
    "ClassViewAction",
]
```

- [x] **Step 2: Update importers**

`class_command.py` and `tests/unit/actions/test_class_action.py` import from `rhapsody_cli.actions.classifier`.

- [x] **Step 3: Delete, gate, commit**

```bash
git rm src/rhapsody_cli/actions/class_action.py
pytest tests/unit -q && ruff check src/ tests/ && black --check src/ tests/
git add -u src/rhapsody_cli/ tests/unit/actions/test_class_action.py
git commit -m "refactor(cli): split class actions into actions/classifier/"
```

### Task 14: Split `attribute_action.py`, `operation_action.py`, `port_action.py`

**Files:**
- Create: `src/rhapsody_cli/actions/attribute/{__init__,base,create,delete,list,view,update}.py`
- Create: `src/rhapsody_cli/actions/operation/{__init__,base,create,delete,list,view,update}.py`
- Create: `src/rhapsody_cli/actions/port/{__init__,base,create,delete,list,view,update}.py`
- Delete: the three source modules
- Modify: the three command groups; the three test files

- [x] **Step 1: Move classes verbatim (same pattern as Tasks 12-13)**

Per domain: `base.py` ← the `Abstract<Domain>Action` base; then one file per concrete class. Each `__init__.py` follows the package template (attribute example; operation/port mirror it):

```python
"""Attribute command actions."""

from rhapsody_cli.actions.attribute.base import AbstractAttributeAction
from rhapsody_cli.actions.attribute.create import AttributeCreateAction
from rhapsody_cli.actions.attribute.delete import AttributeDeleteAction
from rhapsody_cli.actions.attribute.list import AttributeListAction
from rhapsody_cli.actions.attribute.update import AttributeUpdateAction
from rhapsody_cli.actions.attribute.view import AttributeViewAction

__all__ = [
    "AbstractAttributeAction",
    "AttributeCreateAction",
    "AttributeDeleteAction",
    "AttributeListAction",
    "AttributeUpdateAction",
    "AttributeViewAction",
]
```

(operation: `AbstractOperationAction` + Create/Delete/List/View/Update; port: `AbstractPortAction` + Create/Delete/List/View/Update — adjust names in the template.)

- [x] **Step 2: Update the three command groups and test files, delete sources, gate, commit**

```bash
git rm src/rhapsody_cli/actions/attribute_action.py src/rhapsody_cli/actions/operation_action.py src/rhapsody_cli/actions/port_action.py
pytest tests/unit -q && ruff check src/ tests/ && black --check src/ tests/
git add -u src/rhapsody_cli/ tests/unit/actions/
git commit -m "refactor(cli): split attribute/operation/port actions into per-action modules"
```

### Task 15: Split `project_action.py` → `actions/project/`

**Files:**
- Create: `src/rhapsody_cli/actions/project/{__init__,open,list,close,new,export,importer}.py`
- Delete: `src/rhapsody_cli/actions/project_action.py`
- Modify: `src/rhapsody_cli/commands/project_command.py`, `tests/unit/actions/test_project_action.py`

- [x] **Step 1: Move classes verbatim**

`open.py` ← `ProjectOpenAction`; `list.py` ← `ProjectListAction`; `close.py` ← `ProjectCloseAction`; `new.py` ← `ProjectNewAction`; `export.py` ← `ProjectExportAction`; `importer.py` ← `ProjectImportAction` (keyword-avoiding name, same as transfer). These extend `RhapsodyContextAction` directly — import from `abstract_action` in each file.

`src/rhapsody_cli/actions/project/__init__.py`:

```python
"""Project command actions."""

from rhapsody_cli.actions.project.close import ProjectCloseAction
from rhapsody_cli.actions.project.export import ProjectExportAction
from rhapsody_cli.actions.project.importer import ProjectImportAction
from rhapsody_cli.actions.project.list import ProjectListAction
from rhapsody_cli.actions.project.new import ProjectNewAction
from rhapsody_cli.actions.project.open import ProjectOpenAction

__all__ = [
    "ProjectCloseAction",
    "ProjectExportAction",
    "ProjectImportAction",
    "ProjectListAction",
    "ProjectNewAction",
    "ProjectOpenAction",
]
```

- [x] **Step 2: Update importers, delete, gate, commit**

```bash
git rm src/rhapsody_cli/actions/project_action.py
pytest tests/unit -q && ruff check src/ tests/ && black --check src/ tests/
git add -u src/rhapsody_cli/ tests/unit/actions/test_project_action.py
git commit -m "refactor(cli): split project actions into actions/project/"
```

---

## Stage 5 — Docs

### Task 16: AGENTS.md and docs updates

**Files:**
- Modify: `AGENTS.md`
- Modify: `docs/superpowers/specs/2026-11-27-cli-command-reorg-design.md` (no — spec is frozen; instead add plan-completion note to the plan file itself)

- [x] **Step 1: Fix the CLI section of AGENTS.md**

Replace the "CLI Subcommands" boilerplate and the Architecture table's CLI row with the real surface:

```markdown
| CLI | `src/rhapsody_cli/cli/` + `commands/` + `actions/` | argparse (stdlib), "PanGu style": registry-driven root parser → `CliEntry.register()/run()` → `AbstractAction.execute()`. **Command surface:** root `connect`, `disconnect`, `status`, `version`, `export`, `import`; groups `class`, `attribute`, `operation`, `package`, `port`, `project`. Global flags `--format {table,json,csv}` and `-v` are accepted before the command only. Actions live one-per-file under `actions/<domain>/`. |
```

And replace the "CLI Subcommands" how-to with:

```markdown
## CLI Subcommands

1. Create the action class in its own file `src/rhapsody_cli/actions/<domain>/<action>.py`, inheriting `AbstractAction` (or `SessionAwareAction` / `ElementManagementAction` / `RootCommandAction`)
2. Implement `init_arguments(sub_parser)` and `execute(args)`; read `args.format` / `args.verbose` from the namespace (they are global)
3. Register it in the domain's `__init__.py` and the group's `get_actions()` in `src/rhapsody_cli/commands/`; for a brand-new ROOT command, make the class a `RootCommandAction` and add it to `build_registry()` in `cli/cli.py`
```

- [x] **Step 2: Cross-check remaining docs for stale CLI references**

Run: `grep -rn "package export\|package import\|element\b.*command\|\bio\b.*command" docs/ AGENTS.md --include="*.md" | grep -v superpowers`
Update each hit to the new surface (`rhapsody-cli export --file ... --path pkg`, etc.).

- [x] **Step 3: Full gate + commit**

```bash
pytest tests/unit -q && ruff check src/ tests/ && black --check src/ tests/
git add AGENTS.md docs/
git commit -m "docs: update CLI architecture and command surface documentation"
```

---

## Self-review checklist (completed during planning)

- **Spec coverage:** §3 dispatch → Tasks 5-6; §3.4 export/import → Task 7; §4 layout → Tasks 11-15; §5 consolidation → Tasks 3, 8-10; §6 unchanged flow → preserved by construction (SessionAwareAction untouched); §7 characterization → Tasks 1-2, intended-change flips in Task 5; §8 staging → stage mapping is 1:1; §9 risks → `importer.py` naming (Tasks 7/15), `classifier/` package rename for the `class` keyword (Task 13), worktree execution note in header.
- **Type consistency:** `register(subparsers)` / `run(namespace)` used identically in `CliEntry`, `RootCommandAction`, `AbstractCommand`; `load_json_mapping`/`write_text_file` names consistent between Task 8 tests and implementation; `ExportAction`/`ImportAction` consistent across Task 5 registry, Task 7 files, and tests.
- **Known sequencing hazard:** Task 5 depends on Task 6 step 3's inheritance change for session actions — noted inline; execute tasks in order.
