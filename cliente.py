#librerias
from socket import AF_INET,socket, SOCK_STREAM
from threading import Thread
from tkinter import *

#creacion de objeto GUI
top = Tk()
top.title("chat de sergio")

#metodo de escuchar
def receive():
    while True:
        try:
            mensaje = client_socket.recv(1024).decode("utf-8")
            mensaje_list.insert(END,str(mensaje))
        except OSError:
            break
#metodo de enviar
def send(event=None):
    mensaje = mi_ms.get()
    mi_ms.set("")
    client_socket.send(str(mensaje).encode("utf-8"))
    mensaje_list.insert(END,str(mensaje))

#uso de objetos layout de tkinter
messages_frame = Frame(top)
mi_ms = StringVar()
mi_ms.set("")
scrollbar = Scrollbar(messages_frame)

mensaje_list = Listbox(messages_frame,height=25, width=50,yscrollcommand = scrollbar.set )
scrollbar.pack(side=RIGHT,fill=Y)
mensaje_list.pack(side=RIGHT,fill=BOTH)
mensaje_list.pack()
messages_frame.pack()

entry_field=Entry(top,textvariable=mi_ms)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = Button(top,text="Enviar",command=send)
send_button.pack()


ip_server = 'localhost'
port = 8080
ADDR = (ip_server,port)

client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

mainloop()