import paho.mqtt.client as mqtt
import time
import numpy as np
import pandas as pd

client = mqtt.Client()

#Update server address below
client.connect("192.168.56.1", 1883)

#Update the file path below
file_path = "/home/sandesh/mqtt_project/10MB"

with open(file_path, "rb") as file:
    content = file.read()
    file_content = bytearray(content)
    # file_content = bytearray_content
    print("sending data")

transfer_times = []

#input the number time you want to transfer data. In this case it is 10
for i in range(10):
    start_time = time.time()
    client.publish("file_topic", file_content, qos=2)
    end_time = time.time()
    transfer_time = end_time - start_time
    transfer_times.append(transfer_time)

print("sent data")


average_transfer_time = np.mean(transfer_times)
std_deviation = np.std(transfer_times)

print("Average Transfer Time: ", average_transfer_time)
print("Standard Deviation: ", std_deviation)

# Create a DataFrame to store the transfer times
data = pd.DataFrame({'Transfer Time': transfer_times})

# Calculate the average and standard deviation
average_transfer_time = data['Transfer Time'].mean()
std_deviation = data['Transfer Time'].std()

# Write the data to an Excel file
with pd.ExcelWriter('transfer_times.xlsx', engine='xlsxwriter') as writer:
    data.to_excel(writer, sheet_name='Transfer Times', index=False)
   
    # Create a new sheet for average and standard deviation
    summary = pd.DataFrame({'Average Transfer Time': [average_transfer_time], 'Standard Deviation': [std_deviation]})
    summary.to_excel(writer, sheet_name='Summary', index=False)
    
client.loop_forever()
