## SWR_ELEM_00017: IRPAssociationClass Wrapper

**ID:** SWR_ELEM_00017
**Title:** IRPAssociationClass wraps IRPAssociationClass, a class acting as an association
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPAssociationClass` JavaDoc interface represents an association that is also
a class. The Python `IRPAssociationClass` shall extend `IRPClass` and expose the
three owned properties: read-only `end1` and `end2`, plus read/write `is_class`.
All three COM members (`end1`, `end2`, `isClass`) are
pywin32 **properties** read/written via `get_com_property`/`set_com_property` behind
those Python properties. Names used only in
`cast()` are imported locally inside the property. The module uses
`from __future__ import annotations` with unquoted type references.
The wrapper registers itself for meta class `"AssociationClass"`.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_association_class.py:IRPAssociationClass
(class renamed from `RPAssociationClass`; §2 canonical package move completed; 4
legacy/direct call sites bound to the catalogued properties)
**Last Changed:** 2026-11-24
