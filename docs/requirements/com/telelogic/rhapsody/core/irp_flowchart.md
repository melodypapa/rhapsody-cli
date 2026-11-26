## SWR_ELEM_00040: IRPFlowchart Wrapper

**ID:** SWR_ELEM_00040
**Title:** IRPFlowchart exposes activity creation, analysis mode, owner, and swimlanes through the pywin32 contract
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPFlowchart` JavaDoc interface represents activities in Rhapsody models.
The Python `IRPFlowchart` shall extend `IRPStatechart`, register itself for meta
class `"Flowchart"`, and expose activity-node creation methods plus the three
JavaDoc accessors that pywin32 surfaces as COM properties.

`is_analysis_only`, `its_owner`, and `swimlanes` are read with
`get_com_property`; the first two also have setters using `set_com_property`.
The remaining eleven members are method-shaped COM calls made through
`call_com` with the exact camelCase member name. The wrapper uses
`from __future__ import annotations` with unquoted type references and local
imports for names used only in `cast()`.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_flowchart.py`; the
class was split out of the shared `irp_activity.py` module in its own sync run.
Unit tests in the mirrored unit path use only fake COM objects and give 100%
statement/branch coverage of the wrapper. Integration tests in the mirrored
integration path create real activities, root states, operations, and
swimlanes, assert populated getter values, and delete the owning package
during cleanup. Those live assertions are CI-only on Windows and are
unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_flowchart.py:IRPFlowchart
**Last Changed:** 2026-11-26
