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

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_build_no

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_code_gen_simplifiers_registry

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_diag_synth_api

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_external_checker_registry

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_external_ide_registry

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_external_roundtrip_invoker

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_is_hidden_ui

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_omroot

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_ow_pane_mgr

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_projects

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_search_manager

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.get_selection

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.open_project

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.quit

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.regenerate

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.save_all

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.set_hidden_ui

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.set_log

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application.IRPApplication.version
