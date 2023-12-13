from http import server
from socket import socket,SOCK_STREAM,AF_INET
from datetime import datetime
import socketserver
from threading import Thread
import time

from numpy import add

class Server():
    def __init__(self):
        self.server=socket(family=AF_INET,type=SOCK_STREAM)
        self.server.bind(('192.168.211.195',35555))
        self.server.listen(512)
        print("begin.....")

    def server_connet(self):
        num=0
        while True:
            client,addr=self.server.accept()
            num+=1
            print(f"现在有{num}个client")
            Thread(target=self.client_session,args=(client,addr))
         

    def client_session(self,client: socket,addr):
        print(f"{addr}  连接到服务器")
        recv_message=client.recv(1024).decode('utf-8')
        print(f"client{client} time :{datetime.now()} 发来一条信息:{recv_message}")


def main():
    server=Server()
    server.server_connet()

if __name__=="__main__":
    main()
    
    
