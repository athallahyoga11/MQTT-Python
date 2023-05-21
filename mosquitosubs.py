import paho.mqtt.client as mqtt

# Inisialisasi client MQTT
client = mqtt.Client()

# Callback function ketika koneksi ke broker berhasil didirikan
def on_connect(client, userdata, flags, rc):
    print("Terhubung ke broker dengan kode:", rc)
    # Subscribe ke topik "topic/test" untuk menerima pesan
    client.subscribe("topic/test")

# Callback function ketika menerima pesan
def on_message(client, userdata, msg):
    print("Pesan diterima dari topik:", msg.topic)
    print("Isi pesan:", msg.payload.decode())

# Mengatur callback function saat terhubung ke broker
client.on_connect = on_connect

# Mengatur callback function saat menerima pesan
client.on_message = on_message

# Koneksi ke broker MQTT
client.connect("broker.hivemq.com", 1883)

# Loop forever untuk menerima pesan
client.loop_forever()
