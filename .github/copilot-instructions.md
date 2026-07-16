# Copilot Instructions for rhapsody-cli

## Quick Reference

**Language:** Python 3.8+  
**Build System:** setuptools (src-layout)  
**Testing:** pytest with unit tests only (no Rhapsody installation required)  
**Quality Tools:** ruff (linting), black (formatting), mypy (type checking)  
**CLI Framework:** argparse (stdlib) with class-based command/action architecture

---

## Build & Test Commands

### Installation

```bash
pip install -e ".[dev,cli]"  # Full dev setup: required to run the full test suite (CLI tests need tabulate/rich)
pip install -e ".[dev]"      # Dev tools only (ruff/black/mypy/pytest) - tests that import tabulate/rich will fail
pip install -e ".[cli]"      # CLI runtime dependencies only
pip install -e .             # Install package only (pywin32 on Windows)
```

### Testing

```bash
pytest                                    # Run all tests (unit + integration + system)
pytest tests/unit                         # Run only unit tests (what CI runs)
pytest tests/unit/cli/                    # Run only CLI support unit tests
pytest tests/unit/models/elements/        # Run only element wrapper tests
pytest tests/unit/models/test_core.py     # Run a single test module
pytest tests/unit/models/test_core.py::TestClassName::test_method_name  # Run one test
pytest -k "test_open"                     # Run tests matching a name pattern
pytest -v                                 # Verbose output
pytest --co -q                            # List all tests without running
```

`tests/integration/` and `tests/system/` require a running, licensed Rhapsody instance (Windows only) and are skipped/not run in CI. `tests/integration/conftest.py` auto-skips the whole session if it can't attach to Rhapsody with an open project.

### Linting & Formatting

```bash
ruff check src/ tests/      # Run linter
ruff check src/ tests/ --fix # Auto-fix issues
black --check src/ tests/   # Check formatting
black src/ tests/           # Auto-format
mypy src/ tests/            # Type checking (strict mode, python_version 3.9)
```

### Running Everything

```bash
ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit
```

Note: CI (`.github/workflows/python-package.yml`) only runs `mypy` for Python < 3.10, and runs `pytest tests/unit -v --cov=src/rhapsody_cli --cov-report=xml` (not the integration/system suites) across Python 3.8–3.13 on `windows-latest`.

---

## Git Workflow

### Mandatory Rules

**1. Do NOT add Copilot as co-author**

Never include `Co-authored-by: Copilot` in commits. Each commit must be authored by the human developer only:

```bash
# ✅ CORRECT: Human-authored only
git commit -m "feat: add new model element"

# ❌ WRONG: Do not add Copilot trailer
git commit -m "feat: add new model element

Co-authored-by: Copilot <...@users.noreply.github.com>"
```

**2. All changes go to feature branches, NEVER directly to main**

Always work on a feature branch. Main is reserved for tested, production-ready code:

```bash
# ✅ CORRECT: Work on feature branch
git checkout -b feature/add-new-element
# ... make changes ...
git commit -m "feat: add element wrapper for MyClass"
git push -u origin feature/add-new-element

# ❌ WRONG: Never commit directly to main
git checkout main
git commit -m "..."  # ✗ FORBIDDEN
git push origin main
```

### Feature Branch Workflow

```bash
# 1. Create and switch to feature branch
git checkout -b feature/<type>-<short-description>

# 2. Make changes, test, commit (locally on feature branch)
git add src/rhapsody_cli/models/elements/myclass.py tests/elements/test_myclass.py
git commit -m "feat: add RPMyClass element wrapper"

# 3. Push to origin
git push -u origin feature/<type>-<short-description>

# 4. Create pull request on GitHub for review
# (via gh pr create or GitHub web UI)

# 5. After PR approval and merge, delete local branch
git checkout main
git pull origin main
git branch -d feature/<type>-<short-description>
```

### Branch Naming Convention

Use kebab-case with a type prefix:

- `feature/add-element-wrapper` — New functionality
- `fix/connection-error-handling` — Bug fix
- `refactor/class-based-element` — Code reorganization
- `docs/update-guidelines` — Documentation only

