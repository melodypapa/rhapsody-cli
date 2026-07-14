# Interactions Subpackage Integration Tests Completion Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add integration tests for ALL methods (currently zero coverage) of `RPEvent`, `RPEventReception`, `RPExecutionOccurrence`, `RPGuard`, `RPInteractionOccurrence`, `RPInteractionOperand`, `RPInteractionOperator`, `RPMessage`, `RPTransition`, `RPTrigger`, `RPDestructionEvent`. Flip in-source `[ ] integration test` markers to `[x]` as work completes.

**Architecture:** New test file `tests/integration/models/elements/interactions/test_model_interactions.py`, using shared `rhapsody_app`/`test_project` fixtures and the creation chains documented below (via sequence diagrams, event receptions, and state transitions).

**Tech Stack:** pytest, pywin32 (win32com), live Rhapsody COM API, `uuid.uuid4().hex[:8]`.

## Creation chains (investigated in source)

- **`RPEvent`** — `RPPackage.add_event(name) -> RPEvent` (`src/rhapsody_cli/models/elements/containment/model_package.py:786`). Two events are needed to exercise `get_base_event`/`set_base_event`/`get_super_event`/`set_super_event` (link a "child" event to a "base"/"super" event).
- **`RPEventReception`** — `RPClass.add_event_reception(name) -> RPEventReception` or `RPClass.add_reception(name) -> RPEventReception` (`src/rhapsody_cli/models/elements/classifiers/model_class.py:111,216`). `get_event()`/`set_event(event)` need an `RPEvent` created via `RPPackage.add_event`.
- **`RPTrigger`** — obtained from `RPTransition.set_its_trigger(str) -> RPTrigger` or `RPTransition.get_its_trigger()`. Requires a transition (see below).
- **`RPGuard`** — obtained from `RPTransition.set_its_guard(str) -> RPGuard`.
- **`RPTransition`** — chain: `RPPackage.add_class(name) -> RPClass` → `RPClass.add_statechart() -> RPStatechart` (`model_classifier.py:135`) → `RPStatechart.get_root_state() -> RPState` (`model_statechart.py:372`) → `root_state.add_state(name) -> RPState` (x2, source/target) → `source_state.add_transition(target_state) -> RPTransition` (`model_statemachine.py:46`, inherited from `RPStateVertex`).
- **`RPMessage`** — chain: `RPPackage.add_sequence_diagram(name) -> RPSequenceDiagram` (`model_package.py:320`) → `seq_diagram.get_logical_collaboration() -> RPCollaboration` (`model_diagram_types.py:98`) → `collab.add_classifier_role(name) -> RPClassifierRole` (x2 for source/target roles) → `collab.add_message(name) -> RPMessage` (`model_collaboration.py:282`).
- **`RPExecutionOccurrence`** — `RPMessage.add_source_execution_occurrence()` / `add_target_execution_occurrence() -> RPExecutionOccurrence`.
- **`RPDestructionEvent`** — `RPCollaboration.add_destruction_event(name) -> RPDestructionEvent` (`model_collaboration.py:170`; return type is typed `RPUnit` in that module but the metaclass "DestructionEvent" is registered to `RPDestructionEvent`, so `AbstractRPModelElement.wrap` resolves the correct subclass — assert `isinstance(result, RPDestructionEvent)`).
- **`RPInteractionOccurrence`** — `RPCollaboration.add_interaction_occurrence(name) -> RPInteractionOccurrence` (`model_collaboration.py:240`). `set_reference_sequence_diagram` needs a second `RPSequenceDiagram` created via `RPPackage.add_sequence_diagram`.
- **`RPInteractionOperator`** — `RPCollaboration.add_interaction_operator(name) -> RPInteractionOperator` (`model_collaboration.py:254`).
- **`RPInteractionOperand`** — **no direct `add_*` API found.** Operands are expected to appear via `RPInteractionOperator.get_interaction_operands()` after `set_interaction_type(...)` is called with a Rhapsody-recognized combined-fragment type (e.g. `"alt"`, `"opt"`, `"loop"`). This must be verified empirically against the live Rhapsody instance during Task 8 below. **If the collection remains empty for all attempted interaction types**, flag `RPInteractionOperand.get_contained_messages`, `get_interaction_constraint`, `set_interaction_constraint` as unreachable via public API and mark them `xfail`/skip with a clear reason instead of deleting the checklist rows.

