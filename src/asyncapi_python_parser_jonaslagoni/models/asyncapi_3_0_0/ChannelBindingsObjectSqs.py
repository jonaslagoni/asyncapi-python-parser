from __future__ import annotations
import json
from typing import Any, Dict
from . import BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion
from . import ChannelSchema
class ChannelBindingsObjectSqs: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion.BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion = BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion.BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion(input['binding_version'])
    if 'queue' in input:
      self._queue: ChannelSchema.ChannelSchema = ChannelSchema.ChannelSchema(input['queue'])
    if 'dead_letter_queue' in input:
      self._dead_letter_queue: ChannelSchema.ChannelSchema = ChannelSchema.ChannelSchema(input['dead_letter_queue'])
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion.BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion.BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion):
    self._binding_version = binding_version

  @property
  def queue(self) -> ChannelSchema.ChannelSchema:
    return self._queue
  @queue.setter
  def queue(self, queue: ChannelSchema.ChannelSchema):
    self._queue = queue

  @property
  def dead_letter_queue(self) -> ChannelSchema.ChannelSchema:
    return self._dead_letter_queue
  @dead_letter_queue.setter
  def dead_letter_queue(self, dead_letter_queue: ChannelSchema.ChannelSchema):
    self._dead_letter_queue = dead_letter_queue

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
    return ChannelBindingsObjectSqs(**json.loads(json_string))
