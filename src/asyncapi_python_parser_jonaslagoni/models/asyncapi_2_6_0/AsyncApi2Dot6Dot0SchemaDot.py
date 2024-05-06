from __future__ import annotations
import json
from typing import Any, List, Dict
from . import Asyncapi
from . import Info
from . import Reference
from . import Server
from . import ChannelItem
from . import Components
from . import Tag
from . import ExternalDocs
class AsyncApi2Dot6Dot0SchemaDot: 
  def __init__(self, input: Dict):
    self._asyncapi: Asyncapi.Asyncapi = Asyncapi.Asyncapi(input['asyncapi'])
    if 'id' in input:
      self._id: str = input['id']
    self._info: Info.Info = Info.Info(input['info'])
    if 'servers' in input:
      self._servers: dict[str, Reference.Reference | Server.Server] = input['servers']
    if 'default_content_type' in input:
      self._default_content_type: str = input['default_content_type']
    self._channels: dict[str, ChannelItem.ChannelItem] = input['channels']
    if 'components' in input:
      self._components: Components.Components = Components.Components(input['components'])
    if 'tags' in input:
      self._tags: List[Tag.Tag] = input['tags']
    if 'external_docs' in input:
      self._external_docs: ExternalDocs.ExternalDocs = ExternalDocs.ExternalDocs(input['external_docs'])
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def asyncapi(self) -> Asyncapi.Asyncapi:
    return self._asyncapi
  @asyncapi.setter
  def asyncapi(self, asyncapi: Asyncapi.Asyncapi):
    self._asyncapi = asyncapi

  @property
  def id(self) -> str:
    return self._id
  @id.setter
  def id(self, id: str):
    self._id = id

  @property
  def info(self) -> Info.Info:
    return self._info
  @info.setter
  def info(self, info: Info.Info):
    self._info = info

  @property
  def servers(self) -> dict[str, Reference.Reference | Server.Server]:
    return self._servers
  @servers.setter
  def servers(self, servers: dict[str, Reference.Reference | Server.Server]):
    self._servers = servers

  @property
  def default_content_type(self) -> str:
    return self._default_content_type
  @default_content_type.setter
  def default_content_type(self, default_content_type: str):
    self._default_content_type = default_content_type

  @property
  def channels(self) -> dict[str, ChannelItem.ChannelItem]:
    return self._channels
  @channels.setter
  def channels(self, channels: dict[str, ChannelItem.ChannelItem]):
    self._channels = channels

  @property
  def components(self) -> Components.Components:
    return self._components
  @components.setter
  def components(self, components: Components.Components):
    self._components = components

  @property
  def tags(self) -> List[Tag.Tag]:
    return self._tags
  @tags.setter
  def tags(self, tags: List[Tag.Tag]):
    self._tags = tags

  @property
  def external_docs(self) -> ExternalDocs.ExternalDocs:
    return self._external_docs
  @external_docs.setter
  def external_docs(self, external_docs: ExternalDocs.ExternalDocs):
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
    return AsyncApi2Dot6Dot0SchemaDot(**json.loads(json_string))
