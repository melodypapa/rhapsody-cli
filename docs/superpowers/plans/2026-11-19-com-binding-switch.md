# COM Binding Switch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the COM binding switchable via `RHAPSODY_COM_BINDING` (`dynamic` default, `early` opt-in) so `EnsureDispatch` early-bound objects can be validated against the full live workload before any default flip.

**Architecture:** All changes are in `src/rhapsody_cli/application.py`: a `_get_binding()` env-var reader, an `early` branch in `_launch()` that calls `gencache.EnsureDispatch`, and `_attach()` unchanged (always `GetActiveObject` — attach must never launch). Wrappers, `com_utils.py`, CLI, and actions are untouched (spec Non-Goals); the property-style fallback in `com_utils._get_method_or_property` behaves identically under both bindings (probe-verified).

**Tech Stack:** Python 3.8+, pywin32 (`win32com.client.gencache.EnsureDispatch`), pytest + `unittest.mock`, live IBM Rhapsody 10.0.3 (Windows) for Tasks 6-7.

**Spec:** `docs/superpowers/specs/2026-11-19-com-binding-switch-design.md`

## Global Constraints

- Branch: `docs/com-binding-switch` (spec commit already on it). Never commit to `main`.
- Python 3.8 compatible (`typing.Optional`/`Dict`; no PEP 604 unions, no `from __future__ import annotations`, no `Any` in annotations).
- Quality gate before every "done" claim: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
- No real COM in unit tests — patch `rhapsody_cli.application.win32com` (module-level name inside `application.py`, platform-safe).
- snake_case public API stays; `com_utils.py` unchanged; CLI/actions unchanged (spec Non-Goals).
- Commit style: conventional commits, no AI attribution.
- Live tasks (6-7) require Windows + licensed Rhapsody 10.0.3; scratch projects only, cleaned up afterward.

---

### Task 1: `_get_binding()` env-var reader

**Files:**
- Modify: `src/rhapsody_cli/application.py`
- Test: `tests/unit/test_application.py`

**Interfaces:**
- Produces: `_get_binding() -> str` module-level function returning `"dynamic"` or `"early"`. Behavior: unset/empty -> `"dynamic"`; `"early"`/`"EARLY"`/`"Early"` -> `"early"` (case-insensitive); `"dynamic"`/`"DYNAMIC"` -> `"dynamic"`; any other value -> log warning via module `logger` and return `"dynamic"`. Read at call time (not import time). Task 2 consumes it inside `_launch()`.

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

    def test_invalid_value_falls_back_to_dynamic(self, capsys: pytest.CaptureFixture[str]) -> None:
        from rhapsody_cli.application import _get_binding

        with patch.dict(os.environ, {"RHAPSODY_COM_BINDING": "bogus"}):
            assert _get_binding() == "dynamic"
```

Note: `import os` and `import pytest` must exist at the top of the file (pytest already imported; add `os` if missing).

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

Also add `import os` to the stdlib import block at the top of the file (before `from typing import ...`; keep ruff/isort order).

- [ ] **Step 4: Run the tests to verify they pass**

Run: `pytest tests/unit/test_application.py::TestGetBinding --no-cov -q`
Expected: 4 PASS.

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/application.py tests/unit/test_application.py
git commit -m "feat: add RHAPSODY_COM_BINDING env-var binding reader"
```

---

### Task 2: `early` branch in `_launch()`

**Files:**
- Modify: `src/rhapsody_cli/application.py`
- Test: `tests/unit/test_application.py`

**Interfaces:**
- Consumes: `_get_binding()` (Task 1).
- Produces: `_launch()` uses `win32com.client.gencache.EnsureDispatch(_PROG_ID)` when binding is `early`, `win32com.client.Dispatch(_PROG_ID)` when `dynamic`; identical `RhapsodyConnectionError` wrapping and `cls(com_obj)` return in both branches. `connect(show_gui=...)` behavior unchanged.

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

    @patch("rhapsody_cli.application.win32com")
    def test_launch_wraps_com_error_as_connection_error(self, mock_win32com: MagicMock) -> None:
        import pywintypes

        mock_win32com.client.Dispatch.side_effect = pywintypes.com_error(-2147352567, "boom", None, None)

        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("RHAPSODY_COM_BINDING", None)
            with pytest.raises(RhapsodyConnectionError, match="Failed to launch"):
                RhapsodyApplication._launch()
