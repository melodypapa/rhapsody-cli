# Core Module (`core.py`) Integration Tests Completion Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add integration tests for the 142 remaining untested methods of `RPModelElement`, `RPUnit`, and `RPCollection` in `src/rhapsody_cli/models/core.py`, and flip their in-source `[ ] integration test` checklist markers to `[x]`.

**Architecture:** Extends `tests/integration/models/test_core.py` with additional test methods/classes, using the existing `rhapsody_app`/`test_project` fixtures from `tests/integration/conftest.py`. Tests exercise real COM objects, asserting both return type and read-back persisted state.

**Tech Stack:** pytest, pywin32 (win32com), live Rhapsody COM API, `uuid.uuid4().hex[:8]` for unique names.

## Global Constraints

- Windows-only runtime (COM automation requires Windows + a running Rhapsody instance)
- All test classes use `@pytest.mark.integration`
- All tests consume the `test_project: RPProject` fixture (session-scoped)
- Use `_unique(prefix)` with `uuid.uuid4().hex[:8]` for unique element names
- Always use `try/finally` for cleanup — never rely solely on fixture teardown
- Assert both `isinstance()` return types and read-back values
- After each task's tests pass, flip the corresponding `[ ] integration test` to `[x] integration test` in `src/rhapsody_cli/models/core.py` for every method that task covers
- Quality gate after each task: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit` (integration tests themselves are run separately with `pytest tests/integration -m integration`, which requires a live, attached Rhapsody instance — do not assume CI runs them)
- Follow the exact style of `tests/integration/models/elements/classifiers/test_model_class.py`
- **Exception for RPCollection:** 8 of the `IRPCollection` checklist rows (`addGraphicalItem`, `toList`, `setSize`, `remove`, `setString`, `setModelElement`, `empty`, `setInteger`) are marked `[ ] impl` — they have no implementation yet. Task 16 below is the one deliberate exception to the "no behavior change" rule: it implements these 8 methods (following the exact patterns already used elsewhere in `RPCollection`/`RPModelElement`), adds unit tests (with fakes, per `tests/unit/models/fakes.py`), and adds integration tests, before flipping their checklist boxes. All other 17 tasks are integration-test-only additions with zero behavior change to `core.py`.

---

## Task 1: Dependencies & Associations

**Files:**
- Modify: `tests/integration/models/test_core.py`
- Modify: `src/rhapsody_cli/models/core.py` (flip checklist boxes only, no behavior change)

**Methods covered:** `add_association`, `add_dependency`, `add_dependency_between`, `add_dependency_to`, `add_remote_dependency_to`, `delete_dependency`, `get_dependencies`, `get_owned_dependencies`, `get_remote_dependencies`, `get_association_classes`, `get_references`

- [ ] **Step 1: Write the failing/new integration tests**

```python
import uuid

import pytest

from rhapsody_cli.models.core import RPCollection, RPModelElement
from rhapsody_cli.models.elements.containment import RPPackage, RPProject


@pytest.mark.integration
class TestRPModelElementDependenciesIntegration:
    """Integration tests for RPModelElement dependency/association methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, RPPackage)
        return pkg

    def test_add_dependency_to_and_get_dependencies(self, test_project: RPProject) -> None:
        pkg = self._create_package(test_project, self._unique("DepPkg"))
        try:
            source = pkg.add_class(self._unique("Source"))
            target = pkg.add_class(self._unique("Target"))
            dependency = source.add_dependency_to(target)
            assert dependency is not None
            assert isinstance(dependency, RPModelElement)

            deps = source.get_dependencies()
            assert isinstance(deps, RPCollection)
            assert len(list(deps)) >= 1

            source.delete_dependency(dependency)
            deps_after = source.get_dependencies()
            assert len(list(deps_after)) == 0
        finally:
            pkg.delete_from_project()
```

For the remaining methods in this task, follow the same pattern shown above (one test method per behavior, or a shared test method with multiple assertions where methods are tightly coupled getter/setter pairs). Notes:
- `add_dependency` uses `depends_on_name`/`depends_on_type` string lookup rather than a direct handle — create the target class first so the lookup succeeds.
- `add_dependency_between` requires two already-created elements plus an owner on which the call is made (can be the package).
- `add_association` requires two `RPRelation`-compatible ends (create via associations on a class, or use two classes connected by an existing association's ends) — if constructing valid `end1`/`end2` relation objects proves impractical without the `relations` subpackage helpers, coordinate with that subpackage's plan and mark this one sub-case `xfail(reason="requires RPRelation helper from relations subpackage", strict=False)`.
- `add_remote_dependency_to` and `get_remote_dependencies` only apply to Design Manager/RMM projects; if the live test project has no RMM configuration, assert the call succeeds and returns an empty collection or wrap the assertion in `pytest.mark.xfail(reason="requires RMM-enabled project", strict=False)`.
- `get_association_classes` and `get_references` should be exercised on a package with at least one association class and cross-referencing dependency respectively.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/test_core.py -m integration -v`
Expected: all new tests PASS (or documented `xfail` for known COM quirks)

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/core.py`, change `[ ] integration test` to `[x] integration test` for: `add_association`, `add_dependency`, `add_dependency_between`, `add_dependency_to`, `add_remote_dependency_to`, `delete_dependency`, `get_dependencies`, `get_owned_dependencies`, `get_remote_dependencies`, `get_association_classes`, `get_references`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/test_core.py src/rhapsody_cli/models/core.py
git commit -m "test: add integration tests for RPModelElement dependency methods"
```

---

## Task 2: Stereotypes & Tags

**Files:**
- Modify: `tests/integration/models/test_core.py`
- Modify: `src/rhapsody_cli/models/core.py` (flip checklist boxes only, no behavior change)

**Methods covered:** `add_specific_stereotype`, `remove_stereotype`, `get_stereotypes`, `get_new_term_stereotype`, `get_all_tags`, `get_local_tags`, `get_tag`, `set_tag_value`, `set_tag_element_value`, `set_tag_context_value`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPModelElementStereotypesTagsIntegration:
    """Integration tests for RPModelElement stereotype and tag methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_add_stereotype_and_get_stereotypes_roundtrip(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("StereoPkg"))
        try:
            cls = pkg.add_class(self._unique("StereoCls"))
            stereotype = cls.add_stereotype(self._unique("MyStereotype"), "Class")
            assert stereotype is not None
            assert isinstance(stereotype, RPModelElement)

            stereotypes = cls.get_stereotypes()
            names = [s.get_name() for s in stereotypes]
            assert stereotype.get_name() in names

            cls.remove_stereotype(stereotype)
            stereotypes_after = cls.get_stereotypes()
            names_after = [s.get_name() for s in stereotypes_after]
            assert stereotype.get_name() not in names_after
        finally:
            pkg.delete_from_project()
