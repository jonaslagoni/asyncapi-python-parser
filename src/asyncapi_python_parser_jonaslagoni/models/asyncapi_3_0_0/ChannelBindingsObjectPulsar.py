from __future__ import annotations
import json
from typing import List, Any, Dict
from . import ChannelBindingsObjectPulsarBindingVersion
from . import BindingsMinusPulsarMinus0Dot1Dot0MinusChannelPersistence
from . import BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention
class ChannelBindingsObjectPulsar: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: ChannelBindingsObjectPulsarBindingVersion.ChannelBindingsObjectPulsarBindingVersion = ChannelBindingsObjectPulsarBindingVersion.ChannelBindingsObjectPulsarBindingVersion(input['binding_version'])
    if 'namespace' in input:
      self._namespace: str = input['namespace']
    if 'persistence' in input:
      self._persistence: BindingsMinusPulsarMinus0Dot1Dot0MinusChannelPersistence.BindingsMinusPulsarMinus0Dot1Dot0MinusChannelPersistence = BindingsMinusPulsarMinus0Dot1Dot0MinusChannelPersistence.BindingsMinusPulsarMinus0Dot1Dot0MinusChannelPersistence(input['persistence'])
    if 'compaction' in input:
      self._compaction: int = input['compaction']
    if 'geo_replication' in input:
      self._geo_replication: List[str] = input['geo_replication']
    if 'retention' in input:
      self._retention: BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention.BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention = BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention.BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention(input['retention'])
    if 'ttl' in input:
      self._ttl: int = input['ttl']
    if 'deduplication' in input:
      self._deduplication: bool = input['deduplication']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> ChannelBindingsObjectPulsarBindingVersion.ChannelBindingsObjectPulsarBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ChannelBindingsObjectPulsarBindingVersion.ChannelBindingsObjectPulsarBindingVersion):
    self._binding_version = binding_version

  @property
  def namespace(self) -> str:
    return self._namespace
  @namespace.setter
  def namespace(self, namespace: str):
    self._namespace = namespace

  @property
  def persistence(self) -> BindingsMinusPulsarMinus0Dot1Dot0MinusChannelPersistence.BindingsMinusPulsarMinus0Dot1Dot0MinusChannelPersistence:
    return self._persistence
  @persistence.setter
  def persistence(self, persistence: BindingsMinusPulsarMinus0Dot1Dot0MinusChannelPersistence.BindingsMinusPulsarMinus0Dot1Dot0MinusChannelPersistence):
    self._persistence = persistence

  @property
  def compaction(self) -> int:
    return self._compaction
  @compaction.setter
  def compaction(self, compaction: int):
    self._compaction = compaction

  @property
  def geo_replication(self) -> List[str]:
    return self._geo_replication
  @geo_replication.setter
  def geo_replication(self, geo_replication: List[str]):
    self._geo_replication = geo_replication

  @property
  def retention(self) -> BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention.BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention:
    return self._retention
  @retention.setter
  def retention(self, retention: BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention.BindingsMinusPulsarMinus0Dot1Dot0MinusChannelRetention):
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
