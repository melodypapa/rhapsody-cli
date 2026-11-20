# COM Boundary Hardening, Wrapper Refactor, and Live API Audit — Combined Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use `- [ ]` checkboxes.

**Status:** Active. Combines and supersedes the three 2026-11-20 plans: `2026-11-20-com-utils-hardening.md`, `2026-11-20-remove-abstract-model-element.md`, and `2026-11-20-live-com-api-parity-test.md`. Those files are deleted from the working tree; the committed one remains in git history. It also supersedes `2026-11-19-com-binding-switch.md` (abandoned — no `EnsureDispatch` switch).

**Goal:** Harden the single COM boundary (`com_utils.call_com`) with structured error translation, HRESULT-classified bounded retry, portable COM error fakes, and optional STA apartments; then remove the `AbstractRPModelElement` base class by moving its registry/factory to module-level functions in `models/core.py` and its COM helpers to a `ComHelpers` mixin; finally add a Windows-only live integration test that audits a wrapper class definition against the COM object's real member inventory.

**Architecture:** Phase A changes `com_utils.py`, `exceptions/core.py`, `fakes.py`, `test_com_utils.py`, `pyproject.toml`, and CLAUDE.md only. Phase B changes `models/core.py`, wrapper call sites, tests, exports, and docs; the new module-level `wrap`/`register_wrapper` are the source of truth while `RPModelElement` exposes thin staticmethod aliases so ~600 `self.*` helper calls need no edits. Phase C is audit-only: all new code lives under `tests/integration/` plus one test-spec section — no production changes and no javadoc dependency (the live COM inventory is the comparison source). `call_com(func)` keeps its signature, so every existing call site benefits from retry with zero edits. The existing `Any` return on `_get_method_or_property` is preserved verbatim.

**Tech Stack:** Python 3.8+, pywin32 (`pywintypes.com_error`, `pythoncom`, `ITypeInfo`), pytest + `unittest.mock`, mypy strict, ruff + black, live IBM Rhapsody on Windows for the audit test.

---

## Global constraints

- Branch: work on the current feature branch (`docs/com-binding-switch`) unless you choose to cut a dedicated branch first; never commit to `main`. Do not push without asking.
- Pre-flight: the working tree carries unrelated uncommitted changes — `D docs/plans/type-annotation-audit-round3.md`, `M docs/superpowers/plans/2026-11-19-com-binding-switch.md`, and previously untracked 2026-11-20 plans now combined into this file. Leave unrelated changes untouched; every commit uses explicit paths, never `git add -A` / `git add .`.
- Quality gate after every task: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit -q`. Unused imports fail ruff `F401`; every snippet is lint-clean at the commit that introduces it.
- Python 3.8 compatible: no `from __future__ import annotations`, no PEP 604 unions. No `Any` in **new** annotations; the existing `Any` on `_get_method_or_property` and the two preserved `Any -> Any` on `_wrap_if_element` stay verbatim. Use `staticmethod` aliases, not classmethod forwarding.
- `call_com` must keep: positional single callable argument, generic return `T`, re-raise non-COM exceptions unchanged, `from exc` chaining, `str(exc)` as the message. The added `retries` keyword defaults to `None`; explicit values are clamped to 0–`_MAX_RETRIES` with a warning.
- Retry is default-on but narrow: only `RPC_E_CALL_REJECTED` and `RPC_E_SERVERCALL_RETRYLATER`. All other COM errors, including `DISP_E_*`, fail fast.
- Behavior-neutral refactor in Phase B: no signature, registry key, metaclass string, return shape, or exception contract change. No real COM in unit tests.
- Phase C is audit-only: `git diff --name-only src/` must be empty for its commits. It skips off Windows via the existing `_require_rhapsody` fixture.
- Because retry changes behavior at every `call_com` site, the live busy-server gate in the Verification checklist is **required before merge**; fake-based tests alone are not merge evidence.
- Do not edit historical plans/specs under `docs/superpowers/` or `docs/plans/`; only active docs (`CLAUDE.md`, package docstrings, one new test-spec section, one traceability row) are updated.
- Commit style: conventional commits, English messages, no AI attribution. Migration scripts under `build/` are temporary and deleted in Task 9.

---

## Part A — COM boundary hardening (Tasks 1–5)

### Task 1: Make `com_error` fakes portable across platforms

**Files:**
- Modify: `tests/unit/models/fakes.py`
- Test: `tests/unit/models/test_core.py` (no new assertions; proves existing tests still collect and pass)

**Why:** `fakes.py` currently does a bare `import pywintypes`. pywin32 is `sys_platform == 'win32'`-only in `pyproject.toml`, so on macOS/Linux the whole unit suite fails to import — meaning COM error-path tests run only on Windows CI. The hardening work must be verifiable locally.

- [ ] **Step 1: Write the failing test (red)**

Add to `tests/unit/test_com_utils.py` (new file, created now with just this import check):

```python
from tests.unit.models.fakes import com_error_type, make_com_error


def test_com_error_fake_is_available_without_pywin32() -> None:
    exc = make_com_error("portable failure")
    assert isinstance(exc, com_error_type)
    assert "portable failure" in str(exc)
```

Do not add `import pytest` here — this single test uses no pytest API, and an unused import would fail ruff `F401` at this commit. Task 3 introduces `pytest` when fixtures are added.

Run: `pytest tests/unit/test_com_utils.py --no-cov -q`
Expected: collection error — `com_error_type` does not exist.

- [ ] **Step 2: Implement the portable fake**

In `tests/unit/models/fakes.py`, replace the bare `import pywintypes` with a guarded import plus a fallback class:

```python
try:
    import pywintypes
except ImportError:  # pragma: no cover - exercised only off Windows
    pywintypes = None


class _FallbackComError(Exception):
    def __init__(self, hresult: int, message: str, arg_error: object, excepinfo: object) -> None:
        super().__init__(message)
        self.hresult = hresult
        self.arg_error = arg_error
        self.excepinfo = excepinfo


