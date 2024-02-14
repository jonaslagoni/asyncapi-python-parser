from .OperationBindingsObjectAmqpBindingVersion import OperationBindingsObjectAmqpBindingVersion
from .BindingsMinusAmqpMinus0Dot3Dot0MinusOperationDeliveryMode import BindingsMinusAmqpMinus0Dot3Dot0MinusOperationDeliveryMode
import json
from typing import List, Any, Dict
class OperationBindingsObjectAmqp: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: OperationBindingsObjectAmqpBindingVersion = OperationBindingsObjectAmqpBindingVersion(input['binding_version'])
    if hasattr(input, 'expiration'):
      self._expiration: int = input['expiration']
    if hasattr(input, 'user_id'):
      self._user_id: str = input['user_id']
    if hasattr(input, 'cc'):
      self._cc: List[str] = input['cc']
    if hasattr(input, 'priority'):
      self._priority: int = input['priority']
    if hasattr(input, 'delivery_mode'):
      self._delivery_mode: BindingsMinusAmqpMinus0Dot3Dot0MinusOperationDeliveryMode = BindingsMinusAmqpMinus0Dot3Dot0MinusOperationDeliveryMode(input['delivery_mode'])
    if hasattr(input, 'mandatory'):
      self._mandatory: bool = input['mandatory']
    if hasattr(input, 'bcc'):
      self._bcc: List[str] = input['bcc']
    if hasattr(input, 'timestamp'):
      self._timestamp: bool = input['timestamp']
    if hasattr(input, 'ack'):
      self._ack: bool = input['ack']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> OperationBindingsObjectAmqpBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: OperationBindingsObjectAmqpBindingVersion):
    self._binding_version = binding_version

  @property
  def expiration(self) -> int:
    return self._expiration
  @expiration.setter
  def expiration(self, expiration: int):
    self._expiration = expiration

  @property
  def user_id(self) -> str:
    return self._user_id
  @user_id.setter
  def user_id(self, user_id: str):
    self._user_id = user_id

  @property
  def cc(self) -> List[str]:
    return self._cc
  @cc.setter
  def cc(self, cc: List[str]):
    self._cc = cc

  @property
  def priority(self) -> int:
    return self._priority
  @priority.setter
  def priority(self, priority: int):
    self._priority = priority

  @property
  def delivery_mode(self) -> BindingsMinusAmqpMinus0Dot3Dot0MinusOperationDeliveryMode:
    return self._delivery_mode
  @delivery_mode.setter
  def delivery_mode(self, delivery_mode: BindingsMinusAmqpMinus0Dot3Dot0MinusOperationDeliveryMode):
    self._delivery_mode = delivery_mode

  @property
  def mandatory(self) -> bool:
    return self._mandatory
  @mandatory.setter
  def mandatory(self, mandatory: bool):
    self._mandatory = mandatory

  @property
  def bcc(self) -> List[str]:
    return self._bcc
  @bcc.setter
  def bcc(self, bcc: List[str]):
    self._bcc = bcc

  @property
  def timestamp(self) -> bool:
    return self._timestamp
  @timestamp.setter
  def timestamp(self, timestamp: bool):
    self._timestamp = timestamp

  @property
  def ack(self) -> bool:
    return self._ack
  @ack.setter
  def ack(self, ack: bool):
    self._ack = ack

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
    return OperationBindingsObjectAmqp(**json.loads(json_string))
