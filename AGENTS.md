# AGENTS.md

## Project

Pythonic wrapper around the IBM Rhapsody COM API. All method names use snake_case (e.g. `get_name`, `set_name`). Internal COM calls preserve the camelCase API (`self._com.methodName(...)`). Windows-only for runtime (COM); tests run anywhere via fakes.

## Architecture (3 layers, bottom-up)

| Layer | Path | Purpose |
|-------|------|---------|
| Models | `src/rhapsody_cli/models/` | COM wrappers for 97+ element types. `elements/` has 13 domain subpackages (`activity/`, `classifiers/`, `common/`, `containment/`, `diagrams/`, `graphics/`, `interactions/`, `relations/`, `requirements/`, `statemachine/`, `templates/`, `values/`, `variables/`). `support/` wraps codegen/IDE/file APIs. `core.py` = `AbstractRPModelElement`, `RPModelElement`, `RPCollection`, `RPUnit`. |
| Application | `src/rhapsody_cli/application.py` | `RhapsodyApplication` — attach/launch/connect to Rhapsody. Prog ID: `Rhapsody2.Application.1`. |
| CLI | `src/rhapsody_cli/cli/` + `commands/` + `actions/` | argparse (stdlib), "PanGu style": `AbstractCommand` → `AbstractAction`. Dispatch: `main()` → `AbstractCommand.execute()` → `AbstractAction.execute()`. **Actual command groups:** `class`, `attribute`, `operation`, `package`, `port`, `project` (not `element`/`io` — older docs are stale). |

## COM Wrapping Rules (critical)

- Standalone COM utilities in `com_utils.py`: `call_com()`, `_get_method_or_property()`, `_set_method_or_property()`. Used by both `RhapsodyApplication` and element wrappers.
- All COM calls → `call_com(lambda: self._com.methodName(...))` (translates `com_error` → `RhapsodyRuntimeException`). On elements, use `self.call_com(...)` (classmethod on `AbstractRPModelElement` forwards to `com_utils.call_com`).
- No-arg getters → `_get_method_or_property(self._com, "getX", "x")` (prefers method, falls back to property; strings are COM identifiers, not Python names)
- Parameterized getters → MUST use `call_com` directly (`_get_method_or_property` drops extra args)
- Single-arg setters → `_set_method_or_property(self._com, "setX", "x", value)`
- Multi-arg setters → MUST use `call_com` directly
- Return wrapped element → `AbstractRPModelElement.wrap(...)` or specific wrapper constructor
- Return collection → `RPCollection(self.call_com(...))`

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

**Why:** `RPModelElement` methods (`get_name`, `get_meta_class`, `get_owner`, `delete_from_project`) and `RPClassifier` methods (`add_attribute`, `add_operation`, `add_relation_to`, `add_statechart`, …) are already covered in `test_core.py` and `test_model_classifier.py`. Re-testing them in a child's file is noise and hides the child's own (often untested) methods.

**Rules:**

1. Before writing a test, read the model module's checklist. Assert only on methods **not** marked `[inherited]`.
2. Build the fixture with parent methods; the assertion block calls only own-class methods. Reference pattern: `test_model_association_class.py` — uses `add_relation_to` (an `RPClassifier` method) to build the fixture, then asserts on `RPAssociationClass`'s own four methods (`get_end1`/`get_end2`/`get_is_class`/`set_is_class`).
3. If the class **redefines** an inherited method with a different signature/return type (e.g. `RPActor.get_is_behavior_overriden()` → `bool` vs `RPClass.get_is_behavior_overriden()` → `int`; `RPActor.update_contained_diagrams_on_server()` no-arg vs `RPClass` takes `int`), the test must assert the **child's** contract so it would fail if it resolved to the parent's override (e.g. `assert x is False`, not `assert x == 0`).
4. Testing an abstract base via a concrete subclass is fine (e.g. `RPInterfaceItem` via `RPOperation`) — but assert the base's methods, not the subclass's overrides.
5. Pure creation/navigation smoke tests (only `get_name`/`get_meta_class`/`get_owner` + a parent `add_*`) belong in `test_core.py`, not a child element file.

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

- `from __future__ import annotations` (use string-quoted forward refs or `TYPE_CHECKING` imports instead)
- `Any` type in type annotations (use accurate concrete types, `Union`, `TypedDict`, or `object` instead — see [docs/CODE_GUIDELINES.md](docs/CODE_GUIDELINES.md#type-annotations))
- `element._com.delete()` (use `element.delete_from_project()` instead)
- `Co-authored-by: Copilot` or any AI attribution
- Direct commits to `main` — always use `feature/`, `fix/`, `refactor/`, `docs/` branches

## Element Wrappers

**Read `docs/java_api` (HTML dir) first** — javadoc-generated, documents Java model classes with exact method names/signatures. Authoritative for "does this method exist on this IRP* interface".

1. Create `src/rhapsody_cli/models/elements/<subpackage>/model_<class>.py`
2. Subclass `RPModelElement`, add methods using snake_case names mirroring Java API
3. `AbstractRPModelElement.register_wrapper("MetaClass", RPMyClass)` at module level
4. Add import in the subpackage's `__init__.py`
5. Write tests using `make_fake_element` / `make_fake_collection` (mock exact Java method names from `docs/java_api` HTML docs)

## CLI Subcommands

1. Create action class in `src/rhapsody_cli/actions/` inheriting `AbstractAction` (or `RhapsodyContextAction` / `ElementManagementAction`)
2. Implement `init_arguments(sub_parser)` and `execute(args)`
3. Register action in the appropriate command group's `get_actions()` method in `src/rhapsody_cli/commands/`
4. Wire the command group in `src/rhapsody_cli/cli/cli.py::main()`
