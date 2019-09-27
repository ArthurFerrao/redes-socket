from socket import *
import sys

port = 3000 
addr = ('', port) 
serv_socket = socket(AF_INET, SOCK_STREAM)
serv_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
serv_socket.bind(addr) 
serv_socket.listen(1)

print('Server rodando')

def getType(arq):
    tp = arq.split('.')[1]
    if tp == 'txt' :
        ct = 'text/plain'
    elif tp == 'png' :
        ct = 'image/png'
    elif tp == 'pdf' :
        ct = 'application/pdf'
    else :
        ct = ''

    return ct


while True :
    con, cliente = serv_socket.accept()
    req = con.recv(1024).decode('utf8')
    parts = req.split()
    try:
        flname = '.' + parts[1]
        fl = open(flname, 'rb')
        content = fl.read()
        fl.close()

        header = parts[2] + " 200 OK\r\n"
        header += "Content-Type: " + getType(parts[1]) + "; charset=utf-8\r\n"
    except:
        header = parts[2] + ' 404 Not Found\r\n'
        content = "<h1>Error 404 - File not found.</h1>".encode('utf8')
    
    res = header.encode('utf-8')
    res += '\r\n'.encode('utf-8')
    res += content
    res += '\r\n'.encode('utf-8')

    con.send(res)
    con.close()
