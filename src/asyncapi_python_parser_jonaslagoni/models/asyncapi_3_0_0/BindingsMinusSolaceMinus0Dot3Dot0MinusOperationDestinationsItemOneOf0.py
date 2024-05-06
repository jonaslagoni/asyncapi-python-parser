from __future__ import annotations
import json
from typing import List, Any, Dict
from . import BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemDeliveryMode
from . import BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0Queue
class BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0: 
  def __init__(self, input: Dict):
    if 'delivery_mode' in input:
      self._delivery_mode: BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemDeliveryMode.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemDeliveryMode = BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemDeliveryMode.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemDeliveryMode(input['delivery_mode'])
    self._destination_type: str = 'queue'
    if 'queue' in input:
      self._queue: BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0Queue.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0Queue = BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0Queue.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0Queue(input['queue'])
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def delivery_mode(self) -> BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemDeliveryMode.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemDeliveryMode:
    return self._delivery_mode
  @delivery_mode.setter
  def delivery_mode(self, delivery_mode: BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemDeliveryMode.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemDeliveryMode):
    self._delivery_mode = delivery_mode

  @property
  def destination_type(self) -> str:
    return self._destination_type

  @property
  def queue(self) -> BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0Queue.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0Queue:
    return self._queue
  @queue.setter
  def queue(self, queue: BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0Queue.BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0Queue):
    self._queue = queue

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
    return BindingsMinusSolaceMinus0Dot3Dot0MinusOperationDestinationsItemOneOf0(**json.loads(json_string))