# Rhapsody API Validation: IRPModelElement

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPModelElement` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_model_element.py`)
- Members: Python `103`, Java `119`, pywin32 `104`
- Deviation items: `7` (actionable `2`, expected binding differences `2`, wrapper backlog `3`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| constraints_by_him (property) (no static COM member) | getConstraintsByHim (method) | constraintsByHim (property) | PYTHON_METHOD_NAME_MISMATCH; COM_MEMBER_NOT_EXPOSED | Use the constraintsByHim property or a getter/setter fallback instead of calling getConstraintsByHim directly. |
| hyper_links (property) (no static COM member) | getHyperLinks (method) | hyperLinks (property) | PYTHON_METHOD_NAME_MISMATCH; COM_MEMBER_NOT_EXPOSED | Use the hyperLinks property or a getter/setter fallback instead of calling getHyperLinks directly. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | resolveRemoteArtifact (method) | — | JAVA_ONLY_MEMBER | Verify the Java documentation against the installed COM type library. |
| get_rmm_url() (no static COM member) | getRmmUrl (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | lockOnDesignManager (method) | lockOnDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getOSLCLinks (method) | getOSLCLinks (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | unlockOnDesignManager (method) | unlockOnDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |

<details>
<summary>Correct items (95) — bindings verified against pywin32</summary>


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
| all_tags (property) -> allTags | getAllTags (method) | allTags (property) | MATCH | — |
| annotations (property) -> annotations | getAnnotations (method) | annotations (property) | MATCH | — |
| association_classes (property) -> associationClasses | getAssociationClasses (method) | associationClasses (property) | MATCH | — |
| become_template_instantiation_of() -> becomeTemplateInstantiationOf | becomeTemplateInstantiationOf (method) | becomeTemplateInstantiationOf (method) | MATCH | — |
| binary_id (property) -> BinaryID | getBinaryID (method) | BinaryID (property) | MATCH | — |
| change_to() -> changeTo | changeTo (method) | changeTo (method) | MATCH | — |
| clone() -> clone | clone (method) | clone (method) | MATCH | — |
| constraints (property) -> constraints | getConstraints (method) | constraints (property) | MATCH | — |
| controlled_files (property) -> controlledFiles | getControlledFiles (method) | controlledFiles (property) | MATCH | — |
| create_oslc_link() (no static COM member) | createOSLCLink (method) | createOSLCLink (method) | MATCH | — |
| delete_dependency() -> deleteDependency | deleteDependency (method) | deleteDependency (method) | MATCH | — |
| delete_from_project() -> deleteFromProject | deleteFromProject (method) | deleteFromProject (method) | MATCH | — |
| delete_oslc_link() (no static COM member) | deleteOSLCLink (method) | deleteOSLCLink (method) | MATCH | — |
| dependencies (property) -> dependencies | getDependencies (method) | dependencies (property) | MATCH | — |
| description (property) -> description | getDescription (method); setDescription (method) | description (property) | MATCH | — |
| description_html (property) -> descriptionHTML; set_description_html() (no static COM member) | getDescriptionHTML (method); setDescriptionHTML (method) | descriptionHTML (property) | MATCH | — |
| description_plain_text (property) -> descriptionPlainText | getDescriptionPlainText (method) | descriptionPlainText (property) | MATCH | — |
| description_rtf (property) -> descriptionRTF | getDescriptionRTF (method); setDescriptionRTF (method) | descriptionRTF (property) | MATCH | — |
| display_name (property) -> displayName | getDisplayName (method); setDisplayName (method) | displayName (property) | MATCH | — |
| error_message() -> errorMessage; get_error_message() -> getErrorMessage | errorMessage (method); getErrorMessage (method) | errorMessage (method); getErrorMessage (method) | MATCH | — |
| find_elements_by_full_name() -> findElementsByFullName | findElementsByFullName (method) | findElementsByFullName (method) | MATCH | — |
| find_nested_element() -> findNestedElement | findNestedElement (method) | findNestedElement (method) | MATCH | — |
| find_nested_element_recursive() -> findNestedElementRecursive | findNestedElementRecursive (method) | findNestedElementRecursive (method) | MATCH | — |
| get_decoration_style() -> getDecorationStyle; set_decoration_style() -> setDecorationStyle | getDecorationStyle (method); setDecorationStyle (method) | getDecorationStyle (method); setDecorationStyle (method) | MATCH | — |
| get_display_name_rtf() -> getDisplayNameRTF; set_display_name_rtf() -> setDisplayNameRTF | getDisplayNameRTF (method); setDisplayNameRTF (method) | getDisplayNameRTF (method); setDisplayNameRTF (method) | MATCH | — |
| get_full_path_name() -> getFullPathName | getFullPathName (method) | getFullPathName (method) | MATCH | — |
| get_full_path_name_in() -> getFullPathNameIn | getFullPathNameIn (method) | getFullPathNameIn (method) | MATCH | — |
| get_icon_file_name() -> getIconFileName | getIconFileName (method) | getIconFileName (method) | MATCH | — |
| get_is_of_meta_class() -> isOfMetaClass | getIsOfMetaClass (method) | isOfMetaClass (method) | MATCH | — |
| get_nested_elements() -> getNestedElements | getNestedElements (method) | getNestedElements (method) | MATCH | — |
| get_nested_elements_by_meta_class() -> getNestedElementsByMetaClass | getNestedElementsByMetaClass (method) | getNestedElementsByMetaClass (method) | MATCH | — |
| get_nested_elements_recursive() -> getNestedElementsRecursive | getNestedElementsRecursive (method) | getNestedElementsRecursive (method) | MATCH | — |
| get_new_term_stereotype() -> getNewTermStereotype | getNewTermStereotype (method) | getNewTermStereotype (method) | MATCH | — |
| get_overlay_icon_file_name() -> getOverlayIconFileName | getOverlayIconFileName (method) | getOverlayIconFileName (method) | MATCH | — |
| get_overridden_properties() -> getOverriddenProperties | getOverriddenProperties (method) | getOverriddenProperties (method) | MATCH | — |
| get_overridden_properties_by_pattern() -> getOverriddenPropertiesByPattern | getOverriddenPropertiesByPattern (method) | getOverriddenPropertiesByPattern (method) | MATCH | — |
| get_owned_dependencies() -> getOwnedDependencies | getOwnedDependencies (method) | getOwnedDependencies (method) | MATCH | — |
| get_property_value() -> getPropertyValue; set_property_value() -> setPropertyValue | getPropertyValue (method); setPropertyValue (method) | getPropertyValue (method); setPropertyValue (method) | MATCH | — |
| get_property_value_conditional() -> getPropertyValueConditional | getPropertyValueConditional (method) | getPropertyValueConditional (method) | MATCH | — |
| get_property_value_conditional_explicit() -> getPropertyValueConditionalExplicit | getPropertyValueConditionalExplicit (method) | getPropertyValueConditionalExplicit (method) | MATCH | — |
| get_property_value_explicit() -> getPropertyValueExplicit | getPropertyValueExplicit (method) | getPropertyValueExplicit (method) | MATCH | — |
| get_redefines() -> getRedefines | getRedefines (method) | getRedefines (method) | MATCH | — |
| get_remote_dependencies() -> getRemoteDependencies | getRemoteDependencies (method) | getRemoteDependencies (method) | MATCH | — |
| get_remote_uri() -> getRemoteURI | getRemoteURI (method) | getRemoteURI (method) | MATCH | — |
| get_save_unit() -> getSaveUnit | getSaveUnit (method) | getSaveUnit (method) | MATCH | — |
| get_tag() -> getTag | getTag (method) | getTag (method) | MATCH | — |
| get_tool_tip_html() -> getToolTipHTML | getToolTipHTML (method) | getToolTipHTML (method) | MATCH | — |
| guid (property) -> GUID | getGUID (method); setGUID (method) | GUID (property) | MATCH | — |
| has_nested_elements() -> hasNestedElements | hasNestedElements (method) | hasNestedElements (method) | MATCH | — |
| has_panel_widget() -> hasPanelWidget | hasPanelWidget (method) | hasPanelWidget (method) | MATCH | — |
| high_light_element() -> highLightElement | highLightElement (method) | highLightElement (method) | MATCH | — |
| interface_name (property) -> interfaceName | getInterfaceName (method) | interfaceName (property) | MATCH | — |
| is_a_template() -> isATemplate | isATemplate (method) | isATemplate (method) | MATCH | — |
| is_description_rtf() -> isDescriptionRTF | isDescriptionRTF (method) | isDescriptionRTF (method) | MATCH | — |
| is_display_name_rtf() -> isDisplayNameRTF | isDisplayNameRTF (method) | isDisplayNameRTF (method) | MATCH | — |
| is_external (property) -> isExternal | getIsExternal (method) | isExternal (property) | MATCH | — |
| is_modified() -> isModified | isModified (method) | isModified (method) | MATCH | — |
| is_remote() -> isRemote | isRemote (method) | isRemote (method) | MATCH | — |
| is_show_display_name (property) -> isShowDisplayName | getIsShowDisplayName (method); setIsShowDisplayName (method) | isShowDisplayName (property) | MATCH | — |
| is_unresolved (property) -> isUnresolved | getIsUnresolved (method) | isUnresolved (property) | MATCH | — |
| local_tags (property) -> localTags | getLocalTags (method) | localTags (property) | MATCH | — |
| locate_in_browser() -> locateInBrowser | locateInBrowser (method) | locateInBrowser (method) | MATCH | — |
| main_diagram (property) -> mainDiagram | getMainDiagram (method); setMainDiagram (method) | mainDiagram (property) | MATCH | — |
| meta_class (property) -> metaClass | getMetaClass (method) | metaClass (property) | MATCH | — |
| name (property) -> name | getName (method); setName (method) | name (property) | MATCH | — |
| of_template (property) -> ofTemplate | getOfTemplate (method); setOfTemplate (method) | ofTemplate (property) | MATCH | — |
| open_features_dialog() -> openFeaturesDialog | openFeaturesDialog (method) | openFeaturesDialog (method) | MATCH | — |
| owner (property) -> owner | getOwner (method); setOwner (method) | owner (property) | MATCH | — |
| project (property) -> project | getProject (method) | project (property) | MATCH | — |
| references (property) -> references | getReferences (method) | references (property) | MATCH | — |
| remove_property() -> removeProperty | removeProperty (method) | removeProperty (method) | MATCH | — |
| remove_redefines() -> removeRedefines | removeRedefines (method) | removeRedefines (method) | MATCH | — |
| remove_stereotype() -> removeStereotype | removeStereotype (method) | removeStereotype (method) | MATCH | — |
| requirement_traceability_handle (property) -> requirementTraceabilityHandle | getRequirementTraceabilityHandle (method); setRequirementTraceabilityHandle (method) | requirementTraceabilityHandle (property) | MATCH | — |
| set_description_and_hyperlinks() -> setDescriptionAndHyperlinks | setDescriptionAndHyperlinks (method) | setDescriptionAndHyperlinks (method) | MATCH | — |
| set_tag_context_value() -> setTagContextValue | setTagContextValue (method) | setTagContextValue (method) | MATCH | — |
| set_tag_element_value() -> setTagElementValue | setTagElementValue (method) | setTagElementValue (method) | MATCH | — |
| set_tag_value() -> setTagValue | setTagValue (method) | setTagValue (method) | MATCH | — |
| stereotype (property) -> stereotype | getStereotype (method); setStereotype (method) | stereotype (property) | MATCH | — |
| stereotypes (property) -> stereotypes | getStereotypes (method) | stereotypes (property) | MATCH | — |
| synchronize_template_instantiation() -> synchronizeTemplateInstantiation | synchronizeTemplateInstantiation (method) | synchronizeTemplateInstantiation (method) | MATCH | — |
| template_parameters (property) -> templateParameters | getTemplateParameters (method) | templateParameters (property) | MATCH | — |
| ti (property) -> ti | getTi (method); setTi (method) | ti (property) | MATCH | — |
| user_defined_meta_class (property) -> userDefinedMetaClass | getUserDefinedMetaClass (method) | userDefinedMetaClass (property) | MATCH | — |

</details>

## AI Fix Guidance

### PYTHON_METHOD_NAME_MISMATCH; COM_MEMBER_NOT_EXPOSED (2 findings)
- **Target:** `IRPModelElement` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_model_element.py`
- **Affected call(s):** constraints_by_him (property) (no static COM member); hyper_links (property) (no static COM member)
- **Recommended change:** Use the constraintsByHim property or a getter/setter fallback instead of calling getConstraintsByHim directly.
- **Recommended change:** Use the hyperLinks property or a getter/setter fallback instead of calling getHyperLinks directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
