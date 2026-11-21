.. _rhapsody-java-interface-IRPModelElement:

RPModelElement
==============

The IRPModelElement interface is the base interface for all model elements.

- **Java interface:** IRPModelElement
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The base interface of all Rhapsody model elements.
- **Python wrapper:** RPModelElement
- **Python import:** ``from rhapsody_cli.models.core import RPModelElement``
- **Canonical module:** pending — the §2 package move is deferred until the IRPCollection and
  IRPUnit rows leave ``models/core.py`` (see ``docs/reports/sync-todo``).


Zero actionable deviations require code changes. Every migrated member calls exactly one
pywin32-exposed COM member: method-shaped members via ``call_com``, property-shaped members
via ``get_com_property``/``set_com_property``. ``get_rmm_url`` is a documented blocker: the
``getRmmUrl``/``rmmUrl`` members are absent from the committed pywin32 catalog, so its legacy
dual-binding call site stays unchanged until Windows typelib evidence lands. The
Python-implementation column reflects the post-migration single-member labels.


.. list-table:: Verified IRPModelElement deviations and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - getRmmUrl (method)
     - —
     - get_rmm_url() -> getRmmUrl; get_rmm_url() -> rmmUrl
     - PYWIN32_MEMBER_MISSING; Use a member exposed by the registered type library or verify the Rhapsody version.
   * - —
     - —
     - get_oslc_links() (no static COM member)
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - lockOnDesignManager (method)
     - lockOnDesignManager (method)
     - —
     - MISSING_PYTHON_WRAPPER; Implement the Python wrapper or mark this API member intentionally unsupported.
   * - getOSLCLinks (method)
     - getOSLCLinks (method)
     - —
     - MISSING_PYTHON_WRAPPER; Implement the Python wrapper or mark this API member intentionally unsupported.
   * - getStereotype (method); setStereotype (method)
     - stereotype (property)
     - —
     - MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Implement the Python wrapper or mark this API member intentionally unsupported.
   * - unlockOnDesignManager (method)
     - unlockOnDesignManager (method)
     - —
     - MISSING_PYTHON_WRAPPER; Implement the Python wrapper or mark this API member intentionally unsupported.

