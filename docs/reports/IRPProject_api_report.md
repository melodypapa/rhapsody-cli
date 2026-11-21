# Rhapsody API Validation: IRPProject

## Summary
- Target wrapper: `RPProject` (`src/rhapsody_cli/models/elements/containment/model_project.py`)
- Members: Python `311`, Java `316`, pywin32 `287`
- Deviations: `18`
- Deviations by status:
  - `COM_MEMBER_NOT_EXPOSED`: 4
  - `PYTHON_METHOD_NAME_MISMATCH`: 4
  - `PYWIN32_MEMBER_MISSING`: 10

- Informational binding differences (expected): `85`
- Wrapper backlog (supported members without wrappers): `8`
- Documented aliases: `0`, documented unavailable: `0`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| add_instance_specification() -> addInstanceSpecification | addInstanceSpecification (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| add_statechart_diagram() -> addStatechart | addStatechart (method) | addStatechart (method) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| get_description_html() -> descriptionHTML; get_description_html() -> getDescriptionHTML | getDescriptionHTML (method); setDescriptionHTML (method) | descriptionHTML (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| enable_rhapsody_model_manager() -> enableRhapsodyModelManager | enableRhapsodyModelManager (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| gateway_export_to_xml() -> gatewayExportToXML | gatewayExportToXML (method) | GatewayExportToXML (method) | COM_MEMBER_NOT_EXPOSED | Change the COM call to a member exposed by the registered pywin32 interface. |
| gateway_export_to_xml2() -> gatewayExportToXML2 | gatewayExportToXML2 (method) | GatewayExportToXML2 (method) | COM_MEMBER_NOT_EXPOSED | Change the COM call to a member exposed by the registered pywin32 interface. |
| generate_report() -> generateReport | generateReport (method) | GenerateReport (method) | COM_MEMBER_NOT_EXPOSED | Change the COM call to a member exposed by the registered pywin32 interface. |
| set_global_configuration() -> globalConfiguration; set_global_configuration() -> setGlobalConfiguration | setGlobalConfiguration (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| login_to_remote_artifact_server() -> loginToRemoteArtifactServer | loginToRemoteArtifactServer (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| migrate_design_manager_links() -> migrateDesignManagerLinks | migrateDesignManagerLinks (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| recalculate_events_base_id() -> reCalculateEventsBaseId | reCalculateEventsBaseId (method) | reCalculateEventsBaseId (method) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| get_rmm_url() -> getRmmUrl; get_rmm_url() -> rmmUrl | getRmmUrl (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_root_instance_specifications() -> getRootInstanceSpecifications; get_root_instance_specifications() -> rootInstanceSpecifications | getRootInstanceSpecifications (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_saved_in_separate_directory() -> getSavedInSeperateDirectory; get_saved_in_separate_directory() -> savedInSeperateDirectory; set_saved_in_separate_directory() -> savedInSeperateDirectory; set_saved_in_separate_directory() -> setSavedInSeperateDirectory | getSavedInSeperateDirectory (method); setSavedInSeperateDirectory (method) | savedInSeperateDirectory (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| update_contained_diagrams_on_server() -> updateContainedDiagramsOnServer | updateContainedDiagramsOnServer (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| update_contained_matrices_on_server() -> updateContainedMatricesOnServer | updateContainedMatricesOnServer (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| update_contained_tables_on_server() -> updateContainedTablesOnServer | updateContainedTablesOnServer (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| set_use_unique_stereotype_and_ref_cache() -> setUseUniqueStereotypeAndRefCache; set_use_unique_stereotype_and_ref_cache() -> useUniqueStereotypeAndRefCache | setUseUniqueStereotypeAndRefCache (method) | UseUniqueStereotypeAndRefCache (property) | COM_MEMBER_NOT_EXPOSED | Use the UseUniqueStereotypeAndRefCache property or a getter/setter fallback instead of calling setUseUniqueStereotypeAndRefCache and useUniqueStereotypeAndRefCache directly. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| is_a_template() -> aTemplate | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_active_component() -> activeComponent; get_active_component() -> getActiveComponent; set_active_component() -> setActiveComponent | getActiveComponent (method); setActiveComponent (method) | activeComponent (property); setActiveComponent (method) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_active_configuration() -> activeConfiguration; get_active_configuration() -> getActiveConfiguration; set_active_configuration() -> setActiveConfiguration | getActiveConfiguration (method); setActiveConfiguration (method) | activeConfiguration (property); setActiveConfiguration (method) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| is_actively_managed() -> activelyManaged | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_actors() -> actors; get_actors() -> getActors | getActors (method) | actors (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_all_stereotypes() -> allStereotypes; get_all_stereotypes() -> getAllStereotypes | getAllStereotypes (method) | allStereotypes (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_all_tags() -> allTags; get_all_tags() -> getAllTags | getAllTags (method) | allTags (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_annotations() -> annotations; get_annotations() -> getAnnotations | getAnnotations (method) | annotations (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_association_classes() -> associationClasses; get_association_classes() -> getAssociationClasses | getAssociationClasses (method) | associationClasses (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_behavioral_diagrams() -> behavioralDiagrams; get_behavioral_diagrams() -> getBehavioralDiagrams | getBehavioralDiagrams (method) | behavioralDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_binary_id() -> BinaryID; get_binary_id() -> getBinaryID | getBinaryID (method) | BinaryID (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_cm_header() -> CMHeader; get_cm_header() -> getCMHeader; set_cm_header() -> CMHeader; set_cm_header() -> setCMHeader | getCMHeader (method); setCMHeader (method) | CMHeader (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_cg_simplified_model_package() -> cgSimplifiedModelPackage; get_cg_simplified_model_package() -> getCgSimplifiedModelPackage | getCgSimplifiedModelPackage (method) | cgSimplifiedModelPackage (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_classes() -> classes; get_classes() -> getClasses | getClasses (method) | classes (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_collaboration_diagrams() -> collaborationDiagrams; get_collaboration_diagrams() -> getCollaborationDiagrams | getCollaborationDiagrams (method) | collaborationDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_component_diagrams() -> componentDiagrams; get_component_diagrams() -> getComponentDiagrams | getComponentDiagrams (method) | componentDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_components() -> components; get_components() -> getComponents | getComponents (method) | components (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_constraints() -> constraints; get_constraints() -> getConstraints | getConstraints (method) | constraints (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_constraints_by_him() -> constraintsByHim; get_constraints_by_him() -> getConstraintsByHim | getConstraintsByHim (method) | constraintsByHim (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_controlled_files() -> controlledFiles; get_controlled_files() -> getControlledFiles | getControlledFiles (method) | controlledFiles (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_current_directory() -> currentDirectory; get_current_directory() -> getCurrentDirectory | getCurrentDirectory (method) | currentDirectory (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_default_directory_scheme() -> defaultDirectoryScheme; get_default_directory_scheme() -> getDefaultDirectoryScheme; set_default_directory_scheme() -> defaultDirectoryScheme; set_default_directory_scheme() -> setDefaultDirectoryScheme | getDefaultDirectoryScheme (method); setDefaultDirectoryScheme (method) | defaultDirectoryScheme (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_dependencies() -> dependencies; get_dependencies() -> getDependencies | getDependencies (method) | dependencies (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_deployment_diagrams() -> deploymentDiagrams; get_deployment_diagrams() -> getDeploymentDiagrams | getDeploymentDiagrams (method) | deploymentDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_description() -> description; get_description() -> getDescription; set_description() -> description; set_description() -> setDescription | getDescription (method); setDescription (method) | description (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_description_plain_text() -> descriptionPlainText; get_description_plain_text() -> getDescriptionPlainText | getDescriptionPlainText (method) | descriptionPlainText (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_description_rtf() -> descriptionRTF; get_description_rtf() -> getDescriptionRTF; is_description_rtf() -> descriptionRTF; set_description_rtf() -> descriptionRTF; set_description_rtf() -> setDescriptionRTF | getDescriptionRTF (method); setDescriptionRTF (method) | descriptionRTF (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_display_name() -> displayName; get_display_name() -> getDisplayName; set_display_name() -> displayName; set_display_name() -> setDisplayName | getDisplayName (method); setDisplayName (method) | displayName (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_events() -> events; get_events() -> getEvents | getEvents (method) | events (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_events_base_id() -> eventsBaseId; get_events_base_id() -> getEventsBaseId | getEventsBaseId (method) | eventsBaseId (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| check_events_base_ids_solve_collisions() -> eventsBaseIdsSolveCollisions | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_filename() -> filename; get_filename() -> getFilename; set_filename() -> filename; set_filename() -> setFilename | getFilename (method); setFilename (method) | filename (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_flow_items() -> flowItems; get_flow_items() -> getFlowItems | getFlowItems (method) | flowItems (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_flows() -> flows; get_flows() -> getFlows | getFlows (method) | flows (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_guid() -> GUID; get_guid() -> getGUID; set_guid() -> GUID; set_guid() -> setGUID | getGUID (method); setGUID (method) | GUID (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_global_functions() -> getGlobalFunctions; get_global_functions() -> globalFunctions | getGlobalFunctions (method) | globalFunctions (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_global_objects() -> getGlobalObjects; get_global_objects() -> globalObjects | getGlobalObjects (method) | globalObjects (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_global_variables() -> getGlobalVariables; get_global_variables() -> globalVariables | getGlobalVariables (method) | globalVariables (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_hyper_links() -> getHyperLinks; get_hyper_links() -> hyperLinks | getHyperLinks (method) | hyperLinks (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_include_in_next_load() -> getIncludeInNextLoad; get_include_in_next_load() -> includeInNextLoad; set_include_in_next_load() -> includeInNextLoad; set_include_in_next_load() -> setIncludeInNextLoad | getIncludeInNextLoad (method); setIncludeInNextLoad (method) | includeInNextLoad (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_instance_specifications() -> getInstanceSpecifications; get_instance_specifications() -> instanceSpecifications | getInstanceSpecifications (method) | instanceSpecifications (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_interface_name() -> getInterfaceName; get_interface_name() -> interfaceName | getInterfaceName (method) | interfaceName (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_external() -> getIsExternal; get_is_external() -> isExternal | getIsExternal (method) | isExternal (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_of_meta_class() -> isOfMetaClass | getIsOfMetaClass (method) | isOfMetaClass (method) | ACCESSOR_ALIAS_MISMATCH | Review the related API spellings and document the intended mapping. |
| get_is_show_display_name() -> getIsShowDisplayName; get_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> setIsShowDisplayName | getIsShowDisplayName (method); setIsShowDisplayName (method) | isShowDisplayName (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_stub() -> getIsStub; get_is_stub() -> isStub | getIsStub (method) | isStub (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_unresolved() -> getIsUnresolved; get_is_unresolved() -> isUnresolved | getIsUnresolved (method) | isUnresolved (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_links() -> getLinks; get_links() -> links | getLinks (method) | links (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_local_tags() -> getLocalTags; get_local_tags() -> localTags | getLocalTags (method) | localTags (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_main_diagram() -> getMainDiagram; get_main_diagram() -> mainDiagram; set_main_diagram() -> mainDiagram; set_main_diagram() -> setMainDiagram | getMainDiagram (method); setMainDiagram (method) | mainDiagram (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_meta_class() -> getMetaClass; get_meta_class() -> metaClass | getMetaClass (method) | metaClass (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| is_modified() -> modified | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_modules() -> getModules; get_modules() -> modules | getModules (method) | modules (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_name() -> getName; get_name() -> name; set_name() -> name; set_name() -> setName | getName (method); setName (method) | name (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_nested_classifiers() -> getNestedClassifiers; get_nested_classifiers() -> nestedClassifiers | getNestedClassifiers (method) | nestedClassifiers (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_nested_components() -> getNestedComponents; get_nested_components() -> nestedComponents | getNestedComponents (method) | nestedComponents (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_nodes() -> getNodes; get_nodes() -> nodes | getNodes (method) | nodes (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_object_model_diagrams() -> getObjectModelDiagrams; get_object_model_diagrams() -> objectModelDiagrams | getObjectModelDiagrams (method) | objectModelDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_of_template() -> getOfTemplate; get_of_template() -> ofTemplate; set_of_template() -> ofTemplate; set_of_template() -> setOfTemplate | getOfTemplate (method); setOfTemplate (method) | ofTemplate (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_owner() -> getOwner; get_owner() -> owner; set_owner() -> owner; set_owner() -> setOwner | getOwner (method); setOwner (method) | owner (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_nested_packages() -> getPackages; get_nested_packages() -> packages; get_packages() -> getPackages; get_packages() -> packages | getPackages (method) | packages (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_panel_diagrams() -> getPanelDiagrams; get_panel_diagrams() -> panelDiagrams | getPanelDiagrams (method) | panelDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_profiles() -> getProfiles; get_profiles() -> profiles | getProfiles (method) | profiles (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_project() -> getProject; get_project() -> project | getProject (method) | project (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| create_oslc_link() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| delete_oslc_link() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_oslc_links() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| set_description_html() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| is_reference_unit() -> referenceUnit | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_references() -> getReferences; get_references() -> references | getReferences (method) | references (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| is_remote() -> remote | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_requirement_traceability_handle() -> getRequirementTraceabilityHandle; get_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> setRequirementTraceabilityHandle | getRequirementTraceabilityHandle (method); setRequirementTraceabilityHandle (method) | requirementTraceabilityHandle (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_sequence_diagrams() -> getSequenceDiagrams; get_sequence_diagrams() -> sequenceDiagrams | getSequenceDiagrams (method) | sequenceDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_source_artifacts() -> getSourceArtifacts; get_source_artifacts() -> sourceArtifacts | getSourceArtifacts (method) | sourceArtifacts (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_stereotypes() -> getStereotypes; get_stereotypes() -> stereotypes | getStereotypes (method) | stereotypes (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_structure_diagrams() -> getStructureDiagrams; get_structure_diagrams() -> structureDiagrams | getStructureDiagrams (method) | structureDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_template_parameters() -> getTemplateParameters; get_template_parameters() -> templateParameters | getTemplateParameters (method) | templateParameters (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_ti() -> getTi; get_ti() -> ti; set_ti() -> setTi; set_ti() -> ti | getTi (method); setTi (method) | ti (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_timing_diagrams() -> getTimingDiagrams; get_timing_diagrams() -> timingDiagrams | getTimingDiagrams (method) | timingDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_types() -> getTypes; get_types() -> types | getTypes (method) | types (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_unit_path() -> getUnitPath; set_unit_path() -> setUnitPath; set_unit_path() -> unitPath | getUnitPath (method); setUnitPath (method) | setUnitPath (method) | ACCESSOR_ALIAS_MISMATCH | Review the related API spellings and document the intended mapping. |
| get_use_case_diagrams() -> getUseCaseDiagrams; get_use_case_diagrams() -> useCaseDiagrams | getUseCaseDiagrams (method) | useCaseDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_use_cases() -> getUseCases; get_use_cases() -> useCases | getUseCases (method) | useCases (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_user_defined_meta_class() -> getUserDefinedMetaClass; get_user_defined_meta_class() -> userDefinedMetaClass | getUserDefinedMetaClass (method) | userDefinedMetaClass (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_user_defined_stereotypes() -> getUserDefinedStereotypes; get_user_defined_stereotypes() -> userDefinedStereotypes | getUserDefinedStereotypes (method) | userDefinedStereotypes (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | createOSLCLink (method) | createOSLCLink (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteOSLCLink (method) | deleteOSLCLink (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | lockOnDesignManager (method) | lockOnDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | moveToDesignManager (method) | moveToDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | moveToDesignManagerAfterLogin (method) | moveToDesignManagerAfterLogin (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getOSLCLinks (method) | getOSLCLinks (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getStereotype (method); setStereotype (method) | stereotype (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | unlockOnDesignManager (method) | unlockOnDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |

## AI Fix Guidance

### Finding 1: PYWIN32_MEMBER_MISSING
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** add_instance_specification() -> addInstanceSpecification
- **Expected Python method(s):** `add_instance_specification`
- **Java signature(s):** `IRPPackage.addInstanceSpecification(java.lang.String, com.telelogic.rhapsody.core.IRPClassifier)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 2: PYTHON_METHOD_NAME_MISMATCH
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** add_statechart_diagram() -> addStatechart
- **Expected Python method(s):** `add_statechart`
- **Java signature(s):** `IRPPackage.addStatechart()`
- **pywin32 member(s):** addStatechart (method)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 3: PYTHON_METHOD_NAME_MISMATCH
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** get_description_html() -> descriptionHTML; get_description_html() -> getDescriptionHTML
- **Expected Python method(s):** `get_description_html`, `set_description_html`
- **Java signature(s):** `IRPModelElement.getDescriptionHTML()`, `IRPModelElement.setDescriptionHTML(java.lang.String)`
- **pywin32 member(s):** descriptionHTML (property)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 4: PYWIN32_MEMBER_MISSING
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** enable_rhapsody_model_manager() -> enableRhapsodyModelManager
- **Expected Python method(s):** `enable_rhapsody_model_manager`
- **Java signature(s):** `IRPProject.enableRhapsodyModelManager()`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 5: COM_MEMBER_NOT_EXPOSED
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** gateway_export_to_xml() -> gatewayExportToXML
- **Expected Python method(s):** `gateway_export_to_xml`
- **Java signature(s):** `IRPProject.gatewayExportToXML(java.lang.String, java.lang.String)`
- **pywin32 member(s):** GatewayExportToXML (method)
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 6: COM_MEMBER_NOT_EXPOSED
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** gateway_export_to_xml2() -> gatewayExportToXML2
- **Expected Python method(s):** `gateway_export_to_xml2`
- **Java signature(s):** `IRPProject.gatewayExportToXML2(java.lang.String, java.lang.String, com.telelogic.rhapsody.core.IRPProject)`
- **pywin32 member(s):** GatewayExportToXML2 (method)
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 7: COM_MEMBER_NOT_EXPOSED
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** generate_report() -> generateReport
- **Expected Python method(s):** `generate_report`
- **Java signature(s):** `IRPProject.generateReport(java.lang.String, java.lang.String, java.lang.String, java.lang.String, int, int)`
- **pywin32 member(s):** GenerateReport (method)
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 8: PYWIN32_MEMBER_MISSING
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** set_global_configuration() -> globalConfiguration; set_global_configuration() -> setGlobalConfiguration
- **Expected Python method(s):** `set_global_configuration`
- **Java signature(s):** `IRPProject.setGlobalConfiguration(java.lang.String, java.lang.String)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 9: PYWIN32_MEMBER_MISSING
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** login_to_remote_artifact_server() -> loginToRemoteArtifactServer
- **Expected Python method(s):** `login_to_remote_artifact_server`
- **Java signature(s):** `IRPPackage.loginToRemoteArtifactServer()`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 10: PYWIN32_MEMBER_MISSING
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** migrate_design_manager_links() -> migrateDesignManagerLinks
- **Expected Python method(s):** `migrate_design_manager_links`
- **Java signature(s):** `IRPProject.migrateDesignManagerLinks()`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 11: PYTHON_METHOD_NAME_MISMATCH
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** recalculate_events_base_id() -> reCalculateEventsBaseId
- **Expected Python method(s):** `re_calculate_events_base_id`
- **Java signature(s):** `IRPPackage.reCalculateEventsBaseId()`
- **pywin32 member(s):** reCalculateEventsBaseId (method)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 12: PYWIN32_MEMBER_MISSING
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** get_rmm_url() -> getRmmUrl; get_rmm_url() -> rmmUrl
- **Expected Python method(s):** `get_rmm_url`
- **Java signature(s):** `IRPModelElement.getRmmUrl()`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 13: PYWIN32_MEMBER_MISSING
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** get_root_instance_specifications() -> getRootInstanceSpecifications; get_root_instance_specifications() -> rootInstanceSpecifications
- **Expected Python method(s):** `get_root_instance_specifications`
- **Java signature(s):** `IRPPackage.getRootInstanceSpecifications()`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 14: PYTHON_METHOD_NAME_MISMATCH
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** get_saved_in_separate_directory() -> getSavedInSeperateDirectory; get_saved_in_separate_directory() -> savedInSeperateDirectory; set_saved_in_separate_directory() -> savedInSeperateDirectory; set_saved_in_separate_directory() -> setSavedInSeperateDirectory
- **Expected Python method(s):** `get_saved_in_seperate_directory`, `set_saved_in_seperate_directory`
- **Java signature(s):** `IRPPackage.getSavedInSeperateDirectory()`, `IRPPackage.setSavedInSeperateDirectory(int)`
- **pywin32 member(s):** savedInSeperateDirectory (property)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 15: PYWIN32_MEMBER_MISSING
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** update_contained_diagrams_on_server() -> updateContainedDiagramsOnServer
- **Expected Python method(s):** `update_contained_diagrams_on_server`
- **Java signature(s):** `IRPPackage.updateContainedDiagramsOnServer(int)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 16: PYWIN32_MEMBER_MISSING
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** update_contained_matrices_on_server() -> updateContainedMatricesOnServer
- **Expected Python method(s):** `update_contained_matrices_on_server`
- **Java signature(s):** `IRPPackage.updateContainedMatricesOnServer(int)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 17: PYWIN32_MEMBER_MISSING
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** update_contained_tables_on_server() -> updateContainedTablesOnServer
- **Expected Python method(s):** `update_contained_tables_on_server`
- **Java signature(s):** `IRPPackage.updateContainedTablesOnServer(int)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 18: COM_MEMBER_NOT_EXPOSED
- **Target:** `RPProject` in `src/rhapsody_cli/models/elements/containment/model_project.py`
- **Current Python wrapper/COM call:** set_use_unique_stereotype_and_ref_cache() -> setUseUniqueStereotypeAndRefCache; set_use_unique_stereotype_and_ref_cache() -> useUniqueStereotypeAndRefCache
- **Expected Python method(s):** `set_use_unique_stereotype_and_ref_cache`
- **Java signature(s):** `IRPProject.setUseUniqueStereotypeAndRefCache(int)`
- **pywin32 member(s):** UseUniqueStereotypeAndRefCache (property)
- **Recommended change:** Use the UseUniqueStereotypeAndRefCache property or a getter/setter fallback instead of calling setUseUniqueStereotypeAndRefCache and useUniqueStereotypeAndRefCache directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
