from .Contact import Contact
from .License import License
from .Reference import Reference
from .Tag import Tag
from .ExternalDocs import ExternalDocs
import json
from typing import Any, List, Dict
class Info: 
  def __init__(self, input: Dict):
    self._title: str = input['title']
    self._version: str = input['version']
    if hasattr(input, 'description'):
      self._description: str = input['description']
    if hasattr(input, 'terms_of_service'):
      self._terms_of_service: str = input['terms_of_service']
    if hasattr(input, 'contact'):
      self._contact: Contact = Contact(input['contact'])
    if hasattr(input, 'license'):
      self._license: License = License(input['license'])
    if hasattr(input, 'tags'):
      self._tags: List[Reference | Tag] = input['tags']
    if hasattr(input, 'external_docs'):
      self._external_docs: Reference | ExternalDocs = input['external_docs']
    if hasattr(input, 'additional_properties'):
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
  def contact(self) -> Contact:
    return self._contact
  @contact.setter
  def contact(self, contact: Contact):
    self._contact = contact

  @property
  def license(self) -> License:
    return self._license
  @license.setter
  def license(self, license: License):
    self._license = license

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
