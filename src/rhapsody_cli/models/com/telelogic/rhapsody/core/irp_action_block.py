"""Wrapper for ``com.telelogic.rhapsody.core.IRPActionBlock``."""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPMessage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class IRPActionBlock(IRPMessage):
    """Represents an action block in a sequence diagram.

    All API members are inherited from ``IRPMessage``.
    """

    pass


IRPModelElement.register_wrapper("ActionBlock", IRPActionBlock)
