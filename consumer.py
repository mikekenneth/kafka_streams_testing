import json
from kafka import KafkaConsumer

bootstrap_servers = ["localhost:9092"]
topics = ["quickstart-events"]

consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, auto_offset_reset="earliest")
consumer.subscribe(topics=topics)


for event in consumer:
    print(event)
