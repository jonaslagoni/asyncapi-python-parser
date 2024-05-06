from __future__ import annotations
import json
from typing import Any, Dict

class MessageOneOf1OneOf1ExamplesItem: 
  def __init__(self, input: Dict):
    if 'headers' in input:
      self._headers: dict[str, Any] = input['headers']
    if 'payload' in input:
      self._payload: Any = input['payload']

  @property
  def headers(self) -> dict[str, Any]:
    return self._headers
  @headers.setter
  def headers(self, headers: dict[str, Any]):
    self._headers = headers

  @property
  def payload(self) -> Any:
    return self._payload
  @payload.setter
  def payload(self, payload: Any):
    self._payload = payload

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return MessageOneOf1OneOf1ExamplesItem(**json.loads(json_string))