---

## Architecture

### High-Level Overview

**rhapsody-cli** is a Pythonic wrapper around the IBM Rhapsody COM API. It consists of three layers:

1. **Core Model Wrapping** (`src/rhapsody_cli/models/`)
   - `src/rhapsody_cli/models/core.py` defines `AbstractRPModelElement` (shared utilities: `call_com()`, `wrap()`, `register_wrapper()`, the `_WRAPPER_REGISTRY`) and `RPModelElement`/`RPCollection`/`RPUnit`
   - Element subclasses live under `src/rhapsody_cli/models/elements/` (see subpackages `classifiers/`, `containment/`, `relations/`, plus `model_diagrams.py`, `model_requirements.py`, `model_variables.py`, `model_misc.py`) and mirror the Rhapsody Java API (e.g. `RPClass`, `RPPackage`, `RPProject`, `RPActor`)
   - Wrapper registry pattern: each element module calls `AbstractRPModelElement.register_wrapper(meta_class_str, WrapperClass)` at import time; `AbstractRPModelElement.wrap(com_obj)` dispatches a raw COM object to the correct subclass via `getMetaClass()`
   - `AbstractRPModelElement.call_com(lambda: ...)` translates `pywintypes.com_error` into `RhapsodyRuntimeException`

2. **Application Entry Point** (`src/rhapsody_cli/application.py`)
   - `RhapsodyApplication` wraps `IRPApplication` (Prog ID `Rhapsody2.Application.1`)
   - Supports three connection modes: `attach()` (existing instance via `GetActiveObject`), `launch()` (new instance via `Dispatch`), `connect()` (try attach then launch)

3. **CLI Layer** (`src/rhapsody_cli/cli/` + `src/rhapsody_cli/commands/` + `src/rhapsody_cli/actions/`)
   - argparse-based (stdlib) CLI using a class-based command/action architecture — **not** Click, despite some older docs/specs mentioning Click (migration is complete)
   - `cli/main.py` → `cli/cli.py` `main()` dispatches on the first argv token (`element` | `package` | `project`) to the matching command group class
   - Command groups (`ElementCommand`, `ProjectCommand`, `PackageCommand`) each own a set of `AbstractAction` subcommands, returned from `get_actions()`
   - Each action (`actions/element_action.py`, `actions/package_action.py`, `actions/project_action.py`) registers its own argparse subparser (`init_arguments`) and owns its execution (`execute`)
   - `cli/path_resolver.py` — `PathResolver` navigates `/`- or `\`-separated element paths from a root/container
   - `cli/context.py` — `RhapsodyContext` manages session state (`app`, `project`, `output_format`)
   - `cli/formatters.py` — `OutputFormatter` handles table/JSON/CSV output

### Key Data Flow

```
User CLI Input
    ↓
CLI Command (class-based) → RhapsodyContext → RhapsodyApplication
    ↓
COM Call wrapped in call_com()
    ↓
RPModelElement (wrapper class from registry)
    ↓
Formatted Output (table/JSON/CSV)
```

### API Mirroring

Method names and class hierarchy **exactly mirror** the Rhapsody Java API (`com.telelogic.rhapsody.core`):
- Java: `com.telelogic.rhapsody.core.IRPClass` → Python: `rhapsody_cli.models.elements.classifiers.model_class.RPClass`
- Java: `getNestedElements()` → Python: `getNestedElements()`
- COM errors become `RhapsodyRuntimeException` for consistent error handling

---

## Key Conventions

### Test-Driven Development (TDD)

**Mandatory:** All code changes must follow strict TDD:

1. Write tests **BEFORE** implementation
2. Watch tests fail (red phase)
3. Write minimal code to pass (green phase)
4. Refactor while keeping tests passing (refactor phase)

**Coverage targets:** 80% minimum, 90%+ preferred. See `docs/CODE_GUIDELINES.md` for full details.

### Class-Based Architecture

**Mandatory for CLI:** All CLI commands must be class-based (not function-based with decorators):

```python
# ✅ CORRECT: Class-based action (argparse)
class ElementAddAction(ElementManagementAction):
    def __init__(self) -> None:
        super().__init__(command_id="add")

    def init_arguments(self, sub_parser) -> None:
        add_parser = sub_parser.add_parser("add", help="Add a new element")
        add_parser.add_argument("--type", required=True)
        add_parser.add_argument("--name", required=True)

    def execute(self, args: argparse.Namespace) -> None:
        # Business logic here
        ...

