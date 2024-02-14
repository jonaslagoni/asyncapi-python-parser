from .StreamFramingOneOf0 import StreamFramingOneOf0
from .StreamFramingOneOf1 import StreamFramingOneOf1
from .Message import Message
import json
from typing import Any, List, Dict
class StreamObject: 
  def __init__(self, input: Dict):
    if hasattr(input, 'framing'):
      self._framing: StreamFramingOneOf0 | StreamFramingOneOf1 = input['framing']
    if hasattr(input, 'read'):
      self._read: List[Message] = input['read']
    if hasattr(input, 'write'):
      self._write: List[Message] = input['write']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def framing(self) -> StreamFramingOneOf0 | StreamFramingOneOf1:
    return self._framing
  @framing.setter
  def framing(self, framing: StreamFramingOneOf0 | StreamFramingOneOf1):
    self._framing = framing

  @property
  def read(self) -> List[Message]:
    return self._read
  @read.setter
  def read(self, read: List[Message]):
    self._read = read

  @property
  def write(self) -> List[Message]:
    return self._write
  @write.setter
  def write(self, write: List[Message]):
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
