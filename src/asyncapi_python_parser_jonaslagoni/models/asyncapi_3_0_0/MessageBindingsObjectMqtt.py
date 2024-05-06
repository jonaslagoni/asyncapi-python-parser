from __future__ import annotations
import json
from typing import Any, List, Dict
from . import MessageBindingsObjectMqttBindingVersion
from . import BindingsMinusMqttMinus0Dot2Dot0MinusMessagePayloadFormatIndicator
from . import SchemaObject
from . import Reference
class MessageBindingsObjectMqtt: 
  def __init__(self, input: Dict):
    if 'binding_version' in input:
      self._binding_version: MessageBindingsObjectMqttBindingVersion.MessageBindingsObjectMqttBindingVersion = MessageBindingsObjectMqttBindingVersion.MessageBindingsObjectMqttBindingVersion(input['binding_version'])
    if 'payload_format_indicator' in input:
      self._payload_format_indicator: BindingsMinusMqttMinus0Dot2Dot0MinusMessagePayloadFormatIndicator.BindingsMinusMqttMinus0Dot2Dot0MinusMessagePayloadFormatIndicator = BindingsMinusMqttMinus0Dot2Dot0MinusMessagePayloadFormatIndicator.BindingsMinusMqttMinus0Dot2Dot0MinusMessagePayloadFormatIndicator(input['payload_format_indicator'])
    if 'correlation_data' in input:
      self._correlation_data: SchemaObject.SchemaObject | bool | Reference.Reference = input['correlation_data']
    if 'content_type' in input:
      self._content_type: str = input['content_type']
    if 'response_topic' in input:
      self._response_topic: str | SchemaObject.SchemaObject | bool | Reference.Reference = input['response_topic']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> MessageBindingsObjectMqttBindingVersion.MessageBindingsObjectMqttBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: MessageBindingsObjectMqttBindingVersion.MessageBindingsObjectMqttBindingVersion):
    self._binding_version = binding_version

  @property
  def payload_format_indicator(self) -> BindingsMinusMqttMinus0Dot2Dot0MinusMessagePayloadFormatIndicator.BindingsMinusMqttMinus0Dot2Dot0MinusMessagePayloadFormatIndicator:
    return self._payload_format_indicator
  @payload_format_indicator.setter
  def payload_format_indicator(self, payload_format_indicator: BindingsMinusMqttMinus0Dot2Dot0MinusMessagePayloadFormatIndicator.BindingsMinusMqttMinus0Dot2Dot0MinusMessagePayloadFormatIndicator):
    self._payload_format_indicator = payload_format_indicator

  @property
  def correlation_data(self) -> SchemaObject.SchemaObject | bool | Reference.Reference:
    return self._correlation_data
  @correlation_data.setter
  def correlation_data(self, correlation_data: SchemaObject.SchemaObject | bool | Reference.Reference):
    self._correlation_data = correlation_data

  @property
  def content_type(self) -> str:
    return self._content_type
  @content_type.setter
  def content_type(self, content_type: str):
    self._content_type = content_type

  @property
  def response_topic(self) -> str | SchemaObject.SchemaObject | bool | Reference.Reference:
    return self._response_topic
  @response_topic.setter
  def response_topic(self, response_topic: str | SchemaObject.SchemaObject | bool | Reference.Reference):
    self._response_topic = response_topic

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
    return MessageBindingsObjectMqtt(**json.loads(json_string))
