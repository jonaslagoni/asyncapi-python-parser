from __future__ import annotations
import json
from typing import Any, List, Dict
from . import Reference
from . import OperationReplyAddress
class OperationReply: 
  def __init__(self, input: Dict):
    if 'address' in input:
      self._address: Reference.Reference | OperationReplyAddress.OperationReplyAddress = input['address']
    if 'channel' in input:
      self._channel: Reference.Reference = Reference.Reference(input['channel'])
    if 'messages' in input:
      self._messages: List[Reference.Reference] = input['messages']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def address(self) -> Reference.Reference | OperationReplyAddress.OperationReplyAddress:
    return self._address
  @address.setter
  def address(self, address: Reference.Reference | OperationReplyAddress.OperationReplyAddress):
    self._address = address

  @property
  def channel(self) -> Reference.Reference:
    return self._channel
  @channel.setter
  def channel(self, channel: Reference.Reference):
    self._channel = channel

  @property
  def messages(self) -> List[Reference.Reference]:
    return self._messages
  @messages.setter
  def messages(self, messages: List[Reference.Reference]):
    self._messages = messages

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
    return OperationReply(**json.loads(json_string))
