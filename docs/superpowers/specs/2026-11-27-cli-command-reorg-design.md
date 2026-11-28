# CLI Command Reorganization — Design

- **Date:** 2026-11-27
- **Status:** Approved design (pending implementation plan)
- **Scope:** `src/rhapsody_cli/cli/`, `src/rhapsody_cli/commands/`, `src/rhapsody_cli/actions/`, their unit tests, and the CLI-related docs (AGENTS.md)
- **Decisions locked with Ray (2026-11-27):** in-place reorg (keep argparse + PanGu style); consolidate flag semantics (`--format`/`-v` strictly global); one action class per file; characterize-then-refactor testing; root-parser registry dispatch; promote `export`/`import` to root commands as a clean move (no deprecation alias).

## 1. Current state and problems

PanGu-style flow today: `main()` → `AbstractCommand.execute()` → `AbstractAction.execute()`.

| Problem | Evidence |
|---|---|
| Hand-rolled dispatch | `cli/cli.py::main()` (158 lines): if/elif chains for 6 command groups plus 4 single-level commands, each single-level command building an inline `argparse` parser; `-v`/`--format` found by string-scanning raw argv; `_usage()` hand-writes help text argparse can generate |
| Mega-files | `actions/class_action.py` (739), `package_action.py` (672), `operation_action.py` (639), `attribute_action.py` (603), `port_action.py` (573) — ~33 action classes in 5 files |
| Copy-paste helpers | `_load_json_data` (×5), `_write_to_file` (×4), `_format_output` (×5) defined per domain file even though `RhapsodyContextAction._print_formatted_output` already exists; `_set_attributes` ×5 are domain-specific subsets sharing a `name`/`description` core |
| Three-headed flag plumbing | `--format` registered globally (string-scanned, injected via `hasattr(action, "output_format")`) *and* per-subcommand on `list`/`view` (`args.format`) — two sources of truth; same for `-v` |
| Surface addition | `export`/`import` are buried as `package export`/`package import`; Ray wants them as root commands |
| Stale docs | AGENTS.md still mentions `element`/`io` command groups that do not exist |

Healthy parts kept as-is: `AbstractCommand`'s subparser-from-actions mechanism, the 6 thin command-group classes, the `AbstractAction` → `RhapsodyContextAction` → {`SessionAwareAction`, `ElementManagementAction`} hierarchy, `SessionManager` gating, `OutputFormatter`, `PathResolver`, the `CliExecutionError` exit-code funnel.

## 2. Goals

1. `main()` becomes a registry-driven ~40-line funnel: build root parser → parse → configure logging → dispatch → error funnel.
2. Every action class lives in its own small module (target: every module under ~150 lines).
3. Identical helper copies are merged into one shared home; formatting goes through the existing base-class helper.
4. `--format` and `-v` are strictly global flags (accepted before the command group; rejected after it).
5. `export` and `import` are root commands.
6. No framework migration, no command renames other than the export/import promotion, argparse stays.

## 3. Dispatch architecture

### 3.1 Root parser and registry

`cli.py` builds one root `argparse.ArgumentParser(prog="rhapsody-cli")` whose global flags come from a parent parser: `--format {table,json,csv}` (default `table`) and `-v/--verbose`. A module-level registry maps every top-level command to an entry:

```python
COMMANDS: dict[str, CliEntry]  # e.g. {"connect": ConnectAction, ..., "package": PackageCommand, "export": ExportAction, ...}
```

`CliEntry` is a minimal protocol satisfied by both shapes:

- `register(subparsers) -> None` — creates its subparser and registers arguments/actions under it.
- `run(namespace) -> None` — executes using values from the parsed namespace.

Domain groups (`AbstractCommand` subclasses) implement `register()` by adding their subparser and delegating to their actions' existing `init_arguments()`; `run()` resolves the chosen action by `command_id` exactly as today. Single-level commands (`connect`, `disconnect`, `status`, `version`, `export`, `import`) are `AbstractAction` subclasses whose `init_arguments()` gains the parser-creation duty their inline copies in `main()` used to have.

### 3.2 Flag semantics (consolidated)

- `--format` and `-v` exist **only** on the root parser. Argparse propagates root defaults into sub-namespaces, so actions read `args.format` / `args.verbose` from the same namespace — the `hasattr(action, "output_format")` injection and the argv string-scanning are deleted.
- Per-subcommand `--format` arguments on `list`/`view` are removed.
- `rhapsody-cli package list --format json` becomes an argparse "unrecognized arguments" error (exit 2). The supported form is `rhapsody-cli --format json package list`.

### 3.3 `main()` after

```python
def main() -> None:
    parser = build_root_parser(COMMANDS)
    namespace = parser.parse_args()
    CliLoggingConfigurator(verbose=namespace.verbose).configure()
    try:
        namespace.entry.run(namespace)
    except KeyboardInterrupt:
        print("\nInterrupted"); sys.exit(130)
    except CliExecutionError as e:
        logger.error(str(e)); sys.exit(e.exit_code)
    except Exception as e:
        logger.error("Command failed: %s", e); sys.exit(1)
```

