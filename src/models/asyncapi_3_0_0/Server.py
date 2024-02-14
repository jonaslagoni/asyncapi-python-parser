from .Reference import Reference
from .ServerVariable import ServerVariable
from .UserPassword import UserPassword
from .ApiKey import ApiKey
from .X509 import X509
from .SymmetricEncryption import SymmetricEncryption
from .AsymmetricEncryption import AsymmetricEncryption
from .BearerHttpSecurityScheme import BearerHttpSecurityScheme
from .ApiKeyHttpSecurityScheme import ApiKeyHttpSecurityScheme
from .Oauth2Flows import Oauth2Flows
from .OpenIdConnect import OpenIdConnect
from .SaslPlainSecurityScheme import SaslPlainSecurityScheme
from .SaslScramSecurityScheme import SaslScramSecurityScheme
from .SaslGssapiSecurityScheme import SaslGssapiSecurityScheme
from .Tag import Tag
from .ExternalDocs import ExternalDocs
from .ServerBindingsObject import ServerBindingsObject
import json
from typing import Any, List, Dict
class Server: 
  def __init__(self, input: Dict):
    self._host: str = input['host']
    if hasattr(input, 'pathname'):
      self._pathname: str = input['pathname']
    if hasattr(input, 'title'):
      self._title: str = input['title']
    if hasattr(input, 'summary'):
      self._summary: str = input['summary']
    if hasattr(input, 'description'):
      self._description: str = input['description']
    self._protocol: str = input['protocol']
    if hasattr(input, 'protocol_version'):
      self._protocol_version: str = input['protocol_version']
    if hasattr(input, 'variables'):
      self._variables: dict[str, Reference | ServerVariable] = input['variables']
    if hasattr(input, 'security'):
      self._security: List[Reference | UserPassword | ApiKey | X509 | SymmetricEncryption | AsymmetricEncryption | Any | BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme | Oauth2Flows | OpenIdConnect | SaslPlainSecurityScheme | SaslScramSecurityScheme | SaslGssapiSecurityScheme] = input['security']
    if hasattr(input, 'tags'):
      self._tags: List[Reference | Tag] = input['tags']
    if hasattr(input, 'external_docs'):
      self._external_docs: Reference | ExternalDocs = input['external_docs']
    if hasattr(input, 'bindings'):
      self._bindings: Reference | ServerBindingsObject = input['bindings']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def host(self) -> str:
    return self._host
  @host.setter
  def host(self, host: str):
    self._host = host

  @property
  def pathname(self) -> str:
    return self._pathname
  @pathname.setter
  def pathname(self, pathname: str):
    self._pathname = pathname

  @property
  def title(self) -> str:
    return self._title
  @title.setter
  def title(self, title: str):
    self._title = title

  @property
  def summary(self) -> str:
    return self._summary
  @summary.setter
  def summary(self, summary: str):
    self._summary = summary

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
  def variables(self) -> dict[str, Reference | ServerVariable]:
    return self._variables
  @variables.setter
  def variables(self, variables: dict[str, Reference | ServerVariable]):
    self._variables = variables

  @property
  def security(self) -> List[Reference | UserPassword | ApiKey | X509 | SymmetricEncryption | AsymmetricEncryption | Any | BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme | Oauth2Flows | OpenIdConnect | SaslPlainSecurityScheme | SaslScramSecurityScheme | SaslGssapiSecurityScheme]:
    return self._security
  @security.setter
  def security(self, security: List[Reference | UserPassword | ApiKey | X509 | SymmetricEncryption | AsymmetricEncryption | Any | BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme | Oauth2Flows | OpenIdConnect | SaslPlainSecurityScheme | SaslScramSecurityScheme | SaslGssapiSecurityScheme]):
    self._security = security

  @property
  def tags(self) -> List[Reference | Tag]:
    return self._tags
  @tags.setter
  def tags(self, tags: List[Reference | Tag]):
    self._tags = tags

  @property
  def external_docs(self) -> Reference | ExternalDocs:
    return self._external_docs
  @external_docs.setter
  def external_docs(self, external_docs: Reference | ExternalDocs):
    self._external_docs = external_docs

  @property
  def bindings(self) -> Reference | ServerBindingsObject:
    return self._bindings
  @bindings.setter
  def bindings(self, bindings: Reference | ServerBindingsObject):
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
