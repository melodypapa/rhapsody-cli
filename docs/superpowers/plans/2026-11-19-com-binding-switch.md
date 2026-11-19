# COM Binding Switch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an opt-in `EnsureDispatch` early-binding mode, guarantee all returned model COM objects are gen_py typed objects in that mode, validate wrapper parity on live Rhapsody, and flip the default to early only if all typed-object and command smoke gates pass.

**Architecture:** Changes are limited to `src/rhapsody_cli/application.py`, docs, and tests. Existing `models/`, `com_utils.py`, wrappers, CLI and actions remain unchanged and continue to be used. `_launch()` chooses `EnsureDispatch(prog_id)` or `Dispatch(prog_id)`; `_attach()` first obtains the running object via `GetActiveObject` (so it never launches), then in early mode passes that acquired object to `EnsureDispatch(raw_dispatch)` to generate/apply typed wrappers without a ProgID launch. Model wrappers continue exposing snake_case methods around the underlying COM objects.

**Tech Stack:** Python 3.8+, pywin32 (`win32com.client.gencache.EnsureDispatch`), pytest + `unittest.mock`, live IBM Rhapsody 10.0.3 (Windows) for typed-object spike and smoke.

**Spec:** `docs/superpowers/specs/2026-11-19-com-binding-switch-design.md`

## Global Constraints

- Branch: `docs/com-binding-switch` (spec branch, non-main). Never commit to `main`.
- No refactor of `models/`, `com_utils.py`, CLI, or actions; these layers and their current interfaces stay active and unchanged.
- Python 3.8 compatible; no `from __future__ import annotations`, no PEP 604 unions, no `Any` in new annotations.
- Quality gate: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`.
- No real COM in unit tests; patch `rhapsody_cli.application.win32com`.
- Live checks require licensed Rhapsody on Windows; use scratch projects and clean them afterward.
- `early` must not be considered successful unless project, package, class, component, and collection-element `_com` objects are from `win32com.gen_py` and wrapper operations succeed on them.
- Commit style: conventional commits; no AI attribution.

---

### Task 1: Add `_get_binding()` and unit tests

**Files:**
- Modify: `src/rhapsody_cli/application.py`
- Test: `tests/unit/test_application.py`

**Produces:** `_get_binding() -> str`, read at connect time. Unset/empty/`dynamic` -> `"dynamic"`; case-insensitive `early` -> `"early"`; invalid -> warning + `"dynamic"`.

- [ ] **Step 1: Write tests first**

Add `import os` to test imports, then append:

```python
class TestGetBinding:
    def test_default_is_dynamic_when_unset(self) -> None:
        from rhapsody_cli.application import _get_binding
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("RHAPSODY_COM_BINDING", None)
            assert _get_binding() == "dynamic"

    def test_early_is_case_insensitive(self) -> None:
        from rhapsody_cli.application import _get_binding
        for value in ("early", "EARLY", "Early"):
            with patch.dict(os.environ, {"RHAPSODY_COM_BINDING": value}):
                assert _get_binding() == "early"

    def test_dynamic_can_be_selected_explicitly(self) -> None:
        from rhapsody_cli.application import _get_binding
        with patch.dict(os.environ, {"RHAPSODY_COM_BINDING": "DYNAMIC"}):
            assert _get_binding() == "dynamic"

    def test_invalid_value_warns_and_falls_back(self, caplog: pytest.LogCaptureFixture) -> None:
        from rhapsody_cli.application import _get_binding
        with patch.dict(os.environ, {"RHAPSODY_COM_BINDING": "bogus"}):
            assert _get_binding() == "dynamic"
        assert "Unknown RHAPSODY_COM_BINDING" in caplog.text
```

- [ ] **Step 2: Verify red**

Run: `pytest tests/unit/test_application.py::TestGetBinding --no-cov -q`
Expected: 4 failures because `_get_binding` does not yet exist.

- [ ] **Step 3: Implement**

In `application.py`, add `import os` and after `_PROG_ID`:

```python
_BINDING_ENV = "RHAPSODY_COM_BINDING"


def _get_binding() -> str:
    """Return the binding requested by RHAPSODY_COM_BINDING."""
    value = os.environ.get(_BINDING_ENV, "").strip().lower()
    if value == "early":
        return "early"
    if value in ("", "dynamic"):
        return "dynamic"
    logger.warning("Unknown %s value '%s'; using dynamic binding", _BINDING_ENV, value)
    return "dynamic"