```

Note: `pywintypes` is import-guarded in `application.py`; in tests import it directly (available on Windows; on non-Windows CI this one test must be skipped — wrap with `@pytest.mark.skipif(pywintypes is None)` logic: add at top of the test module `try: import pywintypes except ImportError: pywintypes = None` and decorate: `@pytest.mark.skipif(pywintypes is None, reason="pywintypes unavailable")`).

- [ ] **Step 2: Run the tests to verify they fail**

Run: `pytest tests/unit/test_application.py::TestLaunchBinding --no-cov -q`
Expected: FAIL — `_launch` currently calls `win32com.client.Dispatch` unconditionally, so `EnsureDispatch` is never called under `early` (first test fails); others may pass.

- [ ] **Step 3: Implement**

Replace the body of `_launch()` in `src/rhapsody_cli/application.py`:

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
                com_obj = com_utils.call_com(lambda: client.gencache.EnsureDispatch(_PROG_ID))
            else:
                com_obj = com_utils.call_com(lambda: client.Dispatch(_PROG_ID))
        except RhapsodyRuntimeException as exc:
            raise RhapsodyConnectionError(f"Failed to launch Rhapsody instance: {exc}") from exc
        return cls(com_obj)
```

(Note: `client.gencache` — `gencache` is a submodule of `win32com.client`; accessing it through the mocked client in tests mirrors the real attribute path. If the plain `Dispatch` import path does not expose `gencache` at runtime, add `import win32com.client.gencache` inside the guarded import block at the top of `application.py` next to `import win32com.client` so the attribute exists unconditionally.)

- [ ] **Step 4: Run the tests to verify they pass**

Run: `pytest tests/unit/test_application.py --no-cov -q`
Expected: all PASS (existing connect-lifecycle tests are unaffected — they patch `_launch`/`_attach` wholesale).

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/application.py tests/unit/test_application.py
git commit -m "feat: launch via EnsureDispatch under RHAPSODY_COM_BINDING=early"
```

---

### Task 3: `_attach()` binding invariance test

**Files:**
- Modify: `src/rhapsody_cli/application.py` (docstring only)
- Test: `tests/unit/test_application.py`

**Interfaces:**
- Consumes: `_get_binding()` (documented as intentionally NOT consulted here).
- Produces: explicit contract test — attach never launches and always uses `GetActiveObject`, regardless of binding.

- [ ] **Step 1: Write the failing test**

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
        mock_win32com.client.gencache.EnsureDispatch.assert_not_called()
        assert app._com is fake_com
```

- [ ] **Step 2: Run to verify it passes against current code**

Run: `pytest tests/unit/test_application.py::TestAttachBindingInvariance --no-cov -q`
Expected: PASS immediately (`_attach` already only calls `GetActiveObject`; `gencache.EnsureDispatch` is not referenced there, so `assert_not_called` holds on the mock). If it fails, `_attach` was modified — restore `GetActiveObject`-only behavior.

- [ ] **Step 3: Update the `_attach` docstring**

Add one line to the `_attach` docstring (after the existing description):

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

### Task 4: Documentation

**Files:**
- Modify: `CLAUDE.md`
- Modify: `docs/user_guide/cli_tools.rst`

- [ ] **Step 1: CLAUDE.md — add binding section**

Insert after the "### Layer 2 — Application Entry Point" block (before "### Layer 3"):

