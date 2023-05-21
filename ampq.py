import pika

# Buat koneksi
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Deklarasikan antrian
channel.queue_declare(queue='nama_antrian')

# Ambil input pesan dari pengguna
pesan = input("Masukkan pesan Anda: ")

# Kirim pesan
channel.basic_publish(exchange='', routing_key='nama_antrian', body=pesan)
print("Pesan berhasil dikirim: ", pesan)

# Tutup saluran dan koneksi
channel.close()
connection.close()
