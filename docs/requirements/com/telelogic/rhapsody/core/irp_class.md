## SWR_ELEM_00004: IRPClass Wrapper

**ID:** SWR_ELEM_00004
**Title:** IRPClass wraps the IRPClass Java interface, a class in Rhapsody models
**Status:** Implemented
**Priority:** High
**Description:**
The `IRPClass` interface represents classes in Rhapsody models. The Python `IRPClass` shall extend
`RPClassifier` to wrap the Java `IRPClass`. It shall expose Java-mirrored methods:
`addSuperclass(super_class)` (accepts an `IRPClass`), `addConstructor(arguments_data)`
(returns wrapped constructor), `addDestructor()` (returns wrapped destructor),
`is_abstract` (property returning bool), and `addClass(name)` (returns wrapped class).
Every COM call shall target exactly one pywin32-exposed member from
`docs/reports/pywin32_authority.json` with no runtime name probing: property-shaped
flags (`isAbstract`, `isActive`, `isBehaviorOverriden`, `isComposite`, `isReactive`)
are read/written via `get_com_property`/`set_com_property`, and method-shaped members
(`getIsFinal`, `setIsFinal`, `addClass`, ...) are invoked via `call_com`.
The wrapper shall register itself for the meta class `"Class"`.
Members `addEventReceptionWithEvent` and `updateContainedDiagramsOnServer` are documented
by JavaDoc but unavailable in the Rhapsody2.Application.1 COM type library; the wrapper
keeps `add_event_reception_with_event` as an explicit `NotImplementedError` facade and
omits the server diagram update entirely.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_class.py:IRPClass
**Last Changed:** 2026-11-21