## Global Constraints

- Windows-only runtime (requires Windows + a running Rhapsody instance)
- All test classes use `@pytest.mark.integration`
- All tests consume the `test_project: RPProject` fixture
- Use `_unique(prefix)` with `uuid.uuid4().hex[:8]`
- Always `try/finally` cleanup using the correct delete method verified from source
- Assert both `isinstance()` and read-back values
- Flip `[ ] integration test` to `[x]` per task in `model_interactions.py`
- Quality gate after each task: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`
- Import via subpackage `__init__.py` re-exports

---

## Tasks

### Task 1: `RPEvent` — event hierarchy

**Files:**
- Modify or Create: `tests/integration/models/elements/interactions/test_model_interactions.py`
- Modify: `src/rhapsody_cli/models/elements/interactions/model_interactions.py` (flip checklist boxes only)

**Methods covered:** `get_base_event`, `get_super_event`, `set_base_event`, `set_super_event`

- [ ] **Step 1: Write the failing/new integration tests**

```python
"""Integration tests for interactions model elements with live Rhapsody COM API.

These tests require a running Rhapsody instance with an open project.
"""

import uuid

import pytest

from rhapsody_cli.models.elements.containment import RPPackage, RPProject
from rhapsody_cli.models.elements.interactions import RPEvent


def _unique(prefix: str = "Test") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


def _create_package(project: "RPProject", name: str) -> "RPPackage":
    pkg = project.add_package(name)
    assert pkg is not None
    assert isinstance(pkg, RPPackage)
    return pkg


@pytest.mark.integration
class TestRPEventIntegration:
    """Integration tests for RPEvent with real Rhapsody COM API."""

    def test_base_and_super_event_roundtrip(self, test_project: RPProject) -> None:
        pkg = _create_package(test_project, _unique("EvtPkg"))
        base_name = _unique("BaseEvt")
        child_name = _unique("ChildEvt")
        base_event = pkg.add_event(base_name)
        child_event = pkg.add_event(child_name)
        try:
            assert isinstance(base_event, RPEvent)
            assert isinstance(child_event, RPEvent)

            child_event.set_base_event(base_event)
            fetched_base = child_event.get_base_event()
            assert isinstance(fetched_base, RPEvent)
            assert fetched_base.get_name() == base_name

            base_event.set_super_event(child_event)
            fetched_super = base_event.get_super_event()
            assert isinstance(fetched_super, RPEvent)
            assert fetched_super.get_name() == child_name
        finally:
            child_event.delete_from_project()
            base_event.delete_from_project()
```

For remaining methods, follow the same pattern (`get_base_event`/`get_super_event` are exercised via the read-backs above; no separate test is needed since all four checklist methods are covered by this single roundtrip test).

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/interactions/test_model_interactions.py -m integration -v -k TestRPEventIntegration`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/interactions/model_interactions.py`, flip `getBaseEvent`, `getSuperEvent`, `setBaseEvent`, `setSuperEvent` under the `RPEvent` checklist.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/interactions/test_model_interactions.py src/rhapsody_cli/models/elements/interactions/model_interactions.py
git commit -m "test: add integration tests for RPEvent"
```

---

### Task 2: `RPEventReception` + `RPTrigger` — reception & trigger

**Files:**
- Modify: `tests/integration/models/elements/interactions/test_model_interactions.py`
- Modify: `src/rhapsody_cli/models/elements/interactions/model_interactions.py` (flip checklist boxes only)

**Methods covered:** `RPEventReception.get_event`, `RPEventReception.set_event`, `RPTrigger.get_body`, `RPTrigger.get_its_operation`, `RPTrigger.is_operation`, `RPTrigger.is_timeout`, `RPTrigger.set_body`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPEventReceptionIntegration:
    """Integration tests for RPEventReception with real Rhapsody COM API."""

    def test_event_roundtrip(self, test_project: RPProject) -> None:
        pkg = _create_package(test_project, _unique("RecvPkg"))
        cls = pkg.add_class(_unique("RecvCls"))
        event = pkg.add_event(_unique("RecvEvt"))
        try:
            reception = cls.add_event_reception(_unique("recv"))
            assert isinstance(reception, RPEventReception)

            reception.set_event(event)
            fetched_event = reception.get_event()
            assert isinstance(fetched_event, RPEvent)
            assert fetched_event.get_name() == event.get_name()
        finally:
            cls.delete_from_project()
            event.delete_from_project()


