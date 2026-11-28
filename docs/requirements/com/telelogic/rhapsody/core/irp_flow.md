## SWR_ELEM_00039: IRPFlow Wrapper

**ID:** SWR_ELEM_00039
**Title:** IRPFlow exposes flow ends, conveyed elements, and direction through the pywin32 contract
**Status:** Implemented with approved live endpoint deviation
**Priority:** Medium
**Description:**
The `IRPFlow` JavaDoc interface represents a flow between two model elements in
an activity diagram. The Python `IRPFlow` shall extend `IRPModelElement`,
register itself for meta class `"Flow"`, and expose the flow's conveyed
elements, direction, and both ends (including port and SysML-port ends).

The pywin32 catalog exposes the JavaDoc accessors of this interface as COM
**properties**, so the Python surface uses `@property` accessors rather than
`get_*` / `set_*` methods: `conveyed`, `direction` (read/write), `end1`
(read/write), `end1_port`, `end1_sys_ml_port`, `end2` (read/write), `end2_port`,
and `end2_sys_ml_port`. Each property reads or writes exactly one catalog
member via `get_com_property` / `set_com_property`. The six method-shaped
members (`add_conveyed`, `remove_conveyed`, `set_end1_via_port`,
`set_end1_via_sys_ml_port`, `set_end2_via_port`, `set_end2_via_sys_ml_port`)
use `call_com` with the exact camelCase COM name and the catalog's argument
count. The module uses `from __future__ import annotations` with unquoted type
references and local imports for names used only in `cast()`.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_flow.py`; the class was
split out of the shared `irp_activity.py` module in its own sync run. Unit
tests in `tests/unit/models/com/telelogic/rhapsody/core/test_irp_flow.py` use
only fake COM objects and give 100% statement/branch coverage of the wrapper.
Integration tests in the mirrored path create real Rhapsody flows, classes,
instances, and ports, assert populated getter values by identity/name, and
delete the owning package during cleanup. The four `set_end*_via_port` and
`set_end*_via_sys_ml_port` tests are user-approved skips: the exact documented
calls return COM error `-2147221494` even with the port and an `Object` created
by the same class. The live blocker and skipped methods are recorded in
`docs/reports/sync-todo/index.md` and issue #202; this requirement remains open
for a valid endpoint fixture.

**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_flow.py:IRPFlow
**Last Changed:** 2026-03-19
