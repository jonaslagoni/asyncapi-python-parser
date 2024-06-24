from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import MessageOneOf1OneOf1HeadersObject
from . import MessageOneOf1OneOf1PayloadObject
from . import Reference
from . import CorrelationId
from . import Tag
from . import ExternalDocs
from . import BindingsObject
from . import MessageTrait
class MessageOneOf1OneOf1(BaseModel): 
  schema_format: Optional[str] = Field(default=None, alias='''schemaFormat''')
  content_type: Optional[str] = Field(default=None, alias='''contentType''')
  headers: Optional[Union[MessageOneOf1OneOf1HeadersObject.MessageOneOf1OneOf1HeadersObject, bool]] = Field(default=None)
  message_id: Optional[str] = Field(default=None, alias='''messageId''')
  payload: Optional[Union[MessageOneOf1OneOf1PayloadObject.MessageOneOf1OneOf1PayloadObject, bool]] = Field(default=None)
  correlation_id: Optional[Union[Reference.Reference, CorrelationId.CorrelationId]] = Field(default=None, alias='''correlationId''')
  tags: Optional[List[Tag.Tag]] = Field(default=None)
  summary: Optional[str] = Field(description='''A brief summary of the message.''', default=None)
  name: Optional[str] = Field(description='''Name of the message.''', default=None)
  title: Optional[str] = Field(description='''A human-friendly title for the message.''', default=None)
  description: Optional[str] = Field(description='''A longer description of the message. CommonMark is allowed.''', default=None)
  external_docs: Optional[ExternalDocs.ExternalDocs] = Field(description='''Allows referencing an external resource for extended documentation.''', default=None, alias='''externalDocs''')
  deprecated: Optional[bool] = Field(default=None)
  examples: Optional[List[Any]] = Field(description='''List of examples.''', default=None)
  bindings: Optional[BindingsObject.BindingsObject] = Field(description='''Map describing protocol-specific definitions for a server.''', default=None)
  traits: Optional[List[Reference.Reference | MessageTrait.MessageTrait]] = Field(default=None)
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
    known_object_properties = ['schema_format', 'content_type', 'headers', 'message_id', 'payload', 'correlation_id', 'tags', 'summary', 'name', 'title', 'description', 'external_docs', 'deprecated', 'examples', 'bindings', 'traits', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['schemaFormat', 'contentType', 'headers', 'messageId', 'payload', 'correlationId', 'tags', 'summary', 'name', 'title', 'description', 'externalDocs', 'deprecated', 'examples', 'bindings', 'traits', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

