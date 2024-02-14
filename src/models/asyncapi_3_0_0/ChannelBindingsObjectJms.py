from .ChannelBindingsObjectJmsBindingVersion import ChannelBindingsObjectJmsBindingVersion
from .BindingsMinusJmsMinus0Dot0Dot1MinusChannelDestinationType import BindingsMinusJmsMinus0Dot0Dot1MinusChannelDestinationType
import json
from typing import Any, Dict
class ChannelBindingsObjectJms: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: ChannelBindingsObjectJmsBindingVersion = ChannelBindingsObjectJmsBindingVersion(input['binding_version'])
    if hasattr(input, 'destination'):
      self._destination: str = input['destination']
    if hasattr(input, 'destination_type'):
      self._destination_type: BindingsMinusJmsMinus0Dot0Dot1MinusChannelDestinationType = BindingsMinusJmsMinus0Dot0Dot1MinusChannelDestinationType(input['destination_type'])
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> ChannelBindingsObjectJmsBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ChannelBindingsObjectJmsBindingVersion):
    self._binding_version = binding_version

  @property
  def destination(self) -> str:
    return self._destination
  @destination.setter
  def destination(self, destination: str):
    self._destination = destination

  @property
  def destination_type(self) -> BindingsMinusJmsMinus0Dot0Dot1MinusChannelDestinationType:
    return self._destination_type
  @destination_type.setter
  def destination_type(self, destination_type: BindingsMinusJmsMinus0Dot0Dot1MinusChannelDestinationType):
    self._destination_type = destination_type

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
    return ChannelBindingsObjectJms(**json.loads(json_string))
