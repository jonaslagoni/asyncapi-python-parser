from .MessageBindingsObjectHttp import MessageBindingsObjectHttp
from .MessageBindingsObjectAmqp import MessageBindingsObjectAmqp
from .MessageBindingsObjectMqtt import MessageBindingsObjectMqtt
from .MessageBindingsObjectKafka import MessageBindingsObjectKafka
from .MessageBindingsObjectAnypointmq import MessageBindingsObjectAnypointmq
from .MessageBindingsObjectJms import MessageBindingsObjectJms
from .MessageBindingsObjectIbmmq import MessageBindingsObjectIbmmq
from .MessageBindingsObjectGooglepubsub import MessageBindingsObjectGooglepubsub
import json
from typing import Any, List, Dict
class MessageBindingsObject: 
  def __init__(self, input: Dict):
    if hasattr(input, 'http'):
      self._http: MessageBindingsObjectHttp = MessageBindingsObjectHttp(input['http'])
    if hasattr(input, 'ws'):
      self._ws: Any = input['ws']
    if hasattr(input, 'amqp'):
      self._amqp: MessageBindingsObjectAmqp = MessageBindingsObjectAmqp(input['amqp'])
    if hasattr(input, 'amqp1'):
      self._amqp1: Any = input['amqp1']
    if hasattr(input, 'mqtt'):
      self._mqtt: MessageBindingsObjectMqtt = MessageBindingsObjectMqtt(input['mqtt'])
    if hasattr(input, 'kafka'):
      self._kafka: MessageBindingsObjectKafka = MessageBindingsObjectKafka(input['kafka'])
    if hasattr(input, 'anypointmq'):
      self._anypointmq: MessageBindingsObjectAnypointmq = MessageBindingsObjectAnypointmq(input['anypointmq'])
    if hasattr(input, 'nats'):
      self._nats: Any = input['nats']
    if hasattr(input, 'jms'):
      self._jms: MessageBindingsObjectJms = MessageBindingsObjectJms(input['jms'])
    if hasattr(input, 'sns'):
      self._sns: Any = input['sns']
    if hasattr(input, 'sqs'):
      self._sqs: Any = input['sqs']
    if hasattr(input, 'stomp'):
      self._stomp: Any = input['stomp']
    if hasattr(input, 'redis'):
      self._redis: Any = input['redis']
    if hasattr(input, 'ibmmq'):
      self._ibmmq: MessageBindingsObjectIbmmq = MessageBindingsObjectIbmmq(input['ibmmq'])
    if hasattr(input, 'solace'):
      self._solace: Any = input['solace']
    if hasattr(input, 'googlepubsub'):
      self._googlepubsub: MessageBindingsObjectGooglepubsub = MessageBindingsObjectGooglepubsub(input['googlepubsub'])
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def http(self) -> MessageBindingsObjectHttp:
    return self._http
  @http.setter
  def http(self, http: MessageBindingsObjectHttp):
    self._http = http

  @property
  def ws(self) -> Any:
    return self._ws
  @ws.setter
  def ws(self, ws: Any):
    self._ws = ws

  @property
  def amqp(self) -> MessageBindingsObjectAmqp:
    return self._amqp
  @amqp.setter
  def amqp(self, amqp: MessageBindingsObjectAmqp):
    self._amqp = amqp

  @property
  def amqp1(self) -> Any:
    return self._amqp1
  @amqp1.setter
  def amqp1(self, amqp1: Any):
    self._amqp1 = amqp1

  @property
  def mqtt(self) -> MessageBindingsObjectMqtt:
    return self._mqtt
  @mqtt.setter
  def mqtt(self, mqtt: MessageBindingsObjectMqtt):
    self._mqtt = mqtt

  @property
  def kafka(self) -> MessageBindingsObjectKafka:
    return self._kafka
  @kafka.setter
  def kafka(self, kafka: MessageBindingsObjectKafka):
    self._kafka = kafka

  @property
  def anypointmq(self) -> MessageBindingsObjectAnypointmq:
    return self._anypointmq
  @anypointmq.setter
  def anypointmq(self, anypointmq: MessageBindingsObjectAnypointmq):
    self._anypointmq = anypointmq

  @property
  def nats(self) -> Any:
    return self._nats
  @nats.setter
  def nats(self, nats: Any):
    self._nats = nats

  @property
  def jms(self) -> MessageBindingsObjectJms:
    return self._jms
  @jms.setter
  def jms(self, jms: MessageBindingsObjectJms):
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
  def ibmmq(self) -> MessageBindingsObjectIbmmq:
    return self._ibmmq
  @ibmmq.setter
  def ibmmq(self, ibmmq: MessageBindingsObjectIbmmq):
    self._ibmmq = ibmmq

  @property
  def solace(self) -> Any:
    return self._solace
  @solace.setter
  def solace(self, solace: Any):
    self._solace = solace

  @property
  def googlepubsub(self) -> MessageBindingsObjectGooglepubsub:
    return self._googlepubsub
  @googlepubsub.setter
  def googlepubsub(self, googlepubsub: MessageBindingsObjectGooglepubsub):
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
