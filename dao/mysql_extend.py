# coding:utf-8

import dao.mysql_base as mysql_base


class MysqlExtend(mysql_base.MysqlBase):
    def __init__(self, host=None, port=None, username=None, password=None, db=None, charset=None):
        mysql_base.MysqlBase.__init__(self, host=host, port=port, username=username, password=password, db=db, charset=charset)

    # 查询大于某一时间段的所有微信记录
    def find_by_time(self, begin_time):
        selectsql = "SELECT * FROM article_in_cc WHERE SUBSTR(publication_time,1,10) >= '%s'" % (begin_time)
        return self.selectSQL(selectsql)

    # 查询所有newslist中的数据
    def find_all_news(self, table):
        selectsql = "SELECT * FROM %s " % table
        return self.selectSQL(selectsql)