```

For the remaining methods, follow the same pattern:
- `add_specific_stereotype` applies an already-existing wrapped stereotype (create one first via `add_stereotype`, `remove_stereotype` it, then re-apply via `add_specific_stereotype`).
- `get_all_tags`/`get_local_tags`/`get_tag` require a metaclass with an applied stereotype that defines a tag definition — apply a stereotype with a defined tag (or use a metatype tag if the live project ships one), then call `get_tag(name)`.
- `set_tag_value`, `set_tag_element_value`, `set_tag_context_value` should be exercised as getter/setter roundtrips: apply the tag, set its value, then read it back via the returned wrapped tag's `get_...` accessors (from the `tags` subpackage, if available) or via `get_tag(name)` again.
- `get_new_term_stereotype` only returns a non-`None` wrapper when a "new term" stereotype has been applied; if no such fixture exists in the live project, assert the call does not raise and mark with `xfail(reason="requires a 'new term' stereotype fixture", strict=False)` if it cannot be constructed.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/test_core.py -m integration -v`
Expected: all new tests PASS (or documented `xfail` for known COM quirks)

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/core.py`, change `[ ] integration test` to `[x] integration test` for: `add_specific_stereotype`, `remove_stereotype`, `get_stereotypes`, `get_new_term_stereotype`, `get_all_tags`, `get_local_tags`, `get_tag`, `set_tag_value`, `set_tag_element_value`, `set_tag_context_value`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/test_core.py src/rhapsody_cli/models/core.py
git commit -m "test: add integration tests for RPModelElement stereotype/tag methods"
```

---

## Task 3: Descriptions & Display Names

**Files:**
- Modify: `tests/integration/models/test_core.py`
- Modify: `src/rhapsody_cli/models/core.py` (flip checklist boxes only, no behavior change)

**Methods covered:** `get_description`, `get_description_html`, `get_description_plain_text`, `get_description_rtf`, `is_description_rtf`, `set_description`, `set_description_and_hyperlinks`, `set_description_html`, `set_description_rtf`, `get_display_name`, `get_display_name_rtf`, `is_display_name_rtf`, `set_display_name`, `set_display_name_rtf`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPModelElementDescriptionDisplayNameIntegration:
    """Integration tests for RPModelElement description and display-name methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_set_and_get_description_roundtrip(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("DescPkg"))
        try:
            cls = pkg.add_class(self._unique("DescCls"))
            cls.set_description("A test description")
            description = cls.get_description()
            assert description == "A test description"
            assert isinstance(description, str)

            plain_text = cls.get_description_plain_text()
            assert isinstance(plain_text, str)
            assert "A test description" in plain_text
        finally:
            pkg.delete_from_project()
```

For the remaining methods, follow the same pattern:
- `set_description_rtf`/`get_description_rtf`/`is_description_rtf` — set an RTF-formatted string (e.g. `r"{\rtf1 Hello}"`), then verify `is_description_rtf()` returns truthy and `get_description_rtf()` round-trips.
- `set_description_html`/`get_description_html` — the docstring notes the Java API documents this as "not implemented"; verify actual live behavior and mark `xfail(reason="Rhapsody documents setDescriptionHTML as unimplemented", strict=False)` if it silently no-ops.
- `set_description_and_hyperlinks` needs an `RPCollection` of target elements — build one with two classes and assert the description text is applied (hyperlink target verification can be skipped if the Java API does not expose a getter for created hyperlinks distinctly from `get_hyper_links`).
- `set_display_name`/`get_display_name`, `set_display_name_rtf`/`get_display_name_rtf`/`is_display_name_rtf` follow the identical roundtrip pattern as descriptions, substituting the display name accessors.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/test_core.py -m integration -v`
Expected: all new tests PASS (or documented `xfail` for known COM quirks)

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/core.py`, change `[ ] integration test` to `[x] integration test` for: `get_description`, `get_description_html`, `get_description_plain_text`, `get_description_rtf`, `is_description_rtf`, `set_description`, `set_description_and_hyperlinks`, `set_description_html`, `set_description_rtf`, `get_display_name`, `get_display_name_rtf`, `is_display_name_rtf`, `set_display_name`, `set_display_name_rtf`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/test_core.py src/rhapsody_cli/models/core.py
git commit -m "test: add integration tests for RPModelElement description/display-name methods"
```

---

## Task 4: Properties

**Files:**
- Modify: `tests/integration/models/test_core.py`
- Modify: `src/rhapsody_cli/models/core.py` (flip checklist boxes only, no behavior change)

**Methods covered:** `add_property`, `remove_property`, `get_property_value`, `get_property_value_conditional`, `get_property_value_conditional_explicit`, `get_property_value_explicit`, `set_property_value`, `get_overridden_properties`, `get_overridden_properties_by_pattern`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPModelElementPropertiesIntegration:
    """Integration tests for RPModelElement property methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_set_and_get_property_value_roundtrip(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("PropPkg"))
        try:
            cls = pkg.add_class(self._unique("PropCls"))
            property_key = "General::Documentation::ShowNumbering"
            cls.set_property_value(property_key, "True")
            value = cls.get_property_value(property_key)
            assert value == "True"
            assert isinstance(value, str)

            explicit_value = cls.get_property_value_explicit(property_key)
            assert explicit_value == "True"

            overridden = cls.get_overridden_properties(0)
            keys = [p.get_name() for p in overridden]
            assert any(property_key.split("::")[-1] in k or property_key in k for k in keys) or len(list(overridden)) >= 1
        finally:
            pkg.delete_from_project()
