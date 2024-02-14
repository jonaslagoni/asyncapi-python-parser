from .BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfigurationCleanupDotPolicyItem import BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfigurationCleanupDotPolicyItem
import json
from typing import List, Dict
class BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration: 
  def __init__(self, input: Dict):
    if hasattr(input, 'cleanup_dot_policy'):
      self._cleanup_dot_policy: List[BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfigurationCleanupDotPolicyItem] = input['cleanup_dot_policy']
    if hasattr(input, 'retention_dot_ms'):
      self._retention_dot_ms: int = input['retention_dot_ms']
    if hasattr(input, 'retention_dot_bytes'):
      self._retention_dot_bytes: int = input['retention_dot_bytes']
    if hasattr(input, 'delete_dot_retention_dot_ms'):
      self._delete_dot_retention_dot_ms: int = input['delete_dot_retention_dot_ms']
    if hasattr(input, 'max_dot_message_dot_bytes'):
      self._max_dot_message_dot_bytes: int = input['max_dot_message_dot_bytes']

  @property
  def cleanup_dot_policy(self) -> List[BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfigurationCleanupDotPolicyItem]:
    return self._cleanup_dot_policy
  @cleanup_dot_policy.setter
  def cleanup_dot_policy(self, cleanup_dot_policy: List[BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfigurationCleanupDotPolicyItem]):
    self._cleanup_dot_policy = cleanup_dot_policy

  @property
  def retention_dot_ms(self) -> int:
    return self._retention_dot_ms
  @retention_dot_ms.setter
  def retention_dot_ms(self, retention_dot_ms: int):
    self._retention_dot_ms = retention_dot_ms

  @property
  def retention_dot_bytes(self) -> int:
    return self._retention_dot_bytes
  @retention_dot_bytes.setter
  def retention_dot_bytes(self, retention_dot_bytes: int):
    self._retention_dot_bytes = retention_dot_bytes

  @property
  def delete_dot_retention_dot_ms(self) -> int:
    return self._delete_dot_retention_dot_ms
  @delete_dot_retention_dot_ms.setter
  def delete_dot_retention_dot_ms(self, delete_dot_retention_dot_ms: int):
    self._delete_dot_retention_dot_ms = delete_dot_retention_dot_ms

  @property
  def max_dot_message_dot_bytes(self) -> int:
    return self._max_dot_message_dot_bytes
  @max_dot_message_dot_bytes.setter
  def max_dot_message_dot_bytes(self, max_dot_message_dot_bytes: int):
    self._max_dot_message_dot_bytes = max_dot_message_dot_bytes

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration(**json.loads(json_string))
