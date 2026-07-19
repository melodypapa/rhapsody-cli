"""RhapsodyImporter: YAML dict -> Rhapsody model.

SWR_XCH_002: Project Import
SWR_XCH_004: Package Import
SWR_XCH_006: Element Find-or-Create (uses RhapsodyModelHelper)
SWR_XCH_008: Core Type-Specific Fields
SWR_XCH_009: Error Handling and Skip-on-Unsupported
"""

import logging
from typing import Any, Dict, Optional

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

    def import_template(self, data: Dict[str, Any], root_element: RPModelElement) -> None:
        """Import elements from data['rhapsody-model'] as children of root_element.

        Args:
            data: Parsed YAML dict (must have version and rhapsody-model keys).
            root_element: Container to import into (project root or package).

        Raises:
            CliExecutionError: If schema version does not match SCHEMA_VERSION.
        """
        version = data.get(VERSION_KEY)
        if version != SCHEMA_VERSION:
            raise CliExecutionError(
                f"Unsupported schema version: {version} (expected {SCHEMA_VERSION})"
            )
        self.project = root_element  # type: ignore[assignment]
        for spec in data.get(RHAPSODY_MODEL_KEY, []):
            self._process_element(root_element, spec)

    def _process_element(
        self, parent: RPModelElement, spec: Dict[str, Any]
    ) -> Optional[RPModelElement]:
        """Dispatch a single element spec to find_or_create_<type>, then apply extras.

        Args:
            parent: Container element to create under.
            spec: Element spec dict (must have 'name' and 'type').

        Returns:
            The created/existing element, or None if the type is unsupported.
        """
        element_type = spec["type"]
        name = spec["name"]

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
            element = self.find_or_create_type(parent, name, spec.get("kind"))
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
        self.apply_stereotypes(element, spec.get("stereotypes", []))
        self.apply_tags(element, spec.get("tags", {}))

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
        # Dependency/Generalization/Relation/Port/Event/EventReception extras
        # are added in Task 6.

        # Generic children (Package, Class, Type with kind=Structure)
        if element_type in ("Package", "Class", "Type"):
            for child_spec in spec.get("children", []):
                self._process_element(element, child_spec)
        return element

    # ------------------------------------------------------------------
    # Type-specific extras (YAML spec fields -> element property setters)
    # ------------------------------------------------------------------

    def _apply_operation_extras(self, operation: RPModelElement, spec: Dict[str, Any]) -> None:
        """Apply Operation-specific fields: return_type, is_static, arguments."""
        if "return_type" in spec:
            classifier = self.resolve_classifier(spec["return_type"])
            if classifier is not None:
                operation.set_returns(classifier)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve return_type '%s' for operation '%s'",
                    spec["return_type"],
                    operation.get_name(),
                )
        if "is_static" in spec:
            operation.set_is_static(spec["is_static"])  # type: ignore[attr-defined]
        for arg_spec in spec.get("arguments", []):
            arg = self.find_or_create_argument(operation, arg_spec["name"])
            self._apply_argument_extras(arg, arg_spec)

    def _apply_argument_extras(self, arg: RPModelElement, spec: Dict[str, Any]) -> None:
        """Apply Argument-specific fields: data_type, direction, stereotypes, tags."""
        if "data_type" in spec:
            classifier = self.resolve_classifier(spec["data_type"])
            if classifier is not None:
                arg.set_type(classifier)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve data_type '%s' for argument '%s'",
                    spec["data_type"],
                    arg.get_name(),
                )
        if "direction" in spec:
            arg.set_argument_direction(spec["direction"])  # type: ignore[attr-defined]
        # Common properties (parity with _process_element path)
        self.apply_stereotypes(arg, spec.get("stereotypes", []))
        self.apply_tags(arg, spec.get("tags", {}))

    def _apply_attribute_extras(self, attr: RPModelElement, spec: Dict[str, Any]) -> None:
        """Apply Attribute-specific fields: data_type, visibility, multiplicity, is_static."""
        if "data_type" in spec:
            classifier = self.resolve_classifier(spec["data_type"])
            if classifier is not None:
                attr.set_type(classifier)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve data_type '%s' for attribute '%s'",
                    spec["data_type"],
                    attr.get_name(),
                )
        if "visibility" in spec:
            attr.set_visibility(spec["visibility"])  # type: ignore[attr-defined]
        if "multiplicity" in spec:
            attr.set_multiplicity(spec["multiplicity"])  # type: ignore[attr-defined]
        if "is_static" in spec:
            attr.set_is_static(spec["is_static"])  # type: ignore[attr-defined]

    def _apply_type_extras(self, type_element: RPModelElement, spec: Dict[str, Any]) -> None:
        """Apply Type-specific fields: enumeration literals (kind already set in find_or_create_type)."""
        if spec.get("kind") == "Enumeration":
            for literal_spec in spec.get("literals", []):
                literal = self.find_or_create_enumeration_literal(type_element, literal_spec["name"])
                self.apply_stereotypes(literal, literal_spec.get("stereotypes", []))
                self.apply_tags(literal, literal_spec.get("tags", {}))

    def _apply_object_extras(self, obj: RPModelElement, spec: Dict[str, Any]) -> None:
        """Apply Object-specific fields: classifier."""
        if "classifier" in spec:
            classifier = self.resolve_classifier(spec["classifier"])
            if classifier is not None:
                obj.set_classifier(classifier)  # type: ignore[attr-defined]
            else:
                logger.warning(
                    "Cannot resolve classifier '%s' for object '%s'",
                    spec["classifier"],
                    obj.get_name(),
                )
