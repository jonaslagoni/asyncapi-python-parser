from __future__ import annotations
import json
from typing import Any, Dict
from . import BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion
class ChannelSchema: 
  def __init__(self, input: Dict):
    self._queue: ChannelSchema = ChannelSchema(input['queue'])
    if 'dead_letter_queue' in input:
      self._dead_letter_queue: ChannelSchema = ChannelSchema(input['dead_letter_queue'])
    if 'binding_version' in input:
      self._binding_version: BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion.BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion = BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion.BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion(input['binding_version'])
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

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
  def binding_version(self) -> BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion.BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion.BindingsMinusSqsMinus0Dot2Dot0MinusChannelBindingVersion):
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
    return ChannelSchema(**json.loads(json_string))
