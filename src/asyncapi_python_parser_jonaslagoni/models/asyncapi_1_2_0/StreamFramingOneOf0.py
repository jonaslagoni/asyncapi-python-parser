from __future__ import annotations
import json
from typing import Dict
from . import StreamFramingOneOf0Type
from . import StreamFramingOneOf0Delimiter
class StreamFramingOneOf0: 
  def __init__(self, input: Dict):
    if 'type' in input:
      self._type: StreamFramingOneOf0Type.StreamFramingOneOf0Type = StreamFramingOneOf0Type.StreamFramingOneOf0Type(input['type'])
    if 'delimiter' in input:
      self._delimiter: StreamFramingOneOf0Delimiter.StreamFramingOneOf0Delimiter = StreamFramingOneOf0Delimiter.StreamFramingOneOf0Delimiter(input['delimiter'])

  @property
  def type(self) -> StreamFramingOneOf0Type.StreamFramingOneOf0Type:
    return self._type
  @type.setter
  def type(self, type: StreamFramingOneOf0Type.StreamFramingOneOf0Type):
    self._type = type

  @property
  def delimiter(self) -> StreamFramingOneOf0Delimiter.StreamFramingOneOf0Delimiter:
    return self._delimiter
  @delimiter.setter
  def delimiter(self, delimiter: StreamFramingOneOf0Delimiter.StreamFramingOneOf0Delimiter):
    self._delimiter = delimiter

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return StreamFramingOneOf0(**json.loads(json_string))