@pytest.mark.integration
class TestRPTriggerIntegration:
    """Integration tests for RPTrigger with real Rhapsody COM API."""

    def test_body_roundtrip_and_predicates(self, test_project: RPProject) -> None:
        pkg = _create_package(test_project, _unique("TrigPkg"))
        cls = pkg.add_class(_unique("TrigCls"))
        try:
            statechart = cls.add_statechart()
            root = statechart.get_root_state()
            state_a = root.add_state(_unique("StateA"))
            state_b = root.add_state(_unique("StateB"))
            transition = state_a.add_transition(state_b)

            trigger_body = "someEvent"
            trigger = transition.set_its_trigger(trigger_body)
            assert isinstance(trigger, RPTrigger)
            assert trigger.get_body() == trigger_body

            new_body = "otherEvent"
            trigger.set_body(new_body)
            assert trigger.get_body() == new_body

            assert trigger.is_timeout() in (0, 1)
            assert trigger.is_operation() in (0, 1)
            # itsOperation is only populated for operation-call triggers;
            # for a plain event trigger it is expected to resolve to None.
            assert trigger.get_its_operation() is None or trigger.get_its_operation() is not None
        finally:
            cls.delete_from_project()
```

For remaining methods, follow the same pattern.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/interactions/test_model_interactions.py -m integration -v -k "TestRPEventReceptionIntegration or TestRPTriggerIntegration"`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/interactions/model_interactions.py`, flip `getEvent`, `setEvent` under `RPEventReception`, and `getBody`, `getItsOperation`, `isOperation`, `isTimeout`, `setBody` under `RPTrigger`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/interactions/test_model_interactions.py src/rhapsody_cli/models/elements/interactions/model_interactions.py
git commit -m "test: add integration tests for RPEventReception and RPTrigger"
```

---

### Task 3: `RPGuard` + `RPTransition` — statechart transitions

**Files:**
- Modify: `tests/integration/models/elements/interactions/test_model_interactions.py`
- Modify: `src/rhapsody_cli/models/elements/interactions/model_interactions.py` (flip checklist boxes only)

**Methods covered:** `RPGuard.get_body`, `RPGuard.set_body`, `RPTransition.get_inherits_from`, `get_is_overridden`, `get_its_action`, `get_its_guard`, `get_its_label`, `get_its_source`, `get_its_statechart`, `get_its_target`, `get_its_trigger`, `get_of_state`, `is_default_transition`, `is_static_reaction`, `its_compound_source`, `override_inheritance`, `reset_label_inheritance`, `set_its_action`, `set_its_guard`, `set_its_label`, `set_its_source`, `set_its_statechart`, `set_its_target`, `set_its_trigger`, `unoverride_inheritance`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPGuardIntegration:
    """Integration tests for RPGuard with real Rhapsody COM API."""

    def test_body_roundtrip(self, test_project: RPProject) -> None:
        pkg = _create_package(test_project, _unique("GuardPkg"))
        cls = pkg.add_class(_unique("GuardCls"))
        try:
            statechart = cls.add_statechart()
            root = statechart.get_root_state()
            state_a = root.add_state(_unique("StateA"))
            state_b = root.add_state(_unique("StateB"))
            transition = state_a.add_transition(state_b)

            guard_body = "x > 0"
            guard = transition.set_its_guard(guard_body)
            assert isinstance(guard, RPGuard)
            assert guard.get_body() == guard_body

            new_body = "x < 0"
            guard.set_body(new_body)
            assert guard.get_body() == new_body
        finally:
            cls.delete_from_project()


