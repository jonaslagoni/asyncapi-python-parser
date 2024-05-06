from __future__ import annotations
import json
from typing import Any, Dict

class SchemaAllOf1DiscriminatorObject: 
  def __init__(self, input: Dict):
    self._property_name: str = input['property_name']
    if 'mapping' in input:
      self._mapping: dict[str, str] = input['mapping']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def property_name(self) -> str:
    return self._property_name
  @property_name.setter
  def property_name(self, property_name: str):
    self._property_name = property_name

  @property
  def mapping(self) -> dict[str, str]:
    return self._mapping
  @mapping.setter
  def mapping(self, mapping: dict[str, str]):
    self._mapping = mapping

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
    return SchemaAllOf1DiscriminatorObject(**json.loads(json_string))
