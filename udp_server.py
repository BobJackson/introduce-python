from datetime import datetime
import socket

sever_address = ('localhost', 6789)
max_size = 4096

print('Starting the server at', datetime.now())
print('Waiting for client to call.')
sever = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sever.bind(sever_address)

data, client = sever.recvfrom(max_size)

print('At', datetime.now(), client, 'said', data)
sever.sendto(b'Are you talking to me?', client)
sever.close()
