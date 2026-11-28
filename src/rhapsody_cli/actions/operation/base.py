"""AbstractOperationAction — split from operation_action.py."""

import logging
from typing import cast

from rhapsody_cli.actions.abstract_action import ElementManagementAction, SessionAwareAction
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class AbstractOperationAction(SessionAwareAction, ElementManagementAction):
    """Base class for operation actions with common path, name and GUID validation.

    SWR_OP_00006: Path and Name Validation
    SWR_OP_00009: Error Handling and Logging
    SWR_OP_00010: GUID Lookup Support
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

    def _resolve_operation(self, classifier: IRPModelElement, name: str) -> IRPModelElement:
        """Find an operation by name within a classifier.

        Args:
            classifier: The parent classifier COM object.
            name: The operation name to find.

        Returns:
            Operation COM object.

        Raises:
            CliExecutionError: If operation not found.
        """
        operation = classifier.find_interface_item(name)  # type: ignore[attr-defined]
        if operation is None:
            raise CliExecutionError(f"Operation '{name}' not found in classifier")
        return cast(IRPModelElement, operation)

    def _resolve_operation_by_guid(self, guid: str) -> IRPModelElement:
        """Locate an operation by GUID and validate it's an Operation element.

        SWR_OP_00010: GUID Lookup Support

        Args:
            guid: GUID string in format 12345678-1234-1234-1234-123456789abc.

        Returns:
            Operation COM object.

        Raises:
            CliExecutionError: If GUID not found or element is not an Operation.
        """
        project = self._get_active_project()
        try:
            element = project.find_element_by_guid(guid)
        except Exception as e:
            self._handle_execution_error(e, f"Failed to locate operation by GUID '{guid}'")

        if element is None:
            raise CliExecutionError(f"No element found with GUID '{guid}'")

        meta_class = element.meta_class
        if meta_class != "Operation":
            raise CliExecutionError(f"GUID '{guid}' does not resolve to an Operation (found {meta_class})")

        return element
