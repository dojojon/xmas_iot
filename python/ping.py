import paho.mqtt.client as paho
import time

MSG_TOPIC = "chat/msg"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code")
    n = 0
    while True:
        n = n + 1
        client.publish(MSG_TOPIC, "Jingle " + str(n))
        time.sleep(2)

client = paho.Client()
client.on_connect = on_connect
client.connect("192.168.1.20", 1883)
client.loop_forever()
