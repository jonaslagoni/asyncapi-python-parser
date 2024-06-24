from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import Reference
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
from . import OperationBindingsObject
class OperationTrait(BaseModel): 
  title: Optional[str] = Field(description='''A human-friendly title for the operation.''', default=None)
  summary: Optional[str] = Field(description='''A short summary of what the operation is about.''', default=None)
  description: Optional[str] = Field(description='''A verbose explanation of the operation. CommonMark syntax can be used for rich text representation.''', default=None)
  security: Optional[List[Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme | Oauth2Flows.Oauth2Flows | OpenIdConnect.OpenIdConnect | SaslPlainSecurityScheme.SaslPlainSecurityScheme | SaslScramSecurityScheme.SaslScramSecurityScheme | SaslGssapiSecurityScheme.SaslGssapiSecurityScheme]] = Field(description='''A declaration of which security schemes are associated with this operation. Only one of the security scheme objects MUST be satisfied to authorize an operation. In cases where Server Security also applies, it MUST also be satisfied.''', default=None)
  tags: Optional[List[Reference.Reference | Tag.Tag]] = Field(description='''A list of tags for logical grouping and categorization of operations.''', default=None)
  external_docs: Optional[Union[Reference.Reference, ExternalDocs.ExternalDocs]] = Field(description='''Additional external documentation for this operation.''', default=None, alias='''externalDocs''')
  bindings: Optional[Union[Reference.Reference, OperationBindingsObject.OperationBindingsObject]] = Field(description='''A map where the keys describe the name of the protocol and the values describe protocol-specific definitions for the operation.''', default=None)
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
    known_object_properties = ['title', 'summary', 'description', 'security', 'tags', 'external_docs', 'bindings', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['title', 'summary', 'description', 'security', 'tags', 'externalDocs', 'bindings', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

