from .CoreSchemaMetaMinusSchemaObject import CoreSchemaMetaMinusSchemaObject
from .JsonMinusSchemaMinusDraftMinus07MinusSchemaType import JsonMinusSchemaMinusDraftMinus07MinusSchemaType
from .SchemaAllOf1DiscriminatorObject import SchemaAllOf1DiscriminatorObject
from .ExternalDocs import ExternalDocs
from .OpenapiSchema30Xml import OpenapiSchema30Xml
import json
from typing import Any, List, Dict
class MessageOneOf1OneOf1PayloadObject: 
  def __init__(self, input: Dict):
    if hasattr(input, 'dollar_id'):
      self._dollar_id: str = input['dollar_id']
    if hasattr(input, 'dollar_schema'):
      self._dollar_schema: str = input['dollar_schema']
    if hasattr(input, 'dollar_ref'):
      self._dollar_ref: str = input['dollar_ref']
    if hasattr(input, 'dollar_comment'):
      self._dollar_comment: str = input['dollar_comment']
    if hasattr(input, 'title'):
      self._title: str = input['title']
    if hasattr(input, 'description'):
      self._description: str = input['description']
    if hasattr(input, 'default'):
      self._default: Any = input['default']
    if hasattr(input, 'read_only'):
      self._read_only: bool = input['read_only']
    if hasattr(input, 'write_only'):
      self._write_only: bool = input['write_only']
    if hasattr(input, 'examples'):
      self._examples: List[Any] = input['examples']
    if hasattr(input, 'multiple_of'):
      self._multiple_of: float = input['multiple_of']
    if hasattr(input, 'maximum'):
      self._maximum: float = input['maximum']
    if hasattr(input, 'exclusive_maximum'):
      self._exclusive_maximum: float | bool = input['exclusive_maximum']
    if hasattr(input, 'minimum'):
      self._minimum: float = input['minimum']
    if hasattr(input, 'exclusive_minimum'):
      self._exclusive_minimum: float | bool = input['exclusive_minimum']
    if hasattr(input, 'max_length'):
      self._max_length: int = input['max_length']
    if hasattr(input, 'min_length'):
      self._min_length: int = input['min_length']
    if hasattr(input, 'pattern'):
      self._pattern: str = input['pattern']
    if hasattr(input, 'additional_items'):
      self._additional_items: MessageOneOf1OneOf1PayloadObject | bool = input['additional_items']
    if hasattr(input, 'items'):
      self._items: CoreSchemaMetaMinusSchemaObject | bool | List[MessageOneOf1OneOf1PayloadObject | bool] = input['items']
    if hasattr(input, 'max_items'):
      self._max_items: int = input['max_items']
    if hasattr(input, 'min_items'):
      self._min_items: int = input['min_items']
    if hasattr(input, 'unique_items'):
      self._unique_items: bool = input['unique_items']
    if hasattr(input, 'contains'):
      self._contains: MessageOneOf1OneOf1PayloadObject | bool = input['contains']
    if hasattr(input, 'max_properties'):
      self._max_properties: int = input['max_properties']
    if hasattr(input, 'min_properties'):
      self._min_properties: int = input['min_properties']
    if hasattr(input, 'required'):
      self._required: List[str] = input['required']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: MessageOneOf1OneOf1PayloadObject | bool = input['additional_properties']
    if hasattr(input, 'definitions'):
      self._definitions: dict[str, MessageOneOf1OneOf1PayloadObject | bool] = input['definitions']
    if hasattr(input, 'properties'):
      self._properties: dict[str, MessageOneOf1OneOf1PayloadObject | bool] = input['properties']
    if hasattr(input, 'pattern_properties'):
      self._pattern_properties: dict[str, MessageOneOf1OneOf1PayloadObject | bool] = input['pattern_properties']
    if hasattr(input, 'dependencies'):
      self._dependencies: dict[str,  | List[str]] = input['dependencies']
    if hasattr(input, 'property_names'):
      self._property_names: MessageOneOf1OneOf1PayloadObject | bool = input['property_names']
    if hasattr(input, 'const'):
      self._const: Any = input['const']
    if hasattr(input, 'enum'):
      self._enum: List[Any] = input['enum']
    self._type: JsonMinusSchemaMinusDraftMinus07MinusSchemaType = JsonMinusSchemaMinusDraftMinus07MinusSchemaType.OBJECT
    if hasattr(input, 'format'):
      self._format: str = input['format']
    if hasattr(input, 'content_media_type'):
      self._content_media_type: str = input['content_media_type']
    if hasattr(input, 'content_encoding'):
      self._content_encoding: str = input['content_encoding']
    if hasattr(input, 'reserved_if'):
      self._reserved_if: MessageOneOf1OneOf1PayloadObject | bool = input['reserved_if']
    if hasattr(input, 'then'):
      self._then: MessageOneOf1OneOf1PayloadObject | bool = input['then']
    if hasattr(input, 'reserved_else'):
      self._reserved_else: MessageOneOf1OneOf1PayloadObject | bool = input['reserved_else']
    if hasattr(input, 'all_of'):
      self._all_of: List[MessageOneOf1OneOf1PayloadObject | bool] = input['all_of']
    if hasattr(input, 'any_of'):
      self._any_of: List[MessageOneOf1OneOf1PayloadObject | bool] = input['any_of']
    if hasattr(input, 'one_of'):
      self._one_of: List[MessageOneOf1OneOf1PayloadObject | bool] = input['one_of']
    if hasattr(input, 'reserved_not'):
      self._reserved_not: MessageOneOf1OneOf1PayloadObject | bool = input['reserved_not']
    if hasattr(input, 'discriminator'):
      self._discriminator: SchemaAllOf1DiscriminatorObject | str = input['discriminator']
    if hasattr(input, 'external_docs'):
      self._external_docs: ExternalDocs = ExternalDocs(input['external_docs'])
    if hasattr(input, 'deprecated'):
      self._deprecated: bool = input['deprecated']
    if hasattr(input, 'nullable'):
      self._nullable: bool = input['nullable']
    if hasattr(input, 'example'):
      self._example: Any = input['example']
    if hasattr(input, 'xml'):
      self._xml: OpenapiSchema30Xml = OpenapiSchema30Xml(input['xml'])
    if hasattr(input, 'reserved_additional_properties'):
      self._reserved_additional_properties: dict[str, Any | Any] = input['reserved_additional_properties']

  @property
  def dollar_id(self) -> str:
    return self._dollar_id
  @dollar_id.setter
  def dollar_id(self, dollar_id: str):
    self._dollar_id = dollar_id

  @property
  def dollar_schema(self) -> str:
    return self._dollar_schema
  @dollar_schema.setter
  def dollar_schema(self, dollar_schema: str):
    self._dollar_schema = dollar_schema

  @property
  def dollar_ref(self) -> str:
    return self._dollar_ref
  @dollar_ref.setter
  def dollar_ref(self, dollar_ref: str):
    self._dollar_ref = dollar_ref

  @property
  def dollar_comment(self) -> str:
    return self._dollar_comment
  @dollar_comment.setter
  def dollar_comment(self, dollar_comment: str):
    self._dollar_comment = dollar_comment

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
  def default(self) -> Any:
    return self._default
  @default.setter
  def default(self, default: Any):
    self._default = default

  @property
  def read_only(self) -> bool:
    return self._read_only
  @read_only.setter
  def read_only(self, read_only: bool):
    self._read_only = read_only

  @property
  def write_only(self) -> bool:
    return self._write_only
  @write_only.setter
  def write_only(self, write_only: bool):
    self._write_only = write_only

  @property
  def examples(self) -> List[Any]:
    return self._examples
  @examples.setter
  def examples(self, examples: List[Any]):
    self._examples = examples

  @property
  def multiple_of(self) -> float:
    return self._multiple_of
  @multiple_of.setter
  def multiple_of(self, multiple_of: float):
    self._multiple_of = multiple_of

  @property
  def maximum(self) -> float:
    return self._maximum
  @maximum.setter
  def maximum(self, maximum: float):
    self._maximum = maximum

  @property
  def exclusive_maximum(self) -> float | bool:
    return self._exclusive_maximum
  @exclusive_maximum.setter
  def exclusive_maximum(self, exclusive_maximum: float | bool):
    self._exclusive_maximum = exclusive_maximum

  @property
  def minimum(self) -> float:
    return self._minimum
  @minimum.setter
  def minimum(self, minimum: float):
    self._minimum = minimum

  @property
  def exclusive_minimum(self) -> float | bool:
    return self._exclusive_minimum
  @exclusive_minimum.setter
  def exclusive_minimum(self, exclusive_minimum: float | bool):
    self._exclusive_minimum = exclusive_minimum

  @property
  def max_length(self) -> int:
    return self._max_length
  @max_length.setter
  def max_length(self, max_length: int):
    self._max_length = max_length

  @property
  def min_length(self) -> int:
    return self._min_length
  @min_length.setter
  def min_length(self, min_length: int):
    self._min_length = min_length

  @property
  def pattern(self) -> str:
    return self._pattern
  @pattern.setter
  def pattern(self, pattern: str):
    self._pattern = pattern

  @property
  def additional_items(self) -> MessageOneOf1OneOf1PayloadObject | bool:
    return self._additional_items
  @additional_items.setter
  def additional_items(self, additional_items: MessageOneOf1OneOf1PayloadObject | bool):
    self._additional_items = additional_items

  @property
  def items(self) -> CoreSchemaMetaMinusSchemaObject | bool | List[MessageOneOf1OneOf1PayloadObject | bool]:
    return self._items
  @items.setter
  def items(self, items: CoreSchemaMetaMinusSchemaObject | bool | List[MessageOneOf1OneOf1PayloadObject | bool]):
    self._items = items

  @property
  def max_items(self) -> int:
    return self._max_items
  @max_items.setter
  def max_items(self, max_items: int):
    self._max_items = max_items

  @property
  def min_items(self) -> int:
    return self._min_items
  @min_items.setter
  def min_items(self, min_items: int):
    self._min_items = min_items

  @property
  def unique_items(self) -> bool:
    return self._unique_items
  @unique_items.setter
  def unique_items(self, unique_items: bool):
    self._unique_items = unique_items

  @property
  def contains(self) -> MessageOneOf1OneOf1PayloadObject | bool:
    return self._contains
  @contains.setter
  def contains(self, contains: MessageOneOf1OneOf1PayloadObject | bool):
    self._contains = contains

  @property
  def max_properties(self) -> int:
    return self._max_properties
  @max_properties.setter
  def max_properties(self, max_properties: int):
    self._max_properties = max_properties

  @property
  def min_properties(self) -> int:
    return self._min_properties
  @min_properties.setter
  def min_properties(self, min_properties: int):
    self._min_properties = min_properties

  @property
  def required(self) -> List[str]:
    return self._required
  @required.setter
  def required(self, required: List[str]):
    self._required = required

  @property
  def additional_properties(self) -> MessageOneOf1OneOf1PayloadObject | bool:
    return self._additional_properties
  @additional_properties.setter
  def additional_properties(self, additional_properties: MessageOneOf1OneOf1PayloadObject | bool):
    self._additional_properties = additional_properties

  @property
  def definitions(self) -> dict[str, MessageOneOf1OneOf1PayloadObject | bool]:
    return self._definitions
  @definitions.setter
  def definitions(self, definitions: dict[str, MessageOneOf1OneOf1PayloadObject | bool]):
    self._definitions = definitions

  @property
  def properties(self) -> dict[str, MessageOneOf1OneOf1PayloadObject | bool]:
    return self._properties
  @properties.setter
  def properties(self, properties: dict[str, MessageOneOf1OneOf1PayloadObject | bool]):
    self._properties = properties

  @property
  def pattern_properties(self) -> dict[str, MessageOneOf1OneOf1PayloadObject | bool]:
    return self._pattern_properties
  @pattern_properties.setter
  def pattern_properties(self, pattern_properties: dict[str, MessageOneOf1OneOf1PayloadObject | bool]):
    self._pattern_properties = pattern_properties

  @property
  def dependencies(self) -> dict[str,  | List[str]]:
    return self._dependencies
  @dependencies.setter
  def dependencies(self, dependencies: dict[str,  | List[str]]):
    self._dependencies = dependencies

  @property
  def property_names(self) -> MessageOneOf1OneOf1PayloadObject | bool:
    return self._property_names
  @property_names.setter
  def property_names(self, property_names: MessageOneOf1OneOf1PayloadObject | bool):
    self._property_names = property_names

  @property
  def const(self) -> Any:
    return self._const
  @const.setter
  def const(self, const: Any):
    self._const = const

  @property
  def enum(self) -> List[Any]:
    return self._enum
  @enum.setter
  def enum(self, enum: List[Any]):
    self._enum = enum

  @property
  def type(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchemaType:
    return self._type

  @property
  def format(self) -> str:
    return self._format
  @format.setter
  def format(self, format: str):
    self._format = format

  @property
  def content_media_type(self) -> str:
    return self._content_media_type
  @content_media_type.setter
  def content_media_type(self, content_media_type: str):
    self._content_media_type = content_media_type

  @property
  def content_encoding(self) -> str:
    return self._content_encoding
  @content_encoding.setter
  def content_encoding(self, content_encoding: str):
    self._content_encoding = content_encoding

  @property
  def reserved_if(self) -> MessageOneOf1OneOf1PayloadObject | bool:
    return self._reserved_if
  @reserved_if.setter
  def reserved_if(self, reserved_if: MessageOneOf1OneOf1PayloadObject | bool):
    self._reserved_if = reserved_if

  @property
  def then(self) -> MessageOneOf1OneOf1PayloadObject | bool:
    return self._then
  @then.setter
  def then(self, then: MessageOneOf1OneOf1PayloadObject | bool):
    self._then = then

  @property
  def reserved_else(self) -> MessageOneOf1OneOf1PayloadObject | bool:
    return self._reserved_else
  @reserved_else.setter
  def reserved_else(self, reserved_else: MessageOneOf1OneOf1PayloadObject | bool):
    self._reserved_else = reserved_else

  @property
  def all_of(self) -> List[MessageOneOf1OneOf1PayloadObject | bool]:
    return self._all_of
  @all_of.setter
  def all_of(self, all_of: List[MessageOneOf1OneOf1PayloadObject | bool]):
    self._all_of = all_of

  @property
  def any_of(self) -> List[MessageOneOf1OneOf1PayloadObject | bool]:
    return self._any_of
  @any_of.setter
  def any_of(self, any_of: List[MessageOneOf1OneOf1PayloadObject | bool]):
    self._any_of = any_of

  @property
  def one_of(self) -> List[MessageOneOf1OneOf1PayloadObject | bool]:
    return self._one_of
  @one_of.setter
  def one_of(self, one_of: List[MessageOneOf1OneOf1PayloadObject | bool]):
    self._one_of = one_of

  @property
  def reserved_not(self) -> MessageOneOf1OneOf1PayloadObject | bool:
    return self._reserved_not
  @reserved_not.setter
  def reserved_not(self, reserved_not: MessageOneOf1OneOf1PayloadObject | bool):
    self._reserved_not = reserved_not

  @property
  def discriminator(self) -> SchemaAllOf1DiscriminatorObject | str:
    return self._discriminator
  @discriminator.setter
  def discriminator(self, discriminator: SchemaAllOf1DiscriminatorObject | str):
    self._discriminator = discriminator

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
  def nullable(self) -> bool:
    return self._nullable
  @nullable.setter
  def nullable(self, nullable: bool):
    self._nullable = nullable

  @property
  def example(self) -> Any:
    return self._example
  @example.setter
  def example(self, example: Any):
    self._example = example

  @property
  def xml(self) -> OpenapiSchema30Xml:
    return self._xml
  @xml.setter
  def xml(self, xml: OpenapiSchema30Xml):
    self._xml = xml

  @property
  def reserved_additional_properties(self) -> dict[str, Any | Any]:
    return self._reserved_additional_properties
  @reserved_additional_properties.setter
  def reserved_additional_properties(self, reserved_additional_properties: dict[str, Any | Any]):
    self._reserved_additional_properties = reserved_additional_properties

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return MessageOneOf1OneOf1PayloadObject(**json.loads(json_string))
