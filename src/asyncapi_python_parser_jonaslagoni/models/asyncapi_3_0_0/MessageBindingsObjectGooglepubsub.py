from __future__ import annotations
import json
from typing import Any, Dict
from . import MessageBindingsObjectGooglepubsubBindingVersion
from . import BindingsMinusGooglepubsubMinus0Dot2Dot0MinusMessageSchema
class MessageBindingsObjectGooglepubsub: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: MessageBindingsObjectGooglepubsubBindingVersion.MessageBindingsObjectGooglepubsubBindingVersion = MessageBindingsObjectGooglepubsubBindingVersion.MessageBindingsObjectGooglepubsubBindingVersion(input['binding_version'])
    if 'attributes' in input:
      self._attributes: dict[str, Any] = input['attributes']
    if 'ordering_key' in input:
      self._ordering_key: str = input['ordering_key']
    if 'schema' in input:
      self._schema: BindingsMinusGooglepubsubMinus0Dot2Dot0MinusMessageSchema.BindingsMinusGooglepubsubMinus0Dot2Dot0MinusMessageSchema = BindingsMinusGooglepubsubMinus0Dot2Dot0MinusMessageSchema.BindingsMinusGooglepubsubMinus0Dot2Dot0MinusMessageSchema(input['schema'])
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def binding_version(self) -> MessageBindingsObjectGooglepubsubBindingVersion.MessageBindingsObjectGooglepubsubBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: MessageBindingsObjectGooglepubsubBindingVersion.MessageBindingsObjectGooglepubsubBindingVersion):
    self._binding_version = binding_version

  @property
  def attributes(self) -> dict[str, Any]:
    return self._attributes
  @attributes.setter
  def attributes(self, attributes: dict[str, Any]):
    self._attributes = attributes

  @property
  def ordering_key(self) -> str:
    return self._ordering_key
  @ordering_key.setter
  def ordering_key(self, ordering_key: str):
    self._ordering_key = ordering_key

  @property
  def schema(self) -> BindingsMinusGooglepubsubMinus0Dot2Dot0MinusMessageSchema.BindingsMinusGooglepubsubMinus0Dot2Dot0MinusMessageSchema:
    return self._schema
  @schema.setter
  def schema(self, schema: BindingsMinusGooglepubsubMinus0Dot2Dot0MinusMessageSchema.BindingsMinusGooglepubsubMinus0Dot2Dot0MinusMessageSchema):
    self._schema = schema

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
    return MessageBindingsObjectGooglepubsub(**json.loads(json_string))
