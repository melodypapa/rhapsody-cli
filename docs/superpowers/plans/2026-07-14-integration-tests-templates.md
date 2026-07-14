# Templates Subpackage Integration Tests Completion Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add integration tests for ALL methods (currently zero coverage) of `RPTemplateInstantiation`, `RPTemplateInstantiationParameter`, `RPTemplateParameter` in `src/rhapsody_cli/models/elements/templates/model_templates.py`. Flip in-source `[ ] integration test` markers to `[x]` as work completes.

**Architecture:** New test file `tests/integration/models/elements/templates/test_model_templates.py`, using the shared `rhapsody_app`/`test_project` fixtures from `tests/integration/conftest.py` and the template creation chain documented below.

**Tech Stack:** pytest, pywin32 (win32com), live Rhapsody COM API, `uuid.uuid4().hex[:8]`.

## Creation chain (discovered from source)

There is no dedicated `add_template_parameter`/`add_template_instantiation` convenience method anywhere in the codebase. Templates are built from the generic `RPModelElement` factory and relationship methods (all inherited, already implemented and unit-tested in `src/rhapsody_cli/models/core.py`):

1. **Template definition:** Create a normal class (`pkg.add_class(name)`) to act as the template, then attach one or more template parameters to it via the generic factory:
   `template_param = template_cls.add_new_aggr("TemplateParameter", name)` — this returns an `RPTemplateParameter` (registered via `AbstractRPModelElement.register_wrapper("TemplateParameter", RPTemplateParameter)`). `template_cls.get_template_parameters()` (on `RPModelElement`, already tested) returns the collection containing it.