com_error_type = pywintypes.com_error if pywintypes is not None else _FallbackComError
```

Change `make_com_error` annotation to `-> Exception` and return `com_error_type(-2147352567, message, None, None)`.

- [ ] **Step 3: Verify green and commit**

Run: `pytest tests/unit/test_com_utils.py tests/unit/models/test_core.py --no-cov -q` — expected all pass, including on this macOS host. Then run the full quality gate before committing:

```bash
ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit -q
```

```bash
git add tests/unit/models/fakes.py tests/unit/test_com_utils.py
git commit -m "test: make COM error fakes portable without pywin32"
```

---

### Task 2: Carry HRESULT on `RhapsodyRuntimeException`

**Files:**
- Modify: `src/rhapsody_cli/exceptions/core.py`
- Test: `tests/unit/exceptions/test_core.py`

**Why:** Today `call_com` does `RhapsodyRuntimeException(str(exc))`, discarding the only machine-readable fact about a COM failure. Classification (Task 3) and diagnostics both need it. Change is additive and backward compatible.

- [ ] **Step 1: Write failing tests**

```python
def test_runtime_exception_keeps_hresult_and_message() -> None:
    exc = RhapsodyRuntimeException("boom", hresult=-2147418111)
    assert str(exc) == "boom"
    assert exc.hresult == -2147418111


def test_runtime_exception_defaults_to_no_hresult() -> None:
    exc = RhapsodyRuntimeException("boom")
    assert exc.hresult is None
```

Run: `pytest tests/unit/exceptions/test_core.py --no-cov -q` — expected 2 failures (`unexpected keyword argument`).

- [ ] **Step 2: Implement**

In `RhapsodyRuntimeException`, add:

```python
def __init__(self, message: str, hresult: Optional[int] = None) -> None:
    super().__init__(message)
    self.hresult = hresult
```

Add `from typing import Optional` at module top. Leave `RhapsodyConnectionError` and `CliExecutionError` untouched.

- [ ] **Step 3: Verify green and commit**

Run: `pytest tests/unit/exceptions/test_core.py --no-cov -q` — all pass. Then the full quality gate:

```bash
ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit -q
```

```bash
git add src/rhapsody_cli/exceptions/core.py tests/unit/exceptions/test_core.py
git commit -m "feat: preserve HRESULT on RhapsodyRuntimeException"
```

---

### Task 3: HRESULT-classified bounded retry in `call_com`

**Files:**
- Modify: `src/rhapsody_cli/com_utils.py`
- Test: `tests/unit/test_com_utils.py`

**Why:** pywin32's `RPC_E_CALL_REJECTED` / `RPC_E_SERVERCALL_RETRYLATER` mean the COM server refused the call *before executing it* — retrying is safe even for mutating calls. All other COM errors (including `DISP_E_*` from a real method failure) must fail fast. This is the behavior seen in real Rhapsody automation projects, replacing ad-hoc `try/except` loops.

- [ ] **Step 1: Write failing tests**

**Rewrite the whole file** created in Task 1 so that all imports stay at module top (ruff `E402` / `I001` are enabled — appending imports below a function would fail the quality gate). The autouse fixture injects the portable fake as the COM error class and makes sleeps instant:

```python
"""Unit tests for the COM boundary helpers."""

from types import SimpleNamespace

import pytest

from rhapsody_cli import com_utils
from rhapsody_cli.exceptions import RhapsodyRuntimeException
from tests.unit.models.fakes import com_error_type, make_com_error


@pytest.fixture(autouse=True)
def _patch_com_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(com_utils, "pywintypes", SimpleNamespace(com_error=com_error_type))
    monkeypatch.setattr(com_utils, "time", SimpleNamespace(sleep=lambda _seconds: None), raising=False)


def test_com_error_fake_is_available_without_pywin32() -> None:
    exc = make_com_error("portable failure")
    assert isinstance(exc, com_error_type)
    assert "portable failure" in str(exc)
```

Then append only the test functions below. Do **not** import `unittest.mock.patch` — none of these tests use it, and an unused import fails ruff `F401`.

Patch `com_utils.time` with `raising=False` as shown: `import time` is only added in Step 2, so during the red phase `com_utils.time` does not exist yet. Patching `com_utils.time.sleep` directly would raise `AttributeError` in fixture setup and every test would error instead of failing for the intended reason.

Tests to add:

```python
def test_non_com_error_is_reraised_unchanged() -> None:
    with pytest.raises(ValueError, match="not a COM error"):
        com_utils.call_com(lambda: (_ for _ in ()).throw(ValueError("not a COM error")))


def test_com_error_is_translated_with_hresult_and_chaining() -> None:
    original = make_com_error("getName failed")
    with pytest.raises(RhapsodyRuntimeException, match="getName failed") as info:
        com_utils.call_com(lambda: (_ for _ in ()).throw(original))
    assert info.value.hresult == -2147352567
    assert info.value.__cause__ is original


def test_rejected_call_is_retried_then_succeeds() -> None:
    attempts = []

    def flaky() -> str:
        attempts.append(1)
        if len(attempts) == 1:
            raise com_error_type(-2147418111, "RPC_E_CALL_REJECTED", None, None)
        return "ok"

    assert com_utils.call_com(flaky) == "ok"
    assert len(attempts) == 2


def test_server_call_retry_later_is_retried() -> None:
    attempts = []

    def flaky() -> str:
        attempts.append(1)
        if len(attempts) < 3:
            raise com_error_type(-2147417846, "RPC_E_SERVERCALL_RETRYLATER", None, None)
        return "ok"

    assert com_utils.call_com(flaky) == "ok"
    assert len(attempts) == 3


def test_other_com_error_is_not_retried() -> None:
    attempts = []

    def failing() -> None:
        attempts.append(1)
        raise make_com_error("method failed normally")

    with pytest.raises(RhapsodyRuntimeException):
        com_utils.call_com(failing)
    assert len(attempts) == 1


def test_retries_are_bounded_and_last_error_surfaces() -> None:
    attempts = []

    def always_busy() -> None:
        attempts.append(1)
        raise com_error_type(-2147418111, "busy", None, None)

    with pytest.raises(RhapsodyRuntimeException, match="busy"):
        com_utils.call_com(always_busy, retries=2)
    assert len(attempts) == 3


def test_retries_can_be_disabled() -> None:
    attempts = []

    def busy_once() -> str:
        attempts.append(1)
        raise com_error_type(-2147418111, "busy", None, None)

    with pytest.raises(RhapsodyRuntimeException):
        com_utils.call_com(busy_once, retries=0)
    assert len(attempts) == 1


