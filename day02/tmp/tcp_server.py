import time
from socket import *

#建立tcp连接
sock = socket()
sock.bind(("0.0.0.0",8888))
sock.listen(5)
print("等待连接中...")
#等待客户端连接
connfd,addr = sock.accept()
print("Connect from ",addr)


filename = "%d-%d-%d.jpg"%(time.localtime()[:3])
f = open(filename,"wb")
while True:
    data = connfd.recv(1024)
    if not data:
        break
    f.write(data)
f.close()

connfd.close()
sock.close()