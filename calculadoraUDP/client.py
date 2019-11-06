from socket import *

sock = socket(AF_INET, SOCK_DGRAM)

calc = input('Digite o calculo:')

sock.sendto(calc.encode('utf-8'), ('localhost', 3001))


response = sock.recvfrom(1024)[0].decode('utf-8')

print(response)