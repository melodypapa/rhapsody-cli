# Integration Test: Own-Class-Methods Focus Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite the element-focused integration test files so each one tests only the methods its class actually owns; parent-class methods are used strictly for setup, and redefined methods are exercised in a way that proves the correct override is invoked.

**Architecture:** No production code changes. Every model method already exists and has unit-test coverage via fakes. This plan only edits files under `tests/integration/models/elements/`. The gold-standard pattern to imitate is `tests/integration/models/elements/classifiers/test_model_classifier.py` and the user-cited example `test_model_association_class.py` (uses `add_relation_to` — an `RPClassifier` method — only to build the fixture, then asserts on `RPAssociationClass`'s own four methods). Per test file we either (a) replace parent-method tests with own-method tests, or (b) delete pure setup-only / duplicate tests.

**Tech Stack:** pytest (`@pytest.mark.integration`), Rhapsody COM wrappers under `src/rhapsody_cli/models/`, fakes-free live COM.

## Global Constraints

- **Runtime needs Windows + a running Rhapsody instance.** These tests cannot be executed in this environment. The verification step for every task is therefore `pytest <file> --collect-only -q` (proves the module imports and every test is collected with no syntax/import errors). Live execution happens later on `windows-latest` CI.
- **Model implementations already exist and are unit-tested.** Do NOT edit any file under `src/`. If a test reveals a model bug, stop and report it instead of "fixing" the model inline.
- **Python 3.8 compatible.** No `from __future__ import annotations` (forbidden). No lowercase-generic runtime annotations like `tuple[X, Y]` / `X | Y`; use `typing.Tuple` / `typing.Union` if a compound annotation is needed (the existing tests avoid compound returns — follow that lead).
- **Style gate per file:** `ruff check <file> && black --check <file> && mypy <file>` must pass. line-length 200, snake_case, full-package imports (no relative imports).
- **Naming:** the COM identifiers stay camelCase (e.g. `self._com.addClass`); only the Python wrapper method names are snake_case.
- **One commit per task.** Branch: `test/integration-own-methods-focus` (branch off `main`). Commit message prefix `test:`.

## Reference: the pattern to follow

`tests/integration/models/elements/classifiers/test_model_classifier.py` is the reference. Each test:
1. Builds a fixture using **parent** methods only (`test_project` → `add_package` → `add_class`).
2. Calls **only methods owned by the class under test**.
3. Cleans up in `finally`.

The class-under-test's own methods are read from the model module's docstring checklist lines that are **not** marked `[inherited]`. Read the model file before writing each task.

---

## File Structure

| File (test) | Class under test | Action |
|-------------|------------------|--------|
| `tests/integration/models/elements/variables/test_model_attribute.py` | `RPAttribute` | **Rewrite**: 4 current tests all hit `RPVariable`/`RPClassifier`; replace with 6 tests covering all 12 `RPAttribute`-owned getters/setters. |
| `tests/integration/models/elements/classifiers/test_model_stereotype.py` | `RPStereotype` | **Rewrite**: 2 current tests only call `RPModelElement.add_stereotype`; replace with 3 tests covering all 6 `RPStereotype`-owned methods. |
| `tests/integration/models/elements/classifiers/test_model_statechart.py` | `RPStatechart` | **Rewrite**: 1 current test only calls `RPClassifier.add_statechart`; replace with 4 tests on `RPStatechart`-owned methods. |
| `tests/integration/models/elements/classifiers/test_model_usecase.py` | `RPUseCase` | **Rewrite**: 1 current test is creation-only; replace with 4 tests on `RPUseCase`-owned methods. |
| `tests/integration/models/elements/requirements/test_model_requirements.py` | `RPRequirement` | **Extend**: keep creation test, add `RPRequirement`-owned `get_requirement_id`/`set_requirement_id` roundtrip. |
| `tests/integration/models/elements/classifiers/test_model_class.py` | `RPClass` | **Trim**: delete `test_create_operation_in_class` (duplicate `RPClassifier` coverage) + 3 setup-only tests. |
| `tests/integration/models/elements/classifiers/test_model_actor.py` | `RPActor` | **Trim**: delete 2 setup-only tests; keep the 2 that exercise `RPActor`-owned overrides. |
| `tests/integration/models/elements/common/test_model_misc.py` | `RPConstraint` | **Extend**: add `RPConstraint.get_constraints_by_me` test (`RPComment` has no own methods — leave it). |
| `tests/integration/models/elements/classifiers/test_model_association_class.py` | `RPAssociationClass` | **Fix**: uncomment the `xfail` decorator so the file matches its own docstring. |

---

### Task 1: Rewrite `test_model_attribute.py` to test `RPAttribute`-owned methods

**Files:**
- Rewrite: `tests/integration/models/elements/variables/test_model_attribute.py`
- Read-only reference: `src/rhapsody_cli/models/elements/variables/model_variables.py` (class `RPAttribute` — its 12 own methods: `get_is_constant`/`set_is_constant`, `get_is_ordered`/`set_is_ordered`, `get_is_reference`/`set_is_reference`, `get_is_static`/`set_is_static`, `get_multiplicity`/`set_multiplicity`, `get_visibility`/`set_visibility`).

**Interfaces:**
- Consumes: `RPProject.add_package(name) -> RPPackage`; `RPPackage.add_class(name) -> RPClass`; `RPClass.add_attribute(name) -> RPAttribute` (this last one is an `RPClassifier` method — used **only** as setup to obtain the instance).
- Produces: nothing (test-only).

- [ ] **Step 1: Replace the file contents**

Overwrite `tests/integration/models/elements/variables/test_model_attribute.py` with:

```python
"""Integration tests for RPAttribute with live Rhapsody COM API.

Scope: only methods that RPAttribute owns (the 12 is_*/multiplicity/visibility
getters and setters declared on IRPAttribute). Parent-class behaviour
(IRPVariable::set_declaration / get_type / set_default_value, IRPClassifier::
add_attribute) is exercised in its own integration tests; here
``add_attribute`` is used purely to obtain an RPAttribute instance.
"""

import uuid

import pytest

from rhapsody_cli.models.elements.containment import RPPackage, RPProject
from rhapsody_cli.models.elements.variables import RPAttribute


@pytest.mark.integration
class TestRPAttributeIntegration:
    """Integration tests for RPAttribute with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_is_static_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            assert isinstance(attr, RPAttribute)
            assert attr.get_is_static() is False
            attr.set_is_static(True)
            assert attr.get_is_static() is True
            attr.set_is_static(False)
            assert attr.get_is_static() is False
        finally:
            test_class.delete_from_project()

    def test_is_constant_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            assert attr.get_is_constant() in (0, 1)
            attr.set_is_constant(True)
            assert attr.get_is_constant() == 1
            attr.set_is_constant(False)
            assert attr.get_is_constant() == 0
        finally:
            test_class.delete_from_project()

    def test_is_ordered_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            assert attr.get_is_ordered() in (0, 1)
            attr.set_is_ordered(True)
            assert attr.get_is_ordered() == 1
            attr.set_is_ordered(False)
            assert attr.get_is_ordered() == 0
        finally:
            test_class.delete_from_project()

    def test_is_reference_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            assert attr.get_is_reference() in (0, 1)
            attr.set_is_reference(True)
            assert attr.get_is_reference() == 1
            attr.set_is_reference(False)
            assert attr.get_is_reference() == 0
        finally:
            test_class.delete_from_project()

    def test_multiplicity_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            attr.set_multiplicity("0..*")
            assert attr.get_multiplicity() == "0..*"
        finally:
            test_class.delete_from_project()

    def test_visibility_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            attr = test_class.add_attribute(attr_name)
            attr.set_visibility("private")
            assert attr.get_visibility() == "private"
        finally:
            test_class.delete_from_project()
```

- [ ] **Step 2: Verify the file collects without import/syntax errors**

Run: `python -m pytest tests/integration/models/elements/variables/test_model_attribute.py --collect-only -q`
Expected: 6 test IDs listed, no errors:
```
...::TestRPAttributeIntegration::test_is_static_roundtrip
...::TestRPAttributeIntegration::test_is_constant_roundtrip
...::TestRPAttributeIntegration::test_is_ordered_roundtrip
...::TestRPAttributeIntegration::test_is_reference_roundtrip
...::TestRPAttributeIntegration::test_multiplicity_roundtrip
...::TestRPAttributeIntegration::test_visibility_roundtrip
```

- [ ] **Step 3: Lint the file**

Run: `ruff check tests/integration/models/elements/variables/test_model_attribute.py && black --check tests/integration/models/elements/variables/test_model_attribute.py && mypy tests/integration/models/elements/variables/test_model_attribute.py`
Expected: all clean (no output / "All done!").

- [ ] **Step 4: Commit**

```bash
git add tests/integration/models/elements/variables/test_model_attribute.py
git commit -m "test: rewrite RPAttribute integration tests to cover own methods"
```

---

### Task 2: Rewrite `test_model_stereotype.py` to test `RPStereotype`-owned methods

**Files:**
- Rewrite: `tests/integration/models/elements/classifiers/test_model_stereotype.py`
- Read-only reference: `src/rhapsody_cli/models/elements/classifiers/model_stereotype.py` (class `RPStereotype` — 6 own methods: `add_meta_class`, `remove_meta_class`, `get_of_meta_class`, `get_icon`, `get_is_new_term`, `set_is_new_term`).

**Interfaces:**
- Consumes: `RPModelElement.add_stereotype(name, meta_type) -> RPStereotype` (a parent `RPModelElement` method — used **only** to build the stereotype fixture; its own coverage lives in `test_core.py::TestRPModelElementStereotypesTagsIntegration`).
- Produces: nothing.

- [ ] **Step 1: Replace the file contents**

Overwrite `tests/integration/models/elements/classifiers/test_model_stereotype.py` with:

```python
"""Integration tests for RPStereotype with live Rhapsody COM API.

Scope: only methods that RPStereotype owns (IRPStereotype::addMetaClass,
removeMetaClass, getOfMetaClass, getIcon, getIsNewTerm, setIsNewTerm).
``add_stereotype`` (an IRPModelElement method) is used only to create the
fixture; its behaviour is covered by test_core.py.
"""

import uuid

import pytest

from rhapsody_cli.models.elements.classifiers import RPStereotype
from rhapsody_cli.models.elements.containment import RPPackage, RPProject


@pytest.mark.integration
class TestRPStereotypeIntegration:
    """Integration tests for RPStereotype with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_meta_class_add_get_remove(self, test_project: RPProject) -> None:
        pkg_name = self._unique("SterPkg")
        stereo_name = self._unique("MyStereotype")
        pkg = self._create_package(test_project, pkg_name)
        try:
            stereotype = pkg.add_stereotype(stereo_name, "Class")
            assert isinstance(stereotype, RPStereotype)
            # Created for "Class"; adding another applicable metaclass should grow the list.
            before = stereotype.get_of_meta_class()
            assert isinstance(before, str)
            stereotype.add_meta_class("Attribute")
            after_add = stereotype.get_of_meta_class()
            assert "Attribute" in after_add
            stereotype.remove_meta_class("Attribute")
            after_remove = stereotype.get_of_meta_class()
            assert "Attribute" not in after_remove
        finally:
            stereotype.delete_from_project()

    def test_is_new_term_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("SterPkg")
        stereo_name = self._unique("MyStereotype")
        pkg = self._create_package(test_project, pkg_name)
        try:
            stereotype = pkg.add_stereotype(stereo_name, "Class")
            assert stereotype.get_is_new_term() in (0, 1)
            stereotype.set_is_new_term(1)
            assert stereotype.get_is_new_term() == 1
            stereotype.set_is_new_term(0)
            assert stereotype.get_is_new_term() == 0
        finally:
            stereotype.delete_from_project()

    def test_get_icon_is_string(self, test_project: RPProject) -> None:
        pkg_name = self._unique("SterPkg")
        stereo_name = self._unique("MyStereotype")
        pkg = self._create_package(test_project, pkg_name)
        try:
            stereotype = pkg.add_stereotype(stereo_name, "Class")
            icon = stereotype.get_icon()
            assert isinstance(icon, str)
        finally:
            stereotype.delete_from_project()
```

- [ ] **Step 2: Verify the file collects**

Run: `python -m pytest tests/integration/models/elements/classifiers/test_model_stereotype.py --collect-only -q`
Expected: 3 test IDs (`test_meta_class_add_get_remove`, `test_is_new_term_roundtrip`, `test_get_icon_is_string`), no errors.

- [ ] **Step 3: Lint the file**

Run: `ruff check tests/integration/models/elements/classifiers/test_model_stereotype.py && black --check tests/integration/models/elements/classifiers/test_model_stereotype.py && mypy tests/integration/models/elements/classifiers/test_model_stereotype.py`
Expected: clean.

- [ ] **Step 4: Commit**

```bash
git add tests/integration/models/elements/classifiers/test_model_stereotype.py
git commit -m "test: rewrite RPStereotype integration tests to cover own methods"
```

---

### Task 3: Rewrite `test_model_statechart.py` to test `RPStatechart`-owned methods

**Files:**
- Rewrite: `tests/integration/models/elements/classifiers/test_model_statechart.py`
- Read-only reference: `src/rhapsody_cli/models/elements/classifiers/model_statechart.py` (class `RPStatechart` — own methods include `create_graphics`, `close_diagram`, `get_root_state`, `get_its_class`, `get_is_main_behavior`, `delete_state`, `populate_diagram`, etc.). **`add_statechart` belongs to `RPClassifier`, not `RPStatechart`** — it is setup only.

**Interfaces:**
- Consumes: `RPClass.add_statechart() -> RPStatechart` (an `RPClassifier` method — setup only; already covered by `test_model_classifier.py::test_get_statechart`).
- Produces: nothing.

- [ ] **Step 1: Replace the file contents**

Overwrite `tests/integration/models/elements/classifiers/test_model_statechart.py` with:

```python
"""Integration tests for RPStatechart with live Rhapsody COM API.

Scope: only methods that RPStatechart owns (IRPStatechart::createGraphics,
closeDiagram, getRootState, getItsClass, getIsMainBehavior, ...).
``add_statechart`` is an IRPClassifier method used only to build the fixture
(its coverage is in test_model_classifier.py).
"""

import uuid

import pytest

from rhapsody_cli.models.elements.classifiers import RPClass, RPStatechart
from rhapsody_cli.models.elements.containment import RPPackage, RPProject
from rhapsody_cli.models.core import RPModelElement


@pytest.mark.integration
class TestRPStatechartIntegration:
    """Integration tests for RPStatechart with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_get_its_class_returns_owning_class(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ScPkg")
        class_name = self._unique("ScCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            sc = test_class.add_statechart()
            assert isinstance(sc, RPStatechart)
            owner = sc.get_its_class()
            assert isinstance(owner, RPClass)
            assert owner.get_name() == class_name
        finally:
            test_class.delete_from_project()

    def test_get_is_main_behavior(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ScPkg")
        class_name = self._unique("ScCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            sc = test_class.add_statechart()
            assert sc.get_is_main_behavior() in (0, 1)
        finally:
            test_class.delete_from_project()

    def test_get_root_state(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ScPkg")
        class_name = self._unique("ScCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            sc = test_class.add_statechart()
            root = sc.get_root_state()
            assert root is not None
            assert isinstance(root, RPModelElement)
        finally:
            test_class.delete_from_project()

    def test_create_graphics_then_close_diagram(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ScPkg")
        class_name = self._unique("ScCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            sc = test_class.add_statechart()
            sc.create_graphics()  # no return value; verify it does not raise
            sc.close_diagram()  # no return value; verify it does not raise
        finally:
            test_class.delete_from_project()
```

- [ ] **Step 2: Verify the file collects**

Run: `python -m pytest tests/integration/models/elements/classifiers/test_model_statechart.py --collect-only -q`
Expected: 4 test IDs (`test_get_its_class_returns_owning_class`, `test_get_is_main_behavior`, `test_get_root_state`, `test_create_graphics_then_close_diagram`), no errors.

- [ ] **Step 3: Lint the file**

Run: `ruff check tests/integration/models/elements/classifiers/test_model_statechart.py && black --check tests/integration/models/elements/classifiers/test_model_statechart.py && mypy tests/integration/models/elements/classifiers/test_model_statechart.py`
Expected: clean.

- [ ] **Step 4: Commit**

```bash
git add tests/integration/models/elements/classifiers/test_model_statechart.py
git commit -m "test: rewrite RPStatechart integration tests to cover own methods"
```

---

### Task 4: Rewrite `test_model_usecase.py` to test `RPUseCase`-owned methods

**Files:**
- Rewrite: `tests/integration/models/elements/classifiers/test_model_usecase.py`
- Read-only reference: `src/rhapsody_cli/models/elements/classifiers/model_usecase.py` (class `RPUseCase` — own methods: `add_extension_point`, `get_extension_points`, `delete_extension_point`, `find_extension_point`, `get_entry_points`, `delete_entry_point`, `get_is_behavior_overriden`, `set_is_behavior_overriden`, plus diagram ones). **Note:** unlike `RPActor`, `RPUseCase.add_event_reception_with_event` has a *real* COM implementation (no `NotImplementedError`) — but it needs an event fixture, so we keep this task focused on the extension-point + behavior-override methods.

**Interfaces:**
- Consumes: `RPPackage.add_use_case(name) -> RPUseCase` (setup only).
- Produces: nothing.

- [ ] **Step 1: Replace the file contents**

Overwrite `tests/integration/models/elements/classifiers/test_model_usecase.py` with:

```python
"""Integration tests for RPUseCase with live Rhapsody COM API.

Scope: only methods that RPUseCase owns (IRPUseCase::addExtensionPoint,
getExtensionPoints, findExtensionPoint, deleteExtensionPoint, getEntryPoints,
getIsBehaviorOverriden, setIsBehaviorOverriden). ``add_use_case`` is an
IRPPackage method used only to build the fixture.
"""

import uuid

import pytest

from rhapsody_cli.models.elements.classifiers import RPUseCase
from rhapsody_cli.models.elements.containment import RPPackage, RPProject


@pytest.mark.integration
class TestRPUseCaseIntegration:
    """Integration tests for RPUseCase with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_extension_point_add_get_find_delete(self, test_project: RPProject) -> None:
        pkg_name = self._unique("UcPkg")
        uc_name = self._unique("MyUseCase")
        ep_name = self._unique("MyExtensionPoint")
        pkg = self._create_package(test_project, pkg_name)
        uc = pkg.add_use_case(uc_name)
        try:
            assert isinstance(uc, RPUseCase)
            uc.add_extension_point(ep_name)
            assert ep_name in [str(e) for e in uc.get_extension_points()]
            found = uc.find_extension_point(ep_name)
            assert found is not None and found.get_name() == ep_name
            uc.delete_extension_point(ep_name)
            assert ep_name not in [str(e) for e in uc.get_extension_points()]
        finally:
            uc.delete_from_project()

    def test_get_entry_points_empty(self, test_project: RPProject) -> None:
        pkg_name = self._unique("UcPkg")
        uc_name = self._unique("MyUseCase")
        pkg = self._create_package(test_project, pkg_name)
        uc = pkg.add_use_case(uc_name)
        try:
            entry_points = list(uc.get_entry_points())
            assert isinstance(entry_points, list)
        finally:
            uc.delete_from_project()

    def test_is_behavior_overriden_roundtrip(self, test_project: RPProject) -> None:
        # RPUseCase redefines getIsBehaviorOverriden/setIsBehaviorOverriden as int-typed
        # (its sibling RPClass also has them; this asserts the int contract specifically).
        pkg_name = self._unique("UcPkg")
        uc_name = self._unique("MyUseCase")
        pkg = self._create_package(test_project, pkg_name)
        uc = pkg.add_use_case(uc_name)
        try:
            assert uc.get_is_behavior_overriden() in (0, 1)
            uc.set_is_behavior_overriden(1)
            assert uc.get_is_behavior_overriden() == 1
            uc.set_is_behavior_overriden(0)
            assert uc.get_is_behavior_overriden() == 0
        finally:
            uc.delete_from_project()
```

- [ ] **Step 2: Verify the file collects**

Run: `python -m pytest tests/integration/models/elements/classifiers/test_model_usecase.py --collect-only -q`
Expected: 3 test IDs (`test_extension_point_add_get_find_delete`, `test_get_entry_points_empty`, `test_is_behavior_overriden_roundtrip`), no errors.

- [ ] **Step 3: Lint the file**

Run: `ruff check tests/integration/models/elements/classifiers/test_model_usecase.py && black --check tests/integration/models/elements/classifiers/test_model_usecase.py && mypy tests/integration/models/elements/classifiers/test_model_usecase.py`
Expected: clean.

- [ ] **Step 4: Commit**

```bash
git add tests/integration/models/elements/classifiers/test_model_usecase.py
git commit -m "test: rewrite RPUseCase integration tests to cover own methods"
```

---

### Task 5: Extend `test_model_requirements.py` with `RPRequirement`-owned method test

**Files:**
- Modify: `tests/integration/models/elements/requirements/test_model_requirements.py`
- Read-only reference: `src/rhapsody_cli/models/elements/requirements/model_requirements.py` (class `RPRequirement` — 2 own methods: `get_requirement_id`, `set_requirement_id`).

**Interfaces:**
- Consumes: `RPModelElement.add_new_aggr("Requirement", name) -> RPRequirement` (parent method — setup only).
- Produces: nothing.

- [ ] **Step 1: Replace the file contents**

Overwrite `tests/integration/models/elements/requirements/test_model_requirements.py` with:

```python
"""Integration tests for RPRequirement with live Rhapsody COM API.

Scope: the RPRequirement-owned methods (IRPRequirement::getRequirementID,
setRequirementID). A creation smoke-test is kept to confirm the element is
wrapped correctly; ``add_new_aggr`` is an IRPModelElement method used only
to build the fixture.
"""

import uuid

import pytest

from rhapsody_cli.models.elements.containment import RPPackage, RPProject
from rhapsody_cli.models.elements.requirements import RPRequirement


@pytest.mark.integration
class TestRPRequirementIntegration:
    """Integration tests for RPRequirement with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_create_requirement_in_package(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ReqPkg")
        req_name = self._unique("MyRequirement")
        pkg = self._create_package(test_project, pkg_name)
        try:
            req = pkg.add_new_aggr("Requirement", req_name)
            assert req is not None
            assert isinstance(req, RPRequirement)
            assert req.get_name() == req_name
            assert req.get_meta_class() == "Requirement"
        finally:
            req.delete_from_project()

    def test_requirement_id_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ReqPkg")
        req_name = self._unique("MyRequirement")
        pkg = self._create_package(test_project, pkg_name)
        req = pkg.add_new_aggr("Requirement", req_name)
        try:
            assert isinstance(req.get_requirement_id(), str)
            req.set_requirement_id("REQ-001")
            assert req.get_requirement_id() == "REQ-001"
            req.set_requirement_id("REQ-002")
            assert req.get_requirement_id() == "REQ-002"
        finally:
            req.delete_from_project()
```

- [ ] **Step 2: Verify the file collects**

Run: `python -m pytest tests/integration/models/elements/requirements/test_model_requirements.py --collect-only -q`
Expected: 2 test IDs (`test_create_requirement_in_package`, `test_requirement_id_roundtrip`), no errors.

- [ ] **Step 3: Lint the file**

Run: `ruff check tests/integration/models/elements/requirements/test_model_requirements.py && black --check tests/integration/models/elements/requirements/test_model_requirements.py && mypy tests/integration/models/elements/requirements/test_model_requirements.py`
Expected: clean.

- [ ] **Step 4: Commit**

```bash
git add tests/integration/models/elements/requirements/test_model_requirements.py
git commit -m "test: add RPRequirement.owned get/set_requirement_id integration test"
```

---

### Task 6: Trim `test_model_class.py` — remove `RPClassifier`-duplicate and setup-only tests

**Files:**
- Modify: `tests/integration/models/elements/classifiers/test_model_class.py`
- Read-only reference: `src/rhapsody_cli/models/elements/classifiers/model_class.py` (class `RPClass`). The methods `add_operation` / `get_operations` are declared on **`RPClassifier`**, not `RPClass`; their integration coverage lives in `test_model_classifier.py`. `get_name` / `get_meta_class` / `get_owner` / `delete_from_project` are `RPModelElement` methods covered in `test_core.py`.

**Interfaces:** none new.

**Tests to delete and why:**
- `test_create_operation_in_class` — exercises `RPClassifier.add_operation` + `RPClassifier.get_operations` (wrong class; duplicate of `test_model_classifier.py`).
- `test_create_class_in_package` — only `RPModelElement.get_name`/`get_meta_class` + `RPPackage.add_class` (setup-only, no `RPClass` method).
- `test_class_hierarchy_navigation` — only `RPModelElement.get_owner` (setup-only).
- `test_class_delete` — only `RPModelElement.delete_from_project` (setup-only).

- [ ] **Step 1: Delete the four tests**

In `tests/integration/models/elements/classifiers/test_model_class.py`, remove these four entire method definitions (each runs from its `def test_...` line through the closing `test_class.delete_from_project()` of its `try/finally`):
- `test_create_class_in_package`
- `test_class_hierarchy_navigation`
- `test_create_operation_in_class`
- `test_class_delete`

Leave every other test in the file untouched (they all call `RPClass`-owned methods: `add_superclass`, `add_constructor`, `add_destructor`, `get_is_abstract`, `add_type`, `add_reception`, `add_event_reception`, `add_triggered_operation`, `add_class`, `delete_*`, `get_is_active`, etc.).

After deletion, confirm the remaining first test is `test_class_inheritance`.

- [ ] **Step 2: Verify the file still collects the expected tests**

Run: `python -m pytest tests/integration/models/elements/classifiers/test_model_class.py --collect-only -q`
Expected: the four deleted IDs are gone; the remaining IDs include at least `test_class_inheritance`, `test_constructor_destructor`, `test_set_is_abstract_raises_not_implemented`, `test_type_management`, `test_add_and_delete_reception`, `test_active_flag_roundtrip`, `test_behavior_overriden_roundtrip`, `test_is_composite_readonly`, `test_is_final_roundtrip`, `test_is_reactive_readonly`, `test_update_contained_diagrams_on_server`, `test_delete_nested_class`, `test_delete_constructor`, `test_delete_destructor`, `test_delete_event_reception`, `test_delete_type`, `test_add_event_reception`, `test_add_event_reception_with_event`, `test_add_triggered_operation`. No errors.

- [ ] **Step 3: Lint the file**

Run: `ruff check tests/integration/models/elements/classifiers/test_model_class.py && black --check tests/integration/models/elements/classifiers/test_model_class.py && mypy tests/integration/models/elements/classifiers/test_model_class.py`
Expected: clean. (If `RPOperation`/`cast` imports become unused after removing `test_create_operation_in_class`, ruff will flag `F401` — remove any now-unused import that ruff names.)

- [ ] **Step 4: Commit**

```bash
git add tests/integration/models/elements/classifiers/test_model_class.py
git commit -m "test: drop RPClassifier-duplicate and setup-only tests from RPClass suite"
```

---

### Task 7: Trim `test_model_actor.py` — remove setup-only tests

**Files:**
- Modify: `tests/integration/models/elements/classifiers/test_model_actor.py`
- Read-only reference: `src/rhapsody_cli/models/elements/classifiers/model_actor.py` (class `RPActor(RPClassifier)`). `RPActor` *redefines* `get_is_behavior_overriden`/`set_is_behavior_overriden`/`update_contained_diagrams_on_server` with **different signatures** (`bool` / no-arg) than its sibling `RPClass` (`int` / `int`-arg). The tests that stay assert those `bool` contracts and so prove the correct override is invoked.

**Interfaces:** none new.

**Tests to delete and why:**
- `test_create_actor_in_package` — only `RPModelElement.get_name`/`get_meta_class` + `RPPackage.get_actors` (setup-only, no `RPActor` method).
- `test_actor_owner` — only `RPModelElement.get_owner` (setup-only).

**Tests to keep:** `test_actor_behavior_override` (exercises `RPActor.get_is_behavior_overriden`/`set_is_behavior_overriden` with `is True`/`is False` — would fail if it resolved to the `RPClass` `int` version) and `test_add_event_reception_with_event` (exercises `RPActor.add_event_reception_with_event` which raises `NotImplementedError`).

- [ ] **Step 1: Delete the two setup-only tests**

In `tests/integration/models/elements/classifiers/test_model_actor.py`, remove the entire `test_create_actor_in_package` method and the entire `test_actor_owner` method. Keep `test_actor_behavior_override` and `test_add_event_reception_with_event`. After deletion the first remaining test is `test_actor_behavior_override`.

- [ ] **Step 2: Verify the file still collects the expected tests**

Run: `python -m pytest tests/integration/models/elements/classifiers/test_model_actor.py --collect-only -q`
Expected: 2 test IDs only — `test_actor_behavior_override`, `test_add_event_reception_with_event`. No errors.

- [ ] **Step 3: Lint the file**

Run: `ruff check tests/integration/models/elements/classifiers/test_model_actor.py && black --check tests/integration/models/elements/classifiers/test_model_actor.py && mypy tests/integration/models/elements/classifiers/test_model_actor.py`
Expected: clean. (If `RPActor` import becomes unused after deletion — it won't, both kept tests still reference it — do not remove it. Only remove imports ruff reports as `F401` unused.)

- [ ] **Step 4: Commit**

```bash
git add tests/integration/models/elements/classifiers/test_model_actor.py
git commit -m "test: drop setup-only tests from RPActor suite"
```

---

### Task 8: Extend `test_model_misc.py` with `RPConstraint.get_constraints_by_me` test

**Files:**
- Modify: `tests/integration/models/elements/common/test_model_misc.py`
- Read-only reference: `src/rhapsody_cli/models/elements/common/model_misc.py` (class `RPConstraint` — 1 own method: `get_constraints_by_me`). `RPComment` has **no** own methods (only `[inherited]`), so its creation smoke-test is left as-is.

**Interfaces:**
- Consumes: `RPModelElement.add_new_aggr("Constraint", name) -> RPConstraint` (parent method — setup only).
- Produces: nothing.

- [ ] **Step 1: Add a test to the existing `TestRPConstraintIntegration` class**

In `tests/integration/models/elements/common/test_model_misc.py`, inside the existing `TestRPConstraintIntegration` class, add this method after `test_create_constraint_in_package`:

```python
    def test_get_constraints_by_me_returns_collection(self, test_project: RPProject) -> None:
        from rhapsody_cli.models.core import RPCollection

        pkg_name = self._unique("ConPkg")
        con_name = self._unique("MyConstraint")
        pkg = self._create_package(test_project, pkg_name)
        constraint = pkg.add_new_aggr("Constraint", con_name)
        try:
            result = constraint.get_constraints_by_me()
            assert isinstance(result, RPCollection)
            assert isinstance(result.get_count(), int)
        finally:
            constraint.delete_from_project()
```

- [ ] **Step 2: Verify the file collects**

Run: `python -m pytest tests/integration/models/elements/common/test_model_misc.py --collect-only -q`
Expected: existing tests plus the new `...::TestRPConstraintIntegration::test_get_constraints_by_me_returns_collection`. No errors.

- [ ] **Step 3: Lint the file**

Run: `ruff check tests/integration/models/elements/common/test_model_misc.py && black --check tests/integration/models/elements/common/test_model_misc.py && mypy tests/integration/models/elements/common/test_model_misc.py`
Expected: clean.

- [ ] **Step 4: Commit**

```bash
git add tests/integration/models/elements/common/test_model_misc.py
git commit -m "test: add RPConstraint.get_constraints_by_me integration test"
```

---

### Task 9: Fix `test_model_association_class.py` xfail/docstring inconsistency

**Files:**
- Modify: `tests/integration/models/elements/classifiers/test_model_association_class.py`
- Read-only reference: the file's own class docstring states *"the integration test below is marked ``xfail``"*, but the `@pytest.mark.xfail(...)` line is currently **commented out** (`# @pytest.mark.xfail(...)`), so the test runs and hard-fails instead of xfail-ing. The limitation is real: `addRelationTo(linkName)` does not create an `AssociationClass` in this Rhapsody COM build.

**Interfaces:** none new.

- [ ] **Step 1: Uncomment the xfail decorator**

In `tests/integration/models/elements/classifiers/test_model_association_class.py`, change the commented decorator line directly above `def test_association_class_found_via_package`:

From:
```python
    # @pytest.mark.xfail(strict=False, reason="addRelationTo(linkName) does not create AssociationClass in this Rhapsody COM build")
    def test_association_class_found_via_package(self, test_project: RPProject) -> None:
```

To:
```python
    @pytest.mark.xfail(strict=False, reason="addRelationTo(linkName) does not create AssociationClass in this Rhapsody COM build")
    def test_association_class_found_via_package(self, test_project: RPProject) -> None:
```

Change only the leading `# ` — leave the reason string and everything else untouched.

- [ ] **Step 2: Verify the file collects**

Run: `python -m pytest tests/integration/models/elements/classifiers/test_model_association_class.py --collect-only -q`
Expected: 1 test ID `...::TestRPAssociationClassIntegration::test_association_class_found_via_package`, no errors.

- [ ] **Step 3: Lint the file**

Run: `ruff check tests/integration/models/elements/classifiers/test_model_association_class.py && black --check tests/integration/models/elements/classifiers/test_model_association_class.py && mypy tests/integration/models/elements/classifiers/test_model_association_class.py`
Expected: clean.

- [ ] **Step 4: Commit**

```bash
git add tests/integration/models/elements/classifiers/test_model_association_class.py
git commit -m "test: mark RPAssociationClass integration test xfail to match its docstring"
```

---

### Task 10: Whole-suite collection gate + final verification

**Files:** none modified (verification only).

- [ ] **Step 1: Collect the entire integration tree**

Run: `python -m pytest tests/integration/ --collect-only -q`
Expected: every integration module collects with no import/syntax errors. Count the `RPAttribute` (6), `RPStereotype` (3), `RPStatechart` (4), `RPUseCase` (3), `RPRequirement` (2), `RPClass` (19, down from 23), `RPActor` (2, down from 4), `RPConstraint` (2) IDs and confirm they match the per-task expectations.

- [ ] **Step 2: Run the full lint gate on the touched files**

Run:
```bash
ruff check tests/integration/ && black --check tests/integration/ && mypy tests/integration/
```
Expected: clean.

- [ ] **Step 3: Confirm unit tests still pass (sanity — nothing under src/ changed)**

Run: `python -m pytest tests/unit/ -q`
Expected: all pass.

- [ ] **Step 4: Push the branch and open review**

```bash
git push -u origin test/integration-own-methods-focus
```
Note in the PR description that live execution is Windows-only (CI); locally only `--collect-only` was used.

---

## Self-Review

**1. Spec coverage (each audit finding → a task):**
- `test_model_attribute.py` all-parent → Task 1 ✅
- `test_model_stereotype.py` add_stereotype-only → Task 2 ✅
- `test_model_statechart.py` add_statechart-only → Task 3 ✅
- `test_model_usecase.py` creation-only → Task 4 ✅
- `test_model_requirements.py` creation-only → Task 5 ✅
- `test_model_class.py` `RPClassifier`-duplicate + setup-only → Task 6 ✅
- `test_model_actor.py` setup-only → Task 7 ✅
- `test_model_misc.py` `RPConstraint` untested → Task 8 ✅
- `test_model_association_class.py` xfail/docstring mismatch → Task 9 ✅
- Whole-suite verification → Task 10 ✅
- (Files already correct — `test_model_classifier.py`, `test_model_interface_item.py`, `test_model_operation.py`, `test_core.py`, `test_model_project.py`, `test_model_diagrams.py`, `test_model_generalization.py`, `cli/test_package_cli_integration.py` — intentionally not in scope; no finding against them.)

**2. Placeholder scan:** no "TBD"/"implement later"/"similar to Task N". Every code step shows the full file or full method to add/delete. Deletion steps name the exact symbols and their replacement boundary.

**3. Type/name consistency:** method names and signatures used in test code were taken verbatim from the referenced model modules (`get_is_static`/`set_is_static`, `add_meta_class`/`get_of_meta_class`/`remove_meta_class`, `get_its_class`/`get_is_main_behavior`/`get_root_state`/`create_graphics`/`close_diagram`, `add_extension_point`/`get_extension_points`/`find_extension_point`/`delete_extension_point`/`get_entry_points`/`get_is_behavior_overriden`/`set_is_behavior_overriden`, `get_requirement_id`/`set_requirement_id`, `get_constraints_by_me`). Setup entry points (`add_attribute`, `add_stereotype`, `add_statechart`, `add_use_case`, `add_new_aggr`) all confirmed to exist on the parent classes (`RPClassifier`, `RPModelElement`, `RPPackage`). No `from __future__ import annotations`; no py3.9+ generic syntax; no `Any`.

**Caveat (called out, not a gap):** assertions on live COM return values (e.g. default `get_is_constant()` value, whether `get_of_meta_class()` is comma-separated) are reasoned from docstring semantics, not from a live run; the `--collect-only` gate cannot validate them. The first CI run on `windows-latest` is the real proof and may surface xfail-worthy Rhapsody quirks (as already seen with `set_is_final` / `set_is_abstract` in the existing suite). If a live run shows a method genuinely does not persist, mark that single test `@pytest.mark.xfail(strict=False, reason=...)` following the existing convention — do not change `src/`.
