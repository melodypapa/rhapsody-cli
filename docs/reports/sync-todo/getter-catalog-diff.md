# Getter implementation vs pywin32 catalog

Per-owned-getter comparison of the Python binding against `docs/reports/pywin32_authority.json`.
Regenerate one interface section with
`python .agents/skills/rhapsody-sync/scripts/verify_sync.py <INTERFACE> --write-getter-diff`.

Statuses: `match` — the bound COM member exists with the catalog's shape; `catalog-missing` — the bound member is absent
from the catalog; `shape-mismatch` — the binding form differs from the catalog shape; `no-binding` — the property is pure
Python; `stub` — the property raises `NotImplementedError` (see the stub evidence ledger); `catalog-only` — a catalog
property has no Python property with the derived snake_case name anywhere in the wrapper MRO, a candidate gap for human
review rather than a failure.

## Summary

| Status | Count |
| --- | --- |
| match | 204 |
| catalog-missing | 0 |
| shape-mismatch | 0 |
| no-binding | 0 |
| stub | 2 |
| catalog-only | 1 |

## IRPApplication

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `projects` | `projects` | property | property | match |
| `is_hidden_ui` | `isHiddenUI` | property | property | match |
| `build_no` | `BuildNo` | property | property | match |
| `omroot` | `OMROOT` | property | property | match |
| `application_root` | `ApplicationRoot` | property | property | match |
| `interface_name` | `interfaceName` | property | property | match |
| `is_load_on_demand` | `isLoadOnDemand` | property | property | match |
| `language` | `Language` | property | property | match |
| `log_root` | `LogRoot` | property | property | match |
| `serial_no` | `SerialNo` | property | property | match |
| `tool_set` | `ToolSet` | property | property | match |
| `user_data_root` | `UserDataRoot` | property | property | match |
| `user_omroot` | `UserOMROOT` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPArgument

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `argument_direction` | `argumentDirection` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPAssociationClass

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `end1` | `end1` | property | property | match |
| `end2` | `end2` | property | property | match |
| `is_class` | `isClass` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPAttribute

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `is_constant` | `isConstant` | property | property | match |
| `is_ordered` | `isOrdered` | property | property | match |
| `is_reference` | `isReference` | property | property | match |
| `is_static` | `isStatic` | property | property | match |
| `multiplicity` | `multiplicity` | property | property | match |
| `visibility` | `visibility` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPClass

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `is_abstract` | `isAbstract` | property | property | match |
| `is_active` | `isActive` | property | property | match |
| `is_behavior_overriden` | `isBehaviorOverriden` | property | property | match |
| `is_composite` | `isComposite` | property | property | match |
| `is_reactive` | `isReactive` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPClassifier

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `attributes` | `attributes` | property | property | match |
| `operations` | `operations` | property | property | match |
| `activity_diagram` | `activityDiagram` | property | property | match |
| `base_classifiers` | `baseClassifiers` | property | property | match |
| `behavioral_diagrams` | `behavioralDiagrams` | property | property | match |
| `derived_classifiers` | `derivedClassifiers` | property | property | match |
| `flow_items` | `flowItems` | property | property | match |
| `flows` | `flows` | property | property | match |
| `generalizations` | `generalizations` | property | property | match |
| `interface_items` | `interfaceItems` | property | property | match |
| `links` | `links` | property | property | match |
| `nested_classifiers` | `nestedClassifiers` | property | property | match |
| `ports` | `ports` | property | property | match |
| `relations` | `relations` | property | property | match |
| `sequence_diagrams` | `sequenceDiagrams` | property | property | match |
| `source_artifacts` | `sourceArtifacts` | property | property | match |
| `statechart` | `statechart` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPCollection

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `count` | `Count` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPInterfaceItem

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `arguments` | `arguments` | property | property | match |
| `signature` | `signature` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPModelElement

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `name` | `name` | property | property | match |
| `meta_class` | `metaClass` | property | property | match |
| `guid` | `GUID` | property | property | match |
| `all_tags` | `allTags` | property | property | match |
| `annotations` | `annotations` | property | property | match |
| `association_classes` | `associationClasses` | property | property | match |
| `binary_id` | `BinaryID` | property | property | match |
| `constraints` | `constraints` | property | property | match |
| `constraints_by_him` | — | — | — | stub |
| `controlled_files` | `controlledFiles` | property | property | match |
| `dependencies` | `dependencies` | property | property | match |
| `description` | `description` | property | property | match |
| `description_html` | `descriptionHTML` | property | property | match |
| `description_plain_text` | `descriptionPlainText` | property | property | match |
| `description_rtf` | `descriptionRTF` | property | property | match |
| `display_name` | `displayName` | property | property | match |
| `hyper_links` | — | — | — | stub |
| `interface_name` | `interfaceName` | property | property | match |
| `is_external` | `isExternal` | property | property | match |
| `is_show_display_name` | `isShowDisplayName` | property | property | match |
| `is_unresolved` | `isUnresolved` | property | property | match |
| `local_tags` | `localTags` | property | property | match |
| `main_diagram` | `mainDiagram` | property | property | match |
| `of_template` | `ofTemplate` | property | property | match |
| `owner` | `owner` | property | property | match |
| `project` | `project` | property | property | match |
| `references` | `references` | property | property | match |
| `requirement_traceability_handle` | `requirementTraceabilityHandle` | property | property | match |
| `stereotype` | `stereotype` | property | property | match |
| `stereotypes` | `stereotypes` | property | property | match |
| `template_parameters` | `templateParameters` | property | property | match |
| `ti` | `ti` | property | property | match |
| `user_defined_meta_class` | `userDefinedMetaClass` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPOperation

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `body` | `body` | property | property | match |
| `is_abstract` | `isAbstract` | property | property | match |
| `is_static` | `isStatic` | property | property | match |
| `is_virtual` | `isVirtual` | property | property | match |
| `returns` | `returns` | property | property | match |
| `flowchart` | `flowchart` | property | property | match |
| `initializer` | `initializer` | property | property | match |
| `is_cg_derived` | `isCgDerived` | property | property | match |
| `is_const` | `isConst` | property | property | match |
| `is_ctor` | `isCtor` | property | property | match |
| `is_dtor` | `isDtor` | property | property | match |
| `is_final` | `isFinal` | property | property | match |
| `is_inline` | `isInline` | property | property | match |
| `is_trigger` | `isTrigger` | property | property | match |
| `visibility` | `visibility` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPPackage

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `packages` | `packages` | property | property | match |
| `classes` | `classes` | property | property | match |
| `actors` | `actors` | property | property | match |
| `use_cases` | `useCases` | property | property | match |
| `sequence_diagrams` | `sequenceDiagrams` | property | property | match |
| `use_case_diagrams` | `useCaseDiagrams` | property | property | match |
| `collaboration_diagrams` | `collaborationDiagrams` | property | property | match |
| `component_diagrams` | `componentDiagrams` | property | property | match |
| `deployment_diagrams` | `deploymentDiagrams` | property | property | match |
| `object_model_diagrams` | `objectModelDiagrams` | property | property | match |
| `timing_diagrams` | `timingDiagrams` | property | property | match |
| `panel_diagrams` | `panelDiagrams` | property | property | match |
| `events` | `events` | property | property | match |
| `flow_items` | `flowItems` | property | property | match |
| `flows` | `flows` | property | property | match |
| `nodes` | `nodes` | property | property | match |
| `modules` | `modules` | property | property | match |
| `types` | `types` | property | property | match |
| `global_functions` | `globalFunctions` | property | property | match |
| `global_objects` | `globalObjects` | property | property | match |
| `global_variables` | `globalVariables` | property | property | match |
| `nested_classifiers` | `nestedClassifiers` | property | property | match |
| `nested_components` | `nestedComponents` | property | property | match |
| `instance_specifications` | `instanceSpecifications` | property | property | match |
| `links` | `links` | property | property | match |
| `behavioral_diagrams` | `behavioralDiagrams` | property | property | match |
| `source_artifacts` | `sourceArtifacts` | property | property | match |
| `events_base_id` | `eventsBaseId` | property | property | match |
| `saved_in_seperate_directory` | `savedInSeperateDirectory` | property | property | match |
| `user_defined_stereotypes` | `userDefinedStereotypes` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPPort

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `is_behavioral` | `isBehavioral` | property | property | match |
| `is_reversed` | `isReversed` | property | property | match |
| `port_contract` | `portContract` | property | property | match |
| `provided_interfaces` | `providedInterfaces` | property | property | match |
| `required_interfaces` | `requiredInterfaces` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPProject

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `components` | `components` | property | property | match |
| `active_configuration` | `activeConfiguration` | property | property | match |
| `active_component` | `activeComponent` | property | property | match |
| `all_stereotypes` | `allStereotypes` | property | property | match |
| `profiles` | `profiles` | property | property | match |
| `cg_simplified_model_package` | `cgSimplifiedModelPackage` | property | property | match |
| `default_directory_scheme` | `defaultDirectoryScheme` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| `UseUniqueStereotypeAndRefCache` | `use_unique_stereotype_and_ref_cache` | catalog-only |

