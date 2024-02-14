from .ServerBindingsObjectMqttBindingVersion import ServerBindingsObjectMqttBindingVersion
from .BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill import BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill
from .SchemaObject import SchemaObject
from .Reference import Reference
import json
from typing import Any, List, Dict
class ServerBindingsObjectMqtt: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: ServerBindingsObjectMqttBindingVersion = ServerBindingsObjectMqttBindingVersion(input['binding_version'])
    if hasattr(input, 'client_id'):
      self._client_id: str = input['client_id']
    if hasattr(input, 'clean_session'):
      self._clean_session: bool = input['clean_session']
    if hasattr(input, 'last_will'):
      self._last_will: BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill = BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill(input['last_will'])
    if hasattr(input, 'keep_alive'):
      self._keep_alive: int = input['keep_alive']
    if hasattr(input, 'session_expiry_interval'):
      self._session_expiry_interval: int | SchemaObject | bool | Reference = input['session_expiry_interval']
    if hasattr(input, 'maximum_packet_size'):
      self._maximum_packet_size: int | SchemaObject | bool | Reference = input['maximum_packet_size']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> ServerBindingsObjectMqttBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ServerBindingsObjectMqttBindingVersion):
    self._binding_version = binding_version

  @property
  def client_id(self) -> str:
    return self._client_id
  @client_id.setter
  def client_id(self, client_id: str):
    self._client_id = client_id

  @property
  def clean_session(self) -> bool:
    return self._clean_session
  @clean_session.setter
  def clean_session(self, clean_session: bool):
    self._clean_session = clean_session

  @property
  def last_will(self) -> BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill:
    return self._last_will
  @last_will.setter
  def last_will(self, last_will: BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill):
    self._last_will = last_will

  @property
  def keep_alive(self) -> int:
    return self._keep_alive
  @keep_alive.setter
  def keep_alive(self, keep_alive: int):
    self._keep_alive = keep_alive

  @property
  def session_expiry_interval(self) -> int | SchemaObject | bool | Reference:
    return self._session_expiry_interval
  @session_expiry_interval.setter
  def session_expiry_interval(self, session_expiry_interval: int | SchemaObject | bool | Reference):
    self._session_expiry_interval = session_expiry_interval

  @property
  def maximum_packet_size(self) -> int | SchemaObject | bool | Reference:
    return self._maximum_packet_size
  @maximum_packet_size.setter
  def maximum_packet_size(self, maximum_packet_size: int | SchemaObject | bool | Reference):
    self._maximum_packet_size = maximum_packet_size

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
    return ServerBindingsObjectMqtt(**json.loads(json_string))
