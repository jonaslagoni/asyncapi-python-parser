from .JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes import JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes
import json
from typing import Any, List, Dict
class JsonMinusSchemaMinusDraftMinus07MinusSchema: 
  def __init__(self, input: Dict):
    if hasattr(input, 'id'):
      self._id: str = input['id']
    if hasattr(input, 'dollar_schema'):
      self._dollar_schema: str = input['dollar_schema']
    if hasattr(input, 'title'):
      self._title: str = input['title']
    if hasattr(input, 'description'):
      self._description: str = input['description']
    if hasattr(input, 'default'):
      self._default: Any = input['default']
    if hasattr(input, 'multiple_of'):
      self._multiple_of: float = input['multiple_of']
    if hasattr(input, 'maximum'):
      self._maximum: float = input['maximum']
    if hasattr(input, 'exclusive_maximum'):
      self._exclusive_maximum: bool = input['exclusive_maximum']
    if hasattr(input, 'minimum'):
      self._minimum: float = input['minimum']
    if hasattr(input, 'exclusive_minimum'):
      self._exclusive_minimum: bool = input['exclusive_minimum']
    if hasattr(input, 'max_length'):
      self._max_length: int = input['max_length']
    if hasattr(input, 'min_length'):
      self._min_length: int = input['min_length']
    if hasattr(input, 'pattern'):
      self._pattern: str = input['pattern']
    if hasattr(input, 'additional_items'):
      self._additional_items: bool | JsonMinusSchemaMinusDraftMinus07MinusSchema = input['additional_items']
    if hasattr(input, 'items'):
      self._items: JsonMinusSchemaMinusDraftMinus07MinusSchema | List[JsonMinusSchemaMinusDraftMinus07MinusSchema] = input['items']
    if hasattr(input, 'max_items'):
      self._max_items: int = input['max_items']
    if hasattr(input, 'min_items'):
      self._min_items: int = input['min_items']
    if hasattr(input, 'unique_items'):
      self._unique_items: bool = input['unique_items']
    if hasattr(input, 'max_properties'):
      self._max_properties: int = input['max_properties']
    if hasattr(input, 'min_properties'):
      self._min_properties: int = input['min_properties']
    if hasattr(input, 'required'):
      self._required: List[str] = input['required']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: bool | JsonMinusSchemaMinusDraftMinus07MinusSchema = input['additional_properties']
    if hasattr(input, 'definitions'):
      self._definitions: dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema] = input['definitions']
    if hasattr(input, 'properties'):
      self._properties: dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema] = input['properties']
    if hasattr(input, 'pattern_properties'):
      self._pattern_properties: dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema] = input['pattern_properties']
    if hasattr(input, 'dependencies'):
      self._dependencies: dict[str, JsonMinusSchemaMinusDraftMinus07MinusSchema | List[str]] = input['dependencies']
    if hasattr(input, 'enum'):
      self._enum: List[Any] = input['enum']
    if hasattr(input, 'type'):
      self._type: JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes | List[JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes] = input['type']
    if hasattr(input, 'format'):
      self._format: str = input['format']
    if hasattr(input, 'all_of'):
      self._all_of: List[JsonMinusSchemaMinusDraftMinus07MinusSchema] = input['all_of']
    if hasattr(input, 'any_of'):
      self._any_of: List[JsonMinusSchemaMinusDraftMinus07MinusSchema] = input['any_of']
    if hasattr(input, 'one_of'):
      self._one_of: List[JsonMinusSchemaMinusDraftMinus07MinusSchema] = input['one_of']
    if hasattr(input, 'reserved_not'):
      self._reserved_not: JsonMinusSchemaMinusDraftMinus07MinusSchema = JsonMinusSchemaMinusDraftMinus07MinusSchema(input['reserved_not'])
    if hasattr(input, 'reserved_additional_properties'):
      self._reserved_additional_properties: dict[str, Any] = input['reserved_additional_properties']

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
  def type(self) -> JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes | List[JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes]:
    return self._type
  @type.setter
  def type(self, type: JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes | List[JsonMinusSchemaMinusDraftMinus07MinusSchemaSimpleTypes]):
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
  def reserved_additional_properties(self) -> dict[str, Any]:
    return self._reserved_additional_properties
  @reserved_additional_properties.setter
  def reserved_additional_properties(self, reserved_additional_properties: dict[str, Any]):
    self._reserved_additional_properties = reserved_additional_properties

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return JsonMinusSchemaMinusDraftMinus07MinusSchema(**json.loads(json_string))
