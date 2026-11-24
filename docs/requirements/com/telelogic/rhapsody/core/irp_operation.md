## SWR_ELEM_00006: IRPOperation Wrapper

**ID:** SWR_ELEM_00006
**Title:** IRPOperation wraps IRPOperation, a class/package-level operation or function
**Status:** Implemented
**Priority:** High
**Description:**
The `IRPOperation` JavaDoc interface represents an operation or method in a classifier.
The Python `IRPOperation` shall extend `IRPInterfaceItem` and expose Java-mirrored
members: body/initializer (`body`, `initializer`), return type (`returns`,
`get_return_type_declaration`/`set_return_type_declaration`), flags (`is_abstract`,
`is_static`, `is_virtual`, `is_cg_derived`, `is_const`, `is_ctor`, `is_dtor`,
`is_final`, `is_inline`, `is_trigger`), flowchart (`flowchart`,
`create_auto_flow_chart`, `delete_flowchart`), signature/visibility
(`get_implementation_signature`, `visibility`), arguments (`delete_argument`) and
server diagrams (`update_contained_diagrams_on_server`). The wrapper registers itself
for meta class `"Operation"`.
Every COM call targets exactly one pywin32-exposed member from
`docs/reports/pywin32_authority.json`, with no runtime name probing. Property-shaped
members (`body`, `isAbstract`, `isStatic`, `isVirtual`, `returns`, `flowchart`,
`initializer`, `isCgDerived`, `isConst`, `isCtor`, `isDtor`, `isFinal`, `isInline`,
`isTrigger`, `visibility`) are pywin32 **properties** and are exposed as Python
`@property` accessors (with a setter for the writable members) backed by
`get_com_property`/`set_com_property`; the two JavaDoc method-shaped members
(`getReturnTypeDeclaration`/`setReturnTypeDeclaration`, `getImplementationSignature`)
use `call_com`.
`update_contained_diagrams_on_server()` calls the Java-shaped member directly — it
is absent from the committed catalog and is recorded as a `PYWIN32_MEMBER_MISSING`
blocker in the API report. The module uses `from __future__ import annotations` with
unquoted type references and local imports for names used only in `cast()`.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_operation.py:IRPOperation
(class renamed from `RPOperation`; §2 canonical package move completed; 25 legacy
dual-binding call sites migrated; 25 property-shaped members converted to `@property`)
**Last Changed:** 2026-11-24
