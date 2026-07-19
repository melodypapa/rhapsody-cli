"""Rhapsody model -> YAML dict exporter.

SWR_XCH_001: Export Rhapsody model to YAML
SWR_XCH_003: Project Export
"""

import logging
from typing import Any, Dict, List, Optional

from rhapsody_cli.exchange.core import RhapsodyModelHelper
from rhapsody_cli.exchange.schema import PROJECT_KEY, RHAPSODY_MODEL_KEY, SCHEMA_VERSION, VERSION_KEY
from rhapsody_cli.models.core import RPModelElement

_LOGGER = logging.getLogger(__name__)


class RhapsodyExporter(RhapsodyModelHelper):
    """Walks a Rhapsody container and produces a YAML-serializable dict."""

    def export(self, container: Any) -> Dict[str, Any]:
        """Export the container's children to a YAML dict.

        Args:
            container: A wrapped RPModelElement (Project or Package) whose
                children will be exported.

        Returns:
            A dict with keys: version, project, rhapsody-model.
        """
        wrapped = self._wrap_if_needed(container)
        project_name = self._get_project_name(wrapped)
        children = self._collect_children(wrapped)
        model_list: List[Dict[str, Any]] = []
        for child in children:
            spec = self._export_element(child)
            if spec is not None:
                model_list.append(spec)
        return {
            VERSION_KEY: SCHEMA_VERSION,
            PROJECT_KEY: project_name,
            RHAPSODY_MODEL_KEY: model_list,
        }

    def _export_element(self, element: Any) -> Optional[Dict[str, Any]]:
        """Dispatch to a type-specific exporter based on metaclass.

        Args:
            element: A wrapped or raw model element.

        Returns:
            A YAML dict for the element, or None if the metaclass is unsupported.
        """
        if element is None:
            return None
        wrapped = self._wrap_if_needed(element)
        try:
            meta_class = wrapped.get_meta_class()
        except Exception:
            return None
        dispatch = {
            "Package": self._export_package,
            "Class": self._export_class,
            "Operation": self._export_operation,
            "Argument": self._export_argument,
            "Attribute": self._export_attribute,
            "Type": self._export_type,
            "Object": self._export_object,
            "EnumerationLiteral": self._export_enumeration_literal,
        }
        exporter = dispatch.get(meta_class)
        if exporter is None:
            _LOGGER.warning("Skipping unsupported metaclass: %s", meta_class)
            return None
        spec = exporter(wrapped)
        self._attach_common_fields(spec, wrapped)
        return spec

    def _export_package(self, pkg: RPModelElement) -> Dict[str, Any]:
        return self._export_container(pkg, "Package")

    def _export_class(self, cls: RPModelElement) -> Dict[str, Any]:
        return self._export_container(cls, "Class")

    def _export_type(self, type_element: RPModelElement) -> Dict[str, Any]:
        spec: Dict[str, Any] = {"name": type_element.get_name(), "type": "Type"}
        kind = self._safe_get(type_element, "get_kind")
        if kind:
            spec["kind"] = kind
        if kind == "Enumeration":
            literals = self._export_collection(type_element, "get_enumeration_literals")
            if literals:
                spec["literals"] = literals
        elif kind == "Structure":
            children = self._collect_children(type_element)
            child_specs = self._export_children(children)
            if child_specs:
                spec["children"] = child_specs
        return spec

    def _export_operation(self, op: RPModelElement) -> Dict[str, Any]:
        spec: Dict[str, Any] = {"name": op.get_name(), "type": "Operation"}
        return_classifier = self._safe_get(op, "get_returns")
        return_name = self.get_classifier_name(return_classifier) if return_classifier is not None else None
        if return_name:
            spec["return_type"] = return_name
        is_static = self._safe_get(op, "get_is_static")
        if is_static is not None:
            spec["is_static"] = bool(is_static)
        arguments = self._export_collection(op, "get_arguments")
        if arguments:
            spec["arguments"] = arguments
        return spec

    def _export_argument(self, arg: RPModelElement) -> Dict[str, Any]:
        spec: Dict[str, Any] = {"name": arg.get_name(), "type": "Argument"}
        type_classifier = self._safe_get(arg, "get_type")
        type_name = self.get_classifier_name(type_classifier) if type_classifier is not None else None
        if type_name:
            spec["data_type"] = type_name
        direction = self._safe_get(arg, "get_argument_direction")
        if direction:
            spec["direction"] = direction
        return spec

    def _export_attribute(self, attr: RPModelElement) -> Dict[str, Any]:
        spec: Dict[str, Any] = {"name": attr.get_name(), "type": "Attribute"}
        type_classifier = self._safe_get(attr, "get_type")
        type_name = self.get_classifier_name(type_classifier) if type_classifier is not None else None
        if type_name:
            spec["data_type"] = type_name
        visibility = self._safe_get(attr, "get_visibility")
        if visibility:
            spec["visibility"] = visibility
        multiplicity = self._safe_get(attr, "get_multiplicity")
        if multiplicity:
            spec["multiplicity"] = multiplicity
        is_static = self._safe_get(attr, "get_is_static")
        if is_static is not None:
            spec["is_static"] = bool(is_static)
        return spec

    def _export_object(self, obj: RPModelElement) -> Dict[str, Any]:
        spec: Dict[str, Any] = {"name": obj.get_name(), "type": "Object"}
        classifier = self._safe_get(obj, "get_classifier")
        classifier_name = self.get_classifier_name(classifier) if classifier is not None else None
        if classifier_name:
            spec["classifier"] = classifier_name
        return spec

    def _export_enumeration_literal(self, literal: RPModelElement) -> Dict[str, Any]:
        return {"name": literal.get_name(), "type": "EnumerationLiteral"}

    def _export_stereotypes(self, element: RPModelElement) -> List[str]:
        result: List[str] = []
        try:
            collection = element.get_stereotypes()
            for st in collection:
                try:
                    result.append(st.get_name())
                except Exception:
                    continue
        except Exception:
            return result
        return result

    def _export_tags(self, element: RPModelElement) -> Dict[str, str]:
        result: Dict[str, str] = {}
        try:
            collection = element.get_all_tags()
            for tag in collection:
                try:
                    name = tag.get_name()
                    value = tag.get_value()
                    if name and value is not None:
                        result[name] = str(value)
                except Exception:
                    continue
        except Exception:
            return result
        return result

    # --- Private helpers ---

    def _wrap_if_needed(self, element: Any) -> RPModelElement:
        if isinstance(element, RPModelElement):
            return element
        return RPModelElement.wrap(element)

    def _export_container(self, container: RPModelElement, type_name: str) -> Dict[str, Any]:
        spec: Dict[str, Any] = {"name": container.get_name(), "type": type_name}
        children = self._collect_children(container)
        child_specs = self._export_children(children)
        if child_specs:
            spec["children"] = child_specs
        return spec

    def _export_children(self, children: List[RPModelElement]) -> List[Dict[str, Any]]:
        result: List[Dict[str, Any]] = []
        for child in children:
            spec = self._export_element(child)
            if spec is not None:
                result.append(spec)
        return result

    def _export_collection(self, element: RPModelElement, method_name: str) -> List[Dict[str, Any]]:
        if not hasattr(element, method_name):
            return []
        collection = getattr(element, method_name)()
        if collection is None:
            return []
        result: List[Dict[str, Any]] = []
        for item in collection:
            spec = self._export_element(item)
            if spec is not None:
                result.append(spec)
        return result

    def _safe_get(self, element: RPModelElement, method_name: str) -> Any:
        if not hasattr(element, method_name):
            return None
        try:
            return getattr(element, method_name)()
        except Exception:
            return None

    def _attach_common_fields(self, spec: Dict[str, Any], element: RPModelElement) -> None:
        stereotypes = self._export_stereotypes(element)
        if stereotypes:
            spec["stereotypes"] = stereotypes
        tags = self._export_tags(element)
        if tags:
            spec["tags"] = tags
