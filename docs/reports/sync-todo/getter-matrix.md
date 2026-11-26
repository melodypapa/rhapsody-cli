# Getter fixture matrix

Machine-readable record of one integration test per owned getter, checked by `verify_sync.py` Step 8.
Regenerate an interface section with
`python .agents/skills/rhapsody-sync/scripts/verify_sync.py <INTERFACE> --write-getter-matrix`,
then replace a `MISSING` or `WEAK` row with the test that really asserts the getter.

## IRPApplication

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `application_root` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_application_root_is_the_install_directory` | identity/value | OK |
| `build_no` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_build_number_is_numeric` | identity/value | OK |
| `interface_name` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_interface_name_is_irp_application` | identity/value | OK |
| `is_hidden_ui` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_hidden_ui_roundtrip_uses_real_state` | identity/value | OK |
| `is_load_on_demand` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_environment_language_toolset_and_load_on_demand` | identity/value | OK |
| `language` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_environment_language_toolset_and_load_on_demand` | identity/value | OK |
| `log_root` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_log_root` | identity/value | OK |
| `omroot` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_omroot_is_share_directory_under_application_root` | identity/value | OK |
| `projects` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_projects_collection_contains_the_test_project` | identity/value | OK |
| `serial_no` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_serial_number_is_non_empty` | identity/value | OK |
| `tool_set` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_environment_language_toolset_and_load_on_demand` | identity/value | OK |
| `user_data_root` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_user_data_root` | identity/value | OK |
| `user_omroot` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_application.py::test_user_omroot` | identity/value | OK |

## IRPArgument

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `argument_direction` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_argument.py::test_argument_direction_is_readable` | identity/value | OK |

## IRPAssociationClass

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `end1` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_association_class.py::test_owned_properties_via_wrapped_com_object` | identity/value | OK |
| `end2` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_association_class.py::test_owned_properties_via_wrapped_com_object` | identity/value | OK |
| `is_class` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_association_class.py::test_owned_properties_via_wrapped_com_object` | identity/value | OK |

## IRPAttribute

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `is_constant` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_attribute.py::test_is_constant_roundtrip` | identity/value | OK |
| `is_ordered` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_attribute.py::test_is_ordered_roundtrip` | identity/value | OK |
| `is_reference` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_attribute.py::test_is_reference_roundtrip` | identity/value | OK |
| `is_static` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_attribute.py::test_is_static_roundtrip` | identity/value | OK |
| `multiplicity` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_attribute.py::test_multiplicity_roundtrip` | identity/value | OK |
| `visibility` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_attribute.py::test_visibility_roundtrip` | identity/value | OK |

## IRPClass

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `is_abstract` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_operation.py::test_abstract_roundtrip` | identity/value | OK |
| `is_active` | — | none | MISSING |
| `is_behavior_overriden` | — | none | MISSING |
| `is_composite` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_class.py::test_is_composite_readonly` | identity/value | OK |
| `is_reactive` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_class.py::test_is_reactive_readonly` | identity/value | OK |

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
| `links` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_links` | identity/value | OK |
| `nested_classifiers` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_nested_classifiers_and_find` | identity/value | OK |
| `operations` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_delete_operation` | identity/value | OK |
| `ports` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_get_ports_returns_port_created_with_generic_factory` | identity/value | OK |
| `relations` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_get_relations_including_bases` | identity/value | OK |
| `sequence_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_sequence_diagrams` | identity/value | OK |
| `source_artifacts` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_source_artifacts` | identity/value | OK |
| `statechart` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier.py::test_get_statechart` | identity/value | OK |

## IRPCollection

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `count` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_collection.py::test_collection_mutators_and_accessors` | identity/value | OK |

## IRPInterfaceItem

