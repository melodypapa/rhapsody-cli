# RhapsodyApplication Redesign — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refactor `RhapsodyApplication` to remove its dependency on `AbstractRPModelElement` by extracting COM utility functions into a standalone module, simplify the lifecycle API (`connect`/`disconnect`), and add ~15 missing IRPApplication methods.

**Architecture:** Extract `call_com`, `get_method_or_property`, `set_method_or_property` into `com_utils.py`. `AbstractRPModelElement` forwards to these via one-liner classmethods (0 diff in 100+ call sites). `RhapsodyApplication` uses `com_utils` directly with no imports from the element hierarchy. `connect()` gains `attach_only` and `show_gui` params; `attach()`/`launch()` become private; `disconnect()` wraps `quit()`.

**Tech Stack:** Python 3.8+, pywin32 (COM), MagicMock (tests)

## Global Constraints

- No changes to element wrapper call sites (100+ references to `AbstractRPModelElement.call_com(...)` stay unchanged)
- Method names must mirror the Rhapsody Java API exactly (`getName`, `activeProject`, `quit`, etc.)
- All COM calls must go through `call_com(lambda: ...)` or the helper accessors
- No use of `from __future__ import annotations`
- Tests must use MagicMock-based fakes from `tests/unit/models/fakes.py`
- The `pywintypes` import guard (`try/except ImportError`) must stay for cross-platform compatibility (Sphinx on Linux)

## File Structure

| File | Action | Responsibility |
|------|--------|---------------|
| `src/rhapsody_cli/com_utils.py` | **Create** | Standalone COM utilities: `call_com`, `get_method_or_property`, `set_method_or_property` |
| `src/rhapsody_cli/models/core.py` | **Modify** | Classmethods become one-line forwarders to `com_utils` |
| `src/rhapsody_cli/application.py` | **Modify** | Switch to `com_utils`, lifecycle changes, new API methods |
| `src/rhapsody_cli/cli/context.py` | **Modify** | Simplify `connect()`, update `disconnect()` |
| `src/rhapsody_cli/actions/project_action.py` | **Modify** | `ctx.connect("attach")` → `ctx.connect()` |
| `tests/unit/test_com_utils.py` | **Create** | Tests for standalone COM utilities |
| `tests/unit/test_application.py` | **Modify** | Rewrite lifecycle tests, add new method tests |
| `tests/integration/conftest.py` | **Modify** | `RhapsodyApplication.attach()` → `RhapsodyApplication.connect()` |

---

### Task 1: Create `com_utils.py` and forward from `AbstractRPModelElement`

**Files:**
- Create: `src/rhapsody_cli/com_utils.py`
- Modify: `src/rhapsody_cli/models/core.py`
- Test: `tests/unit/test_com_utils.py`

**Interfaces:**
- Consumes: `RhapsodyRuntimeException` from `rhapsody_cli.exceptions`
- Produces: `com_utils.call_com(func)`, `com_utils.get_method_or_property(com_obj, method_name, prop_name)`, `com_utils.set_method_or_property(com_obj, method_name, prop_name, value)`

- [ ] **Step 1: Create `src/rhapsody_cli/com_utils.py`**

