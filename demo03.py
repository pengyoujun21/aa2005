"""
    练习： 使用装饰器，为旧功能添加新功能。
            验证权限
"""

def validation_permissions(func):
    def wrapper(*args,**kwargs):
        print("验证权限中....")
        return func(*args,**kwargs)
    return wrapper
@validation_permissions
def insert():
    print("插入成功")
@validation_permissions
def delete():
    print("删除成功")



insert()

delete()
