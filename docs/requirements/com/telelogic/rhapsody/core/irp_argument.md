## SWR_CORE_00008: IRPArgument Wrapper

**ID:** SWR_CORE_00008
**Title:** IRPArgument wraps IRPArgument, an operation argument or parameter
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPArgument` JavaDoc interface represents an argument (parameter) of an
operation. The Python `IRPArgument` shall extend `RPVariable` and expose
`get_argument_direction()` / `set_argument_direction(argument_direction)` for the
argument direction string. The wrapper registers itself for meta class `"Argument"`.
Every COM call targets exactly one pywin32-exposed member from
`docs/reports/pywin32_authority.json`: `argumentDirection` is a pywin32 **property**
and is read/written with `get_com_property`/`set_com_property` while the Python-facing
`get_*`/`set_*` method names are retained. The module uses
`from __future__ import annotations`.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_argument.py:IRPArgument
(class renamed from `RPArgument`; §2 canonical package move completed; 2 legacy
dual-binding call sites migrated)
**Last Changed:** 2026-11-22
