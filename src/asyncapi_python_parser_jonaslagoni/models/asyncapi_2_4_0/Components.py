from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
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
class Components(BaseModel): 
  schemas: Optional[dict[str, SchemaObject.SchemaObject | bool]] = Field(default=None)
  servers: Optional[dict[str, Reference.Reference | Server.Server]] = Field(default=None)
  channels: Optional[dict[str, ChannelItem.ChannelItem]] = Field(default=None)
  server_variables: Optional[dict[str, ServerVariable.ServerVariable]] = Field(default=None, alias='''serverVariables''')
  messages: Optional[dict[str, Reference.Reference | MessageOneOf1OneOf0.MessageOneOf1OneOf0 | MessageOneOf1OneOf1.MessageOneOf1OneOf1]] = Field(default=None)
  security_schemes: Optional[dict[str, Any | Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme | Oauth2Flows.Oauth2Flows | OpenIdConnect.OpenIdConnect | SaslPlainSecurityScheme.SaslPlainSecurityScheme | SaslScramSecurityScheme.SaslScramSecurityScheme | SaslGssapiSecurityScheme.SaslGssapiSecurityScheme]] = Field(default=None, alias='''securitySchemes''')
  parameters: Optional[dict[str, Reference.Reference | Parameter.Parameter]] = Field(default=None)
  correlation_ids: Optional[dict[str, Any | Reference.Reference | CorrelationId.CorrelationId]] = Field(default=None, alias='''correlationIds''')
  operation_traits: Optional[dict[str, OperationTrait.OperationTrait]] = Field(default=None, alias='''operationTraits''')
  message_traits: Optional[dict[str, MessageTrait.MessageTrait]] = Field(default=None, alias='''messageTraits''')
  server_bindings: Optional[dict[str, BindingsObject.BindingsObject]] = Field(default=None, alias='''serverBindings''')
  channel_bindings: Optional[dict[str, BindingsObject.BindingsObject]] = Field(default=None, alias='''channelBindings''')
  operation_bindings: Optional[dict[str, BindingsObject.BindingsObject]] = Field(default=None, alias='''operationBindings''')
  message_bindings: Optional[dict[str, BindingsObject.BindingsObject]] = Field(default=None, alias='''messageBindings''')
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
    known_object_properties = ['schemas', 'servers', 'channels', 'server_variables', 'messages', 'security_schemes', 'parameters', 'correlation_ids', 'operation_traits', 'message_traits', 'server_bindings', 'channel_bindings', 'operation_bindings', 'message_bindings', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['schemas', 'servers', 'channels', 'serverVariables', 'messages', 'securitySchemes', 'parameters', 'correlationIds', 'operationTraits', 'messageTraits', 'serverBindings', 'channelBindings', 'operationBindings', 'messageBindings', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