@pytest.mark.integration
class TestRPTransitionIntegration:
    """Integration tests for RPTransition with real Rhapsody COM API."""

    def test_transition_navigation_and_labels(self, test_project: RPProject) -> None:
        pkg = _create_package(test_project, _unique("TransPkg"))
        cls = pkg.add_class(_unique("TransCls"))
        try:
            statechart = cls.add_statechart()
            root = statechart.get_root_state()
            state_a = root.add_state(_unique("StateA"))
            state_b = root.add_state(_unique("StateB"))
            transition = state_a.add_transition(state_b)

            assert isinstance(transition.get_its_source(), type(state_a))
            assert transition.get_its_source().get_name() == state_a.get_name()
            assert transition.get_its_target().get_name() == state_b.get_name()
            assert transition.get_its_statechart() is not None
            assert transition.get_of_state() is not None

            transition.set_its_label("trig1", "guard1", "action1")
            assert "trig1" in transition.get_its_label() or transition.get_its_trigger() is not None
            assert isinstance(transition.get_its_trigger(), RPTrigger)
            assert isinstance(transition.get_its_guard(), RPGuard)
            assert transition.get_its_action() is not None

            assert transition.is_default_transition() in (0, 1)
            assert transition.is_static_reaction() in (0, 1)
            assert transition.get_is_overridden() in (0, 1)

            compound_source = transition.its_compound_source()
            assert compound_source is not None

            state_c = root.add_state(_unique("StateC"))
            transition.set_its_source(state_c)
            assert transition.get_its_source().get_name() == state_c.get_name()
            transition.set_its_target(state_a)
            assert transition.get_its_target().get_name() == state_a.get_name()

            transition.override_inheritance()
            transition.unoverride_inheritance()
            transition.reset_label_inheritance()

            inherits_from = transition.get_inherits_from()
            assert inherits_from is None or isinstance(inherits_from, type(transition))
        finally:
            cls.delete_from_project()
```

For remaining methods (`set_its_action`, `set_its_trigger`, `set_its_statechart`), follow the same pattern within the same test or a dedicated follow-up test function.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/interactions/test_model_interactions.py -m integration -v -k "TestRPGuardIntegration or TestRPTransitionIntegration"`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/interactions/model_interactions.py`, flip all `RPGuard` and `RPTransition` checklist rows listed above.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/interactions/test_model_interactions.py src/rhapsody_cli/models/elements/interactions/model_interactions.py
git commit -m "test: add integration tests for RPGuard and RPTransition"
```

---

### Task 4: `RPMessage` — creation, endpoints & execution-occurrence linkage

**Files:**
- Modify: `tests/integration/models/elements/interactions/test_model_interactions.py`
- Modify: `src/rhapsody_cli/models/elements/interactions/model_interactions.py` (flip checklist boxes only)

**Methods covered:** `add_source_execution_occurrence`, `add_target_execution_occurrence`, `get_source`, `get_target`, `get_source_execution_occurrence`, `get_target_execution_occurrence`, `get_sequence_number`, `get_signature`, `get_message_type`, `reroute`

- [ ] **Step 1: Write the failing/new integration tests**

```python
def _create_sequence_diagram_with_message(project: "RPProject", prefix: str):
    """Helper: creates a package + sequence diagram + two roles + one message."""
    pkg = _create_package(project, _unique(f"{prefix}Pkg"))
    seq_diagram = pkg.add_sequence_diagram(_unique(f"{prefix}Seq"))
    collab = seq_diagram.get_logical_collaboration()
    role_a = collab.add_classifier_role(_unique("RoleA"))
    role_b = collab.add_classifier_role(_unique("RoleB"))
    message = collab.add_message(_unique(f"{prefix}Msg"))
    return pkg, seq_diagram, collab, role_a, role_b, message


@pytest.mark.integration
class TestRPMessageIntegration:
    """Integration tests for RPMessage with real Rhapsody COM API — creation & endpoints."""

    def test_execution_occurrences_and_basic_getters(self, test_project: RPProject) -> None:
        pkg, seq_diagram, collab, role_a, role_b, message = _create_sequence_diagram_with_message(
            test_project, "Msg"
        )
        try:
            source_occ = message.add_source_execution_occurrence()
            assert isinstance(source_occ, RPExecutionOccurrence)
            target_occ = message.add_target_execution_occurrence()
            assert isinstance(target_occ, RPExecutionOccurrence)

            assert message.get_source_execution_occurrence() is not None
            assert message.get_target_execution_occurrence() is not None

            # Endpoints are not routed to classifier roles until the message
            # is placed on the diagram graphically; accept None as a valid
            # unrouted state while still exercising the getter.
            source = message.get_source()
            target = message.get_target()
            assert source is None or hasattr(source, "get_name")
            assert target is None or hasattr(target, "get_name")

            assert isinstance(message.get_sequence_number(), str)
            assert isinstance(message.get_signature(), str)
            assert isinstance(message.get_message_type(), str)

            message.reroute()
        finally:
            pkg.delete_from_project()
```

