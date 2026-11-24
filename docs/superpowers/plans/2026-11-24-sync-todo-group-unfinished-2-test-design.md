# Group-unfinished-2 Test Design Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Design and write the Step 4 (unit) and Step 5 (integration) tests for all 10 wrapper migrations in `docs/reports/sync-todo/Group-unfinished-2.md`, using the JavaDoc contract in `docs/java_api/com/telelogic/rhapsody/core/` and the rhapsody-sync skill rules.

**Architecture:** Phase 0 removes the hard COM-evidence blocker (all 10 interfaces are absent from `docs/reports/pywin32_authority.json` and have no `*_api_report.md`). Each interface then gets a data-driven fake-COM unit module and an authentic-data integration module, following the existing `IRPClass`/`IRPPackage` patterns. The plan is test-design scoped: wrapper code changes are only the minimal edits required to turn red tests green. Steps 6 (SWR), 7 (RST), and 8 (full verify) are out of scope here and remain open on the TODO rows.

**Tech Stack:** Python 3.8–3.13, pytest, `unittest.mock.MagicMock`, `tests.unit.models.fakes.make_fake_element` / `make_fake_collection` / `make_com_error`, pywin32 (Windows only), `uv run` for the project venv.

---

## Hard constraints (read before any task)

1. **JavaDoc path is `docs/java_api/`, not `docs/java_doc/`.** All 10 pages exist at `docs/java_api/com/telelogic/rhapsody/core/<INTERFACE>.html`. Owned members are the rows inside the page's single "Method Summary" table; the "Methods inherited from interface …" tables that follow are NOT owned and must not get per-member tests in the child file (`AGENTS.md` integration ownership rule).
2. **COM evidence blocker.** `docs/reports/pywin32_authority.json` (`catalog`, `signatures`, `documented_aliases`, `documented_unavailable`) currently contains only 16 interfaces. None of `IRPState`, `IRPComponent`, `IRPInstance`, `IRPRelation`, `IRPFlow`, `IRPStatechart`, `IRPDiagram`, `IRPMessage`, `IRPTableLayout`, `IRPCollaboration` is present. Skill §3 forbids editing wrapper/tests/docs on unverifiable evidence. Phase 0 must complete first.
3. **One pywin32 member per wrapper member.** Method-shaped → `call_com(lambda: self._com.Name(...))`; property-shaped → `get_com_property` / `set_com_property`. Never `_get_method_or_property` / `_set_method_or_property`, never a Java-name-first probe, never a fallback.
4. **100% statement and branch coverage of the wrapper module from the unit file alone.** Command: `uv run pytest tests/unit/models/com/telelogic/rhapsody/core/test_irp_<x>.py --cov=rhapsody_cli.models.com.telelogic.rhapsody.core.irp_<x> --cov-report=term-missing -o addopts=`. No `# pragma: no cover`, no exclusions, no combining with integration coverage.
5. **No `Any` type annotations.** Use concrete types, `object`, `Union`, or `TypedDict`. Test data tuples may be annotated as `tuple[object, ...]` with `from __future__ import annotations`.
6. **No skipped or xfailed model-class tests.** No `pytest.skip`, no `@pytest.mark.xfail`, no early `return`. The only permitted exception assertion is `pytest.raises(NotImplementedError)` for a JavaDoc-defined / pywin32-absent stub.
7. **Integration tests use authentic data** (real created Rhapsody objects and real identifiers), never `"arg"` / `"x"` / fabricated UUIDs. Clean up every created object. No `try`/`except` in test bodies — use `try`/`finally` only for teardown.
8. **Setup-only parent calls in the integration snippets below (`add_package`, `add_class`, `add_part`, `add_flow`, `add_statechart`, `add_class_diagram`, `add_collaboration`, `add_table_layout`, …) must be verified against the parent wrapper's own checklist before the test is run.** They are fixture construction, never assertions in the child file. A wrong parent method name is a test bug, not a COM blocker — check the parent's module and fix the call, do not weaken the child assertion.

## Shared unit-test harness (copy verbatim into each `test_irp_<x>.py`)

Every interface unit file below uses this harness. It is written out in full once here; Task 2 (IRPState) shows a complete instantiated file. For every later interface, copy the harness and substitute `META`, `WRAPPER`, `MODULE`, and the five data lists. This is not a stub — every data row is specified in full in that interface's task.

```python
"""Unit tests for <WrapperClass> (fake COM only; no real Rhapsody)."""

from __future__ import annotations

from typing import cast

import pytest

from rhapsody_cli.exceptions import RhapsodyRuntimeException
from rhapsody_cli.models.com.telelogic.rhapsody.core import <WrapperClass>
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_com_error, make_fake_collection, make_fake_element

# One wrapped element reused as an element-typed argument; _ARG_COM is the raw COM
# object the wrapper must pass through after unwrapping with `._com`.
_ARG_COM = make_fake_element("ModelElement", properties={"name": "arg"})
_ARG = cast(IRPModelElement, IRPModelElement.wrap(_ARG_COM))

META = "<MetaClass>"
WRAPPER = <WrapperClass>
MODULE = "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_<x>"

# (java_member, python_member, args, com_args)
VOID_METHODS: list[tuple[str, str, tuple[object, ...], tuple[object, ...]]] = []
# (java_member, python_member, args, com_args, com_return, python_expected)
VALUE_METHODS: list[tuple[str, str, tuple[object, ...], tuple[object, ...], object, object]] = []
# (java_member, python_member, args, com_args, returned_meta_class)
ELEMENT_METHODS: list[tuple[str, str, tuple[object, ...], tuple[object, ...], str]] = []
# (java_member, python_member, args, com_args, item_meta_class)
COLLECTION_METHODS: list[tuple[str, str, tuple[object, ...], tuple[object, ...], str]] = []
# (com_property, python_property, com_read_value, python_expected, writable, com_write_value)
PROPERTIES: list[tuple[str, str, object, object, bool, object]] = []
# (java_member, python_member, args) -- populated from the report's documented_unavailable section
STUBS: list[tuple[str, str, tuple[object, ...]]] = []


@pytest.mark.parametrize("row", VOID_METHODS, ids=lambda row: row[1])
def test_void_method_delegates_to_single_com_member(row: tuple[object, ...]) -> None:
    java_name, python_name, args, com_args = row
    fake = make_fake_element(META)
    getattr(WRAPPER(fake), cast(str, python_name))(*cast(tuple[object, ...], args))
    getattr(fake, cast(str, java_name)).assert_called_once_with(*cast(tuple[object, ...], com_args))


@pytest.mark.parametrize("row", VALUE_METHODS, ids=lambda row: row[1])
def test_value_method_returns_com_value(row: tuple[object, ...]) -> None:
    java_name, python_name, args, com_args, com_return, expected = row
    fake = make_fake_element(META)
    getattr(fake, cast(str, java_name)).return_value = com_return
    result = getattr(WRAPPER(fake), cast(str, python_name))(*cast(tuple[object, ...], args))
    getattr(fake, cast(str, java_name)).assert_called_once_with(*cast(tuple[object, ...], com_args))
    assert result == expected


@pytest.mark.parametrize("row", ELEMENT_METHODS, ids=lambda row: row[1])
def test_element_method_unwraps_args_and_wraps_result(row: tuple[object, ...]) -> None:
    java_name, python_name, args, com_args, returned_meta = row
    fake = make_fake_element(META)
    child = make_fake_element(cast(str, returned_meta), properties={"name": "child"})
    getattr(fake, cast(str, java_name)).return_value = child
    result = getattr(WRAPPER(fake), cast(str, python_name))(*cast(tuple[object, ...], args))
    getattr(fake, cast(str, java_name)).assert_called_once_with(*cast(tuple[object, ...], com_args))
    assert result is not None
    assert result.get_name() == "child"


@pytest.mark.parametrize("row", COLLECTION_METHODS, ids=lambda row: row[1])
def test_collection_method_wraps_result(row: tuple[object, ...]) -> None:
    java_name, python_name, args, com_args, item_meta = row
    fake = make_fake_element(META)
    child = make_fake_element(cast(str, item_meta), properties={"name": "child"})
    getattr(fake, cast(str, java_name)).return_value = make_fake_collection([child])
    result = getattr(WRAPPER(fake), cast(str, python_name))(*cast(tuple[object, ...], args))
    getattr(fake, cast(str, java_name)).assert_called_once_with(*cast(tuple[object, ...], com_args))
    assert isinstance(result, IRPCollection)
    assert len(list(result)) == 1


@pytest.mark.parametrize("row", PROPERTIES, ids=lambda row: row[1])
def test_property_uses_single_com_property(row: tuple[object, ...]) -> None:
    com_name, python_name, read_value, expected, writable, write_value = row
    fake = make_fake_element(META, properties={cast(str, com_name): read_value})
    wrapper = WRAPPER(fake)
    assert getattr(wrapper, cast(str, python_name)) == expected
    if cast(bool, writable):
        setattr(wrapper, cast(str, python_name), write_value)
        assert getattr(fake, cast(str, com_name)) == write_value


@pytest.mark.parametrize("row", STUBS, ids=lambda row: row[1])
def test_documented_unavailable_stub_raises_without_dispatch(row: tuple[object, ...]) -> None:
    java_name, python_name, args = row
    fake = make_fake_element(META)
    with pytest.raises(NotImplementedError):
        getattr(WRAPPER(fake), cast(str, python_name))(*cast(tuple[object, ...], args))
    getattr(fake, cast(str, java_name)).assert_not_called()


def test_com_failure_is_translated() -> None:
    """One translation test per binding shape actually used by this module."""
    fake = make_fake_element(META)
    first = VOID_METHODS[0] or VALUE_METHODS[0] or ELEMENT_METHODS[0] or COLLECTION_METHODS[0]
    getattr(fake, cast(str, first[0])).side_effect = make_com_error()
    with pytest.raises(RhapsodyRuntimeException):
        getattr(WRAPPER(fake), cast(str, first[1]))(*cast(tuple[object, ...], first[2]))


def test_wrapper_is_registered() -> None:
    fake = make_fake_element(META, properties={"name": "widget"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, WRAPPER)
```

