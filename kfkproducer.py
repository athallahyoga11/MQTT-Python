from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092')
message = {'key': 'value'}
producer.send('my_topic', json.dumps(message).encode('utf-8'))
