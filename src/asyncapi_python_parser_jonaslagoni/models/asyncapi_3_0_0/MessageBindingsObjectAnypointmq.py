from __future__ import annotations
import json
from typing import Any, List, Dict
from . import MessageBindingsObjectAnypointmqBindingVersion
from . import SchemaObject
from . import Reference
class MessageBindingsObjectAnypointmq: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: MessageBindingsObjectAnypointmqBindingVersion.MessageBindingsObjectAnypointmqBindingVersion = MessageBindingsObjectAnypointmqBindingVersion.MessageBindingsObjectAnypointmqBindingVersion(input['binding_version'])
    if 'headers' in input:
      self._headers: SchemaObject.SchemaObject | bool | Reference.Reference = input['headers']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def binding_version(self) -> MessageBindingsObjectAnypointmqBindingVersion.MessageBindingsObjectAnypointmqBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: MessageBindingsObjectAnypointmqBindingVersion.MessageBindingsObjectAnypointmqBindingVersion):
    self._binding_version = binding_version

  @property
  def headers(self) -> SchemaObject.SchemaObject | bool | Reference.Reference:
    return self._headers
  @headers.setter
  def headers(self, headers: SchemaObject.SchemaObject | bool | Reference.Reference):
    self._headers = headers

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
    return MessageBindingsObjectAnypointmq(**json.loads(json_string))
