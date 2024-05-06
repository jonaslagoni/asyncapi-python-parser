from __future__ import annotations
import json
from typing import Any, Dict
from . import PrimitiveType
class PrimitiveTypeWithMetadata: 
  def __init__(self, input: Dict):
    self._type: PrimitiveType.PrimitiveType = PrimitiveType.PrimitiveType(input['type'])
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def type(self) -> PrimitiveType.PrimitiveType:
    return self._type
  @type.setter
  def type(self, type: PrimitiveType.PrimitiveType):
    self._type = type

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
    return PrimitiveTypeWithMetadata(**json.loads(json_string))
