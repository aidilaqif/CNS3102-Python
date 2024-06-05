#This is the Server code for the example of part 1 (communication between two
#processes in the same host). Take note over the IP Address of 127.0.0.1, also
#known as localhost. This means the two process are communicating from one to
#another in the same machine. Take note over the methods used for this server code

import socket

def start_server(host='your_ip_address', port='port number'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        try:
            server_socket.bind((host, port))
            server_socket.listen()
            print(f'Server listening on {host}:{port}')
            while True:
                conn, addr = server_socket.accept()
                with conn:
                    print(f'Connected by {addr}')
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            print("Connection closed by client")
                            break
                        print(f'Received from client: {data.decode()}')
                        conn.sendall(data)  # Echo back to client
        except Exception as e:
            print(f'Error: {e}')

if __name__ == "__main__":
    start_server()