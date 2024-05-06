from __future__ import annotations
import json
from typing import Any, Dict
from . import AsymmetricEncryptionType
class AsymmetricEncryption: 
  def __init__(self, input: Dict):
    self._type: AsymmetricEncryptionType.AsymmetricEncryptionType = AsymmetricEncryptionType.AsymmetricEncryptionType(input['type'])
    if 'description' in input:
      self._description: str = input['description']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def type(self) -> AsymmetricEncryptionType.AsymmetricEncryptionType:
    return self._type
  @type.setter
  def type(self, type: AsymmetricEncryptionType.AsymmetricEncryptionType):
    self._type = type

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

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
    return AsymmetricEncryption(**json.loads(json_string))
