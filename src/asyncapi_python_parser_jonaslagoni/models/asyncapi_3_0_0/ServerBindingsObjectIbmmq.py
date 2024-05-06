from __future__ import annotations
import json
from typing import Any, Dict
from . import ServerBindingsObjectIbmmqBindingVersion
class ServerBindingsObjectIbmmq: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: ServerBindingsObjectIbmmqBindingVersion.ServerBindingsObjectIbmmqBindingVersion = ServerBindingsObjectIbmmqBindingVersion.ServerBindingsObjectIbmmqBindingVersion(input['binding_version'])
    if 'group_id' in input:
      self._group_id: str = input['group_id']
    if 'ccdt_queue_manager_name' in input:
      self._ccdt_queue_manager_name: str = input['ccdt_queue_manager_name']
    if 'cipher_spec' in input:
      self._cipher_spec: str = input['cipher_spec']
    if 'multi_endpoint_server' in input:
      self._multi_endpoint_server: bool = input['multi_endpoint_server']
    if 'heart_beat_interval' in input:
      self._heart_beat_interval: int = input['heart_beat_interval']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def binding_version(self) -> ServerBindingsObjectIbmmqBindingVersion.ServerBindingsObjectIbmmqBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ServerBindingsObjectIbmmqBindingVersion.ServerBindingsObjectIbmmqBindingVersion):
    self._binding_version = binding_version

  @property
  def group_id(self) -> str:
    return self._group_id
  @group_id.setter
  def group_id(self, group_id: str):
    self._group_id = group_id

  @property
  def ccdt_queue_manager_name(self) -> str:
    return self._ccdt_queue_manager_name
  @ccdt_queue_manager_name.setter
  def ccdt_queue_manager_name(self, ccdt_queue_manager_name: str):
    self._ccdt_queue_manager_name = ccdt_queue_manager_name

  @property
  def cipher_spec(self) -> str:
    return self._cipher_spec
  @cipher_spec.setter
  def cipher_spec(self, cipher_spec: str):
    self._cipher_spec = cipher_spec

  @property
  def multi_endpoint_server(self) -> bool:
    return self._multi_endpoint_server
  @multi_endpoint_server.setter
  def multi_endpoint_server(self, multi_endpoint_server: bool):
    self._multi_endpoint_server = multi_endpoint_server

  @property
  def heart_beat_interval(self) -> int:
    return self._heart_beat_interval
  @heart_beat_interval.setter
  def heart_beat_interval(self, heart_beat_interval: int):
    self._heart_beat_interval = heart_beat_interval

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
    return ServerBindingsObjectIbmmq(**json.loads(json_string))
