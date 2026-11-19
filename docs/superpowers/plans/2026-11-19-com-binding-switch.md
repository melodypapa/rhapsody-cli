# COM Binding Switch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** (1) Obsolete `com_utils.py` — zero internal callers, file retained with `DeprecationWarning` for external users; (2) make the COM binding switchable via `RHAPSODY_COM_BINDING` (`dynamic` default until parity proven, `early` opt-in) so `EnsureDispatch` early-bound objects can be validated against the full live workload.

**Architecture:** First the three `com_utils` helpers are nativized into `models/core.py` (behavior-identical move: `AbstractRPModelElement.call_com`/`_get_method_or_property`/`_set_method_or_property` stop forwarding, `application.py` imports `call_com` from `models.core`) — this clears all internal callers in one stroke. Then `application.py` gains a `_get_binding()` env-var reader and an `early` branch in `_launch()` calling the native `call_com`. Wrappers, CLI, and actions are untouched.

**Tech Stack:** Python 3.8+, pywin32 (`win32com.client.gencache.EnsureDispatch`), pytest + `unittest.mock`, live IBM Rhapsody 10.0.3 (Windows) for Tasks 7-8.

**Spec:** `docs/superpowers/specs/2026-11-19-com-binding-switch-design.md`

## Global Constraints

- Branch: `docs/com-binding-switch` (spec commit already on it). Never commit to `main`.
- Python 3.8 compatible (`typing.Optional`/`Dict`; no PEP 604 unions, no `from __future__ import annotations`, no `Any` in annotations).
- Quality gate before every "done" claim: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
- No real COM in unit tests — patch `rhapsody_cli.application.win32com` (module-level name inside `application.py`, platform-safe).
- **com_utils policy (user directive):** after Task 2, `src/` contains zero references to `com_utils`; the file stays with `DeprecationWarning` shims for external users. snake_case public API stays; CLI/actions unchanged.
- Commit style: conventional commits, no AI attribution.
- Live tasks (7-8) require Windows + licensed Rhapsody 10.0.3; scratch projects only, cleaned up afterward.

---

### Task 1: `_get_binding()` env-var reader

**Files:**
- Modify: `src/rhapsody_cli/application.py`
- Test: `tests/unit/test_application.py`

**Interfaces:**
- Produces: `_get_binding() -> str` module-level function returning `"dynamic"` or `"early"`. Behavior: unset/empty -> `"dynamic"`; `"early"`/`"EARLY"`/`"Early"` -> `"early"` (case-insensitive); `"dynamic"`/`"DYNAMIC"` -> `"dynamic"`; any other value -> log warning via module `logger` and return `"dynamic"`. Read at call time (not import time). Task 3 consumes it inside `_launch()`.

- [ ] **Step 1: Write the failing tests**

Append to `tests/unit/test_application.py` (add `import os` to the stdlib imports at the top):

```python
class TestGetBinding:
    """Tests for the RHAPSODY_COM_BINDING env-var reader."""

    def test_default_is_dynamic_when_unset(self) -> None:
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("RHAPSODY_COM_BINDING", None)
            from rhapsody_cli.application import _get_binding

            assert _get_binding() == "dynamic"

    def test_early_binding_selected_case_insensitive(self) -> None:
        from rhapsody_cli.application import _get_binding

        for value in ("early", "EARLY", "Early"):
            with patch.dict(os.environ, {"RHAPSODY_COM_BINDING": value}):
                assert _get_binding() == "early"

    def test_dynamic_selected_explicitly(self) -> None:
        from rhapsody_cli.application import _get_binding

        with patch.dict(os.environ, {"RHAPSODY_COM_BINDING": "DYNAMIC"}):
            assert _get_binding() == "dynamic"

    def test_invalid_value_falls_back_to_dynamic(self) -> None:
        from rhapsody_cli.application import _get_binding

        with patch.dict(os.environ, {"RHAPSODY_COM_BINDING": "bogus"}):
            assert _get_binding() == "dynamic"
```

Note: `import pytest` already exists in the test module; add `import os` if missing.

- [ ] **Step 2: Run the tests to verify they fail**

Run: `pytest tests/unit/test_application.py::TestGetBinding --no-cov -q`
Expected: FAIL with `ImportError: cannot import name '_get_binding'`.

- [ ] **Step 3: Implement**

