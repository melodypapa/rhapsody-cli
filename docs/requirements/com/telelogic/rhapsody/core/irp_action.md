## SWR_ELEM_00042: IRPAction Wrapper

**ID:** SWR_ELEM_00042
**Title:** IRPAction exposes transition action code through the pywin32 body property
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPAction` JavaDoc interface represents the action defined for a
transition in a statechart. The Python `IRPAction` shall extend
`IRPModelElement`, register itself for meta class `"Action"`, and expose the
action code as a read/write `body` property.

Pywin32 exposes the JavaDoc `getBody` / `setBody` pair as a single `body`
property, so the wrapper reads it with `get_com_property` and writes it with
`set_com_property`. The module uses `from __future__ import annotations` with
unquoted type references.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_action.py`; the class
was split out of the shared `irp_actions.py` module in its own sync run, and
`IRPSendAction` now inherits from the canonical module. Unit tests in the
mirrored unit path use only fake COM objects and give 100% statement/branch
coverage of the wrapper. Integration tests in the mirrored integration path
create a real statechart transition and action, assert the body value and a
setter round-trip, and delete the owning package during cleanup. Live
assertions are CI-only on Windows and are unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_action.py:IRPAction
**Last Changed:** 2026-11-26
