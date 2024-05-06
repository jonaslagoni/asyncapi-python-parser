from __future__ import annotations
import json
from typing import Any, Dict
from . import ChannelBindingsObjectAmqpBindingVersion
class ChannelBindingsObjectAmqp: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: ChannelBindingsObjectAmqpBindingVersion.ChannelBindingsObjectAmqpBindingVersion = ChannelBindingsObjectAmqpBindingVersion.ChannelBindingsObjectAmqpBindingVersion(input['binding_version'])
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def binding_version(self) -> ChannelBindingsObjectAmqpBindingVersion.ChannelBindingsObjectAmqpBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ChannelBindingsObjectAmqpBindingVersion.ChannelBindingsObjectAmqpBindingVersion):
    self._binding_version = binding_version

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
    return ChannelBindingsObjectAmqp(**json.loads(json_string))
