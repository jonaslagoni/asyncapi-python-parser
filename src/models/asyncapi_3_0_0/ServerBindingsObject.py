from .ServerBindingsObjectMqtt import ServerBindingsObjectMqtt
from .ServerBindingsObjectKafka import ServerBindingsObjectKafka
from .ServerBindingsObjectJms import ServerBindingsObjectJms
from .ServerBindingsObjectIbmmq import ServerBindingsObjectIbmmq
from .ServerBindingsObjectSolace import ServerBindingsObjectSolace
from .ServerBindingsObjectPulsar import ServerBindingsObjectPulsar
import json
from typing import Any, List, Dict
class ServerBindingsObject: 
  def __init__(self, input: Dict):
    if hasattr(input, 'http'):
      self._http: Any = input['http']
    if hasattr(input, 'ws'):
      self._ws: Any = input['ws']
    if hasattr(input, 'amqp'):
      self._amqp: Any = input['amqp']
    if hasattr(input, 'amqp1'):
      self._amqp1: Any = input['amqp1']
    if hasattr(input, 'mqtt'):
      self._mqtt: ServerBindingsObjectMqtt = ServerBindingsObjectMqtt(input['mqtt'])
    if hasattr(input, 'kafka'):
      self._kafka: ServerBindingsObjectKafka = ServerBindingsObjectKafka(input['kafka'])
    if hasattr(input, 'anypointmq'):
      self._anypointmq: Any = input['anypointmq']
    if hasattr(input, 'nats'):
      self._nats: Any = input['nats']
    if hasattr(input, 'jms'):
      self._jms: ServerBindingsObjectJms = ServerBindingsObjectJms(input['jms'])
    if hasattr(input, 'sns'):
      self._sns: Any = input['sns']
    if hasattr(input, 'sqs'):
      self._sqs: Any = input['sqs']
    if hasattr(input, 'stomp'):
      self._stomp: Any = input['stomp']
    if hasattr(input, 'redis'):
      self._redis: Any = input['redis']
    if hasattr(input, 'ibmmq'):
      self._ibmmq: ServerBindingsObjectIbmmq = ServerBindingsObjectIbmmq(input['ibmmq'])
    if hasattr(input, 'solace'):
      self._solace: ServerBindingsObjectSolace = ServerBindingsObjectSolace(input['solace'])
    if hasattr(input, 'googlepubsub'):
      self._googlepubsub: Any = input['googlepubsub']
    if hasattr(input, 'pulsar'):
      self._pulsar: ServerBindingsObjectPulsar = ServerBindingsObjectPulsar(input['pulsar'])
    if hasattr(input, 'additional_properties'):
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
  def mqtt(self) -> ServerBindingsObjectMqtt:
    return self._mqtt
  @mqtt.setter
  def mqtt(self, mqtt: ServerBindingsObjectMqtt):
    self._mqtt = mqtt

  @property
  def kafka(self) -> ServerBindingsObjectKafka:
    return self._kafka
  @kafka.setter
  def kafka(self, kafka: ServerBindingsObjectKafka):
    self._kafka = kafka

  @property
  def anypointmq(self) -> Any:
    return self._anypointmq
  @anypointmq.setter
  def anypointmq(self, anypointmq: Any):
    self._anypointmq = anypointmq

  @property
  def nats(self) -> Any:
    return self._nats
  @nats.setter
  def nats(self, nats: Any):
    self._nats = nats

  @property
  def jms(self) -> ServerBindingsObjectJms:
    return self._jms
  @jms.setter
  def jms(self, jms: ServerBindingsObjectJms):
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
  def ibmmq(self) -> ServerBindingsObjectIbmmq:
    return self._ibmmq
  @ibmmq.setter
  def ibmmq(self, ibmmq: ServerBindingsObjectIbmmq):
    self._ibmmq = ibmmq

  @property
  def solace(self) -> ServerBindingsObjectSolace:
    return self._solace
  @solace.setter
  def solace(self, solace: ServerBindingsObjectSolace):
    self._solace = solace

  @property
  def googlepubsub(self) -> Any:
    return self._googlepubsub
  @googlepubsub.setter
  def googlepubsub(self, googlepubsub: Any):
    self._googlepubsub = googlepubsub

  @property
  def pulsar(self) -> ServerBindingsObjectPulsar:
    return self._pulsar
  @pulsar.setter
  def pulsar(self, pulsar: ServerBindingsObjectPulsar):
    self._pulsar = pulsar

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
    return ServerBindingsObject(**json.loads(json_string))
