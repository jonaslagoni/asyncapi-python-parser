from .PrimitiveType import PrimitiveType
import json
from typing import Any, Dict
class PrimitiveTypeWithMetadata: 
  def __init__(self, input: Dict):
    self._type: PrimitiveType = PrimitiveType(input['type'])
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def type(self) -> PrimitiveType:
    return self._type
  @type.setter
  def type(self, type: PrimitiveType):
    self._type = type

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
    return PrimitiveTypeWithMetadata(**json.loads(json_string))
