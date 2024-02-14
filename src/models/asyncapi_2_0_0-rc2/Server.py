from .ServerVariable import ServerVariable
from .BindingsObject import BindingsObject
import json
from typing import List, Any, Dict
class Server: 
  def __init__(self, input: Dict):
    self._url: str = input['url']
    if hasattr(input, 'description'):
      self._description: str = input['description']
    self._protocol: str = input['protocol']
    if hasattr(input, 'protocol_version'):
      self._protocol_version: str = input['protocol_version']
    if hasattr(input, 'variables'):
      self._variables: dict[str, ServerVariable] = input['variables']
    if hasattr(input, 'security'):
      self._security: List[dict[str, List[str]]] = input['security']
    if hasattr(input, 'bindings'):
      self._bindings: BindingsObject = BindingsObject(input['bindings'])
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
  def variables(self) -> dict[str, ServerVariable]:
    return self._variables
  @variables.setter
  def variables(self, variables: dict[str, ServerVariable]):
    self._variables = variables

  @property
  def security(self) -> List[dict[str, List[str]]]:
    return self._security
  @security.setter
  def security(self, security: List[dict[str, List[str]]]):
    self._security = security

  @property
  def bindings(self) -> BindingsObject:
    return self._bindings
  @bindings.setter
  def bindings(self, bindings: BindingsObject):
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
