from .OperationBindingsObjectHttp import OperationBindingsObjectHttp
from .OperationBindingsObjectAmqp import OperationBindingsObjectAmqp
from .OperationBindingsObjectMqtt import OperationBindingsObjectMqtt
from .OperationBindingsObjectKafka import OperationBindingsObjectKafka
from .OperationBindingsObjectNats import OperationBindingsObjectNats
from .OperationBindingsObjectSns import OperationBindingsObjectSns
from .OperationBindingsObjectSqs import OperationBindingsObjectSqs
from .OperationBindingsObjectSolace import OperationBindingsObjectSolace
import json
from typing import Any, List, Dict
class OperationBindingsObject: 
  def __init__(self, input: Dict):
    if hasattr(input, 'http'):
      self._http: OperationBindingsObjectHttp = OperationBindingsObjectHttp(input['http'])
    if hasattr(input, 'ws'):
      self._ws: Any = input['ws']
    if hasattr(input, 'amqp'):
      self._amqp: OperationBindingsObjectAmqp = OperationBindingsObjectAmqp(input['amqp'])
    if hasattr(input, 'amqp1'):
      self._amqp1: Any = input['amqp1']
    if hasattr(input, 'mqtt'):
      self._mqtt: OperationBindingsObjectMqtt = OperationBindingsObjectMqtt(input['mqtt'])
    if hasattr(input, 'kafka'):
      self._kafka: OperationBindingsObjectKafka = OperationBindingsObjectKafka(input['kafka'])
    if hasattr(input, 'anypointmq'):
      self._anypointmq: Any = input['anypointmq']
    if hasattr(input, 'nats'):
      self._nats: OperationBindingsObjectNats = OperationBindingsObjectNats(input['nats'])
    if hasattr(input, 'jms'):
      self._jms: Any = input['jms']
    if hasattr(input, 'sns'):
      self._sns: OperationBindingsObjectSns = OperationBindingsObjectSns(input['sns'])
    if hasattr(input, 'sqs'):
      self._sqs: OperationBindingsObjectSqs = OperationBindingsObjectSqs(input['sqs'])
    if hasattr(input, 'stomp'):
      self._stomp: Any = input['stomp']
    if hasattr(input, 'redis'):
      self._redis: Any = input['redis']
    if hasattr(input, 'ibmmq'):
      self._ibmmq: Any = input['ibmmq']
    if hasattr(input, 'solace'):
      self._solace: OperationBindingsObjectSolace = OperationBindingsObjectSolace(input['solace'])
    if hasattr(input, 'googlepubsub'):
      self._googlepubsub: Any = input['googlepubsub']
    if hasattr(input, 'additional_properties'):
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def http(self) -> OperationBindingsObjectHttp:
    return self._http
  @http.setter
  def http(self, http: OperationBindingsObjectHttp):
    self._http = http

  @property
  def ws(self) -> Any:
    return self._ws
  @ws.setter
  def ws(self, ws: Any):
    self._ws = ws

  @property
  def amqp(self) -> OperationBindingsObjectAmqp:
    return self._amqp
  @amqp.setter
  def amqp(self, amqp: OperationBindingsObjectAmqp):
    self._amqp = amqp

  @property
  def amqp1(self) -> Any:
    return self._amqp1
  @amqp1.setter
  def amqp1(self, amqp1: Any):
    self._amqp1 = amqp1

  @property
  def mqtt(self) -> OperationBindingsObjectMqtt:
    return self._mqtt
  @mqtt.setter
  def mqtt(self, mqtt: OperationBindingsObjectMqtt):
    self._mqtt = mqtt

  @property
  def kafka(self) -> OperationBindingsObjectKafka:
    return self._kafka
  @kafka.setter
  def kafka(self, kafka: OperationBindingsObjectKafka):
    self._kafka = kafka

  @property
  def anypointmq(self) -> Any:
    return self._anypointmq
  @anypointmq.setter
  def anypointmq(self, anypointmq: Any):
    self._anypointmq = anypointmq

  @property
  def nats(self) -> OperationBindingsObjectNats:
    return self._nats
  @nats.setter
  def nats(self, nats: OperationBindingsObjectNats):
    self._nats = nats

  @property
  def jms(self) -> Any:
    return self._jms
  @jms.setter
  def jms(self, jms: Any):
    self._jms = jms

  @property
  def sns(self) -> OperationBindingsObjectSns:
    return self._sns
  @sns.setter
  def sns(self, sns: OperationBindingsObjectSns):
    self._sns = sns

  @property
  def sqs(self) -> OperationBindingsObjectSqs:
    return self._sqs
  @sqs.setter
  def sqs(self, sqs: OperationBindingsObjectSqs):
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
  def ibmmq(self) -> Any:
    return self._ibmmq
  @ibmmq.setter
  def ibmmq(self, ibmmq: Any):
    self._ibmmq = ibmmq

  @property
  def solace(self) -> OperationBindingsObjectSolace:
    return self._solace
  @solace.setter
  def solace(self, solace: OperationBindingsObjectSolace):
    self._solace = solace

  @property
  def googlepubsub(self) -> Any:
    return self._googlepubsub
  @googlepubsub.setter
  def googlepubsub(self, googlepubsub: Any):
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
    return OperationBindingsObject(**json.loads(json_string))
