from __future__ import annotations
import json
from typing import Any, List, Dict
from . import Schema
from . import Message
from . import Reference
from . import UserPassword
from . import ApiKey
from . import X509
from . import SymmetricEncryption
from . import AsymmetricEncryption
from . import BearerHttpSecurityScheme
from . import ApiKeyHttpSecurityScheme
class Components: 
  def __init__(self, input: Dict):
    if 'schemas' in input:
      self._schemas: dict[str, Schema.Schema] = input['schemas']
    if 'messages' in input:
      self._messages: dict[str, Message.Message] = input['messages']
    if 'security_schemes' in input:
      self._security_schemes: dict[str, Any | Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme] = input['security_schemes']

  @property
  def schemas(self) -> dict[str, Schema.Schema]:
    return self._schemas
  @schemas.setter
  def schemas(self, schemas: dict[str, Schema.Schema]):
    self._schemas = schemas

  @property
  def messages(self) -> dict[str, Message.Message]:
    return self._messages
  @messages.setter
  def messages(self, messages: dict[str, Message.Message]):
    self._messages = messages

  @property
  def security_schemes(self) -> dict[str, Any | Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme]:
    return self._security_schemes
  @security_schemes.setter
  def security_schemes(self, security_schemes: dict[str, Any | Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme]):
    self._security_schemes = security_schemes

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return Components(**json.loads(json_string))
