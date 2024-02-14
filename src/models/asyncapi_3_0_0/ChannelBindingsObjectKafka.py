from .ChannelBindingsObjectKafkaBindingVersion import ChannelBindingsObjectKafkaBindingVersion
from .BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration import BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration
import json
from typing import List, Any, Dict
class ChannelBindingsObjectKafka: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: ChannelBindingsObjectKafkaBindingVersion = ChannelBindingsObjectKafkaBindingVersion(input['binding_version'])
    if hasattr(input, 'topic'):
      self._topic: str = input['topic']
    if hasattr(input, 'partitions'):
      self._partitions: int = input['partitions']
    if hasattr(input, 'replicas'):
      self._replicas: int = input['replicas']
    if hasattr(input, 'topic_configuration'):
      self._topic_configuration: BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration = BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration(input['topic_configuration'])
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> ChannelBindingsObjectKafkaBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ChannelBindingsObjectKafkaBindingVersion):
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
  def topic_configuration(self) -> BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration:
    return self._topic_configuration
  @topic_configuration.setter
  def topic_configuration(self, topic_configuration: BindingsMinusKafkaMinus0Dot4Dot0MinusChannelTopicConfiguration):
    self._topic_configuration = topic_configuration

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
    return ChannelBindingsObjectKafka(**json.loads(json_string))