```python
"""Standalone COM utility functions for rhapsody_cli.

These were extracted from ``AbstractRPModelElement`` so they can be used
by both the element wrapper hierarchy and ``RhapsodyApplication`` without
a class-hierarchy dependency.
"""

from typing import Any, Callable, TypeVar

from rhapsody_cli.exceptions import RhapsodyRuntimeException

try:
    import pywintypes
except ImportError:
    pywintypes = None

T = TypeVar("T")


def call_com(func: Callable[[], T]) -> T:
    """Invoke a COM call, translating COM errors into RhapsodyRuntimeException."""
    try:
        return func()
    except Exception as exc:
        if pywintypes is not None and isinstance(exc, pywintypes.com_error):
            raise RhapsodyRuntimeException(str(exc)) from exc
        raise


def get_method_or_property(com_obj: Any, method_name: str, prop_name: str) -> Any:
    """Read a value from com_obj, preferring the Java-style method with bare COM property fallback."""
    if hasattr(com_obj, method_name):
        return call_com(lambda: getattr(com_obj, method_name)())
    return call_com(lambda: getattr(com_obj, prop_name))


def set_method_or_property(com_obj: Any, method_name: str, prop_name: str, value: Any) -> None:
    """Write a value to com_obj, preferring the Java-style setter with bare COM property fallback."""
    if hasattr(com_obj, method_name):
        call_com(lambda: getattr(com_obj, method_name)(value))
    else:
        call_com(lambda: setattr(com_obj, prop_name, value))
```

- [ ] **Step 2: Add forwarders in `src/rhapsody_cli/models/core.py`**

At the top of the file, add the import:
```python
from rhapsody_cli import com_utils
```

Remove the `pywintypes` import guard (the `try: import pywintypes ... except ImportError` block around lines 16-19) since it now lives in `com_utils.py`.

Keep `from rhapsody_cli.exceptions import RhapsodyRuntimeException` — it's still referenced in docstrings.

Replace the three classmethod bodies in `AbstractRPModelElement`:

`call_com` (lines 42-51):
```python
@classmethod
def call_com(cls, func):
    return com_utils.call_com(func)
```

`_get_method_or_property` (lines 74-86):
```python
@classmethod
def _get_method_or_property(cls, com_obj, method_name, prop_name):
    return com_utils.get_method_or_property(com_obj, method_name, prop_name)
```

`_set_method_or_property` (lines 89-97):
```python
@classmethod
def _set_method_or_property(cls, com_obj, method_name, prop_name, value):
    return com_utils.set_method_or_property(com_obj, method_name, prop_name, value)
```

- [ ] **Step 3: Write `tests/unit/test_com_utils.py`**

```python
"""Tests for rhapsody_cli.com_utils."""

from unittest.mock import MagicMock

import pytest
import pywintypes

from rhapsody_cli.com_utils import call_com, get_method_or_property, set_method_or_property
from rhapsody_cli.exceptions import RhapsodyRuntimeException


def test_call_com_returns_on_success() -> None:
    result = call_com(lambda: 42)
    assert result == 42


def test_call_com_wraps_com_error() -> None:
    with pytest.raises(RhapsodyRuntimeException):
        call_com(lambda: (_ for _ in ()).throw(pywintypes.com_error(-2147352567, "failed", None, None)))


def test_call_com_passes_through_non_com_exception() -> None:
    with pytest.raises(ValueError):
        call_com(lambda: (_ for _ in ()).throw(ValueError("boom")))


def test_get_method_or_property_prefers_method() -> None:
    obj = MagicMock()
    obj.getName.return_value = "MethodResult"
    obj.name = "PropertyFallback"
    result = get_method_or_property(obj, "getName", "name")
    assert result == "MethodResult"
    obj.getName.assert_called_once_with()


def test_get_method_or_property_falls_back_to_property() -> None:
    obj = MagicMock(spec=["name"])
    obj.name = "PropertyFallback"
    result = get_method_or_property(obj, "getName", "name")
    assert result == "PropertyFallback"


def test_set_method_or_property_prefers_setter() -> None:
    obj = MagicMock()
    set_method_or_property(obj, "setName", "name", "NewName")
    obj.setName.assert_called_once_with("NewName")


def test_set_method_or_property_falls_back_to_property() -> None:
    obj = MagicMock(spec=["name"])
    set_method_or_property(obj, "setName", "name", "NewName")
    assert obj.name == "NewName"
```

- [ ] **Step 4: Run the com_utils tests**

Run: `pytest tests/unit/test_com_utils.py -v`
Expected: 7 passed

