from __future__ import annotations
import json
from typing import Any, List, Dict
from . import ChannelBindingsObjectWs
from . import ChannelBindingsObjectAmqp
from . import ChannelBindingsObjectKafka
from . import ChannelBindingsObjectAnypointmq
from . import ChannelBindingsObjectJms
from . import ChannelBindingsObjectSns
from . import ChannelBindingsObjectSqs
from . import ChannelBindingsObjectIbmmq
from . import ChannelBindingsObjectGooglepubsub
from . import ChannelBindingsObjectPulsar
class ChannelBindingsObject: 
  def __init__(self, input: Dict):
    if 'http' in input:
      self._http: Any = input['http']
    if 'ws' in input:
      self._ws: ChannelBindingsObjectWs.ChannelBindingsObjectWs = ChannelBindingsObjectWs.ChannelBindingsObjectWs(input['ws'])
    if 'amqp' in input:
      self._amqp: ChannelBindingsObjectAmqp.ChannelBindingsObjectAmqp = ChannelBindingsObjectAmqp.ChannelBindingsObjectAmqp(input['amqp'])
    if 'amqp1' in input:
      self._amqp1: Any = input['amqp1']
    if 'mqtt' in input:
      self._mqtt: Any = input['mqtt']
    if 'kafka' in input:
      self._kafka: ChannelBindingsObjectKafka.ChannelBindingsObjectKafka = ChannelBindingsObjectKafka.ChannelBindingsObjectKafka(input['kafka'])
    if 'anypointmq' in input:
      self._anypointmq: ChannelBindingsObjectAnypointmq.ChannelBindingsObjectAnypointmq = ChannelBindingsObjectAnypointmq.ChannelBindingsObjectAnypointmq(input['anypointmq'])
    if 'nats' in input:
      self._nats: Any = input['nats']
    if 'jms' in input:
      self._jms: ChannelBindingsObjectJms.ChannelBindingsObjectJms = ChannelBindingsObjectJms.ChannelBindingsObjectJms(input['jms'])
    if 'sns' in input:
      self._sns: ChannelBindingsObjectSns.ChannelBindingsObjectSns = ChannelBindingsObjectSns.ChannelBindingsObjectSns(input['sns'])
    if 'sqs' in input:
      self._sqs: ChannelBindingsObjectSqs.ChannelBindingsObjectSqs = ChannelBindingsObjectSqs.ChannelBindingsObjectSqs(input['sqs'])
    if 'stomp' in input:
      self._stomp: Any = input['stomp']
    if 'redis' in input:
      self._redis: Any = input['redis']
    if 'ibmmq' in input:
      self._ibmmq: ChannelBindingsObjectIbmmq.ChannelBindingsObjectIbmmq = ChannelBindingsObjectIbmmq.ChannelBindingsObjectIbmmq(input['ibmmq'])
    if 'solace' in input:
      self._solace: Any = input['solace']
    if 'googlepubsub' in input:
      self._googlepubsub: ChannelBindingsObjectGooglepubsub.ChannelBindingsObjectGooglepubsub = ChannelBindingsObjectGooglepubsub.ChannelBindingsObjectGooglepubsub(input['googlepubsub'])
    if 'pulsar' in input:
      self._pulsar: ChannelBindingsObjectPulsar.ChannelBindingsObjectPulsar = ChannelBindingsObjectPulsar.ChannelBindingsObjectPulsar(input['pulsar'])
    if 'extensions' in input:
      self._extensions: dict[str, Any] = input['extensions']

  @property
  def http(self) -> Any:
    return self._http
  @http.setter
  def http(self, http: Any):
    self._http = http

  @property
  def ws(self) -> ChannelBindingsObjectWs.ChannelBindingsObjectWs:
    return self._ws
  @ws.setter
  def ws(self, ws: ChannelBindingsObjectWs.ChannelBindingsObjectWs):
    self._ws = ws

  @property
  def amqp(self) -> ChannelBindingsObjectAmqp.ChannelBindingsObjectAmqp:
    return self._amqp
  @amqp.setter
  def amqp(self, amqp: ChannelBindingsObjectAmqp.ChannelBindingsObjectAmqp):
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
  def kafka(self) -> ChannelBindingsObjectKafka.ChannelBindingsObjectKafka:
    return self._kafka
  @kafka.setter
  def kafka(self, kafka: ChannelBindingsObjectKafka.ChannelBindingsObjectKafka):
    self._kafka = kafka

  @property
  def anypointmq(self) -> ChannelBindingsObjectAnypointmq.ChannelBindingsObjectAnypointmq:
    return self._anypointmq
  @anypointmq.setter
  def anypointmq(self, anypointmq: ChannelBindingsObjectAnypointmq.ChannelBindingsObjectAnypointmq):
    self._anypointmq = anypointmq

  @property
  def nats(self) -> Any:
    return self._nats
  @nats.setter
  def nats(self, nats: Any):
    self._nats = nats

  @property
  def jms(self) -> ChannelBindingsObjectJms.ChannelBindingsObjectJms:
    return self._jms
  @jms.setter
  def jms(self, jms: ChannelBindingsObjectJms.ChannelBindingsObjectJms):
    self._jms = jms

  @property
  def sns(self) -> ChannelBindingsObjectSns.ChannelBindingsObjectSns:
    return self._sns
  @sns.setter
  def sns(self, sns: ChannelBindingsObjectSns.ChannelBindingsObjectSns):
    self._sns = sns

  @property
  def sqs(self) -> ChannelBindingsObjectSqs.ChannelBindingsObjectSqs:
    return self._sqs
  @sqs.setter
  def sqs(self, sqs: ChannelBindingsObjectSqs.ChannelBindingsObjectSqs):
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
  def ibmmq(self) -> ChannelBindingsObjectIbmmq.ChannelBindingsObjectIbmmq:
    return self._ibmmq
  @ibmmq.setter
  def ibmmq(self, ibmmq: ChannelBindingsObjectIbmmq.ChannelBindingsObjectIbmmq):
    self._ibmmq = ibmmq

  @property
  def solace(self) -> Any:
    return self._solace
  @solace.setter
  def solace(self, solace: Any):
    self._solace = solace

  @property
  def googlepubsub(self) -> ChannelBindingsObjectGooglepubsub.ChannelBindingsObjectGooglepubsub:
    return self._googlepubsub
  @googlepubsub.setter
  def googlepubsub(self, googlepubsub: ChannelBindingsObjectGooglepubsub.ChannelBindingsObjectGooglepubsub):
    self._googlepubsub = googlepubsub

  @property
  def pulsar(self) -> ChannelBindingsObjectPulsar.ChannelBindingsObjectPulsar:
    return self._pulsar
  @pulsar.setter
  def pulsar(self, pulsar: ChannelBindingsObjectPulsar.ChannelBindingsObjectPulsar):
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
    return ChannelBindingsObject(**json.loads(json_string))
