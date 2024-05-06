from __future__ import annotations
import json
from typing import Any, List, Dict
from . import Message
class TopicItem: 
  def __init__(self, input: Dict):
    if 'dollar_ref' in input:
      self._dollar_ref: str = input['dollar_ref']
    if 'publish' in input:
      self._publish: Message.Message = Message.Message(input['publish'])
    if 'subscribe' in input:
      self._subscribe: Message.Message = Message.Message(input['subscribe'])
    if 'deprecated' in input:
      self._deprecated: bool = input['deprecated']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def dollar_ref(self) -> str:
    return self._dollar_ref
  @dollar_ref.setter
  def dollar_ref(self, dollar_ref: str):
    self._dollar_ref = dollar_ref

  @property
  def publish(self) -> Message.Message:
    return self._publish
  @publish.setter
  def publish(self, publish: Message.Message):
    self._publish = publish

  @property
  def subscribe(self) -> Message.Message:
    return self._subscribe
  @subscribe.setter
  def subscribe(self, subscribe: Message.Message):
    self._subscribe = subscribe

  @property
  def deprecated(self) -> bool:
    return self._deprecated
  @deprecated.setter
  def deprecated(self, deprecated: bool):
    self._deprecated = deprecated

  @property
  def additional_properties(self) -> dict[str, Any]:
    return self._additional_properties
  @additional_properties.setter
  def additional_properties(self, additional_properties: dict[str, Any]):
    self._additional_properties = additional_properties

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return TopicItem(**json.loads(json_string))
