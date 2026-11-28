# AGENTS.md

## Project

Pythonic wrapper around the IBM Rhapsody COM API. Python member names use snake_case: COM properties become Python properties (e.g. `name`), while COM methods remain methods (e.g. `find_nested_element`). Internal COM calls preserve the camelCase API (`self._com.methodName(...)`). Windows-only for runtime (COM); tests run anywhere via fakes.

## Architecture (3 layers, bottom-up)

| Layer | Path | Purpose |
|-------|------|---------|
| Models | `src/rhapsody_cli/models/` | COM wrappers for 97+ element types. `elements/` has 13 domain subpackages (`activity/`, `classifiers/`, `common/`, `containment/`, `diagrams/`, `graphics/`, `interactions/`, `relations/`, `requirements/`, `statemachine/`, `templates/`, `values/`, `variables/`). `support/` wraps codegen/IDE/file APIs. `core.py` = `ComHelper`, `IRPModelElement`, `IRPCollection`, `RPUnit`. |
| Application | `src/rhapsody_cli/application.py` | `RhapsodyApplication` — attach/launch/connect to Rhapsody. Prog ID: `Rhapsody2.Application.1`. |
| CLI | `src/rhapsody_cli/cli/` + `commands/` + `actions/` | argparse (stdlib), "PanGu style": registry-driven root parser → `CliEntry.register()/run()` → `AbstractAction.execute()`. **Root commands:** `connect`, `disconnect`, `status`, `version`, `export`, `import`; **groups:** `class`, `attribute`, `operation`, `package`, `port`, `project`. Global flags `--format {table,json,csv}` / `-v` are accepted **before** the command only. Actions live one-per-file under `actions/<domain>/`. |

## COM Wrapping Rules (critical)

- The generated pywin32 interface is authoritative: the member name and method/property shape for every COM call come from `docs/reports/pywin32_authority.json`. COM names (`BinaryID`, `isAbstract`, `getIsFinal`) are **string arguments only**, never Python identifiers.
- COM helpers are classmethods on `ComHelper` in `models/core.py`: `call_com()`, `get_com_property()`, `set_com_property()` (inherited by `IRPModelElement` and used by element wrappers). Legacy fallback pair `_get_method_or_property()` / `_set_method_or_property()` remains only in wrappers not yet migrated.
- **No runtime name probing or fallback**: never "try the Java-style method name first". A wrapper calls exactly one pywin32-exposed member.
- **Python shape follows the pywin32 catalog**: expose catalog properties as `@property` (add a setter only for writable properties) and catalog methods as methods. Do not retain duplicate `get_`/`set_` aliases for properties.
- All method-shaped COM calls → `call_com(lambda: self._com.methodName(...))` (translates `com_error` → `RhapsodyRuntimeException`). On elements, use `self.call_com(...)` (classmethod inherited from `ComHelper`). Parameterized/multi-arg calls MUST use this form.
- Property-shaped members → `self.get_com_property(self._com, "propName")` / `self.set_com_property(self._com, "propName", value)` (read/write exactly the authoritative name).
- Return wrapped element → `self.wrap(...)` or specific wrapper constructor
- Return collection → `IRPCollection(self.call_com(...))`
- Migration is per-class via rhapsody-sync runs: each synced class's own methods drop the legacy helpers; the legacy pair is deleted after the last class migrates.
- **Wrapper classes are named after the Java interface** (`IRPClass`, `IRPModelElement`, `IRPCollection`, ...) — never the legacy `RP*` facade name. The class's module, mirrored test modules, and per-class requirement/RST documents use the same Java-derived snake_case (`irp_class.py`, `test_irp_class.py`, `irp_class.md`). Each sync run renames its class; the COM-helper infrastructure base (not a Java interface) has been renamed to `ComHelper`.

## Testing

```bash
pip install -e ".[dev,cli]"          # full setup (CLI tests need tabulate/rich)
pytest tests/unit/                    # unit tests only — what CI runs (not `pytest` alone, which also runs integration/system)
pytest tests/unit/models/test_core.py # single file
pytest -k "test_foo"                  # pattern match
```

- All unit tests use fakes from `tests/unit/models/fakes.py` (`make_fake_element`, `make_fake_collection`). **Never real COM in tests.**
- `tests/integration/` and `tests/system/` require Windows + Rhapsody — auto-skipped in CI.
- See `CLAUDE.md` for full test structure and integration test details.

## TDD Requirement

Write failing test first, then implement. Coverage target 80% min, 90%+ preferred.

## Integration Test Scope Rules

Each file under `tests/integration/models/elements/` targets **exactly one wrapper class** and asserts only on methods that class **owns**. Parent-class methods are **setup only**, never the subject of an assertion.

**Why:** `IRPModelElement` members (`name`, `meta_class`, `owner`, `delete_from_project`) and `RPClassifier` methods (`add_attribute`, `add_operation`, `add_relation_to`, `add_statechart`, …) are already covered in `test_core.py` and `test_model_classifier.py`. Re-testing them in a child's file is noise and hides the child's own (often untested) methods.

**Rules:**

