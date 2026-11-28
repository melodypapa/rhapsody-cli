## SWR_ELEM_00010: IRPRequirement Wrapper

**ID:** SWR_ELEM_00010
**Title:** IRPRequirement wraps a traceable requirement in the model
**Status:** Implemented
**Priority:** Medium
**Description:**
The JavaDoc `IRPRequirement` interface represents a requirement in a Rhapsody
model and extends `IRPAnnotation`. The Python `IRPRequirement` wrapper shall
extend `IRPAnnotation` and register for meta class `"Requirement"`. JavaDoc's
`getRequirementID()` / `setRequirementID(String)` accessors map to the pywin32
read/write `requirementID` property and are exposed as the single Python
`requirement_id` property. The wrapper casts generic pywin model-element
dispatches to the exact `IRPRequirement` interface before accessing that
property.
**Implementation:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_requirement.py:IRPRequirement`
**Last Changed:** 2026-03-19
