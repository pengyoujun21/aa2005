"""
    循环创建多个进程
"""

from multiprocessing import Process
import os,sys
from signal import *


def fun01():
    print("吃饭....")
    print(f"父ID:{os.getppid()}----当前子id:{os.getpid()}")

def fun02():
    sys.exit("不睡觉了")
    print(f"父ID:{os.getppid()}----当前子id:{os.getpid()}")

def fun03():
    print("打游戏....")
    print(f"父ID:{os.getppid()}----当前子id:{os.getpid()}")

if __name__ == '__main__':
    signal(SIGCHLD,SIG_IGN)
    funs = [fun01,fun02,fun03]
    jobs = []
    for f in funs:
        p = Process(target=f)
        p.start()
        jobs.append(p)

    for i in jobs:
        i.join()