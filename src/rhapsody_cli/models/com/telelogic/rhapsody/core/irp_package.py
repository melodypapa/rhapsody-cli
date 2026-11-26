"""Wrappers for ``com.telelogic.rhapsody.core.IRPPackage``.

Canonical module for :class:`IRPPackage`; see the class requirement document at
``docs/requirements/com/telelogic/rhapsody/core/irp_package.md``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import (
        IRPClass,
        IRPClassifier,
        IRPCollaborationDiagram,
        IRPComponentDiagram,
        IRPDeploymentDiagram,
        IRPObjectModelDiagram,
        IRPPort,
        IRPSequenceDiagram,
        IRPTimingDiagram,
        IRPUseCaseDiagram,
    )
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actor import IRPActor
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flow import IRPFlow
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flow_item import IRPFlowItem
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flowchart import IRPFlowchart
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPLink
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_other_model import IRPSysMLPort
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_relation import IRPRelation
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart import IRPStatechart
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_use_case import IRPUseCase


class IRPPackage(IRPUnit):
    """Wraps ``IRPPackage``: represents a package that contains model elements."""

    # IRPPackage method parity checklist:
    # [x] add_activity_diagram  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_actor  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_class  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] add_collaboration_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_component_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_deployment_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_event  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] add_flow_items  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_flows  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_global_function  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] add_global_object  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_global_variable  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] add_implicit_object  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] add_instance_specification  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_link  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] add_link_between_sysml_ports  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] add_module  [x] impl  [x] docstring  [ ] unit test  [x] integration test
    # [x] add_nested_package  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [ ] add_node  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_object_model_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_panel_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] add_sequence_diagram  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] add_statechart  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_timing_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_type  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] add_use_case  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [ ] add_use_case_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] delete_actor  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] delete_class  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] delete_collaboration_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] delete_component_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] delete_deployment_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] delete_event  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] delete_flow_items  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] delete_flows  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] delete_global_function  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] delete_global_object  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] delete_global_variable  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] delete_node  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] delete_object_model_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] delete_package  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] delete_panel_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] delete_sequence_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] delete_timing_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] delete_type  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] delete_use_case  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] delete_use_case_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] find_actor  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] find_all_by_name  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] find_class  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] find_event  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] find_global_function  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] find_global_object  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] find_global_variable  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] find_node  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] find_type  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] find_usage  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] find_use_case  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] get_actors  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_all_nested_elements  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] get_behavioral_diagrams  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] get_classes  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [ ] get_collaboration_diagrams  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_component_diagrams  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_deployment_diagrams  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] get_events  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_events_base_id  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_flow_items  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_flows  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] get_global_functions  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_global_objects  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_global_variables  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_instance_specifications  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_links  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_modules  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] get_namespace  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] get_nested_classifiers  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_nested_components  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] get_nodes  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] get_object_model_diagrams  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] get_packages  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [ ] get_panel_diagrams  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] get_remote_requirements_populate_mode  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_root_instance_specifications  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_saved_in_seperate_directory  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_sequence_diagrams  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] get_source_artifacts  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_timing_diagrams  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_types  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_use_case_diagrams  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] get_use_cases  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_user_defined_stereotypes  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] login_to_remote_artifact_server  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] populate_remote_requirements  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] re_calculate_events_base_id  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_remote_requirements_populate_mode  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_saved_in_seperate_directory  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] update_contained_diagrams_on_server  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] update_contained_matrices_on_server  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] update_contained_tables_on_server  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_unit / irp_model_element methods (covered by rp_unit / rp_model_element checklists)
    # No deprecated IRPPackage methods.

    def add_class(self, name: str) -> IRPClass:
        """Adds a new class to the package.

        Args:
            name: The name of the new class.

        Returns:
            The wrapped ``IRPClass`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addClass(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass

        return cast(IRPClass, self.wrap(self.call_com(lambda: self._com.addClass(name))))

    def add_nested_package(self, name: str) -> IRPPackage:
        """Adds a nested package to this package.

        Args:
            name: The name of the new nested package.

        Returns:
            The wrapped ``IRPPackage`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addNestedPackage(java.lang.String name)
        """
        return cast(IRPPackage, self.wrap(self.call_com(lambda: self._com.addNestedPackage(name))))

    def add_actor(self, name: str) -> IRPActor:
        """Adds a new actor to the package.

        Args:
            name: The name of the new actor.

        Returns:
            The wrapped ``IRPActor`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addActor(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actor import IRPActor

        return cast(IRPActor, self.wrap(self.call_com(lambda: self._com.addActor(name))))

    def add_global_function(self, name: str) -> IRPOperation:
        """Adds a new global function to the package.

        Args:
            name: The name of the new global function.

        Returns:
            The wrapped function element created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addGlobalFunction(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation

        return cast(IRPOperation, self.wrap(self.call_com(lambda: self._com.addGlobalFunction(name))))

    def add_flow_items(self, name: str) -> IRPFlowItem:
        """Adds a new flow item to the package.

        Args:
            name: The name of the new flow item.

        Returns:
            The wrapped flow item element created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addFlowItems(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flow_item import IRPFlowItem

        return cast(IRPFlowItem, self.wrap(self.call_com(lambda: self._com.addFlowItems(name))))

    def add_flows(self, name: str) -> IRPFlow:
        """Adds a new flow to the package.

        Args:
            name: The name of the new flow.

        Returns:
            The wrapped flow element created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addFlows(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flow import IRPFlow

        return cast(IRPFlow, self.wrap(self.call_com(lambda: self._com.addFlows(name))))

    @property
    def packages(self) -> IRPCollection:
        """Returns all nested packages in this package.

        Returns:
            An ``IRPCollection`` of ``IRPPackage`` objects.
        """
        return IRPCollection(self.get_com_property(self._com, "packages"))

    @property
    def classes(self) -> IRPCollection:
        """Returns all classes contained in this package.

        Returns:
            An ``IRPCollection`` of ``IRPClass`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getClasses()
        """
        return IRPCollection(self.get_com_property(self._com, "classes"))

    @property
    def actors(self) -> IRPCollection:
        """Returns all actors contained in this package.

        Returns:
            An ``IRPCollection`` of ``IRPActor`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getActors()
        """
        return IRPCollection(self.get_com_property(self._com, "actors"))

    @property
    def use_cases(self) -> IRPCollection:
        """Returns all use cases contained in this package.

        Returns:
            An ``IRPCollection`` of ``IRPUseCase`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getUseCases()
        """
        return IRPCollection(self.get_com_property(self._com, "useCases"))

    def add_use_case(self, name: str) -> IRPUseCase:
        """Adds a new use case to the package.

        Args:
            name: The name of the new use case.

        Returns:
            The wrapped ``IRPUseCase`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addUseCase(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_use_case import IRPUseCase

        return cast(IRPUseCase, self.wrap(self.call_com(lambda: self._com.addUseCase(name))))

    # --- Diagram adders (Pattern E) ---
    def add_activity_diagram(self) -> IRPFlowchart:
        """Adds a new activity diagram to the package.

        Returns:
            The wrapped flowchart created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addActivityDiagram()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flowchart import IRPFlowchart

        return cast(IRPFlowchart, self.wrap(self.call_com(lambda: self._com.addActivityDiagram())))

    def add_sequence_diagram(self, name: str) -> IRPSequenceDiagram:
        """Adds a new sequence diagram to the package.

        Args:
            name: The name of the new sequence diagram.

        Returns:
            The wrapped ``IRPSequenceDiagram`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addSequenceDiagram(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPSequenceDiagram

        return cast(IRPSequenceDiagram, self.wrap(self.call_com(lambda: self._com.addSequenceDiagram(name))))

    def add_use_case_diagram(self, name: str) -> IRPUseCaseDiagram:
        """Adds a new use case diagram to the package.

        Args:
            name: The name of the new use case diagram.

        Returns:
            The wrapped ``IRPUseCaseDiagram`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addUseCaseDiagram(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUseCaseDiagram

        return cast(IRPUseCaseDiagram, self.wrap(self.call_com(lambda: self._com.addUseCaseDiagram(name))))

    def add_collaboration_diagram(self, name: str) -> IRPCollaborationDiagram:
        """Adds a new collaboration diagram to the package.

        Args:
            name: The name of the new collaboration diagram.

        Returns:
            The wrapped ``IRPCollaborationDiagram`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addCollaborationDiagram(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPCollaborationDiagram

        return cast(IRPCollaborationDiagram, self.wrap(self.call_com(lambda: self._com.addCollaborationDiagram(name))))

    def add_component_diagram(self, name: str) -> IRPComponentDiagram:
        """Adds a new component diagram to the package.

        Args:
            name: The name of the new component diagram.

        Returns:
            The wrapped ``IRPComponentDiagram`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addComponentDiagram(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPComponentDiagram

        return cast(IRPComponentDiagram, self.wrap(self.call_com(lambda: self._com.addComponentDiagram(name))))

    def add_deployment_diagram(self, name: str) -> IRPDeploymentDiagram:
        """Adds a new deployment diagram to the package.

        Args:
            name: The name of the new deployment diagram.

        Returns:
            The wrapped ``IRPDeploymentDiagram`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addDeploymentDiagram(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPDeploymentDiagram

        return cast(IRPDeploymentDiagram, self.wrap(self.call_com(lambda: self._com.addDeploymentDiagram(name))))

    def add_object_model_diagram(self, name: str) -> IRPObjectModelDiagram:
        """Adds a new object model diagram to the package.

        Args:
            name: The name of the new object model diagram.

        Returns:
            The wrapped ``IRPObjectModelDiagram`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addObjectModelDiagram(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPObjectModelDiagram

        return cast(IRPObjectModelDiagram, self.wrap(self.call_com(lambda: self._com.addObjectModelDiagram(name))))

    def add_statechart(self) -> IRPStatechart:
        """Adds a new statechart to the package.

        Returns:
            The wrapped statechart created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addStatechart()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart import IRPStatechart

        return cast(IRPStatechart, self.wrap(self.call_com(lambda: self._com.addStatechart())))

    def add_timing_diagram(self, name: str) -> IRPTimingDiagram:
        """Adds a new timing diagram to the package.

        Args:
            name: The name of the new timing diagram.

        Returns:
            The wrapped ``IRPTimingDiagram`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addTimingDiagram(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTimingDiagram

        return cast(IRPTimingDiagram, self.wrap(self.call_com(lambda: self._com.addTimingDiagram(name))))

    def add_panel_diagram(self, name: str) -> IRPModelElement:
        """Adds a new panel diagram to the package.

        Args:
            name: The name of the new panel diagram.

        Returns:
            The wrapped panel diagram element created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addPanelDiagram(java.lang.String name)
        """
        return cast(IRPModelElement, self.wrap(self.call_com(lambda: self._com.addPanelDiagram(name))))

    # --- Diagram getters (Pattern C) ---
    @property
    def sequence_diagrams(self) -> IRPCollection:
        """Returns all sequence diagrams contained in this package.

        Returns:
            An ``IRPCollection`` of ``IRPSequenceDiagram`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getSequenceDiagrams()
        """
        return IRPCollection(self.get_com_property(self._com, "sequenceDiagrams"))

    @property
    def use_case_diagrams(self) -> IRPCollection:
        """Returns all use case diagrams contained in this package.

        Returns:
            An ``IRPCollection`` of ``IRPUseCaseDiagram`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getUseCaseDiagrams()
        """
        return IRPCollection(self.get_com_property(self._com, "useCaseDiagrams"))

    @property
    def collaboration_diagrams(self) -> IRPCollection:
        """Returns all collaboration diagrams contained in this package.

        Returns:
            An ``IRPCollection`` of ``IRPCollaborationDiagram`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getCollaborationDiagrams()
        """
        return IRPCollection(self.get_com_property(self._com, "collaborationDiagrams"))

    @property
    def component_diagrams(self) -> IRPCollection:
        """Returns all component diagrams contained in this package.

        Returns:
            An ``IRPCollection`` of ``IRPComponentDiagram`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getComponentDiagrams()
        """
        return IRPCollection(self.get_com_property(self._com, "componentDiagrams"))

    @property
    def deployment_diagrams(self) -> IRPCollection:
        """Returns all deployment diagrams contained in this package.

        Returns:
            An ``IRPCollection`` of ``IRPDeploymentDiagram`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getDeploymentDiagrams()
        """
        return IRPCollection(self.get_com_property(self._com, "deploymentDiagrams"))

    @property
    def object_model_diagrams(self) -> IRPCollection:
        """Returns all object model diagrams contained in this package.

        Returns:
            An ``IRPCollection`` of ``IRPObjectModelDiagram`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getObjectModelDiagrams()
        """
        return IRPCollection(self.get_com_property(self._com, "objectModelDiagrams"))

    @property
    def timing_diagrams(self) -> IRPCollection:
        """Returns all timing diagrams contained in this package.

        Returns:
            An ``IRPCollection`` of ``IRPTimingDiagram`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getTimingDiagrams()
        """
        return IRPCollection(self.get_com_property(self._com, "timingDiagrams"))

    @property
    def panel_diagrams(self) -> IRPCollection:
        """Returns all panel diagrams contained in this package.

        Returns:
            An ``IRPCollection`` of panel diagram elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getPanelDiagrams()
        """
        return IRPCollection(self.get_com_property(self._com, "panelDiagrams"))

    # --- Diagram deleters (Pattern F) ---
    def delete_sequence_diagram(self, name: str) -> None:
        """Deletes the sequence diagram with the specified name.

        Args:
            name: The name of the sequence diagram to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteSequenceDiagram(java.lang.String name)
        """
        self.call_com(lambda: self._com.deleteSequenceDiagram(name))

    def delete_use_case_diagram(self, name: str) -> None:
        """Deletes the use case diagram with the specified name.

        Args:
            name: The name of the use case diagram to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteUseCaseDiagram(java.lang.String name)
        """
        self.call_com(lambda: self._com.deleteUseCaseDiagram(name))

    def delete_collaboration_diagram(self, name: str) -> None:
        """Deletes the collaboration diagram with the specified name.

        Args:
            name: The name of the collaboration diagram to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteCollaborationDiagram(java.lang.String name)
        """
        self.call_com(lambda: self._com.deleteCollaborationDiagram(name))

    def delete_component_diagram(self, name: str) -> None:
        """Deletes the component diagram with the specified name.

        Args:
            name: The name of the component diagram to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteComponentDiagram(java.lang.String name)
        """
        self.call_com(lambda: self._com.deleteComponentDiagram(name))

    def delete_deployment_diagram(self, name: str) -> None:
        """Deletes the deployment diagram with the specified name.

        Args:
            name: The name of the deployment diagram to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteDeploymentDiagram(java.lang.String name)
        """
        self.call_com(lambda: self._com.deleteDeploymentDiagram(name))

    def delete_object_model_diagram(self, name: str) -> None:
        """Deletes the object model diagram with the specified name.

        Args:
            name: The name of the object model diagram to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteObjectModelDiagram(java.lang.String name)
        """
        self.call_com(lambda: self._com.deleteObjectModelDiagram(name))

    def delete_timing_diagram(self, name: str) -> None:
        """Deletes the timing diagram with the specified name.

        Args:
            name: The name of the timing diagram to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteTimingDiagram(java.lang.String name)
        """
        self.call_com(lambda: self._com.deleteTimingDiagram(name))

    def delete_panel_diagram(self, name: str) -> None:
        """Deletes the panel diagram with the specified name.

        Args:
            name: The name of the panel diagram to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deletePanelDiagram(java.lang.String name)
        """
        self.call_com(lambda: self._com.deletePanelDiagram(name))

    # --- Classifier deleters (Pattern F) ---
    def delete_class(self, cls: IRPModelElement) -> None:
        """Deletes a class from the package.

        Args:
            cls: The class to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteClass(com.telelogic.rhapsody.core.IRPClass cls)
        """
        self.call_com(lambda: self._com.deleteClass(cls._com))

    def delete_actor(self, actor: IRPModelElement) -> None:
        """Deletes an actor from the package.

        Args:
            actor: The actor to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteActor(com.telelogic.rhapsody.core.IRPActor actor)
        """
        self.call_com(lambda: self._com.deleteActor(actor._com))

    def delete_use_case(self, use_case: IRPModelElement) -> None:
        """Deletes a use case from the package.

        Args:
            use_case: The use case to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteUseCase(com.telelogic.rhapsody.core.IRPUseCase useCase)
        """
        self.call_com(lambda: self._com.deleteUseCase(use_case._com))

    def delete_flow_items(self, flow_item: IRPFlowItem) -> None:
        """Deletes a flow item from the package.

        Args:
            flow_item: The flow item to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteFlowItems(com.telelogic.rhapsody.core.IRPFlowItem flowItem)
        """
        self.call_com(lambda: self._com.deleteFlowItems(flow_item._com))

    def delete_flows(self, flow: IRPFlow) -> None:
        """Deletes a flow from the package.

        Args:
            flow: The flow to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteFlows(com.telelogic.rhapsody.core.IRPFlow flow)
        """
        self.call_com(lambda: self._com.deleteFlows(flow._com))

    def delete_package(self) -> None:
        """Deletes this package.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deletePackage()
        """
        self.call_com(lambda: self._com.deletePackage())

    # --- Finders (Pattern B) ---
    def find_class(self, name: str) -> IRPClass:
        """Finds a class in the package by name.

        Args:
            name: The name of the class to find.

        Returns:
            The wrapped ``IRPClass`` if found, otherwise empty wrapper.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::findClass(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass

        return cast(IRPClass, self.wrap(self.call_com(lambda: self._com.findClass(name))))

    def find_actor(self, name: str) -> IRPActor:
        """Finds an actor in the package by name.

        Args:
            name: The name of the actor to find.

        Returns:
            The wrapped ``IRPActor`` if found, otherwise empty wrapper.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::findActor(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actor import IRPActor

        return cast(IRPActor, self.wrap(self.call_com(lambda: self._com.findActor(name))))

    def find_use_case(self, name: str) -> IRPUseCase:
        """Finds a use case in the package by name.

        Args:
            name: The name of the use case to find.

        Returns:
            The wrapped ``IRPUseCase`` if found, otherwise empty wrapper.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::findUseCase(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_use_case import IRPUseCase

        return cast(IRPUseCase, self.wrap(self.call_com(lambda: self._com.findUseCase(name))))

    # --- Event methods ---
    def add_event(self, name: str) -> IRPModelElement:
        """Adds a new event to the package.

        Args:
            name: The name of the new event.

        Returns:
            The wrapped event element created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addEvent(java.lang.String name)
        """
        return cast(IRPModelElement, self.wrap(self.call_com(lambda: self._com.addEvent(name))))

    @property
    def events(self) -> IRPCollection:
        """Returns all events contained in this package.

        Returns:
            An ``IRPCollection`` of event elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getEvents()
        """
        return IRPCollection(self.get_com_property(self._com, "events"))

    @property
    def flow_items(self) -> IRPCollection:
        """Returns all flow items contained in this package.

        Returns:
            An ``IRPCollection`` of flow item elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getFlowItems()
        """
        return IRPCollection(self.get_com_property(self._com, "flowItems"))

    @property
    def flows(self) -> IRPCollection:
        """Returns all flows contained in this package.

        Returns:
            An ``IRPCollection`` of flow elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getFlows()
        """
        return IRPCollection(self.get_com_property(self._com, "flows"))

    def find_event(self, name: str) -> IRPModelElement | None:
        """Finds an event in the package by name.

        Args:
            name: The name of the event to find.

        Returns:
            The wrapped event element if found.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::findEvent(java.lang.String name)
        """
        return self.wrap(self.call_com(lambda: self._com.findEvent(name)))

    def delete_event(self, event: IRPModelElement) -> None:
        """Deletes an event from the package.

        Args:
            event: The event to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteEvent(com.telelogic.rhapsody.core.IRPEvent event)
        """
        self.call_com(lambda: self._com.deleteEvent(event._com))

    # --- Node methods ---
    def add_node(self, name: str) -> IRPModelElement:
        """Adds a new node to the package.

        Args:
            name: The name of the new node.

        Returns:
            The wrapped node element created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addNode(java.lang.String name)
        """
        return cast(IRPModelElement, self.wrap(self.call_com(lambda: self._com.addNode(name))))

    @property
    def nodes(self) -> IRPCollection:
        """Returns all nodes contained in this package.

        Returns:
            An ``IRPCollection`` of node elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getNodes()
        """
        return IRPCollection(self.get_com_property(self._com, "nodes"))

    def find_node(self, name: str) -> IRPModelElement | None:
        """Finds a node in the package by name.

        Args:
            name: The name of the node to find.

        Returns:
            The wrapped node element if found.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::findNode(java.lang.String name)
        """
        return self.wrap(self.call_com(lambda: self._com.findNode(name)))

    def delete_node(self, name: str) -> None:
        """Deletes the node with the specified name.

        Args:
            name: The name of the node to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteNode(java.lang.String name)
        """
        self.call_com(lambda: self._com.deleteNode(name))

    # --- Module methods ---
    def add_module(self, name: str) -> IRPModelElement:
        """Adds a new module to the package.

        Args:
            name: The name of the new module.

        Returns:
            The wrapped module element created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addModule(java.lang.String name)
        """
        return cast(IRPModelElement, self.wrap(self.call_com(lambda: self._com.addModule(name))))

    @property
    def modules(self) -> IRPCollection:
        """Returns all modules contained in this package.

        Returns:
            An ``IRPCollection`` of module elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getModules()
        """
        return IRPCollection(self.get_com_property(self._com, "modules"))

    # --- Type methods ---
    def add_type(self, name: str) -> IRPModelElement:
        """Adds a new type to the package.

        Args:
            name: The name of the new type.

        Returns:
            The wrapped type element created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addType(java.lang.String name)
        """
        return cast(IRPModelElement, self.wrap(self.call_com(lambda: self._com.addType(name))))

    @property
    def types(self) -> IRPCollection:
        """Returns all types contained in this package.

        Returns:
            An ``IRPCollection`` of type elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getTypes()
        """
        return IRPCollection(self.get_com_property(self._com, "types"))

    def find_type(self, name: str) -> IRPModelElement | None:
        """Finds a type in the package by name.

        Args:
            name: The name of the type to find.

        Returns:
            The wrapped type element if found.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::findType(java.lang.String name)
        """
        return self.wrap(self.call_com(lambda: self._com.findType(name)))

    def delete_type(self, type_elem: IRPModelElement) -> None:
        """Deletes a type from the package.

        Args:
            type_elem: The type to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteType(com.telelogic.rhapsody.core.IRPType type)
        """
        self.call_com(lambda: self._com.deleteType(type_elem._com))

    # --- Global function methods ---
    def find_global_function(self, name: str) -> IRPOperation:
        """Finds a global function in the package by name.

        Args:
            name: The name of the global function to find.

        Returns:
            The wrapped operation element if found.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::findGlobalFunction(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation

        return cast(IRPOperation, self.wrap(self.call_com(lambda: self._com.findGlobalFunction(name))))

    @property
    def global_functions(self) -> IRPCollection:
        """Returns all global functions contained in this package.

        Returns:
            An ``IRPCollection`` of operation elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getGlobalFunctions()
        """
        return IRPCollection(self.get_com_property(self._com, "globalFunctions"))

    def delete_global_function(self, func: IRPModelElement) -> None:
        """Deletes a global function from the package.

        Args:
            func: The global function to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteGlobalFunction(com.telelogic.rhapsody.core.IRPOperation func)
        """
        self.call_com(lambda: self._com.deleteGlobalFunction(func._com))

    # --- Global object methods ---
    def add_global_object(self, name: str, other_class_name: str, other_class_package_name: str) -> IRPRelation:
        """Adds an instance of an existing class to the package.

        Args:
            name: The name of the new object.
            other_class_name: The name of the class to instantiate.
            other_class_package_name: The name of the package containing that class.

        Returns:
            The wrapped object relation created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addGlobalObject(java.lang.String name, java.lang.String otherClassName, java.lang.String otherClassPackageName)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_relation import IRPRelation

        return cast(IRPRelation, self.wrap(self.call_com(lambda: self._com.addGlobalObject(name, other_class_name, other_class_package_name))))

    @property
    def global_objects(self) -> IRPCollection:
        """Returns all global objects contained in this package.

        Returns:
            An ``IRPCollection`` of global object elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getGlobalObjects()
        """
        return IRPCollection(self.get_com_property(self._com, "globalObjects"))

    def find_global_object(self, name: str) -> IRPModelElement | None:
        """Finds a global object in the package by name.

        Args:
            name: The name of the global object to find.

        Returns:
            The wrapped global object element if found.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::findGlobalObject(java.lang.String name)
        """
        return self.wrap(self.call_com(lambda: self._com.findGlobalObject(name)))

    def delete_global_object(self, obj: IRPModelElement) -> None:
        """Deletes a global object from the package.

        Args:
            obj: The global object to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteGlobalObject(com.telelogic.rhapsody.core.IRPGlobalObject obj)
        """
        self.call_com(lambda: self._com.deleteGlobalObject(obj._com))

    # --- Global variable methods ---
    def add_global_variable(self, name: str) -> IRPModelElement:
        """Adds a new global variable to the package.

        Args:
            name: The name of the new global variable.

        Returns:
            The wrapped global variable element created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addGlobalVariable(java.lang.String name)
        """
        return cast(IRPModelElement, self.wrap(self.call_com(lambda: self._com.addGlobalVariable(name))))

    @property
    def global_variables(self) -> IRPCollection:
        """Returns all global variables contained in this package.

        Returns:
            An ``IRPCollection`` of global variable elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getGlobalVariables()
        """
        return IRPCollection(self.get_com_property(self._com, "globalVariables"))

    def find_global_variable(self, name: str) -> IRPModelElement | None:
        """Finds a global variable in the package by name.

        Args:
            name: The name of the global variable to find.

        Returns:
            The wrapped global variable element if found.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::findGlobalVariable(java.lang.String name)
        """
        return self.wrap(self.call_com(lambda: self._com.findGlobalVariable(name)))

    def delete_global_variable(self, var: IRPModelElement) -> None:
        """Deletes a global variable from the package.

        Args:
            var: The global variable to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::deleteGlobalVariable(com.telelogic.rhapsody.core.IRPVariable var)
        """
        self.call_com(lambda: self._com.deleteGlobalVariable(var._com))

    # --- Nested classifier methods ---
    @property
    def nested_classifiers(self) -> IRPCollection:
        """Returns all nested classifiers in this package.

        Returns:
            An ``IRPCollection`` of classifier elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getNestedClassifiers()
        """
        return IRPCollection(self.get_com_property(self._com, "nestedClassifiers"))

    @property
    def nested_components(self) -> IRPCollection:
        """Returns all nested components in this package.

        Returns:
            An ``IRPCollection`` of component elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getNestedComponents()
        """
        return IRPCollection(self.get_com_property(self._com, "nestedComponents"))

    # --- Instance specification methods ---
    def add_instance_specification(self, name: str, classifier: IRPClassifier) -> IRPModelElement:
        """Add an instance specification for a classifier.

        Args:
            name: The name of the new instance specification.
            classifier: The classifier that the instance specification should instantiate.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addInstanceSpecification(java.lang.String name, com.telelogic.rhapsody.core.IRPClassifier classifier)
        """
        raise NotImplementedError("addInstanceSpecification is not exposed in the Rhapsody COM automation type library.")

    @property
    def instance_specifications(self) -> IRPCollection:
        """Returns all instance specifications contained in this package.

        Returns:
            An ``IRPCollection`` of instance specification elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getInstanceSpecifications()
        """
        return IRPCollection(self.get_com_property(self._com, "instanceSpecifications"))

    # --- Link methods ---
    def add_link(self, from_part: IRPInstance, to_part: IRPInstance, assoc: IRPRelation | None, from_port: IRPPort | None, to_port: IRPPort | None) -> IRPLink:
        """Creates a link between two objects in the package.

        Args:
            from_part: The source object.
            to_part: The target object.
            assoc: The association represented by the link, or ``None`` when ports are specified.
            from_port: The source port, or ``None`` when an association is specified.
            to_port: The target port, or ``None`` when an association is specified.

        Returns:
            The wrapped link created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addLink(
                com.telelogic.rhapsody.core.IRPInstance fromPart,
                com.telelogic.rhapsody.core.IRPInstance toPart,
                com.telelogic.rhapsody.core.IRPRelation assoc,
                com.telelogic.rhapsody.core.IRPPort fromPort,
                com.telelogic.rhapsody.core.IRPPort toPort)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPLink

        assoc_com = assoc._com if assoc is not None else None
        from_port_com = from_port._com if from_port is not None else None
        to_port_com = to_port._com if to_port is not None else None
        return cast(IRPLink, self.wrap(self.call_com(lambda: self._com.addLink(from_part._com, to_part._com, assoc_com, from_port_com, to_port_com))))

    @property
    def links(self) -> IRPCollection:
        """Returns all links contained in this package.

        Returns:
            An ``IRPCollection`` of link elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getLinks()
        """
        return IRPCollection(self.get_com_property(self._com, "links"))

    # --- Find all by name ---
    def find_all_by_name(self, name: str, meta_class: str) -> IRPModelElement:
        """Finds the first element with the given name and metaclass in this package.

        Args:
            name: The name of the element to find.
            meta_class: The metaclass of the element to find.

        Returns:
            The first matching model element.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::findAllByName(java.lang.String name, java.lang.String metaClass)
        """
        return cast(IRPModelElement, self.wrap(self.call_com(lambda: self._com.findAllByName(name, meta_class))))

    # --- Behavioral diagrams ---
    @property
    def behavioral_diagrams(self) -> IRPCollection:
        """Returns all behavioral diagrams contained in this package.

        Returns:
            An ``IRPCollection`` of behavioral diagram elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getBehavioralDiagrams()
        """
        return IRPCollection(self.get_com_property(self._com, "behavioralDiagrams"))

    # --- Source artifacts ---
    @property
    def source_artifacts(self) -> IRPCollection:
        """Returns all source artifacts contained in this package.

        Returns:
            An ``IRPCollection`` of source artifact elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getSourceArtifacts()
        """
        return IRPCollection(self.get_com_property(self._com, "sourceArtifacts"))

    # --- Find usage ---
    def find_usage(self, element: IRPModelElement) -> IRPCollection:
        """Finds all usages of an element in this package.

        Args:
            element: The element to find usages for.

        Returns:
            An ``IRPCollection`` of elements that use the given element.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::findUsage(com.telelogic.rhapsody.core.IRPModelElement element)
        """
        return IRPCollection(self.call_com(lambda: self._com.findUsage(element._com)))

    # --- Remote Requirements Methods (Task 3) ---
    def get_remote_requirements_populate_mode(self) -> str:
        """Returns the remote requirements populate mode for this package.

        Returns:
            The populate mode, one of ``"All"``, ``"Linked"``, or ``"None"``.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getRemoteRequirementsPopulateMode()
        """
        return str(self.call_com(lambda: self._com.getRemoteRequirementsPopulateMode()))

    def get_root_instance_specifications(self) -> IRPCollection:
        """Return root instance specifications in this package.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getRootInstanceSpecifications()
        """
        raise NotImplementedError("getRootInstanceSpecifications is not exposed in the Rhapsody COM automation type library.")

    def login_to_remote_artifact_server(self) -> None:
        """Log in to the remote artifact server for this package.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::loginToRemoteArtifactServer()
        """
        raise NotImplementedError("loginToRemoteArtifactServer is not exposed in the Rhapsody COM automation type library.")

    def populate_remote_requirements(self) -> None:
        """Populates remote requirements for this package.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::populateRemoteRequirements()
        """
        self.call_com(lambda: self._com.populateRemoteRequirements())

    def re_calculate_events_base_id(self) -> None:
        """Recalculates the events base ID for this package.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::reCalculateEventsBaseId()
        """
        self.call_com(lambda: self._com.reCalculateEventsBaseId())

    def set_remote_requirements_populate_mode(self, mode: str) -> None:
        """Sets which remote requirements should be loaded when opening the model.

        Args:
            mode: One of ``"All"``, ``"Linked"``, or ``"None"``.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::setRemoteRequirementsPopulateMode(java.lang.String populateMode)
        """
        self.call_com(lambda: self._com.setRemoteRequirementsPopulateMode(mode))

    def update_contained_diagrams_on_server(self, enforce_update: int) -> int:
        """Update the contained diagrams on the server.

        Args:
            enforce_update: ``0`` updates changed views only; ``1`` forces an update.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::updateContainedDiagramsOnServer(int enforceUpdate)
        """
        raise NotImplementedError("updateContainedDiagramsOnServer is not exposed in the Rhapsody COM automation type library.")

    # --- SysML Methods (Task 4) ---
    def add_implicit_object(self, name: str) -> IRPInstance:
        """Adds a new implicit object to the package.

        Args:
            name: The name of the new implicit object.

        Returns:
            The wrapped ``IRPInstance`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addImplicitObject(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance

        return cast(IRPInstance, self.wrap(self.call_com(lambda: self._com.addImplicitObject(name))))

    def add_link_between_sysml_ports(self, from_part: IRPInstance, to_part: IRPInstance, assoc: IRPRelation | None, from_port: IRPSysMLPort | None, to_port: IRPSysMLPort | None) -> IRPLink:
        """Creates a link between two objects using SysML flow ports or an association.

        Args:
            from_part: The source object.
            to_part: The target object.
            assoc: The association represented by the link, or ``None`` when ports are specified.
            from_port: The source flow port, or ``None`` when an association is specified.
            to_port: The target flow port, or ``None`` when an association is specified.

        Returns:
            The wrapped link created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addLinkBetweenSYSMLPorts(
                com.telelogic.rhapsody.core.IRPInstance fromPart,
                com.telelogic.rhapsody.core.IRPInstance toPart,
                com.telelogic.rhapsody.core.IRPRelation assoc,
                com.telelogic.rhapsody.core.IRPSysMLPort fromPort,
                com.telelogic.rhapsody.core.IRPSysMLPort toPort)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPLink

        assoc_com = assoc._com if assoc is not None else None
        from_port_com = from_port._com if from_port is not None else None
        to_port_com = to_port._com if to_port is not None else None
        return cast(IRPLink, self.wrap(self.call_com(lambda: self._com.addLinkBetweenSYSMLPorts(from_part._com, to_part._com, assoc_com, from_port_com, to_port_com))))

    # --- Misc Methods (Task 5) ---
    def get_all_nested_elements(self) -> IRPCollection:
        """Returns all nested elements in this package.

        Returns:
            An ``IRPCollection`` of nested elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getAllNestedElements()
        """
        return IRPCollection(self.call_com(lambda: self._com.getAllNestedElements()))

    @property
    def events_base_id(self) -> str:
        """Returns the events base ID for this package.

        Returns:
            The events base ID as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getEventsBaseId()
        """
        return str(self.get_com_property(self._com, "eventsBaseId"))

    def get_namespace(self) -> str:
        """Returns the namespace for this package.

        Returns:
            The namespace as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getNamespace()
        """
        return str(self.call_com(lambda: self._com.getNamespace()))

    @property
    def saved_in_seperate_directory(self) -> int:
        """Returns whether the package is saved in a separate directory.

        Returns:
            ``1`` if saved in separate directory, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getSavedInSeperateDirectory()
        """
        return int(self.get_com_property(self._com, "savedInSeperateDirectory"))

    @saved_in_seperate_directory.setter
    def saved_in_seperate_directory(self, value: int) -> None:
        """Sets whether the package is saved in a separate directory.

        Args:
            value: ``1`` to save in separate directory, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::setSavedInSeperateDirectory(int value)
        """
        self.set_com_property(self._com, "savedInSeperateDirectory", value)

    @property
    def user_defined_stereotypes(self) -> IRPCollection:
        """Returns all user-defined stereotypes in this package.

        Returns:
            An ``IRPCollection`` of stereotype elements.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getUserDefinedStereotypes()
        """
        return IRPCollection(self.get_com_property(self._com, "userDefinedStereotypes"))

    def update_contained_matrices_on_server(self, enforce_update: int) -> int:
        """Update the contained matrices on the server.

        Args:
            enforce_update: ``0`` updates changed views only; ``1`` forces an update.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::updateContainedMatricesOnServer(int enforceUpdate)
        """
        raise NotImplementedError("updateContainedMatricesOnServer is not exposed in the Rhapsody COM automation type library.")

    def update_contained_tables_on_server(self, enforce_update: int) -> int:
        """Update the contained tables on the server.

        Args:
            enforce_update: ``0`` updates changed views only; ``1`` forces an update.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::updateContainedTablesOnServer(int enforceUpdate)
        """
        raise NotImplementedError("updateContainedTablesOnServer is not exposed in the Rhapsody COM automation type library.")


IRPModelElement.register_wrapper("Package", IRPPackage)
