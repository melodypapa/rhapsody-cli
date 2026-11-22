## SWR_CORE_00006: IRPOperation Wrapper

**ID:** SWR_CORE_00006
**Title:** IRPOperation wraps IRPOperation, a class/package-level operation or function
**Status:** Implemented
**Priority:** High
**Description:**
The `IRPOperation` JavaDoc interface represents an operation or method in a classifier.
The Python `IRPOperation` shall extend `IRPInterfaceItem` and expose Java-mirrored
members: body/initializer (`get_body`/`set_body`, `get_initializer`/`set_initializer`),
return type (`get_returns`/`set_returns`, `get_return_type_declaration`/
`set_return_type_declaration`), flags (`get_is_abstract`/`set_is_abstract`,
`get_is_static`/`set_is_static`, `get_is_virtual`/`set_is_virtual`,
`get_is_cg_derived`, `get_is_const`/`set_is_const`, `get_is_ctor`, `get_is_dtor`,
`get_is_final`/`set_is_final`, `get_is_inline`, `get_is_trigger`), flowchart
(`get_flowchart`/`set_flowchart`, `create_auto_flow_chart`, `delete_flowchart`),
signature/visibility (`get_implementation_signature`, `get_visibility`/
`set_visibility`), arguments (`delete_argument`) and server diagrams
(`update_contained_diagrams_on_server`). The wrapper registers itself for meta class
`"Operation"`.
Every COM call targets exactly one pywin32-exposed member from
`docs/reports/pywin32_authority.json`, with no runtime name probing. Property-shaped
members (`body`, `isAbstract`, `isStatic`, `isVirtual`, `returns`, `flowchart`,
`initializer`, `isCgDerived`, `isConst`, `isCtor`, `isDtor`, `isFinal`, `isInline`,
`isTrigger`, `visibility`) are read/written via `get_com_property`/`set_com_property`;
the three JavaDoc method-shaped getters (`getReturnTypeDeclaration`,
`setReturnTypeDeclaration`, `getImplementationSignature`) use `call_com`.
`update_contained_diagrams_on_server()` calls the Java-shaped member directly — it
is absent from the committed catalog and is recorded as a `PYWIN32_MEMBER_MISSING`
blocker in the API report. The module uses `from __future__ import annotations` with
unquoted type references and local imports for names used only in `cast()`.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_operation.py:IRPOperation
(class renamed from `RPOperation`; §2 canonical package move completed; 25 legacy
dual-binding call sites migrated)
**Last Changed:** 2026-11-22
