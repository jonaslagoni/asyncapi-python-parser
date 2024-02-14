from .BearerHttpSecuritySchemeScheme import BearerHttpSecuritySchemeScheme
from .BearerHttpSecuritySchemeType import BearerHttpSecuritySchemeType
import json
from typing import Any, Dict
class BearerHttpSecurityScheme: 
  def __init__(self, input: Dict):
    self._scheme: BearerHttpSecuritySchemeScheme = BearerHttpSecuritySchemeScheme(input['scheme'])
    if hasattr(input, 'bearer_format'):
      self._bearer_format: str = input['bearer_format']
    self._type: BearerHttpSecuritySchemeType = BearerHttpSecuritySchemeType(input['type'])
    if hasattr(input, 'description'):
      self._description: str = input['description']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def scheme(self) -> BearerHttpSecuritySchemeScheme:
    return self._scheme
  @scheme.setter
  def scheme(self, scheme: BearerHttpSecuritySchemeScheme):
    self._scheme = scheme

  @property
  def bearer_format(self) -> str:
    return self._bearer_format
  @bearer_format.setter
  def bearer_format(self, bearer_format: str):
    self._bearer_format = bearer_format

  @property
  def type(self) -> BearerHttpSecuritySchemeType:
    return self._type
  @type.setter
  def type(self, type: BearerHttpSecuritySchemeType):
    self._type = type

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

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
    return BearerHttpSecurityScheme(**json.loads(json_string))