```markdown
### COM Binding (`RHAPSODY_COM_BINDING`)

`RhapsodyApplication` supports two COM bindings, selected by the
`RHAPSODY_COM_BINDING` environment variable at connect time:

- `dynamic` (default) — `Dispatch`/`GetActiveObject`; members resolve by name
  at runtime.
- `early` — `gencache.EnsureDispatch` for launches; typelib-typed objects with
  fail-fast member access.

Property-style access (e.g. `name` instead of `getName()`) is required under
**both** bindings on `Rhapsody2.Application.1` — `com_utils._get_method_or_property`
handles this and must not be bypassed. `_attach` never launches regardless of
binding. The gen_py cache (`%TEMP%\gen_py\3.9\<typelib-guid>`) is machine-global;
after a Rhapsody upgrade clear it via `win32com.client.gencache.Rebuild()` or by
deleting the GUID folder.
```

- [ ] **Step 2: user guide — add env-var note**

In `docs/user_guide/cli_tools.rst`, under `Global Options` section, append:

```rst
COM Binding
~~~~~~~~~~~

Set ``RHAPSODY_COM_BINDING=early`` before connecting to use typelib early
binding (``EnsureDispatch``); the default is ``dynamic``. Early binding gives
fail-fast member access at the cost of a generated cache under
``%TEMP%\gen_py``; after upgrading Rhapsody, clear that cache (or run
``win32com.client.gencache.Rebuild()``) if member access behaves unexpectedly.
```

- [ ] **Step 3: Verify + commit**

Run: `rg -n "RHAPSODY_COM_BINDING" CLAUDE.md docs/user_guide/cli_tools.rst`
Expected: present in both files.

```bash
git add CLAUDE.md docs/user_guide/cli_tools.rst
git commit -m "docs: document RHAPSODY_COM_BINDING and gen_py cache remediation"
```

---

### Task 5: Quality gate

**Files:** possibly any flagged file.

- [ ] **Step 1: Run the gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit -q`
Expected: all green. Watch for: `os` import placement (ruff I), `pywintypes` import guard in tests (mypy strict: annotate as `Optional[module]` with `# type: ignore[import-untyped]` per repo convention).

- [ ] **Step 2: Fix and commit if needed**

```bash
git add -A && git commit -m "chore: pass quality gate after binding switch"
```

(Skip if nothing was flagged.)

---

### Task 6: Live spike — go/no-go (Windows + Rhapsody)

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

Any member failing under `early` that works under `dynamic` (retry the failing command with `RHAPSODY_COM_BINDING=dynamic` to confirm) and not fixable by the property fallback → **STOP**: record the divergence in this plan, keep `dynamic` default, and report back for design revision. If all pass → continue to Task 7.

- [ ] **Step 3: Record the spike result**

Append to this plan: spike date, Rhapsody version, per-command results.

---

### Task 7: Live smoke — 26-command checklist under early

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

### Task 8: Default flip (conditional on Tasks 6-7 green)

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

Update `TestGetBinding`: unset -> `"early"`; invalid value -> `"early"`; `"dynamic"` explicit -> `"dynamic"`; `"early"` variants -> `"early"`. Update Task 2's dynamic test to set `RHAPSODY_COM_BINDING=dynamic` explicitly instead of popping it. Update CLAUDE.md/user-guide wording: `early` is the default, `dynamic` the escape hatch.

- [ ] **Step 3: Full gate + live control run**

Run the quality gate, then one control pass of the smoke checklist with
`RHAPSODY_COM_BINDING=dynamic` to confirm the escape hatch still works.

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "feat: make early binding the default (dynamic remains escape hatch)"
```

If Tasks 6-7 were not green, skip Task 8 entirely and record why in the plan.

---

## Self-Review Notes

- Spec coverage: env reader (Task 1), launch branch (Task 2), attach invariance (Task 3), docs (Task 4), gate (Task 5), spike go/no-go (Task 6), smoke gate (Task 7), conditional default flip (Task 8) — matches spec §1-§5.
- Type consistency: `_get_binding() -> str`; tests patch `rhapsody_cli.application.win32com` (module-level name — works on Windows and CI where the guarded import yields None); `pywintypes` com_error test guarded by skipif.
- Non-Goals respected: no changes to `com_utils.py`, wrappers, CLI, or actions.
