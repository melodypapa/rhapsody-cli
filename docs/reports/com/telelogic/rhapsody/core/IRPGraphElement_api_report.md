# Rhapsody API Validation: IRPGraphElement

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPGraphElement` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`)
- Members: Python `22`, Java `22`, pywin32 `19`
- Deviation items: `6` (actionable `6`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_associated_image() -> associatedImage; set_associated_image() -> associatedImage | getAssociatedImage (method); setAssociatedImage (method) | associatedImage (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_graphical_parent() -> getGraphicalParent | getGraphicalParent (method) | graphicalParent (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the graphicalParent property or a getter/setter fallback instead of calling getGraphicalParent directly. |
| get_image_layout() -> imageLayout; set_image_layout() -> imageLayout | getImageLayout (method); setImageLayout (method) | imageLayout (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_interface_name() -> interfaceName | getInterfaceName (method) | interfaceName (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_model_object() -> getModelObject | getModelObject (method) | modelObject (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the modelObject property or a getter/setter fallback instead of calling getModelObject directly. |
| get_selected_image() -> selectedImage; set_selected_image() -> selectedImage | getSelectedImage (method); setSelectedImage (method) | selectedImage (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (10) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_property() -> addProperty | addProperty (method) | addProperty (method) | MATCH | — |
| get_all_graphical_properties() -> getAllGraphicalProperties | getAllGraphicalProperties (method) | getAllGraphicalProperties (method) | MATCH | — |
| get_all_properties() -> getAllProperties | getAllProperties (method) | getAllProperties (method) | MATCH | — |
| apply_default_format() -> applyDefaultFormat | applyDefaultFormat (method) | applyDefaultFormat (method) | MATCH | — |
| get_diagram() -> getDiagram | getDiagram (method) | getDiagram (method) | MATCH | — |
| get_graphical_property() -> getGraphicalProperty; set_graphical_property() -> setGraphicalProperty | getGraphicalProperty (method); setGraphicalProperty (method) | getGraphicalProperty (method); setGraphicalProperty (method) | MATCH | — |
| get_graphical_property_of_text() -> getGraphicalPropertyOfText; set_graphical_property_of_text() -> setGraphicalPropertyOfText | getGraphicalPropertyOfText (method); setGraphicalPropertyOfText (method) | getGraphicalPropertyOfText (method); setGraphicalPropertyOfText (method) | MATCH | — |
| get_local_properties() -> getLocalProperties | getLocalProperties (method) | getLocalProperties (method) | MATCH | — |
| get_property_value() -> getPropertyValue; set_property_value() -> setPropertyValue | getPropertyValue (method); setPropertyValue (method) | getPropertyValue (method); setPropertyValue (method) | MATCH | — |
| remove_property() -> removeProperty | removeProperty (method) | removeProperty (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (4 findings)
- **Target:** `IRPGraphElement` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_associated_image() -> associatedImage; set_associated_image() -> associatedImage; get_image_layout() -> imageLayout; set_image_layout() -> imageLayout; get_interface_name() -> interfaceName; get_selected_image() -> selectedImage; set_selected_image() -> selectedImage
- **Java signature(s):** `IRPGraphElement.getAssociatedImage()`, `IRPGraphElement.setSelectedImage(java.lang.String)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPGraphElement` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_graphical_parent() -> getGraphicalParent; get_model_object() -> getModelObject
- **Recommended change:** Use the graphicalParent property or a getter/setter fallback instead of calling getGraphicalParent directly.
- **Recommended change:** Use the modelObject property or a getter/setter fallback instead of calling getModelObject directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
