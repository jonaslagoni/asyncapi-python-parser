from __future__ import annotations
import json
from typing import Any, Dict

class Reference: 
  def __init__(self, input: Dict):
    self._dollar_ref: str = input['dollar_ref']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def dollar_ref(self) -> str:
    return self._dollar_ref
  @dollar_ref.setter
  def dollar_ref(self, dollar_ref: str):
    self._dollar_ref = dollar_ref

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
    return Reference(**json.loads(json_string))
