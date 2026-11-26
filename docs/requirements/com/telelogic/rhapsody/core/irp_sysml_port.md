## SWR_ELEM_00049: IRPSysMLPort Wrapper

**ID:** SWR_ELEM_00049
**Title:** IRPSysMLPort exposes flowport direction, conjugation, and type through the pywin32 contract
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPSysMLPort` JavaDoc interface represents flowport elements in Rhapsody
models. The Python `IRPSysMLPort` shall extend `IRPInstance`, register itself
for meta class `"SysMLPort"`, and expose whether the port is conjugated, its
direction, and its type.

Pywin32 exposes the JavaDoc accessor pairs as three read/write properties
(`isReversed`, `portDirection`, `type`), so the wrapper uses `get_com_property`
and `set_com_property`. `add_link` is method-shaped and calls `addLink` through
`call_com` with five arguments. The module uses `from __future__ import
annotations` with unquoted type references and local imports for names used
only in `cast()`.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_sysml_port.py`; the
class was split out of the shared `irp_other_model.py` module in its own sync
run. Unit tests in the mirrored unit path use only fake COM objects and give
100% statement/branch coverage of the wrapper. Integration tests in the
mirrored integration path create real flowports, instances, and an association,
assert populated getter values, and delete the owning package during cleanup.
Live assertions are CI-only on Windows and are unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_sysml_port.py:IRPSysMLPort
**Last Changed:** 2026-11-27
