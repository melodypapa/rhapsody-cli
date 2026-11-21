# Rhapsody API Validation: IRPAssociationClass

## Summary
- Target wrapper: `RPAssociationClass` (`src/rhapsody_cli/models/elements/classifiers/model_association_class.py`)
- Members: Python `4`, Java `226`, pywin32 `204`
- Deviations: `0`
- Deviations by status:
  - None

- Informational binding differences (expected): `6`
- Wrapper backlog (supported members without wrappers): `195`
- Documented aliases: `0`, documented unavailable: `0`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | addEventReceptionWithEvent (method) | — | JAVA_ONLY_MEMBER | Verify the Java documentation against the installed COM type library. |
| get_end1() -> end1; get_end1() -> getEnd1 | getEnd1 (method) | end1 (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_end2() -> end2; get_end2() -> getEnd2 | getEnd2 (method) | end2 (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_class() -> getIsClass; get_is_class() -> isClass; set_is_class() -> setIsClass | getIsClass (method); setIsClass (method) | isClass (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | getRmmUrl (method) | — | JAVA_ONLY_MEMBER | Verify the Java documentation against the installed COM type library. |
| — | updateContainedDiagramsOnServer (method) | — | JAVA_ONLY_MEMBER | Verify the Java documentation against the installed COM type library. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | getActivityDiagram (method) | activityDiagram (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addActivityDiagram (method) | addActivityDiagram (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addAssociation (method) | addAssociation (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addAttribute (method) | addAttribute (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addClass (method) | addClass (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addConstructor (method) | addConstructor (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addDependency (method) | addDependency (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addDependencyBetween (method) | addDependencyBetween (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addDependencyTo (method) | addDependencyTo (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addDestructor (method) | addDestructor (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addEventReception (method) | addEventReception (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addFlowItems (method) | addFlowItems (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addFlows (method) | addFlows (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addGeneralization (method) | addGeneralization (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addLink (method) | addLink (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addLinkToElement (method) | addLinkToElement (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addLinkToPartViaPort (method) | addLinkToPartViaPort (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addNewAggr (method) | addNewAggr (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addOperation (method) | addOperation (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addProperty (method) | addProperty (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addReception (method) | addReception (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addRedefines (method) | addRedefines (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addRelation (method) | addRelation (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addRelationTo (method) | addRelationTo (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addRemoteDependencyTo (method) | addRemoteDependencyTo (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addSpecificStereotype (method) | addSpecificStereotype (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addStatechart (method) | addStatechart (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addStereotype (method) | addStereotype (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addSuperclass (method) | addSuperclass (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getAddToModelMode (method) | getAddToModelMode (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addTriggeredOperation (method) | addTriggeredOperation (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addType (method) | addType (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addUnidirectionalRelation (method) | addUnidirectionalRelation (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addUnidirectionalRelationTo (method) | addUnidirectionalRelationTo (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getAllTags (method) | allTags (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getAnnotations (method) | annotations (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getAssociationClasses (method) | associationClasses (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getAttributes (method) | attributes (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getAttributesIncludingBases (method) | getAttributesIncludingBases (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getBaseClassifiers (method) | baseClassifiers (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | becomeTemplateInstantiationOf (method) | becomeTemplateInstantiationOf (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getBehavioralDiagrams (method) | behavioralDiagrams (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getBinaryID (method) | BinaryID (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getCMHeader (method); setCMHeader (method) | CMHeader (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getCMState (method) | getCMState (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | changeTo (method) | changeTo (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | clone (method) | clone (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getConstraints (method) | constraints (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getConstraintsByHim (method) | constraintsByHim (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getControlledFiles (method) | controlledFiles (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | copyToAnotherProject (method) | copyToAnotherProject (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | createOSLCLink (method) | createOSLCLink (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getCurrentDirectory (method) | currentDirectory (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getDecorationStyle (method); setDecorationStyle (method) | getDecorationStyle (method); setDecorationStyle (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | — | deleteActivityDiagram (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | deleteAttribute (method) | deleteAttribute (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteClass (method) | deleteClass (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteConstructor (method) | deleteConstructor (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteDependency (method) | deleteDependency (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteDestructor (method) | deleteDestructor (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteEventReception (method) | deleteEventReception (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteFlowItems (method) | deleteFlowItems (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteFlows (method) | deleteFlows (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteFromProject (method) | deleteFromProject (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteGeneralization (method) | deleteGeneralization (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteOSLCLink (method) | deleteOSLCLink (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteOperation (method) | deleteOperation (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteReception (method) | deleteReception (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteRelation (method) | deleteRelation (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | — | deleteStatechart (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | deleteSuperclass (method) | deleteSuperclass (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteType (method) | deleteType (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getDependencies (method) | dependencies (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getDerivedClassifiers (method) | derivedClassifiers (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getDescription (method); setDescription (method) | description (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | setDescriptionAndHyperlinks (method) | setDescriptionAndHyperlinks (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getDescriptionHTML (method); setDescriptionHTML (method) | descriptionHTML (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getDescriptionPlainText (method) | descriptionPlainText (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getDescriptionRTF (method); setDescriptionRTF (method) | descriptionRTF (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getDisplayName (method); setDisplayName (method) | displayName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getDisplayNameRTF (method); setDisplayNameRTF (method) | getDisplayNameRTF (method); setDisplayNameRTF (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | errorMessage (method); getErrorMessage (method) | errorMessage (method); getErrorMessage (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getFilename (method); setFilename (method) | filename (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | findAttribute (method) | findAttribute (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | findBaseClassifier (method) | findBaseClassifier (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | findDerivedClassifier (method) | findDerivedClassifier (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | findElementsByFullName (method) | findElementsByFullName (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | findGeneralization (method) | findGeneralization (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | findInterfaceItem (method) | findInterfaceItem (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | findNestedClassifier (method) | findNestedClassifier (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | findNestedClassifierRecursive (method) | findNestedClassifierRecursive (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | findNestedElement (method) | findNestedElement (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | findNestedElementRecursive (method) | findNestedElementRecursive (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | findRelation (method) | findRelation (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | findTrigger (method) | findTrigger (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getFlowItems (method) | flowItems (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getFlows (method) | flows (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getFullPathName (method) | getFullPathName (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getFullPathNameIn (method) | getFullPathNameIn (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getGUID (method); setGUID (method) | GUID (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getGeneralizations (method) | generalizations (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | hasNestedElements (method) | hasNestedElements (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | hasPanelWidget (method) | hasPanelWidget (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | highLightElement (method) | highLightElement (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getHyperLinks (method) | hyperLinks (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getIconFileName (method) | getIconFileName (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getIncludeInNextLoad (method); setIncludeInNextLoad (method) | includeInNextLoad (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getInterfaceItems (method) | interfaceItems (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getInterfaceItemsIncludingBases (method) | getInterfaceItemsIncludingBases (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getInterfaceName (method) | interfaceName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | isATemplate (method) | isATemplate (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getIsAbstract (method); setIsAbstract (method) | isAbstract (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getIsActive (method); setIsActive (method) | isActive (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getIsBehaviorOverriden (method); setIsBehaviorOverriden (method) | isBehaviorOverriden (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getIsComposite (method) | isComposite (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | isDescriptionRTF (method) | isDescriptionRTF (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | isDisplayNameRTF (method) | isDisplayNameRTF (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getIsExternal (method) | isExternal (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getIsFinal (method); setIsFinal (method) | getIsFinal (method); setIsFinal (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | isModified (method) | isModified (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getIsOfMetaClass (method) | isOfMetaClass (method) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getIsReactive (method) | isReactive (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | isReadOnly (method) | isReadOnly (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | isReferenceUnit (method) | isReferenceUnit (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | isRemote (method) | isRemote (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | isSeparateSaveUnit (method) | isSeparateSaveUnit (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getIsShowDisplayName (method); setIsShowDisplayName (method) | isShowDisplayName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getIsStub (method) | isStub (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getIsUnresolved (method) | isUnresolved (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getLanguage (method); setLanguage (method) | getLanguage (method); setLanguage (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getLastModifiedTime (method) | getLastModifiedTime (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getLinks (method) | links (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | load (method) | load (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getLocalTags (method) | localTags (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | locateInBrowser (method) | locateInBrowser (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | lockOnDesignManager (method) | lockOnDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getMainDiagram (method); setMainDiagram (method) | mainDiagram (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getMetaClass (method) | metaClass (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | moveToAnotherProjectLeaveAReference (method) | moveToAnotherProjectLeaveAReference (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getName (method); setName (method) | name (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getNestedClassifiers (method) | nestedClassifiers (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getNestedElements (method) | getNestedElements (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getNestedElementsByMetaClass (method) | getNestedElementsByMetaClass (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getNestedElementsRecursive (method) | getNestedElementsRecursive (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getNestedSaveUnits (method) | getNestedSaveUnits (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getNestedSaveUnitsCount (method) | getNestedSaveUnitsCount (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getNewTermStereotype (method) | getNewTermStereotype (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getOSLCLinks (method) | getOSLCLinks (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getOfTemplate (method); setOfTemplate (method) | ofTemplate (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | openFeaturesDialog (method) | openFeaturesDialog (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getOperations (method) | operations (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getOverlayIconFileName (method) | getOverlayIconFileName (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getOverriddenProperties (method) | getOverriddenProperties (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getOverriddenPropertiesByPattern (method) | getOverriddenPropertiesByPattern (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getOwnedDependencies (method) | getOwnedDependencies (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getOwner (method); setOwner (method) | owner (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getPorts (method) | ports (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getProject (method) | project (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getPropertyValue (method); setPropertyValue (method) | getPropertyValue (method); setPropertyValue (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getPropertyValueConditional (method) | getPropertyValueConditional (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getPropertyValueConditionalExplicit (method) | getPropertyValueConditionalExplicit (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getPropertyValueExplicit (method) | getPropertyValueExplicit (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | setReadOnly (method) | setReadOnly (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getRedefines (method) | getRedefines (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | referenceToAnotherProject (method) | referenceToAnotherProject (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getReferences (method) | references (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getRelations (method) | relations (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getRelationsIncludingBases (method) | getRelationsIncludingBases (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getRemoteDependencies (method) | getRemoteDependencies (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getRemoteURI (method) | getRemoteURI (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | removeProperty (method) | removeProperty (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | removeRedefines (method) | removeRedefines (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | removeStereotype (method) | removeStereotype (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getRequirementTraceabilityHandle (method); setRequirementTraceabilityHandle (method) | requirementTraceabilityHandle (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | save (method) | save (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getSaveUnit (method) | getSaveUnit (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | setSeparateSaveUnit (method) | setSeparateSaveUnit (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getSequenceDiagrams (method) | sequenceDiagrams (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getSourceArtifacts (method) | sourceArtifacts (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getStatechart (method) | statechart (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getStereotype (method); setStereotype (method) | stereotype (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getStereotypes (method) | stereotypes (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getStructureDiagrams (method) | structureDiagrams (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | synchronizeTemplateInstantiation (method) | synchronizeTemplateInstantiation (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getTag (method) | getTag (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | setTagContextValue (method) | setTagContextValue (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | setTagElementValue (method) | setTagElementValue (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | setTagValue (method) | setTagValue (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getTemplateParameters (method) | templateParameters (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getTi (method); setTi (method) | ti (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getToolTipHTML (method) | getToolTipHTML (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getUnitPath (method); setUnitPath (method) | setUnitPath (method) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | unload (method) | unload (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | unlockOnDesignManager (method) | unlockOnDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getUserDefinedMetaClass (method) | userDefinedMetaClass (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |

## AI Fix Guidance
No deviations require changes.
