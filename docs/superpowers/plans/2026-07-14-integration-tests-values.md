# Values Subpackage Integration Tests Completion Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add integration tests for ALL methods (currently zero coverage) of `RPInstanceSlot`, `RPInstanceSpecification`, `RPValueSpecification`, `RPInstanceValue`, `RPLiteralSpecification`. Flip in-source `[ ] integration test` markers to `[x]` as work completes.

**Architecture:** New test file `tests/integration/models/elements/values/test_model_values.py` plus a new `tests/integration/models/elements/values/conftest.py` providing a shared `instance_spec_factory` fixture, using the `test_project`/`rhapsody_app` session fixtures and the instance-specification/slot/value creation chain documented below. The empty package marker `tests/integration/models/elements/values/__init__.py` already exists.

**Tech Stack:** pytest, pywin32 (win32com), live Rhapsody COM API, `uuid.uuid4().hex[:8]`.

## Global Constraints

- Windows-only runtime (requires Windows + a running Rhapsody instance)
- All test classes use `@pytest.mark.integration`
- All tests consume the `test_project: RPProject` fixture
- Use `_unique(prefix)` with `uuid.uuid4().hex[:8]`
- Always `try/finally` cleanup — the owning `RPPackage` created per test is deleted via `delete_from_project()`, which cascades to delete the nested class, attribute, and instance specification (matches the `test_model_class.py`/`test_model_operation.py` pattern)
- Assert both `isinstance()` and read-back values
- Flip `[ ] integration test` to `[x]` per task in `model_values.py`
- Quality gate after each task: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
- Import via subpackage `__init__.py` re-exports

---

## Scope Summary

`src/rhapsody_cli/models/elements/values/model_values.py` — 15 checklist rows total, all currently `[ ] integration test`:

**`RPInstanceSlot`** (5 methods): `add_element_value`, `add_string_value`, `get_slot_property`, `get_values`, `set_slot_property`
**`RPInstanceSpecification`** (6 methods): `add_instance_slot`, `get_classifier`, `get_instance_slots`, `is_root_instance_specification`, `populate_slots`, `set_classifier`
**`RPValueSpecification`** (0 own methods — abstract base for `RPInstanceValue`/`RPLiteralSpecification`/`RPContextSpecification`; body is `pass`; no dedicated checklist rows, but a polymorphism smoke task is still included)
**`RPInstanceValue`** (2 methods): `get_value`, `set_value`
**`RPLiteralSpecification`** (2 methods): `get_value`, `set_value`

5 + 6 + 0 + 2 + 2 = **15 methods**, all untested at the integration level.

### Object creation chain (verified from source)

- `RPProject.add_package(name)` (inherited, `model_package.py`) → `RPPackage`
- `RPPackage.add_class(name)` → `RPClass` (an `RPClassifier`), used as the instance specification's classifier
- `RPClassifier.add_attribute(name)` (`model_classifier.py:74`) → `RPAttribute` (an `RPVariable`), used as the `slot_property` argument for `RPInstanceSpecification.add_instance_slot` / `RPInstanceSlot.set_slot_property`
- `RPPackage.add_instance_specification(name)` (`model_package.py:1127`) → `RPInstanceSpecification`
- `RPInstanceSpecification.set_classifier(classifier)` → binds the instance specification to the `RPClass` created above; `get_classifier()` reads it back
- `RPInstanceSpecification.add_instance_slot(name, slot_property)` (`slot_property` = the `RPAttribute` above) → `RPInstanceSlot`
- `RPInstanceSlot.add_string_value(str)` → `RPLiteralSpecification` (a `RPValueSpecification` subclass)
- `RPInstanceSlot.add_element_value(RPModelElement)` (using a second `RPClass` created in the same package as the element value) → `RPInstanceValue` (a `RPValueSpecification` subclass)
- Cleanup: deleting the owning `RPPackage` via `delete_from_project()` cascades to remove the class(es), attribute, instance specification, instance slot, and all values nested inside it

No methods are flagged as unreachable — all 15 methods have a valid, documented creation/exercise path through the existing public API.

---

