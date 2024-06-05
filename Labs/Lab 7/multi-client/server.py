#Modify these code of two way communication using your Ubuntu Server's IP and port
#number accordingly to do multiple requests from multiple clients. Test and record the
#finding. This code is for server.

import socket
import threading

# Handle client connections
def handle_client(conn, addr):
    print(f'Connected by {addr}')
    while True:
        data = conn.recv(1024)
        if not data:
            print(f'Connection closed by {addr}')
            break
        print(f'Received from {addr}: {data.decode()}')
        response = input('Enter response to send: ')
        conn.sendall(response.encode())
    conn.close()

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('your_ip_address', 'port_number'))
server_socket.listen()
print('Server listening on your_ip_address:port_number')

# Accept connections
while True:
    conn, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()