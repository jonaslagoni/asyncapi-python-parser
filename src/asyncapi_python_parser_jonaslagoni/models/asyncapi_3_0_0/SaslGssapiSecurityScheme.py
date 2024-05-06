from __future__ import annotations
import json
from typing import Any, Dict
from . import SaslGssapiSecuritySchemeType
class SaslGssapiSecurityScheme: 
  def __init__(self, input: Dict):
    self._type: SaslGssapiSecuritySchemeType.SaslGssapiSecuritySchemeType = SaslGssapiSecuritySchemeType.SaslGssapiSecuritySchemeType(input['type'])
    if 'description' in input:
      self._description: str = input['description']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def type(self) -> SaslGssapiSecuritySchemeType.SaslGssapiSecuritySchemeType:
    return self._type
  @type.setter
  def type(self, type: SaslGssapiSecuritySchemeType.SaslGssapiSecuritySchemeType):
    self._type = type

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
    return SaslGssapiSecurityScheme(**json.loads(json_string))
