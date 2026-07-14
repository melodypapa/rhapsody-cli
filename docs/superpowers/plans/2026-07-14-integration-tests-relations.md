# Relations Subpackage Integration Tests Completion Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add integration tests for all remaining untested methods of `RPAssociationRole`, `RPDependency`, `RPGeneralization` (complete the partial coverage), `RPHyperLink`, `RPInstance`, `RPPort`, `RPRelation`. Flip in-source `[ ] integration test` markers to `[x]` as work completes.

**Architecture:** Extends `tests/integration/models/elements/relations/test_model_generalization.py`; creates new test files for the other 6 classes.

**Tech Stack:** pytest, pywin32 (win32com), live Rhapsody COM API, `uuid.uuid4().hex[:8]`.

## Global Constraints

- Windows-only runtime (requires Windows + a running Rhapsody instance)
- All test classes use `@pytest.mark.integration`
- All tests consume the `test_project: RPProject` fixture
- Use `_unique(prefix)` with `uuid.uuid4().hex[:8]`
- Always `try/finally` cleanup via `element.delete_from_project()`
- Assert both `isinstance()` and read-back values
- Flip `[ ] integration test` to `[x]` per task in the relevant `model_*.py` file
- Quality gate after each task: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
- Import via subpackage `__init__.py` re-exports, e.g. `from rhapsody_cli.models.elements.relations import RPPort`
- Generic element creation uses the established `owner.add_new_aggr("<MetaType>", name)` factory pattern (already used for `RPComment`, `RPConstraint`, `RPRequirement` in `tests/integration/models/elements/common/test_model_misc.py` and `tests/integration/models/elements/requirements/test_model_requirements.py`), or a dedicated convenience method where one exists (`RPClassifier.add_port`, `RPPackage.add_association`).
- Where live COM behavior for a method is uncertain ahead of running against real Rhapsody (e.g. methods requiring complex pre-wired part/type/use-case context), mark the test `@pytest.mark.xfail(reason="...", strict=False)` following the precedent in `tests/integration/models/elements/classifiers/test_model_class.py::test_abstract_roundtrip`. Implementers should attempt the real assertion first (TDD) and only fall back to `xfail` if live Rhapsody genuinely does not support the scenario as designed.

---

## Task 1: RPGeneralization — complete partial coverage

**Files:**
- Modify: `tests/integration/models/elements/relations/test_model_generalization.py`
- Modify: `src/rhapsody_cli/models/elements/relations/model_generalization.py` (flip checklist boxes only)

**Methods covered:** `get_derived_class`, `get_extension_point`, `get_is_virtual`, `set_is_virtual`, `get_visibility`, `set_visibility`, `set_base_class`, `set_derived_class`

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_generalization_derived_class_and_flags(self, test_project: RPProject) -> None:
    pkg_name = self._unique("GenPkg")
    parent_name = self._unique("Parent")
    child_name = self._unique("Child")
    pkg = self._create_package(test_project, pkg_name)
    parent = pkg.add_class(parent_name)
    child = pkg.add_class(child_name)
    try:
        child.add_generalization(parent)
        gen = child.find_generalization(parent_name)
        assert gen is not None

        # get_derived_class
        assert gen.get_derived_class() == child

        # get_is_virtual / set_is_virtual roundtrip
        assert gen.get_is_virtual() == 0
        gen.set_is_virtual(1)
        assert gen.get_is_virtual() == 1
        gen.set_is_virtual(0)
        assert gen.get_is_virtual() == 0

        # get_visibility / set_visibility roundtrip
        gen.set_visibility(2)
        assert gen.get_visibility() == 2
    finally:
        child.delete_from_project()
        parent.delete_from_project()
