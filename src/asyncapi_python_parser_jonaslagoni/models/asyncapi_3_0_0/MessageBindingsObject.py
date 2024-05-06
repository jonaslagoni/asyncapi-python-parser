from __future__ import annotations
import json
from typing import Any, List, Dict
from . import MessageBindingsObjectHttp
from . import MessageBindingsObjectAmqp
from . import MessageBindingsObjectMqtt
from . import MessageBindingsObjectKafka
from . import MessageBindingsObjectAnypointmq
from . import MessageBindingsObjectJms
from . import MessageBindingsObjectIbmmq
from . import MessageBindingsObjectGooglepubsub
class MessageBindingsObject: 
  def __init__(self, input: Dict):
    if 'http' in input:
      self._http: MessageBindingsObjectHttp.MessageBindingsObjectHttp = MessageBindingsObjectHttp.MessageBindingsObjectHttp(input['http'])
    if 'ws' in input:
      self._ws: Any = input['ws']
    if 'amqp' in input:
      self._amqp: MessageBindingsObjectAmqp.MessageBindingsObjectAmqp = MessageBindingsObjectAmqp.MessageBindingsObjectAmqp(input['amqp'])
    if 'amqp1' in input:
      self._amqp1: Any = input['amqp1']
    if 'mqtt' in input:
      self._mqtt: MessageBindingsObjectMqtt.MessageBindingsObjectMqtt = MessageBindingsObjectMqtt.MessageBindingsObjectMqtt(input['mqtt'])
    if 'kafka' in input:
      self._kafka: MessageBindingsObjectKafka.MessageBindingsObjectKafka = MessageBindingsObjectKafka.MessageBindingsObjectKafka(input['kafka'])
    if 'anypointmq' in input:
      self._anypointmq: MessageBindingsObjectAnypointmq.MessageBindingsObjectAnypointmq = MessageBindingsObjectAnypointmq.MessageBindingsObjectAnypointmq(input['anypointmq'])
    if 'nats' in input:
      self._nats: Any = input['nats']
    if 'jms' in input:
      self._jms: MessageBindingsObjectJms.MessageBindingsObjectJms = MessageBindingsObjectJms.MessageBindingsObjectJms(input['jms'])
    if 'sns' in input:
      self._sns: Any = input['sns']
    if 'sqs' in input:
      self._sqs: Any = input['sqs']
    if 'stomp' in input:
      self._stomp: Any = input['stomp']
    if 'redis' in input:
      self._redis: Any = input['redis']
    if 'ibmmq' in input:
      self._ibmmq: MessageBindingsObjectIbmmq.MessageBindingsObjectIbmmq = MessageBindingsObjectIbmmq.MessageBindingsObjectIbmmq(input['ibmmq'])
    if 'solace' in input:
      self._solace: Any = input['solace']
    if 'googlepubsub' in input:
      self._googlepubsub: MessageBindingsObjectGooglepubsub.MessageBindingsObjectGooglepubsub = MessageBindingsObjectGooglepubsub.MessageBindingsObjectGooglepubsub(input['googlepubsub'])
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def http(self) -> MessageBindingsObjectHttp.MessageBindingsObjectHttp:
    return self._http
  @http.setter
  def http(self, http: MessageBindingsObjectHttp.MessageBindingsObjectHttp):
    self._http = http

  @property
  def ws(self) -> Any:
    return self._ws
  @ws.setter
  def ws(self, ws: Any):
    self._ws = ws

  @property
  def amqp(self) -> MessageBindingsObjectAmqp.MessageBindingsObjectAmqp:
    return self._amqp
  @amqp.setter
  def amqp(self, amqp: MessageBindingsObjectAmqp.MessageBindingsObjectAmqp):
    self._amqp = amqp

  @property
  def amqp1(self) -> Any:
    return self._amqp1
  @amqp1.setter
  def amqp1(self, amqp1: Any):
    self._amqp1 = amqp1

  @property
  def mqtt(self) -> MessageBindingsObjectMqtt.MessageBindingsObjectMqtt:
    return self._mqtt
  @mqtt.setter
  def mqtt(self, mqtt: MessageBindingsObjectMqtt.MessageBindingsObjectMqtt):
    self._mqtt = mqtt

  @property
  def kafka(self) -> MessageBindingsObjectKafka.MessageBindingsObjectKafka:
    return self._kafka
  @kafka.setter
  def kafka(self, kafka: MessageBindingsObjectKafka.MessageBindingsObjectKafka):
    self._kafka = kafka

  @property
  def anypointmq(self) -> MessageBindingsObjectAnypointmq.MessageBindingsObjectAnypointmq:
    return self._anypointmq
  @anypointmq.setter
  def anypointmq(self, anypointmq: MessageBindingsObjectAnypointmq.MessageBindingsObjectAnypointmq):
    self._anypointmq = anypointmq

  @property
  def nats(self) -> Any:
    return self._nats
  @nats.setter
  def nats(self, nats: Any):
    self._nats = nats

  @property
  def jms(self) -> MessageBindingsObjectJms.MessageBindingsObjectJms:
    return self._jms
  @jms.setter
  def jms(self, jms: MessageBindingsObjectJms.MessageBindingsObjectJms):
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
  def ibmmq(self) -> MessageBindingsObjectIbmmq.MessageBindingsObjectIbmmq:
    return self._ibmmq
  @ibmmq.setter
  def ibmmq(self, ibmmq: MessageBindingsObjectIbmmq.MessageBindingsObjectIbmmq):
    self._ibmmq = ibmmq

  @property
  def solace(self) -> Any:
    return self._solace
  @solace.setter
  def solace(self, solace: Any):
    self._solace = solace

  @property
  def googlepubsub(self) -> MessageBindingsObjectGooglepubsub.MessageBindingsObjectGooglepubsub:
    return self._googlepubsub
  @googlepubsub.setter
  def googlepubsub(self, googlepubsub: MessageBindingsObjectGooglepubsub.MessageBindingsObjectGooglepubsub):
    self._googlepubsub = googlepubsub

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
    return MessageBindingsObject(**json.loads(json_string))