**Reconciliation step (mandatory, once per interface, after Phase 0):** open the generated `docs/reports/com/telelogic/rhapsody/core/<INTERFACE>_api_report.md`. Its pywin32 column is authoritative for shape. For every JavaDoc-owned member:

- pywin32 **method-shaped** → put it in `VOID_METHODS`, `VALUE_METHODS`, `ELEMENT_METHODS`, or `COLLECTION_METHODS` according to its Java return type.
- pywin32 **property-shaped** → put the getter in `PROPERTIES`; if Java declares a matching `setX`, set `writable=True` on the same row.
- JavaDoc present, pywin32 **absent** → put it in `STUBS` and keep the Java signature (skill §4, `documented_unavailable`).
- Any signature whose `count`/`required`/`names`/`types` differ from JavaDoc → stop, record the deviation on the TODO row; do not write a test that blesses a wrong arity.

A row that fails after reconciliation is a real finding, not a test to weaken. Never change an assertion to `pytest.raises(...)` other than `NotImplementedError`.

**Coverage accounting (per interface):** run the exact command in constraint 4. If `term-missing` shows an uncovered line, add a dedicated test to that interface's unit file (never a `# pragma`), rerun, and record the final figure in the sync report later (Step 8, out of scope here).

---

## Phase 0 — COM evidence blocker

### Task 1: Generate and commit reports + refresh the authority catalog

**Files:**
- Modify: `docs/reports/pywin32_authority.json`
- Create: `docs/reports/com/telelogic/rhapsody/core/irp_{state,component,instance,relation,flow,statechart,diagram,message,table_layout,collaboration}_api_report.md`

- [ ] **Step 1: Run the report generator against the live typelib (Windows + Rhapsody required)**

```bash
python scripts/validate_model_api.py IRPState --source typelib --path docs/reports
python scripts/validate_model_api.py IRPComponent --source typelib --path docs/reports
python scripts/validate_model_api.py IRPInstance --source typelib --path docs/reports
python scripts/validate_model_api.py IRPRelation --source typelib --path docs/reports
python scripts/validate_model_api.py IRPFlow --source typelib --path docs/reports
python scripts/validate_model_api.py IRPStatechart --source typelib --path docs/reports
python scripts/validate_model_api.py IRPDiagram --source typelib --path docs/reports
python scripts/validate_model_api.py IRPMessage --source typelib --path docs/reports
python scripts/validate_model_api.py IRPTableLayout --source typelib --path docs/reports
python scripts/validate_model_api.py IRPCollaboration --source typelib --path docs/reports
```
Expected: each writes a report under `docs/reports/com/telelogic/rhapsody/core/`. Exit 1 means actionable deviations (record them, do not guess shape); exit 2 means setup failure (stop the whole plan).

- [ ] **Step 2: Refresh the authority catalog from the new reports**

```bash
python scripts/pywin32_authority.py --source reports --output docs/reports/pywin32_authority.json
```
Expected: `catalog` and `signatures` now contain all 10 interface keys.

- [ ] **Step 3: Confirm each interface is unblocked offline**

```bash
for I in IRPState IRPComponent IRPInstance IRPRelation IRPFlow IRPStatechart IRPDiagram IRPMessage IRPTableLayout IRPCollaboration; do
  python .agents/skills/rhapsody-sync/scripts/validate_interface.py "$I" --source authority || echo "BLOCKED: $I"
done
```
Expected: no `BLOCKED:` lines. Exit 2 for any interface means stop — do not write that interface's tests.

- [ ] **Step 4: Commit only the generated evidence**

```bash
git add docs/reports/pywin32_authority.json docs/reports/com/telelogic/rhapsody/core/irp_*_api_report.md
git commit -m "docs(sync): add pywin32 evidence for Group-unfinished-2 interfaces"
```

- [ ] **Step 5: Open the per-run checklists**

For each now-unblocked row in `docs/reports/sync-todo/Group-unfinished-2.md`, publish §1's checklist with one subtask per owned JavaDoc member (`JavaDoc / COM / wrapper / disposition` boxes) before writing any test. The member inventories in Tasks 2–21 are that checklist content.

---

## IRPState (row 1 — 48 owned members, `elements/statemachine/model_statemachine.py`)

### Task 2: IRPState unit tests (red → green)

**Files:**
- Create: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_state.py`
- Test: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_state.py`

- [ ] **Step 1: Write the failing test file** — copy the shared harness verbatim with `META = "State"`, `WRAPPER = IRPState`, `MODULE = "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_state"`, and these five data lists (one row per owned JavaDoc member; shape reconciled in Phase 0):

```python
VOID_METHODS = [
    ("deleteConnector", "delete_connector", (_ARG,), (_ARG_COM,)),
    ("deleteInternalTransition", "delete_internal_transition", (_ARG,), (_ARG_COM,)),
    ("deleteStaticReaction", "delete_static_reaction", (_ARG,), (_ARG_COM,)),
    ("overrideInheritance", "override_inheritance", (), ()),
    ("setInternalTransition", "set_internal_transition", ("trig", "guard", "action"), ("trig", "guard", "action")),
    ("setStaticReaction", "set_static_reaction", ("trig", "guard", "action"), ("trig", "guard", "action")),
    ("unoverrideInheritance", "unoverride_inheritance", (), ()),
]
ELEMENT_METHODS = [
    ("addActivityFinal", "add_activity_final", (), (), "State"),
    ("addConnector", "add_connector", ("Generalization",), ("Generalization",), "Connector"),
    ("addInternalTransition", "add_internal_transition", (_ARG,), (_ARG_COM,), "Transition"),
    ("addState", "add_state", ("Child",), ("Child",), "State"),
    ("addStaticReaction", "add_static_reaction", (_ARG,), (_ARG_COM,), "Transition"),
    ("addTerminationState", "add_termination_state", (), (), "State"),
    ("createDefaultTransition", "create_default_transition", (_ARG,), (_ARG_COM,), "Transition"),
    ("createNestedStatechart", "create_nested_statechart", (), (), "Statechart"),
    ("createSubStatechart", "create_sub_statechart", (), (), "Statechart"),
    ("resetEntryActionInheritance", "reset_entry_action_inheritance", (), (), "State"),
    ("resetExitActionInheritance", "reset_exit_action_inheritance", (), (), "State"),
]
VALUE_METHODS = [
    ("getIsOverridden", "get_is_overridden", (), (), 1, 1),
    ("getIsReferenceActivity", "get_is_reference_activity", (), (), 1, 1),
    ("isAnd", "is_and", (), (), 1, 1),
    ("isCompound", "is_compound", (), (), 1, 1),
    ("isLeaf", "is_leaf", (), (), 1, 1),
    ("isRoot", "is_root", (), (), 1, 1),
    ("isSendActionState", "is_send_action_state", (), (), 1, 1),
]
COLLECTION_METHODS = [
    ("getInternalTransitions", "get_internal_transitions", (), (), "Transition"),
    ("getLogicalStates", "get_logical_states", (), (), "State"),
    ("getStaticReactions", "get_static_reactions", (), (), "Transition"),
    ("getSubStates", "get_sub_states", (), (), "State"),
    ("getSubStateVertices", "get_sub_state_vertices", (), (), "StateVertex"),
]
PROPERTIES = [
    ("entryAction", "entry_action", "on entry", "on entry", True, "new entry"),
    ("exitAction", "exit_action", "on exit", "on exit", True, "new exit"),
    ("fullNameInStatechart", "full_name_in_statechart", "Top::Idle", "Top::Idle", False, None),
    ("inheritsFrom", "inherits_from", None, None, False, None),
    ("itsStatechart", "its_statechart", None, None, False, None),
    ("itsSwimlane", "its_swimlane", None, None, True, None),
    ("referenceToActivity", "reference_to_activity", None, None, True, None),
    ("stateType", "state_type", "normal", "normal", True, "final"),
    ("sendAction", "send_action", None, None, False, None),
    ("theEntryAction", "the_entry_action", None, None, False, None),
    ("theExitAction", "the_exit_action", None, None, False, None),
]
STUBS = []  # fill from irp_state_api_report.md documented_unavailable
```

- [ ] **Step 2: Run the tests and verify they fail**

```bash
uv run pytest tests/unit/models/com/telelogic/rhapsody/core/test_irp_state.py -q -o addopts=
```
Expected: FAIL at collection (`ModuleNotFoundError: ... irp_state`).

