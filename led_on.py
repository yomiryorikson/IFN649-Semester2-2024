import paho.mqtt.publish as publish 

publish.single("IFN649", "LED_ON", hostname= "52.64.166.204")
print("Done")
