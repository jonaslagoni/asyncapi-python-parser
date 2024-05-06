from __future__ import annotations
import json
from typing import Any, List, Dict
from . import PrimitiveType
from . import PrimitiveTypeWithMetadata
from . import Record
from . import Enum
from . import Array
from . import Map
from . import Fixed
from . import AvroSchemaV1AvroFieldOrder
class Field: 
  def __init__(self, input: Dict):
    self._name: str = input['name']
    self._type: PrimitiveType.PrimitiveType | PrimitiveTypeWithMetadata.PrimitiveTypeWithMetadata | Any | Record.Record | Enum.Enum | Array.Array | Map.Map | Fixed.Fixed | List[] = input['type']
    if 'doc' in input:
      self._doc: str = input['doc']
    if 'default' in input:
      self._default: Any = input['default']
    if 'order' in input:
      self._order: AvroSchemaV1AvroFieldOrder.AvroSchemaV1AvroFieldOrder = AvroSchemaV1AvroFieldOrder.AvroSchemaV1AvroFieldOrder(input['order'])
    if 'aliases' in input:
      self._aliases: List[str] = input['aliases']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def name(self) -> str:
    return self._name
  @name.setter
  def name(self, name: str):
    self._name = name

  @property
  def type(self) -> PrimitiveType.PrimitiveType | PrimitiveTypeWithMetadata.PrimitiveTypeWithMetadata | Any | Record.Record | Enum.Enum | Array.Array | Map.Map | Fixed.Fixed | List[]:
    return self._type
  @type.setter
  def type(self, type: PrimitiveType.PrimitiveType | PrimitiveTypeWithMetadata.PrimitiveTypeWithMetadata | Any | Record.Record | Enum.Enum | Array.Array | Map.Map | Fixed.Fixed | List[]):
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
  def order(self) -> AvroSchemaV1AvroFieldOrder.AvroSchemaV1AvroFieldOrder:
    return self._order
  @order.setter
  def order(self, order: AvroSchemaV1AvroFieldOrder.AvroSchemaV1AvroFieldOrder):
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