| Java getter / Python member | Integration test | Assertion | Status | Real parent and created child/value | JavaDoc-verified setup and relationship | Expected returned identity/value | Cleanup |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `arguments` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_interface_item.py::test_add_argument_and_get_arguments` | identity/value | OK | Test package → class → operation; created `IRPArgument` | `IRPInterfaceItem.addArgument(name)` creates and attaches the argument to the operation's argument list. | `operation.arguments` contains the exact argument returned by `add_argument`. | Delete the test package. |
| `signature` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_interface_item.py::test_signature_methods` | identity/value | OK | Test package → class → operation with a created argument | `addArgument(name)` attaches a real argument; JavaDoc defines `getSignature()` as the operation signature. | Exact live value: `<operation>(int <argument>)`, including the created operation and argument names. | Delete the test package. |

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
| `user_defined_meta_class` | — | none | MISSING |

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
| `instance_specifications` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_instance_specifications_returns_created_instance_specification` | identity/value | OK | Fresh test package → created instance specification | Use documented `IRPModelElement.addNewAggr("InstanceSpecification", name)`; the meta-class is registered for `IRPInstanceSpecification` and the live call succeeds. | `package.instance_specifications` contains that created instance specification. | Delete the test package. |
| `links` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_links_returns_link_created_with_add_link` | identity/value | OK | Fresh test package → two classes, two package-owned objects, and a created link | Create classes with `addClass`, objects with documented `addGlobalObject`, and an association relation with `addRelationTo`; wrap the real object COM references as `IRPInstance`, then call `addLink(fromPart, toPart, assoc, null, null)` because the documented association form requires null ports. | `package.links` contains the exact `IRPLink` returned by `add_link`. | Delete the test package.
| `modules` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_modules` | identity/value | OK |
| `nested_classifiers` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_nested_classifiers` | identity/value | OK |
| `nested_components` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_nested_components_returns_component_created_with_generic_factory` | identity/value | OK | Fresh test package → created component | Use documented `IRPModelElement.addNewAggr("Component", name)`; `Component` is the registered meta-class and live creation succeeds. | `package.nested_components` contains that exact component. | Delete the test package. |
| `nodes` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_nodes` | identity/value | OK |
| `object_model_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_object_model_diagrams` | identity/value | OK |
| `packages` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_nested_packages` | identity/value | OK | Fresh test package → created nested package | `IRPPackage.addNestedPackage(name)` creates and attaches a package. | `package.packages` contains that exact nested package. | Delete the test package. |
| `panel_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_panel_diagrams` | identity/value | OK |
| `saved_in_seperate_directory` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_set_saved_in_separate_directory` | identity/value | OK | Fresh test package → explicitly set scalar flag | Set the writable `savedInSeperateDirectory` COM property to `0`, then read through the package getter. | Returned value is exactly `0`. | Delete the test package. |
| `sequence_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_sequence_diagrams` | identity/value | OK |
| `source_artifacts` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_source_artifacts_returns_file_created_with_generic_factory` | identity/value | OK | Fresh test package → created file/source artifact | Use documented `IRPModelElement.addNewAggr("File", name)`; the live package creates the child successfully. | `package.source_artifacts` contains that created file. | Delete the test package. |
| `timing_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_timing_diagrams` | identity/value | OK |
| `types` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_types` | identity/value | OK |
| `use_case_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_use_case_diagrams` | identity/value | OK |
| `use_cases` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_use_cases` | identity/value | OK |
| `user_defined_stereotypes` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_package.py::test_get_user_defined_stereotypes_returns_stereotype_created_with_generic_factory` | identity/value | OK | Fresh test package → created user-defined stereotype | Use documented `IRPModelElement.addNewAggr("Stereotype", name)`; JavaDoc includes this package example and the live call succeeds. | `package.user_defined_stereotypes` contains that exact stereotype. | Delete the test package. |

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
| `all_stereotypes` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_project.py::test_all_stereotypes` | identity/value | OK |
| `cg_simplified_model_package` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_project.py::test_cg_simplified_model_package` | identity/value | OK |
| `components` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_project.py::test_components` | identity/value | OK |
| `default_directory_scheme` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_project.py::test_default_directory_scheme_roundtrip` | identity/value | OK |
| `profiles` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_project.py::test_profiles` | identity/value | OK |

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
| `cm_header` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_unit.py::test_set_and_get_cm_header_roundtrip` | identity/value | OK |
| `current_directory` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_unit.py::test_get_current_directory_matches_project` | identity/value | OK |
| `filename` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_unit.py::test_set_and_get_filename_roundtrip` | identity/value | OK |
| `include_in_next_load` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_unit.py::test_set_and_get_include_in_next_load_roundtrip` | identity/value | OK |
| `is_stub` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_unit.py::test_load_and_unload_roundtrip` | identity/value | OK |
| `structure_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_unit.py::test_get_structure_diagrams_returns_diagram_created_on_class` | identity/value | OK |

