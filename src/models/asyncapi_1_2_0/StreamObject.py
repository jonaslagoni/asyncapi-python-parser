from __future__ import annotations
import json
from typing import Any, List, Dict
from . import StreamFramingOneOf0
from . import StreamFramingOneOf1
from . import Message
class StreamObject: 
  def __init__(self, input: Dict):
    if 'framing' in input:
      self._framing: StreamFramingOneOf0.StreamFramingOneOf0 | StreamFramingOneOf1.StreamFramingOneOf1 = input['framing']
    if 'read' in input:
      self._read: List[Message.Message] = input['read']
    if 'write' in input:
      self._write: List[Message.Message] = input['write']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def framing(self) -> StreamFramingOneOf0.StreamFramingOneOf0 | StreamFramingOneOf1.StreamFramingOneOf1:
    return self._framing
  @framing.setter
  def framing(self, framing: StreamFramingOneOf0.StreamFramingOneOf0 | StreamFramingOneOf1.StreamFramingOneOf1):
    self._framing = framing

  @property
  def read(self) -> List[Message.Message]:
    return self._read
  @read.setter
  def read(self, read: List[Message.Message]):
    self._read = read

  @property
  def write(self) -> List[Message.Message]:
    return self._write
  @write.setter
  def write(self, write: List[Message.Message]):
    self._write = write

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
    return StreamObject(**json.loads(json_string))
