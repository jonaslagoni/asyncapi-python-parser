from .Reference import Reference
from .OperationReplyAddress import OperationReplyAddress
import json
from typing import Any, List, Dict
class OperationReply: 
  def __init__(self, input: Dict):
    if hasattr(input, 'address'):
      self._address: Reference | OperationReplyAddress = input['address']
    if hasattr(input, 'channel'):
      self._channel: Reference = Reference(input['channel'])
    if hasattr(input, 'messages'):
      self._messages: List[Reference] = input['messages']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def address(self) -> Reference | OperationReplyAddress:
    return self._address
  @address.setter
  def address(self, address: Reference | OperationReplyAddress):
    self._address = address

  @property
  def channel(self) -> Reference:
    return self._channel
  @channel.setter
  def channel(self, channel: Reference):
    self._channel = channel

  @property
  def messages(self) -> List[Reference]:
    return self._messages
  @messages.setter
  def messages(self, messages: List[Reference]):
    self._messages = messages

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
    return OperationReply(**json.loads(json_string))
