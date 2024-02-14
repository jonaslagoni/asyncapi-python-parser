from .PrimitiveType import PrimitiveType
from .PrimitiveTypeWithMetadata import PrimitiveTypeWithMetadata
from .Record import Record
from .Enum import Enum
from .Array import Array
from .Map import Map
from .Fixed import Fixed
from .AvroSchemaV1AvroFieldOrder import AvroSchemaV1AvroFieldOrder
import json
from typing import Any, List, Dict
class Field: 
  def __init__(self, input: Dict):
    self._name: str = input['name']
    self._type: PrimitiveType | PrimitiveTypeWithMetadata | Any | Record | Enum | Array | Map | Fixed | List[] = input['type']
    if hasattr(input, 'doc'):
      self._doc: str = input['doc']
    if hasattr(input, 'default'):
      self._default: Any = input['default']
    if hasattr(input, 'order'):
      self._order: AvroSchemaV1AvroFieldOrder = AvroSchemaV1AvroFieldOrder(input['order'])
    if hasattr(input, 'aliases'):
      self._aliases: List[str] = input['aliases']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def name(self) -> str:
    return self._name
  @name.setter
  def name(self, name: str):
    self._name = name

  @property
  def type(self) -> PrimitiveType | PrimitiveTypeWithMetadata | Any | Record | Enum | Array | Map | Fixed | List[]:
    return self._type
  @type.setter
  def type(self, type: PrimitiveType | PrimitiveTypeWithMetadata | Any | Record | Enum | Array | Map | Fixed | List[]):
    self._type = type

  @property
  def doc(self) -> str:
    return self._doc
  @doc.setter
  def doc(self, doc: str):
    self._doc = doc

  @property
  def default(self) -> Any:
    return self._default
  @default.setter
  def default(self, default: Any):
    self._default = default

  @property
  def order(self) -> AvroSchemaV1AvroFieldOrder:
    return self._order
  @order.setter
  def order(self, order: AvroSchemaV1AvroFieldOrder):
    self._order = order

  @property
  def aliases(self) -> List[str]:
    return self._aliases
  @aliases.setter
  def aliases(self, aliases: List[str]):
    self._aliases = aliases

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
    return Field(**json.loads(json_string))
