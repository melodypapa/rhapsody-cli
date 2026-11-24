## SWR_ELEM_00012: IRPUseCase Wrapper

**ID:** SWR_ELEM_00012
**Title:** IRPUseCase wraps IRPUseCase, a use case in the model
**Status:** Implemented
**Priority:** Medium
**Description:**
The `IRPUseCase` JavaDoc interface represents a use case. The Python `IRPUseCase`
shall extend `IRPClassifier` and expose Java-mirrored members for extension/entry
points (`add_extension_point`, `extension_points`, `find_extension_point`,
`delete_extension_point`, `entry_points`, `find_entry_point`,
`delete_entry_point`), describing diagrams (`add_describing_diagram`,
`get_describing_diagram`, `describing_diagrams`, `delete_describing_diagram`),
event receptions (`add_event_reception_with_event`), behavior override state
(`is_behavior_overriden`, `set_is_behavior_overriden`), and Design Manager
server refresh (`update_contained_diagrams_on_server`). Three members are
documented-unavailable `NotImplementedError` stubs because their COM members are
absent from the registered type library for this build: `set_is_behavior_overriden`
(`setIsBehaviorOverriden`), `add_event_reception_with_event`
(`addEventReceptionWithEvent`), and `update_contained_diagrams_on_server`
(`updateContainedDiagramsOnServer`). Sibling class
`RPExtensionPoint` stays in the legacy module (0 legacy sites, out of scope).
Every catalog-backed COM call targets exactly one pywin32 member: `extensionPoints`,
`entryPoints`, `describingDiagrams` and `isBehaviorOverriden` are properties exposed
as Python `@property` accessors read via `get_com_property`; the remaining members
are method-shaped and use `call_com`. `find_entry_point(gen)` and
`find_extension_point(gen)` take the JavaDoc/pywin32 `IRPGeneralization` COM object
(parameter name `gen`, type `com`) and return a `String`; the wrapper unwraps `gen`
with `._com` and returns the string, matching the catalog signature rather than a
name-string lookup.
`is_behavior_overriden` returns an int, unlike IRPClass's `is_behavior_overriden`
property exposed through get/set COM members. The module uses
`from __future__ import annotations` with unquoted
type references and local imports for names used only in `cast()`.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_use_case.py:IRPUseCase
(class renamed from `RPUseCase`; §2 canonical package move completed; 4 legacy
dual-binding call sites migrated)
**Last Changed:** 2026-11-24
