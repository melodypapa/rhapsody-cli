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
integration path create real activities and nested lanes and delete the owning
package during cleanup. The `contents` case is an approved live blocker: a real
root-state connector accepts `IRPConnector.setItsSwimlane` and reads the lane
back through `getItsSwimlane`, yet the lane's `contents` collection remains
empty. The skip and evidence are recorded in the P0 index and issue #202; do
not claim populated contents are live-verified.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_swimlane.py:IRPSwimlane
**Last Changed:** 2026-03-19
