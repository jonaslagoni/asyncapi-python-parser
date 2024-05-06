from __future__ import annotations
import json
from typing import List, Any, Dict
from . import PrimitiveType
from . import PrimitiveTypeWithMetadata
from . import Record
from . import Enum
from . import Array
from . import Fixed
class Map: 
  def __init__(self, input: Dict):
    self._type: str = 'map'
    if 'name' in input:
      self._name: str = input['name']
    if 'namespace' in input:
      self._namespace: str = input['namespace']
    if 'doc' in input:
      self._doc: str = input['doc']
    if 'aliases' in input:
      self._aliases: List[str] = input['aliases']
    self._values: PrimitiveType.PrimitiveType | PrimitiveTypeWithMetadata.PrimitiveTypeWithMetadata | Any | Record.Record | Enum.Enum | Array.Array | Map | Fixed.Fixed | List[Any] = input['values']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def type(self) -> str:
    return self._type

  @property
  def name(self) -> str:
    return self._name
  @name.setter
  def name(self, name: str):
    self._name = name

  @property
  def namespace(self) -> str:
    return self._namespace
  @namespace.setter
  def namespace(self, namespace: str):
    self._namespace = namespace

  @property
  def doc(self) -> str:
    return self._doc
  @doc.setter
  def doc(self, doc: str):
    self._doc = doc

  @property
  def aliases(self) -> List[str]:
    return self._aliases
  @aliases.setter
  def aliases(self, aliases: List[str]):
    self._aliases = aliases

  @property
  def values(self) -> PrimitiveType.PrimitiveType | PrimitiveTypeWithMetadata.PrimitiveTypeWithMetadata | Any | Record.Record | Enum.Enum | Array.Array | Map | Fixed.Fixed | List[Any]:
    return self._values
  @values.setter
  def values(self, values: PrimitiveType.PrimitiveType | PrimitiveTypeWithMetadata.PrimitiveTypeWithMetadata | Any | Record.Record | Enum.Enum | Array.Array | Map | Fixed.Fixed | List[Any]):
    self._values = values

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
    return Map(**json.loads(json_string))
