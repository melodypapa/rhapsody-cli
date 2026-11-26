# Software Requirements - ELEM (Model Element Wrappers)

**Category:** ELEM
**Prefix:** SWR
**Source:** Extracted from code
**Last Validated:** 2026-07-07

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
