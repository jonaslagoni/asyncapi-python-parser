from .ServerBindingsObjectSolaceBindingVersion import ServerBindingsObjectSolaceBindingVersion
import json
from typing import Any, Dict
class ServerBindingsObjectSolace: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: ServerBindingsObjectSolaceBindingVersion = ServerBindingsObjectSolaceBindingVersion(input['binding_version'])
    if hasattr(input, 'msg_vpn'):
      self._msg_vpn: str = input['msg_vpn']
    if hasattr(input, 'msv_vpn'):
      self._msv_vpn: str = input['msv_vpn']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> ServerBindingsObjectSolaceBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ServerBindingsObjectSolaceBindingVersion):
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
  def additional_properties(self) -> dict[str, Any]:
    return self._additional_properties
  @additional_properties.setter
  def additional_properties(self, additional_properties: dict[str, Any]):
    self._additional_properties = additional_properties

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return ServerBindingsObjectSolace(**json.loads(json_string))
