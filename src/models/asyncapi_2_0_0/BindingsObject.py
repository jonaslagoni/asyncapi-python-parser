from __future__ import annotations
import json
from typing import Any, Dict

class BindingsObject: 
  def __init__(self, input: Dict):
    if 'http' in input:
      self._http: Any = input['http']
    if 'ws' in input:
      self._ws: Any = input['ws']
    if 'amqp' in input:
      self._amqp: Any = input['amqp']
    if 'amqp1' in input:
      self._amqp1: Any = input['amqp1']
    if 'mqtt' in input:
      self._mqtt: Any = input['mqtt']
    if 'mqtt5' in input:
      self._mqtt5: Any = input['mqtt5']
    if 'kafka' in input:
      self._kafka: Any = input['kafka']
    if 'nats' in input:
      self._nats: Any = input['nats']
    if 'jms' in input:
      self._jms: Any = input['jms']
    if 'sns' in input:
      self._sns: Any = input['sns']
    if 'sqs' in input:
      self._sqs: Any = input['sqs']
    if 'stomp' in input:
      self._stomp: Any = input['stomp']
    if 'redis' in input:
      self._redis: Any = input['redis']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def http(self) -> Any:
    return self._http
  @http.setter
  def http(self, http: Any):
    self._http = http

  @property
  def ws(self) -> Any:
    return self._ws
  @ws.setter
  def ws(self, ws: Any):
    self._ws = ws

  @property
  def amqp(self) -> Any:
    return self._amqp
  @amqp.setter
  def amqp(self, amqp: Any):
    self._amqp = amqp

  @property
  def amqp1(self) -> Any:
    return self._amqp1
  @amqp1.setter
  def amqp1(self, amqp1: Any):
    self._amqp1 = amqp1

  @property
  def mqtt(self) -> Any:
    return self._mqtt
  @mqtt.setter
  def mqtt(self, mqtt: Any):
    self._mqtt = mqtt

  @property
  def mqtt5(self) -> Any:
    return self._mqtt5
  @mqtt5.setter
  def mqtt5(self, mqtt5: Any):
    self._mqtt5 = mqtt5

  @property
  def kafka(self) -> Any:
    return self._kafka
  @kafka.setter
  def kafka(self, kafka: Any):
    self._kafka = kafka

  @property
  def nats(self) -> Any:
    return self._nats
  @nats.setter
  def nats(self, nats: Any):
    self._nats = nats

  @property
  def jms(self) -> Any:
    return self._jms
  @jms.setter
  def jms(self, jms: Any):
    self._jms = jms

  @property
  def sns(self) -> Any:
    return self._sns
  @sns.setter
  def sns(self, sns: Any):
    self._sns = sns

  @property
  def sqs(self) -> Any:
    return self._sqs
  @sqs.setter
  def sqs(self, sqs: Any):
    self._sqs = sqs

  @property
  def stomp(self) -> Any:
    return self._stomp
  @stomp.setter
  def stomp(self, stomp: Any):
    self._stomp = stomp

  @property
  def redis(self) -> Any:
    return self._redis
  @redis.setter
  def redis(self, redis: Any):
    self._redis = redis

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
    return BindingsObject(**json.loads(json_string))
