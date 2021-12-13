"""

"""

from socket import *
from multiprocessing import Process

HOST = "0.0.0.0"
PORT = 8000
ADDR = (HOST,PORT)
user = {}


def do_login(sock,name,address):
    if name in user:
        sock.sendto(b"FAIT",address)
        return
    else:
        sock.sendto(b"OK",address)
        #通知其他人
        msg = "欢迎%s进入聊天室"%name
        for i in user:
            sock.sendto(msg.encode(),user[i])
        user[name] = address #存储用户


def do_chat(sock, name,content):
    msg = "%s : %s"%(name,content)
    for i in user:
        if i != name:
            sock.sendto(msg.encode(),user[i])


def do_exit(sock, name):
    del user[name] #移除此人
    msg = "%s 退出聊天室" % (name)
    for i in user:
        if i != name:
            sock.sendto(msg.encode(), user[i])

def handle(sock):
    while True:
        data,addr = sock.recvfrom(1024)
        tmp = data.decode().split(" ",2) #对请求进行解析
        if tmp[0] == "L":
            do_login(sock,tmp[1],addr)  #处理用户进入聊天具体事件
        elif tmp[0] == "C":
            do_chat(sock,tmp[1],tmp[2])
        elif tmp[0] == "E":
            do_exit(sock,tmp[1])

def main():
    sock = socket(AF_INET,SOCK_DGRAM)
    sock.bind(ADDR)

    p = Process(target=handle,args=(sock,))
    p.daemon = True
    p.start()
    while True:
        content = input("管理员消息：")
        #服务端整个退出
        if content == "quit":
            break
        msg = "C 管理员: "+content

        sock.sendto(msg.encode(),("127.0.0.1",8000))






if __name__ == '__main__':
    main()