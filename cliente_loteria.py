import socket

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip="192.168.56.1"
try:
    client_socket.connect((host_ip,0))
except:
    print("Ha habido un problema")
    client_socket.close()
    client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host_ip,0))
while True:
    mensaje_servidor=client_socket.recv(1024).decode()
    print(mensaje_servidor)
    client_socket.close()
