from __future__ import annotations
import json
from typing import Any, Dict

class ExternalDocs: 
  def __init__(self, input: Dict):
    if 'description' in input:
      self._description: str = input['description']
    self._url: str = input['url']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

  @property
  def url(self) -> str:
    return self._url
  @url.setter
  def url(self, url: str):
    self._url = url

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
    return ExternalDocs(**json.loads(json_string))
