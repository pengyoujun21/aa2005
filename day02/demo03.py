"""
    拷贝文件夹功能：
        采用连接池方式，多线程执行

"""
import os
from multiprocessing import Pool,Queue
from time import time


class MyProcessQueue:

    def __init__(self):
        self.queue_obj =Queue()

    # 复制文件函数
    def copy_file(self,source_file, to_file):
        fr = open(source_file, "rb")
        fw = open(to_file, "wb")
        while True:
            data = fr.read(1024)
            if not data:
                break
            n = fw.write(data)
            self.queue_obj.put(n)
        fr.close()
        fw.close()


def get_totle_size(source_path):
    f_list = os.listdir(source_path)
    total_size = 0
    for f in f_list:
        total_size += os.path.getsize(source_path+f)

    return total_size


def get_totole_time(fun):
    def wapper(*args,**kwargs):
        start_time = time()
        fun(*args,**kwargs)
        end_time = time()
        return end_time - start_time
    return wapper
#复制目录函数
###@get_totole_time
def copy_fold(source_path,to_path):
    if not os.path.exists(to_path):
        os.mkdir(to_path)
    f_list = os.listdir(source_path)
    total_size = get_totle_size(source_path)
    print("total_size:",total_size)
    pool = Pool()
    for f in f_list:
        s_file = source_path+f
        t_file = to_path+"/"+f
        pool.apply_async(func=copy_file,args=(s_file,t_file))

    copy_size = 0
    global q
    while copy_size < total_size:
        copy_size += q.get(timeout=3)
        print("拷贝了%.2f%%"%(copy_size/total_size*100))
    pool.close()
    pool.join()

if __name__ == '__main__':
    res = copy_fold("../day01/","tmp")
    print(res)
