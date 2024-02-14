from .MessageBindingsObjectAmqpBindingVersion import MessageBindingsObjectAmqpBindingVersion
import json
from typing import Any, Dict
class MessageBindingsObjectAmqp: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: MessageBindingsObjectAmqpBindingVersion = MessageBindingsObjectAmqpBindingVersion(input['binding_version'])
    if hasattr(input, 'content_encoding'):
      self._content_encoding: str = input['content_encoding']
    if hasattr(input, 'message_type'):
      self._message_type: str = input['message_type']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> MessageBindingsObjectAmqpBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: MessageBindingsObjectAmqpBindingVersion):
    self._binding_version = binding_version

  @property
  def content_encoding(self) -> str:
    return self._content_encoding
  @content_encoding.setter
  def content_encoding(self, content_encoding: str):
    self._content_encoding = content_encoding

  @property
  def message_type(self) -> str:
    return self._message_type
  @message_type.setter
  def message_type(self, message_type: str):
    self._message_type = message_type

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
    return MessageBindingsObjectAmqp(**json.loads(json_string))
