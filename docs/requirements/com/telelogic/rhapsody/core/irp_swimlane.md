## SWR_ELEM_00041: IRPSwimlane Wrapper

**ID:** SWR_ELEM_00041
**Title:** IRPSwimlane exposes lane contents, represented element, and nested lanes through the pywin32 contract
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPSwimlane` JavaDoc interface represents swimlanes in an activity diagram.
The Python `IRPSwimlane` shall extend `IRPModelElement`, register itself for
meta class `"Swimlane"`, and expose the elements contained in a lane, the
element it represents, and its nested lanes.

The pywin32 catalog exposes `contents`, `represents`, and `swimlanes` as
properties: they are read with `get_com_property`, and `represents` also has a
setter using `set_com_property`. `add_swimlane` is method-shaped and calls
`addSwimlane` through `call_com`. The module uses
`from __future__ import annotations` with unquoted type references.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_swimlane.py`; the
class was split out of the shared `irp_activity.py` module in its own sync run.
Unit tests in the mirrored unit path use only fake COM objects and give 100%
statement/branch coverage of the wrapper. Integration tests in the mirrored
integration path create real activities and nested lanes, assert populated
getter values by identity/membership, and delete the owning package during
cleanup. The `contents` getter has no documented API that places an element
inside a lane; its fresh-lane empty state is the only observable result and is
recorded as a P0 blocker in `docs/reports/sync-todo/index.md`. Live assertions
are CI-only on Windows and are unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_swimlane.py:IRPSwimlane
**Last Changed:** 2026-11-26
