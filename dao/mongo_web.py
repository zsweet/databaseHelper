# coding:utf-8

import datetime
import mongo_base


class MongoWeb(mongo_base.MongoBase):
    def __init__(self, collection=None, database=None):
        mongo_base.MongoBase.__init__(self, collection=collection, database=database)

    # 按照bookname查找
    def find_news(self,bookname,skip_num,limit_num):
        qres = self.collection.find({'bookname':bookname}).skip(skip_num).limit(limit_num)
        return qres

    # 查询mongo通过日期查询每日统计信息
    def find_by_date(self, time):
        qres = self.collection.find({'time': time})
        return qres

    # 查询mongo通过日期查询每日统计信息
    def find_one_by_date(self, time):
        qres = self.collection.find_one({'time': time})
        return qres


    # 查询mongo通过日期查询每日统计信息
    def find_by_date_span(self, below, top):
        qres = self.collection.find({'time': {'$lte':top,'$gte':below}}).sort([("time",-1)])
        return qres

    # 查询mongo通过日期查询每日统计信息
    def find_by_date_span_reverse(self, below, top):
        qres = self.collection.find({'time': {'$lte':top,'$gte':below}}).sort([("time",1)])
        return qres

    #获取没有分析过的input实例
    def find_latest_input(self):
        qres = self.collection.find({'analysis_finish_mark':0},{'input_id':1})
        return qres

    # 更新记录(通过input_id)
    def update_by_input_id(self, input_id, value):
        self.collection.update_one({'input_id': input_id}, {'$set': value}, upsert=True)


    # 查询记录
    def find(self, query):
        qres = self.collection.find(query).sort([('time',-1)])
        return qres

    # 查询记录
    def find_skip_limit(self, query,skip_num,limit_num):
        qres = self.collection.find(query).skip(skip_num).limit(limit_num)
        return qres

    # 更新记录(通过input_id)
    def find_one(self,query):
        return self.collection.find_one(query)


    def update_leader(self,condition,query):
        return self.collection.update(condition,query,False,False)


if __name__ == '__main__':
    mongo = MongoWeb()
    mongo.find_update_enote()
