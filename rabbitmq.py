import pika

QUEUE_NAME = 'hello'

# Membuat koneksi ke broker RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Deklarasi queue
channel.queue_declare(queue=QUEUE_NAME)

# Meminta input dari user untuk isi pesan
pesan = input("Masukkan pesan: ")

# Mengirim pesan
channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=pesan)
print(" [x] Sent '" + pesan + "'")

# Menutup koneksi
channel.close()
connection.close()
