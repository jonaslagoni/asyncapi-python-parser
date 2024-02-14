from .SchemaObject import SchemaObject
from .Reference import Reference
from .MessageOneOf1OneOf0 import MessageOneOf1OneOf0
from .MessageOneOf1OneOf1 import MessageOneOf1OneOf1
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
from .BindingsObject import BindingsObject
import json
from typing import Any, List, Dict
class Components: 
  def __init__(self, input: Dict):
    if hasattr(input, 'schemas'):
      self._schemas: dict[str, SchemaObject | bool] = input['schemas']
    if hasattr(input, 'messages'):
      self._messages: dict[str, Reference | MessageOneOf1OneOf0 | MessageOneOf1OneOf1] = input['messages']
    if hasattr(input, 'security_schemes'):
      self._security_schemes: dict[str, Any | Reference | UserPassword | ApiKey | X509 | SymmetricEncryption | AsymmetricEncryption | Any | BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme | Oauth2Flows | OpenIdConnect] = input['security_schemes']
    if hasattr(input, 'parameters'):
      self._parameters: dict[str, Reference | Parameter] = input['parameters']
    if hasattr(input, 'correlation_ids'):
      self._correlation_ids: dict[str, Any | Reference | CorrelationId] = input['correlation_ids']
    if hasattr(input, 'operation_traits'):
      self._operation_traits: dict[str, OperationTrait] = input['operation_traits']
    if hasattr(input, 'message_traits'):
      self._message_traits: dict[str, MessageTrait] = input['message_traits']
    if hasattr(input, 'server_bindings'):
      self._server_bindings: dict[str, BindingsObject] = input['server_bindings']
    if hasattr(input, 'channel_bindings'):
      self._channel_bindings: dict[str, BindingsObject] = input['channel_bindings']
    if hasattr(input, 'operation_bindings'):
      self._operation_bindings: dict[str, BindingsObject] = input['operation_bindings']
    if hasattr(input, 'message_bindings'):
      self._message_bindings: dict[str, BindingsObject] = input['message_bindings']

  @property
  def schemas(self) -> dict[str, SchemaObject | bool]:
    return self._schemas
  @schemas.setter
  def schemas(self, schemas: dict[str, SchemaObject | bool]):
    self._schemas = schemas

  @property
  def messages(self) -> dict[str, Reference | MessageOneOf1OneOf0 | MessageOneOf1OneOf1]:
    return self._messages
  @messages.setter
  def messages(self, messages: dict[str, Reference | MessageOneOf1OneOf0 | MessageOneOf1OneOf1]):
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
  def operation_traits(self) -> dict[str, OperationTrait]:
    return self._operation_traits
  @operation_traits.setter
  def operation_traits(self, operation_traits: dict[str, OperationTrait]):
    self._operation_traits = operation_traits

  @property
  def message_traits(self) -> dict[str, MessageTrait]:
    return self._message_traits
  @message_traits.setter
  def message_traits(self, message_traits: dict[str, MessageTrait]):
    self._message_traits = message_traits

  @property
  def server_bindings(self) -> dict[str, BindingsObject]:
    return self._server_bindings
  @server_bindings.setter
  def server_bindings(self, server_bindings: dict[str, BindingsObject]):
    self._server_bindings = server_bindings

  @property
  def channel_bindings(self) -> dict[str, BindingsObject]:
    return self._channel_bindings
  @channel_bindings.setter
  def channel_bindings(self, channel_bindings: dict[str, BindingsObject]):
    self._channel_bindings = channel_bindings

  @property
  def operation_bindings(self) -> dict[str, BindingsObject]:
    return self._operation_bindings
  @operation_bindings.setter
  def operation_bindings(self, operation_bindings: dict[str, BindingsObject]):
    self._operation_bindings = operation_bindings

  @property
  def message_bindings(self) -> dict[str, BindingsObject]:
    return self._message_bindings
  @message_bindings.setter
  def message_bindings(self, message_bindings: dict[str, BindingsObject]):
    self._message_bindings = message_bindings

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return Components(**json.loads(json_string))