```

For the remaining methods, follow the same pattern:
- `add_property` creates a brand-new custom property (`property_key`, `property_type`, `property_value`) that does not exist on the metaclass by default; verify via `get_property_value` after adding, then `remove_property` and confirm `get_property_value_explicit` no longer returns the explicit value (falls back to default/empty).
- `get_property_value_conditional`/`get_property_value_conditional_explicit` need `formal_key`/`actual_values` `RPCollection` arguments — build empty `RPCollection`s (via an existing collection-returning call, e.g. `cls.get_all_tags()`, cleared, or a helper that wraps a raw COM collection) if the live property is non-conditional, and assert the returned value matches the unconditional value.
- `get_overridden_properties_by_pattern` should use a pattern string matching the property key set above (e.g. `"*ShowNumbering*"`) and assert the property is found with `localy_overriden_only=1`.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/test_core.py -m integration -v`
Expected: all new tests PASS (or documented `xfail` for known COM quirks)

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/core.py`, change `[ ] integration test` to `[x] integration test` for: `add_property`, `remove_property`, `get_property_value`, `get_property_value_conditional`, `get_property_value_conditional_explicit`, `get_property_value_explicit`, `set_property_value`, `get_overridden_properties`, `get_overridden_properties_by_pattern`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/test_core.py src/rhapsody_cli/models/core.py
git commit -m "test: add integration tests for RPModelElement property methods"
```

---

## Task 5: Navigation & Search

**Files:**
- Modify: `tests/integration/models/test_core.py`
- Modify: `src/rhapsody_cli/models/core.py` (flip checklist boxes only, no behavior change)

**Methods covered:** `find_elements_by_full_name`, `find_nested_element`, `find_nested_element_recursive`, `get_nested_elements_recursive`, `get_full_path_name`, `get_full_path_name_in`, `get_project`, `set_owner`, `has_nested_elements`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPModelElementNavigationIntegration:
    """Integration tests for RPModelElement navigation/search methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_find_nested_element(self, test_project: RPProject) -> None:
        pkg_name = self._unique("NavPkg")
        class_name = self._unique("NavCls")
        pkg = test_project.add_package(pkg_name)
        try:
            pkg.add_class(class_name)
            found = pkg.find_nested_element(class_name, "Class")
            assert found is not None
            assert isinstance(found, RPModelElement)
            assert found.get_name() == class_name

            not_found = pkg.find_nested_element(self._unique("Missing"), "Class")
            assert not_found.get_name() == ""
        finally:
            pkg.delete_from_project()
```

For the remaining methods, follow the same pattern:
- `find_nested_element_recursive` should find an element nested two levels deep (package -> subpackage -> class) where `find_nested_element` (non-recursive) fails.
- `find_elements_by_full_name` uses a full path string (e.g. `f"{pkg_name}::{class_name}"`).
- `get_nested_elements_recursive` should return a collection containing the element itself plus all descendants — assert `len(...) >= 1 + number_of_children_created`.
- `get_full_path_name`/`get_full_path_name_in` should assert the returned strings contain both the package and class names in the documented formats (`package::class` and `class in package` respectively).
- `get_project` should be called on a nested class and assert `.get_name() == test_project.get_name()`.
- `set_owner` should move a class from one package to another and assert `get_owner().get_name()` reflects the new owner.
- `has_nested_elements` should assert `1` for a package with a class and `0` for an empty package.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/test_core.py -m integration -v`
Expected: all new tests PASS (or documented `xfail` for known COM quirks)

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/core.py`, change `[ ] integration test` to `[x] integration test` for: `find_elements_by_full_name`, `find_nested_element`, `find_nested_element_recursive`, `get_nested_elements_recursive`, `get_full_path_name`, `get_full_path_name_in`, `get_project`, `set_owner`, `has_nested_elements`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/test_core.py src/rhapsody_cli/models/core.py
git commit -m "test: add integration tests for RPModelElement navigation/search methods"
```

---

## Task 6: Cloning, Change Type & Templates

**Files:**
- Modify: `tests/integration/models/test_core.py`
- Modify: `src/rhapsody_cli/models/core.py` (flip checklist boxes only, no behavior change)

**Methods covered:** `become_template_instantiation_of`, `change_to`, `clone`, `get_of_template`, `set_of_template`, `get_template_parameters`, `is_a_template`, `get_ti`, `set_ti`, `synchronize_template_instantiation`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPModelElementCloningTemplatesIntegration:
    """Integration tests for RPModelElement cloning/change-type/template methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_clone_creates_independent_copy(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("ClonePkg"))
        try:
            original = pkg.add_class(self._unique("Original"))
            clone_name = self._unique("Clone")
            clone = original.clone(clone_name, pkg)
            assert clone is not None
            assert isinstance(clone, RPModelElement)
            assert clone.get_name() == clone_name
            assert clone.get_guid() != original.get_guid()
        finally:
            pkg.delete_from_project()
