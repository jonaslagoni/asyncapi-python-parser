from __future__ import annotations
import json
from typing import Any, Dict
from . import ServerBindingsObjectKafkaBindingVersion
class ServerBindingsObjectKafka: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: ServerBindingsObjectKafkaBindingVersion.ServerBindingsObjectKafkaBindingVersion = ServerBindingsObjectKafkaBindingVersion.ServerBindingsObjectKafkaBindingVersion(input['binding_version'])
    if 'schema_registry_url' in input:
      self._schema_registry_url: str = input['schema_registry_url']
    if 'schema_registry_vendor' in input:
      self._schema_registry_vendor: str = input['schema_registry_vendor']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> ServerBindingsObjectKafkaBindingVersion.ServerBindingsObjectKafkaBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ServerBindingsObjectKafkaBindingVersion.ServerBindingsObjectKafkaBindingVersion):
    self._binding_version = binding_version

  @property
  def schema_registry_url(self) -> str:
    return self._schema_registry_url
  @schema_registry_url.setter
  def schema_registry_url(self, schema_registry_url: str):
    self._schema_registry_url = schema_registry_url

  @property
  def schema_registry_vendor(self) -> str:
    return self._schema_registry_vendor
  @schema_registry_vendor.setter
  def schema_registry_vendor(self, schema_registry_vendor: str):
    self._schema_registry_vendor = schema_registry_vendor

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
    return ServerBindingsObjectKafka(**json.loads(json_string))