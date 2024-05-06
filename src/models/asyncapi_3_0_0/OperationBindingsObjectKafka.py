from __future__ import annotations
import json
from typing import Any, List, Dict
from . import OperationBindingsObjectKafkaBindingVersion
from . import SchemaObject
class OperationBindingsObjectKafka: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: OperationBindingsObjectKafkaBindingVersion.OperationBindingsObjectKafkaBindingVersion = OperationBindingsObjectKafkaBindingVersion.OperationBindingsObjectKafkaBindingVersion(input['binding_version'])
    if 'group_id' in input:
      self._group_id: SchemaObject.SchemaObject | bool = input['group_id']
    if 'client_id' in input:
      self._client_id: SchemaObject.SchemaObject | bool = input['client_id']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> OperationBindingsObjectKafkaBindingVersion.OperationBindingsObjectKafkaBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: OperationBindingsObjectKafkaBindingVersion.OperationBindingsObjectKafkaBindingVersion):
    self._binding_version = binding_version

  @property
  def group_id(self) -> SchemaObject.SchemaObject | bool:
    return self._group_id
  @group_id.setter
  def group_id(self, group_id: SchemaObject.SchemaObject | bool):
    self._group_id = group_id

  @property
  def client_id(self) -> SchemaObject.SchemaObject | bool:
    return self._client_id
  @client_id.setter
  def client_id(self, client_id: SchemaObject.SchemaObject | bool):
    self._client_id = client_id

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
    return OperationBindingsObjectKafka(**json.loads(json_string))
