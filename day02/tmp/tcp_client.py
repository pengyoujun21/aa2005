"""
    思路：
    1.创建套接字
    2.连接服务器
    3.读取图片内容
    4.发送图片内容
    5.发送完毕关闭
"""

from socket import *

sock = socket()
sock.connect(("127.0.0.1",8888))
f = open("test.png","rb")
while True:
    data = f.read(1024)
    if not data:
        break
    sock.send(data)

f.close()
sock.close()