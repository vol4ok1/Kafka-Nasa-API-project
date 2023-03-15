#
#PRODUCER
#
from kafka import KafkaProducer
import requests
import json



def send_message(topic, message):
    producer = KafkaProducer(bootstrap_servers=['node1.cloudera:9092'], 
    value_serializer=lambda x: json.dumps(x).encode('utf-8'), acks='all')
    producer.send(topic, message)
    producer.flush()
    producer.close()



#send_message()
