from __future__ import annotations
import json
from typing import Any, List, Dict
from . import ChannelBindingsObjectGooglepubsubBindingVersion
from . import BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy
from . import BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings
class ChannelBindingsObjectGooglepubsub: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: ChannelBindingsObjectGooglepubsubBindingVersion.ChannelBindingsObjectGooglepubsubBindingVersion = ChannelBindingsObjectGooglepubsubBindingVersion.ChannelBindingsObjectGooglepubsubBindingVersion(input['binding_version'])
    if 'labels' in input:
      self._labels: dict[str, Any] = input['labels']
    if 'message_retention_duration' in input:
      self._message_retention_duration: str = input['message_retention_duration']
    if 'message_storage_policy' in input:
      self._message_storage_policy: BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy.BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy = BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy.BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy(input['message_storage_policy'])
    if 'schema_settings' in input:
      self._schema_settings: BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings.BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings = BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings.BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings(input['schema_settings'])
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def binding_version(self) -> ChannelBindingsObjectGooglepubsubBindingVersion.ChannelBindingsObjectGooglepubsubBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ChannelBindingsObjectGooglepubsubBindingVersion.ChannelBindingsObjectGooglepubsubBindingVersion):
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
  def message_storage_policy(self) -> BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy.BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy:
    return self._message_storage_policy
  @message_storage_policy.setter
  def message_storage_policy(self, message_storage_policy: BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy.BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelMessageStoragePolicy):
    self._message_storage_policy = message_storage_policy

  @property
  def schema_settings(self) -> BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings.BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings:
    return self._schema_settings
  @schema_settings.setter
  def schema_settings(self, schema_settings: BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings.BindingsMinusGooglepubsubMinus0Dot2Dot0MinusChannelSchemaSettings):
    self._schema_settings = schema_settings

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
    return ChannelBindingsObjectGooglepubsub(**json.loads(json_string))
