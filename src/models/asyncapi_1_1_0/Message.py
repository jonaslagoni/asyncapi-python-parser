from __future__ import annotations
import json
from typing import Any, List, Dict
from . import Schema
from . import Tag
from . import ExternalDocs
class Message: 
  def __init__(self, input: Dict):
    if 'dollar_ref' in input:
      self._dollar_ref: str = input['dollar_ref']
    if 'headers' in input:
      self._headers: Schema.Schema = Schema.Schema(input['headers'])
    if 'payload' in input:
      self._payload: Schema.Schema = Schema.Schema(input['payload'])
    if 'tags' in input:
      self._tags: List[Tag.Tag] = input['tags']
    if 'summary' in input:
      self._summary: str = input['summary']
    if 'description' in input:
      self._description: str = input['description']
    if 'external_docs' in input:
      self._external_docs: ExternalDocs.ExternalDocs = ExternalDocs.ExternalDocs(input['external_docs'])
    if 'deprecated' in input:
      self._deprecated: bool = input['deprecated']
    if 'example' in input:
      self._example: Any = input['example']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def dollar_ref(self) -> str:
    return self._dollar_ref
  @dollar_ref.setter
  def dollar_ref(self, dollar_ref: str):
    self._dollar_ref = dollar_ref

  @property
  def headers(self) -> Schema.Schema:
    return self._headers
  @headers.setter
  def headers(self, headers: Schema.Schema):
    self._headers = headers

  @property
  def payload(self) -> Schema.Schema:
    return self._payload
  @payload.setter
  def payload(self, payload: Schema.Schema):
    self._payload = payload

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
