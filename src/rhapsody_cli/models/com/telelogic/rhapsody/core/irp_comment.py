"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPComment``."""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class IRPComment(IRPModelElement):
    """Wraps ``IRPComment``: a free-text comment element.

    The JavaDoc interface declares no owned members; all behavior is inherited
    from ``IRPModelElement``.
    """

    # IRPComment method parity checklist:
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)
    # No owned IRPComment members.


IRPModelElement.register_wrapper("Comment", IRPComment)
