# Structural Model Wrappers Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete the structural layer of the Rhapsody model wrapper to full Java API parity — fill gaps on 8 existing wrappers, add 17 new wrappers, refactor the flat `elements/` directory into packages, and backfill docstrings on every method.

**Architecture:** Bottom-up through the inheritance tree (`RPModelElement` → `RPUnit` → mid-layer → containment → leaves). Step 0 is a pure file move (refactor `classifiers.py`, `relations.py`, `containment.py` from flat modules into packages with `model_*.py` per-class files). All new code lands in its final location. Every method mirrors its Java API counterpart exactly, carries a docstring sourced from `docs/java_api/`, and is tested via fake COM objects.

**Tech Stack:** Python 3.8+, pywin32 (COM), pytest, ruff, black (line-length 200), mypy (strict). No `from __future__ import annotations`.

## Global Constraints

These apply to every task. Copy values verbatim; do not deviate.

- **Python target:** 3.8+ (string-quoted forward refs like `"RPCollection"`, no `from __future__ import annotations` per `docs/CODE_GUIDELINES.md`).
- **Black:** line-length 200, target-version `py38`.
- **Ruff:** line-length 200, rules `E, F, I, UP, B`.
- **Mypy:** strict mode, python_version 3.9, `warn_unused_ignores = true`. Overrides already ignore missing imports for `win32com.*` and `pywintypes`.
- **All COM calls** go through `call_com(lambda: ...)` from `rhapsody_cli.models._core`.
- **Method/property dispatch:** use `_get_method_or_property(self._com, "getX", "x")` for reads, `_set_method_or_property(self._com, "setX", "x", value)` for writes. Some wrappers (e.g. `classifiers.py`) call methods directly via `call_com(lambda: self._com.getX())` — match the surrounding file's existing style.
- **Returns:** single element → `wrap(call_com(lambda: ...))`; collection → `RPCollection(call_com(lambda: ...))`; primitive → cast with `str(...)`, `int(...)`, or `bool(...)`.
- **Wrapper params:** unwrap to `._com` inline, e.g. `call_com(lambda: self._com.addStereotype(stereotype._com))`.
- **Docstrings:** every public method gets a Google-style docstring. First line is the Java API description (sourced from `docs/java_api/com/telelogic/rhapsody/core/<Interface>.html`). Include `Args:`, `Returns:`, `Raises:` sections.
- **Deprecated methods:** if the Java API marks a method `@deprecated`, skip it and mark `deprecated - skipped` in the file's checklist comment.
- **Registration:** `register_wrapper("<MetaClassString>", RPXxx)` at the end of each `model_*.py` file. Use the metaclass string from the spec (e.g. `"Stereotype"`, `"Dependency"`).
- **Test naming:** `test_{class}_{method}_{behavior}` (e.g. `test_class_add_superclass_delegates_to_com`).
- **Test fakes:** use `make_fake_element(meta_class, **method_returns)`, `make_fake_collection(items)`, `make_com_error(message)` from `tests/unit/models/fakes.py`.
- **Branch:** all work goes on `docs/structural-model-wrappers-design` (already created for the spec commit). Implementation continues on this branch. After all tasks pass, open a PR.
- **Commits:** human-authored only. No `Co-authored-by` AI trailers. Commit message style: `feat:`, `refactor:`, `docs:`, `test:`, `style:` prefix matching recent history.

---

## File Structure

After all tasks complete, the `src/rhapsody_cli/models/elements/` directory looks like:

```
elements/
├── __init__.py                    (modified — imports new packages)
├── classifiers/                   (package — Task 1)
│   ├── __init__.py
│   ├── model_classifier.py        (RPClassifier — Task 4)
│   ├── model_class.py             (RPClass — Task 5)
│   ├── model_actor.py             (RPActor — Task 1)
│   ├── model_usecase.py           (RPUseCase — Task 1)
│   ├── model_operation.py         (RPOperation — Task 1)
│   ├── model_interface_item.py    (RPInterfaceItem — Task 1)
│   ├── model_statechart.py        (RPStatechart — Task 1)
│   ├── model_stereotype.py        (RPStereotype — Task 9)
│   └── model_association_class.py (RPAssociationClass — Task 9)
├── containment/                   (package — Task 1)
│   ├── __init__.py
│   ├── model_package.py           (RPPackage — Task 6)
│   ├── model_project.py           (RPProject — Task 6)
│   ├── model_profile.py           (RPProfile — Task 7)
│   ├── model_component.py         (RPComponent — Task 7)
│   ├── model_configuration.py     (RPConfiguration — Task 7)
│   ├── model_node.py              (RPNode — Task 7)
│   ├── model_module.py            (RPModule — Task 7)
│   ├── model_collaboration.py     (RPCollaboration — Task 7)
│   └── model_component_instance.py(RPComponentInstance — Task 7)
├── relations/                     (package — Task 1)
│   ├── __init__.py
│   ├── model_relation.py          (RPRelation — Task 5)
│   ├── model_instance.py          (RPInstance — Task 5)
│   ├── model_generalization.py    (RPGeneralization — Task 8)
│   ├── model_dependency.py        (RPDependency — Task 8)
│   ├── model_hyperlink.py         (RPHyperLink — Task 8)
│   └── model_association_role.py  (RPAssociationRole — Task 8)
├── diagrams.py                    (unchanged)
├── requirements.py                (unchanged)
├── misc.py                        (Task 8 — RPComment, RPConstraint, RPEnumerationLiteral)
└── variables.py                   (Task 9 — add RPTag)
```

Test files mirror this under `tests/unit/models/elements/` with `test_*.py` per class.

---

## Progress

| Task | Status | Commit | Summary |
|------|--------|--------|---------|
| 1 | DONE | `93ebd3c` | Split flat modules into packages, 467 tests pass |
| 2 | DONE | `b1129cd` | 110 new methods on RPModelElement, 143 tests |
| 3 | DONE | `a398907` | 24 new methods on RPUnit, 168 tests |
| 4 | DONE | `1620485` | 40 new methods on RPClassifier, 47 tests |
| 5 | DONE | `e637a4b` | 24 new RPClass methods, 8 new RPInstance methods, RPRelation audited |
| 6 | TODO | — | Complete RPPackage and RPProject |
| 7 | TODO | — | Add 7 containment wrappers |
| 8 | TODO | — | Add leaf wrappers Group A + misc |
| 9 | TODO | — | Add leaf wrappers Group B |
| 10 | TODO | — | Integration tests + final audit |

**Test count:** 467 passed, 2 skipped (as of Task 5).

---

## Task Index

- **Task 1:** ~~Refactor flat modules into packages (pure move, no new methods)~~ DONE
- **Task 2:** ~~Complete `RPModelElement` (base layer — `_core.py`)~~ DONE
- **Task 3:** ~~Complete `RPUnit` (base layer — `_core.py`)~~ DONE
- **Task 4:** ~~Complete `RPClassifier` (mid layer)~~ DONE
- **Task 5:** ~~Complete `RPClass`, audit `RPRelation`, complete `RPInstance` (mid layer)~~ DONE
- **Task 6:** Complete `RPPackage` and `RPProject` (containment layer)
- **Task 7:** Add containment wrappers (`RPProfile`, `RPComponent`, `RPConfiguration`, `RPModule`, `RPNode`, `RPCollaboration`, `RPComponentInstance`)
- **Task 8:** Add leaf wrappers Group A + B relations + misc (`RPGeneralization`, `RPDependency`, `RPHyperLink`, `RPAssociationRole`, `RPComment`, `RPConstraint`, `RPEnumerationLiteral`)
- **Task 9:** Add leaf wrappers Group B (`RPStereotype`, `RPAssociationClass`, `RPTag`)
- **Task 10:** Integration tests + final audit

---

### Task 1: Refactor Flat Modules Into Packages

**Goal:** Convert `classifiers.py`, `relations.py`, `containment.py` from flat modules into packages with `model_*.py` per-class files. No new methods. All existing imports must keep working.

