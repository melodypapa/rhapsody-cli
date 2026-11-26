Elements
========

.. automodule:: rhapsody_cli.models.elements
   :members:
   :undoc-members:
   :show-inheritance:

Supported Element Types
-----------------------

rhapsody-cli provides wrapper classes for all major Rhapsody element types:

**Structural Elements**

* IRPProject - Project container
* IRPPackage - Package container
* IRPActor - Actor in a Rhapsody model
* IRPUseCase - Use case
* RPInstance - Object instance
* RPDiagram - Diagram
* IRPStatechart - Statechart behavior

**Behavioral Elements**

* IRPAttribute - Class attribute
* IRPOperation - Class operation
* RPParameter - Operation parameter
* IRPClassifier - Base classifier

**Other Elements**

* RPRequirement - Requirement element
* RPConnector - Connection between elements

All element types inherit from ``IRPModelElement`` and follow the same interface patterns.

See :doc:`../user_guide/working_with_elements` for usage examples.

Java Package API Reference
--------------------------

`com.telelogic.rhapsody.core`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 1

   com/telelogic/rhapsody/core/irp_actor
   com/telelogic/rhapsody/core/irp_application
   com/telelogic/rhapsody/core/irp_association_class
   com/telelogic/rhapsody/core/irp_argument
   com/telelogic/rhapsody/core/irp_attribute
   com/telelogic/rhapsody/core/irp_class
   com/telelogic/rhapsody/core/irp_classifier
   com/telelogic/rhapsody/core/irp_instance
   com/telelogic/rhapsody/core/irp_interface_item
   com/telelogic/rhapsody/core/irp_model_element
   com/telelogic/rhapsody/core/irp_operation
   com/telelogic/rhapsody/core/irp_package
   com/telelogic/rhapsody/core/irp_port
   com/telelogic/rhapsody/core/irp_project
   com/telelogic/rhapsody/core/irp_statechart
   com/telelogic/rhapsody/core/irp_stereotype
   com/telelogic/rhapsody/core/irp_type
   com/telelogic/rhapsody/core/irp_use_case
   com/telelogic/rhapsody/core/irp_collection
   com/telelogic/rhapsody/core/irp_unit
