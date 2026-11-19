# Remove AbstractRPModelElement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove the `AbstractRPModelElement` base class with zero behavior change: move its wrapper registry and factory to module-level functions in `models/core.py`, and its three COM helpers to a small `ComHelpers` mixin that aliases `com_utils`.

**Architecture:** `com_utils.py` remains the single COM boundary and is not functionally changed. `models/core.py` gains module-level `_WRAPPER_REGISTRY`, `register_wrapper()`, `wrap()`, and `_wrap_if_element()`, plus `ComHelpers` whose members are `staticmethod` aliases of the `com_utils` functions. `RPModelElement(ComHelpers)` re-exposes `wrap`/`register_wrapper` as thin staticmethod aliases, so the ~440 `AbstractRPModelElement.wrap(...)` / `register_wrapper(...)` call sites need only a class-name rename and the ~600 `self.call_com(...)` / `self._get_method_or_property(...)` / `self._set_method_or_property(...)` sites need no change at all. A transitional `AbstractRPModelElement` facade keeps every existing caller working until Task 4, when it is deleted.

**Tech Stack:** Python 3.8+, pytest + `unittest.mock`, mypy strict, ruff + black.

---

## Global constraints

- Branch: `refactor/remove-abstract-model-element` (never commit to `main`).
- Pre-flight: the working tree carries unrelated uncommitted changes — `D docs/plans/type-annotation-audit-round3.md`, `M docs/superpowers/plans/2026-11-19-com-binding-switch.md`, and `?? docs/superpowers/plans/2026-11-20-com-utils-hardening.md`. Leave all of them untouched; every commit below uses explicit paths, never `git add -A` / `git add .`.
- Quality gate after every task: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit -q`.
- Python 3.8 compatible: no `from __future__ import annotations`, no PEP 604 unions, no `Any` annotations beyond the two preserved verbatim on the moved `_wrap_if_element` (`Any -> Any`). Use `staticmethod` aliases, not classmethod forwarding — staticmethod objects are not directly callable on Python 3.8, and every access in this codebase is via class or instance.
- Behavior-neutral refactor: no method signature, registry key, metaclass string, return shape, or exception contract changes. The existing unit suite is the safety net.
- No real COM in unit tests; use `tests/unit/models/fakes.py`.
- Do not edit historical plans/specs under `docs/superpowers/` or `docs/plans/` — they are a record of past decisions. Only active docs (`CLAUDE.md`, package docstrings) are updated.
- Commit style: conventional commits, no AI attribution. Every commit uses explicit paths.
- The two migration scripts are temporary build artifacts under `build/` and must be deleted in Task 4.

---

### Task 1: Add the module-level API and `ComHelpers` behind the facade

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
    """Transitional facade — deleted in Task 4 once all call sites are migrated."""

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

### Task 2: Migrate all `src/` call sites

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
Expected: only the bare docstring mention in `com_utils.py` (removed in Task 4). In `core.py` the only remaining matches must be the transitional facade class itself.

- [ ] **Step 4: Run the quality gate and commit**

Run the full quality gate — all green.

```bash
git add src/rhapsody_cli
git commit -m "refactor: point source call sites at RPModelElement facade"
```

---

### Task 3: Migrate tests, exports, and package docstrings

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

Also remove `AbstractRPModelElement` from the `from rhapsody_cli.models.core import (...)` block at the top of that file — the Task 2 script already removed it from single-line imports, but this file uses a parenthesized multi-line import that the script does not rewrite.

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

Run: `rg -n 'AbstractRPModelElement' src/rhapsody_cli tests` — expected: only the transitional facade in `core.py` and the bare docstring mention in `com_utils.py` (both removed in Task 4).
Then run the full quality gate.

```bash
git add src/rhapsody_cli/models/__init__.py tests/
git commit -m "refactor: migrate tests and exports off AbstractRPModelElement"
```

---

### Task 4: Delete the facade and update active documentation

**Files:** `src/rhapsody_cli/models/core.py`, `CLAUDE.md`, `src/rhapsody_cli/com_utils.py`

- [ ] **Step 1: Delete the transitional class**

Delete the entire `AbstractRPModelElement` class block from `src/rhapsody_cli/models/core.py` (the seven-line class added in Task 1). Keep `ComHelpers` and the module-level functions above it.

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

## Self-review notes

- **Spec coverage:** all four responsibilities of the old class are preserved — COM helpers (`ComHelpers`), registry, factory, and `_wrap_if_element` (module-level in `core.py`). No call site is left behind.
- **Python 3.8 safety:** `staticmethod` aliases are accessed through class or instance everywhere; no code calls `ComHelpers.call_com` as a bare staticmethod object.
- **Type consistency:** `wrap()` keeps the exact `Optional[RPModelElement]` return contract and the `None`-in/`None`-out behavior; `register_wrapper()` keeps its two-argument signature.
- **Circular imports:** none introduced — module-level functions live in the same module as `RPModelElement` and resolve it at call time.
- **Migration script correctness:** the import-line regex handles both single-line and indented imports; parenthesized multi-line imports are handled manually in Task 3 Step 2.
- **No behavior change:** the only semantic risk is `rpcollection.get_item()`'s `_wrap_if_element` call, which is explicitly redirected to the module-level function in the script.
