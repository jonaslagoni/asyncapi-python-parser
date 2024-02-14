from .BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion import BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion
import json
from typing import Any, Dict
class ChannelSchema: 
  def __init__(self, input: Dict):
    self._queue: ChannelSchema = ChannelSchema(input['queue'])
    if hasattr(input, 'dead_letter_queue'):
      self._dead_letter_queue: ChannelSchema = ChannelSchema(input['dead_letter_queue'])
    if hasattr(input, 'binding_version'):
      self._binding_version: BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion = BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion(input['binding_version'])
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def queue(self) -> ChannelSchema:
    return self._queue
  @queue.setter
  def queue(self, queue: ChannelSchema):
    self._queue = queue

  @property
  def dead_letter_queue(self) -> ChannelSchema:
    return self._dead_letter_queue
  @dead_letter_queue.setter
  def dead_letter_queue(self, dead_letter_queue: ChannelSchema):
    self._dead_letter_queue = dead_letter_queue

  @property
  def binding_version(self) -> BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion):
    self._binding_version = binding_version

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
    return ChannelSchema(**json.loads(json_string))
