import paho.mqtt.client as mqtt
import time

client = mqtt.Client()

#Update the broker IP address
client.connect("192.168.56.1",1883)
client.subscribe("file_topic")
i=0

def on_message(client, userdata, message):
	global i, start_time
	if(i==0):
		start_time = time.time()
	#	print("receiving data")
	file_content = message.payload
	
	
	#Input number of time the client receives. Can be ignored. This can be useful in knowing broker to receiver transfer rate
	i=i+1
	if(i==(10000)):
		i=0
		transfer_time = time.time() - start_time
		print("Transfer time = ", transfer_time)	
		message_size = len(file_content)
		print("File size     = ", message_size)
		with open('/home/sandesh/mqtt_project/100KB.txt','wb') as file:
			file.write(file_content)
	
client.on_message = on_message

client.loop_forever()
