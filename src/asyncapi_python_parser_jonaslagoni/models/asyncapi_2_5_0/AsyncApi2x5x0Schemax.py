from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import Info
from . import Reference
from . import Server
from . import ChannelItem
from . import Components
from . import Tag
from . import ExternalDocs
class AsyncApi2x5x0Schemax(BaseModel): 
  asyncapi: str = Field(description='''The AsyncAPI specification version of this document.''')
  id: Optional[str] = Field(description='''A unique id representing the application.''', default=None)
  info: Info.Info = Field(description='''General information about the API.''')
  servers: Optional[dict[str, Reference.Reference | Server.Server]] = Field(default=None)
  default_content_type: Optional[str] = Field(default=None, alias='''defaultContentType''')
  channels: dict[str, ChannelItem.ChannelItem] = Field()
  components: Optional[Components.Components] = Field(description='''An object to hold a set of reusable objects for different aspects of the AsyncAPI Specification.''', default=None)
  tags: Optional[List[Tag.Tag]] = Field(default=None)
  external_docs: Optional[ExternalDocs.ExternalDocs] = Field(default=None, alias='''externalDocs''')
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
    known_object_properties = ['asyncapi', 'id', 'info', 'servers', 'default_content_type', 'channels', 'components', 'tags', 'external_docs', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['asyncapi', 'id', 'info', 'servers', 'defaultContentType', 'channels', 'components', 'tags', 'externalDocs', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

