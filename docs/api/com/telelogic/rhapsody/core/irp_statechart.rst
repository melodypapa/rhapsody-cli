.. _rhapsody-java-interface-IRPStatechart:

IRPStatechart
=============

The ``IRPStatechart`` interface represents the statechart elements underlying a statechart. The statechart itself is represented by ``IRPStatechartDiagram``. Create a statechart through ``IRPClass.add_statechart()``.

- **Java interface:** IRPStatechart
- **Java package:** ``com.telelogic.rhapsody.core``
- **JavaDoc description:** The ``IRPStatechart`` interface represents the statechart elements underlying a statechart. The statechart itself is represented by ``IRPStatechartDiagram``.
- **Python wrapper:** ``IRPStatechart``
- **Python import:** ``from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPStatechart``
- **Canonical module:** ``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart``

API reference
-------------

``IRPStatechart`` wraps the statechart behavior and its graphical representation. Python methods use snake_case; catalog properties are exposed as read-only Python properties.

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.add_free_shape_by_type

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.add_image

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.add_new_accept_event_action

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.add_new_accept_time_event

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.add_new_edge_by_type

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.add_new_edge_for_element

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.add_new_node_by_type

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.add_new_node_for_element

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.add_text_box

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.open_diagram_view

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.close_diagram

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.create_graphics

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.delete_state

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.find_trigger

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.get_all_triggers

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.get_elements_in_diagram

.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.graphical_elements

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.get_inherits_from

.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.is_main_behavior

.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.is_overridden

.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.its_class

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.get_picture

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.get_picture_as

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.get_picture_as_divided_metafiles

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.get_pictures_with_image_map

.. autoproperty:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.root_state

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.get_statechart_diagram

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.override_inheritance

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.populate_diagram

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.set_as_main_behavior

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.set_show_diagram_frame

.. automethod:: rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart.IRPStatechart.unoverride_inheritance