```

- [ ] **Step 4: Verify green and commit**

Run: `pytest tests/unit/test_application.py::TestGetBinding --no-cov -q` — expected 4 passed.

```bash
git add src/rhapsody_cli/application.py tests/unit/test_application.py
git commit -m "feat: add RHAPSODY_COM_BINDING selection"
```

---

### Task 2: Use EnsureDispatch on launch when early

**Files:**
- Modify: `src/rhapsody_cli/application.py`
- Test: `tests/unit/test_application.py`

**Produces:** `_launch()` selects `EnsureDispatch(_PROG_ID)` for `early`, `Dispatch(_PROG_ID)` otherwise; existing `call_com` error translation and `RhapsodyConnectionError` handling remain unchanged.

- [ ] **Step 1: Add failing tests**

Append:

```python
class TestLaunchBinding:
    @patch("rhapsody_cli.application.win32com")
    def test_early_uses_ensure_dispatch(self, mock_win32com: MagicMock) -> None:
        fake_com = MagicMock(name="EarlyApplication")
        mock_win32com.client.gencache.EnsureDispatch.return_value = fake_com
        with patch.dict(os.environ, {"RHAPSODY_COM_BINDING": "early"}):
            app = RhapsodyApplication._launch()
        mock_win32com.client.gencache.EnsureDispatch.assert_called_once_with("Rhapsody2.Application.1")
        mock_win32com.client.Dispatch.assert_not_called()
        assert app._com is fake_com

    @patch("rhapsody_cli.application.win32com")
    def test_dynamic_uses_dispatch(self, mock_win32com: MagicMock) -> None:
        fake_com = MagicMock(name="DynamicApplication")
        mock_win32com.client.Dispatch.return_value = fake_com
        with patch.dict(os.environ, {"RHAPSODY_COM_BINDING": "dynamic"}):
            app = RhapsodyApplication._launch()
        mock_win32com.client.Dispatch.assert_called_once_with("Rhapsody2.Application.1")
        mock_win32com.client.gencache.EnsureDispatch.assert_not_called()
        assert app._com is fake_com
```

- [ ] **Step 2: Verify red**

Run: `pytest tests/unit/test_application.py::TestLaunchBinding --no-cov -q`
Expected: early test fails because `_launch` currently always uses `Dispatch`.

- [ ] **Step 3: Implement**

In `_launch`, keep the existing pywin32 guard and exception handling, but branch inside the `try`:

```python
            if _get_binding() == "early":
                com_obj = com_utils.call_com(lambda: win32com.client.gencache.EnsureDispatch(_PROG_ID))
            else:
                com_obj = com_utils.call_com(lambda: win32com.client.Dispatch(_PROG_ID))
```

If `client.gencache` is not present through the normal guarded import, import `win32com.client.gencache` inside the same guarded import block and call it through that imported module. Do not change `com_utils` or any model wrapper.

- [ ] **Step 4: Verify and commit**

Run: `pytest tests/unit/test_application.py --no-cov -q` — expected all pass.

```bash
git add src/rhapsody_cli/application.py tests/unit/test_application.py
git commit -m "feat: use EnsureDispatch for early-bound Rhapsody launches"
```

---

### Task 3: Early attach must return typed objects without launching

**Files:**
- Modify: `src/rhapsody_cli/application.py`
- Test: `tests/unit/test_application.py`

**Produces:** `_attach()` always starts with `GetActiveObject(_PROG_ID)`. In dynamic mode it returns that object unchanged; in early mode it calls `EnsureDispatch(raw_com_object)` on the already-acquired object. Never call `EnsureDispatch(_PROG_ID)` from `_attach`, since that can launch.

- [ ] **Step 1: Write tests first**

Append:

```python
class TestAttachBinding:
    @patch("rhapsody_cli.application.win32com")
    def test_dynamic_attach_returns_get_active_object(self, mock_win32com: MagicMock) -> None:
        raw = MagicMock(name="RawDynamicApplication")
        mock_win32com.client.GetActiveObject.return_value = raw
        with patch.dict(os.environ, {"RHAPSODY_COM_BINDING": "dynamic"}):
            app = RhapsodyApplication._attach()
        mock_win32com.client.GetActiveObject.assert_called_once_with("Rhapsody2.Application.1")
        mock_win32com.client.gencache.EnsureDispatch.assert_not_called()
        assert app._com is raw

    @patch("rhapsody_cli.application.win32com")
    def test_early_attach_types_existing_object_without_launch(self, mock_win32com: MagicMock) -> None:
        raw = MagicMock(name="AlreadyRunningApplication")
        typed = MagicMock(name="TypedApplication")
        mock_win32com.client.GetActiveObject.return_value = raw
        mock_win32com.client.gencache.EnsureDispatch.return_value = typed
        with patch.dict(os.environ, {"RHAPSODY_COM_BINDING": "early"}):
            app = RhapsodyApplication._attach()
        mock_win32com.client.GetActiveObject.assert_called_once_with("Rhapsody2.Application.1")
        mock_win32com.client.gencache.EnsureDispatch.assert_called_once_with(raw)
        mock_win32com.client.Dispatch.assert_not_called()
        assert app._com is typed
