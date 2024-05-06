from __future__ import annotations
import json
from typing import Any, List, Dict
from . import SchemaObject
class Parameter: 
  def __init__(self, input: Dict):
    if 'description' in input:
      self._description: str = input['description']
    if 'schema' in input:
      self._schema: SchemaObject.SchemaObject | bool = input['schema']
    if 'location' in input:
      self._location: str = input['location']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

  @property
  def schema(self) -> SchemaObject.SchemaObject | bool:
    return self._schema
  @schema.setter
  def schema(self, schema: SchemaObject.SchemaObject | bool):
    self._schema = schema

  @property
  def location(self) -> str:
    return self._location
  @location.setter
  def location(self, location: str):
    self._location = location

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
    return Parameter(**json.loads(json_string))