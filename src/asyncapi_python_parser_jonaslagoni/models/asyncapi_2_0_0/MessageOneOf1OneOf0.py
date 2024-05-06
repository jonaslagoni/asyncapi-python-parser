from __future__ import annotations
import json
from typing import Any, List, Dict
from . import Reference
from . import MessageOneOf1OneOf1
class MessageOneOf1OneOf0: 
  def __init__(self, input: Dict):
    self._one_of: List[Reference.Reference | MessageOneOf1OneOf0 | MessageOneOf1OneOf1.MessageOneOf1OneOf1] = input['one_of']

  @property
  def one_of(self) -> List[Reference.Reference | MessageOneOf1OneOf0 | MessageOneOf1OneOf1.MessageOneOf1OneOf1]:
    return self._one_of
  @one_of.setter
  def one_of(self, one_of: List[Reference.Reference | MessageOneOf1OneOf0 | MessageOneOf1OneOf1.MessageOneOf1OneOf1]):
    self._one_of = one_of

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return MessageOneOf1OneOf0(**json.loads(json_string))
