from .MessageBindingsObjectAnypointmqBindingVersion import MessageBindingsObjectAnypointmqBindingVersion
from .SchemaObject import SchemaObject
from .Reference import Reference
import json
from typing import Any, List, Dict
class MessageBindingsObjectAnypointmq: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: MessageBindingsObjectAnypointmqBindingVersion = MessageBindingsObjectAnypointmqBindingVersion(input['binding_version'])
    if hasattr(input, 'headers'):
      self._headers: SchemaObject | bool | Reference = input['headers']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> MessageBindingsObjectAnypointmqBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: MessageBindingsObjectAnypointmqBindingVersion):
    self._binding_version = binding_version

  @property
  def headers(self) -> SchemaObject | bool | Reference:
    return self._headers
  @headers.setter
  def headers(self, headers: SchemaObject | bool | Reference):
    self._headers = headers

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
    return MessageBindingsObjectAnypointmq(**json.loads(json_string))
