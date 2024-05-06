from __future__ import annotations
import json
from typing import Any, Dict
from . import Reference
from . import ExternalDocs
class Tag: 
  def __init__(self, input: Dict):
    self._name: str = input['name']
    if 'description' in input:
      self._description: str = input['description']
    if 'external_docs' in input:
      self._external_docs: Reference.Reference | ExternalDocs.ExternalDocs = input['external_docs']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

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
  def external_docs(self) -> Reference.Reference | ExternalDocs.ExternalDocs:
    return self._external_docs
  @external_docs.setter
  def external_docs(self, external_docs: Reference.Reference | ExternalDocs.ExternalDocs):
    self._external_docs = external_docs

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
    return Tag(**json.loads(json_string))
