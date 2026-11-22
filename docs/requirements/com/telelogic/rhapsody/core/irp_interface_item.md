## SWR_CORE_00013: IRPInterfaceItem Wrapper

**ID:** SWR_CORE_00013
**Title:** IRPInterfaceItem wraps IRPInterfaceItem, the base for operation-like elements
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPInterfaceItem` JavaDoc interface represents operation-like elements that
carry an argument list and signature. The Python `IRPInterfaceItem` shall extend
`IRPClassifier` and expose `add_argument`, `add_argument_before_position`,
`get_arguments`, `get_signature`, `get_signature_no_arg_names`,
`get_signature_no_arg_types` and `match_on_signature`. The wrapper registers
itself for meta class `"InterfaceItem"`.
Every COM call targets exactly one pywin32 member from
`docs/reports/pywin32_authority.json`: `arguments` and `signature` are
**properties** read via `get_com_property`; `getSignatureNoArgNames` and
`getSignatureNoArgTypes` are **methods** called via `call_com`; the remaining
members are method-shaped. Names used only in `cast()` are imported locally.
The module uses `from __future__ import annotations` with unquoted type references.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_interface_item.py:IRPInterfaceItem
(class renamed from `RPInterfaceItem`; §2 canonical package move completed; 4
legacy dual-binding call sites migrated)
**Last Changed:** 2026-11-22
