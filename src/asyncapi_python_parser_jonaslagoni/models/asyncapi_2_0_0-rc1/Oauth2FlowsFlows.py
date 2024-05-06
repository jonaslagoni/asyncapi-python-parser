from __future__ import annotations
import json
from typing import Any, Dict
from . import Oauth2FlowsFlowsImplicit
from . import Oauth2FlowsFlowsPassword
from . import Oauth2FlowsFlowsClientCredentials
from . import Oauth2FlowsFlowsAuthorizationCode
class Oauth2FlowsFlows: 
  def __init__(self, input: Dict):
    if 'implicit' in input:
      self._implicit: Oauth2FlowsFlowsImplicit.Oauth2FlowsFlowsImplicit = Oauth2FlowsFlowsImplicit.Oauth2FlowsFlowsImplicit(input['implicit'])
    if 'password' in input:
      self._password: Oauth2FlowsFlowsPassword.Oauth2FlowsFlowsPassword = Oauth2FlowsFlowsPassword.Oauth2FlowsFlowsPassword(input['password'])
    if 'client_credentials' in input:
      self._client_credentials: Oauth2FlowsFlowsClientCredentials.Oauth2FlowsFlowsClientCredentials = Oauth2FlowsFlowsClientCredentials.Oauth2FlowsFlowsClientCredentials(input['client_credentials'])
    if 'authorization_code' in input:
      self._authorization_code: Oauth2FlowsFlowsAuthorizationCode.Oauth2FlowsFlowsAuthorizationCode = Oauth2FlowsFlowsAuthorizationCode.Oauth2FlowsFlowsAuthorizationCode(input['authorization_code'])

  @property
  def implicit(self) -> Oauth2FlowsFlowsImplicit.Oauth2FlowsFlowsImplicit:
    return self._implicit
  @implicit.setter
  def implicit(self, implicit: Oauth2FlowsFlowsImplicit.Oauth2FlowsFlowsImplicit):
    self._implicit = implicit

  @property
  def password(self) -> Oauth2FlowsFlowsPassword.Oauth2FlowsFlowsPassword:
    return self._password
  @password.setter
  def password(self, password: Oauth2FlowsFlowsPassword.Oauth2FlowsFlowsPassword):
    self._password = password

  @property
  def client_credentials(self) -> Oauth2FlowsFlowsClientCredentials.Oauth2FlowsFlowsClientCredentials:
    return self._client_credentials
  @client_credentials.setter
  def client_credentials(self, client_credentials: Oauth2FlowsFlowsClientCredentials.Oauth2FlowsFlowsClientCredentials):
    self._client_credentials = client_credentials

  @property
  def authorization_code(self) -> Oauth2FlowsFlowsAuthorizationCode.Oauth2FlowsFlowsAuthorizationCode:
    return self._authorization_code
  @authorization_code.setter
  def authorization_code(self, authorization_code: Oauth2FlowsFlowsAuthorizationCode.Oauth2FlowsFlowsAuthorizationCode):
    self._authorization_code = authorization_code

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return Oauth2FlowsFlows(**json.loads(json_string))
