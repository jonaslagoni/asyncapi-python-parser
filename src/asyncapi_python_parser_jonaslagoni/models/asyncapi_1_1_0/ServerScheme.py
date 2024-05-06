from enum import Enum

class ServerScheme(Enum): 
  KAFKA = "kafka"
  KAFKA_MINUS_SECURE = "kafka-secure"
  AMQP = "amqp"
  AMQPS = "amqps"
  MQTT = "mqtt"
  MQTTS = "mqtts"
  SECURE_MINUS_MQTT = "secure-mqtt"
  WS = "ws"
  WSS = "wss"
  STOMP = "stomp"
  STOMPS = "stomps"
  JMS = "jms"