## IRPUseCase

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `describing_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_use_case.py::test_describing_diagrams` | identity/value | OK |
| `entry_points` | — | none | MISSING |
| `extension_points` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_use_case.py::test_extension_points` | identity/value | OK |
| `is_behavior_overriden` | — | none | MISSING |

## IRPActor

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `is_behavior_overriden` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_actor.py::test_is_behavior_overriden` | identity/value | OK |

## IRPStatechart

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `graphical_elements` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_statechart.py::test_graphical_elements` | identity/value | OK |
| `is_main_behavior` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_statechart.py::test_is_main_behavior` | identity/value | OK |
| `is_overridden` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_statechart.py::test_is_overridden` | identity/value | OK |
| `its_class` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_statechart.py::test_its_class` | identity/value | OK |
| `root_state` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_statechart.py::test_root_state` | identity/value | OK |

## IRPStereotype

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `icon` | — | none | MISSING |
| `is_new_term` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_stereotype.py::test_is_new_term` | identity/value | OK |
| `of_meta_class` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_stereotype.py::test_of_meta_class` | identity/value | OK |

## IRPInstance

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `instantiated_by` | — | none | MISSING |

## IRPModule

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
## IRPRelation

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `inverse` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_relation.py::test_inverse` | identity/value | OK |
| `is_navigable` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_relation.py::test_is_navigable` | identity/value | OK |
| `is_symmetric` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_relation.py::test_is_symmetric` | identity/value | OK |
| `multiplicity` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_relation.py::test_multiplicity` | identity/value | OK |
| `object_as_object_type` | — | none | MISSING |
| `of_class` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_relation.py::test_of_class` | identity/value | OK |
| `other_class` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_relation.py::test_other_class` | identity/value | OK |
| `qualifier` | — | none | MISSING |
| `relation_label` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_relation.py::test_relation_label` | identity/value | OK |
| `relation_link_name` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_relation.py::test_relation_link_name` | identity/value | OK |
| `relation_role_name` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_relation.py::test_relation_role_name` | identity/value | OK |
| `relation_type` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_relation.py::test_relation_type` | identity/value | OK |
| `visibility` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_relation.py::test_visibility` | identity/value | OK |

## IRPDependency

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `dependent` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_dependency.py::test_dependent` | identity/value | OK |
| `depends_on` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_dependency.py::test_depends_on` | identity/value | OK |

## IRPFlow

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `conveyed` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_flow.py::test_conveyed` | identity/value | OK |
| `direction` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_flow.py::test_direction` | identity/value | OK |
| `end1` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_flow.py::test_end1` | identity/value | OK |
| `end1_port` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_flow.py::test_end1_port` | identity/value | OK |
| `end1_sys_ml_port` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_flow.py::test_end1_sys_ml_port` | identity/value | OK |
| `end2` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_flow.py::test_end2` | identity/value | OK |
| `end2_port` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_flow.py::test_end2_port` | identity/value | OK |
| `end2_sys_ml_port` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_flow.py::test_end2_sys_ml_port` | identity/value | OK |

## IRPFlowchart

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `is_analysis_only` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_flowchart.py::test_is_analysis_only` | identity/value | OK |
| `its_owner` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_flowchart.py::test_its_owner` | identity/value | OK |
| `swimlanes` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_flowchart.py::test_swimlanes` | identity/value | OK |

## IRPSwimlane

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `contents` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_swimlane.py::test_contents` | identity/value | OK |
| `represents` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_swimlane.py::test_represents` | identity/value | OK |
| `swimlanes` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_swimlane.py::test_swimlanes` | identity/value | OK |

## IRPAction

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `body` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_action.py::test_body` | identity/value | OK |

## IRPSendAction

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `arg_vals` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_send_action.py::test_arg_vals` | identity/value | OK |
| `event` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_send_action.py::test_event` | identity/value | OK |
| `invoked_operation` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_send_action.py::test_invoked_operation` | identity/value | OK |
| `target` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_send_action.py::test_target` | identity/value | OK |

## IRPFlowItem

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `represented` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_flow_item.py::test_represented` | identity/value | OK |