```

For remaining methods, follow the same pattern:
- `set_base_class` / `set_derived_class`: create a third class `other`, call `gen.set_base_class(other)` then assert `gen.get_base_class() == other`; likewise for `set_derived_class`.
- `get_extension_point`: this is a use-case-extension-only concept. Write a test that calls `gen.get_extension_point()` on the class-to-class generalization created above and asserts it does not raise (returns an empty/None-like wrapper). Mark `@pytest.mark.xfail(reason="getExtensionPoint is only meaningful for use-case Extend relationships; class generalizations return an unwrapped/empty COM object which may not satisfy isinstance checks. TODO: revisit with a real use-case Extend fixture.", strict=False)`.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/relations/test_model_generalization.py -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/relations/model_generalization.py`, flip `get_derived_class`, `get_extension_point`, `get_is_virtual`, `set_is_virtual`, `get_visibility`, `set_visibility`, `set_base_class`, `set_derived_class` integration-test boxes to `[x]`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/relations/test_model_generalization.py src/rhapsody_cli/models/elements/relations/model_generalization.py
git commit -m "test: complete integration tests for RPGeneralization"
```

---

## Task 2: RPDependency — full coverage

**Files:**
- Create: `tests/integration/models/elements/relations/test_model_dependency.py`
- Modify: `src/rhapsody_cli/models/elements/relations/model_dependency.py` (flip checklist boxes only)

**Methods covered:** `get_dependent`, `get_depends_on`, `is_need_to_migrate`, `set_dependent`, `set_depends_on`, `set_link_type`, `set_owner_without_changing_dependent`

- [ ] **Step 1: Write the failing/new integration tests**

```python
import uuid

import pytest

from rhapsody_cli.models.elements.containment import RPPackage, RPProject
from rhapsody_cli.models.elements.relations import RPDependency


@pytest.mark.integration
class TestRPDependencyIntegration:
    """Integration tests for RPDependency with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_dependency_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("DepPkg")
        dependent_name = self._unique("Dependent")
        depends_on_name = self._unique("DependsOn")
        dep_name = self._unique("Dep")
        pkg = self._create_package(test_project, pkg_name)
        dependent = pkg.add_class(dependent_name)
        depends_on = pkg.add_class(depends_on_name)
        dependency = pkg.add_new_aggr("Dependency", dep_name)
        try:
            assert isinstance(dependency, RPDependency)
            assert dependency.get_meta_class() == "Dependency"

            dependency.set_dependent(dependent)
            assert dependency.get_dependent() == dependent

            dependency.set_depends_on(depends_on)
            assert dependency.get_depends_on() == depends_on

            dependency.set_link_type("Usage")

            assert isinstance(dependency.is_need_to_migrate(), int)

            dependency.set_owner_without_changing_dependent(pkg)
            assert dependency.get_owner() == pkg
            assert dependency.get_dependent() == dependent
        finally:
            dependency.delete_from_project()
            dependent.delete_from_project()
            depends_on.delete_from_project()
```

For remaining methods: all 7 methods are exercised directly above in one roundtrip test; no additional test needed unless splitting for clarity is preferred.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/relations/test_model_dependency.py -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/relations/model_dependency.py`, flip `getDependent`, `getDependsOn`, `isNeedToMigrate`, `setDependent`, `setDependsOn`, `setLinkType`, `setOwnerWithoutChangingDependent` integration-test boxes to `[x]`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/relations/test_model_dependency.py src/rhapsody_cli/models/elements/relations/model_dependency.py
git commit -m "test: add integration tests for RPDependency"
```

---

## Task 3: RPHyperLink — full coverage

**Files:**
- Create: `tests/integration/models/elements/relations/test_model_hyperlink.py`
- Modify: `src/rhapsody_cli/models/elements/relations/model_hyperlink.py` (flip checklist boxes only)

**Methods covered:** `get_target`, `get_url`, `set_display_option`, `set_target`, `set_url`

- [ ] **Step 1: Write the failing/new integration tests**

```python
import uuid

import pytest

from rhapsody_cli.models.elements.containment import RPPackage, RPProject
from rhapsody_cli.models.elements.relations import RPHyperLink


@pytest.mark.integration
class TestRPHyperLinkIntegration:
    """Integration tests for RPHyperLink with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_hyperlink_target_and_url_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("LinkPkg")
        target_name = self._unique("Target")
        link_name = self._unique("Link")
        pkg = self._create_package(test_project, pkg_name)
        target = pkg.add_class(target_name)
        hyperlink = pkg.add_new_aggr("HyperLink", link_name)
        try:
            assert isinstance(hyperlink, RPHyperLink)
            assert hyperlink.get_meta_class() == "HyperLink"

            hyperlink.set_target(target)
            assert hyperlink.get_target() == target

            hyperlink.set_url("https://example.com/docs")
            assert hyperlink.get_url() == "https://example.com/docs"

            hyperlink.set_display_option(1)
        finally:
            hyperlink.delete_from_project()
            target.delete_from_project()
