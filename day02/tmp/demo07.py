import time
from multiprocessing import Process

#判断一个数是不是质数
def isPrime(n):
    if n <= 1:
        return  False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True



def get_totole_time(fun):
    def wapper(*args,**kwargs):
        start_time = time.time()
        fun(*args,**kwargs)
        end_time = time.time()
        return end_time - start_time
    return wapper

# @get_totole_time
# def comp_num():
#     primes = []
#     for i in range(1,100001):
#         if isPrime(i):
#             primes.append(i)
#     print(sum(primes))
#
#
# time_res = comp_num()
# print(time_res)

class MyProcess(Process):
    def __init__(self,begin,end):
        self.begin = begin
        self.end = end
        super().__init__()

    def run(self):
        primes = []
        for i in range(self.begin, self.end):
            if isPrime(i):
                primes.append(i)
        print(sum(primes))

@get_totole_time
def comp_4_process():
    pro_list = []
    for i in range(1,100001,10000):
        p = MyProcess(i,i+10000)
        pro_list.append(p)
        p.start()

    for po in pro_list:
        po.join()
if __name__ == '__main__':

    res = comp_4_process()
    print(res)