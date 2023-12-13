from socket import socket,SOCK_STREAM,AF_INET
from time import sleep

def client():
    client=socket()
    client.connect(("192.168.211.195",35555))
    send_message=f"august nihao!".encode('utf-8')
    client.send(send_message)
    client.close()

for i in range(0,50):
    client()
    sleep(1)
