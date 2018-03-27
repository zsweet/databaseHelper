# coding:utf-8

import os
import sys
from imp import reload

reload(sys)
sys.setdefaultencoding('utf8')
import pymysql
import configparser
import g_val


class MysqlBase(object):
    # 数据库配置方式(读取配置文件或程序设置参数，  优先程序配置)
    def __init__(self, host=None, port=None, username=None, password=None, db=None, charset=None):
        self.Option = {"host": "", "password": "", "username": "", "db": "", "port": "", "charset": ""}
        self.__mysql_config()
        if host: self.Option['host'] = host
        if port: self.Option['port'] = port
        if username: self.Option['username'] = username
        if password: self.Option['password'] = password
        if db: self.Option['db'] = db
        if charset: self.Option['charset'] = charset
        self.connectDB()

    # mongodb配置用config对象读取配置文件
    def __mysql_config(self):
        config = configparser.ConfigParser()
        config.read(g_val.db_path)
        self.Option['host'] = config.get("db", "MYSQL_HOST")
        self.Option['port'] = int(config.get("db", "MYSQL_PORT"))
        self.Option['username'] = config.get("db", "MYSQL_USERNAME")
        self.Option['password'] = config.get("db", "MYSQL_PASSWORD")
        self.Option['db'] = config.get("db", "MYSQL_DB")
        self.Option['charset'] = config.get("db", "MYSQL_CHARSET")

    # 连接数据库
    def connectDB(self):
        print('connecting mysql database on ' + str(self.Option['host']) + ':' + str(self.Option['port']))
        self.conn = pymysql.connect(
            host=self.Option['host'],
            port=self.Option['port'],
            user=self.Option['username'],
            passwd=self.Option['password'],
            db=self.Option['db'],
            charset=self.Option['charset'],
        )

    # 关闭数据库
    def closeDB(self):  # 关闭数据库
        print('closing mysql database')
        self.conn.close()
        print('mysql database closed')

    # 查询
    def selectSQL(self, sql):  # 在数据库中执行查询语句，返回查询的结果总数和结果信息
        print('selecting sql: ' + sql)
        cur = self.conn.cursor()
        total = cur.execute(sql)
        infos = cur.fetchmany(total)
        cur.close()
        print('select sql finished: ' + sql)
        return infos

    # 插入
    def insertSQL(self, sql, values):  # 在数据库中执行插入语句
        print('inserting sql: ' + sql)
        cur = self.conn.cursor()
        cur.executemany(sql, values)
        cur.close()
        self.conn.commit()
        print('insert sql finished: ' + sql)

    # 更新
    def updateSQL(self, sql):  # 在数据库中执行更新语句
        print('updating sql: ' + sql)
        cur = self.conn.cursor()
        cur.execute(sql)
        cur.close()
        self.conn.commit()
        print('update sql finished: ' + sql)

    # 删除
    def deleteSQL(self, sql):  # 在数据库中执行删除语句
        print('deleting sql: ' + sql)
        cur = self.conn.cursor()
        cur.execute(sql)
        cur.close()
        print('delete sql finished: ' + sql)


if __name__ == "__main__":
    mysqldb = MysqlBase(db='wedata')
    mysqldb.connectDB()
    infos = mysqldb.selectSQL('SELECT * FROM article where id<50')
    for i in infos:
        print(i)
    mysqldb.closeDB()
