"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPAction``."""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class IRPAction(IRPModelElement):
    """Wraps ``IRPAction``: represents the action defined for a transition.

    The JavaDoc ``getBody`` / ``setBody`` accessors are exposed by pywin32 as
    a single ``body`` property.
    """

    # IRPAction method parity checklist:
    # [x] body                          [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)

    @property
    def body(self) -> str:
        """Returns the code defined as the action for the transition.

        Returns:
            The action code.

        Reference:
            com.telelogic.rhapsody.core.IRPAction::getBody()
        """
        return str(self.get_com_property(self._com, "body"))

    @body.setter
    def body(self, body: str) -> None:
        """Specifies the code that serves as the action for the transition.

        Args:
            body: The code to use as the action.

        Reference:
            com.telelogic.rhapsody.core.IRPAction::setBody(java.lang.String body)
        """
        self.set_com_property(self._com, "body", body)


IRPModelElement.register_wrapper("Action", IRPAction)
