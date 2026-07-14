# Common Subpackage Integration Tests Completion Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add integration tests for all remaining untested methods of `RPEnumerationLiteral`, `RPComment`, `RPConstraint`, `RPClassifierRole`, `RPSysMLPort`, `RPType`. Flip in-source `[ ] integration test` markers to `[x]` as work completes.

**Architecture:** Extends `tests/integration/models/elements/common/test_model_misc.py`; creates new `tests/integration/models/elements/common/test_model_other_model.py` for the `model_other_model.py` classes.

**Tech Stack:** pytest, pywin32 (win32com), live Rhapsody COM API, `uuid.uuid4().hex[:8]`.

## Scope Summary

| Class | File | Untested methods | Creation path |
|---|---|---|---|
| `RPEnumerationLiteral` | `model_misc.py` | `get_value`, `set_value` | `RPType.add_enumeration_literal(name)` |
| `RPComment` | `model_misc.py` | none (only inherited methods; creation already covered) | `pkg.add_new_aggr("Comment", name)` |
| `RPConstraint` | `model_misc.py` | `get_constraints_by_me` | `pkg.add_new_aggr("Constraint", name)` |
| `RPClassifierRole` | `model_other_model.py` | `get_formal_classifier`, `get_formal_instance`, `get_referenced_sequence_diagram`, `get_referencing_classifier_roles_recursively`, `get_role_type`, `set_formal_classifier`, `set_formal_instance`, `set_referenced_sequence_diagram` | `pkg.add_new_aggr("Collaboration", name)` → `collab.add_classifier_role(name)` |
| `RPSysMLPort` | `model_other_model.py` | `add_link`, `get_is_reversed`, `get_port_direction`, `get_type`, `set_is_reversed`, `set_port_direction`, `set_type` | `test_class.add_new_aggr("SysMLPort", name)` (may require SysML profile; guard with `xfail` if unavailable) |
| `RPType` | `model_other_model.py` | `add_enumeration_literal`, `delete_enumeration_literal`, `get_declaration`, `get_enumeration_literals`, `get_is_predefined`, `get_is_typedef`, `get_is_typedef_constant`, `get_is_typedef_ordered`, `get_is_typedef_reference`, `get_kind`, `get_typedef_base_type`, `get_typedef_multiplicity`, `is_array`, `is_enum`, `is_equal_to`, `is_implicit`, `is_kind_enumeration`, `is_kind_language`, `is_kind_struct`, `is_kind_typedef`, `is_kind_union`, `is_pointer`, `is_pointer_to_pointer`, `is_reference`, `is_reference_to_pointer`, `is_struct`, `is_template`, `is_union`, `set_declaration`, `set_is_typedef_constant`, `set_is_typedef_ordered`, `set_is_typedef_reference`, `set_kind`, `set_typedef_base_type`, `set_typedef_multiplicity` | `pkg.add_class(name).add_type(name)` |

