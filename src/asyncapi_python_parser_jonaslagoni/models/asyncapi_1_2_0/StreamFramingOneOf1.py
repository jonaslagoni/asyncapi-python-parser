from __future__ import annotations
import json
from typing import Dict
from . import StreamFramingOneOf1Type
from . import StreamFramingOneOf1Delimiter
class StreamFramingOneOf1: 
  def __init__(self, input: Dict):
    if 'type' in input:
      self._type: StreamFramingOneOf1Type.StreamFramingOneOf1Type = StreamFramingOneOf1Type.StreamFramingOneOf1Type(input['type'])
    if 'delimiter' in input:
      self._delimiter: StreamFramingOneOf1Delimiter.StreamFramingOneOf1Delimiter = StreamFramingOneOf1Delimiter.StreamFramingOneOf1Delimiter(input['delimiter'])

  @property
  def type(self) -> StreamFramingOneOf1Type.StreamFramingOneOf1Type:
    return self._type
  @type.setter
  def type(self, type: StreamFramingOneOf1Type.StreamFramingOneOf1Type):
    self._type = type

  @property
  def delimiter(self) -> StreamFramingOneOf1Delimiter.StreamFramingOneOf1Delimiter:
    return self._delimiter
  @delimiter.setter
  def delimiter(self, delimiter: StreamFramingOneOf1Delimiter.StreamFramingOneOf1Delimiter):
    self._delimiter = delimiter

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return StreamFramingOneOf1(**json.loads(json_string))
