from __future__ import annotations
import json
from typing import List, Any, Dict
from . import ChannelBindingsObjectKafkaBindingVersion
from . import BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration
class ChannelBindingsObjectKafka: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: ChannelBindingsObjectKafkaBindingVersion.ChannelBindingsObjectKafkaBindingVersion = ChannelBindingsObjectKafkaBindingVersion.ChannelBindingsObjectKafkaBindingVersion(input['binding_version'])
    if 'topic' in input:
      self._topic: str = input['topic']
    if 'partitions' in input:
      self._partitions: int = input['partitions']
    if 'replicas' in input:
      self._replicas: int = input['replicas']
    if 'topic_configuration' in input:
      self._topic_configuration: BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration.BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration = BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration.BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration(input['topic_configuration'])
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def binding_version(self) -> ChannelBindingsObjectKafkaBindingVersion.ChannelBindingsObjectKafkaBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ChannelBindingsObjectKafkaBindingVersion.ChannelBindingsObjectKafkaBindingVersion):
    self._binding_version = binding_version

  @property
  def topic(self) -> str:
    return self._topic
  @topic.setter
  def topic(self, topic: str):
    self._topic = topic

  @property
  def partitions(self) -> int:
    return self._partitions
  @partitions.setter
  def partitions(self, partitions: int):
    self._partitions = partitions

  @property
  def replicas(self) -> int:
    return self._replicas
  @replicas.setter
  def replicas(self, replicas: int):
    self._replicas = replicas

  @property
  def topic_configuration(self) -> BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration.BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration:
    return self._topic_configuration
  @topic_configuration.setter
  def topic_configuration(self, topic_configuration: BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration.BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration):
    self._topic_configuration = topic_configuration

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
    return ChannelBindingsObjectKafka(**json.loads(json_string))