**Files:**
- Delete: `src/rhapsody_cli/models/elements/classifiers.py`
- Delete: `src/rhapsody_cli/models/elements/relations.py`
- Delete: `src/rhapsody_cli/models/elements/containment.py`
- Create: `src/rhapsody_cli/models/elements/classifiers/__init__.py`
- Create: `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- Create: `src/rhapsody_cli/models/elements/classifiers/model_class.py`
- Create: `src/rhapsody_cli/models/elements/classifiers/model_actor.py`
- Create: `src/rhapsody_cli/models/elements/classifiers/model_usecase.py`
- Create: `src/rhapsody_cli/models/elements/classifiers/model_operation.py`
- Create: `src/rhapsody_cli/models/elements/classifiers/model_interface_item.py`
- Create: `src/rhapsody_cli/models/elements/classifiers/model_statechart.py`
- Create: `src/rhapsody_cli/models/elements/relations/__init__.py`
- Create: `src/rhapsody_cli/models/elements/relations/model_relation.py`
- Create: `src/rhapsody_cli/models/elements/relations/model_instance.py`
- Create: `src/rhapsody_cli/models/elements/containment/__init__.py`
- Create: `src/rhapsody_cli/models/elements/containment/model_package.py`
- Create: `src/rhapsody_cli/models/elements/containment/model_project.py`
- Modify: `src/rhapsody_cli/models/elements/__init__.py`
- Test: `tests/unit/models/elements/test_class.py` (verify existing tests still pass)

**Interfaces:**
- Consumes: the existing classes in `classifiers.py`, `relations.py`, `containment.py` (read them first to copy exactly).
- Produces: the same classes, importable from the same paths (e.g. `from rhapsody_cli.models.elements.classifiers import RPClass` still works).

**Approach:** For each flat module, the pattern is: (1) read the flat file, (2) create one `model_*.py` per class with that class's code and its imports, (3) create the package `__init__.py` that imports and re-exports every class, (4) delete the flat file, (5) run tests.

- [ ] **Step 1: Read the three flat files to know exactly what to move**

Run: read `src/rhapsody_cli/models/elements/classifiers.py`, `relations.py`, `containment.py` in full. Note the exact import block each uses (they all import from `rhapsody_cli.models._core`) and the exact `register_wrapper` calls at the bottom.

- [ ] **Step 2: Create the `classifiers/` package — one file per class**

Each `model_*.py` file contains: a module docstring, the import block (only what that class needs), the class definition (copied verbatim from `classifiers.py`), and the `register_wrapper` call if that class has one.

`src/rhapsody_cli/models/elements/classifiers/model_classifier.py` — contains `RPClassifier` (the base class, no registration). Import block:
```python
"""Wraps ``com.telelogic.rhapsody.core.IRPClassifier``."""

from typing import Any

from rhapsody_cli.models._core import (
    RPCollection,
    RPUnit,
    call_com,
    wrap,
)
```

`src/rhapsody_cli/models/elements/classifiers/model_class.py` — contains `RPClass` + `register_wrapper("Class", RPClass)`. Imports `RPClassifier` from `model_classifier`:
```python
"""Wraps ``com.telelogic.rhapsody.core.IRPClass``."""

from typing import Any

from rhapsody_cli.models._core import RPCollection, call_com, wrap
from rhapsody_cli.models.elements.classifiers.model_classifier import RPClassifier
```

`src/rhapsody_cli/models/elements/classifiers/model_actor.py` — contains `RPActor` + its registration. Imports `RPClassifier`.

`src/rhapsody_cli/models/elements/classifiers/model_usecase.py` — contains `RPUseCase` + its registration. Imports `RPClassifier`.

`src/rhapsody_cli/models/elements/classifiers/model_operation.py` — contains `RPOperation` + its registration. Imports `RPInterfaceItem`.

`src/rhapsody_cli/models/elements/classifiers/model_interface_item.py` — contains `RPInterfaceItem` (no registration). Imports `RPModelElement` from `_core`.

`src/rhapsody_cli/models/elements/classifiers/model_statechart.py` — contains `RPStatechart` + its registration. Imports `RPClassifier`.

**Important:** Copy the class bodies verbatim from the original `classifiers.py`. Do not modify methods, docstrings, or logic in this task. Pure move.

- [ ] **Step 3: Create `classifiers/__init__.py` re-exporting all classes**

`src/rhapsody_cli/models/elements/classifiers/__init__.py`:
```python
"""Classifiers package — wrappers for IRPClassifier and its subtypes."""

from rhapsody_cli.models.elements.classifiers.model_actor import RPActor  # noqa: F401
from rhapsody_cli.models.elements.classifiers.model_class import RPClass  # noqa: F401
from rhapsody_cli.models.elements.classifiers.model_classifier import RPClassifier  # noqa: F401
from rhapsody_cli.models.elements.classifiers.model_interface_item import (  # noqa: F401
    RPInterfaceItem,
)
from rhapsody_cli.models.elements.classifiers.model_operation import RPOperation  # noqa: F401
from rhapsody_cli.models.elements.classifiers.model_statechart import RPStatechart  # noqa: F401
from rhapsody_cli.models.elements.classifiers.model_usecase import RPUseCase  # noqa: F401

__all__ = [
    "RPActor",
    "RPClass",
    "RPClassifier",
    "RPInterfaceItem",
    "RPOperation",
    "RPStatechart",
    "RPUseCase",
]
```

The imports fire each submodule's `register_wrapper` calls as a side effect.

- [ ] **Step 4: Delete `classifiers.py`**

```bash
git rm src/rhapsody_cli/models/elements/classifiers.py
```

- [ ] **Step 5: Verify classifiers tests pass**

Run: `pytest tests/unit/models/elements/test_class.py tests/unit/models/elements/test_classifier.py tests/unit/models/elements/test_actor.py tests/unit/models/elements/test_usecase.py tests/unit/models/elements/test_operation.py tests/unit/models/elements/test_interface_item.py tests/unit/models/elements/test_statechart.py -v`
Expected: all PASS (no test changes needed — imports still resolve).

- [ ] **Step 6: Create the `relations/` package — `model_relation.py` and `model_instance.py`**

`src/rhapsody_cli/models/elements/relations/model_relation.py` — contains `RPRelation` (no registration). Copy verbatim from `relations.py`.

`src/rhapsody_cli/models/elements/relations/model_instance.py` — contains `RPInstance` + `register_wrapper("Instance", RPInstance)`. Imports `RPRelation` from `model_relation`.

- [ ] **Step 7: Create `relations/__init__.py`**

`src/rhapsody_cli/models/elements/relations/__init__.py`:
```python
"""Relations package — wrappers for IRPRelation and its subtypes."""

from rhapsody_cli.models.elements.relations.model_instance import RPInstance  # noqa: F401
from rhapsody_cli.models.elements.relations.model_relation import RPRelation  # noqa: F401

__all__ = ["RPInstance", "RPRelation"]
```

- [ ] **Step 8: Delete `relations.py`**

```bash
git rm src/rhapsody_cli/models/elements/relations.py
```

- [ ] **Step 9: Verify relations tests pass**

Run: `pytest tests/unit/models/elements/test_relation.py tests/unit/models/elements/test_instance.py -v`
Expected: all PASS.

- [ ] **Step 10: Create the `containment/` package — `model_package.py` and `model_project.py`**

`src/rhapsody_cli/models/elements/containment/model_package.py` — contains `RPPackage` + `register_wrapper("Package", RPPackage)`. Copy verbatim from `containment.py`.

`src/rhapsody_cli/models/elements/containment/model_project.py` — contains `RPProject` + `register_wrapper("Project", RPProject)`. Copy verbatim from `containment.py`.

- [ ] **Step 11: Create `containment/__init__.py`**

`src/rhapsody_cli/models/elements/containment/__init__.py`:
```python
"""Containment package — wrappers for IRPPackage and IRPProject."""

from rhapsody_cli.models.elements.containment.model_package import RPPackage  # noqa: F401
from rhapsody_cli.models.elements.containment.model_project import RPProject  # noqa: F401

