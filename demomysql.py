"""
 连接mysql
"""
import pymysql

from common.dbmysql import Dbmysql

db = Dbmysql(user="root",password="",dbname="python01")

sql = "insert into  `user`(`name`,`datetime`)VALUES(%s,%s)"
list_inserts = [["李四","2021-12-06"],["王四","2021-12-06"],["李紫","2021-12-06"],["李尔","2021-12-06"],["李才","2021-12-06"]]
db.insert_more(sql,list_inserts)
#db = pymysql.connect(user="root",password="",host="localhost",database="python01",charset="utf8")

#cur = db.cursor()
#sql = "INSERT INTO `user`(`name`,`datetime`)VALUES('张三11','2021-12-05'); "

# try:
#
#     sql = "update  user set datetime=%s where name = %s"
#     cur.execute(sql, ["2012-03-01","张三11"])
#     sql = "delete from user1 where id = 1"
#     cur.execute(sql)
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()
#
#
# # data = cur.fetchall()
# for row in cur:
#
#     print(row)
# cur.close()
# db.close()