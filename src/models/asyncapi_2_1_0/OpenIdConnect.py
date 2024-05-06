from __future__ import annotations
import json
from typing import Any, Dict
from . import OpenIdConnectType
class OpenIdConnect: 
  def __init__(self, input: Dict):
    self._type: OpenIdConnectType.OpenIdConnectType = OpenIdConnectType.OpenIdConnectType(input['type'])
    if 'description' in input:
      self._description: str = input['description']
    self._open_id_connect_url: str = input['open_id_connect_url']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def type(self) -> OpenIdConnectType.OpenIdConnectType:
    return self._type
  @type.setter
  def type(self, type: OpenIdConnectType.OpenIdConnectType):
    self._type = type

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

  @property
  def open_id_connect_url(self) -> str:
    return self._open_id_connect_url
  @open_id_connect_url.setter
  def open_id_connect_url(self, open_id_connect_url: str):
    self._open_id_connect_url = open_id_connect_url

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
    return OpenIdConnect(**json.loads(json_string))
