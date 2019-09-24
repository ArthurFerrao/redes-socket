from socket import *
import sys

port = 3000 
addr = ('', port) 
serv_socket = socket(AF_INET, SOCK_STREAM)
serv_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
serv_socket.bind(addr) 
serv_socket.listen(1)

print('Server rodando')

while True :
    con, cliente = serv_socket.accept()
    req = con.recv(1024).decode('utf8')
    parts = req.split()
    try:
        flname = './arquivos' + parts[1]
        fl = open(flname, 'rb')
        arq = fl.read()
        con.send(arq)
        fl.close()
    except:
        err = "Arquivo nao encontrado"
        con.send(err.encode('utf8'))
    con.close()