```

- [ ] **Step 2: Verify red**

Run: `pytest tests/unit/test_application.py::TestAttachBinding --no-cov -q`
Expected: early test fails because `_attach` currently returns the raw object.

- [ ] **Step 3: Implement**

In `_attach()`, preserve the current `GetActiveObject` call and error translation. After acquisition:

```python
        if _get_binding() == "early":
            com_obj = win32com.client.gencache.EnsureDispatch(com_obj)
        return cls(com_obj)
```

Do not pass `_PROG_ID` to `EnsureDispatch` from `_attach`; only pass the COM object already returned by `GetActiveObject`.

- [ ] **Step 4: Verify and commit**

Run: `pytest tests/unit/test_application.py --no-cov -q` — expected all pass.

```bash
git add src/rhapsody_cli/application.py tests/unit/test_application.py
git commit -m "feat: EnsureDispatch existing application on early attach without launching"
```

---

### Task 4: Document binding selection and cache recovery

**Files:**
- Modify: `CLAUDE.md`
- Modify: `docs/user_guide/cli_tools.rst`

- [ ] **Step 1: Document in CLAUDE.md**

Add a `### COM Binding (RHAPSODY_COM_BINDING)` section after the application-layer section and before the CLI-layer section. State: `dynamic` default until the live parity gate; `early` uses EnsureDispatch on launch and on an already-acquired GetActiveObject during attach; models/core, wrappers, com_utils, CLI and actions are unchanged; property access fallback remains required; cache location and rebuild/delete recovery after Rhapsody upgrades.

- [ ] **Step 2: Document in the user guide**

Add a `COM Binding` subsection under the global options section in `docs/user_guide/cli_tools.rst` describing `RHAPSODY_COM_BINDING=early`, the dynamic default, gen_py cache and remediation.

- [ ] **Step 3: Verify documentation and commit**

Run: `rg -n "RHAPSODY_COM_BINDING|EnsureDispatch|gencache.Rebuild" CLAUDE.md docs/user_guide/cli_tools.rst` — expected matches in both docs.

```bash
git add CLAUDE.md docs/user_guide/cli_tools.rst
git commit -m "docs: explain early COM binding and gen_py cache recovery"
```

---

### Task 5: Unit suite and quality gate

**Files:**
- No planned source changes; fix only findings caused by Tasks 1-4.

