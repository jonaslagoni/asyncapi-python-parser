from .MessageBindingsObjectKafkaBindingVersion import MessageBindingsObjectKafkaBindingVersion
from .Reference import Reference
from .SchemaObject import SchemaObject
from .PrimitiveType import PrimitiveType
from .PrimitiveTypeWithMetadata import PrimitiveTypeWithMetadata
from .Record import Record
from .Enum import Enum
from .Array import Array
from .Map import Map
from .Fixed import Fixed
from .BindingsMinusKafkaMinus0Dot4Dot0MinusMessageSchemaIdLocation import BindingsMinusKafkaMinus0Dot4Dot0MinusMessageSchemaIdLocation
import json
from typing import Any, List, Dict
class MessageBindingsObjectKafka: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: MessageBindingsObjectKafkaBindingVersion = MessageBindingsObjectKafkaBindingVersion(input['binding_version'])
    if hasattr(input, 'key'):
      self._key: Reference | SchemaObject | bool | PrimitiveType | PrimitiveTypeWithMetadata | Any | Record | Enum | Array | Map | Fixed | List[] = input['key']
    if hasattr(input, 'schema_id_location'):
      self._schema_id_location: BindingsMinusKafkaMinus0Dot4Dot0MinusMessageSchemaIdLocation = BindingsMinusKafkaMinus0Dot4Dot0MinusMessageSchemaIdLocation(input['schema_id_location'])
    if hasattr(input, 'schema_id_payload_encoding'):
      self._schema_id_payload_encoding: str = input['schema_id_payload_encoding']
    if hasattr(input, 'schema_lookup_strategy'):
      self._schema_lookup_strategy: str = input['schema_lookup_strategy']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> MessageBindingsObjectKafkaBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: MessageBindingsObjectKafkaBindingVersion):
    self._binding_version = binding_version

  @property
  def key(self) -> Reference | SchemaObject | bool | PrimitiveType | PrimitiveTypeWithMetadata | Any | Record | Enum | Array | Map | Fixed | List[]:
    return self._key
  @key.setter
  def key(self, key: Reference | SchemaObject | bool | PrimitiveType | PrimitiveTypeWithMetadata | Any | Record | Enum | Array | Map | Fixed | List[]):
    self._key = key

  @property
  def schema_id_location(self) -> BindingsMinusKafkaMinus0Dot4Dot0MinusMessageSchemaIdLocation:
    return self._schema_id_location
  @schema_id_location.setter
  def schema_id_location(self, schema_id_location: BindingsMinusKafkaMinus0Dot4Dot0MinusMessageSchemaIdLocation):
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
