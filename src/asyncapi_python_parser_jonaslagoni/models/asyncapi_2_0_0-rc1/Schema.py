from __future__ import annotations
import json
from typing import Any, List, Dict
from . import JsonMinusSchemaMinusDraftMinus07MinusSchema
from . import Xml
from . import ExternalDocs
class Schema: 
  def __init__(self, input: Dict):
    if 'dollar_ref' in input:
      self._dollar_ref: str = input['dollar_ref']
    if 'format' in input:
      self._format: str = input['format']
    if 'title' in input:
      self._title: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['title'])
    if 'description' in input:
      self._description: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['description'])
    if 'default' in input:
      self._default: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['default'])
    if 'multiple_of' in input:
      self._multiple_of: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['multiple_of'])
    if 'maximum' in input:
      self._maximum: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['maximum'])
    if 'exclusive_maximum' in input:
      self._exclusive_maximum: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['exclusive_maximum'])
    if 'minimum' in input:
      self._minimum: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['minimum'])
    if 'exclusive_minimum' in input:
      self._exclusive_minimum: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['exclusive_minimum'])
    if 'max_length' in input:
      self._max_length: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['max_length'])
    if 'min_length' in input:
      self._min_length: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['min_length'])
    if 'pattern' in input:
      self._pattern: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['pattern'])
    if 'max_items' in input:
      self._max_items: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['max_items'])
    if 'min_items' in input:
      self._min_items: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['min_items'])
    if 'unique_items' in input:
      self._unique_items: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['unique_items'])
    if 'max_properties' in input:
      self._max_properties: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['max_properties'])
    if 'min_properties' in input:
      self._min_properties: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['min_properties'])
    if 'required' in input:
      self._required: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['required'])
    if 'enum' in input:
      self._enum: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['enum'])
    if 'deprecated' in input:
      self._deprecated: bool = input['deprecated']
    if 'additional_properties' in input:
      self._additional_properties: Schema | bool = input['additional_properties']
    if 'type' in input:
      self._type: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema(input['type'])
    if 'items' in input:
      self._items: Schema | List[Schema] = input['items']
    if 'all_of' in input:
      self._all_of: List[Schema] = input['all_of']
    if 'one_of' in input:
      self._one_of: List[Schema] = input['one_of']
    if 'any_of' in input:
      self._any_of: List[Schema] = input['any_of']
    if 'reserved_not' in input:
      self._reserved_not: Schema = Schema(input['reserved_not'])
    if 'properties' in input:
      self._properties: dict[str, Schema] = input['properties']
    if 'discriminator' in input:
      self._discriminator: str = input['discriminator']
    if 'read_only' in input:
      self._read_only: bool = input['read_only']
    if 'xml' in input:
      self._xml: Xml.Xml = Xml.Xml(input['xml'])
    if 'external_docs' in input:
      self._external_docs: ExternalDocs.ExternalDocs = ExternalDocs.ExternalDocs(input['external_docs'])
    if 'example' in input:
      self._example: Any = input['example']
    if 'examples' in input:
      self._examples: List[Any] = input['examples']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def dollar_ref(self) -> str:
    return self._dollar_ref
  @dollar_ref.setter
  def dollar_ref(self, dollar_ref: str):
    self._dollar_ref = dollar_ref

  @property
  def format(self) -> str:
    return self._format
  @format.setter
  def format(self, format: str):
    self._format = format

  @property
  def title(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._title
  @title.setter
  def title(self, title: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._title = title

  @property
  def description(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._description
  @description.setter
  def description(self, description: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._description = description

  @property
  def default(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._default
  @default.setter
  def default(self, default: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._default = default

  @property
  def multiple_of(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._multiple_of
  @multiple_of.setter
  def multiple_of(self, multiple_of: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._multiple_of = multiple_of

  @property
  def maximum(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._maximum
  @maximum.setter
  def maximum(self, maximum: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._maximum = maximum

  @property
  def exclusive_maximum(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._exclusive_maximum
  @exclusive_maximum.setter
  def exclusive_maximum(self, exclusive_maximum: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._exclusive_maximum = exclusive_maximum

  @property
  def minimum(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._minimum
  @minimum.setter
  def minimum(self, minimum: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._minimum = minimum

  @property
  def exclusive_minimum(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._exclusive_minimum
  @exclusive_minimum.setter
  def exclusive_minimum(self, exclusive_minimum: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._exclusive_minimum = exclusive_minimum

  @property
  def max_length(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._max_length
  @max_length.setter
  def max_length(self, max_length: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._max_length = max_length

  @property
  def min_length(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._min_length
  @min_length.setter
  def min_length(self, min_length: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._min_length = min_length

  @property
  def pattern(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._pattern
  @pattern.setter
  def pattern(self, pattern: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._pattern = pattern

  @property
  def max_items(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._max_items
  @max_items.setter
  def max_items(self, max_items: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._max_items = max_items

  @property
  def min_items(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._min_items
  @min_items.setter
  def min_items(self, min_items: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._min_items = min_items

  @property
  def unique_items(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._unique_items
  @unique_items.setter
  def unique_items(self, unique_items: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._unique_items = unique_items

  @property
  def max_properties(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._max_properties
  @max_properties.setter
  def max_properties(self, max_properties: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._max_properties = max_properties

  @property
  def min_properties(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._min_properties
  @min_properties.setter
  def min_properties(self, min_properties: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._min_properties = min_properties

  @property
  def required(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._required
  @required.setter
  def required(self, required: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._required = required

  @property
  def enum(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._enum
  @enum.setter
  def enum(self, enum: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._enum = enum

  @property
  def deprecated(self) -> bool:
    return self._deprecated
  @deprecated.setter
  def deprecated(self, deprecated: bool):
    self._deprecated = deprecated

  @property
  def additional_properties(self) -> Schema | bool:
    return self._additional_properties
  @additional_properties.setter
  def additional_properties(self, additional_properties: Schema | bool):
    self._additional_properties = additional_properties

  @property
  def type(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._type
  @type.setter
  def type(self, type: JsonMinusSchemaMinusDraftMinus07MinusSchema.JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._type = type

  @property
  def items(self) -> Schema | List[Schema]:
    return self._items
  @items.setter
  def items(self, items: Schema | List[Schema]):
    self._items = items

  @property
  def all_of(self) -> List[Schema]:
    return self._all_of
  @all_of.setter
  def all_of(self, all_of: List[Schema]):
    self._all_of = all_of

  @property
  def one_of(self) -> List[Schema]:
    return self._one_of
  @one_of.setter
  def one_of(self, one_of: List[Schema]):
    self._one_of = one_of

  @property
  def any_of(self) -> List[Schema]:
    return self._any_of
  @any_of.setter
  def any_of(self, any_of: List[Schema]):
    self._any_of = any_of

  @property
  def reserved_not(self) -> Schema:
    return self._reserved_not
  @reserved_not.setter
  def reserved_not(self, reserved_not: Schema):
    self._reserved_not = reserved_not

  @property
  def properties(self) -> dict[str, Schema]:
    return self._properties
  @properties.setter
  def properties(self, properties: dict[str, Schema]):
    self._properties = properties

  @property
  def discriminator(self) -> str:
    return self._discriminator
  @discriminator.setter
  def discriminator(self, discriminator: str):
    self._discriminator = discriminator

  @property
  def read_only(self) -> bool:
    return self._read_only
  @read_only.setter
  def read_only(self, read_only: bool):
    self._read_only = read_only

  @property
  def xml(self) -> Xml.Xml:
    return self._xml
  @xml.setter
  def xml(self, xml: Xml.Xml):
    self._xml = xml

  @property
  def external_docs(self) -> ExternalDocs.ExternalDocs:
    return self._external_docs
  @external_docs.setter
  def external_docs(self, external_docs: ExternalDocs.ExternalDocs):
    self._external_docs = external_docs

  @property
  def example(self) -> Any:
    return self._example
  @example.setter
  def example(self, example: Any):
    self._example = example

  @property
  def examples(self) -> List[Any]:
    return self._examples
  @examples.setter
  def examples(self, examples: List[Any]):
    self._examples = examples

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
    return Schema(**json.loads(json_string))
