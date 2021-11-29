# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     operate_mysql
   Description :
   Author :       xiaoyu
   date：          2021/11/29
-------------------------------------------------
"""
import pymysql
from operate_config import GetConfig


class OperateMysql:
    def __init__(self):
        """
        初始化函数，创建数据库连接及游标
        """
        self.db = pymysql.connect(host=GetConfig().get_config("mysql", "host"),
                                  user=GetConfig().get_config("mysql", "user"),
                                  password=GetConfig().get_config("mysql", "password"),
                                  port=GetConfig().get_config_int("mysql", "port"),
                                  database=GetConfig().get_config("mysql", "database"), charset="utf8")
        # 创建游标
        self.cs = self.db.cursor()

    def search(self, sql):
        """
        查询数据库数据
        :param sql: sql语句
        :return: 返回查询结果
        """
        self.cs.execute(sql)
        self.close()
        return self.cs.fetchone()

    def execution(self, sql):
        """
        对数据库进行增删改操作
        :param sql:
        :return:
        """
        self.cs.execute(sql)
        self.db.commit()
        self.close()

    def close(self):
        self.cs.close()
        self.db.close()


# sql = "select * from bankcards where id=1"
# res = OperateMysql().search(sql)
# print(res)
