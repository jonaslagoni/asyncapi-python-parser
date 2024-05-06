from __future__ import annotations
import json
from typing import Any, Dict
from . import ServerBindingsObjectSolaceBindingVersion
class ServerBindingsObjectSolace: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: ServerBindingsObjectSolaceBindingVersion.ServerBindingsObjectSolaceBindingVersion = ServerBindingsObjectSolaceBindingVersion.ServerBindingsObjectSolaceBindingVersion(input['binding_version'])
    if 'msg_vpn' in input:
      self._msg_vpn: str = input['msg_vpn']
    if 'msv_vpn' in input:
      self._msv_vpn: str = input['msv_vpn']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def binding_version(self) -> ServerBindingsObjectSolaceBindingVersion.ServerBindingsObjectSolaceBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ServerBindingsObjectSolaceBindingVersion.ServerBindingsObjectSolaceBindingVersion):
    self._binding_version = binding_version

  @property
  def msg_vpn(self) -> str:
    return self._msg_vpn
  @msg_vpn.setter
  def msg_vpn(self, msg_vpn: str):
    self._msg_vpn = msg_vpn

  @property
  def msv_vpn(self) -> str:
    return self._msv_vpn
  @msv_vpn.setter
  def msv_vpn(self, msv_vpn: str):
    self._msv_vpn = msv_vpn

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
    return ServerBindingsObjectSolace(**json.loads(json_string))
