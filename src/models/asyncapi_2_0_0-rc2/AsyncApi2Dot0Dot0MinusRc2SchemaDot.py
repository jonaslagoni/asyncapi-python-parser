from .Asyncapi import Asyncapi
from .Info import Info
from .Server import Server
from .ChannelItem import ChannelItem
from .Components import Components
from .Tag import Tag
from .ExternalDocs import ExternalDocs
import json
from typing import Any, List, Dict
class AsyncApi2Dot0Dot0MinusRc2SchemaDot: 
  def __init__(self, input: Dict):
    self._asyncapi: Asyncapi = Asyncapi(input['asyncapi'])
    if hasattr(input, 'id'):
      self._id: str = input['id']
    self._info: Info = Info(input['info'])
    if hasattr(input, 'servers'):
      self._servers: dict[str, Server] = input['servers']
    if hasattr(input, 'default_content_type'):
      self._default_content_type: str = input['default_content_type']
    self._channels: dict[str, ChannelItem] = input['channels']
    if hasattr(input, 'components'):
      self._components: Components = Components(input['components'])
    if hasattr(input, 'tags'):
      self._tags: List[Tag] = input['tags']
    if hasattr(input, 'external_docs'):
      self._external_docs: ExternalDocs = ExternalDocs(input['external_docs'])
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def asyncapi(self) -> Asyncapi:
    return self._asyncapi
  @asyncapi.setter
  def asyncapi(self, asyncapi: Asyncapi):
    self._asyncapi = asyncapi

  @property
  def id(self) -> str:
    return self._id
  @id.setter
  def id(self, id: str):
    self._id = id

  @property
  def info(self) -> Info:
    return self._info
  @info.setter
  def info(self, info: Info):
    self._info = info

  @property
  def servers(self) -> dict[str, Server]:
    return self._servers
  @servers.setter
  def servers(self, servers: dict[str, Server]):
    self._servers = servers

  @property
  def default_content_type(self) -> str:
    return self._default_content_type
  @default_content_type.setter
  def default_content_type(self, default_content_type: str):
    self._default_content_type = default_content_type

  @property
  def channels(self) -> dict[str, ChannelItem]:
    return self._channels
  @channels.setter
  def channels(self, channels: dict[str, ChannelItem]):
    self._channels = channels

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
    return AsyncApi2Dot0Dot0MinusRc2SchemaDot(**json.loads(json_string))
