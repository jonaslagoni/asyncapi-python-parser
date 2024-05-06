from __future__ import annotations
import json
from typing import List, Any, Dict
from . import ServerVariable
from . import BindingsObject
class Server: 
  def __init__(self, input: Dict):
    self._url: str = input['url']
    if 'description' in input:
      self._description: str = input['description']
    self._protocol: str = input['protocol']
    if 'protocol_version' in input:
      self._protocol_version: str = input['protocol_version']
    if 'variables' in input:
      self._variables: dict[str, ServerVariable.ServerVariable] = input['variables']
    if 'security' in input:
      self._security: List[dict[str, List[str]]] = input['security']
    if 'bindings' in input:
      self._bindings: BindingsObject.BindingsObject = BindingsObject.BindingsObject(input['bindings'])
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
  def protocol(self) -> str:
    return self._protocol
  @protocol.setter
  def protocol(self, protocol: str):
    self._protocol = protocol

  @property
  def protocol_version(self) -> str:
    return self._protocol_version
  @protocol_version.setter
  def protocol_version(self, protocol_version: str):
    self._protocol_version = protocol_version

  @property
  def variables(self) -> dict[str, ServerVariable.ServerVariable]:
    return self._variables
  @variables.setter
  def variables(self, variables: dict[str, ServerVariable.ServerVariable]):
    self._variables = variables

  @property
  def security(self) -> List[dict[str, List[str]]]:
    return self._security
  @security.setter
  def security(self, security: List[dict[str, List[str]]]):
    self._security = security

  @property
  def bindings(self) -> BindingsObject.BindingsObject:
    return self._bindings
  @bindings.setter
  def bindings(self, bindings: BindingsObject.BindingsObject):
    self._bindings = bindings

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
