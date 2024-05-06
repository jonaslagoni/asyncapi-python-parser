from __future__ import annotations
import json
from typing import Any, List, Dict
from . import BindingsMinusSqsMinus0Dot2Dot0MinusOperationBindingVersion
from . import OperationSchema
class OperationBindingsObjectSqs: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: BindingsMinusSqsMinus0Dot2Dot0MinusOperationBindingVersion.BindingsMinusSqsMinus0Dot2Dot0MinusOperationBindingVersion = BindingsMinusSqsMinus0Dot2Dot0MinusOperationBindingVersion.BindingsMinusSqsMinus0Dot2Dot0MinusOperationBindingVersion(input['binding_version'])
    if 'queues' in input:
      self._queues: List[OperationSchema.OperationSchema] = input['queues']
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def binding_version(self) -> BindingsMinusSqsMinus0Dot2Dot0MinusOperationBindingVersion.BindingsMinusSqsMinus0Dot2Dot0MinusOperationBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: BindingsMinusSqsMinus0Dot2Dot0MinusOperationBindingVersion.BindingsMinusSqsMinus0Dot2Dot0MinusOperationBindingVersion):
    self._binding_version = binding_version

  @property
  def queues(self) -> List[OperationSchema.OperationSchema]:
    return self._queues
  @queues.setter
  def queues(self, queues: List[OperationSchema.OperationSchema]):
    self._queues = queues

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
    return OperationBindingsObjectSqs(**json.loads(json_string))
