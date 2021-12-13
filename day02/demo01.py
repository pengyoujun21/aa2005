
"""
    进程池 Pool
"""
from multiprocessing import Pool,Queue
from time import sleep,ctime,time

q = Queue()

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def get_totole_time(fun):
    def wapper(*args,**kwargs):
        start_time = time()
        fun(*args,**kwargs)
        end_time = time()
        return end_time - start_time
    return wapper


def jisuan(msg,begin,end):
    print(msg)
    primes = []
    for i in range(begin, end):
        if isPrime(i):
            primes.append(i)
    sum_res = sum(primes)
    q.put(sum_res)


def work(msg,sec):

    print(msg)
    sleep(sec)

#@get_totole_time
def exec_pool():
    pool = Pool()  # 不传参数，默认为电脑cpu核数
    num = 0
    for i in range(1, 100001, 10000):
        num += 1
        msg = f"pool-demo-----{i}"
        pool.apply_async(func=jisuan, args=(msg, i, i + 10000))

    ct = 0
    sum_res = 0
    print("num=",num)
    while ct < num:
        ct +=1
        sum_res +=q.get()
        print(f"--总和为：{sum_res}")
    print(f"总和为：{sum_res}")


    pool.close()  # 关闭进程池，不能添加新的事件
    pool.join()  # 等事件都执行完，回收进程池
if __name__ == '__main__':
    res = exec_pool()
    print(res)


