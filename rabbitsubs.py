import pika

QUEUE_NAME = 'hello'

# Callback function ketika menerima pesan
def callback(ch, method, properties, body):
    print("Pesan diterima:", body.decode())

# Membuat koneksi ke broker RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Deklarasi queue
channel.queue_declare(queue=QUEUE_NAME)

# Mengatur callback function saat menerima pesan
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)

print('Menunggu pesan...')

# Memulai proses menerima pesan
channel.start_consuming()
