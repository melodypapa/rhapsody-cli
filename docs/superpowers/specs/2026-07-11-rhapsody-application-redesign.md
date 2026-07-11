# RhapsodyApplication Redesign — Spec

## Problem

`RhapsodyApplication` wraps `IRPApplication` (the top-level Rhapsody automation object), but it has two structural problems:

1. **Wrong dependency direction.** It calls `AbstractRPModelElement.call_com()`, `AbstractRPModelElement._get_method_or_property()`, and `AbstractRPModelElement._set_method_or_property()` as static methods. Yet `RhapsodyApplication` is **not** an `IRPModelElement` — `IRPApplication` sits outside the element hierarchy in the Java API. Borrowing utilities from a class hierarchy it doesn't belong to is a layering violation that confuses readers and creates a fragile import dependency from `application.py` into the element model.

2. **Incomplete API surface.** `RhapsodyApplication` exposes only 8 of `IRPApplication`'s methods. Methods for version info, project lifecycle, code generation, model import, and model checking are absent, forcing users who need them to drop down to raw COM calls.

## Scope

This design fixes both problems:

- Extracts the three COM utility functions (`call_com`, `_get_method_or_property`, `_set_method_or_property`) into a new standalone module so both `AbstractRPModelElement` and `RhapsodyApplication` can use them without a class-hierarchy dependency.
- Adds ~15 missing `IRPApplication` methods grouped by concern.

## Non-Goals

- No changes to element wrapper classes (`RPModelElement`, `RPUnit`, `RPProject`, etc.) beyond the one-line forwarding in `AbstractRPModelElement`.
- No changes to the `RhapsodyContext` or CLI layer — they already use `RhapsodyApplication` through its public API and are unaffected.
- No changes to the public API of `rhapsody_cli/__init__.py`.
- `loginToDesignManager*` / `openProjectFromDesignManager*` remain excluded (deprecated in the Java API).
- `addToModelByReference`, `addToModelFromURL`, `applyNewTermsProfile`, `allowBrowserRefresh`, `allowGERefresh`, `addSelectedToFavorites` — excluded as lower-value until a use case appears.

## Design

### 1. New module: `src/rhapsody_cli/com_utils.py`

Standalone module with three functions extracted verbatim from `AbstractRPModelElement`:

```python
def call_com(func: Callable[[], T]) -> T:
    """Invoke func, translating pywintypes.com_error into RhapsodyRuntimeException."""

def get_method_or_property(com_obj: Any, method_name: str, prop_name: str) -> Any:
    """Read via Java-style method (getXxx) with bare COM property fallback (xxx)."""

def set_method_or_property(com_obj: Any, method_name: str, prop_name: str, value: Any) -> None:
    """Write via Java-style setter (setXxx) with bare COM property fallback (xxx = value)."""
```

Also moves the `pywintypes` import guard (`try/except ImportError`) here — it's the only place that needs it for the COM error type check.

The `cls` parameter was unused in all three original classmethods — no signature change needed.

### 2. Changes to `models/core.py`

`AbstractRPModelElement.call_com`, `AbstractRPModelElement._get_method_or_property`, and `AbstractRPModelElement._set_method_or_property` become thin **forwarding classmethods**:

```python
@classmethod
def call_com(cls, func):
    return com_utils.call_com(func)
```

This keeps the **100+ existing call sites** (`AbstractRPModelElement.call_com(...)`, `cls.call_com(...)`) across all element modules unchanged — zero diff in element code.

The `pywintypes` import guard and the import of `RhapsodyRuntimeException` can be removed from this file if they are no longer used directly (they become transitive via `com_utils`). However, `RhapsodyRuntimeException` is also referenced in `models/core.py` docstrings, so keep the import for that module if it's still used.

### 3. Changes to `application.py`

`RhapsodyApplication` now imports `com_utils` directly. All static references to `AbstractRPModelElement.xxx` are replaced:

| Before | After |
|--------|-------|
| `AbstractRPModelElement.call_com(lambda: ...)` | `com_utils.call_com(lambda: ...)` |
| `AbstractRPModelElement._get_method_or_property(...)` | `com_utils.get_method_or_property(...)` |
| `AbstractRPModelElement._set_method_or_property(...)` | `com_utils.set_method_or_property(...)` |

After this change, `RhapsodyApplication` has **zero imports from the element hierarchy** (`models.core`, `models.elements`). The only remaining imports from `models` are `RPProject` and `RPCollection` (return types from COM calls, not static dependencies).

