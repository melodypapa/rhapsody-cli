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
The `typedefBaseType` COM property is catalog-backed and readable/writable, but
this Rhapsody build rejects writes with COM HRESULT `-2147221498`, including
package-created `IRPType` base classifiers. The positive getter fixture cannot
be populated. `test_get_typedef_base_type` is an explicitly user-approved skip;
the exact property binding remains, and the live blocker is recorded in the P0
index and issue #202.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_type.py:IRPType.typedef_base_type
**Last Changed:** 2026-03-19

## SWR_ELEM_00032: IRPType typedef property writes live blocker

**ID:** SWR_ELEM_00032
**Title:** typedef flag and multiplicity setters have no successful live write
**Status:** Blocked
**Priority:** Low
**Description:**
`isTypedefConstant`, `isTypedefOrdered`, `isTypedefReference`, and
`typedefMultiplicity` are catalog-backed writable properties, but this
Rhapsody build returns HRESULT `0x80040006` for writes to real type elements.
Their integration round-trip nodes are explicitly user-approved skips; the
exact bindings and fake-COM coverage are retained. `addEnumerationLiteral` and
`deleteEnumerationLiteral` now pass live integration tests and are no longer
listed as blockers. The remaining setter deviations are in the P0 index and
issue #202.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_type.py:IRPType
**Last Changed:** 2026-03-19
