from __future__ import annotations
import json
from typing import Any, Dict

class OpenapiSchema30Xml: 
  def __init__(self, input: Dict):
    if 'name' in input:
      self._name: str = input['name']
    if 'namespace' in input:
      self._namespace: str = input['namespace']
    if 'prefix' in input:
      self._prefix: str = input['prefix']
    if 'attribute' in input:
      self._attribute: bool = input['attribute']
    if 'wrapped' in input:
      self._wrapped: bool = input['wrapped']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

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
  def prefix(self) -> str:
    return self._prefix
  @prefix.setter
  def prefix(self, prefix: str):
    self._prefix = prefix

  @property
  def attribute(self) -> bool:
    return self._attribute
  @attribute.setter
  def attribute(self, attribute: bool):
    self._attribute = attribute

  @property
  def wrapped(self) -> bool:
    return self._wrapped
  @wrapped.setter
  def wrapped(self, wrapped: bool):
    self._wrapped = wrapped

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
    return OpenapiSchema30Xml(**json.loads(json_string))
