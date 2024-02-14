from .ChannelBindingsObjectWs import ChannelBindingsObjectWs
from .ChannelBindingsObjectAmqp import ChannelBindingsObjectAmqp
from .ChannelBindingsObjectKafka import ChannelBindingsObjectKafka
from .ChannelBindingsObjectAnypointmq import ChannelBindingsObjectAnypointmq
from .ChannelBindingsObjectJms import ChannelBindingsObjectJms
from .ChannelBindingsObjectSns import ChannelBindingsObjectSns
from .ChannelBindingsObjectSqs import ChannelBindingsObjectSqs
from .ChannelBindingsObjectIbmmq import ChannelBindingsObjectIbmmq
from .ChannelBindingsObjectGooglepubsub import ChannelBindingsObjectGooglepubsub
from .ChannelBindingsObjectPulsar import ChannelBindingsObjectPulsar
import json
from typing import Any, List, Dict
class ChannelBindingsObject: 
  def __init__(self, input: Dict):
    if hasattr(input, 'http'):
      self._http: Any = input['http']
    if hasattr(input, 'ws'):
      self._ws: ChannelBindingsObjectWs = ChannelBindingsObjectWs(input['ws'])
    if hasattr(input, 'amqp'):
      self._amqp: ChannelBindingsObjectAmqp = ChannelBindingsObjectAmqp(input['amqp'])
    if hasattr(input, 'amqp1'):
      self._amqp1: Any = input['amqp1']
    if hasattr(input, 'mqtt'):
      self._mqtt: Any = input['mqtt']
    if hasattr(input, 'kafka'):
      self._kafka: ChannelBindingsObjectKafka = ChannelBindingsObjectKafka(input['kafka'])
    if hasattr(input, 'anypointmq'):
      self._anypointmq: ChannelBindingsObjectAnypointmq = ChannelBindingsObjectAnypointmq(input['anypointmq'])
    if hasattr(input, 'nats'):
      self._nats: Any = input['nats']
    if hasattr(input, 'jms'):
      self._jms: ChannelBindingsObjectJms = ChannelBindingsObjectJms(input['jms'])
    if hasattr(input, 'sns'):
      self._sns: ChannelBindingsObjectSns = ChannelBindingsObjectSns(input['sns'])
    if hasattr(input, 'sqs'):
      self._sqs: ChannelBindingsObjectSqs = ChannelBindingsObjectSqs(input['sqs'])
    if hasattr(input, 'stomp'):
      self._stomp: Any = input['stomp']
    if hasattr(input, 'redis'):
      self._redis: Any = input['redis']
    if hasattr(input, 'ibmmq'):
      self._ibmmq: ChannelBindingsObjectIbmmq = ChannelBindingsObjectIbmmq(input['ibmmq'])
    if hasattr(input, 'solace'):
      self._solace: Any = input['solace']
    if hasattr(input, 'googlepubsub'):
      self._googlepubsub: ChannelBindingsObjectGooglepubsub = ChannelBindingsObjectGooglepubsub(input['googlepubsub'])
    if hasattr(input, 'pulsar'):
      self._pulsar: ChannelBindingsObjectPulsar = ChannelBindingsObjectPulsar(input['pulsar'])
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def http(self) -> Any:
    return self._http
  @http.setter
  def http(self, http: Any):
    self._http = http

  @property
  def ws(self) -> ChannelBindingsObjectWs:
    return self._ws
  @ws.setter
  def ws(self, ws: ChannelBindingsObjectWs):
    self._ws = ws

  @property
  def amqp(self) -> ChannelBindingsObjectAmqp:
    return self._amqp
  @amqp.setter
  def amqp(self, amqp: ChannelBindingsObjectAmqp):
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
  def kafka(self) -> ChannelBindingsObjectKafka:
    return self._kafka
  @kafka.setter
  def kafka(self, kafka: ChannelBindingsObjectKafka):
    self._kafka = kafka

  @property
  def anypointmq(self) -> ChannelBindingsObjectAnypointmq:
    return self._anypointmq
  @anypointmq.setter
  def anypointmq(self, anypointmq: ChannelBindingsObjectAnypointmq):
    self._anypointmq = anypointmq

  @property
  def nats(self) -> Any:
    return self._nats
  @nats.setter
  def nats(self, nats: Any):
    self._nats = nats

  @property
  def jms(self) -> ChannelBindingsObjectJms:
    return self._jms
  @jms.setter
  def jms(self, jms: ChannelBindingsObjectJms):
    self._jms = jms

  @property
  def sns(self) -> ChannelBindingsObjectSns:
    return self._sns
  @sns.setter
  def sns(self, sns: ChannelBindingsObjectSns):
    self._sns = sns

  @property
  def sqs(self) -> ChannelBindingsObjectSqs:
    return self._sqs
  @sqs.setter
  def sqs(self, sqs: ChannelBindingsObjectSqs):
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
  def ibmmq(self) -> ChannelBindingsObjectIbmmq:
    return self._ibmmq
  @ibmmq.setter
  def ibmmq(self, ibmmq: ChannelBindingsObjectIbmmq):
    self._ibmmq = ibmmq

  @property
  def solace(self) -> Any:
    return self._solace
  @solace.setter
  def solace(self, solace: Any):
    self._solace = solace

  @property
  def googlepubsub(self) -> ChannelBindingsObjectGooglepubsub:
    return self._googlepubsub
  @googlepubsub.setter
  def googlepubsub(self, googlepubsub: ChannelBindingsObjectGooglepubsub):
    self._googlepubsub = googlepubsub

  @property
  def pulsar(self) -> ChannelBindingsObjectPulsar:
    return self._pulsar
  @pulsar.setter
  def pulsar(self, pulsar: ChannelBindingsObjectPulsar):
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
    return ChannelBindingsObject(**json.loads(json_string))
