"""RhapsodyImporter: YAML dict -> Rhapsody model.

SWR_XCH_002: Project Import
SWR_XCH_004: Package Import
SWR_XCH_006: Element Find-or-Create (uses RhapsodyModelHelper)
SWR_XCH_008: Core Type-Specific Fields
SWR_XCH_009: Error Handling and Skip-on-Unsupported
"""

import logging
from typing import Dict, List, Optional, cast

from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.exchange.core import RhapsodyModelHelper
from rhapsody_cli.exchange.schema import RHAPSODY_MODEL_KEY, SCHEMA_VERSION, VERSION_KEY
from rhapsody_cli.models.core import RPModelElement

logger = logging.getLogger(__name__)


class RhapsodyImporter(RhapsodyModelHelper):
    """Imports a YAML dict into a Rhapsody model container.

    Each element spec is processed via _process_element, which dispatches
    to find_or_create_<type>, applies common properties (stereotypes, tags),
    then applies type-specific extras and recurses into children.
    """

    def import_template(self, data: Dict[str, object], root_element: RPModelElement) -> None:
        """Import elements from data['rhapsody-model'] as children of root_element.

        Args:
            data: Parsed YAML dict (must have version and rhapsody-model keys).
            root_element: Container to import into (project root or package).

        Raises:
            CliExecutionError: If schema version does not match SCHEMA_VERSION.
        """
        version = data.get(VERSION_KEY)
        if version != SCHEMA_VERSION:
            raise CliExecutionError(f"Unsupported schema version: {version} (expected {SCHEMA_VERSION})")
        self.project = root_element  # type: ignore[assignment]
        for spec in cast(List[Dict[str, object]], data.get(RHAPSODY_MODEL_KEY, [])):
            self._process_element(root_element, spec)

    def _process_element(self, parent: RPModelElement, spec: Dict[str, object]) -> Optional[RPModelElement]:
        """Dispatch a single element spec to find_or_create_<type>, then apply extras.

        Args:
            parent: Container element to create under.
            spec: Element spec dict (must have 'name' and 'type').

        Returns:
            The created/existing element, or None if the type is unsupported.
        """
        element_type = cast(str, spec["type"])
        name = cast(str, spec["name"])

        if element_type == "Package":
            element = self.find_or_create_package(parent, name)
        elif element_type == "Class":
            element = self.find_or_create_class(parent, name)
        elif element_type == "Operation":
            element = self.find_or_create_operation(parent, name)
        elif element_type == "Attribute":
            element = self.find_or_create_attribute(parent, name)
        elif element_type == "Argument":
            element = self.find_or_create_argument(parent, name)
        elif element_type == "Type":
            element = self.find_or_create_type(parent, name, cast(Optional[str], spec.get("kind")))
        elif element_type == "Object":
            element = self.find_or_create_object(parent, name)
        elif element_type == "EnumerationLiteral":
            element = self.find_or_create_enumeration_literal(parent, name)
        elif element_type == "Dependency":
            element = self.find_or_create_dependency(parent, name)
        elif element_type == "Generalization":
            element = self.find_or_create_generalization(parent, name)
        elif element_type == "Relation":
            element = self.find_or_create_relation(parent, name)
        elif element_type == "Port":
            element = self.find_or_create_port(parent, name)
        elif element_type == "Event":
            element = self.find_or_create_event(parent, name)
        elif element_type == "EventReception":
            element = self.find_or_create_event_reception(parent, name)
        else:
            logger.warning("Unsupported element type '%s'; skipping", element_type)
            return None

        # Common properties
        self.apply_stereotypes(element, cast(List[str], spec.get("stereotypes", [])))
        self.apply_tags(element, cast(Dict[str, str], spec.get("tags", {})))

        # Type-specific extras
        if element_type == "Operation":
            self._apply_operation_extras(element, spec)
        elif element_type == "Attribute":
            self._apply_attribute_extras(element, spec)
        elif element_type == "Argument":
            self._apply_argument_extras(element, spec)
        elif element_type == "Type":
            self._apply_type_extras(element, spec)
        elif element_type == "Object":
            self._apply_object_extras(element, spec)
        elif element_type == "Dependency":
            self._apply_dependency_extras(element, spec, parent)
        elif element_type == "Generalization":
            self._apply_generalization_extras(element, spec, parent)
        elif element_type == "Relation":
            self._apply_relation_extras(element, spec, parent)
        elif element_type == "Port":
            self._apply_port_extras(element, spec)
        elif element_type == "Event":
            self._apply_event_extras(element, spec)
        elif element_type == "EventReception":
            self._apply_event_reception_extras(element, spec)

        # Generic children (Package, Class, Type with kind=Structure)
        if element_type in ("Package", "Class", "Type"):
            for child_spec in cast(List[Dict[str, object]], spec.get("children", [])):
                self._process_element(element, child_spec)
        return element

    # ------------------------------------------------------------------
    # Type-specific extras (YAML spec fields -> element property setters)
    # ------------------------------------------------------------------

    def _apply_operation_extras(self, operation: RPModelElement, spec: Dict[str, object]) -> None:
        """Apply Operation-specific fields: return_type, is_static, arguments."""
        if "return_type" in spec:
            return_type = cast(str, spec["return_type"])
            classifier = self.resolve_classifier(return_type)
            if classifier is not None:
                operation.set_returns(classifier)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve return_type '%s' for operation '%s'",
                    return_type,
                    operation.get_name(),
                )
        if "is_static" in spec:
            operation.set_is_static(cast(bool, spec["is_static"]))  # type: ignore[attr-defined]
        for arg_spec in cast(List[Dict[str, object]], spec.get("arguments", [])):
            arg = self.find_or_create_argument(operation, cast(str, arg_spec["name"]))
            self._apply_argument_extras(arg, arg_spec)

    def _apply_argument_extras(self, arg: RPModelElement, spec: Dict[str, object]) -> None:
        """Apply Argument-specific fields: data_type, direction, stereotypes, tags."""
        if "data_type" in spec:
            data_type = cast(str, spec["data_type"])
            classifier = self.resolve_classifier(data_type)
            if classifier is not None:
                arg.set_type(classifier)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve data_type '%s' for argument '%s'",
                    data_type,
                    arg.get_name(),
                )
        if "direction" in spec:
            arg.set_argument_direction(cast(str, spec["direction"]))  # type: ignore[attr-defined]
        # Common properties (parity with _process_element path)
        self.apply_stereotypes(arg, cast(List[str], spec.get("stereotypes", [])))
        self.apply_tags(arg, cast(Dict[str, str], spec.get("tags", {})))

    def _apply_attribute_extras(self, attr: RPModelElement, spec: Dict[str, object]) -> None:
        """Apply Attribute-specific fields: data_type, visibility, multiplicity, is_static."""
        if "data_type" in spec:
            data_type = cast(str, spec["data_type"])
            classifier = self.resolve_classifier(data_type)
            if classifier is not None:
                attr.set_type(classifier)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve data_type '%s' for attribute '%s'",
                    data_type,
                    attr.get_name(),
                )
        if "visibility" in spec:
            attr.set_visibility(cast(str, spec["visibility"]))  # type: ignore[attr-defined]
        if "multiplicity" in spec:
            attr.set_multiplicity(cast(str, spec["multiplicity"]))  # type: ignore[attr-defined]
        if "is_static" in spec:
            attr.set_is_static(cast(bool, spec["is_static"]))  # type: ignore[attr-defined]

    def _apply_type_extras(self, type_element: RPModelElement, spec: Dict[str, object]) -> None:
        """Apply Type-specific fields: enumeration literals (kind already set in find_or_create_type)."""
        if spec.get("kind") == "Enumeration":
            for literal_spec in cast(List[Dict[str, object]], spec.get("literals", [])):
                literal = self.find_or_create_enumeration_literal(type_element, cast(str, literal_spec["name"]))
                self.apply_stereotypes(literal, cast(List[str], literal_spec.get("stereotypes", [])))
                self.apply_tags(literal, cast(Dict[str, str], literal_spec.get("tags", {})))

    def _apply_object_extras(self, obj: RPModelElement, spec: Dict[str, object]) -> None:
        """Apply Object-specific fields: classifier."""
        if "classifier" in spec:
            classifier_name = cast(str, spec["classifier"])
            classifier = self.resolve_classifier(classifier_name)
            if classifier is not None:
                obj.set_classifier(classifier)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve classifier '%s' for object '%s'",
                    classifier_name,
                    obj.get_name(),
                )

    def _apply_dependency_extras(self, dependency: RPModelElement, spec: Dict[str, object], parent: RPModelElement) -> None:
        """Apply Dependency-specific fields: source (parent) and target (depends_on)."""
        dependency.set_dependent(parent)  # type: ignore[attr-defined]
        if "depends_on" in spec:
            depends_on = cast(str, spec["depends_on"])
            target = self.resolve_classifier(depends_on)
            if target is not None:
                dependency.set_depends_on(target)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve depends_on '%s' for dependency '%s'",
                    depends_on,
                    dependency.get_name(),
                )

    def _apply_generalization_extras(self, generalization: RPModelElement, spec: Dict[str, object], parent: RPModelElement) -> None:
        """Apply Generalization-specific fields: derived_class (parent), base_class, visibility, is_virtual."""
        generalization.set_derived_class(parent)  # type: ignore[attr-defined]
        if "base_class" in spec:
            base_class = cast(str, spec["base_class"])
            target = self.resolve_classifier(base_class)
            if target is not None:
                generalization.set_base_class(target)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve base_class '%s' for generalization '%s'",
                    base_class,
                    generalization.get_name(),
                )
        if "visibility" in spec:
            generalization.set_visibility(cast(str, spec["visibility"]))  # type: ignore[attr-defined]
        if "is_virtual" in spec:
            generalization.set_is_virtual(cast(bool, spec["is_virtual"]))  # type: ignore[attr-defined]

    def _apply_relation_extras(self, relation: RPModelElement, spec: Dict[str, object], parent: RPModelElement) -> None:
        """Apply Relation-specific fields: from (source), to (target), relation_type, multiplicity, etc."""
        if "from" in spec:
            from_name = cast(str, spec["from"])
            source = self.resolve_classifier(from_name)
            if source is None:
                logger.warning(
                    "Cannot resolve from '%s' for relation '%s'; using parent",
                    from_name,
                    relation.get_name(),
                )
                source = parent
        else:
            source = parent
        relation.set_of_class(source)  # type: ignore[attr-defined]
        if "to" in spec:
            to_name = cast(str, spec["to"])
            target = self.resolve_classifier(to_name)
            if target is not None:
                relation.set_other_class(target)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve to '%s' for relation '%s'",
                    to_name,
                    relation.get_name(),
                )
        if "relation_type" in spec:
            relation.set_relation_type(cast(str, spec["relation_type"]))  # type: ignore[attr-defined]
        if "multiplicity" in spec:
            relation.set_multiplicity(cast(str, spec["multiplicity"]))  # type: ignore[attr-defined]
        if "is_navigable" in spec:
            relation.set_is_navigable(cast(bool, spec["is_navigable"]))  # type: ignore[attr-defined]
        if "role" in spec:
            relation.set_relation_role_name(cast(str, spec["role"]))  # type: ignore[attr-defined]
        if "visibility" in spec:
            relation.set_visibility(cast(str, spec["visibility"]))  # type: ignore[attr-defined]

    def _apply_port_extras(self, port: RPModelElement, spec: Dict[str, object]) -> None:
        """Apply Port-specific fields: is_behavioral, is_reversed, contract, provided/required_interfaces."""
        if "is_behavioral" in spec:
            port.set_is_behavioral(cast(bool, spec["is_behavioral"]))  # type: ignore[attr-defined]
        if "is_reversed" in spec:
            port.set_is_reversed(cast(bool, spec["is_reversed"]))  # type: ignore[attr-defined]
        if "contract" in spec:
            contract_name = cast(str, spec["contract"])
            classifier = self.resolve_classifier(contract_name)
            if classifier is not None:
                port.set_contract(classifier)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve contract '%s' for port '%s'",
                    contract_name,
                    port.get_name(),
                )
        for iface_name in cast(List[str], spec.get("provided_interfaces", [])):
            iface = self.resolve_classifier(iface_name)
            if iface is not None:
                port.add_provided_interface(iface)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve provided_interface '%s' for port '%s'",
                    iface_name,
                    port.get_name(),
                )
        for iface_name in cast(List[str], spec.get("required_interfaces", [])):
            iface = self.resolve_classifier(iface_name)
            if iface is not None:
                port.add_required_interface(iface)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve required_interface '%s' for port '%s'",
                    iface_name,
                    port.get_name(),
                )

    def _apply_event_extras(self, event: RPModelElement, spec: Dict[str, object]) -> None:
        """Apply Event-specific fields: base_event, super_event."""
        if "base_event" in spec:
            base_event_name = cast(str, spec["base_event"])
            target = self.resolve_classifier(base_event_name)
            if target is not None:
                event.set_base_event(target)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve base_event '%s' for event '%s'",
                    base_event_name,
                    event.get_name(),
                )
        if "super_event" in spec:
            super_event_name = cast(str, spec["super_event"])
            target = self.resolve_classifier(super_event_name)
            if target is not None:
                event.set_super_event(target)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve super_event '%s' for event '%s'",
                    super_event_name,
                    event.get_name(),
                )

    def _apply_event_reception_extras(self, reception: RPModelElement, spec: Dict[str, object]) -> None:
        """Apply EventReception-specific fields: event reference."""
        if "event" in spec:
            event_name = cast(str, spec["event"])
            target = self.resolve_classifier(event_name)
            if target is not None:
                reception.set_event(target)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve event '%s' for reception '%s'",
                    event_name,
                    reception.get_name(),
                )
