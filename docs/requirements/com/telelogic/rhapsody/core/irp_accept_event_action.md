## SWR_ELEM_00055: IRPAcceptEventAction Wrapper

**ID:** SWR_ELEM_00055
**Title:** IRPAcceptEventAction exposes its event through the pywin32 event property
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPAcceptEventAction` JavaDoc interface represents Accept Event Action
elements in a statechart or activity diagram. The Python wrapper shall extend
`IRPState` and register for the COM meta class `"AcceptEventAction"`.

JavaDoc declares `getEvent()` and `setEvent(IRPEvent)`, while pywin32 exposes
the read/write `event` property. The Python API therefore exposes one
read/write `event` property backed by `get_com_property` and `set_com_property`;
the getter wraps the returned COM object as `IRPEvent`.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_accept_event_action.py`;
the class was split from the shared `irp_actions.py` module. Mirrored unit tests
use fake COM objects to verify property access, wrapping, inheritance, and
registration. The integration test creates a real Accept Event Action and
`IRPEvent`, sets the relationship, and checks populated retrieval. The focused
Windows integration test passed against live Rhapsody; package cleanup runs in
a `finally` block.

**Implementation:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_accept_event_action.py:IRPAcceptEventAction`
**Last Changed:** 2026-11-26
