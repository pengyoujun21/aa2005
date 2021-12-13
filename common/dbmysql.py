"""
    Mysql 工具类
"""
import pymysql

class Dbmysql:
    
    def __init__(self, user="", password="",dbname="", host="localhost", charset="utf8"):
        self.__user = user
        self.__password = password
        self.__host = host
        self.__dbname = dbname
        self.__charset = charset
        try:
            self.__db = pymysql.connect(user=self.__user,password=self.__password,database=self.__dbname,host=self.__host,charset=self.__charset)
            self.__cur = self.__db.cursor()
        except Exception as e:
            print(e)
            print("database connect error !!!")

    def close(self):
        self.__db.close()
        self.__cur.close()

    def insert_more(self,sql,list):
        """
        :param insert(field1,field2)values(%s,%s):
        :param list: [[value1,value2],[value1,value2]...]
        :return:
        """
        try:
            self.__cur.executemany(sql,list)
            self.__db.commit()
        except Exception as e:
            print(e)
            self.__db.rollback()
        finally:
            self.__db.close()
