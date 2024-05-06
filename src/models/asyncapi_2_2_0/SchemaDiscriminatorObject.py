
import json
from typing import Any, Dict
class SchemaDiscriminatorObject: 
  def __init__(self, input: Dict):
    self._property_name: str = input['property_name']
    if 'mapping' in input:
      self._mapping: dict[str, str] = input['mapping']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

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
  def additional_properties(self) -> dict[str, Any]:
    return self._additional_properties
  @additional_properties.setter
  def additional_properties(self, additional_properties: dict[str, Any]):
    self._additional_properties = additional_properties

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return SchemaDiscriminatorObject(**json.loads(json_string))
