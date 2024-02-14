
import json
from typing import Any, Dict
class ExternalDocs: 
  def __init__(self, input: Dict):
    if hasattr(input, 'description'):
      self._description: str = input['description']
    self._url: str = input['url']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any | Any] = input['additional_properties']

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
  def additional_properties(self) -> dict[str, Any | Any]:
    return self._additional_properties
  @additional_properties.setter
  def additional_properties(self, additional_properties: dict[str, Any | Any]):
    self._additional_properties = additional_properties

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return ExternalDocs(**json.loads(json_string))