In `src/rhapsody_cli/application.py`, add after the `_PROG_ID = "Rhapsody2.Application.1"` line:

```python
_BINDING_ENV = "RHAPSODY_COM_BINDING"


def _get_binding() -> str:
    """Return the COM binding selected by RHAPSODY_COM_BINDING.

    ``early`` (case-insensitive) selects typelib early binding via
    ``EnsureDispatch``; anything else selects dynamic binding. An unknown
    value is logged and dynamic binding is used.
    """
    value = os.environ.get(_BINDING_ENV, "").strip().lower()
    if value == "early":
        return "early"
    if value == "dynamic" or value == "":
        return "dynamic"
    logger.warning("Unknown %s value '%s'; using dynamic binding", _BINDING_ENV, value)
    return "dynamic"
```

Also add `import os` to the stdlib import block at the top of the file (keep ruff/isort order).

- [ ] **Step 4: Run the tests to verify they pass**

Run: `pytest tests/unit/test_application.py::TestGetBinding --no-cov -q`
Expected: 4 PASS.

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/application.py tests/unit/test_application.py
git commit -m "feat: add RHAPSODY_COM_BINDING env-var binding reader"
```

---

### Task 2: Nativize the com_utils helpers; deprecate com_utils

**Files:**
- Modify: `src/rhapsody_cli/models/core.py`
- Modify: `src/rhapsody_cli/application.py`
- Modify: `src/rhapsody_cli/com_utils.py` (deprecation shims only)
- Test: `tests/unit/test_application.py` (deprecation-warning test) + full suite as behavioral gate

**Interfaces:**
- Produces (this is what every later task consumes):
  - Module-level `call_com(func: Callable[[], T]) -> T` in `rhapsody_cli.models.core` — identical behavior to `com_utils.call_com` (translates `pywintypes.com_error` -> `RhapsodyRuntimeException`).
  - `AbstractRPModelElement.call_com` classmethod — native body (no forwarding).
  - `AbstractRPModelElement._get_method_or_property(com_obj, method_name, prop_name)` and `_set_method_or_property(com_obj, method_name, prop_name, value)` — native static bodies (identical logic).
  - `application.py` imports `call_com` from `rhapsody_cli.models.core`; zero `com_utils` references anywhere in `src/`.
- `com_utils.py` keeps working (external users) but every function emits `DeprecationWarning`.

- [ ] **Step 1: Write the failing deprecation test**

Append to `tests/unit/test_application.py`:

```python
def test_com_utils_functions_emit_deprecation_warning() -> None:
    """com_utils is obsoleted internally; the shims warn external users."""
    import warnings

    from rhapsody_cli import com_utils

    fake_com = MagicMock(name="FakeCom")
    fake_com.name = "Probe"
    with pytest.warns(DeprecationWarning):
        com_utils._get_method_or_property(fake_com, "getName", "name")
    with pytest.warns(DeprecationWarning):
        com_utils._set_method_or_property(fake_com, "setName", "name", "x")
    with pytest.warns(DeprecationWarning):
        com_utils.call_com(lambda: "ok")
```

- [ ] **Step 2: Run to verify it fails**

Run: `pytest tests/unit/test_application.py::test_com_utils_functions_emit_deprecation_warning --no-cov -q`
Expected: FAIL — no warning emitted today.

- [ ] **Step 3: Nativize into `models/core.py`**

In `src/rhapsody_cli/models/core.py`:

- Replace `from rhapsody_cli import com_utils` with a guarded pywintypes import (next to the existing imports):

```python
try:
    import pywintypes  # type: ignore[import-untyped]
except ImportError:  # pragma: no cover - pywintypes is Windows-only
    pywintypes = None
```

- Add a module-level native function (place directly above `class AbstractRPModelElement`):

```python
def call_com(func: Callable[[], T]) -> T:
    """Invoke a COM call, translating COM errors into RhapsodyRuntimeException."""
    try:
        return func()
    except Exception as exc:
        if pywintypes is not None and isinstance(exc, pywintypes.com_error):
            raise RhapsodyRuntimeException(str(exc)) from exc
        raise
