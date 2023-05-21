import paho.mqtt.client as mqtt

# Inisialisasi client MQTT
client = mqtt.Client()

# Koneksi ke broker HiveMQ
client.connect("broker.hivemq.com", 1883)

# Meminta input dari user untuk isi pesan
pesan = input("Masukkan pesan: ")

# Mengirim pesan
result = client.publish("topic/test", pesan)

# Menunggu hingga pesan berhasil terkirimkan
if result.rc == mqtt.MQTT_ERR_SUCCESS:
    print("Pesan berhasil terkirim.")
    print("Isi pesan:", pesan)
else:
    print("Gagal mengirim pesan dengan kode kesalahan:", result.rc)
