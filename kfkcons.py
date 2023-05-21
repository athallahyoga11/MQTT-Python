from kafka import KafkaConsumer

# Inisialisasi consumer
consumer = KafkaConsumer('<nama_topic>', bootstrap_servers=['localhost:3000'], auto_offset_reset='earliest')

# Baca pesan dari topic
for message in consumer:
    print(message.value)
