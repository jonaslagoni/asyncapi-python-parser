from .Reference import Reference
from .Message1 import Message1
import json
from typing import Any, List, Dict
class Message: 
  def __init__(self, input: Dict):
    self._one_of: List[Reference | Message | Message1] = input['one_of']

  @property
  def one_of(self) -> List[Reference | Message | Message1]:
    return self._one_of
  @one_of.setter
  def one_of(self, one_of: List[Reference | Message | Message1]):
    self._one_of = one_of

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return Message(**json.loads(json_string))