### Task 1: `RPInstanceSpecification` — shared fixture + classifier/slot management

**Files:**
- Create: `tests/integration/models/elements/values/conftest.py`
- Create: `tests/integration/models/elements/values/test_model_values.py`
- Modify: `src/rhapsody_cli/models/elements/values/model_values.py` (flip checklist boxes only)

**Methods covered:** `add_instance_slot`, `get_classifier`, `get_instance_slots`, `is_root_instance_specification`, `populate_slots`, `set_classifier`

- [ ] **Step 1: Write the shared fixture**

```python
# tests/integration/models/elements/values/conftest.py
"""Shared fixtures for values subpackage integration tests."""

import uuid

import pytest

from rhapsody_cli.models.elements.classifiers import RPAttribute, RPClass
from rhapsody_cli.models.elements.containment import RPPackage, RPProject
from rhapsody_cli.models.elements.values import RPInstanceSpecification


def unique(prefix: str = "Test") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


@pytest.fixture
def instance_spec_factory(test_project: RPProject):
    """Factory fixture: creates an ``RPPackage`` containing a classifier (with
    one attribute) and an ``RPInstanceSpecification`` bound to it.

    Returns a callable ``() -> tuple[RPPackage, RPClass, RPAttribute, RPInstanceSpecification]``.
    The package is deleted (cascading delete of everything nested inside it)
    when the fixture tears down.
    """
    created = []

    def _make():
        pkg: RPPackage = test_project.add_package(unique("ValPkg"))
        test_class: RPClass = pkg.add_class(unique("ValCls"))
        attribute: RPAttribute = test_class.add_attribute(unique("attr"))
        instance_spec = pkg.add_instance_specification(unique("Inst"))
        assert instance_spec is not None
        assert isinstance(instance_spec, RPInstanceSpecification)
        created.append(pkg)
        return pkg, test_class, attribute, instance_spec

    yield _make

    for pkg in created:
        try:
            pkg.delete_from_project()
        except Exception:
            pass
```

- [ ] **Step 2: Write the failing/new integration tests**

```python
# tests/integration/models/elements/values/test_model_values.py
"""Integration tests for the values model elements with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.elements.values import (
    RPInstanceSlot,
    RPInstanceSpecification,
)


def _unique(prefix: str = "Test") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


@pytest.mark.integration
class TestRPInstanceSpecificationIntegration:
    """Integration tests for RPInstanceSpecification with real Rhapsody COM API."""

    def test_classifier_and_slot_management(self, instance_spec_factory) -> None:
        pkg, test_class, attribute, instance_spec = instance_spec_factory()
        try:
            assert isinstance(instance_spec, RPInstanceSpecification)

            # Root instance specifications are not nested inside another one.
            assert instance_spec.is_root_instance_specification() == 1

            instance_spec.set_classifier(test_class)
            assert instance_spec.get_classifier() == test_class

            slot_name = _unique("Slot")
            slot = instance_spec.add_instance_slot(slot_name, attribute)
            assert isinstance(slot, RPInstanceSlot)

            slots = list(instance_spec.get_instance_slots())
            assert slot in slots

            # populate_slots auto-creates any remaining slots for the
            # classifier's attributes that don't already have one; the slot
            # created above must still be present afterwards.
            instance_spec.populate_slots()
            slots_after_populate = list(instance_spec.get_instance_slots())
            assert slot in slots_after_populate
        finally:
            pkg.delete_from_project()
```

For remaining methods in this task's scope, they are all exercised inline above — no further tests are needed for this task.

- [ ] **Step 3: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/values/test_model_values.py -m integration -v -k TestRPInstanceSpecificationIntegration`

- [ ] **Step 4: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/values/model_values.py`, flip `addInstanceSlot`, `getClassifier`, `getInstanceSlots`, `isRootInstanceSpecification`, `populateSlots`, `setClassifier` (under `RPInstanceSpecification`) rows to `[x] integration test`.

- [ ] **Step 5: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 6: Commit**

