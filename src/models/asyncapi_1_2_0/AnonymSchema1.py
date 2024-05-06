from .Asyncapi import Asyncapi
from .Info import Info
from .Server import Server
from .Topics import Topics
from .StreamObject import StreamObject
from .Components import Components
from .Tag import Tag
from .ExternalDocs import ExternalDocs
import json
from typing import Any, List, Dict
class AnonymSchema1: 
  def __init__(self, input: Dict):
    self._asyncapi: Asyncapi = Asyncapi(input['asyncapi'])
    self._info: Info = Info(input['info'])
    if 'base_topic' in input:
      self._base_topic: str = input['base_topic']
    if 'servers' in input:
      self._servers: List[Server] = input['servers']
    self._topics: Topics = Topics(input['topics'])
    if 'stream' in input:
      self._stream: StreamObject = StreamObject(input['stream'])
    if 'events' in input:
      self._events: Any | Any = input['events']
    if 'components' in input:
      self._components: Components = Components(input['components'])
    if 'tags' in input:
      self._tags: List[Tag] = input['tags']
    if 'security' in input:
      self._security: List[dict[str, List[str]]] = input['security']
    if 'external_docs' in input:
      self._external_docs: ExternalDocs = ExternalDocs(input['external_docs'])
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def asyncapi(self) -> Asyncapi:
    return self._asyncapi
  @asyncapi.setter
  def asyncapi(self, asyncapi: Asyncapi):
    self._asyncapi = asyncapi

  @property
  def info(self) -> Info:
    return self._info
  @info.setter
  def info(self, info: Info):
    self._info = info

  @property
  def base_topic(self) -> str:
    return self._base_topic
  @base_topic.setter
  def base_topic(self, base_topic: str):
    self._base_topic = base_topic

  @property
  def servers(self) -> List[Server]:
    return self._servers
  @servers.setter
  def servers(self, servers: List[Server]):
    self._servers = servers

  @property
  def topics(self) -> Topics:
    return self._topics
  @topics.setter
  def topics(self, topics: Topics):
    self._topics = topics

  @property
  def stream(self) -> StreamObject:
    return self._stream
  @stream.setter
  def stream(self, stream: StreamObject):
    self._stream = stream

  @property
  def events(self) -> Any | Any:
    return self._events
  @events.setter
  def events(self, events: Any | Any):
    self._events = events

  @property
  def components(self) -> Components:
    return self._components
  @components.setter
  def components(self, components: Components):
    self._components = components

  @property
  def tags(self) -> List[Tag]:
    return self._tags
  @tags.setter
  def tags(self, tags: List[Tag]):
    self._tags = tags

  @property
  def security(self) -> List[dict[str, List[str]]]:
    return self._security
  @security.setter
  def security(self, security: List[dict[str, List[str]]]):
    self._security = security

  @property
  def external_docs(self) -> ExternalDocs:
    return self._external_docs
  @external_docs.setter
  def external_docs(self, external_docs: ExternalDocs):
    self._external_docs = external_docs

  @property
  def additional_properties(self) -> dict[str, Any]:
    return self._additional_properties
  @additional_properties.setter
  def additional_properties(self, additional_properties: dict[str, Any]):
    self._additional_properties = additional_properties

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return AnonymSchema1(**json.loads(json_string))