@pytest.mark.parametrize("retries", [-1, 99])
def test_explicit_retries_out_of_range_uses_default(
    retries: int, caplog: pytest.LogCaptureFixture, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(com_utils, "_WARNED_BAD_RETRIES", set())
    attempts = []

    def busy_once() -> None:
        attempts.append(1)
        raise com_error_type(-2147418111, "busy", None, None)

    with pytest.raises(RhapsodyRuntimeException):
        com_utils.call_com(busy_once, retries=retries)
    assert len(attempts) == 3  # default 2 retries + first attempt
    assert "out of range" in caplog.text


def test_retry_respects_environment_override(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("RHAPSODY_COM_RETRIES", "0")
    attempts = []

    def busy_once() -> None:
        attempts.append(1)
        raise com_error_type(-2147418111, "busy", None, None)

    with pytest.raises(RhapsodyRuntimeException):
        com_utils.call_com(busy_once)
    assert len(attempts) == 1


def test_invalid_retry_environment_value_warns_and_uses_default(
    caplog: pytest.LogCaptureFixture, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("RHAPSODY_COM_RETRIES", "not-a-number")
    monkeypatch.setattr(com_utils, "_WARNED_BAD_RETRIES", set())
    assert com_utils._get_retries() == 2
    assert "RHAPSODY_COM_RETRIES" in caplog.text
```

Run: `pytest tests/unit/test_com_utils.py --no-cov -q` — expected failures for missing `retries`, `_get_retries`, and retry behavior.

- [ ] **Step 2: Implement**

In `src/rhapsody_cli/com_utils.py`, replace the existing `typing` import line with the one below, then insert the new constants and helper functions between the guarded `pywintypes` import and `_get_method_or_property`. Keep `T = TypeVar("T")`, the guarded `pywintypes` import, `RhapsodyRuntimeException`, and the two helper functions in place — the block below is additive except for the `typing` import:

```python
import logging
import os
import time
from typing import Any, Callable, FrozenSet, Optional, Set, TypeVar

logger = logging.getLogger(__name__)
_RETRIES_ENV = "RHAPSODY_COM_RETRIES"
_DEFAULT_RETRIES = 2
_MAX_RETRIES = 5
_RETRY_BASE_DELAY = 0.05
_WARNED_BAD_RETRIES: Set[str] = set()
# Only HRESULTs with documented "refused before execution" semantics.
# 0x8001010B (RPC_E_SERVERCALL_REJECTED) is excluded: MSDN treats SERVERCALL_REJECTED
# as usually final, and a filter-less client sees both reject modes as 0x80010001.
_RETRYABLE_HRESULTS: FrozenSet[int] = frozenset(
    {
        -2147418111,  # RPC_E_CALL_REJECTED  (0x80010001)
        -2147417846,  # RPC_E_SERVERCALL_RETRYLATER (0x8001010A)
    }
)


def _warn_bad_retries(key: str, message: str, *args: object) -> None:
    """Warn once per distinct bad retry source; call_com runs for every COM call."""
    if key not in _WARNED_BAD_RETRIES:
        logger.warning(message, *args)
        _WARNED_BAD_RETRIES.add(key)


def _normalize_retries(value: int, source: str) -> int:
    """Clamp an explicit or env-derived retry count to the supported range."""
    if 0 <= value <= _MAX_RETRIES:
        return value
    _warn_bad_retries(source, "%s out of range (0-%d); using %d", source, _MAX_RETRIES, _DEFAULT_RETRIES)
    return _DEFAULT_RETRIES


def _get_retries() -> int:
    raw = os.environ.get(_RETRIES_ENV, "").strip()
    if not raw:
        return _DEFAULT_RETRIES
    try:
        value = int(raw)
    except ValueError:
        _warn_bad_retries(raw, "Invalid %s value %r; using %d", _RETRIES_ENV, raw, _DEFAULT_RETRIES)
        return _DEFAULT_RETRIES
    return _normalize_retries(value, raw)


def call_com(func: Callable[[], T], retries: Optional[int] = None) -> T:
    attempts = _get_retries() if retries is None else _normalize_retries(retries, f"retries={retries}")
    for attempt in range(attempts + 1):
        try:
            return func()
        except Exception as exc:
            if pywintypes is None or not isinstance(exc, pywintypes.com_error):
                raise
            hresult = getattr(exc, "hresult", None)
            if hresult in _RETRYABLE_HRESULTS and attempt < attempts:
                delay = _RETRY_BASE_DELAY * (2**attempt)
                logger.warning("COM call rejected (0x%08X); retry %d/%d in %.3fs", hresult & 0xFFFFFFFF, attempt + 1, attempts, delay)
                time.sleep(delay)
                continue
            raise RhapsodyRuntimeException(str(exc), hresult=hresult) from exc
    raise AssertionError("unreachable")  # pragma: no cover
```

`Any` must stay in the `typing` import: `_get_method_or_property` (kept unchanged below) is annotated `-> Any`. Dropping it causes a `NameError` at module import and breaks the entire suite.

Keep `_get_method_or_property` / `_set_method_or_property` exactly as-is — they already route through `call_com` and inherit retry for free. `_warn_bad_retries` and `_normalize_retries` are the only new helpers; the former prevents an invalid retry count from emitting a warning on every one of the thousands of COM calls a CLI command makes, and the latter applies the same 0–`_MAX_RETRIES` bound to both the environment variable and an explicit `retries=` argument (keyed on `retries=<value>` for warning de-duplication). `_get_retries()` still reads the environment at call time, so `monkeypatch.setenv` in the tests above continues to work.

Also fix the stale module docstring at the top of `com_utils.py`: it currently names `get_method_or_property()` / `set_method_or_property()` without the leading underscores. Replace the two affected lines with:

```python
Provides ``call_com()``, ``_get_method_or_property()``, and
``_set_method_or_property()`` as module-level functions so that both
```

- [ ] **Step 3: Verify green and commit**

Run: `pytest tests/unit/test_com_utils.py tests/unit/models/test_core.py tests/unit/test_application.py --no-cov -q` — all pass. Then full quality gate.

```bash
git add src/rhapsody_cli/com_utils.py tests/unit/test_com_utils.py
git commit -m "feat: classify and retry rejected COM calls in call_com"
```

---

### Task 4: Optional STA apartment context manager

**Files:**
- Modify: `src/rhapsody_cli/com_utils.py`
- Modify: `pyproject.toml` (mypy override for `pythoncom` only)
- Test: `tests/unit/test_com_utils.py`

**Why:** pywin32 initializes COM automatically on the main thread, but a worker thread that calls COM without its own apartment fails with `CO_E_NOTINITIALIZED`. This is the classic "works locally, dies in a thread pool" bug. Provide an explicit, opt-in context manager; do not wrap every call site.

- [ ] **Step 1: Write failing tests**

Append to the existing `tests/unit/test_com_utils.py`; `pytest`, `SimpleNamespace`, and `com_utils` are already imported by Task 3. Do not import `contextmanager` in the test file — it is unused here (only the implementation needs it) and would fail ruff `F401`.

```python
def test_com_apartment_initializes_and_uninitializes(monkeypatch: pytest.MonkeyPatch) -> None:
    events = []
    fake = SimpleNamespace(
        CoInitialize=lambda: events.append("init") or 0,
        CoUninitialize=lambda: events.append("uninit"),
    )
    monkeypatch.setattr(com_utils, "pythoncom", fake)
    with com_utils.com_apartment():
        events.append("body")
    assert events == ["init", "body", "uninit"]


def test_com_apartment_does_not_uninitialize_when_already_initialized(monkeypatch: pytest.MonkeyPatch) -> None:
    events = []
    fake = SimpleNamespace(
        CoInitialize=lambda: events.append("init") or 1,  # S_FALSE: already initialized
        CoUninitialize=lambda: events.append("uninit"),
    )
    monkeypatch.setattr(com_utils, "pythoncom", fake)
    with com_utils.com_apartment():
        pass
    assert events == ["init"]


def test_com_apartment_uninitializes_on_exception(monkeypatch: pytest.MonkeyPatch) -> None:
    events = []
    fake = SimpleNamespace(
        CoInitialize=lambda: events.append("init") or 0,
        CoUninitialize=lambda: events.append("uninit"),
    )
    monkeypatch.setattr(com_utils, "pythoncom", fake)
    with pytest.raises(RuntimeError), com_utils.com_apartment():
        raise RuntimeError("boom")
    assert events == ["init", "uninit"]
```

Run: `pytest tests/unit/test_com_utils.py -k apartment --no-cov -q` — expected failures (attribute missing).

- [ ] **Step 2: Implement**

Add `from contextlib import contextmanager` to the stdlib imports at the top of `com_utils.py` (alongside `import logging` / `import os` / `import time`), then add a guarded import beside `pywintypes`:

```python
from contextlib import contextmanager

try:
    import pythoncom
except ImportError:  # pragma: no cover - pywin32 is Windows-only
    pythoncom = None
```

`pythoncom` has no stub package in the dev dependencies and no existing mypy override (only `pywintypes` and `win32com.*` are listed), so add one beside the `pywintypes` override in `pyproject.toml`. A config override is preferred over an inline `# type: ignore` because `warn_unused_ignores = true` would make the ignore itself fail on platforms where mypy can resolve the module:

```toml
[[tool.mypy.overrides]]
module = "pythoncom"
ignore_missing_imports = true
```

Add:

```python
@contextmanager
def com_apartment() -> Iterator[None]:
    if pythoncom is None:
        yield
        return
    result = pythoncom.CoInitialize()
    try:
        yield
    finally:
        if result == 0:  # S_OK only; S_FALSE means already initialized
            pythoncom.CoUninitialize()
```

Extend the existing `typing` import from Task 3 with `Iterator` — keep `Any`, `Callable`, `FrozenSet`, `Optional`, `Set`, and `TypeVar` already listed there. Document in the docstring that this is for worker threads only and must not be nested around the main CLI thread.

- [ ] **Step 3: Verify green and commit**

Run: `pytest tests/unit/test_com_utils.py --no-cov -q` — all pass. Full quality gate.

```bash
git add src/rhapsody_cli/com_utils.py tests/unit/test_com_utils.py pyproject.toml
git commit -m "feat: add opt-in STA apartment context manager for COM threads"
```

---

### Task 5: Documentation and final gate

**Files:**
- Modify: `CLAUDE.md`
- Optional: `docs/api/exceptions.rst` — only if you also fix its stale `RhapsodyException` hierarchy; it does not document exception fields, so no change is required here.

- [ ] **Step 1: Document**

Add a short `### COM boundary behaviour` section to `CLAUDE.md` near the existing COM wrapping rules. State: `call_com` retries only `RPC_E_CALL_REJECTED` / `RPC_E_SERVERCALL_RETRYLATER` up to 2 times by default, controlled by `RHAPSODY_COM_RETRIES` (0–5, 0 disables); explicit `retries=` is clamped to the same range; `RhapsodyRuntimeException.hresult` carries the HRESULT; `com_apartment()` is for worker threads only; no `EnsureDispatch` / early binding is used (see Decision Log). While there, correct the existing line that still locates `call_com` at `models/core.py:42` — it now lives in `com_utils.py`.

- [ ] **Step 2: Run and commit**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit -q`

```bash
git add CLAUDE.md  # add docs/api/exceptions.rst only if actually edited
git commit -m "docs: describe COM retry policy and STA guidance"
```

---
---

## Part B — Remove `AbstractRPModelElement` (Tasks 6–9)

### Task 6: Add the module-level API and `ComHelpers` behind the facade

**Files:**
- Modify: `src/rhapsody_cli/models/core.py`
- Create: `tests/unit/models/test_com_helpers.py`

**Why:** Establish the new structure first with characterization tests while the old facade still exists, so the suite stays green throughout the migration.

- [ ] **Step 1: Write failing tests**

Create `tests/unit/models/test_com_helpers.py`:

```python
"""Characterization tests for the module-level wrapper registry and ComHelpers."""

from unittest.mock import patch

import rhapsody_cli.models.core as core_module
from rhapsody_cli import com_utils
from rhapsody_cli.models.core import ComHelpers, RPModelElement
from tests.unit.models.fakes import make_fake_element


def test_module_level_wrap_resolves_registered_wrapper() -> None:
    element = core_module.wrap(make_fake_element("Class"))

    assert element is not None
    assert element.get_meta_class() == "Class"


def test_module_level_wrap_returns_none_for_none() -> None:
    assert core_module.wrap(None) is None


def test_module_level_register_wrapper_updates_registry() -> None:
    with patch.dict(core_module._WRAPPER_REGISTRY, clear=False):
        core_module.register_wrapper("ProbeMetaClass", RPModelElement)
        assert core_module._WRAPPER_REGISTRY["ProbeMetaClass"] is RPModelElement


def test_module_level_wrap_if_element_wraps_com_objects() -> None:
    fake = make_fake_element("Class")

    assert isinstance(core_module._wrap_if_element(fake), RPModelElement)
    assert core_module._wrap_if_element("plain string") == "plain string"


def test_com_helpers_methods_are_aliases_of_com_utils() -> None:
    assert ComHelpers.__dict__["call_com"].__func__ is com_utils.call_com
    assert ComHelpers.__dict__["_get_method_or_property"].__func__ is com_utils._get_method_or_property
    assert ComHelpers.__dict__["_set_method_or_property"].__func__ is com_utils._set_method_or_property


def test_rp_model_element_exposes_module_level_aliases() -> None:
    assert RPModelElement.__dict__["wrap"].__func__ is core_module.wrap
    assert RPModelElement.__dict__["register_wrapper"].__func__ is core_module.register_wrapper
```

- [ ] **Step 2: Verify red**

Run: `pytest tests/unit/models/test_com_helpers.py --no-cov -q`
Expected: collection error — `ComHelpers` and module-level `wrap`/`register_wrapper` do not exist yet.

- [ ] **Step 3: Implement the module-level API**

In `src/rhapsody_cli/models/core.py`:

1. Change the `typing` import line from:

```python
from typing import TYPE_CHECKING, Any, Callable, Dict, Iterator, List, Optional, Type, TypeVar, cast
```

to:

```python
from typing import TYPE_CHECKING, Any, Dict, Iterator, List, Optional, Type, cast
```

2. Replace the `T = TypeVar("T")` line and the entire `AbstractRPModelElement` class (currently lines 27–95) with:

```python
_WRAPPER_REGISTRY: Dict[str, Type["RPModelElement"]] = {}


def register_wrapper(meta_class: str, wrapper_cls: Type["RPModelElement"]) -> None:
    """Register ``wrapper_cls`` as the wrapper for COM objects of ``meta_class``."""
    _WRAPPER_REGISTRY[meta_class] = wrapper_cls


def _wrap_if_element(value: Any) -> Any:
    """Wrap ``value`` if it looks like a Rhapsody model element."""
    if hasattr(value, "getMetaClass") or hasattr(value, "metaClass"):
        return wrap(value)
    return value


def wrap(com_obj: object) -> Optional["RPModelElement"]:
    """Wrap a raw Rhapsody COM model element in its matching wrapper class.

    ``None`` is returned for a COM ``None`` (e.g. a failed find) rather than
    being wrapped. Unregistered meta classes fall back to ``RPModelElement``.
    """
    if com_obj is None:
        return None
    meta_class = str(com_utils._get_method_or_property(com_obj, "getMetaClass", "metaClass"))
    wrapper_cls = _WRAPPER_REGISTRY.get(meta_class, RPModelElement)
    return wrapper_cls(com_obj)


class ComHelpers:
    """COM boundary helpers shared by every Rhapsody element wrapper."""

    call_com = staticmethod(com_utils.call_com)
    _get_method_or_property = staticmethod(com_utils._get_method_or_property)
    _set_method_or_property = staticmethod(com_utils._set_method_or_property)


class AbstractRPModelElement:
    """Transitional facade — deleted in Task 9 once all call sites are migrated."""

    _WRAPPER_REGISTRY = _WRAPPER_REGISTRY
    register_wrapper = staticmethod(register_wrapper)
    call_com = staticmethod(com_utils.call_com)
    _wrap_if_element = staticmethod(_wrap_if_element)
    wrap = staticmethod(wrap)
    _get_method_or_property = staticmethod(com_utils._get_method_or_property)
    _set_method_or_property = staticmethod(com_utils._set_method_or_property)
```

`wrap()` references `RPModelElement` at call time; the class is defined later in the same module, which is safe because `wrap()` is never called during module import. `_WRAPPER_REGISTRY` on the facade is the *same dict object* as the module-level registry, so registrations through either name are visible to both.

3. Change the class declaration from `class RPModelElement(AbstractRPModelElement):` to `class RPModelElement(ComHelpers):`, and insert these two aliases immediately after that class's docstring (before the method-parity checklist comment):

```python
    register_wrapper = staticmethod(register_wrapper)
    wrap = staticmethod(wrap)
```

- [ ] **Step 4: Verify green and run the quality gate**

Run: `pytest tests/unit/models/test_com_helpers.py --no-cov -q` — expected 6 passed.
Then run the full quality gate (all green).

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/models/core.py tests/unit/models/test_com_helpers.py
git commit -m "refactor: add module-level wrapper registry and ComHelpers mixin"
```

---

### Task 7: Migrate all `src/` call sites

**Files:** Every `*.py` under `src/rhapsody_cli/` that references `AbstractRPModelElement`.

**Why:** A pure textual migration now that `RPModelElement` exposes the same API. No behavior changes.

- [ ] **Step 1: Create the migration script**

Create `build/migrate_abstract_model_element.py`:

```python
"""One-off migration of AbstractRPModelElement references to RPModelElement."""

import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
import_line = re.compile(r"^(\s*)from rhapsody_cli\.models\.core import (.+)$")

for path in root.rglob("*.py"):
    text = path.read_text()
    out = []
    for line in text.splitlines(keepends=True):
        match = import_line.match(line.rstrip("\n"))
        if match and "AbstractRPModelElement" in match.group(2):
            names = [name.strip() for name in match.group(2).split(",")]
            names = [name for name in names if name and name != "AbstractRPModelElement"]
            if "RPModelElement" not in names:
                names.append("RPModelElement")
            newline = "\n" if line.endswith("\n") else ""
            out.append(f"{match.group(1)}from rhapsody_cli.models.core import {', '.join(sorted(names))}{newline}")
        else:
            out.append(line.replace("AbstractRPModelElement.", "RPModelElement."))
    new_text = "".join(out)
    if path.parts[-2:] == ("models", "core.py"):
        new_text = new_text.replace("RPModelElement._wrap_if_element(", "_wrap_if_element(")
    if new_text != text:
        path.write_text(new_text)
```

The import-line handling is required because some modules import both names; a blind identifier rename would produce duplicate `RPModelElement` imports and fail ruff `F811`. The `core.py` special case redirects its single `_wrap_if_element` caller to the module-level function.

- [ ] **Step 2: Run the migration and format**

```bash
mkdir -p build
python build/migrate_abstract_model_element.py src/rhapsody_cli
ruff check src/ --fix
black src/
```

- [ ] **Step 3: Verify no stale references remain in source**

Run: `rg -n 'AbstractRPModelElement' src/rhapsody_cli --glob '!**/core.py'`
Expected: only the bare docstring mention in `com_utils.py` (removed in Task 9). In `core.py` the only remaining matches must be the transitional facade class itself.

- [ ] **Step 4: Run the quality gate and commit**

Run the full quality gate — all green.

```bash
git add src/rhapsody_cli
git commit -m "refactor: point source call sites at RPModelElement facade"
```

---

### Task 8: Migrate tests, exports, and package docstrings

**Files:** `tests/**/*.py`, `src/rhapsody_cli/models/__init__.py`, `src/rhapsody_cli/__init__.py`, `tests/unit/models/test_core.py`

- [ ] **Step 1: Migrate test call sites**

```bash
python build/migrate_abstract_model_element.py tests
ruff check tests/ --fix
black tests/
```

- [ ] **Step 2: Update the backward-compatibility assertion in `tests/unit/models/test_core.py`**

Replace the existing test at lines 51–60 with:

```python
def test_core_module_does_not_reexport_com_helpers() -> None:
    """COM helpers live in com_utils; core exposes only the registry API."""
    for helper_name in (
        "call_com",
        "_get_method_or_property",
        "_set_method_or_property",
    ):
        assert not hasattr(core_module, helper_name)


def test_core_module_exports_registry_api() -> None:
    for api_name in ("wrap", "register_wrapper", "_wrap_if_element", "_WRAPPER_REGISTRY"):
        assert hasattr(core_module, api_name)
```

Also remove `AbstractRPModelElement` from the `from rhapsody_cli.models.core import (...)` block at the top of that file — the Task 7 script already removed it from single-line imports, but this file uses a parenthesized multi-line import that the script does not rewrite.

- [ ] **Step 3: Update `src/rhapsody_cli/models/__init__.py`**

The migration script already removed `AbstractRPModelElement` from the `core` import line. Change that line to add `ComHelpers`, and update `__all__`:

```python
from rhapsody_cli.models.core import ComHelpers, RPCollection, RPModelElement, RPUnit

__all__ = [
    "ComHelpers",
    "RPCollection",
    "RPModelElement",
    "RPUnit",
    "elements",
    "support",
]
```

The top-level `src/rhapsody_cli/__init__.py` docstring was already updated by the script to read ``RPModelElement.wrap()``; no further change is needed there.

- [ ] **Step 4: Verify and commit**

Run: `rg -n 'AbstractRPModelElement' src/rhapsody_cli tests` — expected: only the transitional facade in `core.py` and the bare docstring mention in `com_utils.py` (both removed in Task 9).
Then run the full quality gate.

```bash
git add src/rhapsody_cli/models/__init__.py tests/
git commit -m "refactor: migrate tests and exports off AbstractRPModelElement"
```

---

### Task 9: Delete the facade and update active documentation

**Files:** `src/rhapsody_cli/models/core.py`, `CLAUDE.md`, `src/rhapsody_cli/com_utils.py`

- [ ] **Step 1: Delete the transitional class**

Delete the entire `AbstractRPModelElement` class block from `src/rhapsody_cli/models/core.py` (the seven-line class added in Task 6). Keep `ComHelpers` and the module-level functions above it.

- [ ] **Step 2: Update active docs**

In `CLAUDE.md`, apply these exact replacements:

```python
# line 193
from rhapsody_cli.models.core import RPModelElement, AbstractRPModelElement
→
from rhapsody_cli.models.core import RPModelElement, register_wrapper

# line 199
AbstractRPModelElement.register_wrapper("MyClass", RPMyClass)
→
register_wrapper("MyClass", RPMyClass)

# line 213
- **Return wrapped element** → Use `AbstractRPModelElement.wrap(...)` or specific wrapper constructor
→
- **Return wrapped element** → Use `RPModelElement.wrap(...)` or specific wrapper constructor

# line 297
3. Call `AbstractRPModelElement.register_wrapper("MyClass", RPMyClass)` at module level
→
3. Call `register_wrapper("MyClass", RPMyClass)` at module level
```

In `src/rhapsody_cli/com_utils.py`, replace the last line of the module docstring:

```python
inheriting from ``AbstractRPModelElement``.
→
inheriting from ``ComHelpers``.
```

This is docstring-only; if the parallel `2026-11-20-com-utils-hardening.md` plan is applied first and already edited this line, keep its wording and only confirm the name is `ComHelpers`.

- [ ] **Step 3: Remove temporary artifacts**

```bash
rm -f build/migrate_abstract_model_element.py
```

- [ ] **Step 4: Final verification and quality gate**

```bash
rg -n 'AbstractRPModelElement' src/ tests/ CLAUDE.md docs/index.rst || true
```

Expected: no matches outside historical `docs/superpowers/` plans/specs.

Then run the full quality gate and confirm `pytest tests/unit` is still fully green.

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/models/core.py src/rhapsody_cli/com_utils.py CLAUDE.md
git commit -m "refactor: remove AbstractRPModelElement base class"
```

---
---

## Part C — Live COM API parity audit (Tasks 10–13)

### Pass/fail criteria (decision to review)

- **Fail:** a public method defined on the audited wrapper class (or its `RP*` ancestors) has no matching member in the live COM inventory, after camel↔snake normalization and excluding the infrastructure allowlist below. This is a real definition error — the wrapper claims an API the COM object does not have.
- **Report only:** live COM members with no wrapper method. These are coverage gaps, many intentionally unwrapped; printing them is the audit value. The test does not fail on them.
- **Infrastructure allowlist** (excluded from both sides): `__init__`, `__repr__`, `__eq__`, `__hash__`, `wrap`, `register_wrapper`, `call_com`, `_get_method_or_property`, `_set_method_or_property`, `_wrap_if_element`, `_WRAPPER_REGISTRY`, and any name starting with `_`.
- **Dynamic-only properties** (`name`, `GUID`, `metaClass`) are accepted as COM counterparts for `get_name`, `get_guid`, `get_meta_class` even when absent from type info — the binding-switch spec established these work live but are not in generated member lists.

---

### Task 10: Pure normalization helpers and their unit tests

**Files:**
- Create: `tests/integration/com_api_audit.py`
- Test: `tests/unit/test_com_api_audit.py`

**Why:** Decide the name-mapping and filtering rules locally, where they can be tested without Rhapsody, before touching live COM.

- [ ] **Step 1: Write failing tests**

Create `tests/unit/test_com_api_audit.py`:

```python
"""Unit tests for the pure parts of the live COM API audit helper."""

from tests.integration.com_api_audit import (
    INFRASTRUCTURE_NAMES,
    com_name_to_wrapper_name,
    wrapper_methods_of,
)


def test_com_name_to_wrapper_name_uses_mapping_json() -> None:
    assert com_name_to_wrapper_name("getName") == "get_name"
    assert com_name_to_wrapper_name("getIsAbstract") == "get_is_abstract"
    assert com_name_to_wrapper_name("addToModel") == "add_to_model"


def test_com_name_to_wrapper_name_leaves_unmapped_names_alone() -> None:
    assert com_name_to_wrapper_name("SomeUnknownMember") == "SomeUnknownMember"


def test_wrapper_methods_of_excludes_infrastructure_and_private_names() -> None:
    class Probe:
        def get_name(self) -> str:
            return "n"

        def _private(self) -> None:
            pass

        def call_com(self) -> None:
            pass

    methods = wrapper_methods_of(Probe)

    assert "get_name" in methods
    assert "_private" not in methods
    assert "call_com" not in methods
    assert INFRASTRUCTURE_NAMES.isdisjoint(methods)
```

- [ ] **Step 2: Verify red**

Run: `pytest tests/unit/test_com_api_audit.py --no-cov -q`
Expected: collection error — `tests.integration.com_api_audit` does not exist.

- [ ] **Step 3: Implement the pure helpers**

Create `tests/integration/com_api_audit.py` with the import guards and the pure layer:

```python
"""Live COM API audit helpers shared by the integration parity test.

Pure functions here are importable off Windows so they can be unit-tested;
COM enumeration functions raise a clear error when pywin32 is unavailable.
"""

import json
import re
from pathlib import Path
from typing import Any, Dict, FrozenSet, List, Set, Tuple, Type

from rhapsody_cli.com_utils import call_com

INFRASTRUCTURE_NAMES: FrozenSet[str] = frozenset(
    {
        "wrap",
        "register_wrapper",
        "call_com",
        "_get_method_or_property",
        "_set_method_or_property",
        "_wrap_if_element",
        "_WRAPPER_REGISTRY",
    }
)

_MAPPING_PATH = Path(__file__).resolve().parents[2] / "scripts" / "_method_mapping.json"
_WITH_MAPPING: Dict[str, str] = json.loads(_MAPPING_PATH.read_text(encoding="utf-8"))


def _camel_to_snake(name: str) -> str:
    first = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", first).lower()


def com_name_to_wrapper_name(com_name: str) -> str:
    """Map a COM member name to the snake_case name a wrapper would use."""
    return _WITH_MAPPING.get(com_name, _camel_to_snake(com_name))


def wrapper_methods_of(wrapper_cls: Type[Any]) -> Set[str]:
    """Collect public Python methods declared by a wrapper and its RP* bases."""
    result: Set[str] = set()
    for cls in wrapper_cls.__mro__:
        if not cls.__name__.startswith("RP"):
            continue
        for name, value in vars(cls).items():
            if name.startswith("_") or name in INFRASTRUCTURE_NAMES:
                continue
            if callable(value):
                result.add(name)
    return result
```

- [ ] **Step 4: Verify green and commit**

Run: `pytest tests/unit/test_com_api_audit.py --no-cov -q` — expected 4 passed. Then the full quality gate.

```bash
git add tests/integration/com_api_audit.py tests/unit/test_com_api_audit.py
git commit -m "test: add pure helpers for live COM API audit"
```

---

### Task 11: Windows spike — confirm the type-info shape

**Files:**
- Modify: `tests/integration/com_api_audit.py`
- Modify: this plan (record observed shape)

**Why:** pywin32's `ITypeInfo.GetTypeAttr()` / `GetFuncDesc()` return shapes vary across versions. Lock down the actual shape on Windows before writing assertions that depend on it.

- [ ] **Step 1: Add the enumeration function with defensive normalization**

Append to `tests/integration/com_api_audit.py`:

```python
def com_member_names(com_obj: object) -> Tuple[List[str], List[str]]:
    """Return ``(method_names, property_names)`` declared by the COM object's type info.

    Falls back to ``dir()`` when type info is unavailable, because some
    Rhapsody Prog IDs expose members dynamically only.
    """
    try:
        type_info = call_com(lambda: com_obj.GetTypeInfo())  # type: ignore[attr-defined]
    except Exception:
        names = call_com(lambda: dir(com_obj))
        return sorted(n for n in names if not n.startswith("_")), []

    if isinstance(type_info, tuple):
        type_info = type_info[0]
    attr = call_com(lambda: type_info.GetTypeAttr())

    method_names: List[str] = []
    property_names: List[str] = []
    func_count = getattr(attr, "cFuncs", 0)
    var_count = getattr(attr, "cVars", 0)
    for index in range(func_count):
        desc = call_com(lambda: type_info.GetFuncDesc(index))
        names = call_com(lambda: type_info.GetNames(desc[0]))
        if names:
            method_names.append(names[0])
    for index in range(var_count):
        desc = call_com(lambda: type_info.GetVarDesc(index))
        names = call_com(lambda: type_info.GetNames(desc[0]))
        if names:
            property_names.append(names[0])
    return sorted(method_names), sorted(property_names)
```

No `from __future__ import annotations` or builtin-generic annotations — `Tuple[List[str], List[str]]` keeps Python 3.8 and mypy strict happy.

- [ ] **Step 2: Run the live spike on Windows**

Create a temporary test file `tests/integration/models/test_00_api_spike.py` that uses the existing `test_project` fixture, calls `pkg.add_class("SpikeClass")`, then:

```python
methods, properties = com_member_names(cls._com)
print("TYPE_INFO_METHODS", methods[:20], len(methods))
print("TYPE_INFO_PROPERTIES", properties[:20], len(properties))
print("TYPE_INFO_RAW", type(cls._com.GetTypeInfo()).__name__)
```

Run: `pytest tests/integration/models/test_00_api_spike.py -s --no-cov -q` on Windows with licensed Rhapsody.

Record in this plan: the concrete `GetTypeInfo()` return shape, whether `cFuncs`/`cVars` are attributes or tuple indices, and whether `name`/`GUID`/`metaClass` appear in the inventory. Adjust `com_member_names()` if the probe contradicts the assumptions above, then delete the spike file.

- [ ] **Step 3: Commit**

```bash
git add tests/integration/com_api_audit.py
git commit -m "test: add live COM type-info enumeration helper"
```

---

### Task 12: The first live parity integration test

**Files:**
- Create: `tests/integration/models/test_00_api_parity.py`

**Why:** This is the audit itself — collected before the other integration tests because of the `00` prefix.

- [ ] **Step 1: Write the test**

```python
"""First live integration test: audit RPClass against its COM type info."""

import pytest

from rhapsody_cli.models.elements.classifiers import RPClass
from rhapsody_cli.models.elements.containment import RPProject
from tests.integration.com_api_audit import (
    com_member_names,
    com_name_to_wrapper_name,
    wrapper_methods_of,
)
from tests.integration.conftest import TEST_PROJECT_DIR

DYNAMIC_ONLY_COM_NAMES = frozenset({"name", "GUID", "metaClass"})


@pytest.mark.integration
class TestLiveApiParity:
    def test_rp_class_members_match_com_inventory(self, test_project: RPProject) -> None:
        pkg = test_project.add_nested_package("ApiAuditPackage")
        cls = pkg.add_class("ApiAuditClass")

        methods, properties = com_member_names(cls._com)
        com_names = set(methods) | set(properties) | DYNAMIC_ONLY_COM_NAMES
        expected = {com_name_to_wrapper_name(name) for name in com_names}
        actual = wrapper_methods_of(RPClass)

        missing = sorted(expected - actual)
        phantom = sorted(actual - expected)

        print(f"COM members audited: {len(com_names)}")
        print(f"Unwrapped COM members ({len(missing)}): {missing}")
        print(f"Wrapper methods with no COM member ({len(phantom)}): {phantom}")

        assert phantom == [], f"wrapper methods absent from live COM inventory: {phantom}"
```

- [ ] **Step 2: Verify it skips locally and runs on Windows**

Run locally: `pytest tests/integration/models/test_00_api_parity.py --no-cov -q` — expected SKIP (no Rhapsody).
Run on Windows with licensed Rhapsody: expected PASS with a printed gap report. If `phantom` is non-empty, investigate each entry: either the mapping JSON needs a correction, or the wrapper declares a method the COM object genuinely lacks — fix the wrapper definition, not the test.

- [ ] **Step 3: Commit**

```bash
git add tests/integration/models/test_00_api_parity.py
git commit -m "test: audit RPClass definition against live COM members"
```

---

### Task 13: Test-spec document, traceability entry, and final gate

**Files:**
- Modify: `docs/tests/integration/its_core_test-specs.md`
- Modify: `docs/traceability_matrix.md`

- [ ] **Step 1: Append the test spec**

Specs are sections inside `its_core_test-specs.md`, not one file per id. Append a new section with the next free id, **`ITS_CORE_00009`** (existing ids are `00001`–`00008`), using the exact heading/section format of the preceding entries: `ITS_CORE_00009`, title "Live COM member audit of RPClass wrapper definition", purpose (verify every public wrapper method has a live COM counterpart and report unwrapped COM members), fixtures (`rhapsody_app`, `test_project`), procedure (create package/class, enumerate type info, normalize names, diff), expected result (`phantom` empty; gap report printed), and a note that it skips off Windows.

- [ ] **Step 2: Add the traceability row**

Add one row to `docs/traceability_matrix.md` using the same column format as the surrounding `SWR_CORE_*` rows; reference `ITS_CORE_00009` in the integration-test column and `tests/integration/models/test_00_api_parity.py` as the test location.

- [ ] **Step 3: Final gate and commit**

Run the full quality gate. Confirm `git diff --name-only src/` is empty.

```bash
git add docs/tests/integration/its_core_test-specs.md docs/traceability_matrix.md
git commit -m "docs: specify live COM API parity audit test"
```

---

---

## Decision log (why we are not doing other things)

- **No `EnsureDispatch` / early binding.** pywin32's `win32com.client.Dispatch` already returns gen_py-typed objects whenever a cache exists (see `client/__init__.py::__WrapDispatch` → `gencache.GetClassForCLSID`). `EnsureDispatch` only *generates the cache* when absent. It is not a binding switch; a `RHAPSODY_COM_BINDING` variable would be a misleading "generate cache" toggle, and a populated cache makes any "dynamic" control run invalid. See abandoned `2026-11-19-com-binding-switch.md`.
- **No COM message filter (`CoRegisterMessageFilter`).** It is process-global state, must be registered on the STA thread, and has a non-obvious lifetime. Retries at the single `call_com` seam cover the same `RPC_E_*` cases with far less global coupling. Revisit only if live telemetry shows rejects that the bounded retry cannot absorb.
- **No retry for `DISP_E_*` or generic COM failures.** Those mean the server executed the method and it failed; retrying could duplicate side effects. Only "rejected before execution" HRESULTs are retried.
- **No retry for `RPC_E_SERVERCALL_REJECTED` (`0x8001010B`).** MSDN's `IMessageFilter::RetryRejectedCall` guidance is to silently retry `SERVERCALL_RETRYLATER`; `SERVERCALL_REJECTED` is usually final and should surface to the caller. A filter-less client sees both modes as `RPC_E_CALL_REJECTED` (`0x80010001`), which is already retried, so adding `0x8001010B` buys nothing and can mask a deliberate refusal.
- **No retry for `0x80010108` (`RPC_E_DISCONNECTED`) or `0x800706BA` (`RPC_E_SERVER_UNAVAILABLE`).** These indicate a dead server; the connection must be re-established at a higher layer, not by re-calling.
- **No jitter in backoff.** With at most 5 attempts and a 0.05s base, deterministic exponential backoff is easier to test and reason about; thundering-herd risk is negligible for a single-user CLI.
- **No change to `models/`, `application.py`, CLI or actions.** The seam is already correctly placed; changes belong at the seam.

## Verification checklist

- [ ] Full quality gate green on this macOS host (`pytest tests/unit` no longer requires pywin32).
- [ ] Full quality gate green on `windows-latest` CI (Python 3.8–3.13 matrix).
- [ ] **Required before merge:** a live smoke run against Rhapsody (Windows, licensed) that deliberately triggers a busy server — start a long-running UI operation, run a read-only CLI command, capture at least one `COM call rejected` warning followed by a successful result, and record the trace in the PR. If licensed Rhapsody is unavailable, state the gap explicitly and do not mark the change merge-ready.
- [ ] Live API audit test (`test_00_api_parity.py`) passes on Windows with a printed gap report; any `phantom` entry is resolved by fixing the wrapper definition, not the test.
- [ ] `rg -n 'AbstractRPModelElement' src/ tests/ CLAUDE.md docs/index.rst` returns no matches outside historical plans/specs.
- [ ] Confirm Phase C made no `src/` changes: `git diff --name-only src/` is empty for its commits.

## Rollback

Revert the thirteen commits in reverse order. Phase A is additive — `RhapsodyRuntimeException(message)` remains valid, and `RHAPSODY_COM_RETRIES=0` disables retries without code changes. Phase B is behavior-neutral; reverting restores the old facade. Phase C deletes only test and spec files.
