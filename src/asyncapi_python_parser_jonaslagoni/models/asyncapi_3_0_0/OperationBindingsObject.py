from __future__ import annotations
import json
from typing import Any, List, Dict
from . import OperationBindingsObjectHttp
from . import OperationBindingsObjectAmqp
from . import OperationBindingsObjectMqtt
from . import OperationBindingsObjectKafka
from . import OperationBindingsObjectNats
from . import OperationBindingsObjectSns
from . import OperationBindingsObjectSqs
from . import OperationBindingsObjectSolace
class OperationBindingsObject: 
  def __init__(self, input: Dict):
    if 'http' in input:
      self._http: OperationBindingsObjectHttp.OperationBindingsObjectHttp = OperationBindingsObjectHttp.OperationBindingsObjectHttp(input['http'])
    if 'ws' in input:
      self._ws: Any = input['ws']
    if 'amqp' in input:
      self._amqp: OperationBindingsObjectAmqp.OperationBindingsObjectAmqp = OperationBindingsObjectAmqp.OperationBindingsObjectAmqp(input['amqp'])
    if 'amqp1' in input:
      self._amqp1: Any = input['amqp1']
    if 'mqtt' in input:
      self._mqtt: OperationBindingsObjectMqtt.OperationBindingsObjectMqtt = OperationBindingsObjectMqtt.OperationBindingsObjectMqtt(input['mqtt'])
    if 'kafka' in input:
      self._kafka: OperationBindingsObjectKafka.OperationBindingsObjectKafka = OperationBindingsObjectKafka.OperationBindingsObjectKafka(input['kafka'])
    if 'anypointmq' in input:
      self._anypointmq: Any = input['anypointmq']
    if 'nats' in input:
      self._nats: OperationBindingsObjectNats.OperationBindingsObjectNats = OperationBindingsObjectNats.OperationBindingsObjectNats(input['nats'])
    if 'jms' in input:
      self._jms: Any = input['jms']
    if 'sns' in input:
      self._sns: OperationBindingsObjectSns.OperationBindingsObjectSns = OperationBindingsObjectSns.OperationBindingsObjectSns(input['sns'])
    if 'sqs' in input:
      self._sqs: OperationBindingsObjectSqs.OperationBindingsObjectSqs = OperationBindingsObjectSqs.OperationBindingsObjectSqs(input['sqs'])
    if 'stomp' in input:
      self._stomp: Any = input['stomp']
    if 'redis' in input:
      self._redis: Any = input['redis']
    if 'ibmmq' in input:
      self._ibmmq: Any = input['ibmmq']
    if 'solace' in input:
      self._solace: OperationBindingsObjectSolace.OperationBindingsObjectSolace = OperationBindingsObjectSolace.OperationBindingsObjectSolace(input['solace'])
    if 'googlepubsub' in input:
      self._googlepubsub: Any = input['googlepubsub']
    if 'additional_properties' in input:
      self._additional_properties: dict[str, Any] = input['additional_properties']

  @property
  def http(self) -> OperationBindingsObjectHttp.OperationBindingsObjectHttp:
    return self._http
  @http.setter
  def http(self, http: OperationBindingsObjectHttp.OperationBindingsObjectHttp):
    self._http = http

  @property
  def ws(self) -> Any:
    return self._ws
  @ws.setter
  def ws(self, ws: Any):
    self._ws = ws

  @property
  def amqp(self) -> OperationBindingsObjectAmqp.OperationBindingsObjectAmqp:
    return self._amqp
  @amqp.setter
  def amqp(self, amqp: OperationBindingsObjectAmqp.OperationBindingsObjectAmqp):
    self._amqp = amqp

  @property
  def amqp1(self) -> Any:
    return self._amqp1
  @amqp1.setter
  def amqp1(self, amqp1: Any):
    self._amqp1 = amqp1

  @property
  def mqtt(self) -> OperationBindingsObjectMqtt.OperationBindingsObjectMqtt:
    return self._mqtt
  @mqtt.setter
  def mqtt(self, mqtt: OperationBindingsObjectMqtt.OperationBindingsObjectMqtt):
    self._mqtt = mqtt

  @property
  def kafka(self) -> OperationBindingsObjectKafka.OperationBindingsObjectKafka:
    return self._kafka
  @kafka.setter
  def kafka(self, kafka: OperationBindingsObjectKafka.OperationBindingsObjectKafka):
    self._kafka = kafka

  @property
  def anypointmq(self) -> Any:
    return self._anypointmq
  @anypointmq.setter
  def anypointmq(self, anypointmq: Any):
    self._anypointmq = anypointmq

  @property
  def nats(self) -> OperationBindingsObjectNats.OperationBindingsObjectNats:
    return self._nats
  @nats.setter
  def nats(self, nats: OperationBindingsObjectNats.OperationBindingsObjectNats):
    self._nats = nats

  @property
  def jms(self) -> Any:
    return self._jms
  @jms.setter
  def jms(self, jms: Any):
    self._jms = jms

  @property
  def sns(self) -> OperationBindingsObjectSns.OperationBindingsObjectSns:
    return self._sns
  @sns.setter
  def sns(self, sns: OperationBindingsObjectSns.OperationBindingsObjectSns):
    self._sns = sns

  @property
  def sqs(self) -> OperationBindingsObjectSqs.OperationBindingsObjectSqs:
    return self._sqs
  @sqs.setter
  def sqs(self, sqs: OperationBindingsObjectSqs.OperationBindingsObjectSqs):
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
  def solace(self) -> OperationBindingsObjectSolace.OperationBindingsObjectSolace:
    return self._solace
  @solace.setter
  def solace(self, solace: OperationBindingsObjectSolace.OperationBindingsObjectSolace):
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