```

(Verify `Callable`, `T`, `RhapsodyRuntimeException` are already imported in `models/core.py` — `Callable`/`T` are used by the existing signatures; add to imports if missing.)

- Replace the three forwarding method bodies with native logic:

```python
    @classmethod
    def call_com(cls, func: Callable[[], T]) -> T:
        """Invoke a COM call, translating COM errors into RhapsodyRuntimeException."""
        return call_com(func)

    @classmethod
    def _get_method_or_property(cls, com_obj: Any, method_name: str, prop_name: str) -> Any:
        """Read ``method_name``/``prop_name`` preferring the Java-style method."""
        if hasattr(com_obj, method_name):
            return call_com(lambda: getattr(com_obj, method_name)())
        return call_com(lambda: getattr(com_obj, prop_name))

    @classmethod
    def _set_method_or_property(cls, com_obj: Any, method_name: str, prop_name: str, value: object) -> None:
        """Write ``value`` preferring the Java-style setter, else the property."""
        if hasattr(com_obj, method_name):
            call_com(lambda: getattr(com_obj, method_name)(value))
        else:
            call_com(lambda: setattr(com_obj, prop_name, value))
```

(Keep the existing docstrings of these methods; only the bodies and the "Forwards to..." lines change.)

- Remove the now-unused `from rhapsody_cli import com_utils` import.

- [ ] **Step 4: Migrate `application.py` and add deprecation shims**

- In `src/rhapsody_cli/application.py`:

  - Remove `from rhapsody_cli import com_utils`.
  - Add to the models import block: `from rhapsody_cli.models.core import RPCollection, call_com`.
  - Replace all 32 occurrences of `com_utils.call_com(` with `call_com(`.

- In `src/rhapsody_cli/com_utils.py`:

  - Prepend to the module docstring: `""".. deprecated:: Wrapper-internal COM helpers moved to :mod:`rhapsody_cli.models.core`. Kept for external compatibility; emits DeprecationWarning."""`
  - Add `import warnings` and emit a warning once per function call:

```python
def _warn_deprecated() -> None:
    warnings.warn(
        "rhapsody_cli.com_utils is deprecated; use rhapsody_cli.models.core.call_com",
        DeprecationWarning,
        stacklevel=3,
    )
```

  Call `_warn_deprecated()` as the first statement of `call_com`, `_get_method_or_property`, and `_set_method_or_property`.

- [ ] **Step 5: Verify behavior-identical + zero internal callers**

Run:
```bash
pytest tests/unit -q --no-cov
rg -n "com_utils" src/ --glob '!**/__pycache__/**'
rg -n "com_utils" src/rhapsody_cli/com_utils.py | wc -l
```
Expected: full unit suite PASS (1672+); the only `com_utils` references in `src/` outside `com_utils.py` itself are zero (first rg returns nothing).

- [ ] **Step 6: Run deprecation test to verify it passes, then commit**

Run: `pytest tests/unit/test_application.py::test_com_utils_functions_emit_deprecation_warning --no-cov -q`
Expected: PASS.

```bash
git add src/rhapsody_cli/models/core.py src/rhapsody_cli/application.py src/rhapsody_cli/com_utils.py tests/unit/test_application.py
git commit -m "refactor: nativize com_utils helpers into models.core; deprecate com_utils"
```

---

### Task 3: `early` branch in `_launch()`

**Files:**
- Modify: `src/rhapsody_cli/application.py`
- Test: `tests/unit/test_application.py`

**Interfaces:**
- Consumes: `_get_binding()` (Task 1), native `call_com` (Task 2).
- Produces: `_launch()` uses `win32com.client.gencache.EnsureDispatch(_PROG_ID)` when binding is `early`, `win32com.client.Dispatch(_PROG_ID)` when `dynamic`; identical `RhapsodyConnectionError` wrapping and `cls(com_obj)` return in both branches.

- [ ] **Step 1: Write the failing tests**

Append to `tests/unit/test_application.py`:

```python
class TestLaunchBinding:
    """Tests for the early/dynamic launch branches."""

    @patch("rhapsody_cli.application.win32com")
    def test_launch_uses_ensure_dispatch_when_early(self, mock_win32com: MagicMock) -> None:
        from rhapsody_cli import application as app_module

        fake_com = MagicMock(name="FakeApplication")
        mock_win32com.client.gencache.EnsureDispatch.return_value = fake_com

        with patch.dict(os.environ, {"RHAPSODY_COM_BINDING": "early"}):
            app = RhapsodyApplication._launch()

        mock_win32com.client.gencache.EnsureDispatch.assert_called_once_with("Rhapsody2.Application.1")
        assert app._com is fake_com

    @patch("rhapsody_cli.application.win32com")
    def test_launch_uses_dispatch_when_dynamic(self, mock_win32com: MagicMock) -> None:
        fake_com = MagicMock(name="FakeApplication")
        mock_win32com.client.Dispatch.return_value = fake_com

        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("RHAPSODY_COM_BINDING", None)
            app = RhapsodyApplication._launch()

        mock_win32com.client.Dispatch.assert_called_once_with("Rhapsody2.Application.1")
        mock_win32com.client.gencache.EnsureDispatch.assert_not_called()
        assert app._com is fake_com

    @pytest.mark.skipif(pywintypes is None, reason="pywintypes unavailable on this platform")
    @patch("rhapsody_cli.application.win32com")
    def test_launch_wraps_com_error_as_connection_error(self, mock_win32com: MagicMock) -> None:
        mock_win32com.client.Dispatch.side_effect = pywintypes.com_error(-2147352567, "boom", None, None)

        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("RHAPSODY_COM_BINDING", None)
            with pytest.raises(RhapsodyConnectionError, match="Failed to launch"):
                RhapsodyApplication._launch()
```

Note: add at the top of the test module:

```python
try:
    import pywintypes  # type: ignore[import-untyped]
except ImportError:  # pragma: no cover - Windows-only
    pywintypes = None
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `pytest tests/unit/test_application.py::TestLaunchBinding --no-cov -q`
Expected: FAIL — `_launch` currently calls `win32com.client.Dispatch` unconditionally, so `EnsureDispatch` is never called under `early` (first test fails); others may pass.

- [ ] **Step 3: Implement**

Replace the body of `_launch()` in `src/rhapsody_cli/application.py` (the com_error wrapping through `call_com` is now the native translation from Task 2, raised as `RhapsodyRuntimeException` and converted to `RhapsodyConnectionError` exactly as today):

```python
    def _launch(cls) -> "RhapsodyApplication":
        """Launch a new Rhapsody instance (internal helper).

        Uses typelib early binding (``EnsureDispatch``) when
        ``RHAPSODY_COM_BINDING=early``, dynamic binding otherwise.

        Returns:
            A RhapsodyApplication wrapping the newly launched COM object.

        Raises:
            RhapsodyConnectionError: If pywin32 is unavailable or launching
                Rhapsody fails.
        """
        if win32com is None:
            raise RhapsodyConnectionError("pywin32 is not available; Rhapsody automation requires Windows.")
        client = win32com.client
        try:
            if _get_binding() == "early":
                com_obj = call_com(lambda: client.gencache.EnsureDispatch(_PROG_ID))
            else:
                com_obj = call_com(lambda: client.Dispatch(_PROG_ID))
        except RhapsodyRuntimeException as exc:
            raise RhapsodyConnectionError(f"Failed to launch Rhapsody instance: {exc}") from exc
        return cls(com_obj)
```

(If accessing `client.gencache` fails at runtime because the plain `win32com.client` import does not expose `gencache`, add `import win32com.client.gencache` inside the guarded import block at the top of `application.py` next to `import win32com.client`.)

- [ ] **Step 4: Run the tests to verify they pass**

Run: `pytest tests/unit/test_application.py --no-cov -q`
Expected: all PASS (existing connect-lifecycle tests are unaffected — they patch `_launch`/`_attach` wholesale).

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/application.py tests/unit/test_application.py
git commit -m "feat: launch via EnsureDispatch under RHAPSODY_COM_BINDING=early"
```

---

### Task 4: `_attach()` binding invariance test

**Files:**
- Modify: `src/rhapsody_cli/application.py` (docstring only)
- Test: `tests/unit/test_application.py`

**Interfaces:**
- Consumes: `_get_binding()` (documented as intentionally NOT consulted here).
- Produces: explicit contract test — attach never launches and always uses `GetActiveObject`, regardless of binding.

- [ ] **Step 1: Write the test**

Append to `tests/unit/test_application.py`:

```python
class TestAttachBindingInvariance:
    """Attach always uses GetActiveObject regardless of binding (never launches)."""

    @patch("rhapsody_cli.application.win32com")
    def test_attach_uses_get_active_object_under_early(self, mock_win32com: MagicMock) -> None:
        fake_com = MagicMock(name="FakeApplication")
        mock_win32com.client.GetActiveObject.return_value = fake_com

        with patch.dict(os.environ, {"RHAPSODY_COM_BINDING": "early"}):
            app = RhapsodyApplication._attach()

        mock_win32com.client.GetActiveObject.assert_called_once_with("Rhapsody2.Application.1")
        assert app._com is fake_com
```

- [ ] **Step 2: Run to verify it passes against current code**

Run: `pytest tests/unit/test_application.py::TestAttachBindingInvariance --no-cov -q`
Expected: PASS immediately (`_attach` already only calls `GetActiveObject`). If it fails, `_attach` was modified — restore `GetActiveObject`-only behavior.

- [ ] **Step 3: Update the `_attach` docstring**

Add to the `_attach` docstring:

```python
        Binding note: attach intentionally ignores RHAPSODY_COM_BINDING and
        always uses dynamic GetActiveObject; attach must never launch a new
        instance. With a populated gen_py cache the returned object is
        early-bound automatically (documented pywin32 behavior).
```

- [ ] **Step 4: Run and commit**

Run: `pytest tests/unit/test_application.py --no-cov -q`
Expected: all PASS.

```bash
git add src/rhapsody_cli/application.py tests/unit/test_application.py
git commit -m "test: attach binding invariance (never launches)"
```

---

### Task 5: Documentation

**Files:**
- Modify: `CLAUDE.md`
- Modify: `docs/user_guide/cli_tools.rst`

- [ ] **Step 1: CLAUDE.md — binding + deprecation sections**

Insert after the "### Layer 2 — Application Entry Point" block (before "### Layer 3"):

```markdown
### COM Binding (`RHAPSODY_COM_BINDING`) and com_utils deprecation

`RhapsodyApplication` supports two COM bindings, selected by the
`RHAPSODY_COM_BINDING` environment variable at connect time:

- `dynamic` (default until early-binding parity is proven) —
  `Dispatch`/`GetActiveObject`; members resolve by name at runtime.
- `early` — `gencache.EnsureDispatch` for launches; typelib-typed objects with
  fail-fast member access.

Property-style access (e.g. `name` instead of `getName()`) is required under
**both** bindings on `Rhapsody2.Application.1` — the native helpers
(`AbstractRPModelElement.call_com`/`_get_method_or_property`/`_set_method_or_property`
in `models/core.py`) handle this and must not be bypassed. `_attach` never
launches regardless of binding.

`rhapsody_cli.com_utils` is **deprecated** (emits `DeprecationWarning`; kept
only for external compatibility — internal code uses `models.core.call_com`).
The gen_py cache (`%TEMP%\gen_py\3.9\<typelib-guid>`) is machine-global; after
a Rhapsody upgrade clear it via `win32com.client.gencache.Rebuild()` or by
deleting the GUID folder.
```

- [ ] **Step 2: user guide — env-var + deprecation note**

In `docs/user_guide/cli_tools.rst`, under `Global Options`, append:

```rst
COM Binding
~~~~~~~~~~~

Set ``RHAPSODY_COM_BINDING=early`` before connecting to use typelib early
binding (``EnsureDispatch``); the default is ``dynamic``. Early binding gives
fail-fast member access at the cost of a generated cache under
``%TEMP%\gen_py``; after upgrading Rhapsody, clear that cache (or run
``win32com.client.gencache.Rebuild()``) if member access behaves unexpectedly.

``rhapsody_cli.com_utils`` is deprecated; use
``rhapsody_cli.models.core.call_com`` instead.
```

- [ ] **Step 3: Verify + commit**

Run: `rg -n "RHAPSODY_COM_BINDING|com_utils" CLAUDE.md docs/user_guide/cli_tools.rst`
Expected: present in both files.

```bash
git add CLAUDE.md docs/user_guide/cli_tools.rst
git commit -m "docs: document RHAPSODY_COM_BINDING and com_utils deprecation"
```

---

### Task 6: Quality gate

**Files:** possibly any flagged file.

- [ ] **Step 1: Run the gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit -q`
Expected: all green. Watch for: `os` import placement (ruff I), `pywintypes` guarded import (mypy: `# type: ignore[import-untyped]`), unused imports after migration (ruff F401).

- [ ] **Step 2: Fix and commit if needed**

```bash
git add -A && git commit -m "chore: pass quality gate after binding switch"
```

(Skip if nothing was flagged.)

---

### Task 7: Live spike — go/no-go (Windows + Rhapsody)

**Files:**
- Modify: this plan file (record results).

**Interfaces:**
- Consumes: `RHAPSODY_COM_BINDING=early`; scratch project; every wrapper member the actions/exchange rely on.

- [ ] **Step 1: Run the member-inventory spike**

```bash
set RHAPSODY_COM_BINDING=early
rhapsody-cli connect --no-gui
rhapsody-cli project new build/binding-spike SpikeProj
rhapsody-cli package create '{"name": "Sensors"}'
rhapsody-cli class create --path Sensors '{"name": "ProbeClass"}'
rhapsody-cli class view --path Sensors/ProbeClass --format json
rhapsody-cli package list --path Sensors
rhapsody-cli class link --path Sensors/ProbeClass --add ProbeClass
rhapsody-cli export --file build/binding-spike/spike.yaml
rhapsody-cli import --path Sensors --file build/binding-spike/spike.yaml
rhapsody-cli disconnect
```

Expected: all exit 0 (or the known `import` generalization behavior); `class view` returns full JSON; export produces non-empty YAML.

- [ ] **Step 2: Go/no-go**

Any member failing under `early` that works under `dynamic` (retry the failing command with `RHAPSODY_COM_BINDING=dynamic` to confirm) and not fixable by the property fallback → **STOP**: record the divergence in this plan, keep `dynamic` default, and report back for design revision. If all pass → continue to Task 8.

- [ ] **Step 3: Record the spike result**

Append to this plan: spike date, Rhapsody version, per-command results.

---

### Task 8: Live smoke — 26-command checklist under early

**Files:**
- Modify: this plan file (append results).

- [ ] **Step 1: Run the full checklist**

Run the 26-command checklist from
`docs/superpowers/plans/2026-11-19-cli-simplification.md` (Execution Results
section) with `RHAPSODY_COM_BINDING=early` exported for every invocation, on a
fresh scratch project.

- [ ] **Step 2: Record and commit**

Append the early-binding results table + date + Rhapsody version to this plan.

```bash
git add docs/superpowers/plans/2026-11-19-com-binding-switch.md
git commit -m "test: record early-binding live smoke results"
```

---

### Task 9: Default flip (conditional on Tasks 7-8 green)

**Files:**
- Modify: `src/rhapsody_cli/application.py`
- Test: `tests/unit/test_application.py`

- [ ] **Step 1: Flip the default**

In `_get_binding()`, change the unset/empty fallback:

```python
    value = os.environ.get(_BINDING_ENV, "").strip().lower()
    if value == "dynamic":
        return "dynamic"
    if value == "early" or value == "":
        return "early"
    logger.warning("Unknown %s value '%s'; using early binding", _BINDING_ENV, value)
    return "early"
```

- [ ] **Step 2: Update the tests**

Update `TestGetBinding`: unset -> `"early"`; invalid value -> `"early"`; `"dynamic"` explicit -> `"dynamic"`; `"early"` variants -> `"early"`. Update Task 3's dynamic test to set `RHAPSODY_COM_BINDING=dynamic` explicitly instead of popping it. Update CLAUDE.md/user-guide wording: `early` is the default, `dynamic` the escape hatch.

- [ ] **Step 3: Full gate + live control run**

Run the quality gate, then one control pass of the smoke checklist with
`RHAPSODY_COM_BINDING=dynamic` to confirm the escape hatch still works.

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "feat: make early binding the default (dynamic remains escape hatch)"
```

If Tasks 7-8 were not green, skip Task 9 entirely and record why in the plan.

---

## Self-Review Notes

- Spec coverage + user directive: env reader (Task 1), com_utils obsoletion (Task 2 — user directive "keep the file, do not call any function in it"; zero internal callers enforced by grep gate), launch branch (Task 3, consumes native `call_com`), attach invariance (Task 4), docs incl. deprecation note (Task 5), gate (Task 6), spike go/no-go (Task 7), smoke gate (Task 8), conditional default flip (Task 9).
- Behavior safety: Task 2 is a behavior-identical move — the full unit suite (1672+) passing unchanged is the gate, because every wrapper test routes through the nativized base methods.
- Type consistency: `_get_binding() -> str`; native `call_com(func: Callable[[], T]) -> T` mirrors the deprecated shim's signature; tests patch `rhapsody_cli.application.win32com` (platform-safe); `pywintypes` guarded + skipif.