#### Lifecycle simplification: connect/disconnect pair

`attach()` and `launch()` become private classmethods `_attach()` and `_launch()`. `connect()` is the only public entry point, with two optional parameters:

- `attach_only: bool = False` — when True, only try to attach to a running instance; raise on failure instead of falling back to launch. Default `False` preserves the current auto-mode behavior.
- `show_gui: bool = True` — when launching a new instance, controls whether the Rhapsody GUI window is visible. Default `True` (show GUI). Only applies when a new instance is launched.

`quit()` remains as a direct mirror of `IRPApplication.quit()`. A new `disconnect()` method is added on top — it calls `self.quit()` and provides a hook point for future cleanup (e.g. logging, resource release). This forms a natural lifecycle pair: `connect()` / `disconnect()`.

```python
# RhapsodyApplication — simplified public API
@classmethod
def connect(cls, attach_only: bool = False, show_gui: bool = True) -> "RhapsodyApplication":
    """Connect to Rhapsody.

    Args:
        attach_only: If True, only attach to a running instance (no fallback launch).
        show_gui: If launching a new instance, whether to show the GUI window.

    Returns:
        A RhapsodyApplication wrapping the connected COM object.

    Raises:
        RhapsodyConnectionError: If attach_only is True and no instance is running,
            or if both attach and launch fail.
    """
    if attach_only:
        return cls._attach()
    try:
        return cls._attach()
    except RhapsodyConnectionError:
        app = cls._launch()
        if show_gui:
            app.setHiddenUI(False)
        return app

@classmethod
def _attach(cls) -> "RhapsodyApplication":
    """(internal) Attach to a running Rhapsody instance."""
    ...

@classmethod
def _launch(cls) -> "RhapsodyApplication":
    """(internal) Launch a new Rhapsody instance."""
    ...

def disconnect(self) -> None:
    """Disconnect from Rhapsody. Calls quit() and provides a cleanup hook."""
    # Future: add logging, resource teardown here
    self.quit()

def quit(self) -> None:
    """Quit the Rhapsody application (mirrors IRPApplication.quit())."""
    ...
```

`RhapsodyContext.connect()` loses its `method` parameter — it delegates to `RhapsodyApplication.connect()`. `RhapsodyContext.disconnect()` calls `self.app.disconnect()` instead of `self.app.quit()`.

Call sites in project actions change from `ctx.connect("attach")` to `ctx.connect()`.

### 4. Missing API surface

All new methods follow the existing pattern: delegate to `self._com.<method>()` via `com_utils.call_com`, and for getter/setter pairs use `com_utils._get_method_or_property`/`com_utils._set_method_or_property` for the method+property fallback.

#### Project lifecycle

```python
def closeAllProjects(self) -> None:
    """Close all open projects without quitting Rhapsody."""

def saveAll(self) -> None:
    """Save all open projects."""
```

#### Version and installation info

```python
def getVersion(self) -> str:
    """Get the Rhapsody version string (e.g. "8.3.1")."""

def getBuildNo(self) -> str:
    """Get the Rhapsody build number."""

def getRhapsodyDir(self) -> str:
    """Get the Rhapsody installation directory path."""

def getOMROOT(self) -> str:
    """Get the OMROOT directory path used by Rhapsody."""
```

#### Code generation

```python
def generate(self) -> None:
    """Generate code for the active configuration."""

def generateElements(self, elements: RPCollection) -> None:
    """Generate code for the specified collection of elements."""

def generateEntireProject(self) -> None:
    """Generate code for the entire active project."""

def regenerate(self) -> None:
    """Regenerate application code."""
```

#### Model import

```python
def addToModel(self, filename: str, withDescendant: int) -> None:
    """Add a unit file to the model."""

def addToModelEx(self, filename: str, mode: int, addSubUnits: int, addDependents: int) -> None:
    """Add a unit to the model with explicit control over add mode, sub-units, and dependents.
    The `mode` parameter corresponds to one of `AddToModelMode` values.
    """
```

#### Model checking

```python
def setLog(self, fullPathname: str) -> None:
    """Set the log file path for model-checking output."""

def checkModel(self) -> None:
    """Run model checking and write results to the log file (set via setLog)."""
```

### 5. Tests

#### New test file: `tests/unit/test_com_utils.py`

Tests for the extracted standalone functions:

