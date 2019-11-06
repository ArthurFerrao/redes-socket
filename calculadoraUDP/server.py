from socket import *
import sender
from time import sleep

port = 3001 
# Create a UDP socket
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('localhost', port))

print('Server rodando')

while True :
    data, addr = sender.receive_and_send_ack(sock)
    op, x, y = data.decode('utf-8').split()

    x = int(x)
    y = int(y)

    if (op == 'ADD'):
        res = x + y
    elif (op == 'SUB'):
        res = x - y
    elif (op == 'MULT'):
        res = x * y
    elif (op == 'DIV'):
        if (y == 0):
            res = 'Invalido'
        else:
            res = x / y
    elif (op == 'EXP'):
        res = x ** y

    sender.send_data(sock, str(res).encode('utf-8'), addr)