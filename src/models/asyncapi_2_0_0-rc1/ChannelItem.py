from .Reference import Reference
from .Parameter import Parameter
from .Operation import Operation
import json
from typing import Any, List, Dict
class ChannelItem: 
  def __init__(self, input: Dict):
    if hasattr(input, 'dollar_ref'):
      self._dollar_ref: str = input['dollar_ref']
    if hasattr(input, 'parameters'):
      self._parameters: dict[str, Reference | Parameter] = input['parameters']
    if hasattr(input, 'publish'):
      self._publish: Operation = Operation(input['publish'])
    if hasattr(input, 'subscribe'):
      self._subscribe: Operation = Operation(input['subscribe'])
    if hasattr(input, 'deprecated'):
      self._deprecated: bool = input['deprecated']
    if hasattr(input, 'protocol_info'):
      self._protocol_info: dict[str, dict[str, Any]] = input['protocol_info']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def dollar_ref(self) -> str:
    return self._dollar_ref
  @dollar_ref.setter
  def dollar_ref(self, dollar_ref: str):
    self._dollar_ref = dollar_ref

  @property
  def parameters(self) -> dict[str, Reference | Parameter]:
    return self._parameters
  @parameters.setter
  def parameters(self, parameters: dict[str, Reference | Parameter]):
    self._parameters = parameters

  @property
  def publish(self) -> Operation:
    return self._publish
  @publish.setter
  def publish(self, publish: Operation):
    self._publish = publish

  @property
  def subscribe(self) -> Operation:
    return self._subscribe
  @subscribe.setter
  def subscribe(self, subscribe: Operation):
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
  def additional_properties(self) -> dict[str, Any]:
    return self._additional_properties
  @additional_properties.setter
  def additional_properties(self, additional_properties: dict[str, Any]):
    self._additional_properties = additional_properties

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return ChannelItem(**json.loads(json_string))