- [ ] **Step 3: Implement the wrapper to go green** — create `irp_state.py` with `class IRPState(IRPStateVertex)` (import from the legacy module until a base row migrates), `IRPModelElement.register_wrapper("State", IRPState)`, and one member per data row above. Method-shaped: `self.call_com(lambda: self._com.<JavaName>(...))`; unwrap element args with `._com`; wrap returns with `cast(..., self.wrap(...))`. Property-shaped: `@property` + setter using `self.get_com_property(self._com, "<comProp>")` / `self.set_com_property(...)`. Stubs: Java-signature method that raises `NotImplementedError("<JavaName> is not exposed in the Rhapsody COM automation type library.")` without a COM call.

- [ ] **Step 4: Run the tests and verify they pass, with 100% coverage**

```bash
uv run pytest tests/unit/models/com/telelogic/rhapsody/core/test_irp_state.py -q -o addopts= --cov=rhapsody_cli.models.com.telelogic.rhapsody.core.irp_state --cov-report=term-missing
```
Expected: all PASS, `TOTAL ... 100%`. Any missing line gets a dedicated test, not a pragma.

- [ ] **Step 5: Commit**

```bash
git add src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_state.py tests/unit/models/com/telelogic/rhapsody/core/test_irp_state.py
git commit -m "test(sync): add fake-COM unit tests for IRPState"
```

### Task 3: IRPState integration tests (live Rhapsody)

**Files:**
- Test: `tests/integration/models/com/telelogic/rhapsody/core/test_irp_state.py`

- [ ] **Step 1: Write the file** — `@pytest.mark.integration` class with the standard `_unique()` helper, a `_create_statechart(project, name)` setup helper (build a package via `project.add_package`, a class via `pkg.add_class`, then `add_statechart(...)`), and these tests. Every created object is deleted in `finally`:

```python
def test_add_state_and_sub_states(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("StatePkg"))
    sc = self._create_statechart(pkg, self._unique("StateSC"))
    try:
        root = sc.get_root_state()
        assert root is not None
        child = root.add_state(self._unique("ChildState"))
        assert child is not None
        assert child.get_name() in [s.get_name() for s in root.get_sub_states()]
        grandchild = child.add_state(self._unique("GrandChild"))
        assert grandchild is not None
    finally:
        sc.delete_from_project()

def test_internal_transition_round_trip(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("TransPkg"))
    sc = self._create_statechart(pkg, self._unique("TransSC"))
    try:
        root = sc.get_root_state()
        root.set_internal_transition("sig", "guard == 1", "counter++")
        transitions = list(root.get_internal_transitions())
        assert transitions
    finally:
        sc.delete_from_project()

def test_entry_and_exit_action_properties(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("ActionPkg"))
    sc = self._create_statechart(pkg, self._unique("ActionSC"))
    try:
        state = sc.get_root_state().add_state(self._unique("ActionState"))
        state.entry_action = "log('enter')"
        assert state.entry_action == "log('enter')"
        state.exit_action = "log('exit')"
        assert state.exit_action == "log('exit')"
    finally:
        sc.delete_from_project()

def test_state_type_property(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("TypePkg"))
    sc = self._create_statechart(pkg, self._unique("TypeSC"))
    try:
        state = sc.get_root_state().add_state(self._unique("TypedState"))
        state.state_type = "final"
        assert state.state_type == "final"
    finally:
        sc.delete_from_project()
```

- [ ] **Step 2: Add one `pytest.raises(NotImplementedError)` test per member in `STUBS`**, invoking through the concrete wrapper created above; assert the same exception after `finally` cleanup. No other exception assertion is allowed.

- [ ] **Step 3: Verify collection and live execution**

```bash
uv run pytest tests/integration/models/com/telelogic/rhapsody/core/test_irp_state.py --collect-only -q -o addopts=
```
Expected on non-Windows: collection succeeds. On Windows with Rhapsody: `uv run pytest tests/integration/models/com/telelogic/rhapsody/core/test_irp_state.py -q -o addopts=` → all PASS.

- [ ] **Step 4: Commit**

```bash
git add tests/integration/models/com/telelogic/rhapsody/core/test_irp_state.py
git commit -m "test(sync): add live integration tests for IRPState"
```

---

## IRPComponent (row 2 — 43 owned members, `elements/containment/model_component.py`)

### Task 4: IRPComponent unit tests

**Files:**
- Create: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_component.py`
- Test: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_component.py`

- [ ] **Step 1:** Copy the shared harness with `META = "Component"`, `WRAPPER = IRPComponent`, `MODULE = "...irp_component"`, and:

```python
VOID_METHODS = [
    ("addScopeElement", "add_scope_element", (_ARG,), (_ARG_COM,)),
    ("addScopeElementWithoutAggregates", "add_scope_element_without_aggregates", (_ARG,), (_ARG_COM,)),
    ("allElementsInScope", "all_elements_in_scope", (), ()),
    ("deleteConfiguration", "delete_configuration", (_ARG,), (_ARG_COM,)),
    ("deleteFile", "delete_file", (_ARG,), (_ARG_COM,)),
    ("removeScopeElement", "remove_scope_element", (_ARG,), (_ARG_COM,)),
]
ELEMENT_METHODS = [
    ("addConfiguration", "add_configuration", ("Cfg",), ("Cfg",), "Configuration"),
    ("addFile", "add_file", ("File.cpp",), ("File.cpp",), "File"),
    ("addFolder", "add_folder", ("include",), ("include",), "File"),
    ("addNestedComponent", "add_nested_component", ("Child",), ("Child",), "Component"),
    ("findConfiguration", "find_configuration", ("Cfg",), ("Cfg",), "Configuration"),
    ("getConfigByDependency", "get_config_by_dependency", (_ARG,), (_ARG_COM,), "Configuration"),
    ("getFile", "get_file", (_ARG, 1, 1), (_ARG_COM, 1, 1), "File"),
    ("getPackageFile", "get_package_file", (_ARG, 1), (_ARG_COM, 1), "File"),
    ("getVariant", "get_variant", (_ARG,), (_ARG_COM,), "ModelElement"),
]
COLLECTION_METHODS = [
    ("getConfigurations", "get_configurations", (), (), "Configuration"),
    ("getFiles", "get_files", (), (), "File"),
    ("getNestedComponents", "get_nested_components", (), (), "Component"),
    ("getPanelDiagrams", "get_panel_diagrams", (), (), "PanelDiagram"),
    ("getPossibleVariants", "get_possible_variants", (_ARG,), (_ARG_COM,), "ModelElement"),
    ("getScopeElements", "get_scope_elements", (), (), "ModelElement"),
    ("getScopeElementsByCategory", "get_scope_elements_by_category", ("source",), ("source",), "ModelElement"),
    ("getVariationPoints", "get_variation_points", (), (), "ModelElement"),
]
VALUE_METHODS = [
    ("getFileName", "get_file_name", (_ARG, 1, 1), (_ARG_COM, 1, 1), "File.cpp", "File.cpp"),
    ("getModelElementFileName", "get_model_element_file_name", (_ARG, 1, 1), (_ARG_COM, 1, 1), "Elem.h", "Elem.h"),
    ("getPath", "get_path", (1,), (1,), "/proj", "/proj"),
    ("getScopeBySelectedElements", "get_scope_by_selected_elements", (), (), 1, 1),
    ("isDirectoryPerModelComponent", "is_directory_per_model_component", (_ARG,), (_ARG_COM,), 1, 1),
    ("updateContainedDiagramsOnServer", "update_contained_diagrams_on_server", (1,), (1,), 1, 1),
]
PROPERTIES = [
    ("additionalSources", "additional_sources", "src/", "src/", True, "src2/"),
    ("buildType", "build_type", "debug", "debug", True, "release"),
    ("includePath", "include_path", "inc", "inc", True, "inc2"),
    ("libraries", "libraries", "lib", "lib", True, "lib2"),
    ("path", "path", "/p", "/p", True, "/p2"),
    ("scopeBySelectedElements", "scope_by_selected_elements", 1, 1, True, 0),
    ("standardHeaders", "standard_headers", "std.h", "std.h", True, "std2.h"),
]
STUBS = []  # fill from irp_component_api_report.md documented_unavailable
```

- [ ] **Steps 2–5:** identical to Task 2 Steps 2–5, substituting `component` and the commit message `test(sync): add fake-COM unit tests for IRPComponent`.

### Task 5: IRPComponent integration tests

**Files:** Test `tests/integration/models/com/telelogic/rhapsody/core/test_irp_component.py`

- [ ] **Step 1:** Copy the IRPState integration skeleton with `META`-appropriate setup: `project.add_package` → `pkg.add_class` → `project.add_component(...)` (parent/setup calls only). Write:

