
import json
from typing import Dict
class Xml: 
  def __init__(self, input: Dict):
    if hasattr(input, 'name'):
      self._name: str = input['name']
    if hasattr(input, 'namespace'):
      self._namespace: str = input['namespace']
    if hasattr(input, 'prefix'):
      self._prefix: str = input['prefix']
    if hasattr(input, 'attribute'):
      self._attribute: bool = input['attribute']
    if hasattr(input, 'wrapped'):
      self._wrapped: bool = input['wrapped']

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

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return Xml(**json.loads(json_string))
