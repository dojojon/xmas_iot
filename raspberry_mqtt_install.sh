#!/bin/bash

echo 'apt-get update'
sudo apt-get update

sleep 5

echo 'Installing Mosquitto'
sudo apt-get install -y mosquitto mosquitto-clients

sleep 5

echo 'Installing poha-mqtt'
sudo pip3 install paho-mqtt

echo 'Done'

sleep 5
