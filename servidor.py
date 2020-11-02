#librerias
import socket
import select
import sys
import _thread

#creando socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

#direccion ip y puertos
ip = str('localhost')
port = int(8080)

server.bind((ip,port))

#cantidad de datos en cola
server.listen(100)

#lista de los clientes ingresando
list_clients = []

#esperando respuestas de clientes
def clientthread(conn,addr):
    conn.send(str("Dentro del Grupo Del Chat").encode("utf-8"))
    while True:
        try:
            message = conn.recv(2048).decode("utf-8")
            if (int(len(str(message))) >0):
                print("<" + addr[0] + ">: " + message)
                broadcast(message,conn)
            else:
                remove(conn)
        except:
            continue

#algoritmo para envio de mensaje (send) a todos los clientes conectados
def broadcast(message,connection):
    for clients in list_clients:
        if (clients != connection):
            try:
                clients.send(message.encode("utf-8"))
            except:
                clients.close()
                remove(clients)

def remove(connection):
    if connection in list_clients:
        list_clients.remove(connection)
#bucle para ir escuchado los clientes que van ingresando dentro del socket
while True:
    conn,addr = server.accept()
    list_clients.append(conn)
    print("Se a unido al chat: "+str(conn))
    _thread.start_new_thread(clientthread,(conn,addr))
#cerrmos conexiones
conn.close()
server.close()