from __future__ import annotations
import json
from typing import List, Dict

class BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy: 
  def __init__(self, input: Dict):
    if 'allowed_persistence_regions' in input:
      self._allowed_persistence_regions: List[str] = input['allowed_persistence_regions']

  @property
  def allowed_persistence_regions(self) -> List[str]:
    return self._allowed_persistence_regions
  @allowed_persistence_regions.setter
  def allowed_persistence_regions(self, allowed_persistence_regions: List[str]):
    self._allowed_persistence_regions = allowed_persistence_regions

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy(**json.loads(json_string))
