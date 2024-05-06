from __future__ import annotations
import json
from typing import Any, Dict
from . import ServerBindingsObjectPulsarBindingVersion
class ServerBindingsObjectPulsar: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: ServerBindingsObjectPulsarBindingVersion.ServerBindingsObjectPulsarBindingVersion = ServerBindingsObjectPulsarBindingVersion.ServerBindingsObjectPulsarBindingVersion(input['binding_version'])
    if 'tenant' in input:
      self._tenant: str = input['tenant']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> ServerBindingsObjectPulsarBindingVersion.ServerBindingsObjectPulsarBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ServerBindingsObjectPulsarBindingVersion.ServerBindingsObjectPulsarBindingVersion):
    self._binding_version = binding_version

  @property
  def tenant(self) -> str:
    return self._tenant
  @tenant.setter
  def tenant(self, tenant: str):
    self._tenant = tenant

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
    return ServerBindingsObjectPulsar(**json.loads(json_string))