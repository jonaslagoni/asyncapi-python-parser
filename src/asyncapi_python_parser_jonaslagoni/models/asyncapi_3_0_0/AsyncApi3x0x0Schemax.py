from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import Info
from . import Reference
from . import Server
from . import Channel
from . import Operation
from . import Components
class AsyncApi3x0x0Schemax(BaseModel): 
  asyncapi: str = Field(description='''The AsyncAPI specification version of this document.''')
  id: Optional[str] = Field(description='''A unique id representing the application.''', default=None)
  info: Info.Info = Field(description='''The object provides metadata about the API. The metadata can be used by the clients if needed.''')
  servers: Optional[dict[str, Reference.Reference | Server.Server]] = Field(default=None)
  default_content_type: Optional[str] = Field(description='''Default content type to use when encoding/decoding a message's payload.''', default=None, alias='''defaultContentType''')
  channels: Optional[dict[str, Reference.Reference | Channel.Channel]] = Field(default=None)
  operations: Optional[dict[str, Reference.Reference | Operation.Operation]] = Field(default=None)
  components: Optional[Components.Components] = Field(description='''An object to hold a set of reusable objects for different aspects of the AsyncAPI specification. All objects defined within the components object will have no effect on the API unless they are explicitly referenced from properties outside the components object.''', default=None)
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
    known_object_properties = ['asyncapi', 'id', 'info', 'servers', 'default_content_type', 'channels', 'operations', 'components', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['asyncapi', 'id', 'info', 'servers', 'defaultContentType', 'channels', 'operations', 'components', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

