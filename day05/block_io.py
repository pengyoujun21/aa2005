"""
    非阻塞IO
"""
import time
from socket import *


tcp_socke = socket()
tcp_socke.bind(("0.0.0.0",8888))
tcp_socke.listen(5)
fw = open("mylog.txt","a")

tcp_socke.setblocking(False)



while True:
    print("等待客户端连接...")
    try:
        confd,addr = tcp_socke.accept()
        print(f"客户端：{addr}已连接!!!")
    except BlockingIOError as e:
        msg = "%s:\n"%time.ctime()
        fw.write(msg)
        fw.flush()
        time.sleep(2)

