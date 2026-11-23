.. _rhapsody-java-interface-IRPApplication:

IRPApplication
==============

The IRPApplication interface represents the Rhapsody application, and its methods reflect many of the commands that can be accessed from the Rhapsody menu bar.

- **Java interface:** IRPApplication
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The IRPApplication interface represents the Rhapsody application, and its methods reflect many of the commands that you can access from the Rhapsody menu bar.
- **Python wrapper:** IRPApplication
- **Python import:** ``from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPApplication``
- **Canonical module:** ``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application``

API reference
-------------

The wrapper exposes the Rhapsody application COM interface. ``active_project()`` returns ``None`` when the COM member reports that no project is active; commands that require a project handle that condition at the CLI boundary.

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.active_project

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.add_to_model

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.add_to_model_ex

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.bring_window_to_top

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.check_model

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.create_new_collection

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.create_new_project

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.generate

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.generate_elements

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.generate_entire_project

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.build_no
.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.build_no

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_code_gen_simplifiers_registry

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_diag_synth_api

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_external_checker_registry

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_external_ide_registry

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_external_roundtrip_invoker

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.is_hidden_ui
.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.is_hidden_ui

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.omroot
.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.omroot

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_ow_pane_mgr

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.projects
.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.projects

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_search_manager

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_selection

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.open_project

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.quit

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.regenerate

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.save_all

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.set_hidden_ui

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.set_log

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.version

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.add_profile_to_model
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.add_selected_to_favorites
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.add_to_model_by_reference
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.add_to_model_from_url
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.add_units_to_model
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.allow_browser_refresh
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.allow_ge_refresh
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.allow_rmm_remote_oslc_links_load
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_application_connection_string
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_application_name
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.application_root
.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.application_root
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_application_status
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.set_application_status
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.apply_new_terms_profile
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.apply_window_layout
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.arc_check_out
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.build
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.build_entire_project
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.build_with_dependencies
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.can_redo
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.can_undo
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.check_in
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.check_out
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.clean
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.clear_output_window
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.close_all_animated_sequence_diagrams
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.compare_sequence_diagram
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.set_component
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.set_configuration
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.connect_to_archive
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.connect_to_imported_model
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.connect_to_target
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.create_and_insert_project
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.create_domain_from_profile
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.create_embedded_web_view_window
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.create_progress_bar
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_dm_bool_property
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.set_dm_bool_property
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_dm_model_workspace_folder
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_dm_property
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.set_dm_property
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.d_m_refresh_recursive
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.d_m_sync_and_refresh
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.dbg_check_com_in
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.dbg_check_com_out
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.deferred_add_to_model
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.delete_project_from_list
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.delete_window_layout
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_diagram_of_selected_element
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.disconnect_from_target
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.download_to_target
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.end_undo_transaction
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.enter_animation_command
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.error_message
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_error_message
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_executable_folder
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.execute_command
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.execute_command_line
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.execute_transformation_sequence
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.expand_string_keywords
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.export_window_layout
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.fixpack
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.force_output2_console
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.force_roundtrip
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.force_roundtrip_elements
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.generate_main_and_make_files
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.generate_with_dependencies
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_helper_status
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.set_helper_status
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.high_light_element
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.highlight_by_handle
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.import_classes
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.import_design_manager_model
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.import_sync_simulink_block2
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.import_tlb
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.import_window_layout
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_ini_file_parameter_value
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.insert_project
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.insert_project_from_design_manager
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.interface_name
.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.interface_name
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.invoke_plugins_method
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.invoke_rpe
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.is_load_on_demand
.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.is_load_on_demand
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.is_rhapsody_cl
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.is_rhapsody_file_type
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.is_valid_web_view
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.language
.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.language
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_list_of_factory_properties
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_list_of_selected_elements
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_list_of_site_properties
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_locale_name
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.log_root
.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.log_root
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.login_to_design_manager_with_alias
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.login_to_design_manager_with_certificate
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.login_to_design_manager_with_username
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.make
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.merge_elements
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_model_element_from_source
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.new_project_on_design_manager
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.notify_file_changed
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.open_active_x_view
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.open_advanced_search_and_replace_dialog
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.open_diagram_view
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.open_file_list
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.open_project_from_design_manager
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.open_project_from_design_manager_after_login
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.open_project_from_url
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.open_project_with_last_session
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.open_project_without_sub_units
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_output_window_text
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_progress_bar
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.rebuild
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.rebuild_entire_project
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.rebuild_with_dependencies
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.redo
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.refactor_selected_operation
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.refresh_all_views
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.regenerate_elements
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.regenerate_entire_project
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.regenerate_with_dependencies
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.register_com_client
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.remove_progress_bar
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.rename_window_layout
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.report
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.reset_window_layout
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_rhapsody_handle_error_function
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_rhapsody_handle_error_function_long
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.rhp_checkin_license
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.rhp_checkout_license
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.roundtrip
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.roundtrip_elements
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.run_application
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.run_helper
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.run_helper_with_parameters
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.save_check_model_result
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.save_window_layout
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.select_graph_elements
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.select_model_elements
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_selected_element
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_selected_graph_elements
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.serial_no
.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.serial_no
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.start_undo_transaction
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.sync_build
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.terminate_application
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_the_code_generator_interface
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_the_external_code_generator_invoker
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_the_integrator_interface
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_the_java_plugins_interface
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_the_roundtrip_interface
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.tool_set
.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.tool_set
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.undo
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.unload_from_target
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.unregister_com_client
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.set_update_recent_file_list
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.update_rmm_data_to_new_version
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.user_data_root
.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.user_data_root
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.user_omroot
.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.user_omroot
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.version_number_long
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_web_view_url
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.set_web_view_url
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_window_layout_list
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.write_to_output_window
.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_plug_in_window
