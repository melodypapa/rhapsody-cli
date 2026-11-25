## SWR_ELEM_00005: IRPActor Wrapper

**ID:** SWR_ELEM_00005
**Title:** IRPActor represents actors in Rhapsody models
**Status:** Implemented
**Priority:** Medium
**Description:**
The JavaDoc `IRPActor` interface represents actors in Rhapsody models and extends `IRPClassifier`. The Python wrapper shall preserve the `"Actor"` meta-class registration, expose `is_behavior_overriden` as a read/write Python property backed by the typelib property `isBehaviorOverriden`, and expose JavaDoc-only `add_event_reception_with_event(name, event)` and `update_contained_diagrams_on_server(enforce_update)` as signature-preserving `NotImplementedError` stubs because neither member is present in the registered IRPActor typelib. The `update_contained_diagrams_on_server` Java return type is `int`; no COM dispatch is attempted by either stub.
Every available COM binding uses exactly one pywin32 member: property access uses `get_com_property` / `set_com_property`, and no runtime probing or Java-name fallback is permitted. Inherited classifier/unit/model-element members remain owned by their base wrappers.
**Implementation:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_actor.py:IRPActor` (canonical package; class registration retained; behavior override getter/setter mapped to one writable property; two JavaDoc-only stubs tested at both layers).
**Last Changed:** 2026-11-25
