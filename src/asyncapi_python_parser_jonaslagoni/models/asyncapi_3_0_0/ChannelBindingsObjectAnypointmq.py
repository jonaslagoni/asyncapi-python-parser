from __future__ import annotations
import json
from typing import Any, Dict
from . import ChannelBindingsObjectAnypointmqBindingVersion
from . import BindingsMinusAnypointmqMinus0Dot0Dot1MinusChannelDestinationType
class ChannelBindingsObjectAnypointmq: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: ChannelBindingsObjectAnypointmqBindingVersion.ChannelBindingsObjectAnypointmqBindingVersion = ChannelBindingsObjectAnypointmqBindingVersion.ChannelBindingsObjectAnypointmqBindingVersion(input['binding_version'])
    if 'destination' in input:
      self._destination: str = input['destination']
    if 'destination_type' in input:
      self._destination_type: BindingsMinusAnypointmqMinus0Dot0Dot1MinusChannelDestinationType.BindingsMinusAnypointmqMinus0Dot0Dot1MinusChannelDestinationType = BindingsMinusAnypointmqMinus0Dot0Dot1MinusChannelDestinationType.BindingsMinusAnypointmqMinus0Dot0Dot1MinusChannelDestinationType(input['destination_type'])
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def binding_version(self) -> ChannelBindingsObjectAnypointmqBindingVersion.ChannelBindingsObjectAnypointmqBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ChannelBindingsObjectAnypointmqBindingVersion.ChannelBindingsObjectAnypointmqBindingVersion):
    self._binding_version = binding_version

  @property
  def destination(self) -> str:
    return self._destination
  @destination.setter
  def destination(self, destination: str):
    self._destination = destination

  @property
  def destination_type(self) -> BindingsMinusAnypointmqMinus0Dot0Dot1MinusChannelDestinationType.BindingsMinusAnypointmqMinus0Dot0Dot1MinusChannelDestinationType:
    return self._destination_type
  @destination_type.setter
  def destination_type(self, destination_type: BindingsMinusAnypointmqMinus0Dot0Dot1MinusChannelDestinationType.BindingsMinusAnypointmqMinus0Dot0Dot1MinusChannelDestinationType):
    self._destination_type = destination_type

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
    return ChannelBindingsObjectAnypointmq(**json.loads(json_string))
