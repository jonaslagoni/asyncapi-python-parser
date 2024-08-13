from __future__ import annotations
from typing import List, Any, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import BindingsSolace0x3x0OperationDestinationsItemDeliveryMode
from . import BindingsSolace0x3x0OperationDestinationsItemOneOf0Queue
class BindingsSolace0x3x0OperationDestinationsItemOneOf0(BaseModel): 
  delivery_mode: Optional[BindingsSolace0x3x0OperationDestinationsItemDeliveryMode.BindingsSolace0x3x0OperationDestinationsItemDeliveryMode] = Field(default=None, alias='''deliveryMode''')
  destination_type: Optional[str] = Field(description='''If the type is queue, then the subscriber can bind to the queue. The queue subscribes to the given topicSubscriptions. If no topicSubscriptions are provied, the queue will subscribe to the topic as represented by the channel name.''', default=None, alias='''destinationType''')
  queue: Optional[BindingsSolace0x3x0OperationDestinationsItemOneOf0Queue.BindingsSolace0x3x0OperationDestinationsItemOneOf0Queue] = Field(default=None)
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
    known_object_properties = ['delivery_mode', 'destination_type', 'queue', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['deliveryMode', 'destinationType', 'queue', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

