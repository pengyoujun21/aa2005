"""
    tcp 客户端
"""
from socket import *

#创建tcp套接字
tcp_socket = socket()

tcp_socket.connect(("127.0.0.1",8888))

#发送消息
while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("From server:",data.decode())