from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import Info
from . import Server
from . import Topics
from . import Components
from . import Tag
from . import ExternalDocs
class AsyncApi1x0Schemax(BaseModel): 
  asyncapi: str = Field(description='''The AsyncAPI specification version of this document.''')
  info: Info.Info = Field(description='''General information about the API.''')
  base_topic: Optional[str] = Field(description='''The base topic to the API. Example: 'hitch'.''', default=None, alias='''baseTopic''')
  servers: Optional[List[Server.Server]] = Field(default=None)
  topics: Topics.Topics = Field(description='''Relative paths to the individual topics. They must be relative to the 'baseTopic'.''')
  components: Optional[Components.Components] = Field(description='''An object to hold a set of reusable objects for different aspects of the AsyncAPI Specification.''', default=None)
  tags: Optional[List[Tag.Tag]] = Field(default=None)
  security: Optional[List[dict[str, List[str]]]] = Field(default=None)
  external_docs: Optional[ExternalDocs.ExternalDocs] = Field(description='''information about external documentation''', default=None, alias='''externalDocs''')
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
    known_object_properties = ['asyncapi', 'info', 'base_topic', 'servers', 'topics', 'components', 'tags', 'security', 'external_docs', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['asyncapi', 'info', 'baseTopic', 'servers', 'topics', 'components', 'tags', 'security', 'externalDocs', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

