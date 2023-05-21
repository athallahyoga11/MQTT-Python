import pika

# Buat koneksi
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Deklarasikan antrian
channel.queue_declare(queue='nama_antrian')

def callback(ch, method, properties, body):
    # Fungsi ini akan dipanggil ketika pesan diterima
    print("Pesan diterima: ", body)

# Tentukan fungsi callback sebagai konsumen pesan
channel.basic_consume(queue='nama_antrian', on_message_callback=callback, auto_ack=True)

# Mulai mengonsumsi pesan-pesan yang masuk
print('Menunggu pesan. Tekan CTRL+C untuk keluar.')
channel.start_consuming()

# Tutup saluran dan koneksi
channel.close()
connection.close()