## IRPObjectNode

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `in_state` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_object_node.py::test_in_state` | identity/value | OK |
| `in_state_list` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_object_node.py::test_in_state_list` | identity/value | OK |
| `represents` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_object_node.py::test_represents` | identity/value | OK |

## IRPCallOperation

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `operation` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_call_operation.py::test_operation` | identity/value | OK |
| `target` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_call_operation.py::test_target` | identity/value | OK |

## IRPContextSpecification

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `multiplicities` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_context_specification.py::test_multiplicities` | identity/value | OK |
| `value` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_context_specification.py::test_value` | identity/value | OK |

## IRPAcceptTimeEvent

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `duration_time` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_accept_time_event.py::test_duration_time` | identity/value | OK |

## IRPComponent

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `additional_sources` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_component.py::test_additional_sources` | identity/value | OK |
| `build_type` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_component.py::test_build_type` | identity/value | OK |
| `configurations` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_component.py::test_configurations` | identity/value | OK |
| `files` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_component.py::test_files` | identity/value | OK |
| `include_path` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_component.py::test_include_path` | identity/value | OK |
| `libraries` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_component.py::test_libraries` | identity/value | OK |
| `nested_components` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_component.py::test_nested_components` | identity/value | OK |
| `panel_diagrams` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_component.py::test_panel_diagrams_empty_state` | weak | WEAK |
| `scope_by_selected_elements` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_component.py::test_scope_by_selected_elements` | identity/value | OK |
| `scope_elements` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_component.py::test_scope_elements` | identity/value | OK |
| `standard_headers` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_component.py::test_standard_headers` | identity/value | OK |
| `variation_points` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_component.py::test_variation_points_empty_state` | weak | WEAK |

## IRPCollaboration

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `activation_condition` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_collaboration.py::test_activation_condition` | identity/value | OK |
| `activation_mode` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_collaboration.py::test_activation_mode` | identity/value | OK |
| `associations` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_collaboration.py::test_associations` | weak | WEAK |
| `classifier` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_collaboration.py::test_classifier` | identity/value | OK |
| `execution_occurrences` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_collaboration.py::test_execution_occurrences` | weak | WEAK |
| `interaction_occurrences` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_collaboration.py::test_interaction_occurrences` | weak | WEAK |
| `interaction_operators` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_collaboration.py::test_interaction_operators` | weak | WEAK |
| `message_points` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_collaboration.py::test_message_points` | weak | WEAK |
| `messages` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_collaboration.py::test_messages` | identity/value | OK |
| `mode` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_collaboration.py::test_mode` | identity/value | OK |

## IRPConfiguration

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `additional_sources` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_additional_sources` | identity/value | OK |
| `all_elements_in_instrumentation_scope` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_all_elements_in_instrumentation_scope` | weak | WEAK |
| `build_set` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_build_set` | identity/value | OK |
| `compiler_switches` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_compiler_switches` | identity/value | OK |
| `generate_code_for_actors` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_generate_code_for_actors` | identity/value | OK |
| `include_path` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_include_path` | identity/value | OK |
| `initial_instances` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_initial_instances` | weak | WEAK |
| `initialization_code` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_initialization_code` | identity/value | OK |
| `instrumentation_scope` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_instrumentation_scope` | weak | WEAK |
| `instrumentation_type` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_instrumentation_type` | identity/value | OK |
| `libraries` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_libraries` | identity/value | OK |
| `link_switches` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_link_switches` | identity/value | OK |
| `scope_type` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_scope_type` | identity/value | OK |
| `standard_headers` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_standard_headers` | identity/value | OK |
| `statechart_implementation` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_statechart_implementation` | identity/value | OK |
| `time_model` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_configuration.py::test_time_model` | identity/value | OK |

## IRPNode

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `component_instances` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_node.py::test_component_instances` | identity/value | OK |
| `cpu_type` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_node.py::test_cpu_type` | identity/value | OK |

## IRPComponentInstance

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
| `component_type` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_component_instance.py::test_component_type` | identity/value | OK |
| `node` | `tests/integration/models/com/telelogic/rhapsody/core/test_irp_component_instance.py::test_node` | identity/value | OK |

## IRPProfile

| Java getter / Python member | Integration test | Assertion | Status |
| --- | --- | --- | --- |
