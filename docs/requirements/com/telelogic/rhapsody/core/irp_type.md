## SWR_ELEM_00020: IRPType Wrapper

**ID:** SWR_ELEM_00020
**Title:** IRPType wraps IRPType, a named type definition
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPType` JavaDoc interface represents a named type definition. The Python
`IRPType` shall extend `IRPClassifier` and expose Java-mirrored members for typedef
state (`declaration`, `kind`,
`typedef_multiplicity`,
`is_typedef_constant`,
`is_typedef_ordered`,
`is_typedef_reference`,
`is_typedef`, `typedef_base_type`) and enumeration
helpers (`enumeration_literals`, `add_enumeration_literal`,
`delete_enumeration_literal`). Catalog-backed members call exactly one pywin32
member from `docs/reports/pywin32_authority.json`: the nine migrated members are
property-shaped and exposed as Python `@property` accessors (with a setter for the
writable members) backed by `get_com_property`/`set_com_property`; the remaining
JavaDoc method-shaped getters have no matching pywin32 member and are documented
binding differences left unchanged. The module uses `from __future__ import
annotations` with unquoted type references and local imports for names used only
in `cast()`.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_type.py:IRPType
(class renamed from `RPType`; §2 canonical package move completed; 9 legacy
dual-binding call sites migrated; sibling RPClassifierRole/RPSysMLPort stay in the
legacy module as out of scope)
**Last Changed:** 2026-11-24

## SWR_ELEM_00021: IRPType typedef_base_type live-fixture blocker

**ID:** SWR_ELEM_00021
**Title:** typedef_base_type setter has no live integration proof
**Status:** Blocked
**Priority:** Low
**Description:**
The `typedefBaseType` COM property is readable, but in the local Rhapsody build
assigning a real classifier through the `IRPType.typedef_base_type` setter does
not yield a retrievable value. The former integration test asserted a mocked
`set_com_property` call shape, which proves only the binding and not that the
setter works against Rhapsody (SKILL §5). That test was removed; the binding keeps
full fake-COM unit coverage. Live verification needs a Rhapsody build where the
setter persists the assigned base type, after which the integration row can be
closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_type.py:IRPType.typedef_base_type
**Last Changed:** 2026-11-25

## SWR_ELEM_00032: IRPType typedef write live-fixture blocker

**ID:** SWR_ELEM_00032
**Title:** typedef property writes and enumeration literals have no live proof
**Status:** Blocked
**Priority:** Low
**Description:**
`isTypedefConstant`/`isTypedefOrdered`/`isTypedefReference`/`typedefMultiplicity`
writes and `addEnumerationLiteral`/`deleteEnumerationLiteral` are catalog-backed,
but this Rhapsody build rejects them with HRESULT `0x80040006` on a real type
element. The integration tests were removed per SKILL §5; the bindings keep full
fake-COM unit coverage. Live verification needs a build that accepts these
writes, after which the rows can be closed.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_type.py:IRPType
**Last Changed:** 2026-11-25
