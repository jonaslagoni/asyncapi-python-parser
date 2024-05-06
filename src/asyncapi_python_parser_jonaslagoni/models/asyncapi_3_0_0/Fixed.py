from __future__ import annotations
import json
from typing import List, Any, Dict

class Fixed: 
  def __init__(self, input: Dict):
    self._type: str = 'fixed'
    self._name: str = input['name']
    if 'namespace' in input:
      self._namespace: str = input['namespace']
    if 'doc' in input:
      self._doc: str = input['doc']
    if 'aliases' in input:
      self._aliases: List[str] = input['aliases']
    self._size: float = input['size']
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
  def size(self) -> float:
    return self._size
  @size.setter
  def size(self, size: float):
    self._size = size

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
    return Fixed(**json.loads(json_string))