```python
def test_add_configuration_and_find(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("CompPkg"))
    comp = test_project.add_component(self._unique("Component"))
    try:
        name = self._unique("Cfg")
        created = comp.add_configuration(name)
        assert created is not None
        found = comp.find_configuration(name)
        assert found is not None
        assert found.get_name() == name
        assert found in list(comp.get_configurations())
    finally:
        comp.delete_from_project()

def test_file_and_folder_creation(self, test_project: IRPProject) -> None:
    comp = test_project.add_component(self._unique("FileComp"))
    try:
        f = comp.add_file(self._unique("File.cpp"))
        folder = comp.add_folder(self._unique("include"))
        assert f is not None and folder is not None
        assert f.get_name() in [item.get_name() for item in comp.get_files()]
    finally:
        comp.delete_from_project()

def test_nested_component_creation(self, test_project: IRPProject) -> None:
    comp = test_project.add_component(self._unique("ParentComp"))
    try:
        child = comp.add_nested_component(self._unique("ChildComp"))
        assert child is not None
        assert child.get_name() in [c.get_name() for c in comp.get_nested_components()]
    finally:
        comp.delete_from_project()

def test_build_properties_round_trip(self, test_project: IRPProject) -> None:
    comp = test_project.add_component(self._unique("PropComp"))
    try:
        comp.build_type = "release"
        assert comp.build_type == "release"
        comp.include_path = "inc"
        assert comp.include_path == "inc"
        comp.libraries = "lib"
        assert comp.libraries == "lib"
    finally:
        comp.delete_from_project()
```

- [ ] **Step 2:** Add `pytest.raises(NotImplementedError)` tests for every `STUBS` row. **Step 3:** collect-only on non-Windows, full run on Windows. **Step 4:** commit with `test(sync): add live integration tests for IRPComponent`.

---

## IRPRelation (row 4 — do before IRPInstance — 31 owned members, `elements/relations/model_relation.py`)

### Task 6: IRPRelation unit tests

**Files:** Create `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_relation.py`; test `tests/unit/models/com/telelogic/rhapsody/core/test_irp_relation.py`

- [ ] **Step 1:** Harness with `META = "Relation"`, `WRAPPER = IRPRelation`, and:

```python
VOID_METHODS = [
    ("addQualifier", "add_qualifier", (_ARG,), (_ARG_COM,)),
    ("makeUnidirect", "make_unidirect", (), ()),
    ("removeQualifier", "remove_qualifier", (_ARG,), (_ARG_COM,)),
    ("setInverse", "set_inverse", ("role", "link"), ("role", "link")),
]
ELEMENT_METHODS = [
    ("getAssociationClass", "get_association_class", (), (), "AssociationClass"),
    ("getInverse", "get_inverse", (), (), "Relation"),
    ("getObjectAsObjectType", "get_object_as_object_type", (), (), "Class"),
    ("getOfClass", "get_of_class", (), (), "Class"),
    ("getOtherClass", "get_other_class", (), (), "Class"),
    ("getQualifierType", "get_qualifier_type", (), (), "Class"),
]
COLLECTION_METHODS = [
    ("getQualifiers", "get_qualifiers", (), (), "ModelElement"),
]
VALUE_METHODS = [
    ("getIsNavigable", "get_is_navigable", (), (), 1, 1),
    ("getIsSymmetric", "get_is_symmetric", (), (), 1, 1),
    ("getMultiplicity", "get_multiplicity", (), (), "0..*", "0..*"),
    ("getQualifier", "get_qualifier", (), (), "q", "q"),
    ("getRelationLabel", "get_relation_label", (), (), "label", "label"),
    ("getRelationLinkName", "get_relation_link_name", (), (), "link", "link"),
    ("getRelationRoleName", "get_relation_role_name", (), (), "role", "role"),
    ("getRelationType", "get_relation_type", (), (), "Association", "Association"),
    ("getVisibility", "get_visibility", (), (), "public", "public"),
    ("isTypelessObject", "is_typeless_object", (), (), 1, 1),
    ("setIsNavigable", "set_is_navigable", (1,), (1,), 1, 1),
    ("setMultiplicity", "set_multiplicity", ("1",), ("1",), "1", "1"),
    ("setQualifier", "set_qualifier", ("q",), ("q",), "q", "q"),
    ("setRelationLabel", "set_relation_label", ("l",), ("l",), "l", "l"),
    ("setRelationLinkName", "set_relation_link_name", ("ln",), ("ln",), "ln", "ln"),
    ("setRelationRoleName", "set_relation_role_name", ("r",), ("r",), "r", "r"),
    ("setRelationType", "set_relation_type", ("Association",), ("Association",), "Association", "Association"),
]
PROPERTIES = [
    ("ofClass", "of_class", None, None, True, None),
    ("otherClass", "other_class", None, None, True, None),
    ("qualifierType", "qualifier_type", None, None, True, None),
]
STUBS = []  # fill from irp_relation_api_report.md documented_unavailable
```

- [ ] **Steps 2–5:** as Task 2 with `relation`; commit `test(sync): add fake-COM unit tests for IRPRelation`.

### Task 7: IRPRelation integration tests

**Files:** Test `tests/integration/models/com/telelogic/rhapsody/core/test_irp_relation.py`

- [ ] **Step 1:** Setup uses `project.add_package`, `pkg.add_class`, then parent `add_relation_to` (parent method, setup only). Write:

```python
def test_multiplicity_and_label_round_trip(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("RelPkg"))
    a = pkg.add_class(self._unique("RelA"))
    b = pkg.add_class(self._unique("RelB"))
    try:
        rel = a.add_relation_to(b, "Association")
        rel.multiplicity = "0..*"
        assert rel.multiplicity == "0..*"
        rel.set_relation_label("owns")
        assert rel.get_relation_label() == "owns"
    finally:
        a.delete_from_project()
        b.delete_from_project()

def test_of_class_and_other_class(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("RelPkg2"))
    a = pkg.add_class(self._unique("RelC"))
    b = pkg.add_class(self._unique("RelD"))
    try:
        rel = a.add_relation_to(b, "Association")
        assert rel.get_of_class() is not None
        assert rel.get_other_class() is not None
    finally:
        a.delete_from_project()
        b.delete_from_project()

def test_qualifier_round_trip(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("QualPkg"))
    a = pkg.add_class(self._unique("QualA"))
    b = pkg.add_class(self._unique("QualB"))
    try:
        rel = a.add_relation_to(b, "Association")
        rel.set_qualifier("key")
        assert rel.get_qualifier() == "key"
    finally:
        a.delete_from_project()
        b.delete_from_project()
```

- [ ] **Steps 2–4:** stubs, collect-only/live run, commit `test(sync): add live integration tests for IRPRelation`.

---

## IRPInstance (row 3 — 13 owned members, `elements/relations/model_instance.py`)

Dependency: Task 6 must be committed first; inherited `RPRelation` members are setup-only, never asserted here.

### Task 8: IRPInstance unit tests

**Files:** Create `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_instance.py`; test `tests/unit/models/com/telelogic/rhapsody/core/test_irp_instance.py`

- [ ] **Step 1:** Harness with `META = "Instance"`, `WRAPPER = IRPInstance`, and:

```python
VOID_METHODS = [
    ("setExplicit", "set_explicit", (), ()),
    ("setImplicit", "set_implicit", (), ()),
    ("setAttributeValue", "set_attribute_value", ("attr", "value"), ("attr", "value")),
    ("setInitializerArgumentValue", "set_initializer_argument_value", ("arg", "value"), ("arg", "value")),
]
ELEMENT_METHODS = [
    ("addRelationToTheWhole", "add_relation_to_the_whole", ("Link",), ("Link",), "Relation"),
    ("getInstantiatedBy", "get_instantiated_by", (), (), "Operation"),
]
COLLECTION_METHODS = [
    ("getAllNestedElements", "get_all_nested_elements", (), (), "ModelElement"),
    ("getInLinks", "get_in_links", (), (), "Relation"),
    ("getListOfInitializerArguments", "get_list_of_initializer_arguments", (), (), "Argument"),
    ("getOutLinks", "get_out_links", (), (), "Relation"),
]
VALUE_METHODS = [
    ("getAttributeValue", "get_attribute_value", ("attr",), ("attr",), "value", "value"),
    ("updateContainedDiagramsOnServer", "update_contained_diagrams_on_server", (1,), (1,), 1, 1),
]
PROPERTIES = [
    ("instantiatedBy", "instantiated_by", None, None, True, None),
]
STUBS = []  # fill from irp_instance_api_report.md documented_unavailable
```

- [ ] **Steps 2–5:** as Task 2 with `instance`; commit `test(sync): add fake-COM unit tests for IRPInstance`.

### Task 9: IRPInstance integration tests

**Files:** Test `tests/integration/models/com/telelogic/rhapsody/core/test_irp_instance.py`

- [ ] **Step 1:** Setup via `project.add_package` → `pkg.add_class` → `parent.add_part(...)` (inherited, setup only). Write:

```python
def test_part_attribute_value_round_trip(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("InstPkg"))
    klass = pkg.add_class(self._unique("InstClass"))
    try:
        part = klass.add_part(self._unique("part"))
        part.set_attribute_value("attr", "value")
        assert part.get_attribute_value("attr") == "value"
    finally:
        klass.delete_from_project()

def test_part_initializer_argument(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("InstPkg2"))
    klass = pkg.add_class(self._unique("InstClass2"))
    try:
        part = klass.add_part(self._unique("part2"))
        part.set_initializer_argument_value("arg", "value")
        assert len(list(part.get_list_of_initializer_arguments())) >= 1
    finally:
        klass.delete_from_project()

def test_nested_elements_and_links(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("InstPkg3"))
    klass = pkg.add_class(self._unique("InstClass3"))
    try:
        part = klass.add_part(self._unique("part3"))
        assert list(part.get_all_nested_elements()) is not None
        assert list(part.get_in_links()) is not None
        assert list(part.get_out_links()) is not None
    finally:
        klass.delete_from_project()
```

