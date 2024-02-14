from .Schema import Schema
from .Tag import Tag
from .ExternalDocs import ExternalDocs
import json
from typing import Any, List, Dict
class Message: 
  def __init__(self, input: Dict):
    if hasattr(input, 'dollar_ref'):
      self._dollar_ref: str = input['dollar_ref']
    if hasattr(input, 'headers'):
      self._headers: Schema = Schema(input['headers'])
    if hasattr(input, 'payload'):
      self._payload: Schema = Schema(input['payload'])
    if hasattr(input, 'tags'):
      self._tags: List[Tag] = input['tags']
    if hasattr(input, 'summary'):
      self._summary: str = input['summary']
    if hasattr(input, 'description'):
      self._description: str = input['description']
    if hasattr(input, 'external_docs'):
      self._external_docs: ExternalDocs = ExternalDocs(input['external_docs'])
    if hasattr(input, 'deprecated'):
      self._deprecated: bool = input['deprecated']
    if hasattr(input, 'example'):
      self._example: Any = input['example']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def dollar_ref(self) -> str:
    return self._dollar_ref
  @dollar_ref.setter
  def dollar_ref(self, dollar_ref: str):
    self._dollar_ref = dollar_ref

  @property
  def headers(self) -> Schema:
    return self._headers
  @headers.setter
  def headers(self, headers: Schema):
    self._headers = headers

  @property
  def payload(self) -> Schema:
    return self._payload
  @payload.setter
  def payload(self, payload: Schema):
    self._payload = payload

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
  def example(self) -> Any:
    return self._example
  @example.setter
  def example(self, example: Any):
    self._example = example

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
    return Message(**json.loads(json_string))
