from .OperationSchema import OperationSchema
import json
from typing import Any, List, Dict
class OperationBindingsObjectSns: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: str = input['binding_version']
    if hasattr(input, 'topic'):
      self._topic: OperationSchema = OperationSchema(input['topic'])
    if hasattr(input, 'consumers'):
      self._consumers: List[OperationSchema] = input['consumers']
    if hasattr(input, 'delivery_policy'):
      self._delivery_policy: OperationSchema = OperationSchema(input['delivery_policy'])
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> str:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: str):
    self._binding_version = binding_version

  @property
  def topic(self) -> OperationSchema:
    return self._topic
  @topic.setter
  def topic(self, topic: OperationSchema):
    self._topic = topic

  @property
  def consumers(self) -> List[OperationSchema]:
    return self._consumers
  @consumers.setter
  def consumers(self, consumers: List[OperationSchema]):
    self._consumers = consumers

  @property
  def delivery_policy(self) -> OperationSchema:
    return self._delivery_policy
  @delivery_policy.setter
  def delivery_policy(self, delivery_policy: OperationSchema):
    self._delivery_policy = delivery_policy

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
    return OperationBindingsObjectSns(**json.loads(json_string))
