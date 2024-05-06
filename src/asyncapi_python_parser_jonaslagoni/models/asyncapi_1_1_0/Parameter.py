from __future__ import annotations
import json
from typing import Any, List, Dict
from . import Schema
class Parameter: 
  def __init__(self, input: Dict):
    if 'description' in input:
      self._description: str = input['description']
    if 'name' in input:
      self._name: str = input['name']
    if 'schema' in input:
      self._schema: Schema.Schema = Schema.Schema(input['schema'])
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

  @property
  def name(self) -> str:
    return self._name
  @name.setter
  def name(self, name: str):
    self._name = name

  @property
  def schema(self) -> Schema.Schema:
    return self._schema
  @schema.setter
  def schema(self, schema: Schema.Schema):
    self._schema = schema

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
    return Parameter(**json.loads(json_string))
