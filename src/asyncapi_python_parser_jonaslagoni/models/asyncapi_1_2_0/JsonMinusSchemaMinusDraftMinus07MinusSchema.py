from __future__ import annotations
import json
from typing import Any, List, Dict
from . import JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes
class JsonMinusSchemaMinusDraftMinus07MinusSchema: 
  def __init__(self, input: Dict):
    if 'id' in input:
      self._id: str = input['id']
    if 'dollar_schema' in input:
      self._dollar_schema: str = input['dollar_schema']
    if 'title' in input:
      self._title: str = input['title']
    if 'description' in input:
      self._description: str = input['description']
    if 'default' in input:
      self._default: Any = input['default']
    if 'multiple_of' in input:
      self._multiple_of: float = input['multiple_of']
    if 'maximum' in input:
      self._maximum: float = input['maximum']
    if 'exclusive_maximum' in input:
      self._exclusive_maximum: bool = input['exclusive_maximum']
    if 'minimum' in input:
      self._minimum: float = input['minimum']
    if 'exclusive_minimum' in input:
      self._exclusive_minimum: bool = input['exclusive_minimum']
    if 'max_length' in input:
      self._max_length: int = input['max_length']
    if 'min_length' in input:
      self._min_length: int = input['min_length']
    if 'pattern' in input:
      self._pattern: str = input['pattern']
    if 'additional_items' in input:
      self._additional_items: bool | JsonMinusSchemaMinusDraftMinus07MinusSchema = input['additional_items']
    if 'items' in input:
      self._items: JsonMinusSchemaMinusDraftMinus07MinusSchema | List[JsonMinusSchemaMinusDraftMinus07MinusSchema] = input['items']
    if 'max_items' in input:
      self._max_items: int = input['max_items']
    if 'min_items' in input:
      self._min_items: int = input['min_items']
    if 'unique_items' in input:
      self._unique_items: bool = input['unique_items']
    if 'max_properties' in input:
      self._max_properties: int = input['max_properties']
    if 'min_properties' in input:
      self._min_properties: int = input['min_properties']
    if 'required' in input:
      self._required: List[str] = input['required']
    if 'additional_properties' in input:
      self._additional_properties: bool | JsonMinusSchemaMinusDraftMinus07MinusSchema = input['additional_properties']
    if 'definitions' in input:
      self._definitions: dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema] = input['definitions']
    if 'properties' in input:
      self._properties: dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema] = input['properties']
    if 'pattern_properties' in input:
      self._pattern_properties: dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema] = input['pattern_properties']
    if 'dependencies' in input:
      self._dependencies: dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema | List[str]] = input['dependencies']
    if 'enum' in input:
      self._enum: List[Any] = input['enum']
    if 'type' in input:
      self._type: JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes.JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes | List[JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes.JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes] = input['type']
    if 'format' in input:
      self._format: str = input['format']
    if 'all_of' in input:
      self._all_of: List[JsonMinusSchemaMinusDraftMinus07MinusSchema] = input['all_of']
    if 'any_of' in input:
      self._any_of: List[JsonMinusSchemaMinusDraftMinus07MinusSchema] = input['any_of']
    if 'one_of' in input:
      self._one_of: List[JsonMinusSchemaMinusDraftMinus07MinusSchema] = input['one_of']
    if 'reserved_not' in input:
      self._reserved_not: JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema(input['reserved_not'])
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def id(self) -> str:
    return self._id
  @id.setter
  def id(self, id: str):
    self._id = id

  @property
  def dollar_schema(self) -> str:
    return self._dollar_schema
  @dollar_schema.setter
  def dollar_schema(self, dollar_schema: str):
    self._dollar_schema = dollar_schema

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
  def exclusive_maximum(self) -> bool:
    return self._exclusive_maximum
  @exclusive_maximum.setter
  def exclusive_maximum(self, exclusive_maximum: bool):
    self._exclusive_maximum = exclusive_maximum

  @property
  def minimum(self) -> float:
    return self._minimum
  @minimum.setter
  def minimum(self, minimum: float):
    self._minimum = minimum

  @property
  def exclusive_minimum(self) -> bool:
    return self._exclusive_minimum
  @exclusive_minimum.setter
  def exclusive_minimum(self, exclusive_minimum: bool):
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
  def additional_items(self) -> bool | JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._additional_items
  @additional_items.setter
  def additional_items(self, additional_items: bool | JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._additional_items = additional_items

  @property
  def items(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema | List[JsonMinusSchemaMinusDraftMinus07MinusSchema]:
    return self._items
  @items.setter
  def items(self, items: JsonMinusSchemaMinusDraftMinus07MinusSchema | List[JsonMinusSchemaMinusDraftMinus07MinusSchema]):
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
  def additional_properties(self) -> bool | JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._additional_properties
  @additional_properties.setter
  def additional_properties(self, additional_properties: bool | JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._additional_properties = additional_properties

  @property
  def definitions(self) -> dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema]:
    return self._definitions
  @definitions.setter
  def definitions(self, definitions: dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema]):
    self._definitions = definitions

  @property
  def properties(self) -> dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema]:
    return self._properties
  @properties.setter
  def properties(self, properties: dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema]):
    self._properties = properties

  @property
  def pattern_properties(self) -> dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema]:
    return self._pattern_properties
  @pattern_properties.setter
  def pattern_properties(self, pattern_properties: dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema]):
    self._pattern_properties = pattern_properties

  @property
  def dependencies(self) -> dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema | List[str]]:
    return self._dependencies
  @dependencies.setter
  def dependencies(self, dependencies: dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema | List[str]]):
    self._dependencies = dependencies

  @property
  def enum(self) -> List[Any]:
    return self._enum
  @enum.setter
  def enum(self, enum: List[Any]):
    self._enum = enum

  @property
  def type(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes.JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes | List[JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes.JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes]:
    return self._type
  @type.setter
  def type(self, type: JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes.JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes | List[JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes.JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes]):
    self._type = type

  @property
  def format(self) -> str:
    return self._format
  @format.setter
  def format(self, format: str):
    self._format = format

  @property
  def all_of(self) -> List[JsonMinusSchemaMinusDraftMinus07MinusSchema]:
    return self._all_of
  @all_of.setter
  def all_of(self, all_of: List[JsonMinusSchemaMinusDraftMinus07MinusSchema]):
    self._all_of = all_of

  @property
  def any_of(self) -> List[JsonMinusSchemaMinusDraftMinus07MinusSchema]:
    return self._any_of
  @any_of.setter
  def any_of(self, any_of: List[JsonMinusSchemaMinusDraftMinus07MinusSchema]):
    self._any_of = any_of

  @property
  def one_of(self) -> List[JsonMinusSchemaMinusDraftMinus07MinusSchema]:
    return self._one_of
  @one_of.setter
  def one_of(self, one_of: List[JsonMinusSchemaMinusDraftMinus07MinusSchema]):
    self._one_of = one_of

  @property
  def reserved_not(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchema:
    return self._reserved_not
  @reserved_not.setter
  def reserved_not(self, reserved_not: JsonMinusSchemaMinusDraftMinus07MinusSchema):
    self._reserved_not = reserved_not

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
    return JsonMinusSchemaMinusDraftMinus07MinusSchema(**json.loads(json_string))