```

For remaining methods: all 5 methods are exercised directly above in one roundtrip test; `set_display_option` has no dedicated getter so is only smoke-tested (asserts no exception raised).

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/relations/test_model_hyperlink.py -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/relations/model_hyperlink.py`, flip `getTarget`, `getURL`, `setDisplayOption`, `setTarget`, `setURL` integration-test boxes to `[x]`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/relations/test_model_hyperlink.py src/rhapsody_cli/models/elements/relations/model_hyperlink.py
git commit -m "test: add integration tests for RPHyperLink"
```

---

## Task 4: RPAssociationRole — full coverage

**Files:**
- Create: `tests/integration/models/elements/relations/test_model_association_role.py`
- Modify: `src/rhapsody_cli/models/elements/relations/model_association_role.py` (flip checklist boxes only)

**Methods covered:** `get_classifier_roles`, `get_formal_relations`, `get_role_type`

- [ ] **Step 1: Write the failing/new integration tests**

```python
import uuid

import pytest

from rhapsody_cli.models.core import RPCollection
from rhapsody_cli.models.elements.containment import RPPackage, RPProject
from rhapsody_cli.models.elements.relations import RPAssociationRole


@pytest.mark.integration
class TestRPAssociationRoleIntegration:
    """Integration tests for RPAssociationRole with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_association_role_basic_accessors(self, test_project: RPProject) -> None:
        pkg_name = self._unique("RolePkg")
        role_name = self._unique("Role")
        pkg = self._create_package(test_project, pkg_name)
        role = pkg.add_new_aggr("AssociationRole", role_name)
        try:
            assert isinstance(role, RPAssociationRole)
            assert role.get_meta_class() == "AssociationRole"

            classifier_roles = role.get_classifier_roles()
            assert isinstance(classifier_roles, RPCollection)

            formal_relations = role.get_formal_relations()
            assert isinstance(formal_relations, RPCollection)

            role_type = role.get_role_type()
            assert role_type is not None
        finally:
            role.delete_from_project()
```

For remaining methods: all 3 methods are exercised directly above; since a standalone `AssociationRole` typically has empty classifier roles/formal relations/role type when not wired into an actual association-role link context, assertions focus on type/no-exception rather than specific content. If live Rhapsody rejects `addNewAggr("AssociationRole", ...)` as a standalone element, fall back to creating it via a sequence-diagram/collaboration context and mark unreachable parts `xfail` with a clear reason.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/relations/test_model_association_role.py -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/relations/model_association_role.py`, flip `getClassifierRoles`, `getFormalRelations`, `getRoleType` integration-test boxes to `[x]`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/relations/test_model_association_role.py src/rhapsody_cli/models/elements/relations/model_association_role.py
git commit -m "test: add integration tests for RPAssociationRole"
```

---

## Task 5: RPInstance — lifecycle, nesting, and links

**Files:**
- Create: `tests/integration/models/elements/relations/test_model_instance.py`
- Modify: `src/rhapsody_cli/models/elements/relations/model_instance.py` (flip checklist boxes only, this task's subset)

**Methods covered:** `get_all_nested_elements`, `get_in_links`, `get_out_links`, `set_explicit`, `set_implicit`, `get_attribute_value`, `set_attribute_value`

- [ ] **Step 1: Write the failing/new integration tests**

```python
import uuid

import pytest

from rhapsody_cli.models.core import RPCollection
from rhapsody_cli.models.elements.containment import RPPackage, RPProject
from rhapsody_cli.models.elements.relations import RPInstance


@pytest.mark.integration
class TestRPInstanceIntegration:
    """Integration tests for RPInstance with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_instance_lifecycle_and_nesting(self, test_project: RPProject) -> None:
        pkg_name = self._unique("InstPkg")
        inst_name = self._unique("Inst")
        pkg = self._create_package(test_project, pkg_name)
        instance = pkg.add_new_aggr("Instance", inst_name)
        try:
            assert isinstance(instance, RPInstance)
            assert instance.get_meta_class() == "Instance"

            nested = instance.get_all_nested_elements()
            assert isinstance(nested, RPCollection)

            in_links = instance.get_in_links()
            assert isinstance(in_links, RPCollection)

            out_links = instance.get_out_links()
            assert isinstance(out_links, RPCollection)

            instance.set_explicit()
            instance.set_implicit()
        finally:
            instance.delete_from_project()
