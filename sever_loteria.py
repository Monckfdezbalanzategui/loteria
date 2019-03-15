import socket
from random import randrage

host_ip="192.168.56.1"
port=8900
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((host_ip,port))
except:
    print("Ha habido un problema")
    server_socket.close()
server_socket.listen(10)
numero_aleatorio=randrange(0,9)
print(numero_aleatorio)
print("Esperando conexion")
while True:
    conexion, addr_cliente=server_socket.accept()
    print("Se ha conectado el usuario: " addr_cliente)
    lista_numeros=[]
    numeros_ip=addr_cliente.split(".")
    numeros_ip=int(numero_ip)
    lista_numeros=lista_numeros.append(numeros_ip)
    suma= lista_numeros[0]+lista_numeros[1]+lista_numeros[2]+lista_nuemros[3]+lista_numeros[4]
    resto=suma%10
    if resto=numero_aleatorio:
        conexion.send("""¡Enhorabuena! Te ha tocado
        el número era, """ numero_aleatorio).encode()
    else:
        conxion.send("Lo sentimos, más suerte la próxima")
    print("El cliente se ha desconectado")
    continue
server_socket.close()
