from common.Iterable import IterableHelper


class EmployeeModel:
    def __init__(self,eid=0,did=0,name="",money=0.0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

list_employee = [
    EmployeeModel(1001,9003,"林玉玲1",13000),
    EmployeeModel(1002,9003,"林玉玲2",15000),
    EmployeeModel(1003,9003,"林玉玲3",12000),
    EmployeeModel(1004,9005,"林玉玲4",17000),
    EmployeeModel(1005,9005,"林玉玲5",19000),
    EmployeeModel(1006,9005,"林玉玲6",18000),
    EmployeeModel(1007,9007,"林玉玲7",16000),
]



def conf_money_gt_15k(item):
    return item.money > 15000

def conf_find_eid(item):
    return item.eid == 1005

def conf_did_eq_9005(item):
    return item.did == 9005

# for item in IterableHelper.find(list_employee,lambda item:item.money > 15000):
#     print(item.__dict__)
# print("------------")
# for item in IterableHelper.find(list_employee,lambda item:item.eid == 1005):
#     print(item.__dict__)
# print("------------")
# for item in IterableHelper.find(list_employee,lambda item:item.did == 9005):
#     print(item.__dict__)

# for item in IterableHelper.del_all(list_employee,lambda item:item.money > 15000):
#     print(item.__dict__)

pre_emp = ""
for item in list_employee:
    if pre_emp == "":
        pre_emp = item
    else:
        if item.money > pre_emp.money:
            pre_emp = item
#print(pre_emp.__dict__)

def fun01(item):
    return item.eid

# def get_max_eid(fun01):
#     pre_emp = list_employee[0]
#     for item in list_employee:
#         if fun01(item) > fun01(pre_emp):
#             pre_emp = item
#     return pre_emp


# r = get_max_eid(lambda item:item.eid)
# print(r.__dict__)
# r = get_max_eid(lambda item:item.money)
# print(r.__dict__)

# res = IterableHelper.get_max(list_employee,lambda item:item.eid)
# print(res.__dict__)
#
# res = IterableHelper.get_max(list_employee,lambda item:item.money)
# print(res.__dict__)

# for item in IterableHelper.del_all(list_employee,lambda item:item.did == 9003):
#     print(item.__dict__)


def fun02(item):
    return item.money

# res = sorted(list_employee,key=lambda emp:emp.eid,reverse=True)
# for r in res:
#     print(r.__dict__)

# res = filter(lambda emp:emp.money > 15000,list_employee)
# for r in res:
#     print(r.__dict__)

# list01 = [(1,1,1),(2,2),(3,3,3),(4,4,4)]
# res = max(list01,key=lambda item:len(item))
# print(res)

res = map(lambda emp:(emp.eid,emp.name),list_employee)
for r in res:
    print(r)


#
# IterableHelper.ascending_sort(list_employee,lambda it:it.money)
# for item in list_employee:
#     print(item.__dict__)
# print("------------")
# for emp in IterableHelper.ascending_sort(list_employee,lambda it:it.eid):
#     print(emp.__dict__)
# print("------------")

def fun02():
    print("fun02执行了!!!")

@IterableHelper.print_func_name
def fun01():
    print("fun01执行了!!!")
    fun02()

fun01()