__all__ = ["RPPackage", "RPProject"]
```

- [ ] **Step 12: Delete `containment.py`**

```bash
git rm src/rhapsody_cli/models/elements/containment.py
```

- [ ] **Step 13: Verify containment tests pass**

Run: `pytest tests/unit/models/elements/test_package.py tests/unit/models/elements/test_project.py -v`
Expected: all PASS.

- [ ] **Step 14: Run the full test suite + linters**

Run:
```bash
pytest tests/ -v
ruff check src/ tests/
black --check src/ tests/
mypy src/ tests/
```
Expected: all PASS, no lint errors, no type errors.

- [ ] **Step 15: Commit**

```bash
git add src/rhapsody_cli/models/elements/
git commit -m "refactor: split classifiers/relations/containment into packages"
```

---

### Task 2: Complete `RPModelElement` (Base Layer)

**Goal:** Add every non-deprecated method from `IRPModelElement` to `RPModelElement` in `_core.py`, each with a docstring sourced from `docs/java_api/com/telelogic/rhapsody/core/IRPModelElement.html`, and one test per method.

**Files:**
- Modify: `src/rhapsody_cli/models/_core.py` (the `RPModelElement` class, lines 85-119)
- Test: `tests/unit/models/test_core.py`
- Test helper: `tests/unit/models/fakes.py` (add helpers as needed)

**Interfaces:**
- Consumes: `call_com`, `wrap`, `RPCollection` (all in `_core.py` already).
- Produces: a complete `RPModelElement` that all other wrappers inherit from. Later tasks rely on methods like `getOwner()`, `getStereotypes()`, `addDependencyTo()` being available on every wrapper.

**Approach:** `IRPModelElement.html` is large. Read it in chunks (use the Read tool with `offset`/`limit` or use an Explore subagent) to extract the full method list. For each method, follow TDD: write the test first, watch it fail, implement, watch it pass.

The spec groups methods into 10 categories (navigation, identification, stereotypes, tags, dependencies, properties, lifecycle, diagrams, OSLC, other). Work through them in order. Below is the pattern for one method per category; repeat for every method discovered in the HTML.

- [ ] **Step 1: Enumerate the full method list from the Java docs**

Read `docs/java_api/com/telelogic/rhapsody/core/IRPModelElement.html`. Extract every method signature and its description text. Cross-reference with `docs/java_api/deprecated-list.html` to identify deprecated methods (skip those). Write the full list into a checklist comment at the top of `RPModelElement` in `_core.py`:

```python
# IRPModelElement method parity checklist:
# [ ] getName              [x] impl  [ ] docstring  [ ] test   (already implemented)
# [ ] setName              [x] impl  [ ] docstring  [ ] test   (already implemented)
# [ ] getMetaClass         [x] impl  [ ] docstring  [ ] test   (already implemented)
# [ ] getGUID              [x] impl  [ ] docstring  [ ] test   (already implemented)
# [ ] getOwner             [ ] impl  [ ] docstring  [ ] test
# [ ] getDescription       [ ] impl  [ ] docstring  [ ] test
# [ ] getStereotypes       [ ] impl  [ ] docstring  [ ] test
# [ ] addStereotype        [ ] impl  [ ] docstring  [ ] test
# [ ] getDependencies      [ ] impl  [ ] docstring  [ ] test
# [ ] addDependencyTo      [ ] impl  [ ] docstring  [ ] test
# [ ] getProperty          [ ] impl  [ ] docstring  [ ] test
# [ ] ... (every method from the HTML, except deprecated)
# [deprecated] someOldMethod  - skipped
```

Also backfill docstrings on the 4 existing methods (`getName`, `setName`, `getMetaClass`, `getGUID`) — check the `[ ] docstring` box to `[x]`.

- [ ] **Step 2: Write failing tests for a navigation method — `getOwner`**

In `tests/unit/models/test_core.py`, add:

```python
def test_model_element_get_owner_wraps_result() -> None:
    owner_fake = make_fake_element("Package", getName="RootPkg")
    fake = make_fake_element("Class", getOwner=owner_fake)
    element = RPModelElement(fake)

    result = element.getOwner()

    fake.getOwner.assert_called_once_with()
    assert isinstance(result, RPPackage)
    assert result.getName() == "RootPkg"
```

Imports needed at the top of `test_core.py` (add if not present):
```python
from rhapsody_cli.models._core import RPModelElement
from rhapsody_cli.models.elements.containment import RPPackage
from tests.unit.models.fakes import make_fake_element
```

- [ ] **Step 3: Run the test to verify it fails**

Run: `pytest tests/unit/models/test_core.py::test_model_element_get_owner_wraps_result -v`
Expected: FAIL with `AttributeError: 'RPModelElement' object has no attribute 'getOwner'`.

- [ ] **Step 4: Implement `getOwner` with a docstring**

In `src/rhapsody_cli/models/_core.py`, inside `RPModelElement`:

```python
def getOwner(self) -> "RPModelElement":
    """Returns the owner of the model element.

    Returns:
        The ``IRPModelElement`` that owns this element, wrapped in its
        matching Python wrapper class.
    """
    return wrap(call_com(lambda: self._com.getOwner()))
```

- [ ] **Step 5: Run the test to verify it passes**

Run: `pytest tests/unit/models/test_core.py::test_model_element_get_owner_wraps_result -v`
Expected: PASS.

- [ ] **Step 6: Update the checklist comment**

Change the `getOwner` row to:
```python
# [x] getOwner             [x] impl  [x] docstring  [x] test
```

- [ ] **Step 7: Repeat Steps 2-6 for every method in the checklist**

Work through every method discovered in Step 1. For each:
1. Write a failing test (naming: `test_model_element_{method}_{behavior}`).
2. Run it to verify it fails.
3. Implement with a docstring sourced from the Java API HTML.
4. Run it to verify it passes.
5. Check off the checklist row.

**Method-specific notes:**
- `getStereotypes()` returns `RPCollection` of `RPStereotype`. Test with `make_fake_collection([make_fake_element("Stereotype", getName="MyStereo")])`.
- `addStereotype(name: str)` — Java takes a string name, returns the stereotype. Test: `fake.addStereotype.return_value = make_fake_element("Stereotype")`.
- `addDependencyTo(element)` takes a wrapper, unwraps to `._com`. Test asserts `fake.addDependencyTo.assert_called_once_with(target._com)`.
- `getProperty(name)` / `getPropertyValue(name)` / `setPropertyValue(name, value)` — primitives, straightforward.
- `getNestedElements()` — already on `RPUnit`, but `IRPModelElement` may also declare it. If so, it's inherited; just backfill the docstring if missing.
- OSLC methods (`getOSLCLinks`, `createOSLCLink`, `deleteOSLCLink`): model `OSLCLink` as a dataclass in `_core.py`. If the COM API doesn't expose them cleanly, implement the method body as `raise NotImplementedError("Rhapsody2.Application.1 does not expose getOSLCLinks; method is defined for Java API parity only.")`.

- [ ] **Step 8: Backfill docstrings on the 4 existing methods**

`getName`, `setName`, `getMetaClass`, `getGUID` — add Google-style docstrings sourced from `IRPModelElement.html`. Example:

```python
def getName(self) -> str:
    """Returns the name of the model element.

    Returns:
        The element's name as a string.
    """
    return str(_get_method_or_property(self._com, "getName", "name"))
