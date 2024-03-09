from datetime import datetime
import socket

sever_address = ('localhost', 6789)
max_size = 1000

print('Staring the server at', datetime.now())
print('Waiting for a client to call.')
sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever.bind(sever_address)
sever.listen(5)

client, addr = sever.accept()
data = client.recv(max_size)

print('At', datetime.now(), client, 'said', data)
client.sendall(b'Are you talking to me?')
client.close()
sever.close()