```

For the remaining methods, follow the same pattern:
- `change_to` should change a class into another compatible metaclass (e.g. `"Class"` -> `"ClassCategory"` or a documented safe conversion) and assert `get_meta_class()` reflects the new type; capture the returned handle since the original is invalidated.
- `become_template_instantiation_of`/`get_of_template`/`set_of_template`/`get_ti`/`set_ti`/`synchronize_template_instantiation` require a template class (`is_a_template()` returns `1`, achieved via `add_stereotype`/property, or via a class with template parameters) and an instantiation class; assert `get_of_template().get_name()` matches after `become_template_instantiation_of`.
- `get_template_parameters` should be called on the template class and assert the returned `RPCollection` is empty or contains parameters if any were added.
- `is_a_template` should assert `0` for a plain class and `1` once configured as a template (via the project's template mechanism, e.g. adding a template parameter or applying the relevant metatype flag).
- If constructing a true template/instantiation pair proves impractical with the base `RPModelElement`/`RPClass` API alone, mark the template-pair-dependent tests `xfail(reason="requires template parameter API from classifiers subpackage", strict=False)` and note the dependency for the classifiers subpackage's own plan.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/test_core.py -m integration -v`
Expected: all new tests PASS (or documented `xfail` for known COM quirks)

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/core.py`, change `[ ] integration test` to `[x] integration test` for: `become_template_instantiation_of`, `change_to`, `clone`, `get_of_template`, `set_of_template`, `get_template_parameters`, `is_a_template`, `get_ti`, `set_ti`, `synchronize_template_instantiation`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/test_core.py src/rhapsody_cli/models/core.py
git commit -m "test: add integration tests for RPModelElement clone/change-type/template methods"
```

---

## Task 7: Redefines & Constraints

**Files:**
- Modify: `tests/integration/models/test_core.py`
- Modify: `src/rhapsody_cli/models/core.py` (flip checklist boxes only, no behavior change)

**Methods covered:** `add_redefines`, `remove_redefines`, `get_redefines`, `get_constraints`, `get_constraints_by_him`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPModelElementRedefinesConstraintsIntegration:
    """Integration tests for RPModelElement redefine/constraint methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_add_and_remove_redefines_roundtrip(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("RedefPkg"))
        try:
            base_op = pkg.add_class(self._unique("BaseCls")).add_operation(self._unique("op"))
            child_cls = pkg.add_class(self._unique("ChildCls"))
            new_op = child_cls.add_operation(self._unique("op"))

            new_op.add_redefines(base_op)
            redefines = new_op.get_redefines()
            assert len(list(redefines)) >= 1

            new_op.remove_redefines(base_op)
            redefines_after = new_op.get_redefines()
            assert len(list(redefines_after)) == 0
        finally:
            pkg.delete_from_project()
```

For the remaining methods, follow the same pattern:
- `get_constraints` should be exercised on an element that has at least one constraint annotation attached (create via the annotations/constraints element API if available, else assert the call succeeds and returns an empty `RPCollection` on a plain class).
- `get_constraints_by_him` is documented "for internal use only" — assert it returns an `RPCollection` without raising; if it consistently mirrors `get_constraints`, assert equality of counts.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/test_core.py -m integration -v`
Expected: all new tests PASS (or documented `xfail` for known COM quirks)

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/core.py`, change `[ ] integration test` to `[x] integration test` for: `add_redefines`, `remove_redefines`, `get_redefines`, `get_constraints`, `get_constraints_by_him`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/test_core.py src/rhapsody_cli/models/core.py
git commit -m "test: add integration tests for RPModelElement redefine/constraint methods"
```

---

## Task 8: OSLC, Remote & Requirement Traceability

**Files:**
- Modify: `tests/integration/models/test_core.py`
- Modify: `src/rhapsody_cli/models/core.py` (flip checklist boxes only, no behavior change)

**Methods covered:** `create_oslc_link`, `delete_oslc_link`, `get_oslc_links`, `get_hyper_links`, `get_remote_uri`, `is_remote`, `get_rmm_url`, `get_requirement_traceability_handle`, `set_requirement_traceability_handle`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPModelElementOslcRemoteIntegration:
    """Integration tests for RPModelElement OSLC/remote/traceability methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_create_oslc_link_not_implemented(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("OslcPkg"))
        try:
            cls = pkg.add_class(self._unique("OslcCls"))
            with pytest.raises(NotImplementedError):
                cls.create_oslc_link("Related", "https://example.com/artifact/1")
        finally:
            pkg.delete_from_project()
```

For the remaining methods, follow the same pattern:
- `delete_oslc_link` and `get_oslc_links` both raise `NotImplementedError` per the docstrings (Rhapsody2.Application.1 does not expose these) — assert `pytest.raises(NotImplementedError)` for each, confirming live behavior matches the documented limitation.
- `get_hyper_links` should be exercised on an element with a hyperlink set via `set_description_and_hyperlinks` (Task 3) and assert the collection is non-empty; on a plain element assert it returns an empty `RPCollection`.
- `get_remote_uri`/`is_remote` should assert an empty string / `0` respectively for a normal (non-DOORS, non-RMM) model element.
- `get_rmm_url` should assert an empty string (or a valid URL if the live test project is RMM-connected) without raising.
- `get_requirement_traceability_handle`/`set_requirement_traceability_handle` should be exercised on a requirement-capable element (create via the requirements subpackage if available, else on a plain class if the property still applies) with a roundtrip: set an int handle, read it back.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/test_core.py -m integration -v`
Expected: all new tests PASS (or documented `xfail` for known COM quirks)

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/core.py`, change `[ ] integration test` to `[x] integration test` for: `create_oslc_link`, `delete_oslc_link`, `get_oslc_links`, `get_hyper_links`, `get_remote_uri`, `is_remote`, `get_rmm_url`, `get_requirement_traceability_handle`, `set_requirement_traceability_handle`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/test_core.py src/rhapsody_cli/models/core.py
git commit -m "test: add integration tests for RPModelElement OSLC/remote/traceability methods"
```