```

For remaining methods:
- `get_attribute_value` / `set_attribute_value`: create a class with an attribute (`attr_class = pkg.add_class(...)`, `attr_class.add_attribute("myAttr")`), then create the instance as a part typed by that class if a typing mechanism is available; if the wrapper API has no `set_type` for `RPInstance` in this subpackage, mark this test `@pytest.mark.xfail(reason="RPInstance.set_attribute_value/get_attribute_value require the instance to be typed by a classifier with a matching attribute; no wrapped set_type API exists to wire this in isolation. TODO: revisit once part/type wiring is exposed.", strict=False)` and still write the test body attempting the real call so it can start passing automatically once support exists.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/relations/test_model_instance.py -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/relations/model_instance.py`, flip integration-test boxes for `get_all_nested_elements`, `get_in_links`, `get_out_links`, `set_explicit`, `set_implicit`, `get_attribute_value`, `set_attribute_value` to `[x]` (unless left `xfail`, in which case leave unflipped and note in a follow-up).

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/relations/test_model_instance.py src/rhapsody_cli/models/elements/relations/model_instance.py
git commit -m "test: add integration tests for RPInstance lifecycle and nesting"
```

---

## Task 6: RPInstance — instantiation and initializer arguments

**Files:**
- Modify: `tests/integration/models/elements/relations/test_model_instance.py`
- Modify: `src/rhapsody_cli/models/elements/relations/model_instance.py` (flip checklist boxes only, this task's subset)

**Methods covered:** `add_relation_to_the_whole`, `get_instantiated_by`, `set_instantiated_by`, `get_list_of_initializer_arguments`, `set_initializer_argument_value`, `update_contained_diagrams_on_server`

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_instance_instantiated_by_roundtrip(self, test_project: RPProject) -> None:
    pkg_name = self._unique("InstOpPkg")
    class_name = self._unique("OwnerClass")
    op_name = self._unique("factoryOp")
    inst_name = self._unique("Inst")
    pkg = self._create_package(test_project, pkg_name)
    owner_class = pkg.add_class(class_name)
    operation = owner_class.add_operation(op_name)
    instance = pkg.add_new_aggr("Instance", inst_name)
    try:
        instance.set_instantiated_by(operation)
        assert instance.get_instantiated_by() == operation

        result = instance.update_contained_diagrams_on_server(0)
        assert isinstance(result, int)
    finally:
        instance.delete_from_project()
        owner_class.delete_from_project()
```

For remaining methods:
- `add_relation_to_the_whole`: requires an existing whole/part composite structure with a named relation role; write the test attempting `instance.add_relation_to_the_whole(rel_name)` against a class-composed part and assert the result `isinstance(_, RPRelation)`. Mark `@pytest.mark.xfail(reason="addRelationToTheWhole requires the instance to already be a part in a composite structure with a defined whole-part relation; minimal fixture may not satisfy Rhapsody's internal precondition. TODO: revisit with a full composite-structure fixture.", strict=False)` if it does not pass on first live run.
- `get_list_of_initializer_arguments` / `set_initializer_argument_value`: requires a constructor with parameters on the instance's type. Create `owner_class.add_constructor("int arg1")`, instantiate accordingly, then call `instance.get_list_of_initializer_arguments()` (assert `RPCollection`) and `instance.set_initializer_argument_value("arg1", "5")`. Mark `xfail` with a clear reason if live Rhapsody requires the instance to be explicitly typed by `owner_class` first and no such wiring API exists in this subpackage.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/relations/test_model_instance.py -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/relations/model_instance.py`, flip integration-test boxes for `add_relation_to_the_whole`, `get_instantiated_by`, `set_instantiated_by`, `get_list_of_initializer_arguments`, `set_initializer_argument_value`, `update_contained_diagrams_on_server` to `[x]` (unless left `xfail`).

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/relations/test_model_instance.py src/rhapsody_cli/models/elements/relations/model_instance.py
git commit -m "test: add integration tests for RPInstance instantiation"
```

---

## Task 7: RPPort — behavioral, reversed, and contract

**Files:**
- Create: `tests/integration/models/elements/relations/test_model_port.py`
- Modify: `src/rhapsody_cli/models/elements/relations/model_port.py` (flip checklist boxes only, this task's subset)

**Methods covered:** `get_is_behavioral`, `set_is_behavioral`, `get_is_reversed`, `set_is_reversed`, `get_port_contract`, `set_port_contract`

- [ ] **Step 1: Write the failing/new integration tests**

```python
import uuid

