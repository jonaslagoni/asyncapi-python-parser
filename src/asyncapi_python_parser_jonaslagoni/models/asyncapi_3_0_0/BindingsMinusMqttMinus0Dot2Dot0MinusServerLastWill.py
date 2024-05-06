from __future__ import annotations
import json
from typing import Any, Dict
from . import BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWillQos
class BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill: 
  def __init__(self, input: Dict):
    if 'topic' in input:
      self._topic: str = input['topic']
    if 'qos' in input:
      self._qos: BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWillQos.BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWillQos = BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWillQos.BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWillQos(input['qos'])
    if 'message' in input:
      self._message: str = input['message']
    if 'retain' in input:
      self._retain: bool = input['retain']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def topic(self) -> str:
    return self._topic
  @topic.setter
  def topic(self, topic: str):
    self._topic = topic

  @property
  def qos(self) -> BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWillQos.BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWillQos:
    return self._qos
  @qos.setter
  def qos(self, qos: BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWillQos.BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWillQos):
    self._qos = qos

  @property
  def message(self) -> str:
    return self._message
  @message.setter
  def message(self, message: str):
    self._message = message

  @property
  def retain(self) -> bool:
    return self._retain
  @retain.setter
  def retain(self, retain: bool):
    self._retain = retain

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
    return BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill(**json.loads(json_string))
