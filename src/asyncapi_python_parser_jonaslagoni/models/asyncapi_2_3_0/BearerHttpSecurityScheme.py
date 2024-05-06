from __future__ import annotations
import json
from typing import Any, Dict
from . import BearerHttpSecuritySchemeScheme
from . import BearerHttpSecuritySchemeType
class BearerHttpSecurityScheme: 
  def __init__(self, input: Dict):
    self._scheme: BearerHttpSecuritySchemeScheme.BearerHttpSecuritySchemeScheme = BearerHttpSecuritySchemeScheme.BearerHttpSecuritySchemeScheme(input['scheme'])
    if 'bearer_format' in input:
      self._bearer_format: str = input['bearer_format']
    self._type: BearerHttpSecuritySchemeType.BearerHttpSecuritySchemeType = BearerHttpSecuritySchemeType.BearerHttpSecuritySchemeType(input['type'])
    if 'description' in input:
      self._description: str = input['description']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def scheme(self) -> BearerHttpSecuritySchemeScheme.BearerHttpSecuritySchemeScheme:
    return self._scheme
  @scheme.setter
  def scheme(self, scheme: BearerHttpSecuritySchemeScheme.BearerHttpSecuritySchemeScheme):
    self._scheme = scheme

  @property
  def bearer_format(self) -> str:
    return self._bearer_format
  @bearer_format.setter
  def bearer_format(self, bearer_format: str):
    self._bearer_format = bearer_format

  @property
  def type(self) -> BearerHttpSecuritySchemeType.BearerHttpSecuritySchemeType:
    return self._type
  @type.setter
  def type(self, type: BearerHttpSecuritySchemeType.BearerHttpSecuritySchemeType):
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
    return BearerHttpSecurityScheme(**json.loads(json_string))
