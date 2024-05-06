from __future__ import annotations
import json
from typing import Any, Dict

class Oauth2FlowsFlowsAuthorizationCode: 
  def __init__(self, input: Dict):
    self._authorization_url: str = input['authorization_url']
    self._token_url: str = input['token_url']
    if 'refresh_url' in input:
      self._refresh_url: str = input['refresh_url']
    self._scopes: dict[str, str] = input['scopes']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def authorization_url(self) -> str:
    return self._authorization_url
  @authorization_url.setter
  def authorization_url(self, authorization_url: str):
    self._authorization_url = authorization_url

  @property
  def token_url(self) -> str:
    return self._token_url
  @token_url.setter
  def token_url(self, token_url: str):
    self._token_url = token_url

  @property
  def refresh_url(self) -> str:
    return self._refresh_url
  @refresh_url.setter
  def refresh_url(self, refresh_url: str):
    self._refresh_url = refresh_url

  @property
  def scopes(self) -> dict[str, str]:
    return self._scopes
  @scopes.setter
  def scopes(self, scopes: dict[str, str]):
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
    return Oauth2FlowsFlowsAuthorizationCode(**json.loads(json_string))