- [ ] **Step 5: Run the full unit suite to verify no regression from core.py changes**

Run: `pytest tests/unit/ -v`
Expected: All existing tests pass

- [ ] **Step 6: Commit**

```bash
git add src/rhapsody_cli/com_utils.py src/rhapsody_cli/models/core.py tests/unit/test_com_utils.py
git commit -m "refactor: extract COM utilities into com_utils.py module"
```

---

### Task 2: Refactor `application.py` — lifecycle and com_utils migration

**Files:**
- Modify: `src/rhapsody_cli/application.py`

**Interfaces:**
- Consumes: `com_utils.call_com`, `com_utils.get_method_or_property`, `com_utils.set_method_or_property`
- Produces: Updated `RhapsodyApplication` with `connect(attach_only, show_gui)`, `_attach`, `_launch`, `disconnect()`

- [ ] **Step 1: Replace imports in `application.py`**

Remove:
```python
from rhapsody_cli.models.core import AbstractRPModelElement, RPCollection
```

Add:
```python
from rhapsody_cli import com_utils
from rhapsody_cli.models.core import RPCollection
```

Keep `RPProject` import unchanged.

- [ ] **Step 2: Rewrite the classmethods**

Replace `attach()` (lines 33-49) with `_attach()`:
```python
@classmethod
def _attach(cls) -> "RhapsodyApplication":
    if win32com is None:
        raise RhapsodyConnectionError("pywin32 is not available; Rhapsody automation requires Windows.")
    try:
        com_obj = com_utils.call_com(lambda: win32com.client.GetActiveObject(_PROG_ID))
    except RhapsodyRuntimeException as exc:
        raise RhapsodyConnectionError(f"No running Rhapsody instance found: {exc}") from exc
    return cls(com_obj)
```

Replace `launch()` (lines 51-68) with `_launch()`:
```python
@classmethod
def _launch(cls) -> "RhapsodyApplication":
    if win32com is None:
        raise RhapsodyConnectionError("pywin32 is not available; Rhapsody automation requires Windows.")
    try:
        com_obj = com_utils.call_com(lambda: win32com.client.Dispatch(_PROG_ID))
    except RhapsodyRuntimeException as exc:
        raise RhapsodyConnectionError(f"Failed to launch Rhapsody instance: {exc}") from exc
    return cls(com_obj)
```

Replace `connect()` (lines 70-86):
```python
@classmethod
def connect(cls, attach_only: bool = False, show_gui: bool = True) -> "RhapsodyApplication":
    if attach_only:
        return cls._attach()
    try:
        return cls._attach()
    except RhapsodyConnectionError:
        app = cls._launch()
        if show_gui:
            app.setHiddenUI(False)
        return app
```

- [ ] **Step 3: Replace `AbstractRPModelElement` references in existing methods**

`openProject` (line 97):
```python
return RPProject(com_utils.call_com(lambda: self._com.openProject(filename)))
```

`createNewProject` (line 109):
```python
com_utils.call_com(lambda: self._com.createNewProject(project_location, project_name))
```

`activeProject` (line 118):
```python
return RPProject(com_utils.call_com(lambda: self._com.activeProject()))
```

`getProjects` (line 126):
```python
return RPCollection(com_utils.get_method_or_property(self._com, "getProjects", "projects"))
```

`quit` (line 133):
```python
com_utils.call_com(lambda: self._com.quit())
```

`getIsHiddenUI` (line 141):
```python
return bool(com_utils.get_method_or_property(self._com, "getIsHiddenUI", "isHiddenUI"))
```

`setHiddenUI` (line 153):
```python
com_utils.set_method_or_property(self._com, "setHiddenUI", "isHiddenUI", hidden)
```

`bringWindowToTop` (line 162):
```python
com_utils.call_com(lambda: self._com.bringWindowToTop())
```

- [ ] **Step 4: Add `disconnect()` method after `quit()`**