- [ ] **Step 1: Run the complete gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit -q`
Expected: all green. `win32com` remains guarded on non-Windows; mock tests never call real COM.

- [ ] **Step 2: If needed, fix and commit**

Only fix failures caused by this change; do not make unrelated style/API changes.

```bash
git add <specific changed files>
git commit -m "fix: resolve early binding unit and type-check issues"
```

---

### Task 6: Live typed-object spike (go/no-go; Windows + licensed Rhapsody)

**Files:**
- Create temporarily: `build/probe_early_binding.py` (delete after run)
- Modify: this plan (record results)

- [ ] **Step 1: Create an isolated scratch project**

Set `RHAPSODY_COM_BINDING=early`, connect/attach to Rhapsody 10.0.3, and create a fresh scratch project under `build/early-binding-spike/`. Never open or modify user models.

- [ ] **Step 2: Assert typedness across returned model objects**

Through the existing wrapper API, obtain a project, package, class, component, a `RPCollection`, and elements retrieved from that collection. For every wrapper, inspect its underlying `_com` and assert:

```python
assert type(wrapper._com).__module__.startswith("win32com.gen_py")
```

Also verify the active application `_com` and the raw active project/component/package objects returned from COM are gen_py generated types. Record each runtime type/module in the plan.

- [ ] **Step 3: Exercise wrapper access and mutation**

Using the existing snake_case APIs (do not change wrappers): `get_name`, `get_meta_class`, `add_nested_package`, `get_nested_packages`, `add_class`, `get_classes`, `add_generalization`, `find_nested_element_recursive`, `add_component`, `get_components`, collection iteration/indexing. Each should work while the underlying `_com` objects remain gen_py typed.

- [ ] **Step 4: Go/no-go**

Any returned model object is not gen_py typed, or any wrapper operation that succeeds under `dynamic` fails under `early` → STOP; do not flip the default. Record element type, member, error, and dynamic control result in this plan. Ask for design revision before broad smoke. If all typedness and member checks pass, continue to Task 7.

- [ ] **Step 5: Clean scratch project and record results**

Close the project, disconnect, remove `build/early-binding-spike/`, and record Rhapsody version + runtime types + pass/fail.

---

### Task 7: Full live CLI smoke under early binding

**Files:**
- Modify: this plan (append results)

- [ ] **Step 1: Run all 26 commands**

Use the 26-command checklist in `docs/superpowers/plans/2026-11-19-cli-simplification.md` (Execution Results section), with `RHAPSODY_COM_BINDING=early` for **each** CLI invocation. Use a fresh scratch project; do not touch user models. All kept `connect`/`project`/`package`/`class`/`export`/`import` commands plus suspended-command behavior must match the dynamic results.

- [ ] **Step 2: Record results**

Append a per-command PASS/FAIL table, Rhapsody version, and any COM type signatures. If any smoke check fails, retry that exact command with `RHAPSODY_COM_BINDING=dynamic` to distinguish a binding regression from an existing issue. No default flip unless every required command passes.

- [ ] **Step 3: Commit results**

```bash
git add docs/superpowers/plans/2026-11-19-com-binding-switch.md
git commit -m "test: record early-binding typed-object and CLI smoke results"
```

---

### Task 8: Flip the default only after both live gates pass

**Files:**
- Modify: `src/rhapsody_cli/application.py`
- Test: `tests/unit/test_application.py`
- Modify docs from Task 4

- [ ] **Step 1: Change `_get_binding()` default**

Only if Tasks 6-7 are fully green, change unset/empty and invalid values to `early`; explicit `RHAPSODY_COM_BINDING=dynamic` remains a rollback escape hatch. If either live gate has a failure or untyped object, do not flip.

- [ ] **Step 2: Update tests/docs**

Update env-var tests so unset/empty -> `early`, explicit `dynamic` -> `dynamic`, and invalid -> warning + `early`. Update CLAUDE.md/user guide to state early is default and dynamic is the escape hatch.

- [ ] **Step 3: Verify**

Run the full quality gate and one control smoke pass with `RHAPSODY_COM_BINDING=dynamic` to prove rollback mode still works.

- [ ] **Step 4: Commit**

```bash
git add src/rhapsody_cli/application.py tests/unit/test_application.py CLAUDE.md docs/user_guide/cli_tools.rst
git commit -m "feat: make typed EnsureDispatch binding the default"
```

## Self-Review Notes

- User constraints: no model/wrapper refactor; keep and continue using `com_utils.py`; CLI and actions keep their existing wrapper objects; every underlying model COM object must be gen_py typed in early mode. Tasks 1-4 meet these constraints; Task 6 makes typedness an explicit pass/fail gate.
- Attach safety: `GetActiveObject` occurs before EnsureDispatch and the acquired object—not the ProgID—is passed into EnsureDispatch, so early attach cannot launch a new instance.
- Spec coverage: binding selection, launch, attach, cache docs, live typed object gate, full smoke and conditional default flip are all covered.
- No com_utils nativization/deprecation task: user explicitly disallowed model-layer refactoring and said to keep model objects/com_utils in use; com_utils therefore remains unchanged and is expected to have internal callers.
