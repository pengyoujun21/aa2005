"""
自定义进程类
"""

from multiprocessing import  Process


#自定义类
class MyProcess(Process):
    def __init__(self,val):
        self.val = val
        super().__init__()

    def fun1(self):
        print("执行步骤1",self.val)
    def fun2(self):
        print("执行步骤2",self.val)
    #重写run,将其作为一个新进程的执行内容
    def run(self):
        self.fun1()
        self.fun2()


if __name__ == '__main__':

    process = MyProcess(2)
    process.start()
    process.join()