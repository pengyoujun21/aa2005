import  threading
from time import sleep
import os


a = 1

def musiz():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放音乐")
    global a
    print("a=",a)
    a=10000




th = threading.Thread(target=musiz)
th.start()

for i in range(4):
    sleep(1)
    print(os.getpid(),"播放：葫芦娃")

th.join()

print("a=",a)