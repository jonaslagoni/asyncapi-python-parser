from __future__ import annotations
import json
from typing import Any, List, Dict
from . import Reference
from . import Parameter
from . import Operation
from . import BindingsObject
class ChannelItem: 
  def __init__(self, input: Dict):
    if 'dollar_ref' in input:
      self._dollar_ref: str = input['dollar_ref']
    if 'parameters' in input:
      self._parameters: dict[str, Reference.Reference | Parameter.Parameter] = input['parameters']
    if 'description' in input:
      self._description: str = input['description']
    if 'servers' in input:
      self._servers: List[str] = input['servers']
    if 'publish' in input:
      self._publish: Operation.Operation = Operation.Operation(input['publish'])
    if 'subscribe' in input:
      self._subscribe: Operation.Operation = Operation.Operation(input['subscribe'])
    if 'deprecated' in input:
      self._deprecated: bool = input['deprecated']
    if 'bindings' in input:
      self._bindings: BindingsObject.BindingsObject = BindingsObject.BindingsObject(input['bindings'])
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def dollar_ref(self) -> str:
    return self._dollar_ref
  @dollar_ref.setter
  def dollar_ref(self, dollar_ref: str):
    self._dollar_ref = dollar_ref

  @property
  def parameters(self) -> dict[str, Reference.Reference | Parameter.Parameter]:
    return self._parameters
  @parameters.setter
  def parameters(self, parameters: dict[str, Reference.Reference | Parameter.Parameter]):
    self._parameters = parameters

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

  @property
  def servers(self) -> List[str]:
    return self._servers
  @servers.setter
  def servers(self, servers: List[str]):
    self._servers = servers

  @property
  def publish(self) -> Operation.Operation:
    return self._publish
  @publish.setter
  def publish(self, publish: Operation.Operation):
    self._publish = publish

  @property
  def subscribe(self) -> Operation.Operation:
    return self._subscribe
  @subscribe.setter
  def subscribe(self, subscribe: Operation.Operation):
    self._subscribe = subscribe

  @property
  def deprecated(self) -> bool:
    return self._deprecated
  @deprecated.setter
  def deprecated(self, deprecated: bool):
    self._deprecated = deprecated

  @property
  def bindings(self) -> BindingsObject.BindingsObject:
    return self._bindings
  @bindings.setter
  def bindings(self, bindings: BindingsObject.BindingsObject):
    self._bindings = bindings

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
    return ChannelItem(**json.loads(json_string))
