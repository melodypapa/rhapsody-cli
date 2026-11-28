"""ClassUpdateAction — split from class_action.py."""

import argparse
import json
import logging
from typing import Dict, List, cast

from rhapsody_cli.actions.classifier.base import AbstractClassAction
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class ClassUpdateAction(AbstractClassAction):
    """Update attributes of an existing class.

    SWR_CLS_00014: Class Update Command
    SWR_CLS_00006: External JSON File Support
    SWR_CLS_00007: Stereotype and Tag Support
    SWR_CLS_00012: Boolean Flag Support
    SWR_CLS_00013: GUID Lookup Support
    """

    VALID_ATTRIBUTES = {
        "name",
        "description",
        "isAbstract",
        "isFinal",
        "isActive",
        "stereotypes",
        "tags",
    }

    def __init__(self) -> None:
        """Initialize the 'update' action."""
        super().__init__(command_id="update")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'update' subcommand and its arguments."""
        parser = sub_parser.add_parser("update", help="Update attributes of an existing class")
        self.add_path_argument(parser, required=False, help_text="Class path to update")
        parser.add_argument("--guid", default=None, help="GUID of the class to update")
        parser.add_argument("--input", default=None, help="JSON file with class attributes")
        parser.add_argument("attributes", nargs="?", default=None, help="Inline JSON or JSON file path")

    def _load_json_data(self, args: argparse.Namespace) -> Dict[str, object]:
        """Load JSON data from inline string or file.

        SWR_CLS_0006: External JSON File Support

        Args:
            args: Parsed argparse.Namespace with `input` and `attributes`.

        Returns:
            Dictionary of class attributes (empty if neither provided).
        """
        if args.input:
            try:
                with open(args.input, encoding="utf-8") as f:
                    return cast(Dict[str, object], json.load(f))
            except FileNotFoundError:
                raise CliExecutionError(f"File not found: {args.input}") from None
            except json.JSONDecodeError as e:
                raise CliExecutionError(f"Invalid JSON: {e}") from e
        elif args.attributes:
            data_str = args.attributes.strip()
            if data_str.startswith("{"):
                try:
                    return cast(Dict[str, object], json.loads(data_str))
                except json.JSONDecodeError as e:
                    raise CliExecutionError(f"Invalid JSON: {e}") from e
            else:
                try:
                    with open(data_str, encoding="utf-8") as f:
                        return cast(Dict[str, object], json.load(f))
                except FileNotFoundError:
                    raise CliExecutionError(f"File not found: {data_str}") from None
                except json.JSONDecodeError as e:
                    raise CliExecutionError(f"Invalid JSON: {e}") from e
        return {}

    def _set_attributes(self, cls: IRPModelElement, data: Dict[str, object]) -> None:
        """Set validated attributes on class (partial update).

        SWR_CLS_00012: Boolean Flag Support

        Only fields present in `data` are modified; unknown fields are
        skipped with a warning log.

        Args:
            cls: Class COM object to update.
            data: Dictionary of attributes to apply.
        """
        for key, value in data.items():
            if key not in self.VALID_ATTRIBUTES:
                self.logger.warning("Skipping unknown attribute: %s", key)
                continue
            if key == "name":
                cls.name = cast(str, value)
            elif key == "description":
                cls.description = cast(str, value)
            elif key == "isAbstract":
                cls.is_abstract = bool(value)  # type: ignore[attr-defined]
            elif key == "isFinal":
                cls.set_is_final(1 if value else 0)  # type: ignore[attr-defined]
            elif key == "isActive":
                cls.is_active = 1 if value else 0  # type: ignore[attr-defined]
            elif key == "stereotypes":
                for stereotype in cast(List[str], value):
                    cls.add_stereotype(stereotype, "Class")
            elif key == "tags":
                for tag_key, tag_value in cast(Dict[str, str], value).items():
                    cls.set_property_value(tag_key, tag_value)

    def execute(self, args: argparse.Namespace) -> None:
        """Execute class update.

        Args:
            args: Parsed argparse.Namespace with path/guid and attribute data.
        """
        super().execute(args)
        self.logger.info("Starting class update...")
        if not args.path and not args.guid:
            raise CliExecutionError("Either --path or --guid is required")
        if args.guid:
            self.logger.info("Resolving class by GUID '%s'...", args.guid)
            cls = self._resolve_class_by_guid(args.guid)
        else:
            self.logger.info("Resolving class path '%s'...", args.path)
            cls = self._resolve_and_validate_class(args.path)
        data = self._load_json_data(args)
        self._set_attributes(cls, data)
        self.logger.info("Successfully updated class: %s", cls.name)
