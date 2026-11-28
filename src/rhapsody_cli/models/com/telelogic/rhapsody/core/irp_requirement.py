"""Wrapper for the Java ``IRPRequirement`` interface."""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_requirements import IRPAnnotation


def _cast_requirement_dispatch(com_obj: object) -> object:
    """Cast a generic pywin dispatch to the concrete requirement interface."""
    try:
        from win32com.client import CastTo, DispatchBaseClass
    except ImportError:
        return com_obj
    if isinstance(com_obj, DispatchBaseClass):
        return CastTo(com_obj, "IRPRequirement")
    return com_obj


class IRPRequirement(IRPAnnotation):
    """Wraps ``IRPRequirement``: represents a requirement in the model."""

    # IRPRequirement property parity checklist:
    # [x] requirement_id  [x] getter  [x] setter  [x] unit test  [ ] integration test
    # [inherited] irp_annotation / irp_unit / irp_model_element methods

    def __init__(self, com_obj: object) -> None:
        super().__init__(_cast_requirement_dispatch(com_obj))

    @property
    def requirement_id(self) -> str:
        """Returns the ID that was set for the requirement.

        Returns:
            The requirement ID string.

        Reference:
            com.telelogic.rhapsody.core.IRPRequirement::getRequirementID()
        """
        return str(self.get_com_property(self._com, "requirementID"))

    @requirement_id.setter
    def requirement_id(self, requirement_id: str) -> None:
        """Sets the ID for the requirement.

        Args:
            requirement_id: The new requirement ID to set.

        Reference:
            com.telelogic.rhapsody.core.IRPRequirement::setRequirementID(java.lang.String requirementID)
        """
        self.set_com_property(self._com, "requirementID", requirement_id)


IRPModelElement.register_wrapper("Requirement", IRPRequirement)
