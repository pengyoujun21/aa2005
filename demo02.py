"""
    查找编号为1005的员工
"""
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

for it in IterableHelper.select(list_employee,lambda t:t.name):
    print(it)