from .OperationBindingsObjectMqttBindingVersion import OperationBindingsObjectMqttBindingVersion
from .BindingsMinusMqttMinus0Dot2Dot0MinusOperationQos import BindingsMinusMqttMinus0Dot2Dot0MinusOperationQos
from .SchemaObject import SchemaObject
from .Reference import Reference
import json
from typing import Any, List, Dict
class OperationBindingsObjectMqtt: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: OperationBindingsObjectMqttBindingVersion = OperationBindingsObjectMqttBindingVersion(input['binding_version'])
    if hasattr(input, 'qos'):
      self._qos: BindingsMinusMqttMinus0Dot2Dot0MinusOperationQos = BindingsMinusMqttMinus0Dot2Dot0MinusOperationQos(input['qos'])
    if hasattr(input, 'retain'):
      self._retain: bool = input['retain']
    if hasattr(input, 'message_expiry_interval'):
      self._message_expiry_interval: int | SchemaObject | bool | Reference = input['message_expiry_interval']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> OperationBindingsObjectMqttBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: OperationBindingsObjectMqttBindingVersion):
    self._binding_version = binding_version

  @property
  def qos(self) -> BindingsMinusMqttMinus0Dot2Dot0MinusOperationQos:
    return self._qos
  @qos.setter
  def qos(self, qos: BindingsMinusMqttMinus0Dot2Dot0MinusOperationQos):
    self._qos = qos

  @property
  def retain(self) -> bool:
    return self._retain
  @retain.setter
  def retain(self, retain: bool):
    self._retain = retain

  @property
  def message_expiry_interval(self) -> int | SchemaObject | bool | Reference:
    return self._message_expiry_interval
  @message_expiry_interval.setter
  def message_expiry_interval(self, message_expiry_interval: int | SchemaObject | bool | Reference):
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