```python
def disconnect(self) -> None:
    """Disconnect from Rhapsody. Calls quit() and provides a cleanup hook."""
    self.quit()
```

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/application.py
git commit -m "refactor: migrate application.py to com_utils, add disconnect, simplify connect"
```

---

### Task 3: Add missing IRPApplication methods

**Files:**
- Modify: `src/rhapsody_cli/application.py`

- [ ] **Step 1: Add project lifecycle methods after `bringWindowToTop()`**

```python
def closeAllProjects(self) -> None:
    com_utils.call_com(lambda: self._com.closeAllProjects())

def saveAll(self) -> None:
    com_utils.call_com(lambda: self._com.saveAll())
```

- [ ] **Step 2: Add version/info methods**

```python
def getVersion(self) -> str:
    return str(com_utils.call_com(lambda: self._com.getVersion()))

def getBuildNo(self) -> str:
    return str(com_utils.call_com(lambda: self._com.getBuildNo()))

def getRhapsodyDir(self) -> str:
    return str(com_utils.call_com(lambda: self._com.getRhapsodyDir()))

def getOMROOT(self) -> str:
    return str(com_utils.call_com(lambda: self._com.getOMROOT()))
```

- [ ] **Step 3: Add code generation methods**

```python
def generate(self) -> None:
    com_utils.call_com(lambda: self._com.generate())

def generateElements(self, elements: RPCollection) -> None:
    com_utils.call_com(lambda: self._com.generateElements(elements._com))

def generateEntireProject(self) -> None:
    com_utils.call_com(lambda: self._com.generateEntireProject())

def regenerate(self) -> None:
    com_utils.call_com(lambda: self._com.regenerate())
```

- [ ] **Step 4: Add model import methods**

```python
def addToModel(self, filename: str, withDescendant: int) -> None:
    com_utils.call_com(lambda: self._com.addToModel(filename, withDescendant))

def addToModelEx(self, filename: str, mode: int, addSubUnits: int, addDependents: int) -> None:
    com_utils.call_com(lambda: self._com.addToModelEx(filename, mode, addSubUnits, addDependents))
```

- [ ] **Step 5: Add model checking methods**

```python
def setLog(self, fullPathname: str) -> None:
    com_utils.call_com(lambda: self._com.setLog(fullPathname))

def checkModel(self) -> None:
    com_utils.call_com(lambda: self._com.checkModel())
```

- [ ] **Step 6: Verify syntax**

Run: `python -c "import ast; ast.parse(open('src/rhapsody_cli/application.py').read()); print('OK')"`
Expected: OK

- [ ] **Step 7: Commit**

```bash
git add src/rhapsody_cli/application.py
git commit -m "feat: add missing IRPApplication methods to RhapsodyApplication"
```

---

### Task 4: Update `cli/context.py` and CLI action callers

**Files:**
- Modify: `src/rhapsody_cli/cli/context.py`
- Modify: `src/rhapsody_cli/actions/project_action.py`

- [ ] **Step 1: Simplify `connect()` in `context.py`**

Replace:
```python
def connect(self, method: str = "attach") -> RhapsodyApplication:
    if self.app is None:
        if method == "attach":
            self.app = RhapsodyApplication.attach()
        else:
            self.app = RhapsodyApplication.launch()
    return self.app
```

With:
```python
def connect(self) -> RhapsodyApplication:
    if self.app is None:
        self.app = RhapsodyApplication.connect()
    return self.app
```

- [ ] **Step 2: Update `disconnect()` in `context.py`**

Replace:
```python
def disconnect(self) -> None:
    self.close_project()
    if self.app:
        self.app.quit()
        self.app = None
```

With:
```python
def disconnect(self) -> None:
    self.close_project()
    if self.app:
        self.app.disconnect()
        self.app = None
