from .Reference import Reference
from .OperationTrait import OperationTrait
from .Tag import Tag
from .ExternalDocs import ExternalDocs
from .Message import Message
from .OperationMessageOneOf1 import OperationMessageOneOf1
import json
from typing import Any, List, Dict
class Operation: 
  def __init__(self, input: Dict):
    if hasattr(input, 'traits'):
      self._traits: List[Reference | OperationTrait] = input['traits']
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
    if hasattr(input, 'protocol_info'):
      self._protocol_info: dict[str, dict[str, Any]] = input['protocol_info']
    if hasattr(input, 'message'):
      self._message: Message | OperationMessageOneOf1 = input['message']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def traits(self) -> List[Reference | OperationTrait]:
    return self._traits
  @traits.setter
  def traits(self, traits: List[Reference | OperationTrait]):
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
  def protocol_info(self) -> dict[str, dict[str, Any]]:
    return self._protocol_info
  @protocol_info.setter
  def protocol_info(self, protocol_info: dict[str, dict[str, Any]]):
    self._protocol_info = protocol_info

  @property
  def message(self) -> Message | OperationMessageOneOf1:
    return self._message
  @message.setter
  def message(self, message: Message | OperationMessageOneOf1):
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
