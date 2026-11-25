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

## SWR_ELEM_00025: IRPArgument argumentDirection setter live-fixture blocker

**ID:** SWR_ELEM_00025
**Title:** argument_direction setter has no live integration proof
**Status:** Blocked
**Priority:** Low
**Description:**
The `argumentDirection` property is readable on a real argument, but assigning a
documented direction value (`"out"`) through the wrapper setter makes this
Rhapsody build throw a COM server exception. The former integration test mocked
the setter to assert its call shape; per SKILL §5 a mock cannot prove live
behaviour, so that test was replaced with a live read-only assertion and the
setter row recorded as blocked. The binding keeps full fake-COM unit coverage.
Live verification needs a build that accepts the write, after which the row can
be closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_argument.py:IRPArgument.argument_direction
**Last Changed:** 2026-11-25
