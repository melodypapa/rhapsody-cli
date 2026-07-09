"""Miscellaneous model element wrappers — RPComment, RPConstraint, RPEnumerationLiteral."""

from rhapsody_cli.models.core import AbstractRPModelElement, RPModelElement


class RPEnumerationLiteral(RPModelElement):
    """Wraps ``IRPEnumerationLiteral``: a literal value in an enumeration."""

    pass


AbstractRPModelElement.register_wrapper("EnumerationLiteral", RPEnumerationLiteral)


class RPComment(RPModelElement):
    """Wraps ``IRPComment``: a free-text comment element."""

    pass


AbstractRPModelElement.register_wrapper("Comment", RPComment)


class RPConstraint(RPModelElement):
    """Wraps ``IRPConstraint``: a constraint element."""

    pass


AbstractRPModelElement.register_wrapper("Constraint", RPConstraint)
