from .ChannelBindingsObjectPulsarBindingVersion import ChannelBindingsObjectPulsarBindingVersion
from .BindingsMinusPulsarMinus0Dot1Dot0MinusChannelPersistence import BindingsMinusPulsarMinus0Dot1Dot0MinusChannelPersistence
from .BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention import BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention
import json
from typing import List, Any, Dict
class ChannelBindingsObjectPulsar: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: ChannelBindingsObjectPulsarBindingVersion = ChannelBindingsObjectPulsarBindingVersion(input['binding_version'])
    if hasattr(input, 'namespace'):
      self._namespace: str = input['namespace']
    if hasattr(input, 'persistence'):
      self._persistence: BindingsMinusPulsarMinus0Dot1Dot0MinusChannelPersistence = BindingsMinusPulsarMinus0Dot1Dot0MinusChannelPersistence(input['persistence'])
    if hasattr(input, 'compaction'):
      self._compaction: int = input['compaction']
    if hasattr(input, 'geo_minus_replication'):
      self._geo_minus_replication: List[str] = input['geo_minus_replication']
    if hasattr(input, 'retention'):
      self._retention: BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention = BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention(input['retention'])
    if hasattr(input, 'ttl'):
      self._ttl: int = input['ttl']
    if hasattr(input, 'deduplication'):
      self._deduplication: bool = input['deduplication']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> ChannelBindingsObjectPulsarBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ChannelBindingsObjectPulsarBindingVersion):
    self._binding_version = binding_version

  @property
  def namespace(self) -> str:
    return self._namespace
  @namespace.setter
  def namespace(self, namespace: str):
    self._namespace = namespace

  @property
  def persistence(self) -> BindingsMinusPulsarMinus0Dot1Dot0MinusChannelPersistence:
    return self._persistence
  @persistence.setter
  def persistence(self, persistence: BindingsMinusPulsarMinus0Dot1Dot0MinusChannelPersistence):
    self._persistence = persistence

  @property
  def compaction(self) -> int:
    return self._compaction
  @compaction.setter
  def compaction(self, compaction: int):
    self._compaction = compaction

  @property
  def geo_minus_replication(self) -> List[str]:
    return self._geo_minus_replication
  @geo_minus_replication.setter
  def geo_minus_replication(self, geo_minus_replication: List[str]):
    self._geo_minus_replication = geo_minus_replication

  @property
  def retention(self) -> BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention:
    return self._retention
  @retention.setter
  def retention(self, retention: BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention):
    self._retention = retention

  @property
  def ttl(self) -> int:
    return self._ttl
  @ttl.setter
  def ttl(self, ttl: int):
    self._ttl = ttl

  @property
  def deduplication(self) -> bool:
    return self._deduplication
  @deduplication.setter
  def deduplication(self, deduplication: bool):
    self._deduplication = deduplication

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
    return ChannelBindingsObjectPulsar(**json.loads(json_string))
