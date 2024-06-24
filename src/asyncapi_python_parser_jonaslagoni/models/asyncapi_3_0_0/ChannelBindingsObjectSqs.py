from __future__ import annotations
from typing import Any, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import BindingsSqs0x2x0ChannelBindingVersion
from . import ChannelSchema
class ChannelBindingsObjectSqs(BaseModel): 
  binding_version: Optional[BindingsSqs0x2x0ChannelBindingVersion.BindingsSqs0x2x0ChannelBindingVersion] = Field(default=None, alias='''bindingVersion''')
  queue: Optional[ChannelSchema.ChannelSchema] = Field(default=None)
  dead_letter_queue: Optional[ChannelSchema.ChannelSchema] = Field(default=None, alias='''deadLetterQueue''')
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
    known_object_properties = ['binding_version', 'queue', 'dead_letter_queue', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['bindingVersion', 'queue', 'deadLetterQueue', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

