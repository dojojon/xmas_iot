import paho.mqtt.publish as publish
import time

MSG_TOPIC = "chat/msg"
n = 0

while True:
    n = n + 1
    msg = "Ping " + str(n)
    publish.single(MSG_TOPIC, msg, hostname="192.168.1.20")
    print("Sent:" + msg)
    time.sleep(5)