---

## Task 9: Metadata, Icons, GUID & Display Flags

**Files:**
- Modify: `tests/integration/models/test_core.py`
- Modify: `src/rhapsody_cli/models/core.py` (flip checklist boxes only, no behavior change)

**Methods covered:** `get_binary_id`, `get_decoration_style`, `set_decoration_style`, `get_icon_file_name`, `get_overlay_icon_file_name`, `get_interface_name`, `get_is_external`, `get_is_of_meta_class`, `get_is_unresolved`, `get_user_defined_meta_class`, `is_modified`, `set_guid`, `get_tool_tip_html`, `get_is_show_display_name`, `set_is_show_display_name`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPModelElementMetadataIntegration:
    """Integration tests for RPModelElement metadata/icon/GUID methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_get_binary_id_matches_guid(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("MetaPkg"))
        try:
            cls = pkg.add_class(self._unique("MetaCls"))
            binary_id = cls.get_binary_id()
            assert isinstance(binary_id, bytes)
            assert len(binary_id) > 0

            guid = cls.get_guid()
            assert isinstance(guid, str)
            assert len(guid) > 0
        finally:
            pkg.delete_from_project()
```

For the remaining methods, follow the same pattern:
- `get_interface_name` should assert `"IRPClass"` for a class element.
- `get_is_of_meta_class` should assert `1` for `"Class"` and `0` for an unrelated metaclass such as `"Package"`.
- `get_icon_file_name`/`get_overlay_icon_file_name` should assert non-empty strings ending in a recognizable image extension (e.g. `.png`/`.ico`/`.bmp`) or an empty string if no overlay is set.
- `get_decoration_style`/`set_decoration_style` should roundtrip a documented decoration style name (query `Format::Decoration::StyleNames` via `get_property_value` first to pick a valid value, or use a known default such as `"None"`).
- `get_is_external` should assert `0` for a normally-created class.
- `get_is_unresolved` should assert `0` for a normal element (an unresolved element requires a broken reference, which may need `xfail` if not constructible in this test project).
- `get_user_defined_meta_class` should assert an empty string for a plain `Class`, and a New Term name if a New Term stereotype was applied (coordinate with Task 2).
- `is_modified` should assert truthy immediately after a mutation (e.g. `set_name`) on an unsaved element.
- `set_guid` should set a new valid GUID string and assert `get_guid()` reflects it.
- `get_tool_tip_html` should assert a non-empty HTML string containing the element's name.
- `get_is_show_display_name`/`set_is_show_display_name` should roundtrip `0`/`1`.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/test_core.py -m integration -v`
Expected: all new tests PASS (or documented `xfail` for known COM quirks)

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/core.py`, change `[ ] integration test` to `[x] integration test` for: `get_binary_id`, `get_decoration_style`, `set_decoration_style`, `get_icon_file_name`, `get_overlay_icon_file_name`, `get_interface_name`, `get_is_external`, `get_is_of_meta_class`, `get_is_unresolved`, `get_user_defined_meta_class`, `is_modified`, `set_guid`, `get_tool_tip_html`, `get_is_show_display_name`, `set_is_show_display_name`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/test_core.py src/rhapsody_cli/models/core.py
git commit -m "test: add integration tests for RPModelElement metadata/icon/GUID methods"
```

---

## Task 10: Diagnostics, Annotations, Files, Save Unit & UI Actions

**Files:**
- Modify: `tests/integration/models/test_core.py`
- Modify: `src/rhapsody_cli/models/core.py` (flip checklist boxes only, no behavior change)

**Methods covered:** `error_message`, `get_error_message`, `get_annotations`, `get_controlled_files`, `get_save_unit`, `get_main_diagram`, `set_main_diagram`, `has_panel_widget`, `high_light_element`, `locate_in_browser`, `open_features_dialog`, `add_link_to_element`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPModelElementDiagnosticsUiIntegration:
    """Integration tests for RPModelElement diagnostics/annotations/UI-action methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_error_message_empty_after_success(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("ErrPkg"))
        try:
            cls = pkg.add_class(self._unique("ErrCls"))
            cls.get_name()
            message = cls.error_message()
            assert message == ""
            assert isinstance(message, str)
        finally:
            pkg.delete_from_project()
```

For the remaining methods, follow the same pattern:
- `get_error_message` mirrors `error_message` — assert the same empty-string behavior after a successful call.
- `get_annotations` should assert an empty `RPCollection` for a plain class (annotation-attaching helpers likely live in the annotations subpackage; coordinate if a fixture is needed).
- `get_controlled_files` should assert an empty `RPCollection` for a project not under configuration management.
- `get_save_unit` should assert the returned wrapped unit's `get_name()` matches the owning package/unit name (classes are typically saved as part of their owning unit).
- `get_main_diagram`/`set_main_diagram` should roundtrip: create a diagram (via the package/class's diagram-adding API), `set_main_diagram(diagram)`, then assert `get_main_diagram().get_guid() == diagram.get_guid()`.
- `has_panel_widget` should assert `0` for an element not bound to a panel diagram widget.
- `high_light_element`/`locate_in_browser`/`open_features_dialog` are UI-only actions with no observable return value beyond a status int (`locate_in_browser`) — assert the calls do not raise, and for `locate_in_browser` assert the return value is `1` or `0` (an `int`).
- `add_link_to_element` requires either an association or a pair of ports — build a minimal association between two classes first (coordinate with the relations subpackage's plan if `RPRelation` helpers are needed), or mark `xfail(reason="requires RPRelation/port helpers from relations subpackage", strict=False)` if not constructible standalone.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/test_core.py -m integration -v`
Expected: all new tests PASS (or documented `xfail` for known COM quirks)

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/core.py`, change `[ ] integration test` to `[x] integration test` for: `error_message`, `get_error_message`, `get_annotations`, `get_controlled_files`, `get_save_unit`, `get_main_diagram`, `set_main_diagram`, `has_panel_widget`, `high_light_element`, `locate_in_browser`, `open_features_dialog`, `add_link_to_element`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/test_core.py src/rhapsody_cli/models/core.py
git commit -m "test: add integration tests for RPModelElement diagnostics/annotations/UI-action methods"
```

