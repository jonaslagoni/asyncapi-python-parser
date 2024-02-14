from .Reference import Reference
from .MessageObject import MessageObject
from .Parameter import Parameter
from .Tag import Tag
from .ExternalDocs import ExternalDocs
from .ChannelBindingsObject import ChannelBindingsObject
import json
from typing import Any, List, Dict
class Channel: 
  def __init__(self, input: Dict):
    if hasattr(input, 'address'):
      self._address: str = input['address']
    if hasattr(input, 'messages'):
      self._messages: dict[str, Reference | MessageObject] = input['messages']
    if hasattr(input, 'parameters'):
      self._parameters: dict[str, Reference | Parameter] = input['parameters']
    if hasattr(input, 'title'):
      self._title: str = input['title']
    if hasattr(input, 'summary'):
      self._summary: str = input['summary']
    if hasattr(input, 'description'):
      self._description: str = input['description']
    if hasattr(input, 'servers'):
      self._servers: List[Reference] = input['servers']
    if hasattr(input, 'tags'):
      self._tags: List[Reference | Tag] = input['tags']
    if hasattr(input, 'external_docs'):
      self._external_docs: Reference | ExternalDocs = input['external_docs']
    if hasattr(input, 'bindings'):
      self._bindings: Reference | ChannelBindingsObject = input['bindings']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def address(self) -> str:
    return self._address
  @address.setter
  def address(self, address: str):
    self._address = address

  @property
  def messages(self) -> dict[str, Reference | MessageObject]:
    return self._messages
  @messages.setter
  def messages(self, messages: dict[str, Reference | MessageObject]):
    self._messages = messages

  @property
  def parameters(self) -> dict[str, Reference | Parameter]:
    return self._parameters
  @parameters.setter
  def parameters(self, parameters: dict[str, Reference | Parameter]):
    self._parameters = parameters

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
  def servers(self) -> List[Reference]:
    return self._servers
  @servers.setter
  def servers(self, servers: List[Reference]):
    self._servers = servers

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
  def bindings(self) -> Reference | ChannelBindingsObject:
    return self._bindings
  @bindings.setter
  def bindings(self, bindings: Reference | ChannelBindingsObject):
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
    return Channel(**json.loads(json_string))