```

- [ ] **Step 3: Update `project_action.py` callers**

Replace `ctx.connect("attach")` with `ctx.connect()` in:

- `ProjectOpenAction.execute()` (line 27)
- `ProjectListAction.execute()` (line 52)
- `ProjectNewAction.execute()` (line 117)

- [ ] **Step 4: Commit**

```bash
git add src/rhapsody_cli/cli/context.py src/rhapsody_cli/actions/project_action.py
git commit -m "refactor: simplify RhapsodyContext connect/disconnect lifecycle"
```

---

### Task 5: Update `tests/unit/test_application.py`

**Files:**
- Modify: `tests/unit/test_application.py`

- [ ] **Step 1: Replace lifecycle tests (lines 13-88)**

Replace the block from `test_attach_wraps_active_com_object` through `test_connect_raises_connection_error_when_launch_fails` with:

```python
from rhapsody_cli.application import RhapsodyApplication
from rhapsody_cli.exceptions import RhapsodyConnectionError
from rhapsody_cli.models.core import RPCollection
from rhapsody_cli.models.elements.containment import RPProject
from tests.unit.models.fakes import make_fake_collection, make_fake_element


# --- connect() lifecycle tests ---

@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_uses_attach_when_running(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    fake_com = MagicMock(name="FakeApplication")
    mock_attach.return_value = RhapsodyApplication(fake_com)

    app = RhapsodyApplication.connect()

    mock_attach.assert_called_once()
    mock_launch.assert_not_called()
    assert app._com is fake_com


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_uses_launch_when_attach_fails(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    mock_attach.side_effect = RhapsodyConnectionError("no instance")
    fake_com = MagicMock(name="FakeApplication")
    mock_launch.return_value = RhapsodyApplication(fake_com)

    app = RhapsodyApplication.connect()

    mock_attach.assert_called_once()
    mock_launch.assert_called_once()
    assert app._com is fake_com


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_raises_when_both_fail(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    mock_attach.side_effect = RhapsodyConnectionError("no instance")
    mock_launch.side_effect = RhapsodyConnectionError("launch failed")

    with pytest.raises(RhapsodyConnectionError):
        RhapsodyApplication.connect()

    mock_attach.assert_called_once()
    mock_launch.assert_called_once()


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_attach_only_raises_when_not_running(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    mock_attach.side_effect = RhapsodyConnectionError("no instance")

    with pytest.raises(RhapsodyConnectionError):
        RhapsodyApplication.connect(attach_only=True)

    mock_attach.assert_called_once()
    mock_launch.assert_not_called()


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_launch_shows_gui_by_default(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    mock_attach.side_effect = RhapsodyConnectionError("no instance")
    fake_com = MagicMock(name="FakeApplication")
    mock_launch.return_value = RhapsodyApplication(fake_com)

    RhapsodyApplication.connect()

    fake_com.setHiddenUI.assert_called_once_with(False)


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_launch_hides_gui_when_specified(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    mock_attach.side_effect = RhapsodyConnectionError("no instance")
    fake_com = MagicMock(name="FakeApplication")
    mock_launch.return_value = RhapsodyApplication(fake_com)

    RhapsodyApplication.connect(show_gui=False)

    fake_com.setHiddenUI.assert_not_called()
```

- [ ] **Step 2: Add `disconnect()` test after `test_bring_window_to_top`**

```python
def test_disconnect_calls_quit() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)

    app.disconnect()

    fake_app.quit.assert_called_once_with()
```

- [ ] **Step 3: Add missing API method tests after `test_disconnect_calls_quit`**

```python
# --- Project lifecycle ---

def test_close_all_projects_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)
    app.closeAllProjects()
    fake_app.closeAllProjects.assert_called_once_with()


def test_save_all_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)
    app.saveAll()
    fake_app.saveAll.assert_called_once_with()


# --- Version info ---

def test_get_version_returns_string() -> None:
    fake_app = MagicMock(name="FakeApplication")
    fake_app.getVersion.return_value = "8.3.1"
    app = RhapsodyApplication(fake_app)
    assert app.getVersion() == "8.3.1"


def test_get_build_no_returns_string() -> None:
    fake_app = MagicMock(name="FakeApplication")
    fake_app.getBuildNo.return_value = "12345"
    app = RhapsodyApplication(fake_app)
    assert app.getBuildNo() == "12345"


def test_get_rhapsody_dir_returns_string() -> None:
    fake_app = MagicMock(name="FakeApplication")
    fake_app.getRhapsodyDir.return_value = "C:/Program Files/Rhapsody"
    app = RhapsodyApplication(fake_app)
    assert app.getRhapsodyDir() == "C:/Program Files/Rhapsody"


def test_get_omroot_returns_string() -> None:
    fake_app = MagicMock(name="FakeApplication")
    fake_app.getOMROOT.return_value = "C:/Rhapsody/OMROOT"
    app = RhapsodyApplication(fake_app)
    assert app.getOMROOT() == "C:/Rhapsody/OMROOT"


# --- Code generation ---

def test_generate_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)
    app.generate()
    fake_app.generate.assert_called_once_with()


def test_generate_elements_passes_collection_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    fake_collection = make_fake_collection([])
    app = RhapsodyApplication(fake_app)
    app.generateElements(RPCollection(fake_collection))
    fake_app.generateElements.assert_called_once_with(fake_collection)


def test_generate_entire_project_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)
    app.generateEntireProject()
    fake_app.generateEntireProject.assert_called_once_with()


def test_regenerate_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)
    app.regenerate()
    fake_app.regenerate.assert_called_once_with()


