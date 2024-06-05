#YOUR LAB QUESTION PART #2
#Instruction:
#Find out the IP address of your Ubuntu Client.
#If you have installed an Apache web server in the Server, what is the port number
#used for it? With the info above, modify the code below and eexcute the server
#code first
#Run this code after modification and record the video later from initial step of
#finding the IP address etc.sss

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