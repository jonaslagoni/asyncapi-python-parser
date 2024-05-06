from __future__ import annotations
import json
from typing import Any, List, Dict
from . import ServerBindingsObjectMqttBindingVersion
from . import BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill
from . import SchemaObject
from . import Reference
class ServerBindingsObjectMqtt: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: ServerBindingsObjectMqttBindingVersion.ServerBindingsObjectMqttBindingVersion = ServerBindingsObjectMqttBindingVersion.ServerBindingsObjectMqttBindingVersion(input['binding_version'])
    if 'client_id' in input:
      self._client_id: str = input['client_id']
    if 'clean_session' in input:
      self._clean_session: bool = input['clean_session']
    if 'last_will' in input:
      self._last_will: BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill.BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill = BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill.BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill(input['last_will'])
    if 'keep_alive' in input:
      self._keep_alive: int = input['keep_alive']
    if 'session_expiry_interval' in input:
      self._session_expiry_interval: int | SchemaObject.SchemaObject | bool | Reference.Reference = input['session_expiry_interval']
    if 'maximum_packet_size' in input:
      self._maximum_packet_size: int | SchemaObject.SchemaObject | bool | Reference.Reference = input['maximum_packet_size']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def binding_version(self) -> ServerBindingsObjectMqttBindingVersion.ServerBindingsObjectMqttBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ServerBindingsObjectMqttBindingVersion.ServerBindingsObjectMqttBindingVersion):
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
  def last_will(self) -> BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill.BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill:
    return self._last_will
  @last_will.setter
  def last_will(self, last_will: BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill.BindingsMinusMqttMinus0Dot2Dot0MinusServerLastWill):
    self._last_will = last_will

  @property
  def keep_alive(self) -> int:
    return self._keep_alive
  @keep_alive.setter
  def keep_alive(self, keep_alive: int):
    self._keep_alive = keep_alive

  @property
  def session_expiry_interval(self) -> int | SchemaObject.SchemaObject | bool | Reference.Reference:
    return self._session_expiry_interval
  @session_expiry_interval.setter
  def session_expiry_interval(self, session_expiry_interval: int | SchemaObject.SchemaObject | bool | Reference.Reference):
    self._session_expiry_interval = session_expiry_interval

  @property
  def maximum_packet_size(self) -> int | SchemaObject.SchemaObject | bool | Reference.Reference:
    return self._maximum_packet_size
  @maximum_packet_size.setter
  def maximum_packet_size(self, maximum_packet_size: int | SchemaObject.SchemaObject | bool | Reference.Reference):
    self._maximum_packet_size = maximum_packet_size

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
    return ServerBindingsObjectMqtt(**json.loads(json_string))
