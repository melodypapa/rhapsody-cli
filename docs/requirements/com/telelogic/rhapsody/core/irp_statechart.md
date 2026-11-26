## SWR_ELEM_00011: IRPStatechart Wrapper

**ID:** SWR_ELEM_00011
**Title:** IRPStatechart wraps the statechart elements underlying a statechart diagram
**Status:** Implemented
**Priority:** Medium
**Description:**
The JavaDoc `IRPStatechart` interface represents the statechart elements underlying a statechart; the diagram itself is represented by `IRPStatechartDiagram`. The Python `IRPStatechart` shall extend `IRPClass`, register for COM meta class `"Statechart"`, and expose its JavaDoc-owned methods with snake_case names. Five pywin32 properties (`graphicalElements`, `isMainBehavior`, `isOverridden`, `itsClass`, and `rootState`) shall be exposed as read-only Python properties (`graphical_elements`, `is_main_behavior`, `is_overridden`, `its_class`, and `root_state`). The JavaDoc members `addNewAcceptEventAction` and `addNewAcceptTimeEvent` remain callable Python stubs raising `NotImplementedError` because neither is exposed by the registered pywin32 interface.
Every COM binding shall call exactly one catalogued member using `call_com` for methods or the COM property helpers for properties. Calls returning graph interfaces shall construct their specific wrapper directly because those pywin32 interfaces do not expose the model-element `metaClass` property required by `wrap()`. The `getPictureAs` and `getPicturesWithImageMap` COM calls return the filenames and output image-map collections as a pywin32 tuple; the Python wrapper returns the filename collection and replaces the passed collection wrapper's COM object with the returned image-map collection.
**Implementation:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_statechart.py:IRPStatechart` (renamed from `RPStatechart`; canonical package move completed; direct pywin32 members and property shapes verified against the registered typelib; 2 JavaDoc-only members documented as unavailable).
**Last Changed:** 2026-11-25

---

## SWR_ELEM_00036: IRPStatechart live integration limitations

**ID:** SWR_ELEM_00036
**Title:** IRPStatechart inherited behavior and Eclipse/edge APIs need live follow-up
**Status:** Blocked
**Priority:** Medium
**Description:**
The wrapper and fake-COM tests cover the JavaDoc/pywin32 contract, but this Rhapsody installation cannot establish live outcomes for several members. `AddNewEdgeByType` returns COM error `-2147221498` for JavaDoc-listed connector types with real diagram nodes. `OpenDiagramView` returns COM error `-2147221504`; JavaDoc describes it as an internal Rhapsody-Eclipse integration API, which is not available in the test environment. `getInheritsFrom` returned no statechart even after a real classifier generalization and base/derived statecharts were created; `overrideInheritance` and `unoverrideInheritance` return COM error `-2147467263` (`E_NOTIMPL`) in that setup. These live observations do not authorize exception assertions or runtime `NotImplementedError` stubs; the wrappers retain the catalogued direct bindings. A populated positive `get_inherits_from` getter fixture and live assertions for these members remain open until a supported inheritance/Eclipse environment or confirmed working setup is available.
**Implementation:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_statechart.py:IRPStatechart` and `tests/integration/models/com/telelogic/rhapsody/core/test_irp_statechart.py` (live blockers tracked in `docs/reports/sync-todo/Group-classifiers-1.md`).
**Last Changed:** 2026-11-25
