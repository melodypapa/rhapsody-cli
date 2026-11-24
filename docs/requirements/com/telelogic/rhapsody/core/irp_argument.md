## SWR_ELEM_00016: IRPArgument Wrapper

**ID:** SWR_ELEM_00016
**Title:** IRPArgument wraps IRPArgument, an operation argument or parameter
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPArgument` JavaDoc interface represents an argument (parameter) of an
operation. The Python `IRPArgument` shall extend `RPVariable` and expose a
read/write `argument_direction` property for the argument direction string. The
wrapper registers itself for meta class `"Argument"`.
Every COM call targets exactly one pywin32-exposed member from
`docs/reports/pywin32_authority.json`: `argumentDirection` is a pywin32 **property**
read/written with `get_com_property`/`set_com_property` behind the Python property.
The module uses
`from __future__ import annotations`.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_argument.py:IRPArgument
(class renamed from `RPArgument`; §2 canonical package move completed; 2 legacy
dual-binding call sites migrated)
**Last Changed:** 2026-11-24
