from __future__ import annotations
import json
from typing import Any, List, Dict
from . import Contact
from . import License
from . import Reference
from . import Tag
from . import ExternalDocs
class Info: 
  def __init__(self, input: Dict):
    self._title: str = input['title']
    self._version: str = input['version']
    if 'description' in input:
      self._description: str = input['description']
    if 'terms_of_service' in input:
      self._terms_of_service: str = input['terms_of_service']
    if 'contact' in input:
      self._contact: Contact.Contact = Contact.Contact(input['contact'])
    if 'license' in input:
      self._license: License.License = License.License(input['license'])
    if 'tags' in input:
      self._tags: List[Reference.Reference | Tag.Tag] = input['tags']
    if 'external_docs' in input:
      self._external_docs: Reference.Reference | ExternalDocs.ExternalDocs = input['external_docs']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def title(self) -> str:
    return self._title
  @title.setter
  def title(self, title: str):
    self._title = title

  @property
  def version(self) -> str:
    return self._version
  @version.setter
  def version(self, version: str):
    self._version = version

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

  @property
  def terms_of_service(self) -> str:
    return self._terms_of_service
  @terms_of_service.setter
  def terms_of_service(self, terms_of_service: str):
    self._terms_of_service = terms_of_service

  @property
  def contact(self) -> Contact.Contact:
    return self._contact
  @contact.setter
  def contact(self, contact: Contact.Contact):
    self._contact = contact

  @property
  def license(self) -> License.License:
    return self._license
  @license.setter
  def license(self, license: License.License):
    self._license = license

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
  def additional_properties(self) -> dict[str, Any]:
    return self._additional_properties
  @additional_properties.setter
  def additional_properties(self, additional_properties: dict[str, Any]):
    self._additional_properties = additional_properties

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return Info(**json.loads(json_string))
