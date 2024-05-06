from __future__ import annotations
import json
from typing import Any, List, Dict
from . import MessageOneOf1OneOf1HeadersObject
from . import MessageOneOf1OneOf1PayloadObject
from . import Reference
from . import CorrelationId
from . import Tag
from . import ExternalDocs
from . import MessageOneOf1OneOf1ExamplesItem
from . import BindingsObject
from . import MessageTrait
class MessageOneOf1OneOf1: 
  def __init__(self, input: Dict):
    if 'schema_format' in input:
      self._schema_format: str = input['schema_format']
    if 'content_type' in input:
      self._content_type: str = input['content_type']
    if 'headers' in input:
      self._headers: MessageOneOf1OneOf1HeadersObject.MessageOneOf1OneOf1HeadersObject | bool = input['headers']
    if 'payload' in input:
      self._payload: MessageOneOf1OneOf1PayloadObject.MessageOneOf1OneOf1PayloadObject | bool = input['payload']
    if 'correlation_id' in input:
      self._correlation_id: Reference.Reference | CorrelationId.CorrelationId = input['correlation_id']
    if 'tags' in input:
      self._tags: List[Tag.Tag] = input['tags']
    if 'summary' in input:
      self._summary: str = input['summary']
    if 'name' in input:
      self._name: str = input['name']
    if 'title' in input:
      self._title: str = input['title']
    if 'description' in input:
      self._description: str = input['description']
    if 'external_docs' in input:
      self._external_docs: ExternalDocs.ExternalDocs = ExternalDocs.ExternalDocs(input['external_docs'])
    if 'deprecated' in input:
      self._deprecated: bool = input['deprecated']
    if 'examples' in input:
      self._examples: List[MessageOneOf1OneOf1ExamplesItem.MessageOneOf1OneOf1ExamplesItem] = input['examples']
    if 'bindings' in input:
      self._bindings: BindingsObject.BindingsObject = BindingsObject.BindingsObject(input['bindings'])
    if 'traits' in input:
      self._traits: List[Reference.Reference | MessageTrait.MessageTrait] = input['traits']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def schema_format(self) -> str:
    return self._schema_format
  @schema_format.setter
  def schema_format(self, schema_format: str):
    self._schema_format = schema_format

  @property
  def content_type(self) -> str:
    return self._content_type
  @content_type.setter
  def content_type(self, content_type: str):
    self._content_type = content_type

  @property
  def headers(self) -> MessageOneOf1OneOf1HeadersObject.MessageOneOf1OneOf1HeadersObject | bool:
    return self._headers
  @headers.setter
  def headers(self, headers: MessageOneOf1OneOf1HeadersObject.MessageOneOf1OneOf1HeadersObject | bool):
    self._headers = headers

  @property
  def payload(self) -> MessageOneOf1OneOf1PayloadObject.MessageOneOf1OneOf1PayloadObject | bool:
    return self._payload
  @payload.setter
  def payload(self, payload: MessageOneOf1OneOf1PayloadObject.MessageOneOf1OneOf1PayloadObject | bool):
    self._payload = payload

  @property
  def correlation_id(self) -> Reference.Reference | CorrelationId.CorrelationId:
    return self._correlation_id
  @correlation_id.setter
  def correlation_id(self, correlation_id: Reference.Reference | CorrelationId.CorrelationId):
    self._correlation_id = correlation_id

  @property
  def tags(self) -> List[Tag.Tag]:
    return self._tags
  @tags.setter
  def tags(self, tags: List[Tag.Tag]):
    self._tags = tags

  @property
  def summary(self) -> str:
    return self._summary
  @summary.setter
  def summary(self, summary: str):
    self._summary = summary

  @property
  def name(self) -> str:
    return self._name
  @name.setter
  def name(self, name: str):
    self._name = name

  @property
  def title(self) -> str:
    return self._title
  @title.setter
  def title(self, title: str):
    self._title = title

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

  @property
  def external_docs(self) -> ExternalDocs.ExternalDocs:
    return self._external_docs
  @external_docs.setter
  def external_docs(self, external_docs: ExternalDocs.ExternalDocs):
    self._external_docs = external_docs

  @property
  def deprecated(self) -> bool:
    return self._deprecated
  @deprecated.setter
  def deprecated(self, deprecated: bool):
    self._deprecated = deprecated

  @property
  def examples(self) -> List[MessageOneOf1OneOf1ExamplesItem.MessageOneOf1OneOf1ExamplesItem]:
    return self._examples
  @examples.setter
  def examples(self, examples: List[MessageOneOf1OneOf1ExamplesItem.MessageOneOf1OneOf1ExamplesItem]):
    self._examples = examples

  @property
  def bindings(self) -> BindingsObject.BindingsObject:
    return self._bindings
  @bindings.setter
  def bindings(self, bindings: BindingsObject.BindingsObject):
    self._bindings = bindings

  @property
  def traits(self) -> List[Reference.Reference | MessageTrait.MessageTrait]:
    return self._traits
  @traits.setter
  def traits(self, traits: List[Reference.Reference | MessageTrait.MessageTrait]):
    self._traits = traits

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
    return MessageOneOf1OneOf1(**json.loads(json_string))