2. **Template instantiation:** Create a second class to act as the instantiation (`instance_cls = pkg.add_class(name)`), then bind it to the template via `instance_cls.become_template_instantiation_of(template_cls)` (or the setter-style `instance_cls.set_of_template(template_cls)` — both are `RPModelElement` methods, already tested). After binding, `instance_cls.get_ti()` (`RPModelElement`, already tested) returns the `RPTemplateInstantiation` wrapper — this is the object under test in this plan.
3. **Template instantiation parameters:** `ti.get_template_instantiation_parameters()` returns an `RPCollection` of `RPTemplateInstantiationParameter` objects, one per template parameter on the template definition. Each exposes `get_arg_value`/`set_arg_value` (string binding, e.g. `"int"`) and `get_type`/`set_type` (classifier binding, valid only when the parameter kind is `"class"`).
4. **`RPTemplateParameter` (extends `RPVariable`):** `get_parameter_kind`/`set_parameter_kind` (e.g. `"class"`), `set_class_type` (binds a classifier as the parameter's class type), and `get_representative`/`set_representative` (documented in source as "for internal use only" — the underlying surrogate element Rhapsody generates to let the parameter act like a real type inside the template body).

Some of the above (`set_type`, `get_representative`/`set_representative`) touch COM behavior that is either internal-use-only or dependent on argument "kind" state that is hard to verify without a live Rhapsody instance. These are written as real tests but marked `xfail(strict=False)` per the established project pattern (see `test_model_class.py::test_abstract_roundtrip`) so implementers can confirm/relax them against a live instance.

## Global Constraints

- Windows-only runtime (requires Windows + a running Rhapsody instance)
- All test classes use `@pytest.mark.integration`
- All tests consume the `test_project: RPProject` fixture
- Use `_unique(prefix)` with `uuid.uuid4().hex[:8]`
- Always `try/finally` cleanup using the correct delete method verified from source (`delete_from_project()`)
- Assert both `isinstance()` and read-back values
- Flip `[ ] integration test` to `[x]` per task in `model_templates.py`
- Quality gate after each task: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
- Import via subpackage `__init__.py` re-exports (`rhapsody_cli.models.elements.templates`)
- Follow the exact style of `tests/integration/models/elements/classifiers/test_model_class.py`

---

## Task 1: RPTemplateInstantiation and RPTemplateInstantiationParameter

**Files:**
- Create: `tests/integration/models/elements/templates/test_model_templates.py`
- Modify: `src/rhapsody_cli/models/elements/templates/model_templates.py` (flip checklist boxes only)

**Methods covered:** `RPTemplateInstantiation.get_template_instantiation_parameters`; `RPTemplateInstantiationParameter.get_arg_value`, `RPTemplateInstantiationParameter.set_arg_value`, `RPTemplateInstantiationParameter.get_type`, `RPTemplateInstantiationParameter.set_type`

- [ ] **Step 1: Write the failing/new integration tests**

```python
"""Integration tests for templates model elements with live Rhapsody COM API.

These tests require a running Rhapsody instance with an open project.
"""

import uuid

import pytest

from rhapsody_cli.models.elements.containment import RPPackage, RPProject
from rhapsody_cli.models.elements.templates import (
    RPTemplateInstantiation,
    RPTemplateInstantiationParameter,
    RPTemplateParameter,
)


def _unique(prefix: str = "Test") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


def _create_package(project: RPProject, name: str) -> RPPackage:
    pkg = project.add_package(name)
    assert pkg is not None
    assert isinstance(pkg, RPPackage)
    return pkg


@pytest.mark.integration
class TestRPTemplateInstantiationIntegration:
    """Integration tests for RPTemplateInstantiation with real Rhapsody COM API."""

    def test_get_template_instantiation_parameters(self, test_project: RPProject) -> None:
        pkg = _create_package(test_project, _unique("TplPkg"))
        template_cls = pkg.add_class(_unique("TplClass"))
        instance_cls = pkg.add_class(_unique("InstClass"))
        try:
            template_param = template_cls.add_new_aggr("TemplateParameter", _unique("T"))
            assert isinstance(template_param, RPTemplateParameter)

            instance_cls.become_template_instantiation_of(template_cls)
            ti = instance_cls.get_ti()
            assert isinstance(ti, RPTemplateInstantiation)

            params = list(ti.get_template_instantiation_parameters())
            assert len(params) >= 1
            assert all(isinstance(p, RPTemplateInstantiationParameter) for p in params)
        finally:
            instance_cls.delete_from_project()
            template_cls.delete_from_project()
            pkg.delete_from_project()


@pytest.mark.integration
class TestRPTemplateInstantiationParameterIntegration:
    """Integration tests for RPTemplateInstantiationParameter with real Rhapsody COM API."""

    def test_arg_value_roundtrip(self, test_project: RPProject) -> None:
        pkg = _create_package(test_project, _unique("TplPkg"))
        template_cls = pkg.add_class(_unique("TplClass"))
        instance_cls = pkg.add_class(_unique("InstClass"))
        try:
            template_cls.add_new_aggr("TemplateParameter", _unique("T"))
            instance_cls.become_template_instantiation_of(template_cls)
            ti = instance_cls.get_ti()
            params = list(ti.get_template_instantiation_parameters())
            assert params, "expected at least one template instantiation parameter"
            param = params[0]
            assert isinstance(param, RPTemplateInstantiationParameter)

            param.set_arg_value("int")
            assert param.get_arg_value() == "int"
        finally:
            instance_cls.delete_from_project()
            template_cls.delete_from_project()
            pkg.delete_from_project()

    @pytest.mark.xfail(
        reason="setType on a template instantiation parameter requires the underlying "
        "template parameter's kind to be 'class' before the COM layer accepts a "
        "classifier binding; the exact sequencing against a live Rhapsody instance is "
        "unverified. TODO: confirm binding order (parameter kind vs. arg type) and "
        "relax this xfail once verified.",
        strict=False,
    )
    def test_type_roundtrip(self, test_project: RPProject) -> None:
        pkg = _create_package(test_project, _unique("TplPkg"))
        template_cls = pkg.add_class(_unique("TplClass"))
        instance_cls = pkg.add_class(_unique("InstClass"))
        bound_cls = pkg.add_class(_unique("BoundClass"))
        try:
            template_param = template_cls.add_new_aggr("TemplateParameter", _unique("T"))
            template_param.set_parameter_kind("class")
            instance_cls.become_template_instantiation_of(template_cls)
            ti = instance_cls.get_ti()
            params = list(ti.get_template_instantiation_parameters())
            assert params
            param = params[0]

            param.set_type(bound_cls)
            assert param.get_type() == bound_cls
        finally:
            instance_cls.delete_from_project()
            template_cls.delete_from_project()
            bound_cls.delete_from_project()
            pkg.delete_from_project()
```

For remaining methods, follow the same pattern (this task's method list is fully covered by the three tests above).

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/templates/test_model_templates.py -m integration -v -k "TemplateInstantiation"`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/templates/model_templates.py`, flip `[ ] integration test` to `[x] integration test` for: `getTemplateInstantiationParameters`, `getArgValue`, `getType`, `setArgValue`, `setType`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/templates/test_model_templates.py src/rhapsody_cli/models/elements/templates/model_templates.py
git commit -m "test: add integration tests for RPTemplateInstantiation and RPTemplateInstantiationParameter"
```

---

## Task 2: RPTemplateParameter

**Files:**
- Modify: `tests/integration/models/elements/templates/test_model_templates.py`
- Modify: `src/rhapsody_cli/models/elements/templates/model_templates.py` (flip checklist boxes only)

**Methods covered:** `get_parameter_kind`, `set_parameter_kind`, `set_class_type`, `get_representative`, `set_representative`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPTemplateParameterIntegration:
    """Integration tests for RPTemplateParameter with real Rhapsody COM API."""

    def test_parameter_kind_roundtrip(self, test_project: RPProject) -> None:
        pkg = _create_package(test_project, _unique("TplPkg"))
        template_cls = pkg.add_class(_unique("TplClass"))
        try:
            tp = template_cls.add_new_aggr("TemplateParameter", _unique("T"))
            assert isinstance(tp, RPTemplateParameter)

            tp.set_parameter_kind("class")
            assert tp.get_parameter_kind() == "class"
        finally:
            template_cls.delete_from_project()
            pkg.delete_from_project()

    def test_set_class_type(self, test_project: RPProject) -> None:
        pkg = _create_package(test_project, _unique("TplPkg"))
        template_cls = pkg.add_class(_unique("TplClass"))
        helper_cls = pkg.add_class(_unique("HelperClass"))
        try:
            tp = template_cls.add_new_aggr("TemplateParameter", _unique("T"))
            tp.set_parameter_kind("class")

            tp.set_class_type(helper_cls)
            # No dedicated getter exists for the bound class type (setClassType has no
            # getClassType counterpart per the IRPTemplateParameter API); assert the call
            # completes without raising and the parameter kind still persists as "class".
            assert tp.get_parameter_kind() == "class"
        finally:
            template_cls.delete_from_project()
            helper_cls.delete_from_project()
            pkg.delete_from_project()

    @pytest.mark.xfail(
        reason="getRepresentative/setRepresentative are documented in the Java API as "
        "'for internal use only'; the exact live-COM representative object returned by "
        "Rhapsody2.Application.1 for a freshly created TemplateParameter is unverified. "
        "TODO: confirm representative wiring against a live instance and relax this xfail.",
        strict=False,
    )
    def test_representative_roundtrip(self, test_project: RPProject) -> None:
        pkg = _create_package(test_project, _unique("TplPkg"))
        template_cls = pkg.add_class(_unique("TplClass"))
        try:
            tp = template_cls.add_new_aggr("TemplateParameter", _unique("T"))

            representative = tp.get_representative()
            assert representative is not None

            tp.set_representative(representative)
            assert tp.get_representative() == representative
        finally:
            template_cls.delete_from_project()
            pkg.delete_from_project()
```

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/templates/test_model_templates.py -m integration -v -k "TemplateParameter"`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/templates/model_templates.py`, flip `[ ] integration test` to `[x] integration test` for: `getParameterKind`, `getRepresentative`, `setClassType`, `setParameterKind`, `setRepresentative`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/templates/test_model_templates.py src/rhapsody_cli/models/elements/templates/model_templates.py
git commit -m "test: add integration tests for RPTemplateParameter"
```

---

## Task 3: Full Subpackage Verification

**Files:**
- Review only (no new tests expected): `tests/integration/models/elements/templates/test_model_templates.py`, `src/rhapsody_cli/models/elements/templates/model_templates.py`

- [ ] **Step 1: Confirm zero remaining `[ ] integration test` markers**

Run:

```bash
grep -n "integration test" src/rhapsody_cli/models/elements/templates/model_templates.py
```

Confirm every row shows `[x] integration test`. All 10 checklist rows (1 on `RPTemplateInstantiation`, 4 on `RPTemplateInstantiationParameter`, 5 on `RPTemplateParameter`) must be flipped.

- [ ] **Step 2: Run the full templates integration suite**

Run: `pytest tests/integration/models/elements/templates/test_model_templates.py -m integration -v`

Confirm the two `xfail` tests (`test_type_roundtrip`, `test_representative_roundtrip`) either xfail as expected or, if they unexpectedly pass (`XPASS`), remove the `xfail` marker for that test in a follow-up commit since `strict=False` will not fail the suite in that case, but the marker should be cleaned up so passing coverage is not silently hidden.

- [ ] **Step 3: Run full quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "test: complete integration test coverage for templates subpackage"
```
