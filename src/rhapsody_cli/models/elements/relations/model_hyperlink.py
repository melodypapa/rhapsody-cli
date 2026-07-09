"""Wraps ``com.telelogic.rhapsody.core.IRPHyperLink``."""

from rhapsody_cli.models.core import AbstractRPModelElement
from rhapsody_cli.models.elements.relations.model_dependency import RPDependency


class RPHyperLink(RPDependency):
    """Wraps ``IRPHyperLink``: a hyperlink that extends ``IRPDependency``."""

    pass


AbstractRPModelElement.register_wrapper("HyperLink", RPHyperLink)
