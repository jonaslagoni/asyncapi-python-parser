from .OperationBindingsObjectHttpBindingVersion import OperationBindingsObjectHttpBindingVersion
from .BindingsMinusHttpMinus0Dot2Dot0MinusOperationMethod import BindingsMinusHttpMinus0Dot2Dot0MinusOperationMethod
from .SchemaObject import SchemaObject
import json
from typing import Any, List, Dict
class OperationBindingsObjectHttp: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: OperationBindingsObjectHttpBindingVersion = OperationBindingsObjectHttpBindingVersion(input['binding_version'])
    if hasattr(input, 'method'):
      self._method: BindingsMinusHttpMinus0Dot2Dot0MinusOperationMethod = BindingsMinusHttpMinus0Dot2Dot0MinusOperationMethod(input['method'])
    if hasattr(input, 'query'):
      self._query: SchemaObject | bool = input['query']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> OperationBindingsObjectHttpBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: OperationBindingsObjectHttpBindingVersion):
    self._binding_version = binding_version

  @property
  def method(self) -> BindingsMinusHttpMinus0Dot2Dot0MinusOperationMethod:
    return self._method
  @method.setter
  def method(self, method: BindingsMinusHttpMinus0Dot2Dot0MinusOperationMethod):
    self._method = method

  @property
  def query(self) -> SchemaObject | bool:
    return self._query
  @query.setter
  def query(self, query: SchemaObject | bool):
    self._query = query

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
    return OperationBindingsObjectHttp(**json.loads(json_string))
