from __future__ import annotations
import json
from typing import List, Any, Dict

class ServerVariable: 
  def __init__(self, input: Dict):
    if 'enum' in input:
      self._enum: List[str] = input['enum']
    if 'default' in input:
      self._default: str = input['default']
    if 'description' in input:
      self._description: str = input['description']
    if 'examples' in input:
      self._examples: List[str] = input['examples']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def enum(self) -> List[str]:
    return self._enum
  @enum.setter
  def enum(self, enum: List[str]):
    self._enum = enum

  @property
  def default(self) -> str:
    return self._default
  @default.setter
  def default(self, default: str):
    self._default = default

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

  @property
  def examples(self) -> List[str]:
    return self._examples
  @examples.setter
  def examples(self, examples: List[str]):
    self._examples = examples

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
    return ServerVariable(**json.loads(json_string))
