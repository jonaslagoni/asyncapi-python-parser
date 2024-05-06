from __future__ import annotations
import json
from typing import List, Any, Dict
from . import BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion
class ServerSchema: 
  def __init__(self, input: Dict):
    self._jms_connection_factory: str = input['jms_connection_factory']
    if 'properties' in input:
      self._properties: List[ServerSchema] = input['properties']
    if 'client_id' in input:
      self._client_id: str = input['client_id']
    if 'binding_version' in input:
      self._binding_version: BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion.BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion = BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion.BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion(input['binding_version'])
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def jms_connection_factory(self) -> str:
    return self._jms_connection_factory
  @jms_connection_factory.setter
  def jms_connection_factory(self, jms_connection_factory: str):
    self._jms_connection_factory = jms_connection_factory

  @property
  def properties(self) -> List[ServerSchema]:
    return self._properties
  @properties.setter
  def properties(self, properties: List[ServerSchema]):
    self._properties = properties

  @property
  def client_id(self) -> str:
    return self._client_id
  @client_id.setter
  def client_id(self, client_id: str):
    self._client_id = client_id

  @property
  def binding_version(self) -> BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion.BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion.BindingsMinusJmsMinus0Dot0Dot1MinusServerBindingVersion):
    self._binding_version = binding_version

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
    return ServerSchema(**json.loads(json_string))
