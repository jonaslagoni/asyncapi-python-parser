from .MessageBindingsObjectMqttBindingVersion import MessageBindingsObjectMqttBindingVersion
from .BindingsMinusMqttMinus0Dot2Dot0MinusMessagePayloadFormatIndicator import BindingsMinusMqttMinus0Dot2Dot0MinusMessagePayloadFormatIndicator
from .SchemaObject import SchemaObject
from .Reference import Reference
import json
from typing import Any, List, Dict
class MessageBindingsObjectMqtt: 
  def __init__(self, input: Dict):
    if hasattr(input, 'binding_version'):
      self._binding_version: MessageBindingsObjectMqttBindingVersion = MessageBindingsObjectMqttBindingVersion(input['binding_version'])
    if hasattr(input, 'payload_format_indicator'):
      self._payload_format_indicator: BindingsMinusMqttMinus0Dot2Dot0MinusMessagePayloadFormatIndicator = BindingsMinusMqttMinus0Dot2Dot0MinusMessagePayloadFormatIndicator(input['payload_format_indicator'])
    if hasattr(input, 'correlation_data'):
      self._correlation_data: SchemaObject | bool | Reference = input['correlation_data']
    if hasattr(input, 'content_type'):
      self._content_type: str = input['content_type']
    if hasattr(input, 'response_topic'):
      self._response_topic: str | SchemaObject | bool | Reference = input['response_topic']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def binding_version(self) -> MessageBindingsObjectMqttBindingVersion:
    return self._binding_version
  @binding_version.setter
  def binding_version(self, binding_version: MessageBindingsObjectMqttBindingVersion):
    self._binding_version = binding_version

  @property
  def payload_format_indicator(self) -> BindingsMinusMqttMinus0Dot2Dot0MinusMessagePayloadFormatIndicator:
    return self._payload_format_indicator
  @payload_format_indicator.setter
  def payload_format_indicator(self, payload_format_indicator: BindingsMinusMqttMinus0Dot2Dot0MinusMessagePayloadFormatIndicator):
    self._payload_format_indicator = payload_format_indicator

  @property
  def correlation_data(self) -> SchemaObject | bool | Reference:
    return self._correlation_data
  @correlation_data.setter
  def correlation_data(self, correlation_data: SchemaObject | bool | Reference):
    self._correlation_data = correlation_data

  @property
  def content_type(self) -> str:
    return self._content_type
  @content_type.setter
  def content_type(self, content_type: str):
    self._content_type = content_type

  @property
  def response_topic(self) -> str | SchemaObject | bool | Reference:
    return self._response_topic
  @response_topic.setter
  def response_topic(self, response_topic: str | SchemaObject | bool | Reference):
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
