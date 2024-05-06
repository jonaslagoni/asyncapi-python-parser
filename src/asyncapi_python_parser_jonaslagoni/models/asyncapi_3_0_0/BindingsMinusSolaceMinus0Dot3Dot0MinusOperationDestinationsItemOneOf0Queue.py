from __future__ import annotations
import json
from typing import List, Any, Dict
from . import BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0QueueAccessType
class BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0Queue: 
  def __init__(self, input: Dict):
    if 'name' in input:
      self._name: str = input['name']
    if 'topic_subscriptions' in input:
      self._topic_subscriptions: List[str] = input['topic_subscriptions']
    if 'access_type' in input:
      self._access_type: BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0QueueAccessType.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0QueueAccessType = BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0QueueAccessType.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0QueueAccessType(input['access_type'])
    if 'max_ttl' in input:
      self._max_ttl: str = input['max_ttl']
    if 'max_msg_spool_usage' in input:
      self._max_msg_spool_usage: str = input['max_msg_spool_usage']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def name(self) -> str:
    return self._name
  @name.setter
  def name(self, name: str):
    self._name = name

  @property
  def topic_subscriptions(self) -> List[str]:
    return self._topic_subscriptions
  @topic_subscriptions.setter
  def topic_subscriptions(self, topic_subscriptions: List[str]):
    self._topic_subscriptions = topic_subscriptions

  @property
  def access_type(self) -> BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0QueueAccessType.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0QueueAccessType:
    return self._access_type
  @access_type.setter
  def access_type(self, access_type: BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0QueueAccessType.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0QueueAccessType):
    self._access_type = access_type

  @property
  def max_ttl(self) -> str:
    return self._max_ttl
  @max_ttl.setter
  def max_ttl(self, max_ttl: str):
    self._max_ttl = max_ttl

  @property
  def max_msg_spool_usage(self) -> str:
    return self._max_msg_spool_usage
  @max_msg_spool_usage.setter
  def max_msg_spool_usage(self, max_msg_spool_usage: str):
    self._max_msg_spool_usage = max_msg_spool_usage

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
    return BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0Queue(**json.loads(json_string))
