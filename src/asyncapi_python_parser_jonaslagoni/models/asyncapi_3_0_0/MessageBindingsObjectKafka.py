from __future__ import annotations
import json
from typing import Any, List, Dict
from . import MessageBindingsObjectKafkaBindingVersion
from . import Reference
from . import SchemaObject
from . import PrimitiveType
from . import PrimitiveTypeWithMetadata
from . import Record
from . import Enum
from . import Array
from . import Map
from . import Fixed
from . import BindingsMinusKafkaMinus0Dot4Dot0MinusMessageSchemaIdLocation
class MessageBindingsObjectKafka: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: MessageBindingsObjectKafkaBindingVersion.MessageBindingsObjectKafkaBindingVersion = MessageBindingsObjectKafkaBindingVersion.MessageBindingsObjectKafkaBindingVersion(input['binding_version'])
    if 'key' in input:
      self._key: Reference.Reference | SchemaObject.SchemaObject | bool | PrimitiveType.PrimitiveType | PrimitiveTypeWithMetadata.PrimitiveTypeWithMetadata | Any | Record.Record | Enum.Enum | Array.Array | Map.Map | Fixed.Fixed | List[Any] = input['key']
    if 'schema_id_location' in input:
      self._schema_id_location: BindingsMinusKafkaMinus0Dot4Dot0MinusMessageSchemaIdLocation.BindingsMinusKafkaMinus0Dot4Dot0MinusMessageSchemaIdLocation = BindingsMinusKafkaMinus0Dot4Dot0MinusMessageSchemaIdLocation.BindingsMinusKafkaMinus0Dot4Dot0MinusMessageSchemaIdLocation(input['schema_id_location'])
    if 'schema_id_payload_encoding' in input:
      self._schema_id_payload_encoding: str = input['schema_id_payload_encoding']
    if 'schema_lookup_strategy' in input:
      self._schema_lookup_strategy: str = input['schema_lookup_strategy']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> MessageBindingsObjectKafkaBindingVersion.MessageBindingsObjectKafkaBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: MessageBindingsObjectKafkaBindingVersion.MessageBindingsObjectKafkaBindingVersion):
    self._binding_version = binding_version

  @property
  def key(self) -> Reference.Reference | SchemaObject.SchemaObject | bool | PrimitiveType.PrimitiveType | PrimitiveTypeWithMetadata.PrimitiveTypeWithMetadata | Any | Record.Record | Enum.Enum | Array.Array | Map.Map | Fixed.Fixed | List[Any]:
    return self._key
  @key.setter
  def key(self, key: Reference.Reference | SchemaObject.SchemaObject | bool | PrimitiveType.PrimitiveType | PrimitiveTypeWithMetadata.PrimitiveTypeWithMetadata | Any | Record.Record | Enum.Enum | Array.Array | Map.Map | Fixed.Fixed | List[Any]):
    self._key = key

  @property
  def schema_id_location(self) -> BindingsMinusKafkaMinus0Dot4Dot0MinusMessageSchemaIdLocation.BindingsMinusKafkaMinus0Dot4Dot0MinusMessageSchemaIdLocation:
    return self._schema_id_location
  @schema_id_location.setter
  def schema_id_location(self, schema_id_location: BindingsMinusKafkaMinus0Dot4Dot0MinusMessageSchemaIdLocation.BindingsMinusKafkaMinus0Dot4Dot0MinusMessageSchemaIdLocation):
    self._schema_id_location = schema_id_location

  @property
  def schema_id_payload_encoding(self) -> str:
    return self._schema_id_payload_encoding
  @schema_id_payload_encoding.setter
  def schema_id_payload_encoding(self, schema_id_payload_encoding: str):
    self._schema_id_payload_encoding = schema_id_payload_encoding

  @property
  def schema_lookup_strategy(self) -> str:
    return self._schema_lookup_strategy
  @schema_lookup_strategy.setter
  def schema_lookup_strategy(self, schema_lookup_strategy: str):
    self._schema_lookup_strategy = schema_lookup_strategy

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
    return MessageBindingsObjectKafka(**json.loads(json_string))
