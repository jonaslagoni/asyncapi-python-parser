from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import MessageBindingsObjectHttp
from . import MessageBindingsObjectAmqp
from . import MessageBindingsObjectMqtt
from . import MessageBindingsObjectKafka
from . import MessageBindingsObjectAnypointmq
from . import MessageBindingsObjectJms
from . import MessageBindingsObjectIbmmq
from . import MessageBindingsObjectGooglepubsub
class MessageBindingsObject(BaseModel): 
  http: Optional[MessageBindingsObjectHttp.MessageBindingsObjectHttp] = Field(default=None)
  ws: Optional[Any] = Field(default=None)
  amqp: Optional[MessageBindingsObjectAmqp.MessageBindingsObjectAmqp] = Field(default=None)
  amqp1: Optional[Any] = Field(default=None)
  mqtt: Optional[MessageBindingsObjectMqtt.MessageBindingsObjectMqtt] = Field(default=None)
  kafka: Optional[MessageBindingsObjectKafka.MessageBindingsObjectKafka] = Field(default=None)
  anypointmq: Optional[MessageBindingsObjectAnypointmq.MessageBindingsObjectAnypointmq] = Field(default=None)
  nats: Optional[Any] = Field(default=None)
  jms: Optional[MessageBindingsObjectJms.MessageBindingsObjectJms] = Field(default=None)
  sns: Optional[Any] = Field(default=None)
  sqs: Optional[Any] = Field(default=None)
  stomp: Optional[Any] = Field(default=None)
  redis: Optional[Any] = Field(default=None)
  ibmmq: Optional[MessageBindingsObjectIbmmq.MessageBindingsObjectIbmmq] = Field(default=None)
  solace: Optional[Any] = Field(default=None)
  googlepubsub: Optional[MessageBindingsObjectGooglepubsub.MessageBindingsObjectGooglepubsub] = Field(default=None)
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
    known_object_properties = ['http', 'ws', 'amqp', 'amqp1', 'mqtt', 'kafka', 'anypointmq', 'nats', 'jms', 'sns', 'sqs', 'stomp', 'redis', 'ibmmq', 'solace', 'googlepubsub', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['http', 'ws', 'amqp', 'amqp1', 'mqtt', 'kafka', 'anypointmq', 'nats', 'jms', 'sns', 'sqs', 'stomp', 'redis', 'ibmmq', 'solace', 'googlepubsub', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