```

- [ ] **Step 9: Run full suite + linters**

Run:
```bash
pytest tests/unit/models/test_core.py -v
ruff check src/ tests/
black --check src/ tests/
mypy src/ tests/
```
Expected: all PASS.

- [ ] **Step 10: Commit**

```bash
git add src/rhapsody_cli/models/_core.py tests/unit/models/test_core.py tests/unit/models/fakes.py
git commit -m "feat: complete RPModelElement to full IRPModelElement parity"
```

---

### Task 3: Complete `RPUnit` (Base Layer)

**Goal:** Add every non-deprecated method from `IRPUnit` to `RPUnit` in `_core.py`, with docstrings and tests.

**Files:**
- Modify: `src/rhapsody_cli/models/_core.py` (the `RPUnit` class, lines 121-146)
- Test: `tests/unit/models/test_core.py`

**Interfaces:**
- Consumes: `call_com`, `wrap`, `RPCollection`.
- Produces: a complete `RPUnit` inherited by `RPPackage`, `RPProject`, `RPClassifier`, `RPRelation`, `RPComponent`.

**Approach:** Same TDD pattern as Task 2. Read `docs/java_api/com/telelogic/rhapsody/core/IRPUnit.html` for the full method list.

- [ ] **Step 1: Enumerate methods from `IRPUnit.html` and write the checklist**

Add the checklist comment above `RPUnit`:
```python
# IRPUnit method parity checklist:
# [ ] save                [x] impl  [ ] docstring  [ ] test   (already implemented)
# [ ] getFilename         [x] impl  [ ] docstring  [ ] test   (already implemented)
# [ ] setFilename         [x] impl  [ ] docstring  [ ] test   (already implemented)
# [ ] isReadOnly          [x] impl  [ ] docstring  [ ] test   (already implemented)
# [ ] setReadOnly         [x] impl  [ ] docstring  [ ] test   (already implemented)
# [ ] getNestedElements   [x] impl  [ ] docstring  [ ] test   (already implemented)
# [ ] load                [ ] impl  [ ] docstring  [ ] test
# [ ] unload              [ ] impl  [ ] docstring  [ ] test
# [ ] reload              [ ] impl  [ ] docstring  [ ] test
# [ ] reloadIfStatusChanged [ ] impl [ ] docstring [ ] test
# [ ] getStatus           [ ] impl  [ ] docstring  [ ] test
# [ ] isLoaded            [ ] impl  [ ] docstring  [ ] test
# [ ] isSeparateSaveUnit  [ ] impl  [ ] docstring  [ ] test
# [ ] setSeparateSaveUnit [ ] impl  [ ] docstring  [ ] test
# [ ] getLanguage         [ ] impl  [ ] docstring  [ ] test
# [ ] setLanguage         [ ] impl  [ ] docstring  [ ] test
# [ ] saveAs              [ ] impl  [ ] docstring  [ ] test
# [ ] copyToAnotherProject [ ] impl [ ] docstring  [ ] test
# [ ] getNestedSaveUnits  [ ] impl  [ ] docstring  [ ] test
# [ ] getNestedSaveUnitsCount [ ] impl [ ] docstring [ ] test
# [ ] getStructureDiagrams [ ] impl [ ] docstring  [ ] test
# [ ] getAddToModelMode   [ ] impl  [ ] docstring  [ ] test
# [ ] setAddToModelMode   [ ] impl  [ ] docstring  [ ] test
# [deprecated] <any deprecated> - skipped
```

- [ ] **Step 2: Write failing test for `load`**

```python
def test_unit_load_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    unit = RPUnit(fake)

    unit.load(1)

    fake.load.assert_called_once_with(1)
```

- [ ] **Step 3: Run to verify it fails**

Run: `pytest tests/unit/models/test_core.py::test_unit_load_delegates_to_com -v`
Expected: FAIL — `AttributeError: 'RPUnit' object has no attribute 'load'`.

- [ ] **Step 4: Implement `load`**

```python
def load(self, with_subs: int) -> None:
    """Loads the unit.

    Args:
        with_subs: ``1`` to load nested sub-units, ``0`` to load only this unit.
    """
    call_com(lambda: self._com.load(with_subs))
```

- [ ] **Step 5: Run to verify it passes, check off checklist**

Run: `pytest tests/unit/models/test_core.py::test_unit_load_delegates_to_com -v`
Expected: PASS.

- [ ] **Step 6: Repeat for every method in the checklist**

For `AddToModelMode`, if the Java API defines named constant values, add a module-level `IntEnum` in `_core.py`:

```python
from enum import IntEnum

class AddToModelMode(IntEnum):
    """Mirror of IRPApplication.AddToModel_Mode constants."""
    # Values confirmed from IRPApplication.AddToModel_Mode.html
    REPLACE_EXISTING = 0
    KEEP_EXISTING = 1
```

(Read `docs/java_api/com/telelogic/rhapsody/core/IRPApplication.AddToModel_Mode.html` for the actual values.)

- [ ] **Step 7: Backfill docstrings on the 6 existing methods**

`save`, `getFilename`, `setFilename`, `isReadOnly`, `setReadOnly`, `getNestedElements` — add docstrings sourced from `IRPUnit.html`.

- [ ] **Step 8: Run full suite + linters, commit**

```bash
pytest tests/unit/models/test_core.py -v
ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/
git add src/rhapsody_cli/models/_core.py tests/unit/models/test_core.py
git commit -m "feat: complete RPUnit to full IRPUnit parity"
```

---

### Task 4: Complete `RPClassifier` (Mid Layer)

**Goal:** Add every non-deprecated method from `IRPClassifier` to `RPClassifier` in `classifiers/model_classifier.py`, with docstrings and tests.

**Files:**
- Modify: `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- Test: `tests/unit/models/elements/test_classifier.py`

**Interfaces:**
- Consumes: `RPUnit` (parent), `call_com`, `wrap`, `RPCollection`.
- Produces: a complete `RPClassifier` inherited by `RPClass`, `RPActor`, `RPUseCase`, `RPStereotype`.

- [ ] **Step 1: Enumerate methods from `IRPClassifier.html`, write the checklist**

Read `docs/java_api/com/telelogic/rhapsody/core/IRPClassifier.html`. Write the checklist comment at the top of `model_classifier.py`. Mark the 6 existing methods (`addAttribute`, `addOperation`, `getAttributes`, `getOperations`, `addGeneralization`, `addStatechart`) as `[x] impl` but `[ ] docstring` / `[ ] test` (backfill those).

- [ ] **Step 2-6: TDD cycle for each new method**

Follow the same pattern as Task 2 Steps 2-6. Test file: `tests/unit/models/elements/test_classifier.py`. Test naming: `test_classifier_{method}_{behavior}`.

**Key methods to implement** (from the spec):
- Factory methods: `addClass`, `addInterface`, `addActor`, `addUseCase`, `addSignal`, `addException`, `addEnumeration`, `addAssociation`, `addAssociationClass`, `addDependency`, `addNestedPackage`
- Traversal: `getNestedClassifiers`, `getGeneralizations`, `getNestedAssociations`
- State/behavior: `getStatecharts`, `addActivityDiagram`, `getActivityDiagrams`
- Flags: `getIsAbstract`, `setIsAbstract`, `getIsLeaf`, `setIsLeaf`

Each factory method returns a wrapped element (`wrap(call_com(lambda: ...))`). Each traversal method returns `RPCollection`. Each flag method returns `bool` / `int`.

If a method doesn't exist on the COM Prog ID, implement the body as:
```python
raise NotImplementedError(
    "Rhapsody2.Application.1 does not expose addInterface on Classifier; "
    "method is defined for Java API parity only."
)
```
And test it with `pytest.raises(NotImplementedError)`.

- [ ] **Step 7: Backfill docstrings + tests on the 6 existing methods**

- [ ] **Step 8: Run suite + linters, commit**

```bash
pytest tests/unit/models/elements/test_classifier.py -v
ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/
git add src/rhapsody_cli/models/elements/classifiers/model_classifier.py tests/unit/models/elements/test_classifier.py
git commit -m "feat: complete RPClassifier to full IRPClassifier parity"
```

---

### Task 5: Complete `RPClass`, Audit `RPRelation`, Complete `RPInstance` (Mid Layer)

