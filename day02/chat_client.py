import sys
from socket import  *
from multiprocessing import Process
ADDR = ("127.0.0.1",8000)


def login(sock):
    while True:
        name = input("Name:")
        msg = "L " + name
        sock.sendto(msg.encode(),ADDR)
        result,addr = sock.recvfrom(128)
        if result.decode() == 'OK':
            print("您已进入聊天室")
            return name
        else:
            print("你的名字太受欢迎了，换一个吧")

#接收消息
def recv_msg(sock):
    while True:
        data,addr = sock.recvfrom(2048)
        print("\n"+data.decode()+"\n我：",end=" ")

#发送消息
def send_msg(sock,name):
    while True:
        try:
            msg = input("我：")
        except KeyboardInterrupt:
            msg = "exit"   #客户端崩溃了
        if msg == "exit":
            data = "E " + name
            sock.sendto(data.encode(),ADDR)
            sys.exit("您已退出聊天室")

        data = "C %s %s"%(name,msg)
        sock.sendto(data.encode(),ADDR)

def main():
    sock = socket(AF_INET,SOCK_DGRAM)
    name = login(sock) #进入聊天室
    p = Process(target = recv_msg,args=(sock,))
    p.daemon = True  #父进程退出子进程退出
    p.start()
    send_msg(sock,name)



if __name__ == '__main__':
    main()