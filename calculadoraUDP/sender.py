from socket import *
__name__ = 'sender'

TIMEOUT = 2
BUFFER_SIZE = 1024
def send_data(udpsocket, data, destino):
    send(udpsocket, data, destino, 3)

def send(udpsocket, data, destino, attempts):
    if attempts <= 0:
        udpsocket.settimeout(None)
        print('Timeout')
        return

    try:
        udpsocket.sendto(data, destino)
        udpsocket.settimeout(TIMEOUT)
        data = ''
        while(data != 'ACK'):
            data, client = udpsocket.recvfrom(BUFFER_SIZE)
        print(data)
    except:
        print('No response, retrying...')
        send(udpsocket, data, destino, attempts - 1)
    
    udpsocket.settimeout(None)

def receive_and_send_ack(udpsocket):
    data, client = udpsocket.recvfrom(BUFFER_SIZE)
    if(data != 'ACK'):
        udpsocket.sendto('ACK', client)
    return data, client