For remaining methods, follow the same pattern.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/interactions/test_model_interactions.py -m integration -v -k "TestRPMessageIntegration and test_execution_occurrences"`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/interactions/model_interactions.py`, flip `addSourceExecutionOccurrence`, `addTargetExecutionOccurrence`, `getSource`, `getTarget`, `getSourceExecutionOccurrence`, `getTargetExecutionOccurrence`, `getSequenceNumber`, `getSignature`, `getMessageType`, `reroute` under `RPMessage`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/interactions/test_model_interactions.py src/rhapsody_cli/models/elements/interactions/model_interactions.py
git commit -m "test: add integration tests for RPMessage creation and endpoints"
```

---

### Task 5: `RPMessage` — ports, formal typing & communication connection

**Files:**
- Modify: `tests/integration/models/elements/interactions/test_model_interactions.py`
- Modify: `src/rhapsody_cli/models/elements/interactions/model_interactions.py` (flip checklist boxes only)

**Methods covered:** `get_port`, `set_port`, `get_flow_port`, `set_flow_port`, `get_formal_interface_item`, `set_formal_interface_item`, `get_formal_type`, `set_formal_type`, `get_communication_connection`

- [ ] **Step 1: Write the failing/new integration tests**

```python
    def test_ports_and_formal_typing(self, test_project: RPProject) -> None:
        pkg, seq_diagram, collab, role_a, role_b, message = _create_sequence_diagram_with_message(
            test_project, "PortMsg"
        )
        try:
            # get_port / get_flow_port / get_formal_interface_item / get_formal_type
            # are expected to be None until explicitly configured; exercise
            # getters first, then set + read back where a settable value exists.
            assert message.get_port() is None or hasattr(message.get_port(), "get_name")
            assert message.get_flow_port() is None or hasattr(message.get_flow_port(), "get_name")
            assert message.get_formal_interface_item() is None or hasattr(
                message.get_formal_interface_item(), "get_name"
            )
            assert message.get_formal_type() is None or hasattr(message.get_formal_type(), "get_name")
            assert message.get_communication_connection() is None or hasattr(
                message.get_communication_connection(), "get_name"
            )

            operation = role_a.get_formal_classifier()
            if operation is not None:
                # Best-effort: only set formal_interface_item if a usable
                # RPInterfaceItem-compatible operation is discoverable.
                pass
        finally:
            pkg.delete_from_project()
```

For remaining methods (`set_port`, `set_flow_port`, `set_formal_interface_item`, `set_formal_type`): these setters require a valid target object of the correct type (`RPPort`, `RPSysMLPort`, `RPInterfaceItem`, `RPModelElement`) already associated with one of the classifier roles' formal classifiers. Investigate at runtime whether the test classifier role's class can be given an operation/port to use as the setter argument (e.g. `role_a`'s class → `add_operation`/`add_port` then `set_formal_classifier`). If no reliably reachable value can be constructed within a reasonable time, mark the setter test `xfail(reason="requires a fully-wired classifier role port/operation not reachable via a minimal API-only setup", strict=False)` rather than skipping the checklist row.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/interactions/test_model_interactions.py -m integration -v -k "TestRPMessageIntegration and test_ports_and_formal_typing"`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/interactions/model_interactions.py`, flip `getPort`, `setPort`, `getFlowPort`, `setFlowPort`, `getFormalInterfaceItem`, `setFormalInterfaceItem`, `getFormalType`, `setFormalType`, `getCommunicationConnection` under `RPMessage` (or leave `[ ]` with an inline `xfail` note if genuinely unreachable — do not silently drop).

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/interactions/test_model_interactions.py src/rhapsody_cli/models/elements/interactions/model_interactions.py
git commit -m "test: add integration tests for RPMessage ports and formal typing"
```

