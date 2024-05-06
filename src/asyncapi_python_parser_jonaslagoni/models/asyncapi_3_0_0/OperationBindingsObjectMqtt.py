from __future__ import annotations
import json
from typing import Any, List, Dict
from . import OperationBindingsObjectMqttBindingVersion
from . import BindingsMinusMqttMinus0Dot2Dot0MinusOperationQos
from . import SchemaObject
from . import Reference
class OperationBindingsObjectMqtt: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: OperationBindingsObjectMqttBindingVersion.OperationBindingsObjectMqttBindingVersion = OperationBindingsObjectMqttBindingVersion.OperationBindingsObjectMqttBindingVersion(input['binding_version'])
    if 'qos' in input:
      self._qos: BindingsMinusMqttMinus0Dot2Dot0MinusOperationQos.BindingsMinusMqttMinus0Dot2Dot0MinusOperationQos = BindingsMinusMqttMinus0Dot2Dot0MinusOperationQos.BindingsMinusMqttMinus0Dot2Dot0MinusOperationQos(input['qos'])
    if 'retain' in input:
      self._retain: bool = input['retain']
    if 'message_expiry_interval' in input:
      self._message_expiry_interval: int | SchemaObject.SchemaObject | bool | Reference.Reference = input['message_expiry_interval']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> OperationBindingsObjectMqttBindingVersion.OperationBindingsObjectMqttBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: OperationBindingsObjectMqttBindingVersion.OperationBindingsObjectMqttBindingVersion):
    self._binding_version = binding_version

  @property
  def qos(self) -> BindingsMinusMqttMinus0Dot2Dot0MinusOperationQos.BindingsMinusMqttMinus0Dot2Dot0MinusOperationQos:
    return self._qos
  @qos.setter
  def qos(self, qos: BindingsMinusMqttMinus0Dot2Dot0MinusOperationQos.BindingsMinusMqttMinus0Dot2Dot0MinusOperationQos):
    self._qos = qos

  @property
  def retain(self) -> bool:
    return self._retain
  @retain.setter
  def retain(self, retain: bool):
    self._retain = retain

  @property
  def message_expiry_interval(self) -> int | SchemaObject.SchemaObject | bool | Reference.Reference:
    return self._message_expiry_interval
  @message_expiry_interval.setter
  def message_expiry_interval(self, message_expiry_interval: int | SchemaObject.SchemaObject | bool | Reference.Reference):
    self._message_expiry_interval = message_expiry_interval

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
    return OperationBindingsObjectMqtt(**json.loads(json_string))
