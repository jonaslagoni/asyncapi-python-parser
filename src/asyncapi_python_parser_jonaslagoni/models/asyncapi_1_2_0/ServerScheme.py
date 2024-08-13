from enum import Enum

class ServerScheme(Enum): 
  KAFKA = "kafka"
  KAFKA_SECURE = "kafka-secure"
  AMQP = "amqp"
  AMQPS = "amqps"
  MQTT = "mqtt"
  MQTTS = "mqtts"
  SECURE_MQTT = "secure-mqtt"
  WS = "ws"
  WSS = "wss"
  STOMP = "stomp"
  STOMPS = "stomps"
  JMS = "jms"
  HTTP = "http"
  HTTPS = "https"