from __future__ import annotations
import json
from typing import Any, Dict
from . import Oauth2FlowsType
from . import Oauth2FlowsFlows
class Oauth2Flows: 
  def __init__(self, input: Dict):
    self._type: Oauth2FlowsType.Oauth2FlowsType = Oauth2FlowsType.Oauth2FlowsType(input['type'])
    if 'description' in input:
      self._description: str = input['description']
    self._flows: Oauth2FlowsFlows.Oauth2FlowsFlows = Oauth2FlowsFlows.Oauth2FlowsFlows(input['flows'])
    if 'extensions' in input:
      self._extensions: dict[str, Any | Any] = input['extensions']

  @property
  def type(self) -> Oauth2FlowsType.Oauth2FlowsType:
    return self._type
  @type.setter
  def type(self, type: Oauth2FlowsType.Oauth2FlowsType):
    self._type = type

  @property
  def description(self) -> str:
    return self._description
  @description.setter
  def description(self, description: str):
    self._description = description

  @property
  def flows(self) -> Oauth2FlowsFlows.Oauth2FlowsFlows:
    return self._flows
  @flows.setter
  def flows(self, flows: Oauth2FlowsFlows.Oauth2FlowsFlows):
    self._flows = flows

  @property
  def extensions(self) -> dict[str, Any | Any]:
    return self._extensions
  @extensions.setter
  def extensions(self, extensions: dict[str, Any | Any]):
    self._extensions = extensions

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return Oauth2Flows(**json.loads(json_string))
