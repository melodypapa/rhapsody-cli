"""AbstractClassAction — split from class_action.py."""

import logging
from typing import Optional, cast

from rhapsody_cli.actions.abstract_action import ElementManagementAction, SessionAwareAction
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class AbstractClassAction(SessionAwareAction, ElementManagementAction):
    """Base class for class actions with common path and GUID validation.

    SWR_CLS_00005: Path Validation
    SWR_CLS_00010: Error Handling and Logging
    SWR_CLS_00013: GUID Lookup Support
    """

    _PACKAGE_META_CLASSES = {"Package", "Project"}

    def _find_nested_by_name(self, owner: IRPModelElement, name: str) -> Optional[IRPModelElement]:
        """Fall back to a recursive walk when the COM finder is unavailable."""
        try:
            nested = owner.get_nested_elements()
        except (AttributeError, RuntimeError):
            return None
        for element in nested:
            wrapped = cast(IRPModelElement, element)
            if wrapped.name == name:
                return wrapped
            found = self._find_nested_by_name(wrapped, name)
            if found is not None:
                return found
        return None

    def _resolve_and_validate_package(self, path: str) -> IRPModelElement:
        """Resolve path and validate it's a Package or Project element.

        Used by create and list. IRPProject inherits addClass/getClasses from
        IRPPackage, so the project root is a valid parent.

        Args:
            path: Package path to resolve.

        Returns:
            Package or Project COM object.

        Raises:
            CliExecutionError: If path not found or not a Package/Project.
        """
        root = self._get_active_root()
        container = self._resolve_container_or_element(root, path, resolve_element=False, operation=f"resolve package path '{path}'")

        meta_class = container.meta_class
        if meta_class not in self._PACKAGE_META_CLASSES:
            raise CliExecutionError(f"Path '{path}' does not resolve to a Package or Project (found {meta_class})")

        return container

    def _resolve_and_validate_class(self, path: str) -> IRPModelElement:
        """Resolve path and validate it's a Class element.

        Used by delete, view, and link.

        Args:
            path: Class path to resolve.

        Returns:
            Class COM object.

        Raises:
            CliExecutionError: If path not found or not a Class.
        """
        root = self._get_active_root()
        element = self._resolve_container_or_element(root, path, resolve_element=True, operation=f"resolve class path '{path}'")

        meta_class = element.meta_class
        if meta_class != "Class":
            raise CliExecutionError(f"Path '{path}' does not resolve to a Class (found {meta_class})")

        return element

    def _resolve_class_by_guid(self, guid: str) -> IRPModelElement:
        """Locate a class by GUID and validate it's a Class element.

        SWR_CLS_00013: GUID Lookup Support

        Args:
            guid: GUID string in format 12345678-1234-1234-1234-123456789abc.

        Returns:
            Class COM object.

        Raises:
            CliExecutionError: If GUID not found or element is not a Class.
        """
        project = self._get_active_project()
        try:
            element = project.find_element_by_guid(guid)
        except Exception as e:
            self._handle_execution_error(e, f"Failed to locate class by GUID '{guid}'")

        if element is None:
            raise CliExecutionError(f"No element found with GUID '{guid}'")

        meta_class = element.meta_class
        if meta_class != "Class":
            raise CliExecutionError(f"GUID '{guid}' does not resolve to a Class (found {meta_class})")

        return element