.. list-table:: Correct items (verified direct bindings)
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - addAssociation (method)
     - addAssociation (method)
     - add_association() -> addAssociation
     - MATCH; —
   * - addDependency (method)
     - addDependency (method)
     - add_dependency() -> addDependency
     - MATCH; —
   * - addDependencyBetween (method)
     - addDependencyBetween (method)
     - add_dependency_between() -> addDependencyBetween
     - MATCH; —
   * - addDependencyTo (method)
     - addDependencyTo (method)
     - add_dependency_to() -> addDependencyTo
     - MATCH; —
   * - addLinkToElement (method)
     - addLinkToElement (method)
     - add_link_to_element() -> addLinkToElement
     - MATCH; —
   * - addNewAggr (method)
     - addNewAggr (method)
     - add_new_aggr() -> addNewAggr
     - MATCH; —
   * - addProperty (method)
     - addProperty (method)
     - add_property() -> addProperty
     - MATCH; —
   * - addRedefines (method)
     - addRedefines (method)
     - add_redefines() -> addRedefines
     - MATCH; —
   * - addRemoteDependencyTo (method)
     - addRemoteDependencyTo (method)
     - add_remote_dependency_to() -> addRemoteDependencyTo
     - MATCH; —
   * - addSpecificStereotype (method)
     - addSpecificStereotype (method)
     - add_specific_stereotype() -> addSpecificStereotype
     - MATCH; —
   * - addStereotype (method)
     - addStereotype (method)
     - add_stereotype() -> addStereotype
     - MATCH; —
   * - becomeTemplateInstantiationOf (method)
     - becomeTemplateInstantiationOf (method)
     - become_template_instantiation_of() -> becomeTemplateInstantiationOf
     - MATCH; —
   * - changeTo (method)
     - changeTo (method)
     - change_to() -> changeTo
     - MATCH; —
   * - clone (method)
     - clone (method)
     - clone() -> clone
     - MATCH; —
   * - createOSLCLink (method)
     - createOSLCLink (method)
     - create_oslc_link() (no static COM member)
     - MATCH; —
   * - deleteDependency (method)
     - deleteDependency (method)
     - delete_dependency() -> deleteDependency
     - MATCH; —
   * - deleteFromProject (method)
     - deleteFromProject (method)
     - delete_from_project() -> deleteFromProject
     - MATCH; —
   * - deleteOSLCLink (method)
     - deleteOSLCLink (method)
     - delete_oslc_link() (no static COM member)
     - MATCH; —
   * - errorMessage (method); getErrorMessage (method)
     - errorMessage (method); getErrorMessage (method)
     - error_message() -> errorMessage; get_error_message() -> getErrorMessage
     - MATCH; —
   * - findElementsByFullName (method)
     - findElementsByFullName (method)
     - find_elements_by_full_name() -> findElementsByFullName
     - MATCH; —
   * - findNestedElement (method)
     - findNestedElement (method)
     - find_nested_element() -> findNestedElement
     - MATCH; —
   * - findNestedElementRecursive (method)
     - findNestedElementRecursive (method)
     - find_nested_element_recursive() -> findNestedElementRecursive
     - MATCH; —
   * - getAllTags (method)
     - allTags (property)
     - get_all_tags() -> allTags
     - MATCH; —
   * - getAnnotations (method)
     - annotations (property)
     - get_annotations() -> annotations
     - MATCH; —
   * - getAssociationClasses (method)
     - associationClasses (property)
     - get_association_classes() -> associationClasses
     - MATCH; —
   * - getBinaryID (method)
     - BinaryID (property)
     - get_binary_id() -> BinaryID
     - MATCH; —
   * - getConstraints (method)
     - constraints (property)
     - get_constraints() -> constraints
     - MATCH; —
   * - getConstraintsByHim (method)
     - constraintsByHim (property)
     - get_constraints_by_him() -> constraintsByHim
     - MATCH; —
   * - getControlledFiles (method)
     - controlledFiles (property)
     - get_controlled_files() -> controlledFiles
     - MATCH; —
   * - getDecorationStyle (method); setDecorationStyle (method)
     - getDecorationStyle (method); setDecorationStyle (method)
     - get_decoration_style() -> getDecorationStyle; set_decoration_style() -> setDecorationStyle
     - MATCH; —
   * - getDependencies (method)
     - dependencies (property)
     - get_dependencies() -> dependencies
     - MATCH; —
   * - getDescription (method); setDescription (method)
     - description (property)
     - get_description() -> description; set_description() -> description
     - MATCH; —
   * - getDescriptionHTML (method); setDescriptionHTML (method)
     - descriptionHTML (property)
     - get_description_html() -> descriptionHTML; set_description_html() (no static COM member)
     - MATCH; —
   * - getDescriptionPlainText (method)
     - descriptionPlainText (property)
     - get_description_plain_text() -> descriptionPlainText
     - MATCH; —
   * - getDescriptionRTF (method); setDescriptionRTF (method)
     - descriptionRTF (property)
     - get_description_rtf() -> descriptionRTF; is_description_rtf() -> isDescriptionRTF; set_description_rtf() -> descriptionRTF
     - MATCH; —
   * - getDisplayName (method); setDisplayName (method)
     - displayName (property)
     - get_display_name() -> displayName; set_display_name() -> displayName
     - MATCH; —
   * - getDisplayNameRTF (method); setDisplayNameRTF (method)
     - getDisplayNameRTF (method); setDisplayNameRTF (method)
     - get_display_name_rtf() -> getDisplayNameRTF; set_display_name_rtf() -> setDisplayNameRTF
     - MATCH; —
   * - getFullPathName (method)
     - getFullPathName (method)
     - get_full_path_name() -> getFullPathName
     - MATCH; —
   * - getFullPathNameIn (method)
     - getFullPathNameIn (method)
     - get_full_path_name_in() -> getFullPathNameIn
     - MATCH; —
   * - getGUID (method); setGUID (method)
     - GUID (property)
     - get_guid() -> GUID; set_guid() -> GUID
     - MATCH; —
   * - getHyperLinks (method)
     - hyperLinks (property)
     - get_hyper_links() -> hyperLinks
     - MATCH; —
   * - getIconFileName (method)
     - getIconFileName (method)
     - get_icon_file_name() -> getIconFileName
     - MATCH; —
   * - getInterfaceName (method)
     - interfaceName (property)
     - get_interface_name() -> interfaceName
     - MATCH; —
   * - getIsExternal (method)
     - isExternal (property)
     - get_is_external() -> isExternal
     - MATCH; —
   * - getIsOfMetaClass (method)
     - isOfMetaClass (method)
     - get_is_of_meta_class() -> isOfMetaClass
     - MATCH; —
   * - getIsShowDisplayName (method); setIsShowDisplayName (method)
     - isShowDisplayName (property)
     - get_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> isShowDisplayName
     - MATCH; —
   * - getIsUnresolved (method)
     - isUnresolved (property)
     - get_is_unresolved() -> isUnresolved
     - MATCH; —
   * - getLocalTags (method)
     - localTags (property)
     - get_local_tags() -> localTags
     - MATCH; —
   * - getMainDiagram (method); setMainDiagram (method)
     - mainDiagram (property)
     - get_main_diagram() -> mainDiagram; set_main_diagram() -> mainDiagram
     - MATCH; —
   * - getMetaClass (method)
     - metaClass (property)
     - get_meta_class() -> metaClass
     - MATCH; —
   * - getName (method); setName (method)
     - name (property)
     - get_name() -> name; set_name() -> name
     - MATCH; —
   * - getNestedElements (method)
     - getNestedElements (method)
     - get_nested_elements() -> getNestedElements
     - MATCH; —
   * - getNestedElementsByMetaClass (method)
     - getNestedElementsByMetaClass (method)
     - get_nested_elements_by_meta_class() -> getNestedElementsByMetaClass
     - MATCH; —
   * - getNestedElementsRecursive (method)
     - getNestedElementsRecursive (method)
     - get_nested_elements_recursive() -> getNestedElementsRecursive
     - MATCH; —
   * - getNewTermStereotype (method)
     - getNewTermStereotype (method)
     - get_new_term_stereotype() -> getNewTermStereotype
     - MATCH; —
   * - getOfTemplate (method); setOfTemplate (method)
     - ofTemplate (property)
     - get_of_template() -> ofTemplate; set_of_template() -> ofTemplate
     - MATCH; —
   * - getOverlayIconFileName (method)
     - getOverlayIconFileName (method)
     - get_overlay_icon_file_name() -> getOverlayIconFileName
     - MATCH; —
   * - getOverriddenProperties (method)
     - getOverriddenProperties (method)
     - get_overridden_properties() -> getOverriddenProperties
     - MATCH; —
   * - getOverriddenPropertiesByPattern (method)
     - getOverriddenPropertiesByPattern (method)
     - get_overridden_properties_by_pattern() -> getOverriddenPropertiesByPattern
     - MATCH; —
   * - getOwnedDependencies (method)
     - getOwnedDependencies (method)
     - get_owned_dependencies() -> getOwnedDependencies
     - MATCH; —
   * - getOwner (method); setOwner (method)
     - owner (property)
     - get_owner() -> owner; set_owner() -> owner
     - MATCH; —
   * - getProject (method)
     - project (property)
     - get_project() -> project
     - MATCH; —
   * - getPropertyValue (method); setPropertyValue (method)
     - getPropertyValue (method); setPropertyValue (method)
     - get_property_value() -> getPropertyValue; set_property_value() -> setPropertyValue
     - MATCH; —
   * - getPropertyValueConditional (method)
     - getPropertyValueConditional (method)
     - get_property_value_conditional() -> getPropertyValueConditional
     - MATCH; —
   * - getPropertyValueConditionalExplicit (method)
     - getPropertyValueConditionalExplicit (method)
     - get_property_value_conditional_explicit() -> getPropertyValueConditionalExplicit
     - MATCH; —
   * - getPropertyValueExplicit (method)
     - getPropertyValueExplicit (method)
     - get_property_value_explicit() -> getPropertyValueExplicit
     - MATCH; —
   * - getRedefines (method)
     - getRedefines (method)
     - get_redefines() -> getRedefines
     - MATCH; —
   * - getReferences (method)
     - references (property)
     - get_references() -> references
     - MATCH; —
   * - getRemoteDependencies (method)
     - getRemoteDependencies (method)
     - get_remote_dependencies() -> getRemoteDependencies
     - MATCH; —
   * - getRemoteURI (method)
     - getRemoteURI (method)
     - get_remote_uri() -> getRemoteURI
     - MATCH; —
   * - getRequirementTraceabilityHandle (method); setRequirementTraceabilityHandle (method)
     - requirementTraceabilityHandle (property)
     - get_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> requirementTraceabilityHandle
     - MATCH; —
   * - getSaveUnit (method)
     - getSaveUnit (method)
     - get_save_unit() -> getSaveUnit
     - MATCH; —
   * - getStereotypes (method)
     - stereotypes (property)
     - get_stereotypes() -> stereotypes
     - MATCH; —
   * - getTag (method)
     - getTag (method)
     - get_tag() -> getTag
     - MATCH; —
   * - getTemplateParameters (method)
     - templateParameters (property)
     - get_template_parameters() -> templateParameters
     - MATCH; —
   * - getTi (method); setTi (method)
     - ti (property)
     - get_ti() -> ti; set_ti() -> ti
     - MATCH; —
   * - getToolTipHTML (method)
     - getToolTipHTML (method)
     - get_tool_tip_html() -> getToolTipHTML
     - MATCH; —
   * - getUserDefinedMetaClass (method)
     - userDefinedMetaClass (property)
     - get_user_defined_meta_class() -> userDefinedMetaClass
     - MATCH; —
   * - hasNestedElements (method)
     - hasNestedElements (method)
     - has_nested_elements() -> hasNestedElements
     - MATCH; —
   * - hasPanelWidget (method)
     - hasPanelWidget (method)
     - has_panel_widget() -> hasPanelWidget
     - MATCH; —
   * - highLightElement (method)
     - highLightElement (method)
     - high_light_element() -> highLightElement
     - MATCH; —
   * - isATemplate (method)
     - isATemplate (method)
     - is_a_template() -> isATemplate
     - MATCH; —
   * - isDescriptionRTF (method)
     - isDescriptionRTF (method)
     - is_description_rtf() -> isDescriptionRTF
     - MATCH; —
   * - isDisplayNameRTF (method)
     - isDisplayNameRTF (method)
     - is_display_name_rtf() -> isDisplayNameRTF
     - MATCH; —
   * - isModified (method)
     - isModified (method)
     - is_modified() -> isModified
     - MATCH; —
   * - isRemote (method)
     - isRemote (method)
     - is_remote() -> isRemote
     - MATCH; —
   * - locateInBrowser (method)
     - locateInBrowser (method)
     - locate_in_browser() -> locateInBrowser
     - MATCH; —
   * - openFeaturesDialog (method)
     - openFeaturesDialog (method)
     - open_features_dialog() -> openFeaturesDialog
     - MATCH; —
   * - removeProperty (method)
     - removeProperty (method)
     - remove_property() -> removeProperty
     - MATCH; —
   * - removeRedefines (method)
     - removeRedefines (method)
     - remove_redefines() -> removeRedefines
     - MATCH; —
   * - removeStereotype (method)
     - removeStereotype (method)
     - remove_stereotype() -> removeStereotype
     - MATCH; —
   * - setDescriptionAndHyperlinks (method)
     - setDescriptionAndHyperlinks (method)
     - set_description_and_hyperlinks() -> setDescriptionAndHyperlinks
     - MATCH; —
   * - setTagContextValue (method)
     - setTagContextValue (method)
     - set_tag_context_value() -> setTagContextValue
     - MATCH; —
   * - setTagElementValue (method)
     - setTagElementValue (method)
     - set_tag_element_value() -> setTagElementValue
     - MATCH; —
   * - setTagValue (method)
     - setTagValue (method)
     - set_tag_value() -> setTagValue
     - MATCH; —
   * - synchronizeTemplateInstantiation (method)
     - synchronizeTemplateInstantiation (method)
     - synchronize_template_instantiation() -> synchronizeTemplateInstantiation
     - MATCH; —