- [ ] **Steps 2–4:** stubs, collect-only/live, commit `test(sync): add live integration tests for IRPInstance`.

---

## IRPFlow (row 5 — 17 owned members, `elements/activity/model_activity.py`)

Migrate only `RPFlow`; `RPFlowchart` / `RPFlowItem` / `RPObjectNode` stay in the legacy module.

### Task 10: IRPFlow unit tests

**Files:** Create `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_flow.py`; test `tests/unit/models/com/telelogic/rhapsody/core/test_irp_flow.py`

- [ ] **Step 1:** Harness with `META = "Flow"`, `WRAPPER = IRPFlow`, and:

```python
VOID_METHODS = [
    ("addConveyed", "add_conveyed", (_ARG,), (_ARG_COM,)),
    ("removeConveyed", "remove_conveyed", (_ARG,), (_ARG_COM,)),
]
ELEMENT_METHODS = [
    ("getEnd1", "get_end1", (), (), "ModelElement"),
    ("getEnd1Port", "get_end1_port", (), (), "Port"),
    ("getEnd1SysMLPort", "get_end1_sysml_port", (), (), "SysMLPort"),
    ("getEnd2", "get_end2", (), (), "ModelElement"),
    ("getEnd2Port", "get_end2_port", (), (), "Port"),
    ("getEnd2SysMLPort", "get_end2_sysml_port", (), (), "SysMLPort"),
]
COLLECTION_METHODS = [
    ("getConveyed", "get_conveyed", (), (), "ModelElement"),
]
VALUE_METHODS = [
    ("getDirection", "get_direction", (), (), "in", "in"),
    ("setDirection", "set_direction", ("out",), ("out",), "out", "out"),
]
PROPERTIES = [
    ("end1", "end1", None, None, True, None),
    ("end2", "end2", None, None, True, None),
    ("direction", "direction", "in", "in", True, "out"),
]
STUBS = []  # fill from irp_flow_api_report.md documented_unavailable
```

- [ ] **Steps 2–5:** as Task 2 with `flow`; commit `test(sync): add fake-COM unit tests for IRPFlow`.

### Task 11: IRPFlow integration tests

**Files:** Test `tests/integration/models/com/telelogic/rhapsody/core/test_irp_flow.py`

- [ ] **Step 1:** Setup via a real activity/operation pair, then parent `add_flow(...)` (parent, setup only):

```python
def test_flow_end_direction_round_trip(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("FlowPkg"))
    klass = pkg.add_class(self._unique("FlowClass"))
    try:
        op = klass.add_operation(self._unique("flowOp"))
        flow = op.add_flow()
        flow.direction = "out"
        assert flow.direction == "out"
        assert flow.get_end1() is not None or flow.get_end2() is not None
    finally:
        klass.delete_from_project()

def test_flow_conveyed_elements(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("FlowPkg2"))
    klass = pkg.add_class(self._unique("FlowClass2"))
    try:
        op = klass.add_operation(self._unique("flowOp2"))
        flow = op.add_flow()
        item = pkg.add_class(self._unique("Conveyed"))
        flow.add_conveyed(item)
        assert item in list(flow.get_conveyed())
        flow.remove_conveyed(item)
        assert item not in list(flow.get_conveyed())
    finally:
        klass.delete_from_project()
```

- [ ] **Steps 2–4:** stubs, collect-only/live, commit `test(sync): add live integration tests for IRPFlow`.

---

## IRPStatechart (row 6 — 32 owned members, `elements/classifiers/model_statechart.py`)

