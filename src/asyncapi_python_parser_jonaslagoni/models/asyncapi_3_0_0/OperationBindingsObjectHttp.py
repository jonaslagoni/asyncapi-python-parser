from __future__ import annotations
import json
from typing import Any, List, Dict
from . import OperationBindingsObjectHttpBindingVersion
from . import BindingsMinusHttpMinus0Dot2Dot0MinusOperationMethod
from . import SchemaObject
class OperationBindingsObjectHttp: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: OperationBindingsObjectHttpBindingVersion.OperationBindingsObjectHttpBindingVersion = OperationBindingsObjectHttpBindingVersion.OperationBindingsObjectHttpBindingVersion(input['binding_version'])
    if 'method' in input:
      self._method: BindingsMinusHttpMinus0Dot2Dot0MinusOperationMethod.BindingsMinusHttpMinus0Dot2Dot0MinusOperationMethod = BindingsMinusHttpMinus0Dot2Dot0MinusOperationMethod.BindingsMinusHttpMinus0Dot2Dot0MinusOperationMethod(input['method'])
    if 'query' in input:
      self._query: SchemaObject.SchemaObject | bool = input['query']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def binding_version(self) -> OperationBindingsObjectHttpBindingVersion.OperationBindingsObjectHttpBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: OperationBindingsObjectHttpBindingVersion.OperationBindingsObjectHttpBindingVersion):
    self._binding_version = binding_version

  @property
  def method(self) -> BindingsMinusHttpMinus0Dot2Dot0MinusOperationMethod.BindingsMinusHttpMinus0Dot2Dot0MinusOperationMethod:
    return self._method
  @method.setter
  def method(self, method: BindingsMinusHttpMinus0Dot2Dot0MinusOperationMethod.BindingsMinusHttpMinus0Dot2Dot0MinusOperationMethod):
    self._method = method

  @property
  def query(self) -> SchemaObject.SchemaObject | bool:
    return self._query
  @query.setter
  def query(self, query: SchemaObject.SchemaObject | bool):
    self._query = query

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
    return OperationBindingsObjectHttp(**json.loads(json_string))
