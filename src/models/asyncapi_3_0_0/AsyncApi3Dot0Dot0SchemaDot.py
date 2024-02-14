from .Info import Info
from .Reference import Reference
from .Server import Server
from .Channel import Channel
from .Operation import Operation
from .Components import Components
import json
from typing import Any, List, Dict
class AsyncApi3Dot0Dot0SchemaDot: 
  def __init__(self, input: Dict):
    self._asyncapi: str = '3.0.0'
    if hasattr(input, 'id'):
      self._id: str = input['id']
    self._info: Info = Info(input['info'])
    if hasattr(input, 'servers'):
      self._servers: dict[str, Reference | Server] = input['servers']
    if hasattr(input, 'default_content_type'):
      self._default_content_type: str = input['default_content_type']
    if hasattr(input, 'channels'):
      self._channels: dict[str, Reference | Channel] = input['channels']
    if hasattr(input, 'operations'):
      self._operations: dict[str, Reference | Operation] = input['operations']
    if hasattr(input, 'components'):
      self._components: Components = Components(input['components'])
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

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
  def info(self) -> Info:
    return self._info
  @info.setter
  def info(self, info: Info):
    self._info = info

  @property
  def servers(self) -> dict[str, Reference | Server]:
    return self._servers
  @servers.setter
  def servers(self, servers: dict[str, Reference | Server]):
    self._servers = servers

  @property
  def default_content_type(self) -> str:
    return self._default_content_type
  @default_content_type.setter
  def default_content_type(self, default_content_type: str):
    self._default_content_type = default_content_type

  @property
  def channels(self) -> dict[str, Reference | Channel]:
    return self._channels
  @channels.setter
  def channels(self, channels: dict[str, Reference | Channel]):
    self._channels = channels

  @property
  def operations(self) -> dict[str, Reference | Operation]:
    return self._operations
  @operations.setter
  def operations(self, operations: dict[str, Reference | Operation]):
    self._operations = operations

  @property
  def components(self) -> Components:
    return self._components
  @components.setter
  def components(self, components: Components):
    self._components = components

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
    return AsyncApi3Dot0Dot0SchemaDot(**json.loads(json_string))
