# Rhapsody API Validation: IRPModelElement

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPModelElement` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_model_element.py`)
- Members: Python `113`, Java `118`, pywin32 `104`
- Deviation items: `6` (actionable `1`, expected binding differences `1`, wrapper backlog `4`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_error_message() -> getErrorMessage | — | getErrorMessage (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [0] arg(s) but pywin32 declares 1 parameter(s) (1 required; params: _MIDL__IRPModelElement0002_; types: —). Pass the documented parameters. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_rmm_url() (no static COM member) | getRmmUrl (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | lockOnDesignManager (method) | lockOnDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getOSLCLinks (method) | getOSLCLinks (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getStereotype (method); setStereotype (method) | stereotype (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | unlockOnDesignManager (method) | unlockOnDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |

<details>
<summary>Correct items (96) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_association() -> addAssociation | addAssociation (method) | addAssociation (method) | MATCH | — |
| add_dependency() -> addDependency | addDependency (method) | addDependency (method) | MATCH | — |
| add_dependency_between() -> addDependencyBetween | addDependencyBetween (method) | addDependencyBetween (method) | MATCH | — |
| add_dependency_to() -> addDependencyTo | addDependencyTo (method) | addDependencyTo (method) | MATCH | — |
| add_link_to_element() -> addLinkToElement | addLinkToElement (method) | addLinkToElement (method) | MATCH | — |
| add_new_aggr() -> addNewAggr | addNewAggr (method) | addNewAggr (method) | MATCH | — |
| add_property() -> addProperty | addProperty (method) | addProperty (method) | MATCH | — |
| add_redefines() -> addRedefines | addRedefines (method) | addRedefines (method) | MATCH | — |
| add_remote_dependency_to() -> addRemoteDependencyTo | addRemoteDependencyTo (method) | addRemoteDependencyTo (method) | MATCH | — |
| add_specific_stereotype() -> addSpecificStereotype | addSpecificStereotype (method) | addSpecificStereotype (method) | MATCH | — |
| add_stereotype() -> addStereotype | addStereotype (method) | addStereotype (method) | MATCH | — |
| become_template_instantiation_of() -> becomeTemplateInstantiationOf | becomeTemplateInstantiationOf (method) | becomeTemplateInstantiationOf (method) | MATCH | — |
| change_to() -> changeTo | changeTo (method) | changeTo (method) | MATCH | — |
| clone() -> clone | clone (method) | clone (method) | MATCH | — |
| create_oslc_link() (no static COM member) | createOSLCLink (method) | createOSLCLink (method) | MATCH | — |
| delete_dependency() -> deleteDependency | deleteDependency (method) | deleteDependency (method) | MATCH | — |
| delete_from_project() -> deleteFromProject | deleteFromProject (method) | deleteFromProject (method) | MATCH | — |
| delete_oslc_link() (no static COM member) | deleteOSLCLink (method) | deleteOSLCLink (method) | MATCH | — |
| error_message() -> errorMessage; get_error_message() -> getErrorMessage | errorMessage (method); getErrorMessage (method) | errorMessage (method); getErrorMessage (method) | MATCH | — |
| find_elements_by_full_name() -> findElementsByFullName | findElementsByFullName (method) | findElementsByFullName (method) | MATCH | — |
| find_nested_element() -> findNestedElement | findNestedElement (method) | findNestedElement (method) | MATCH | — |
| find_nested_element_recursive() -> findNestedElementRecursive | findNestedElementRecursive (method) | findNestedElementRecursive (method) | MATCH | — |
| get_all_tags() -> allTags | getAllTags (method) | allTags (property) | MATCH | — |
| get_annotations() -> annotations | getAnnotations (method) | annotations (property) | MATCH | — |
| get_association_classes() -> associationClasses | getAssociationClasses (method) | associationClasses (property) | MATCH | — |
| get_binary_id() -> BinaryID | getBinaryID (method) | BinaryID (property) | MATCH | — |
| get_constraints() -> constraints | getConstraints (method) | constraints (property) | MATCH | — |
| get_constraints_by_him() -> constraintsByHim | getConstraintsByHim (method) | constraintsByHim (property) | MATCH | — |
| get_controlled_files() -> controlledFiles | getControlledFiles (method) | controlledFiles (property) | MATCH | — |
| get_decoration_style() -> getDecorationStyle; set_decoration_style() -> setDecorationStyle | getDecorationStyle (method); setDecorationStyle (method) | getDecorationStyle (method); setDecorationStyle (method) | MATCH | — |
| get_dependencies() -> dependencies | getDependencies (method) | dependencies (property) | MATCH | — |
| get_description() -> description; set_description() -> description | getDescription (method); setDescription (method) | description (property) | MATCH | — |
| get_description_html() -> descriptionHTML; set_description_html() (no static COM member) | getDescriptionHTML (method); setDescriptionHTML (method) | descriptionHTML (property) | MATCH | — |
| get_description_plain_text() -> descriptionPlainText | getDescriptionPlainText (method) | descriptionPlainText (property) | MATCH | — |
| get_description_rtf() -> descriptionRTF; set_description_rtf() -> descriptionRTF | getDescriptionRTF (method); setDescriptionRTF (method) | descriptionRTF (property) | MATCH | — |
| get_display_name() -> displayName; set_display_name() -> displayName | getDisplayName (method); setDisplayName (method) | displayName (property) | MATCH | — |
| get_display_name_rtf() -> getDisplayNameRTF; set_display_name_rtf() -> setDisplayNameRTF | getDisplayNameRTF (method); setDisplayNameRTF (method) | getDisplayNameRTF (method); setDisplayNameRTF (method) | MATCH | — |
| get_full_path_name() -> getFullPathName | getFullPathName (method) | getFullPathName (method) | MATCH | — |
| get_full_path_name_in() -> getFullPathNameIn | getFullPathNameIn (method) | getFullPathNameIn (method) | MATCH | — |
| get_guid() -> GUID; set_guid() -> GUID | getGUID (method); setGUID (method) | GUID (property) | MATCH | — |
| get_hyper_links() -> hyperLinks | getHyperLinks (method) | hyperLinks (property) | MATCH | — |
| get_icon_file_name() -> getIconFileName | getIconFileName (method) | getIconFileName (method) | MATCH | — |
| get_interface_name() -> interfaceName | getInterfaceName (method) | interfaceName (property) | MATCH | — |
| get_is_external() -> isExternal | getIsExternal (method) | isExternal (property) | MATCH | — |
| get_is_of_meta_class() -> isOfMetaClass | getIsOfMetaClass (method) | isOfMetaClass (method) | MATCH | — |
| get_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> isShowDisplayName | getIsShowDisplayName (method); setIsShowDisplayName (method) | isShowDisplayName (property) | MATCH | — |
| get_is_unresolved() -> isUnresolved | getIsUnresolved (method) | isUnresolved (property) | MATCH | — |
| get_local_tags() -> localTags | getLocalTags (method) | localTags (property) | MATCH | — |
| get_main_diagram() -> mainDiagram; set_main_diagram() -> mainDiagram | getMainDiagram (method); setMainDiagram (method) | mainDiagram (property) | MATCH | — |
| get_meta_class() -> metaClass | getMetaClass (method) | metaClass (property) | MATCH | — |
| get_name() -> name; set_name() -> name | getName (method); setName (method) | name (property) | MATCH | — |
| get_nested_elements() -> getNestedElements | getNestedElements (method) | getNestedElements (method) | MATCH | — |
| get_nested_elements_by_meta_class() -> getNestedElementsByMetaClass | getNestedElementsByMetaClass (method) | getNestedElementsByMetaClass (method) | MATCH | — |
| get_nested_elements_recursive() -> getNestedElementsRecursive | getNestedElementsRecursive (method) | getNestedElementsRecursive (method) | MATCH | — |
| get_new_term_stereotype() -> getNewTermStereotype | getNewTermStereotype (method) | getNewTermStereotype (method) | MATCH | — |
| get_of_template() -> ofTemplate; set_of_template() -> ofTemplate | getOfTemplate (method); setOfTemplate (method) | ofTemplate (property) | MATCH | — |
| get_overlay_icon_file_name() -> getOverlayIconFileName | getOverlayIconFileName (method) | getOverlayIconFileName (method) | MATCH | — |
| get_overridden_properties() -> getOverriddenProperties | getOverriddenProperties (method) | getOverriddenProperties (method) | MATCH | — |
| get_overridden_properties_by_pattern() -> getOverriddenPropertiesByPattern | getOverriddenPropertiesByPattern (method) | getOverriddenPropertiesByPattern (method) | MATCH | — |
| get_owned_dependencies() -> getOwnedDependencies | getOwnedDependencies (method) | getOwnedDependencies (method) | MATCH | — |
| get_owner() -> owner; set_owner() -> owner | getOwner (method); setOwner (method) | owner (property) | MATCH | — |
| get_project() -> project | getProject (method) | project (property) | MATCH | — |
| get_property_value() -> getPropertyValue; set_property_value() -> setPropertyValue | getPropertyValue (method); setPropertyValue (method) | getPropertyValue (method); setPropertyValue (method) | MATCH | — |
| get_property_value_conditional() -> getPropertyValueConditional | getPropertyValueConditional (method) | getPropertyValueConditional (method) | MATCH | — |
| get_property_value_conditional_explicit() -> getPropertyValueConditionalExplicit | getPropertyValueConditionalExplicit (method) | getPropertyValueConditionalExplicit (method) | MATCH | — |
| get_property_value_explicit() -> getPropertyValueExplicit | getPropertyValueExplicit (method) | getPropertyValueExplicit (method) | MATCH | — |
| get_redefines() -> getRedefines | getRedefines (method) | getRedefines (method) | MATCH | — |
| get_references() -> references | getReferences (method) | references (property) | MATCH | — |
| get_remote_dependencies() -> getRemoteDependencies | getRemoteDependencies (method) | getRemoteDependencies (method) | MATCH | — |
| get_remote_uri() -> getRemoteURI | getRemoteURI (method) | getRemoteURI (method) | MATCH | — |
| get_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> requirementTraceabilityHandle | getRequirementTraceabilityHandle (method); setRequirementTraceabilityHandle (method) | requirementTraceabilityHandle (property) | MATCH | — |
| get_save_unit() -> getSaveUnit | getSaveUnit (method) | getSaveUnit (method) | MATCH | — |
| get_stereotypes() -> stereotypes | getStereotypes (method) | stereotypes (property) | MATCH | — |
| get_tag() -> getTag | getTag (method) | getTag (method) | MATCH | — |
| get_template_parameters() -> templateParameters | getTemplateParameters (method) | templateParameters (property) | MATCH | — |
| get_ti() -> ti; set_ti() -> ti | getTi (method); setTi (method) | ti (property) | MATCH | — |
| get_tool_tip_html() -> getToolTipHTML | getToolTipHTML (method) | getToolTipHTML (method) | MATCH | — |
| get_user_defined_meta_class() -> userDefinedMetaClass | getUserDefinedMetaClass (method) | userDefinedMetaClass (property) | MATCH | — |
| has_nested_elements() -> hasNestedElements | hasNestedElements (method) | hasNestedElements (method) | MATCH | — |
| has_panel_widget() -> hasPanelWidget | hasPanelWidget (method) | hasPanelWidget (method) | MATCH | — |
| high_light_element() -> highLightElement | highLightElement (method) | highLightElement (method) | MATCH | — |
| is_a_template() -> isATemplate | isATemplate (method) | isATemplate (method) | MATCH | — |
| is_description_rtf() -> isDescriptionRTF | isDescriptionRTF (method) | isDescriptionRTF (method) | MATCH | — |
| is_display_name_rtf() -> isDisplayNameRTF | isDisplayNameRTF (method) | isDisplayNameRTF (method) | MATCH | — |
| is_modified() -> isModified | isModified (method) | isModified (method) | MATCH | — |
| is_remote() -> isRemote | isRemote (method) | isRemote (method) | MATCH | — |
| locate_in_browser() -> locateInBrowser | locateInBrowser (method) | locateInBrowser (method) | MATCH | — |
| open_features_dialog() -> openFeaturesDialog | openFeaturesDialog (method) | openFeaturesDialog (method) | MATCH | — |
| remove_property() -> removeProperty | removeProperty (method) | removeProperty (method) | MATCH | — |
| remove_redefines() -> removeRedefines | removeRedefines (method) | removeRedefines (method) | MATCH | — |
| remove_stereotype() -> removeStereotype | removeStereotype (method) | removeStereotype (method) | MATCH | — |
| set_description_and_hyperlinks() -> setDescriptionAndHyperlinks | setDescriptionAndHyperlinks (method) | setDescriptionAndHyperlinks (method) | MATCH | — |
| set_tag_context_value() -> setTagContextValue | setTagContextValue (method) | setTagContextValue (method) | MATCH | — |
| set_tag_element_value() -> setTagElementValue | setTagElementValue (method) | setTagElementValue (method) | MATCH | — |
| set_tag_value() -> setTagValue | setTagValue (method) | setTagValue (method) | MATCH | — |
| synchronize_template_instantiation() -> synchronizeTemplateInstantiation | synchronizeTemplateInstantiation (method) | synchronizeTemplateInstantiation (method) | MATCH | — |

</details>

## AI Fix Guidance

### SIGNATURE_ARITY_MISMATCH (1 finding)
- **Target:** `IRPModelElement` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_model_element.py`
- **Affected call(s):** get_error_message() -> getErrorMessage
- **Recommended change:** Wrapper passes [0] arg(s) but pywin32 declares 1 parameter(s) (1 required; params: _MIDL__IRPModelElement0002_; types: —). Pass the documented parameters.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
