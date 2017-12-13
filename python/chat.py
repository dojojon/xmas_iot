import paho.mqtt.client as paho

MSG_TOPIC = "chat/msg"


def on_message(client, userdata, msg):

    # Check that the message comes from the topic we expected
    if msg.topic == MSG_TOPIC:
        payload = msg.payload.decode("utf-8")
        print(payload)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code")

client = paho.Client()
client.on_message = on_message
client.on_connect = on_connect
client.connect("192.168.1.20", 1883)
client.subscribe(MSG_TOPIC, qos=1)

client.loop_forever()
