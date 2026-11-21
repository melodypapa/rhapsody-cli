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

* RPProject - Project container
* RPPackage - Package container
* RPActor - System actor
* RPUseCase - Use case
* RPInstance - Object instance
* RPDiagram - Diagram
* RPStatechart - State machine

**Behavioral Elements**

* RPAttribute - Class attribute
* RPOperation - Class operation
* RPParameter - Operation parameter
* RPClassifier - Base classifier

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

   com/telelogic/rhapsody/core/irp_class
   com/telelogic/rhapsody/core/irp_model_element
   com/telelogic/rhapsody/core/irp_collection