import pytest

from rhapsody_cli.models.elements.containment import RPPackage, RPProject
from rhapsody_cli.models.elements.relations import RPPort


@pytest.mark.integration
class TestRPPortIntegration:
    """Integration tests for RPPort with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_port_behavioral_reversed_and_contract(self, test_project: RPProject) -> None:
        pkg_name = self._unique("PortPkg")
        class_name = self._unique("PortOwner")
        contract_name = self._unique("Contract")
        port_name = self._unique("port")
        pkg = self._create_package(test_project, pkg_name)
        owner_class = pkg.add_class(class_name)
        contract_class = pkg.add_class(contract_name)
        port = owner_class.add_port(port_name)
        try:
            assert isinstance(port, RPPort)
            assert port.get_meta_class() == "Port"

            assert port.get_is_behavioral() == 0
            port.set_is_behavioral(1)
            assert port.get_is_behavioral() == 1

            assert port.get_is_reversed() == 0
            port.set_is_reversed(1)
            assert port.get_is_reversed() == 1

            port.set_port_contract(contract_class)
            assert port.get_port_contract() == contract_class
        finally:
            port.delete_from_project()
            owner_class.delete_from_project()
            contract_class.delete_from_project()
```

For remaining methods: all 6 methods are exercised directly above in one roundtrip test.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/relations/test_model_port.py -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/relations/model_port.py`, flip integration-test boxes for `get_is_behavioral`, `set_is_behavioral`, `get_is_reversed`, `set_is_reversed`, `get_port_contract`, `set_port_contract` to `[x]`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/relations/test_model_port.py src/rhapsody_cli/models/elements/relations/model_port.py
git commit -m "test: add integration tests for RPPort behavioral/reversed/contract"
```

---

## Task 8: RPPort — provided/required interfaces and deprecated contract aliases

**Files:**
- Modify: `tests/integration/models/elements/relations/test_model_port.py`
- Modify: `src/rhapsody_cli/models/elements/relations/model_port.py` (flip checklist boxes only, this task's subset)

**Methods covered:** `get_provided_interfaces`, `add_provided_interface`, `remove_provided_interface`, `get_required_interfaces`, `add_required_interface`, `remove_required_interface`, `get_contract`, `set_contract`

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_port_provided_and_required_interfaces(self, test_project: RPProject) -> None:
    pkg_name = self._unique("IfacePkg")
    class_name = self._unique("IfaceOwner")
    provided_name = self._unique("ProvidedIface")
    required_name = self._unique("RequiredIface")
    port_name = self._unique("ifacePort")
    pkg = self._create_package(test_project, pkg_name)
    owner_class = pkg.add_class(class_name)
    provided_iface = pkg.add_class(provided_name)
    required_iface = pkg.add_class(required_name)
    port = owner_class.add_port(port_name)
    try:
        port.add_provided_interface(provided_iface)
        assert provided_iface in list(port.get_provided_interfaces())
        port.remove_provided_interface(provided_iface)
        assert provided_iface not in list(port.get_provided_interfaces())

        port.add_required_interface(required_iface)
        assert required_iface in list(port.get_required_interfaces())
        port.remove_required_interface(required_iface)
        assert required_iface not in list(port.get_required_interfaces())
    finally:
        port.delete_from_project()
        owner_class.delete_from_project()
        provided_iface.delete_from_project()
        required_iface.delete_from_project()
```

For remaining methods:
- `get_contract` / `set_contract` (deprecated aliases of `get_port_contract`/`set_port_contract`): reuse the contract-class setup pattern from Task 7 — `port.set_contract(contract_class)`, then assert `port.get_contract() == contract_class`.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/relations/test_model_port.py -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/relations/model_port.py`, flip integration-test boxes for `get_provided_interfaces`, `add_provided_interface`, `remove_provided_interface`, `get_required_interfaces`, `add_required_interface`, `remove_required_interface`, `get_contract` (deprecated), `set_contract` (deprecated) to `[x]`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/relations/test_model_port.py src/rhapsody_cli/models/elements/relations/model_port.py
git commit -m "test: add integration tests for RPPort provided/required interfaces"
```

---

## Task 9: RPRelation — core identity and type/label

**Files:**
- Create: `tests/integration/models/elements/relations/test_model_relation.py`
- Modify: `src/rhapsody_cli/models/elements/relations/model_relation.py` (flip checklist boxes only, this task's subset)

**Methods covered:** `get_of_class`, `set_of_class`, `get_other_class`, `set_other_class`, `get_relation_type`, `set_relation_type`, `get_relation_label`, `set_relation_label`

- [ ] **Step 1: Write the failing/new integration tests**

```python
import uuid

import pytest

from rhapsody_cli.models.elements.containment import RPPackage, RPProject
from rhapsody_cli.models.elements.relations import RPRelation


@pytest.mark.integration
class TestRPRelationIntegration:
    """Integration tests for RPRelation with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_relation_of_class_other_class_and_type(self, test_project: RPProject) -> None:
        pkg_name = self._unique("RelPkg")
        class_a_name = self._unique("ClassA")
        class_b_name = self._unique("ClassB")
        assoc_name = self._unique("Assoc")
        pkg = self._create_package(test_project, pkg_name)
        class_a = pkg.add_class(class_a_name)
        class_b = pkg.add_class(class_b_name)
        relation = pkg.add_association(assoc_name)
        try:
            assert isinstance(relation, RPRelation)
            assert relation.get_meta_class() == "Association"

            relation.set_of_class(class_a)
            assert relation.get_of_class() == class_a

            relation.set_other_class(class_b)
            assert relation.get_other_class() == class_b

            relation.set_relation_type("Association")
            assert relation.get_relation_type() == "Association"

            relation.set_relation_label(self._unique("Label"))
            assert relation.get_relation_label() != ""
        finally:
            pkg.delete_association(relation)
            class_a.delete_from_project()
            class_b.delete_from_project()
