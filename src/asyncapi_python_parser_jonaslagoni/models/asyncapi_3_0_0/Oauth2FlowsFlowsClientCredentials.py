from __future__ import annotations
import json
from typing import Any, Dict

class Oauth2FlowsFlowsClientCredentials: 
  def __init__(self, input: Dict):
    if 'authorization_url' in input:
      self._authorization_url: str = input['authorization_url']
    self._token_url: str = input['token_url']
    if 'refresh_url' in input:
      self._refresh_url: str = input['refresh_url']
    self._available_scopes: dict[str, str] = input['available_scopes']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

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
  def available_scopes(self) -> dict[str, str]:
    return self._available_scopes
  @available_scopes.setter
  def available_scopes(self, available_scopes: dict[str, str]):
    self._available_scopes = available_scopes

  @property
  def extensions(self) -> dict[str, Any]:
    return self._extensions
  @extensions.setter
  def extensions(self, extensions: dict[str, Any]):
    self._extensions = extensions

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return Oauth2FlowsFlowsClientCredentials(**json.loads(json_string))
