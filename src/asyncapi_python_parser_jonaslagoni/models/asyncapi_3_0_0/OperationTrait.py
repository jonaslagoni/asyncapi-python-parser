from __future__ import annotations
import json
from typing import Any, List, Dict
from . import Reference
from . import UserPassword
from . import ApiKey
from . import X509
from . import SymmetricEncryption
from . import AsymmetricEncryption
from . import BearerHttpSecurityScheme
from . import ApiKeyHttpSecurityScheme
from . import Oauth2Flows
from . import OpenIdConnect
from . import SaslPlainSecurityScheme
from . import SaslScramSecurityScheme
from . import SaslGssapiSecurityScheme
from . import Tag
from . import ExternalDocs
from . import OperationBindingsObject
class OperationTrait: 
  def __init__(self, input: Dict):
    if 'title' in input:
      self._title: str = input['title']
    if 'summary' in input:
      self._summary: str = input['summary']
    if 'description' in input:
      self._description: str = input['description']
    if 'security' in input:
      self._security: List[Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme | Oauth2Flows.Oauth2Flows | OpenIdConnect.OpenIdConnect | SaslPlainSecurityScheme.SaslPlainSecurityScheme | SaslScramSecurityScheme.SaslScramSecurityScheme | SaslGssapiSecurityScheme.SaslGssapiSecurityScheme] = input['security']
    if 'tags' in input:
      self._tags: List[Reference.Reference | Tag.Tag] = input['tags']
    if 'external_docs' in input:
      self._external_docs: Reference.Reference | ExternalDocs.ExternalDocs = input['external_docs']
    if 'bindings' in input:
      self._bindings: Reference.Reference | OperationBindingsObject.OperationBindingsObject = input['bindings']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

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
  def security(self) -> List[Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme | Oauth2Flows.Oauth2Flows | OpenIdConnect.OpenIdConnect | SaslPlainSecurityScheme.SaslPlainSecurityScheme | SaslScramSecurityScheme.SaslScramSecurityScheme | SaslGssapiSecurityScheme.SaslGssapiSecurityScheme]:
    return self._security
  @security.setter
  def security(self, security: List[Reference.Reference | UserPassword.UserPassword | ApiKey.ApiKey | X509.X509 | SymmetricEncryption.SymmetricEncryption | AsymmetricEncryption.AsymmetricEncryption | Any | BearerHttpSecurityScheme.BearerHttpSecurityScheme | ApiKeyHttpSecurityScheme.ApiKeyHttpSecurityScheme | Oauth2Flows.Oauth2Flows | OpenIdConnect.OpenIdConnect | SaslPlainSecurityScheme.SaslPlainSecurityScheme | SaslScramSecurityScheme.SaslScramSecurityScheme | SaslGssapiSecurityScheme.SaslGssapiSecurityScheme]):
    self._security = security

  @property
  def tags(self) -> List[Reference.Reference | Tag.Tag]:
    return self._tags
  @tags.setter
  def tags(self, tags: List[Reference.Reference | Tag.Tag]):
    self._tags = tags

  @property
  def external_docs(self) -> Reference.Reference | ExternalDocs.ExternalDocs:
    return self._external_docs
  @external_docs.setter
  def external_docs(self, external_docs: Reference.Reference | ExternalDocs.ExternalDocs):
    self._external_docs = external_docs

  @property
  def bindings(self) -> Reference.Reference | OperationBindingsObject.OperationBindingsObject:
    return self._bindings
  @bindings.setter
  def bindings(self, bindings: Reference.Reference | OperationBindingsObject.OperationBindingsObject):
    self._bindings = bindings

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
    return OperationTrait(**json.loads(json_string))