# Command groups inherit from AbstractCommand and register actions in get_actions():
class ElementCommand(AbstractCommand):
    def __init__(self, args: List[str]) -> None:
        super().__init__("element", args)

    def get_actions(self) -> List[AbstractAction]:
        return [ElementAddAction(), ElementViewAction(), ElementQueryAction(), ElementDeleteAction()]

# ❌ WRONG: Function-based with decorators (Click style) — not used in this project
```

### Wrapper Registry Pattern

New element types must register at module import time:

```python
# src/rhapsody_cli/models/elements/containment/model_myclass.py
from rhapsody_cli.models.core import AbstractRPModelElement, RPModelElement

class RPMyClass(RPModelElement):
    """Wraps IRPMyClass."""
    pass

AbstractRPModelElement.register_wrapper("MyClass", RPMyClass)
```

Then add the import to the relevant subpackage's `__init__.py` (e.g. `models/elements/containment/__init__.py`) so registration fires on package import. This enables automatic dispatch: `AbstractRPModelElement.wrap(com_object)` returns the correct subclass based on `getMetaClass()`.

### Error Handling

- Use `call_com(lambda: ...)` to wrap all COM calls
- Catch `RhapsodyConnectionError` for connection issues
- Catch `RhapsodyRuntimeException` for COM API failures
- CLI actions use `sys.exit(1)` for errors after logging via `_handle_connection_error` / `_handle_execution_error`

```python
try:
    ctx.connect("attach")
except RhapsodyConnectionError as e:
    self._handle_connection_error(e)
    sys.exit(1)
```

### Deleting Elements

Call the wrapped `element.deleteFromProject()` method — never call `element._com.delete()` directly. The raw COM object does not expose a `delete()` method; using `_com` directly bypasses the wrapper and raises `AttributeError`.

### Type Annotations

- **`from __future__ import annotations` is FORBIDDEN** — do not add it to any file, and remove it if found. Use string-quoted forward refs (`'RhapsodyContext'`) or `TYPE_CHECKING` imports instead. This was deliberately fixed project-wide; see `docs/CODE_GUIDELINES.md`.
- **mypy strict mode** (config targets `python_version = "3.9"`): all functions must have return type annotations (`-> None`, `-> int`, etc.).
- **COM API:** Use `# type: ignore[attr-defined]` sparingly for `win32com`/`pywintypes` (they lack stubs; `pyproject.toml` overrides already ignore missing imports for those modules).

```python
def open_project(path: str) -> None:  # ✅ Required return annotation
    com_obj = AbstractRPModelElement.call_com(lambda: self._com.openProject(path))  # ✅ COM call wrapped
```

### Testing with Fakes

All unit tests use fake COM objects from `tests/unit/models/fakes.py`. Never use real COM calls in tests:

```python
from tests.unit.models.fakes import make_fake_element, make_fake_collection

# Create fake Class element with name
fake_class = make_fake_element("Class", getName="MyClass")

# Create fake collection
fake_items = make_fake_collection([fake_class])
```

No Rhapsody installation or license is required to run `tests/unit/`.

### Code Layout

