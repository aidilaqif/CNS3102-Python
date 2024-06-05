#YOUR LAB QUESTION PART #1
#Instruction:
#Find out the IP address of your Ubuntu Server.
#Make sure you have install Apache2 web server into your 'Server' Ubuntu.
#If you have installed an Apache web server, what is the port number used for it?
#With the info above, modify the code below and eexcute the server code first

import socket

def start_server(host='your_ip_address', port='port_number'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f'Server listening on {host}:{port}')
        conn, addr = server_socket.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f'Received from client: {data.decode()}')
                conn.sendall(data)  # Echo back to client

if __name__ == "__main__":
    start_server()