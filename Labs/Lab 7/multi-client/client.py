#Modify these code of two way communication using your Ubuntu Server's IP and port
#number accordingly to do multiple requests from multiple clients. Test and record the
#finding. This code is for client.

import socket
import threading
# Receive messages from server
def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            print('Server closed the connection')
            break
        print(f'Received from server: {data.decode()}')

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('your_ip_adress', 'port_number'))  # Replace with the actual server IP
print('Connected to server at your_ip_address:port_number')

# Start thread to receive messages
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Send messages to server
while True:
    message = input('Enter message to send: ')
    if message.lower() == 'exit':
        break
    client_socket.sendall(message.encode())