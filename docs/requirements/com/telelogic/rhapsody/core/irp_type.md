## SWR_CORE_00010: IRPType Wrapper

**ID:** SWR_CORE_00010
**Title:** IRPType wraps IRPType, a named type definition
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPType` JavaDoc interface represents a named type definition. The Python
`IRPType` shall extend `IRPClassifier` and expose Java-mirrored members for typedef
state (`get_declaration`/`set_declaration`, `get_kind`/`set_kind`,
`get_typedef_multiplicity`/`set_typedef_multiplicity`,
`get_is_typedef_constant`/`set_is_typedef_constant`,
`get_is_typedef_ordered`/`set_is_typedef_ordered`,
`get_is_typedef_reference`/`set_is_typedef_reference`,
`get_is_typedef`, `get_typedef_base_type`/`set_typedef_base_type`) and enumeration
helpers (`get_enumeration_literals`, `add_enumeration_literal`,
`delete_enumeration_literal`). Catalog-backed members call exactly one pywin32
member from `docs/reports/pywin32_authority.json`: the nine migrated members are
property-shaped and use `get_com_property`/`set_com_property`; the remaining
JavaDoc method-shaped getters have no matching pywin32 member and are documented
binding differences left unchanged. The module uses `from __future__ import
annotations` with unquoted type references and local imports for names used only
in `cast()`.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_type.py:IRPType
(class renamed from `RPType`; §2 canonical package move completed; 9 legacy
dual-binding call sites migrated; sibling RPClassifierRole/RPSysMLPort stay in the
legacy module as out of scope)
**Last Changed:** 2026-11-22
