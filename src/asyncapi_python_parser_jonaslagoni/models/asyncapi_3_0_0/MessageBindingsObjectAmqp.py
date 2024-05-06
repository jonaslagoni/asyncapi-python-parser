from __future__ import annotations
import json
from typing import Any, Dict
from . import MessageBindingsObjectAmqpBindingVersion
class MessageBindingsObjectAmqp: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: MessageBindingsObjectAmqpBindingVersion.MessageBindingsObjectAmqpBindingVersion = MessageBindingsObjectAmqpBindingVersion.MessageBindingsObjectAmqpBindingVersion(input['binding_version'])
    if 'content_encoding' in input:
      self._content_encoding: str = input['content_encoding']
    if 'message_type' in input:
      self._message_type: str = input['message_type']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def binding_version(self) -> MessageBindingsObjectAmqpBindingVersion.MessageBindingsObjectAmqpBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: MessageBindingsObjectAmqpBindingVersion.MessageBindingsObjectAmqpBindingVersion):
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
  def extensions(self) -> dict[str, Any]:
    return self._extensions
  @extensions.setter
  def extensions(self, extensions: dict[str, Any]):
    self._extensions = extensions

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return MessageBindingsObjectAmqp(**json.loads(json_string))
