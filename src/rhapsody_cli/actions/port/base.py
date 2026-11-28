"""AbstractPortAction — split from port_action.py."""

import logging
from typing import cast

from rhapsody_cli.actions.abstract_action import ElementManagementAction, SessionAwareAction
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class AbstractPortAction(SessionAwareAction, ElementManagementAction):
    """Base class for port actions with common path, name and GUID validation.

    SWR_PORT_00006: Path and Name Validation
    SWR_PORT_00009: Error Handling and Logging
    SWR_PORT_00010: GUID Lookup Support
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

    def _resolve_port(self, classifier: IRPModelElement, name: str) -> IRPModelElement:
        """Find a port by name within a classifier by iterating getPorts().

        Args:
            classifier: The parent classifier COM object.
            name: The port name to find.

        Returns:
            Port COM object.

        Raises:
            CliExecutionError: If port not found.
        """
        ports = classifier.ports  # type: ignore[attr-defined]
        for port in ports:
            if cast(IRPModelElement, port).name == name:
                return cast(IRPModelElement, port)
        raise CliExecutionError(f"Port '{name}' not found in classifier")

    def _resolve_port_by_guid(self, guid: str) -> IRPModelElement:
        """Locate a port by GUID and validate it's a Port element.

        SWR_PORT_00010: GUID Lookup Support

        Args:
            guid: GUID string in format 12345678-1234-1234-1234-123456789abc.

        Returns:
            Port COM object.

        Raises:
            CliExecutionError: If GUID not found or element is not a Port.
        """
        project = self._get_active_project()
        try:
            element = project.find_element_by_guid(guid)
        except Exception as e:
            self._handle_execution_error(e, f"Failed to locate port by GUID '{guid}'")

        if element is None:
            raise CliExecutionError(f"No element found with GUID '{guid}'")

        meta_class = element.meta_class
        if meta_class != "Port":
            raise CliExecutionError(f"GUID '{guid}' does not resolve to a Port (found {meta_class})")

        return element
