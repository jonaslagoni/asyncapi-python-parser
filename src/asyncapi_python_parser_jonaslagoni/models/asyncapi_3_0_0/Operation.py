from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import OperationAction
from . import Reference
from . import OperationReply
from . import OperationTrait
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
class Operation(BaseModel): 
  action: OperationAction.OperationAction = Field(description='''Allowed values are send and receive. Use send when it's expected that the application will send a message to the given channel, and receive when the application should expect receiving messages from the given channel.''')
  channel: Reference.Reference = Field(description='''A simple object to allow referencing other components in the specification, internally and externally.''')
  messages: Optional[List[Reference.Reference]] = Field(description='''A list of $ref pointers pointing to the supported Message Objects that can be processed by this operation. It MUST contain a subset of the messages defined in the channel referenced in this operation. Every message processed by this operation MUST be valid against one, and only one, of the message objects referenced in this list. Please note the messages property value MUST be a list of Reference Objects and, therefore, MUST NOT contain Message Objects. However, it is RECOMMENDED that parsers (or other software) dereference this property for a better development experience.''', default=None)
  reply: Optional[Union[Reference.Reference, OperationReply.OperationReply]] = Field(default=None)
  traits: Optional[List[Reference.Reference | OperationTrait.OperationTrait]] = Field(description='''A list of traits to apply to the operation object. Traits MUST be merged using traits merge mechanism. The resulting object MUST be a valid Operation Object.''', default=None)
  title: Optional[str] = Field(description='''A human-friendly title for the operation.''', default=None)
  summary: Optional[str] = Field(description='''A brief summary of the operation.''', default=None)
  description: Optional[str] = Field(description='''A longer description of the operation. CommonMark is allowed.''', default=None)
  security: Optional[List[Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme | Oauth2Flows.Oauth2Flows | OpenIdConnect.OpenIdConnect | SaslPlainSecurityScheme.SaslPlainSecurityScheme | SaslScramSecurityScheme.SaslScramSecurityScheme | SaslGssapiSecurityScheme.SaslGssapiSecurityScheme]] = Field(description='''An array representing security requirements.''', default=None)
  tags: Optional[List[Reference.Reference | Tag.Tag]] = Field(description='''A list of tags for logical grouping and categorization of operations.''', default=None)
  external_docs: Optional[Union[Reference.Reference, ExternalDocs.ExternalDocs]] = Field(default=None, alias='''externalDocs''')
  bindings: Optional[Union[Reference.Reference, OperationBindingsObject.OperationBindingsObject]] = Field(default=None)
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
    known_object_properties = ['action', 'channel', 'messages', 'reply', 'traits', 'title', 'summary', 'description', 'security', 'tags', 'external_docs', 'bindings', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['action', 'channel', 'messages', 'reply', 'traits', 'title', 'summary', 'description', 'security', 'tags', 'externalDocs', 'bindings', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