```bash
git add tests/integration/models/elements/values/conftest.py tests/integration/models/elements/values/test_model_values.py src/rhapsody_cli/models/elements/values/model_values.py
git commit -m "test: add integration tests for RPInstanceSpecification"
```

---

### Task 2: `RPInstanceSlot`

**Files:**
- Modify: `tests/integration/models/elements/values/test_model_values.py`
- Modify: `src/rhapsody_cli/models/elements/values/model_values.py` (flip checklist boxes only)

**Methods covered:** `add_element_value`, `add_string_value`, `get_slot_property`, `get_values`, `set_slot_property`

- [ ] **Step 1: Write the failing/new integration tests**

```python
from rhapsody_cli.models.elements.values import RPInstanceValue, RPLiteralSpecification


@pytest.mark.integration
class TestRPInstanceSlotIntegration:
    """Integration tests for RPInstanceSlot with real Rhapsody COM API."""

    def test_slot_property_and_values(self, instance_spec_factory) -> None:
        pkg, test_class, attribute, instance_spec = instance_spec_factory()
        other_attribute = test_class.add_attribute(_unique("otherAttr"))
        element_val = pkg.add_class(_unique("ElementVal"))
        try:
            instance_spec.set_classifier(test_class)
            slot = instance_spec.add_instance_slot(_unique("Slot"), attribute)
            assert isinstance(slot, RPInstanceSlot)

            # get_slot_property / set_slot_property roundtrip.
            assert slot.get_slot_property() == attribute
            slot.set_slot_property(other_attribute)
            assert slot.get_slot_property() == other_attribute

            # add_string_value returns an RPLiteralSpecification value.
            literal = slot.add_string_value("hello")
            assert isinstance(literal, RPLiteralSpecification)

            # add_element_value returns an RPInstanceValue value.
            instance_value = slot.add_element_value(element_val)
            assert isinstance(instance_value, RPInstanceValue)

            # get_values must surface both values added above.
            values = list(slot.get_values())
            assert literal in values
            assert instance_value in values
        finally:
            pkg.delete_from_project()
```

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/values/test_model_values.py -m integration -v -k TestRPInstanceSlotIntegration`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/values/model_values.py`, flip `addElementValue`, `addStringValue`, `getSlotProperty`, `getValues`, `setSlotProperty` (under `RPInstanceSlot`) rows to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/values/test_model_values.py src/rhapsody_cli/models/elements/values/model_values.py
git commit -m "test: add integration tests for RPInstanceSlot"
```

---

### Task 3: `RPValueSpecification` (polymorphism smoke check — no own methods)

**Files:**
- Modify: `tests/integration/models/elements/values/test_model_values.py`
- Read-only: `src/rhapsody_cli/models/elements/values/model_values.py` (no checklist rows exist for this class — nothing to flip)

**Methods covered:** none directly — `RPValueSpecification` has zero own methods (its body is `pass`; it exists purely as the common base for `RPInstanceValue`, `RPLiteralSpecification`, and `RPContextSpecification`). This task adds a lightweight polymorphism smoke test so the base-class wrapping is proven to resolve correctly, even though there is no checklist box to flip.

- [ ] **Step 1: Write the failing/new integration tests**

```python
from rhapsody_cli.models.elements.values import RPValueSpecification


@pytest.mark.integration
class TestRPValueSpecificationIntegration:
    """Smoke test for RPValueSpecification base-class wrapping (no own methods to test)."""

    def test_instance_value_and_literal_specification_are_value_specifications(
        self, instance_spec_factory
    ) -> None:
        pkg, test_class, attribute, instance_spec = instance_spec_factory()
        element_val = pkg.add_class(_unique("ElementVal2"))
        try:
            instance_spec.set_classifier(test_class)
            slot = instance_spec.add_instance_slot(_unique("Slot2"), attribute)

            literal = slot.add_string_value("world")
            assert isinstance(literal, RPValueSpecification)

            instance_value = slot.add_element_value(element_val)
            assert isinstance(instance_value, RPValueSpecification)
        finally:
            pkg.delete_from_project()
```

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/values/test_model_values.py -m integration -v -k TestRPValueSpecificationIntegration`

