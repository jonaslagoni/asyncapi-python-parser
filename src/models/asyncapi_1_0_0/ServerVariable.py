
import json
from typing import List, Any, Dict
class ServerVariable: 
  def __init__(self, input: Dict):
    if hasattr(input, 'enum'):
      self._enum: List[str] = input['enum']
    if hasattr(input, 'default'):
      self._default: str = input['default']
    if hasattr(input, 'description'):
      self._description: str = input['description']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def enum(self) -> List[str]:
    return self._enum
  @enum.setter
  def enum(self, enum: List[str]):
    self._enum = enum

  @property
  def default(self) -> str:
    return self._default
  @default.setter
  def default(self, default: str):
    self._default = default

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

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
    return ServerVariable(**json.loads(json_string))
