from __future__ import annotations
from typing import List, Any, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import BindingsAmqp0x3x0OperationDeliveryMode
class OperationBindingsObjectAmqp(BaseModel): 
  binding_version: Optional[str] = Field(default=None, alias='''bindingVersion''')
  expiration: Optional[int] = Field(default=None)
  user_id: Optional[str] = Field(default=None, alias='''userId''')
  cc: Optional[List[str]] = Field(default=None)
  priority: Optional[int] = Field(default=None)
  delivery_mode: Optional[BindingsAmqp0x3x0OperationDeliveryMode.BindingsAmqp0x3x0OperationDeliveryMode] = Field(default=None, alias='''deliveryMode''')
  mandatory: Optional[bool] = Field(default=None)
  bcc: Optional[List[str]] = Field(default=None)
  timestamp: Optional[bool] = Field(default=None)
  ack: Optional[bool] = Field(default=None)
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
    known_object_properties = ['binding_version', 'expiration', 'user_id', 'cc', 'priority', 'delivery_mode', 'mandatory', 'bcc', 'timestamp', 'ack', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['bindingVersion', 'expiration', 'userId', 'cc', 'priority', 'deliveryMode', 'mandatory', 'bcc', 'timestamp', 'ack', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