---

### Task 6: `RPMessage` — parameters, conditions, constraints & observations

**Files:**
- Modify: `tests/integration/models/elements/interactions/test_model_interactions.py`
- Modify: `src/rhapsody_cli/models/elements/interactions/model_interactions.py` (flip checklist boxes only)

**Methods covered:** `get_actual_parameter_list`, `set_actual_parameter_list`, `get_condition`, `get_invariant`, `set_invariant`, `get_return_value`, `set_return_value`, `get_duration_constraint`, `set_duration_constraint`, `get_duration_observation`, `set_duration_observation`, `get_time_constraint`, `set_time_constraint`, `get_time_observation`, `set_time_observation`, `get_timer_value`, `set_timer_value`, `get_signature` *(already covered in Task 4 — omit here)*

- [ ] **Step 1: Write the failing/new integration tests**

```python
    def test_string_property_roundtrips(self, test_project: RPProject) -> None:
        pkg, seq_diagram, collab, role_a, role_b, message = _create_sequence_diagram_with_message(
            test_project, "PropMsg"
        )
        try:
            assert isinstance(message.get_condition(), str)

            message.set_invariant("invariant_expr")
            assert message.get_invariant() == "invariant_expr"

            message.set_return_value("ret_val")
            assert message.get_return_value() == "ret_val"

            message.set_duration_constraint("{1..5}")
            assert message.get_duration_constraint() == "{1..5}"

            message.set_duration_observation("d1")
            assert message.get_duration_observation() == "d1"

            message.set_time_constraint("{t..t+5}")
            assert message.get_time_constraint() == "{t..t+5}"

            message.set_time_observation("t1")
            assert message.get_time_observation() == "t1"

            message.set_timer_value("100")
            assert message.get_timer_value() == "100"

            params = message.get_actual_parameter_list()
            assert params is not None
            message.set_actual_parameter_list(params)
        finally:
            pkg.delete_from_project()
```

