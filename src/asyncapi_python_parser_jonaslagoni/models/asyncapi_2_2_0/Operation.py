from __future__ import annotations
import json
from typing import Any, List, Dict
from . import Reference
from . import OperationTrait
from . import Tag
from . import ExternalDocs
from . import BindingsObject
from . import MessageOneOf1OneOf0
from . import MessageOneOf1OneOf1
class Operation: 
  def __init__(self, input: Dict):
    if 'traits' in input:
      self._traits: List[Reference.Reference | OperationTrait.OperationTrait] = input['traits']
    if 'summary' in input:
      self._summary: str = input['summary']
    if 'description' in input:
      self._description: str = input['description']
    if 'tags' in input:
      self._tags: List[Tag.Tag] = input['tags']
    if 'external_docs' in input:
      self._external_docs: ExternalDocs.ExternalDocs = ExternalDocs.ExternalDocs(input['external_docs'])
    if 'operation_id' in input:
      self._operation_id: str = input['operation_id']
    if 'bindings' in input:
      self._bindings: BindingsObject.BindingsObject = BindingsObject.BindingsObject(input['bindings'])
    if 'message' in input:
      self._message: Reference.Reference | MessageOneOf1OneOf0.MessageOneOf1OneOf0 | MessageOneOf1OneOf1.MessageOneOf1OneOf1 = input['message']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def traits(self) -> List[Reference.Reference | OperationTrait.OperationTrait]:
    return self._traits
  @traits.setter
  def traits(self, traits: List[Reference.Reference | OperationTrait.OperationTrait]):
    self._traits = traits

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
  def tags(self) -> List[Tag.Tag]:
    return self._tags
  @tags.setter
  def tags(self, tags: List[Tag.Tag]):
    self._tags = tags

  @property
  def external_docs(self) -> ExternalDocs.ExternalDocs:
    return self._external_docs
  @external_docs.setter
  def external_docs(self, external_docs: ExternalDocs.ExternalDocs):
    self._external_docs = external_docs

  @property
  def operation_id(self) -> str:
    return self._operation_id
  @operation_id.setter
  def operation_id(self, operation_id: str):
    self._operation_id = operation_id

  @property
  def bindings(self) -> BindingsObject.BindingsObject:
    return self._bindings
  @bindings.setter
  def bindings(self, bindings: BindingsObject.BindingsObject):
    self._bindings = bindings

  @property
  def message(self) -> Reference.Reference | MessageOneOf1OneOf0.MessageOneOf1OneOf0 | MessageOneOf1OneOf1.MessageOneOf1OneOf1:
    return self._message
  @message.setter
  def message(self, message: Reference.Reference | MessageOneOf1OneOf0.MessageOneOf1OneOf0 | MessageOneOf1OneOf1.MessageOneOf1OneOf1):
    self._message = message

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
    return Operation(**json.loads(json_string))