- `test_call_com_returns_on_success`
- `test_call_com_wraps_com_error`
- `test_call_com_passes_through_non_com_exception`
- `test_get_method_or_property_prefers_method`
- `test_get_method_or_property_falls_back_to_property`
- `test_set_method_or_property_prefers_setter`
- `test_set_method_or_property_falls_back_to_property`

#### Updated tests in `tests/unit/test_application.py`

Existing tests that reference `RhapsodyApplication.attach()`, `.launch()`, or `.quit()` are updated:

- `test_attach_wraps_active_com_object` → `test_connect_uses_attach_when_running` (mocks `_attach` success path inside `connect()`)
- `test_attach_raises_connection_error_when_none_running` → `test_connect_uses_launch_when_attach_fails` (mocks `_attach` failure, verifies `_launch` is called)
- `test_launch_wraps_new_com_object` — removed (tested implicitly via `connect` fallback path)
- `test_launch_raises_connection_error_when_dispatch_fails` → `test_connect_raises_when_both_fail`
- `test_connect_prefers_attach...` / `test_connect_falls_back...` / `test_connect_raises...` — simplified to single `test_connect` tests
- `test_quit_delegates_to_com` — unchanged (quit mirrors Java API)
- `test_disconnect_calls_quit` — new test that verifies `disconnect()` delegates to `quit()`
- `test_connect_attach_only_raises_when_not_running` — tests `connect(attach_only=True)` with no running instance
- `test_connect_launch_shows_gui_by_default` — tests that after launch, `setHiddenUI(False)` is called
- `test_connect_launch_hides_gui_when_specified` — tests `connect(show_gui=False)` keeps UI hidden

For each new API method, a test that:
- Mocks `self._com.<method>` on a `MagicMock` fake app
- Verifies the wrapper calls the correct COM method
- Verifies return type (if applicable)

### 6. Public API — unchanged

`__init__.py` continues exporting `RhapsodyApplication`, `RPModelElement`, etc. `com_utils` is internal (no `__all__` entry, no public import).

### 7. `_wrap_if_element` — stays on `AbstractRPModelElement`

This method calls `cls.wrap()` which is element-specific. Not moved to `com_utils`.

## Implementation Plan

### Step 1: Create `com_utils.py`

Extract `call_com`, `_get_method_or_property`, `_set_method_or_property` from `AbstractRPModelElement` into `src/rhapsody_cli/com_utils.py` as module-level functions. Move the `pywintypes` import guard. Strip the unused `cls` parameter. Rename the public-facing functions to not have the underscore prefix: `call_com`, `get_method_or_property`, `set_method_or_property`.

### Step 2: Update `models/core.py`

- Add `from rhapsody_cli.com_utils import call_com, get_method_or_property, set_method_or_property`
- Replace `AbstractRPModelElement.call_com`, `_get_method_or_property`, `_set_method_or_property` with one-line forwarders
- Remove the `pywintypes` import guard if no longer directly used
- Verify `RhapsodyRuntimeException` import is still needed (it is, for `call_com`'s forwarding return type / docstrings)

### Step 3: Update `application.py`

- Replace all `AbstractRPModelElement.xxx` calls with `com_utils.xxx`
- Rename `attach()` → `_attach()` (private classmethod)
- Rename `launch()` → `_launch()` (private classmethod)
- Simplify `connect()` — `connect(attach_only=False, show_gui=True)`, call `_attach()` then `_launch()` with GUI control
- Keep `quit()` as-is (Java API mirror)
- Add `disconnect()` that calls `self.quit()` (cleanup/lifecycle hook)
- Add all new methods from section 4 above
- Remove the import of `AbstractRPModelElement` from `models.core`

### Step 3b: Update `cli/context.py` and callers

- Simplify `RhapsodyContext.connect()` — remove `method` param, delegate to `RhapsodyApplication.connect()`
- `RhapsodyContext.disconnect()` — call `self.app.disconnect()` instead of `self.app.quit()`
- Update all CLI action callers: `ctx.connect("attach")` → `ctx.connect()` in `project_action.py`

### Step 4: Write tests

- Create `tests/unit/test_com_utils.py`
- Add test methods for each new application method in `tests/unit/test_application.py`
- Run `pytest tests/unit/` and verify all pass

### Step 5: Quality gate

```bash
ruff check src/ tests/
black --check src/ tests/
mypy src/ tests/
pytest tests/unit/
```