# --- Model import ---

def test_add_to_model_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)
    app.addToModel("myfile.rpy", 1)
    fake_app.addToModel.assert_called_once_with("myfile.rpy", 1)


def test_add_to_model_ex_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)
    app.addToModelEx("myfile.rpy", 1, 1, 1)
    fake_app.addToModelEx.assert_called_once_with("myfile.rpy", 1, 1, 1)


# --- Model checking ---

def test_set_log_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)
    app.setLog("C:/log.txt")
    fake_app.setLog.assert_called_once_with("C:/log.txt")


def test_check_model_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)
    app.checkModel()
    fake_app.checkModel.assert_called_once_with()
```

- [ ] **Step 4: Run all application tests**

Run: `pytest tests/unit/test_application.py -v`
Expected: All ~30 tests pass

- [ ] **Step 5: Commit**

```bash
git add tests/unit/test_application.py
git commit -m "test: update application tests for lifecycle and new API methods"
```

---

### Task 6: Update integration conftest and final quality gate

**Files:**
- Modify: `tests/integration/conftest.py`

- [ ] **Step 1: Update `tests/integration/conftest.py`**

Replace `app = RhapsodyApplication.attach()` on line 19:
```python
app = RhapsodyApplication.connect()
```

- [ ] **Step 2: Run full quality gate**

```bash
ruff check src/ tests/
black --check src/ tests/
mypy src/ tests/
pytest tests/unit/
```

Expected: All pass cleanly.

- [ ] **Step 3: Commit**

```bash
git add tests/integration/conftest.py
git commit -m "chore: update integration conftest to use connect()"
```

---

### Task 7: Update requirements document

**Files:**
- Modify: `docs/requirements/swr_app_requirements.md`

- [ ] **Step 1: Update SWR_APP_00001 (attach → _attach)**

Replace `RhapsodyApplication.attach()` with `RhapsodyApplication._attach()` and add a note that it is a private helper used internally by `connect()`.

- [ ] **Step 2: Update SWR_APP_00002 (launch → _launch)**

Same treatment as SWR_APP_00001 — `launch()` → `_launch()`, mark private.

- [ ] **Step 3: Rewrite SWR_APP_00003 (connect)**

Replace `connect(prefer_attach: bool = True)` with `connect(attach_only: bool = False, show_gui: bool = True)`:
- `attach_only=True` — only try to attach; no fallback to launch
- `attach_only=False` (default) — try attach first, fall back to launch
- `show_gui=True` (default) — show GUI on newly launched instance
- `show_gui=False` — keep Rhapsody GUI hidden

- [ ] **Step 4: Add SWR_APP_00010–00023 for new methods**

Add new requirements for: `closeAllProjects`, `saveAll`, `getVersion`, `getBuildNo`, `getRhapsodyDir`, `getOMROOT`, `generate`, `generateElements`, `generateEntireProject`, `regenerate`, `addToModel`, `addToModelEx`, `setLog`, `checkModel`. Each should reference the exact method signature and COM delegation pattern.

- [ ] **Step 5: Add SWR_APP_00024 for disconnect()**

Add requirement for `disconnect()` method that wraps `quit()` as a lifecycle pair.

- [ ] **Step 6: Verify**

```bash
ruff check docs/requirements/swr_app_requirements.md
```
Expected: No issues (or linter-skip if markdown not in scope)

- [ ] **Step 7: Commit**

```bash
git add docs/requirements/swr_app_requirements.md
git commit -m "docs: update application requirements for redesigned lifecycle and new API"
```

---

### Task 8: Update test spec document

**Files:**
- Modify: `docs/tests/unit/uts_app_test-specs.md`

- [ ] **Step 1: Rewrite UTS_APP_00001–00002 (attach lifecycle)**

These now describe `_attach()` as a private helper, tested indirectly via `connect()` tests.

- [ ] **Step 2: Rewrite UTS_APP_00003–00004 (launch lifecycle)**

Same treatment as attach — `_launch()` is private, tested via `connect()`.

- [ ] **Step 3: Rewrite UTS_APP_00005–00007 (connect lifecycle)**

Replace `prefer_attach` parameter with `attach_only`/`show_gui`:
- `UTS_APP_00005`: `connect()` falls back to launch when attach fails
- `UTS_APP_00006`: `connect()` uses attach when it succeeds
- `UTS_APP_00007`: `connect(attach_only=True)` raises when not running
- Add new: `connect(show_gui=True)` shows GUI on launch
- Add new: `connect(show_gui=False)` hides GUI on launch

- [ ] **Step 4: Add UTS_APP_00016–00030 for new methods**

Add test specs for: `disconnect()`, `closeAllProjects()`, `saveAll()`, `getVersion()`, `getBuildNo()`, `getRhapsodyDir()`, `getOMROOT()`, `generate()`, `generateElements()`, `generateEntireProject()`, `regenerate()`, `addToModel()`, `addToModelEx()`, `setLog()`, `checkModel()`. Each traces to the corresponding SWR_APP requirement.

- [ ] **Step 5: Commit**

```bash
git add docs/tests/unit/uts_app_test-specs.md
git commit -m "docs: update application test specs for redesigned lifecycle and new API"
```

---

### Task 9: Update user guide and API docs

**Files:**
- Modify: `docs/user_guide/connecting_to_rhapsody.rst`

- [ ] **Step 1: Rewrite connection mode section**

Replace the three public methods (attach/launch/connect) with the simplified API:

From:
```python
app = RhapsodyApplication()
app.attach()  # or app.launch() or app.connect()
```

To:
```python
# Default: try attach, fall back to launch, show GUI
app = RhapsodyApplication.connect()

