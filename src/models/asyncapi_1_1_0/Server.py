from .ServerScheme import ServerScheme
from .ServerVariable import ServerVariable
import json
from typing import List, Any, Dict
class Server: 
  def __init__(self, input: Dict):
    self._url: str = input['url']
    if hasattr(input, 'description'):
      self._description: str = input['description']
    self._scheme: ServerScheme = ServerScheme(input['scheme'])
    if hasattr(input, 'scheme_version'):
      self._scheme_version: str = input['scheme_version']
    if hasattr(input, 'variables'):
      self._variables: dict[str, ServerVariable] = input['variables']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def url(self) -> str:
    return self._url
  @url.setter
  def url(self, url: str):
    self._url = url

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

  @property
  def scheme(self) -> ServerScheme:
    return self._scheme
  @scheme.setter
  def scheme(self, scheme: ServerScheme):
    self._scheme = scheme

  @property
  def scheme_version(self) -> str:
    return self._scheme_version
  @scheme_version.setter
  def scheme_version(self, scheme_version: str):
    self._scheme_version = scheme_version

  @property
  def variables(self) -> dict[str, ServerVariable]:
    return self._variables
  @variables.setter
  def variables(self, variables: dict[str, ServerVariable]):
    self._variables = variables

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
    return Server(**json.loads(json_string))
