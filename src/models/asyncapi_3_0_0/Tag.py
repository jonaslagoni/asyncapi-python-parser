from .Reference import Reference
from .ExternalDocs import ExternalDocs
import json
from typing import Any, Dict
class Tag: 
  def __init__(self, input: Dict):
    self._name: str = input['name']
    if hasattr(input, 'description'):
      self._description: str = input['description']
    if hasattr(input, 'external_docs'):
      self._external_docs: Reference | ExternalDocs = input['external_docs']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def name(self) -> str:
    return self._name
  @name.setter
  def name(self, name: str):
    self._name = name

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

  @property
  def external_docs(self) -> Reference | ExternalDocs:
    return self._external_docs
  @external_docs.setter
  def external_docs(self, external_docs: Reference | ExternalDocs):
    self._external_docs = external_docs

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
    return Tag(**json.loads(json_string))
