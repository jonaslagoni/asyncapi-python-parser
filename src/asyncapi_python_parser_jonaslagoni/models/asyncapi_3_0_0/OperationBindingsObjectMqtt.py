from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import BindingsMqtt0x2x0OperationQos
from . import SchemaObject
from . import Reference
class OperationBindingsObjectMqtt(BaseModel): 
  binding_version: Optional[str] = Field(default=None, alias='''bindingVersion''')
  qos: Optional[BindingsMqtt0x2x0OperationQos.BindingsMqtt0x2x0OperationQos] = Field(default=None)
  retain: Optional[bool] = Field(default=None)
  message_expiry_interval: Optional[Union[int, SchemaObject.SchemaObject | bool, Reference.Reference]] = Field(default=None, alias='''messageExpiryInterval''')
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
    known_object_properties = ['binding_version', 'qos', 'retain', 'message_expiry_interval', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['bindingVersion', 'qos', 'retain', 'messageExpiryInterval', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

