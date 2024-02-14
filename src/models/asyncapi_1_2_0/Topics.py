from .TopicItem import TopicItem
import json
from typing import Any, List, Dict
class Topics: 
  def __init__(self, input: Dict):
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any | TopicItem] = input['additional_properties']

  @property
  def additional_properties(self) -> dict[str, Any | TopicItem]:
    return self._additional_properties
  @additional_properties.setter
  def additional_properties(self, additional_properties: dict[str, Any | TopicItem]):
    self._additional_properties = additional_properties

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return Topics(**json.loads(json_string))
