from __future__ import annotations
import json
from typing import Any, List, Dict
from . import Reference
from . import Parameter
from . import Operation
class ChannelItem: 
  def __init__(self, input: Dict):
    if 'dollar_ref' in input:
      self._dollar_ref: str = input['dollar_ref']
    if 'parameters' in input:
      self._parameters: dict[str, Reference.Reference | Parameter.Parameter] = input['parameters']
    if 'publish' in input:
      self._publish: Operation.Operation = Operation.Operation(input['publish'])
    if 'subscribe' in input:
      self._subscribe: Operation.Operation = Operation.Operation(input['subscribe'])
    if 'deprecated' in input:
      self._deprecated: bool = input['deprecated']
    if 'protocol_info' in input:
      self._protocol_info: dict[str, dict[str, Any]] = input['protocol_info']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def dollar_ref(self) -> str:
    return self._dollar_ref
  @dollar_ref.setter
  def dollar_ref(self, dollar_ref: str):
    self._dollar_ref = dollar_ref

  @property
  def parameters(self) -> dict[str, Reference.Reference | Parameter.Parameter]:
    return self._parameters
  @parameters.setter
  def parameters(self, parameters: dict[str, Reference.Reference | Parameter.Parameter]):
    self._parameters = parameters

  @property
  def publish(self) -> Operation.Operation:
    return self._publish
  @publish.setter
  def publish(self, publish: Operation.Operation):
    self._publish = publish

  @property
  def subscribe(self) -> Operation.Operation:
    return self._subscribe
  @subscribe.setter
  def subscribe(self, subscribe: Operation.Operation):
    self._subscribe = subscribe

  @property
  def deprecated(self) -> bool:
    return self._deprecated
  @deprecated.setter
  def deprecated(self, deprecated: bool):
    self._deprecated = deprecated

  @property
  def protocol_info(self) -> dict[str, dict[str, Any]]:
    return self._protocol_info
  @protocol_info.setter
  def protocol_info(self, protocol_info: dict[str, dict[str, Any]]):
    self._protocol_info = protocol_info

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
    return ChannelItem(**json.loads(json_string))
