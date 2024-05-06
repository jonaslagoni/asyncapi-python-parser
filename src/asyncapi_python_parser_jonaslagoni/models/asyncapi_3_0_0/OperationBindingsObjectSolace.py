from __future__ import annotations
import json
from typing import List, Any, Dict
from . import OperationBindingsObjectSolaceBindingVersion
from . import BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0
from . import BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf1
class OperationBindingsObjectSolace: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: OperationBindingsObjectSolaceBindingVersion.OperationBindingsObjectSolaceBindingVersion = OperationBindingsObjectSolaceBindingVersion.OperationBindingsObjectSolaceBindingVersion(input['binding_version'])
    if 'destinations' in input:
      self._destinations: List[BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0 | BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf1.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf1] = input['destinations']

  @property
  def binding_version(self) -> OperationBindingsObjectSolaceBindingVersion.OperationBindingsObjectSolaceBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: OperationBindingsObjectSolaceBindingVersion.OperationBindingsObjectSolaceBindingVersion):
    self._binding_version = binding_version

  @property
  def destinations(self) -> List[BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0 | BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf1.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf1]:
    return self._destinations
  @destinations.setter
  def destinations(self, destinations: List[BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0 | BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf1.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf1]):
    self._destinations = destinations

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return OperationBindingsObjectSolace(**json.loads(json_string))