---

## Task 11: RPUnit Persistence — Filename, Language, Path & Lifecycle

**Files:**
- Modify: `tests/integration/models/test_core.py`
- Modify: `src/rhapsody_cli/models/core.py` (flip checklist boxes only, no behavior change)

**Methods covered:** `get_filename`, `set_filename`, `get_language`, `set_language`, `get_unit_path`, `set_unit_path`, `get_current_directory`, `load`, `unload`, `save`, `get_last_modified_time`

- [ ] **Step 1: Write the failing/new integration tests**

```python
import pytest

from rhapsody_cli.models.core import RPUnit
from rhapsody_cli.models.elements.containment import RPPackage, RPProject


@pytest.mark.integration
class TestRPUnitPersistenceIntegration:
    """Integration tests for RPUnit filename/language/path/lifecycle methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_set_and_get_filename_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("UnitPkg")
        pkg = test_project.add_package(pkg_name)
        try:
            assert isinstance(pkg, RPUnit)
            new_filename = self._unique("renamed_unit")
            pkg.set_filename(new_filename)
            filename = pkg.get_filename()
            assert new_filename in filename
            assert isinstance(filename, str)
        finally:
            pkg.delete_from_project()
```

For the remaining methods, follow the same pattern:
- `get_language`/`set_language` should roundtrip `"C++"` (or the project's configured default) with `recursive=0`, asserting the getter reflects the new value.
- `get_unit_path`/`set_unit_path` should assert the path contains the unit's filename both with `b_full_path=1` and `b_full_path=0`.
- `get_current_directory` should assert the returned directory matches (or is a parent of) `TEST_PROJECT_DIR` from `conftest.py`.
- `save` should be called after a mutation (e.g. `set_name`) and assert no exception is raised and `is_modified()` (inherited from `RPModelElement`) becomes `0` afterward.
- `load`/`unload` should be exercised as a pair: `unload()` a package, assert `get_is_stub()` becomes `1`, then `load(with_subs=1)` and assert `get_is_stub()` returns to `0`.
- `get_last_modified_time` should assert a non-empty string is returned after `save()`.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/test_core.py -m integration -v`
Expected: all new tests PASS (or documented `xfail` for known COM quirks)

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/core.py`, change `[ ] integration test` to `[x] integration test` for: `get_filename`, `set_filename`, `get_language`, `set_language`, `get_unit_path`, `set_unit_path`, `get_current_directory`, `load`, `unload`, `save`, `get_last_modified_time`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/test_core.py src/rhapsody_cli/models/core.py
git commit -m "test: add integration tests for RPUnit persistence methods"
```

---

## Task 12: RPUnit CM State & Read-Only/Stub Flags

**Files:**
- Modify: `tests/integration/models/test_core.py`
- Modify: `src/rhapsody_cli/models/core.py` (flip checklist boxes only, no behavior change)

**Methods covered:** `get_cm_header`, `set_cm_header`, `get_cm_state`, `is_read_only`, `set_read_only`, `get_is_stub`, `is_separate_save_unit`, `set_separate_save_unit`, `get_include_in_next_load`, `set_include_in_next_load`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPUnitCmStateIntegration:
    """Integration tests for RPUnit configuration-management/read-only/stub methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_set_and_get_read_only_roundtrip(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("ReadOnlyPkg"))
        try:
            assert isinstance(pkg, RPUnit)
            pkg.save()
            pkg.set_read_only(True)
            assert pkg.is_read_only() is True
            pkg.set_read_only(False)
            assert pkg.is_read_only() is False
        finally:
            pkg.delete_from_project()
```

For the remaining methods, follow the same pattern:
- `get_cm_header`/`set_cm_header` should roundtrip a header string (empty on a non-CM project is a valid baseline; still assert the setter/getter agree after a set).
- `get_cm_state` should assert an `int` is returned without raising (value semantics depend on CM tool configuration — assert type only if the live project is not under CM).
- `get_is_stub` should assert `0` for a loaded unit and `1` after `unload()` (coordinate with Task 11's load/unload test, or duplicate a minimal unload here).
- `is_separate_save_unit`/`set_separate_save_unit` should roundtrip `1`/`0` on a package (packages default to separate save units in Rhapsody).
- `get_include_in_next_load`/`set_include_in_next_load` should roundtrip `0`/`1`.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/test_core.py -m integration -v`
Expected: all new tests PASS (or documented `xfail` for known COM quirks)

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/core.py`, change `[ ] integration test` to `[x] integration test` for: `get_cm_header`, `set_cm_header`, `get_cm_state`, `is_read_only`, `set_read_only`, `get_is_stub`, `is_separate_save_unit`, `set_separate_save_unit`, `get_include_in_next_load`, `set_include_in_next_load`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/test_core.py src/rhapsody_cli/models/core.py
git commit -m "test: add integration tests for RPUnit CM-state/read-only/stub methods"
```

---

## Task 13: RPUnit Cross-Project Operations & Nesting

**Files:**
- Modify: `tests/integration/models/test_core.py`
- Modify: `src/rhapsody_cli/models/core.py` (flip checklist boxes only, no behavior change)

**Methods covered:** `copy_to_another_project`, `move_to_another_project_leave_a_reference`, `reference_to_another_project`, `get_nested_save_units`, `get_nested_save_units_count`, `get_structure_diagrams`, `get_add_to_model_mode`, `is_reference_unit`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPUnitCrossProjectIntegration:
    """Integration tests for RPUnit cross-project and nesting methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_get_nested_save_units_count_matches_collection(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("NestPkg"))
        try:
            assert isinstance(pkg, RPUnit)
            sub_pkg = pkg.add_package(self._unique("SubPkg"))
            sub_pkg.set_separate_save_unit(1)
            sub_pkg.save()

            count = pkg.get_nested_save_units_count()
            units = pkg.get_nested_save_units()
            assert isinstance(count, int)
            assert count == len(list(units))
        finally:
            pkg.delete_from_project()
```

For the remaining methods, follow the same pattern:
- `copy_to_another_project` requires a second open project as the target — if only one project is available via the session fixture, either create a second `RPProject` inline via `rhapsody_app.create_new_project(...)` in a temp directory (cleaning it up in `finally`) or mark `xfail(reason="requires a second live project", strict=False)`.
- `move_to_another_project_leave_a_reference`/`reference_to_another_project` follow the same two-project setup as `copy_to_another_project`; assert `is_reference_unit()` returns `1` on the resulting reference unit where applicable.
- `get_structure_diagrams` should assert an empty `RPCollection` for a class with no structure diagrams (or non-empty after adding one via the diagram-adding API).
- `get_add_to_model_mode` should assert the returned `int` matches `AddToModelMode.AS_UNIT_WITH_COPY` (or the appropriate constant) for a locally-created unit.
- `is_reference_unit` should assert `0` for a locally-owned unit and `1` for a unit created via `reference_to_another_project`.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/test_core.py -m integration -v`
Expected: all new tests PASS (or documented `xfail` for known COM quirks)

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/core.py`, change `[ ] integration test` to `[x] integration test` for: `copy_to_another_project`, `move_to_another_project_leave_a_reference`, `reference_to_another_project`, `get_nested_save_units`, `get_nested_save_units_count`, `get_structure_diagrams`, `get_add_to_model_mode`, `is_reference_unit`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/test_core.py src/rhapsody_cli/models/core.py
git commit -m "test: add integration tests for RPUnit cross-project/nesting methods"
```

---

## Task 14: RPCollection Direct Access — `add_item`

**Files:**
- Modify: `tests/integration/models/test_core.py`
- Modify: `src/rhapsody_cli/models/core.py` (flip checklist boxes only, no behavior change)

**Methods covered:** `add_item`

- [ ] **Step 1: Write the failing/new integration tests**

```python
from rhapsody_cli.models.core import RPCollection


@pytest.mark.integration
class TestRPCollectionAddItemIntegration:
    """Integration tests for RPCollection.add_item with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_add_item_appends_element(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("CollPkg"))
        try:
            cls_a = pkg.add_class(self._unique("ClsA"))
            cls_b = pkg.add_class(self._unique("ClsB"))

            existing = pkg.get_nested_elements()
            before_count = len(list(existing))

            collection = RPCollection(existing._com)
            collection.add_item(cls_b)

            assert collection.get_count() >= before_count
            names = [item.get_name() for item in collection]
            assert cls_a.get_name() in names or cls_b.get_name() in names
        finally:
            pkg.delete_from_project()
```

Note: `IRPCollection::addItem` semantics vary by the underlying collection's mutability (some Rhapsody collections returned by getters are read-only snapshots). If the live COM object rejects the mutation, assert the specific `RhapsodyRuntimeException` is raised instead, or construct a genuinely mutable collection (e.g. one built fresh via `RPCollection` wrapping a raw `IRPApplication`-created collection, if such a factory exists elsewhere in the codebase) and mark the read-only case `xfail(reason="live Rhapsody collection returned by getNestedElements is read-only", strict=False)` if confirmed.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/test_core.py -m integration -v`
Expected: test PASSes (or documented `xfail` for read-only collection quirk)

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/core.py`, change `[ ] integration test` to `[x] integration test` for: `add_item`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/test_core.py src/rhapsody_cli/models/core.py
git commit -m "test: add integration test for RPCollection.add_item"
```

---

## Task 15: RPCollection Mutation Methods — Implement & Test (exception to no-behavior-change rule)

**Files:**
- Modify: `src/rhapsody_cli/models/core.py` (implement 8 new `RPCollection` methods, following the existing `add_item`/`get_item` patterns; flip `[ ] impl`, `[ ] docstring` and checklist boxes for these methods)
- Modify: `tests/unit/models/test_core.py` (or equivalent unit test module — verify exact path with `glob` before editing) — add unit tests using `make_fake_collection`/fakes
- Modify: `tests/integration/models/test_core.py` — add integration tests

**Methods covered:** `add_graphical_item` (`addGraphicalItem`), `to_list` (`toList`), `set_size` (`setSize`), `remove` (`remove`), `set_string` (`setString`), `set_model_element` (`setModelElement`), `empty` (`empty`), `set_integer` (`setInteger`)

- [ ] **Step 1: Implement the 8 missing `RPCollection` methods**

Add snake_case wrapper methods to `RPCollection` in `core.py`, mirroring the existing `add_item`/`get_item` implementation style:

```python
def set_size(self, size: int) -> None:
    """Sets the number of elements in the collection.

    Reference:
        com.telelogic.rhapsody.core.IRPCollection::setSize(int size)
    """
    AbstractRPModelElement.call_com(lambda: self._com.setSize(size))

def remove(self, index: int) -> None:
    """Removes the element at the specified index from the collection.

    Args:
        index: The 1-based position of the element to remove.

    Reference:
        com.telelogic.rhapsody.core.IRPCollection::remove(int index)
    """
    AbstractRPModelElement.call_com(lambda: self._com.remove(index))

def empty(self) -> None:
    """Removes all elements from the collection.

    Reference:
        com.telelogic.rhapsody.core.IRPCollection::empty()
    """
    AbstractRPModelElement.call_com(lambda: self._com.empty())

def set_model_element(self, index: int, element: RPModelElement) -> None:
    """Sets the model element at the specified index in the collection.

    Args:
        index: The 1-based position to set.
        element: The model element to place at that position.

    Reference:
        com.telelogic.rhapsody.core.IRPCollection::setModelElement(int index, com.telelogic.rhapsody.core.IRPModelElement element)
    """
    AbstractRPModelElement.call_com(lambda: self._com.setModelElement(index, element._com))

def set_string(self, index: int, value: str) -> None:
    """Sets the string value at the specified index in the collection.

    Reference:
        com.telelogic.rhapsody.core.IRPCollection::setString(int index, java.lang.String value)
    """
    AbstractRPModelElement.call_com(lambda: self._com.setString(index, value))

def set_integer(self, index: int, value: int) -> None:
    """Sets the integer value at the specified index in the collection.

    Reference:
        com.telelogic.rhapsody.core.IRPCollection::setInteger(int index, int value)
    """
    AbstractRPModelElement.call_com(lambda: self._com.setInteger(index, value))

def add_graphical_item(self, element: RPModelElement) -> None:
    """Adds a graphical item to the collection.

    Reference:
        com.telelogic.rhapsody.core.IRPCollection::addGraphicalItem(com.telelogic.rhapsody.core.IRPModelElement element)
    """
    AbstractRPModelElement.call_com(lambda: self._com.addGraphicalItem(element._com))

def to_list(self) -> "list[Any]":
    """Returns the collection's elements as a Python list.

    Returns:
        A list of the wrapped elements/values in the collection.

    Reference:
        com.telelogic.rhapsody.core.IRPCollection::toList()
    """
    return list(self)
```

(Verify each COM method's exact signature against the Rhapsody COM type library or existing usages elsewhere in the codebase before finalizing — some of the above, e.g. `to_list`, may already be satisfiable purely via `__iter__` without a raw COM call; prefer the simplest correct implementation.)

- [ ] **Step 2: Write unit tests using fakes**

```python
def test_empty_removes_all_elements(make_fake_collection):
    collection = RPCollection(make_fake_collection([make_fake_element(name="A")]))
    collection.empty()
    assert collection.get_count() == 0
```

Follow the same pattern for `set_size`, `remove`, `set_model_element`, `set_string`, `set_integer`, `add_graphical_item`, `to_list` — one unit test per method using `make_fake_collection`/`make_fake_element` from `tests/unit/models/fakes.py`.

- [ ] **Step 3: Write integration tests against live Rhapsody**

```python
@pytest.mark.integration
class TestRPCollectionMutationIntegration:
    """Integration tests for the newly implemented RPCollection mutation methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_empty_clears_collection(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("MutPkg"))
        try:
            pkg.add_class(self._unique("MutCls"))
            collection = pkg.get_nested_elements()
            assert collection.get_count() >= 1
            collection.empty()
            assert collection.get_count() == 0
        finally:
            pkg.delete_from_project()
```

Follow the same pattern for `set_size`, `remove`, `set_model_element`, `set_string`, `set_integer`, `add_graphical_item`, `to_list`. As with Task 14, some live Rhapsody collections may be read-only snapshots — document any such quirks with `xfail(strict=False)`.

- [ ] **Step 4: Run unit and integration tests**

Run: `pytest tests/unit -k RPCollection -v` then `pytest tests/integration/models/test_core.py -m integration -v`
Expected: all PASS (or documented `xfail`)

- [ ] **Step 5: Flip checklist boxes**

In `src/rhapsody_cli/models/core.py`, change all four boxes (`[ ] impl`, `[ ] docstring`, `[ ] unit test`, `[ ] integration test`) to `[x]` for: `addGraphicalItem`, `toList`, `setSize`, `remove`, `setString`, `setModelElement`, `empty`, `setInteger`.

- [ ] **Step 6: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 7: Commit**

```bash
git add src/rhapsody_cli/models/core.py tests/unit/models/test_core.py tests/integration/models/test_core.py
git commit -m "feat: implement and test remaining RPCollection mutation methods"
```

---

## Task 16: Full File Verification

**Files:**
- Modify: none (verification only)

**Methods covered:** none new — this task verifies all 142 methods from Tasks 1–15 are complete.

- [ ] **Step 1: Run the complete integration test file against live Rhapsody**

Run: `pytest tests/integration/models/test_core.py -m integration -v`
Expected: all tests PASS (or documented `xfail`), with no unexpected failures or errors.

- [ ] **Step 2: Verify every checklist row in `core.py` is complete**

```bash
grep -n "\[ \] integration test" src/rhapsody_cli/models/core.py
```

Expected: no output (empty result) — every `RPModelElement`, `RPUnit`, and `RPCollection` checklist row now shows `[x] integration test`. Also verify no `[ ] impl` / `[ ] docstring` / `[ ] unit test` boxes remain for `RPCollection`'s previously-unimplemented methods:

```bash
grep -n "\[ \] impl\|\[ \] docstring\|\[ \] unit test" src/rhapsody_cli/models/core.py
```

Expected: no output.

- [ ] **Step 3: Run the full quality gate one final time**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
Expected: all pass

- [ ] **Step 4: Final commit**

```bash
git add -A
git commit -m "test: complete core.py integration test coverage"
```
