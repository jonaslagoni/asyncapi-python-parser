from __future__ import annotations
from typing import Any, List, Dict, Optional, Union
from pydantic import model_serializer, model_validator, BaseModel, Field
from . import Reference
from . import ServerVariable
from . import BindingsObject
from . import Tag
class Server(BaseModel): 
  url: str = Field(description='''A URL to the target host. This URL supports Server Variables and MAY be relative, to indicate that the host location is relative to the location where the AsyncAPI document is being served.''')
  description: Optional[str] = Field(description='''An optional string describing the host designated by the URL. CommonMark syntax MAY be used for rich text representation.''', default=None)
  protocol: str = Field(description='''The protocol this URL supports for connection. Supported protocol include, but are not limited to: amqp, amqps, http, https, ibmmq, jms, kafka, kafka-secure, anypointmq, mqtt, secure-mqtt, solace, stomp, stomps, ws, wss, mercure, googlepubsub.''')
  protocol_version: Optional[str] = Field(description='''The version of the protocol used for connection. For instance: AMQP 0.9.1, HTTP 2.0, Kafka 1.0.0, etc.''', default=None, alias='''protocolVersion''')
  variables: Optional[dict[str, Reference.Reference | ServerVariable.ServerVariable]] = Field(default=None)
  security: Optional[List[dict[str, List[str]]]] = Field(description='''A declaration of which security mechanisms can be used with this server. The list of values includes alternative security requirement objects that can be used. ''', default=None)
  bindings: Optional[BindingsObject.BindingsObject] = Field(description='''A map where the keys describe the name of the protocol and the values describe protocol-specific definitions for the server.''', default=None)
  tags: Optional[List[Tag.Tag]] = Field(description='''A list of tags for logical grouping and categorization of servers.''', default=None)
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
    known_object_properties = ['url', 'description', 'protocol', 'protocol_version', 'variables', 'security', 'bindings', 'tags', 'extensions']
    unknown_object_properties = [element for element in json_properties if element not in known_object_properties]
    # Ignore attempts that validate regular models, only when unknown input is used we add unwrap extensions
    if len(unknown_object_properties) == 0: 
      return data
  
    known_json_properties = ['url', 'description', 'protocol', 'protocolVersion', 'variables', 'security', 'bindings', 'tags', 'extensions']
    extensions = {}
    for obj_key in list(data.keys()):
      if not known_json_properties.__contains__(obj_key):
        extensions[obj_key] = data.pop(obj_key, None)
    data['extensions'] = extensions
    return data

