# Getter fixture matrix

Machine-readable record of one integration test per owned getter, checked by `verify_sync.py` Step 8.
Regenerate an interface section with
`python .agents/skills/rhapsody-sync/scripts/verify_sync.py <INTERFACE> --write-getter-matrix`,
then replace a `MISSING` or `WEAK` row with the test that really asserts the getter.

## IRPApplication

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `application_root` | — | none | MISSING |
| `build_no` | — | none | MISSING |
| `interface_name` | — | none | MISSING |
| `is_hidden_ui` | — | none | MISSING |
| `is_load_on_demand` | — | none | MISSING |
| `language` | — | none | MISSING |
| `log_root` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_log_root` | identity/value | OK |
| `omroot` | — | none | MISSING |
| `projects` | — | none | MISSING |
| `serial_no` | — | none | MISSING |
| `tool_set` | — | none | MISSING |
| `user_data_root` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_user_data_root` | identity/value | OK |
| `user_omroot` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_user_omroot` | identity/value | OK |

## IRPArgument

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `argument_direction` | — | none | MISSING |

## IRPAssociationClass

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `end1` | — | none | MISSING |
| `end2` | — | none | MISSING |
| `is_class` | — | none | MISSING |

## IRPAttribute

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `is_constant` | — | none | MISSING |
| `is_ordered` | — | none | MISSING |
| `is_reference` | — | none | MISSING |
| `is_static` | — | none | MISSING |
| `multiplicity` | — | none | MISSING |
| `visibility` | — | none | MISSING |

## IRPClass

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `is_abstract` | — | none | MISSING |
| `is_active` | — | none | MISSING |
| `is_behavior_overriden` | — | none | MISSING |
| `is_composite` | — | none | MISSING |
| `is_reactive` | — | none | MISSING |

## IRPClassifier

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `activity_diagram` | — | none | MISSING |
| `attributes` | — | none | MISSING |
| `base_classifiers` | — | none | MISSING |
| `behavioral_diagrams` | — | none | MISSING |
| `derived_classifiers` | — | none | MISSING |
| `flow_items` | — | none | MISSING |
| `flows` | — | none | MISSING |
| `generalizations` | — | none | MISSING |
| `interface_items` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_get_interface_items` | identity/value | OK |
| `links` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_get_links_empty` | weak | WEAK |
| `nested_classifiers` | — | none | MISSING |
| `operations` | — | none | MISSING |
| `ports` | — | none | MISSING |
| `relations` | — | none | MISSING |
| `sequence_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_get_sequence_diagrams_empty` | weak | WEAK |
| `source_artifacts` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_get_source_artifacts_empty` | weak | WEAK |
| `statechart` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_get_statechart` | identity/value | OK |

## IRPCollection

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `count` | — | none | MISSING |

## IRPInterfaceItem

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `arguments` | — | none | MISSING |
| `signature` | — | none | MISSING |

## IRPModelElement

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `all_tags` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_all_tags` | identity/value | OK |
| `annotations` | — | none | MISSING |
| `association_classes` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_association_classes` | identity/value | OK |
| `binary_id` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_binary_id` | identity/value | OK |
| `constraints` | — | none | MISSING |
| `constraints_by_him` | — | none | MISSING |
| `controlled_files` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_controlled_files_empty` | identity/value | OK |
| `dependencies` | — | none | MISSING |
| `description` | — | none | MISSING |
| `description_html` | — | none | MISSING |
| `description_plain_text` | — | none | MISSING |
| `description_rtf` | — | none | MISSING |
| `display_name` | — | none | MISSING |
| `guid` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_guid` | identity/value | OK |
| `hyper_links` | — | none | MISSING |
| `interface_name` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_interface_name` | identity/value | OK |
| `is_external` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_is_external` | identity/value | OK |
| `is_show_display_name` | — | none | MISSING |
| `is_unresolved` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_is_unresolved` | identity/value | OK |
| `local_tags` | — | none | MISSING |
| `main_diagram` | — | none | MISSING |
| `meta_class` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_meta_class` | identity/value | OK |
| `name` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_name` | identity/value | OK |
| `of_template` | — | none | MISSING |
| `owner` | — | none | MISSING |
| `project` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_project` | identity/value | OK |
| `references` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_references` | identity/value | OK |
| `requirement_traceability_handle` | — | none | MISSING |
| `stereotype` | — | none | MISSING |
| `stereotypes` | — | none | MISSING |
| `template_parameters` | — | none | MISSING |
| `ti` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_ti` | identity/value | OK |
| `user_defined_meta_class` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_user_defined_meta_class` | weak | WEAK |

## IRPOperation

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `body` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_body` | identity/value | OK |
| `flowchart` | — | none | MISSING |
| `initializer` | — | none | MISSING |
| `is_abstract` | — | none | MISSING |
| `is_cg_derived` | — | none | MISSING |
| `is_const` | — | none | MISSING |
| `is_ctor` | — | none | MISSING |
| `is_dtor` | — | none | MISSING |
| `is_final` | — | none | MISSING |
| `is_inline` | — | none | MISSING |
| `is_static` | — | none | MISSING |
| `is_trigger` | — | none | MISSING |
| `is_virtual` | — | none | MISSING |
| `returns` | — | none | MISSING |
| `visibility` | — | none | MISSING |