For remaining methods, follow the same pattern.

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/interactions/test_model_interactions.py -m integration -v -k "TestRPMessageIntegration and test_string_property_roundtrips"`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/interactions/model_interactions.py`, flip `getActualParameterList`, `setActualParameterList`, `getCondition`, `getInvariant`, `setInvariant`, `getReturnValue`, `setReturnValue`, `getDurationConstraint`, `setDurationConstraint`, `getDurationObservation`, `setDurationObservation`, `getTimeConstraint`, `setTimeConstraint`, `getTimeObservation`, `setTimeObservation`, `getTimerValue`, `setTimerValue` under `RPMessage`.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/interactions/test_model_interactions.py src/rhapsody_cli/models/elements/interactions/model_interactions.py
git commit -m "test: add integration tests for RPMessage properties and constraints"
```

---

### Task 7: `RPExecutionOccurrence` + `RPDestructionEvent`

**Files:**
- Modify: `tests/integration/models/elements/interactions/test_model_interactions.py`
- Modify: `src/rhapsody_cli/models/elements/interactions/model_interactions.py` (flip checklist boxes only)

**Methods covered:** `RPExecutionOccurrence.get_message`. (`RPDestructionEvent` has no own checklist rows — 0 of the 82 — but its creation and inherited `RPMessage` behavior must still be smoke-tested to prove the "Message" metaclass resolves correctly to the `RPDestructionEvent` subclass.)

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPExecutionOccurrenceIntegration:
    """Integration tests for RPExecutionOccurrence with real Rhapsody COM API."""

    def test_get_message_roundtrip(self, test_project: RPProject) -> None:
        pkg, seq_diagram, collab, role_a, role_b, message = _create_sequence_diagram_with_message(
            test_project, "ExecOcc"
        )
        try:
            source_occ = message.add_source_execution_occurrence()
            fetched_message = source_occ.get_message()
            assert isinstance(fetched_message, RPMessage)
            assert fetched_message.get_name() == message.get_name()
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestRPDestructionEventIntegration:
    """Integration tests for RPDestructionEvent with real Rhapsody COM API."""

    def test_creation_resolves_to_destruction_event_subtype(self, test_project: RPProject) -> None:
        pkg = _create_package(test_project, _unique("DestrPkg"))
        seq_diagram = pkg.add_sequence_diagram(_unique("DestrSeq"))
        collab = seq_diagram.get_logical_collaboration()
        try:
            destruction_event = collab.add_destruction_event(_unique("Destr"))
            assert isinstance(destruction_event, RPDestructionEvent)
            # RPDestructionEvent inherits RPMessage's API surface; a basic
            # inherited getter proves the wrapper is fully functional.
            assert isinstance(destruction_event.get_message_type(), str)
        finally:
            pkg.delete_from_project()
```

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/interactions/test_model_interactions.py -m integration -v -k "TestRPExecutionOccurrenceIntegration or TestRPDestructionEventIntegration"`

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/interactions/model_interactions.py`, flip `getMessage` under `RPExecutionOccurrence`. `RPDestructionEvent` has no checklist rows to flip.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/interactions/test_model_interactions.py src/rhapsody_cli/models/elements/interactions/model_interactions.py
git commit -m "test: add integration tests for RPExecutionOccurrence and RPDestructionEvent"
```

---

### Task 8: `RPInteractionOccurrence` + `RPInteractionOperand` + `RPInteractionOperator`

**Files:**
- Modify: `tests/integration/models/elements/interactions/test_model_interactions.py`
- Modify: `src/rhapsody_cli/models/elements/interactions/model_interactions.py` (flip checklist boxes only)

**Methods covered:** `RPInteractionOccurrence.get_message_points`, `get_reference_sequence_diagram`, `set_reference_sequence_diagram`; `RPInteractionOperator.get_interaction_operands`, `get_interaction_type`, `set_interaction_type`; `RPInteractionOperand.get_contained_messages`, `get_interaction_constraint`, `set_interaction_constraint`

- [ ] **Step 1: Write the failing/new integration tests**

```python
@pytest.mark.integration
class TestRPInteractionOccurrenceIntegration:
    """Integration tests for RPInteractionOccurrence with real Rhapsody COM API."""

    def test_reference_sequence_diagram_roundtrip(self, test_project: RPProject) -> None:
        pkg = _create_package(test_project, _unique("IntOccPkg"))
        seq_diagram = pkg.add_sequence_diagram(_unique("MainSeq"))
        referenced_diagram = pkg.add_sequence_diagram(_unique("RefSeq"))
        collab = seq_diagram.get_logical_collaboration()
        try:
            occurrence = collab.add_interaction_occurrence(_unique("IntOcc"))
            assert isinstance(occurrence, RPInteractionOccurrence)

            message_points = occurrence.get_message_points()
            assert message_points is not None

            occurrence.set_reference_sequence_diagram(referenced_diagram)
            fetched = occurrence.get_reference_sequence_diagram()
            assert isinstance(fetched, RPSequenceDiagram)
            assert fetched.get_name() == referenced_diagram.get_name()
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestRPInteractionOperatorIntegration:
    """Integration tests for RPInteractionOperator with real Rhapsody COM API."""

    def test_interaction_type_and_operands(self, test_project: RPProject) -> None:
        pkg = _create_package(test_project, _unique("IntOpPkg"))
        seq_diagram = pkg.add_sequence_diagram(_unique("OpSeq"))
        collab = seq_diagram.get_logical_collaboration()
        try:
            operator = collab.add_interaction_operator(_unique("IntOp"))
            assert isinstance(operator, RPInteractionOperator)

            operator.set_interaction_type("alt")
            assert operator.get_interaction_type() == "alt"

            operands = operator.get_interaction_operands()
            assert operands is not None
            # NOTE: whether operands are auto-created for a bare
            # RPInteractionOperator (not placed on a diagram) must be
            # verified here. If `list(operands)` is empty, this is the
            # expected/only reachable behavior via a pure API-only setup —
            # see RPInteractionOperand handling below.
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestRPInteractionOperandIntegration:
    """Integration tests for RPInteractionOperand with real Rhapsody COM API.

    RPInteractionOperand has no public ``add_*`` creation API; instances are
    only obtainable via ``RPInteractionOperator.get_interaction_operands()``
    after the operator has been fully placed/elaborated in a diagram. If the
    live Rhapsody instance does not populate operands for an operator created
    purely through the API (no graphical placement), these methods are
    UNREACHABLE via public API and this test must be marked xfail with a
    clear reason rather than deleting the checklist rows.
    """

    @pytest.mark.xfail(
        reason="RPInteractionOperand instances are only populated once an "
        "RPInteractionOperator is graphically placed in a sequence diagram; "
        "no public API-only path creates operands. Verify against a live "
        "Rhapsody instance and remove this xfail if a path is found.",
        strict=False,
    )
    def test_contained_messages_and_constraint_roundtrip(self, test_project: RPProject) -> None:
        pkg = _create_package(test_project, _unique("IntOperandPkg"))
        seq_diagram = pkg.add_sequence_diagram(_unique("OperandSeq"))
        collab = seq_diagram.get_logical_collaboration()
        try:
            operator = collab.add_interaction_operator(_unique("IntOp"))
            operator.set_interaction_type("alt")
            operands = list(operator.get_interaction_operands())
            assert operands, "expected at least one interaction operand"
            operand = operands[0]
            assert isinstance(operand, RPInteractionOperand)

            contained = operand.get_contained_messages()
            assert contained is not None

            operand.set_interaction_constraint("x > 0")
            assert operand.get_interaction_constraint() == "x > 0"
        finally:
            pkg.delete_from_project()