## IRPType

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `declaration` | `declaration` | property | property | match |
| `enumeration_literals` | `enumerationLiterals` | property | property | match |
| `is_predefined` | `isPredefined` | property | property | match |
| `is_typedef` | `isTypedef` | property | property | match |
| `is_typedef_constant` | `isTypedefConstant` | property | property | match |
| `is_typedef_ordered` | `isTypedefOrdered` | property | property | match |
| `is_typedef_reference` | `isTypedefReference` | property | property | match |
| `kind` | `kind` | property | property | match |
| `typedef_base_type` | `typedefBaseType` | property | property | match |
| `typedef_multiplicity` | `typedefMultiplicity` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPUnit

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `cm_header` | `CMHeader` | property | property | match |
| `current_directory` | `currentDirectory` | property | property | match |
| `filename` | `filename` | property | property | match |
| `include_in_next_load` | `includeInNextLoad` | property | property | match |
| `is_stub` | `isStub` | property | property | match |
| `structure_diagrams` | `structureDiagrams` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPUseCase

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `extension_points` | `extensionPoints` | property | property | match |
| `entry_points` | `entryPoints` | property | property | match |
| `describing_diagrams` | `describingDiagrams` | property | property | match |
| `is_behavior_overriden` | `isBehaviorOverriden` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPFlow

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `conveyed` | `conveyed` | property | property | match |
| `direction` | `direction` | property | property | match |
| `end1` | `end1` | property | property | match |
| `end1_port` | `end1Port` | property | property | match |
| `end1_sys_ml_port` | `end1SysMLPort` | property | property | match |
| `end2` | `end2` | property | property | match |
| `end2_port` | `end2Port` | property | property | match |
| `end2_sys_ml_port` | `end2SysMLPort` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPFlowchart

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `is_analysis_only` | `isAnalysisOnly` | property | property | match |
| `its_owner` | `itsOwner` | property | property | match |
| `swimlanes` | `swimlanes` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPSwimlane

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `contents` | `contents` | property | property | match |
| `represents` | `represents` | property | property | match |
| `swimlanes` | `swimlanes` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPAction

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `body` | `body` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPSendAction

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `arg_vals` | `argVals` | property | property | match |
| `event` | `event` | property | property | match |
| `invoked_operation` | `invokedOperation` | property | property | match |
| `target` | `target` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPFlowItem

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `represented` | `represented` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPObjectNode

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `in_state` | `inState` | property | property | match |
| `in_state_list` | `inStateList` | property | property | match |
| `represents` | `represents` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPCallOperation

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `operation` | `operation` | property | property | match |
| `target` | `target` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPContextSpecification

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `multiplicities` | `multiplicities` | property | property | match |
| `value` | `value` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPAcceptTimeEvent

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `duration_time` | `durationTime` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPStatechart

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `graphical_elements` | `graphicalElements` | property | property | match |
| `is_main_behavior` | `isMainBehavior` | property | property | match |
| `is_overridden` | `isOverridden` | property | property | match |
| `its_class` | `itsClass` | property | property | match |
| `root_state` | `rootState` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPStereotype

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `icon` | `icon` | property | property | match |
| `is_new_term` | `isNewTerm` | property | property | match |
| `of_meta_class` | `ofMetaClass` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |

## IRPComponent

| Python getter | COM member | Binding shape | Catalog shape | Status |
| --- | --- | --- | --- | --- |
| `additional_sources` | `additionalSources` | property | property | match |
| `build_type` | `buildType` | property | property | match |
| `configurations` | `configurations` | property | property | match |
| `files` | `files` | property | property | match |
| `include_path` | `includePath` | property | property | match |
| `libraries` | `libraries` | property | property | match |
| `nested_components` | `nestedComponents` | property | property | match |
| `panel_diagrams` | `panelDiagrams` | property | property | match |
| `scope_by_selected_elements` | `scopeBySelectedElements` | property | property | match |
| `scope_elements` | `scopeElements` | property | property | match |
| `standard_headers` | `standardHeaders` | property | property | match |
| `variation_points` | `variationPoints` | property | property | match |

### Catalog properties with no matching Python property

| Catalog property | Derived Python name | Status |
| --- | --- | --- |
| — | — | — |
