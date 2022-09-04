#Imports of the current application
from kafka import KafkaProducer
from json import dumps
#Imports to interact with the operating system

#Section imports

productor = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

def produce(topic,data):
    
    productor.send(topic, data)
    
    return "ok"

