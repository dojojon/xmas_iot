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

### Subscriber

In this section we are going to write a script to connect to the broker and listen for chat messages.

1.  Create a new python script and save it with the name sub.py. Add the following import statement.  

```
import paho.mqtt.client as paho
```

2. Add a constant for our topic.  Our program will subscribe (listen) for messages that are sent from others with this.

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

6.  Try running the program.  If it does not work, check out the example in the python folder.


## Publisher

Next we will create another script to publish chat messages.

1.  Create another python script, this time save it with the name pub.py. Add the following import statements.  

```
import paho.mqtt.publish as publish
import time
```
2.  Again add a constant for our topic.  This needs to match the value used in our sub.py script

```
MSG_TOPIC = "chat/msg"
```

3.  Next we are going ask the user to enter there name and store it in a variable.

```
name = input("Enter your name:")
```

4. We want the script to repeatedly as the user for messages until they exit.  We will use a variable named ```running``` and a while loop

```
running = True
while running:
```

5. In the while loop we will ask the user to type a message.  If they type 'exit' we will set running to false.  If its something else, then we will build the message to send and publish it.

```
    msg = input("Enter a message (type exit to quit):")

    if msg == 'exit':
        running = False
    else:
        msg = name + ":" + msg
        publish.single(MSG_TOPIC, msg, hostname="192.168.1.20")

```

6.  Try running the program in a new terminal window.  You want to have both scripts running at the same time. If it does not work, check out the example in the python folder.



