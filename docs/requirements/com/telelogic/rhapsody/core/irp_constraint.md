## SWR_ELEM_00052: IRPConstraint Wrapper

**ID:** SWR_ELEM_00052
**Title:** IRPConstraint exposes affected elements through the read-only pywin32 constraintsByMe property
**Status:** Implemented
**Priority:** Low
**Description:**
The `IRPConstraint` JavaDoc interface represents a constraint element. The
Python `IRPConstraint` shall extend `IRPModelElement`, register itself for meta
class `"Constraint"`, and expose the model elements affected by the constraint.

Pywin32 exposes the JavaDoc `getConstraintsByMe` accessor as a read-only
`constraintsByMe` property read with `get_com_property`. The module uses
`from __future__ import annotations` with unquoted type references.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_constraint.py`; the
class was split out of the shared `irp_misc.py` module in its own sync run.
Unit tests in the mirrored unit path use only fake COM objects and give 100%
statement/branch coverage of the wrapper. The mirrored integration test creates
a real constraint through the documented generic aggregation factory and asserts
the documented empty result; a populated `constraints_by_me` fixture remains a
P0 blocker because JavaDoc exposes no API to attach an affected element. Live
assertions are CI-only on Windows and are unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_constraint.py:IRPConstraint
**Last Changed:** 2026-11-27
