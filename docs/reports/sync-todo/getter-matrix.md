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
| `activity_diagram` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_add_activity_diagram_and_get_behavioral_diagrams` | identity/value | OK |
| `attributes` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_find_attribute_and_delete_attribute` | identity/value | OK |
| `base_classifiers` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_generalization_hierarchy` | identity/value | OK |
| `behavioral_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_add_activity_diagram_and_get_behavioral_diagrams` | identity/value | OK |
| `derived_classifiers` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_generalization_hierarchy` | identity/value | OK |
| `flow_items` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_add_flow_items_and_delete` | identity/value | OK |
| `flows` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_add_flows_and_delete` | identity/value | OK |
| `generalizations` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_generalization_hierarchy` | identity/value | OK |
| `interface_items` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_get_interface_items` | identity/value | OK |
| `links` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_get_links_empty` | weak | WEAK |
| `nested_classifiers` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_nested_classifiers_and_find` | identity/value | OK |
| `operations` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_delete_operation` | identity/value | OK |
| `ports` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_add_port_and_get_ports` | identity/value | OK |
| `relations` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_get_relations_including_bases` | identity/value | OK |
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
| `annotations` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_annotations_returns_annotation_created_on_element` | identity/value | OK |
| `association_classes` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_association_classes` | identity/value | OK |
| `binary_id` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_binary_id` | identity/value | OK |
| `constraints` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_constraints_returns_constraint_created_on_element` | identity/value | OK |
| `constraints_by_him` | — | none | MISSING |
| `controlled_files` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_controlled_files_empty` | identity/value | OK |
| `dependencies` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_add_dependency_to_and_get_dependencies` | identity/value | OK |
| `description` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_set_and_get_description_roundtrip` | identity/value | OK |
| `description_html` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_set_and_get_description_html` | identity/value | OK |
| `description_plain_text` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_set_and_get_description_roundtrip` | identity/value | OK |
| `description_rtf` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_set_and_get_description_rtf_roundtrip` | identity/value | OK |
| `display_name` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_set_and_get_display_name_roundtrip` | identity/value | OK |
| `guid` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_guid` | identity/value | OK |
| `hyper_links` | — | none | MISSING |
| `interface_name` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_interface_name` | identity/value | OK |
| `is_external` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_is_external` | identity/value | OK |
| `is_show_display_name` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_is_show_display_name_roundtrip` | identity/value | OK |
| `is_unresolved` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_is_unresolved` | identity/value | OK |
| `local_tags` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_local_tags_returns_tag_created_on_element` | identity/value | OK |
| `main_diagram` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_main_diagram_and_set_main_diagram_roundtrip` | identity/value | OK |
| `meta_class` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_meta_class` | identity/value | OK |
| `name` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_name` | identity/value | OK |
| `of_template` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_become_template_instantiation_of` | identity/value | OK |
| `owner` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_set_owner` | identity/value | OK |
| `project` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_project` | identity/value | OK |
| `references` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_references` | identity/value | OK |
| `requirement_traceability_handle` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_set_and_get_requirement_traceability_handle_roundtrip` | identity/value | OK |
| `stereotype` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_stereotype_property_reads_and_writes_applied_stereotype` | identity/value | OK |
| `stereotypes` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_add_stereotype_and_get_stereotypes` | identity/value | OK |
| `template_parameters` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_become_template_instantiation_of` | identity/value | OK |
| `ti` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_ti` | identity/value | OK |
| `user_defined_meta_class` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_model_element.py::test_get_user_defined_meta_class` | weak | WEAK |

## IRPOperation

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `body` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_body` | identity/value | OK |
| `flowchart` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_flowchart_getters` | identity/value | OK |
| `initializer` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_property_getters` | identity/value | OK |
| `is_abstract` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_abstract_roundtrip` | identity/value | OK |
| `is_cg_derived` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_integer_flags` | identity/value | OK |
| `is_const` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_integer_flags` | identity/value | OK |
| `is_ctor` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_integer_flags` | identity/value | OK |
| `is_dtor` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_integer_flags` | identity/value | OK |
| `is_final` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_integer_flags` | identity/value | OK |
| `is_inline` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_integer_flags` | identity/value | OK |
| `is_static` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_static_roundtrip` | identity/value | OK |
| `is_trigger` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_integer_flags` | identity/value | OK |
| `is_virtual` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_virtual_roundtrip` | identity/value | OK |
| `returns` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_returns_roundtrip` | identity/value | OK |
| `visibility` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_property_setters_round_trip` | identity/value | OK |

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
