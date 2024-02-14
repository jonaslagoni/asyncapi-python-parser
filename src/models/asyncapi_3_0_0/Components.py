from .Reference import Reference
from .AnySchemaObject import AnySchemaObject
from .Server import Server
from .Channel import Channel
from .ServerVariable import ServerVariable
from .Operation import Operation
from .MessageObject import MessageObject
from .UserPassword import UserPassword
from .ApiKey import ApiKey
from .X509 import X509
from .SymmetricEncryption import SymmetricEncryption
from .AsymmetricEncryption import AsymmetricEncryption
from .BearerHttpSecurityScheme import BearerHttpSecurityScheme
from .ApiKeyHttpSecurityScheme import ApiKeyHttpSecurityScheme
from .Oauth2Flows import Oauth2Flows
from .OpenIdConnect import OpenIdConnect
from .SaslPlainSecurityScheme import SaslPlainSecurityScheme
from .SaslScramSecurityScheme import SaslScramSecurityScheme
from .SaslGssapiSecurityScheme import SaslGssapiSecurityScheme
from .Parameter import Parameter
from .CorrelationId import CorrelationId
from .OperationTrait import OperationTrait
from .MessageTrait import MessageTrait
from .OperationReply import OperationReply
from .OperationReplyAddress import OperationReplyAddress
from .ServerBindingsObject import ServerBindingsObject
from .ChannelBindingsObject import ChannelBindingsObject
from .OperationBindingsObject import OperationBindingsObject
from .MessageBindingsObject import MessageBindingsObject
from .Tag import Tag
from .ExternalDocs import ExternalDocs
import json
from typing import Any, List, Dict
class Components: 
  def __init__(self, input: Dict):
    if hasattr(input, 'schemas'):
      self._schemas: dict[str, Any | Reference | AnySchemaObject | bool] = input['schemas']
    if hasattr(input, 'servers'):
      self._servers: dict[str, Any | Reference | Server] = input['servers']
    if hasattr(input, 'channels'):
      self._channels: dict[str, Any | Reference | Channel] = input['channels']
    if hasattr(input, 'server_variables'):
      self._server_variables: dict[str, Any | Reference | ServerVariable] = input['server_variables']
    if hasattr(input, 'operations'):
      self._operations: dict[str, Any | Reference | Operation] = input['operations']
    if hasattr(input, 'messages'):
      self._messages: dict[str, Any | Reference | MessageObject] = input['messages']
    if hasattr(input, 'security_schemes'):
      self._security_schemes: dict[str, Any | Reference | UserPassword | ApiKey | X509 | SymmetricEncryption | AsymmetricEncryption | Any | BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme | Oauth2Flows | OpenIdConnect | SaslPlainSecurityScheme | SaslScramSecurityScheme | SaslGssapiSecurityScheme] = input['security_schemes']
    if hasattr(input, 'parameters'):
      self._parameters: dict[str, Any | Reference | Parameter] = input['parameters']
    if hasattr(input, 'correlation_ids'):
      self._correlation_ids: dict[str, Any | Reference | CorrelationId] = input['correlation_ids']
    if hasattr(input, 'operation_traits'):
      self._operation_traits: dict[str, Any | Reference | OperationTrait] = input['operation_traits']
    if hasattr(input, 'message_traits'):
      self._message_traits: dict[str, Any | Reference | MessageTrait] = input['message_traits']
    if hasattr(input, 'replies'):
      self._replies: dict[str, Any | Reference | OperationReply] = input['replies']
    if hasattr(input, 'reply_addresses'):
      self._reply_addresses: dict[str, Any | Reference | OperationReplyAddress] = input['reply_addresses']
    if hasattr(input, 'server_bindings'):
      self._server_bindings: dict[str, Any | Reference | ServerBindingsObject] = input['server_bindings']
    if hasattr(input, 'channel_bindings'):
      self._channel_bindings: dict[str, Any | Reference | ChannelBindingsObject] = input['channel_bindings']
    if hasattr(input, 'operation_bindings'):
      self._operation_bindings: dict[str, Any | Reference | OperationBindingsObject] = input['operation_bindings']
    if hasattr(input, 'message_bindings'):
      self._message_bindings: dict[str, Any | Reference | MessageBindingsObject] = input['message_bindings']
    if hasattr(input, 'tags'):
      self._tags: dict[str, Any | Reference | Tag] = input['tags']
    if hasattr(input, 'external_docs'):
      self._external_docs: dict[str, Any | Reference | ExternalDocs] = input['external_docs']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def schemas(self) -> dict[str, Any | Reference | AnySchemaObject | bool]:
    return self._schemas
  @schemas.setter
  def schemas(self, schemas: dict[str, Any | Reference | AnySchemaObject | bool]):
    self._schemas = schemas

  @property
  def servers(self) -> dict[str, Any | Reference | Server]:
    return self._servers
  @servers.setter
  def servers(self, servers: dict[str, Any | Reference | Server]):
    self._servers = servers

  @property
  def channels(self) -> dict[str, Any | Reference | Channel]:
    return self._channels
  @channels.setter
  def channels(self, channels: dict[str, Any | Reference | Channel]):
    self._channels = channels

  @property
  def server_variables(self) -> dict[str, Any | Reference | ServerVariable]:
    return self._server_variables
  @server_variables.setter
  def server_variables(self, server_variables: dict[str, Any | Reference | ServerVariable]):
    self._server_variables = server_variables

  @property
  def operations(self) -> dict[str, Any | Reference | Operation]:
    return self._operations
  @operations.setter
  def operations(self, operations: dict[str, Any | Reference | Operation]):
    self._operations = operations

  @property
  def messages(self) -> dict[str, Any | Reference | MessageObject]:
    return self._messages
  @messages.setter
  def messages(self, messages: dict[str, Any | Reference | MessageObject]):
    self._messages = messages

  @property
  def security_schemes(self) -> dict[str, Any | Reference | UserPassword | ApiKey | X509 | SymmetricEncryption | AsymmetricEncryption | Any | BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme | Oauth2Flows | OpenIdConnect | SaslPlainSecurityScheme | SaslScramSecurityScheme | SaslGssapiSecurityScheme]:
    return self._security_schemes
  @security_schemes.setter
  def security_schemes(self, security_schemes: dict[str, Any | Reference | UserPassword | ApiKey | X509 | SymmetricEncryption | AsymmetricEncryption | Any | BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme | Oauth2Flows | OpenIdConnect | SaslPlainSecurityScheme | SaslScramSecurityScheme | SaslGssapiSecurityScheme]):
    self._security_schemes = security_schemes

  @property
  def parameters(self) -> dict[str, Any | Reference | Parameter]:
    return self._parameters
  @parameters.setter
  def parameters(self, parameters: dict[str, Any | Reference | Parameter]):
    self._parameters = parameters

  @property
  def correlation_ids(self) -> dict[str, Any | Reference | CorrelationId]:
    return self._correlation_ids
  @correlation_ids.setter
  def correlation_ids(self, correlation_ids: dict[str, Any | Reference | CorrelationId]):
    self._correlation_ids = correlation_ids

  @property
  def operation_traits(self) -> dict[str, Any | Reference | OperationTrait]:
    return self._operation_traits
  @operation_traits.setter
  def operation_traits(self, operation_traits: dict[str, Any | Reference | OperationTrait]):
    self._operation_traits = operation_traits

  @property
  def message_traits(self) -> dict[str, Any | Reference | MessageTrait]:
    return self._message_traits
  @message_traits.setter
  def message_traits(self, message_traits: dict[str, Any | Reference | MessageTrait]):
    self._message_traits = message_traits

  @property
  def replies(self) -> dict[str, Any | Reference | OperationReply]:
    return self._replies
  @replies.setter
  def replies(self, replies: dict[str, Any | Reference | OperationReply]):
    self._replies = replies

  @property
  def reply_addresses(self) -> dict[str, Any | Reference | OperationReplyAddress]:
    return self._reply_addresses
  @reply_addresses.setter
  def reply_addresses(self, reply_addresses: dict[str, Any | Reference | OperationReplyAddress]):
    self._reply_addresses = reply_addresses

  @property
  def server_bindings(self) -> dict[str, Any | Reference | ServerBindingsObject]:
    return self._server_bindings
  @server_bindings.setter
  def server_bindings(self, server_bindings: dict[str, Any | Reference | ServerBindingsObject]):
    self._server_bindings = server_bindings

  @property
  def channel_bindings(self) -> dict[str, Any | Reference | ChannelBindingsObject]:
    return self._channel_bindings
  @channel_bindings.setter
  def channel_bindings(self, channel_bindings: dict[str, Any | Reference | ChannelBindingsObject]):
    self._channel_bindings = channel_bindings

  @property
  def operation_bindings(self) -> dict[str, Any | Reference | OperationBindingsObject]:
    return self._operation_bindings
  @operation_bindings.setter
  def operation_bindings(self, operation_bindings: dict[str, Any | Reference | OperationBindingsObject]):
    self._operation_bindings = operation_bindings

  @property
  def message_bindings(self) -> dict[str, Any | Reference | MessageBindingsObject]:
    return self._message_bindings
  @message_bindings.setter
  def message_bindings(self, message_bindings: dict[str, Any | Reference | MessageBindingsObject]):
    self._message_bindings = message_bindings

  @property
  def tags(self) -> dict[str, Any | Reference | Tag]:
    return self._tags
  @tags.setter
  def tags(self, tags: dict[str, Any | Reference | Tag]):
    self._tags = tags

  @property
  def external_docs(self) -> dict[str, Any | Reference | ExternalDocs]:
    return self._external_docs
  @external_docs.setter
  def external_docs(self, external_docs: dict[str, Any | Reference | ExternalDocs]):
    self._external_docs = external_docs

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
