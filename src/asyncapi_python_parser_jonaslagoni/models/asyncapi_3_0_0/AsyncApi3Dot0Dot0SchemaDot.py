from __future__ import annotations
import json
from typing import Any, List, Dict
from . import Info
from . import Reference
from . import Server
from . import Channel
from . import Operation
from . import Components
class AsyncApi3Dot0Dot0SchemaDot: 
  def __init__(self, input: Dict):
    self._asyncapi: str = '3.0.0'
    if 'id' in input:
      self._id: str = input['id']
    self._info: Info.Info = Info.Info(input['info'])
    if 'servers' in input:
      self._servers: dict[str, Reference.Reference | Server.Server] = input['servers']
    if 'default_content_type' in input:
      self._default_content_type: str = input['default_content_type']
    if 'channels' in input:
      self._channels: dict[str, Reference.Reference | Channel.Channel] = input['channels']
    if 'operations' in input:
      self._operations: dict[str, Reference.Reference | Operation.Operation] = input['operations']
    if 'components' in input:
      self._components: Components.Components = Components.Components(input['components'])
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def asyncapi(self) -> str:
    return self._asyncapi

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
  def channels(self) -> dict[str, Reference.Reference | Channel.Channel]:
    return self._channels
  @channels.setter
  def channels(self, channels: dict[str, Reference.Reference | Channel.Channel]):
    self._channels = channels

  @property
  def operations(self) -> dict[str, Reference.Reference | Operation.Operation]:
    return self._operations
  @operations.setter
  def operations(self, operations: dict[str, Reference.Reference | Operation.Operation]):
    self._operations = operations

  @property
  def components(self) -> Components.Components:
    return self._components
  @components.setter
  def components(self, components: Components.Components):
    self._components = components

  @property
  def extensions(self) -> dict[str, Any]:
    return self._extensions
  @extensions.setter
  def extensions(self, extensions: dict[str, Any]):
    self._extensions = extensions

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return AsyncApi3Dot0Dot0SchemaDot(**json.loads(json_string))
