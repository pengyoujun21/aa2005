"""
    常用工具类
"""
class IterableHelper:
    """
        可迭代对象助手
    """
    #根据条件查找所有
    @staticmethod
    def find_all(iterable,func):
        """
        :param iterable: 可迭代容器
        :param func: 条件函数，筛选数据
        :return:  yield生成器类返回对象，节约内存
        """
        for item in iterable:
            if func(item):
                yield item


    #根据条件查找单个
    @staticmethod
    def find_single(iterable, func):
        """
        :param iterable: 可迭代容器
        :param func: 条件函数，筛选数据
        :return:  yield生成器类返回对象，节约内存
        """
        for item in iterable:
            if func(item):
                return item

    #获取指定属性
    @staticmethod
    def select(iterable, func):
        """
        :param iterable: 可迭代容器
        :param func: 筛选数据,比如查找对象中的所有指定信息，比如员工对象中的编号/名称
        :return:  yield生成器类返回对象，节约内存
        """
        for item in iterable:
            yield func(item)
    #按条件删除所有数据
    @staticmethod
    def del_all(iterable,func):
        count = 0
        for item in iterable:
            if func(item):
                del item
                count += 1
        return

    #按条件查询最大值
    @staticmethod
    def get_max(iterable,func):
        pre_emp = iterable[0]
        for item in iterable:
            if func(item) > func(pre_emp):
                pre_emp = item
        return pre_emp

    #按指定属性排序
    @staticmethod
    def ascending_sort(iterable,func):
        for x in range(len(iterable) - 1):
            for j in range(x + 1, len(iterable)):
                if func(iterable[x]) > func(iterable[j]):
                    iterable[x], iterable[j] = iterable[j], iterable[x]


    #打印调用函数的轨迹，并输出函数名称---装饰器应用
    @staticmethod
    def print_func_name(func):
        def wrapper(*args,**kwargs):
            #新功能：打印出入的函数名称
            print("-----",func.__name__,"-----")
            return func(*args,**kwargs)
        return wrapper