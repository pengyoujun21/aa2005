"""
    tcp server 服务器端
"""

from socket import *
from multiprocessing import Process
from signal import *


HOST="0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)


def handle(confd):
    while True:
        try:
            data = confd.recv(1024)
            print(data)
            if not data:
                break
            print("Recv:", data.decode())
            confd.send(b"Thanks")
        except ConnectionResetError:
            print("异常关闭")
            confd.close()

    confd.close()


def main():
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    print("Listen the port %s"%PORT)
   # signal(SIGCHLD,SIG_IGN)
    while True:
        try:
            connf,addr = sock.accept()
        except KeyboardInterrupt:
            sock.close()
            return
        p = Process(target=handle,args=(connf,))
        p.daemon = True
        p.start()



if __name__ == '__main__':
    main()