- [ ] **Step 3: No checklist boxes to flip**

`RPValueSpecification` has no `[ ] integration test` rows in `model_values.py` (only an `[inherited]` comment and "no deprecated methods" note) — skip this step for this task.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/values/test_model_values.py
git commit -m "test: add polymorphism smoke test for RPValueSpecification"
```

---

### Task 4: `RPInstanceValue`

**Files:**
- Modify: `tests/integration/models/elements/values/test_model_values.py`
- Modify: `src/rhapsody_cli/models/elements/values/model_values.py` (flip checklist boxes only)

**Methods covered:** `get_value`, `set_value`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPInstanceValueIntegration:
    """Integration tests for RPInstanceValue with real Rhapsody COM API."""

    def test_value_roundtrip(self, instance_spec_factory) -> None:
        pkg, test_class, attribute, instance_spec = instance_spec_factory()
        first_val = pkg.add_class(_unique("FirstVal"))
        second_val = pkg.add_class(_unique("SecondVal"))
        try:
            instance_spec.set_classifier(test_class)
            slot = instance_spec.add_instance_slot(_unique("Slot3"), attribute)

            instance_value = slot.add_element_value(first_val)
            assert isinstance(instance_value, RPInstanceValue)
            assert instance_value.get_value() == first_val

            instance_value.set_value(second_val)
            assert instance_value.get_value() == second_val
        finally:
            pkg.delete_from_project()
```

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/values/test_model_values.py -m integration -v -k TestRPInstanceValueIntegration`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/values/model_values.py`, flip `getValue`/`setValue` (under `RPInstanceValue`) rows to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/values/test_model_values.py src/rhapsody_cli/models/elements/values/model_values.py
git commit -m "test: add integration tests for RPInstanceValue"
```

---

### Task 5: `RPLiteralSpecification`

**Files:**
- Modify: `tests/integration/models/elements/values/test_model_values.py`
- Modify: `src/rhapsody_cli/models/elements/values/model_values.py` (flip checklist boxes only)

**Methods covered:** `get_value`, `set_value`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPLiteralSpecificationIntegration:
    """Integration tests for RPLiteralSpecification with real Rhapsody COM API."""

    def test_value_roundtrip(self, instance_spec_factory) -> None:
        pkg, test_class, attribute, instance_spec = instance_spec_factory()
        try:
            instance_spec.set_classifier(test_class)
            slot = instance_spec.add_instance_slot(_unique("Slot4"), attribute)

            literal = slot.add_string_value("initial")
            assert isinstance(literal, RPLiteralSpecification)
            assert literal.get_value() == "initial"

            literal.set_value("changed")
            assert literal.get_value() == "changed"
        finally:
            pkg.delete_from_project()
```

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/values/test_model_values.py -m integration -v -k TestRPLiteralSpecificationIntegration`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/values/model_values.py`, flip `getValue`/`setValue` (under `RPLiteralSpecification`) rows to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/values/test_model_values.py src/rhapsody_cli/models/elements/values/model_values.py
git commit -m "test: add integration tests for RPLiteralSpecification"
```

---

### Task 6: Full Subpackage Verification

**Files:**
- Read-only verification: `src/rhapsody_cli/models/elements/values/model_values.py`
- Read-only verification: `tests/integration/models/elements/values/conftest.py`
- Read-only verification: `tests/integration/models/elements/values/test_model_values.py`

- [ ] **Step 1: Confirm all 15 checklist rows are flipped**

```bash
grep -c "\[ \] integration test" src/rhapsody_cli/models/elements/values/model_values.py
```

Expected output: `0`.

- [ ] **Step 2: Run the complete integration test suite for the subpackage**

Run: `pytest tests/integration/models/elements/values/ -m integration -v`

All tests from Tasks 1–5 must pass. No `xfail`-marked tests are expected in this subpackage — all 15 methods have a valid public-API creation/exercise path.

- [ ] **Step 3: Run the full quality gate one final time**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 4: Commit final verification (if any cleanup was needed)**

```bash
git add -A
git commit -m "test: complete values subpackage integration test coverage"
```
