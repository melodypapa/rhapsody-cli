# Rhapsody API Validation: IRPModelElement

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPModelElement` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_model_element.py`)
- Members: Python `103`, Java `119`, pywin32 `104`
- Deviation items: `38` (actionable `33`, expected binding differences `2`, wrapper backlog `3`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| all_tags() -> allTags | getAllTags (method) | allTags (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| annotations() -> annotations | getAnnotations (method) | annotations (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| association_classes() -> associationClasses | getAssociationClasses (method) | associationClasses (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| binary_id() -> BinaryID | getBinaryID (method) | BinaryID (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| constraints() -> constraints | getConstraints (method) | constraints (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| constraints_by_him() -> constraintsByHim | getConstraintsByHim (method) | constraintsByHim (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| controlled_files() -> controlledFiles | getControlledFiles (method) | controlledFiles (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| dependencies() -> dependencies | getDependencies (method) | dependencies (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| description() -> description | getDescription (method); setDescription (method) | description (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| description_html() -> descriptionHTML; set_description_html() (no static COM member) | getDescriptionHTML (method); setDescriptionHTML (method) | descriptionHTML (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| description_plain_text() -> descriptionPlainText | getDescriptionPlainText (method) | descriptionPlainText (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| description_rtf() -> descriptionRTF | getDescriptionRTF (method); setDescriptionRTF (method) | descriptionRTF (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| display_name() -> displayName | getDisplayName (method); setDisplayName (method) | displayName (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| guid() -> GUID | getGUID (method); setGUID (method) | GUID (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| hyper_links() -> hyperLinks | getHyperLinks (method) | hyperLinks (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| interface_name() -> interfaceName | getInterfaceName (method) | interfaceName (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| is_external() -> isExternal | getIsExternal (method) | isExternal (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| is_show_display_name() -> isShowDisplayName | getIsShowDisplayName (method); setIsShowDisplayName (method) | isShowDisplayName (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| is_unresolved() -> isUnresolved | getIsUnresolved (method) | isUnresolved (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| local_tags() -> localTags | getLocalTags (method) | localTags (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| main_diagram() -> mainDiagram | getMainDiagram (method); setMainDiagram (method) | mainDiagram (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| meta_class() -> metaClass | getMetaClass (method) | metaClass (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| name() -> name | getName (method); setName (method) | name (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| of_template() -> ofTemplate | getOfTemplate (method); setOfTemplate (method) | ofTemplate (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| owner() -> owner | getOwner (method); setOwner (method) | owner (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| project() -> project | getProject (method) | project (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| references() -> references | getReferences (method) | references (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| requirement_traceability_handle() -> requirementTraceabilityHandle | getRequirementTraceabilityHandle (method); setRequirementTraceabilityHandle (method) | requirementTraceabilityHandle (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| stereotype() -> stereotype | getStereotype (method); setStereotype (method) | stereotype (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| stereotypes() -> stereotypes | getStereotypes (method) | stereotypes (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| template_parameters() -> templateParameters | getTemplateParameters (method) | templateParameters (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| ti() -> ti | getTi (method); setTi (method) | ti (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| user_defined_meta_class() -> userDefinedMetaClass | getUserDefinedMetaClass (method) | userDefinedMetaClass (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |

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
<summary>Correct items (64) — bindings verified against pywin32</summary>


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

### PYTHON_METHOD_NAME_MISMATCH (33 findings)
- **Target:** `IRPModelElement` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_model_element.py`
- **Affected call(s):** all_tags() -> allTags; annotations() -> annotations; association_classes() -> associationClasses; binary_id() -> BinaryID; constraints() -> constraints; constraints_by_him() -> constraintsByHim; controlled_files() -> controlledFiles; dependencies() -> dependencies; description() -> description; description_html() -> descriptionHTML; set_description_html() (no static COM member); description_plain_text() -> descriptionPlainText; description_rtf() -> descriptionRTF; display_name() -> displayName; guid() -> GUID; hyper_links() -> hyperLinks; interface_name() -> interfaceName; is_external() -> isExternal; is_show_display_name() -> isShowDisplayName; is_unresolved() -> isUnresolved; local_tags() -> localTags; main_diagram() -> mainDiagram; meta_class() -> metaClass; name() -> name; of_template() -> ofTemplate; owner() -> owner; project() -> project; references() -> references; requirement_traceability_handle() -> requirementTraceabilityHandle; stereotype() -> stereotype; stereotypes() -> stereotypes; template_parameters() -> templateParameters; ti() -> ti; user_defined_meta_class() -> userDefinedMetaClass
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
