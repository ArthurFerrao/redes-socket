from socket import *
import sender
from time import sleep

sock = socket(AF_INET, SOCK_DGRAM)

calc = raw_input('Digite o calculo: ')
sender.send_data(sock, calc.encode('utf-8'), ('localhost', 3001))
response, client = sock.recvfrom(1024)
print(response.decode('utf-8'))
sleep(2)
sock.sendto('ACK', ('localhost', 3001))

