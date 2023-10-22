import logging
import asyncio
import time
from aiocoap import *
import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO)

async def request_file_transfer(protocol, server_ip, file_required, num_requests):
    transfer_times = []
    total_bytes_transferred = 0

    for i in range(num_requests):
        start_time = time.time()
        request = Message(code=GET, uri=server_ip + file_required)

        try:
            response = await protocol.request(request).response
        except Exception as e:
            print(f'Failed to fetch resource for {file_required}:')
            print(e)
            continue

        transfer_time = time.time() - start_time
        transfer_times.append(transfer_time)
        total_bytes_transferred += len(response.payload)
        header_size = len(str(response.opt).encode('utf-8'))

    return transfer_times, total_bytes_transferred,header_size

async def main():
    protocol = await Context.create_client_context()

    server_ip = "coap://192.0.2.5"

    requests = [
        ("100B", 10000),
        ("10KB", 1000),
        ("1MB", 40),
        ("10MB", 10)
        
    ]

    for file_size, num_requests in requests:
        file_required = "/" + file_size
        transfer_times, total_bytes, header_size = await request_file_transfer(protocol, server_ip, file_required, num_requests)

        average_time = np.mean(transfer_times)
        std_deviation = np.std(transfer_times)

        print(f"File Size: {file_size}, Num Requests: {num_requests}")
        print(f"Total Transfer Time: {sum(transfer_times)} seconds")
        print(f"Average Transfer Time per Request: {average_time:.6f} seconds")
        print(f"Total Bytes Transferred: {total_bytes} bytes")
        print(f"Standard deviation: {std_deviation:.6f}")
        print("Header Size", header_size)
        

        # Save the data to an Excel file
        data = pd.DataFrame({'Transfer Time': transfer_times})
        with pd.ExcelWriter(f'transfer_times_{file_size}.xlsx', engine='xlsxwriter') as writer:
            data.to_excel(writer, sheet_name='Transfer Times', index=False)
            summary = pd.DataFrame({'Average Transfer Time': [average_time], 'Standard Deviation': [std_deviation]})
            summary.to_excel(writer, sheet_name='Summary', index=False)

if __name__ == "__main__":
    asyncio.run(main())