```

For remaining methods: all 8 methods are exercised directly above (or via trivial variants of the same roundtrip pattern) in one test.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/relations/test_model_relation.py -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/relations/model_relation.py`, flip integration-test boxes for `get_of_class`, `set_of_class`, `get_other_class`, `set_other_class`, `get_relation_type`, `set_relation_type`, `get_relation_label`, `set_relation_label` to `[x]`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/relations/test_model_relation.py src/rhapsody_cli/models/elements/relations/model_relation.py
git commit -m "test: add integration tests for RPRelation core identity"
```

---

## Task 10: RPRelation — link naming, visibility, multiplicity, navigability, inverse

**Files:**
- Modify: `tests/integration/models/elements/relations/test_model_relation.py`
- Modify: `src/rhapsody_cli/models/elements/relations/model_relation.py` (flip checklist boxes only, this task's subset)

**Methods covered:** `get_relation_link_name`, `set_relation_link_name`, `get_relation_role_name`, `set_relation_role_name`, `get_visibility`, `get_multiplicity`, `set_multiplicity`, `get_is_navigable`, `set_is_navigable`, `get_is_symmetric`, `is_typeless_object`

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_relation_naming_visibility_and_navigability(self, test_project: RPProject) -> None:
    pkg_name = self._unique("RelPkg2")
    class_a_name = self._unique("ClassA2")
    class_b_name = self._unique("ClassB2")
    assoc_name = self._unique("Assoc2")
    pkg = self._create_package(test_project, pkg_name)
    class_a = pkg.add_class(class_a_name)
    class_b = pkg.add_class(class_b_name)
    relation = pkg.add_association(assoc_name)
    try:
        relation.set_of_class(class_a)
        relation.set_other_class(class_b)

        relation.set_relation_link_name(self._unique("LinkName"))
        assert relation.get_relation_link_name() != ""

        relation.set_relation_role_name(self._unique("RoleName"))
        assert relation.get_relation_role_name() != ""

        assert isinstance(relation.get_visibility(), str)

        relation.set_multiplicity("0..*")
        assert relation.get_multiplicity() == "0..*"

        relation.set_is_navigable(True)
        assert relation.get_is_navigable() is True

        assert isinstance(relation.get_is_symmetric(), bool)
        assert isinstance(relation.is_typeless_object(), bool)
    finally:
        pkg.delete_association(relation)
        class_a.delete_from_project()
        class_b.delete_from_project()
```

