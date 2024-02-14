from .Message import Message
import json
from typing import Any, List, Dict
class TopicItem: 
  def __init__(self, input: Dict):
    if hasattr(input, 'dollar_ref'):
      self._dollar_ref: str = input['dollar_ref']
    if hasattr(input, 'publish'):
      self._publish: Message = Message(input['publish'])
    if hasattr(input, 'subscribe'):
      self._subscribe: Message = Message(input['subscribe'])
    if hasattr(input, 'deprecated'):
      self._deprecated: bool = input['deprecated']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def dollar_ref(self) -> str:
    return self._dollar_ref
  @dollar_ref.setter
  def dollar_ref(self, dollar_ref: str):
    self._dollar_ref = dollar_ref

  @property
  def publish(self) -> Message:
    return self._publish
  @publish.setter
  def publish(self, publish: Message):
    self._publish = publish

  @property
  def subscribe(self) -> Message:
    return self._subscribe
  @subscribe.setter
  def subscribe(self, subscribe: Message):
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
