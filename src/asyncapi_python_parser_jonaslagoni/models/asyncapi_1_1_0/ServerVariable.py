from __future__ import annotations
import json
from typing import List, Any, Dict

class ServerVariable: 
  def __init__(self, input: Dict):
    if 'enum' in input:
      self._enum: List[str] = input['enum']
    if 'default' in input:
      self._default: str = input['default']
    if 'description' in input:
      self._description: str = input['description']
    if 'additional_properties' in input:
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