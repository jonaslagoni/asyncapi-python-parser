from .ChannelBindingsObjectGooglepubsubBindingVersion import ChannelBindingsObjectGooglepubsubBindingVersion
from .BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy import BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy
from .BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings import BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings
import json
from typing import Any, List, Dict
class ChannelBindingsObjectGooglepubsub: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: ChannelBindingsObjectGooglepubsubBindingVersion = ChannelBindingsObjectGooglepubsubBindingVersion(input['binding_version'])
    if hasattr(input, 'labels'):
      self._labels: dict[str, Any] = input['labels']
    if hasattr(input, 'message_retention_duration'):
      self._message_retention_duration: str = input['message_retention_duration']
    if hasattr(input, 'message_storage_policy'):
      self._message_storage_policy: BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy = BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy(input['message_storage_policy'])
    if hasattr(input, 'schema_settings'):
      self._schema_settings: BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings = BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings(input['schema_settings'])
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> ChannelBindingsObjectGooglepubsubBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ChannelBindingsObjectGooglepubsubBindingVersion):
    self._binding_version = binding_version

  @property
  def labels(self) -> dict[str, Any]:
    return self._labels
  @labels.setter
  def labels(self, labels: dict[str, Any]):
    self._labels = labels

  @property
  def message_retention_duration(self) -> str:
    return self._message_retention_duration
  @message_retention_duration.setter
  def message_retention_duration(self, message_retention_duration: str):
    self._message_retention_duration = message_retention_duration

  @property
  def message_storage_policy(self) -> BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy:
    return self._message_storage_policy
  @message_storage_policy.setter
  def message_storage_policy(self, message_storage_policy: BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy):
    self._message_storage_policy = message_storage_policy

  @property
  def schema_settings(self) -> BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings:
    return self._schema_settings
  @schema_settings.setter
  def schema_settings(self, schema_settings: BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings):
    self._schema_settings = schema_settings

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
    return ChannelBindingsObjectGooglepubsub(**json.loads(json_string))
