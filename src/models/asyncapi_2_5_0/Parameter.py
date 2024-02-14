from .SchemaObject import SchemaObject
import json
from typing import Any, List, Dict
class Parameter: 
  def __init__(self, input: Dict):
    if hasattr(input, 'description'):
      self._description: str = input['description']
    if hasattr(input, 'schema'):
      self._schema: SchemaObject | bool = input['schema']
    if hasattr(input, 'location'):
      self._location: str = input['location']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

  @property
  def schema(self) -> SchemaObject | bool:
    return self._schema
  @schema.setter
  def schema(self, schema: SchemaObject | bool):
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
