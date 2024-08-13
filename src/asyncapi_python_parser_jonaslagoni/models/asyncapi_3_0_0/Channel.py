from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import Reference
from . import MessageObject
from . import Parameter
from . import Tag
from . import ExternalDocs
from . import ChannelBindingsObject
class Channel(BaseModel): 
  address: Optional[str] = Field(description='''An optional string representation of this channel's address. The address is typically the "topic name", "routing key", "event type", or "path". When `null` or absent, it MUST be interpreted as unknown. This is useful when the address is generated dynamically at runtime or can't be known upfront. It MAY contain Channel Address Expressions.''', default=None)
  messages: Optional[dict[str, Reference.Reference | MessageObject.MessageObject]] = Field(default=None)
  parameters: Optional[dict[str, Reference.Reference | Parameter.Parameter]] = Field(default=None)
  title: Optional[str] = Field(description='''A human-friendly title for the channel.''', default=None)
  summary: Optional[str] = Field(description='''A brief summary of the channel.''', default=None)
  description: Optional[str] = Field(description='''A longer description of the channel. CommonMark is allowed.''', default=None)
  servers: Optional[List[Reference.Reference]] = Field(description='''The references of the servers on which this channel is available. If absent or empty then this channel must be available on all servers.''', default=None)
  tags: Optional[List[Reference.Reference | Tag.Tag]] = Field(description='''A list of tags for logical grouping of channels.''', default=None)
  external_docs: Optional[Union[Reference.Reference, ExternalDocs.ExternalDocs]] = Field(default=None, alias='''externalDocs''')
  bindings: Optional[Union[Reference.Reference, ChannelBindingsObject.ChannelBindingsObject]] = Field(default=None)
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
    known_object_properties = ['address', 'messages', 'parameters', 'title', 'summary', 'description', 'servers', 'tags', 'external_docs', 'bindings', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['address', 'messages', 'parameters', 'title', 'summary', 'description', 'servers', 'tags', 'externalDocs', 'bindings', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

