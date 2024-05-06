from .StreamFramingType1 import StreamFramingType1
from .StreamFramingDelimiter1 import StreamFramingDelimiter1
import json
from typing import Dict
class StreamFraming1: 
  def __init__(self, input: Dict):
    if 'type' in input:
      self._type: StreamFramingType1 = StreamFramingType1(input['type'])
    if 'delimiter' in input:
      self._delimiter: StreamFramingDelimiter1 = StreamFramingDelimiter1(input['delimiter'])

  @property
  def type(self) -> StreamFramingType1:
    return self._type
  @type.setter
  def type(self, type: StreamFramingType1):
    self._type = type

  @property
  def delimiter(self) -> StreamFramingDelimiter1:
    return self._delimiter
  @delimiter.setter
  def delimiter(self, delimiter: StreamFramingDelimiter1):
    self._delimiter = delimiter

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return StreamFraming1(**json.loads(json_string))
