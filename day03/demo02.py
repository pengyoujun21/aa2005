from threading import Thread
from time import sleep

def fun(sec,name):
    print("含有参数的线程")
    sleep(sec)
    print("%s 线程执行完毕"%name)

#创建多个线程

jobs = []
for i in range(5):
    t = Thread(target=fun,args=(2,),kwargs={"name":"T%d"%i})
    jobs.append(t)
    t.start()

[j.join() for j in jobs]