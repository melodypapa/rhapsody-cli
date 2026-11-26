## SWR_ELEM_00044: IRPFlowItem Wrapper

**ID:** SWR_ELEM_00044
**Title:** IRPFlowItem exposes represented information elements through the pywin32 contract
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPFlowItem` JavaDoc interface represents item flows in Rhapsody models.
The Python `IRPFlowItem` shall extend `IRPClassifier`, register itself for meta
class `"FlowItem"`, and expose the information elements represented by the
item flow.

Pywin32 exposes the JavaDoc `getRepresented` accessor as a `represented`
property read with `get_com_property`. `add_represented` and
`remove_represented` are method-shaped and call `addRepresented` and
`removeRepresented` through `call_com`. The module uses
`from __future__ import annotations` with unquoted type references.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_flow_item.py`; the
class was split out of the shared `irp_activity.py` module in its own sync run.
Unit tests in the mirrored unit path use only fake COM objects and give 100%
statement/branch coverage of the wrapper. Integration tests in the mirrored
integration path create real flow items and classes, assert the represented
collection by membership, and delete the owning package during cleanup. Live
assertions are CI-only on Windows and are unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_flow_item.py:IRPFlowItem
**Last Changed:** 2026-11-26
