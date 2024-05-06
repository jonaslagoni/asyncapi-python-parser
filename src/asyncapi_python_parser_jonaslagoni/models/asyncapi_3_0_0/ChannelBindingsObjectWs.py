from __future__ import annotations
import json
from typing import Any, List, Dict
from . import ChannelBindingsObjectWsBindingVersion
from . import BindingsMinusWebsocketsMinus0Dot1Dot0MinusChannelMethod
from . import SchemaObject
from . import Reference
class ChannelBindingsObjectWs: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: ChannelBindingsObjectWsBindingVersion.ChannelBindingsObjectWsBindingVersion = ChannelBindingsObjectWsBindingVersion.ChannelBindingsObjectWsBindingVersion(input['binding_version'])
    if 'method' in input:
      self._method: BindingsMinusWebsocketsMinus0Dot1Dot0MinusChannelMethod.BindingsMinusWebsocketsMinus0Dot1Dot0MinusChannelMethod = BindingsMinusWebsocketsMinus0Dot1Dot0MinusChannelMethod.BindingsMinusWebsocketsMinus0Dot1Dot0MinusChannelMethod(input['method'])
    if 'query' in input:
      self._query: SchemaObject.SchemaObject | bool | Reference.Reference = input['query']
    if 'headers' in input:
      self._headers: SchemaObject.SchemaObject | bool | Reference.Reference = input['headers']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> ChannelBindingsObjectWsBindingVersion.ChannelBindingsObjectWsBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ChannelBindingsObjectWsBindingVersion.ChannelBindingsObjectWsBindingVersion):
    self._binding_version = binding_version

  @property
  def method(self) -> BindingsMinusWebsocketsMinus0Dot1Dot0MinusChannelMethod.BindingsMinusWebsocketsMinus0Dot1Dot0MinusChannelMethod:
    return self._method
  @method.setter
  def method(self, method: BindingsMinusWebsocketsMinus0Dot1Dot0MinusChannelMethod.BindingsMinusWebsocketsMinus0Dot1Dot0MinusChannelMethod):
    self._method = method

  @property
  def query(self) -> SchemaObject.SchemaObject | bool | Reference.Reference:
    return self._query
  @query.setter
  def query(self, query: SchemaObject.SchemaObject | bool | Reference.Reference):
    self._query = query

  @property
  def headers(self) -> SchemaObject.SchemaObject | bool | Reference.Reference:
    return self._headers
  @headers.setter
  def headers(self, headers: SchemaObject.SchemaObject | bool | Reference.Reference):
    self._headers = headers

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
    return ChannelBindingsObjectWs(**json.loads(json_string))
