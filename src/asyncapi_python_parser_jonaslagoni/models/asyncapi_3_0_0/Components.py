from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import Reference
from . import MultiFormatSchema
from . import CoreSchemaMetaSchemaObject
from . import Server
from . import Channel
from . import ServerVariable
from . import Operation
from . import MessageObject
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
from . import OperationReply
from . import OperationReplyAddress
from . import ServerBindingsObject
from . import ChannelBindingsObject
from . import OperationBindingsObject
from . import MessageBindingsObject
from . import Tag
from . import ExternalDocs
class Components(BaseModel): 
  schemas: Optional[dict[str, Any | Reference.Reference | MultiFormatSchema.MultiFormatSchema | CoreSchemaMetaSchemaObject.CoreSchemaMetaSchemaObject | bool]] = Field(default=None)
  servers: Optional[dict[str, Any | Reference.Reference | Server.Server]] = Field(default=None)
  channels: Optional[dict[str, Any | Reference.Reference | Channel.Channel]] = Field(default=None)
  server_variables: Optional[dict[str, Any | Reference.Reference | ServerVariable.ServerVariable]] = Field(default=None, alias='''serverVariables''')
  operations: Optional[dict[str, Any | Reference.Reference | Operation.Operation]] = Field(default=None)
  messages: Optional[dict[str, Any | Reference.Reference | MessageObject.MessageObject]] = Field(default=None)
  security_schemes: Optional[dict[str, Any | Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme | Oauth2Flows.Oauth2Flows | OpenIdConnect.OpenIdConnect | SaslPlainSecurityScheme.SaslPlainSecurityScheme | SaslScramSecurityScheme.SaslScramSecurityScheme | SaslGssapiSecurityScheme.SaslGssapiSecurityScheme]] = Field(default=None, alias='''securitySchemes''')
  parameters: Optional[dict[str, Any | Reference.Reference | Parameter.Parameter]] = Field(default=None)
  correlation_ids: Optional[dict[str, Any | Reference.Reference | CorrelationId.CorrelationId]] = Field(default=None, alias='''correlationIds''')
  operation_traits: Optional[dict[str, Any | Reference.Reference | OperationTrait.OperationTrait]] = Field(default=None, alias='''operationTraits''')
  message_traits: Optional[dict[str, Any | Reference.Reference | MessageTrait.MessageTrait]] = Field(default=None, alias='''messageTraits''')
  replies: Optional[dict[str, Any | Reference.Reference | OperationReply.OperationReply]] = Field(default=None)
  reply_addresses: Optional[dict[str, Any | Reference.Reference | OperationReplyAddress.OperationReplyAddress]] = Field(default=None, alias='''replyAddresses''')
  server_bindings: Optional[dict[str, Any | Reference.Reference | ServerBindingsObject.ServerBindingsObject]] = Field(default=None, alias='''serverBindings''')
  channel_bindings: Optional[dict[str, Any | Reference.Reference | ChannelBindingsObject.ChannelBindingsObject]] = Field(default=None, alias='''channelBindings''')
  operation_bindings: Optional[dict[str, Any | Reference.Reference | OperationBindingsObject.OperationBindingsObject]] = Field(default=None, alias='''operationBindings''')
  message_bindings: Optional[dict[str, Any | Reference.Reference | MessageBindingsObject.MessageBindingsObject]] = Field(default=None, alias='''messageBindings''')
  tags: Optional[dict[str, Any | Reference.Reference | Tag.Tag]] = Field(default=None)
  external_docs: Optional[dict[str, Any | Reference.Reference | ExternalDocs.ExternalDocs]] = Field(default=None, alias='''externalDocs''')
  extensions: Optional[dict[str, Any]] = Field(exclude=True, default=None)

  @model_serializer(mode='wrap')
  def custom_serializer(self, handler):
    serialized_self = handler(self)
    extensions = getattr(self, "extensions")
    if extensions is not None:
      for key, value in extensions.items():
        # Never overwrite existing values, to avoid clashes
        if not hasattr(serialized_self, key):
          serialized_self[key] = value

    return serialized_self

  @model_validator(mode='before')
  @classmethod
  def unwrap_extensions(cls, data):
    json_properties = list(data.keys())
    known_object_properties = ['schemas', 'servers', 'channels', 'server_variables', 'operations', 'messages', 'security_schemes', 'parameters', 'correlation_ids', 'operation_traits', 'message_traits', 'replies', 'reply_addresses', 'server_bindings', 'channel_bindings', 'operation_bindings', 'message_bindings', 'tags', 'external_docs', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['schemas', 'servers', 'channels', 'serverVariables', 'operations', 'messages', 'securitySchemes', 'parameters', 'correlationIds', 'operationTraits', 'messageTraits', 'replies', 'replyAddresses', 'serverBindings', 'channelBindings', 'operationBindings', 'messageBindings', 'tags', 'externalDocs', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

