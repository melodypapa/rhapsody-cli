# CLI Simplification: Active vs Suspended Commands and Individual export/import

- **Date:** 2026-11-19
- **Status:** Approved design (brainstorming session, pending implementation plan)
- **Scope:** `src/rhapsody_cli/cli/`, `src/rhapsody_cli/commands/`, CLI docs, CLI tests

## Problem

The CLI exposes 10 command groups; several (`attribute`, `operation`, `port`) are
rarely used and not fully proven against live Rhapsody. The surface should shrink
to the frequently used commands, made 100% working, while keeping suspended
implementations in the codebase. Additionally, model import/export should be
individual top-level commands at package granularity (exporting the root package
covers the whole model), not subcommands of `project`/`package`.

## Goals

1. Keep `connect`, `disconnect`, `status`, `version`, `project`, `package`, `class`
   active and verified working end-to-end against a live Rhapsody instance.
2. Suspend `attribute`, `operation`, `port` with an explicit notice; retain their
   implementations and tests unchanged.
3. Add individual `export` and `import` single-level commands (package-level
   granularity, `--path` defaults to project root).
4. Update README, user guide, CLAUDE.md, and AGENTS.md to match the new surface.

## Non-Goals

- Deleting or rewriting any action/command/model implementation.
- Project-level export/import (`ProjectExportAction` / `ProjectImportAction`
  stay in the codebase, unwired).
- Config- or env-var-driven command enablement (re-enablement is a one-line
  code change).

## Target Command Surface

| Tier | Commands |
| ------ | ---------- |
| Single-level (active) | `connect`, `disconnect`, `status`, `version`, `export`, `import` |
| Two-level (active) | `project` (`new`, `open`, `list`, `close`), `package` (`create`, `view`, `list`, `update`, `delete`), `class` (`create`, `view`, `list`, `link`, `update`, `delete`) |
| Suspended | `attribute`, `operation`, `port` |

## Design

### 1. Suspension mechanics — `src/rhapsody_cli/cli/cli.py`

Module-level constant:

```python
SUSPENDED_COMMANDS = {"attribute", "operation", "port"}
```

`main()` check order: `--help`/`-h` → suspended check → session commands →
two-level dispatch. A suspended command prints to stderr and exits 2
(same code as usage errors):

```text
rhapsody-cli: command 'attribute' is temporarily suspended.
Active commands: connect, disconnect, status, version, export, import, project, package, class
```

`_usage()` renders three sections:

```text
Single-Level Commands:
  connect / disconnect / status / version / export / import

Two-Level Commands:
  project / package / class

Suspended Commands (temporarily disabled, implementations retained):
  attribute / operation / port
```

Unknown commands keep the existing `_usage(f"Unknown command: {name}")` path.

### 2. Individual `export` / `import` commands

New single-level commands following the existing session-command pattern in
`cli.py` (inline parser, action instance, `execute(parsed_args)`):

```bash
rhapsody-cli export --file model.yaml              # root package of active project
rhapsody-cli export --path Sensors --file sensors.yaml
rhapsody-cli import --file model.yaml              # imports into root package
rhapsody-cli import --path Sensors --file model.yaml
```

Implementation reuses the existing action classes unchanged:

- `export` → `PackageExportAction` (`--path` optional, default root; `--file` required)
- `import` → `PackageImportAction` (same argument shape)

Both are safe outside the two-level flow: `output_format` defaults to
`"table"` in `RhapsodyContextAction.__init__`, and `SessionAwareAction.execute`
enforces a valid session before running (consistent with other element
commands). Export/import produce YAML files, so no `--format` handling is
needed.

`project` and `package` groups lose their `export`/`import` subcommands:

- `ProjectCommand.get_actions()` → `open`, `list`, `close`, `new` only.
  `ProjectExportAction`/`ProjectImportAction` remain in `project_action.py`,
  unwired (implementation retained per the suspend-but-keep rule).
- `PackageCommand.get_actions()` → `create`, `view`, `list`, `update`, `delete`
  only. `PackageExportAction`/`PackageImportAction` stay in
  `package_action.py` — they now power the top-level commands (no dead code).

### 3. Untouched code

`actions/attribute_action.py`, `operation_action.py`, `port_action.py`, their
command classes, and the models layer are unchanged. All existing unit tests
for suspended implementations keep passing.

### 4. Docs

- **README.md** — CLI section: session/project/package/class examples updated
  for the new surface; `export`/`import` shown with the new syntax;
  `attribute`/`operation`/`port` moved to a short "Suspended commands" note.
- **docs/user_guide/cli_tools.rst** — same split.
- **CLAUDE.md** — stale `element`/`io` references and command-group lists
  corrected to active vs suspended reality.
- **AGENTS.md** — "Actual command groups" line updated.

### 5. Error handling

Exit codes: `0` success; `2` usage errors and suspended-command notices;
`1` runtime failures; `130` interrupt (unchanged). Connection/session errors
keep the existing `RhapsodyConnectionError`/`CliExecutionError` messaging from
the reused actions.

## Testing

TDD: write failing tests first, then implement.

- **New unit tests** (`tests/unit/cli/test_cli.py` or a new sibling module):
  suspended command exits 2 with the notice on stderr; `_usage()` renders the
  three sections; `export`/`import` single-level dispatch invokes the reused
  actions with parsed `--path`/`--file`.
- **Updated unit tests**: `tests/unit/commands/test_project_command.py` and
  `tests/unit/commands/test_package_command.py` drop export/import subcommand
  cases.
- **Untouched**: action-level tests for `PackageExportAction`,
  `PackageImportAction`, `ProjectExportAction`, `ProjectImportAction`, and all
  suspended-action tests.
- **Quality gate**: `ruff check src/ tests/ && black --check src/ tests/ &&
  mypy src/ tests/ && pytest tests/unit`.

## Live Smoke Verification (Windows + real Rhapsody)

Fixture: scratch copy of `demos/test_project/TestProject.rpy`; never touch real
models; clean up afterward. Run every kept subcommand at least once, exercising
`--format table/json` where supported:

```text
version → status → connect
project new / open / list / close            (scratch project)
package create / view / list / update / delete
class create / view / list / link / update / delete
export (root + nested package) → import (back into fresh package)
status → disconnect
```

Any bug found: failing unit test first, fix, re-run the failed smoke step.
Results recorded as a checklist in the implementation plan.

## Re-enablement Path

Remove a name from `SUSPENDED_COMMANDS` and its line from the usage text;
re-add the command class to the dispatch or `get_actions()`. No other changes
required because implementations and tests never left.