# Attach-only mode (raise if no running instance)
app = RhapsodyApplication.connect(attach_only=True)

# Launch a headless instance (no GUI)
app = RhapsodyApplication.connect(show_gui=False)
```

- [ ] **Step 2: Fix constructor usage**

Replace all `app = RhapsodyApplication()` patterns (the constructor takes a COM object, not designed for end-user calls) with `app = RhapsodyApplication.connect()`.

- [ ] **Step 3: Fix `quit()` → `disconnect()` in cleanup examples**

Replace `app.quit()` with `app.disconnect()` in all code snippets.

- [ ] **Step 4: Update Multiple Instance Management example**

Replace `app1.attach()` / `app2.launch()` with `RhapsodyApplication.connect(attach_only=True)` for existing and `RhapsodyApplication.connect()` for new.

- [ ] **Step 5: Remove or fix context manager example**

Line 88 (`with RhapsodyApplication() as app:`) uses an incorrect pattern — either remove or note it's not yet implemented.

- [ ] **Step 6: Verify**

```bash
# rstcheck or just visual review
```

- [ ] **Step 7: Commit**

```bash
git add docs/user_guide/connecting_to_rhapsody.rst
git commit -m "docs: update user guide for simplified RhapsodyApplication.connect() API"
```

---

### Task 10: Update demo files

**Files:**
- Modify: `demos/demo_01_basic_connection.py`
- Modify: `demos/demo_02_project_operations.py`
- Modify: `demos/demo_03_element_navigation.py`
- Modify: `demos/demo_04_basic_element_creation.py`
- Modify: `demos/demo_05_error_handling.py`
- Modify: `demos/_bootstrap_demo_project.py`

- [ ] **Step 1: Update `demo_01_basic_connection.py`**

- Replace `RhapsodyApplication.attach()` with `RhapsodyApplication.connect(attach_only=True)` in `demo_attach()`
- Replace `RhapsodyApplication.launch()` with `RhapsodyApplication.connect()` in `demo_launch()`
- Replace `RhapsodyApplication.connect(prefer_attach=True)` with `RhapsodyApplication.connect()` in `demo_connect()`
- Replace `app.quit()` with `app.disconnect()` in all three demo functions
- Update docstring and print messages to reflect simplified API
- Remove `demo_attach` / `demo_launch` or keep them as `connect(attach_only=True)` / `connect()` demos

- [ ] **Step 2: Update `demo_02_project_operations.py`**

- Replace `RhapsodyApplication.connect(prefer_attach=False)` with `RhapsodyApplication.connect(show_gui=True)`
- Remove the manual `setHiddenUI(False)` / `bringWindowToTop()` calls (connect now handles GUI visibility via `show_gui` param)
- Replace `app.quit()` with `app.disconnect()`
- Update docstring

- [ ] **Step 3: Update `demo_03_element_navigation.py`**

- Replace `RhapsodyApplication.connect()` call (already correct) — no param change needed
- Replace `app.quit()` with `app.disconnect()`
- No other changes needed

- [ ] **Step 4: Update `demo_04_basic_element_creation.py`**

- `RhapsodyApplication.connect()` already correct
- Replace `app.quit()` with `app.disconnect()`
- No other changes needed

- [ ] **Step 5: Update `demo_05_error_handling.py`**

- Replace the manual attach → launch fallback in `demo_connection_error_handling()` with `RhapsodyApplication.connect()` (the smart `connect()` already implements this pattern)
- Remove the `RhapsodyApplication.attach()` / `RhapsodyApplication.launch()` direct calls
- Replace `app.quit()` with `app.disconnect()`
- Update docstring to reflect "smart connect" pattern rather than manual fallback
- Update troubleshooting text

- [ ] **Step 6: Update `_bootstrap_demo_project.py`**

- Replace `RhapsodyApplication.launch()` with `RhapsodyApplication.connect()`
- Replace `app.quit()` with `app.disconnect()`
- Update docstring

- [ ] **Step 7: Verify syntax of all demo files**

```bash
python -c "
import ast, os, glob
for f in glob.glob('demos/*.py'):
    ast.parse(open(f).read())
    print(f'OK: {f}')
"
```
Expected: All six demo files parse successfully.

- [ ] **Step 8: Commit**

```bash
git add demos/
git commit -m "docs: update demos to use simplified connect()/disconnect() API"
```
