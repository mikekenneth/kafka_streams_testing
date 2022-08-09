import json
from kafka import KafkaProducer

bootstrap_servers = ["localhost:9092"]
topic_name = "quickstart-events"

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

with open("data/input.txt") as f:
    lines = f.readlines()

for line in lines:
    print(line)
    producer.send(topic=topic_name, value=json.dumps(line).encode("utf-8"))
