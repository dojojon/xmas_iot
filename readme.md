# Christmas IOT using MQTT and Python

We are going to learn how to IoT enable our Christmas tree lights using MQTT and Python.  


## Some definitions

Lets define some things first.

### IoT - Internet of Things

The Internet of things (IoT) is the network of physical devices, vehicles, home appliances, and other items embedded with electronics, software, sensors, actuators, and network connectivity which enable these objects to connect and exchange data.

###  MQTT - MQ Telemetry Transport or Message Queuing Telemetry Transport

A lightweight messaging protocol for small sensors and mobile devices, optimized for high-latency or unreliable networks.  It what IoT things can use to communicate with each other things and with computers.

Sounds complex, but once you have a basic understanding you will start to see lots of uses for it.

### Python

A high-level general-purpose programming language.  We are going to be using Python 3.  

You can follow this tutorial without any programming or Python experience, but it's a good idea to have completed through the Beginners Python (http://kata.coderdojo.com/wiki/Beginner_Python) and Intermediate Python (http://kata.coderdojo.com/wiki/Intermediate_Python) Sushi Cards if you have no experience.

## The Post Office

...


### Client
### Broker
### Message
### Subscription
### Topic


## Set Up

....


##  Lets write a client to listen for chat messages

1.  Create a new python script file in your ide and add the following import statements.

```
import paho.mqtt.client as paho
```

2. Add a constant as shown below.  This is our topic and is like an address for messages we are interested in.

```
MSG_TOPIC = "chat/msg"
```

3. Next we are going to add a function that will get called when our client receives a message

```
def on_message(client, userdata, msg):

    # Check that the message comes from the topic we expected
    # The client can subscribe to multiple topics so we can use an if
    # statement to do different things for different topics

    if msg.topic == MSG_TOPIC:
        payload = msg.payload.decode("utf-8")
        print(payload)
```

4. Add another function that will get called when the client connects.  This is useful to see when if we are connected to the message broker.

```
def on_connect(client, userdata, flags, rc):

    # print out a message to the terminal window
    print("Connected")

    # subscribe to receive messages
    client.subscribe(MSG_TOPIC, qos=1)
```

5. Below these two functions we can add the code to create a client.

client = paho.Client()

6.  The client has a number of callbacks.  We can use these to run our code when things happen on the client.

```
#  This callback calls our function when it receives a message we have subscribed to.

client.on_message = on_message

# This callback is run when the client connects to the broker
client.on_connect = on_connect
```

7.  Almost done, we need to call the clients connect function with the ip address of the broker and the port.  

```
client.connect("192.168.1.20", 1883)
```

8.  Last of all we want our client to loop forever whilst its running

```
client.loop_forever()
```

9. Try running the client, it should run without error.





