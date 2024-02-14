from .ApiKeyHttpSecuritySchemeType import ApiKeyHttpSecuritySchemeType
from .ApiKeyHttpSecuritySchemeIn import ApiKeyHttpSecuritySchemeIn
import json
from typing import Any, Dict
class ApiKeyHttpSecurityScheme: 
  def __init__(self, input: Dict):
    self._type: ApiKeyHttpSecuritySchemeType = ApiKeyHttpSecuritySchemeType(input['type'])
    self._name: str = input['name']
    self._reserved_in: ApiKeyHttpSecuritySchemeIn = ApiKeyHttpSecuritySchemeIn(input['reserved_in'])
    if hasattr(input, 'description'):
      self._description: str = input['description']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def type(self) -> ApiKeyHttpSecuritySchemeType:
    return self._type
  @type.setter
  def type(self, type: ApiKeyHttpSecuritySchemeType):
    self._type = type

  @property
  def name(self) -> str:
    return self._name
  @name.setter
  def name(self, name: str):
    self._name = name

  @property
  def reserved_in(self) -> ApiKeyHttpSecuritySchemeIn:
    return self._reserved_in
  @reserved_in.setter
  def reserved_in(self, reserved_in: ApiKeyHttpSecuritySchemeIn):
    self._reserved_in = reserved_in

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
    return ApiKeyHttpSecurityScheme(**json.loads(json_string))
