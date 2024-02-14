from .StreamFramingOneOf1Type import StreamFramingOneOf1Type
from .StreamFramingOneOf1Delimiter import StreamFramingOneOf1Delimiter
import json
from typing import Dict
class StreamFramingOneOf1: 
  def __init__(self, input: Dict):
    if hasattr(input, 'type'):
      self._type: StreamFramingOneOf1Type = StreamFramingOneOf1Type(input['type'])
    if hasattr(input, 'delimiter'):
      self._delimiter: StreamFramingOneOf1Delimiter = StreamFramingOneOf1Delimiter(input['delimiter'])

  @property
  def type(self) -> StreamFramingOneOf1Type:
    return self._type
  @type.setter
  def type(self, type: StreamFramingOneOf1Type):
    self._type = type

  @property
  def delimiter(self) -> StreamFramingOneOf1Delimiter:
    return self._delimiter
  @delimiter.setter
  def delimiter(self, delimiter: StreamFramingOneOf1Delimiter):
    self._delimiter = delimiter

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return StreamFramingOneOf1(**json.loads(json_string))
