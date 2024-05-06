from __future__ import annotations
import json
from typing import Any, Dict

class BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings: 
  def __init__(self, input: Dict):
    self._encoding: str = input['encoding']
    if 'first_revision_id' in input:
      self._first_revision_id: str = input['first_revision_id']
    if 'last_revision_id' in input:
      self._last_revision_id: str = input['last_revision_id']
    self._name: str = input['name']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def encoding(self) -> str:
    return self._encoding
  @encoding.setter
  def encoding(self, encoding: str):
    self._encoding = encoding

  @property
  def first_revision_id(self) -> str:
    return self._first_revision_id
  @first_revision_id.setter
  def first_revision_id(self, first_revision_id: str):
    self._first_revision_id = first_revision_id

  @property
  def last_revision_id(self) -> str:
    return self._last_revision_id
  @last_revision_id.setter
  def last_revision_id(self, last_revision_id: str):
    self._last_revision_id = last_revision_id

  @property
  def name(self) -> str:
    return self._name
  @name.setter
  def name(self, name: str):
    self._name = name

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
    return BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings(**json.loads(json_string))
