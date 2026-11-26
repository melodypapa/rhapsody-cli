## SWR_ELEM_00048: IRPAcceptTimeEvent Wrapper

**ID:** SWR_ELEM_00048
**Title:** IRPAcceptTimeEvent exposes duration through the pywin32 durationTime property
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPAcceptTimeEvent` JavaDoc interface represents Accept Time Event
elements in activity diagrams and statecharts. The Python
`IRPAcceptTimeEvent` shall extend `IRPState`, register itself for meta class
`"AcceptTimeEvent"`, and expose the specified duration.

Pywin32 exposes the JavaDoc `getDurationTime` / `setDurationTime` pair as a
single read/write `durationTime` property, so the wrapper reads it with
`get_com_property` and writes it with `set_com_property`. The module uses
`from __future__ import annotations` with unquoted type references.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_accept_time_event.py`;
the class was split out of the shared `irp_actions.py` module in its own sync
run. Unit tests in the mirrored unit path use only fake COM objects and give
100% statement/branch coverage of the wrapper. Integration tests in the
mirrored integration path create a real Accept Time Event in an activity and
assert a duration write/read round-trip, deleting the owning package during
cleanup. Live assertions are CI-only on Windows and are unverified in offline
runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_accept_time_event.py:IRPAcceptTimeEvent
**Last Changed:** 2026-11-26
