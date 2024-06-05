#Try to execute this on your Pycharm or Visual Studio Code for more understanding.
#Havent test this code on Colab before.
#The code is simple as I didnt explore the other function associated with socket.
#For this code can also be run from Google Colab and it will show the IP address
#too.

import socket

host = socket.gethostname()
hostIP = socket.gethostbyname(host)

print(host)
print(hostIP)
#print(hostinfo)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, 65432))
server.listen(5)
print("Server is listening at port 80")