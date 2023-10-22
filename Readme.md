The Project compares the throughput and Overhead ratio of transferring files through MQTT, CoAP and HTTP protocols.

Libraries required: numpy, pandas, xlsxwriter, aiocoap

MQTT:
 - MQTT requires a broker, publisher and a subscriber. The publisher and subscriber sourcecodes are in the MQTT directory. 
 - The subscriber code can be run in a virtual machine or a computer and should be connected to a MQTT broker. In this case a mosquitto broker has been used with an IP address:  192.56.0.1. This should be modified in your case. It subscribes to the topic "File_topic" on which the publisbher publishes its files
 - The publisher is also connected to the MQTT broker and publishes the files to the topic "File_topic". 
 - The files can be accessed in DataFiles and the path to access should be changed based on users location.
 - The files can be run on command line, publisher publishes files using different qos(quality of service): 0,1 and 2. 
 - An excel file is generated displaying the total file transfer time.

 Command to execute:  1. Update the broker IP address in subscriber and publisher file; 2. Open Command prompt; 3. Run the command: python3 Subscribe.py on subscriber; 4. Run command: python3 Publish.py on publisher   

COAP:
 - COAP only requires a server and a client.
 - The path of the DataFiles should be updated in the server file and then it can be run using command line.
 - The client should conenct to the server using the servers ip address and place a GET request for the required file. 
 - The client then records the total time taken for file transfer to receive it since the request is placed.
 - The transfer time is exported to an excel sheet which can be useful to analyze in case of several transfers.

 Command to execute:  1. Update the server IP address in client file; 2. Open Command prompt; 3. Run the command: python3 CoAP_server.py on server; 4. Run command: python3 CoAP_client.py on the client pc.   

HTTP:
 - HTTP protocol also requires a server and a client.
 - The path of the DataFiles should be updated in the server file and then it can be run using command line.
 - The client should conenct to the server using the servers ip address and place a GET request for the required file. 
 - The client then records the total time taken for file transfer to receive it since the request is placed.
 - The transfer time is exported to an excel sheet which can be useful to analyze in case of several transfers.

 Command to execute:  1. Update the server IP address in client file; 2. Open Command prompt; 3. Run the command: python3 HTTP_Server.py on server; 4. Run command: python3 HTTP_Slient.py on the client pc.