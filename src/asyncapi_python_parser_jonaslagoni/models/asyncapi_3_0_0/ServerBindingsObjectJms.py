from __future__ import annotations
import json
from typing import Any, List, Dict
from . import BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion
from . import ServerSchema
class ServerBindingsObjectJms: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion.BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion = BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion.BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion(input['binding_version'])
    if 'jms_connection_factory' in input:
      self._jms_connection_factory: str = input['jms_connection_factory']
    if 'properties' in input:
      self._properties: List[ServerSchema.ServerSchema] = input['properties']
    if 'client_id' in input:
      self._client_id: str = input['client_id']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def binding_version(self) -> BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion.BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion.BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion):
    self._binding_version = binding_version

  @property
  def jms_connection_factory(self) -> str:
    return self._jms_connection_factory
  @jms_connection_factory.setter
  def jms_connection_factory(self, jms_connection_factory: str):
    self._jms_connection_factory = jms_connection_factory

  @property
  def properties(self) -> List[ServerSchema.ServerSchema]:
    return self._properties
  @properties.setter
  def properties(self, properties: List[ServerSchema.ServerSchema]):
    self._properties = properties

  @property
  def client_id(self) -> str:
    return self._client_id
  @client_id.setter
  def client_id(self, client_id: str):
    self._client_id = client_id

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
    return ServerBindingsObjectJms(**json.loads(json_string))
