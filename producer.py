#
#PRODUCER
#
from kafka import KafkaProducer
import requests
import json

#topic = 'edvin_topic' # doesn't make sense now 
#message = request_nasa_data()


def send_message(topic, message):
    producer = KafkaProducer(bootstrap_servers=['node1.cloudera:9092'], 
    value_serializer=lambda x: json.dumps(x).encode('utf-8'), acks='all')
    producer.send(topic, message)
    producer.flush()
    producer.close()



#send_message()



#1 "Leave producer"
#2 nasa api change topic to correct (per documentation)
#3 Create topics on crypton.
#4 ###How to console consumer - collects
#5 Start nasa api client (it produces/fetches records) <
#6 Check output in console consumer

