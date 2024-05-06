from __future__ import annotations
import json
from typing import Any, List, Dict
from . import SchemaObject
from . import Reference
from . import Server
from . import ChannelItem
from . import ServerVariable
from . import MessageOneOf1OneOf0
from . import MessageOneOf1OneOf1
from . import UserPassword
from . import ApiKey
from . import X509
from . import SymmetricEncryption
from . import AsymmetricEncryption
from . import BearerHttpSecurityScheme
from . import ApiKeyHttpSecurityScheme
from . import Oauth2Flows
from . import OpenIdConnect
from . import SaslPlainSecurityScheme
from . import SaslScramSecurityScheme
from . import SaslGssapiSecurityScheme
from . import Parameter
from . import CorrelationId
from . import OperationTrait
from . import MessageTrait
from . import BindingsObject
class Components: 
  def __init__(self, input: Dict):
    if 'schemas' in input:
      self._schemas: dict[str, SchemaObject.SchemaObject | bool] = input['schemas']
    if 'servers' in input:
      self._servers: dict[str, Reference.Reference | Server.Server] = input['servers']
    if 'channels' in input:
      self._channels: dict[str, ChannelItem.ChannelItem] = input['channels']
    if 'server_variables' in input:
      self._server_variables: dict[str, ServerVariable.ServerVariable] = input['server_variables']
    if 'messages' in input:
      self._messages: dict[str, Reference.Reference | MessageOneOf1OneOf0.MessageOneOf1OneOf0 | MessageOneOf1OneOf1.MessageOneOf1OneOf1] = input['messages']
    if 'security_schemes' in input:
      self._security_schemes: dict[str, Any | Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme | Oauth2Flows.Oauth2Flows | OpenIdConnect.OpenIdConnect | SaslPlainSecurityScheme.SaslPlainSecurityScheme | SaslScramSecurityScheme.SaslScramSecurityScheme | SaslGssapiSecurityScheme.SaslGssapiSecurityScheme] = input['security_schemes']
    if 'parameters' in input:
      self._parameters: dict[str, Reference.Reference | Parameter.Parameter] = input['parameters']
    if 'correlation_ids' in input:
      self._correlation_ids: dict[str, Any | Reference.Reference | CorrelationId.CorrelationId] = input['correlation_ids']
    if 'operation_traits' in input:
      self._operation_traits: dict[str, OperationTrait.OperationTrait] = input['operation_traits']
    if 'message_traits' in input:
      self._message_traits: dict[str, MessageTrait.MessageTrait] = input['message_traits']
    if 'server_bindings' in input:
      self._server_bindings: dict[str, BindingsObject.BindingsObject] = input['server_bindings']
    if 'channel_bindings' in input:
      self._channel_bindings: dict[str, BindingsObject.BindingsObject] = input['channel_bindings']
    if 'operation_bindings' in input:
      self._operation_bindings: dict[str, BindingsObject.BindingsObject] = input['operation_bindings']
    if 'message_bindings' in input:
      self._message_bindings: dict[str, BindingsObject.BindingsObject] = input['message_bindings']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def schemas(self) -> dict[str, SchemaObject.SchemaObject | bool]:
    return self._schemas
  @schemas.setter
  def schemas(self, schemas: dict[str, SchemaObject.SchemaObject | bool]):
    self._schemas = schemas

  @property
  def servers(self) -> dict[str, Reference.Reference | Server.Server]:
    return self._servers
  @servers.setter
  def servers(self, servers: dict[str, Reference.Reference | Server.Server]):
    self._servers = servers

  @property
  def channels(self) -> dict[str, ChannelItem.ChannelItem]:
    return self._channels
  @channels.setter
  def channels(self, channels: dict[str, ChannelItem.ChannelItem]):
    self._channels = channels

  @property
  def server_variables(self) -> dict[str, ServerVariable.ServerVariable]:
    return self._server_variables
  @server_variables.setter
  def server_variables(self, server_variables: dict[str, ServerVariable.ServerVariable]):
    self._server_variables = server_variables

  @property
  def messages(self) -> dict[str, Reference.Reference | MessageOneOf1OneOf0.MessageOneOf1OneOf0 | MessageOneOf1OneOf1.MessageOneOf1OneOf1]:
    return self._messages
  @messages.setter
  def messages(self, messages: dict[str, Reference.Reference | MessageOneOf1OneOf0.MessageOneOf1OneOf0 | MessageOneOf1OneOf1.MessageOneOf1OneOf1]):
    self._messages = messages

  @property
  def security_schemes(self) -> dict[str, Any | Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme | Oauth2Flows.Oauth2Flows | OpenIdConnect.OpenIdConnect | SaslPlainSecurityScheme.SaslPlainSecurityScheme | SaslScramSecurityScheme.SaslScramSecurityScheme | SaslGssapiSecurityScheme.SaslGssapiSecurityScheme]:
    return self._security_schemes
  @security_schemes.setter
  def security_schemes(self, security_schemes: dict[str, Any | Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme | Oauth2Flows.Oauth2Flows | OpenIdConnect.OpenIdConnect | SaslPlainSecurityScheme.SaslPlainSecurityScheme | SaslScramSecurityScheme.SaslScramSecurityScheme | SaslGssapiSecurityScheme.SaslGssapiSecurityScheme]):
    self._security_schemes = security_schemes

  @property
  def parameters(self) -> dict[str, Reference.Reference | Parameter.Parameter]:
    return self._parameters
  @parameters.setter
  def parameters(self, parameters: dict[str, Reference.Reference | Parameter.Parameter]):
    self._parameters = parameters

  @property
  def correlation_ids(self) -> dict[str, Any | Reference.Reference | CorrelationId.CorrelationId]:
    return self._correlation_ids
  @correlation_ids.setter
  def correlation_ids(self, correlation_ids: dict[str, Any | Reference.Reference | CorrelationId.CorrelationId]):
    self._correlation_ids = correlation_ids

  @property
  def operation_traits(self) -> dict[str, OperationTrait.OperationTrait]:
    return self._operation_traits
  @operation_traits.setter
  def operation_traits(self, operation_traits: dict[str, OperationTrait.OperationTrait]):
    self._operation_traits = operation_traits

  @property
  def message_traits(self) -> dict[str, MessageTrait.MessageTrait]:
    return self._message_traits
  @message_traits.setter
  def message_traits(self, message_traits: dict[str, MessageTrait.MessageTrait]):
    self._message_traits = message_traits

  @property
  def server_bindings(self) -> dict[str, BindingsObject.BindingsObject]:
    return self._server_bindings
  @server_bindings.setter
  def server_bindings(self, server_bindings: dict[str, BindingsObject.BindingsObject]):
    self._server_bindings = server_bindings

  @property
  def channel_bindings(self) -> dict[str, BindingsObject.BindingsObject]:
    return self._channel_bindings
  @channel_bindings.setter
  def channel_bindings(self, channel_bindings: dict[str, BindingsObject.BindingsObject]):
    self._channel_bindings = channel_bindings

  @property
  def operation_bindings(self) -> dict[str, BindingsObject.BindingsObject]:
    return self._operation_bindings
  @operation_bindings.setter
  def operation_bindings(self, operation_bindings: dict[str, BindingsObject.BindingsObject]):
    self._operation_bindings = operation_bindings

  @property
  def message_bindings(self) -> dict[str, BindingsObject.BindingsObject]:
    return self._message_bindings
  @message_bindings.setter
  def message_bindings(self, message_bindings: dict[str, BindingsObject.BindingsObject]):
    self._message_bindings = message_bindings

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
    return Components(**json.loads(json_string))
