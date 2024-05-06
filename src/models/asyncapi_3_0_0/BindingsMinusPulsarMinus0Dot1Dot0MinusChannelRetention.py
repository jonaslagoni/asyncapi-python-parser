from __future__ import annotations
import json
from typing import Dict

class BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention: 
  def __init__(self, input: Dict):
    if 'time' in input:
      self._time: int = input['time']
    if 'size' in input:
      self._size: int = input['size']

  @property
  def time(self) -> int:
    return self._time
  @time.setter
  def time(self, time: int):
    self._time = time

  @property
  def size(self) -> int:
    return self._size
  @size.setter
  def size(self, size: int):
    self._size = size

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention(**json.loads(json_string))
