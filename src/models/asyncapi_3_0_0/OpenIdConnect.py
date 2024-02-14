from .OpenIdConnectType import OpenIdConnectType
import json
from typing import List, Any, Dict
class OpenIdConnect: 
  def __init__(self, input: Dict):
    self._type: OpenIdConnectType = OpenIdConnectType(input['type'])
    if hasattr(input, 'description'):
      self._description: str = input['description']
    self._open_id_connect_url: str = input['open_id_connect_url']
    if hasattr(input, 'scopes'):
      self._scopes: List[str] = input['scopes']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def type(self) -> OpenIdConnectType:
    return self._type
  @type.setter
  def type(self, type: OpenIdConnectType):
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
  def scopes(self) -> List[str]:
    return self._scopes
  @scopes.setter
  def scopes(self, scopes: List[str]):
    self._scopes = scopes

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
