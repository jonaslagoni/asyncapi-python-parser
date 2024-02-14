from .PrimitiveType import PrimitiveType
from .PrimitiveTypeWithMetadata import PrimitiveTypeWithMetadata
from .Record import Record
from .Enum import Enum
from .Map import Map
from .Fixed import Fixed
import json
from typing import List, Any, Dict
class Array: 
  def __init__(self, input: Dict):
    self._type: str = 'array'
    if hasattr(input, 'name'):
      self._name: str = input['name']
    if hasattr(input, 'namespace'):
      self._namespace: str = input['namespace']
    if hasattr(input, 'doc'):
      self._doc: str = input['doc']
    if hasattr(input, 'aliases'):
      self._aliases: List[str] = input['aliases']
    self._items: PrimitiveType | PrimitiveTypeWithMetadata | Any | Record | Enum | Array | Map | Fixed | List[] = input['items']
    if hasattr(input, 'additional_properties'):
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
  def items(self) -> PrimitiveType | PrimitiveTypeWithMetadata | Any | Record | Enum | Array | Map | Fixed | List[]:
    return self._items
  @items.setter
  def items(self, items: PrimitiveType | PrimitiveTypeWithMetadata | Any | Record | Enum | Array | Map | Fixed | List[]):
    self._items = items

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
    return Array(**json.loads(json_string))
