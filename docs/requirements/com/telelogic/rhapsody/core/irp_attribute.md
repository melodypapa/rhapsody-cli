## SWR_ELEM_00007: IRPAttribute Wrapper

**ID:** SWR_ELEM_00007
**Title:** IRPAttribute wraps IRPAttribute, a class/package-level attribute or variable
**Status:** Implemented
**Priority:** High
**Description:**
The `IRPAttribute` JavaDoc interface represents an attribute of a classifier. The
Python `IRPAttribute` shall extend `RPVariable` and expose Java-mirrored members for
multiplicity (`multiplicity`), static state (`is_static`, Python bool translated to
1/0), visibility (`visibility`), and the `isConstant`, `isOrdered`, and `isReference`
flags (`is_constant`/`is_ordered`/`is_reference`, Python bool translated to 1/0).
The wrapper registers itself for meta class `"Attribute"`.
Every COM call targets exactly one pywin32-exposed member from
`docs/reports/pywin32_authority.json`: `isConstant`, `isOrdered`, `isReference`,
`isStatic`, `multiplicity`, and `visibility` are pywin32 **properties** and are
exposed as Python `@property` accessors (with a setter for the writable members)
backed by `get_com_property`/`set_com_property`. No runtime name probing is used. The
module uses `from __future__ import annotations` with unquoted type references.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_attribute.py:IRPAttribute
(class renamed from `RPAttribute`; §2 canonical package move completed; 12 legacy
dual-binding call sites migrated)
**Last Changed:** 2026-11-24
