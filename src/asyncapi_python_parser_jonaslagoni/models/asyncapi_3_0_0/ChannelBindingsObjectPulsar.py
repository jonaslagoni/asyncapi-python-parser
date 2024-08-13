from __future__ import annotations
from typing import List, Any, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import BindingsPulsar0x1x0ChannelPersistence
from . import BindingsPulsar0x1x0ChannelRetention
class ChannelBindingsObjectPulsar(BaseModel): 
  binding_version: Optional[str] = Field(default=None, alias='''bindingVersion''')
  namespace: Optional[str] = Field(default=None)
  persistence: Optional[BindingsPulsar0x1x0ChannelPersistence.BindingsPulsar0x1x0ChannelPersistence] = Field(default=None)
  compaction: Optional[int] = Field(default=None)
  geo_replication: Optional[List[str]] = Field(default=None, alias='''geo-replication''')
  retention: Optional[BindingsPulsar0x1x0ChannelRetention.BindingsPulsar0x1x0ChannelRetention] = Field(default=None)
  ttl: Optional[int] = Field(default=None)
  deduplication: Optional[bool] = Field(default=None)
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
    known_object_properties = ['binding_version', 'namespace', 'persistence', 'compaction', 'geo_replication', 'retention', 'ttl', 'deduplication', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['bindingVersion', 'namespace', 'persistence', 'compaction', 'geo-replication', 'retention', 'ttl', 'deduplication', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

