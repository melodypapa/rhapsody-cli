## SWR_ELEM_00051: IRPEnumerationLiteral Wrapper

**ID:** SWR_ELEM_00051
**Title:** IRPEnumerationLiteral exposes its value through the pywin32 value property
**Status:** Implemented
**Priority:** Low
**Description:**
The `IRPEnumerationLiteral` JavaDoc interface represents a literal value in an
enumeration. The Python `IRPEnumerationLiteral` shall extend `IRPModelElement`,
register itself for meta class `"EnumerationLiteral"`, and expose the literal
value.

Pywin32 exposes the JavaDoc `getValue` / `setValue` pair as a single read/write
`value` property, so the wrapper uses `get_com_property` and
`set_com_property`. The module uses `from __future__ import annotations` with
unquoted type references.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_enumeration_literal.py`;
the class was split out of the shared `irp_misc.py` module in its own sync run.
Unit tests in the mirrored unit path use only fake COM objects and give 100%
statement/branch coverage of the wrapper. Integration tests in the mirrored
integration path create a real enumeration type and literal through the
documented `IRPType.add_enumeration_literal` API and assert a value round-trip,
deleting the owning package during cleanup. Live assertions are CI-only on
Windows and are unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_enumeration_literal.py:IRPEnumerationLiteral
**Last Changed:** 2026-11-27
