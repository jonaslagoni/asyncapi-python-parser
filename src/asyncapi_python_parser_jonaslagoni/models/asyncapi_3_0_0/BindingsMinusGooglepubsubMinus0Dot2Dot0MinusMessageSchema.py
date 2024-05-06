from __future__ import annotations
import json
from typing import Any, Dict

class BindingsMinusGooglepubsubMinus0Dot2Dot0MinusMessageSchema: 
  def __init__(self, input: Dict):
    self._name: str = input['name']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def name(self) -> str:
    return self._name
  @name.setter
  def name(self, name: str):
    self._name = name

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
    return BindingsMinusGooglepubsubMinus0Dot2Dot0MinusMessageSchema(**json.loads(json_string))