#This is the Client code for the example of part 1 (communication between two
#processes in the same host). Take note over the IP Address of 127.0.0.1, also
#known as localhost. This means the two process are communicating from one to
#another in the same machine. Take note over the methods used for this server code
#However this code cannot be used to be executed and communicate with the Server code
#above because its in Google Colab. Both needs to be run in your local Ubuntu host.

import socket

def start_client(host='your_ip_address', port='port number'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f'Connected to server at {host}:{port}')
        while True:
            message = input("Enter message to send: ")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f'Received from server: {data.decode()}')

if __name__ == "__main__":
    start_client()