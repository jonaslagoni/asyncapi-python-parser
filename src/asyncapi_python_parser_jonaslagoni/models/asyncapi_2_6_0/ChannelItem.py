from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import Reference
from . import Parameter
from . import Operation
from . import BindingsObject
class ChannelItem(BaseModel): 
  dollar_ref: Optional[str] = Field(description='''A simple object to allow referencing other components in the specification, internally and externally.''', default=None, alias='''$ref''')
  parameters: Optional[dict[str, Reference.Reference | Parameter.Parameter]] = Field(default=None)
  description: Optional[str] = Field(description='''A description of the channel.''', default=None)
  servers: Optional[List[str]] = Field(description='''The names of the servers on which this channel is available. If absent or empty then this channel must be available on all servers.''', default=None)
  publish: Optional[Operation.Operation] = Field(description='''Describes a publish or a subscribe operation. This provides a place to document how and why messages are sent and received.''', default=None)
  subscribe: Optional[Operation.Operation] = Field(description='''Describes a publish or a subscribe operation. This provides a place to document how and why messages are sent and received.''', default=None)
  deprecated: Optional[bool] = Field(default=None)
  bindings: Optional[BindingsObject.BindingsObject] = Field(description='''Map describing protocol-specific definitions for a server.''', default=None)
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
    known_object_properties = ['dollar_ref', 'parameters', 'description', 'servers', 'publish', 'subscribe', 'deprecated', 'bindings', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['$ref', 'parameters', 'description', 'servers', 'publish', 'subscribe', 'deprecated', 'bindings', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

