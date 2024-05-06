from __future__ import annotations
import json
from typing import List, Any, Dict
from . import ServerScheme
from . import ServerVariable
class Server: 
  def __init__(self, input: Dict):
    self._url: str = input['url']
    if 'description' in input:
      self._description: str = input['description']
    self._scheme: ServerScheme.ServerScheme = ServerScheme.ServerScheme(input['scheme'])
    if 'scheme_version' in input:
      self._scheme_version: str = input['scheme_version']
    if 'variables' in input:
      self._variables: dict[str, ServerVariable.ServerVariable] = input['variables']
    if 'additional_properties' in input:
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
  def scheme(self) -> ServerScheme.ServerScheme:
    return self._scheme
  @scheme.setter
  def scheme(self, scheme: ServerScheme.ServerScheme):
    self._scheme = scheme

  @property
  def scheme_version(self) -> str:
    return self._scheme_version
  @scheme_version.setter
  def scheme_version(self, scheme_version: str):
    self._scheme_version = scheme_version

  @property
  def variables(self) -> dict[str, ServerVariable.ServerVariable]:
    return self._variables
  @variables.setter
  def variables(self, variables: dict[str, ServerVariable.ServerVariable]):
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
