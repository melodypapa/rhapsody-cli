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
Python-implementation column below already reflects the post-migration single-member labels.

.. list-table:: Verified IRPModelElement deviations and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - ---
     - ---
     - ---
     - ---; ---
   * - getDescriptionHTML (method); setDescriptionHTML (method)
     - descriptionHTML (property)
     - get_description_html() -> descriptionHTML
     - PYTHON_METHOD_NAME_MISMATCH; Rename the Python method to the snake_case Java API name or document the alias.
   * - getRmmUrl (method)
     - —
     - get_rmm_url() -> getRmmUrl; get_rmm_url() -> rmmUrl
     - PYWIN32_MEMBER_MISSING; Use a member exposed by the registered type library or verify the Rhapsody version.
   * - ---
     - ---
     - ---
     - ---; ---
   * - —
     - —
     - is_a_template() -> isATemplate
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - getAllTags (method)
     - allTags (property)
     - get_all_tags() -> allTags
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getAnnotations (method)
     - annotations (property)
     - get_annotations() -> annotations
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getAssociationClasses (method)
     - associationClasses (property)
     - get_association_classes() -> associationClasses
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getBinaryID (method)
     - BinaryID (property)
     - get_binary_id() -> BinaryID
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getConstraints (method)
     - constraints (property)
     - get_constraints() -> constraints
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getConstraintsByHim (method)
     - constraintsByHim (property)
     - get_constraints_by_him() -> constraintsByHim
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getControlledFiles (method)
     - controlledFiles (property)
     - get_controlled_files() -> controlledFiles
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getDependencies (method)
     - dependencies (property)
     - get_dependencies() -> dependencies
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getDescription (method); setDescription (method)
     - description (property)
     - get_description() -> description; set_description() -> description
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getDescriptionPlainText (method)
     - descriptionPlainText (property)
     - get_description_plain_text() -> descriptionPlainText
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getDescriptionRTF (method); setDescriptionRTF (method)
     - descriptionRTF (property)
     - get_description_rtf() -> descriptionRTF; is_description_rtf() -> isDescriptionRTF; set_description_rtf() -> descriptionRTF
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getDisplayName (method); setDisplayName (method)
     - displayName (property)
     - get_display_name() -> displayName; set_display_name() -> displayName
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getGUID (method); setGUID (method)
     - GUID (property)
     - get_guid() -> GUID; set_guid() -> GUID
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getHyperLinks (method)
     - hyperLinks (property)
     - get_hyper_links() -> hyperLinks
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getInterfaceName (method)
     - interfaceName (property)
     - get_interface_name() -> interfaceName
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getIsExternal (method)
     - isExternal (property)
     - get_is_external() -> isExternal
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getIsOfMetaClass (method)
     - isOfMetaClass (method)
     - get_is_of_meta_class() -> isOfMetaClass
     - ACCESSOR_ALIAS_MISMATCH; Review the related API spellings and document the intended mapping.
   * - getIsShowDisplayName (method); setIsShowDisplayName (method)
     - isShowDisplayName (property)
     - get_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> isShowDisplayName
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getIsUnresolved (method)
     - isUnresolved (property)
     - get_is_unresolved() -> isUnresolved
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getLocalTags (method)
     - localTags (property)
     - get_local_tags() -> localTags
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getMainDiagram (method); setMainDiagram (method)
     - mainDiagram (property)
     - get_main_diagram() -> mainDiagram; set_main_diagram() -> mainDiagram
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getMetaClass (method)
     - metaClass (property)
     - get_meta_class() -> metaClass
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - —
     - —
     - is_modified() -> isModified
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - getName (method); setName (method)
     - name (property)
     - get_name() -> name; set_name() -> name
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getOfTemplate (method); setOfTemplate (method)
     - ofTemplate (property)
     - get_of_template() -> ofTemplate; set_of_template() -> ofTemplate
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getOwner (method); setOwner (method)
     - owner (property)
     - get_owner() -> owner; set_owner() -> owner
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getProject (method)
     - project (property)
     - get_project() -> project
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - —
     - —
     - create_oslc_link() (no static COM member)
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - —
     - —
     - delete_oslc_link() (no static COM member)
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - —
     - —
     - get_oslc_links() (no static COM member)
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - —
     - —
     - set_description_html() (no static COM member)
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - getReferences (method)
     - references (property)
     - get_references() -> references
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - —
     - —
     - is_remote() -> isRemote
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - getRequirementTraceabilityHandle (method); setRequirementTraceabilityHandle (method)
     - requirementTraceabilityHandle (property)
     - get_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> requirementTraceabilityHandle
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getStereotypes (method)
     - stereotypes (property)
     - get_stereotypes() -> stereotypes
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getTemplateParameters (method)
     - templateParameters (property)
     - get_template_parameters() -> templateParameters
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getTi (method); setTi (method)
     - ti (property)
     - get_ti() -> ti; set_ti() -> ti
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getUserDefinedMetaClass (method)
     - userDefinedMetaClass (property)
     - get_user_defined_meta_class() -> userDefinedMetaClass
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - ---
     - ---
     - ---
     - ---; ---
   * - createOSLCLink (method)
     - createOSLCLink (method)
     - —
     - MISSING_PYTHON_WRAPPER; Implement the Python wrapper or mark this API member intentionally unsupported.
   * - deleteOSLCLink (method)
     - deleteOSLCLink (method)
     - —
     - MISSING_PYTHON_WRAPPER; Implement the Python wrapper or mark this API member intentionally unsupported.
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
