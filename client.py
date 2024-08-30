import paho.mqtt.client as mqtt 

def on_connect(client, userdata, flags,rc):
	print("Connected to MQTT")
	print("Connection returned result: " + str(rc))

	client.subscribe("IFN649")

def on_message(client, userdata, msg):
	print(msg.topic+""+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("52.64.166.204", 1883, 60)

client.loop_forever()

