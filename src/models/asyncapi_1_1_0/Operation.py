from .Message import Message
import json
from typing import Any, List, Dict
class Operation: 
  def __init__(self, input: Dict):
    self._one_of: List[Message] = input['one_of']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def one_of(self) -> List[Message]:
    return self._one_of
  @one_of.setter
  def one_of(self, one_of: List[Message]):
    self._one_of = one_of

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
    return Operation(**json.loads(json_string))
