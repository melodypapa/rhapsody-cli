"""AbstractAttributeAction — split from attribute_action.py."""

import logging
from typing import cast

from rhapsody_cli.actions.abstract_action import ElementManagementAction, SessionAwareAction
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class AbstractAttributeAction(SessionAwareAction, ElementManagementAction):
    """Base class for attribute actions with common path, name and GUID validation.

    SWR_ATTR_00006: Path and Name Validation
    SWR_ATTR_00009: Error Handling and Logging
    SWR_ATTR_00010: GUID Lookup Support
    """

    def _resolve_classifier(self, path: str) -> IRPModelElement:
        """Resolve a parent classifier path.

        Args:
            path: Classifier path to resolve.

        Returns:
            Classifier COM object.

        Raises:
            CliExecutionError: If path not found.
        """
        root = self._get_active_root()
        return self._resolve_container_or_element(root, path, resolve_element=True, operation=f"resolve classifier path '{path}'")

    def _resolve_attribute(self, classifier: IRPModelElement, name: str) -> IRPModelElement:
        """Find an attribute by name within a classifier.

        Args:
            classifier: The parent classifier COM object.
            name: The attribute name to find.

        Returns:
            Attribute COM object.

        Raises:
            CliExecutionError: If attribute not found.
        """
        attribute = classifier.find_attribute(name)  # type: ignore[attr-defined]
        if attribute is None:
            raise CliExecutionError(f"Attribute '{name}' not found in classifier")
        return cast(IRPModelElement, attribute)

    def _resolve_attribute_by_guid(self, guid: str) -> IRPModelElement:
        """Locate an attribute by GUID and validate it's an Attribute element.

        SWR_ATTR_00010: GUID Lookup Support

        Args:
            guid: GUID string in format 12345678-1234-1234-1234-123456789abc.

        Returns:
            Attribute COM object.

        Raises:
            CliExecutionError: If GUID not found or element is not an Attribute.
        """
        project = self._get_active_project()
        try:
            element = project.find_element_by_guid(guid)
        except Exception as e:
            self._handle_execution_error(e, f"Failed to locate attribute by GUID '{guid}'")

        if element is None:
            raise CliExecutionError(f"No element found with GUID '{guid}'")

        meta_class = element.meta_class
        if meta_class != "Attribute":
            raise CliExecutionError(f"GUID '{guid}' does not resolve to an Attribute (found {meta_class})")

        return element
