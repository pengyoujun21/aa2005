"""
线程锁演示
"""
from threading import Thread,Lock

a = b = 0
lock = Lock()
def comp():
    while True:
        lock.acquire()
        if a != b:
            print(f"{a} != {b}")
        lock.release()

t = Thread(target=comp)
t.start()
while True:
    lock.acquire()
    a += 1
    b += 1
    lock.release()
t.join()
