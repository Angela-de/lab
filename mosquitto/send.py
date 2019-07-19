import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:
        print("Connection failed")

Connected = False

client = mqtt.Client()
client.on_connect = on_connect
client.connect("104.248.163.70", 1883, 60)
client.loop_start()
while Connected != True: 
    time.sleep(0.1)

try:
    while True:
        message = input('Your message: ')
        client.publish("UCC/Ann", message)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
