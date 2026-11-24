"""Wrappers for ``com.telelogic.rhapsody.core.IRPModelElement``.

Canonical module for :class:`IRPModelElement`; see the class requirement document at
``docs/requirements/com/telelogic/rhapsody/core/irp_model_element.md``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.core import ComHelper

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTag
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_association_class import IRPAssociationClass
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_dependency import IRPDependency
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagrams import IRPDiagram
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPLink
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_relation import IRPRelation
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_stereotype import IRPStereotype
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_templates import IRPTemplateInstantiation
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_unit import IRPUnit


class IRPModelElement(ComHelper):
    """Wraps ``IRPModelElement``: the base interface for all model elements.

    Python member names use snake_case. Catalog properties are Python
    attributes (for example, ``name`` and ``meta_class``); method-shaped COM
    members remain methods (for example, ``find_nested_element``). Internal
    COM calls preserve the camelCase API (``self._com.methodName(...)``).
    Bindings are pywin32-authoritative: every member calls exactly one
    pywin32-exposed COM member recorded in
    ``docs/reports/pywin32_authority.json`` — method-shaped members via
    ``call_com`` and property-shaped members via :meth:`get_com_property` /
    :meth:`set_com_property` — with no runtime name probing or Java-name
    fallback.
    """

    # IRPModelElement method parity checklist:
    # [x] add_association                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_dependency                   [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_dependency_between            [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_dependency_to                 [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_link_to_element                [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_new_aggr                      [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_property                     [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_redefines                    [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_remote_dependency_to           [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_specific_stereotype           [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_stereotype                   [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] become_template_instantiation_of   [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] change_to                        [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] clone                           [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] create_oslc_link                  [x] impl  [x] docstring  [x] unit test  [x] integration test  (not_implemented_error)
    # [x] delete_dependency                [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] delete_from_project               [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] delete_oslc_link                  [x] impl  [x] docstring  [x] unit test  [x] integration test  (not_implemented_error)
    # [x] error_message                    [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] find_elements_by_full_name          [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] find_nested_element               [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] find_nested_element_recursive      [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_all_tags                      [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_annotations                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_association_classes           [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_binary_id                     [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_constraints                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_constraints_by_him             [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_controlled_files              [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_decoration_style              [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_dependencies                 [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_description                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_description_html              [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_description_plain_text         [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_description_rtf               [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_display_name                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_display_name_rtf               [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_error_message                 [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_full_path_name                 [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_full_path_name_in               [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_guid                         [x] impl  [x] docstring  [x] unit test  [x] integration test   (already implemented)
    # [x] get_hyper_links                   [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_icon_file_name                 [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_interface_name                [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_is_external                   [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_is_of_meta_class                [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_is_show_display_name            [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_is_unresolved                 [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_local_tags                    [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_main_diagram                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_meta_class                    [x] impl  [x] docstring  [x] unit test  [x] integration test   (already implemented)
    # [x] get_name                         [x] impl  [x] docstring  [x] unit test  [x] integration test   (already implemented)
    # [x] get_nested_elements               [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_nested_elements_by_meta_class    [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_nested_elements_recursive      [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_new_term_stereotype            [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_of_template                   [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_overlay_icon_file_name          [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_overridden_properties         [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_overridden_properties_by_pattern [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_owned_dependencies            [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_owner                        [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_project                      [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_property_value                [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_property_value_conditional     [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_property_value_conditional_explicit [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_property_value_explicit        [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_redefines                    [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_references                   [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_remote_dependencies           [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_remote_uri                    [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_requirement_traceability_handle [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [!] get_rmm_url                       [x] impl (raises NotImplementedError) [x] docstring  [x] unit test  [x] integration test  (COM method not exposed)
    # [x] get_save_unit                     [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_stereotypes                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_tag                          [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_template_parameters           [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_ti                           [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_tool_tip_html                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_user_defined_meta_class         [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] has_nested_elements               [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] has_panel_widget                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] high_light_element                [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] is_a_template                     [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] is_description_rtf                [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] is_display_name_rtf                [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] is_modified                      [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] is_remote                        [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] locate_in_browser                 [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] open_features_dialog              [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] remove_property                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] remove_redefines                 [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] remove_stereotype                [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_decoration_style              [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_description                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_description_and_hyperlinks     [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_description_html              [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_description_rtf               [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_display_name                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_display_name_rtf               [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_guid                         [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_is_show_display_name            [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_main_diagram                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_name                         [x] impl  [x] docstring  [x] unit test  [x] integration test   (already implemented)
    # [x] set_of_template                   [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_owner                        [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_property_value                [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_requirement_traceability_handle [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_tag_context_value              [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_tag_element_value              [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_tag_value                     [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_ti                           [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] synchronize_template_instantiation [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [deprecated] get_stereotype          - skipped (use get_stereotypes)
    # [deprecated] set_stereotype          - skipped (use add_specific_stereotype / add_stereotype / remove_stereotype)
    # [deprecated] lock_on_design_manager    - skipped (Design Manager removed in Rhapsody 8.4)
    # [deprecated] unlock_on_design_manager  - skipped (Design Manager removed in Rhapsody 8.4)

    def __init__(self, com_obj: Any) -> None:
        self._com = com_obj

    @property
    def name(self) -> str:
        """Returns the name of the element.

        Returns:
            The element's name as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getName()
        """
        return str(ComHelper.get_com_property(self._com, "name"))

    @name.setter
    def name(self, name: str) -> None:
        """Sets the specified string as the name of the element.

        Args:
            name: The new name for the element.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setName(java.lang.String name)
        """
        ComHelper.set_com_property(self._com, "name", name)

    @property
    def meta_class(self) -> str:
        """Gets the name of the metaclass on which the model element is based.

        Returns:
            The metaclass name as a string (e.g. ``"Class"``, ``"Package"``).

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getMetaClass()
        """
        return str(ComHelper.get_com_property(self._com, "metaClass"))

    @property
    def guid(self) -> str:
        """Returns the GUID of the model element.

        Returns:
            The element's GUID as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getGUID()
        """
        return str(ComHelper.get_com_property(self._com, "GUID"))

    @guid.setter
    def guid(self, guid: str) -> None:
        """Sets a new GUID for the model element.

        Args:
            guid: The new GUID to set.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setGUID(java.lang.String gUID)
        """
        ComHelper.set_com_property(self._com, "GUID", guid)

    def add_association(self, end1: IRPRelation, end2: IRPRelation, name: str) -> IRPAssociationClass:
        """Creates an association class using the specified IRPRelation elements.

        Can only be called on elements that can contain association classes -
        packages and classes.

        Args:
            end1: The relation element at one end of the association.
            end2: The relation element at the second end of the association.
            name: The name to use for the new association class.

        Returns:
            The wrapped association class that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::addAssociation(com.telelogic.rhapsody.core.IRPRelation end1, com.telelogic.rhapsody.core.IRPRelation end2, java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_association_class import IRPAssociationClass

        association_class_com = self.call_com(lambda: self._com.addAssociation(end1._com, end2._com, name))
        return IRPAssociationClass(association_class_com)

    def add_dependency(self, depends_on_name: str, depends_on_type: str) -> IRPDependency:
        """Adds a dependency from the model element to the model element specified by the parameters.

        The method searches the model recursively until it finds an element
        that matches the name and metaclass specified. Since a model may
        contain multiple elements with the same name and type in different
        packages, prefer :meth:`add_dependency_to` when a specific element is
        available.

        Args:
            depends_on_name: The name of the model element on which this
                element depends.
            depends_on_type: The type (metaclass) of the model element on
                which this element depends.

        Returns:
            The wrapped dependency that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::addDependency(java.lang.String dependsOnName, java.lang.String dependsOnType)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_dependency import IRPDependency

        return cast(IRPDependency, ComHelper.wrap(ComHelper.call_com(lambda: self._com.addDependency(depends_on_name, depends_on_type))))

    def add_dependency_between(self, dependent: IRPModelElement, depends_on: IRPModelElement) -> IRPDependency:
        """Creates a dependency between the two specified elements.

        In most cases :meth:`add_dependency_to` should be used. This method is
        useful when creating a dependency between two read-only elements and
        assigning ownership of the dependency to a third model element.

        Args:
            dependent: The model element that is dependent on the other.
            depends_on: The model element that the first element depends upon.

        Returns:
            The wrapped dependency that was created.

        Raises:
            RhapsodyRuntimeException: If the dependency cannot be created.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::addDependencyBetween(com.telelogic.rhapsody.core.IRPModelElement dependent, com.telelogic.rhapsody.core.IRPModelElement dependsOn)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_dependency import IRPDependency

        return cast(IRPDependency, ComHelper.wrap(ComHelper.call_com(lambda: self._com.addDependencyBetween(dependent._com, depends_on._com))))

    def add_dependency_to(self, element: IRPModelElement) -> IRPDependency:
        """Adds a dependency upon another model element.

        Args:
            element: The model element that this element depends upon.

        Returns:
            The wrapped dependency that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::addDependencyTo(com.telelogic.rhapsody.core.IRPModelElement element)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_dependency import IRPDependency

        return cast(IRPDependency, ComHelper.wrap(ComHelper.call_com(lambda: self._com.addDependencyTo(element._com))))

    def add_link_to_element(self, to_element: IRPModelElement, assoc: IRPRelation, from_port: IRPModelElement | None, to_port: IRPModelElement | None) -> IRPLink:
        """Creates a link between this model element and the model element specified as an argument.

        In addition to the other element to connect, you must specify either
        the association that the link should represent, or the two ports to
        use for the link. Pass ``None`` for the association when specifying
        ports, and ``None`` for the ports when specifying an association.

        Args:
            to_element: The model element that the link should connect to.
            assoc: The association that the link should represent.
            from_port: The "from" port for the link.
            to_port: The "to" port for the link.

        Returns:
            The wrapped link that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::addLinkToElement(
                com.telelogic.rhapsody.core.IRPModelElement toElement,
                com.telelogic.rhapsody.core.IRPRelation assoc,
                com.telelogic.rhapsody.core.IRPModelElement fromPort,
                com.telelogic.rhapsody.core.IRPModelElement toPort)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPLink

        from_port_com = from_port._com if from_port is not None else None
        to_port_com = to_port._com if to_port is not None else None
        return cast(IRPLink, ComHelper.wrap(ComHelper.call_com(lambda: self._com.addLinkToElement(to_element._com, assoc._com, from_port_com, to_port_com))))

    def add_new_aggr(self, meta_type: str, name: str) -> IRPModelElement:
        """Adds a new model element to the current element, for example, adding a class to a package.

        Args:
            meta_type: The metaclass of the new element to create.
            name: The name of the new element.

        Returns:
            The wrapped model element that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::addNewAggr(java.lang.String metaType, java.lang.String name)
        """
        return cast(IRPModelElement, ComHelper.wrap(ComHelper.call_com(lambda: self._com.addNewAggr(meta_type, name))))

    def add_property(self, property_key: str, property_type: str, property_value: str) -> None:
        """Adds a new property to the model element and assigns a value to it.

        Args:
            property_key: The key (name) of the property to add.
            property_type: The type of the property.
            property_value: The value to assign to the property.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::addProperty(java.lang.String propertyKey, java.lang.String propertyType, java.lang.String propertyValue)
        """
        ComHelper.call_com(lambda: self._com.addProperty(property_key, property_type, property_value))

    def add_redefines(self, new_redefine: IRPModelElement) -> None:
        """Adds a redefine relationship to the model element.

        Args:
            new_redefine: The model element to redefine.

        Raises:
            RhapsodyRuntimeException: If the redefine relationship cannot be added.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::addRedefines(com.telelogic.rhapsody.core.IRPModelElement newRedefine)
        """
        ComHelper.call_com(lambda: self._com.addRedefines(new_redefine._com))

    def add_remote_dependency_to(self, element: IRPModelElement, link_type: str) -> IRPDependency:
        """For Design Manager projects, creates a dependency from a model element to a remote element.

        Args:
            element: The remote model element that this element depends upon.
            link_type: The type of link to create.

        Returns:
            The wrapped dependency that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::addRemoteDependencyTo(com.telelogic.rhapsody.core.IRPModelElement element, java.lang.String linkType)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_dependency import IRPDependency

        return cast(IRPDependency, ComHelper.wrap(ComHelper.call_com(lambda: self._com.addRemoteDependencyTo(element._com, link_type))))

    def add_specific_stereotype(self, stereotype: IRPStereotype) -> None:
        """Applies the specified stereotype to the model element.

        Args:
            stereotype: The wrapped stereotype to apply.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::addSpecificStereotype(com.telelogic.rhapsody.core.IRPStereotype stereotype)
        """
        ComHelper.call_com(lambda: self._com.addSpecificStereotype(stereotype._com))

    def add_stereotype(self, name: str, meta_type: str) -> IRPStereotype:
        """Applies the specified stereotype to the model element.

        If the project already contains a stereotype with the given name
        applicable to the given metaclass, that stereotype is applied. If the
        project does not yet contain such a stereotype, it is created in the
        package that owns this element and then applied.

        Args:
            name: The name of the stereotype to apply (or create and apply).
            meta_type: The metaclass to which the stereotype applies.

        Returns:
            The wrapped stereotype that was applied (or created and applied).

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::addStereotype(java.lang.String name, java.lang.String metaType)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_stereotype import IRPStereotype

        return cast(IRPStereotype, ComHelper.wrap(ComHelper.call_com(lambda: self._com.addStereotype(name, meta_type))))

    def become_template_instantiation_of(self, new_val: IRPModelElement) -> None:
        """Makes the current model element a template instantiation of the specified template.

        Args:
            new_val: The template to instantiate.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::becomeTemplateInstantiationOf(com.telelogic.rhapsody.core.IRPModelElement newVal)
        """
        ComHelper.call_com(lambda: self._com.becomeTemplateInstantiationOf(new_val._com))

    def change_to(self, meta_class: str) -> IRPModelElement:
        """Changes the model element to the type of element specified by the parameter provided.

        The original model element is destroyed by this operation, so the
        returned element must be captured in a variable; accessing the
        original element afterwards is unsafe.

        Args:
            meta_class: The metaclass to change this element into.

        Returns:
            The wrapped model element after the change.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::changeTo(java.lang.String metaClass)
        """
        return cast(IRPModelElement, ComHelper.wrap(ComHelper.call_com(lambda: self._com.changeTo(meta_class))))

    def clone(self, name: str, new_owner: IRPModelElement) -> IRPModelElement:
        """Clones a model element.

        Args:
            name: The name to use for the cloned element.
            new_owner: The model element that should own the clone.

        Returns:
            The wrapped clone that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::clone(java.lang.String name, com.telelogic.rhapsody.core.IRPModelElement newOwner)
        """
        return cast(IRPModelElement, ComHelper.wrap(ComHelper.call_com(lambda: self._com.clone(name, new_owner._com))))

    def create_oslc_link(self, type: str, purl: str) -> None:
        """Creates an OSLC link between the element and the element represented by the specified URL.

        Args:
            type: The type of OSLC link to create.
            purl: The URL of the target element.

        Raises:
            NotImplementedError: Rhapsody2.Application.1 does not expose
                createOSLCLink; the method is defined for Java API parity only.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::createOSLCLink(java.lang.String type, java.lang.String purl)
        """
        raise NotImplementedError("Rhapsody2.Application.1 does not expose createOSLCLink; method is defined for Java API parity only.")

    def delete_dependency(self, dependency: IRPDependency) -> None:
        """Deletes the specified dependency from the model.

        Args:
            dependency: The wrapped dependency to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::deleteDependency(com.telelogic.rhapsody.core.IRPDependency dependency)
        """
        ComHelper.call_com(lambda: self._com.deleteDependency(dependency._com))

    def delete_from_project(self) -> None:
        """Deletes the current model element from the model.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::deleteFromProject()
        """
        ComHelper.call_com(lambda: self._com.deleteFromProject())

    def delete_oslc_link(self, type: str, purl: str) -> None:
        """Deletes the specified OSLC link from the model.

        Args:
            type: The type of OSLC link to delete.
            purl: The URL of the target element.

        Raises:
            NotImplementedError: Rhapsody2.Application.1 does not expose
                deleteOSLCLink; the method is defined for Java API parity only.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::deleteOSLCLink(java.lang.String type, java.lang.String purl)
        """
        raise NotImplementedError("Rhapsody2.Application.1 does not expose deleteOSLCLink; method is defined for Java API parity only.")

    def error_message(self) -> str:
        """Returns the error message for the last method called.

        If the last method completed successfully, an empty string is returned,
        so this must be called immediately after the method it concerns.

        Returns:
            The error message as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::errorMessage()
        """
        return str(ComHelper.call_com(lambda: self._com.errorMessage()))

    def find_elements_by_full_name(self, name: str, meta_class: str) -> IRPModelElement | None:
        """Searches for the specified model element in the specified path under the current model element.

        Args:
            name: The full path name of the element to find.
            meta_class: The metaclass of the element to find.

        Returns:
            The wrapped matching model element, or None if not found.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::findElementsByFullName(java.lang.String name, java.lang.String metaClass)
        """
        return ComHelper.wrap(ComHelper.call_com(lambda: self._com.findElementsByFullName(name, meta_class)))

    def find_nested_element(self, name: str, meta_class: str) -> IRPModelElement | None:
        """Searches for the specified model element.

        Only the first level of nesting below the current element is searched;
        use :meth:`find_nested_element_recursive` to search all levels.

        Args:
            name: The name of the element to find.
            meta_class: The metaclass of the element to find.

        Returns:
            The wrapped matching model element, or None if not found.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::findNestedElement(java.lang.String name, java.lang.String metaClass)
        """
        return ComHelper.wrap(ComHelper.call_com(lambda: self._com.findNestedElement(name, meta_class)))

    def find_nested_element_recursive(self, name: str, meta_class: str) -> IRPModelElement | None:
        """Searches recursively for the specified model element.

        All levels of nesting below the current element are searched; use
        :meth:`find_nested_element` to search only the first level.

        Args:
            name: The name of the element to find.
            meta_class: The metaclass of the element to find.

        Returns:
            The wrapped matching model element, or None if not found.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::findNestedElementRecursive(java.lang.String name, java.lang.String metaClass)
        """
        return ComHelper.wrap(ComHelper.call_com(lambda: self._com.findNestedElementRecursive(name, meta_class)))

    @property
    def all_tags(self) -> IRPCollection:
        """Returns a collection of all the element's tags.

        Returns:
            An ``IRPCollection`` of the element's tags.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getAllTags()
        """
        return IRPCollection(ComHelper.get_com_property(self._com, "allTags"))

    @property
    def annotations(self) -> IRPCollection:
        """Returns all of the element's annotations.

        Annotations include comments, constraints, and requirements.

        Returns:
            An ``IRPCollection`` of the element's annotations.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getAnnotations()
        """
        return IRPCollection(ComHelper.get_com_property(self._com, "annotations"))

    @property
    def association_classes(self) -> IRPCollection:
        """Returns a collection of all the association classes directly beneath this model element.

        Returns:
            An ``IRPCollection`` of association classes.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getAssociationClasses()
        """
        return IRPCollection(ComHelper.get_com_property(self._com, "associationClasses"))

    @property
    def binary_id(self) -> bytes:
        """Returns the GUID of the model element as an array of bytes.

        As opposed to :attr:`guid`, which returns the GUID as a string.

        Returns:
            The element's GUID as bytes.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getBinaryID()
        """
        return bytes(ComHelper.get_com_property(self._com, "BinaryID"))

    @property
    def constraints(self) -> IRPCollection:
        """Returns all of the element's constraints.

        Returns:
            An ``IRPCollection`` of the element's constraints.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getConstraints()
        """
        return IRPCollection(ComHelper.get_com_property(self._com, "constraints"))

    @property
    def constraints_by_him(self) -> IRPCollection:
        """Returns all of the element's constraints (for internal use only).

        This getter is intentionally unavailable because the Java API documents
        it as internal-only and no supported live retrieval setup is known.

        Raises:
            NotImplementedError: Always raised because the runtime behavior is unsupported.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getConstraintsByHim()
        """
        raise NotImplementedError("constraints_by_him is unsupported because its Java API is internal-only")

    @property
    def controlled_files(self) -> IRPCollection:
        """Returns a collection of all the element's controlled files.

        Returns:
            An ``IRPCollection`` of controlled files.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getControlledFiles()
        """
        return IRPCollection(ComHelper.get_com_property(self._com, "controlledFiles"))

    def get_decoration_style(self) -> str:
        """Returns the name of the decoration style currently associated with the model element.

        Returns:
            The decoration style name as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getDecorationStyle()
        """
        return str(ComHelper.call_com(lambda: self._com.getDecorationStyle()))

    @property
    def dependencies(self) -> IRPCollection:
        """Returns all of the element's dependencies.

        Returns:
            An ``IRPCollection`` of the element's dependencies.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getDependencies()
        """
        return IRPCollection(ComHelper.get_com_property(self._com, "dependencies"))

    @property
    def description(self) -> str:
        """Returns the description defined for the element.

        Returns:
            The element's description as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getDescription()
        """
        return str(ComHelper.get_com_property(self._com, "description"))

    @description.setter
    def description(self, description: str) -> None:
        """Sets the specified string as the description of the element.

        Args:
            description: The description text to set.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setDescription(java.lang.String description)
        """
        ComHelper.set_com_property(self._com, "description", description)

    @property
    def description_html(self) -> str:
        """Returns HTML representation of the element description.

        Returns:
            The element's description as an HTML string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getDescriptionHTML()
        """
        return str(ComHelper.get_com_property(self._com, "descriptionHTML"))

    @property
    def description_plain_text(self) -> str:
        """Returns the description defined for the element in plain text format.

        Returns:
            The element's description as plain text.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getDescriptionPlainText()
        """
        return str(ComHelper.get_com_property(self._com, "descriptionPlainText"))

    @property
    def description_rtf(self) -> str:
        """Returns the description defined for the element in RTF format.

        Returns:
            The element's description as an RTF string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getDescriptionRTF()
        """
        return str(ComHelper.get_com_property(self._com, "descriptionRTF"))

    @description_rtf.setter
    def description_rtf(self, description_rtf: str) -> None:
        """Specifies the RTF string to use for the description of the model element.

        Args:
            description_rtf: The RTF description to set.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setDescriptionRTF(java.lang.String descriptionRTF)
        """
        ComHelper.set_com_property(self._com, "descriptionRTF", description_rtf)

    @property
    def display_name(self) -> str:
        """Returns the label of the model element.

        Returns:
            The element's display label as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getDisplayName()
        """
        return str(ComHelper.get_com_property(self._com, "displayName"))

    @display_name.setter
    def display_name(self, display_name: str) -> None:
        """Specifies the text to use for the label of the model element.

        Args:
            display_name: The label text to set.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setDisplayName(java.lang.String displayName)
        """
        ComHelper.set_com_property(self._com, "displayName", display_name)

    def get_display_name_rtf(self) -> str:
        """Returns the label of the model element as an RTF string.

        Returns:
            The element's display label as an RTF string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getDisplayNameRTF()
        """
        return str(ComHelper.call_com(lambda: self._com.getDisplayNameRTF()))

    def get_error_message(self, _midl__irp_model_element0002_: str) -> str:
        """Returns the error message for the last method called.

        If the last method completed successfully, an empty string is returned,
        so this must be called immediately after the method it concerns. The
        string argument is a pywin32 MIDL output buffer required by the COM signature.

        Args:
            _midl__irp_model_element0002_: The string buffer required by pywin32.

        Returns:
            The error message as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getErrorMessage()
        """
        return str(ComHelper.call_com(lambda: self._com.getErrorMessage(_midl__irp_model_element0002_)))

    def get_full_path_name(self) -> str:
        """Returns the full path name of the model element.

        The returned string uses the format ``package::subpackage::class``.

        Returns:
            The element's full path name as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getFullPathName()
        """
        return str(ComHelper.call_com(lambda: self._com.getFullPathName()))

    def get_full_path_name_in(self) -> str:
        """Retrieves the full path name of the element as ``(class) in (package)``.

        Returns:
            The element's full path name as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getFullPathNameIn()
        """
        return str(ComHelper.call_com(lambda: self._com.getFullPathNameIn()))

    @property
    def hyper_links(self) -> IRPCollection:
        """Returns a collection of all the hyperlinks associated with the element.

        Runtime retrieval is intentionally unavailable because the documented
        live setup APIs have not produced a retrievable hyperlink.

        Raises:
            NotImplementedError: Always raised because live retrieval is unsupported.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getHyperLinks()
        """
        raise NotImplementedError("hyper_links is unsupported because live retrieval could not be established")

    def get_icon_file_name(self) -> str:
        """Returns the full path of the graphic file used to represent elements of this type in the browser.

        Returns:
            The icon file path as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getIconFileName()
        """
        return str(ComHelper.call_com(lambda: self._com.getIconFileName()))

    @property
    def interface_name(self) -> str:
        """Returns the name of the API interface corresponding to the current element.

        For example, ``"IRPClass"`` for a class element, ``"IRPOperation"``
        for an operation element.

        Returns:
            The API interface name as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getInterfaceName()
        """
        return str(ComHelper.get_com_property(self._com, "interfaceName"))

    @property
    def is_external(self) -> int:
        """Checks whether the element is an "external" element.

        Corresponds to the value of the property ``UseAsExternal``.

        Returns:
            ``1`` if the element is external, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getIsExternal()
        """
        return int(ComHelper.get_com_property(self._com, "isExternal"))

    def get_is_of_meta_class(self, meta_class: str) -> int:
        """Indicates whether the model element is based on the metaclass provided as a parameter.

        Args:
            meta_class: The metaclass name to check against.

        Returns:
            ``1`` if the element is based on the metaclass, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getIsOfMetaClass(java.lang.String metaClass)
        """
        return int(ComHelper.call_com(lambda: self._com.isOfMetaClass(meta_class)))

    @property
    def is_show_display_name(self) -> int:
        """Checks whether the model element is configured to display its label instead of its name in diagrams.

        Returns:
            ``1`` if the label is shown, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getIsShowDisplayName()
        """
        return int(ComHelper.get_com_property(self._com, "isShowDisplayName"))

    @is_show_display_name.setter
    def is_show_display_name(self, is_show_display_name: int) -> None:
        """Specifies whether the element label is shown in diagrams.

        Args:
            is_show_display_name: ``1`` to show the label, ``0`` to show the name.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setIsShowDisplayName(int isShowDisplayName)
        """
        ComHelper.set_com_property(self._com, "isShowDisplayName", is_show_display_name)

    @property
    def is_unresolved(self) -> int:
        """Checks if the element is an element that can't be resolved by Rhapsody.

        Returns:
            ``1`` if the element is unresolved, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getIsUnresolved()
        """
        return int(ComHelper.get_com_property(self._com, "isUnresolved"))

    @property
    def local_tags(self) -> IRPCollection:
        """Returns a collection of the tags that were created locally for this model element.

        Returns:
            An ``IRPCollection`` of locally created tags.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getLocalTags()
        """
        return IRPCollection(ComHelper.get_com_property(self._com, "localTags"))

    @property
    def main_diagram(self) -> IRPDiagram:
        """Returns the "main" diagram for the element.

        This operation is valid only for packages, classes, actors, use
        cases, objects, and interfaces.

        Returns:
            The wrapped main diagram.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getMainDiagram()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagrams import IRPDiagram

        return cast(IRPDiagram, ComHelper.wrap(ComHelper.get_com_property(self._com, "mainDiagram")))

    @main_diagram.setter
    def main_diagram(self, main_diagram: IRPDiagram) -> None:
        """Specifies the main diagram for packages, classes, actors, use cases, objects, and interfaces.

        Args:
            main_diagram: The wrapped diagram to set as the main diagram.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setMainDiagram(com.telelogic.rhapsody.core.IRPDiagram mainDiagram)
        """
        ComHelper.set_com_property(self._com, "mainDiagram", main_diagram._com)

    def get_nested_elements(self) -> IRPCollection:
        """Gets a collection of all the model elements that are directly under the current element.

        Note that when called on a package, the returned collection does not
        include functions, global variables, or global objects, because these
        are contained in a class called ``TopLevel``. Use the ``IRPPackage``
        methods ``getGlobalFunctions``, ``getGlobalVariables``, and
        ``getGlobalObjects`` to retrieve them.

        Returns:
            An ``IRPCollection`` of nested model elements.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getNestedElements()
        """
        return IRPCollection(ComHelper.call_com(lambda: self._com.getNestedElements()))

    def get_nested_elements_by_meta_class(self, meta_class: str, recursive: int) -> IRPCollection:
        """Retrieves all of the model elements of the specified type below the current element.

        Args:
            meta_class: The metaclass of the elements to retrieve.
            recursive: ``1`` to search recursively, ``0`` for direct children only.

        Returns:
            An ``IRPCollection`` of matching nested elements.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getNestedElementsByMetaClass(java.lang.String metaClass, int recursive)
        """
        return IRPCollection(ComHelper.call_com(lambda: self._com.getNestedElementsByMetaClass(meta_class, recursive)))

    def get_nested_elements_recursive(self) -> IRPCollection:
        """Returns a collection that consists of the current element and all of the model elements below it.

        Returns:
            An ``IRPCollection`` of this element and all nested elements.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getNestedElementsRecursive()
        """
        return IRPCollection(ComHelper.call_com(lambda: self._com.getNestedElementsRecursive()))

    def get_new_term_stereotype(self) -> IRPStereotype:
        """If a "new term" stereotype has been applied to the element, returns the stereotype.

        Returns:
            The wrapped "new term" stereotype.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getNewTermStereotype()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_stereotype import IRPStereotype

        return cast(IRPStereotype, ComHelper.wrap(ComHelper.call_com(lambda: self._com.getNewTermStereotype())))

    @property
    def of_template(self) -> IRPModelElement:
        """If the element is an instantiation of a template, returns the template that it instantiates.

        Returns:
            The wrapped template that this element instantiates.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getOfTemplate()
        """
        return cast(IRPModelElement, ComHelper.wrap(ComHelper.get_com_property(self._com, "ofTemplate")))

    @of_template.setter
    def of_template(self, of_template: IRPModelElement) -> None:
        """Makes the current model element a template instantiation of the specified template.

        Args:
            of_template: The wrapped template to instantiate.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setOfTemplate(com.telelogic.rhapsody.core.IRPModelElement ofTemplate)
        """
        ComHelper.set_com_property(self._com, "ofTemplate", of_template._com)

    def get_overlay_icon_file_name(self) -> str:
        """Returns the full path of the graphic file used as an overlay on this specific model element.

        The overlay is drawn on top of the regular icon that represents
        elements of this type in the browser.

        Returns:
            The overlay icon file path as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getOverlayIconFileName()
        """
        return str(ComHelper.call_com(lambda: self._com.getOverlayIconFileName()))

    def get_overridden_properties(self, recursive: int) -> IRPCollection:
        """Returns a collection of all the properties whose value was overridden for this model element.

        Args:
            recursive: ``1`` to include overridden properties of nested
                elements, ``0`` for this element only.

        Returns:
            An ``IRPCollection`` of overridden properties.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getOverriddenProperties(int recursive)
        """
        return IRPCollection(ComHelper.call_com(lambda: self._com.getOverriddenProperties(recursive)))

    def get_overridden_properties_by_pattern(self, pattern: str, localy_overriden_only: int, with_default_values: int) -> IRPCollection:
        """Returns the overridden properties matching the specified pattern.

        Args:
            pattern: The pattern to match property keys against.
            localy_overriden_only: ``1`` to return only locally overridden
                properties, ``0`` otherwise.
            with_default_values: ``1`` to include default values, ``0`` otherwise.

        Returns:
            An ``IRPCollection`` of matching overridden properties.

        Raises:
            RhapsodyRuntimeException: if the pattern is invalid or the
                overridden properties cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getOverriddenPropertiesByPattern(java.lang.String pattern, int localyOverridenOnly, int withDefaultValues)
        """
        return IRPCollection(ComHelper.call_com(lambda: self._com.getOverriddenPropertiesByPattern(pattern, localy_overriden_only, with_default_values)))

    def get_owned_dependencies(self) -> IRPCollection:
        """Returns all of the dependencies that are owned by the element.

        Returns:
            An ``IRPCollection`` of owned dependencies.

        Raises:
            RhapsodyRuntimeException: if the owned dependencies cannot be
                retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getOwnedDependencies()
        """
        return IRPCollection(ComHelper.call_com(lambda: self._com.getOwnedDependencies()))

    @property
    def owner(self) -> IRPModelElement:
        """Returns the model element that owns this model element.

        Returns:
            The wrapped owner element.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getOwner()
        """
        return cast(IRPModelElement, ComHelper.wrap(ComHelper.get_com_property(self._com, "owner")))

    @owner.setter
    def owner(self, owner: IRPModelElement) -> None:
        """Specifies the model element that should own this element.

        Args:
            owner: The wrapped owner element.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setOwner(com.telelogic.rhapsody.core.IRPModelElement owner)
        """
        ComHelper.set_com_property(self._com, "owner", owner._com)

    @property
    def project(self) -> IRPProject:
        """Returns the project that the current element belongs to.

        Returns:
            The wrapped project element.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getProject()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject

        return cast(IRPProject, ComHelper.wrap(ComHelper.get_com_property(self._com, "project")))

    def get_property_value(self, property_key: str) -> str:
        """Returns the value of the specified property for the model element.

        The property key uses the syntax ``Subject.Metaclass.Property``
        (for example, ``CG.Class.ActiveThreadName``). If no value has been set
        specifically for this element, the default value propagated from a
        higher level is returned.

        Args:
            property_key: The key (name) of the property.

        Returns:
            The property value as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getPropertyValue(java.lang.String propertyKey)
        """
        return str(ComHelper.call_com(lambda: self._com.getPropertyValue(property_key)))

    def get_property_value_conditional(self, property_key: str, formal_key: IRPCollection, actual_values: IRPCollection) -> str:
        """Returns the value of the specified property, taking into account the tokens and token values specified.

        The property key uses the syntax ``Subject.Metaclass.Property``. For
        details on using tokens in property values, see "Conditional
        Properties" in the Rhapsody help.

        Args:
            property_key: The key (name) of the property.
            formal_key: A collection of formal tokens.
            actual_values: A collection of token values.

        Returns:
            The property value as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getPropertyValueConditional(
                java.lang.String propertyKey,
                com.telelogic.rhapsody.core.IRPCollection formalKey,
                com.telelogic.rhapsody.core.IRPCollection actualValues)
        """
        return str(ComHelper.call_com(lambda: self._com.getPropertyValueConditional(property_key, formal_key._com, actual_values._com)))

    def get_property_value_conditional_explicit(self, property_key: str, formal_key: IRPCollection, actual_values: IRPCollection) -> str:
        """Returns the property value if overridden, taking into account the tokens and token values specified.

        Unlike :meth:`get_property_value_conditional`, this returns only the value
        that was explicitly set for the model element; if no explicit value
        exists, the default value is not returned.

        Args:
            property_key: The key (name) of the property.
            formal_key: A collection of formal tokens.
            actual_values: A collection of token values.

        Returns:
            The explicitly-set property value as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getPropertyValueConditionalExplicit(
                java.lang.String propertyKey,
                com.telelogic.rhapsody.core.IRPCollection formalKey,
                com.telelogic.rhapsody.core.IRPCollection actualValues)
        """
        return str(ComHelper.call_com(lambda: self._com.getPropertyValueConditionalExplicit(property_key, formal_key._com, actual_values._com)))

    def get_property_value_explicit(self, property_key: str) -> str:
        """Returns the value of the specified property if the default value was overridden.

        Unlike :meth:`get_property_value`, this returns only the value that was
        explicitly set for the model element; if no explicit value exists, the
        default value is not returned.

        Args:
            property_key: The key (name) of the property.

        Returns:
            The explicitly-set property value as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getPropertyValueExplicit(java.lang.String propertyKey)
        """
        return str(ComHelper.call_com(lambda: self._com.getPropertyValueExplicit(property_key)))

    def get_redefines(self) -> IRPCollection:
        """Returns the redefine relationships of the model element.

        Returns:
            An ``IRPCollection`` of redefine relationships.

        Raises:
            RhapsodyRuntimeException: if the redefine relationships cannot be
                retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getRedefines()
        """
        return IRPCollection(ComHelper.call_com(lambda: self._com.getRedefines()))

    @property
    def references(self) -> IRPCollection:
        """Returns a collection of all the model elements that point to this model element.

        Returns:
            An ``IRPCollection`` of referencing elements.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getReferences()
        """
        return IRPCollection(ComHelper.get_com_property(self._com, "references"))

    def get_remote_dependencies(self) -> IRPCollection:
        """For Rhapsody Model Manager projects, returns the dependencies on remote artifacts.

        Returns:
            An ``IRPCollection`` of remote dependencies.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getRemoteDependencies()
        """
        return IRPCollection(ComHelper.call_com(lambda: self._com.getRemoteDependencies()))

    def get_remote_uri(self) -> str:
        """For elements that are remote resources, returns the URI of the resource.

        If called on an element that is not a remote resource, an empty string
        is returned.

        Returns:
            The remote URI as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getRemoteURI()
        """
        return str(ComHelper.call_com(lambda: self._com.getRemoteURI()))

    @property
    def requirement_traceability_handle(self) -> int:
        """Returns the ID used by DOORS to refer to this requirement.

        Returns:
            The DOORS traceability handle as an int.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getRequirementTraceabilityHandle()
        """
        return int(ComHelper.get_com_property(self._com, "requirementTraceabilityHandle"))

    @requirement_traceability_handle.setter
    def requirement_traceability_handle(self, requirement_traceability_handle: int) -> None:
        """Sets a new DOORS traceability handle for the requirement.

        Args:
            requirement_traceability_handle: The new DOORS traceability handle.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setRequirementTraceabilityHandle(int requirementTraceabilityHandle)
        """
        ComHelper.set_com_property(self._com, "requirementTraceabilityHandle", requirement_traceability_handle)

    def get_rmm_url(self) -> str:
        """Return the Rhapsody Model Manager URL for the model element.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getRmmUrl()
        """
        raise NotImplementedError("getRmmUrl is not exposed in the Rhapsody COM automation type library.")

    def get_save_unit(self) -> IRPUnit:
        """Returns the unit that the model element is saved in.

        Returns:
            The wrapped save unit.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getSaveUnit()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_unit import IRPUnit

        return cast(IRPUnit, ComHelper.wrap(ComHelper.call_com(lambda: self._com.getSaveUnit())))

    @property
    def stereotype(self) -> IRPStereotype | None:
        """Returns or sets the deprecated single stereotype on this element.

        The Java API deprecated this member in favor of :attr:`stereotypes` and
        :meth:`add_specific_stereotype`.

        Returns:
            The applied single stereotype, or ``None`` if no stereotype is set.
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_stereotype import IRPStereotype

        raw_stereotype = ComHelper.get_com_property(self._com, "stereotype")
        if raw_stereotype is None:
            return None
        return cast(IRPStereotype, ComHelper.wrap(raw_stereotype))

    @stereotype.setter
    def stereotype(self, stereotype: IRPStereotype) -> None:
        ComHelper.set_com_property(self._com, "stereotype", stereotype._com)

    @property
    def stereotypes(self) -> IRPCollection:
        """Returns a collection of the stereotypes that have been applied to the element.

        Returns:
            An ``IRPCollection`` of applied stereotypes.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getStereotypes()
        """
        return IRPCollection(ComHelper.get_com_property(self._com, "stereotypes"))

    def get_tag(self, name: str) -> IRPTag:
        """Returns the tag specified.

        This method can be used for both local tags and global tags.

        Args:
            name: The name of the tag to return.

        Returns:
            The wrapped tag.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getTag(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTag

        return cast(IRPTag, ComHelper.wrap(ComHelper.call_com(lambda: self._com.getTag(name))))

    @property
    def template_parameters(self) -> IRPCollection:
        """For model elements that are templates, returns the template parameters.

        Returns:
            An ``IRPCollection`` of template parameters.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getTemplateParameters()
        """
        return IRPCollection(ComHelper.get_com_property(self._com, "templateParameters"))

    @property
    def ti(self) -> IRPTemplateInstantiation:
        """For template instantiations, returns an object containing the template instantiation parameters.

        Returns:
            The wrapped template instantiation.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getTi()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_templates import IRPTemplateInstantiation

        return cast(IRPTemplateInstantiation, ComHelper.wrap(ComHelper.get_com_property(self._com, "ti")))

    @ti.setter
    def ti(self, ti: IRPTemplateInstantiation) -> None:
        """Sets the template instantiation for the model element.

        Args:
            ti: The wrapped template instantiation to set.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setTi(com.telelogic.rhapsody.core.IRPTemplateInstantiation ti)
        """
        ComHelper.set_com_property(self._com, "ti", ti._com)

    def get_tool_tip_html(self) -> str:
        """Returns the HTML that would be used to display the tooltip for the element in the user interface.

        Returns:
            The tooltip HTML as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getToolTipHTML()
        """
        return str(ComHelper.call_com(lambda: self._com.getToolTipHTML()))

    @property
    def user_defined_meta_class(self) -> str:
        """Gets the name of the New Term on which the model element is based.

        To get the name of the metaclass on which the New Term is based, use
        :attr:`meta_class`.

        Returns:
            The user-defined metaclass name as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::getUserDefinedMetaClass()
        """
        return str(ComHelper.get_com_property(self._com, "userDefinedMetaClass"))

    def has_nested_elements(self) -> int:
        """Checks whether the model element contains other elements.

        Returns:
            ``1`` if the element contains nested elements, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::hasNestedElements()
        """
        return int(ComHelper.call_com(lambda: self._com.hasNestedElements()))

    def has_panel_widget(self) -> int:
        """Checks whether the model element is bound to a panel diagram widget.

        Returns:
            ``1`` if bound to a panel widget, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::hasPanelWidget()
        """
        return int(ComHelper.call_com(lambda: self._com.hasPanelWidget()))

    def high_light_element(self) -> None:
        """Locates the element in the Rhapsody browser, and highlights it in the diagram where it appears.

        The element is highlighted in the diagram only if it is the kind of
        element that can appear in only one diagram, for example a state.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::highLightElement()
        """
        ComHelper.call_com(lambda: self._com.highLightElement())

    def is_a_template(self) -> int:
        """Checks whether the model element is a template.

        Returns:
            ``1`` if the element is a template, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::isATemplate()
        """
        return int(ComHelper.call_com(lambda: self._com.isATemplate()))

    def is_description_rtf(self) -> int:
        """Checks whether the description for the element is in RTF format.

        Returns:
            ``1`` if the description is RTF, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::isDescriptionRTF()
        """
        return int(ComHelper.call_com(lambda: self._com.isDescriptionRTF()))

    def is_display_name_rtf(self) -> int:
        """Checks whether the label of the element is in RTF format.

        Returns:
            ``1`` if the label is RTF, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::isDisplayNameRTF()
        """
        return int(ComHelper.call_com(lambda: self._com.isDisplayNameRTF()))

    def is_modified(self) -> int:
        """Checks if the element was modified since the model was last saved.

        Returns:
            ``1`` if the element was modified, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::isModified()
        """
        return int(ComHelper.call_com(lambda: self._com.isModified()))

    def is_remote(self) -> int:
        """Checks whether the model element is a remote resource such as a DOORS/DOORS Next requirement.

        Returns:
            ``1`` if the element is remote, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::isRemote()
        """
        return int(ComHelper.call_com(lambda: self._com.isRemote()))

    def locate_in_browser(self) -> int:
        """Locates the model element in the Rhapsody browser.

        Returns:
            ``1`` if the element was located, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::locateInBrowser()
        """
        return int(ComHelper.call_com(lambda: self._com.locateInBrowser()))

    def open_features_dialog(self, new_dialog: int) -> None:
        """Displays the information for the element in the Features window.

        Depending on ``new_dialog``, opens a new Features window or uses an
        already-open one.

        Args:
            new_dialog: ``1`` to open in a new dialog, ``0`` to use an existing
                window (or a new one if none is open).

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::openFeaturesDialog(int newDialog)
        """
        ComHelper.call_com(lambda: self._com.openFeaturesDialog(new_dialog))

    def remove_property(self, property_key: str) -> None:
        """Removes the value that was set for the specified property.

        This is equivalent to the "un-override" option in the Features window.
        The property key uses the syntax ``Subject.Metaclass.Property``.

        Args:
            property_key: The key (name) of the property to remove.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::removeProperty(java.lang.String propertyKey)
        """
        ComHelper.call_com(lambda: self._com.removeProperty(property_key))

    def remove_redefines(self, removed_redefine: IRPModelElement) -> None:
        """Removes a redefine relationship from the model element.

        Args:
            removed_redefine: The redefine relationship to remove.

        Raises:
            RhapsodyRuntimeException: if the redefine relationship cannot be
                removed.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::removeRedefines(com.telelogic.rhapsody.core.IRPModelElement removedRedefine)
        """
        ComHelper.call_com(lambda: self._com.removeRedefines(removed_redefine._com))

    def remove_stereotype(self, stereotype: IRPStereotype) -> None:
        """Removes the specified stereotype from the element.

        Args:
            stereotype: The wrapped stereotype to remove.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::removeStereotype(com.telelogic.rhapsody.core.IRPStereotype stereotype)
        """
        ComHelper.call_com(lambda: self._com.removeStereotype(stereotype._com))

    def set_decoration_style(self, new_val: str) -> None:
        """Specifies the decoration style that should now be associated with the model element.

        The value must be one of the strings defined by the
        ``Format::Decoration::StyleNames`` property.

        Args:
            new_val: The decoration style name to associate.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setDecorationStyle(java.lang.String newVal)
        """
        ComHelper.call_com(lambda: self._com.setDecorationStyle(new_val))

    def set_description_and_hyperlinks(self, rtf_text: str, targets: IRPCollection) -> None:
        """Specifies an RTF description for the element and a collection of elements to hyperlink.

        Args:
            rtf_text: The RTF string to use as the description (must be RTF).
            targets: A collection of elements to which hyperlinks should be created.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setDescriptionAndHyperlinks(java.lang.String rtfText, com.telelogic.rhapsody.core.IRPCollection targets)
        """
        ComHelper.call_com(lambda: self._com.setDescriptionAndHyperlinks(rtf_text, targets._com))

    def set_description_html(self, description_html: str) -> None:
        """Sets the HTML representation of the element description.

        Note: The Java API documents this method as "Not implemented - should not be used."
        This method raises NotImplementedError to prevent its use.

        Args:
            description_html: The HTML description to set.

        Raises:
            NotImplementedError: Always raised, as this method is not implemented in Rhapsody.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setDescriptionHTML(java.lang.String descriptionHTML)
        """
        raise NotImplementedError("setDescriptionHTML is documented as 'Not implemented - should not be used' in the Rhapsody Java API. This method is not available in the COM automation interface.")

    def set_display_name_rtf(self, new_val: str) -> None:
        """Specifies the RTF string to use for the label of the model element.

        Args:
            new_val: The RTF label text to set.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setDisplayNameRTF(java.lang.String newVal)
        """
        ComHelper.call_com(lambda: self._com.setDisplayNameRTF(new_val))

    def set_property_value(self, property_key: str, property_value: str) -> None:
        """Sets the value of a property for the model element.

        The property key uses the syntax ``Subject.Metaclass.Property`` (for
        example, ``CG.Class.ActiveThreadName``). For boolean properties, use
        ``"True"`` or ``"False"``.

        Args:
            property_key: The key (name) of the property.
            property_value: The value to assign to the property.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setPropertyValue(java.lang.String propertyKey, java.lang.String propertyValue)
        """
        ComHelper.call_com(lambda: self._com.setPropertyValue(property_key, property_value))

    def set_tag_context_value(self, tag: IRPTag, elements: IRPCollection, multiplicities: IRPCollection) -> IRPTag:
        """Applies the specified tag and sets its value to a specific instance of another model element.

        ``elements`` is a collection of model elements representing the full
        path to the target element (used to set the value to its full path);
        it must contain ``IRPModelElement`` objects. ``multiplicities`` is a
        collection of the relevant indices for each element in ``elements``
        (as strings), allowing the value to point to a specific instance when
        multiplicity is greater than one.

        Args:
            tag: The wrapped tag to apply.
            elements: A collection of model elements forming the target path.
            multiplicities: A collection of multiplicities (indices) as strings.

        Returns:
            The wrapped tag that was set.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setTagContextValue(
                com.telelogic.rhapsody.core.IRPTag tag,
                com.telelogic.rhapsody.core.IRPCollection elements,
                com.telelogic.rhapsody.core.IRPCollection multiplicities)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTag

        return cast(IRPTag, ComHelper.wrap(ComHelper.call_com(lambda: self._com.setTagContextValue(tag._com, elements._com, multiplicities._com))))

    def set_tag_element_value(self, tag: IRPTag, val: IRPModelElement) -> IRPTag:
        """Applies a tag whose type is a model element to the current element with the value specified.

        If the tag has already been applied, this method can be used to modify
        its value.

        Args:
            tag: The wrapped tag to apply.
            val: The wrapped model element value.

        Returns:
            The wrapped tag that was set.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setTagElementValue(com.telelogic.rhapsody.core.IRPTag tag, com.telelogic.rhapsody.core.IRPModelElement val)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTag

        return cast(IRPTag, ComHelper.wrap(ComHelper.call_com(lambda: self._com.setTagElementValue(tag._com, val._com))))

    def set_tag_value(self, tag: IRPTag, val: str) -> IRPTag:
        """Applies the specified tag to the model element with the value specified.

        If the tag has already been applied, this method can be used to modify
        its value.

        Args:
            tag: The wrapped tag to apply.
            val: The value to assign to the tag.

        Returns:
            The wrapped tag that was set.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::setTagValue(com.telelogic.rhapsody.core.IRPTag tag, java.lang.String val)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTag

        return cast(IRPTag, ComHelper.wrap(ComHelper.call_com(lambda: self._com.setTagValue(tag._com, val))))

    def synchronize_template_instantiation(self) -> None:
        """Updates the instantiation to match changes made to its template.

        After changes are made to a template, this method can be called on
        each instantiation of the template in order to update the
        instantiation to match the changes that were made to the template.

        Reference:
            com.telelogic.rhapsody.core.IRPModelElement::synchronizeTemplateInstantiation()
        """
        ComHelper.call_com(lambda: self._com.synchronizeTemplateInstantiation())

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, IRPModelElement):
            return NotImplemented
        return bool(self._com == other._com)

    def __hash__(self) -> int:
        return hash(id(self._com))

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name!r})"
