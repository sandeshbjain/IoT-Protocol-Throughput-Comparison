import time
import requests
import numpy as np
import pandas as pd

server_ip = "192.0.2.5"
server_port = 8000

def transfer_file(file_size, num_transfers):
    server_url = f"http://{server_ip}:{server_port}/{file_size}"
    transfer_times = []
    total_transferred_data = 0
   
    for _ in range(num_transfers):
        start_time = time.time()
        response = requests.get(server_url)
        end_time = time.time()
        transfer_time = end_time - start_time
        transfer_times.append(transfer_time)
        transferred_data = len(response.content)
        total_transferred_data += transferred_data
        
    # Calculate average and standard deviation
    average_time = np.mean(transfer_times)
    std_deviation = np.std(transfer_times)
    header_len = len(str(response.headers).encode('utf-8'))
    header_len = len(str(response.headers))
    	
    print(f"Downloaded {num_transfers} times with an average time of {average_time:.6f} seconds standard deviation og {std_deviation:.6f} for {file_size}")
    #print("Total transfer time for", file_size, "=", sum(transfer_times), "total size =", total_transferred_data)
    print("Header Length = ", header_len)
   
    # Save the data to an Excel file
    data = pd.DataFrame({'Transfer Time': transfer_times})
    with pd.ExcelWriter(f'transfer_times_{file_size}.xlsx', engine='xlsxwriter') as writer:
        data.to_excel(writer, sheet_name='Transfer Times', index=False)
        summary = pd.DataFrame({'Average Transfer Time': [average_time], 'Standard Deviation': [std_deviation]})
        summary.to_excel(writer, sheet_name='Summary', index=False)

# Experiment 1: Transfer the 100 B file 10,000 times
transfer_file("100B", 10000)

# Experiment 2: Transfer the 10 kB file 1,000 times
transfer_file("10KB", 1000)

# Experiment 3: Transfer the 1 MB file 100 times
transfer_file("1MB", 100)

# Experiment 4: Transfer the 10 MB file 10 times

transfer_file("10MB", 10)
