"""ClassLinkAction — split from class_action.py."""

import argparse
import logging

from rhapsody_cli.actions.classifier.base import AbstractClassAction
from rhapsody_cli.exceptions import CliExecutionError

logger = logging.getLogger(__name__)


class ClassLinkAction(AbstractClassAction):
    """Add or remove generalization relationships between classes.

    SWR_CLS_00011: Class Link Command (generalization only — association
        and unidirectional deferred to future iteration)
    SWR_CLS_00013: GUID Lookup Support
    """

    def __init__(self) -> None:
        """Initialize the 'link' action."""
        super().__init__(command_id="link")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'link' subcommand and its arguments."""
        parser = sub_parser.add_parser("link", help="Add or remove generalization relationships")
        self.add_path_argument(parser, required=False, help_text="Class path to modify")
        parser.add_argument("--guid", default=None, help="Class GUID to modify")
        parser.add_argument("--add", default=None, help="Add a generalization to target class by name")
        parser.add_argument("--remove", default=None, help="Remove a generalization to target class by name")
        parser.add_argument(
            "--type",
            choices=["generalization"],
            default="generalization",
            help="Relationship type (v1 supports only generalization)",
        )

    def execute(self, args: argparse.Namespace) -> None:
        """Execute class link operation."""
        super().execute(args)
        if args.path and args.guid:
            raise CliExecutionError("Only one of --path or --guid may be specified")
        if not args.path and not args.guid:
            raise CliExecutionError("Either --path or --guid must be specified")
        if args.add and args.remove:
            raise CliExecutionError("Only one of --add or --remove may be specified")
        if not args.add and not args.remove:
            raise CliExecutionError("Either --add or --remove must be specified")

        if args.guid:
            source = self._resolve_class_by_guid(args.guid)
        else:
            source = self._resolve_and_validate_class(args.path)

        target_name = args.add if args.add else args.remove
        owner = source.owner
        try:
            target = owner.find_nested_classifier_recursive(target_name)  # type: ignore[attr-defined]
        except AttributeError:
            # Some Rhapsody builds expose the owning element as a generic
            # IRPModelElement COM object without the classifier finder; fall
            # back to a recursive walk through nested elements.
            target = self._find_nested_by_name(owner, target_name)
        if target is None:
            raise CliExecutionError(f"Class '{target_name}' not found")

        try:
            if args.add:
                source.add_generalization(target)  # type: ignore[attr-defined]
                self.logger.info(
                    "Added generalization: %s -> %s",
                    args.path or args.guid,
                    target_name,
                )
            else:
                source.delete_generalization(target)  # type: ignore[attr-defined]
                self.logger.info(
                    "Removed generalization: %s -/-> %s",
                    args.path or args.guid,
                    target_name,
                )
        except Exception as e:
            self._handle_execution_error(e, f"Failed to modify generalization for class '{args.path or args.guid}'")
