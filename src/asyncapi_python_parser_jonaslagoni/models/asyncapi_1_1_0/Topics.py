from __future__ import annotations
import json
from typing import Any, List, Dict
from . import TopicItem
class Topics: 
  def __init__(self, input: Dict):
    if 'extensions' in input:
      self._extensions: dict[str, Any | TopicItem.TopicItem] = input['extensions']

  @property
  def extensions(self) -> dict[str, Any | TopicItem.TopicItem]:
    return self._extensions
  @extensions.setter
  def extensions(self, extensions: dict[str, Any | TopicItem.TopicItem]):
    self._extensions = extensions

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return Topics(**json.loads(json_string))
