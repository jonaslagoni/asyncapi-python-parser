from __future__ import annotations
import json
from typing import Any, List, Dict
from . import Reference
from . import MessageObject
from . import Parameter
from . import Tag
from . import ExternalDocs
from . import ChannelBindingsObject
class Channel: 
  def __init__(self, input: Dict):
    if 'address' in input:
      self._address: str = input['address']
    if 'messages' in input:
      self._messages: dict[str, Reference.Reference | MessageObject.MessageObject] = input['messages']
    if 'parameters' in input:
      self._parameters: dict[str, Reference.Reference | Parameter.Parameter] = input['parameters']
    if 'title' in input:
      self._title: str = input['title']
    if 'summary' in input:
      self._summary: str = input['summary']
    if 'description' in input:
      self._description: str = input['description']
    if 'servers' in input:
      self._servers: List[Reference.Reference] = input['servers']
    if 'tags' in input:
      self._tags: List[Reference.Reference | Tag.Tag] = input['tags']
    if 'external_docs' in input:
      self._external_docs: Reference.Reference | ExternalDocs.ExternalDocs = input['external_docs']
    if 'bindings' in input:
      self._bindings: Reference.Reference | ChannelBindingsObject.ChannelBindingsObject = input['bindings']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def address(self) -> str:
    return self._address
  @address.setter
  def address(self, address: str):
    self._address = address

  @property
  def messages(self) -> dict[str, Reference.Reference | MessageObject.MessageObject]:
    return self._messages
  @messages.setter
  def messages(self, messages: dict[str, Reference.Reference | MessageObject.MessageObject]):
    self._messages = messages

  @property
  def parameters(self) -> dict[str, Reference.Reference | Parameter.Parameter]:
    return self._parameters
  @parameters.setter
  def parameters(self, parameters: dict[str, Reference.Reference | Parameter.Parameter]):
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
  def servers(self) -> List[Reference.Reference]:
    return self._servers
  @servers.setter
  def servers(self, servers: List[Reference.Reference]):
    self._servers = servers

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
  def bindings(self) -> Reference.Reference | ChannelBindingsObject.ChannelBindingsObject:
    return self._bindings
  @bindings.setter
  def bindings(self, bindings: Reference.Reference | ChannelBindingsObject.ChannelBindingsObject):
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
    return Channel(**json.loads(json_string))
