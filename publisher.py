import paho.mqtt.publish as publish 

publish.single("IFN649", "Hello World", hostname= "52.64.166.204")
print("Done")
