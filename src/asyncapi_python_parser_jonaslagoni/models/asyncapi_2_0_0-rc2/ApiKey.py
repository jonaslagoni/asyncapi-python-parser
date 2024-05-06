from __future__ import annotations
import json
from typing import Any, Dict
from . import ApiKeyType
from . import ApiKeyIn
class ApiKey: 
  def __init__(self, input: Dict):
    self._type: ApiKeyType.ApiKeyType = ApiKeyType.ApiKeyType(input['type'])
    self._reserved_in: ApiKeyIn.ApiKeyIn = ApiKeyIn.ApiKeyIn(input['reserved_in'])
    if 'description' in input:
      self._description: str = input['description']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def type(self) -> ApiKeyType.ApiKeyType:
    return self._type
  @type.setter
  def type(self, type: ApiKeyType.ApiKeyType):
    self._type = type

  @property
  def reserved_in(self) -> ApiKeyIn.ApiKeyIn:
    return self._reserved_in
  @reserved_in.setter
  def reserved_in(self, reserved_in: ApiKeyIn.ApiKeyIn):
    self._reserved_in = reserved_in

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
    return ApiKey(**json.loads(json_string))
