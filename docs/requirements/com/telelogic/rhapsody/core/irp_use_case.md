## SWR_CORE_00014: IRPUseCase Wrapper

**ID:** SWR_CORE_00014
**Title:** IRPUseCase wraps IRPUseCase, a use case in the model
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPUseCase` JavaDoc interface represents a use case. The Python `IRPUseCase`
shall extend `IRPClassifier` and expose Java-mirrored members for extension/entry
points (`add_extension_point`, `get_extension_points`, `find_extension_point`,
`delete_extension_point`, `get_entry_points`, `find_entry_point`,
`delete_entry_point`), describing diagrams (`add_describing_diagram`,
`get_describing_diagram`, `get_describing_diagrams`, `delete_describing_diagram`),
event receptions (`add_event_reception_with_event`), and behavior override state
(`get_is_behavior_overriden`, `set_is_behavior_overriden`). The setter is a
documented-unavailable `NotImplementedError` stub because `setIsBehaviorOverriden`
is absent from the registered type library for use cases. Sibling class
`RPExtensionPoint` stays in the legacy module (0 legacy sites, out of scope).
Every catalog-backed COM call targets exactly one pywin32 member: `extensionPoints`,
`entryPoints`, `describingDiagrams` and `isBehaviorOverriden` are properties read
via `get_com_property`; the remaining members are method-shaped and use `call_com`.
`get_is_behavior_overriden` returns an int, unlike IRPClass's method-exposed
`getIsFinal`. The module uses `from __future__ import annotations` with unquoted
type references and local imports for names used only in `cast()`.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_use_case.py:IRPUseCase
(class renamed from `RPUseCase`; §2 canonical package move completed; 4 legacy
dual-binding call sites migrated)
**Last Changed:** 2026-11-22
