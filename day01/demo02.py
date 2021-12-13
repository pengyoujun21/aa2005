"""
    进程创建过程
        1。将需要新进程执行
"""

import multiprocessing
from time import sleep

#进程执行函数
def fun():
    print("开始执行进程函数.....")

    sleep(2)
    print("进程函数执行完了!!!")

if __name__ == '__main__':

    p = multiprocessing.Process(target=fun)

    #启动进程  进程诞生，执行fun函数内容
    p.start()

    print("原来的进程做点事")
    sleep(3)
    print("事情干完了")
    #等待执行完后回收
    p.join()