**Goal:** Three mid-layer wrappers in one task (they're interdependent and similarly sized).

**Files:**
- Modify: `src/rhapsody_cli/models/elements/classifiers/model_class.py`
- Modify: `src/rhapsody_cli/models/elements/relations/model_relation.py`
- Modify: `src/rhapsody_cli/models/elements/relations/model_instance.py`
- Test: `tests/unit/models/elements/test_class.py`
- Test: `tests/unit/models/elements/test_relation.py`
- Test: `tests/unit/models/elements/test_instance.py`

**Interfaces:**
- Consumes: `RPClassifier`, `RPRelation` (parents).
- Produces: complete `RPClass` (inherited by `RPAssociationClass`), complete `RPInstance` (inherited by `RPModule`, `RPComponentInstance`, `RPAssociationRole`).

- [ ] **Step 1: Enumerate methods for all three interfaces**

Read `IRPClass.html`, `IRPRelation.html`, `IRPInstance.html`. Write checklist comments at the top of each file.

- [ ] **Step 2: Audit `RPRelation` — verify every method exists**

`RPRelation` is already near-complete (~30 methods). For each method in the checklist, verify it's implemented. If any are missing, add them via TDD. If all are present, just backfill docstrings on those that lack them and check off the checklist.

- [ ] **Step 3: Complete `RPClass` via TDD**

Test file: `test_class.py`. Key methods to add (from spec):
- Inheritance: `getSuperclasses`, `getSubclasses`, `removeSuperclass`
- Structural: `getNestedClasses`, `getAssociations`, `getPorts`, `getInterfaces`
- Constructors: `getConstructors`, `getDestructors`
- Flags: `setIsAbstract`, `getIsLeaf`, `setIsLeaf`, `getIsActive`, `setIsActive`, `getIsRoot`, `setIsRoot`
- Template: `getTemplateParameters`, `addTemplateParameter`, `isTemplate`, `instantiateTemplate`

- [ ] **Step 4: Complete `RPInstance` via TDD**

Test file: `test_instance.py`. Key methods to add (from spec):
- `getInstantiatedBy`, `setInstantiatedBy`, `getListOfInitializerArguments`, `setInitializerArgumentValue`, `setExplicit`, `setImplicit`
- `addRelationToTheWhole`
- `updateContainedDiagramsOnServer` (may be `NotImplementedError`)

- [ ] **Step 5: Backfill docstrings on all existing methods across all three files**

- [ ] **Step 6: Run suite + linters, commit**

```bash
pytest tests/unit/models/elements/test_class.py tests/unit/models/elements/test_relation.py tests/unit/models/elements/test_instance.py -v
ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/
git add src/rhapsody_cli/models/elements/classifiers/model_class.py src/rhapsody_cli/models/elements/relations/ tests/unit/models/elements/test_class.py tests/unit/models/elements/test_relation.py tests/unit/models/elements/test_instance.py
git commit -m "feat: complete RPClass/RPRelation/RPInstance to full parity"
```

---

### Task 6: Complete `RPPackage` and `RPProject` (Containment Layer)

**Goal:** Fill the gaps on the two top-level containers.

**Files:**
- Modify: `src/rhapsody_cli/models/elements/containment/model_package.py`
- Modify: `src/rhapsody_cli/models/elements/containment/model_project.py`
- Test: `tests/unit/models/elements/test_package.py`
- Test: `tests/unit/models/elements/test_project.py`

**Interfaces:**
- Consumes: `RPUnit` (parent), `wrap`, `RPCollection`.
- Produces: complete `RPPackage` (inherited by `RPProfile`), complete `RPProject`.

- [ ] **Step 1: Enumerate methods from `IRPPackage.html` and `IRPProject.html`, write checklists**

- [ ] **Step 2: Complete `RPPackage` via TDD**

Key methods to add (from spec):
- Factory: `addUseCase`, `addInterface`, `addSignal`, `addException`, `addEnumeration`, `addAssociation`, `addAssociationClass`, `addDependency`, `addPackage`, `addRequirement`, `addComment`, `addConstraint`, `addDiagram` variants
- Traversal: `getNestedPackages`, `getClasses`, `getActors`, `getUseCases`, `getInterfaces`, `getEnumerations`, `getSignals`, `getExceptions`, `getAssociations`, `getDependencies`, `getComponents`, `getSubSystems`, `getDiagrams`, `getRequirements`, `getComments`, `getConstraints`
- Import/export: `importFromFile`, `exportToFile` (if on `IRPPackage`)

- [ ] **Step 3: Complete `RPProject` via TDD**

Key methods to add (from spec):
- Factory: `addClass`, `addActor`, `addUseCase`, `addInterface`, `addEnumeration`, `addAssociation`, `addDependency`, `addProfile`, `addConfiguration`, `addDiagram` variants
- Traversal: `getAllElements`, `getUnits`, `getComponents`, `getConfigurations`, `getActiveConfiguration`, `getProfiles`, `getDiagrams`
- Profile: `addProfile`, `removeProfile`, `getProfiles`, `applyProfile`
- Config: `getConfigurations`, `getActiveConfiguration`, `setActiveConfiguration`, `addConfiguration`, `removeConfiguration`
- File: `saveAs`, `importSubProject`, `exportSubProject`, `importPackage`
- Search: `findByName`, `findByMetaClass`, `findElementByGUID`
- Lifecycle: `isDirty`, `setDirty`

- [ ] **Step 4: Backfill docstrings on existing methods**

- [ ] **Step 5: Run suite + linters, commit**

```bash
pytest tests/unit/models/elements/test_package.py tests/unit/models/elements/test_project.py -v
ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/
git add src/rhapsody_cli/models/elements/containment/model_package.py src/rhapsody_cli/models/elements/containment/model_project.py tests/unit/models/elements/test_package.py tests/unit/models/elements/test_project.py
git commit -m "feat: complete RPPackage and RPProject to full parity"
```

---

### Task 7: Add Containment Wrappers

**Goal:** Add 7 new wrappers: `RPProfile`, `RPComponent`, `RPConfiguration`, `RPModule`, `RPNode`, `RPCollaboration`, `RPComponentInstance`.

**Files:**
- Create: `src/rhapsody_cli/models/elements/containment/model_profile.py`
- Create: `src/rhapsody_cli/models/elements/containment/model_component.py`
- Create: `src/rhapsody_cli/models/elements/containment/model_configuration.py`
- Create: `src/rhapsody_cli/models/elements/containment/model_node.py`
- Create: `src/rhapsody_cli/models/elements/containment/model_module.py`
- Create: `src/rhapsody_cli/models/elements/containment/model_collaboration.py`
- Create: `src/rhapsody_cli/models/elements/containment/model_component_instance.py`
- Modify: `src/rhapsody_cli/models/elements/containment/__init__.py`
- Test: `tests/unit/models/elements/test_profile.py`, `test_component.py`, `test_configuration.py`, `test_module.py`, `test_node.py`, `test_collaboration.py`, `test_component_instance.py`

**Interfaces:**
- Consumes: `RPPackage`, `RPUnit`, `RPInstance` (parents from Tasks 5-6).
- Produces: 7 registered wrappers that `wrap()` dispatches to.

- [ ] **Step 1: Confirm parent interfaces for the 3 TBD wrappers**

Read the top of these Java docs to confirm `extends`:
- `docs/java_api/com/telelogic/rhapsody/core/IRPConfiguration.html`
- `docs/java_api/com/telelogic/rhapsody/core/IRPNode.html`
- `docs/java_api/com/telelogic/rhapsody/core/IRPCollaboration.html`

If the parent is `IRPModelElement` or `IRPUnit`, place the file in `containment/` as planned. If the parent is something unexpected (e.g. `IRPNode extends IRPInstance`), move the file to `relations/` and update the package `__init__.py` there instead.

- [ ] **Step 2: TDD for `RPProfile` (extends `RPPackage`)**

Write `test_profile.py` first:

```python
from rhapsody_cli.models._core import wrap
from rhapsody_cli.models.elements.containment import RPPackage, RPProfile
from tests.unit.models.fakes import make_fake_element


def test_profile_is_a_package() -> None:
    fake = make_fake_element("Profile", getName="SysML")
    profile = RPProfile(fake)

    assert isinstance(profile, RPPackage)
    assert profile.getName() == "SysML"


def test_profile_is_registered_for_meta_class_profile() -> None:
    fake = make_fake_element("Profile", getName="SysML")

    wrapped = wrap(fake)

    assert isinstance(wrapped, RPProfile)
```

Run to verify it fails (`ImportError` — `RPProfile` doesn't exist yet).

- [ ] **Step 3: Implement `RPProfile`**

`src/rhapsody_cli/models/elements/containment/model_profile.py`:
```python
"""Wraps ``com.telelogic.rhapsody.core.IRPProfile``."""

from typing import Any

from rhapsody_cli.models._core import RPCollection, call_com, wrap
from rhapsody_cli.models.elements.containment.model_package import RPPackage


class RPProfile(RPPackage):
    """Wraps ``IRPProfile``: a profile (extends ``IRPPackage``)."""

    # Methods enumerated from IRPProfile.html — add via TDD one at a time
    pass


register_wrapper("Profile", RPProfile)
```

(Add `from rhapsody_cli.models._core import register_wrapper` to the import block.)

Read `IRPProfile.html` for the full method list, then add each method via TDD following the pattern from Task 2.

- [ ] **Step 4: Register in `containment/__init__.py`**

Add to the imports:
```python
from rhapsody_cli.models.elements.containment.model_profile import RPProfile  # noqa: F401
```
Add `"RPProfile"` to `__all__`.

- [ ] **Step 5: Run test, commit `RPProfile`**

```bash
pytest tests/unit/models/elements/test_profile.py -v
git add src/rhapsody_cli/models/elements/containment/model_profile.py src/rhapsody_cli/models/elements/containment/__init__.py tests/unit/models/elements/test_profile.py
git commit -m "feat: add RPProfile wrapper"
```

- [ ] **Step 6: Repeat Steps 2-5 for `RPComponent` (extends `RPUnit`)**

File: `model_component.py`. Registration: `register_wrapper("Component", RPComponent)`. Read `IRPComponent.html` for methods.

- [ ] **Step 7: Repeat for `RPConfiguration`**

File: `model_configuration.py`. Registration: `register_wrapper("Configuration", RPConfiguration)`. Parent confirmed in Step 1. Read `IRPConfiguration.html`.

- [ ] **Step 8: Repeat for `RPModule` (extends `RPInstance`)**

File: `model_module.py`. Registration: `register_wrapper("Module", RPModule)`. Import `RPInstance` from `relations.model_instance`. Read `IRPModule.html`.

- [ ] **Step 9: Repeat for `RPNode`**

File: `model_node.py` (or `relations/model_node.py` if parent is `RPInstance`). Registration: `register_wrapper("Node", RPNode)`. Read `IRPNode.html`.

- [ ] **Step 10: Repeat for `RPCollaboration`**

File: `model_collaboration.py`. Registration: `register_wrapper("Collaboration", RPCollaboration)`. Read `IRPCollaboration.html`.

- [ ] **Step 11: Repeat for `RPComponentInstance` (extends `RPInstance`)**

File: `model_component_instance.py`. Registration: `register_wrapper("ComponentInstance", RPComponentInstance)`. Read `IRPComponentInstance.html`.

- [ ] **Step 12: Run full suite + linters, final commit for the task**

```bash
pytest tests/unit/models/elements/ -v
ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/
git add src/rhapsody_cli/models/elements/containment/ tests/unit/models/elements/
git commit -m "feat: add containment wrappers (Profile, Component, Configuration, Module, Node, Collaboration, ComponentInstance)"
```

---

### Task 8: Add Leaf Wrappers (Relations Group A + Misc)

**Goal:** Add 7 leaf wrappers: `RPGeneralization`, `RPDependency`, `RPHyperLink`, `RPAssociationRole`, `RPComment`, `RPConstraint`, `RPEnumerationLiteral`.

**Files:**
- Create: `src/rhapsody_cli/models/elements/relations/model_generalization.py`
- Create: `src/rhapsody_cli/models/elements/relations/model_dependency.py`
- Create: `src/rhapsody_cli/models/elements/relations/model_hyperlink.py`
- Create: `src/rhapsody_cli/models/elements/relations/model_association_role.py`
- Create: `src/rhapsody_cli/models/elements/misc.py`
- Modify: `src/rhapsody_cli/models/elements/relations/__init__.py`
- Test: `tests/unit/models/elements/test_generalization.py`, `test_dependency.py`, `test_hyperlink.py`, `test_association_role.py`, `test_misc.py`

**Interfaces:**
- Consumes: `RPModelElement` (from `_core`), `RPDependency` (parent of `RPHyperLink`), `RPInstance` (parent of `RPAssociationRole`).
- Produces: 7 registered wrappers. `RPModelElement.getDependencies()` (Task 2) returns these.

- [ ] **Step 1: TDD `RPGeneralization` (extends `RPModelElement`)**

`test_generalization.py`:
```python
from rhapsody_cli.models._core import RPModelElement, wrap
from rhapsody_cli.models.elements.classifiers import RPClassifier
from rhapsody_cli.models.elements.relations import RPGeneralization
from tests.unit.models.fakes import make_fake_element


def test_generalization_is_a_model_element() -> None:
    fake = make_fake_element("Generalization")
    gen = RPGeneralization(fake)

    assert isinstance(gen, RPModelElement)


def test_generalization_is_registered() -> None:
    fake = make_fake_element("Generalization")

    wrapped = wrap(fake)

    assert isinstance(wrapped, RPGeneralization)


def test_generalization_get_base_class_wraps_result() -> None:
    base_fake = make_fake_element("Class", getName="Base")
    fake = make_fake_element("Generalization", getBaseClass=base_fake)
    gen = RPGeneralization(fake)

    result = gen.getBaseClass()

    fake.getBaseClass.assert_called_once_with()
    assert isinstance(result, RPClassifier)
    assert result.getName() == "Base"


def test_generalization_set_base_class_unwraps_param() -> None:
    fake = make_fake_element("Generalization")
    base_fake = make_fake_element("Class", getName="Base")
    gen = RPGeneralization(fake)

    gen.setBaseClass(RPClassifier(base_fake))

    fake.setBaseClass.assert_called_once_with(base_fake)
```

Run to verify it fails.

- [ ] **Step 2: Implement `RPGeneralization`**

`src/rhapsody_cli/models/elements/relations/model_generalization.py`:
```python
"""Wraps ``com.telelogic.rhapsody.core.IRPGeneralization``."""

from typing import Any

from rhapsody_cli.models._core import RPModelElement, call_com, wrap
from rhapsody_cli.models._core import register_wrapper


class RPGeneralization(RPModelElement):
    """Wraps ``IRPGeneralization``: a generalization (inheritance) relationship."""

    def getBaseClass(self) -> Any:
        """Returns the base class of this generalization.

        Returns:
            The ``IRPClassifier`` that is the parent class, wrapped.
        """
        return wrap(call_com(lambda: self._com.getBaseClass()))

    def setBaseClass(self, base_class: Any) -> None:
        """Sets the base class of this generalization.

        Args:
            base_class: The ``IRPClassifier`` to set as the parent class.
        """
        call_com(lambda: self._com.setBaseClass(base_class._com))

    def getDerivedClass(self) -> Any:
        """Returns the derived class of this generalization.

        Returns:
            The ``IRPClassifier`` that is the child class, wrapped.
        """
        return wrap(call_com(lambda: self._com.getDerivedClass()))

    def setDerivedClass(self, derived_class: Any) -> None:
        """Sets the derived class of this generalization.

        Args:
            derived_class: The ``IRPClassifier`` to set as the child class.
        """
        call_com(lambda: self._com.setDerivedClass(derived_class._com))

    def getExtensionPoint(self) -> str:
        """Returns the extension point of this generalization.

        Returns:
            The extension point string.
        """
        return str(call_com(lambda: self._com.getExtensionPoint()))

    def setExtensionPoint(self, name: str) -> None:
        """Sets the extension point of this generalization.

        Args:
            name: The extension point string.
        """
        call_com(lambda: self._com.setExtensionPoint(name))

    def getIsVirtual(self) -> int:
        """Checks whether this generalization is virtual.

        Returns:
            ``1`` if virtual, ``0`` otherwise.
        """
        return int(call_com(lambda: self._com.getIsVirtual()))

    def setIsVirtual(self, is_virtual: int) -> None:
        """Sets whether this generalization is virtual.

        Args:
            is_virtual: ``1`` for virtual, ``0`` otherwise.
        """
        call_com(lambda: self._com.setIsVirtual(is_virtual))

    def getVisibility(self) -> str:
        """Returns the visibility of this generalization.

        Returns:
            The visibility string (e.g. ``"public"``, ``"private"``).
        """
        return str(call_com(lambda: self._com.getVisibility()))

    def setVisibility(self, visibility: str) -> None:
        """Sets the visibility of this generalization.

        Args:
            visibility: The visibility string.
        """
        call_com(lambda: self._com.setVisibility(visibility))


register_wrapper("Generalization", RPGeneralization)
```

- [ ] **Step 3: Register in `relations/__init__.py`**

Add:
```python
from rhapsody_cli.models.elements.relations.model_generalization import RPGeneralization  # noqa: F401
```
Add `"RPGeneralization"` to `__all__`.

- [ ] **Step 4: Run test, verify pass**

- [ ] **Step 5: TDD + implement `RPDependency` (extends `RPModelElement`)**

`model_dependency.py`. Methods (from spec): `getDependent`, `setDependent`, `getDependsOn`, `setDependsOn`, `isNeedToMigrate`, `setLinkType`, `setOwnerWithoutChangingDependent`. Registration: `register_wrapper("Dependency", RPDependency)`.

- [ ] **Step 6: TDD + implement `RPHyperLink` (extends `RPDependency`)**

`model_hyperlink.py`. Read `IRPHyperLink.html` for the method list. Import `RPDependency` from `model_dependency`. Registration: `register_wrapper("HyperLink", RPHyperLink)`.

- [ ] **Step 7: TDD + implement `RPAssociationRole` (extends `RPInstance`)**

`model_association_role.py`. Read `IRPAssociationRole.html`. Import `RPInstance` from `relations.model_instance`. Registration: `register_wrapper("AssociationRole", RPAssociationRole)`.

- [ ] **Step 8: Create `misc.py` with `RPComment`, `RPConstraint`, `RPEnumerationLiteral`**

`src/rhapsody_cli/models/elements/misc.py`:
```python
"""Miscellaneous model element wrappers — IRPComment, IRPConstraint, IRPEnumerationLiteral."""

from rhapsody_cli.models._core import RPModelElement, call_com, register_wrapper


class RPEnumerationLiteral(RPModelElement):
    """Wraps ``IRPEnumerationLiteral``: a literal value in an enumeration."""

    def getValue(self) -> str:
        """Returns the value of this enumeration literal.

        Returns:
            The literal's value string.
        """
        return str(call_com(lambda: self._com.getValue()))

    def setValue(self, value: str) -> None:
        """Sets the value of this enumeration literal.

        Args:
            value: The value string.
        """
        call_com(lambda: self._com.setValue(value))


register_wrapper("EnumerationLiteral", RPEnumerationLiteral)


class RPComment(RPModelElement):
    """Wraps ``IRPComment``: a free-text comment element."""

    # Methods enumerated from IRPComment.html — add via TDD
    pass


register_wrapper("Comment", RPComment)


class RPConstraint(RPModelElement):
    """Wraps ``IRPConstraint``: a constraint element."""

    # Methods enumerated from IRPConstraint.html — add via TDD
    pass


register_wrapper("Constraint", RPConstraint)
```

Read `IRPComment.html` and `IRPConstraint.html` for their method lists, add methods via TDD. Write `test_misc.py` covering all three classes.

- [ ] **Step 9: Update `elements/__init__.py` to import `misc`**

Add:
```python
from rhapsody_cli.models.elements import misc as misc  # noqa: F401
```

- [ ] **Step 10: Run full suite + linters, commit**

```bash
pytest tests/unit/models/elements/ -v
ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/
git add src/rhapsody_cli/models/elements/relations/ src/rhapsody_cli/models/elements/misc.py src/rhapsody_cli/models/elements/__init__.py tests/unit/models/elements/
git commit -m "feat: add leaf wrappers (Generalization, Dependency, HyperLink, AssociationRole, Comment, Constraint, EnumerationLiteral)"
```

---

### Task 9: Add Leaf Wrappers (Classifiers Group B + Variables)

**Goal:** Add 3 wrappers: `RPStereotype` (extends `RPClassifier`), `RPAssociationClass` (extends `RPClass`), `RPTag` (extends `RPVariable`).

**Files:**
- Create: `src/rhapsody_cli/models/elements/classifiers/model_stereotype.py`
- Create: `src/rhapsody_cli/models/elements/classifiers/model_association_class.py`
- Modify: `src/rhapsody_cli/models/elements/variables.py` (add `RPTag`)
- Modify: `src/rhapsody_cli/models/elements/classifiers/__init__.py`
- Test: `tests/unit/models/elements/test_stereotype.py`, `test_association_class.py`, `test_tag.py`

**Interfaces:**
- Consumes: `RPClassifier`, `RPClass`, `RPVariable`.
- Produces: 3 registered wrappers. `RPModelElement.getStereotypes()` (Task 2) returns `RPStereotype` instances.

- [ ] **Step 1: TDD `RPStereotype` (extends `RPClassifier`)**

`test_stereotype.py`:
```python
from rhapsody_cli.models._core import wrap
from rhapsody_cli.models.elements.classifiers import RPClassifier, RPStereotype
from tests.unit.models.fakes import make_fake_element


def test_stereotype_is_a_classifier() -> None:
    fake = make_fake_element("Stereotype", getName="MyStereo")
    stereo = RPStereotype(fake)

    assert isinstance(stereo, RPClassifier)
    assert stereo.getName() == "MyStereo"


def test_stereotype_is_registered() -> None:
    fake = make_fake_element("Stereotype")

    wrapped = wrap(fake)

    assert isinstance(wrapped, RPStereotype)


def test_stereotype_add_meta_class_delegates_to_com() -> None:
    fake = make_fake_element("Stereotype")
    stereo = RPStereotype(fake)

    stereo.addMetaClass("Class")

    fake.addMetaClass.assert_called_once_with("Class")


def test_stereotype_get_of_meta_class_returns_string() -> None:
    fake = make_fake_element("Stereotype", getOfMetaClass="Class, Attribute")
    stereo = RPStereotype(fake)

    result = stereo.getOfMetaClass()

    fake.getOfMetaClass.assert_called_once_with()
    assert result == "Class, Attribute"
```

- [ ] **Step 2: Implement `RPStereotype`**

`src/rhapsody_cli/models/elements/classifiers/model_stereotype.py`:
```python
"""Wraps ``com.telelogic.rhapsody.core.IRPStereotype``."""

from rhapsody_cli.models._core import call_com, register_wrapper
from rhapsody_cli.models.elements.classifiers.model_classifier import RPClassifier


class RPStereotype(RPClassifier):
    """Wraps ``IRPStereotype``: a stereotype (extends ``IRPClassifier``)."""

    def addMetaClass(self, meta_class: str) -> None:
        """Adds a metaclass to the list this stereotype can be applied to.

        Args:
            meta_class: The metaclass name to add (e.g. ``"Class"``).
        """
        call_com(lambda: self._com.addMetaClass(meta_class))

    def removeMetaClass(self, meta_class: str) -> None:
        """Removes a metaclass from the list this stereotype applies to.

        Args:
            meta_class: The metaclass name to remove.
        """
        call_com(lambda: self._com.removeMetaClass(meta_class))

    def getOfMetaClass(self) -> str:
        """Returns the metaclasses this stereotype can be applied to.

        Returns:
            Comma-separated metaclass names.
        """
        return str(call_com(lambda: self._com.getOfMetaClass()))

    def getIcon(self) -> str:
        """Returns the full path to the stereotype's image file.

        Returns:
            The icon file path string.
        """
        return str(call_com(lambda: self._com.getIcon()))

    def getIsNewTerm(self) -> int:
        """Checks whether this stereotype is a "new term" stereotype.

        Returns:
            ``1`` if new term, ``0`` otherwise.
        """
        return int(call_com(lambda: self._com.getIsNewTerm()))

    def setIsNewTerm(self, is_new_term: int) -> None:
        """Toggles the "new term" status of this stereotype.

        Args:
            is_new_term: ``1`` for new term, ``0`` otherwise.
        """
        call_com(lambda: self._com.setIsNewTerm(is_new_term))


register_wrapper("Stereotype", RPStereotype)
```

- [ ] **Step 3: Register in `classifiers/__init__.py`**

Add:
```python
from rhapsody_cli.models.elements.classifiers.model_stereotype import RPStereotype  # noqa: F401
```
Add `"RPStereotype"` to `__all__`.

- [ ] **Step 4: Run test, verify pass, commit**

```bash
pytest tests/unit/models/elements/test_stereotype.py -v
git add src/rhapsody_cli/models/elements/classifiers/model_stereotype.py src/rhapsody_cli/models/elements/classifiers/__init__.py tests/unit/models/elements/test_stereotype.py
git commit -m "feat: add RPStereotype wrapper"
```

- [ ] **Step 5: TDD + implement `RPAssociationClass` (extends `RPClass`)**

`model_association_class.py`. Methods (from spec): `getEnd1`, `getEnd2`, `getIsClass`, `setIsClass`. Registration: `register_wrapper("AssociationClass", RPAssociationClass)`. Import `RPClass` from `model_class`. Add to `classifiers/__init__.py`.

Test pattern:
```python
def test_association_class_is_a_class() -> None:
    fake = make_fake_element("AssociationClass", getName="MyAssoc")
    ac = RPAssociationClass(fake)

    assert isinstance(ac, RPClass)
```

- [ ] **Step 6: TDD + implement `RPTag` (extends `RPVariable`)**

Add `RPTag` to `src/rhapsody_cli/models/elements/variables.py`. Methods (from spec): `getBase`, `getFromProfile`, `getMultiplicity`, `setMultiplicity`, `getTagMetaClass`, `setTagMetaClass`, `getValue`, `setValue`, `setTagContextValue`. Registration: `register_wrapper("Tag", RPTag)`.

Import `RPVariable` already in the file. Add `RPTag` class below `RPAttribute`.

Test pattern:
```python
def test_tag_is_a_variable() -> None:
    fake = make_fake_element("Tag", getName="MyTag")
    tag = RPTag(fake)

    assert isinstance(tag, RPVariable)
```

- [ ] **Step 7: Run full suite + linters, commit**

```bash
pytest tests/unit/models/elements/ -v
ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/
git add src/rhapsody_cli/models/elements/classifiers/ src/rhapsody_cli/models/elements/variables.py tests/unit/models/elements/
git commit -m "feat: add RPStereotype, RPAssociationClass, RPTag wrappers"
```

---

### Task 10: Integration Tests + Final Audit

**Goal:** Verify cross-wrapper behavior works end-to-end, then run the full quality gate.

**Files:**
- Create: `tests/unit/models/test_integration.py`
- Verify: every `model_*.py` has a fully checked-off checklist comment

**Interfaces:**
- Consumes: all wrappers from Tasks 2-9.
- Produces: green CI.

- [ ] **Step 1: Write integration tests for factory-method return types**

`tests/unit/models/test_integration.py`:
```python
"""Cross-wrapper integration tests: factory methods return correct subclasses."""

from rhapsody_cli.models._core import RPCollection, wrap
from rhapsody_cli.models.elements.classifiers import RPClass, RPStereotype
from rhapsody_cli.models.elements.containment import RPPackage, RPProfile, RPProject
from rhapsody_cli.models.elements.relations import RPDependency, RPGeneralization
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_package_add_class_returns_rpclass() -> None:
    class_fake = make_fake_element("Class", getName="Widget")
    fake = make_fake_element("Package", addClass=class_fake)
    pkg = RPPackage(fake)

    result = pkg.addClass("Widget")

    fake.addClass.assert_called_once_with("Widget")
    assert isinstance(result, RPClass)
    assert result.getName() == "Widget"


def test_model_element_get_stereotypes_returns_collection_of_rpstereotype() -> None:
    stereo1 = make_fake_element("Stereotype", getName="A")
    stereo2 = make_fake_element("Stereotype", getName="B")
    coll = make_fake_collection([stereo1, stereo2])
    fake = make_fake_element("Class", getStereotypes=coll)
    from rhapsody_cli.models._core import RPModelElement

    element = RPModelElement(fake)
    result = element.getStereotypes()

    assert isinstance(result, RPCollection)
    assert len(result) == 2
    assert isinstance(result[0], RPStereotype)
    assert result[0].getName() == "A"
    assert isinstance(result[1], RPStereotype)
    assert result[1].getName() == "B"


def test_model_element_add_dependency_to_returns_rpdependency() -> None:
    dep_fake = make_fake_element("Dependency", getName="dep")
    target_fake = make_fake_element("Class", getName="Target")
    fake = make_fake_element("Class", getName="Source", addDependencyTo=dep_fake)
    from rhapsody_cli.models._core import RPModelElement

    element = RPModelElement(fake)
    target = wrap(target_fake)

    result = element.addDependencyTo(target)

    fake.addDependencyTo.assert_called_once_with(target_fake)
    assert isinstance(result, RPDependency)


def test_classifier_add_generalization_returns_rpgeneralization() -> None:
    gen_fake = make_fake_element("Generalization")
    base_fake = make_fake_element("Class", getName="Base")
    fake = make_fake_element("Class", getName="Derived", addGeneralization=gen_fake)
    from rhapsody_cli.models.elements.classifiers import RPClassifier

    classifier = RPClassifier(fake)
    base = wrap(base_fake)

    result = classifier.addGeneralization(base)

    assert isinstance(result, RPGeneralization)


def test_project_add_profile_returns_rpprofile() -> None:
    profile_fake = make_fake_element("Profile", getName="SysML")
    fake = make_fake_element("Project", addProfile=profile_fake)
    project = RPProject(fake)

    result = project.addProfile("SysML")

    assert isinstance(result, RPProfile)
    assert result.getName() == "SysML"
```

- [ ] **Step 2: Run integration tests**

Run: `pytest tests/unit/models/test_integration.py -v`
Expected: all PASS. If any fail, fix the underlying wrapper (the factory method may not be returning a wrapped result, or `wrap()` isn't dispatching to the right subclass).

- [ ] **Step 3: Verify every checklist comment is fully checked off**

Read each `model_*.py` file and confirm every row is `[x] impl  [x] docstring  [x] test` (or `deprecated - skipped`). No `[ ]` boxes should remain.

- [ ] **Step 4: Run the full quality gate**

```bash
pytest tests/ -v
ruff check src/ tests/
black --check src/ tests/
mypy src/ tests/
```
Expected: all PASS, zero errors.

- [ ] **Step 5: Check coverage**

```bash
pytest tests/ --cov=src/rhapsody_cli --cov-report=term-missing
```
Expected: total coverage ≥ 80% (target 90%+). If below 80%, add tests for uncovered methods.

- [ ] **Step 6: Commit integration tests**

```bash
git add tests/unit/models/test_integration.py
git commit -m "test: add cross-wrapper integration tests"
```

- [ ] **Step 7: Final commit if any checklist/comment fixes were made**

If Steps 3-5 surfaced any issues (missing docstring, unchecked box, lint finding), fix and commit:
```bash
git add -A
git commit -m "style: final audit fixes for structural wrappers"
```

- [ ] **Step 8: Open a PR**

```bash
git push -u origin docs/structural-model-wrappers-design
gh pr create --title "feat: structural model wrappers — full Java API parity (Iteration 1)" --body "$(cat <<'EOF'
## Summary

- Completes 8 existing wrappers to full method parity with their Java interfaces (RPModelElement, RPUnit, RPClassifier, RPClass, RPRelation, RPInstance, RPPackage, RPProject)
- Adds 17 new wrappers (RPGeneralization, RPDependency, RPHyperLink, RPEnumerationLiteral, RPComment, RPConstraint, RPTag, RPStereotype, RPAssociationClass, RPAssociationRole, RPProfile, RPComponent, RPConfiguration, RPModule, RPNode, RPCollaboration, RPComponentInstance)
- Refactors classifiers/relations/containment from flat modules into packages with model_*.py per-class files
- Backfills Java API docstrings on every public method

Spec: `docs/superpowers/specs/2026-07-08-structural-model-wrappers-design.md`

## Test plan

- [x] All unit tests pass (`pytest tests/`)
- [x] Ruff passes (`ruff check src/ tests/`)
- [x] Black passes (`black --check src/ tests/`)
- [x] Mypy passes (`mypy src/ tests/`)
- [x] Coverage ≥ 80%
- [x] Every wrapper file has its method-parity checklist fully checked off
EOF
)"
```

---

## Self-Review Notes

**Spec coverage check:**
- Step 0 (refactor) → Task 1 ✓
- Step 1 (base layer) → Tasks 2-3 ✓
- Step 2 (mid layer) → Tasks 4-5 ✓
- Step 3 (containment layer) → Tasks 6-7 ✓
- Step 4 (leaf wrappers) → Tasks 8-9 ✓
- Step 5 (integration tests) → Task 10 ✓
- Step 6 (audit) → Task 10 ✓
- Java API docs as docstrings → Global Constraints + every task's TDD steps ✓
- Deprecated methods skipped → Global Constraints + checklist convention ✓
- Re-export rule (backwards compat) → Task 1 package `__init__.py` files ✓
- Coverage tracking checklists → every task's Step 1 ✓

**Type consistency check:**
- `RPModelElement`, `RPUnit`, `RPCollection` imported from `_core` consistently.
- `wrap()` return type is `RPModelElement`; subclasses are confirmed via `isinstance` in tests.
- Factory methods return `Any` (typed as the wrapper in docstrings) — consistent with existing `addAttribute` pattern in `classifiers.py`.
- All wrapper params unwrapped via `._com` — consistent across all examples.

**Placeholder check:** No "TBD" or "TODO" left in actionable steps. The 3 TBD-parent wrappers (RPConfiguration, RPNode, RPCollaboration) have Step 1 of Task 7 dedicated to resolving them before implementation.