```
src/rhapsody_cli/
├── __init__.py                    # Public API exports
├── application.py                 # RhapsodyApplication entry point
├── exceptions/core.py             # RhapsodyConnectionError, RhapsodyRuntimeException
├── models/
│   ├── core.py                    # AbstractRPModelElement, RPModelElement, RPCollection, RPUnit, wrap(), call_com(), registry
│   └── elements/
│       ├── classifiers/           # model_class.py, model_actor.py, model_classifier.py, model_usecase.py, ...
│       ├── containment/           # model_package.py, model_project.py, model_component.py, model_node.py, ...
│       ├── relations/             # relation/association/dependency element wrappers
│       ├── model_diagrams.py, model_requirements.py, model_variables.py, model_misc.py
├── commands/                      # ElementCommand, ProjectCommand, PackageCommand (argparse, class-based)
├── actions/                       # element_action.py, package_action.py, project_action.py (Add/View/Query/Delete actions)
└── cli/
    ├── main.py, cli.py            # Entry point + dispatcher
    ├── context.py                 # RhapsodyContext (state management)
    ├── path_resolver.py           # PathResolver (navigate "/" or "\" element paths)
    ├── formatters.py              # OutputFormatter (table/JSON/CSV)
    └── logging_config.py          # CliLoggingConfigurator

tests/
├── unit/                          # Mocked COM, no Rhapsody needed — this is what CI runs
│   ├── models/fakes.py            # Fake COM objects (make_fake_element, make_fake_collection)
│   ├── models/test_core.py, models/elements/  # Core + element wrapper tests
│   ├── cli/, commands/, actions/, exceptions/
├── integration/                   # Requires live, licensed Rhapsody instance (Windows); auto-skips if unavailable
└── system/                        # End-to-end subprocess tests
```

### GitHub Actions CI/CD

- **CI:** `.github/workflows/python-package.yml` runs on `windows-latest` across Python 3.8–3.13. Steps: `ruff check src/ tests/`, `black --check src/ tests/`, `mypy src/ tests/`, then `pytest tests/unit -v --cov=src/rhapsody_cli --cov-report=xml`. Integration/system tests are **not** run in CI (they need a live Rhapsody instance).
- **CD:** `.github/workflows/python-publish.yml` auto-publishes to PyPI on GitHub release.

---

## When Adding Features

1. **Read `docs/CODE_GUIDELINES.md`** — comprehensive TDD and architecture patterns
2. **Write tests first** — then implementation
3. **Use `call_com(lambda: ...)`** for all COM calls
4. **Register new element wrappers** in the wrapper registry
5. **Class-based CLI actions** — never function-based or Click-decorator-based
6. **Type annotations on all functions** — mypy strict mode enforces this
7. **Run quality gates:** `ruff check`, `black --check`, `mypy`, `pytest`

---

## Common Tasks

### Add a new element wrapper

1. Create `src/rhapsody_cli/models/elements/<subpackage>/model_myclass.py` (subpackage = `classifiers`, `containment`, `relations`, etc., based on what the element represents)
2. Define `RPMyClass(RPModelElement)` with method mirrors
3. Call `AbstractRPModelElement.register_wrapper("MyClass", RPMyClass)` at module level
4. Write tests in `tests/unit/models/elements/test_myclass.py` with fakes from `tests/unit/models/fakes.py`
5. Add the import to the subpackage's `__init__.py` so registration fires on import

### Add a new CLI command

1. Write tests first in appropriate tests/unit/cli/ or tests/unit/commands/ module
2. Create an action class inheriting from AbstractAction (or RhapsodyContextAction / ElementManagementAction)
3. Implement init_arguments() to register the subparser and execute() for business logic
4. Register the action in the appropriate command group's get_actions() (`ElementCommand`, `PackageCommand`, or `ProjectCommand`)
5. Verify all unit tests pass

### Fix a type checking error

mypy strict mode can be strict. Common patterns:

```python
# ✅ Optional handling
if value is not None:
    use_value(value)

# ✅ Type narrowing
if isinstance(obj, MyClass):
    obj.my_method()

# ✅ Explicit cast when necessary
from typing import cast
result = cast(str, com_call())
```

---

## References

- **Design & Architecture:** `docs/superpowers/specs/2026-07-06-rhapsody-cli-com-api-design.md`
- **Code Guidelines (TDD/Classes):** `docs/CODE_GUIDELINES.md`
- **Rhapsody Java API:** https://www.ibm.com/docs/en/rhapsody (method/class reference)
- **argparse documentation:** https://docs.python.org/3/library/argparse.html
