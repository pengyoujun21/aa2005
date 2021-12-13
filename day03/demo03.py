from threading import Thread,Event
from time import sleep
import sys

start_index = -1
tick_list = []
for i in range(1,501):
    t = f"t{i}"
    tick_list.append(t)
e = Event()

def get_tick(name,num):
    try:
        while tick_list:

            #global start_index
            #start_index += 1
            #tk = tick_list[start_index]

            print(f"name:{name}---num:--tk:{tick_list.pop(0)}")
            sleep(0.1)

    except Exception:
        print("卖完了！！！")







jobs = []
for i in range(1,11,1): 
    th = Thread(target=get_tick,args=("w%d"%i,50))
    jobs.append(th)
    th.start()

[j.join() for j in jobs]