from .StreamFramingType import StreamFramingType
from .StreamFramingDelimiter import StreamFramingDelimiter
import json
from typing import Dict
class StreamFraming: 
  def __init__(self, input: Dict):
    if 'type' in input:
      self._type: StreamFramingType = StreamFramingType(input['type'])
    if 'delimiter' in input:
      self._delimiter: StreamFramingDelimiter = StreamFramingDelimiter(input['delimiter'])

  @property
  def type(self) -> StreamFramingType:
    return self._type
  @type.setter
  def type(self, type: StreamFramingType):
    self._type = type

  @property
  def delimiter(self) -> StreamFramingDelimiter:
    return self._delimiter
  @delimiter.setter
  def delimiter(self, delimiter: StreamFramingDelimiter):
    self._delimiter = delimiter

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return StreamFraming(**json.loads(json_string))
