"""Miscellaneous model element wrapper — IRPComment."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class IRPComment(IRPModelElement):
    """Wraps ``IRPComment``: a free-text comment element."""

    # IRPComment method parity checklist:
    # [inherited] irp_model_element methods (covered by rp_model_element checklists)
    # No deprecated IRPComment methods.

    pass


IRPModelElement.register_wrapper("Comment", IRPComment)