1. Before writing a test, read the model module's checklist. Assert only on methods **not** marked `[inherited]`.
2. Build the fixture with parent methods; the assertion block calls only own-class methods. Reference pattern: `test_model_association_class.py` — uses `add_relation_to` (an `RPClassifier` method) to build the fixture, then asserts on `RPAssociationClass`'s own four methods (`get_end1`/`get_end2`/`get_is_class`/`set_is_class`).
3. If the class **redefines** an inherited method with a different signature/return type (e.g. `RPActor.get_is_behavior_overriden()` → `bool` vs `RPClass.get_is_behavior_overriden()` → `int`; `RPActor.update_contained_diagrams_on_server()` no-arg vs `RPClass` takes `int`), the test must assert the **child's** contract so it would fail if it resolved to the parent's override (e.g. `assert x is False`, not `assert x == 0`).
4. Testing an abstract base via a concrete subclass is fine (e.g. `RPInterfaceItem` via `RPOperation`) — but assert the base's methods, not the subclass's overrides.
5. Pure creation/navigation smoke tests (only `name`/`meta_class`/`owner` + a parent `add_*`) belong in `test_core.py`, not a child element file.

Before a live integration test switches projects (for example, calls `create_new_project()` or `open_project()`), call `rhapsody_app.save_all()` immediately before the switch, after making any intended model changes. Rhapsody can otherwise display a modal “Save changes?” prompt that blocks COM automation. Keep this explicit in the test so future project-switching cases do not hang on a GUI dialog.

For non-visual live integration runs, use `pytest tests/integration --rhapsody-hidden-ui`. The opt-in flag connects with `show_gui=False`, then explicitly calls `set_hidden_ui(True)`; the integration fixture does not bring the window to the foreground. This is session-wide and must not be used for tests that assert visible diagram rendering. The `test_irp_application.py` module also hides the UI by default with a file-local fixture and restores the prior state after the module; tests that explicitly show the window restore the hidden state they received. This file-local setting takes effect after the shared session app is obtained, so the option is required to suppress the launch window itself. Neither mechanism guarantees every COM operation is non-modal; verify the specific case and record any remaining prompt as a blocker.

**Offline verification (no Rhapsody available):** `pytest <file> --collect-only -q` proves imports/syntax; live execution is CI-only on `windows-latest`. See `docs/superpowers/plans/2026-08-02-integration-test-own-methods-focus.md` for the audit + cleanup pass that established these rules.

## Quality Gate

```bash
ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit
```

- ruff: E, F, I, UP, B, N rule sets. Black: line-length 200, py38 target.
- mypy strict mode (py3.9 target). `win32com.*` / `pywintypes`: `ignore_missing_imports`.
- CI runs `mypy` only on Python < 3.10 (pattern-matching syntax issue in pytest on 3.10+).
- CI runs full gate on `windows-latest` across Python 3.8–3.13. Codecov upload.

## Coding Guidelines

See [docs/CODE_GUIDELINES.md](docs/CODE_GUIDELINES.md) for detailed coding standards including:

- Naming conventions (UPPERCASE constants, snake_case methods)
- Import style (full package path, no relative imports)
- Function definition style (arguments on one line)
- Type annotations (**no `Any` type** — use accurate concrete types)
- TDD methodology and coverage targets
- Class-based architecture patterns
- CLI command patterns

## Forbidden

- `Any` type in type annotations (use accurate concrete types, `Union`, `TypedDict`, or `object` instead — see [docs/CODE_GUIDELINES.md](docs/CODE_GUIDELINES.md#type-annotations))
- `element._com.delete()` (use `element.delete_from_project()` instead)
- `Co-authored-by: Copilot` or any AI attribution
- Direct commits to `main` — always use `feature/`, `fix/`, `refactor/`, `docs/` branches

## Element Wrappers

**Read `docs/java_api` (HTML dir) first** — javadoc-generated, documents Java model classes with exact method names/signatures. Authoritative for "does this method exist on this IRP* interface". Also consult `docs/java_api/rational_rhapsody_api_getting_started.pdf` for API workflows and model-construction examples; it is supplementary and does not override JavaDoc or `docs/reports/pywin32_authority.json` for exact COM members and shapes.

1. Create `src/rhapsody_cli/models/elements/<subpackage>/model_<class>.py`
2. Subclass `IRPModelElement`, add methods using snake_case names mirroring Java API
3. `IRPModelElement.register_wrapper("MetaClass", RPMyClass)` at module level
4. Add import in the subpackage's `__init__.py`
5. Write tests using `make_fake_element` / `make_fake_collection` (mock exact Java method names from `docs/java_api` HTML docs)

## CLI Subcommands

1. Create the action class in its own file `src/rhapsody_cli/actions/<domain>/<action>.py`, inheriting `AbstractAction` (or `SessionAwareAction` / `ElementManagementAction` / `RootCommandAction` for root commands)
2. Implement `init_arguments(sub_parser)` and `execute(args)`; read `args.format` / `args.verbose` from the namespace (they are global flags)
3. Export it from the domain's `__init__.py` and list it in the group's `get_actions()` in `src/rhapsody_cli/commands/`
4. For a brand-new ROOT command, make the class a `RootCommandAction` and add it to `build_registry()` in `src/rhapsody_cli/cli/cli.py`
