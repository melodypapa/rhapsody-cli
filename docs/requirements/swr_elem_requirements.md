# Software Requirements - ELEM (Model Element Wrappers)

**Category:** ELEM
**Prefix:** SWR
**Source:** Extracted from code
**Last Validated:** 2026-07-07

---

## SWR_ELEM_00005: RPActor Wrapper

**ID:** SWR_ELEM_00005
**Title:** RPActor wraps IRPActor, a UML actor (external role interacting with the system)
**Status:** Implemented
**Priority:** Medium
**Description:**
`RPActor` shall extend `IRPClassifier` to wrap `IRPActor`. It shall expose Java-mirrored
methods: `addEventReceptionWithEvent(name, event)` (accepts an `IRPModelElement` event,
returns wrapped reception), `getIsBehaviorOverriden()` (returns bool), and
`setIsBehaviorOverriden(is_overridden)` (translates Python bool to 1/0). The wrapper
shall register itself for the meta class `"Actor"`.
**Implementation:** src/rhapsody_cli/models/elements/classifiers.py:RPActor
**Last Changed:** 2026-07-07

---

## SWR_ELEM_00008: RPDiagram Wrapper

**ID:** SWR_ELEM_00008
**Title:** RPDiagram wraps IRPDiagram, the base interface for all Rhapsody diagram types
**Status:** Implemented
**Priority:** Medium
**Description:**
`RPDiagram` shall extend `IRPUnit` to wrap `IRPDiagram`. It shall expose Java-mirrored
methods: `closeDiagram()`, `addTextBox(text, x_position, y_position, width, height)`
(returns wrapped text box), `getCustomViews()` (returns `IRPCollection`), and
`getCorrespondingGraphicElements(model_element)` (accepts an `IRPModelElement`, returns
`IRPCollection`). The wrapper shall register itself for the meta class
`"ActivityDiagram"`.
**Implementation:** src/rhapsody_cli/models/elements/diagrams.py:RPDiagram
**Last Changed:** 2026-07-07

---

## SWR_ELEM_00009: RPInstance Wrapper

**ID:** SWR_ELEM_00009
**Title:** RPInstance wraps IRPInstance, an instance/object in the Rhapsody model
**Status:** Implemented
**Priority:** Medium
**Description:**
`RPInstance` shall extend `RPRelation` to wrap `IRPInstance`, matching the Java API
inheritance where `IRPInstance` extends `IRPRelation`. It shall expose Java-mirrored
methods: `getAllNestedElements()` (returns `IRPCollection`), `getAttributeValue(attribute_name)`
(returns str), `setAttributeValue(attribute_name, attribute_value)` (str args),
`getInLinks()` (returns `IRPCollection`), and `getOutLinks()` (returns `IRPCollection`).
The wrapper shall register itself for the meta class `"Instance"`.
**Implementation:** src/rhapsody_cli/models/elements/relations.py:RPInstance
**Last Changed:** 2026-07-07

---

## SWR_ELEM_00010: RPRequirement Wrapper

**ID:** SWR_ELEM_00010
**Title:** RPRequirement wraps IRPRequirement, a traceable requirement in the model
**Status:** Implemented
**Priority:** Medium
**Description:**
`RPRequirement` shall extend `IRPUnit` to wrap `IRPRequirement`. It shall expose
Java-mirrored methods: `getRequirementID()` (returns str) and
`setRequirementID(requirement_id)` (str). The wrapper shall register itself for the
meta class `"Requirement"`.
**Implementation:** src/rhapsody_cli/models/elements/requirements.py:RPRequirement
**Last Changed:** 2026-07-07

---

## SWR_ELEM_00011: RPStatechart Wrapper

**ID:** SWR_ELEM_00011
**Title:** RPStatechart wraps IRPStatechart, a class's behavioral state machine
**Status:** Implemented
**Priority:** Medium
**Description:**
`RPStatechart` shall extend `IRPUnit` to wrap `IRPStatechart`. It shall expose
Java-mirrored methods: `addNewNodeByType(meta_type, x_position, y_position, width, height)`
(returns wrapped node), `createGraphics()`, `closeDiagram()`, and `deleteState(state)`
(accepts an `IRPModelElement`). The wrapper shall register itself for the meta class
`"Statechart"`.
**Implementation:** src/rhapsody_cli/models/elements/classifiers.py:RPStatechart
**Last Changed:** 2026-07-07

---

## SWR_ELEM_00013: Element Module Registration on Import

**ID:** SWR_ELEM_00013
**Title:** Importing rhapsody_cli.models.elements registers all core element wrappers
**Status:** Implemented
**Priority:** High
**Description:**
The `rhapsody_cli.models.elements` package `__init__.py` shall import the family
wrapper modules (`classifiers`, `containment`, `diagrams`, `relations`,
`requirements`, `variables`). Those modules shall call `register_wrapper` at import
time so that, after importing the package, the `wrap()` factory is populated for all
core element types. Legacy one-class modules may re-export wrappers for backward
compatibility, but they shall not change registry contents.
**Implementation:** src/rhapsody_cli/models/elements/__init__.py
**Last Changed:** 2026-07-07
