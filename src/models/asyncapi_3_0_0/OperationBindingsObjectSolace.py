from .OperationBindingsObjectSolaceBindingVersion import OperationBindingsObjectSolaceBindingVersion
from .BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0 import BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0
from .BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf1 import BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf1
import json
from typing import List, Any, Dict
class OperationBindingsObjectSolace: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: OperationBindingsObjectSolaceBindingVersion = OperationBindingsObjectSolaceBindingVersion(input['binding_version'])
    if hasattr(input, 'destinations'):
      self._destinations: List[BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0 | BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf1] = input['destinations']

  @property
  def binding_version(self) -> OperationBindingsObjectSolaceBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: OperationBindingsObjectSolaceBindingVersion):
    self._binding_version = binding_version

  @property
  def destinations(self) -> List[BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0 | BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf1]:
    return self._destinations
  @destinations.setter
  def destinations(self, destinations: List[BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0 | BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf1]):
    self._destinations = destinations

  def serialize_to_json(self):
    return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=2)

  @staticmethod
  def deserialize_from_json(json_string):
    return OperationBindingsObjectSolace(**json.loads(json_string))