`RPComment` has no untested method-level checklist rows (only the `IRPModelElement` inherited items already covered by `RPModelElement`'s own checklist) — no new task is needed for it beyond what `test_model_misc.py` already covers.

## Global Constraints

- Windows-only runtime (requires Windows + a running Rhapsody instance)
- All test classes use `@pytest.mark.integration`
- All tests consume the `test_project: RPProject` fixture
- Use `_unique(prefix)` with `uuid.uuid4().hex[:8]`
- Always `try/finally` cleanup via `element.delete_from_project()`
- Assert both `isinstance()` and read-back values
- Flip `[ ] integration test` to `[x]` per task in the relevant `model_*.py` file
- Quality gate after each task: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit` (live run needs attached Rhapsody)
- Import via subpackage `__init__.py` re-exports (`from rhapsody_cli.models.elements.common import ...`)
- If a COM API turns out to require model configuration not present in the plain `TestProject` fixture (e.g. `RPSysMLPort` needing a SysML profile), guard the test with `@pytest.mark.xfail(reason="...", strict=False)` rather than skipping outright — follow the precedent in `tests/integration/models/elements/classifiers/test_model_class.py::test_abstract_roundtrip`

---

### Task 1: RPType — kind, declaration, typedef, and predicate methods

**Files:**
- Create: `tests/integration/models/elements/common/test_model_other_model.py`
- Modify: `src/rhapsody_cli/models/elements/common/model_other_model.py` (flip checklist boxes only)

**Methods covered:** `get_declaration`, `set_declaration`, `get_kind`, `set_kind`, `get_is_predefined`, `get_is_typedef`, `get_is_typedef_constant`, `set_is_typedef_constant`, `get_is_typedef_ordered`, `set_is_typedef_ordered`, `get_is_typedef_reference`, `set_is_typedef_reference`, `get_typedef_base_type`, `set_typedef_base_type`, `get_typedef_multiplicity`, `set_typedef_multiplicity`, `is_array`, `is_enum`, `is_equal_to`, `is_implicit`, `is_kind_enumeration`, `is_kind_language`, `is_kind_struct`, `is_kind_typedef`, `is_kind_union`, `is_pointer`, `is_pointer_to_pointer`, `is_reference`, `is_reference_to_pointer`, `is_struct`, `is_template`, `is_union`

- [ ] **Step 1: Write the failing/new integration tests**

```python
"""Integration tests for RPClassifierRole, RPSysMLPort, and RPType with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.elements.classifiers import RPClass
from rhapsody_cli.models.elements.common import RPType
from rhapsody_cli.models.elements.containment import RPPackage, RPProject


@pytest.mark.integration
class TestRPTypeIntegration:
    """Integration tests for RPType with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def _create_type(self, project: RPProject, pkg_prefix: str, class_prefix: str, type_prefix: str) -> tuple[RPPackage, RPClass, RPType]:
        pkg = project.add_package(self._unique(pkg_prefix))
        test_class = pkg.add_class(self._unique(class_prefix))
        test_type = test_class.add_type(self._unique(type_prefix))
        assert isinstance(test_type, RPType)
        return pkg, test_class, test_type

    def test_declaration_roundtrip(self, test_project: RPProject) -> None:
        _pkg, test_class, test_type = self._create_type(test_project, "TypeDeclPkg", "TypeDeclCls", "MyType")
        try:
            test_type.set_declaration("int")
            assert test_type.get_declaration() == "int"
        finally:
            test_type.delete_from_project()
            test_class.delete_from_project()

    def test_kind_roundtrip_and_predicates(self, test_project: RPProject) -> None:
        _pkg, test_class, test_type = self._create_type(test_project, "TypeKindPkg", "TypeKindCls", "MyType")
        try:
            assert test_type.get_is_predefined() in (0, 1)

            test_type.set_kind("Enumeration")
            assert test_type.get_kind() == "Enumeration"
            assert test_type.is_kind_enumeration() == 1
            assert test_type.is_kind_language() == 0
            assert test_type.is_kind_struct() == 0
            assert test_type.is_kind_typedef() == 0
            assert test_type.is_kind_union() == 0

            for predicate in (
                test_type.is_array,
                test_type.is_equal_to,
                test_type.is_implicit,
                test_type.is_pointer,
                test_type.is_pointer_to_pointer,
                test_type.is_reference,
                test_type.is_reference_to_pointer,
                test_type.is_struct,
                test_type.is_template,
                test_type.is_union,
                test_type.is_enum,
            ):
                assert predicate() in (0, 1)
        finally:
            test_type.delete_from_project()
            test_class.delete_from_project()

    def test_typedef_roundtrip(self, test_project: RPProject) -> None:
        pkg, test_class, test_type = self._create_type(test_project, "TypedefPkg", "TypedefCls", "MyTypedef")
        base_class = pkg.add_class(self._unique("BaseCls"))
        base_type = base_class.add_type(self._unique("BaseType"))
        try:
            test_type.set_kind("Typedef")
            test_type.set_is_typedef_constant(1)
            assert test_type.get_is_typedef_constant() == 1
            test_type.set_is_typedef_ordered(1)
            assert test_type.get_is_typedef_ordered() == 1
            test_type.set_is_typedef_reference(1)
            assert test_type.get_is_typedef_reference() == 1

            test_type.set_typedef_base_type(base_type)
            assert test_type.get_typedef_base_type() == base_type

            test_type.set_typedef_multiplicity("1")
            assert test_type.get_typedef_multiplicity() == "1"

            assert test_type.get_is_typedef() == 1
        finally:
            test_type.delete_from_project()
            base_type.delete_from_project()
            test_class.delete_from_project()
            base_class.delete_from_project()
```

For remaining methods (`get_is_typedef` beyond the typedef test above is already covered), follow the same pattern: group logically-related getters/setters/predicates into one test method with a `try/finally` cleanup around a freshly created `RPType`.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/common/test_model_other_model.py::TestRPTypeIntegration -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/common/model_other_model.py`, flip the 31 `RPType` checklist rows listed above (all except `addEnumerationLiteral`, `deleteEnumerationLiteral`, `getEnumerationLiterals`, which are covered in Task 2) from `[ ] integration test` to `[x] integration test`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/common/test_model_other_model.py src/rhapsody_cli/models/elements/common/model_other_model.py
git commit -m "test: add integration tests for RPType"
```

---

### Task 2: RPEnumerationLiteral — value roundtrip and RPType enumeration-literal factory methods

**Files:**
- Modify: `tests/integration/models/elements/common/test_model_misc.py`
- Modify: `src/rhapsody_cli/models/elements/common/model_misc.py` (flip checklist boxes only)
- Modify: `src/rhapsody_cli/models/elements/common/model_other_model.py` (flip checklist boxes only, for `RPType.add_enumeration_literal` / `delete_enumeration_literal` / `get_enumeration_literals`)

**Methods covered:** `RPEnumerationLiteral.get_value`, `RPEnumerationLiteral.set_value`, `RPType.add_enumeration_literal`, `RPType.delete_enumeration_literal`, `RPType.get_enumeration_literals`

- [ ] **Step 1: Write the failing/new integration tests**

```python
# Add to tests/integration/models/elements/common/test_model_misc.py

from rhapsody_cli.models.elements.common import RPComment, RPConstraint, RPEnumerationLiteral, RPType
from rhapsody_cli.models.elements.classifiers import RPClass


@pytest.mark.integration
class TestRPEnumerationLiteralIntegration:
    """Integration tests for RPEnumerationLiteral with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_add_get_delete_enumeration_literal(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("EnumPkg"))
        test_class = pkg.add_class(self._unique("EnumCls"))
        enum_type = test_class.add_type(self._unique("MyEnum"))
        try:
            assert isinstance(enum_type, RPType)
            literal = enum_type.add_enumeration_literal(self._unique("LIT"))
            assert isinstance(literal, RPEnumerationLiteral)

            literals = list(enum_type.get_enumeration_literals())
            assert literal in literals

            literal.set_value(5)
            assert literal.get_value() == 5

            enum_type.delete_enumeration_literal(literal)
            literals_after = list(enum_type.get_enumeration_literals())
            assert literal not in literals_after
        finally:
            enum_type.delete_from_project()
            test_class.delete_from_project()
```

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/common/test_model_misc.py::TestRPEnumerationLiteralIntegration -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `model_misc.py`: flip `getValue`, `setValue` for `RPEnumerationLiteral`.
In `model_other_model.py`: flip `addEnumerationLiteral`, `deleteEnumerationLiteral`, `getEnumerationLiterals` for `RPType`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/common/test_model_misc.py src/rhapsody_cli/models/elements/common/model_misc.py src/rhapsody_cli/models/elements/common/model_other_model.py
git commit -m "test: add integration tests for RPEnumerationLiteral"
```

---

### Task 3: RPConstraint — constrained-elements collection

**Files:**
- Modify: `tests/integration/models/elements/common/test_model_misc.py`
- Modify: `src/rhapsody_cli/models/elements/common/model_misc.py` (flip checklist boxes only)

**Methods covered:** `get_constraints_by_me`

- [ ] **Step 1: Write the failing/new integration test**

```python
# Add to the existing TestRPConstraintIntegration class in test_model_misc.py

    def test_get_constraints_by_me_returns_collection(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ConColPkg")
        con_name = self._unique("MyConstraint")
        pkg = self._create_package(test_project, pkg_name)
        constraint = pkg.add_new_aggr("Constraint", con_name)
        try:
            constrained = constraint.get_constraints_by_me()
            # No elements have been associated with the constraint yet — the
            # collection should exist and be iterable/empty.
            assert list(constrained) == []
        finally:
            constraint.delete_from_project()
```

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/common/test_model_misc.py::TestRPConstraintIntegration -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `model_misc.py`, flip `getConstraintsByMe` for `RPConstraint`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/common/test_model_misc.py src/rhapsody_cli/models/elements/common/model_misc.py
git commit -m "test: add integration test for RPConstraint.get_constraints_by_me"
```

---

### Task 4: RPClassifierRole — lifeline creation and formal classifier/instance/diagram roundtrips

**Files:**
- Modify: `tests/integration/models/elements/common/test_model_other_model.py`
- Modify: `src/rhapsody_cli/models/elements/common/model_other_model.py` (flip checklist boxes only)

**Methods covered:** `get_formal_classifier`, `set_formal_classifier`, `get_formal_instance`, `set_formal_instance`, `get_referenced_sequence_diagram`, `set_referenced_sequence_diagram`, `get_referencing_classifier_roles_recursively`, `get_role_type`

- [ ] **Step 1: Write the failing/new integration tests**

```python
# Add to tests/integration/models/elements/common/test_model_other_model.py

from rhapsody_cli.models.elements.common import RPClassifierRole
from rhapsody_cli.models.elements.diagrams import RPSequenceDiagram


@pytest.mark.integration
class TestRPClassifierRoleIntegration:
    """Integration tests for RPClassifierRole with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_formal_classifier_roundtrip(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("RolePkg"))
        collab = pkg.add_new_aggr("Collaboration", self._unique("MyCollab"))
        target_class = pkg.add_class(self._unique("RoleTargetCls"))
        try:
            role = collab.add_classifier_role(self._unique("MyRole"))
            assert isinstance(role, RPClassifierRole)
            assert role.get_role_type() == "CLASS"

            role.set_formal_classifier(target_class)
            assert role.get_formal_classifier() == target_class
        finally:
            collab.delete_from_project()
            target_class.delete_from_project()

    def test_formal_instance_roundtrip(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("RoleInstPkg"))
        collab = pkg.add_new_aggr("Collaboration", self._unique("MyCollab"))
        target_class = pkg.add_class(self._unique("RoleInstTargetCls"))
        instance = pkg.add_new_aggr("Object", self._unique("MyObj"))
        try:
            role = collab.add_classifier_role(self._unique("MyRole"))
            role.set_formal_instance(instance)
            assert role.get_formal_instance() == instance
        finally:
            collab.delete_from_project()
            target_class.delete_from_project()
            instance.delete_from_project()

    def test_referenced_sequence_diagram_roundtrip(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("RoleSeqPkg"))
        collab = pkg.add_new_aggr("Collaboration", self._unique("MyCollab"))
        seq_diagram = pkg.add_sequence_diagram(self._unique("MySeq"))
        try:
            role = collab.add_classifier_role(self._unique("MyRole"))
            assert isinstance(seq_diagram, RPSequenceDiagram)

            role.set_referenced_sequence_diagram(seq_diagram)
            assert role.get_referenced_sequence_diagram() == seq_diagram

            recursive_roles = role.get_referencing_classifier_roles_recursively()
            assert list(recursive_roles) == []
        finally:
            collab.delete_from_project()
            seq_diagram.delete_from_project()
```

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/common/test_model_other_model.py::TestRPClassifierRoleIntegration -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `model_other_model.py`, flip `getFormalClassifier`, `getFormalInstance`, `getReferencedSequenceDiagram`, `getReferencingClassifierRolesRecursively`, `getRoleType`, `setFormalClassifier`, `setFormalInstance`, `setReferencedSequenceDiagram` for `RPClassifierRole`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/common/test_model_other_model.py src/rhapsody_cli/models/elements/common/model_other_model.py
git commit -m "test: add integration tests for RPClassifierRole"
```

---

### Task 5: RPSysMLPort — flowport direction, type, reversal, and link creation

**Files:**
- Modify: `tests/integration/models/elements/common/test_model_other_model.py`
- Modify: `src/rhapsody_cli/models/elements/common/model_other_model.py` (flip checklist boxes only)

**Methods covered:** `get_is_reversed`, `set_is_reversed`, `get_port_direction`, `set_port_direction`, `get_type`, `set_type`, `add_link`

**Note:** `IRPSysMLPort` elements may only be creatable when a SysML/flowport profile is loaded on the project. Verify against the live `test_project` fixture first; if `add_new_aggr("SysMLPort", ...)` raises or returns an incompatible element, guard the affected tests with `@pytest.mark.xfail(reason="SysML flowport profile not loaded in TestProject fixture", strict=False)` rather than deleting the tests, so the checklist can still be flipped once environment support is confirmed.

- [ ] **Step 1: Write the failing/new integration tests**

```python
# Add to tests/integration/models/elements/common/test_model_other_model.py

from rhapsody_cli.models.elements.common import RPSysMLPort


@pytest.mark.integration
class TestRPSysMLPortIntegration:
    """Integration tests for RPSysMLPort with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def _create_port(self, pkg: RPPackage, owner_class: RPClass, name: str) -> RPSysMLPort:
        port = owner_class.add_new_aggr("SysMLPort", name)
        assert isinstance(port, RPSysMLPort)
        return port

    def test_direction_and_reversal_roundtrip(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("PortPkg"))
        owner_class = pkg.add_class(self._unique("PortOwnerCls"))
        try:
            port = self._create_port(pkg, owner_class, self._unique("MyPort"))
            try:
                port.set_port_direction("In")
                assert port.get_port_direction() == "In"

                port.set_is_reversed(1)
                assert port.get_is_reversed() == 1
                port.set_is_reversed(0)
                assert port.get_is_reversed() == 0
            finally:
                port.delete_from_project()
        finally:
            owner_class.delete_from_project()

    def test_type_roundtrip(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("PortTypePkg"))
        owner_class = pkg.add_class(self._unique("PortTypeOwnerCls"))
        type_class = pkg.add_class(self._unique("PortTypeCls"))
        try:
            port = self._create_port(pkg, owner_class, self._unique("MyPort"))
            try:
                port.set_type(type_class)
                assert port.get_type() == type_class
            finally:
                port.delete_from_project()
        finally:
            owner_class.delete_from_project()
            type_class.delete_from_project()

    def test_add_link_between_ports(self, test_project: RPProject) -> None:
        pkg = test_project.add_package(self._unique("PortLinkPkg"))
        owner_class = pkg.add_class(self._unique("LinkOwnerCls"))
        from_part = pkg.add_new_aggr("Object", self._unique("FromPart"))
        to_part = pkg.add_new_aggr("Object", self._unique("ToPart"))
        try:
            from_port = self._create_port(pkg, owner_class, self._unique("FromPort"))
            to_port = self._create_port(pkg, owner_class, self._unique("ToPort"))
            try:
                link = from_port.add_link(from_part, to_part, None, to_port, pkg)
                assert link is not None
            finally:
                from_port.delete_from_project()
                to_port.delete_from_project()
        finally:
            owner_class.delete_from_project()
            from_part.delete_from_project()
            to_part.delete_from_project()
```

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/common/test_model_other_model.py::TestRPSysMLPortIntegration -m integration -v`

- [ ] **Step 3: Flip checklist boxes**

In `model_other_model.py`, flip `addLink`, `getIsReversed`, `getPortDirection`, `getType`, `setIsReversed`, `setPortDirection`, `setType` for `RPSysMLPort` (only for methods whose tests pass without `xfail`).

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/common/test_model_other_model.py src/rhapsody_cli/models/elements/common/model_other_model.py
git commit -m "test: add integration tests for RPSysMLPort"
```

---

### Task 6: Full Subpackage Verification

**Files:** none modified — verification only.

- [ ] **Step 1: Run the entire common-subpackage integration suite**

Run: `pytest tests/integration/models/elements/common/ -m integration -v`

- [ ] **Step 2: Confirm no untested methods remain**

Run: `grep -n "integration test" src/rhapsody_cli/models/elements/common/model_misc.py src/rhapsody_cli/models/elements/common/model_other_model.py` and confirm every checklist row shows `[x] integration test` (except any explicitly deferred with a documented `xfail`).

- [ ] **Step 3: Run the full quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 4: Commit final state (if any cleanup was needed)**

```bash
git add -A
git commit -m "test: complete integration test coverage for common subpackage"
```