## IRPPackage

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `actors` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_actors` | identity/value | OK |
| `behavioral_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_behavioral_diagrams` | identity/value | OK |
| `classes` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_classes` | identity/value | OK |
| `collaboration_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_collaboration_diagrams` | identity/value | OK |
| `component_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_component_diagrams` | identity/value | OK |
| `deployment_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_deployment_diagrams` | identity/value | OK |
| `events` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_events` | identity/value | OK |
| `events_base_id` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_events_base_id` | identity/value | OK |
| `flow_items` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_flow_items` | identity/value | OK |
| `flows` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_flows` | identity/value | OK |
| `global_functions` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_global_functions` | identity/value | OK |
| `global_objects` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_global_objects` | identity/value | OK |
| `global_variables` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_global_variables` | identity/value | OK |
| `instance_specifications` | — | none | MISSING |
| `links` | — | none | MISSING |
| `modules` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_modules` | identity/value | OK |
| `nested_classifiers` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_nested_classifiers` | identity/value | OK |
| `nested_components` | — | none | MISSING |
| `nodes` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_nodes` | identity/value | OK |
| `object_model_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_object_model_diagrams` | identity/value | OK |
| `packages` | — | none | MISSING |
| `panel_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_panel_diagrams` | identity/value | OK |
| `saved_in_seperate_directory` | — | none | MISSING |
| `sequence_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_sequence_diagrams` | identity/value | OK |
| `source_artifacts` | — | none | MISSING |
| `timing_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_timing_diagrams` | identity/value | OK |
| `types` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_types` | identity/value | OK |
| `use_case_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_use_case_diagrams` | identity/value | OK |
| `use_cases` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_use_cases` | identity/value | OK |
| `user_defined_stereotypes` | — | none | MISSING |

## IRPPort

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `is_behavioral` | — | none | MISSING |
| `is_reversed` | — | none | MISSING |
| `port_contract` | — | none | MISSING |
| `provided_interfaces` | — | none | MISSING |
| `required_interfaces` | — | none | MISSING |

## IRPProject

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `active_component` | — | none | MISSING |
| `active_configuration` | — | none | MISSING |
| `all_stereotypes` | — | none | MISSING |
| `cg_simplified_model_package` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_project.py::test_cg_simplified_model_package` | identity/value | OK |
| `components` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_project.py::test_components` | identity/value | OK |
| `default_directory_scheme` | — | none | MISSING |
| `nodes` | — | none | MISSING |
| `packages` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_project.py::test_packages` | identity/value | OK |
| `profiles` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_project.py::test_profiles` | identity/value | OK |
| `use_unique_stereotype_and_ref_cache` | — | none | MISSING |

## IRPType

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `declaration` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_type.py::test_get_declaration` | identity/value | OK |
| `enumeration_literals` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_type.py::test_get_enumeration_literals` | identity/value | OK |
| `is_predefined` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_type.py::test_get_is_predefined` | identity/value | OK |
| `is_typedef` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_type.py::test_get_is_typedef` | identity/value | OK |
| `is_typedef_constant` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_type.py::test_get_is_typedef_constant` | identity/value | OK |
| `is_typedef_ordered` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_type.py::test_get_is_typedef_ordered` | identity/value | OK |
| `is_typedef_reference` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_type.py::test_get_is_typedef_reference` | identity/value | OK |
| `kind` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_type.py::test_get_kind` | identity/value | OK |
| `typedef_base_type` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_type.py::test_get_typedef_base_type` | identity/value | OK |
| `typedef_multiplicity` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_type.py::test_get_typedef_multiplicity` | identity/value | OK |

## IRPUnit

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `cm_header` | — | none | MISSING |
| `current_directory` | — | none | MISSING |
| `filename` | — | none | MISSING |
| `include_in_next_load` | — | none | MISSING |
| `is_stub` | — | none | MISSING |
| `structure_diagrams` | — | none | MISSING |

## IRPUseCase

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `describing_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_use_case.py::test_describing_diagrams` | identity/value | OK |
| `entry_points` | — | none | MISSING |
| `extension_points` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_use_case.py::test_extension_points` | identity/value | OK |
| `is_behavior_overriden` | — | none | MISSING |
