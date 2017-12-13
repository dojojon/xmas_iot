import paho.mqtt.publish as publish
import time

MSG_TOPIC = "chat/msg"

name = input("Enter your name:")

running = True

while running:

    msg = input("Enter a message (type exit to quit):")

    if msg == 'exit':
        running = False
    else:
        msg = name + ":" + msg
        publish.single(MSG_TOPIC, msg, hostname="192.168.1.20")
