from .Schema import Schema
from .Message import Message
from .Reference import Reference
from .UserPassword import UserPassword
from .ApiKey import ApiKey
from .X509 import X509
from .SymmetricEncryption import SymmetricEncryption
from .AsymmetricEncryption import AsymmetricEncryption
from .BearerHttpSecurityScheme import BearerHttpSecurityScheme
from .ApiKeyHttpSecurityScheme import ApiKeyHttpSecurityScheme
from .Oauth2Flows import Oauth2Flows
from .OpenIdConnect import OpenIdConnect
from .Parameter import Parameter
from .CorrelationId import CorrelationId
from .OperationTrait import OperationTrait
from .MessageTrait import MessageTrait
import json
from typing import Any, List, Dict
class Components: 
  def __init__(self, input: Dict):
    if hasattr(input, 'schemas'):
      self._schemas: dict[str, Schema] = input['schemas']
    if hasattr(input, 'messages'):
      self._messages: dict[str, Message] = input['messages']
    if hasattr(input, 'security_schemes'):
      self._security_schemes: dict[str, Any | Reference | UserPassword | ApiKey | X509 | SymmetricEncryption | AsymmetricEncryption | Any | BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme | Oauth2Flows | OpenIdConnect] = input['security_schemes']
    if hasattr(input, 'parameters'):
      self._parameters: dict[str, Reference | Parameter] = input['parameters']
    if hasattr(input, 'correlation_ids'):
      self._correlation_ids: dict[str, Any | Reference | CorrelationId] = input['correlation_ids']
    if hasattr(input, 'traits'):
      self._traits: dict[str, OperationTrait | MessageTrait] = input['traits']

  @property
  def schemas(self) -> dict[str, Schema]:
    return self._schemas
  @schemas.setter
  def schemas(self, schemas: dict[str, Schema]):
    self._schemas = schemas

  @property
  def messages(self) -> dict[str, Message]:
    return self._messages
  @messages.setter
  def messages(self, messages: dict[str, Message]):
    self._messages = messages

  @property
  def security_schemes(self) -> dict[str, Any | Reference | UserPassword | ApiKey | X509 | SymmetricEncryption | AsymmetricEncryption | Any | BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme | Oauth2Flows | OpenIdConnect]:
    return self._security_schemes
  @security_schemes.setter
  def security_schemes(self, security_schemes: dict[str, Any | Reference | UserPassword | ApiKey | X509 | SymmetricEncryption | AsymmetricEncryption | Any | BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme | Oauth2Flows | OpenIdConnect]):
    self._security_schemes = security_schemes

  @property
  def parameters(self) -> dict[str, Reference | Parameter]:
    return self._parameters
  @parameters.setter
  def parameters(self, parameters: dict[str, Reference | Parameter]):
    self._parameters = parameters

  @property
  def correlation_ids(self) -> dict[str, Any | Reference | CorrelationId]:
    return self._correlation_ids
  @correlation_ids.setter
  def correlation_ids(self, correlation_ids: dict[str, Any | Reference | CorrelationId]):
    self._correlation_ids = correlation_ids

  @property
  def traits(self) -> dict[str, OperationTrait | MessageTrait]:
    return self._traits
  @traits.setter
  def traits(self, traits: dict[str, OperationTrait | MessageTrait]):
    self._traits = traits

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return Components(**json.loads(json_string))
