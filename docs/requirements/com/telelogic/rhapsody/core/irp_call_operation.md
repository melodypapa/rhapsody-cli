## SWR_ELEM_00046: IRPCallOperation Wrapper

**ID:** SWR_ELEM_00046
**Title:** IRPCallOperation exposes operation and target through the pywin32 contract
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPCallOperation` JavaDoc interface represents call operation elements in
activity diagrams. The Python `IRPCallOperation` shall extend `IRPState`,
register itself for meta class `"CallOperation"`, and expose the invoked
operation and its target.

Pywin32 exposes the JavaDoc `getOperation` / `getTarget` accessors and their
setters as two read/write properties (`operation` and `target`), so the
wrapper reads them with `get_com_property` and writes them with
`set_com_property`. The module uses `from __future__ import annotations` with
unquoted type references and local imports for names used only in `cast()`.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_call_operation.py`;
the class was split out of the shared `irp_actions.py` module in its own sync
run. Unit tests in the mirrored unit path use only fake COM objects and give
100% statement/branch coverage of the wrapper. Integration tests in the
mirrored integration path create a real activity call operation, an operation,
and an association relation, assert getter values by COM identity, and delete
the owning package during cleanup. Live assertions are CI-only on Windows and
are unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_call_operation.py:IRPCallOperation
**Last Changed:** 2026-11-26
