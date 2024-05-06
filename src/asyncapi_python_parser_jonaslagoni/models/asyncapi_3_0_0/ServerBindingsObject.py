from __future__ import annotations
import json
from typing import Any, List, Dict
from . import ServerBindingsObjectMqtt
from . import ServerBindingsObjectKafka
from . import ServerBindingsObjectJms
from . import ServerBindingsObjectIbmmq
from . import ServerBindingsObjectSolace
from . import ServerBindingsObjectPulsar
class ServerBindingsObject: 
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
      self._mqtt: ServerBindingsObjectMqtt.ServerBindingsObjectMqtt = ServerBindingsObjectMqtt.ServerBindingsObjectMqtt(input['mqtt'])
    if 'kafka' in input:
      self._kafka: ServerBindingsObjectKafka.ServerBindingsObjectKafka = ServerBindingsObjectKafka.ServerBindingsObjectKafka(input['kafka'])
    if 'anypointmq' in input:
      self._anypointmq: Any = input['anypointmq']
    if 'nats' in input:
      self._nats: Any = input['nats']
    if 'jms' in input:
      self._jms: ServerBindingsObjectJms.ServerBindingsObjectJms = ServerBindingsObjectJms.ServerBindingsObjectJms(input['jms'])
    if 'sns' in input:
      self._sns: Any = input['sns']
    if 'sqs' in input:
      self._sqs: Any = input['sqs']
    if 'stomp' in input:
      self._stomp: Any = input['stomp']
    if 'redis' in input:
      self._redis: Any = input['redis']
    if 'ibmmq' in input:
      self._ibmmq: ServerBindingsObjectIbmmq.ServerBindingsObjectIbmmq = ServerBindingsObjectIbmmq.ServerBindingsObjectIbmmq(input['ibmmq'])
    if 'solace' in input:
      self._solace: ServerBindingsObjectSolace.ServerBindingsObjectSolace = ServerBindingsObjectSolace.ServerBindingsObjectSolace(input['solace'])
    if 'googlepubsub' in input:
      self._googlepubsub: Any = input['googlepubsub']
    if 'pulsar' in input:
      self._pulsar: ServerBindingsObjectPulsar.ServerBindingsObjectPulsar = ServerBindingsObjectPulsar.ServerBindingsObjectPulsar(input['pulsar'])
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

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
  def mqtt(self) -> ServerBindingsObjectMqtt.ServerBindingsObjectMqtt:
    return self._mqtt
  @mqtt.setter
  def mqtt(self, mqtt: ServerBindingsObjectMqtt.ServerBindingsObjectMqtt):
    self._mqtt = mqtt

  @property
  def kafka(self) -> ServerBindingsObjectKafka.ServerBindingsObjectKafka:
    return self._kafka
  @kafka.setter
  def kafka(self, kafka: ServerBindingsObjectKafka.ServerBindingsObjectKafka):
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
  def jms(self) -> ServerBindingsObjectJms.ServerBindingsObjectJms:
    return self._jms
  @jms.setter
  def jms(self, jms: ServerBindingsObjectJms.ServerBindingsObjectJms):
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
  def ibmmq(self) -> ServerBindingsObjectIbmmq.ServerBindingsObjectIbmmq:
    return self._ibmmq
  @ibmmq.setter
  def ibmmq(self, ibmmq: ServerBindingsObjectIbmmq.ServerBindingsObjectIbmmq):
    self._ibmmq = ibmmq

  @property
  def solace(self) -> ServerBindingsObjectSolace.ServerBindingsObjectSolace:
    return self._solace
  @solace.setter
  def solace(self, solace: ServerBindingsObjectSolace.ServerBindingsObjectSolace):
    self._solace = solace

  @property
  def googlepubsub(self) -> Any:
    return self._googlepubsub
  @googlepubsub.setter
  def googlepubsub(self, googlepubsub: Any):
    self._googlepubsub = googlepubsub

  @property
  def pulsar(self) -> ServerBindingsObjectPulsar.ServerBindingsObjectPulsar:
    return self._pulsar
  @pulsar.setter
  def pulsar(self, pulsar: ServerBindingsObjectPulsar.ServerBindingsObjectPulsar):
    self._pulsar = pulsar

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
    return ServerBindingsObject(**json.loads(json_string))