The hand-written `_usage()` is deleted; `rhapsody-cli --help` and per-command `--help` are argparse-generated, with a one-line `help=` per registry entry. Exit codes preserved: argparse usage errors → 2, `CliExecutionError.exit_code`, `KeyboardInterrupt` → 130, generic → 1. `SystemExit` from argparse propagates unchanged.

### 3.4 Root command: `export` / `import`

`package export` / `package import` are removed and re-registered at the root (clean move, no alias):

```
rhapsody-cli export  --file out.yaml [--path pkg]      # YAML export via RhapsodyExporter/RhapsodyYaml
rhapsody-cli import  --file in.yaml  [--path target]   # YAML import via RhapsodyImporter, then save_all()
```

Semantics unchanged: session-gated (`SessionAwareAction`), `--path` resolves a package and defaults to the project root, `-v` now inherited from the global flag. Classes renamed `ExportAction` / `ImportAction` (formerly `PackageExportAction` / `PackageImportAction`, SWR_XCH_001 traceability moves with them).

## 4. File layout

```
actions/
  __init__.py
  abstract_action.py          # hierarchy unchanged
  support.py                  # NEW pure helpers (no COM, no session)
  session/
    __init__.py               # re-exports
    connect.py  disconnect.py  status.py  version.py
  package/
    __init__.py               # create.py delete.py view.py list.py update.py export... removed
                              # (export/import moved to transfer/)
  transfer/
    __init__.py
    export.py                 # ExportAction
    importer.py               # ImportAction  ("import.py" is a Python keyword — not a legal module name)
  class/  attribute/  operation/  port/
    __init__.py + one file per action class
  project/
    __init__.py + one file per action class
commands/                     # 6 groups unchanged except import updates
cli/
  cli.py                      # registry + main() + root parser builder
  formatters.py  logging_config.py  path_resolver.py  main.py   # unchanged
```

One action class per file; domain `__init__.py` re-exports so `commands/*.py` keep single-line imports. The package-resolving helper `_resolve_and_validate_package` used by export/import and package actions moves into a small `PackageResolvingMixin` beside the other shared bases in `abstract_action.py` (it resolves via `PathResolver` with meta-class `Package`, which is exactly what both consumers need). Target: every module < ~150 lines.

## 5. Shared behavior consolidation

1. **`actions/support.py`** (pure functions, trivially testable): `load_json_mapping()` merges the five `_load_json_data` copies; `write_text_file()` merges the four `_write_to_file` copies. Create-vs-update file/stdin differences stay as thin per-action glue.
2. **Output formatting**: read actions (`list`, `view`) build `(headers, rows)` and call the existing `RhapsodyContextAction._print_formatted_output`; the five per-file `_format_output` copies are deleted. `OutputFormatter` stays.
3. **Attribute application**: byte-identical logic is merged; the genuinely divergent `_set_attributes` stay domain-side. Shared appliers are factored for the common `name`/`description`/`display_name` core and the duplicated `stereotypes`/`tags` handling (package + class). Package remains the superset; no behavior change.

## 6. Error handling and session flow — unchanged

`SessionAwareAction` gating, `CliExecutionError` exit codes, Ctrl+C → 130, generic failure → 1: preserved verbatim. The `SessionAwareAction.execute` docstring quirk ("does NOT call super()") is documented as-is; redesigning the gate is out of scope.

## 7. Testing strategy — characterize first

1. **Characterization stage (before any refactor):** fake-based tests (no real COM) covering all ~33 actions at the group/entry level: dispatch routing for every command and subcommand, `table`/`json`/`csv` output strings for read actions, `not connected` error paths, exit codes for usage errors.
2. **Refactor stages** keep them green except the two intended behavior changes: `--format` position (global-only) and argparse-generated help text replacing `_usage()`'s exact strings. Those characterization tests are updated in the same commit as the change.
3. Existing unit tests move with their classes (e.g. `TestPackageExportAction` → transfer test module, retargeted at the root command position).

## 8. Staging (PR-sized, each gate-green)

| Stage | Content |
|---|---|
| 1 | Characterization tests over the current surface |
| 2 | Dispatch overhaul: root parser, registry, single-level actions, strict-global flags, `export`/`import` promotion (surface changes + their test updates land together here) |
| 3 | `support.py` extraction, output-formatting unification, shared attribute appliers |
| 4 | Per-domain file splits (pure moves, imports updated) |
| 5 | Docs: AGENTS.md stale `element`/`io` fix, new layout + registry + flag-position documentation, SWR_XCH_001 reference updates |

## 9. Risks and mitigations

- **Behavior drift during the move**: mitigated by the characterization suite (stage 1) and by keeping stages small.
- **`import` as module name**: solved by `importer.py`; the registry key is the string `"import"`, which is legal.
- **Parallel-session churn in the shared checkout**: implementation work uses dedicated branches/worktrees per stage; commits use explicit paths.
- **Downstream scripts using `package export`/`package import` or trailing `--format`**: breaking by design (clean move + flag consolidation), documented in stage 5.
