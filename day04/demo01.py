"""
    一个线程打印1--52  另外一个线程打印A-Z
    两个线程一起启动，要求打印结果  12A 34B .... 5152Z
"""
import string
from threading import Thread,Event,Lock

res = string.ascii_uppercase
num_res = [num for num in range(1,53,1)]

l1 = Lock()
l2 = Lock()


def pt_a_z():
    for asc in res:
        l2.acquire()
        print(asc,end="")
        l1.release()

def pt_num():
    while num_res:
        l1.acquire()
        print(num_res.pop(0), end="")
        print(num_res.pop(0))
        l2.release()

t1 = Thread(target=pt_a_z)
t2 = Thread(target=pt_num)

l1.acquire()

t1.start()
t2.start()

t1.join()
t2.join()