from multiprocessing import Process
from time import sleep


def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

if __name__ == '__main__':

    p = Process(target=worker,args=(2,"levi"))
    p.start()
    p.join()