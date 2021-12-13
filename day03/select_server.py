"""


"""

from socket import *

import select

HOST="0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

tcp_socket = socket()
tcp_socket.bind(ADDR)
tcp_socket.listen(5)
tcp_socket.setblocking(False)

rlist = [tcp_socket]
wlist = []
xlist = []

while True:
    rl,wl,xl = select.select(rlist,wlist,xlist)
    for r in rl:

        if r is tcp_socket:

            confd,addr = r.accept()
            confd.setblocking(False)
            rlist.append(confd)
            print("连接地址：", addr)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print("Recv:", data.decode())
            wlist.append(r)

    #写列表操作
    for w in wl:
        w.send(b"OK")
        wlist.remove(w)