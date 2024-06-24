from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import Reference
from . import ServerVariable
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
from . import Tag
from . import ExternalDocs
from . import ServerBindingsObject
class Server(BaseModel): 
  host: str = Field(description='''The server host name. It MAY include the port. This field supports Server Variables. Variable substitutions will be made when a variable is named in {braces}.''')
  pathname: Optional[str] = Field(description='''The path to a resource in the host. This field supports Server Variables. Variable substitutions will be made when a variable is named in {braces}.''', default=None)
  title: Optional[str] = Field(description='''A human-friendly title for the server.''', default=None)
  summary: Optional[str] = Field(description='''A brief summary of the server.''', default=None)
  description: Optional[str] = Field(description='''A longer description of the server. CommonMark is allowed.''', default=None)
  protocol: str = Field(description='''The protocol this server supports for connection.''')
  protocol_version: Optional[str] = Field(description='''An optional string describing the server. CommonMark syntax MAY be used for rich text representation.''', default=None, alias='''protocolVersion''')
  variables: Optional[dict[str, Reference.Reference | ServerVariable.ServerVariable]] = Field(default=None)
  security: Optional[List[Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme | Oauth2Flows.Oauth2Flows | OpenIdConnect.OpenIdConnect | SaslPlainSecurityScheme.SaslPlainSecurityScheme | SaslScramSecurityScheme.SaslScramSecurityScheme | SaslGssapiSecurityScheme.SaslGssapiSecurityScheme]] = Field(description='''An array representing security requirements.''', default=None)
  tags: Optional[List[Reference.Reference | Tag.Tag]] = Field(default=None)
  external_docs: Optional[Union[Reference.Reference, ExternalDocs.ExternalDocs]] = Field(default=None, alias='''externalDocs''')
  bindings: Optional[Union[Reference.Reference, ServerBindingsObject.ServerBindingsObject]] = Field(default=None)
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
    known_object_properties = ['host', 'pathname', 'title', 'summary', 'description', 'protocol', 'protocol_version', 'variables', 'security', 'tags', 'external_docs', 'bindings', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['host', 'pathname', 'title', 'summary', 'description', 'protocol', 'protocolVersion', 'variables', 'security', 'tags', 'externalDocs', 'bindings', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

