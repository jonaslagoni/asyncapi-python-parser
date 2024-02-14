from .ChannelBindingsObjectWsBindingVersion import ChannelBindingsObjectWsBindingVersion
from .BindingsMinusWebsocketsMinus0Dot1Dot0MinusChannelMethod import BindingsMinusWebsocketsMinus0Dot1Dot0MinusChannelMethod
from .SchemaObject import SchemaObject
from .Reference import Reference
import json
from typing import Any, List, Dict
class ChannelBindingsObjectWs: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: ChannelBindingsObjectWsBindingVersion = ChannelBindingsObjectWsBindingVersion(input['binding_version'])
    if hasattr(input, 'method'):
      self._method: BindingsMinusWebsocketsMinus0Dot1Dot0MinusChannelMethod = BindingsMinusWebsocketsMinus0Dot1Dot0MinusChannelMethod(input['method'])
    if hasattr(input, 'query'):
      self._query: SchemaObject | bool | Reference = input['query']
    if hasattr(input, 'headers'):
      self._headers: SchemaObject | bool | Reference = input['headers']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> ChannelBindingsObjectWsBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: ChannelBindingsObjectWsBindingVersion):
    self._binding_version = binding_version

  @property
  def method(self) -> BindingsMinusWebsocketsMinus0Dot1Dot0MinusChannelMethod:
    return self._method
  @method.setter
  def method(self, method: BindingsMinusWebsocketsMinus0Dot1Dot0MinusChannelMethod):
    self._method = method

  @property
  def query(self) -> SchemaObject | bool | Reference:
    return self._query
  @query.setter
  def query(self, query: SchemaObject | bool | Reference):
    self._query = query

  @property
  def headers(self) -> SchemaObject | bool | Reference:
    return self._headers
  @headers.setter
  def headers(self, headers: SchemaObject | bool | Reference):
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
