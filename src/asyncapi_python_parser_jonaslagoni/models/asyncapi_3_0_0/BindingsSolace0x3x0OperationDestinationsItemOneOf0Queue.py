from __future__ import annotations
from typing import List, Any, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import BindingsSolace0x3x0OperationDestinationsItemOneOf0QueueAccessType
class BindingsSolace0x3x0OperationDestinationsItemOneOf0Queue(BaseModel): 
  name: Optional[str] = Field(description='''The name of the queue''', default=None)
  topic_subscriptions: Optional[List[str]] = Field(description='''The list of topics that the queue subscribes to.''', default=None, alias='''topicSubscriptions''')
  access_type: Optional[BindingsSolace0x3x0OperationDestinationsItemOneOf0QueueAccessType.BindingsSolace0x3x0OperationDestinationsItemOneOf0QueueAccessType] = Field(default=None, alias='''accessType''')
  max_ttl: Optional[str] = Field(description='''The maximum TTL to apply to messages to be spooled.''', default=None, alias='''maxTtl''')
  max_msg_spool_usage: Optional[str] = Field(description='''The maximum amount of message spool that the given queue may use''', default=None, alias='''maxMsgSpoolUsage''')
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
    known_object_properties = ['name', 'topic_subscriptions', 'access_type', 'max_ttl', 'max_msg_spool_usage', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['name', 'topicSubscriptions', 'accessType', 'maxTtl', 'maxMsgSpoolUsage', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

