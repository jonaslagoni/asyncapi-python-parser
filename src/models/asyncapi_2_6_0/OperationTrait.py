from .Tag import Tag
from .ExternalDocs import ExternalDocs
from .BindingsObject import BindingsObject
import json
from typing import Any, List, Dict
class OperationTrait: 
  def __init__(self, input: Dict):
    if hasattr(input, 'summary'):
      self._summary: str = input['summary']
    if hasattr(input, 'description'):
      self._description: str = input['description']
    if hasattr(input, 'tags'):
      self._tags: List[Tag] = input['tags']
    if hasattr(input, 'external_docs'):
      self._external_docs: ExternalDocs = ExternalDocs(input['external_docs'])
    if hasattr(input, 'operation_id'):
      self._operation_id: str = input['operation_id']
    if hasattr(input, 'security'):
      self._security: List[dict[str, List[str]]] = input['security']
    if hasattr(input, 'bindings'):
      self._bindings: BindingsObject = BindingsObject(input['bindings'])
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def summary(self) -> str:
    return self._summary
  @summary.setter
  def summary(self, summary: str):
    self._summary = summary

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

  @property
  def tags(self) -> List[Tag]:
    return self._tags
  @tags.setter
  def tags(self, tags: List[Tag]):
    self._tags = tags

  @property
  def external_docs(self) -> ExternalDocs:
    return self._external_docs
  @external_docs.setter
  def external_docs(self, external_docs: ExternalDocs):
    self._external_docs = external_docs

  @property
  def operation_id(self) -> str:
    return self._operation_id
  @operation_id.setter
  def operation_id(self, operation_id: str):
    self._operation_id = operation_id

  @property
  def security(self) -> List[dict[str, List[str]]]:
    return self._security
  @security.setter
  def security(self, security: List[dict[str, List[str]]]):
    self._security = security

  @property
  def bindings(self) -> BindingsObject:
    return self._bindings
  @bindings.setter
  def bindings(self, bindings: BindingsObject):
    self._bindings = bindings

  @property
  def additional_properties(self) -> dict[str, Any]:
    return self._additional_properties
  @additional_properties.setter
  def additional_properties(self, additional_properties: dict[str, Any]):
    self._additional_properties = additional_properties

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return OperationTrait(**json.loads(json_string))
