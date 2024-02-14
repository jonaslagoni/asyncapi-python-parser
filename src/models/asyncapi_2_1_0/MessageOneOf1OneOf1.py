from .MessageOneOf1OneOf1HeadersObject import MessageOneOf1OneOf1HeadersObject
from .MessageOneOf1OneOf1PayloadObject import MessageOneOf1OneOf1PayloadObject
from .Reference import Reference
from .CorrelationId import CorrelationId
from .Tag import Tag
from .ExternalDocs import ExternalDocs
from .BindingsObject import BindingsObject
from .MessageTrait import MessageTrait
import json
from typing import Any, List, Dict
class MessageOneOf1OneOf1: 
  def __init__(self, input: Dict):
    if hasattr(input, 'schema_format'):
      self._schema_format: str = input['schema_format']
    if hasattr(input, 'content_type'):
      self._content_type: str = input['content_type']
    if hasattr(input, 'headers'):
      self._headers: MessageOneOf1OneOf1HeadersObject | bool = input['headers']
    if hasattr(input, 'payload'):
      self._payload: MessageOneOf1OneOf1PayloadObject | bool = input['payload']
    if hasattr(input, 'correlation_id'):
      self._correlation_id: Reference | CorrelationId = input['correlation_id']
    if hasattr(input, 'tags'):
      self._tags: List[Tag] = input['tags']
    if hasattr(input, 'summary'):
      self._summary: str = input['summary']
    if hasattr(input, 'name'):
      self._name: str = input['name']
    if hasattr(input, 'title'):
      self._title: str = input['title']
    if hasattr(input, 'description'):
      self._description: str = input['description']
    if hasattr(input, 'external_docs'):
      self._external_docs: ExternalDocs = ExternalDocs(input['external_docs'])
    if hasattr(input, 'deprecated'):
      self._deprecated: bool = input['deprecated']
    if hasattr(input, 'examples'):
      self._examples: List[Any | Any] = input['examples']
    if hasattr(input, 'bindings'):
      self._bindings: BindingsObject = BindingsObject(input['bindings'])
    if hasattr(input, 'traits'):
      self._traits: List[Reference | MessageTrait] = input['traits']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

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
  def headers(self) -> MessageOneOf1OneOf1HeadersObject | bool:
    return self._headers
  @headers.setter
  def headers(self, headers: MessageOneOf1OneOf1HeadersObject | bool):
    self._headers = headers

  @property
  def payload(self) -> MessageOneOf1OneOf1PayloadObject | bool:
    return self._payload
  @payload.setter
  def payload(self, payload: MessageOneOf1OneOf1PayloadObject | bool):
    self._payload = payload

  @property
  def correlation_id(self) -> Reference | CorrelationId:
    return self._correlation_id
  @correlation_id.setter
  def correlation_id(self, correlation_id: Reference | CorrelationId):
    self._correlation_id = correlation_id

  @property
  def tags(self) -> List[Tag]:
    return self._tags
  @tags.setter
  def tags(self, tags: List[Tag]):
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
  def external_docs(self) -> ExternalDocs:
    return self._external_docs
  @external_docs.setter
  def external_docs(self, external_docs: ExternalDocs):
    self._external_docs = external_docs

  @property
  def deprecated(self) -> bool:
    return self._deprecated
  @deprecated.setter
  def deprecated(self, deprecated: bool):
    self._deprecated = deprecated

  @property
  def examples(self) -> List[Any | Any]:
    return self._examples
  @examples.setter
  def examples(self, examples: List[Any | Any]):
    self._examples = examples

  @property
  def bindings(self) -> BindingsObject:
    return self._bindings
  @bindings.setter
  def bindings(self, bindings: BindingsObject):
    self._bindings = bindings

  @property
  def traits(self) -> List[Reference | MessageTrait]:
    return self._traits
  @traits.setter
  def traits(self, traits: List[Reference | MessageTrait]):
    self._traits = traits

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
    return MessageOneOf1OneOf1(**json.loads(json_string))