For remaining methods: covered directly above except `set_inverse`/`get_inverse`/`make_unidirect`, which belong to Task 11.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/relations/test_model_relation.py -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/relations/model_relation.py`, flip integration-test boxes for `get_relation_link_name`, `set_relation_link_name`, `get_relation_role_name`, `set_relation_role_name`, `get_visibility`, `get_multiplicity`, `set_multiplicity`, `get_is_navigable`, `set_is_navigable`, `get_is_symmetric`, `is_typeless_object` to `[x]`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/relations/test_model_relation.py src/rhapsody_cli/models/elements/relations/model_relation.py
git commit -m "test: add integration tests for RPRelation naming and navigability"
```

---

## Task 11: RPRelation — qualifiers, association class, inverse

**Files:**
- Modify: `tests/integration/models/elements/relations/test_model_relation.py`
- Modify: `src/rhapsody_cli/models/elements/relations/model_relation.py` (flip checklist boxes only, this task's subset)

**Methods covered:** `add_qualifier`, `remove_qualifier`, `get_qualifier`, `get_qualifiers`, `set_qualifier`, `get_qualifier_type`, `set_qualifier_type`, `get_association_class`, `get_object_as_object_type`, `get_inverse`, `set_inverse`, `make_unidirect`

- [ ] **Step 1: Write the failing/new integration tests**

```python
def test_relation_qualifiers_and_inverse(self, test_project: RPProject) -> None:
    pkg_name = self._unique("RelPkg3")
    class_a_name = self._unique("ClassA3")
    class_b_name = self._unique("ClassB3")
    qualifier_type_name = self._unique("QualType")
    assoc_name = self._unique("Assoc3")
    pkg = self._create_package(test_project, pkg_name)
    class_a = pkg.add_class(class_a_name)
    class_b = pkg.add_class(class_b_name)
    qualifier_type = pkg.add_class(qualifier_type_name)
    relation = pkg.add_association(assoc_name)
    try:
        relation.set_of_class(class_a)
        relation.set_other_class(class_b)

        relation.set_qualifier(self._unique("Qual"))
        assert relation.get_qualifier() != ""

        relation.set_qualifier_type(qualifier_type)
        assert relation.get_qualifier_type() == qualifier_type

        qualifiers = relation.get_qualifiers()
        assert qualifiers is not None

        assoc_class = relation.get_association_class()
        assert assoc_class is not None

        object_type = relation.get_object_as_object_type()
        assert object_type is not None

        relation.set_inverse(self._unique("InverseRole"), "Association")
        inverse = relation.get_inverse()
        assert inverse is not None
    finally:
        pkg.delete_association(relation)
        class_a.delete_from_project()
        class_b.delete_from_project()
        qualifier_type.delete_from_project()
```

For remaining methods:
- `add_qualifier` / `remove_qualifier`: create a small class to use as a qualifier element (`qualifier_elem = pkg.add_class(...)`), call `relation.add_qualifier(qualifier_elem)`, assert `qualifier_elem in list(relation.get_qualifiers())`, then `relation.remove_qualifier(qualifier_elem)` and assert it is no longer present.
- `make_unidirect`: call `relation.make_unidirect()` on a relation created with `set_inverse` already applied, and assert no exception is raised (Rhapsody does not expose a direct boolean getter for "unidirectional" on `IRPRelation` beyond `get_is_navigable`, so this is a smoke test).

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/relations/test_model_relation.py -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/relations/model_relation.py`, flip integration-test boxes for `add_qualifier`, `remove_qualifier`, `get_qualifier`, `get_qualifiers`, `set_qualifier`, `get_qualifier_type`, `set_qualifier_type`, `get_association_class`, `get_object_as_object_type`, `get_inverse`, `set_inverse`, `make_unidirect` to `[x]`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/relations/test_model_relation.py src/rhapsody_cli/models/elements/relations/model_relation.py
git commit -m "test: add integration tests for RPRelation qualifiers and inverse"
```

---

## Task 12: Full Subpackage Verification

**Files:** None modified (verification only).

- [ ] **Step 1: Run the entire relations integration test directory**

Run: `pytest tests/integration/models/elements/relations/ -m integration -v`

- [ ] **Step 2: Confirm no `[ ]` integration-test checklist rows remain unaccounted for**

Run: `grep -rn "\[ \] integration test" src/rhapsody_cli/models/elements/relations/`

Every remaining unchecked row (if any) must correspond to a documented `xfail` test with a clear reason, not a silent gap. Reconcile any discrepancy before proceeding.

- [ ] **Step 3: Run the full quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 4: Final commit (if any cleanup remains)**

```bash
git add -A
git commit -m "test: finalize relations subpackage integration test coverage"
```