Already extends the synced `IRPClass`; the JavaDoc has 32 owned rows (one more than the TODO's 31 — trust the HTML).

### Task 12: IRPStatechart unit tests

**Files:** Create `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_statechart.py`; test `tests/unit/models/com/telelogic/rhapsody/core/test_irp_statechart.py`

- [ ] **Step 1:** Harness with `META = "Statechart"`, `WRAPPER = IRPStatechart`, and:

```python
VOID_METHODS = [
    ("closeDiagram", "close_diagram", (), ()),
    ("createGraphics", "create_graphics", (), ()),
    ("deleteState", "delete_state", (_ARG,), (_ARG_COM,)),
    ("overrideInheritance", "override_inheritance", (), ()),
    ("setAsMainBehavior", "set_as_main_behavior", (), ()),
    ("unoverrideInheritance", "unoverride_inheritance", (), ()),
]
ELEMENT_METHODS = [
    ("addNewAcceptEventAction", "add_new_accept_event_action", ("Evt", IRPState), ("Evt", None), "AcceptEventAction"),
    ("addNewAcceptTimeEvent", "add_new_accept_time_event", ("Tm", IRPState), ("Tm", None), "AcceptTimeEvent"),
    ("addFreeShapeByType", "add_free_shape_by_type", ("Shape", None, None), ("Shape", None, None), "GraphElement"),
    ("addImage", "add_image", ("pic.png", 1, 2, 3, 4), ("pic.png", 1, 2, 3, 4), "GraphElement"),
    ("addTextBox", "add_text_box", ("text", 1, 2, 3, 4), ("text", 1, 2, 3, 4), "GraphElement"),
    ("openDiagramView", "open_diagram_view", (), (), "AXViewCtrl"),
]
COLLECTION_METHODS = [
    ("getAllTriggers", "get_all_triggers", (), (), "InterfaceItem"),
    ("getElementsInDiagram", "get_elements_in_diagram", (), (), "ModelElement"),
    ("getGraphicalElements", "get_graphical_elements", (), (), "GraphElement"),
    ("getPictureAs", "get_picture_as", ("f", "png", 1, None), ("f", "png", 1, None), "ModelElement"),
    ("getPictureAsDividedMetafiles", "get_picture_as_divided_metafiles", ("f",), ("f",), "ModelElement"),
    ("getPicturesWithImageMap", "get_pictures_with_image_map", ("f", None), ("f", None), "ModelElement"),
]
VALUE_METHODS = [
    ("findTrigger", "find_trigger", (_ARG,), (_ARG_COM,), 1, 1),
    ("getIsMainBehavior", "get_is_main_behavior", (), (), 1, 1),
    ("getIsOverridden", "get_is_overridden", (), (), 1, 1),
    ("populateDiagram", "populate_diagram", (None, None, "content"), (None, None, "content"), 1, 1),
]
PROPERTIES = [
    ("inheritsFrom", "inherits_from", None, None, False, None),
    ("itsClass", "its_class", None, None, False, None),
    ("rootState", "root_state", None, None, False, None),
    ("statechartDiagram", "statechart_diagram", None, None, False, None),
    ("showDiagramFrame", "show_diagram_frame", 1, 1, True, 0),
]
STUBS = []  # fill from irp_statechart_api_report.md documented_unavailable
```

- [ ] **Steps 2–5:** as Task 2 with `statechart`; commit `test(sync): add fake-COM unit tests for IRPStatechart`.

### Task 13: IRPStatechart integration tests

**Files:** Test `tests/integration/models/com/telelogic/rhapsody/core/test_irp_statechart.py`

- [ ] **Step 1:** Setup via `project.add_package` → `pkg.add_class` → `klass.add_statechart(...)` (parent, setup only). Write:

```python
def test_root_state_and_graphical_elements(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("SCPkg"))
    klass = pkg.add_class(self._unique("SCClass"))
    sc = klass.add_statechart(self._unique("Statechart"))
    try:
        root = sc.root_state
        assert root is not None
        assert isinstance(root, IRPState)
        assert list(sc.get_graphical_elements()) is not None
    finally:
        sc.delete_from_project()

def test_main_behavior_flag(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("SCPkg2"))
    klass = pkg.add_class(self._unique("SCClass2"))
    sc = klass.add_statechart(self._unique("Statechart2"))
    try:
        sc.set_as_main_behavior()
        assert sc.get_is_main_behavior() == 1
    finally:
        sc.delete_from_project()

def test_diagram_lifecycle(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("SCPkg3"))
    klass = pkg.add_class(self._unique("SCClass3"))
    sc = klass.add_statechart(self._unique("Statechart3"))
    try:
        assert sc.statechart_diagram is not None
        sc.create_graphics()
        assert list(sc.get_elements_in_diagram()) is not None
        sc.close_diagram()
    finally:
        sc.delete_from_project()
```

- [ ] **Steps 2–4:** stubs, collect-only/live, commit `test(sync): add live integration tests for IRPStatechart`.

---

## IRPDiagram (row 7 — 33 owned members, `elements/diagrams/model_diagrams.py`)

Migrate only `RPDiagram`; leaf diagram wrappers stay for a later group.

### Task 14: IRPDiagram unit tests

**Files:** Create `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_diagram.py`; test `tests/unit/models/com/telelogic/rhapsody/core/test_irp_diagram.py`

- [ ] **Step 1:** Harness with `META = "Diagram"`, `WRAPPER = IRPDiagram`, and:

```python
VOID_METHODS = [
    ("closeDiagram", "close_diagram", (), ()),
    ("openDiagram", "open_diagram", (), ()),
    ("populateDiagram", "populate_diagram", (None, None, "content"), (None, None, "content")),
    ("rearrangePorts", "rearrange_ports", (None,), (None,)),
    ("removeGraphElements", "remove_graph_elements", (None,), (None,)),
]
ELEMENT_METHODS = [
    ("addFreeShapeByType", "add_free_shape_by_type", ("Shape", None, None), ("Shape", None, None), "GraphElement"),
    ("addImage", "add_image", ("pic.png", 1, 2, 3, 4), ("pic.png", 1, 2, 3, 4), "GraphElement"),
    ("addTextBox", "add_text_box", ("text", 1, 2, 3, 4), ("text", 1, 2, 3, 4), "GraphElement"),
    ("createDiagramView", "create_diagram_view", (_ARG, None), (_ARG_COM, None), "Diagram"),
    ("openDiagramView", "open_diagram_view", (), (), "AXViewCtrl"),
]
COLLECTION_METHODS = [
    ("getCorrespondingGraphicElements", "get_corresponding_graphic_elements", (_ARG,), (_ARG_COM,), "GraphElement"),
    ("getCustomViews", "get_custom_views", (), (), "ModelElement"),
    ("getDiagramViews", "get_diagram_views", (), (), "Diagram"),
    ("getElementsInDiagram", "get_elements_in_diagram", (), (), "ModelElement"),
    ("getGraphicalElements", "get_graphical_elements", (), (), "GraphElement"),
    ("getPictureAs", "get_picture_as", ("f", "png", 1, None), ("f", "png", 1, None), "ModelElement"),
    ("getPictureAsDividedMetafiles", "get_picture_as_divided_metafiles", ("f",), ("f",), "ModelElement"),
    ("getPicturesWithImageMap", "get_pictures_with_image_map", ("f", None), ("f", None), "ModelElement"),
]
VALUE_METHODS = [
    ("completeRelations", "complete_relations", (None, 1), (None, 1), 1, 1),
    ("getLastVisualizationModifiedTime", "get_last_visualization_modified_time", (), (), "t", "t"),
    ("isDiagramView", "is_diagram_view", (), (), 1, 1),
    ("isOpen", "is_open", (), (), 1, 1),
    ("isShowDiagramFrame", "is_show_diagram_frame", (), (), 1, 1),
    ("updateViewOnServer", "update_view_on_server", (1,), (1,), 1, 1),
]
PROPERTIES = [
    ("customViews", "custom_views", None, None, True, None),
    ("diagramViewOf", "diagram_view_of", None, None, False, None),
    ("showDiagramFrame", "show_diagram_frame", 1, 1, True, 0),
]
STUBS = []  # fill from irp_diagram_api_report.md documented_unavailable
```

- [ ] **Steps 2–5:** as Task 2 with `diagram`; commit `test(sync): add fake-COM unit tests for IRPDiagram`.

### Task 15: IRPDiagram integration tests

**Files:** Test `tests/integration/models/com/telelogic/rhapsody/core/test_irp_diagram.py`

- [ ] **Step 1:** Setup using a real class diagram created through parent methods; assert only owned members:

```python
def test_diagram_graphical_elements(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("DgmPkg"))
    klass = pkg.add_class(self._unique("DgmClass"))
    diagram = klass.add_class_diagram(self._unique("ClassDiagram"))
    try:
        assert list(diagram.get_graphical_elements()) is not None
        assert list(diagram.get_elements_in_diagram()) is not None
    finally:
        diagram.delete_from_project()

def test_diagram_open_close(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("DgmPkg2"))
    klass = pkg.add_class(self._unique("DgmClass2"))
    diagram = klass.add_class_diagram(self._unique("ClassDiagram2"))
    try:
        diagram.open_diagram()
        assert diagram.is_open() == 1
        diagram.close_diagram()
    finally:
        diagram.delete_from_project()

def test_diagram_view_properties(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("DgmPkg3"))
    klass = pkg.add_class(self._unique("DgmClass3"))
    diagram = klass.add_class_diagram(self._unique("ClassDiagram3"))
    try:
        diagram.show_diagram_frame = 1
        assert diagram.is_show_diagram_frame() == 1
        assert list(diagram.get_diagram_views()) is not None
    finally:
        diagram.delete_from_project()
```

- [ ] **Steps 2–4:** stubs, collect-only/live, commit `test(sync): add live integration tests for IRPDiagram`.

---

## IRPMessage (row 8 — 36 owned members, `elements/interactions/model_interactions.py`)

Only `RPFlow`... — specifically only `RPMessage` migrates; `RPEvent` / `RPTransition` etc. stay.

### Task 16: IRPMessage unit tests

**Files:** Create `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_message.py`; test `tests/unit/models/com/telelogic/rhapsody/core/test_irp_message.py`

- [ ] **Step 1:** Harness with `META = "Message"`, `WRAPPER = IRPMessage`, and:

```python
VOID_METHODS = [
    ("reroute", "reroute", (), ()),
    ("setActualParameterList", "set_actual_parameter_list", (None,), (None,)),
]
ELEMENT_METHODS = [
    ("addSourceExecutionOccurrence", "add_source_execution_occurrence", (), (), "ExecutionOccurrence"),
    ("addTargetExecutionOccurrence", "add_target_execution_occurrence", (), (), "ExecutionOccurrence"),
    ("getCommunicationConnection", "get_communication_connection", (), (), "AssociationRole"),
    ("getFlowPort", "get_flow_port", (), (), "SysMLPort"),
    ("getFormalInterfaceItem", "get_formal_interface_item", (), (), "InterfaceItem"),
    ("getFormalType", "get_formal_type", (), (), "ModelElement"),
    ("getPort", "get_port", (), (), "Port"),
    ("getSource", "get_source", (), (), "ClassifierRole"),
    ("getSourceExecutionOccurrence", "get_source_execution_occurrence", (), (), "ExecutionOccurrence"),
    ("getTarget", "get_target", (), (), "ClassifierRole"),
    ("getTargetExecutionOccurrence", "get_target_execution_occurrence", (), (), "ExecutionOccurrence"),
]
COLLECTION_METHODS = [
    ("getActualParameterList", "get_actual_parameter_list", (), (), "ModelElement"),
]
VALUE_METHODS = [
    ("getCondition", "get_condition", (), (), "cond", "cond"),
    ("getDurationConstraint", "get_duration_constraint", (), (), "d", "d"),
    ("getDurationObservation", "get_duration_observation", (), (), "o", "o"),
    ("getInvariant", "get_invariant", (), (), "inv", "inv"),
    ("getMessageType", "get_message_type", (), (), "call", "call"),
    ("getReturnValue", "get_return_value", (), (), "rv", "rv"),
    ("getSequenceNumber", "get_sequence_number", (), (), "1", "1"),
    ("getSignature", "get_signature", (), (), "sig", "sig"),
    ("getTimeConstraint", "get_time_constraint", (), (), "tc", "tc"),
    ("getTimeObservation", "get_time_observation", (), (), "to", "to"),
    ("getTimerValue", "get_timer_value", (), (), "tv", "tv"),
    ("setDurationConstraint", "set_duration_constraint", ("d",), ("d",), "d", "d"),
    ("setDurationObservation", "set_duration_observation", ("o",), ("o",), "o", "o"),
    ("setInvariant", "set_invariant", ("inv",), ("inv",), "inv", "inv"),
    ("setReturnValue", "set_return_value", ("rv",), ("rv",), "rv", "rv"),
    ("setTimeConstraint", "set_time_constraint", ("tc",), ("tc",), "tc", "tc"),
    ("setTimeObservation", "set_time_observation", ("to",), ("to",), "to", "to"),
    ("setTimerValue", "set_timer_value", ("tv",), ("tv",), "tv", "tv"),
]
PROPERTIES = [
    ("formalInterfaceItem", "formal_interface_item", None, None, True, None),
    ("formalType", "formal_type", None, None, True, None),
    ("port", "port", None, None, True, None),
    ("flowPort", "flow_port", None, None, True, None),
]
STUBS = []  # fill from irp_message_api_report.md documented_unavailable
```

- [ ] **Steps 2–5:** as Task 2 with `message`; commit `test(sync): add fake-COM unit tests for IRPMessage`.

### Task 17: IRPMessage integration tests

**Files:** Test `tests/integration/models/com/telelogic/rhapsody/core/test_irp_message.py`

- [ ] **Step 1:** Setup via a real collaboration + message through parent methods (setup only). Write:

```python
def test_message_signature_and_condition(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("MsgPkg"))
    klass = pkg.add_class(self._unique("MsgClass"))
    collab = test_project.add_collaboration(self._unique("MsgCollab"))
    try:
        msg = collab.add_message(klass.add_operation(self._unique("sig")).get_name(), "", None, None)
        msg.condition = "guard == 1"
        assert msg.get_condition() == "guard == 1"
        assert msg.get_signature() is not None
    finally:
        collab.delete_from_project()

def test_message_timing_values(self, test_project: IRPProject) -> None:
    collab = test_project.add_collaboration(self._unique("TimeCollab"))
    try:
        msg = collab.add_found_message(None)
        msg.set_time_constraint("t < 5")
        assert msg.get_time_constraint() == "t < 5"
        msg.set_timer_value("100ms")
        assert msg.get_timer_value() == "100ms"
    finally:
        collab.delete_from_project()

def test_execution_occurrences(self, test_project: IRPProject) -> None:
    collab = test_project.add_collaboration(self._unique("ExecCollab"))
    try:
        msg = collab.add_found_message(None)
        src = msg.add_source_executionOccurrence()
        assert src is not None
        assert msg.get_source_execution_occurrence() is not None
    finally:
        collab.delete_from_project()
```

- [ ] **Steps 2–4:** stubs, collect-only/live, commit `test(sync): add live integration tests for IRPMessage`.

---

## IRPTableLayout (row 9 — 50 owned members, `elements/graphics/model_graphics.py`)

Largest surface. Migrate only `RPTableLayout`; other graphics wrappers stay.

### Task 18: IRPTableLayout unit tests

**Files:** Create `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_table_layout.py`; test `tests/unit/models/com/telelogic/rhapsody/core/test_irp_table_layout.py`

- [ ] **Step 1:** Harness with `META = "TableLayout"`, `WRAPPER = IRPTableLayout`. `COLUMN_INDEX_METHODS` below are method-shaped getters/setters taking an `int Index` (JavaDoc preserves capitalized `Index`/`Property` parameter names, but the values are ordinary ints/strings).

```python
VOID_METHODS = [
    ("addColumn", "add_column", ("Entity", "Name", "NameCol"), ("Entity", "Name", "NameCol")),
    ("removeColumn", "remove_column", (1,), (1,)),
]
VALUE_METHODS = [
    ("addColumnEx", "add_column_ex", ("Entity", "Name", "NameCol", "Ctx"), ("Entity", "Name", "NameCol", "Ctx"), 1, 1),
    ("getColumnContext", "get_column_context", (1,), (1,), "ctx", "ctx"),
    ("getColumnCount", "get_column_count", (), (), 2, 2),
    ("getColumnDefaultWidth", "get_column_default_width", (1,), (1,), 120, 120),
    ("getColumnImplementationAllowNew", "get_column_implementation_allow_new", (1,), (1,), 1, 1),
    ("getColumnImplementationAllowSelect", "get_column_implementation_allow_select", (1,), (1,), 1, 1),
    ("getColumnImplementationCellType", "get_column_implementation_cell_type", (1,), (1,), "text", "text"),
    ("getColumnImplementationDisplayProperty", "get_column_implementation_display_property", (1,), (1,), "Name", "Name"),
    ("getColumnImplementationGetterCode", "get_column_implementation_getter_code", (1,), (1,), "get()", "get()"),
    ("getColumnImplementationImports", "get_column_implementation_imports", (1,), (1,), "import x", "import x"),
    ("getColumnImplementationPickerCode", "get_column_implementation_picker_code", (1,), (1,), "pick()", "pick()"),
    ("getColumnImplementationSetterCode", "get_column_implementation_setter_code", (1,), (1,), "set()", "set()"),
    ("getColumnName", "get_column_name", (1,), (1,), "NameCol", "NameCol"),
    ("getColumnProperty", "get_column_property", (1,), (1,), "Name", "Name"),
    ("getColumnType", "get_column_type", (1,), (1,), "Entity", "Entity"),
    ("getFromElementTypesUseQueryOrElementsList", "get_from_element_types_use_query_or_elements_list", (), (), 1, 1),
    ("getRelationTable", "get_relation_table", (), (), 1, 1),
    ("getToElementTypesUseQueryOrElementsList", "get_to_element_types_use_query_or_elements_list", (), (), 1, 1),
    ("setColumnContext", "set_column_context", (1, "ctx"), (1, "ctx"), "ctx", "ctx"),
    ("setColumnDefaultWidth", "set_column_default_width", (1, 120), (1, 120), 120, 120),
    ("setColumnImplementationAllowNew", "set_column_implementation_allow_new", (1, 1), (1, 1), 1, 1),
    ("setColumnImplementationAllowSelect", "set_column_implementation_allow_select", (1, 1), (1, 1), 1, 1),
    ("setColumnImplementationCellType", "set_column_implementation_cell_type", (1, "text"), (1, "text"), "text", "text"),
    ("setColumnImplementationDisplayProperty", "set_column_implementation_display_property", (1, "Name"), (1, "Name"), "Name", "Name"),
    ("setColumnImplementationGetterCode", "set_column_implementation_getter_code", (1, "get()"), (1, "get()"), "get()", "get()"),
    ("setColumnImplementationImports", "set_column_implementation_imports", (1, "import x"), (1, "import x"), "import x", "import x"),
    ("setColumnImplementationPickerCode", "set_column_implementation_picker_code", (1, "pick()"), (1, "pick()"), "pick()", "pick()"),
    ("setColumnImplementationSetterCode", "set_column_implementation_setter_code", (1, "set()"), (1, "set()"), "set()", "set()"),
    ("setColumnName", "set_column_name", (1, "NameCol"), (1, "NameCol"), "NameCol", "NameCol"),
    ("setColumnProperty", "set_column_property", (1, "Name"), (1, "Name"), "Name", "Name"),
    ("setColumnType", "set_column_type", (1, "Entity"), (1, "Entity"), "Entity", "Entity"),
    ("setFromElementTypesUseQueryOrElementsList", "set_from_element_types_use_query_or_elements_list", (1,), (1,), 1, 1),
    ("setToElementTypesUseQueryOrElementsList", "set_to_element_types_use_query_or_elements_list", (1,), (1,), 1, 1),
]
ELEMENT_METHODS = [
    ("getFromElementTypesQueryToUse", "get_from_element_types_query_to_use", (), (), "TableLayout"),
    ("getToElementTypesQueryToUse", "get_to_element_types_query_to_use", (), (), "TableLayout"),
]
COLLECTION_METHODS = [
    ("getColumns", "get_columns", (), (), "ModelElement"),
    ("getElementTypes", "get_element_types", (), (), "ModelElement"),
    ("getFromElementTypes", "get_from_element_types", (), (), "ModelElement"),
    ("getResultList", "get_result_list", (_ARG,), (_ARG_COM,), "ModelElement"),
    ("getToElementTypes", "get_to_element_types", (), (), "ModelElement"),
]
PROPERTIES = [
    ("collapseFirstColumn", "collapse_first_column", 1, 1, True, 0),
    ("relationTable", "relation_table", 1, 1, True, 0),
    ("fromElementTypes", "from_element_types", None, None, True, None),
    ("fromElementTypesQueryToUse", "from_element_types_query_to_use", None, None, True, None),
    ("toElementTypes", "to_element_types", None, None, True, None),
    ("toElementTypesQueryToUse", "to_element_types_query_to_use", None, None, True, None),
]
STUBS = []  # fill from irp_table_layout_api_report.md documented_unavailable
```

- [ ] **Steps 2–5:** as Task 2 with `table_layout`; commit `test(sync): add fake-COM unit tests for IRPTableLayout`.

### Task 19: IRPTableLayout integration tests

**Files:** Test `tests/integration/models/com/telelogic/rhapsody/core/test_irp_table_layout.py`

- [ ] **Step 1:** Setup via a real table layout created through parent methods (setup only). Write:

```python
def test_column_add_remove_and_reads(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("TblPkg"))
    layout = pkg.add_table_layout(self._unique("Layout"))
    try:
        layout.add_column("Entity", "Name", self._unique("NameCol"))
        assert layout.get_column_count() >= 1
        assert layout.get_column_name(1) != ""
        layout.remove_column(1)
    finally:
        layout.delete_from_project()

def test_column_metadata_round_trip(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("TblPkg2"))
    layout = pkg.add_table_layout(self._unique("Layout2"))
    try:
        layout.add_column("Entity", "Name", "NameCol")
        layout.set_column_context(1, "Context")
        assert layout.get_column_context(1) == "Context"
        layout.set_column_default_width(1, 150)
        assert layout.get_column_default_width(1) == 150
        layout.set_column_property(1, "Name")
        assert layout.get_column_property(1) == "Name"
    finally:
        layout.delete_from_project()

def test_layout_flags(self, test_project: IRPProject) -> None:
    pkg = self._create_package(test_project, self._unique("TblPkg3"))
    layout = pkg.add_table_layout(self._unique("Layout3"))
    try:
        layout.collapse_first_column = 1
        assert layout.collapse_first_column == 1
        assert list(layout.get_columns()) is not None
    finally:
        layout.delete_from_project()
```

- [ ] **Steps 2–4:** stubs, collect-only/live, commit `test(sync): add live integration tests for IRPTableLayout`.

---

## IRPCollaboration (row 10 — 40 owned members, `elements/containment/model_collaboration.py`)

JavaDoc has 40 owned rows (one more than the TODO's 39): `getMessagePoints()` and `getMessagePoints(IRPClassifierRole)` are both real overloads. Both get tests.

### Task 20: IRPCollaboration unit tests

**Files:** Create `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collaboration.py`; test `tests/unit/models/com/telelogic/rhapsody/core/test_irp_collaboration.py`

- [ ] **Step 1:** Harness with `META = "Collaboration"`, `WRAPPER = IRPCollaboration`, and:

```python
ELEMENT_METHODS = [
    ("addActionBlock", "add_action_block", (_ARG,), (_ARG_COM,), "ActionBlock"),
    ("addCancelledTimeout", "add_cancelled_timeout", (_ARG,), (_ARG_COM,), "Message"),
    ("addClassifierRole", "add_classifier_role", ("Role", IRPModelElement), ("Role", None), "ClassifierRole"),
    ("addClassifierRoleByName", "add_classifier_role_by_name", ("Role", "Class"), ("Role", "Class"), "ClassifierRole"),
    ("addClassifierRoleForInstance", "add_classifier_role_for_instance", (_ARG,), (_ARG_COM,), "ClassifierRole"),
    ("addConditionMark", "add_condition_mark", (_ARG,), (_ARG_COM,), "Message"),
    ("addCtor", "add_ctor", (_ARG, "", _ARG, _ARG), (_ARG_COM, "", _ARG_COM, _ARG_COM), "Message"),
    ("addDataFlow", "add_data_flow", (_ARG, "v", _ARG, _ARG), (_ARG_COM, "v", _ARG_COM, _ARG_COM), "Message"),
    ("addDestructionEvent", "add_destruction_event", (_ARG,), (_ARG_COM,), "Message"),
    ("addDtor", "add_dtor", (_ARG, "", _ARG, _ARG), (_ARG_COM, "", _ARG_COM, _ARG_COM), "Message"),
    ("addDurationConstraint", "add_duration_constraint", ("d", _ARG, _ARG), ("d", None, None), "Message"),
    ("addDurationObservation", "add_duration_observation", ("o", _ARG, _ARG), ("o", None, None), "Message"),
    ("addFoundMessage", "add_found_message", (_ARG,), (_ARG_COM,), "Message"),
    ("addInteractionOccurrence", "add_interaction_occurrence", (), (), "InteractionOccurrence"),
    ("addInteractionOperator", "add_interaction_operator", (), (), "InteractionOperator"),
    ("addLostMessage", "add_lost_message", (_ARG,), (_ARG_COM,), "Message"),
    ("addMessage", "add_message", (_ARG, "", _ARG, _ARG), (_ARG_COM, "", _ARG_COM, _ARG_COM), "Message"),
    ("addReplyMessage", "add_reply_message", (_ARG, "", _ARG, _ARG), (_ARG_COM, "", _ARG_COM, _ARG_COM), "Message"),
    ("addStateInvariant", "add_state_invariant", ("inv", IRPModelElement), ("inv", None), "Message"),
    ("addSystemBorder", "add_system_border", (), (), "ClassifierRole"),
    ("addTimeConstraint", "add_time_constraint", ("tc", IRPModelElement), ("tc", None), "Message"),
    ("addTimeInterval", "add_time_interval", (_ARG,), (_ARG_COM,), "Message"),
    ("addTimeObservation", "add_time_observation", ("to", IRPModelElement), ("to", None), "Message"),
    ("addTimeout", "add_timeout", (_ARG, "", _ARG, _ARG), (_ARG_COM, "", _ARG_COM, _ARG_COM), "Message"),
    ("generateSequence", "generate_sequence", ("Seq", IRPModelElement), ("Seq", None), "SequenceDiagram"),
    ("getActivator", "get_activator", (_ARG,), (_ARG_COM,), "Message"),
    ("getPredecessor", "get_predecessor", (_ARG,), (_ARG_COM,), "Message"),
    ("getSuccessor", "get_successor", (_ARG,), (_ARG_COM,), "Message"),
]
COLLECTION_METHODS = [
    ("getAssociations", "get_associations", (), (), "ModelElement"),
    ("getClassifier", "get_classifier", (), (), "ModelElement"),
    ("getConcurrentGroup", "get_concurrent_group", (_ARG,), (_ARG_COM,), "ModelElement"),
    ("getExecutionOccurrences", "get_execution_occurrences", (), (), "ExecutionOccurrence"),
    ("getInteractionOccurrences", "get_interaction_occurrences", (), (), "InteractionOccurrence"),
    ("getInteractionOperators", "get_interaction_operators", (), (), "InteractionOperator"),
    ("getMessagePoints", "get_message_points", (), (), "ModelElement"),
    ("getMessagePoints", "get_message_points_for_classifier", (_ARG,), (_ARG_COM,), "ModelElement"),
    ("getMessages", "get_messages", (), (), "Message"),
]
VALUE_METHODS = [
    ("getActivationCondition", "get_activation_condition", (), (), "cond", "cond"),
    ("getActivationMode", "get_activation_mode", (), (), "mode", "mode"),
    ("getMode", "get_mode", (), (), "mode", "mode"),
]
PROPERTIES = [
    ("activationCondition", "activation_condition", "cond", "cond", False, None),
    ("activationMode", "activation_mode", "mode", "mode", False, None),
    ("mode", "mode", "mode", "mode", False, None),
]
STUBS = []  # fill from irp_collaboration_api_report.md documented_unavailable
```

- [ ] **Step 2:** Add a dedicated arity test for the overload pair (the shared harness uses `ids=row[1]`, so give the two rows distinct Python names as above):

```python
def test_message_points_overloads_keep_distinct_arity() -> None:
    fake = make_fake_element("Collaboration")
    wrapper = IRPCollaboration(fake)
    list(wrapper.get_message_points())
    fake.getMessagePoints.assert_any_call()
    role = make_fake_element("ClassifierRole", properties={"name": "r"})
    list(wrapper.get_message_points_for_classifier(IRPModelElement.wrap(role)))
    fake.getMessagePoints.assert_any_call(role)
```

- [ ] **Steps 3–6:** run red, implement (overloads share one COM member with different arity — bind each Python name to the exact catalog signature), green with 100% coverage, commit `test(sync): add fake-COM unit tests for IRPCollaboration`.

### Task 21: IRPCollaboration integration tests

**Files:** Test `tests/integration/models/com/telelogic/rhapsody/core/test_irp_collaboration.py`

- [ ] **Step 1:** Setup via `project.add_collaboration(...)` (real object); write:

```python
def test_message_creation_and_retrieval(self, test_project: IRPProject) -> None:
    collab = test_project.add_collaboration(self._unique("Collab"))
    try:
        msg = collab.add_found_message(None)
        assert msg is not None
        assert msg in list(collab.get_messages())
    finally:
        collab.delete_from_project()

def test_classifier_role_creation(self, test_project: IRPProject) -> None:
    collab = test_project.add_collaboration(self._unique("CollabRoles"))
    try:
        role = collab.add_classifier_role(self._unique("Role"), "Class")
        assert role is not None
        assert role in list(collab.get_classifier())
    finally:
        collab.delete_from_project()

def test_message_points_overloads_live(self, test_project: IRPProject) -> None:
    collab = test_project.add_collaboration(self._unique("CollabPoints"))
    try:
        role = collab.add_classifier_role(self._unique("RoleP"), "Class")
        assert list(collab.get_message_points()) is not None
        assert list(collab.get_message_points_for_classifier(role)) is not None
    finally:
        collab.delete_from_project()

def test_activation_properties(self, test_project: IRPProject) -> None:
    collab = test_project.add_collaboration(self._unique("CollabMode"))
    try:
        assert collab.activation_mode is not None
        assert collab.mode is not None
    finally:
        collab.delete_from_project()
```

- [ ] **Steps 2–4:** stubs, collect-only/live, commit `test(sync): add live integration tests for IRPCollaboration`.

---

## Final cross-interface gate (still test-design scope)

- [ ] Run all 10 focused unit files with coverage in one command and confirm each wrapper module reports 100% statements and branches:

```bash
for X in state component instance relation flow statechart diagram message table_layout collaboration; do
  uv run pytest "tests/unit/models/com/telelogic/rhapsody/core/test_irp_${X}.py" -q -o addopts= \
    --cov="rhapsody_cli.models.com.telelogic.rhapsody.core.irp_${X}" --cov-report=term-missing || exit 1
done
```

- [ ] Run the full unit suite: `uv run pytest tests/unit -q -o addopts=` → all pass.
- [ ] On non-Windows: collection-only for all 10 integration files. On Windows: full integration suite with authentic data, recording pass/fail counts and the complete `NotImplementedError` list.
- [ ] Do NOT run `verify_sync.py` or edit SWR/RST docs in this plan — those are Steps 6–8 and stay open on `Group-unfinished-2.md`.

## Self-review notes

- **Spec coverage:** all 10 rows of `Group-unfinished-2.md` have a unit-test task and an integration-test task; Phase 0 addresses the catalog/report prerequisite stated in the file. Dependency order respected: IRPRelation (Task 6) before IRPInstance (Task 8).
- **Placeholder scan:** no TBD/TODO; every data row is concrete. The only values deferred by design are `STUBS` rows and the shape classification, both of which are produced by Phase 0's reports (external evidence that cannot exist offline) and governed by an explicit reconciliation procedure.
- **Type consistency:** Python API names are used identically in the harness data lists, wrapper implementation steps, and integration tests. `IRPState`, `IRPComponent`, `IRPRelation`, `IRPInstance`, `IRPFlow`, `IRPStatechart`, `IRPDiagram`, `IRPMessage`, `IRPTableLayout`, `IRPCollaboration` are the canonical class names throughout.