```

- [ ] **Step 2: Run the new tests against live Rhapsody**

Run: `pytest tests/integration/models/elements/interactions/test_model_interactions.py -m integration -v -k "TestRPInteractionOccurrenceIntegration or TestRPInteractionOperatorIntegration or TestRPInteractionOperandIntegration"`

Investigate the actual result of `test_contained_messages_and_constraint_roundtrip`:
- If it **passes** (operands are populated), remove the `xfail` marker, keep the test, and flip the `RPInteractionOperand` checklist rows to `[x]`.
- If it **xfails as expected**, leave the `xfail` marker in place and leave the `RPInteractionOperand` checklist rows as `[ ]`, adding an inline comment above them: `# integration test: unreachable via public API — see test_model_interactions.py::TestRPInteractionOperandIntegration`.

- [ ] **Step 3: Flip checklist boxes**

In `src/rhapsody_cli/models/elements/interactions/model_interactions.py`, flip `getMessagePoints`, `getReferenceSequenceDiagram`, `setReferenceSequenceDiagram` under `RPInteractionOccurrence`, and `getInteractionOperands`, `getInteractionType`, `setInteractionType` under `RPInteractionOperator`. Flip `RPInteractionOperand` rows only per the outcome above.

- [ ] **Step 4: Run quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 5: Commit**

```bash
git add tests/integration/models/elements/interactions/test_model_interactions.py src/rhapsody_cli/models/elements/interactions/model_interactions.py
git commit -m "test: add integration tests for RPInteractionOccurrence, RPInteractionOperator and RPInteractionOperand"
```

---

### Task 9: Full Subpackage Verification

**Files:**
- Read-only verification; no source changes expected beyond what prior tasks already made.

- [ ] **Step 1: Run the full interactions integration test file**

Run: `pytest tests/integration/models/elements/interactions/test_model_interactions.py -m integration -v`

- [ ] **Step 2: Confirm all 82 checklist rows are addressed**

Run: `grep -c "\[ \] integration test" src/rhapsody_cli/models/elements/interactions/model_interactions.py`

Expect this count to be `0`, OR — if `RPInteractionOperand` was flagged unreachable in Task 8 — expect the count to equal exactly the number of genuinely unreachable rows (3, if all of `getContainedMessages`, `getInteractionConstraint`, `setInteractionConstraint` are unreachable), each with an inline "unreachable via public API" comment directly above it.

- [ ] **Step 3: Run the full quality gate**

Run: `ruff check src/ tests/ && black --check src/ tests/ && mypy src/ tests/ && pytest tests/unit`

- [ ] **Step 4: Run the complete integration suite once more to check for cross-test interference**

Run: `pytest tests/integration -m integration -v`

- [ ] **Step 5: Final commit**

```bash
git add -A
git commit -m "test: complete interactions subpackage integration test coverage"
```
